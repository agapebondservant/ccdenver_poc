# STIG Benchmark: Nutanix AOS 5.20.x OS Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000027-GPOS-00008

**Group ID:** `V-254120`

### Rule: Nutanix AOS must limit the number of concurrent sessions to ten for all accounts and/or account types.

**Rule ID:** `SV-254120r958398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Operating system management includes the ability to control the number of users and user sessions that utilize an operating system. Limiting the number of allowed users and sessions per user is helpful in reducing the risks related to DoS attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions must be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Nutanix AOS limits the number of concurrent sessions to "10" or less for all accounts and/or account types by issuing the following command: $ sudo grep "maxlogins" /etc/security/limits.conf If the line * hard maxlogins 10, is missing or set to a number more than 10, this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-254121`

### Rule: Nutanix AOS must disconnect a session after 15 minutes of idle time for all connection types.

**Rule ID:** `SV-254121r958402_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. The operating system session lock event must include an obfuscation of the display screen so as to prevent other users from reading what was previously displayed. Publicly viewable images can include static or dynamic images, for example, patterns used with screen savers, photographic images, solid colors, a clock, a battery life indicator, or a blank screen, with the additional caveat that none of the images convey sensitive information. Satisfies: SRG-OS-000029-GPOS-00010, SRG-OS-000030-GPOS-00011, SRG-OS-000031-GPOS-00012</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured for autologout after 15 minutes of idle time. $ sudo grep -i tmout /etc/profile.d/* /etc/profile.d/os-security.sh:readonly TMOUT=900 If "TMOUT" is not set to "900" or less in a script located in the /etc/profile.d/ directory to enforce session termination after inactivity, this is a finding.

## Group: SRG-OS-000279-GPOS-00109

**Group ID:** `V-254122`

### Rule: Nutanix AOS must automatically terminate a user session after inactivity time-outs have expired or at shutdown.

**Rule ID:** `SV-254122r958636_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination addresses the termination of user-initiated logical sessions in contrast to the termination of network connections associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination terminates all processes associated with a user's logical session except those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific operating system functionality where the system owner, data owner, or organization requires additional assurance. Satisfies: SRG-OS-000279-GPOS-00109, SRG-OS-000126-GPOS-00066, SRG-OS-000163-GPOS-00072</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to auto disconnect remote session to prevent session hijacking. $ sudo grep -i clientalive /etc/ssh/sshd_config ClientAliveInterval 600 ClientAliveCountMax 0 If ClientAliveInterval is not "600" and ClientAliveCountMax is not "0", this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-254123`

### Rule: Nutanix AOS must monitor remote access methods.

**Rule ID:** `SV-254123r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyberattacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS monitors remote access methods. $ sudo grep -i loglevel /etc/ssh/sshd_config If the LogLevel is not set to "VERBOSE", this is a finding.

## Group: SRG-OS-000297-GPOS-00115

**Group ID:** `V-254124`

### Rule: Nutanix AOS must control remote access methods.

**Rule ID:** `SV-254124r958672_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Operating system functionality (e.g., RDP) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS prohibits or restricts the use of remote access methods, using the iptables firewall service. $ sudo service iptables status iptables.service - IPv4 firewall with iptables Loaded: loaded (/usr/lib/systemd/system/iptables.service; enabled; vendor preset: disabled) Active: active (exited) since Mon 2021-08-02 15:02:12 CDT; 2 weeks 6 days ago Main PID: 1250 (code=exited, status=0/SUCCESS) CGroup: /system.slice/iptables.service If IPv6 is in use: $ sudo service ip6tables status ip6tables.service - IPv6 firewall with ip6tables Loaded: loaded (/usr/lib/systemd/system/ip6tables.service; enabled; vendor preset: disabled) Active: active (exited) since Mon 2021-08-02 15:02:12 CDT; 2 weeks 6 days ago Main PID: 1313 (code=exited, status=0/SUCCESS) CGroup: /system.slice/ip6tables.service If no iptables services are "Loaded" and "Active", this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-254125`

### Rule: Nutanix AOS must implement DoD-approved encryption to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-254125r958408_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection (e.g., RDP), thereby providing a degree of confidentiality. The encryption strength of a mechanism is selected based on the security categorization of the information. Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000250-GPOS-00093, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174, SRG-OS-000125-GPOS-00065, SRG-OS-000424-GPOS-00188</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Inspect the "Ciphers" configuration with the following command: $ sudo grep -i ciphers /etc/ssh/sshd_config Ciphers aes256-ctr If any ciphers other than "aes256-ctr" are listed, the "Ciphers" keyword is missing, or the returned line is commented out, this is a finding.

## Group: SRG-OS-000002-GPOS-00002

**Group ID:** `V-254126`

### Rule: Nutanix AOS must automatically remove or disable temporary user accounts after 72 hours.

**Rule ID:** `SV-254126r958364_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If temporary user accounts remain active when no longer needed or for an excessive period, these accounts may be used to gain unauthorized access. To mitigate this risk, automated termination of all temporary accounts must be set upon account creation. Temporary accounts are established as part of normal account activation procedures when there is a need for short-term accounts without the demand for immediacy in account activation. If temporary accounts are used, the operating system must be configured to automatically terminate these types of accounts after a DoD-defined time period of 72 hours. To address access requirements, many operating systems may be integrated with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000002-GPOS-00002, SRG-OS-000123-GPOS-00064</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Nutanix AOS does not natively support temporary user accounts, named or otherwise. However, if temporary accounts are created, they must be configured to automatically terminate these types of accounts after a DoD-defined time period of 72 hours. Verify that temporary accounts have been provisioned with an expiration date of 72 hours. For every existing temporary account, run the following command to obtain its account expiration information. $ sudo chage -l system_account_name Verify each of these accounts has an expiration date set within 72 hours. If any temporary accounts have no expiration date set or do not expire within 72 hours, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-254127`

### Rule: Nutanix AOS must audit all account actions.

**Rule ID:** `SV-254127r958368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create an account. Auditing account creation actions provides logging that can be used for forensic purposes. To address access requirements, many operating systems may be integrated with enterprise level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Nutanix AOS is configured to audit all account creations. Run the following command to verify account creation and modification is audited. $ sudo auditctl -l | grep "audit_account_changes" If the command does not return the following output, this is a finding. -w /etc/group -p wa -k audit_account_changes -w /etc/passwd -p wa -k audit_account_changes -w /etc/gshadow -p wa -k audit_account_changes -w /etc/shadow -p wa -k audit_account_changes -w /etc/security/opasswd -p wa -k audit_account_changes

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-254128`

### Rule: Nutanix AOS must be configured with an encrypted boot password for root.

**Rule ID:** `SV-254128r958472_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to enforce approved authorizations for logical access to information and system resources. $ sudo grep -i password /boot/grub/grub.conf password [superusers-account] [password-hash] If the root password entry does not begin with "password", this is a finding. $ sudo grep -i execstart /usr/lib/systemd/system/rescue.service | grep -i sulogin ExecStart=-/bin/sh -c "/usr/sbin/sulogin; /usr/bin/systemctl --fail --no-block default" If "ExecStart" does not have "/usr/sbin/sulogin" as an option, this is a finding.

## Group: SRG-OS-000312-GPOS-00122

**Group ID:** `V-254129`

### Rule: Nutanix AOS must enforce discretionary access control on symlinks and hardlinks.

**Rule ID:** `SV-254129r958702_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled file permissions. When discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control. Satisfies: SRG-OS-000312-GPOS-00122, SRG-OS-000312-GPOS-00123, SRG-OS-000312-GPOS-00124</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS enforces discretionary access control on symlinks and hardlinks. $ sudo sysctl fs.protected_symlinks fs.protected_symlinks = 1 If "fs.protected_symlinks" is not set to "1" or is missing, this is a finding. Check the status of the fs.protected_hardlinks kernel parameter. $ sudo sysctl fs.protected_hardlinks fs.protected_hardlinks = 1 If "fs.protected_hardlinks" is not set to "1" or is missing, this is a finding.

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-254130`

### Rule: Nutanix AOS must audit the execution of privileged functions.

**Rule ID:** `SV-254130r958732_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to audit the misuse of privileged commands. $ sudo grep -iw execve /etc/audit/audit.rules -a always,exit -F arch=b32 -S execve -C uid!=euid -F euid=0 -k setuid -a always,exit -F arch=b64 -S execve -C uid!=euid -F euid=0 -k setuid -a always,exit -F arch=b32 -S execve -C gid!=egid -F egid=0 -k setgid -a always,exit -F arch=b64 -S execve -C gid!=egid -F egid=0 -k setgid If both the "b32" and "b64" audit rules for "SUID" files are not defined, this is a finding. If both the "b32" and "b64" audit rules for "SGID" files are not defined, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-254131`

### Rule: Nutanix AOS must enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period.

**Rule ID:** `SV-254131r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm that Nutanix AOS locks an account for a minimum of 15 minutes after three unsuccessful logon attempts within a period of 15 minutes with the following command: $ sudo grep pam_faillock.so /etc/pam.d/password-auth auth required pam_faillock.so preauth silent audit deny=3 even_deny_root unlock_time=900 root_unlock_time=900 fail_interval=900 auth [default=die] pam_faillock.so authfail audit deny=3 even_deny_root unlock_time=900 root_unlock_time=900 fail_interval=900 If the "deny" parameter is set to "0" or a value greater than "3" on both "auth" lines with the "pam_faillock.so" module, or is missing from these lines, this is a finding. If the "even_deny_root" parameter is not set on both "auth" lines with the "pam_faillock.so" module, or is missing from these lines, this is a finding. If the "fail_interval" parameter is set to "0" or is set to a value less than "900" on both "auth" lines with the "pam_faillock.so" module, or is missing from these lines, this is a finding. If the "unlock_time" parameter is not set to "0", "never", or is set to a value less than "900" on both "auth" lines with the "pam_faillock.so" module, or is missing from these lines, this is a finding. Note: The maximum configurable value for "unlock_time" is "604800". If any line referencing the "pam_faillock.so" module is commented out, this is a finding. $ sudo grep pam_faillock.so /etc/pam.d/system-auth auth required pam_faillock.so preauth silent audit deny=3 even_deny_root fail_interval=900 unlock_time=900 auth [default=die] pam_faillock.so authfail audit deny=3 even_deny_root fail_interval=900 unlock_time=900 account required pam_faillock.so If the "deny" parameter is set to "0" or a value greater than "3" on both "auth" lines with the "pam_faillock.so" module, or is missing from these lines, this is a finding. If the "even_deny_root" parameter is not set on both "auth" lines with the "pam_faillock.so" module, or is missing from these lines, this is a finding. If the "fail_interval" parameter is set to "0" or is set to a value less than "900" on both "auth" lines with the "pam_faillock.so" module, or is missing from these lines, this is a finding. If the "unlock_time" parameter is not set to "0", "never", or is set to a value less than "900" on both "auth" lines with the "pam_faillock.so" module or is missing from these lines, this is a finding. Note: The maximum configurable value for "unlock_time" is "604800". If any line referencing the "pam_faillock.so" module is commented out, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-254132`

### Rule: Nutanix AOS must be configured to display the Standard Mandatory DoD Notice and Consent Banner before granting access.

**Rule ID:** `SV-254132r958390_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000024-GPOS-00007</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Standard Mandatory DoD Notice and Consent Banner is configured. Verify that SSH is configured to display the Standard Mandatory DoD Notice Consent Banner: $ sudo grep -i banner /etc/ssh/sshd_config banner /etc/issue If "banner" is not set or is commented out, this is a finding.

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-254133`

### Rule: Any publicly accessible connection to Nutanix AOS must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the system.

**Rule ID:** `SV-254133r958586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to use the Standard Mandatory DoD Notice and Consent Banner. $ sudo more /etc/issue The command should return the following text: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the operating system does not display a graphical logon banner or the banner does not match the Standard Mandatory DoD Notice and Consent Banner, this is a finding. If the text in the "/etc/issue" file does not match the Standard Mandatory DoD Notice and Consent Banner, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-254134`

### Rule: Nutanix AOS must provide audit record generation capability for DoD-defined auditable events for successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels).

**Rule ID:** `SV-254134r958442_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the operating system will provide an audit record generation capability as: Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to generate audit records on all successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels). $ sudo grep -w "postdrop" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/postdrop -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -w "postqueue" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/postqueue -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -w "semanage" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/semanage -F perm=x -F auid>=1000 -F auid!=4294967295 -k secobjects $ sudo grep -w "setfiles" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/setfiles -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-priv_change $ sudo grep -w "userhelper" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/userhelper -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-passwd $ sudo grep -w "setsebool" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/setsebool -F perm=x -F auid>=1000 -F auid!=4294967295 -k secobjects $ sudo grep -w "unix_chkpwd" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/unix_chkpwd -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -w faillock /etc/audit/audit.rules -w /var/run/faillock/ -p wa -k logins $ sudo grep -w lastlog /etc/audit/audit.rules -w /var/log/lastlog -p wa -k logins If the command(s) does not return the appropriate response line, as indicated above, or if the line(s) is commented out, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-254135`

