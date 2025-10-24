# STIG Benchmark: VMware NSX-T Manager NDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000033-NDM-000212

**Group ID:** `V-251778`

### Rule: NSX-T Manager must restrict the use of configuration, administration, and the execution of privileged commands to authorized personnel based on organization-defined roles.

**Rule ID:** `SV-251778r879530_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access, privileged access must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. Controls for this requirement include prevention of non-privileged users from executing privileged functions to include disabling, circumventing, or altering implemented security safeguards/countermeasures; enforcing the use of organization-defined role-based access control policies over defined subjects and objects; and restricting access associated with changes to the system components. Satisfies: SRG-APP-000033-NDM-000212, SRG-APP-000340-NDM-000288, SRG-APP-000329-NDM-000287, SRG-APP-000340-NDM-000288</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to System >> Users and Roles >> User Role Assignment. View each user and group and verify the role assigned to it. Application service account and user required privileges must be documented. If any user/group or service account are assigned to roles with privileges that are beyond those assigned by the SSP, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-251779`

### Rule: The NSX-T Manager must be configured to enforce the limit of three consecutive invalid logon attempts, after which time it must block any login attempt for 15 minutes.

**Rule ID:** `SV-251779r879546_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX-T Manager shell, run the following command(s): > get auth-policy api lockout-reset-period Expected result: 900 seconds If the output does not match the expected result, this is a finding. > get auth-policy api lockout-period Expected result: 900 seconds If the output does not match the expected result, this is a finding. > get auth-policy api max-auth-failures Expected result: 3 If the output does not match the expected result, this is a finding. > get auth-policy cli lockout-period Expected result: 900 seconds If the output does not match the expected result, this is a finding. > get auth-policy cli max-auth-failures Expected result: 3 If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-251780`

### Rule: The NSX-T Manager must enforce a minimum 15-character password length.

**Rule ID:** `SV-251780r919231_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX-T Manager shell, run the following command(s): > get auth-policy minimum-password-length Expected result: 15 characters If the "minimum-password-length" is not set to 15 or greater, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-251781`

### Rule: The NSX-T Manager must terminate the device management session at the end of the session or after 10 minutes of inactivity.

**Rule ID:** `SV-251781r916342_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX-T Manager shell, run the following command(s): > get service http | find Session Expected result: Session timeout: 600 If the output does not match the expected result, this is a finding. From an NSX-T Manager shell, run the following command(s): > get cli-timeout Expected result: 600 seconds If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-251782`

### Rule: The NSX-T Manager must be configured to synchronize internal information system clocks using redundant authoritative time sources.

**Rule ID:** `SV-251782r879746_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must utilize an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DoD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DoD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to System >> Fabric >> Profiles >> Node Profiles. Click "All NSX Nodes" and verify the NTP servers listed. or From an NSX-T Manager shell, run the following command(s): > get ntp-server If the output does not contain at least two authoritative time sources, this is a finding. If the output contains unknown or non-authoritative time sources, this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-251783`

### Rule: The NSX-T Manager must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC).

**Rule ID:** `SV-251783r879747_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the application include date and time. Time is commonly expressed in UTC, a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to System >> Fabric >> Profiles >> Node Profiles. Click "All NSX Nodes" and verify the time zone. or From an NSX-T Manager shell, run the following command(s): > get clock If system clock is not configured with the UTC time zone, this is a finding. Note: This check must be run from each NSX-T Manager as they are configured individually if done from the command line.

## Group: SRG-APP-000400-NDM-000313

**Group ID:** `V-251784`

### Rule: The NSX-T Manager must prohibit the use of cached authenticators after an organization-defined time period.

**Rule ID:** `SV-251784r879773_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some authentication implementations can be configured to use cached authenticators. If cached authentication information is out-of-date, the validity of the authentication information may be questionable. The organization-defined time period should be established for each device depending on the nature of the device; for example, a device with just a few administrators in a facility with spotty network connectivity may merit a longer caching time period than a device with many administrators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX-T Manager shell, run the following command(s): > get service http | find Session Expected result: Session timeout: 600 If the output does not match the expected result, this is a finding. From an NSX-T Manager shell, run the following command(s): > get cli-timeout Expected result: 600 seconds If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-251785`

### Rule: The NSX-T Manager must be configured to protect against known types of denial-of-service (DoS) attacks by employing organization-defined security safeguards.

**Rule ID:** `SV-251785r879806_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of network devices to mitigate the impact of DoS attacks that have occurred or are ongoing on device availability. For each network device known, potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the device opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks. The security safeguards cannot be defined at the DoD level because they vary according to the capabilities of the individual network devices and the security controls applied on the adjacent networks (for example, firewalls performing packet filtering to block DoS attacks).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX-T Manager shell, run the following command(s): > get service http | find limit Expected result: Client API rate limit: 100 requests/sec Client API concurrency limit: 40 connections Global API concurrency limit: 199 connections If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000499-NDM-000319

