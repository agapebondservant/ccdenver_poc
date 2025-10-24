# STIG Benchmark: Symantec ProxySG NDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-94413`

### Rule: Symantec ProxySG must enable Attack Detection.

**Rule ID:** `SV-104305r2_rule`
**Severity:** high

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Symantec ProxySG Attack Detection prevents or limits the effects of denial of service (DoS) and distributed-DoS (DDoS) attacks by limiting the number of simultaneous TCP connections and/or excessive repeated requests from each client IP address that can be established within a specified time frame. Configure attack detection for both clients and servers or server groups. The client attack-detection configuration is used to control the behavior of attacking sources. The server attack-detection configuration is used when an administrator wants to prevent a server from becoming overloaded by limiting the number of outstanding requests that are allowed. The default settings should work in most environments, but can be fine tuned to prevent impact on the site's traffic flow. Organizations should also take into consideration the capabilities and configuration of adjacent network devices (e.g., firewalls performing packet filtering to block DoS attacks). The default settings should work in most environments, but can be fine-tuned to prevent impact on the site's traffic flow. Organizations should also take into consideration the capabilities and configuration of adjacent network devices (e.g., firewalls performing packet filtering to block DoS attacks). Default settings for client DDoS settings on the ProxySG are as follows. To view Default settings for client DDoS settings on the ProxySG, type the following command at the command line interface. ProxySG#(config attack-detection)show attack-detection client Client limits enabled: false Client interval: 20 minutes Default client limits: Client concurrent request limit: unlimited Client connection limit: 100 Client failure limit: 50 Client request limit: unlimited Client warning limit: 10 Blocked client action: Drop Client connection unblock time: unlimited Monitor only mode: disabled</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Attack Detection is enabled. 1. SSH into the ProxySG console, type "enable". 2. Enter the correct password, type "configure terminal". 3. Press "Enter", type "show attack-detection configuration". 4. Confirm that "client limits enabled" equals "true". If Attack Detection is not enabled, this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-94653`

### Rule: Symantec ProxySG must be configured with only one local account that is used as the account of last resort.

**Rule ID:** `SV-104483r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privileged level) access to the device is required at all times. An account can be created on the device's local database for use when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is referred to as the account of last resort since it is intended to be used as a last resort and when immediate administrative access is absolutely necessary. The account of last resort logon credentials must be stored in a sealed envelope and kept in a safe. The safe must be periodically audited to verify the envelope remains sealed. The signature of the auditor and the date of the audit should be added to the envelope as a record. Administrators should secure the credentials and disable the root account (if possible) when not needed for system administration functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify local accounts besides the account of last resort do not exist. Show security local-user-list View "Users:" list If any users show in the "Users" configuration list other than the default admin user, this is a finding.

## Group: SRG-APP-000033-NDM-000212

**Group ID:** `V-94655`

### Rule: Symantec ProxySG must be configured to enforce user authorization to implement least privilege.

**Rule ID:** `SV-104485r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Network devices use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the network device to control access between administrators (or processes acting on behalf of administrators) and objects (e.g., device commands, files, records, processes) in the network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain a list of authorized personnel or host IP addresses and associated roles/privileges. Verify there are no unauthorized users/host IP addresses. Verify there are no users or host IP addresses with excess privileges. 1. Log on to the Web Management Console. 2. Click Configuration >> Policy >> Visual Policy Manager. 3. Click the "Launch" button. 4. Click the "Admin Access" layer. Verify that any users, hosts, and groups listed in the "source" field of each rule that have an action of "Allow" are authorized administrators with read-write, read-only, or deny. If users or hosts are configured for excess privileges, this is a finding.

## Group: SRG-APP-000033-NDM-000212

**Group ID:** `V-94657`

### Rule: Symantec ProxySG must configure Web Management Console access restrictions to authorized IP address/ranges.