### Rule: Nutanix AOS must provide audit record generation capability for DoD-defined auditable events for system and account management actions.

**Rule ID:** `SV-254135r958442_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the operating system will provide an audit record generation capability as: Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS auditing is configured to generate audit records for all access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system. $ sudo yum list installed audit Installed Packages audit.x86_64 $ sudo grep -w chcon /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chcon -F perm=x -F auid>=1000 -F auid!=4294967295 -k secobjects $ sudo grep ssh-agent /etc/audit/audit.rules -a always,exit -F path=/usr/bin/ssh-agent -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -w /usr/bin/mount /etc/audit/audit.rules -a always,exit -F path=/usr/bin/mount -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -w /usr/bin/umount /etc/audit/audit.rules -a always,exit -F path=/usr/bin/umount -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep ssh-keysign /etc/audit/audit.rules -a always,exit -F path=/usr/libexec/openssh/ssh-keysign -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -w pam_timestamp_check /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/pam_timestamp_check -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -w crontab /etc/audit/audit.rules -a always,exit -F path=/usr/bin/crontab -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -w chsh /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chsh -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged If the command(s) does not return the appropriate response line, as indicated above, or if the line(s) is commented out, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-254136`

### Rule: Nutanix AOS must provide audit record generation capability for DoD-defined auditable events for file attribute management actions.

**Rule ID:** `SV-254136r958442_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the operating system will provide an audit record generation capability as: Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS auditing is configured to generate audit records for all access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system. $ sudo grep -w lremovexattr /etc/audit/audit.rules -a always,exit -F arch=b64 -S lremovexattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S lremovexattr -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S lremovexattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S lremovexattr -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w removexattr /etc/audit/audit.rules -a always,exit -F arch=b64 -S removexattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S removexattr -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S removexattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S removexattr -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w lsetxattr /etc/audit/audit.rules -a always,exit -F arch=b64 -S lsetxattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S lsetxattr-F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S lsetxattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S lsetxattr -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w fsetxattr /etc/audit/audit.rules -a always,exit -F arch=b64 -S fsetxattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S fsetxattr-F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S fsetxattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S fsetxattr -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w fremovexattr /etc/audit/audit.rules -a always,exit -F arch=b64 -S fremovexattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S fremovexattr -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S fremovexattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S fremovexattr -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w setxattr /etc/audit/audit.rules -a always,exit -F arch=b64 -S setxattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S setxattr -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S setxattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S setxattr -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete If the command(s) does not return the appropriate response line, as indicated above, or if the line(s) is commented out, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-254137`

### Rule: Nutanix AOS must provide audit record generation capability for DoD-defined auditable events for system module management actions.

**Rule ID:** `SV-254137r958442_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the operating system will provide an audit record generation capability as: Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS auditing is configured to generate audit records for all access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system. $ sudo grep -w "init_module" /etc/audit/audit.rules -a always,exit -F arch=b64 -S init_module -k audit_network_modifications_modules -a always,exit -F arch=b32 -S init_module -k audit_network_modifications_modules -a always,exit -F arch=b64 -S init_module -S delete_module -k modules -a always,exit -F arch=b32 -S init_module -S delete_module -k modules $ sudo grep -w "finit_module" /etc/audit/audit.rules -a always,exit -F arch=b32 -S finit_module -k module-change -a always,exit -F arch=b64 -S finit_module -k module-change $ sudo grep -w "delete_module" /etc/audit/audit.rules -a always,exit -F arch=b64 -S delete_module -k audit_network_modifications_modules -a always,exit -F arch=b32 -S delete_module -k audit_network_modifications_modules -a always,exit -F arch=b64 -S delete_module -k modules -a always,exit -F arch=b32 -S delete_module -k modules If the command(s) does not return the appropriate response line, as indicated above, or if the line(s) is commented out, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-254138`

### Rule: Nutanix AOS must provide audit record generation capability for DoD-defined auditable events for directory and permissions management actions.

**Rule ID:** `SV-254138r958442_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the operating system will provide an audit record generation capability as: Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS auditing is configured to generate audit records for all access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system. $ sudo grep -w "\-S mount" /etc/audit/audit.rules -a always,exit -F arch=b64 -S mount -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S mount -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S mount -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S mount -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w "rename" /etc/audit/audit.rules -a always,exit -F arch=b64 -S rename -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S rename -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S rename -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S rename -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w "renameat" /etc/audit/audit.rules -a always,exit -F arch=b64 -S renameat -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S renameat -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S renameat -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S renameat -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w "rmdir" /etc/audit/audit.rules -a always,exit -F arch=b64 -S rmdir -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S rmdir -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S rmdir -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S rmdir -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w "unlink" /etc/audit/audit.rules -a always,exit -F arch=b64 -S unlink -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S unlink -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S unlink -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S unlink -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w "unlinkat" /etc/audit/audit.rules -a always,exit -F arch=b64 -S unlinkat -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S unlinkat -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S unlinkat -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S unlinkat -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w chown /etc/audit/audit.rules -a always,exit -F arch=b64 -S chown -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S chown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S chown -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S chown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w chmod /etc/audit/audit.rules -a always,exit -F arch=b64 -S chmod -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S chmod -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S chmod -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S chmod -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w lchown /etc/audit/audit.rules -a always,exit -F arch=b64 -S lchown -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S lchown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S lchown -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S lchown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w fchownat /etc/audit/audit.rules -a always,exit -F arch=b64 -S fchownat -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S fchownat -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S fchownat -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S fchownat -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w fchown /etc/audit/audit.rules -a always,exit -F arch=b64 -S fchown -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S fchown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S fchown -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S fchown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w fchmodat /etc/audit/audit.rules -a always,exit -F arch=b64 -S fchmodat -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S fchmodat -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S fchmodat -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S fchmodat -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w fchmod /etc/audit/audit.rules -a always,exit -F arch=b64 -S fchmod -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S fchmod -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S fchmod -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S fchmod -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete If the command(s) does not return the appropriate response line, as indicated above, or if the line(s) is commented out, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-254139`

### Rule: Nutanix AOS must provide audit record generation capability for DoD-defined auditable events for file management actions.

**Rule ID:** `SV-254139r958442_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the operating system will provide an audit record generation capability as: Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS auditing is configured to generate audit records for all access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system. $ sudo grep -iw truncate /etc/audit/audit.rules -a always,exit -F arch=b64 -S truncate -F exit=-EACCES -F auid=0 -k access -a always,exit -F arch=b64 -S truncate -F exit=-EPERM -F auid=0 -k access -a always,exit -F arch=b64 -S truncate -F auid>=1000 -F auid!=4294967295 -k access -a always,exit -F arch=b64 -S truncate -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access -a always,exit -F arch=b32 -S truncate -F exit=-EACCES -F auid=0 -k access -a always,exit -F arch=b32 -S truncate -F exit=-EPERM -F auid=0 -k access -a always,exit -F arch=b32 -S truncate -F auid>=1000 -F auid!=4294967295 -k access -a always,exit -F arch=b32 -S truncate -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access $ sudo grep -iw openat /etc/audit/audit.rules -a always,exit -F arch=b64 -S openat -F exit=-EACCES -F auid=0 -k access -a always,exit -F arch=b64 -S openat-F exit=-EPERM -F auid=0 -k access -a always,exit -F arch=b64 -S openat -F auid>=1000 -F auid!=4294967295 -k access -a always,exit -F arch=b64 -S openat -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access -a always,exit -F arch=b32 -S openat -F exit=-EACCES -F auid=0 -k access -a always,exit -F arch=b32 -S openat -F exit=-EPERM -F auid=0 -k access -a always,exit -F arch=b32 -S openat -F auid>=1000 -F auid!=4294967295 -k access -a always,exit -F arch=b32 -S openat -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access $ sudo grep -iw open /etc/audit/audit.rules -a always,exit -F arch=b64 -S open -F exit=-EACCES -F auid=0 -k access -a always,exit -F arch=b64 -S open-F exit=-EPERM -F auid=0 -k access -a always,exit -F arch=b64 -S open -F auid>=1000 -F auid!=4294967295 -k access -a always,exit -F arch=b64 -S open -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access -a always,exit -F arch=b32 -S open -F exit=-EACCES -F auid=0 -k access -a always,exit -F arch=b32 -S open -F exit=-EPERM -F auid=0 -k access -a always,exit -F arch=b32 -S open -F auid>=1000 -F auid!=4294967295 -k access -a always,exit -F arch=b32 -S open -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access $ sudo grep -iw open_by_handle_at /etc/audit/audit.rules -a always,exit -F arch=b64 -S open_by_handle_at -F exit=-EACCES -F auid=0 -k access -a always,exit -F arch=b64 -S open_by_handle_at-F exit=-EPERM -F auid=0 -k access -a always,exit -F arch=b64 -S open_by_handle_at -F auid>=1000 -F auid!=4294967295 -k access -a always,exit -F arch=b64 -S open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access -a always,exit -F arch=b32 -S open_by_handle_at -F exit=-EACCES -F auid=0 -k access -a always,exit -F arch=b32 -S open_by_handle_at -F exit=-EPERM -F auid=0 -k access -a always,exit -F arch=b32 -S open_by_handle_at -F auid>=1000 -F auid!=4294967295 -k access -a always,exit -F arch=b32 -S open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access $ sudo grep -iw ftruncate /etc/audit/audit.rules -a always,exit -F arch=b64 -S ftruncate -F exit=-EACCES -F auid=0 -k access -a always,exit -F arch=b64 -S ftruncate -F exit=-EPERM -F auid=0 -k access -a always,exit -F arch=b64 -S ftruncate -F auid>=1000 -F auid!=4294967295 -k access -a always,exit -F arch=b64 -S ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access -a always,exit -F arch=b32 -S ftruncate -F exit=-EACCES -F auid=0 -k access -a always,exit -F arch=b32 -S ftruncate -F exit=-EPERM -F auid=0 -k access -a always,exit -F arch=b32 -S ftruncate -F auid>=1000 -F auid!=4294967295 -k access -a always,exit -F arch=b32 -S ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access $ sudo grep -iw creat /etc/audit/audit.rules -a always,exit -F arch=b64 -S creat -F exit=-EACCES -F auid=0 -k access -a always,exit -F arch=b64 -S creat -F exit=-EPERM -F auid=0 -k access -a always,exit -F arch=b64 -S creat -F auid>=1000 -F auid!=4294967295 -k access -a always,exit -F arch=b64 -S creat -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access -a always,exit -F arch=b32 -S creat -F exit=-EACCES -F auid=0 -k access -a always,exit -F arch=b32 -S creat -F exit=-EPERM -F auid=0 -k access -a always,exit -F arch=b32 -S creat -F auid>=1000 -F auid!=4294967295 -k access -a always,exit -F arch=b32 -S creat -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access If the command(s) does not return the appropriate response line, as indicated above, or if the line(s) is commented out, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-254140`

### Rule: Nutanix AOS must provide audit record generation capability for DoD-defined auditable events for all account creations, modifications, disabling, and terminations.

**Rule ID:** `SV-254140r958442_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the operating system will provide an audit record generation capability as all account creations, modifications, disabling, and terminations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS auditing is configured to generate audit records for all account creations, modifications, disabling, and terminations. $ sudo grep /etc/shadow /etc/audit/audit.rules -w /etc/shadow -p wa -k audit_account_changes $ sudo grep /etc/security/opasswd /etc/audit/audit.rules -w /etc/security/opasswd -p wa -k audit_account_changes $ sudo grep /etc/passwd /etc/audit/audit.rules -w /etc/passwd -p wa -k audit_account_changes $ sudo grep /etc/gshadow /etc/audit/audit.rules -w /etc/gshadow -p wa -k audit_account_changes $ sudo grep /etc/group /etc/audit/audit.rules -w /etc/group -p wa -k audit_account_changes $ sudo grep /etc/sudoers /etc/audit/audit.rules -w /etc/sudoers -p wa -k actions $ sudo grep /etc/sudoers.d/ /etc/audit/audit.rules -w /etc/sudoers.d/ -p wa -k actions $ sudo grep -w /usr/bin/su /etc/audit/audit.rules -a always,exit -F path=/usr/bin/su -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -w sudo /etc/audit/audit.rules -a always,exit -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -w gpasswd /etc/audit/audit.rules -a always,exit -F path=/usr/bin/gpasswd -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -w passwd /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/userhelper -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-passwd $ sudo grep -w chage /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chage -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -w newgrp /etc/audit/audit.rules -a always,exit -F path=/usr/bin/newgrp -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged If the command(s) does not return the appropriate response line, as indicated above, or if the line(s) is commented out, this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-254141`