**Group ID:** `V-251786`

### Rule: The NSX-T Manager must generate audit records when successful/unsuccessful attempts to delete administrator privileges occur.

**Rule ID:** `SV-251786r879870_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX-T Manager shell, run the following command(s): > get service async_replicator | find Logging > get service http | find Logging > get service manager | find Logging > get service policy | find Logging Expected result: Logging level: info If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-251787`

### Rule: The NSX-T Manager must be configured to send logs to a central log server.

**Rule ID:** `SV-251787r879886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX-T Manager shell, run the following command(s): > get logging-servers If any configured logging-servers are not configured with protocol of "tcp", "li-tls", or "tls" and level of "info", this is a finding. If no logging-servers are configured, this is a finding. Note: This check must be run from each NSX-T Manager as they are configured individually.

## Group: SRG-APP-000516-NDM-000334

**Group ID:** `V-251788`

### Rule: The NSX-T Manager must generate log records for the info level to capture the DoD-required auditable events.

**Rule ID:** `SV-251788r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. Logging the actions of specific events provides a means to investigate an attack; to recognize resource utilization or capacity thresholds; or to identify an improperly configured network device. If auditing is not comprehensive, it will not be useful for intrusion monitoring, security investigations, and forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX-T Manager shell, run the following command(s): > get service async_replicator | find Logging > get service http | find Logging > get service manager | find Logging > get service policy | find Logging Expected result: Logging level: info If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-251789`

### Rule: The NSX-T Manager must integrate with either VMware Identity Manager (vIDM) or VMware Workspace ONE Access.

**Rule ID:** `SV-251789r916111_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Centralized management of authentication settings increases the security of remote and nonlocal access methods. This control is particularly important protection against the insider threat. With robust centralized management, audit records for administrator account access to the organization's network devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each network device. Use VMware Identity Manager or Workspace ONE configured to meet DoD requirements for authentication, authorization, and access control. This does not require an additional license. Configuration details of this product are not in scope beyond this requirement. Ensure the VMware Workspace ONE Access/VMware Identity Manager acts as a broker to different identity stores and providers, including Active Directory and SAML. Two supplements are included with the VMware NSX-T STIG package that provide guidance from the vendor for configuration of VMware Identity Manager and VMware Workspace ONE Access. Satisfies: SRG-APP-000516-NDM-000336, SRG-APP-000177-NDM-000263, SRG-APP-000149-NDM-000247, SRG-APP-000080-NDM-000220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to System >> Users and Roles >> VMware Identity Manager. If the VMware Identity Manager integration is not enabled, this is a finding. If the user is not redirected to VMware Identity Manager or Workspace ONE Access when attempting to log in to the NSX-T Manager web interface and prompted to select a certificate and enter a PIN, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-251790`

### Rule: The NSX-T Manager must be configured to conduct backups on an organizationally defined schedule.

**Rule ID:** `SV-251790r916221_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System-level information includes default and customized settings and security attributes, including ACLs that relate to the network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial of service condition is possible for all who utilize this critical network component. This control requires the network device to support the organizational central backup process for system-level information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to System >> Backup and Restore to view the backup configuration. If backup is not configured and scheduled on a recurring frequency, this is a finding.

## Group: SRG-APP-000516-NDM-000341

**Group ID:** `V-251791`

### Rule: The NSX-T Manager must support organizational requirements to conduct backups of information system documentation, including security-related documentation, when changes occur or weekly, whichever is sooner.

**Rule ID:** `SV-251791r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system backup is a critical step in maintaining data assurance and availability. Information system and security-related documentation contains information pertaining to system configuration and security settings. If this information were not backed up, and a system failure were to occur, the security settings would be difficult to reconfigure quickly and accurately. Maintaining a backup of information system and security-related documentation provides for a quicker recovery time when system outages occur. This control requires the network device to support the organizational central backup process for user account information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to System >> Backup and Restore to view the backup configuration. If backup is not configured and scheduled on a recurring frequency, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-251792`

### Rule: The NSX-T Manager must obtain its public key certificates from an approved DoD certificate authority.

**Rule ID:** `SV-251792r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For Federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this Certification Authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
NSX-T Manager uses a certificate for each manager and one for the cluster VIP. In some cases these are the same, but each node and cluster VIP certificate must be checked individually. Browse to the NSX-T Manager web interface for each node and cluster VIP and view the certificate and its issuer of the website. or From an NSX-T Manager shell, run the following command(s): > get certificate api > get certificate cluster Save the output to a .cer file to examine. If the certificate the NSX-T Manager web interface or cluster is using is not issued by an approved DoD certificate authority and is not currently valid, this is a finding.

## Group: SRG-APP-000516-NDM-000350

**Group ID:** `V-251793`