**Rule ID:** `SV-104487r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>It is important that administrative access (SSH, web) to an appliance using the account of last resort be able to be restricted to only the appropriate networks/subnets in order to reduce the likelihood of unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify console access using the account of last resort has been restricted to specific networks/subnets. 1. Log on to the Web Management Console. 2. Click >> Configuration >> Authentication >> Console Access. 3. Confirm that the correct networks/subnets are specified in the list. If there are no entries in the list, this is a finding.

## Group: SRG-APP-000038-NDM-000213

**Group ID:** `V-94659`

### Rule: Symantec ProxySG must be configured to enforce assigned privilege levels for approved administrators when accessing the management console, SSH, and the command line interface (CLI).

**Rule ID:** `SV-104489r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A mechanism to detect and prevent unauthorized communication flow must be configured or provided as part of the system design. If management information flow is not enforced based on approved authorizations, the network device may become compromised. Information flow control regulates where management information is allowed to travel within a network device. The flow of all management information must be monitored and controlled so it does not introduce any unacceptable risk to the network device or data. Application-specific examples of enforcement occur in systems that employ rule sets or establish configuration settings that restrict information system services or message-filtering capability based on message content (e.g., implementing key word searches or using document characteristics). Applications providing information flow control must be able to enforce approved authorizations for controlling the flow of management information within the system in accordance with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Obtain a list of authorized personnel and IP addresses that should have access to the Web Management Console or CLI. 2. Click Configuration >> Policy >> Visual Policy Manager. 3. Click the "Launch button". 4. Click the "Admin Access" layer. 5. Verify any users and/or groups listed in the "source" field of each rule have the appropriate Action of either "Allow Read/Write access" or "Allow Read-only Access" per the user/group’s assigned privileges. 6. Verify that the users and/or groups have the Service set to "SSH-Console", "HTTPS-Console", or both, depending on the user/group’s assigned privileges. 7. Ensure the account of last resort is not allowed access via the "SSH-Console" or the "HTTPS-Console", but only via the local console port and CLI. If the Symantec ProxySG is not configured to enforce assigned privilege levels for approved administrators when accessing the Management Console and the CLI, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-94661`

### Rule: Symantec ProxySG must be configured to enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period.

**Rule ID:** `SV-104491r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the lockout policy is configured. 1. SSH into the ProxySG console, type "enable", press "Enter". 2. Enter the appropriate password, type "config", press "Enter". 3. Type "show security local-user-list", press "Enter". This should return a value of "3" for the "Max failed attempts" and "900" for the value of both the "lockout duration" and "reset interval" fields. If Symantec ProxySG is not configured to enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-94663`

### Rule: Symantec ProxySG must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-104493r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Display of the DoD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users. Configuration of the notice banner on for logon to the management console requires the configuration of a reverse proxy service and a policy associated with this service. Refer to the detailed documentation for information on configuration. https://origin-symwisedownload.symantec.com//resources/webguides/proxysg/certification/notice_consent_webguide/Notice_Consent_Banner.htm#Topics/create_banner.htm and click on "Create a Banner for the Management Console" or search for "Symantec Notice and Consent Banner Configuration Webguide" in Google and click on "Create the Notice and Consent Banner". The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Standard DoD Banner is displayed: 1. Log on to the Web Management Console of the Symantec ProxySG and confirm that a banner is displayed that complies with the DoD requirement. 2. SSH into the command line interface of the Symantec ProxySG and confirm that a banner is displayed that complies with the DoD requirement. 3. Connect a computer to the serial port of the appliance and confirm that the DoD banner is displayed. If Symantec ProxySG does not display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device, this is a finding.

## Group: SRG-APP-000089-NDM-000221

**Group ID:** `V-94665`

### Rule: Symantec ProxySG must enable event access logging.

**Rule ID:** `SV-104495r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., process, module). Certain specific device functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the device will provide an audit record generation capability as the following: (i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); (ii) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and (iii) All account creation, modification, disabling, and termination actions. ProxySG generates the required logs both automatically and with additional configuration. See the check section for more details. Logs are written locally up to the allowed log size and overwrite the oldest log entries first when the log size limit is reached. The retention of logs written to remote syslog systems are governed by those remote systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify event access logging is enabled. 1. Log on to the Web Management Console. 2. Click Maintenance >> Event Logging and ensure that the log level is set to at least "Configuration Events". If event access logging is not enabled, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-94667`

### Rule: Symantec ProxySG must be configured to support centralized management and configuration of the audit log.

**Rule ID:** `SV-104497r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to centrally manage the content captured in the audit records, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an ongoing attack. The DoD requires centralized management of all network component audit record content. Network components requiring centralized audit log management must have the capability to support centralized management. The content captured in audit records must be managed from a central location (necessitating automation). Centralized management of audit records and logs provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. Ensure at least one Syslog server and local files are configured to support requirements. However, the Syslog itself must also be configured to filter event records so it is not overwhelmed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify event logging to a syslog server is enabled. 1. Log on to the Web Management Console. 2. Click Maintenance >> Event Logging >> Syslog. 3. Ensure that the "Enable Syslog" checkbox is checked and that one or more "syslog loghosts" are specified. If Symantec ProxySG does not off-load audit records onto a different system or media than the system being audited, this is a finding.

