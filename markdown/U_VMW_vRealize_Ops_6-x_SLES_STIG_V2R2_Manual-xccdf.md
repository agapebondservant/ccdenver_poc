# STIG Benchmark: VMware vRealize Operations Manager 6.x SLES Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000001-GPOS-00001

**Group ID:** `V-239441`

### Rule: The SLES for vRealize must provide automated mechanisms for supporting account management functions.

**Rule ID:** `SV-239441r661774_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enterprise environments make account management challenging and complex. A manual process for account management functions adds the risk of a potential oversight or other errors. A comprehensive account management process that includes automation helps to ensure accounts designated as requiring attention are consistently and promptly addressed. Examples include, but are not limited to, using automation to take action on multiple accounts designated as inactive, suspended, or terminated, or by disabling accounts located in non-centralized account stores such as multiple servers. This requirement applies to all account types, including individual/user, shared, group, system, guest/anonymous, emergency, developer/manufacturer/vendor, temporary, and service. The automated mechanisms may reside within the SLES for vRealize itself or may be offered by other infrastructure providing automated account management capabilities. Automated mechanisms may be composed of differing technologies that, when placed together, contain an overall automated mechanism supporting an organization's automated account management requirements. Account management functions include: assigning group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. The use of automated mechanisms can include, for example: using email or text messaging to automatically notify account managers when users are terminated or transferred; using the information system to monitor account usage; and using automated telephonic notification to report atypical system account usage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the server admin to determine if there is automated mechanisms for managing user accounts. If there is not, this is a finding.

## Group: SRG-OS-000002-GPOS-00002

**Group ID:** `V-239442`

### Rule: The SLES for vRealize must automatically remove or disable temporary user accounts after 72 hours.

**Rule ID:** `SV-239442r661777_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If temporary user accounts remain active when no longer needed or for an excessive period, these accounts may be used to gain unauthorized access. To mitigate this risk, automated termination of all temporary accounts must be set upon account creation. Temporary accounts are established as part of normal account activation procedures when there is a need for short-term accounts without the demand for immediacy in account activation. If temporary accounts are used, the SLES for vRealize must be configured to automatically terminate these types of accounts after a DoD-defined time period of 72 hours. To address access requirements, many SLES for vRealize operating systems may be integrated with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For every existing temporary account, run the following command to obtain its account expiration information. # chage -l system_account_name Verify each of these accounts has an expiration date set within "72" hours. If any temporary accounts have no expiration date set or do not expire within "72" hours, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-239443`

### Rule: The SLES for vRealize must audit all account creations.

**Rule ID:** `SV-239443r661780_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply create a new account. Auditing of account creation mitigates this risk. To address access requirements, many SLES for vRealize operating systems may be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if execution of the useradd and groupadd executable are audited. # auditctl -l | egrep '(useradd|groupadd)' If either "useradd" or "groupadd" are not listed with a permissions filter of at least "x", this is a finding. Expected result: LIST_RULES: exit,always watch=/usr/sbin/useradd perm=x key=useradd LIST_RULES: exit,always watch=/usr/sbin/groupadd perm=x key=groupadd

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-239444`

### Rule: In addition to auditing new user and group accounts, these watches will alert the system administrator(s) to any modifications, any unexpected users, groups, or modifications must be investigated for legitimacy.

**Rule ID:** `SV-239444r661783_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply create a new account. Auditing of account creation mitigates this risk. To address access requirements, many SLES for vRealize operating systems may be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if /etc/passwd, /etc/shadow, /etc/group, and /etc/gshadow are audited for appending. # auditctl -l | egrep '(/etc/passwd|/etc/shadow|/etc/group|/etc/gshadow)' | grep perm=a If the "passwd", "shadow", "group", and "gshadow" files are not listed with a permissions filter of at least "a", this is a finding. Expected result: LIST_RULES: exit,always watch=/etc/passwd perm=a key=passwd LIST_RULES: exit,always watch=/etc/shadow perm=a key=shadow LIST_RULES: exit,always watch=/etc/group perm=a key=group LIST_RULES: exit,always watch=/etc/gshadow perm=a key=gshadow

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-239445`

### Rule: The SLES for vRealize must enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period.

**Rule ID:** `SV-239445r661786_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to ensure that the SLES for vRealize enforces the limit of "3" consecutive invalid logon attempts by a user: # grep pam_tally2.so /etc/pam.d/common-auth The output should contain "deny=3" in the returned line. If the output does not contain "deny=3", this is a finding. Expected Result: auth required pam_tally2.so deny=3 onerr=fail even_deny_root unlock_time=86400 root_unlock_time=300

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-239446`

### Rule: The SLES for vRealize must display the Standard Mandatory DoD Notice and Consent Banner before granting access via SSH.

**Rule ID:** `SV-239446r661789_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the SLES for vRealize ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for SLES for vRealize systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for SLES for vRealize systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that the SSH daemon is configured for logon warning banners: # grep -i banner /etc/ssh/sshd_config | grep -v '#' The output should contain "Banner /etc/issue". If the output does not contain "Banner /etc/issue", this is a finding.

## Group: SRG-OS-000027-GPOS-00008

**Group ID:** `V-239447`

### Rule: The SLES for vRealize must limit the number of concurrent sessions to ten for all accounts and/or account types.

**Rule ID:** `SV-239447r877399_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Operating system management includes the ability to control the number of users and user sessions that utilize an operating system. Limiting the number of allowed users and sessions per user is helpful in reducing the risks related to DoS attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SLES for vRealize limits the number of concurrent sessions to "10" for all accounts and/or account types with the following command: # grep maxlogins /etc/security/limits.conf | grep -v '#' The default maxlimits should be set to a max of "10" or a documented site defined number: * hard maxlogins 10 If the default maxlimits is not set to "10" or the documented site defined number, this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-239448`

### Rule: The SLES for vRealize must initiate a session lock after a 15-minute period of inactivity for all connection types.

**Rule ID:** `SV-239448r661795_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, SLES for vRealize needs to be able to identify when a user's session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for the existence of the /etc/profile.d/tmout.sh file: # ls -al /etc/profile.d/tmout.sh Check for the presence of the "TMOUT" variable: # grep TMOUT /etc/profile.d/tmout.sh The value of "TMOUT" should be set to 900 seconds (15 minutes). If the file does not exist, or the "TMOUT" variable is not set, this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-239449`

### Rule: The SLES for vRealize must initiate a session lock after a 15-minute period of inactivity for an SSH connection.

**Rule ID:** `SV-239449r661798_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, SLES for vRealize needs to be able to identify when a user's session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLES for vRealize initiates a session lock after a 15-minute period of inactivity for SSH. Execute the following command: # grep ClientAliveInterval /etc/ssh/sshd_config; grep ClientAliveCountMax /etc/ssh/sshd_config Verify the following result: ClientAliveInterval 900 ClientAliveCountMax 0 If the session lock is not set to a 15-minute period, this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-239450`

### Rule: The SLES for vRealize must monitor remote access methods - SSH Daemon.

**Rule ID:** `SV-239450r661801_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyber attacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSH is configured to verbosely log connection attempts and failed logon attempts to the server by running the following command: # grep LogLevel /etc/ssh/sshd_config | grep -v '#' The output message must contain the following text: LogLevel VERBOSE If it is not set to "VERBOSE", this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-239451`

### Rule: The SLES for vRealize must implement DoD-approved encryption to protect the confidentiality of remote access sessions - SSH Daemon.

**Rule ID:** `SV-239451r877398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection (e.g., RDP), thereby providing a degree of confidentiality. The encryption strength of a mechanism is selected based on the security categorization of the information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for DoD-approved encryption to protect the confidentiality of SSH remote connections by performing the following commands: Check the Cipher setting in the sshd_config file. # grep -i Ciphers /etc/ssh/sshd_config | grep -v '#' The output must contain either none or any number of the following algorithms: aes128-ctr, aes256-ctr. If the output contains an algorithm not listed above, this is a finding. Expected Output: Ciphers aes256-ctr,aes128-ctr

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-239452`

### Rule: The SLES for vRealize must implement DoD-approved encryption to protect the confidentiality of remote access sessions - SSH Client.

**Rule ID:** `SV-239452r877398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection (e.g., RDP), thereby providing a degree of confidentiality. The encryption strength of a mechanism is selected based on the security categorization of the information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for DoD-approved encryption to protect the confidentiality of SSH remote connections by performing the following commands: Check the Cipher setting in the ssh_config file. # grep -i Ciphers /etc/ssh/ssh_config | grep -v '#' The output must contain either none or any number of the following algorithms: aes256-ctr,aes128-ctr. If the output contains an algorithm not listed above, this is a finding. Expected Output: Ciphers aes256-ctr,aes128-ctr

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-239453`

### Rule: The SLES for vRealize must produce audit records.

**Rule ID:** `SV-239453r661810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in the SLES for vRealize audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLES for vRealize produces audit records by running the following command to determine the current status of the "auditd" service: # service auditd status If the service is enabled, the returned message must contain the following text: Checking for: service auditd running If the service is not running, this is a finding.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-239454`

### Rule: The SLES for vRealize must alert the ISSO and SA (at a minimum) in the event of an audit processing failure.

**Rule ID:** `SV-239454r661813_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check /etc/audit/auditd.conf for the "space_left_action" with the following command: # cat /etc/audit/auditd.conf | grep space_left_action If the "space_left_action" parameter is missing, set to "ignore", set to "suspend", set to "single", set to "halt", or is blank, this is a finding. Expected Result: space_left_action = SYSLOG Notes: If the space_left_action is set to "exec" the system executes a designated script. If this script informs the SA of the event, this is not a finding. If the space_left_action is set to "email" and the "action_mail_acct" parameter is not set to the email address of the system administrator, this is a finding. The "action_mail_acct" parameter, if missing, defaults to "root". Note: If the email address of the system administrator is on a remote system "sendmail" must be available.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-239455`

### Rule: The SLES for vRealize must shut down by default upon audit failure (unless availability is an overriding concern).

**Rule ID:** `SV-239455r661816_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the SLES for vRealize is at risk of failing to process audit logs as required, it takes action to mitigate the failure. Audit processing failures include: software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When availability is an overriding concern, other approved actions in response to an audit failure are as follows: 1) If the failure was caused by the lack of audit record storage capacity, the operating system must continue generating audit records if possible (automatically restarting the audit service if necessary), overwriting the oldest audit records in a first-in-first-out manner. 2) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, SLES for vRealize must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the /etc/audit/auditd.conf has the "disk_full_action", "disk_error_action", and "admin_disk_space_left" parameters set. # grep disk_full_action /etc/audit/auditd.conf If the "disk_full_action" parameter is missing or set to "suspend" or "ignore", this is a finding. # grep disk_error_action /etc/audit/auditd.conf If the "disk_error_action" parameter is missing or set to "suspend" or "ignore", this is a finding. # grep admin_space_left_action /etc/audit/auditd.conf If the "admin_space_left_action" parameter is missing or set to "suspend" or "ignore", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-239456`

### Rule: The SLES for vRealize must protect audit information from unauthorized read access - ownership.

**Rule ID:** `SV-239456r661819_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit SLES for vRealize activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SLES for vRealize audit logs are owned by "root". # (audit_log_file=$(grep "^log_file" /etc/audit/auditd.conf|sed s/^[^\/]*//) && if [ -f "${audit_log_file}" ] ; then printf "Log(s) found in "${audit_log_file%/*}":\n"; ls -l ${audit_log_file%/*}; else printf "audit log file(s) not found\n"; fi) If any audit log file is not owned by "root" or "admin", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-239457`

### Rule: The SLES for vRealize must protect audit information from unauthorized read access - group ownership.

**Rule ID:** `SV-239457r661822_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit SLES for vRealize activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SLES for vRealize audit logs are group-owned by "root". # (audit_log_file=$(grep "^log_file" /etc/audit/auditd.conf|sed s/^[^\/]*//) && if [ -f "${audit_log_file}" ] ; then printf "Log(s) found in "${audit_log_file%/*}":\n"; ls -l ${audit_log_file%/*}; else printf "audit log file(s) not found\n"; fi) If any audit log file is not group-owned by "root" or "admin", this is a finding.

## Group: SRG-OS-000058-GPOS-00028

**Group ID:** `V-239458`

### Rule: The SLES for vRealize must protect audit information from unauthorized modification.

**Rule ID:** `SV-239458r661825_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit information were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit information, the SLES for vRealize must protect audit information from unauthorized modification. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit information system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that the SLES for vRealize audit logs with the following command: # (audit_log_file=$(grep "^log_file" /etc/audit/auditd.conf|sed s/^[^\/]*//) && if [ -f "${audit_log_file}" ] ; then printf "Log(s) found in "${audit_log_file%/*}":\n"; ls -l ${audit_log_file%/*}; else printf "audit log file(s) not found\n"; fi) If any audit log file has a mode more permissive than "0640", this is a finding.

## Group: SRG-OS-000059-GPOS-00029

**Group ID:** `V-239459`

### Rule: The SLES for vRealize must protect audit information from unauthorized deletion.

**Rule ID:** `SV-239459r661828_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit information were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit information, the SLES for vRealize must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit information system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that the SLES for vRealize audit logs with the following command: # (audit_log_file=$(grep "^log_file" /etc/audit/auditd.conf|sed s/^[^\/]*//) && if [ -f "${audit_log_file}" ] ; then printf "Log(s) found in "${audit_log_file%/*}":\n"; ls -l ${audit_log_file%/*}; else printf "audit log file(s) not found\n"; fi) If any audit log file has a mode more permissive than "0640", this is a finding.

## Group: SRG-OS-000059-GPOS-00029

**Group ID:** `V-239460`

### Rule: The SLES for vRealize must protect audit information from unauthorized deletion - log directories.

**Rule ID:** `SV-239460r661831_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit information were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit information, the SLES for vRealize must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit information system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to check the mode of the system audit directories: # grep "^log_file" /etc/audit/auditd.conf|sed 's/^[^/]*//; s/[^/]*$//'|xargs stat -c %a:%n Audit directories must be mode "0700". If the audit directories is not set to mode "0700", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-239474`

### Rule: The SLES for vRealize must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited - Permissions.

**Rule ID:** `SV-239474r661873_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the rules files in /etc/audit: # ls -l /etc/audit/ Note: If /etc/audit/audit.rules is a symbolic link to /etc/audit/audit.rules.STIG, then the check is only applicable to /etc/audit/audit.rules.STIG. If the permissions of the file is not set to "640", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-239475`

### Rule: The SLES for vRealize must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited - ownership.

**Rule ID:** `SV-239475r661876_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the rules files in /etc/audit: # ls -l /etc/audit/ Note: If /etc/audit/audit.rules is a symbolic link to /etc/audit/audit.rules.STIG, then the check is only applicable to /etc/audit/audit.rules.STIG. If the ownership is not set to "root", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-239476`

### Rule: The SLES for vRealize must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited - group ownership.

**Rule ID:** `SV-239476r661879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the rules files in /etc/audit: # ls -l /etc/audit/ Note: If /etc/audit/audit.rules is a symbolic link to /etc/audit/audit.rules.STIG, then the check is only applicable to /etc/audit/audit.rules.STIG. If the group owner is not set to "root", this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-239477`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to access privileges occur. The operating system must generate audit records for all discretionary access control permission modifications using chmod.

**Rule ID:** `SV-239477r661882_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine if the system is configured to audit calls to the "chmod" system call, run the following command: # auditctl -l | grep syscall | grep chmod If the system is configured to audit this activity, it will return several lines, such as: LIST_RULES: exit,always arch=3221225534 (0xc000003e) auid=0 syscall=chmod,fchmod,chown,fchown,fchownat,fchmodat LIST_RULES: exit,always arch=3221225534 (0xc000003e) auid>=500 (0x1f4) auid!=-1 (0xffffffff) syscall=chmod,fchmod,chown,fchown,fchownat,fchmodat If no lines are returned, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-239478`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to access privileges occur. The SLES for vRealize must generate audit records for all discretionary access control permission modifications using chown.

