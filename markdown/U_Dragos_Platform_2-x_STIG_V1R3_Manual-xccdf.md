# STIG Benchmark: Dragos Platform 2.x Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000002

**Group ID:** `V-270904`

### Rule: Dragos must configure idle timeouts at 10 minutes.

**Rule ID:** `SV-270904r1058027_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. This is typically at the operating system level but may be at Dragos level. When Dragos design specifies Dragos rather than the operating system will determine when to lock the session, Dragos session lock event must include an obfuscation of the display screen to prevent other users from reading what was previously displayed. Publicly viewable images can include static or dynamic images, for example, patterns used with screen savers, photographic images, solid colors, a clock, a battery life indicator, or a blank screen, with the additional caveat that none of the images convey sensitive information. Satisfies: SRG-APP-000002, SRG-APP-000003, SRG-APP-000190, SRG-APP-000295, SRG-APP-000389</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify session timeout is configured. In the UI, navigate to Admin >> SiteStore Management >> Advanced Settings. Click "Configurations". If Idle Auto-Logout Minutes is not set to "10" minutes, this is a finding. If Re-Authenticate User Device (Inactive) is not set to "1h", this is a finding.

## Group: SRG-APP-000023

**Group ID:** `V-270910`

### Rule: Dragos Platform must use an Identity Provider (IDP) for authentication and authorization processes.

**Rule ID:** `SV-270910r1057994_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enterprise environments make application account management challenging and complex. A manual process for account management functions adds the risk of a potential oversight or other error. A comprehensive application account management process that includes automation helps to ensure accounts designated as requiring attention are consistently and promptly addressed. Examples include, but are not limited to, using automation to take action on multiple accounts designated as inactive, suspended, or terminated or by disabling accounts located in noncentralized account stores such as multiple servers. This requirement applies to all account types, including individual/user, shared, group, system, guest/anonymous, emergency, developer/manufacturer/vendor, temporary, and service. Dragos Platform must be configured to automatically provide account management functions and these functions must immediately enforce the organization's current account policy. The automated mechanisms may reside within Dragos Platform itself or may be offered by the operating system or other infrastructure providing automated account management capabilities. Automated mechanisms may be comprised of differing technologies that when placed together contain an overall automated mechanism supporting an organization's automated account management requirements. Account management functions include: assignment of group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. The use of automated mechanisms can include, for example: using email or text messaging to automatically notify account managers when users are terminated or transferred; using the information system to monitor account usage; and using automated telephonic notification to report atypical system account usage. Satisfies: SRG-APP-000023, SRG-APP-000025, SRG-APP-000065, SRG-APP-000149, SRG-APP-000150, SRG-APP-000151, SRG-APP-000152, SRG-APP-000163, SRG-APP-000165, SRG-APP-000170, SRG-APP-000173, SRG-APP-000233, SRG-APP-000345, SRG-APP-000317, SRG-APP-000318</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the authentication method being used by the Platform. In the UI, navigate to Admin >> SiteStore Management >> Authentication Providers. If the Platform does not have an Authentication Provider configured, this is a finding.

## Group: SRG-APP-000068

**Group ID:** `V-270916`

### Rule: The Dragos Platform must display the Standard Mandatory DOD Notice and Consent Banner before granting local or remote access to the system.

**Rule ID:** `SV-270916r1057996_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." Satisfies: SRG-APP-000068, SRG-APP-000069</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Dragos Platform displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the system when login in via SSH. If the banner does not exist or is not formatted in accordance with applicable DOD policy, this is a finding.

## Group: SRG-APP-000070

**Group ID:** `V-270917`

### Rule: The publicly accessible Dragos Platform application must display the Standard Mandatory DOD Notice and Consent Banner before granting access to Dragos Platform.

**Rule ID:** `SV-270917r1058026_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible application ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with DTM-08-060. Use the following verbiage for desktops, laptops, and other devices accommodating banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Standard Mandatory DOD Notice and Consent Banner appears before being granted access to Dragos Platform UI. If the Standard Mandatory DOD Notice is not presented, this is a finding.

## Group: SRG-APP-000080

**Group ID:** `V-270919`

### Rule: The Dragos Platform must only allow local administrative and service user accounts.