### Rule: Nutanix AOS must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited.

**Rule ID:** `SV-254141r958444_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS must allow only the Information System Security Manager (ISSM) (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited. Note: Nutanix AOS audit facility is locked down so that only root has access to browse below the /etc/audit/ directory. $ sudo su - # ls -al /etc/audit/rules.d/*.rules -rw-r----- 1 root root 1280 Feb 16 17:09 audit.rules $ sudo su - sudo stat -c "%a %n" /etc/audit/auditd.conf 640 /etc/audit/auditd.conf If the files in the "/etc/audit/rules.d/" directory or the "/etc/audit/auditd.conf" file have a mode more permissive than "0640", this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-254142`

### Rule: Nutanix AOS must produce audit records containing the full-text recording of successful and unsuccessful uses and variations of the chown privileged commands.

**Rule ID:** `SV-254142r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS generates audit records on all successful/unsuccessful attempts to access privileges occur. $ sudo grep -iw chown /etc/audit/audit.rules -a always,exit -F arch=b64 -S chown -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S chown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S chown -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S chown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding. $ sudo grep -iw fchown /etc/audit/audit.rules -a always,exit -F arch=b64 -S fchown -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b64 -S fchown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S fchown -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S fchown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. -a exit,never -F arch=b64 -S openat -S open -S fchown -F success=0 -F uid=1000 -F exit=-13. -a exit,never -F arch=b64 -S fchown -F success=0 -F uid=0 -F exit=-13. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding. $ sudo grep -iw lchown /etc/audit/audit.rules -a always,exit -F arch=b64 -S lchown -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b64 -S lchown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S lchown -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S lchown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding. $ sudo grep -iw fchownat /etc/audit/audit.rules -a always,exit -F arch=b64 -S fchownat -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b64 -S fchownat -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S fchownat -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S fchownat -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-254143`

### Rule: Nutanix AOS must produce audit records containing the full-text recording of successful and unsuccessful uses and variations of the creat privileged commands.

**Rule ID:** `SV-254143r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS generates audit records on all successful/unsuccessful attempts to access privileges occur. $ sudo grep -iw creat /etc/audit/audit.rules -a always,exit -F arch=b64 -S creat -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b64 -S creat -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b64 -S creat -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b64 -S creat -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S creat -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b32 -S creat -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b32 -S creat -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S creat -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-254144`

### Rule: Nutanix AOS must produce audit records containing the full-text recording of successful and unsuccessful uses and variations of the open-related privileged commands.

**Rule ID:** `SV-254144r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS generates audit records on all successful/unsuccessful attempts to access privileges occur. $ sudo grep -iw open /etc/audit/audit.rules -a always,exit -F arch=b64 -S open -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b64 -S open -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b64 -S open -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b64 -S open -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S open -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b32 -S open -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b32 -S open -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S open -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding. $ sudo grep -iw openat /etc/audit/audit.rules -a always,exit -F arch=b64 -S openat -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b64 -S openat -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b64 -S openat -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b64 -S openat -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S openat -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b32 -S openat -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b32 -S openat -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S openat -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding. $ sudo grep -iw open_by_handle_at /etc/audit/audit.rules -a always,exit -F arch=b64 -S open_by_handle_at -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b64 -S open_by_handle_at -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b64 -S open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b64 -S open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S open_by_handle_at -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b32 -S open_by_handle_at -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b32 -S open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-254145`

### Rule: Nutanix AOS must produce audit records containing the full-text recording of successful and unsuccessful uses and variations of the truncate-related privileged commands.

**Rule ID:** `SV-254145r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS generates audit records on all successful/unsuccessful attempts to access privileges occur. $ sudo grep -iw truncate /etc/audit/audit.rules -a always,exit -F arch=b64 -S truncate -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b64 -S truncate -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b64 -S truncate -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b64 -S truncate -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S truncate -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b32 -S truncate -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b32 -S truncate -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S truncate -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding. $ sudo grep -iw ftruncate /etc/audit/audit.rules -a always,exit -F arch=b64 -S ftruncate -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b64 -S ftruncate -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b64 -S ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b64 -S ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S ftruncate -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b32 -S ftruncate -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b32 -S ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding.

## Group: SRG-OS-000458-GPOS-00203

**Group ID:** `V-254146`

### Rule: Nutanix AOS must generate audit records for file access actions.

**Rule ID:** `SV-254146r991570_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS generates audit records on all successful/unsuccessful attempts to access categories of information occur. $ sudo grep -iw creat /etc/audit/audit.rules -a always,exit -F arch=b64 -S creat -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b64 -S creat -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b64 -S creat -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b64 -S creat -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S creat -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b32 -S creat -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b32 -S creat -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S creat -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. $ sudo grep -iw open /etc/audit/audit.rules -a always,exit -F arch=b64 -S open -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b64 -S open -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b64 -S open -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b64 -S open -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S open -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b32 -S open -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b32 -S open -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S open -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding. $ sudo grep -iw openat /etc/audit/audit.rules -a always,exit -F arch=b64 -S openat -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b64 -S openat -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b64 -S openat -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b64 -S openat -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S openat -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b32 -S openat -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b32 -S openat -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S openat -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding. $ sudo grep -iw open_by_handle_at /etc/audit/audit.rules -a always,exit -F arch=b64 -S open_by_handle_at -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b64 -S open_by_handle_at -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b64 -S open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b64 -S open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S open_by_handle_at -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b32 -S open_by_handle_at -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b32 -S open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. $ sudo grep -iw truncate /etc/audit/audit.rules -a always,exit -F arch=b64 -S truncate -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b64 -S truncate -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b64 -S truncate -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b64 -S truncate -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S truncate -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b32 -S truncate -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b32 -S truncate -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S truncate -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding. $ sudo grep -iw ftruncate /etc/audit/audit.rules -a always,exit -F arch=b64 -S ftruncate -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b64 -S ftruncate -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b64 -S ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b64 -S ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S ftruncate -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b32 -S ftruncate -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b32 -S ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding.

## Group: SRG-OS-000458-GPOS-00203

**Group ID:** `V-254147`

### Rule: Nutanix AOS must generate audit records for file ownership actions.

**Rule ID:** `SV-254147r991570_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS generates audit records on all successful/unsuccessful attempts to access categories of information occur. $ sudo grep -iw chown /etc/audit/audit.rules -a always,exit -F arch=b64 -S chown -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S chown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S chown -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S chown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. $ sudo grep -iw fchown /etc/audit/audit.rules -a always,exit -F arch=b64 -S fchown -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b64 -S fchown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S fchown -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S fchown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. -a exit,never -F arch=b64 -S openat -S open -S fchown -F success=0 -F uid=1000 -F exit=-13. -a exit,never -F arch=b64 -S fchown -F success=0 -F uid=0 -F exit=-13. $ sudo grep -iw lchown /etc/audit/audit.rules -a always,exit -F arch=b64 -S lchown -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b64 -S lchown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S lchown -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S lchown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. $ sudo grep -iw fchownat /etc/audit/audit.rules -a always,exit -F arch=b64 -S fchownat -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b64 -S fchownat -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S fchownat -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S fchownat -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding.

## Group: SRG-OS-000458-GPOS-00203

**Group ID:** `V-254148`

### Rule: Nutanix AOS must generate audit records for file permission actions.

**Rule ID:** `SV-254148r991570_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS generates audit records on all successful/unsuccessful attempts to access categories of information occur. $ sudo grep -w chmod /etc/audit/audit.rules -a always,exit -F arch=b64 -S chmod -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S chmod -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S chmod -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S chmod -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w fchmod /etc/audit/audit.rules -a always,exit -F arch=b64 -S fchmod -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S fchmod -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S fchmod -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S fchmod -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w fchmodat /etc/audit/audit.rules -a always,exit -F arch=b64 -S fchmodat -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S fchmodat -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S fchmodat -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S fchmodat -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding.

## Group: SRG-OS-000458-GPOS-00203

**Group ID:** `V-254149`

### Rule: Nutanix AOS must generate audit records for file extended attribute actions.

**Rule ID:** `SV-254149r991570_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS generates audit records on all successful/unsuccessful attempts to access categories of information occur. $ sudo grep -w setxattr /etc/audit/audit.rules -a always,exit -F arch=b64 -S setxattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S setxattr -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S setxattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S setxattr -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w fsetxattr /etc/audit/audit.rules -a always,exit -F arch=b64 -S fsetxattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S fsetxattr-F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S fsetxattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S fsetxattr -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w lsetxattr /etc/audit/audit.rules -a always,exit -F arch=b64 -S lsetxattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S lsetxattr-F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S lsetxattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S lsetxattr -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w removexattr /etc/audit/audit.rules -a always,exit -F arch=b64 -S removexattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S removexattr -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S removexattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S removexattr -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w fremovexattr /etc/audit/audit.rules -a always,exit -F arch=b64 -S fremovexattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S fremovexattr -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S fremovexattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S fremovexattr -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -w lremovexattr /etc/audit/audit.rules -a always,exit -F arch=b64 -S lremovexattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S lremovexattr -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S lremovexattr -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S lremovexattr -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding.

## Group: SRG-OS-000461-GPOS-00205

**Group ID:** `V-254150`

### Rule: Nutanix AOS must generate audit records when successful/unsuccessful attempts to access categories of information (e.g., classification levels) occur.

**Rule ID:** `SV-254150r991571_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS generates audit records on all successful/unsuccessful attempts to access categories of information occur. $ sudo grep -iw creat /etc/audit/audit.rules -a always,exit -F arch=b64 -S creat -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b64 -S creat -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b64 -S creat -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b64 -S creat -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S creat -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b32 -S creat -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b32 -S creat -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S creat -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. $ sudo grep -iw open /etc/audit/audit.rules -a always,exit -F arch=b64 -S open -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b64 -S open -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b64 -S open -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b64 -S open -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S open -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b32 -S open -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b32 -S open -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S open -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding. $ sudo grep -iw openat /etc/audit/audit.rules -a always,exit -F arch=b64 -S openat -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b64 -S openat -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b64 -S openat -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b64 -S openat -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S openat -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b32 -S openat -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b32 -S openat -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S openat -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding. $ sudo grep -iw open_by_handle_at /etc/audit/audit.rules -a always,exit -F arch=b64 -S open_by_handle_at -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b64 -S open_by_handle_at -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b64 -S open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b64 -S open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S open_by_handle_at -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b32 -S open_by_handle_at -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b32 -S open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. $ sudo grep -iw truncate /etc/audit/audit.rules -a always,exit -F arch=b64 -S truncate -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b64 -S truncate -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b64 -S truncate -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b64 -S truncate -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S truncate -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b32 -S truncate -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b32 -S truncate -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S truncate -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding. $ sudo grep -iw ftruncate /etc/audit/audit.rules -a always,exit -F arch=b64 -S ftruncate -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b64 -S ftruncate -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b64 -S ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b64 -S ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S ftruncate -F exit=-EACCES -F auid=0 -k access. -a always,exit -F arch=b32 -S ftruncate -F exit=-EPERM -F auid=0 -k access. -a always,exit -F arch=b32 -S ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k access. -a always,exit -F arch=b32 -S ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k access. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding.

## Group: SRG-OS-000462-GPOS-00206

**Group ID:** `V-254151`

### Rule: Nutanix AOS must generate audit records when successful/unsuccessful attempts to modify privileges occur.

**Rule ID:** `SV-254151r991572_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS generates audit records when successful/unsuccessful attempts to modify privileged objects occur. $ sudo grep /etc/sudoers /etc/audit/audit.rules -w /etc/sudoers -p wa -k actions $ sudo grep /etc/sudoers.d/ /etc/audit/audit.rules -w /etc/sudoers.d/ -p wa -k actions $ sudo grep -w /usr/bin/su /etc/audit/audit.rules -a always,exit -F path=/usr/bin/su -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -w sudo /etc/audit/audit.rules -a always,exit -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -w newgrp /etc/audit/audit.rules -a always,exit -F path=/usr/bin/newgrp -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -i /usr/bin/chsh /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chsh -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged If the privileged activities access listed do not return any output, this is a finding.

## Group: SRG-OS-000463-GPOS-00207

**Group ID:** `V-254152`

### Rule: Nutanix AOS must generate audit records when successful/unsuccessful attempts to modify security objects occur.

**Rule ID:** `SV-254152r991573_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS generates audit records for successful/unsuccessful attempts to modify security objects occur. $ sudo grep -i /usr/sbin/semanage /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/semanage -F perm=x -F auid>=1000 -F auid!=4294967295 -k secobjects $ sudo grep -i /usr/sbin/setsebool /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/setsebool -F perm=x -F auid>=1000 -F auid!=4294967295 -k secobjects $ sudo grep -i /usr/bin/chcon /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chcon -F perm=x -F auid>=1000 -F auid!=4294967295 -k secobjects $ sudo grep -iw /usr/sbin/setfiles /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/setfiles -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-priv_change If the commands does not return any output, this is a finding.