**Rule ID:** `SV-239478r661885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine if the SLES for vRealize is configured to audit calls to the "chown" system call, run the following command: # auditctl -l | grep syscall | grep chown If the SLES for vRealize is configured to audit this activity, it will return several lines, such as: LIST_RULES: exit,always arch=3221225534 (0xc000003e) auid=0 syscall=chmod,fchmod,chown,fchown,fchownat,fchmodat LIST_RULES: exit,always arch=3221225534 (0xc000003e) auid>=500 (0x1f4) auid!=-1 (0xffffffff) syscall=chmod,fchmod,chown,fchown,fchownat,fchmodat If no lines are returned, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-239479`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to access privileges occur. The SLES for vRealize must generate audit records for all discretionary access control permission modifications using fchmod.

**Rule ID:** `SV-239479r661888_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine if SLES for vRealize is configured to audit calls to the "fchmod" system call, run the following command: # auditctl -l | grep syscall | grep fchmod If SLES for vRealize is configured to audit this activity, it will return several lines, such as: LIST_RULES: exit,always arch=3221225534 (0xc000003e) auid=0 syscall=chmod,fchmod,chown,fchown,fchownat,fchmodat LIST_RULES: exit,always arch=3221225534 (0xc000003e) auid>=500 (0x1f4) auid!=-1 (0xffffffff) syscall=chmod,fchmod,chown,fchown,fchownat,fchmodat If no lines are returned, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-239480`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to access privileges occur. The SLES for vRealize must generate audit records for all discretionary access control permission modifications using fchmodat.

**Rule ID:** `SV-239480r661891_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine if SLES for vRealize is configured to audit calls to the "fchmodat" system call, run the following command: # auditctl -l | grep syscall | grep fchmodat If SLES for vRealize is configured to audit this activity, it will return several lines, such as: LIST_RULES: exit,always arch=3221225534 (0xc000003e) auid=0 syscall=chmod,fchmod,chown,fchown,fchownat,fchmodat LIST_RULES: exit,always arch=3221225534 (0xc000003e) auid>=500 (0x1f4) auid!=-1 (0xffffffff) syscall=chmod,fchmod,chown,fchown,fchownat,fchmodat If no lines are returned, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-239481`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to access privileges occur. The SLES for vRealize must generate audit records for all discretionary access control permission modifications using fchown.

**Rule ID:** `SV-239481r661894_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine if SLES for vRealize is configured to audit calls to the "fchown" system call, run the following command: # auditctl -l | grep syscall | grep fchown If SLES for vRealize is configured to audit this activity, it will return several lines, such as: LIST_RULES: exit,always arch=3221225534 (0xc000003e) auid=0 syscall=chmod,fchmod,chown,fchown,fchownat,fchmodat LIST_RULES: exit,always arch=3221225534 (0xc000003e) auid>=500 (0x1f4) auid!=-1 (0xffffffff) syscall=chmod,fchmod,chown,fchown,fchownat,fchmodat If no lines are returned, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-239482`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to access privileges occur. The SLES for vRealize must generate audit records for all discretionary access control permission modifications using fchownat.

**Rule ID:** `SV-239482r661897_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine if SLES for vRealize is configured to audit calls to the "fchownat" system call, run the following command: # auditctl -l | grep syscall | grep fchownat If SLES for vRealize is configured to audit this activity, it will return several lines, such as: LIST_RULES: exit,always arch=3221225534 (0xc000003e) auid=0 syscall=chmod,fchmod,chown,fchown,fchownat,fchmodat LIST_RULES: exit,always arch=3221225534 (0xc000003e) auid>=500 (0x1f4) auid!=-1 (0xffffffff) syscall=chmod,fchmod,chown,fchown,fchownat,fchmodat If no lines are returned, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-239483`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to access privileges occur. The SLES for vRealize must generate audit records for all discretionary access control permission modifications using fremovexattr.

**Rule ID:** `SV-239483r661900_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine if SLES for vRealize is configured to audit calls to the "fremovexattr" system call, run the following command: # auditctl -l | grep syscall | grep fremovexattr If SLES for vRealize is configured to audit this activity, it will return several lines, such as: LIST_RULES: exit,always arch=3221225534 (0xc000003e) syscall=lchown,sethostname,init_module,delete_module,setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr,clock_settime If no lines are returned, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-239484`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to access privileges occur. The SLES for vRealize must generate audit records for all discretionary access control permission modifications using fsetxattr.

**Rule ID:** `SV-239484r661903_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine if SLES for vRealize is configured to audit calls to the "fsetxattr" system call, run the following command: # auditctl -l | grep syscall | grep fsetxattr If SLES for vRealize is configured to audit this activity, it will return several lines, such as: LIST_RULES: exit,always arch=3221225534 (0xc000003e) syscall=lchown,sethostname,init_module,delete_module,setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr,clock_settime If no lines are returned, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-239485`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to access privileges occur. The SLES for vRealize must generate audit records for all discretionary access control permission modifications using lchown.

**Rule ID:** `SV-239485r661906_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine if SLES for vRealize is configured to audit calls to the "lchown" system call, run the following command: # auditctl -l | grep syscall | grep lchown If SLES for vRealize is configured to audit this activity, it will return several lines, such as: LIST_RULES: exit,always arch=3221225534 (0xc000003e) syscall=lchown,sethostname,init_module,delete_module,setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr,clock_settime If no lines are returned, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-239486`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to access privileges occur. The SLES for vRealize must generate audit records for all discretionary access control permission modifications using lremovexattr.

**Rule ID:** `SV-239486r661909_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine if SLES for vRealize is configured to audit calls to the "lremovexattr" system call, run the following command: # auditctl -l | grep syscall | grep lremovexattr If SLES for vRealize is configured to audit this activity, it will return several lines, such as: LIST_RULES: exit,always arch=3221225534 (0xc000003e) syscall=lchown,sethostname,init_module,delete_module,setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr,clock_settime If no lines are returned, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-239487`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to access privileges occur. The SLES for vRealize must generate audit records for all discretionary access control permission modifications using lsetxattr.

**Rule ID:** `SV-239487r661912_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine if SLES for vRealize is configured to audit calls to the "lsetxattr" system call, run the following command: # auditctl -l | grep syscall | grep lsetxattr If SLES for vRealize is configured to audit this activity, it will return several lines, such as: LIST_RULES: exit,always arch=3221225534 (0xc000003e) syscall=lchown,sethostname,init_module,delete_module,setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr,clock_settime If no lines are returned, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-239488`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to access privileges occur. The SLES for vRealize must generate audit records for all discretionary access control permission modifications using removexattr.

**Rule ID:** `SV-239488r661915_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine if SLES for vRealize is configured to audit calls to the "removexattr" system call, run the following command: # auditctl -l | grep syscall | grep removexattr If SLES for vRealize is configured to audit this activity, it will return several lines, such as: LIST_RULES: exit,always arch=3221225534 (0xc000003e) syscall=lchown,sethostname,init_module,delete_module,setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr,clock_settime If no lines are returned, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-239489`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to access privileges occur. The SLES for vRealize must generate audit records for all discretionary access control permission modifications using setxattr.

**Rule ID:** `SV-239489r661918_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine if SLES for vRealize is configured to audit calls to the "setxattr" system call, run the following command: # auditctl -l | grep syscall | grep setxattr If SLES for vRealize is configured to audit this activity, it will return several lines, such as: LIST_RULES: exit,always arch=3221225534 (0xc000003e) syscall=lchown,sethostname,init_module,delete_module,setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr,clock_settime If no lines are returned, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-239490`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to access privileges occur. The SLES for vRealize must generate audit records for all failed attempts to access files and programs.

**Rule ID:** `SV-239490r661921_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To check that the SLES for vRealize audit system collects unauthorized file accesses, run the following commands: # grep EACCES /etc/audit/audit.rules -a exit,always -F arch=b64 -S swapon -F exit=-EACCES -a exit,always -F arch=b64 -S creat -F exit=-EACCES -a exit,always -F arch=b64 -S open -F exit=-EACCES # grep EPERM /etc/audit/audit.rules -a exit,always -F arch=b64 -S swapon -F exit=-EPERM -a exit,always -F arch=b64 -S creat -F exit=-EPERM -a exit,always -F arch=b64 -S open -F exit=-EPERM If either command lacks output, this is a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-239491`

### Rule: The SLES for vRealize must enforce password complexity by requiring that at least one upper-case character be used.

**Rule ID:** `SV-239491r661924_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check SLES for vRealize enforces password complexity by requiring that at least one upper-case character be used by using the following command: # grep ucredit /etc/pam.d/common-password-vmware.local If "ucredit" is not set to "-1" or not at all, this is a finding. Expected Result: password requisite pam_cracklib.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=14 difok=4 retry=3

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-239492`

### Rule: Global settings defined in common- {account,auth,password,session} must be applied in the pam.d definition files.

**Rule ID:** `SV-239492r661927_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Pam global requirements are generally defined in the common-account, common-auth, common- password and common-session files located in the /etc/pam.d directory. In order for the requirements to be applied the file(s) containing them must be included directly or indirectly in each program's definition file in /etc/pam.d.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that common-{account, auth, password, session} settings are being applied: Verify that local customization has occurred in the common- {account,auth,password,session}-pc file(s) by some method other than the use of the pam-config utility. The files "/etc/pam.d/common-{account,auth,password,session} -pc" are autogenerated by "pam-config". Any manual changes made to them will be lost if "pam-config" is allowed to run. # ls -l /etc/pam.d/common-{account,auth,password,session} If the symlinks point to "/etc/pam.d/common- {account,auth,password,session}-pc" and manual updates have been made in these files, the updates cannot be protected if pam-config is enabled. # ls -l /usr/sbin/pam-config If the setting for pam-config is not "000", this is a finding.

## Group: SRG-OS-000070-GPOS-00038

**Group ID:** `V-239493`

### Rule: The SLES for vRealize must enforce password complexity by requiring that at least one lower-case character be used.

**Rule ID:** `SV-239493r661930_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLES for vRealize enforces password complexity by requiring that at least one lower-case character be used by using the following command: # grep lcredit /etc/pam.d/common-password-vmware.local If "lcredit" is not set to "-1" or not at all, this is a finding. Expected Result: password requisite pam_cracklib.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=14 difok=4 retry=3

## Group: SRG-OS-000071-GPOS-00039

**Group ID:** `V-239494`

### Rule: The SLES for vRealize must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-239494r661933_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that SLES for vRealize enforces password complexity by requiring that at least one numeric character be used by running the following command: # grep dcredit /etc/pam.d/common-password-vmware.local If "dcredit" is not set to "-1" or not at all, this is a finding. Expected Result: password requisite pam_cracklib.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=14 difok=4 retry=3

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-239495`

### Rule: The SLES for vRealize must require the change of at least eight of the total number of characters when passwords are changed.

**Rule ID:** `SV-239495r661936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> If the operating system allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that at least eight characters need to be changed between old and new passwords during a password change by running the following command: # grep pam_cracklib /etc/pam.d/common-password-vmware.local The "difok" parameter indicates how many characters must be different. The DoD requires at least eight characters to be different during a password change. This would appear as "difok=8". If "difok" is not found or not set to at least "8", this is a finding. Expected Result: password requisite pam_cracklib.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=14 difok=8 retry=3

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-239496`

### Rule: The SLES for vRealize must store only encrypted representations of passwords.

**Rule ID:** `SV-239496r877397_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that the user account passwords are stored hashed using sha512 by running the following command: # cat /etc/default/passwd | grep CRYPT=sha512 If "CRYPT=sha512" is not listed, this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-239497`

### Rule: SLES for vRealize must enforce 24 hours/1 day as the minimum password lifetime.

**Rule ID:** `SV-239497r661942_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To check that SLES for vRealize enforces 24 hours/1 day as the minimum password age, run the following command: # grep PASS_MIN_DAYS /etc/login.defs | grep -v '#' The DoD requirement is "1". If "PASS_MIN_DAYS" is not set to the required value, this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-239498`

### Rule: Users must not be able to change passwords more than once every 24 hours.

**Rule ID:** `SV-239498r661945_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the minimum time period between password changes for each user account is "1" day. # cat /etc/shadow | cut -d ':' -f1,4 | grep -v 1 | grep -v ":$" If any results are returned, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-239499`

### Rule: SLES for vRealize must enforce a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-239499r661948_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If SLES for vRealize does not limit the lifetime of passwords and force users to change their passwords, there is the risk that SLES for vRealize passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To check that SLES for vRealize enforces a "60" days or less maximum password age, run the following command: # grep PASS_MAX_DAYS /etc/login.defs | grep -v "#" The DoD requirement is "60" days or less (Greater than zero, as zero days will lock the account immediately). If "PASS_MAX_DAYS" is not set to the required value, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-239500`

### Rule: User passwords must be changed at least every 60 days.

**Rule ID:** `SV-239500r661951_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If SLES for vRealize does not limit the lifetime of passwords and force users to change their passwords, there is the risk that SLES for vRealize passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the max days field of "/etc/shadow" by running the following command: # cat /etc/shadow | cut -d':' -f1,5 | egrep -v "([0|60])" | grep -v ":$" If any results are returned, this is a finding.

## Group: SRG-OS-000077-GPOS-00045

**Group ID:** `V-239501`

### Rule: The SLES for vRealize must prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-239501r661954_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLES for vRealize prohibits the reuse of a password for a minimum of five generations, by running the following commands: # grep pam_pwhistory.so /etc/pam.d/common-password-vmware.local If the "remember" option in "/etc/pam.d/common-password-vmware.local" file is not "5" or greater, this is a finding.

## Group: SRG-OS-000077-GPOS-00045

**Group ID:** `V-239502`

### Rule: The SLES for vRealize must prohibit password reuse for a minimum of five generations. Ensure the old passwords are being stored.

**Rule ID:** `SV-239502r661957_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the old password file, "opasswd", exists, by running the following command: # ls /etc/security/opasswd If "/etc/security/opasswd" file does not exist, this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-239503`

### Rule: The SLES for vRealize must enforce a minimum 15-character password length.

**Rule ID:** `SV-239503r661960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLES for vRealize enforces a minimum 15-character password length, by running the following command: # grep pam_cracklib /etc/pam.d/common-password-vmware.local # grep pam_cracklib /etc/pam.d/common-password If the result does not contain "minlen=15" or higher, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-239504`

### Rule: The SLES for vRealize must require root password authentication upon booting into single-user mode.

**Rule ID:** `SV-239504r661963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that root password is required for single user mode logon with the following command: # grep sulogin /etc/inittab Expected result: ~~:S:respawn:/sbin/sulogin If the expected result is not displayed, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-239505`

### Rule: Bootloader authentication must be enabled to prevent users without privilege to gain access restricted file system resources.

**Rule ID:** `SV-239505r661966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify a boot password exists. In "/boot/grub/menu.lst" run the following command: # grep password /boot/grub/menu.lst The output should show the following: password --encrypted $1$[rest-of-the-password-hash] If it does not, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-239506`

### Rule: The SLES for the vRealize boot loader configuration file(s) must have mode 0600 or less permissive.

**Rule ID:** `SV-239506r661969_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>File permissions more permissive than 0600 on boot loader configuration files could allow an unauthorized user to view or modify sensitive information pertaining to system boot instructions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the /boot/grub/menu.lst file: # stat /boot/grub/menu.lst If "/boot/grub/menu.lst" has a mode more permissive than "0600", this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-239507`

### Rule: The SLES for the vRealize boot loader configuration files must be owned by root.

**Rule ID:** `SV-239507r661972_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The SLES for vRealize’s boot loader configuration files are critical to the integrity of the system and must be protected. Unauthorized modification of these files resulting from improper ownership could compromise the system's boot loader configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check "/boot/grub/menu.lst" file ownership: # stat /boot/grub/menu.lst If the owner of the file is not "root", this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-239508`