**Rule ID:** `SV-270919r1107124_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only two default accounts facilitate the initial setup and configuration of the Platform. These accounts provide immediate access to the system, allowing administrators to quickly get the system up and running without needing to create new user accounts during the initial installation phase. During maintenance, updates, or support operations, default accounts allow vendor support teams to access the system without needing to manage a variety of customer-specific accounts. This can streamline support activities and reduce downtime. Default accounts passwords need to be protected so they cannot be exploited by attackers to gain unauthorized access to the system. Satisfies: SRG-APP-000080, SRG-APP-000234</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify local user accounts. While logged in to the Dragos Platform with a user account with administrative privileges, navigate to Admin >> User Management >> Users. If any local user except the UI Administrator and DragOS CLI Service Account exists, this is a finding.

## Group: SRG-APP-000108

**Group ID:** `V-270932`

### Rule: The Dragos Platform must have notification and audit services installed.

**Rule ID:** `SV-270932r1058029_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Installing the Knowledge Pack(s) is essential for the Dragos Platform to provide comprehensive security monitoring, compliance, and operational visibility within industrial environments. It enhances the Platform's capabilities in detecting and responding to threats, ensuring regulatory compliance, and maintaining the overall security. It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. The pack provides enhanced visibility into the operations of the Dragos Platform. This includes monitoring user activities, changes to system configurations, and other critical events. Improved visibility helps in identifying potential security issues and operational anomalies before they escalate into significant problems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure all notification and audit services are functional. Log in to the SiteStore CLI and execute the following command: system k3s status If the message does not return "system is ready", this is a finding. (Note that for approximately 15–20 minutes after system startup or reboot, system will not be ready. Additionally, until the sensor is paired with a SiteStore, one pod on the sensor will not be ready).

## Group: SRG-APP-000125

**Group ID:** `V-270944`

### Rule: The Dragos Platform must be configured to send backup audit records.

**Rule ID:** `SV-270944r1107127_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the Dragos Platform to send out backup audit records is a critical best practice for ensuring the security, integrity, and availability of audit data. It supports disaster recovery, regulatory compliance, forensic investigations, and overall operational resilience, thereby strengthening the organization's cybersecurity posture. Storing backup audit records in a separate location ensures that even if the primary system is compromised or experiences a failure, the audit records remain intact and secure. This separation enhances the overall integrity and security of the audit data. In the event of a catastrophic event such as a cyberattack, hardware failure, or natural disaster, having backup audit records stored offsite allows for recovery of critical audit data. This capability is essential for restoring operations and conducting post-incident analyses. In the aftermath of a security incident, forensic investigators rely on audit records to reconstruct events and understand the nature and impact of the incident. Backup audit records provide a reliable source of information for these investigations, even if the primary records are tampered with or deleted. Regularly backing up audit records ensures operational continuity by safeguarding critical data. In case of an unexpected event, the Dragos Platform can quickly access the backup records to continue monitoring and analyzing security events without significant disruption. Regular backups of audit records help ensure accountability by providing a reliable and tamper-evident log of activities. This accountability is essential for maintaining trust and transparency within the organization and with external stakeholders. Satisfies: SRG-APP-000125, SRG-APP-000515, SRG-APP-000358</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify third-party server is used to offload audit records. 1. Check for a configured Syslog Server. In the UI, navigate to Admin >> Integrations. Click "LAUNCH" in the Syslog section. If a Syslog Server is not listed or Status is not connected, this is a finding. If the protocol of the Syslog Server is not TLS or mTLS, this is a finding. 2. Check for an export rule. In the UI, navigate to Notification >> RULES Tab. Verify a rule exists and has the following: Action = "Send Syslog (<your syslog server>)" Criteria = "IF Notification Type equals System" If this rule does not exist with the correct Action and Criteria, this is a finding.

## Group: SRG-APP-000126

**Group ID:** `V-270945`

### Rule: The Dragos Platform must have disk encryption enabled on a virtual machines (VMs).

**Rule ID:** `SV-270945r1107130_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling disk encryption on VMs running the Dragos Platform is a critical security measure to protect sensitive data, ensure compliance with regulations, and provide a robust defense against various threats, including unauthorized access, data breaches, and insider threats. Disk encryption ensures that the data stored on the VM's disk is unreadable to unauthorized users. This is crucial for protecting sensitive information, such as security logs, configurations, and other operational data, from being accessed if the disk is physically stolen or if unauthorized access is obtained. In the event of a security breach, encrypted disks prevent attackers from easily accessing the data stored on the VMs. This is particularly important for mitigating the risks associated with data breaches, including the potential exposure of sensitive operational technology (OT) and industrial control system (ICS) data. VMs can be snapshotted or cloned, creating exact copies of the VM, including its data. Disk encryption ensures that even if a snapshot or clone is made, the data remains protected and cannot be accessed without the appropriate decryption keys. Disk encryption protects data at rest, which is data stored on the disk when the system is not in use. This is a critical aspect of data security, as it ensures that the data remains protected even if the VM is powered off or in a dormant state. For organizations using both on-premises and cloud environments, disk encryption provides a consistent approach to data security. This helps maintain uniform security policies and practices across different infrastructure setups. In multi-tenant environments, where multiple virtual machines run on the same physical hardware, disk encryption ensures that data on one VM cannot be accessed by other tenants or compromised VMs on the same host.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If Dragos is running on an appliance, this check is Not Applicable. If the hypervisor is using full disk encryption, this check is Not Applicable. Check for disk encryption in a VM. Log into the VM and access the VM using remote access method, such as SSH. Use Built-in Tools or Commands: Linux: 1. Open a terminal window. 2. Use the following command to check if any encrypted partitions exist: lsblk -o NAME,FSTYPE,LABEL,UUID,SIZE,MOUNTPOINT,TYPE 3. Check for partitions with the filesystem type "crypto_LUKS" or similar. 4. Use the following command to list encrypted volumes: cryptsetup luksDump /dev/sdX (Replace /dev/sdX with the appropriate device name) If volumes are not encrypted, this is a finding.