## Group: SRG-OS-000465-GPOS-00209

**Group ID:** `V-254153`

### Rule: Nutanix AOS must generate audit records when successful/unsuccessful attempts to modify categories of information occur.

**Rule ID:** `SV-254153r991574_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS generates audit records for successful/unsuccessful attempts to modify categories of information. $ sudo grep -i /usr/sbin/semanage /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/semanage -F perm=x -F auid>=1000 -F auid!=4294967295 -k secobjects $ sudo grep -i /usr/sbin/setsebool /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/setsebool -F perm=x -F auid>=1000 -F auid!=4294967295 -k secobjects $ sudo grep -i /usr/bin/chcon /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chcon -F perm=x -F auid>=1000 -F auid!=4294967295 -k secobjects $ sudo grep -iw /usr/sbin/setfiles /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/setfiles -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-priv_change If the commands does not return any output, this is a finding.

## Group: SRG-OS-000466-GPOS-00210

**Group ID:** `V-254154`

### Rule: Nutanix AOS must audit attempts to modify or delete security objects.

**Rule ID:** `SV-254154r991575_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000466-GPOS-00210, SRG-OS-000467-GPOS-00211, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS generates audit records when successful/unsuccessful attempts to delete security objects occur. $ sudo grep -iw rename /etc/audit/audit.rules -a exit,never -F arch=b64 -S rename -F success=1 -F uid=1000 -F exit=0 -a exit,never -F arch=b64 -S rename -F success=0 -F uid=1000 -F exit=-2 -a always,exit -F arch=b64 -S rename -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S rename -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S rename -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S rename -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -iw renameat /etc/audit/audit.rules -a always,exit -F arch=b64 -S renameat -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S renameat -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S renameat -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S renameat -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete $ sudo grep -iw rmdir /etc/audit/audit.rules -a always,exit -F arch=b64 -S rmdir -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S rmdir -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S rmdir -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S rmdir -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete grep -iw unlink /etc/audit/audit.rules -a exit,never -F arch=b64 -S unlink -F success=1 -F uid=1000 -F exit=0 -a exit,never -F arch=b64 -S unlink -F success=0 -F uid=1000 -F exit=-2 -a always,exit -F arch=b64 -S unlink -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S unlink -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S unlink -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S unlink -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete grep -iw unlinkat /etc/audit/audit.rules -a always,exit -F arch=b64 -S unlinkat -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S unlinkat -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S unlinkat -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b32 -S unlinkat -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete If both the "b32" and "b64" audit rules are not defined for the syscalls listed, this is a finding.

## Group: SRG-OS-000470-GPOS-00214

**Group ID:** `V-254155`

### Rule: Nutanix AOS must generate audit records when successful/unsuccessful logon attempts occur.

**Rule ID:** `SV-254155r991578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS generates audit records when concurrent logons to the same account occur. $ sudo grep -i /var/run/faillock /etc/audit/audit.rules -w /var/run/faillock -p wa -k logins $ sudo grep -i /var/log/lastlog /etc/audit/audit.rules -w /var/log/lastlog -p wa -k logins If the commands listed do not return any output, this is a finding.

## Group: SRG-OS-000471-GPOS-00215

**Group ID:** `V-254156`

### Rule: Nutanix AOS must generate audit records for privileged security activities.

**Rule ID:** `SV-254156r991579_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS generates audit records for privileged activities or other system-level access. $ sudo grep /etc/shadow /etc/audit/audit.rules -w /etc/shadow -p wa -k audit_account_changes $ sudo grep /etc/security/opasswd /etc/audit/audit.rules -w /etc/security/opasswd -p wa -k audit_account_changes $ sudo grep /etc/passwd /etc/audit/audit.rules -w /etc/passwd -p wa -k audit_account_changes $ sudo grep /etc/gshadow /etc/audit/audit.rules -w /etc/gshadow -p wa -k audit_account_changes $ sudo grep /etc/group /etc/audit/audit.rules -w /etc/group -p wa -k audit_account_changes $ sudo grep /etc/sudoers /etc/audit/audit.rules -w /etc/sudoers -p wa -k actions $ sudo grep /etc/sudoers.d/ /etc/audit/audit.rules -w /etc/sudoers.d/ -p wa -k actions $ sudo grep -w /usr/bin/su /etc/audit/audit.rules -a always,exit -F path=/usr/bin/su -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -w sudo /etc/audit/audit.rules -a always,exit -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -w gpasswd /etc/audit/audit.rules -a always,exit -F path=/usr/bin/gpasswd -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -w passwd /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/userhelper -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-passwd If the privileged activities access listed do not return any output, this is a finding.

## Group: SRG-OS-000471-GPOS-00215

**Group ID:** `V-254157`

### Rule: Nutanix AOS must generate audit records for privileged account activities.

**Rule ID:** `SV-254157r991579_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS generates audit records for privileged activities or other system-level access. $ sudo grep -w chage /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chage -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -w newgrp /etc/audit/audit.rules -a always,exit -F path=/usr/bin/newgrp -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -i /usr/bin/chsh /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chsh -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -w "userhelper" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/userhelper -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-passwd $ sudo grep -w "unix_chkpwd" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/unix_chkpwd -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged $ sudo grep -w faillock /etc/audit/audit.rules -w /var/run/faillock/ -p wa -k logins $ sudo grep -w lastlog /etc/audit/audit.rules -w /var/log/lastlog -p wa -k logins $ sudo grep -iw "/usr/sbin/pam_timestamp_check" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/pam_timestamp_check -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged If the privileged activities access listed do not return any output, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-254158`

### Rule: Nutanix AOS must be configured to audit the loading and unloading of dynamic kernel modules.

**Rule ID:** `SV-254158r958442_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000062-GPOS-00031, SRG-OS-000471-GPOS-00216, SRG-OS-000477-GPOS-00222</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS generates audit records for all kernel module load, unload, restart actions, and initiations. $ sudo grep -iw create_module /etc/audit/audit.rules -a always,exit -F arch=b32 -S create_module -k module-change -a always,exit -F arch=b64 -S create_module -k module-change $ sudo grep -iw init_module /etc/audit/audit.rules -a always,exit -F arch=b64 -S init_module -S delete_module -k modules -a always,exit -F arch=b32 -S init_module -S delete_module -k modules $ sudo grep -iw finit_module /etc/audit/audit.rules -a always,exit -F arch=b32 -S finit_module -k module-change -a always,exit -F arch=b64 -S finit_module -k module-change $ sudo grep -iw delete_module /etc/audit/audit.rules -a always,exit -F arch=b64 -S init_module -S delete_module -k modules -a always,exit -F arch=b32 -S init_module -S delete_module -k modules If both the "b32" and "b64" audit rules are not defined for the module(s) listed syscall, this is a finding. $ sudo grep -iw kmod /etc/audit/audit.rules -w /usr/bin/kmod -p x -F auid!=unset -k module-change If the command does not return any output, this is a finding. $ sudo cat /boot/grub/grub.conf | grep audit kernel /boot/vmlinuz-3.10.0-1160.24.1.el7.nutanix.20210425.cvm.x86_64 ro root=UUID=71a1fe8c-812f-4403-80ed-894f554b061c rd_NO_LUKS rd_NO_LVM rd_NO_MD rd_NO_DM LANG=en_US.UTF-8 SYSFONT=latarcyrheb-sun16 rhgb crashkernel=auto KEYBOARDTYPE=pc KEYTABLE=us audit=1 audit_backlog_limit=8192 nousb fips=1 nomodeset biosdevname=0 net.ifnames=0 scsi_mod.use_blk_mq=y panic=30 console=ttyS0,115200n8 console=tty0 clocksource=tsc kvm_nopvspin=1 xen_nopvspin=1 hv_netvsc.ring_size=512 mds=off mitigations=off If the command(s) does not return the appropriate response line, as indicated above, or if the line(s) is commented out, this is a finding.

## Group: SRG-OS-000473-GPOS-00218

**Group ID:** `V-254159`

### Rule: Nutanix AOS must generate audit records when concurrent logons to the same account occur from different sources.

**Rule ID:** `SV-254159r991582_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS generates audit records when concurrent logons to the same account occur. $ sudo grep -i /var/run/faillock /etc/audit/audit.rules -w /var/run/faillock -p wa -k logins $ sudo grep -i /var/log/lastlog /etc/audit/audit.rules -w /var/log/lastlog -p wa -k logins If the commands listed do not return any output, this is a finding.

## Group: SRG-OS-000474-GPOS-00219

**Group ID:** `V-254160`

### Rule: Nutanix AOS must generate audit records when successful/unsuccessful accesses to objects occur.

**Rule ID:** `SV-254160r991583_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS generates audit records on all successful/unsuccessful attempts to access privileges occur. $ sudo grep -iw chown /etc/audit/audit.rules -a always,exit -F arch=b64 -S chown -F auid=0 -k audit_time_perm_mod_export_delete -a always,exit -F arch=b64 -S chown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S chown -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S chown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding. $ sudo grep -iw fchown /etc/audit/audit.rules -a always,exit -F arch=b64 -S fchown -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b64 -S fchown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S fchown -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S fchown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. -a exit,never -F arch=b64 -S openat -S open -S fchown -F success=0 -F uid=1000 -F exit=-13. -a exit,never -F arch=b64 -S fchown -F success=0 -F uid=0 -F exit=-13. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding. $ sudo grep -iw lchown /etc/audit/audit.rules -a always,exit -F arch=b64 -S lchown -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b64 -S lchown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S lchown -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S lchown -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding. $ sudo grep -iw fchownat /etc/audit/audit.rules -a always,exit -F arch=b64 -S fchownat -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b64 -S fchownat -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S fchownat -F auid=0 -k audit_time_perm_mod_export_delete. -a always,exit -F arch=b32 -S fchownat -F auid>=1000 -F auid!=4294967295 -k audit_time_perm_mod_export_delete. If the output does not contain all of the above rules, this is a finding. If both the "b32" and "b64" audit rules are not defined for the listed syscall(s), this is a finding.

## Group: SRG-OS-000472-GPOS-00217

**Group ID:** `V-254161`

### Rule: Nutanix AOS must generate audit records for all direct access to the information system.

**Rule ID:** `SV-254161r991581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000472-GPOS-00217, SRG-OS-000475-GPOS-00220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured with the ausearch tool. The ausearch tool is a feature of the audit rpm. $ sudo yum list installed audit Installed Packages audit.x86_64 If Installed Packages does not list the audit.x86_64 or No matching Packages to list is returned, this is a finding.

## Group: SRG-OS-000476-GPOS-00221

**Group ID:** `V-254162`

### Rule: Nutanix AOS must generate audit records for all account creations, modifications, disabling, and termination events.

**Rule ID:** `SV-254162r991585_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS generates audit records for all account creation, modification, disabling, and termination. $ sudo grep /etc/passwd /etc/audit/audit.rules -w /etc/passwd -p wa -k audit_account_changes If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000254-GPOS-00095

**Group ID:** `V-254163`

### Rule: Nutanix AOS must initiate session audits at system start-up.

**Rule ID:** `SV-254163r991555_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If auditing is enabled late in the start-up process, the actions of some start-up processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if auditing is active by issuing the following command: $ sudo systemctl is-active auditd.service active If the "auditd" status is not active, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-254164`

### Rule: Nutanix AOS must produce audit records containing information to establish what type of events occurred.

**Rule ID:** `SV-254164r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in the operating system audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Nutanix AOS generates audit records when successful/unsuccessful attempts to use the following commands occur. Check that the following system call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo auditctl -l | grep -iw /usr/bin/su /etc/audit/audit.rules If the output is not -a always,exit -F path=/usr/bin/su -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged, this is a finding. $ sudo auditctl -l | grep -iw /usr/bin/sudo /etc/audit/audit.rules If the output is not -a always,exit -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged, this is a finding. $ sudo grep -i "/etc/sudoers" /etc/audit/audit.rules If the output is not -w /etc/sudoers -p wa -k actions, this is a finding. $ sudo grep -i "/etc/sudoers.d/" /etc/audit/audit.rules If the output is not -w /etc/sudoers.d/ -p wa -k actions, this is a finding. $ sudo grep -i /usr/bin/newgrp /etc/audit/audit.rules If the output is not -a always,exit -F path=/usr/bin/newgrp -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged, this is a finding. $ sudo grep -i /usr/bin/chsh /etc/audit/audit.rules If the output is not -a always,exit -F path=/usr/bin/chsh -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged, this is a finding.