### Rule: The SLES for the vRealize boot loader configuration file(s) must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-239508r661975_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The SLES for vRealize’s boot loader configuration files are critical to the integrity of the system and must be protected. Unauthorized modifications resulting from improper group ownership may compromise the boot loader configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check "/boot/grub/menu.lst" file ownership: # stat /boot/grub/menu.lst If the group-owner of the file is not "root", "bin", "sys", or "system", this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-239509`

### Rule: The Bluetooth protocol handler must be disabled or not installed.

**Rule ID:** `SV-239509r661978_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Bluetooth is a personal area network (PAN) technology. Binding this protocol to the network stack increases the attack surface of the host. Unprivileged local processes may be able to cause the kernel to dynamically load a protocol handler by opening a socket using the protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Bluetooth protocol handler is prevented from dynamic loading: # grep "install bluetooth /bin/true" /etc/modprobe.conf /etc/modprobe.conf.local /etc/modprobe.d/* If no result is returned, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-239510`

### Rule: The SLES for vRealize must have USB Mass Storage disabled unless needed.

**Rule ID:** `SV-239510r661981_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>USB is a common computer peripheral interface. USB devices may include storage devices that could be used to install malicious software on a system or exfiltrate data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If SLES for vRealize needs USB storage, this vulnerability is not applicable. Check if the "usb-storage" module is prevented from loading: # grep "install usb-storage /bin/true" /etc/modprobe.conf /etc/modprobe.conf.local /etc/modprobe.d/* If no results are returned, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-239511`

### Rule: The SLES for vRealize must have USB disabled unless needed.

**Rule ID:** `SV-239511r661984_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>USB is a common computer peripheral interface. USB devices may include storage devices that could be used to install malicious software on a system or exfiltrate data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If SLES for vRealize needs USB, this vulnerability is not applicable. Check if the directory "/proc/bus/usb exists". If the directory "/proc/bus/usb exists", this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-239512`

### Rule: The telnet-server package must not be installed.

**Rule ID:** `SV-239512r661987_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Removing the "telnet-server" package decreases the risk of the unencrypted telnet service's accidental (or intentional) activation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if "telnet-server" package is installed: # rpm -q telnet-server If there is a "telnet-server" package listed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-239513`

### Rule: The rsh-server package must not be installed.

**Rule ID:** `SV-239513r661990_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "rsh-server" package provides several obsolete and insecure network services. Removing it decreases the risk of those services' accidental (or intentional) activation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if "rsh-server" package is installed: # rpm -q rsh-server If there is a "rsh-server" package listed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-239514`

### Rule: The ypserv package must not be installed.

**Rule ID:** `SV-239514r661993_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Removing the "ypserv" package decreases the risk of the accidental (or intentional) activation of NIS or NIS+ services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if "ypserv" package is installed: # rpm -q ypserv If there is a "ypserv" package listed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-239515`

### Rule: The yast2-tftp-server package must not be installed.

**Rule ID:** `SV-239515r661996_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Removing the "yast2-tftp-server" package decreases the risk of the accidental (or intentional) activation of tftp services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if "yast2-tftp-server" package is installed: # rpm -q yast2-tftp-server If there is a "yast2-tftp-server" package listed, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239516`

### Rule: The Datagram Congestion Control Protocol (DCCP) must be disabled unless required.

**Rule ID:** `SV-239516r661999_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Datagram Congestion Control Protocol (DCCP) is a proposed transport layer protocol. This protocol is not yet widely used. Binding this protocol to the network stack increases the attack surface of the host. Unprivileged local processes may be able to cause the kernel to dynamically load a protocol handler by opening a socket using the protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that the DCCP protocol handler is prevented from dynamic loading: # grep "install dccp /bin/true" /etc/modprobe.conf /etc/modprobe.conf.local /etc/modprobe.d/* If no result is returned, this is a finding. # grep "install dccp_ipv4 /bin/true" /etc/modprobe.conf /etc/modprobe.conf.local /etc/modprobe.d/* If no result is returned, this is a finding. # grep "install dccp_ipv6" /etc/modprobe.conf /etc/modprobe.conf.local /etc/modprobe.d/* | grep ‘bin/true’ If no result is returned, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239517`

### Rule: The Stream Control Transmission Protocol (SCTP) must be disabled unless required.

**Rule ID:** `SV-239517r662002_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Stream Control Transmission Protocol (SCTP) is an IETF-standardized transport layer protocol. This protocol is not yet widely used. Binding this protocol to the network stack increases the attack surface of the host. Unprivileged local processes may be able to cause the kernel to dynamically load a protocol handler by opening a socket using the protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SCTP protocol handler is prevented from dynamic loading: # grep "install sctp /bin/true" /etc/modprobe.conf /etc/modprobe.conf.local /etc/modprobe.d/* If no result is returned, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239518`

### Rule: The Reliable Datagram Sockets (RDS) protocol must be disabled or not installed unless required.

**Rule ID:** `SV-239518r662005_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Reliable Datagram Sockets (RDS) protocol is a relatively new protocol developed by Oracle for communication between the nodes of a cluster. Binding this protocol to the network stack increases the attack surface of the host. Unprivileged local processes may be able to cause the system to dynamically load a protocol handler by opening a socket using the protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the SA if RDS is required by application software running on the system. If so, this is not applicable. Check that the RDS protocol handler is prevented from dynamic loading: # grep "install rds /bin/true" /etc/modprobe.conf /etc/modprobe.conf.local /etc/modprobe.d/* If no result is returned, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239519`

### Rule: The Transparent Inter-Process Communication (TIPC) must be disabled or not installed.

**Rule ID:** `SV-239519r662008_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Transparent Inter-Process Communication (TIPC) protocol is a relatively new cluster communications protocol developed by Ericsson. Binding this protocol to the network stack increases the attack surface of the host. Unprivileged local processes may be able to cause the kernel to dynamically load a protocol handler by opening a socket using the protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the TIPC protocol handler is prevented from dynamic loading: # grep "install tipc /bin/true" /etc/modprobe.conf /etc/modprobe.conf.local /etc/modprobe.d/* If no result is returned, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239520`

### Rule: The xinetd service must be disabled if no network services utilizing it are enabled.

**Rule ID:** `SV-239520r662011_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The xinetd service provides a dedicated listener service for some programs, which is no longer necessary for commonly-used network services. Disabling it ensures that these uncommon services are not running, and also prevents attacks against xinetd itself.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If network services are using the "xinetd" service, this is not applicable. To check that the "xinetd" service is disabled in system boot configuration, run the following command: # chkconfig "xinetd" --list Output should indicate the "xinetd" service has either not been installed, or has been disabled at all run levels, as shown in the example below: xinetd 0:off 1:off 2:off 3:off 4:off 5:off 6:off Run the following command to verify "xinetd" is disabled through current runtime configuration: # service xinetd status If the "xinetd" service is disabled the command will return the following output: Checking for service xinetd: unused If the "xinetd" service is running, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239521`

### Rule: The ypbind service must not be running if no network services utilizing it are enabled.

**Rule ID:** `SV-239521r662014_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Disabling the "ypbind" service ensures the SLES for vRealize is not acting as a client in a NIS or NIS+ domain when not required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If network services are using the "ypbind" service, this is not applicable. To check that the "ypbind" service is disabled in system boot configuration, run the following command: # chkconfig "ypbind" --list Output should indicate the "ypbind" service has either not been installed, or has been disabled at all runlevels, as shown in the example below: ypbind 0:off 1:off 2:off 3:off 4:off 5:off 6:off Run the following command to verify "ypbind" is disabled through current runtime configuration: # service ypbind status If the "ypbind" service is disabled the command will return the following output: Checking for service ypbind unused If the "ypbind" service is running, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239522`

### Rule: NIS/NIS+/yp files must be owned by root, sys, or bin.

**Rule ID:** `SV-239522r662017_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>NIS/NIS+/yp files are part of the system's identification and authentication processes and are, therefore, critical to system security. Failure to give ownership of sensitive files or utilities to root or bin provides the designated owner and unauthorized users with the potential to access sensitive information or change the system configuration, which could weaken the system's security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Perform the following to check NIS file ownership: # ls -la /var/yp/* If the NIS file ownership is not "root", sys, or bin, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239523`

### Rule: The NIS/NIS+/yp command files must have mode 0755 or less permissive.

**Rule ID:** `SV-239523r662020_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>NIS/NIS+/yp files are part of the system's identification and authentication processes and are, therefore, critical to system security. Unauthorized modification of these files could compromise these processes and SLES for vRealize.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Perform the following to check NIS file ownership: # ls -la /var/yp/* If the NIS file's mode is more permissive than "0755", this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239524`

### Rule: The SLES for vRealize must not use UDP for NIS/NIS+.

**Rule ID:** `SV-239524r662023_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Implementing NIS or NIS+ under UDP may make SLES for vRealize more susceptible to a denial of service attack and does not provide the same quality of service as TCP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If SLES for vRealize does not use NIS or NIS+, this is not applicable. Check if NIS or NIS+ is implemented using UDP: # rpcinfo -p | grep yp | grep udp If NIS or NIS+ is implemented using UDP, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239525`

### Rule: NIS maps must be protected through hard-to-guess domain names.

**Rule ID:** `SV-239525r662026_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of hard-to-guess NIS domain names provides additional protection from unauthorized access to the NIS directory information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If SLES for vRealize does not use NIS or NIS+, this is not applicable. Check the domain name for NIS maps: # domainname If the name returned is simple to guess, such as the organization name, building or room name, etc., this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239526`

### Rule: Mail relaying must be restricted.

**Rule ID:** `SV-239526r662029_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If unrestricted mail relaying is permitted, unauthorized senders could use this host as a mail relay for the purpose of sending SPAM or other unauthorized activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if Sendmail only binds to loopback addresses by examining the "DaemonPortOptions" configuration options. # grep -i "O DaemonPortOptions" /etc/sendmail.cf If there are uncommented "DaemonPortOptions" lines, and all such lines specify system loopback addresses, this is not a finding. Otherwise, determine if "Sendmail" is configured to allow open relay operation. # grep -i promiscuous_relay /etc/mail/sendmail.mc If the promiscuous relay feature is enabled, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239527`

### Rule: The alias files must be owned by root.

**Rule ID:** `SV-239527r662032_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the alias and aliases.db files are not owned by root, an unauthorized user may modify the file to add aliases to run malicious code or redirect email.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of the alias file: # ls -lL /etc/aliases # ls -lL /etc/aliases.db If all the files are not owned by "root", this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239528`

### Rule: The alias files must be group-owned by root, or a system group.

**Rule ID:** `SV-239528r662035_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the aliases and aliases.db file are not group-owned by root or a system group, an unauthorized user may modify one or both of the files to add aliases to run malicious code or redirect email.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the alias files: # ls -lL /etc/aliases # ls -lL /etc/aliases.db If the files are not group-owned by "root", this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239529`

### Rule: The alias files must have mode 0644 or less permissive.

**Rule ID:** `SV-239529r662038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on the alias files may permit unauthorized modification. If an alias file is modified by an unauthorized user, they may modify the file to run malicious code or redirect email.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the alias files: # ls -lL /etc/aliases # ls -lL /etc/aliases.db If the alias files have a mode more permissive than "0644", this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239530`

### Rule: Files executed through a mail aliases file must be owned by root and must reside within a directory owned and writable only by root.

**Rule ID:** `SV-239530r662041_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a file executed through a mail aliases file is not owned and writable only by root, it may be subject to unauthorized modification. Unauthorized modification of files executed through aliases may allow unauthorized users to attain root privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ownership of files referenced within the sendmail aliases file: # more /etc/aliases Examine the aliases file for any utilized directories or paths: # ls -lL <directory or file path> Check the owner for any paths referenced. Check if the file or parent directory is owned by root. If the file or parent directory is not owned by "root", this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239531`

### Rule: Files executed through a mail aliases file must be group-owned by root, bin, sys, or system, and must reside within a directory group-owned by root, bin, sys, or system.

**Rule ID:** `SV-239531r662044_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a file executed through a mail aliases file is not group-owned by root or a system group, it may be subject to unauthorized modification. Unauthorized modification of files executed through aliases may allow unauthorized users to attain root privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the contents of the "/etc/aliases" file: # more /etc/aliases Examine the aliases file for any directories or paths that may be utilized: # ls -lL <file referenced from aliases> Check the permissions for any paths referenced. If the group owner of any file is not "root", "bin", "sys", or "system", this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239532`

### Rule: Files executed through a mail aliases file must have mode 0755 or less permissive.

**Rule ID:** `SV-239532r662047_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a file executed through a mail alias file has permissions greater than 0755, it can be modified by an unauthorized user and may contain malicious code or instructions that could compromise the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the contents of the "/etc/aliases" file: # more /etc/aliases Examine the aliases file for any directories or paths that may be utilized: # ls -lL <file referenced from aliases> Check the permissions for any paths referenced. If any file referenced from the aliases file has a mode more permissive than "0755", this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239533`

### Rule: Sendmail logging must not be set to less than nine in the sendmail.cf file.

**Rule ID:** `SV-239533r662050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Sendmail is not configured to log at level 9, system logs may not contain the information necessary for tracking unauthorized use of the sendmail service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check sendmail to determine if the logging level is set to level "9": # grep "O L" /etc/sendmail.cf OR # grep LogLevel /etc/sendmail.cf If logging is set to less than "9", this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239534`

### Rule: The system syslog service must log informational and more severe SMTP service messages.

**Rule ID:** `SV-239534r662053_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If informational and more severe SMTP service messages are not logged, malicious activity on the system may go unnoticed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the "/etc/syslog-ng/syslog-ng.conf" file for the following log entries: filter f_mailinfo { level(info) and facility(mail); }; filter f_mailwarn { level(warn) and facility(mail); }; filter f_mailerr { level(err, crit) and facility(mail); }; filter f_mail { facility(mail); }; If any of the above log entries are present, this is not a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239535`

### Rule: The SMTP service log files must be owned by root.

**Rule ID:** `SV-239535r662056_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the SMTP service log file is not owned by root, then unauthorized personnel may modify or delete the file to hide a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions on the mail log files: # ls -la /var/log/mail # ls -la /var/log/mail.info # ls -la /var/log/mail.warn # ls -la /var/log/mail.err If any mail log file is not owned by "root", this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239536`

### Rule: The SMTP service log file must have mode 0644 or less permissive.

**Rule ID:** `SV-239536r662059_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the SMTP service log file is more permissive than 0644, unauthorized users may be allowed to change the log file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions on the mail log files: # ls -la /var/log/mail # ls -la /var/log/mail.info # ls -la /var/log/mail.warn # ls -la /var/log/mail.err If the log file permissions are greater than "0644", this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239537`

### Rule: The SMTP service HELP command must not be enabled.

**Rule ID:** `SV-239537r662062_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The HELP command should be disabled to mask version information. The version of the SMTP service software could be used by attackers to target vulnerabilities present in specific software versions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the sendmail helpfile: ls -al /usr/lib/sendmail.d/helpfile If the permissions are not "0000", this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239538`

### Rule: The SMTP services SMTP greeting must not provide version information.

**Rule ID:** `SV-239538r662065_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The version of the SMTP service can be used by attackers to plan an attack based on vulnerabilities present in the specific version.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To check for the sendmail version being displayed in the greeting: # more /etc/sendmail.cf | grep SmtpGreetingMessage If it returns: O SmtpGreetingMessage=$j Sendmail $v/$Z; $b Then sendmail is providing version information, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239539`

### Rule: The SMTP service must not use .forward files.

**Rule ID:** `SV-239539r662068_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The .forward file allows users to automatically forward mail to another system. Use of .forward files could allow the unauthorized forwarding of mail and could potentially create mail loops that could degrade system performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check forwarding from sendmail: # grep "0 ForwardPath" /etc/sendmail.cf If the entry contains a file path and is not commented out, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239540`

### Rule: The SMTP service must not have the EXPN feature active.