### Rule: The NSX-T Manager must be configured to send log data to a central log server for the purpose of forwarding alerts to the administrators and the Information System Security Officer (ISSO).

**Rule ID:** `SV-251793r916114_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The aggregation of log data kept on a syslog server can be used to detect attacks and trigger an alert to the appropriate security personnel. The stored log data can used to detect weaknesses in security that enable the network IA team to find and address these weaknesses before breaches can occur. Reviewing these logs, whether before or after a security breach, is important in showing whether someone is an internal employee or an outside threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX-T Manager shell, run the following command(s): > get logging-servers If any configured logging-servers are not configured with protocol of "tcp", "li-tls", or "tls" and level of "info", this is a finding. If no logging-servers are configured, this is a finding. Note: This check must be run from each NSX-T Manager as they are configured individually.

## Group: SRG-APP-000516-NDM-000351

**Group ID:** `V-251794`

### Rule: The NSX-T Manager must be running a release that is currently supported by the vendor.

**Rule ID:** `SV-251794r879887_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices running an unsupported operating system lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to the System >> Upgrade. If the NSX-T Manager current version is not the latest approved for use in DoD and supported by the vendor, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-251795`

### Rule: The NSX-T Manager must not provide environment information to third parties.

**Rule ID:** `SV-251795r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Providing technical details about an environment's infrastructure to third parties could unknowingly expose sensitive information to bad actors if intercepted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to System >> Customer Experience Improvement Program. If Joined is set to "Yes", this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-251796`

### Rule: The NSX-T Manager must disable SSH.

**Rule ID:** `SV-251796r879588_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The NSX-T shell provides temporary access to commands essential for server maintenance. Intended primarily for use in break-fix scenarios, the NSX-T shell is well suited for checking and modifying configuration details, not always generally accessible, using the web interface. The NSX-T shell is accessible remotely using SSH. Under normal operating conditions, SSH access to the managers must be disabled as is the default. As with the NSX-T shell, SSH is also intended only for temporary use during break-fix scenarios. SSH must therefore be disabled under normal operating conditions and must only be enabled for diagnostics or troubleshooting. Remote access to the managers must therefore be limited to the web interface and API at all other times.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX-T Manager shell, run the following command(s): > get service ssh Expected results: Service name: ssh Service state: stopped Start on boot: False If the output does not match the expected results, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-251797`

### Rule: The NSX-T Manager must disable unused local accounts.

**Rule ID:** `SV-251797r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Prior to NSX-T 3.1 and earlier, there are three local accounts: root, admin, and audit. These local accounts could not be disabled and no additional accounts could be created. Starting in NSX-T 3.1.1, there are two additional guest user accounts: guestuser1 and guestuser2. The local accounts for audit and guest users are disabled by default, but can be deactivated once active; however, admin and root accounts cannot be disabled. These accounts should remain disabled and unique non-local user accounts should be used instead.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If NSX-T is not at least version 3.1.1, this is not applicable. From the NSX-T Manager web interface, go to the System >> Users and Roles >> Local Users and view the status column. If the audit, guestuser1, or guestuser2 local accounts are active, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-251798`

### Rule: The NSX-T Manager must disable TLS 1.1 and enable TLS 1.2.

**Rule ID:** `SV-251798r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>TLS 1.0 and 1.1 are deprecated protocols with well-published shortcomings and vulnerabilities. TLS 1.2 must be enabled on all interfaces and TLS 1.1 and 1.0 disabled where supported.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Viewing TLS protocol enablement must be done via the API. Execute the following API call using curl or another REST API client: GET https://<nsx-mgr>/api/v1/cluster/api-service Expected result: "protocol_versions": [ { "name": "TLSv1.1", "enabled": false }, { "name": "TLSv1.2", "enabled": true } ], If TLS 1.1 is enabled, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-251799`

### Rule: The NSX-T Manager must disable SNMP v2.

**Rule ID:** `SV-251799r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SNMPv3 supports commercial-grade security, including authentication, authorization, access control, and privacy. Previous versions of the protocol contained well-known security weaknesses that were easily exploited. As such, SNMPv1/2 receivers must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to the System >> Fabric >> Profiles >> Node Profiles. Click "All NSX Nodes" and view the SNMP Polling and Traps configuration. If SNMP v2c Polling or Traps are configured, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-251800`

### Rule: The NSX-T Manager must enable the global FIPS compliance mode for load balancers.

**Rule ID:** `SV-251800r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If unsecured protocols (lacking cryptographic mechanisms) are used for load balancing, the contents of those sessions will be susceptible to eavesdropping, potentially putting sensitive data at risk of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to the Home >> Monitoring Dashboards >> Compliance Report. Review the compliance report for code 72024 with description Load balancer FIPS global setting disabled. Note: This may also be checked via the API call GET https://<nsx-mgr>/policy/api/v1/infra/global-config If the global FIPS setting is disabled for load balancers, this is a finding.