## Group: SRG-APP-000133

**Group ID:** `V-270947`

### Rule: Dragos Platforms must limit privileges and not allow the ability to run shell.

**Rule ID:** `SV-270947r1058031_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If Dragos Platform were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to applications with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Satisfies: SRG-APP-000133, SRG-APP-000206, SRG-APP-000246, SRG-APP-000340, SRG-APP-000342, SRG-APP-000384</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify shell environment: Log in to the Dragos Platform CLI. Execute the following command: run shell If the option "run shell" executes successfully and places the terminal session into a shell environment, this is a finding. Note: A shell environment will be noticeable because the terminal line will be in the format "user@dragos:~$" compared to dragoscmd, which would be "dragos>". If shell is properly uninstalled, the return will be "Error: No such command 'shell'."

## Group: SRG-APP-000156

**Group ID:** `V-270952`

### Rule: Dragos must allow only the individuals appointed by the information system security manager (ISSM) to have full admin rights to the system.

**Rule ID:** `SV-270952r1057499_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without restricting which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the LDAP group name mapped to the admin role. Request from the LDAP administrator the group membership of this LDAP group, and compare to the list of individuals appointed by the ISSM. If users that are not defined by the ISSM as requiring admin rights are present in the admin role membership, this is a finding.

## Group: SRG-APP-000164

**Group ID:** `V-270955`

### Rule: The Dragos Platform must configure local password policies.

**Rule ID:** `SV-270955r1058011_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password. Satisfies: SRG-APP-000164, SRG-APP-000166, SRG-APP-000167, SRG-APP-000168, SRG-APP-000169, SRG-APP-000174</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check password configurations. In the UI, navigate to Admin >> SiteStore Management >> Authentication Providers. Click "EDIT" in the Local Authentication section. Verify the following settings: 1. Password Expiration is set to "2 months" or less. 2. Password Reuse Limit is set to "5" or less. 3. Minimum Length is set to "15" or greater. 4. Uppercase and lowercase letters is checked. 5. Special characters is checked. 6. Numeric characters is checked. If any settings are not configured correctly, this is a finding.

## Group: SRG-APP-000231

**Group ID:** `V-270978`

### Rule: Dragos must use FIPS-validated encryption and hashing algorithms to protect the confidentiality and integrity of application configuration files and user-generated data stored or aggregated on the device.

**Rule ID:** `SV-270978r1057577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Confidentiality and integrity protections are intended to address the confidentiality and integrity of system information at rest (e.g., network device rule sets) when it is located on a storage device within the network device or as a component of the network device. This protection is required to prevent unauthorized alteration, corruption, or disclosure of information when not stored directly on the network device. This requirement addresses protection of user-generated data as well as operating system-specific configuration data. Organizations may choose to employ different mechanisms to achieve confidentiality and integrity protections, as appropriate, in accordance with the security category and/or classification of the information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using Dragos hardware, this check is Not Applicable. In a virtual environment, check for FIPS-validated encryption: Check the documentation of the virtual environment being used (e.g., virtual machine software or cloud service provider documentation) to find out if it uses FIPS compliance or FIPS-validated encryption support. Check for configuration settings related to encryption algorithms and cryptographic modules in the virtual environment. Some platforms allow users to enable FIPS mode. Perform testing to ensure that only FIPS-approved cryptographic algorithms are being used within the virtual environment. This would involve testing encryption and decryption processes to confirm compliance with FIPS standards. If the virtual environment is not using FIPS-validated encryption or is not using FIPS compliance, this is a finding.