**Rule ID:** `SV-239540r662071_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The SMTP EXPN function allows an attacker to determine if an account exists on a system, providing significant assistance to a brute force attack on user accounts. EXPN may also provide additional information concerning users on the system, such as the full names of account owners.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the following command to check if EXPN is disabled: # grep -v "^#" /etc/sendmail.cf |grep -i PrivacyOptions If "noexpn" is not returned, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239541`

### Rule: The SMTP service must not have the VRFY feature active.

**Rule ID:** `SV-239541r662074_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The VRFY (Verify) command allows an attacker to determine if an account exists on a system, providing significant assistance to a brute force attack on user accounts. VRFY may provide additional information about users on the system, such as the full names of account owners.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the following command to check if VRFY is disabled: # grep -v "^#" /etc/sendmail.cf |grep -i PrivacyOptions If "novrfy" is not returned, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239542`

### Rule: The Lightweight User Datagram Protocol (UDP-Lite) must be disabled unless required.

**Rule ID:** `SV-239542r662077_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Lightweight User Datagram Protocol (UDP-Lite) is a proposed transport layer protocol. This protocol is not yet widely used. Binding this protocol to the network stack increases the attack surface of the host. Unprivileged local processes may be able to cause SLES for vRealize to dynamically load a protocol handler by opening a socket using the protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command: iptables --list | grep "udplite" If no result is displayed, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239543`

### Rule: The Internetwork Packet Exchange (IPX) protocol must be disabled or not installed.

**Rule ID:** `SV-239543r662080_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Internetwork Packet Exchange (IPX) protocol is a network-layer protocol that is no longer in common use. Binding this protocol to the network stack increases the attack surface of the host. Unprivileged local processes may be able to cause SLES for vRealize to dynamically load a protocol handler by opening a socket using the protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that the "IPX" protocol handler is prevented from dynamic loading: # grep "install ipx /bin/true" /etc/modprobe.conf /etc/modprobe.conf.local /etc/modprobe.d/* If no result is returned, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239544`

### Rule: The AppleTalk protocol must be disabled or not installed.

**Rule ID:** `SV-239544r662083_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The AppleTalk suite of protocols is no longer in common use. Binding this protocol to the network stack increases the attack surface of the host. Unprivileged local processes may be able to cause SLES for vRealize to dynamically load a protocol handler by opening a socket using the protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "AppleTalk" protocol handler is prevented from dynamic loading: # grep "install appletalk /bin/true" /etc/modprobe.conf /etc/modprobe.conf.local /etc/modprobe.d/* If no result is returned, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239545`

### Rule: The DECnet protocol must be disabled or not installed.

**Rule ID:** `SV-239545r662086_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DECnet suite of protocols is no longer in common use. Binding this protocol to the network stack increases the attack surface of the host. Unprivileged local processes may be able to cause SLES for vRealize to dynamically load a protocol handler by opening a socket using the protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that the "DECnet" protocol handler is prevented from dynamic loading: # grep "install decnet /bin/true" /etc/modprobe.conf /etc/modprobe.conf.local /etc/modprobe.d/* If no result is returned, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239546`

### Rule: Proxy Neighbor Discovery Protocol (NDP) must not be enabled on SLES for vRealize.

**Rule ID:** `SV-239546r662089_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Proxy Neighbor Discovery Protocol (NDP) allows a system to respond to NDP requests on one interface on behalf of hosts connected to another interface. If this function is enabled when not required, addressing information may be leaked between the attached network segments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if SLES for vRealize has proxy "NDP", and if it is enabled: # more /proc/sys/net/ipv6/conf/*/proxy_ndp If the file is not found, the kernel does not have proxy "NDP", this is not a finding. If the file has a value of "0", proxy "NDP" is not enabled, this is not a finding. If the file has a value of "1", proxy NDP is enabled, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239547`

### Rule: The SLES for vRealize must not have 6to4 enabled.

**Rule ID:** `SV-239547r662092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>6to4 is an IPv6 transition mechanism that involves tunneling IPv6 packets encapsulated in IPv4 packets on an ad hoc basis. This is not a preferred transition strategy and increases the attack surface of SLES for vRealize.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check SLES for vRealize for any active "6to4" tunnels without specific remote addresses: # ip tun list | grep "remote any" | grep "ipv6/ip" If any results are returned the "tunnel" is the first field. If any results are returned, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239548`

### Rule: The SLES for vRealize must not have Teredo enabled.

**Rule ID:** `SV-239548r662095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Teredo is an IPv6 transition mechanism that involves tunneling IPv6 packets encapsulated in IPv4 packets. Unauthorized tunneling may circumvent network security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "Miredo" service is not running: # ps ax | grep miredo | grep -v grep If the Miredo process is running, this is a finding. Note: For Appliance OS, "Miredo" is not included by default, this is not a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239549`

### Rule: The DHCP client must be disabled if not needed.

**Rule ID:** `SV-239549r662098_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DHCP allows for the unauthenticated configuration of network parameters on SLES for vRealize by exchanging information with a DHCP server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that no interface is configured to use "DHCP": # grep -i bootproto=dhcp4 /etc/sysconfig/network/ifcfg-* If any configuration is found, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-239550`

### Rule: The SLES for vRealize must have IEEE 1394 (Firewire) disabled unless needed.

**Rule ID:** `SV-239550r662101_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Firewire is a common computer peripheral interface. Firewire devices may include storage devices that could be used to install malicious software on a system or exfiltrate data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If SLES for vRealize needs IEEE 1394 (Firewire), this is not applicable. Check if the firewire module is not disabled: # grep "install ieee1394 /bin/true" /etc/modprobe.conf /etc/modprobe.conf.local /etc/modprobe.d/* If no results are returned, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-239551`

### Rule: Duplicate User IDs (UIDs) must not exist for users within the organization.

**Rule ID:** `SV-239551r662104_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of SLES for vRealize. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLES for vRealize contains no duplicate UIDs for organizational users by running the following command: # awk -F ":" 'list[$3]++{print $1, $3}' /etc/passwd If output is produced, this is a finding.

## Group: SRG-OS-000109-GPOS-00056

**Group ID:** `V-239552`

### Rule: The SLES for vRealize must prevent direct logon into the root account.

**Rule ID:** `SV-239552r662107_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To assure individual accountability and prevent unauthorized access, organizational users must be individually identified and authenticated. A group authenticator is a generic account used by multiple individuals. Use of a group authenticator alone does not uniquely identify individual users. Examples of the group authenticator is the UNIX OS "root" user account, the Windows "Administrator" account, the "sa" account, or a "helpdesk" account. For example, the UNIX and Windows operating systems offer a 'switch user' capability allowing users to authenticate with their individual credentials and, when needed, 'switch' to the administrator role. This method provides for unique individual authentication prior to using a group authenticator. Users (and any processes acting on behalf of users) need to be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization, which outlines specific user actions that can be performed on the operating system without identification or authentication. Requiring individuals to be authenticated with an individual authenticator prior to using a group authenticator allows for traceability of actions, as well as adding an additional level of protection of the actions that can be taken with group account knowledge.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLES for vRealize prevents direct logons to the root account by running the following command: # grep root /etc/shadow | cut -d "":"" -f 2 If the returned message contains any text, this is a finding.

## Group: SRG-OS-000112-GPOS-00057

**Group ID:** `V-239553`

### Rule: The SLES for vRealize must enforce SSHv2 for network access to privileged accounts.

**Rule ID:** `SV-239553r852586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to SLES for vRealize. Authentication sessions between the authenticator and SLES for vRealize validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. A privileged account is any information system account with authorizations of a privileged user. Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., TLS, WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLES for vRealize enforces SSHv2 for network access to privileged accounts by running the following command: Replace [ADDRESS] in the following command with the correct IP address based on the current system configuration. # ssh -1 [ADDRESS] An example of the command usage is as follows: # ssh -1 localhost The output must be the following: Protocol major versions differ: 1 vs. 2 If it is not, this is a finding. OR Verify that the ssh is configured to enforce SSHv2 for network access to privileged accounts by running the following command: # grep Protocol /etc/ssh/sshd_config If the result is not "Protocol 2", this is a finding.

## Group: SRG-OS-000113-GPOS-00058

**Group ID:** `V-239554`

### Rule: The SLES for vRealize must enforce SSHv2 for network access to non-privileged accounts.

**Rule ID:** `SV-239554r852587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to SLES for vRealize. Authentication sessions between the authenticator and SLES for vRealize validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. A non-privileged account is any SLES for vRealize account with authorizations of a non-privileged user. Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., TLS, WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLES for vRealize enforces SSHv2 for network access to privileged accounts by running the following command: Replace [ADDRESS] in the following command with the correct IP address based on the current system configuration. # ssh -1 [ADDRESS] An example of the command usage is as follows: # ssh -1 localhost The output must be one of the following items: Protocol major versions differ: 1 vs. 2 OR Protocol 1 not allowed in the FIPS mode. If it does not, this is a finding. OR Verify that the ssh is configured to enforce SSHv2 for network access to privileged accounts by running the following command: # grep Protocol /etc/ssh/sshd_config If the result is not "Protocol 2", this is a finding.

## Group: SRG-OS-000118-GPOS-00060

**Group ID:** `V-239555`

### Rule: The SLES for vRealize must disable account identifiers of individuals and roles (such as root) after 35 days of inactivity after password expiration.

**Rule ID:** `SV-239555r662116_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. SLES for vRealize need to track periods of inactivity and disable application identifiers after 35 days of inactivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLES for vRealize disables account identifiers after "35" days of inactivity after the password expiration, by performing the following commands: # grep "INACTIVE" /etc/default/useradd The output must indicate the "INACTIVE" configuration option is set to an appropriate integer as shown in the example below: grep "INACTIVE" /etc/default/useradd INACTIVE=35 If "INACTIVE" is not set to a value 0<[VALUE]<=35, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-239556`

### Rule: The SLES for vRealize must use mechanisms meeting the requirements of applicable federal laws, Executive orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module.

**Rule ID:** `SV-239556r662119_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised. SLES for vRealize utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DoD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general purpose computing system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the "/etc/default/passwd" file: # grep CRYPT /etc/default/passwd If the "CRYPT" setting in the "/etc/default/passwd" file is not present, or not set to "SHA256" or "SHA512", this is a finding. If the "CRYPT_FILES" setting in the "/etc/default/passwd" file is not present, or not set to "SHA256" or "SHA512", this is a finding.

## Group: SRG-OS-000121-GPOS-00062

**Group ID:** `V-239557`

### Rule: The SLES for vRealize must uniquely identify and must authenticate non-organizational users (or processes acting on behalf of non-organizational users).

**Rule ID:** `SV-239557r662122_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Lack of authentication and identification enables non-organizational users to gain access to the application or possibly other information systems and provides an opportunity for intruders to compromise resources within the application or information system. Non-organizational users include all information system users other than organizational users, which include organizational employees or individuals the organization deems to have equivalent status of an employee (e.g., contractors and guest researchers). Non-organizational users must be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization when related to the use of anonymous access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to check for duplicate account names: # pwck -rq If there are no duplicate names, no line will be returned. If a line is returned, this is a finding.

## Group: SRG-OS-000121-GPOS-00062

**Group ID:** `V-239558`

### Rule: The SLES for vRealize must uniquely identify and must authenticate non-organizational users (or processes acting on behalf of non-organizational users).

**Rule ID:** `SV-239558r662125_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Lack of authentication and identification enables non-organizational users to gain access to the application or possibly other information systems and provides an opportunity for intruders to compromise resources within the application or information system. Non-organizational users include all information system users other than organizational users, which include organizational employees or individuals the organization deems to have equivalent status of an employee (e.g., contractors and guest researchers). Non-organizational users must be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization when related to the use of anonymous access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SLES for vRealize uniquely identifies and authenticates non-organizational users by running the following commands: # awk -F: '{print $3}' /etc/passwd | sort | uniq -d If the output is not blank, this is a finding.

## Group: SRG-OS-000123-GPOS-00064

**Group ID:** `V-239559`

### Rule: The SLES for vRealize must be configured such that emergency administrator accounts are never automatically removed or disabled.

**Rule ID:** `SV-239559r662128_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Emergency administrator accounts are privileged accounts which are established in response to crisis situations where the need for rapid account activation is required. Therefore, emergency account activation may bypass normal account authorization processes. If these accounts are automatically disabled, system maintenance during emergencies may not be possible, thus adversely affecting system availability. Emergency administrator accounts are different from infrequently used accounts (i.e., local logon accounts used by system administrators when network or normal logon/access is not available). Infrequently used accounts also remain available and are not subject to automatic termination dates. However, an emergency administrator account is normally a different account that is created for use by vendors or system maintainers. To address access requirements, many operating systems can be integrated with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each emergency administrator account run the following command: chage -l [user] If the output shows an expiration date for the account, this is a finding.

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-239560`

### Rule: The SLES for vRealize must employ strong authenticators in the establishment of nonlocal maintenance and diagnostic sessions.

**Rule ID:** `SV-239560r877395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If maintenance tools are used by unauthorized personnel, they may accidentally or intentionally damage or compromise the system. The act of managing systems and applications includes the ability to access sensitive application information, such as system configuration details, diagnostic information, user information, and potentially sensitive application data. Some maintenance and test tools are either standalone devices with their own operating systems or are applications bundled with an operating system. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. Typically, strong authentication requires authenticators that are resistant to replay attacks and employ multifactor authentication. Strong authenticators include, for example, PKI where certificates are stored on a token protected by a password, passphrase, or biometric.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for DoD-approved encryption to protect the confidentiality of SSH remote connections by performing the following commands: Check the Cipher setting in the sshd_config file. # grep -i Ciphers /etc/ssh/sshd_config | grep -v '#' The output must contain either none or any number of the following algorithms: aes128-ctr, aes256-ctr. If the output contains an algorithm not listed above, this is a finding. Expected Output: Ciphers aes256-ctr,aes128-ctr

## Group: SRG-OS-000126-GPOS-00066

**Group ID:** `V-239561`

### Rule: The SLES for vRealize must terminate all sessions and network connections related to nonlocal maintenance when nonlocal maintenance is completed.

**Rule ID:** `SV-239561r662134_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> If a maintenance session or connection remains open after maintenance is completed, it may be hijacked by an attacker and used to compromise or damage the system. Some maintenance and test tools are either standalone devices with their own operating systems or are applications bundled with an operating system. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for the existence of the "/etc/profile.d/tmout.sh" file: # ls -al /etc/profile.d/tmout.sh Check for the presence of the "TMOUT" variable: # grep TMOUT /etc/profile.d/tmout.sh The value of "TMOUT" should be set to "900" seconds (15 minutes). If the file does not exist, or the "TMOUT" variable is not set to "900", this is a finding.

## Group: SRG-OS-000142-GPOS-00071

**Group ID:** `V-239562`

### Rule: The SLES for vRealize must manage excess capacity, bandwidth, or other redundancy to limit the effects of information flooding types of Denial of Service (DoS) attacks.

**Rule ID:** `SV-239562r662137_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Managing excess capacity ensures that sufficient capacity is available to counter flooding attacks. Employing increased capacity and service redundancy may reduce the susceptibility to some DoS attacks. Managing excess capacity may include, for example, establishing selected usage priorities, quotas, or partitioning.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that SLES for vRealize is configured to use TCP syncookies when experiencing a TCP SYN flood. # cat /proc/sys/net/ipv4/tcp_syncookies If the result is not "1", this is a finding.

## Group: SRG-OS-000142-GPOS-00071

**Group ID:** `V-239563`

### Rule: The SLES for vRealize must manage excess capacity, bandwidth, or other redundancy to limit the effects of information flooding types of Denial of Service (DoS) attacks.

**Rule ID:** `SV-239563r662140_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Managing excess capacity ensures that sufficient capacity is available to counter flooding attacks. Employing increased capacity and service redundancy may reduce the susceptibility to some DoS attacks. Managing excess capacity may include, for example, establishing selected usage priorities, quotas, or partitioning.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that SLES for vRealize has an appropriate TCP backlog queue size to mitigate against TCP SYN flood DOS attacks with the following command: # cat /proc/sys/net/ipv4/tcp_max_syn_backlog The recommended default setting is "1280". If the TCP backlog queue size is not set to "1280", this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-239564`

