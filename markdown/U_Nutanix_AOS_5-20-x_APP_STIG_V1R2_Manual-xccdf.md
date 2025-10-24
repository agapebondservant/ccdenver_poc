# STIG Benchmark: Nutanix AOS 5.20.x Application Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000295-AS-000263

**Group ID:** `V-254097`

### Rule: Nutanix AOS must automatically terminate a user session after 15 minutes of inactivity.

**Rule ID:** `SV-254097r961221_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An attacker can take advantage of user sessions that are left open, thus bypassing the user authentication process. To thwart the vulnerability of open and unused user sessions, the application server must be configured to close the sessions when a configured condition or trigger event is met. Session termination terminates all processes associated with a user's logical session except those processes specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. Satisfies: SRG-APP-000295-AS-000263, SRG-APP-000389-AS-000253, SRG-APP-000390-AS-000254</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS Session Timeout settings are set to 15 minutes. 1. Log in to Prism Element. 2. Click on the gear icon in the upper right. 3. Navigate to "UI Settings" in the left navigation pane. For each user type, verify that the Session Timeout is set correctly. If not, this is a finding.

## Group: SRG-APP-000315-AS-000094

**Group ID:** `V-254098`

### Rule: Nutanix AOS must disable Remote Support Sessions.

**Rule ID:** `SV-254098r961278_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application servers provide remote access capability and must be able to enforce remote access policy requirements or work in conjunction with enterprise tools designed to enforce policy requirements. Automated monitoring and control of remote access sessions allows organizations to detect cyberattacks and also ensure ongoing compliance with remote access policies by logging connection activities of remote users. Examples of policy requirements include, but are not limited to, authorizing remote access to the information system, limiting access based on authentication credentials, and monitoring for unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS Prism Elements is configured to manage remote access. 1. Log in to Prism Element. 2. Click on the gear icon in the upper right. 3. Navigate to the Remote Support section to verify the ability to disable remote sessions, and that it is checked. If Disable Remote Sessions is not available, or is not checked, this is a finding.

## Group: SRG-APP-000014-AS-000009

**Group ID:** `V-254099`

### Rule: Nutanix AOS must implement cryptography mechanisms to protect the confidentiality and integrity of the remote access session.

**Rule ID:** `SV-254099r960759_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Encryption is critical for protection of remote access sessions. If encryption is not being used for integrity, malicious users may gain the ability to modify the application server configuration. The use of cryptography for ensuring integrity of remote access sessions mitigates that risk. Application servers utilize a web management interface and scripted commands when allowing remote access. Web access requires the use of TLS and scripted access requires using ssh or some other form of approved cryptography. Application servers must have a capability to enable a secure remote admin capability. FIPS 140-2 approved TLS versions must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 specifies the preferred configurations for government systems. Satisfies: SRG-APP-000014-AS-000009, SRG-APP-000015-AS-000010</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Validate that the Signing Algorithm of the current SSL certificate. In the Prism UI, click the gear icon, and then select Settings >> SSL Certificate. If there is no SSL Certificate loaded, this is a finding.

## Group: SRG-APP-000033-AS-000024

**Group ID:** `V-254100`

### Rule: Nutanix AOS role mapping must be configured to the lowest privilege level needed for user access.

**Rule ID:** `SV-254100r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Strong access controls are critical to securing the application server. Access control policies (e.g., identity-based policies, role-based policies, attribute-based policies) and access enforcement mechanisms (e.g., access control lists, access control matrices, cryptography) must be employed by the application server to control access between users (or processes acting on behalf of users) and objects (e.g., applications, files, records, processes, application domains) in the application server. Without stringent logical access and authorization controls, an adversary may have the ability, with very little effort, to compromise the application server and associated supporting infrastructure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Nutanix AOS supports user and group role mapping. Ensure all users or groups match that of the documented mapping policies defined by the ISSO. 1. Log in to Prism Element. 2. Click on the gear icon in the upper right. 3. Navigate to "role mapping". For each user or group listed, ensure the role granted is according to access control policies. If not, this is a finding.

## Group: SRG-APP-000340-AS-000185

**Group ID:** `V-254101`