## Group: SRG-APP-000360-NDM-000295

**Group ID:** `V-94669`

### Rule: Symantec ProxySG must generate an alert to the console when a log processing failure is detected such as loss of communications with the Central Log Server or log records are no longer being sent.

**Rule ID:** `SV-104499r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without an alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Symantec ProxySG is configured to send alerts when event logging fails. 1. Log on to the Web Management Console. 2. Click Maintenance >> Events Logging. 3. Confirm that "Severe" is checked. 4. Select the "Mail" tab and confirm an email address of an administrator is entered. If Symantec ProxySG does not generate an alert to the console when a log processing failure is detected such as loss of communications with the Central Log Server or log records are no longer being sent, this is a finding.

## Group: SRG-APP-000371-NDM-000296

**Group ID:** `V-94671`

### Rule: Symantec ProxySG must compare internal information system clocks at least every 24 hours with an authoritative time server.

**Rule ID:** `SV-104501r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside of the configured acceptable allowance (drift) may be inaccurate. Additionally, unnecessary synchronization may have an adverse impact on system performance and may indicate malicious activity. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Symantec ProxySG is configured to use authoritative NTP servers (the NTP protocol itself enforces periodic checks at least every 24 hours). 1. Log on to the Web Management Console. 2. Click Configuration >> General >> Clock. 3. Confirm that the value of the "Query interval (minutes)" field is at least 1440 (24 hours in minutes). 4. Click "NTP", and confirm that the desired authoritative time servers are present. If Symantec ProxySG does not compare internal information system clocks at least every 24 hours with an authoritative time server, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-94673`

### Rule: Symantec ProxySG must be configured to synchronize internal information system clocks with the primary and secondary time sources located in different geographic regions using redundant authoritative time sources.

**Rule ID:** `SV-104503r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must utilize an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DoD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DoD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Symantec ProxySG is configured to use authoritative NTP servers. 1. Log on to the Web Management Console. 2. Click Configuration >> General >> Clock. 3. Click "NTP", and confirm that the desired authoritative time servers are present. If Symantec ProxySG does not be configured to synchronize internal information system clocks with the primary and secondary time sources located in different geographic regions using redundant authoritative time sources, this is a finding.

## Group: SRG-APP-000122-NDM-000239

**Group ID:** `V-94675`

### Rule: Symantec ProxySG must protect the Web Management Console, SSH, and command line interface (CLI) from unauthorized modification.

**Rule ID:** `SV-104505r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Network devices providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Obtain a list of authorized personnel and IP addresses that should have access to the Web Management Console or CLI. 2. Log on to the Web Management Console. 3. Click Configuration >> Policy >> Visual Policy Manager. 4. Click "Launch", select the "Admin Access" layer. 5. Verify any users and/or groups listed in the "source" field of each rule have the appropriate "Action" of either "Allow Read/Write access" or "Allow Read-only Access" per the user/group’s assigned privileges. 6. Verify that the users and/or groups have the "Service" set to "SSH-Console", "HTTPS-Console", or both, depending on the user/group’s assigned privileges. If the Symantec ProxySG is not configured to protect the Web Management Console, SSH, and CLI from unauthorized modification, this is a finding.

## Group: SRG-APP-000121-NDM-000238

**Group ID:** `V-94677`

### Rule: Symantec ProxySG must protect the Web Management Console, SSH, and command line interface (CLI) from unauthorized access.

**Rule ID:** `SV-104507r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Network devices providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Obtain a list of authorized personnel and IP addresses that should have access to the Web Management Console, SSH, or CLI. 2. Log on to the Web Management Console. 3. Click Configuration >> Policy >> Visual Policy Manager. 4. Click "Launch", select the "Admin Access" layer. 5. Verify any users and/or groups listed in the "source" field of each rule have the appropriate "Action" of either "Allow Read/Write access" or "Allow Read-only Access" per the user/group’s assigned privileges. 6. Verify that the users and/or groups have the "Service" set to "SSH-Console", "HTTPS-Console", or both, depending on the user/group’s assigned privileges. If the Symantec ProxySG is not configured to protect the Web Management Console, SSH, and CLI from unauthorized access, this is a finding.