### Rule: The SLES for vRealize must terminate all network connections associated with a communications session at the end of the session, or as follows: for in-band management sessions (privileged sessions), the session must be terminated after 10 minutes of inactivity; and for user sessions (non-privileged session), the session must be terminated after 15 minutes of inactivity, except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-239564r662405_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, and de-allocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that SLES for vRealize terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for the existence of the "/etc/profile.d/tmout.sh" file: # ls -al /etc/profile.d/tmout.sh Check for the presence of the "TMOUT" variable: # grep TMOUT /etc/profile.d/tmout.sh The value of "TMOUT" should be set to "900" seconds (15 minutes). If the file does not exist, or the "TMOUT" variable is not set to "900", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-239565`

### Rule: The /var/log directory must be group-owned by root.

**Rule ID:** `SV-239565r662146_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the SLES for vRealize system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/var/log" directory is group-owned by "root" by running the following command: # ls -lad /var/log | cut -d' ' -f4 The output must look like the following example: ls -lad /var/log | cut -d' ' -f4 root If "root" is not returned as a result, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-239566`

### Rule: The /var/log directory must be owned by root.

**Rule ID:** `SV-239566r662149_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the SLES for vRealize system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "/var/log" directory is owned by "root" by running the following command: # ls -lad /var/log | cut -d' ' -f3 The output must look like the following example: ls -lad /var/log | cut -d' ' -f3 root If "root" is not returned as a result, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-239567`

### Rule: The /var/log directory must have mode 0750 or less permissive.

**Rule ID:** `SV-239567r662152_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the SLES for vRealize system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "/var/log" directory is the mode 0750 or less permissive by running the following command: # ls -lad /var/log | cut -d' ' -f1 The output must look like the following example: ls -lad /var/log | cut -d' ' -f1 drwxr-x--- If "drwxr-x---" is not returned as a result, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-239568`

### Rule: The /var/log/messages file must be group-owned by root.

**Rule ID:** `SV-239568r662155_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the SLES for vRealize system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "/var/log/messages" file is group-owned by "root" by running the following command: # ls -la /var/log/messages | cut -d' ' -f4 The output must look like the following example: ls -la /var/log/messages | cut -d' ' -f4 root If "root" is not returned as a result, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-239569`

### Rule: The /var/log/messages file must be owned by root.

**Rule ID:** `SV-239569r662158_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the SLES for vRealize system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "/var/log/messages" file is owned by "root" by running the following command: # ls -la /var/log/messages | cut -d' ' -f3 The output must look like the following example: ls -la /var/log/messages | cut -d' ' -f3 root If "root" is not returned as a result, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-239570`

### Rule: The /var/log/messages file must have mode 0640 or less permissive.

**Rule ID:** `SV-239570r662161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the SLES for vRealize system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "/var/log/messages" file is 0640 or less permissive by running the following command: # ls -lad /var/log/messages | cut -d' ' -f1 The output must look like the following example: ls -lad /var/log/messages | cut -d' ' -f1 -rw-r----- If "-rw-r-----" is not returned as a result, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-239571`

### Rule: The SLES for vRealize must reveal error messages only to authorized users.

**Rule ID:** `SV-239571r662164_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the SLES for vRealize system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the syslog configuration file(s): # ls -lL /etc/syslog-ng/syslog-ng.conf If the mode of the file is more permissive than "0640", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-239572`

### Rule: The SLES for vRealize must reveal error messages only to authorized users.

**Rule ID:** `SV-239572r662167_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the SLES for vRealize system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the syslog configuration file(s): # ls -lL /etc/syslog-ng/syslog-ng.conf If the file is not owned by "root", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-239573`

### Rule: The SLES for vRealize must reveal error messages only to authorized users.

**Rule ID:** `SV-239573r662170_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the SLES for vRealize system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the permissions of the syslog configuration file(s): # ls -lL /etc/syslog-ng/syslog-ng.conf If the file is not group owned by "root", this is a finding.

## Group: SRG-OS-000239-GPOS-00089

**Group ID:** `V-239575`

### Rule: The SLES for vRealize must audit all account modifications.

**Rule ID:** `SV-239575r662176_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply modify an existing account. Auditing of account modification is one method for mitigating this risk. To address access requirements, many SLES for vRealize systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if execution of the "usermod" and "groupmod" executable are audited. # auditctl -l | egrep '(usermod|groupmod)' | grep perm=x If either "usermod" or "groupmod" are not listed with a permissions filter of at least "x", this is a finding.

## Group: SRG-OS-000239-GPOS-00089

**Group ID:** `V-239576`

### Rule: The SLES for vRealize must audit all account modifications.

**Rule ID:** `SV-239576r662179_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply modify an existing account. Auditing of account modification is one method for mitigating this risk. To address access requirements, many SLES for vRealize systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if "/etc/passwd", "/etc/shadow", "/etc/group", and "/etc/gshadow" are audited for writing. # auditctl -l | egrep '(/etc/passwd|/etc/shadow|/etc/group|/etc/gshadow)' | grep perm=w If any of these are not listed with a permissions filter of at least "w", this is a finding.

## Group: SRG-OS-000240-GPOS-00090

**Group ID:** `V-239577`

### Rule: The SLES for vRealize must audit all account-disabling actions.

**Rule ID:** `SV-239577r662182_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When SLES for vRealize accounts are disabled, user accessibility is affected. Accounts are utilized for identifying individual users or for identifying the SLES for vRealize processes themselves. In order to detect and respond to events affecting user accessibility and system processing, SLES for vRealize must audit account disabling actions and, as required, notify the appropriate individuals so they can investigate the event. Such a capability greatly reduces the risk that SLES for vRealize accessibility will be negatively affected for extended periods of time and provides logging that can be used for forensic purposes. To address access requirements, many SLES for vRealize systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if execution of the "passwd" executable is audited: # auditctl -l | grep watch=/usr/bin/passwd If "/usr/bin/passwd" is not listed with a permissions filter of at least "x", this is a finding.

## Group: SRG-OS-000241-GPOS-00091

**Group ID:** `V-239578`

### Rule: The SLES for vRealize must audit all account removal actions.

**Rule ID:** `SV-239578r662185_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When SLES for vRealize accounts are removed, user accessibility is affected. Accounts are utilized for identifying individual users or for identifying the SLES for vRealize processes themselves. In order to detect and respond to events affecting user accessibility and system processing, operating systems must audit account removal actions and, as required, notify the appropriate individuals so they can investigate the event. Such a capability greatly reduces the risk that SLES for vRealize accessibility will be negatively affected for extended periods of time and provides logging that can be used for forensic purposes. To address access requirements, many SLES for vRealize systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if execution of the "userdel" and "groupdel" executable are audited: # auditctl -l | egrep '(userdel|groupdel)' If either "userdel" or "groupdel" are not listed with a permissions filter of at least "x", this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-239579`

### Rule: The SLES for vRealize must implement cryptography to protect the integrity of remote access sessions.

**Rule ID:** `SV-239579r877394_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for DoD-approved encryption to protect the confidentiality of SSH remote connections by performing the following commands: Check the Cipher setting in the "sshd_config" file. # grep -i Ciphers /etc/ssh/sshd_config | grep -v '#' The output must contain either none or any number of the following algorithms: aes128-ctr, aes256-ctr. If the output contains an algorithm not listed above, this is a finding. Expected Output: Ciphers aes256-ctr,aes128-ctr

## Group: SRG-OS-000254-GPOS-00095

**Group ID:** `V-239580`

### Rule: The SLES for vRealize must initiate session audits at system start-up.

**Rule ID:** `SV-239580r662191_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If auditing is enabled late in the start-up process, the actions of some start-up processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for the "audit=1" kernel parameter. # grep "audit=1" /proc/cmdline If no results are returned, this is a finding.

## Group: SRG-OS-000255-GPOS-00096

**Group ID:** `V-239581`

### Rule: The SLES for vRealize must produce audit records containing information to establish the identity of any individual or process associated with the event.

**Rule ID:** `SV-239581r662194_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without information that establishes the identity of the subjects (i.e., users or processes acting on behalf of users) associated with the events, security personnel cannot determine responsibility for the potentially harmful event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLES for vRealize produces audit records by running the following command to determine the current status of the "auditd" service: # service auditd status If the service is enabled, the returned message must contain the following text: Checking for service auditd running If the service is not running, this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-239582`

### Rule: The SLES for vRealize must protect audit tools from unauthorized access.

**Rule ID:** `SV-239582r662197_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. SLES for vRealize systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The following command will list which audit files on the system have permissions different from what is expected by the RPM database: # rpm -V audit | grep '^.M' If there is any output, for each file or directory found, compare the RPM-expected permissions with the permissions on the file or directory: # rpm -q --queryformat "[%{FILENAMES} %{FILEMODES:perms}\n]" audit | grep [filename] # ls -lL [filename] If the existing permissions are more permissive than those expected by the RPM database, this is a finding.

## Group: SRG-OS-000257-GPOS-00098

**Group ID:** `V-239583`

### Rule: The SLES for vRealize must protect audit tools from unauthorized modification.

**Rule ID:** `SV-239583r662200_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. SLES for vRealize systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user has in order to make access decisions regarding the modification of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The following command will list which audit files on the system where the group ownership has been modified: # rpm -V audit | grep '^......G' If there is output, this is a finding.

## Group: SRG-OS-000258-GPOS-00099

**Group ID:** `V-239584`

### Rule: The SLES for vRealize must protect audit tools from unauthorized deletion.

**Rule ID:** `SV-239584r662203_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. SLES for vRealize systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user has in order to make access decisions regarding the deletion of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The following command will list which audit files on the system where the ownership has been modified: # rpm -V audit | grep '^.....U' If there is output, this is a finding.

## Group: SRG-OS-000266-GPOS-00101

**Group ID:** `V-239585`

### Rule: The SLES for vRealize must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-239585r662206_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity or strength is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor in determining how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Special characters are those characters that are not alphanumeric. Examples include: ~ ! @ # $ % ^ *.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLES for vRealize enforces password complexity by requiring that at least one special character be used by using the following command: Check the password "ocredit" option: # grep pam_cracklib.so /etc/pam.d/common-password Confirm the "ocredit" option is set to "-1" as in the example: password requisite pam_cracklib.so ocredit=-1 There may be other options on the line. If no such line is found, or the "ocredit" is not "-1", this is a finding.

## Group: SRG-OS-000274-GPOS-00104

**Group ID:** `V-239586`

### Rule: The SLES for vRealize must notify System Administrators and Information Systems Security Officer when accounts are created.

**Rule ID:** `SV-239586r662209_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply create a new account. Notification of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail, which documents the creation of SLES for vRealize user accounts and notifies System Administrators and Information System Security Officers (ISSO) that it exists. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes. To address access requirements, many SLES for vRealize systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the syslog configuration file for remote syslog servers: # cat /etc/syslog-ng/syslog-ng.conf | grep logserver If no line is returned, or the "logserver" is commented out, this is a finding.

## Group: SRG-OS-000275-GPOS-00105

**Group ID:** `V-239587`

### Rule: The SLES for vRealize must notify System Administrators and Information System Security Officers when accounts are modified.

**Rule ID:** `SV-239587r662212_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply modify an existing account. Notification of account modification is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail, which documents the creation of SLES for vRealize user accounts and notifies System Administrators and Information System Security Officers (ISSO) that it exists. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes. To address access requirements, many SLES for vRealize systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the syslog configuration file for remote syslog servers: # cat /etc/syslog-ng/syslog-ng.conf | grep logserver If no line is returned, or the "logserver" is commented out, this is a finding.

## Group: SRG-OS-000276-GPOS-00106

**Group ID:** `V-239588`

### Rule: The SLES for vRealize must notify System Administrators and Information System Security Officers when accounts are disabled.

**Rule ID:** `SV-239588r662215_rule`
**Severity:** low

**Description:**
<VulnDiscussion>When SLES for vRealize accounts are disabled, user accessibility is affected. Accounts are utilized for identifying individual SLES for vRealize users or for identifying the SLES for vRealize processes themselves. In order to detect and respond to events that affect user accessibility and system processing, operating systems must audit account disabling actions and, as required, notify System Administrators and Information System Security Officers (ISSO) so they can investigate the event. Such a capability greatly reduces the risk that operating system accessibility will be negatively affected for extended periods of time and also provides logging that can be used for forensic purposes. To address access requirements, many SLES for vRealize systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the syslog configuration file for remote syslog servers: # cat /etc/syslog-ng/syslog-ng.conf | grep logserver If no line is returned, or the "logserver" is commented out, this is a finding.

## Group: SRG-OS-000277-GPOS-00107

**Group ID:** `V-239589`

### Rule: The SLES for vRealize must notify System Administrators and Information System Security Officers when accounts are removed.

**Rule ID:** `SV-239589r662218_rule`
**Severity:** low

**Description:**
<VulnDiscussion>When SLES for vRealize accounts are removed, user accessibility is affected. Accounts are utilized for identifying individual SLES for vRealize users or for identifying the SLES for vRealize processes themselves. In order to detect and respond to events that affect user accessibility and system processing, SLES for vRealize must audit account removal actions and, as required, notify System Administrators and Information System Security Officers (ISSO) so they can investigate the event. Such a capability greatly reduces the risk that operating system accessibility will be negatively affected for extended periods of time and also provides logging that can be used for forensic purposes. To address access requirements, many operating systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the syslog configuration file for remote syslog servers: # cat /etc/syslog-ng/syslog-ng.conf | grep logserver If no line is returned, or the "logserver" is commented out, this is a finding.

## Group: SRG-OS-000278-GPOS-00108

**Group ID:** `V-239590`

### Rule: The SLES for vRealize must use cryptographic mechanisms to protect the integrity of audit tools.

**Rule ID:** `SV-239590r877393_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting the integrity of the tools used for auditing purposes is a critical step toward ensuring the integrity of audit information. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. It is not uncommon for attackers to replace the audit tools or inject code into the existing tools with the purpose of providing the capability to hide or erase system activity from the audit logs. To address this risk, audit tools must be cryptographically signed in order to provide the capability to identify when the audit tools have been modified, manipulated, or replaced. An example is a checksum hash of the file or files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The following command will list which audit files on the system have file hashes different from what is expected by the RPM database: # rpm -V audit | grep '$1 ~ /..5/ && $2 != "c"' If there is output, this is a finding.

## Group: SRG-OS-000279-GPOS-00109

**Group ID:** `V-239591`

### Rule: The SLES for vRealize must automatically terminate a user session after inactivity time-outs have expired or at shutdown.

**Rule ID:** `SV-239591r852588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination terminates all processes associated with a user's logical session except those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific operating system functionality where the system owner, data owner, or organization requires additional assurance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for the existence of the "/etc/profile.d/tmout.sh" file: # ls -al /etc/profile.d/tmout.sh Check for the presence of the "TMOUT" variable: # grep TMOUT /etc/profile.d/tmout.sh The value of "TMOUT" should be set to "900" seconds (15 minutes). If the file does not exist, or the "TMOUT" variable is not set to "900", this is a finding.

## Group: SRG-OS-000297-GPOS-00115

**Group ID:** `V-239592`

### Rule: The SLES for vRealize must control remote access methods.

**Rule ID:** `SV-239592r852589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. SLES for vRealize functionality (e.g., RDP) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for listening network addresses: # grep -i Listen /etc/ssh/sshd_config | grep -v '^#' If no configuration is returned, or if a returned "Listen" configuration contains addresses not designated for management traffic, this is a finding.

## Group: SRG-OS-000303-GPOS-00120

**Group ID:** `V-239593`

### Rule: The SLES for vRealize must audit all account enabling actions.