### Rule: Nutanix AOS must prevent nonprivileged users from executing privileged functions to include disabling, circumventing, or altering implemented security safeguards/countermeasures.

**Rule ID:** `SV-254101r961353_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing nonprivileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Restricting nonprivileged users also prevents an attacker, who has gained access to a nonprivileged account, from elevating privileges, creating accounts, and performing system checks and maintenance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Display a list of configured users and their roles on the Prism UI: 1. Log in to Prism Element. 2. Click on the gear icon in the upper right. 3. Navigate to "Local User Management". Validate that only authorized accounts have been assigned the "Cluster Admin" role by comparing the above list against the approved user list provided by the ISSM. If there are any users assigned the "Cluster Admin" role that have not been authorized by the ISSM, this is a finding.

## Group: SRG-APP-000068-AS-000035

**Group ID:** `V-254102`

### Rule: Nutanix AOS must display the standard Mandatory DoD Notice and Consent Banner before granting access to the system.

**Rule ID:** `SV-254102r960843_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Application servers are required to display the Standard Mandatory DoD Notice and Consent Banner before granting access to the system management interface, providing privacy and security notices consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance that states that: (i) Users are accessing a U.S. Government information system; (ii) System usage may be monitored, recorded, and subject to audit; (iii) Unauthorized use of the system is prohibited and subject to criminal and civil penalties; and (iv) The use of the system indicates consent to monitoring and recording. System use notification messages can be implemented in the form of warning banners displayed when individuals log on to the information system. System use notification is intended only for information system access including an interactive logon interface with a human user, and is not required when an interactive interface does not exist. Use this banner for desktops, laptops, and other devices accommodating banners of 1300 characters. The banner shall be implemented as a click-through banner at logon (to the extent permitted by the operating system), meaning it prevents further activity on the information system unless and until the user executes a positive action to manifest agreement by clicking on a box indicating "OK". "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Satisfies: SRG-APP-000068-AS-000035, SRG-APP-000069-AS-000036</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Validate that the Prism WebUI "Welcome Banner" is enabled. 1. Log in to Prism Element. 2. Click on the gear icon in the upper right. 3. Navigate to the "Welcome Banner". 4. Verify the "Enable Banner" box is selected. If the "Enable Banner" box is not checked, this is a finding. Confirm Nutanix AOS Prism WebUI is set to display the Standard Mandatory DoD Notice and Consent Banner. 1. Log in to Prism Element. 2. Click on the gear icon in the upper right. 3. Navigate to the "Welcome Banner". If the Welcome Banner is not configured with the Standard Mandatory DoD Notice and Consent Banner, this is a finding.

## Group: SRG-APP-000080-AS-000045

**Group ID:** `V-254103`

### Rule: Nutanix AOS must offload log records onto a syslog server.

**Rule ID:** `SV-254103r960864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system logging capability is critical for accurate forensic analysis. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, filenames involved, access control or flow control rules invoked. Offloading is a common process in information systems with limited log storage capacity. Centralized management of log records provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. Application servers and their related components are required to offload log records onto a different system or media than the system being logged. Satisfies: SRG-APP-000080-AS-000045, SRG-APP-000358-AS-000064, SRG-APP-000515-AS-000203</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to offload log records onto a different system. $ ncli rsyslog-config ls-servers If no remote syslog servers are defined, this is a finding.

## Group: SRG-APP-000359-AS-000065

**Group ID:** `V-254104`

### Rule: Nutanix AOS must provide an immediate warning to the SA and ISSO, at a minimum, when allocated log record storage volume reaches 75 percent of maximum log record storage capacity.

**Rule ID:** `SV-254104r961398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process logs as required. Log processing failures include software/hardware errors, failures in the log capturing mechanisms, and log storage capacity being reached or exceeded. Notification of the storage condition will allow administrators to take actions so that logs are not lost. This requirement can be met by configuring the application server to utilize a dedicated logging tool that meets this requirement. Satisfies: SRG-APP-000359-AS-000065, SRG-APP-000360-AS-000066</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix Cluster Check (NCC) "CVM DISK | System Audit Volume Usage" is enabled and the threshold values are set correctly. 1. Log in to Prism Element. 2. Select "Health dashboard" from navigation dropdown. 3. Select Actions >> Manage Checks. 4. Scroll down to CVM | Disk section, and then select "System Audit Volume Usage". If the selected check is Disabled, this is a finding. Validate the Alert Policy settings for Warning and Critical are set to 75 percent. If the Warning or Critical values are not set to 75 percent, this is a finding.