## Group: SRG-APP-000125-NDM-000241

**Group ID:** `V-94679`

### Rule: Symantec ProxySG must back up event logs onto a different system or system component than the system or component being audited.

**Rule ID:** `SV-104509r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of log data includes assuring log data is not accidentally lost or deleted. Regularly backing up audit records to a different system or onto separate media than the system being audited helps to assure, in the event of a catastrophic system failure, the audit records will be retained. This helps to ensure a compromise of the information system being audited does not also result in a compromise of the audit records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify event logging to a remote events collection server is configured in order to send event logs to a different system. 1. Log on to the Web Management Console. 2. Click Maintenance >> Event Logging >> Syslog. 3. Confirm that "Syslog" is "Enabled" and a syslog server is specified. If Symantec ProxySG does not back up event logs onto a different system or system component than the system or component being audited, this is a finding.

## Group: SRG-APP-000516-NDM-000338

**Group ID:** `V-94681`

### Rule: Symantec ProxySG must employ automated mechanisms to centrally verify authentication settings.

**Rule ID:** `SV-104511r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of authentication servers or other centralized management servers for providing centralized authentication services is required for network device management. Maintaining local administrator accounts for daily usage on each network device without centralized management is not scalable or feasible. Without centralized management, it is likely that credentials for some network devices will be forgotten, leading to delays in administration, which itself leads to delays in remediating production problems and in addressing compromises in a timely fashion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify a AAA server is used for access by system administrators as required in DoD. 1. Log on to the Web Management Console. 2. Click Configuration >> Authentication >> RADIUS. 3. Confirm that a RADIUS realm has been configured. 4. Click Configuration >> Policy >> Visual Policy Manager. 5. Click "Launch", select the "Admin Authentication" layer. 6. Confirm the "Action" in each rule references the RADIUS realm in step 3. If Symantec ProxySG does not employ automated mechanisms to centrally verify authentication settings, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-94683`

### Rule: Accounts for device management must be configured on the authentication server and not on Symantec ProxySG itself, except for the account of last resort.

**Rule ID:** `SV-104513r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Centralized management of authentication settings increases the security of remote and nonlocal access methods. This control is particularly important protection against the insider threat. With robust centralized management, audit records for administrator account access to the organization's network devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Symantec ProxySG uses a centrally administered AAA server (LDAP to Active Directory). 1. Log on to the Web Management Console. 2. Click Configuration >> Authentication >> LDAP. 3. Click through the "LDAP Realms", "LDAP DN", "LDAP Search & Groups", "LDAP Objectclasses", and "LDAP General" tabs and ensure that the settings are appropriate for your organization. If accounts for device management are not configured on the authentication server or are on the Symantec ProxySG itself, except for the account of last resort, this is a finding.

## Group: SRG-APP-000329-NDM-000287

**Group ID:** `V-94685`

### Rule: Symantec ProxySG must use Role-Based Access Control (RBAC) to assign privileges to users for access to files and functions.