**Rule ID:** `SV-239593r852590_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply enable a new or disabled account. Notification of account enabling is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail, which documents the creation of SLES for vRealize user accounts and notifies System Administrators and Information System Security Officers (ISSO) that it exists. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes. To address access requirements, many SLES for vRealize systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if execution of the usermod and groupmod executable are audited: # auditctl -l | egrep '(usermod|groupmod)' If either "useradd" or "groupadd" are not listed with a permissions filter of at least "x", this is a finding. Determine if execution of the "userdel" and "groupdel" executable are audited: # auditctl -l | egrep '(userdel|groupdel)' If either "userdel" or "groupdel" are not listed with a permissions filter of at least "x", this is a finding. Determine if execution of "useradd" and "groupadd" are audited: # auditctl -l | egrep '(useradd|groupadd)' If either "useradd" or "groupadd" are not listed with a permissions filter of at least "x", this is a finding. Determine if execution of the passwd executable is audited: # auditctl -l | grep "/usr/bin/passwd" If "/usr/bin/passwd" is not listed with a permissions filter of at least "x", this is a finding. Determine if "/etc/passwd", "/etc/shadow", "etc/group", and "etc/security/opasswd" are audited for writing: # auditctl -l | egrep '(/etc/passwd|/etc/shadow|/etc/group|/etc/security/opasswd)' If any of these are not listed with a permissions filter of at least "w", this is a finding.

## Group: SRG-OS-000304-GPOS-00121

**Group ID:** `V-239594`

### Rule: The SLES for vRealize must notify System Administrators and Information System Security Officers when accounts are created, or enabled when previously disabled.

**Rule ID:** `SV-239594r852591_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply enable a new or disabled account. Notification of account enabling is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail, which documents the creation of SLES for vRealize user accounts and notifies System Administrators and Information System Security Officers (ISSO) that it exists. Such a process greatly reduces the risk that accounts will be surreptitiously enabled and provides logging that can be used for forensic purposes. In order to detect and respond to events that affect user accessibility and application processing, SLES for vRealize systems must audit account enabling actions and, as required, notify the appropriate individuals so they can investigate the event. To address access requirements, many operating systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if execution of the "usermod" and "groupmod" executable are audited: # auditctl -l | egrep '(usermod|groupmod)' If either "useradd" or "groupadd" are not listed with a permissions filter of at least "x", this is a finding. Determine if execution of the "userdel" and "groupdel" executable are audited: # auditctl -l | egrep '(userdel|groupdel)' If either "userdel" or "groupdel" are not listed with a permissions filter of at least "x", this is a finding. Determine if execution of "useradd" and "groupadd" are audited: # auditctl -l | egrep '(useradd|groupadd)' If either "useradd" or "groupadd" are not listed with a permissions filter of at least "x", this is a finding. Determine if execution of the "passwd" executable is audited: # auditctl -l | grep "/usr/bin/passwd" If "/usr/bin/passwd" is not listed with a permissions filter of at least "x", this is a finding. Determine if "/etc/passwd", "/etc/shadow", "/etc/group", and "/etc/security/opasswd" are audited for writing: # auditctl -l | egrep '(/etc/passwd|/etc/shadow|/etc/group|/etc/security/opasswd)' If any of these are not listed with a permissions filter of at least "w", this is a finding.

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-239595`

### Rule: The SLES for vRealize must audit the execution of privileged functions.

**Rule ID:** `SV-239595r852592_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that auditing of privileged command use is configured, run the following command to find relevant setuid programs: # find / -xdev -type f -perm -4000 -o -perm -2000 2>/dev/null Run the following command to verify entries in the audit rules for all programs found with the previous command: # grep path /etc/audit/audit.rules It should be the case that all relevant setuid programs have a line in the audit rules. If it is not the case, this is a finding.

## Group: SRG-OS-000329-GPOS-00128

**Group ID:** `V-239596`

### Rule: The SLES for vRealize must automatically lock an account until the locked account is released by an administrator when three unsuccessful logon attempts in 15 minutes occur.

**Rule ID:** `SV-239596r852593_rule`
**Severity:** low

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the "pam_tally2" configuration: # more /etc/pam.d/common-auth Confirm the following line is configured: auth required pam_tally2.so deny=3 onerr=fail even_deny_root unlock_ti me=86400 root_unlock_time=300 # more /etc/pam.d/common-account Confirm the following line is configured: account required pam_tally2.so If no such lines are found, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-239597`

### Rule: The SLES for vRealize must off-load audit records onto a different system or media from the system being audited.

**Rule ID:** `SV-239597r877390_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the syslog configuration file for remote syslog servers: # cat /etc/syslog-ng/syslog-ng.conf | grep logserver If no line is returned, or the "logserver" is commented out, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-239598`

### Rule: The SLES for vRealize must immediately notify the SA and ISSO (at a minimum) when allocated audit record storage volume reaches 75% of the repository maximum audit record storage capacity.

**Rule ID:** `SV-239598r877389_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches 75% utilization, they are unable to plan for audit record storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check "/etc/audit/auditd.conf" file for the "space_left_action" parameter with the following command: # cat /etc/audit/auditd.conf | grep space_left_action If the "space_left_action" parameter is missing, set to "ignore", set to "suspend", set to "single", set to "halt", or is blank, this is a finding Expected Result: space_left_action = SYSLOG Notes: If the "space_left_action" parameter is set to "exec" the system executes a designated script. If this script informs the SA of the event, this is not a finding. If the "space_left_action" parameter is set to "email" and the "action_mail_acct" parameter is not set to the email address of the system administrator, this is a finding. The "action_mail_acct" parameter, if missing, defaults to "root". Note that if the email address of the system administrator is on a remote system "sendmail" must be available.

## Group: SRG-OS-000344-GPOS-00135

**Group ID:** `V-239599`

### Rule: The SLES for vRealize must provide an immediate real-time alert to the SA and ISSO, at a minimum, of all audit failure events requiring real-time alerts.

**Rule ID:** `SV-239599r852596_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check "/etc/audit/auditd.conf" file for the "space_left_action" parameter with the following command: # cat /etc/audit/auditd.conf | grep space_left_action If the "space_left_action" parameter is missing, set to "ignore", set to "suspend", set to "single", set to "halt", or is blank, this is a finding Expected Result: space_left_action = SYSLOG Notes: If the "space_left_action" parameter is set to "exec" the system executes a designated script. If this script informs the SA of the event, this is not a finding. If the "space_left_action" parameter is set to "email" and the "action_mail_acct" parameter is not set to the email address of the system administrator, this is a finding. The "action_mail_acct" parameter, if missing, defaults to "root". Note that if the email address of the system administrator is on a remote system "sendmail" must be available.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-239600`

### Rule: The SLES for vRealize must, for networked systems, compare internal information system clocks at least every 24 hours with a server which is synchronized to one of the redundant United States Naval Observatory (USNO) time servers, or a time server designated for the appropriate DoD network (NIPRNet/SIPRNet), and/or the Global Positioning System (GPS).

**Rule ID:** `SV-239600r878121_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider endpoints that may not have regular access to the authoritative timeserver (e.g., mobile, teleworking, and tactical endpoints).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
A remote NTP server should be configured for time synchronization. To verify one is configured, open the following files: # cat /etc/ntp.conf | grep server | grep -v '^#' # cat /etc/ntp.conf | grep peer | grep -v '^#' # cat /etc/ntp.conf | grep multicastclient | grep -v '^#' Confirm the servers and peers or multicastclient (as applicable) are local or an authoritative U.S. DoD source. If a non-local/non-authoritative time-server is used, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-239601`

### Rule: The time synchronization configuration file (such as /etc/ntp.conf) must be owned by root.

**Rule ID:** `SV-239601r877038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A synchronized system clock is critical for the enforcement of time-based policies and the correlation of logs and audit records with other systems. If an illicit time source is used for synchronization, the integrity of system logs and the security of the system could be compromised. If the configuration files controlling time synchronization are not owned by a system account, unauthorized modifications could result in the failure of time synchronization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the ownership of the NTP configuration file: # ls -l /etc/ntp.conf If the owner is not "root", this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-239602`

### Rule: The time synchronization configuration file (such as /etc/ntp.conf) must be group-owned by root, bin, sys, or system.

**Rule ID:** `SV-239602r877038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A synchronized system clock is critical for the enforcement of time-based policies and the correlation of logs and audit records with other systems. If an illicit time source is used for synchronization, the integrity of system logs and the security of the system could be compromised. If the configuration files controlling time synchronization are not owned by a system group, unauthorized modifications could result in the failure of time synchronization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the group ownership of the NTP configuration file: # ls -lL /etc/ntp.conf If the group-owner is not "root", "bin", "sys", or "system", this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-239603`

### Rule: The time synchronization configuration file (such as /etc/ntp.conf) must have mode 0640 or less permissive.

**Rule ID:** `SV-239603r877038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A synchronized system clock is critical for the enforcement of time-based policies and the correlation of logs and audit records with other systems. If an illicit time source is used for synchronization, the integrity of system logs and the security of the system could be compromised. If the configuration files controlling time synchronization are not protected, unauthorized modifications could result in the failure of time synchronization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that the mode for the NTP configuration file is not more permissive than "0640": # ls -l /etc/ntp.conf If the mode is more permissive than "0640", this is a finding.

## Group: SRG-OS-000356-GPOS-00144

**Group ID:** `V-239604`

### Rule: The SLES for vRealize must synchronize internal information system clocks to the authoritative time source when the time difference is greater than one second.

**Rule ID:** `SV-239604r852601_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider setting time periods for different types of systems (e.g., financial, legal, or mission-critical systems). Organizations should also consider endpoints that may not have regular access to the authoritative timeserver (e.g., mobile, teleworking, and tactical endpoints). This requirement is related to the comparison done every 24 hours in SRG-OS-000355 because a comparison must be done in order to determine the time difference.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to determine the current status of the "ntpd" service: # service ntp status If the service is configured, the command should show a list of the ntp servers and the status of the synchronization. If nothing is returned, this is a finding. If the service is configured, but does not show a status of "on", this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-239605`

### Rule: The SLES for vRealize must notify designated personnel if baseline configurations are changed in an unauthorized manner.

**Rule ID:** `SV-239605r852602_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to the operating system. Changes to operating system configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of the SLES for vRealize. SLES for vRealize’s IMO/ISSO and SAs must be notified via email and/or monitoring system trap when there is an unauthorized modification of a configuration item.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLES for vRealize produces audit records by running the following command to determine the current status of the "auditd" service: # service auditd status If the service is enabled, the returned message must contain the following text: Checking for service auditd running If the service is not running, this is a finding.

## Group: SRG-OS-000365-GPOS-00152

**Group ID:** `V-239606`

### Rule: The SLES for vRealize must audit the enforcement actions used to restrict access associated with changes to the system.

**Rule ID:** `SV-239606r852603_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing the enforcement of access restrictions against changes to the application configuration, it will be difficult to identify attempted attacks and an audit trail will not be available for forensic investigation for after-the-fact actions. Enforcement actions are the methods or mechanisms used to prevent unauthorized changes to configuration settings. Enforcement action methods may be as simple as denying access to a file based on the application of file permissions (access restriction). Audit items may consist of lists of actions blocked by access restrictions or changes identified after the fact.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLES for vRealize produces audit records by running the following command to determine the current status of the "auditd" service: # service auditd status If the service is enabled, the returned message must contain the following text: Checking for service auditd running If the service is not running, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-239607`

### Rule: The RPM package management tool must cryptographically verify the authenticity of all software packages during installation.

**Rule ID:** `SV-239607r877463_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. Accordingly, patches, service packs, device drivers, or SLES for vRealize components must be signed with a certificate recognized and approved by the organization. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. SLES for vRealize should not have to verify the software again. This requirement does not mandate DoD certificates for this purpose; however, the certificate used to verify the software must be from an approved CA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify RPM signature validation is not disabled: # grep nosignature /usr/lib/rpm/rpmrc ~root/.rpmrc The result should either respond with no such file or directory, or an empty return. If any configuration is found, this is a finding.

## Group: SRG-OS-000392-GPOS-00172

**Group ID:** `V-239608`

### Rule: The SLES for vRealize must audit all activities performed during nonlocal maintenance and diagnostic sessions.

**Rule ID:** `SV-239608r852605_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If events associated with nonlocal administrative access or diagnostic sessions are not logged, a major tool for assessing and investigating attacks would not be available. This requirement addresses auditing-related issues associated with maintenance tools used specifically for diagnostic and repair actions on organizational information systems. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. This requirement applies to hardware/software diagnostic test equipment or tools. This requirement does not cover hardware/software components that may support information system maintenance, yet are a part of the system, for example, the software implementing "ping," "ls," "ipconfig," or the hardware and software implementing the monitoring port of an Ethernet switch.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all commands run by "root" are being audited with the following command: # cat /etc/audit/audit.rules | grep execve If the following lines are not displayed, this is a finding. -a exit,always -F arch=b64 -F euid=0 -S execve -a exit,always -F arch=b32 -F euid=0 -S execve

## Group: SRG-OS-000393-GPOS-00173

**Group ID:** `V-239609`

### Rule: The SLES for vRealize must implement cryptographic mechanisms to protect the integrity of nonlocal maintenance and diagnostic communications, when used for nonlocal maintenance sessions.

**Rule ID:** `SV-239609r877382_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Privileged access contains control and configuration information and is particularly sensitive, so additional protections are necessary. This is maintained by using cryptographic mechanisms, such as a hash function or digital signature, to protect integrity. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. The SLES for vRealize can meet this requirement through leveraging a cryptographic module. This requirement does not cover hardware/software components that may support information system maintenance, yet are a part of the system (e.g., the software implementing "ping," "ls," "ipconfig," or the hardware and software implementing the monitoring port of an Ethernet switch).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for DoD-approved encryption to protect the confidentiality of SSH remote connections by performing the following commands: Check the Cipher setting in the "sshd_config" file. # grep -i Ciphers /etc/ssh/sshd_config | grep -v '#' The output must contain either none or any number of the following algorithms: aes128-ctr, aes256-ctr. If the output contains an algorithm not listed above, this is a finding. Expected Output: Ciphers aes256-ctr,aes128-ctr

## Group: SRG-OS-000394-GPOS-00174

**Group ID:** `V-239610`

### Rule: The SLES for vRealize must implement cryptographic mechanisms to protect the confidentiality of nonlocal maintenance and diagnostic communications, when used for nonlocal maintenance sessions.

**Rule ID:** `SV-239610r877381_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Privileged access contains control and configuration information and is particularly sensitive, so additional protections are necessary. This is maintained by using cryptographic mechanisms such as encryption to protect confidentiality. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. This requirement applies to hardware/software diagnostic test equipment or tools. This requirement does not cover hardware/software components that may support information system maintenance, yet are a part of the system (e.g., the software implementing "ping," "ls," "ipconfig," or the hardware and software implementing the monitoring port of an Ethernet switch). The SLES for vRealize can meet this requirement through leveraging a cryptographic module.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for allowed MACs: # grep -i macs /etc/ssh/sshd_config | grep -v '^#' If no lines are returned, or the returned MACs list contains any MAC other than "hmac-sha1", this is a finding.

## Group: SRG-OS-000396-GPOS-00176

**Group ID:** `V-239611`

### Rule: The SLES for vRealize must implement NSA-approved cryptography to protect classified information in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.

**Rule ID:** `SV-239611r877380_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The SLES for vRealize must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for DoD-approved encryption to protect the confidentiality of SSH remote connections by performing the following commands: Check the Cipher setting in the "sshd_config" file. # grep -i Ciphers /etc/ssh/sshd_config | grep -v '#' The output must contain either none or any number of the following algorithms: aes128-ctr, aes256-ctr. If the output contains an algorithm not listed above, this is a finding. Expected Output: Ciphers aes256-ctr,aes128-ctr

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-239612`