## Group: SRG-APP-000291

**Group ID:** `V-270993`

### Rule: The Dragos Platform must notify system administrators and information system security officer (ISSO) of local account activity.

**Rule ID:** `SV-270993r1058013_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to an application, the attacker often attempts to create a persistent method of re-establishing access. One way to accomplish this is for the attacker to simply create a new account. Sending notification of account creation events to the system administrator and ISSO is one method for mitigating this risk. Satisfies: SRG-APP-000291, SRG-APP-000292, SRG-APP-000293, SRG-APP-000294</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
While logged in to the Dragos Platform with a user account with administrative privileges, navigate to Admin >> User Management >> Users. Create a new user account (does not require roles or authentication). (Within 15 minutes) 1. Click the "Notifications" button. Verify a notification appears within Dragos Platform notifications page. If a notification does not occur, this is a finding. 2. Observe that the same notification appears in the aggregate server/syslog recipient. (Note: Depending on the software application used, steps to view syslog third-party alerts may vary.) If an alert is not being sent to third-party syslog, this is a finding. 3. Check Rules: Navigate to Notification >> RULES Tab. Verify a rule exists and has the following: Action = "Send Syslog (third-party server)" Criteria = "Detected By Equals Authentication to the Dragos Platform" "Detected By Equals User Account Activity" If a rule does not exist with the correct Action and Criteria, this is a finding. 4. Remove the test user just created.

## Group: SRG-APP-000357

**Group ID:** `V-271008`

### Rule: Dragos Platform must allocate audit record storage retention length.

**Rule ID:** `SV-271008r1057667_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure applications have a sufficient storage capacity in which to write the audit logs, applications need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial installation of Dragos Platform and is closely associated with the database administrator (DBA) and system administrator (SA) roles. The DBA or SA will usually coordinate the allocation of physical drive space with Dragos Platform owner/installer and Dragos Platform will prompt the installer to provide the capacity information, the physical location of the disk, or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the UI, navigate to Admin >> SiteStore Management >> Advanced Settings. Review the System Security Plan (SSP). Verify Deleted Retention Days and Source Data Retention Days is set accordance with organization-defined audit record storage requirements. If not, this is a finding.

## Group: SRG-APP-000383

**Group ID:** `V-271027`

### Rule: The Syslog client must use TCP connections.

**Rule ID:** `SV-271027r1057724_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Removal of unneeded or nonsecure functions, ports, protocols, and services mitigate the risk of unauthorized connection of devices, unauthorized transfer of information, or other exploitation of these resources. The organization must perform a periodic scan/review of Dragos (as required by CCI-000384) and disable functions, ports, protocols, and services deemed to be unneeded or nonsecure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the netstat command to display active UDP connections: netstat -n -p UDP If the syslog client is using a UDP connection, this is a finding.

## Group: SRG-APP-000402

**Group ID:** `V-271034`

### Rule: Dragos Platform must accept the DOD CAC or other PKI credential for identity management and personal authentication.

**Rule ID:** `SV-271034r1057745_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of Personal Identity Verification (PIV) credentials facilitates standardization and reduces the risk of unauthorized access. PIV credentials are those credentials issued by federal agencies that conform to FIPS Publication 201 and supporting guidance documents. OMB Memorandum 11-11 requires federal agencies to continue implementing the requirements specified in HSPD-12 to enable agency-wide use of PIV credentials. Satisfies: SRG-APP-000402, SRG-APP-000403, SRG-APP-000391, SRG-APP-000392, SRG-APP-000402, SRG-APP-000403, SRG-APP-000177, SRG-APP-000176, SRG-APP-000175, SRG-APP-000401</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Dragos is configured to use the DOD CAC or other PKI credential to log in to the application. Log in to the application. If DOD CAC or other PKI is not configured, this is a finding.