**Rule ID:** `SV-104515r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Organizations can create specific roles based on job functions and the authorizations (i.e., privileges) to perform needed operations on organizational information systems associated with the organization-defined roles. When administrators are assigned to the organizational roles, they inherit the authorizations or privileges defined for those roles. RBAC simplifies privilege administration for organizations because privileges are not assigned directly to every administrator (which can be a significant number of individuals for mid- to large-size organizations) but are instead acquired through role assignments. RBAC can be implemented either as a mandatory or discretionary form of access control. The RBAC policies and the subjects and objects are defined uniquely for each network device, so they cannot be specified in the requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm that role-based access control is configured. 1. Log on to the Management Console. 2. Click Configuration >> Policy >> Visual Policy Manager. 3. Click "Launch", select "Admin Access Layer" verify that at least one rule has been defined, and that each rule does not have "Any" or a single user defined in the "Source" field. Instead, each rule should have a user group specified in the "Source" field. 4. Confirm with the ProxySG administrator that each rule has the appropriate permission for the user or group specified in the rule (Action set to "Allow Read-Only Access" or "Allow Read-Write Access"). If Symantec ProxySG does not use Role-Based Access Control (RBAC) to assign privileges to users for access to files and functions, this is a finding.

## Group: SRG-APP-000516-NDM-000337

**Group ID:** `V-94687`

### Rule: Symantec ProxySG must employ automated mechanisms to centrally apply authentication settings.

**Rule ID:** `SV-104517r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of authentication servers or other centralized management servers for providing centralized authentication services is required for network device management. Maintaining local administrator accounts for daily usage on each network device without centralized management is not scalable or feasible. Without centralized management, it is likely that credentials for some network devices will be forgotten, leading to delays in administration, which itself leads to delays in remediating production problems and in addressing compromises in a timely fashion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify a AAA server is used for access by system administrators as required in DoD. 1. Log on to the Web Management Console. 2. Click Configuration >> Authentication >> RADIUS, confirm that a RADIUS realm has been configured. 3. Click Policy >> Visual Policy Manager. 4. Click "Launch", select the "Admin Authentication" layer and confirm that the "Action" in each rule references the RADIUS realm in step 2. If Symantec ProxySG does not employ automated mechanisms to centrally apply authentication settings, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-94689`

### Rule: Symantec ProxySG must support organizational requirements to conduct backups of system level information contained in the ProxySG when changes occur or weekly, whichever is sooner.

**Rule ID:** `SV-104519r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System-level information includes default and customized settings and security attributes, including ACLs that relate to the network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial of service condition is possible for all who utilize this critical network component. This control requires the network device to support the organizational central backup process for system-level information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Symantec ProxySG supports backups natively. Verify that backups are being stored remotely. 1. Check with the Symantec ProxySG administrator to determine what their strategy is for backups. 2. Log on to the Web Management Console. 3. Click Configuration >> General >> Archive >> Archive Storage. 4. Confirm that there are entries in the "Remote Upload" fields (Host, Path, Username). If Symantec ProxySG does not support organizational requirements to conduct backups of system level information contained in the Symantec ProxySG when changes occur or weekly, whichever is sooner, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-94691`

### Rule: Symantec ProxySG must obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-104521r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this Certification Authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all management certificates are issued by an appropriate certificate authority. 1. Log on to the Web Management Console. 2. Click Services >> Management Services, click on HTTPS-Console and click "Edit". 3. Note the name of the "keyring" assigned. 4. Click Configuration >> SSL >> Keyrings. 5. Select the keyring that was noted above, click "View Certificate". 6. Confirm that the certificate is issued by the appropriate certificate authority. If Symantec ProxySG does not obtain its public key certificates from an appropriate certificate policy through an approved service provider, this is a finding.

## Group: SRG-APP-000268-NDM-000274

**Group ID:** `V-94693`

### Rule: Symantec ProxySG must configure the maintenance and health monitoring to send an alarm when a critical condition occurs for a component.

**Rule ID:** `SV-104523r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Predictable failure prevention requires organizational planning to address device failure issues. If components key to maintaining the device's security fail to function, the device could continue operating in an insecure state. If appropriate actions are not taken when a network device failure occurs, a denial of service condition may occur which could result in mission failure since the network would be operating without a critical security monitoring and prevention function. Upon detecting a failure of network device security components, the network device must activate a system alert message or send an alarm. The type of alarm should ensure that an administrator is made aware of the situation within a period specified in the site's SSP based on mission impact. Alarms may be a message send to an events server, SNMP server, email/text, or a monitored console. The following alarms are required for ProxySG devices used in DoD. General * CPU utilization * Memory utilization * Interface(s) utilization Licensing * User license utilization * Base license expiration Status * Disk * Sensor Count Status * Reboot</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Symantec ProxySG is configured to send system health notifications. 1. Log on to Web Management Console. 2. Click Maintenance >> Health Monitoring, select the "General" tab. 3. Confirm that the Notification methods are correct for each metric (Log, Trap, and/or Email). If the Symantec ProxySG is not configured to send system health notifications, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-94695`

### Rule: Symantec ProxySG must use only approved management services protocols.

**Rule ID:** `SV-104525r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable unused or unnecessary physical and logical ports/protocols on information systems. Network devices are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the network device must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved. Some network devices have capabilities enabled by default; if these capabilities are not necessary, they must be disabled. If a particular capability is used, then it must be documented and approved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify unauthorized management protocols are not used on the Symantec ProxySG. 1. Log on to Web Management Console. 2. Click Configuration >> Services >> Management Services. 3. Ensure that only approved management services are enabled. "HTTP-Console", in general, should be disabled. If Symantec ProxySG does not use only approved management services protocols, this is a finding.