## Group: SRG-APP-000108-AS-000067

**Group ID:** `V-254105`

### Rule: Nutanix AOS must be configured to send Cluster Check alerts to the SA and ISSO.

**Rule ID:** `SV-254105r960912_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Logs are essential to monitor the health of the system, investigate changes that occurred to the system, or investigate a security incident. When log processing fails, the events during the failure can be lost. To minimize the timeframe of the log failure, an alert needs to be sent to the SA and ISSO at a minimum. Log processing failures include, but are not limited to, failures in the application server log capturing mechanisms or log storage capacity being reached or exceeded. In some instances, it is preferred to send alarms to individuals rather than to an entire group. Application servers must be able to trigger an alarm and send an alert to, at a minimum, the SA and ISSO in the event there is an application server log processing failure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is set to send SMTP alerts to the organization identified email address(es). 1. Log in to Nutanix Prism Elements. 2. Select "Health" dashboard. 3. On the Actions tab, select "Set NCC Frequency". If the Frequency setting and email address(es) are not set to organization-identified frequency and recipient, this is a finding.

## Group: SRG-APP-000371-AS-000077

**Group ID:** `V-254106`

### Rule: Nutanix AOS must be configured to synchronize internal information system clocks using redundant authoritative time sources.

**Rule ID:** `SV-254106r981685_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Determining the correct time a particular application event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronization of system clocks is needed in order to correctly correlate the timing of events that occur across multiple systems. To meet this requirement, the organization will define an authoritative time source and have each system compare its internal clock at least every 24 hours. Satisfies: SRG-APP-000371-AS-000077, SRG-APP-000372-AS-000212, SRG-APP-000116-AS-000076</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS Prism Elements is configured to use redundant NTP sources. 1. Log in to Prism Element. 2. Click on the gear icon in the upper right. 3. Navigate to the NTP Servers section. 4. Ensure external NTP servers have been configured. If external NTP sources are not configured, this is a finding.

## Group: SRG-APP-000118-AS-000078

**Group ID:** `V-254107`

### Rule: Nutanix AOS must protect log information from any type of unauthorized access.