## Group: SRG-OS-000038-GPOS-00016

**Group ID:** `V-254165`

### Rule: Nutanix AOS must produce audit records containing information to establish when events occurred.

**Rule ID:** `SV-254165r958414_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing when events occurred, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. To compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know when events occurred (date and time). Associating event types with detected events in the operating system audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system produces audit records containing information to establish when (date and time) the events occurred. Determine if auditing is active by issuing the following command: $ sudo systemctl is-active auditd.service active If the "auditd" status is not active, this is a finding.

## Group: SRG-OS-000039-GPOS-00017

**Group ID:** `V-254166`

### Rule: Nutanix AOS must produce audit records containing information to establish where events occurred.

**Rule ID:** `SV-254166r958416_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing where events occurred, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. To compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know where events occurred, such as operating system components, modules, device identifiers, node names, file names, and functionality. Associating information about where the event occurred within the operating system provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system produces audit records containing information to establish when (date and time) the events occurred. Determine if auditing is active by issuing the following command: $ sudo systemctl is-active auditd.service active If the "auditd" status is not active, this is a finding.

## Group: SRG-OS-000040-GPOS-00018

**Group ID:** `V-254167`

### Rule: Nutanix AOS must produce audit records containing information to establish the source of events.

**Rule ID:** `SV-254167r958418_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing the source of the event, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. In addition to logging where events occur within the operating system, the operating system must also generate audit records that identify sources of events. Sources of operating system events include, but are not limited to, processes, and services. To compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know the source of the event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system produces audit records containing information to establish when (date and time) the events occurred. Determine if auditing is active by issuing the following command: $ sudo systemctl is-active auditd.service active If the "auditd" status is not active, this is a finding.

## Group: SRG-OS-000041-GPOS-00019

**Group ID:** `V-254168`

### Rule: Nutanix AOS must produce audit records containing information to establish the outcome of events.

**Rule ID:** `SV-254168r958420_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without information about the outcome of events, security personnel cannot make an accurate assessment as to whether an attack was successful or if changes were made to the security state of the system. Event outcomes can include indicators of event success or failure and event-specific results (e.g., the security state of the information system after the event occurred). As such, they also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system produces audit records containing information to establish when (date and time) the events occurred. Determine if auditing is active by issuing the following command: $ sudo systemctl is-active auditd.service active If the "auditd" status is not active, this is a finding.

## Group: SRG-OS-000255-GPOS-00096

**Group ID:** `V-254169`

### Rule: Nutanix AOS must produce audit records containing information to establish the identity of any individual or process associated with the event.

**Rule ID:** `SV-254169r991556_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without information that establishes the identity of the subjects (i.e., users or processes acting on behalf of users) associated with the events, security personnel cannot determine responsibility for the potentially harmful event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS produces audit records containing information to establish when (date and time) the events occurred. Determine if auditing is active by issuing the following command: $ sudo systemctl is-active auditd.service active If the "auditd" status is not active, this is a finding.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-254170`

### Rule: Nutanix AOS must produce audit records containing the full-text recording of successful and unsuccessful attempts to execute the passwd/gpasswd/unix-chkpwd privileged commands.

**Rule ID:** `SV-254170r958422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Nutanix AOS generates audit records when successful/unsuccessful attempts to use the following commands occur. Check that the following system call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -i /usr/bin/passwd /etc/audit/audit.rules If the output is not -a always,exit -F path=/usr/bin/passwd -F auid>=1000 -F auid!=4294967295 -k privileged, this is a finding. $ sudo grep -iw /usr/sbin/unix_chkpwd /etc/audit/audit.rules If the output is not -a always,exit -F path=/usr/sbin/unix_chkpwd -F auid>=1000 -F auid!=4294967295 -k privileged, this is a finding. $ sudo grep -i /usr/bin/gpasswd /etc/audit/audit.rules If the output is not -a always,exit -F path=/usr/bin/gpasswd -F auid>=1000 -F auid!=4294967295 -k privileged, this is a finding.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-254171`

### Rule: Nutanix AOS must produce audit records containing the full-text recording of successful and unsuccessful attempts to execute the chage privileged command.

**Rule ID:** `SV-254171r958422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Nutanix AOS generates audit records when successful/unsuccessful attempts to use the following commands occur. Check that the following system call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -i /usr/bin/chage /etc/audit/audit.rules If the output is not -a always,exit -F path=/usr/bin/chage -F auid>=1000 -F auid!=4294967295 -k privileged, this is a finding.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-254172`

### Rule: Nutanix AOS must produce audit records containing the full-text recording of successful and unsuccessful attempts to execute the userhelper privileged command.

**Rule ID:** `SV-254172r958422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Nutanix AOS generates audit records when successful/unsuccessful attempts to use the following commands occur. Check that the following system call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -i /usr/sbin/userhelper /etc/audit/audit.rules If the output is not -a always,exit -F path=/usr/sbin/userhelper -F auid>=1000 -F auid!=4294967295 -k privileged-passwd, this is a finding.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-254173`

### Rule: Nutanix AOS must produce audit records containing the full-text recording of successful and unsuccessful attempts to execute the mount and umount privileged commands.

**Rule ID:** `SV-254173r958422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Nutanix AOS generates audit records when successful/unsuccessful attempts to use the following commands occur. Check that the following system call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -iw "mount" /etc/audit/audit.rules If the output is not -a always,exit -F path=/usr/bin/mount -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged, this is a finding. $ sudo grep -iw "/usr/bin/umount" /etc/audit/audit.rules If the output is not -a always,exit -F path=/usr/bin/umount -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged, this is a finding.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-254174`

### Rule: Nutanix AOS must produce audit records containing the full-text recording of successful and unsuccessful attempts to execute the post-related privileged commands.

**Rule ID:** `SV-254174r958422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Nutanix AOS generates audit records when successful/unsuccessful attempts to use the following commands occur. Check that the following system call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -iw /usr/sbin/postdrop /etc/audit/audit.rules If the output is not clear-a always,exit -F path=/usr/sbin/postdrop -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged, this is a finding. $ sudo grep -iw /usr/sbin/postqueue /etc/audit/audit.rules If the output in not, -a always,exit -F path=/usr/sbin/postqueue -F auid>=1000 -F auid!=4294967295 -k privileged, this is a finding.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-254175`

### Rule: Nutanix AOS must produce audit records containing the full-text recording of successful and unsuccessful attempts to execute the opensshrelated privileged commands.

**Rule ID:** `SV-254175r958422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Nutanix AOS generates audit records when successful/unsuccessful attempts to use the following commands occur. Check that the following system call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -iw /usr/libexec/openssh/ssh-keysign /etc/audit/audit.rules If the output is not -a always,exit -F path=/usr/libexec/openssh/ssh-keysign -F auid>=1000 -F auid!=4294967295 -k privileged, this is a finding.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-254176`

### Rule: Nutanix AOS must produce audit records containing the full-text recording of successful and unsuccessful attempts to execute the crontab-related privileged commands.

**Rule ID:** `SV-254176r958422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Nutanix AOS generates audit records when successful/unsuccessful attempts to use the following commands occur. Check that the following system call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -iw /usr/bin/crontab /etc/audit/audit.rules If the output is not -a always,exit -F path=/usr/bin/crontab -F auid>=1000 -F auid!=4294967295 -k privileged, this is a finding.

## Group: SRG-OS-000042-GPOS-00021

**Group ID:** `V-254177`

### Rule: Nutanix AOS must produce audit records containing the individual identities of group account users.

**Rule ID:** `SV-254177r958422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the individual identities of group users. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the actual account involved in the activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Nutanix AOS produces audit records containing information to establish when (date and time) the events occurred. Determine if auditing is active by issuing the following command: $ sudo systemctl is-active auditd.service active If the "auditd" status is not active, this is a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-254178`

### Rule: Nutanix AOS must allocate audit record storage capacity to store at least one week's worth of audit records, when audit records are not immediately sent to a central audit record storage facility.

**Rule ID:** `SV-254178r958752_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure operating systems have a sufficient storage capacity in which to write the audit logs, operating systems must be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial installation of the operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS preconfigures storage for one week's worth of audit records, when audit records are not immediately sent to a central audit record facility. $ sudo cat /boot/grub/grub.conf | grep audit_backlog_limit audit_backlog_limit=8192 If the "audit_backlog_limit" entry does not equal "8192", is missing, or the line is commented out, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-254179`

### Rule: Nutanix AOS must offload audit records to a syslog server.

**Rule ID:** `SV-254179r958754_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. Satisfies: SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to offload the audit records to a site-specific syslog server. $ sudo grep @ /etc/rsyslog.d/rsyslog-nutanix.conf local0.*; @remote-log-host:514 If there are no lines in the "/etc/rsyslog.d/rsyslog-nutanix.conf" files that contain the "@" or "@@" symbol(s), and the lines with the correct symbol(s) to send output to another system do not cover all "rsyslog" output, ask the System Administrator to indicate how the audit logs are offloaded to a different system or media. If the lines are commented out or there is no evidence that the audit logs are being sent to another system, this is a finding.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-254180`

### Rule: Nutanix AOS must shut down by default upon audit failure (unless availability is an overriding concern).

**Rule ID:** `SV-254180r958426_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the operating system is at risk of failing to process audit logs as required, it takes action to mitigate the failure. Audit processing failures include software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When availability is an overriding concern, other approved actions in response to an audit failure are as follows: 1) If the failure was caused by the lack of audit record storage capacity, the operating system must continue generating audit records if possible (automatically restarting the audit service if necessary), overwriting the oldest audit records in a first-in-first-out manner. 2) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, the operating system must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm the audit configuration regarding how auditing processing failures are handled in Nutanix AOS. $ sudo auditctl -s | grep -i "fail" If the output is not failure 1, this is a finding.

## Group: SRG-OS-000051-GPOS-00024

**Group ID:** `V-254181`

### Rule: Nutanix AOS must provide the capability to centrally review and analyze audit records from multiple components within the system.

**Rule ID:** `SV-254181r958428_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Successful incident response and auditing relies on timely, accurate system information and analysis to allow the organization to identify and respond to potential incidents in a proficient manner. If the operating system does not provide the ability to centrally review the operating system logs, forensic analysis is negatively impacted. Segregation of logging data to multiple disparate computer systems is counterproductive and makes log analysis and log event alarming difficult to implement and manage, particularly when the system has multiple logging components writing to different locations or systems. To support the centralized capability, the operating system must be able to provide the information in a format that can be extracted and used, allowing the application performing the centralization of the log records to meet this requirement. Satisfies: SRG-OS-000051-GPOS-00024, SRG-OS-000054-GPOS-00025, SRG-OS-000122-GPOS-00063, SRG-OS-000348-GPOS-00136, SRG-OS-000349-GPOS-00137, SRG-OS-000350-GPOS-00138, SRG-OS-000351-GPOS-00139, SRG-OS-000352-GPOS-00140, SRG-OS-000353-GPOS-00141, SRG-OS-000354-GPOS-00142</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured with the ausearch tool. The ausearch tool is a feature of the audit rpm. $ sudo yum list installed audit Installed Packages audit.x86_64 If Installed Packages does not list the audit.x86_64 or No matching Packages to list is returned, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-254182`

### Rule: Nutanix AOS must compare internal information system clocks at least every 24 hours with a server synchronized to one of the redundant United States Naval Observatory (USNO) time servers, or a time server designated for the appropriate DoD network (NIPRNet/SIPRNet), and/or the Global Positioning System (GPS).

**Rule ID:** `SV-254182r982208_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations must consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). Satisfies: SRG-OS-000355-GPOS-00143, SRG-OS-000356-GPOS-00144</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is running the NTP service. # sudo ps -ef | grep ntp ntp 7447 1 0 Aug17 ? 00:00:05 /usr/sbin/ntpd -u ntp:ntp -g If the NTP service is not running, this is a finding. Next Check the ntp.conf file for the "maxpoll" option setting. $ sudo grep maxpoll /etc/ntp.conf server #.#.#.# maxpoll 10 If the option is set to "17" or is not set, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-254183`

### Rule: Nutanix AOS must protect audit information from unauthorized access.

**Rule ID:** `SV-254183r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Nutanix AOS audit log permissions are "0600" or less permissive. $ sudo stat -c "%a %n" /home/log/audit/audit.log 600 /home/log/audit/audit.log If the audit.log file(s) are more permissive than "0600", this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-254184`