## Group: SRG-APP-000156-NDM-000250

**Group ID:** `V-94697`

### Rule: Symantec ProxySG must implement HTTPS-console to provide replay-resistant authentication mechanisms for network access to privileged accounts.

**Rule ID:** `SV-104527r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., TLS, WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify only TLS management services are enabled. 1. Log on to Web Management Console. 2. Click Configuration >> Services >> Management Services. 3. Verify "HTTP-Console" is not enabled and that "HTTPS-Console" is enabled. If Symantec ProxySG does not implement HTTPS-console, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-94699`

### Rule: Symantec ProxySG must configure SNMPv3 so that cryptographically-based bidirectional authentication is used.

**Rule ID:** `SV-104529r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, Internet). A remote connection is any connection with a device communicating through an external network (e.g., the Internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify only SNMPv3 (which supports authentication) is configured on the Symantec ProxySG. 1. Log on to the Web Management Console. 2. Click Maintenance >> SNMP. 3. Ensure that only "Enable SNMPv3" is checked. 4. Click on "SNMPv3 Users" and ensure that a user exists in the list. If SNMPv3 (which supports authentication) is not configured or is not the only one configured on the Symantec ProxySG, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-94701`

### Rule: Symantec ProxySG must be configured to enforce a minimum 15-character password length for local accounts.

**Rule ID:** `SV-104531r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the minimum password length is set to at least 15 characters. At the CLI, type: Show Security Look for value of the "Minimum Password Length:". If Symantec ProxySG is not configured to enforce a minimum 15-character password length for local accounts, this is a finding.

## Group: SRG-APP-000172-NDM-000259

**Group ID:** `V-94703`

### Rule: Symantec ProxySG must transmit only encrypted representations of passwords.

**Rule ID:** `SV-104533r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Network devices can accomplish this by making direct function calls to encryption modules or by leveraging operating system encryption capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify only TLS management services are enabled. 1. Log on to the Web Management Console. 2. Click Configuration >> Services >> Management Services. 3. Ensure that "HTTP-Console" is not enabled and that "HTTPS-Console" is enabled. If Symantec ProxySG does not transmit only encrypted representations of passwords, this is a finding.

## Group: SRG-APP-000080-NDM-000345

**Group ID:** `V-94705`

### Rule: Symantec ProxySG must not have a default manufacturer passwords when deployed.