**Rule ID:** `SV-254107r960930_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to his or her advantage. Application servers contain admin interfaces that allow reading and manipulation of log records. Therefore, these interfaces should not allow unfettered access to those records. Application servers also write log data to log files which are stored on the OS, so appropriate file permissions must also be used to restrict access. Log information includes all information (e.g., log records, log settings, transaction logs, and log reports) needed to successfully log information system activity. Application servers must protect log information from unauthorized read access. Satisfies: SRG-APP-000118-AS-000078, SRG-APP-000119-AS-000079, SRG-APP-000120-AS-000080</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS application server log files are protected from unauthorized read access. The Nutanix AOS application server log files are owned by the Nutanix user and have a file permission of "640". Step 1. Identify actual file name by looking at alert_manager.INFO, which is a symlink for the actual rotating file name. $ sudo ls -al /home/nutanix/data/logs/alert_manager.INFO lrwxrwxrwx. 1 nutanix nutanix 75 Nov 1 17:50 /home/nutanix/data/logs/alert_manager.INFO -> alert_manager.ntnx-<CVM_NAME>.nutanix.log.INFO.<LOG_NUMBER> Step 2. Execute a stat command on the actual application server log file name. $ sudo stat -c "%a %n" /home/nutanix/data/logs/alert_manager.ntnx-<CVM_NAME>.nutanix.log.INFO.<LOG_NUMBER> 640 /home/nutanix/data/logs/alert_manager.ntnx<CVM_NAME>.nutanix.log.INFO.<LOG_NUMBER> If the output of the actual log file name is not "640", this is a finding.

## Group: SRG-APP-000380-AS-000088

**Group ID:** `V-254108`

### Rule: Nutanix AOS must enforce access restrictions associated with changes to application server configuration.

**Rule ID:** `SV-254108r961461_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with access restrictions pertaining to change control, it should be noted that any changes to the software, and/or application server configuration can potentially have significant effects on the overall security of the system. Access restrictions for changes also include application software libraries. If the application server provides automatic code deployment capability, (where updates to applications hosted on the application server are automatically performed, usually by the developers' IDE tool), it must also provide a capability to restrict the use of automatic application deployment. Automatic code deployments are allowable in a development environment, but not in production.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix Prism Elements is setup with Role Based Access Controls. 1. Log in into Nutanix Prism Elements. 2. Select the gear icon on top right corner. 3. Select "Authentication" from left navigation pane. If no Organizational approved Directory (AD/LDAP) is listed, this is a finding. 4. Select "Role Mapping". If no Role mappings are listed, this is a finding.

## Group: SRG-APP-000148-AS-000101

**Group ID:** `V-254109`

### Rule: Nutanix AOS must use an enterprise user management system to uniquely identify and authenticate users.

**Rule ID:** `SV-254109r960969_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthorized access, application server users must be uniquely identified and authenticated. This is typically accomplished via the use of a user store which is either local (OS-based) or centralized (LDAP) in nature. To ensure support to the enterprise, the authentication must utilize an enterprise solution.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Nutanix AOS is set to use enterprise user management systems. 1. Log in to Prism Element. 2. Click on the gear icon in the upper right. 3. Navigate to the "Authentication" settings. If an Active Directory or OpenLDAP server is not configured, this is a finding. Verify that only one local user account exists as the account of last resort. Navigate to Local User Management. If more than one local user account exists, this is a finding.

## Group: SRG-APP-000149-AS-000102

**Group ID:** `V-254110`

### Rule: Nutanix AOS must use multifactor authentication for account access.

**Rule ID:** `SV-254110r960972_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Multifactor authentication creates a layered defense and makes it more difficult for an unauthorized person to access the application server. If one factor is compromised or broken, the attacker still has at least one more barrier to breach before successfully breaking into the target. Unlike a simple username/password scenario where the attacker could gain access by knowing both the username and password without the user knowing his account was compromised, multifactor authentication adds the requirement that the attacker must have something from the user, such as a token, or to biometrically be the user. Multifactor authentication is defined as using two or more factors to achieve authentication. Factors include: (i) Something a user knows (e.g., password/PIN); (ii) Something a user has (e.g., cryptographic identification device, token); or (iii) Something a user is (e.g., biometric). A CAC or PKI Hardware Token meets this definition. A privileged account is defined as an information system account with authorizations of a privileged user. These accounts would be capable of accessing the web management interface. When accessing the application server via a network connection, administrative access to the application server must be PKI Hardware Token enabled. Satisfies: SRG-APP-000149-AS-000102, SRG-APP-000151-AS-000103</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is set to use multifactor authentication. 1. Log in to Prism Element. 2. Click on the gear icon in the upper right. 3. Navigate to the Authentication settings. If CAC authentication is not enabled, this is a finding.

## Group: SRG-APP-000391-AS-000239

**Group ID:** `V-254111`

### Rule: Nutanix AOS must accept Personal Identity Verification (PIV) credentials to access the management interface.

**Rule ID:** `SV-254111r961494_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. PIV credentials are only used in an unclassified environment. DoD has mandated the use of the CAC to support identity management and personal authentication for systems covered under HSPD 12, as well as its use as a primary component of layered protection for national security systems. The application server must support the use of PIV credentials to access the management interface and perform management functions. Satisfies: SRG-APP-000391-AS-000239, SRG-APP-000392-AS-000240, SRG-APP-000177-AS-000126, SRG-APP-000401-AS-000243, SRG-APP-000402-AS-000247, SRG-APP-000403-AS-000248</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is set to use multifactor authentication. 1. Log in to Prism Element. 2. Click on the gear icon in the upper right. 3. Navigate to the Authentication settings. If CAC authentication is not enabled, this is a finding.

## Group: SRG-APP-000172-AS-000121

**Group ID:** `V-254112`

### Rule: Nutanix AOS must utilize encryption when using LDAP for authentication.

**Rule ID:** `SV-254112r961029_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords during transmission. Application servers have the capability to utilize LDAP directories for authentication. If LDAP connections are not protected during transmission, sensitive authentication credentials can be stolen. When the application server utilizes LDAP, the LDAP traffic must be encrypted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is set to use encryption when using LDAP. 1. Log in to Prism Element. 2. Click on the gear icon in the upper right. 3. Navigate to the Authentication settings. 4. Add an Active Directory or OpenLDAP server to the Directory List. If an Active Directory or OpenLDAP server is not using port 636, this is a finding.

## Group: SRG-APP-000175-AS-000124

**Group ID:** `V-254113`

### Rule: Nutanix AOS must perform RFC 5280-compliant certification path validation.

**Rule ID:** `SV-254113r961038_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is that OCSP checking is enabled. $ ncli authconfig get-client-authentication-config 'Auth Config Status : true' If "Auth config status" is not set to "true", this is a finding.

## Group: SRG-APP-000514-AS-000137

**Group ID:** `V-254114`

### Rule: Nutanix AOS must use DoD- or CNSS-approved PKI Class 3 or Class 4 certificates.

**Rule ID:** `SV-254114r961857_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Class 3 PKI certificates are used for servers and software signing rather than for identifying individuals. Class 4 certificates are used for business-to-business transactions. Utilizing unapproved certificates not issued or approved by DoD or CNS creates an integrity risk. The application server must utilize approved DoD or CNS Class 3 or Class 4 certificates for software signing and business-to-business transactions. Satisfies: SRG-APP-000514-AS-000137, SRG-APP-000427-AS-000264</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured with a trusted DoD root CA signed certificate. 1. Log in to Prism Element. 2. Click on the gear icon in the upper right. 3. Navigate to the SSL Certificate section. 4. Ensure the approved CA signed certificate is installed. If the certificate used is not from an approved DoD-approved CA, this is a finding.

## Group: SRG-APP-000231-AS-000133

**Group ID:** `V-254115`

### Rule: Nutanix AOS must protect the confidentiality and integrity of all information at rest.

**Rule ID:** `SV-254115r961128_rule`
**Severity:** high

**Description:**
<VulnDiscussion>When data is written to digital media such as hard drives, mobile computers, external/removable hard drives, personal digital assistants, flash/thumb drives, etc., there is risk of data loss and data compromise. Fewer protection measures are needed for media containing information determined by the organization to be in the public domain, to be publicly releasable, or to have limited or no adverse impact if accessed by other than authorized personnel. In these situations, it is assumed the physical access controls where the media resides provide adequate protection. As part of a defense-in-depth strategy, data owners and DoD consider routinely encrypting information at rest on selected secondary storage devices. The employment of cryptography is at the discretion of the information owner/steward. The selection of the cryptographic mechanisms used is based upon maintaining the confidentiality and integrity of the information. The strength of mechanisms is commensurate with the classification and sensitivity of the information. The application server must directly provide, or provide access to, cryptographic libraries and functionality that allow applications to encrypt data when it is stored. Satisfies: SRG-APP-000231-AS-000133, SRG-APP-000231-AS-000156, SRG-APP-000428-AS-000265, SRG-APP-000429-AS-000157</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is set to use data at rest encryption. 1. Log in to Prism Element. 2. Click on the gear icon in the upper right. 3. Navigate to the Data-at-Rest Encryption section. 4. Ensure "Software Encryption" is enabled. If Software Encryption is not configured, this is a finding.

## Group: SRG-APP-000267-AS-000170

**Group ID:** `V-254116`

### Rule: Nutanix AOS must restrict error messages only to authorized users.

**Rule ID:** `SV-254116r961170_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the application provides too much information in error logs and administrative messages to the screen, this could lead to compromise. The structure and content of error messages need to be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements. Application servers must protect the error messages created by the application server. All application server user accounts are used for the management of the server and the applications residing on the application server. All accounts are assigned to a certain role with corresponding access rights. The application server must restrict access to error messages so only authorized users may view them. Error messages are usually written to logs contained on the file system. The application server will usually create new log files as needed and must take steps to ensure that the proper file permissions are utilized when the log files are created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Nutanix AOS application server log files are owned by the Nutanix user and have a file permission of "640". Step 1. Identify actual file name by looking at alert_manager.INFO, which is a symlink, the actual rotating file name. $ sudo ls -al /home/nutanix/data/logs/alert_manager.INFO lrwxrwxrwx. 1 nutanix nutanix 75 Nov 1 17:50 /home/nutanix/data/logs/alert_manager.INFO -> alert_manager.ntnx-<CVM_NAME>.nutanix.log.INFO.<LOG_NUMBER> Step 2. Execute a stat command on the actual application server log file name. $ sudo stat -c "%a %n" /home/nutanix/data/logs/alert_manager.ntnx-<CVM_NAME>.nutanix.log.INFO.<LOG_NUMBER> 640 /home/nutanix/data/logs/alert_manager.ntnx<CVM_NAME>.nutanix.log.INFO.<LOG_NUMBER> If the output of the actual log file name is not "640", this is a finding.

## Group: SRG-APP-000211-AS-000146

**Group ID:** `V-254117`

### Rule: Nutanix AOS must separate hosted application functionality from application server management functionality.

**Rule ID:** `SV-254117r961095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The application server consists of the management interface and hosted applications. By separating the management interface from hosted applications, the user must authenticate as a privileged user to the management interface before being presented with management functionality. This prevents nonprivileged users from having visibility to functions not available to the user. By limiting visibility, a compromised nonprivileged account does not offer information to the attacker to functionality and information needed to further the attack on the application server. Application server management functionality includes functions necessary to administer the application server and requires privileged access via one of the accounts assigned to a management role. The hosted application and hosted application functionality consists of the assets needed for the application to function, such as the business logic, databases, user authentication, etc. The separation of application server administration functionality from hosted application functionality is either physical or logical and is accomplished by using different computers, different central processing units, different instances of the operating system, network addresses, network ports, or combinations of these methods, as appropriate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Management information flow can be isolated to a separate vLAN from the guest VMs. 1. Log in to Prism Element. 2. Click on the gear icon in the upper right corner. 3. Under the "Settings" menu click "Network Configuration", and then select the "Internal Interfaces" tab. 4. Click on the "Management LAN" option. If VLAN ID is "0" or blank, this is a finding.

## Group: SRG-APP-000211-AS-000146

**Group ID:** `V-254118`

### Rule: Nutanix AOS must configure network traffic segmentation when using Disaster Recovery Services.

**Rule ID:** `SV-254118r961095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The application server consists of the management interface and hosted applications, as well as cluster management functions. Separating the management interface from hosted applications prevents nonprivileged users from having visibility to functions not available to the user. Isolating cluster management functions ensures that cluster housekeeping tasks such as disaster recovery, replication, etc. function on their own network segment away from production traffic. Application server management functionality includes functions necessary to administer the application server and requires privileged access via one of the accounts assigned to a management role. The hosted application and hosted application functionality consists of the assets needed for the application to function, such as the business logic, databases, user authentication, etc. The separation of application server administration functionality from hosted application functionality is either physical or logical and is accomplished by using different computers, different central processing units, different instances of the operating system, network addresses, network ports, or combinations of these methods, as appropriate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
DR network traffic segmentation is required when using Disaster Recovery Services. Disaster recovery can be used with Asynchronous, NearSync, and Metro Availability replications only if both the primary site and the recovery site are configured with Network Segmentation. Validate that Disaster Recovery Services is configured to use Specific Network Traffic Segmentation. If Disaster Recovery services are not in use this check is NA. 1. Log in to the Prism Elements web console and click the gear icon at the top-right corner of the page. 2. In the left pane, click "Network Configuration". 3. In the details pane, on the Internal Interfaces tab, review the existing interfaces to ensure there is an identified interface for DR traffic. If no identified network interface is defined for DR traffic, this is a finding.

## Group: SRG-APP-000456-AS-000266

**Group ID:** `V-254119`

### Rule: Nutanix AOS must be running an operating system release that is currently supported by the vendor.

**Rule ID:** `SV-254119r1001000_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes) to production systems after thorough testing of the patches within a lab environment. Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Product version is end of life and no longer supported. If the system is running AOS version 5.20.x, this is a finding.