### Rule: The SLES for vRealize must protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-239612r916422_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for DoD-approved encryption to protect the confidentiality of SSH remote connections by performing the following commands: Check the Cipher setting in the "sshd_config" file. # grep -i Ciphers /etc/ssh/sshd_config | grep -v '#' The output must contain either none or any number of the following algorithms: aes128-ctr, aes256-ctr. If the output contains an algorithm not listed above, this is a finding. Expected Output: Ciphers aes256-ctr,aes128-ctr

## Group: SRG-OS-000424-GPOS-00188

**Group ID:** `V-239613`

### Rule: The SLES for vRealize must implement cryptographic mechanisms to prevent unauthorized disclosure of information and/or detect changes to information during transmission unless otherwise protected by alternative physical safeguards, such as, at a minimum, a Protected Distribution System (PDS).

**Rule ID:** `SV-239613r878122_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Encrypting information for transmission protects information from unauthorized disclosure and modification. Cryptographic mechanisms implemented to protect information integrity include, for example, cryptographic hash functions that have common application in digital signatures, checksums, and message authentication codes. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, operating systems need to leverage transmission protection mechanisms such as TLS, SSL VPNs, or IPsec. Alternative physical protection measures include PDS. PDSs are used to transmit unencrypted classified National Security Information (NSI) through an area of lesser classification or control. Since the classified NSI is unencrypted, the PDS must provide adequate electrical, electromagnetic, and physical safeguards to deter exploitation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for allowed MACs: # grep -i macs /etc/ssh/sshd_config | grep -v '^#' If no lines are returned, or the returned MACs list contains any MAC other than "hmac-sha1", this is a finding.

## Group: SRG-OS-000433-GPOS-00192

**Group ID:** `V-239614`

### Rule: The SLES for vRealize must implement non-executable data to protect its memory from unauthorized code execution.

**Rule ID:** `SV-239614r852611_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in non-executable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can either be hardware-enforced or software-enforced with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The stock kernel has support for non-executable program stacks compiled in by default. Verify that the option was specified when the kernel was built: # grep -i "execute" /var/log/boot.msg The message: "NX (Execute Disable) protection: active" will be written in the boot log when compiled in the kernel. This is the default for x86_64. To activate this support, the "noexec=on" kernel parameter must be specified at boot time. Check for a message with the following command: # grep –i "noexec" /var/log/boot.msg The message: "Kernel command line: <boot parameters> noexec=on" will be written to the boot log when properly appended to the "/boot/grub/menu.lst" file. If non-executable program stacks have not been configured, this is a finding.

## Group: SRG-OS-000433-GPOS-00193

**Group ID:** `V-239615`

### Rule: The SLES for vRealize must implement address space layout randomization to protect its memory from unauthorized code execution.

**Rule ID:** `SV-239615r852612_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in non-executable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can either be hardware-enforced or software-enforced with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "randomize_va_space" has not been changed from the default "1" setting. # sysctl kernel.randomize_va_space If the return value is not "kernel.randomize_va_space = 1", this is a finding.

## Group: SRG-OS-000447-GPOS-00201

**Group ID:** `V-239616`

### Rule: The SLES for vRealize must shut down the information system, restart the information system, and/or notify the system administrator when anomalies in the operation of any security functions are discovered.

**Rule ID:** `SV-239616r852613_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If anomalies are not acted upon, security functions may fail to secure the system. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. Notifications provided by information systems include messages to local computer consoles, and/or hardware indications, such as lights. This capability must take into account operational requirements for availability for selecting an appropriate response. The organization may choose to shut down or restart the information system upon security function anomaly detection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the syslog configuration file for remote syslog servers: # cat /etc/syslog-ng/syslog-ng.conf | grep logserver If no line is returned, or the "logserver" is commented out, this is a finding.

## Group: SRG-OS-000458-GPOS-00203

**Group ID:** `V-239617`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to access security objects occur.

**Rule ID:** `SV-239617r662302_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that auditing is configured for system administrator actions, run the following command: # auditctl -l | grep "watch=/etc/sudoers" The result should return a rule for sudoers, such as: LIST_RULES: exit,always watch=/etc/sudoers perm=wa key=sudoers If there is no output, this is a finding.

## Group: SRG-OS-000461-GPOS-00205

**Group ID:** `V-239618`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to access categories of information (e.g., classification levels) occur.

**Rule ID:** `SV-239618r662305_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SLES for vRealize produces audit records by running the following command to determine the current status of the "auditd" service: # service auditd status If the service is enabled, the returned message must contain the following text: Checking for service auditd running If the service is not running, this is a finding.

## Group: SRG-OS-000462-GPOS-00206

**Group ID:** `V-239619`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to modify privileges occur.

**Rule ID:** `SV-239619r662308_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine if SLES for vRealize is configured to audit calls to the "chmod" system call, run the following command: # auditctl -l | grep syscall | grep chmod If the system is configured to audit this activity, it will return several lines, such as: LIST_RULES: exit,always arch=3221225534 (0xc000003e) auid=0 syscall=chmod,fchmod,chown,fchown,fchownat,fchmodat LIST_RULES: exit,always arch=3221225534 (0xc000003e) auid>=500 (0x1f4) auid!=-1 (0xffffffff) syscall=chmod,fchmod,chown,fchown,fchownat,fchmodat LIST_RULES: exit,always arch=1073741827 (0x40000003) syscall=chmod,lchown,sethostname,fchmod,fchown,adjtimex,init_module,delete_module,chown,lchown32,fchown32,chown32,setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr,clock_settime,fchownat,fchmodat If no lines are returned, this is a finding.

## Group: SRG-OS-000463-GPOS-00207

**Group ID:** `V-239620`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to modify security objects occur.

**Rule ID:** `SV-239620r662311_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that auditing is configured for system administrator actions, run the following command: # auditctl -l | grep "watch=/etc/sudoers" The result should return a rule for sudoers, such as: LIST_RULES: exit,always watch=/etc/sudoers perm=wa key=sudoers If there is no output, this is a finding.

## Group: SRG-OS-000465-GPOS-00209

**Group ID:** `V-239621`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to modify categories of information (e.g., classification levels) occur.

**Rule ID:** `SV-239621r662314_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SLES for vRealize produces audit records by running the following command to determine the current status of the "auditd" service: # service auditd status If the service is enabled, the returned message must contain the following text: Checking for service auditd running If the service is not running, this is a finding.

## Group: SRG-OS-000466-GPOS-00210

**Group ID:** `V-239622`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to delete privileges occur.

**Rule ID:** `SV-239622r662317_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine if SLES for vRealize is configured to audit calls to the "chmod" system call, run the following command: # auditctl -l | grep syscall | grep chmod If the system is configured to audit this activity, it will return several lines, such as: LIST_RULES: exit,always arch=3221225534 (0xc000003e) auid=0 syscall=chmod,fchmod,chown,fchown,fchownat,fchmodat LIST_RULES: exit,always arch=3221225534 (0xc000003e) auid>=500 (0x1f4) auid!=-1 (0xffffffff) syscall=chmod,fchmod,chown,fchown,fchownat,fchmodat LIST_RULES: exit,always arch=1073741827 (0x40000003) syscall=chmod,lchown,sethostname,fchmod,fchown,adjtimex,init_module,delete_module,chown,lchown32,fchown32,chown32,setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr,clock_settime,fchownat,fchmodat If no lines are returned, this is a finding.

## Group: SRG-OS-000467-GPOS-00211

**Group ID:** `V-239623`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to delete security levels occur.

**Rule ID:** `SV-239623r662320_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SLES for vRealize produces audit records by running the following command to determine the current status of the "auditd" service: # service auditd status If the service is enabled, the returned message must contain the following text: Checking for service auditd running If the service is not running, this is a finding.

## Group: SRG-OS-000468-GPOS-00212

**Group ID:** `V-239624`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful attempts to delete security objects occur.

**Rule ID:** `SV-239624r662323_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that auditing is configured for system administrator actions, run the following command: # auditctl -l | grep "watch=/etc/sudoers" The result should return a rule for sudoers, such as: LIST_RULES: exit,always watch=/etc/sudoers perm=wa key=sudoers If there is no output, this is a finding.

## Group: SRG-OS-000470-GPOS-00214

**Group ID:** `V-239625`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful logon attempts occur.

**Rule ID:** `SV-239625r662326_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The message types that are always recorded to the "/var/log/audit/audit.log" file include "LOGIN", "USER_LOGIN", "USER_START", "USER_END" among others and do not need to be added to audit.rules. The log files "/var/log/faillog", "/var/log/lastlog", and "/var/log/tallylog" must be protected from tampering of the login records: # egrep "faillog|lastlog|tallylog" /etc/audit/audit.rules If "/var/log/faillog", "/var/log/lastlog", and "/var/log/tallylog" entries do not exist, this is a finding.

## Group: SRG-OS-000471-GPOS-00215

**Group ID:** `V-239626`

### Rule: The SLES for vRealize must generate audit records for privileged activities or other system-level access.

**Rule ID:** `SV-239626r662329_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that auditing of privileged command use is configured, run the following command to find relevant setuid programs: # find / -xdev -type f -perm -4000 -o -perm -2000 2>/dev/null Run the following command to verify entries in the audit rules for all programs found with the previous command: # grep path /etc/audit/audit.rules It should be the case that all relevant setuid programs have a line in the audit rules. If it is not the case, this is a finding.

## Group: SRG-OS-000471-GPOS-00216

**Group ID:** `V-239627`

### Rule: The SLES for vRealize audit system must be configured to audit the loading and unloading of dynamic kernel modules.

**Rule ID:** `SV-239627r662332_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if "/sbin/insmod" is audited: # cat /etc/audit/audit.rules | grep "/sbin/insmod" If the result does not start with "-w" and contain "-p x", this is a finding.

## Group: SRG-OS-000472-GPOS-00217

**Group ID:** `V-239628`

### Rule: The SLES for vRealize must generate audit records showing starting and ending time for user access to the system.

**Rule ID:** `SV-239628r662335_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The message types that are always recorded to the "/var/log/audit/audit.log" file include "LOGIN", "USER_LOGIN", "USER_START", "USER_END" among others and do not need to be added to audit.rules. The log files "/var/log/faillog", "/var/log/lastlog", and "/var/log/tallylog" must be protected from tampering of the login records: # egrep "faillog|lastlog|tallylog" /etc/audit/audit.rules If "/var/log/faillog", "/var/log/lastlog", and "/var/log/tallylog" entries do not exist, this is a finding.

## Group: SRG-OS-000473-GPOS-00218

**Group ID:** `V-239629`

### Rule: The SLES for vRealize must generate audit records when concurrent logons to the same account occur from different sources.

**Rule ID:** `SV-239629r662338_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The message types that are always recorded to the "/var/log/audit/audit.log" file include "LOGIN", "USER_LOGIN", "USER_START", "USER_END" among others and do not need to be added to audit.rules. The log files "/var/log/faillog", "/var/log/lastlog", and "/var/log/tallylog" must be protected from tampering of the login records: # egrep "faillog|lastlog|tallylog" /etc/audit/audit.rules If "/var/log/faillog", "/var/log/lastlog", and "/var/log/tallylog" entries do not exist, this is a finding.

## Group: SRG-OS-000474-GPOS-00219

**Group ID:** `V-239630`

### Rule: The SLES for vRealize must generate audit records when successful/unsuccessful accesses to objects occur.

**Rule ID:** `SV-239630r662341_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SLES for vRealize produces audit records by running the following command to determine the current status of the "auditd" service: # service auditd status If the service is enabled, the returned message must contain the following text: Checking for service auditd running If the service is not running, this is a finding.

## Group: SRG-OS-000474-GPOS-00219

**Group ID:** `V-239631`

### Rule: The SLES for vRealize audit system must be configured to audit failed attempts to access files and programs.

**Rule ID:** `SV-239631r662344_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unsuccessful attempts to access files could be an indicator of malicious activity on a system. Auditing these events could serve as evidence of potential system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify auditd is configured to audit failed file access attempts. There must be both an "-F exit=-EPERM" and "-F exit=-EACCES" for each access syscall: # cat /etc/audit.rules /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S creat" | grep -e "-F exit=-EPERM" # cat /etc/audit.rules /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S creat" | grep -e "-F exit=-EACCES" There must be both an "-F exit=-EPERM" and "-F exit=-EACCES" for each access syscall. If not, this is a finding.

## Group: SRG-OS-000474-GPOS-00219

**Group ID:** `V-239632`

### Rule: The SLES for vRealize audit system must be configured to audit failed attempts to access files and programs.

**Rule ID:** `SV-239632r662347_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unsuccessful attempts to access files could be an indicator of malicious activity on a system. Auditing these events could serve as evidence of potential system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify auditd is configured to audit failed file access attempts. There must be both an "-F exit=-EPERM" and "-F exit=-EACCES" for each access syscall: # cat /etc/audit.rules /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S open" | grep -e "-F exit=-EPERM" # cat /etc/audit.rules /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S open" | grep -e "-F exit=-EACCES" There must be both an "-F exit=-EPERM" and "-F exit=-EACCES" for each access syscall. If not, this is a finding.

## Group: SRG-OS-000474-GPOS-00219

**Group ID:** `V-239633`

### Rule: The SLES for vRealize audit system must be configured to audit failed attempts to access files and programs.

**Rule ID:** `SV-239633r662350_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unsuccessful attempts to access files could be an indicator of malicious activity on a system. Auditing these events could serve as evidence of potential system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify auditd is configured to audit failed file access attempts. There must be an audit rule for each of the access syscalls logging all failed accesses (-F success=0) # cat /etc/audit.rules /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S openat" | grep -e "-F success=0" There must be an audit rule for each of the access syscalls logging all failed accesses (-F success=0). If not, this is a finding.

## Group: SRG-OS-000474-GPOS-00219

**Group ID:** `V-239634`

### Rule: The SLES for vRealize audit system must be configured to audit failed attempts to access files and programs.

**Rule ID:** `SV-239634r662353_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unsuccessful attempts to access files could be an indicator of malicious activity on a system. Auditing these events could serve as evidence of potential system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify auditd is configured to audit failed file access attempts. There must be an audit rule for each of the access syscalls logging all failed accesses (-F success=0) # cat /etc/audit.rules /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S truncate" | grep -e "-F success=0" There must be an audit rule for each of the access syscalls logging all failed accesses (-F success=0). If not, this is a finding.

## Group: SRG-OS-000474-GPOS-00219

**Group ID:** `V-239635`

### Rule: The SLES for vRealize audit system must be configured to audit failed attempts to access files and programs.

**Rule ID:** `SV-239635r662356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unsuccessful attempts to access files could be an indicator of malicious activity on a system. Auditing these events could serve as evidence of potential system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify auditd is configured to audit failed file access attempts. There must be an audit rule for each of the access syscalls logging all failed accesses (-F success=0) # cat /etc/audit.rules /etc/audit/audit.rules | grep -e "-a exit,always" | grep -e "-S ftruncate" | grep -e "-F success=0" There must be an audit rule for each of the access syscalls logging all failed accesses (-F success=0). If not, this is a finding.

## Group: SRG-OS-000474-GPOS-00219

**Group ID:** `V-239636`

### Rule: The SLES for vRealize audit system must be configured to audit user deletions of files and programs.

**Rule ID:** `SV-239636r662359_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing file deletions will create an audit trail for files that are removed from the system. The audit trail could aid in system troubleshooting, as well as detecting malicious processes that attempt to delete log files to conceal their presence.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine if SLES for vRealize is configured to audit calls to the "unlink" system call, run the following command: # auditctl -l | grep syscall | grep unlink | grep -v unlinkat If the system is configured to audit this activity, it will return several lines. To determine if the system is configured to audit calls to the "unlinkat" system call, run the following command: # auditctl -l | grep syscall | grep unlinkat If the system is configured to audit this activity, it will return several lines. To determine if the system is configured to audit calls to the "rename" system call, run the following command: # auditctl -l | grep syscall | grep rename | grep -v renameat If the system is configured to audit this activity, it will return several lines. To determine if the system is configured to audit calls to the "renameat" system call, run the following command: # auditctl -l | grep syscall | grep renameat If the system is configured to audit this activity, it will return several lines. If no line is returned, this is a finding.