**Rule ID:** `SV-104535r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network devices not protected with strong password schemes provide the opportunity for anyone to crack the password and gain access to the device, which can result in loss of availability, confidentiality, or integrity of network traffic. Many default vendor passwords are well known or are easily guessed; therefore, not removing them prior to deploying the network device into production provides an opportunity for a malicious user to gain unauthorized access to the device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the initial configuration has been set. Attempt to logon to an SSH session using the default user name of "Admin". Verify that there is a prompt for a password. If Symantec ProxySG does not prompt for a password when logon is attempted, this is a finding.

## Group: SRG-APP-000179-NDM-000265

**Group ID:** `V-94707`

### Rule: Symantec ProxySG must be configured to use only FIPS 140-2 approved algorithms for authentication to a cryptographic module with any application or protocol.

**Rule ID:** `SV-104537r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not validated and therefore cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised. The Symantec ProxySG can be configured in FIPS-mode, but this is not recommended by the vendor or DoD. Instead, ensure that FIPS-compliant mechanisms are used for authenticating to cryptographic modules when not in FIPS-mode. This is true by default, but must be verified to prevent misconfiguration by an administrator. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DoD requirements. However, authentication algorithms must configure security processes to use only FIPS-approved and NIST-recommended authentication algorithms. To protect the integrity of the authenticator and authentication mechanism used for the cryptographic module used by the network device, the application, operating system, or protocol must be configured to use one of the following hash functions for hashing the password or other authenticator in accordance with SP 800-131Ar1: SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, SHA-512/256, SHA3-224, SHA3-256, SHA3-384, and SHA3-512. Applications also include HMAC, KDFs, Random Bit Generation, and hash-only applications (e.g., hashing passwords and using SHA-1 or higher to compute a checksum). For digital signature verification, SP800-131Ar1 allows SHA-1 for legacy use where needed. Currently, the AES block cipher algorithm is approved for use in DoD for both applying cryptographic protection (e.g., encryption) and removing or verifying the protection that was previously applied (e.g., decryption). NTP devices use MD5 authentication keys. The MD5 algorithm is not specified in either the FIPS or NIST recommendation; thus, a CAT 1 finding if used. However, MD5 is preferred to no authentication at all.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify only FIPS 140-2 approved algorithms are used. 1. Log on to the CLI via SSH. 2. Type "show management services", press "Enter". 3. Ensure that the "Cipher Suite" attribute contains only FIPS 140-2 approved algorithms. If Symantec ProxySG is not configured to use FIPS 140-2 approved algorithms for authentication to a cryptographic module for any protocol or application, this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-94709`

### Rule: The Symantec ProxySG Web Management Console and SSH sessions must implement cryptographic mechanisms to protect the confidentiality of nonlocal maintenance and diagnostic communications.

**Rule ID:** `SV-104539r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This requirement requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to eavesdropping, potentially putting sensitive data (including administrator passwords) at risk of compromise and potentially allowing hijacking of maintenance sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify only AES ciphers are used for nonlocal maintenance and diagnostic communications. 1. Log on to the CLI via SSH. 2. Type "enable", enter the enable password. 3. Type "configure terminal", press "Enter". 4. Type "show management services" and confirm that the Cipher Suite parameter contains only ciphers that use AES. If Web Management Console and SSH sessions does not implement cryptographic mechanisms to protect the confidentiality of nonlocal maintenance and diagnostic communications, this is a finding.

## Group: SRG-APP-000411-NDM-000330

**Group ID:** `V-94711`

### Rule: The Symantec ProxySG must use FIPS-validated Keyed-Hash Message Authentication Code (HMAC) to protect the integrity of nonlocal maintenance and diagnostic communications.

**Rule ID:** `SV-104541r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Currently, HMAC is the only FIPS-approved algorithm for generating and verifying message/data authentication codes in accordance with FIPS 198-1. Products that are FIPS 140-2 validated will have an HMAC that meets specification; however, the option must be configured for use as the only message authentication code used for authentication to cryptographic modules. Separate requirements for configuring applications and protocols used by each application (e.g., SNMPv3, SSHv2, NTP, HTTPS, and other protocols and applications that require server/client authentication) are required to implement this requirement. Where SSH is used, the SSHv2 protocol suite is required because it includes Layer 7 protocols such as SCP and SFTP, which can be used for secure file transfers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify only FIPS compliant HMAC algorithms are in use. 1. Log on to the CLI via SSH. 2. Type "show management services", press "Enter". 3. Ensure that the "Cipher Suite" attribute lists only cipher suites which use FIPS compliant HMAC algorithms. If any cipher suites are listed that use non-FIPS compliant HMAC algorithms, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-94713`

### Rule: Symantec ProxySG must terminate all network connections associated with a device management session at the end of the session, or the session must be terminated after 10 minutes of inactivity except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-104543r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed Symantec ProxySG. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session. By default, when a user logs off of the session all session attributes are terminated. For abruptly terminated sessions, the Keep-alive default is 2 minutes and then the session is terminated and cleans up. This is inherent to the system and cannot be misconfigured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If there is a documented and validated mission requirement which allows the inactivity period to exceed "10" minutes, this is not a finding. Verify the device management session inactivity timeouts are set to "10" minutes. 1. Log on to the Web Management Console. 2. Click Configuration >> Authentication >> Console Access >> Console Account. 3. Confirm that the "Enforce Web auto-logout" and "Enforce CLI auto-logout" options are set to "10" minutes. If Symantec ProxySG is not configured to terminate the management session after "10" minutes of inactivity, this is a finding.