### Rule: Nutanix AOS audit tools must be configured to 0755 or less permissive.

**Rule ID:** `SV-254184r991557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without information that establishes the identity of the subjects (i.e., users or processes acting on behalf of users) associated with the events, security personnel cannot determine responsibility for the potentially harmful event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit tools are protected from unauthorized access, deletion, or modification by checking the permissive mode. Check the octal permission of each audit tool by running the following command: $ sudo stat -c "%a %n" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/rsyslogd /sbin/augenrules 750 /sbin/auditctl 750 /sbin/aureport 750 /sbin/ausearch 750 /sbin/autrace 750 /sbin/auditd 755 /sbin/rsyslogd 755 /sbin/augenrules If any of the audit tools has a mode more permissive than "0755", this is a finding.

## Group: SRG-OS-000257-GPOS-00098

**Group ID:** `V-254185`

### Rule: Nutanix AOS audit tools must be owned by root.

**Rule ID:** `SV-254185r991558_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user has to make access decisions regarding the modification of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit tools are owned by "root" to prevent any unauthorized access, deletion, or modification. Check the owner of each audit tool by running the following commands: $ sudo stat -c "%U %n" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/rsyslogd /sbin/augenrules [sudo] password for admin: root /sbin/auditctl root /sbin/aureport root /sbin/ausearch root /sbin/autrace root /sbin/auditd root /sbin/rsyslogd root /sbin/augenrules If any of the audit tools are not owned by "root", this is a finding.

## Group: SRG-OS-000258-GPOS-00099

**Group ID:** `V-254186`

### Rule: Nutanix AOS audit tools must be group-owned by root.

**Rule ID:** `SV-254186r991559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user has in order to make access decisions regarding the deletion of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit tools are group-owned by "root" to prevent any unauthorized access, deletion, or modification. Check the owner of each audit tool by running the following commands: $ sudo stat -c "%G %n" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/rsyslogd /sbin/augenrules [sudo] password for admin: root /sbin/auditctl root /sbin/aureport root /sbin/ausearch root /sbin/autrace root /sbin/auditd root /sbin/rsyslogd root /sbin/augenrules If any of the audit tools are not group-owned by "root", this is a finding.

## Group: SRG-OS-000278-GPOS-00108

**Group ID:** `V-254187`

### Rule: Nutanix AOS must use cryptographic mechanisms to protect the integrity of audit tools.

**Rule ID:** `SV-254187r991567_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Protecting the integrity of the tools used for auditing purposes is a critical step toward ensuring the integrity of audit information. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. It is not uncommon for attackers to replace the audit tools or inject code into the existing tools with the purpose of providing the capability to hide or erase system activity from the audit logs. To address this risk, audit tools must be cryptographically signed to provide the capability to identify when the audit tools have been modified, manipulated, or replaced. An example is a checksum hash of the file or files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Advanced Intrusion Detection Environment (AIDE) is properly configured to use cryptographic mechanisms to protect the integrity of audit tools. If AIDE is not installed, ask the System Administrator how file integrity checks are performed on the system. Verify the location of the seven auditing tools that require cryptographic protection with the following command: (auditctl, auditd, ausearch, aureport, autrace, augenrules, rsyslogd) $ sudo ls -al /usr/sbin/ | egrep '(audit|au|rsys)' If the seven identified audit tools are not listed, this is a finding. Check the aide.conf file for the configured rule set. $ sudo grep -i "FIPSR =" /etc/aide.conf FIPSR = p+i+n+u+g+s+m+c+acl+selinux+xattrs+sha512 If the FIPSR rule set is commented out or does not display, this is a finding. Check to ensure that the root directory of the seven audit tools is configured to be monitored and that the proper rule set is applied to that directory (/usr/). $ sudo grep -i /usr /etc/aide.conf /usr FIPSR if the /usr directory is not listed or has a preceding '=' or '!' sign or the Rule Set is not set to FIPSR, this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-254188`

### Rule: Nutanix AOS must notify designated personnel if baseline configurations are changed in an unauthorized manner.

**Rule ID:** `SV-254188r958794_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to the operating system. Changes to operating system configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of the operating system. The operating system's ISSO and SAs must be notified via email and/or monitoring system trap when there is an unauthorized modification of a configuration item.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm that Nutanix AOS has been set to have the Advanced Intrusion Detection Environment (AIDE) installed and enabled. $ sudo yum list installed aide Installed Packages aide.x86_64 If the aide_x86_64 package is not installed, this is a finding. Check for the presence of a cron job running daily or weekly on the system that executes AIDE daily to scan for changes to the system baseline. Check the cron directories for a script file controlling the execution of the file integrity application. For example, if AIDE is installed on the system, use the following command: $ sudo ls -al /etc/cron.* | grep aide If the file integrity application does not exist, or a script file controlling the execution of the file integrity application does not exist, this is a finding.

## Group: SRG-OS-000364-GPOS-00151

**Group ID:** `V-254189`

### Rule: Nutanix AOS must not be configured to allow GSSAPIAuthentication.

**Rule ID:** `SV-254189r958796_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to system configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the operating system can have significant effects on the overall security of the system. Accordingly, only qualified and authorized individuals must be allowed to obtain access to operating system components for the purposes of initiating changes, including upgrades and modifications. Logical access restrictions include, for example, controls that restrict access to workflow automation, media libraries, abstract layers (e.g., changes implemented into third-party interfaces rather than directly into information systems), and change windows (e.g., changes occur only during specified times, making unauthorized changes easy to discover).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS enforces access restrictions. Check that the SSH daemon does not permit GSSAPI authentication with the following command: $ sudo grep -i gssapiauth /etc/ssh/sshd_config GSSAPIAuthentication no If the "GSSAPIAuthentication" keyword is missing, is set to "yes" and is not documented with the Information System Security Officer (ISSO), or the returned line is commented out, this is a finding.

## Group: SRG-OS-000364-GPOS-00151

**Group ID:** `V-254190`

### Rule: Nutanix AOS must not be configured to allow KerberosAuthentication.

**Rule ID:** `SV-254190r958796_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to system configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the operating system can have significant effects on the overall security of the system. Accordingly, only qualified and authorized individuals must be allowed to obtain access to operating system components for the purposes of initiating changes, including upgrades and modifications. Logical access restrictions include, for example, controls that restrict access to workflow automation, media libraries, abstract layers (e.g., changes implemented into third-party interfaces rather than directly into information systems), and change windows (e.g., changes occur only during specified times, making unauthorized changes easy to discover).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS enforces access restrictions. Check that the SSH daemon does not permit Kerberos to authenticate passwords with the following command: $ sudo grep -i kerberosauth /etc/ssh/sshd_config KerberosAuthentication no If the "KerberosAuthentication" keyword is missing, or is set to "yes" and is not documented with the Information System Security Officer (ISSO), or the returned line is commented out, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-254191`

### Rule: Nutanix AOS must prevent the installation of patches, service packs, device drivers, or operating system components without verification they have been digitally signed using a certificate that is recognized and approved by the organization.

**Rule ID:** `SV-254191r982212_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. Accordingly, patches, service packs, device drivers, or operating system components must be signed with a certificate recognized and approved by the organization. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. The operating system should not have to verify the software again. This requirement does not mandate DoD certificates for this purpose; however, the certificate used to verify the software must be from an approved CA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm that Nutanix AOS is configured to require gpgcheck and localpkg_gpgcheck for all installation packages provided by the vendor. $ sudo grep gpgcheck /etc/yum.conf gpgcheck=1 $ sudo grep localpkg_gpgcheck /etc/yum.conf localpkg_gpgcheck=1 $ sudo grep repo_gpgcheck /etc/yum.conf repo_gpgcheck=1 If any of the three gpg checks output is not set to "1", this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-254192`

### Rule: Nutanix AOS must prevent the use of dictionary words for passwords.

**Rule ID:** `SV-254192r991587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system allows the user to select passwords based on dictionary words, then this increases the chances of password compromise by increasing the opportunity for successful guesses and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS prevents the use of dictionary words for passwords. Check the /etc/pam.d/password-auth file for pam_pwquality.so $ sudo grep pwquality.so /etc/pam.d/password-auth password requisite pam_pwquality.so try_first_pass local_users_only enforce_for_root retry=3 authtok_type= If the output does not contain "pam_pwquality.so" with the option of "required" or "requisite", this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-254193`

### Rule: Nutanix AOS must enforce a delay of at least four seconds between logon prompts following a failed logon attempt.

**Rule ID:** `SV-254193r991588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of logon attempts over a certain time interval reduces the chances that an unauthorized user may gain access to an account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS enforces a delay of at least four seconds between console logon prompts following a failed logon attempt. $ sudo grep -i fail_delay /etc/login.defs FAIL_DELAY 4 If the value of "FAIL_DELAY" is not set to "4" or greater, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-254194`

### Rule: Nutanix AOS must be configured to run SCMA daily.

**Rule ID:** `SV-254194r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Nutanix platform leverages the use of the Security Configuration Management Automation (SCMA) framework to ensure secure configurations have not been altered from their desired state. If the SCMA framework is not run on a daily basis, changes to the secure baseline could be made, compromising multiple security functions and features on the operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SCMA framework is set to run daily: $ ncli cluster get-cvm-security-config | egrep 'Schedule' Schedule : DAILY If "Schedule" is not set to "DAILY", this is a finding.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-254195`

### Rule: Nutanix AOS must define default permissions for all authenticated users in such a way that the user can only read and modify their own files.

**Rule ID:** `SV-254195r991590_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Setting the most restrictive default permissions ensures that when new accounts are created they do not have unnecessary access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS defines default permissions for all authenticated users in such a way that the user can only read and modify their own files. $ sudo grep -i umask /etc/login.defs UMASK 077 If the value for the "UMASK" parameter is not "077", or the "UMASK" parameter is missing or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-254196`

### Rule: Nutanix AOS must not allow an unattended or automatic logon to the system.

**Rule ID:** `SV-254196r991591_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to restrict system access to authenticated users negatively impacts operating system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS does not allow users to override environment variables to the SSH daemon. Check for the value of the "PermitUserEnvironment" keyword with the following command: $ sudo grep -i permituserenvironment /etc/ssh/sshd_config PermitUserEnvironment no If the "PermitUserEnvironment" keyword is not set to "no", is missing, or is commented out, this is a finding. $ sudo grep -i hostbasedauthentication /etc/ssh/sshd_config HostbasedAuthentication no If the "HostbasedAuthentication" keyword is not set to "no", is missing, or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-254197`

### Rule: Nutanix AOS must be configured so that all local interactive user home directories have mode "0750" or less permissive.

**Rule ID:** `SV-254197r991592_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on local interactive user home directories may allow unauthorized access to user files by other users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS has assigned home directory of all local interactive users has a mode of "0750" or less permissive. Step 1. Determine interactive users $ sudo cat $(awk -F: '($3>=1000)&&($7 !~ /nologin/){print $6}' /etc/passwd) cat: /home/nutanix: Is a directory cat: /home/admin: Is a directory Step 2. Determine permissions on interactive users home directories. $ sudo stat -c "%a %n" /home/admin 750 /home/admin $ sudo stat -c "%a %n" /home/nutanix 750 /home/nutanix If home directories referenced in "/etc/passwd" do not have a mode of "0750" or less permissive, this is a finding.

## Group: SRG-OS-000480-GPOS-00232

**Group ID:** `V-254198`

### Rule: Nutanix AOS must enable an application firewall, if available.

**Rule ID:** `SV-254198r991593_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Firewalls protect computers from network attacks by blocking or limiting access to open network ports. Application firewalls limit which applications are allowed to communicate over the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS prohibits or restricts the use of remote access methods, using the iptables firewall service. $ sudo service iptables status iptables.service - IPv4 firewall with iptables Loaded: loaded (/usr/lib/systemd/system/iptables.service; enabled; vendor preset: disabled) Active: active (exited) since Mon 2021-08-02 15:02:12 CDT; 2 weeks 6 days ago Main PID: 1250 (code=exited, status=0/SUCCESS) CGroup: /system.slice/iptables.service If IPv6 is in use: $ sudo service ip6tables status ip6tables.service - IPv6 firewall with ip6tables Loaded: loaded (/usr/lib/systemd/system/ip6tables.service; enabled; vendor preset: disabled) Active: active (exited) since Mon 2021-08-02 15:02:12 CDT; 2 weeks 6 days ago Main PID: 1313 (code=exited, status=0/SUCCESS) CGroup: /system.slice/ip6tables.service If no iptables services are "Loaded" and "Active", this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-254199`

### Rule: Nutanix AOS must be configured with nodev, nosuid, and noexec options for /dev/shm.