## Group: SRG-OS-000474-GPOS-00219

**Group ID:** `V-239637`

### Rule: The SLES for vRealize audit system must be configured to audit file deletions.

**Rule ID:** `SV-239637r662362_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the SLES for vRealize system is not configured to audit certain activities and write them to an audit log, it is more difficult to detect and track system compromises and damages incurred during a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check SLES for vRealize audit configuration to determine if file and directory deletions are audited: # cat /etc/audit.rules /etc/audit/audit.rules | grep -e "-a exit,always" | grep -i "rmdir" If no results are returned or the results do not contain "-S rmdir", this is a finding.

## Group: SRG-OS-000474-GPOS-00219

**Group ID:** `V-239638`

### Rule: Audit logs must be rotated daily.

**Rule ID:** `SV-239638r662365_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Rotate audit logs daily to preserve audit file system space and to conform to the DISA requirement. If it is not rotated daily and moved to another location, then there is more of a chance for the compromise of audit data by malicious users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for a logrotate entry that rotates audit logs. # ls -l /etc/logrotate.d/audit If it exists, check for the presence of the daily rotate flag: # egrep "daily" /etc/logrotate.d/audit The command should produce a "daily" entry in the logrotate file for the audit daemon. If the daily entry is missing, this is a finding.

## Group: SRG-OS-000475-GPOS-00220

**Group ID:** `V-239639`

### Rule: The SLES for vRealize must generate audit records for all direct access to the information system.

**Rule ID:** `SV-239639r662368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The message types that are always recorded to the "/var/log/audit/audit.log" file include "LOGIN", "USER_LOGIN", "USER_START", "USER_END" among others and do not need to be added to audit.rules. The log files "/var/log/faillog", "/var/log/lastlog", and "/var/log/tallylog" must be protected from tampering of the login records: # egrep "faillog|lastlog|tallylog" /etc/audit/audit.rules If "/var/log/faillog", "/var/log/lastlog", and "/var/log/tallylog" entries do not exist, this is a finding.

## Group: SRG-OS-000476-GPOS-00221

**Group ID:** `V-239640`

### Rule: The SLES for vRealize must generate audit records for all account creations, modifications, disabling, and termination events.

**Rule ID:** `SV-239640r662371_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if execution of the "usermod" and "groupmod" executable are audited: # auditctl -l | egrep '(usermod|groupmod)' If either "useradd" or "groupadd" are not listed with a permissions filter of at least "x", this is a finding. Determine if execution of the "userdel" and "groupdel" executable are audited: # auditctl -l | egrep '(userdel|groupdel)' If either "userdel" or "groupdel" are not listed with a permissions filter of at least "x", this is a finding. Determine if execution of "useradd" and "groupadd" are audited: # auditctl -l | egrep '(useradd|groupadd)' If either "useradd" or "groupadd" are not listed with a permissions filter of at least "x", this is a finding. Determine if execution of the passwd executable is audited: # auditctl -l | grep "/usr/bin/passwd" If "/usr/bin/passwd" is not listed with a permissions filter of at least "x", this is a finding. Determine if "/etc/passwd", "/etc/shadow", "/etc/group", and "/etc/security/opasswd" are audited for writing: # auditctl -l | egrep '(/etc/passwd|/etc/shadow|/etc/group|/etc/security/opasswd)' If any of these are not listed with a permissions filter of at least "w", this is a finding.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-239641`

### Rule: The SLES for vRealize must generate audit records for all kernel module load, unload, and restart actions, and also for all program initiations.

**Rule ID:** `SV-239641r662374_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if "/sbin/insmod" is audited: # cat /etc/audit/audit.rules | grep "/sbin/insmod" If the result does not start with "-w" and contain "-p x", this is a finding.

## Group: SRG-OS-000478-GPOS-00223

**Group ID:** `V-239642`

### Rule: The SLES for vRealize must implement NIST FIPS-validated cryptography for the following: to provision digital signatures, to generate cryptographic hashes, and to protect unclassified information requiring confidentiality and cryptographic protection in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.

**Rule ID:** `SV-239642r878123_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The SLES for vRealize must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the SSH daemon configuration for allowed MACs: # grep -i macs /etc/ssh/sshd_config | grep -v '^#' If no lines are returned, or the returned MACs list contains any MAC other than "hmac-sha1", this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-239643`

### Rule: The SLES for vRealize must, at a minimum, off-load interconnected systems in real time and off-load standalone systems weekly.

**Rule ID:** `SV-239643r852615_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the syslog configuration file for remote syslog servers: # cat /etc/syslog-ng/syslog-ng.conf | grep logserver If no line is returned, or the "logserver" is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-239644`

### Rule: The SLES for vRealize must prevent the use of dictionary words for passwords.

**Rule ID:** `SV-239644r662383_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SLES for vRealize system allows the user to select passwords based on dictionary words, then this increases the chances of password compromise by increasing the opportunity for successful guesses and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check "/etc/pam.d/common-password" for "pam_cracklib" configuration: # grep pam_cracklib /etc/pam.d/common-password* If "pam_cracklib" is not present, this is a finding. Ensure the passwd command uses the common-password settings. # grep common-password /etc/pam.d/passwd If a line "password include common-password" is not found then the password checks in common-password will not be applied to new passwords, this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-239645`

### Rule: The SLES for vRealize must prevent the use of dictionary words for passwords.

**Rule ID:** `SV-239645r662386_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SLES for vRealize allows the user to select passwords based on dictionary words, then this increases the chances of password compromise by increasing the opportunity for successful guesses and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the module "pam_cracklib.so" is present. Procedure: # ls /lib/security/ Confirm that "pam_cracklib.so" is present in the directory listing. If "pam_cracklib.so" is not present, this is a finding. Verify the file "/etc/pam.d/common-password" is configured. Procedure: # grep pam_cracklib /etc/pam.d/common-password* If a line containing "password required pam_cracklib.so" is not present, this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-239646`

### Rule: The SLES for vRealize must prevent the use of dictionary words for passwords.

**Rule ID:** `SV-239646r662389_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SLES for vRealize allows the user to select passwords based on dictionary words, then this increases the chances of password compromise by increasing the opportunity for successful guesses and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "passwd" command uses the "common-password" settings. Procedure: # grep common-password /etc/pam.d/passwd If line "password include common-password" is not found then the password checks in common-password will not be applied to new passwords, and this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-239647`

### Rule: The SLES for vRealize must enforce a delay of at least 4 seconds between logon prompts following a failed logon attempt.

**Rule ID:** `SV-239647r662392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of logon attempts over a certain time interval reduces the chances that an unauthorized user may gain access to an account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the value of the "FAIL_DELAY" variable and the ability to use it: # grep FAIL_DELAY /etc/login.defs The following result should be displayed: FAIL_DELAY 4 If the value does not exist, or is less than "4", this is a finding. Check for the use of "pam_faildelay": # grep pam_faildelay /etc/pam.d/common-auth* The following result should be displayed: /etc/pam.d/common-auth:auth optional pam_faildelay.so If the "pam_faildelay.so" module is not listed or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-239648`

### Rule: The SLES for vRealize must enforce a delay of at least 4 seconds between logon prompts following a failed logon attempt.

**Rule ID:** `SV-239648r662395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of logon attempts over a certain time interval reduces the chances that an unauthorized user may gain access to an account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SLES for vRealize enforces a delay of at least "4" seconds between logon prompts following a failed logon attempt. Review the file "/etc/login.defs" and verify the parameter "FAIL_DELAY" is a value of "4" or greater. Procedure: # grep FAIL_DELAY /etc/login.defs The typical configuration looks something like this: FAIL_DELAY 4 If the parameter "FAIL_DELAY" does not exists, or is less than "4", this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-239649`

### Rule: The SLES for vRealize must enforce a delay of at least 4 seconds between logon prompts following a failed logon attempt.

**Rule ID:** `SV-239649r662398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of logon attempts over a certain time interval reduces the chances that an unauthorized user may gain access to an account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLES for vRealize enforces a delay of at least "4" seconds between logon prompts following a failed logon attempt. Verify the use of the "pam_faildelay" module. Procedure: # grep pam_faildelay /etc/pam.d/common-auth* The typical configuration looks something like this: #delay is in micro seconds auth required pam_faildelay.so delay=4000000 If the line is not present, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-239650`

### Rule: The SLES for vRealize must be configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs.

**Rule ID:** `SV-239650r662401_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLES for vRealize is configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs. If it is not, this is a finding.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-239651`

### Rule: The SLES for vRealize must define default permissions for all authenticated users in such a way that the user can only read and modify their own files.

**Rule ID:** `SV-239651r662404_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the most restrictive default permissions ensures that when new accounts are created they do not have unnecessary access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for the configured umask value in login.defs with the following command: # grep UMASK /etc/login.defs If the default umask is not "077", this a finding. Note: If the default umask is "000" or allows for the creation of world-writable files this becomes a CAT I finding.

## Group: SRG-OS-000480

**Group ID:** `V-258448`

### Rule: The version of vRealize Operations Manager 6.x SLES running on the system must be a supported version.

**Rule ID:** `SV-258448r928863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions used to install patches across the enclave and to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs). </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
vRealize Operations Manager 6.x SLES is no longer supported by the vendor. If the system is running vRealize Operations Manager 6.x SLES, this is a finding.

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-258512`

### Rule: Any publicly accessible connection to the SLES for vRealize must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the system.

**Rule ID:** `SV-258512r929628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible SLES for vRealize ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check issue file to verify that it contains one of the DoD required banners. # cat /etc/issue "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." If it does not, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-258513`

### Rule: The SLES for vRealize audit system must be configured to audit all administrative, privileged, and security actions.

**Rule ID:** `SV-258513r929631_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the operating system will provide an audit record generation capability as the following: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the auditing configuration of the system: # cat /etc/audit/audit.rules | grep -i "auditd.conf" If no results are returned, or the line does not start with "-w", this is a finding. Expected Result: -w /etc/audit/auditd.conf

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-258514`

### Rule: The SLES for vRealize audit system must be configured to audit all attempts to alter system time through adjtimex.

**Rule ID:** `SV-258514r929634_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the SLES for vRealize is capable of generating audit records. DoD has defined the list of events for which the operating system will provide an audit record generation capability as the following: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if SLES for vRealize system is configured to audit calls to the "adjtimex" system call, run the following command: # grep -w "adjtimex" /etc/audit/audit.rules If SLES for vRealize is configured to audit time changes, it will return at least two lines containing "-S adjtimex" that also contain "arch=b64". If no line is returned, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-258515`

### Rule: The SLES for vRealize audit system must be configured to audit all attempts to alter system time through settimeofday.

**Rule ID:** `SV-258515r929637_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the SLES for vRealize is capable of generating audit records. DoD has defined the list of events for which the operating system will provide an audit record generation capability as the following: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if SLES for vRealize is configured to audit calls to the "settimeofday" system call, run the following command: # grep -w "settimeofday" /etc/audit/audit.rules If SLES for vRealize is configured to audit this activity, it will return at least two lines containing "-S settimeofday" that also contain "arch=b64". If no line is returned, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-258516`

### Rule: The SLES for vRealize audit system must be configured to audit all attempts to alter system time through stime.

**Rule ID:** `SV-258516r929640_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the SLES for vRealize is capable of generating audit records. DoD has defined the list of events for which the SLES for vRealize will provide an audit record generation capability as the following: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if SLES for vRealize is configured to audit calls to the "settimeofday" system call, run the following command: # grep -w "stime" /etc/audit/audit.rules If SLES for vRealize is configured to audit this activity, it will return at least two lines containing "-S settimeofday" that also contain "arch=b64". If no line is returned, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-258517`

### Rule: The SLES for vRealize audit system must be configured to audit all attempts to alter system time through clock_settime.

**Rule ID:** `SV-258517r929643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the SLES for vRealize is capable of generating audit records. DoD has defined the list of events for which the operating system will provide an audit record generation capability as the following: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if SLES for vRealize is configured to audit calls to the "clock_settime" system call, run the following command: # grep -w "clock_settime" /etc/audit/audit.rules If SLES for vRealize is configured to audit this activity, it will return at least a line containing "-S clock_settime" that also contain "arch=b64". If no line is returned, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-258518`

### Rule: The SLES for vRealize audit system must be configured to audit all attempts to alter system time through /etc/localtime.

**Rule ID:** `SV-258518r929646_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the SLES for vRealize is capable of generating audit records. DoD has defined the list of events for which the SLES for vRealize will provide an audit record generation capability as the following: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine if SLES for vRealize is configured to audit attempts to alter time via the /etc/localtime file, run the following command: # auditctl -l | grep "watch=/etc/localtime" If SLES for vRealize is configured to audit this activity, it will return a line. LIST_RULES: exit,always watch=/etc/localtime perm=wa key=localtime If no line is returned, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-258519`

### Rule: The SLES for vRealize audit system must be configured to audit all attempts to alter the system through sethostname.

**Rule ID:** `SV-258519r929649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the SLES for vRealize is capable of generating audit records. DoD has defined the list of events for which the SLES for vRealize will provide an audit record generation capability as the following: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if SLES for vRealize is configured to audit calls to the "sethostname" system call, run the following command: # grep -w "sethostname" /etc/audit/audit.rules If SLES for vRealize is configured to audit this activity, it will return at least one line. If no line is returned, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-258520`

### Rule: The SLES for vRealize audit system must be configured to audit all attempts to alter the system through setdomainname.

**Rule ID:** `SV-258520r929652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the SLES for vRealize will provide an audit record generation capability as the following: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if SLES for vRealize is configured to audit calls to the "sethostname" system call, run the following command: # grep -w "setdomainname" /etc/audit/audit.rules If SLES for vRealize is configured to audit this activity, it will return a line. If no line is returned, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-258521`

### Rule: The SLES for vRealize must be configured to audit all attempts to alter the system through sched_setparam.

**Rule ID:** `SV-258521r929655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the SLES for vRealize will provide an audit record generation capability as the following: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if SLES for vRealize is configured to audit calls to the "sethostname" system call, run the following command: # grep -w "sched_setparam" /etc/audit/audit.rules If SLES for vRealize is configured to audit this activity, it will return a line. If no line is returned, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-258522`

### Rule: The SLES for vRealize must be configured to audit all attempts to alter the system through sched_setscheduler.

**Rule ID:** `SV-258522r929658_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the SLES for vRealize will provide an audit record generation capability as the following: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if SLES for vRealize is configured to audit calls to the "sethostname" system call, run the following command: # grep -w "sched_setscheduler" /etc/audit/audit.rules If SLES for vRealize is configured to audit this activity, it will return a line. If no line is returned, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-258523`

### Rule: The SLES for vRealize must be configured to audit all attempts to alter /var/log/faillog.

**Rule ID:** `SV-258523r929661_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the SLES for vRealize will provide an audit record generation capability as the following: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that attempts to alter the log files /var/log/faillog are audited: # egrep "faillog" /etc/audit/audit.rules If "-w /var/log/faillog -p wa" entry does not exist, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-258524`

### Rule: The SLES for vRealize must be configured to audit all attempts to alter /var/log/lastlog.

**Rule ID:** `SV-258524r929664_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the SLES for vRealize will provide an audit record generation capability as the following: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that attempts to alter the log files /var/log/lastlog are audited: # egrep "lastlog" /etc/audit/audit.rules If "-w /var/log/lastlog -p wa" entry does not exist, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-258525`

### Rule: The SLES for vRealize must be configured to audit all attempts to alter /var/log/tallylog.

**Rule ID:** `SV-258525r929667_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the SLES for vRealize will provide an audit record generation capability as the following: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that attempts to alter the log files /var/log/tallylog are audited: # egrep "tallylog" /etc/audit/audit.rules If "-w /var/log/tallylog -p wa" entry does not exist, this is a finding.