## Group: SRG-APP-000427

**Group ID:** `V-271049`

### Rule: The Dragos Platform must only allow the use of DOD PKI established certificate authorities for verification of the establishment of protected sessions.

**Rule ID:** `SV-271049r1057790_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DOD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DOD-approved CA, trust of this CA has not been established. The DOD will only accept PKI certificates obtained from a DOD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of TLS certificates. This requirement focuses on communications protection for Dragos Platform session rather than for the network packet. This requirement applies to applications that use communications sessions. This includes, but is not limited to, web-based applications and Service-Oriented Architectures (SOA). Satisfies: SRG-APP-000427, SRG-APP-000605</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open a web browser and navigate to the Dragos Platform UI. Locate the security or certificate status indicator at the address bar. Open the certificate information. If the certificate is signed by anyone other than DOD, PKI, or CA, this is a finding.

## Group: SRG-APP-000471

**Group ID:** `V-271070`

### Rule: The Dragos Platform must alert the information system security officer (ISSO), information system security manager (ISSM), and other individuals designated by the local organization when events are detected that indicate a compromise or potential for compromise.

**Rule ID:** `SV-271070r1107133_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a security event occurs, Dragos Platform must immediately notify the appropriate support personnel so they can respond appropriately. Alerts may be generated from a variety of sources, including audit records or inputs from malicious code protection mechanisms, intrusion detection mechanisms, or prevention mechanisms. IOCs are forensic artifacts from intrusions that are identified on organizational information systems (at the host or network level). IOCs provide organizations with valuable information on objects or information systems that have been compromised. These indicators reflect the occurrence of a compromise or a potential compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Check Server Configuration. If using Syslog Server: Verify third-party server is used to receive communication-related notifications. Check for a configured Syslog Server. In the UI, navigate to Admin >> Integrations. Click "LAUNCH" in the Syslog section. If no server is configured or the status is not "Connected", this is a finding. If no recipient is configured, this is a finding. 2. Check Rules: Navigate to Notification >> RULES Tab. Verify a rule exists and has the following: Action = "Send (<your syslog server>)" Criteria = "Notification Type Equals System" "Notification Type Equals System Failure" If a rule does not exist with the correct Action and Criteria, this is a finding.

## Group: SRG-APP-000570

**Group ID:** `V-271105`

### Rule: Before establishing a network connection with a Network Time Protocol (NTP) server, Dragos Platform must authenticate using a bidirectional, cryptographically based authentication method that uses a FIPS-validated Advanced Encryption Standard (AES) cipher block algorithm to authenticate with the NTP server.

**Rule ID:** `SV-271105r1057958_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without device-to-device authentication, communications with malicious devices may be established. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. Currently, DOD requires the use of AES for bidirectional authentication since it is the only FIPS-validated AES cipher block algorithm. The NTP uses MD5 authentication keys. The MD5 algorithm is not approved for use in either the FIPS or NIST recommendation; thus, a CAT 1 finding is allocated in CCI-000803. However, the use of MD5 is preferred to no authentication at all and can be used to mitigate this requirement to a CAT II finding. The trusted-key statement permits authenticating NTP servers. The product must be configured to support separate keys for each NTP server. Severs should have PKI device certificate involved for use in the device authentication process. Server authentication is performed by the client using the server's public key certificate, which the server presents during the handshake. The exact nature of the cryptographic operation for server authentication is dependent on the negotiated cipher suite and extensions. In most cases (e.g., RSA for key transport, DH, and ECDH), authentication is performed explicitly through verification of digital signatures present in certificates and implicitly by the use of the server public key by the client during the establishment of the master secret. A successful "Finished" message implies that both parties calculated the same master secret and thus, the server must have known the private key corresponding to the public key used for key establishment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NTP Server. Log in to the Dragos Platform CLI. Execute the following command: config show If an NTP server is configured, the following will be in the output. If the following is not in the output, this is a finding. (Note: "servers" will be the configured server.) "system": { "ntp": { "enabled": true, "servers": [ "pool.ntp.org" ] } }