**Rule ID:** `SV-254199r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Control of program execution is a mechanism used to prevent execution of unauthorized programs. Some operating systems may provide a capability that runs counter to the mission or provides users with functionality that exceeds mission requirements. This includes functions and services installed at the operating system-level. Some of the programs, installed by default, may be harmful or may not be necessary to support essential organizational operations (e.g., key missions, functions). Removal of executable programs is not always possible; therefore, establishing a method of preventing program execution is critical to maintaining a secure system baseline. Methods for complying with this requirement include restricting execution of programs in certain environments, while preventing execution in other environments; or limiting execution of certain program functionality based on organization-defined criteria (e.g., privileges, subnets, sandboxed environments, or roles).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS that "nodev","nosuid", and "noexec" options are configured for /dev/shm: $ cat /etc/fstab | grep /dev/shm tmpfs /dev/shm tmpfs defaults,size=512m,noexec,rw,seclabel,nosuid,nodev 0 0 If /dev/shm is mounted without secure options "nodev", "nosuid", and "noexec", this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-254200`

### Rule: Nutanix AOS must not have the rsh-server package installed.

**Rule ID:** `SV-254200r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of nonessential capabilities include, but are not limited to, games, software packages, tools, and demonstration software, not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled. Satisfies: SRG-OS-000095-GPOS-00049, SRG-OS-000074-GPOS-00042</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to disable nonessential capabilities. $ sudo yum list installed rsh-server If the rsh-server package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-254201`

### Rule: Nutanix AOS must not have the ypserv package installed.

**Rule ID:** `SV-254201r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of nonessential capabilities include, but are not limited to, games, software packages, tools, and demonstration software, not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to disable nonessential capabilities. $ sudo yum list installed ypserv If the "ypserv" package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-254202`

### Rule: Nutanix AOS must not have the telnet-server package installed.

**Rule ID:** `SV-254202r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of nonessential capabilities include, but are not limited to, games, software packages, tools, and demonstration software, not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to disable nonessential capabilities. $ sudo yum list installed telnet-server If the telnet-server package is installed, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-254203`

### Rule: Nutanix AOS must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-254203r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the operating system must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS prohibits or restricts the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments. $ sudo iptables -S If IPv6 is in use: $ sudo ip6tables -S Review the site or program PPSM CAL; verify the services allowed by the firewall match the PPSM CLSA. If there are additional ports, protocols, or services that are not in the PPSM CLSA, or there are ports, protocols, or services that are prohibited by the PPSM Category Assurance List (CAL), this is a finding.

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-254204`

### Rule: Nutanix AOS must require users to reauthenticate for privilege escalation.

**Rule ID:** `SV-254204r987879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the user reauthenticate. Satisfies: SRG-OS-000373-GPOS-00156, SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00158</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured as shown for reauthentication in the sudoers file. $ grep -i nopasswd /etc/sudoers /etc/sudoers.d/* If any occurrences of "NOPASSWD" are returned from the command and have not been documented with the Information System Security Officer (ISSO) as an organizationally defined administrative group utilizing MFA, this is a finding.

## Group: SRG-OS-000112-GPOS-00057

**Group ID:** `V-254205`

### Rule: Nutanix AOS must implement replay-resistant authentication mechanisms for network access to privileged accounts.

**Rule ID:** `SV-254205r958494_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the operating system. Authentication sessions between the authenticator and the operating system validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. A privileged account is any information system account with authorizations of a privileged user. Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., TLS, WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators. Satisfies: SRG-OS-000112-GPOS-00057, SRG-OS-000113-GPOS-00058</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS has SSH loaded and active. $ sudo systemctl status sshd sshd.service - OpenSSH server daemon Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled) Active: active (running) since Tue 2015-11-17 15:17:22 EST; 4 weeks 0 days ago Main PID: 1348 (sshd) CGroup: /system.slice/sshd.service 1053 /usr/sbin/sshd -D If "sshd" does not show a status of "active" and "running", this is a finding. If the "SSH server" package is not installed, this is a finding.

## Group: SRG-OS-000114-GPOS-00059

**Group ID:** `V-254206`

### Rule: Nutanix AOS must be configured to disable USB mass storage devices.

**Rule ID:** `SV-254206r958498_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without identifying devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Peripherals include, but are not limited to, devices such as flash drives, external storage, and printers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to disable USB mass storage devices. $ sudo grep -r usb-storage /etc/modprobe.d/* | grep -i "/bin/true" | grep -v "^#" install usb-storage /bin/true If the command does not return any output, or the line is commented out, and use of USB Storage is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding. Verify the operating system disables the ability to use USB mass storage devices. Determine if USB mass storage is disabled with the following command: $ sudo grep usb-storage /etc/modprobe.d/* | grep -i "blacklist" | grep -v "^#" blacklist usb-storage If the command does not return any output or the output is not "blacklist usb-storage", and use of USB storage devices is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000118-GPOS-00060

**Group ID:** `V-254207`

### Rule: Nutanix AOS must be configured to disable user accounts after the password expires.

**Rule ID:** `SV-254207r982189_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. Operating systems need to track periods of inactivity and disable application identifiers after zero days of inactivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to disable user accounts after the password expires. $ sudo grep -i inactive /etc/default/useradd INACTIVE=0 If the value is not set to "0", is commented out, or is not defined, this is a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-254208`

### Rule: Nutanix AOS must enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-254208r982195_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to require complex passwords. Note: The value to require a number of uppercase characters to be set is expressed as a negative number in "/etc/security/pwquality.conf". Check the value for "ucredit" in "/etc/security/pwquality.conf" with the following command. $ sudo grep ucredit /etc/security/pwquality.conf ucredit = -1 If the value of "ucredit" is not set to a negative value, this is a finding.

## Group: SRG-OS-000070-GPOS-00038

**Group ID:** `V-254209`

### Rule: Nutanix AOS must enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-254209r982196_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to require complex passwords. Note: The value to require a number of lowercase characters to be set is expressed as a negative number in "/etc/security/pwquality.conf". Check the value for "lcredit" in "/etc/security/pwquality.conf" with the following command: $ sudo grep lcredit /etc/security/pwquality.conf lcredit = -1 If the value of "lcredit" is not set to a negative value, this is a finding.

## Group: SRG-OS-000071-GPOS-00039

**Group ID:** `V-254210`

### Rule: Nutanix AOS must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-254210r982197_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to require complex passwords. Note: The value to require a number of numeric characters to be set is expressed as a negative number in "/etc/security/pwquality.conf". Check the value for "dcredit" in "/etc/security/pwquality.conf" with the following command: $ sudo grep dcredit /etc/security/pwquality.conf dcredit = -1 If the value of "dcredit" is not set to a negative value, this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-254211`

### Rule: Nutanix AOS must enforce a minimum 15 character password length.

**Rule ID:** `SV-254211r982202_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to enforce a minimum 15 character password length. $ sudo grep minlen /etc/security/pwquality.conf minlen = 15 If the command does not return a "minlen" value of "15" or greater, this is a finding.

## Group: SRG-OS-000266-GPOS-00101

**Group ID:** `V-254212`

### Rule: Nutanix AOS must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-254212r991561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity or strength is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor in determining how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Special characters are those characters that are not alphanumeric. Examples include: ~ ! @ # $ % ^ *.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS enforces password complexity by requiring that at least one special character be used. Note: The value to require a number of special characters to be set is expressed as a negative number in "/etc/security/pwquality.conf". Check the value for "ocredit" in "/etc/security/pwquality.conf" with the following command: $ sudo grep ocredit /etc/security/pwquality.conf ocredit=-1 If the value of "ocredit" is not set to a negative value, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-254213`

### Rule: Nutanix AOS must require the change of at least 50 percent of the total number of characters when passwords are changed.

**Rule ID:** `SV-254213r982198_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. If the password length is an odd number, then number of changed characters must be rounded up. For example, a password length of 15 characters must require the change of at least eight characters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Nutanix AOS is configured to require complex passwords. $ sudo grep difok /etc/security/pwquality.conf difok = 8 If the value of "difok" is set to less than "8", this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-254214`

### Rule: Nutanix AOS must require the change of at least four character classes when passwords are changed.

**Rule ID:** `SV-254214r982198_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. If the password length is an odd number then number of changed characters must be rounded up. For example, a password length of 15 characters must require the change of at least eight characters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Nutanix AOS is configured to require complex passwords. $ sudo grep minclass /etc/security/pwquality.conf minclass = 4 If the value of "minclass" is set to less than "4", this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-254215`

### Rule: Nutanix AOS must require the maximum number of repeating characters be limited to three when passwords are changed.

**Rule ID:** `SV-254215r982198_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. If the password length is an odd number then number of changed characters must be rounded up. For example, a password length of 15 characters must require the change of at least eight characters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Nutanix AOS is configured to require complex passwords. $ sudo grep maxrepeat /etc/security/pwquality.conf maxrepeat = 2 If the value of "maxrepeat" is set to more than "2", this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-254216`

### Rule: Nutanix AOS must require the maximum number of repeating characters of the same character class be limited to four when passwords are changed.

**Rule ID:** `SV-254216r982198_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. If the password length is an odd number then number of changed characters must be rounded up. For example, a password length of 15 characters must require the change of at least eight characters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Nutanix AOS is configured to require complex passwords. $ sudo grep maxclassrepeat /etc/security/pwquality.conf maxclassrepeat = 4 If the value of "maxclassrepeat" is set to more than "4", this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-254217`

### Rule: Nutanix AOS must store only encrypted representations of passwords.

**Rule ID:** `SV-254217r982199_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to store encrypted representation of passwords and that the encryption meets required standards. $ sudo grep -i encrypt /etc/login.defs ENCRYPT_METHOD SHA512 If the /etc/login.defs file does not contain the required output, this is a finding. $ sudo grep -i sha512 /etc/libuser.conf crypt_style = sha512 If the /etc/libuser.conf file does not contain the required output, this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-254218`

### Rule: Nutanix AOS must enforce 24 hours/1 day as the minimum password lifetime.

**Rule ID:** `SV-254218r982188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to enforce 24 hour/1 day minimum password lifetime. $ sudo grep -i pass_min_days /etc/login.defs PASS_MIN_DAYS 1 If the "PASS_MIN_DAYS" parameter value is not "1" or greater, or is commented out, this is a finding. $ sudo awk -F: '$4 < 1 {print $1 " " $4}' /etc/shadow If any results are returned that are not associated with a system account, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-254219`

### Rule: Nutanix AOS must enforce a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-254219r982200_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If the operating system does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the operating system passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to enforce a 60-day maximum password lifetime. $ sudo grep -i pass_max_days /etc/login.defs PASS_MAX_DAYS 60 If the "PASS_MAX_DAYS" parameter value is not "60" or less, or is commented out, this is a finding. $ sudo awk -F: '$5 > 60 {print $1 " " $5}' /etc/shadow If any results are returned that are not associated with a system account, this is a finding.

## Group: SRG-OS-000077-GPOS-00045

**Group ID:** `V-254220`

### Rule: Nutanix AOS must prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-254220r982201_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to prohibit password reuse for a minimum of five generations. $ sudo grep -i remember /etc/pam.d/system-auth /etc/pam.d/password-auth password requisite pam_pwhistory.so use_authtok remember=5 retry=3 If the line containing the "pam_pwhistory.so" line does not have the "remember" module argument set, is commented out, or the value of the "remember" module argument is set to less than "5", this is a finding.

## Group: SRG-OS-000383-GPOS-00166

**Group ID:** `V-254221`

### Rule: Nutanix AOS must prohibit the use of cached authenticators.

**Rule ID:** `SV-254221r958828_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cached authentication information is out-of-date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is not configured to allow cached credentials via the System Security Session Daemon (SSSD). $ service sssd status If the sssd service is installed or active, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-254222`

### Rule: Nutanix AOS pam_unix.so module must be configured in the password-auth file to use a FIPS 140-2 approved cryptographic hashing algorithm for system authentication.

**Rule ID:** `SV-254222r971535_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms used for authentication to the cryptographic module are not verified and therefore, cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised. Operating systems utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DoD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general purpose computing system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the pam_unix.so module is configured to use SHA512. $ sudo grep password /etc/pam.d/password-auth | grep pam_unix password sufficient pam_unix.so sha512 shadow try_first_pass use_authtok $ sudo grep password /etc/pam.d/system-auth | grep pam_unix password sufficient pam_unix.so sha512 shadow try_first_pass use_authtok If "sha512" is not an option in both outputs, or is commented out, this is a finding.

## Group: SRG-OS-000392-GPOS-00172

**Group ID:** `V-254223`

### Rule: Nutanix AOS must audit all activities performed during nonlocal maintenance and diagnostic sessions.

**Rule ID:** `SV-254223r958846_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If events associated with nonlocal administrative access or diagnostic sessions are not logged, a major tool for assessing and investigating attacks would not be available. This requirement addresses auditing-related issues associated with maintenance tools used specifically for diagnostic and repair actions on organizational information systems. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. This requirement applies to hardware/software diagnostic test equipment or tools. This requirement does not cover hardware/software components that may support information system maintenance, yet are a part of the system, for example, the software implementing "ping," "ls," "ipconfig," or the hardware and software implementing the monitoring port of an Ethernet switch.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS audits all required activities performed during nonlocal maintenance and diagnostic sessions. $ sudo grep -i /usr/sbin/semanage /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/semanage -F perm=x -F auid>=1000 -F auid!=4294967295 -k secobjects $ sudo grep -i /usr/sbin/setsebool /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/setsebool -F perm=x -F auid>=1000 -F auid!=4294967295 -k secobjects $ sudo grep -i /usr/bin/chcon /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chcon -F perm=x -F auid>=1000 -F auid!=4294967295 -k secobjects $ sudo grep -iw /usr/sbin/setfiles /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/setfiles -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-priv_change $ sudo grep -i /var/run/faillock /etc/audit/audit.rules -w /var/run/faillock/ -p wa -k logins $ sudo grep -i /var/log/lastlog /etc/audit/audit.rules -w /var/log/lastlog -p wa -k logins If any of the commands listed do not return any output, this is a finding.

## Group: SRG-OS-000478-GPOS-00223

**Group ID:** `V-254224`

### Rule: Nutanix AOS must enable FIPS mode to implement NIST FIPS-validated cryptography.

**Rule ID:** `SV-254224r959006_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The operating system must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. Satisfies: SRG-OS-000478-GPOS-00223, SRG-OS-000396-GPOS-00176</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS implements DoD-approved encryption to protect the confidentiality of remote access sessions. Determine if the "dracut-fips" package is installed with the following command: $ sudo yum list installed dracut-fips dracut-fips.x86_64-033-572.el7 If dracut-fips package is not installed, this is a finding. Determine if FIPS mode is enabled with the following command: $ fipscheck usage: fipscheck [-s <hmac-suffix>] <paths-to-files> fips mode is on If FIPS mode is "on", Determine if the kernel boot parameter is configured for FIPS mode with the following command: $ sudo cat /boot/grub/grub.conf | grep fips It the kernel output does not list "fips=1", this is a finding. If the kernel boot parameter is configured to use FIPS mode, Determine if the system is in FIPS mode with the following command: $ sudo cat /proc/sys/crypto/fips_enabled 1 If FIPS mode is not "on", the kernel boot parameter is not configured for FIPS mode, or the system does not have a value of "1" for "fips_enabled" in "/proc/sys/crypto", this is a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-254225`

### Rule: Nutanix AOS must be configured to run SELinux Policies.

**Rule ID:** `SV-254225r958518_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Nutanix AOS is configured by default to run SELinux Policies. Confirm Nutanix AOS has the policycoreutils package installed with the following command: $ sudo yum list installed policycoreutils Installed Packages policycoreutils.x86_64 2.5-34.el7 @base If the policycoreutils package is not installed, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-254226`

### Rule: Nutanix AOS must be configured to restrict public directories.

**Rule ID:** `SV-254226r958524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DoD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS provides that all public directories are owned by root or a system account with the following command: $ sudo find / -type d -perm -0002 -exec ls -lLd {} \; drwxrwxrwt. 2 root root 40 Jun 4 15:21 /dev/mqueue drwxrwxrwt. 2 root root 40 Jun 4 15:21 /dev/shm drwxrwxrwt. 7 root root 4096 Jul 28 15:37 /tmp If any of the returned directories are not owned by root or a system account, this is a finding. Determine that all world-writable directories have the sticky bit set by running the following command: $ sudo find / -type d \( -perm -0002 -a ! -perm -1000 \) -print 2>/dev/null drwxrwxrwxt 7 root root 4096 Jul 26 11:19 /tmp If any of the returned directories are world-writable and do not have the sticky bit set, this is a finding.

## Group: SRG-OS-000420-GPOS-00186

**Group ID:** `V-254227`

### Rule: Nutanix AOS must protect against or limit the effects of denial-of-service (DoS) attacks by ensuring the operating system is implementing rate-limiting measures on impacted network interfaces.

**Rule ID:** `SV-254227r958902_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of the operating system to mitigate the impact of DoS attacks that have occurred or are ongoing on system availability. For each system, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or establishing memory partitions). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS protects against or limits the effects of DoS attacks by ensuring that a rate-limiting measures are enabled. $ /sbin/sysctl -a | grep 'net.ipv4.tcp_invalid_ratelimit' net.ipv4.tcp_invalid_ratelimit = 500 If "net.ipv4.tcp_invalid_ratelimit" has a value of "0", this is a finding. If "net.ipv4.tcp_invalid_ratelimit" has a value greater than "1000" and is not documented with the Information System Security Officer (ISSO), this is a finding.

## Group: SRG-OS-000142-GPOS-00071

**Group ID:** `V-254228`

### Rule: Nutanix AOS must be configured to use syncookies to limit denial-of-service (DoS) attacks.

**Rule ID:** `SV-254228r958528_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Managing excess capacity ensures that sufficient capacity is available to counter flooding attacks. Employing increased capacity and service redundancy may reduce the susceptibility to some DoS attacks. Managing excess capacity may include, for example, establishing selected usage priorities, quotas, or partitioning.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to use syncookies. $ sysctl net.ipv4.tcp_syncookies net.ipv4.tcp_syncookies = 1 If the value is not "1", this is a finding. Check the saved value of TCP syncookies with the following command: $ sudo grep -i net.ipv4.tcp_syncookies /etc/sysctl.conf /etc/sysctl.d/* | grep -v '#' If no output is returned, this is a finding.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-254229`

### Rule: Nutanix AOS must protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-254229r958908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS has SSH loaded and active. $ sudo systemctl status sshd sshd.service - OpenSSH server daemon Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled) Active: active (running) since Tue 2015-11-17 15:17:22 EST; 4 weeks 0 days ago Main PID: 1348 (sshd) CGroup: /system.slice/sshd.service 1053 /usr/sbin/sshd -D If "sshd" does not show a status of "active" and "running", this is a finding. If the "SSH server" package is not installed, this is a finding.

## Group: SRG-OS-000425-GPOS-00189

**Group ID:** `V-254230`

### Rule: Nutanix AOS must maintain the confidentiality and integrity of information during preparation for transmission.

**Rule ID:** `SV-254230r958912_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Ensuring the confidentiality of transmitted information requires the operating system to take measures in preparing information for transmission. This can be accomplished via access control and encryption. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, operating systems need to support transmission protection mechanisms such as TLS, SSL VPNs, or IPsec.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS has SSH loaded and active. $ sudo systemctl status sshd sshd.service - OpenSSH server daemon Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled) Active: active (running) since Tue 2015-11-17 15:17:22 EST; 4 weeks 0 days ago Main PID: 1348 (sshd) CGroup: /system.slice/sshd.service 1053 /usr/sbin/sshd -D If "sshd" does not show a status of "active" and "running", this is a finding. If the "SSH server" package is not installed, this is a finding.

## Group: SRG-OS-000426-GPOS-00190

**Group ID:** `V-254231`

### Rule: Nutanix AOS must maintain the confidentiality and integrity of information during reception.

**Rule ID:** `SV-254231r958914_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Ensuring the confidentiality of transmitted information requires the operating system to take measures in preparing information for transmission. This can be accomplished via access control and encryption. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When receiving data, operating systems need to leverage protection mechanisms such as TLS, SSL VPNs, or IPsec.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS has SSH loaded and active. $ sudo systemctl status sshd sshd.service - OpenSSH server daemon Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled) Active: active (running) since Tue 2015-11-17 15:17:22 EST; 4 weeks 0 days ago Main PID: 1348 (sshd) CGroup: /system.slice/sshd.service 1053 /usr/sbin/sshd -D If "sshd" does not show a status of "active" and "running", this is a finding. If the "SSH server" package is not installed, this is a finding.

## Group: SRG-OS-000205-GPOS-00083

**Group ID:** `V-254232`

### Rule: Nutanix AOS must generate error messages that provide information necessary for corrective actions without revealing information that could be exploited by adversaries.

**Rule ID:** `SV-254232r958564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> Any operating system providing too much information in error messages risks compromising the data and security of the structure, and content of error messages needs to be carefully considered by the organization. Organizations carefully consider the structure/content of error messages. The extent to which information systems are able to identify and handle error conditions is guided by organizational policy and operational requirements. Information that could be exploited by adversaries includes, for example, erroneous logon attempts with passwords entered by mistake as the username, mission/business information that can be derived from (if not stated explicitly by) information recorded, and personal information, such as account numbers, social security numbers, and credit card numbers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Nutanix AOS has all system log files under the /home/log directory with a permission set to "640", by using the following command: $ sudo find /home/log -perm /137 -type f -exec stat -c "%n %a" {} \; If command displays any output, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-254233`

### Rule: Nutanix AOS must reveal error messages only to authorized users.

**Rule ID:** `SV-254233r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Nutanix AOS audit logs must be owned by root to prevent unauthorized read access. Determine where the audit log file is located: $sudo grep -iw log_file /etc/audit/auditd.conf log_file = /home/log/audit/audit.log Using the location of the audit log file, determine if the audit log is owned by "root" using the following command: ls -al /home/log/audit/audit.log -rw-------. 1 root root 3427758 Apr 8 18:43 /home/log/audit/audit.log If the audit log is not owned by "root", this is a finding.

## Group: SRG-OS-000433-GPOS-00192

**Group ID:** `V-254234`

### Rule: Nutanix AOS must implement nonexecutable data to protect its memory from unauthorized code execution.

**Rule ID:** `SV-254234r958928_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in nonexecutable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can either be hardware-enforced or software-enforced with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Nutanix AOS is configured to implement nonexecutable data to protect its memory from unauthorized code execution. $ sudo grep flags /proc/cpuinfo | grep -w nx flags. : fpu vme de …. nx pdpe1gb rdtscp... If "flags" does not contain the "nx" flag, this is a finding.

## Group: SRG-OS-000433-GPOS-00193

**Group ID:** `V-254235`

### Rule: Nutanix AOS must implement address space layout randomization to protect its memory from unauthorized code execution.

**Rule ID:** `SV-254235r958928_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in nonexecutable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can either be hardware-enforced or software-enforced with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS is configured to implement address space layout randomization. $ sudo sysctl kernel.randomize_va_space kernel.randomize_va_space = 2 If the value of kernel.randomize_va_space is anything other than "2", this is a finding.

## Group: SRG-OS-000437-GPOS-00194

**Group ID:** `V-254236`

### Rule: Nutanix AOS must remove all software components after updated versions have been installed.

**Rule ID:** `SV-254236r958936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Previous versions of software components that are not removed from the information system after updates have been installed may be exploited by adversaries. Some information technology products may remove older versions of software automatically from the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS removes all software components after updated versions have been installed. $ sudo grep -i clean_requirements_on_remove /etc/yum.conf clean_requirements_on_remove=1 If "clean_requirements_on_remove" is not set to "1", "True", or "yes", or is not set in "/etc/yum.conf", this is a finding.

## Group: SRG-OS-000445-GPOS-00199

**Group ID:** `V-254237`

### Rule: Nutanix AOS must be configured to use SELinux Enforcing mode.

**Rule ID:** `SV-254237r958944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. This requirement applies to operating systems performing security function verification/testing and/or systems and environments that require this functionality. Satisfies: SRG-OS-000445-GPOS-00199, SRG-OS-000446-GPOS-00200, SRG-OS-000447-GPOS-00201, SRG-OS-000134-GPOS-00068</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Nutanix AOS verifies correct operation of all security functions. $ sudo sestatus SELinux status: enabled SELinuxfs mount: /sys/fs/selinux SELinux root directory: /etc/selinux Loaded policy name: targeted Current mode: enforcing Mode from config file: enforcing Policy MLS status: enabled Policy deny_unknown status: allowed Max kernel policy version: 31 If the "Loaded policy name" is not set to "targeted", this is a finding. Verify that the /etc/selinux/config file is configured to the "SELINUXTYPE" to "targeted": $ sudo grep -i "selinuxtype" /etc/selinux/config | grep -v '^#' SELINUXTYPE = targeted If no results are returned or "SELINUXTYPE" is not set to "targeted", this is a finding.

## Group: SRG-OS-000439-GPOS-00195

**Group ID:** `V-264424`

### Rule: Nutanix AOS must be running an operating system release that is currently supported by the vendor.

**Rule ID:** `SV-264424r992069_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes) to production systems after thorough testing of the patches within a lab environment. Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Product version is end of life and no longer supported. If the system is running AOS version 5.20.x, this is a finding.

