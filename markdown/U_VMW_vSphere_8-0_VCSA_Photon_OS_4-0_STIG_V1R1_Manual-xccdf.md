# STIG Benchmark: VMware vSphere 8.0 vCenter Appliance Photon OS 4.0 Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-258801`

### Rule: The Photon operating system must audit all account creations.

**Rule ID:** `SV-258801r933464_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create an account. Auditing account creation actions provides logging that can be used for forensic purposes. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify an audit rule exists to audit account creations: # auditctl -l | grep -E "(useradd|groupadd)" Example result: -w /usr/sbin/useradd -p x -k useradd -w /usr/sbin/groupadd -p x -k groupadd If either "useradd" or "groupadd" are not listed with a permissions filter of at least "x", this is a finding. Note: This check depends on the "auditd" service to be in a running state for accurate results. The "auditd" service is enabled in control PHTN-40-000016.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-258802`

### Rule: The Photon operating system must enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period.

**Rule ID:** `SV-258802r933467_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following commands to verify accounts are locked after three consecutive invalid logon attempts by a user during a 15-minute time period: # grep '^deny =' /etc/security/faillock.conf Example result: deny = 3 If the "deny" option is not set to "3" or less (but not "0"), is missing or commented out, this is a finding. # grep '^fail_interval =' /etc/security/faillock.conf Example result: fail_interval = 900 If the "fail_interval" option is not set to "900" or more, is missing or commented out, this is a finding. Note: If faillock.conf is not used to configure the "pam_faillock.so" module, then these options may be specified on the faillock lines in the system-auth and system-account PAM files.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-258803`

### Rule: The Photon operating system must display the Standard Mandatory DOD Notice and Consent Banner before granting local or remote access to the system.

**Rule ID:** `SV-258803r933470_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify SSH is configured to use the /etc/issue file for a banner: # sshd -T|&grep -i Banner Example result: banner /etc/issue If the "banner" setting is not configured to "/etc/issue", this is a finding. Next, open /etc/issue with a text editor. If the file does not contain the Standard Mandatory DOD Notice and Consent Banner, this is a finding. Standard Mandatory DOD Notice and Consent Banner: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details."

## Group: SRG-OS-000027-GPOS-00008

**Group ID:** `V-258804`

### Rule: The Photon operating system must limit the number of concurrent sessions to ten for all accounts and/or account types.

**Rule ID:** `SV-258804r933473_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Operating system management includes the ability to control the number of users and user sessions that utilize an operating system. Limiting the number of allowed users and sessions per user is helpful in reducing the risks related to Denial of Service (DoS) attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the limit for the number of concurrent sessions: # grep "^[^#].*maxlogins.*" /etc/security/limits.conf Example result: * hard maxlogins 10 If "* hard maxlogins" is not configured to "10", this is a finding. Note: The expected result may be repeated multiple times.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-258805`

### Rule: The Photon operating system must monitor remote access logins.

**Rule ID:** `SV-258805r933476_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyberattacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If another package is used to offload logs, such as syslog-ng, and is properly configured, this is not applicable. At the command line, run the following command to verify rsyslog is configured to log authentication requests: # grep -E "(^auth.*|^authpriv.*|^daemon.*)" /etc/rsyslog.conf Example result: auth.*;authpriv.*;daemon.* /var/log/audit/sshinfo.log If "auth.*", "authpriv.*", and "daemon.*" are not configured to be logged, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-258806`

### Rule: The Photon operating system must have the OpenSSL FIPS provider installed to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-258806r933479_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. OpenSSH on the Photon operating system when configured appropriately can utilize a FIPS validated OpenSSL for cryptographic operations. Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174, SRG-OS-000423-GPOS-00187, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the OpenSSL FIPS provider is installed: # rpm -qa | grep openssl-fips Example result: openssl-fips-provider-3.0.3-1.ph4.x86_64 If there is no output indicating that the OpenSSL FIPS provider is installed, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-258807`

### Rule: The Photon operating system must configure auditd to log to disk.

**Rule ID:** `SV-258807r933482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content must be shipped to a central location, but it must also be logged locally.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify auditd is configured to write logs to disk: # grep '^write_logs' /etc/audit/auditd.conf Example result: write_logs = yes If there is no output, this is not a finding. If "write_logs" exists and is not configured to "yes", this is a finding.

## Group: SRG-OS-000039-GPOS-00017

**Group ID:** `V-258808`

### Rule: The Photon operating system must enable the auditd service.

**Rule ID:** `SV-258808r933485_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. To that end, the auditd service must be configured to start automatically and be running at all times. Satisfies: SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00021, SRG-OS-000062-GPOS-00031, SRG-OS-000255-GPOS-00096, SRG-OS-000363-GPOS-00150, SRG-OS-000365-GPOS-00152, SRG-OS-000446-GPOS-00200</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify auditd is enabled and running: # systemctl status auditd If the service is not enabled and running, this is a finding.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-258809`

### Rule: The Photon operating system must be configured to audit the execution of privileged functions.

**Rule ID:** `SV-258809r933488_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing all actions by superusers is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat. Satisfies: SRG-OS-000042-GPOS-00020, SRG-OS-000326-GPOS-00126</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify audit rules exist to audit privileged functions: # auditctl -l | grep execve Expected result: -a always,exit -F arch=b32 -S execve -C uid!=euid -F euid=0 -F key=execpriv -a always,exit -F arch=b64 -S execve -C uid!=euid -F euid=0 -F key=execpriv -a always,exit -F arch=b32 -S execve -C gid!=egid -F egid=0 -F key=execpriv -a always,exit -F arch=b64 -S execve -C gid!=egid -F egid=0 -F key=execpriv If the output does not match the expected result, this is a finding. Note: This check depends on the "auditd" service to be in a running state for accurate results. The "auditd" service is enabled in control PHTN-40-000016.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-258810`

### Rule: The Photon operating system must alert the ISSO and SA in the event of an audit processing failure.

**Rule ID:** `SV-258810r933491_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. Satisfies: SRG-OS-000046-GPOS-00022, SRG-OS-000344-GPOS-00135</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify auditd is configured to send an alert via syslog in the event of an audit processing failure: # grep -E "^disk_full_action|^disk_error_action|^admin_space_left_action" /etc/audit/auditd.conf Example result: admin_space_left_action = SYSLOG disk_full_action = SYSLOG disk_error_action = SYSLOG If "disk_full_action", "disk_error_action", and "admin_space_left_action" are not set to SYSLOG or are missing, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-258811`

### Rule: The Photon operating system must protect audit logs from unauthorized access.

**Rule ID:** `SV-258811r933494_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to find the current auditd log location: # grep -iw log_file /etc/audit/auditd.conf Example result: log_file = /var/log/audit/audit.log At the command line, run the following command using the file found in the previous step to verify auditd logs are protected from authorized access: # stat -c "%n %U:%G %a" /var/log/audit/audit.log Example result: /var/log/audit/audit.log root:root 600 If the audit log file does not have permissions set to "0600", this is a finding. If the audit log file is not owned by root, this is a finding. If the audit log file is not group owned by root, this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-258812`

### Rule: The Photon operating system must allow only authorized users to configure the auditd service.

**Rule ID:** `SV-258812r933497_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify permissions on auditd configuration and rules files: # find /etc/audit/* -type f -exec stat -c "%n %U:%G %a" {} $1\; If any files are returned with permissions more permissive than "0640", this is a finding. If any files are returned not owned by root, this is a finding. If any files are returned not group owned by root, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-258813`

### Rule: The Photon operating system must generate audit records when successful/unsuccessful attempts to access privileges occur.

**Rule ID:** `SV-258813r933500_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The changing of file permissions could indicate that a user is attempting to gain access to information that would otherwise be disallowed. Auditing DAC modifications can facilitate the identification of patterns of abuse among both authorized and unauthorized users. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206, SRG-OS-000466-GPOS-00210, SRG-OS-000468-GPOS-00212, SRG-OS-000474-GPOS-00219</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify an audit rule exists to audit account creations: # auditctl -l | grep chmod Expected result: -a always,exit -F arch=b64 -S chmod,fchmod,chown,fchown,lchown,setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr,fchownat,fchmodat -F auid>=1000 -F auid!=-1 -F key=perm_mod -a always,exit -F arch=b64 -S chmod,fchmod,chown,fchown,lchown,setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr,fchownat,fchmodat -F auid=0 -F key=perm_mod -a always,exit -F arch=b32 -S chmod,lchown,fchmod,fchown,chown,setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr,fchownat,fchmodat -F auid>=1000 -F auid!=-1 -F key=perm_mod -a always,exit -F arch=b32 -S chmod,lchown,fchmod,fchown,chown,setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr,fchownat,fchmodat -F auid=0 -F key=perm_mod If the output does not match the expected result, this is a finding. Note: This check depends on the "auditd" service to be in a running state for accurate results. The "auditd" service is enabled in control PHTN-40-000016. Note: auid!=-1, auid!=4294967295, auid!=unset are functionally equivalent in this check and the output of the above commands may be displayed in either format.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-258814`

### Rule: The Photon operating system must enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-258814r933503_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify at least one uppercase character be used: # grep '^password.*pam_pwquality.so' /etc/pam.d/system-password Example result: password requisite pam_pwquality.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=15 difok=8 enforce_for_root dictcheck=1 If the "ucredit" option is not < 0, is missing or commented out, this is a finding.

## Group: SRG-OS-000070-GPOS-00038

**Group ID:** `V-258815`

### Rule: The Photon operating system must enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-258815r933506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify at least one lowercase character be used: # grep '^password.*pam_pwquality.so' /etc/pam.d/system-password Example result: password requisite pam_pwquality.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=15 difok=8 enforce_for_root dictcheck=1 If the "lcredit" option is not < 0, is missing or commented out, this is a finding.

## Group: SRG-OS-000071-GPOS-00039

**Group ID:** `V-258816`

### Rule: The Photon operating system must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-258816r933509_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify at least one numeric character be used: # grep '^password.*pam_pwquality.so' /etc/pam.d/system-password Example result: password requisite pam_pwquality.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=15 difok=8 enforce_for_root dictcheck=1 If the "dcredit" option is not < 0, is missing or commented out, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-258817`

### Rule: The Photon operating system must require the change of at least eight characters when passwords are changed.

**Rule ID:** `SV-258817r933512_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> If the operating system allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. If the password length is an odd number then number of changed characters must be rounded up. For example, a password length of 15 characters must require the change of at least eight characters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify at least eight different characters be used: # grep '^password.*pam_pwquality.so' /etc/pam.d/system-password Example result: password requisite pam_pwquality.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=15 difok=8 enforce_for_root dictcheck=1 If the "difok" option is not >= 8, is missing or commented out, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-258818`

### Rule: The operating system must store only encrypted representations of passwords.

**Rule ID:** `SV-258818r933515_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify passwords are stored with only encrypted representations: # grep ^ENCRYPT_METHOD /etc/login.defs Example result: ENCRYPT_METHOD SHA512 If the "ENCRYPT_METHOD" option is not set to "SHA512", is missing or commented out, this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-258819`

### Rule: The Photon operating system must not have the telnet package installed.

**Rule ID:** `SV-258819r933518_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify telnet is not installed: # rpm -qa | grep telnet If any results are returned indicating telnet is installed, this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-258820`

### Rule: The Photon operating system must enforce one day as the minimum password lifetime.

**Rule ID:** `SV-258820r933521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify one day as the minimum password lifetime: # grep '^PASS_MIN_DAYS' /etc/login.defs If "PASS_MIN_DAYS" is not set to 1, is missing or commented out, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-258821`

### Rule: The Photon operating systems must enforce a 90-day maximum password lifetime restriction.

**Rule ID:** `SV-258821r933524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If the operating system does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the operating system passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify a 90-day maximum password lifetime restriction: # grep '^PASS_MAX_DAYS' /etc/login.defs If "PASS_MAX_DAYS" is not set to <= 90, is missing or commented out, this is a finding.

## Group: SRG-OS-000077-GPOS-00045

**Group ID:** `V-258822`

### Rule: The Photon operating system must prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-258822r933527_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following commands to verify passwords are not reused for a minimum of five generations: # grep '^password.*pam_pwhistory.so' /etc/pam.d/system-password Example result: password required pam_pwhistory.so remember=5 retry=3 enforce_for_root use_authtok If the "remember" option is not set to "5" or greater, this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-258823`

### Rule: The Photon operating system must enforce a minimum 15-character password length.

**Rule ID:** `SV-258823r933530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify a minimum 15-character password length: # grep '^password.*pam_pwquality.so' /etc/pam.d/system-password Example result: password requisite pam_pwquality.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=15 difok=8 enforce_for_root dictcheck=1 If the "minlen" option is not >= 15, is missing or commented out, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-258824`

### Rule: The Photon operating system must require authentication upon booting into single-user and maintenance modes.

**Rule ID:** `SV-258824r933533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system does not require authentication before it boots into single-user mode, anyone with console access to the system can trivially access all files on the system. GRUB2 is the boot loader for Photon OS and can be configured to require a password to boot into single-user mode or make modifications to the boot menu. Note: Photon does not support building grub changes via grub2-mkconfig.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify a password is required to edit the grub bootloader to boot into single-user mode: # grep -E "^set\ssuperusers|^password_pbkdf2" /boot/grub2/grub.cfg Example output: set superusers="root" password_pbkdf2 root grub.pbkdf2.sha512.[password_hash] If superusers is not set, this is a finding. If a password is not set for the super user, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-258825`

### Rule: The Photon operating system must disable unnecessary kernel modules.

**Rule ID:** `SV-258825r933536_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of nonessential capabilities include, but are not limited to, games, software packages, tools, and demonstration software, not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled. Satisfies: SRG-OS-000095-GPOS-00049, SRG-OS-000114-GPOS-00059</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the following kernel modules are not loaded: # modprobe --showconfig | grep "^install" | grep "/bin" Expected result: install bridge /bin/false install sctp /bin/false install dccp /bin/false install dccp_ipv4 /bin/false install dccp_ipv6 /bin/false install ipx /bin/false install appletalk /bin/false install decnet /bin/false install rds /bin/false install tipc /bin/false install bluetooth /bin/false install usb_storage /bin/false install ieee1394 /bin/false install cramfs /bin/false install freevxfs /bin/false install jffs2 /bin/false install hfs /bin/false install hfsplus /bin/false install squashfs /bin/false install udf /bin/false The output may include other statements outside of the expected result. If the output does not include at least every statement in the expected result, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-258826`

### Rule: The Photon operating system must not have duplicate User IDs (UIDs).

**Rule ID:** `SV-258826r933539_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational users must be uniquely identified and authenticated to prevent potential misuse and provide for nonrepudiation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify there are no duplicate user IDs present: # awk -F ":" 'list[$3]++{print $1, $3}' /etc/passwd If any lines are returned, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-258827`

### Rule: The Photon operating system must use mechanisms meeting the requirements of applicable federal laws, Executive orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module.

**Rule ID:** `SV-258827r933542_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and DOD data may be compromised. Operating systems utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2/140-3 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DOD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general purpose computing system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify system-password is configured to encrypt representations of passwords: # grep sha512 /etc/pam.d/system-password Example result: password required pam_unix.so sha512 shadow use_authtok If the "pam_unix.so" module is not configured with the "sha512" parameter, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-258828`

### Rule: The Photon operating system must restrict access to the kernel message buffer.

**Rule ID:** `SV-258828r933545_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting access to the kernel message buffer limits access only to root. This prevents attackers from gaining additional system information as a nonprivileged user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify kernel message buffer restrictions are enabled: # /sbin/sysctl kernel.dmesg_restrict Example result: kernel.dmesg_restrict = 1 If the "kernel.dmesg_restrict" kernel parameter is not set to "1", this is a finding.

## Group: SRG-OS-000142-GPOS-00071

**Group ID:** `V-258829`

### Rule: The Photon operating system must be configured to use TCP syncookies.

**Rule ID:** `SV-258829r933548_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A TCP SYN flood attack can cause a Denial of Service (DOS) by filling a system's TCP connection table with connections in the SYN_RCVD state. Syncookies can be used to track a connection when a subsequent ACK is received, verifying the initiator is attempting a valid connection and is not a flood source. This feature is activated when a flood condition is detected and enables the system to continue servicing valid connection requests. Satisfies: SRG-OS-000142-GPOS-00071, SRG-OS-000420-GPOS-00186</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify TCP syncookies are enabled: # /sbin/sysctl net.ipv4.tcp_syncookies Example result: net.ipv4.tcp_syncookies = 1 If "net.ipv4.tcp_syncookies" is not set to "1", this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-258830`

### Rule: The Photon operating system must terminate idle Secure Shell (SSH) sessions after 15 minutes.

**Rule ID:** `SV-258830r933551_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level, and deallocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that the operating system terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session. Satisfies: SRG-OS-000163-GPOS-00072, SRG-OS-000395-GPOS-00175</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the running configuration of sshd: # sshd -T|&grep -i ClientAliveInterval Example result: ClientAliveInterval 900 If there is no output or if "ClientAliveInterval" is not set to "900", this is a finding.

## Group: SRG-OS-000205-GPOS-00083

**Group ID:** `V-258831`

### Rule: The Photon operating system /var/log directory must be restricted.

**Rule ID:** `SV-258831r933554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any operating system providing too much information in error messages risks compromising the data and security of the structure, and content of error messages needs to be carefully considered by the organization. Organizations carefully consider the structure/content of error messages. The extent to which information systems are able to identify and handle error conditions is guided by organizational policy and operational requirements. Information that could be exploited by adversaries includes, for example, erroneous logon attempts with passwords entered by mistake as the username, mission/business information that can be derived from (if not stated explicitly by) information recorded, and personal information, such as account numbers, social security numbers, and credit card numbers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify permissions on the /var/log directory: # stat -c "%n is owned by %U and group owned by %G with permissions of %a" /var/log Expected result: /var/log is owned by root and group owned by root with permissions of 755 If the /var/log directory is not owned by root, this is a finding. If the /var/log directory is not group owned by root, this is a finding. If the /var/log directory permissions are not set to 0755 or less, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-258832`

### Rule: The Photon operating system must reveal error messages only to authorized users.

**Rule ID:** `SV-258832r933557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If another package is used to offload logs, such as syslog-ng, and is properly configured, this is not applicable. At the command line, run the following command to verify rsyslog generates log files that are not world readable: # grep '^\$umask' /etc/rsyslog.conf Example result: $umask 0037 If "$umask" is not set to "0037" or more restrictive, this is a finding.

## Group: SRG-OS-000239-GPOS-00089

**Group ID:** `V-258833`

### Rule: The Photon operating system must audit all account modifications.

**Rule ID:** `SV-258833r933560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to modify an existing account. Auditing account modification actions provides logging that can be used for forensic purposes. To address access requirements, many operating systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify an audit rule exists to audit account modifications: # auditctl -l | grep -E "(usermod|groupmod)" Example result: -w /usr/sbin/usermod -p x -k usermod -w /usr/sbin/groupmod -p x -k groupmod If either "usermod" or "groupmod" are not listed with a permissions filter of at least "x", this is a finding. Note: This check depends on the "auditd" service to be in a running state for accurate results. The "auditd" service is enabled in control PHTN-40-000016.

## Group: SRG-OS-000241-GPOS-00091

**Group ID:** `V-258834`

### Rule: The Photon operating system must audit all account removal actions.

**Rule ID:** `SV-258834r933563_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When operating system accounts are removed, user accessibility is affected. Accounts are utilized for identifying individual users or for identifying the operating system processes themselves. In order to detect and respond to events affecting user accessibility and system processing, operating systems must audit account removal actions and, as required, notify the appropriate individuals so they can investigate the event. Such a capability greatly reduces the risk that operating system accessibility will be negatively affected for extended periods of time and provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify an audit rule exists to audit account removals: # auditctl -l | grep -E "(userdel|groupdel)" Example result: -w /usr/sbin/userdel -p x -k userdel -w /usr/sbin/groupdel -p x -k groupdel If either "userdel" or "groupdel" are not listed with a permissions filter of at least "x", this is a finding. Note: This check depends on the "auditd" service to be in a running state for accurate results. The "auditd" service is enabled in control PHTN-40-000016.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-258835`

### Rule: The Photon operating system must implement only approved ciphers to protect the integrity of remote access sessions.

**Rule ID:** `SV-258835r933566_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the running configuration of sshd: # sshd -T|&grep -i Ciphers Expected result: ciphers aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr If the output matches the ciphers in the expected result or a subset thereof, this is not a finding. If the ciphers in the output contain any ciphers not listed in the expected result, this is a finding.

## Group: SRG-OS-000254-GPOS-00095

**Group ID:** `V-258836`

### Rule: The Photon operating system must initiate session audits at system startup.

**Rule ID:** `SV-258836r933569_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If auditing is enabled late in the startup process, the actions of some startup processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify auditing is enabled at startup: # grep 'audit' /proc/cmdline Example result: BOOT_IMAGE=/boot/vmlinuz-5.10.109-2.ph4-esx root=PARTUUID=6e6293c6-9ab6-49e9-aa97-9b212f2e037a init=/lib/systemd/systemd rcupdate.rcu_expedited=1 rw systemd.show_status=1 quiet noreplace-smp cpu_init_udelay=0 plymouth.enable=0 systemd.legacy_systemd_cgroup_controller=yes audit=1 If the "audit" parameter is not present with a value of "1", this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-258837`

### Rule: The Photon operating system must protect audit tools from unauthorized access.

**Rule ID:** `SV-258837r933572_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000257-GPOS-00098, SRG-OS-000258-GPOS-00099</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify permissions on audit tools: # stat -c "%n is owned by %U and group owned by %G and permissions are %a" /usr/sbin/audispd /usr/sbin/auditctl /usr/sbin/auditd /usr/sbin/aureport /usr/sbin/ausearch /usr/sbin/autrace /usr/sbin/augenrules Expected result: /usr/sbin/audispd is owned by root and group owned by root and permissions are 750 /usr/sbin/auditctl is owned by root and group owned by root and permissions are 755 /usr/sbin/auditd is owned by root and group owned by root and permissions are 755 /usr/sbin/aureport is owned by root and group owned by root and permissions are 755 /usr/sbin/ausearch is owned by root and group owned by root and permissions are 755 /usr/sbin/autrace is owned by root and group owned by root and permissions are 755 /usr/sbin/augenrules is owned by root and group owned by root and permissions are 750 If any file is not owned by root or group owned by root or permissions are more permissive than listed above, this is a finding.

## Group: SRG-OS-000266-GPOS-00101

**Group ID:** `V-258838`

### Rule: The Photon operating system must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-258838r933575_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity or strength is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor in determining how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Special characters are those characters that are not alphanumeric. Examples include: ~ ! @ # $ % ^ *.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify at least one special character be used: # grep '^password.*pam_pwquality.so' /etc/pam.d/system-password Example result: password requisite pam_pwquality.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=15 difok=8 enforce_for_root dictcheck=1 If the "ocredit" option is not < 0, is missing or commented out, this is a finding.

## Group: SRG-OS-000278-GPOS-00108

**Group ID:** `V-258839`

### Rule: The Photon operating system must use cryptographic mechanisms to protect the integrity of audit tools.

**Rule ID:** `SV-258839r933578_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Protecting the integrity of the tools used for auditing purposes is a critical step toward ensuring the integrity of audit information. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. It is not uncommon for attackers to replace the audit tools or inject code into the existing tools with the purpose of providing the capability to hide or erase system activity from the audit logs. To address this risk, audit tools must be cryptographically signed in order to provide the capability to identify when the audit tools have been modified, manipulated, or replaced. An example is a checksum hash of the file or files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the verification capability of rpm to check the MD5 hashes of the audit files on disk versus the expected ones from the installation package. At the command line, run the following command: # rpm -V audit | grep "^..5" Example output: S.5....T. c /etc/audit/auditd.conf If there is any output for files that are not configuration files, this is a finding.

## Group: SRG-OS-000279-GPOS-00109

**Group ID:** `V-258840`

### Rule: The operating system must automatically terminate a user session after inactivity time-outs have expired.

**Rule ID:** `SV-258840r933581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination terminates all processes associated with a user's logical session except those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific operating system functionality where the system owner, data owner, or organization requires additional assurance. Satisfies: SRG-OS-000279-GPOS-00109, SRG-OS-000126-GPOS-00066</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep -E "TMOUT=900" /etc/bash.bashrc /etc/profile.d/* Example result: /etc/profile.d/tmout.sh:TMOUT=900 If the "TMOUT" environmental variable is not set, the value is more than "900", or is set to "0", this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-258841`

### Rule: The Photon operating system must enable symlink access control protection in the kernel.

**Rule ID:** `SV-258841r933584_rule`
**Severity:** high

**Description:**
<VulnDiscussion>By enabling the fs.protected_symlinks kernel parameter, symbolic links are permitted to be followed only when outside a sticky world-writable directory, or when the UID of the link and follower match, or when the directory owner matches the symlink's owner. Disallowing such symlinks helps mitigate vulnerabilities based on insecure file system accessed by privileged programs, avoiding an exploitation vector exploiting unsafe use of open() or creat().</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify symlink protection is enabled: # /sbin/sysctl fs.protected_symlinks Example result: fs.protected_symlinks = 1 If the "fs.protected_symlinks" kernel parameter is not set to "1", this is a finding.

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-258842`

### Rule: The Photon operating system must audit the execution of privileged functions.

**Rule ID:** `SV-258842r933587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000240-GPOS-00090, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to output a list of files with setuid/setgid configured and their corresponding audit rules: # for file in $(find / -xdev -path /var/lib/containerd -prune -o \( -perm -4000 -o -perm -2000 \) -type f -print | sort); do echo "Found file with setuid/setgid configured: $file";rule="$(auditctl -l | grep "$file ")";echo "Audit Rule Result: $rule";echo ""; done Example output: Found file with setuid/setgid configured: /usr/bin/chage Audit Rule Result: -a always,exit -S all -F path=/usr/bin/chage -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged Found file with setuid/setgid configured: /usr/bin/chfn Audit Rule Result: -a always,exit -S all -F path=/usr/bin/chfn -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged If each file returned does not have a corresponding audit rule, this is a finding. Note: This check depends on the "auditd" service to be in a running state for accurate results. The "auditd" service is enabled in control PHTN-40-000016. Note: auid!=-1, auid!=4294967295, auid!=unset are functionally equivalent in this check and the output of the above commands may be displayed in either format.

## Group: SRG-OS-000329-GPOS-00128

**Group ID:** `V-258843`

### Rule: The Photon operating system must automatically lock an account until the locked account is released by an administrator when three unsuccessful logon attempts in 15 minutes occur.

**Rule ID:** `SV-258843r933590_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following commands to verify accounts are locked until the locked account is released by an administrator when three unsuccessful logon attempts in 15 minutes are made: # grep '^unlock_time =' /etc/security/faillock.conf Example result: unlock_time = 0 If the "unlock_time" option is not set to "0", is missing or commented out, this is a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-258844`

### Rule: The Photon operating system must allocate audit record storage capacity to store audit records when audit records are not immediately sent to a central audit record storage facility.

**Rule ID:** `SV-258844r933593_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Audit logs are most useful when accessible by date, rather than size. This can be accomplished through a combination of an audit log rotation and setting a reasonable number of logs to keep. This ensures that audit logs are accessible to the ISSO in the event of a central log processing failure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify auditd is configured to keep a number of audit logs in the event of a central log processing failure: # grep -E "^num_logs|^max_log_file_action" /etc/audit/auditd.conf Example result: num_logs = 5 max_log_file_action = ROTATE If "num_logs" is not configured to "5" or greater, this is a finding. If "max_log_file_action" is not configured to "ROTATE", this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-258845`

### Rule: The Photon operating system must immediately notify the SA and ISSO when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity.

**Rule ID:** `SV-258845r935564_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches 75 percent utilization, they are unable to plan for audit record storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify auditd is alerting when low disk space is detected: # grep '^space_left' /etc/audit/auditd.conf Expected result: space_left = 25% space_left_action = SYSLOG If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-258846`

### Rule: The Photon operating system TDNF package management tool must cryptographically verify the authenticity of all software packages during installation.

**Rule ID:** `SV-258846r933599_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Installation of any nontrusted software, patches, service packs, device drivers, or operating system components can significantly affect the overall security of the operating system. This requirement ensures the software has not been tampered with and has been provided by a trusted vendor.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify software packages are cryptographically verified during installation: # grep '^gpgcheck' /etc/tdnf/tdnf.conf Example result: gpgcheck=1 If "gpgcheck" is not set to "true", "1", or "yes", this is a finding.

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-258847`

### Rule: The Photon operating system must require users to reauthenticate for privilege escalation.

**Rule ID:** `SV-258847r933602_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the user reauthenticate. Satisfies: SRG-OS-000373-GPOS-00156, SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00158</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following commands to verify users with a set password are not allowed to sudo without reauthentication: # grep -ihs nopasswd /etc/sudoers /etc/sudoers.d/*|grep -vE '(^#|^%)' # awk -F: '($2 != "x" && $2 != "!") {print $1}' /etc/shadow If any account listed in the first output is also listed in the second output and is not documented, this is a finding.

## Group: SRG-OS-000433-GPOS-00193

**Group ID:** `V-258848`

### Rule: The Photon operating system must implement address space layout randomization to protect its memory from unauthorized code execution.

**Rule ID:** `SV-258848r933605_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in nonexecutable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can either be hardware-enforced or software-enforced with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify address space layout randomization is enabled: # cat /proc/sys/kernel/randomize_va_space If the value of "randomize_va_space" is not "2", this is a finding.

## Group: SRG-OS-000437-GPOS-00194

**Group ID:** `V-258849`

### Rule: The Photon operating system must remove all software components after updated versions have been installed.

**Rule ID:** `SV-258849r933608_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Previous versions of software components that are not removed from the information system after updates have been installed may be exploited by adversaries. Some information technology products may remove older versions of software automatically from the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep -i '^clean_requirements_on_remove' /etc/tdnf/tdnf.conf Example result: clean_requirements_on_remove=1 If "clean_requirements_on_remove" is not set to "true", "1", or "yes", this is a finding.

## Group: SRG-OS-000470-GPOS-00214

**Group ID:** `V-258850`

### Rule: The Photon operating system must generate audit records when successful/unsuccessful logon attempts occur.

**Rule ID:** `SV-258850r933611_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify an audit rule exists to audit logon attempts: # auditctl -l | grep -E "faillog|lastlog|tallylog" Expected result: -w /var/log/faillog -p wa -k logons -w /var/log/lastlog -p wa -k logons -w /var/log/tallylog -p wa -k logons If the output does not match the expected result, this is a finding. Note: This check depends on the "auditd" service to be in a running state for accurate results. The "auditd" service is enabled in control PHTN-40-000016.

## Group: SRG-OS-000471-GPOS-00216

**Group ID:** `V-258851`

### Rule: The Photon operating system must be configured to audit the loading and unloading of dynamic kernel modules.

**Rule ID:** `SV-258851r933614_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000471-GPOS-00216, SRG-OS-000477-GPOS-00222</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify an audit rule exists to audit kernel modules: # auditctl -l | grep init_module Expected result: -a always,exit -F arch=b32 -S init_module -F key=modules -a always,exit -F arch=b64 -S init_module -F key=modules If the output does not match the expected result, this is a finding. Note: This check depends on the "auditd" service to be in a running state for accurate results. The "auditd" service is enabled in control PHTN-40-000016.

## Group: SRG-OS-000478-GPOS-00223

**Group ID:** `V-258852`

### Rule: The Photon operating system must implement NIST FIPS-validated cryptography for the following: to provision digital signatures, to generate cryptographic hashes, and to protect unclassified information requiring confidentiality and cryptographic protection in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.

**Rule ID:** `SV-258852r933617_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The operating system must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. Satisfies: SRG-OS-000478-GPOS-00223, SRG-OS-000396-GPOS-00176</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify FIPS is enabled for the OS: # cat /proc/sys/crypto/fips_enabled Example result: 1 If "fips_enabled" is not set to "1", this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-258853`

### Rule: The Photon operating system must prevent the use of dictionary words for passwords.

**Rule ID:** `SV-258853r933620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system allows the user to select passwords based on dictionary words, then this increases the chances of password compromise by increasing the opportunity for successful guesses and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify passwords do not match dictionary words: # grep '^password.*pam_pwquality.so' /etc/pam.d/system-password Example result: password requisite pam_pwquality.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=15 difok=8 enforce_for_root dictcheck=1 If the "dictcheck" option is not set to 1, is missing or commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-258854`

### Rule: The Photon operating system must enforce a delay of at least four seconds between logon prompts following a failed logon attempt in login.defs.

**Rule ID:** `SV-258854r933623_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of logon attempts over a certain time interval reduces the chances that an unauthorized user may gain access to an account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify a four second delay is configured between logon attempts: # grep '^FAIL_DELAY' /etc/login.defs Example result: FAIL_DELAY 4 If the "FAIL_DELAY" option is not set to 4 or more, is missing or commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258855`

### Rule: The Photon operating system must ensure audit events are flushed to disk at proper intervals.

**Rule ID:** `SV-258855r933626_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. To that end, the auditd service must be configured to start automatically and be running at all times.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify auditd is configured to flush audit events to disk regularly: # grep -E "freq|flush" /etc/audit/auditd.conf Example result: flush = INCREMENTAL_ASYNC freq = 50 If "flush" is not set to "INCREMENTAL_ASYNC", this is a finding. If "freq" is not set to "50", this is a finding.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-258856`

### Rule: The Photon operating system must define default permissions for all authenticated users in such a way that the user can only read and modify their own files.

**Rule ID:** `SV-258856r933629_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the most restrictive default permissions ensures that when new accounts are created they do not have unnecessary access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the default umask configuration: # grep '^UMASK' /etc/login.defs Expected result: UMASK 077 If the "UMASK" option is not set to "077", is missing or commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-258857`

### Rule: The Photon operating system must configure Secure Shell (SSH) to disallow HostbasedAuthentication.

**Rule ID:** `SV-258857r933632_rule`
**Severity:** high

**Description:**
<VulnDiscussion>SSH trust relationships enable trivial lateral spread after a host compromise and therefore must be explicitly disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the running configuration of sshd: # sshd -T|&grep -i HostbasedAuthentication Example result: hostbasedauthentication no If "HostbasedAuthentication" is not set to "no", this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-258858`

### Rule: The Photon operating system must be configured to use the pam_faillock.so module.

**Rule ID:** `SV-258858r933635_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. This module maintains a list of failed authentication attempts per user during a specified interval and locks the account in case there were more than deny consecutive failed authentications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following commands to verify the pam_faillock.so module is used: # grep '^auth' /etc/pam.d/system-auth Example result: auth required pam_faillock.so preauth auth required pam_unix.so auth required pam_faillock.so authfail If the pam_faillock.so module is not present with the "preauth" line listed before pam_unix.so, this is a finding. If the pam_faillock.so module is not present with the "authfail" line listed after pam_unix.so, this is a finding. # grep '^account' /etc/pam.d/system-account Example result: account required pam_faillock.so account required pam_unix.so If the pam_faillock.so module is not present and listed before pam_unix.so, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-258859`

### Rule: The Photon operating system must prevent leaking information of the existence of a user account.

**Rule ID:** `SV-258859r933638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. If the pam_faillock.so module is not configured to use the silent flag it could leak information about the existence or nonexistence of a user account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify account information is not leaked during the login process: # grep '^silent' /etc/security/faillock.conf Example result: silent If the "silent" option is not set, is missing or commented out, this is a finding. Note: If faillock.conf is not used to configure pam_faillock.so then these options may be specified on the faillock lines in the system-auth and system-account files.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-258860`

### Rule: The Photon operating system must audit logon attempts for unknown users.

**Rule ID:** `SV-258860r933641_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify that audit logon attempts for unknown users is performed: # grep '^audit' /etc/security/faillock.conf Example result: audit If the "audit" option is not set, is missing or commented out, this is a finding. Note: If faillock.conf is not used to configure pam_faillock.so then these options may be specified on the faillock lines in the system-auth and system-account files.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-258861`

### Rule: The Photon operating system must include root when automatically locking an account until the locked account is released by an administrator when three unsuccessful logon attempts occur during a 15-minute time period.

**Rule ID:** `SV-258861r933644_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. Unless specified the root account is not included in the default faillock module options and should be included.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify accounts are locked after three consecutive invalid logon attempts by a user during a 15-minute time period includes the root account: # grep '^even_deny_root' /etc/security/faillock.conf Example result: even_deny_root If the "even_deny_root" option is not set, is missing or commented out, this is a finding. Note: If faillock.conf is not used to configure pam_faillock.so then these options may be specified on the faillock lines in the system-auth and system-account files.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-258862`

### Rule: The Photon operating system must persist lockouts between system reboots.

**Rule ID:** `SV-258862r933647_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. By default, account lockout information is stored under /var/run/faillock and is not persistent between reboots.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify account locking persists lockouts between system reboots: # grep '^dir' /etc/security/faillock.conf Example result: dir = /var/log/faillock If the "dir" option is set to "/var/run/faillock", this is a finding. If the "dir" option is not set to a persistent documented faillock directory, is missing or commented out, this is a finding. Note: If faillock.conf is not used to configure pam_faillock.so then these options may be specified on the faillock lines in the system-auth and system-account files.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-258863`

### Rule: The Photon operating system must be configured to use the pam_pwquality.so module.

**Rule ID:** `SV-258863r933650_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the pam_pwquality.so module is used: # grep '^password' /etc/pam.d/system-password Example result: password requisite pam_pwquality.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=15 difok=8 enforce_for_root dictcheck=1 password required pam_pwhistory.so remember=5 retry=3 enforce_for_root use_authtok password required pam_unix.so sha512 use_authtok shadow try_first_pass If the pam_pwquality.so module is not present, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-258864`

### Rule: The Photon operating system TDNF package management tool must cryptographically verify the authenticity of all software packages during installation for all repos.

**Rule ID:** `SV-258864r933653_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Installation of any nontrusted software, patches, service packs, device drivers, or operating system components can significantly affect the overall security of the operating system. This requirement ensures the software has not been tampered with and has been provided by a trusted vendor.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify software packages are cryptographically verified during installation: # grep gpgcheck /etc/yum.repos.d/* If "gpgcheck" is not set to "1" in any returned file, this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-258865`

### Rule: The Photon operating system must configure the Secure Shell (SSH) SyslogFacility.

**Rule ID:** `SV-258865r933656_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automated monitoring of remote access sessions allows organizations to detect cyberattacks and ensure ongoing compliance with remote access policies by auditing connection activities. Shipping sshd authentication events to syslog allows organizations to use their log aggregators to correlate forensic activities among multiple systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the running configuration of sshd: # sshd -T|&grep -i SyslogFacility Example result: syslogfacility AUTHPRIV If "syslogfacility" is not set to "AUTH" or "AUTHPRIV", this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-258866`

### Rule: The Photon operating system must enable Secure Shell (SSH) authentication logging.

**Rule ID:** `SV-258866r933659_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automated monitoring of remote access sessions allows organizations to detect cyberattacks and ensure ongoing compliance with remote access policies by auditing connection activities. The INFO LogLevel is required, at least, to ensure the capturing of failed login events.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the running configuration of sshd: # sshd -T|&grep -i LogLevel Example result: loglevel INFO If "LogLevel" is not set to "INFO", this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-258867`

### Rule: The Photon operating system must terminate idle Secure Shell (SSH) sessions.

**Rule ID:** `SV-258867r933662_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level, and deallocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that the operating system terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the running configuration of sshd: # sshd -T|&grep -i ClientAliveCountMax Expected result: clientalivecountmax 0 If "ClientAliveCountMax" is not set to "0", this is a finding.

## Group: SRG-OS-000239-GPOS-00089

**Group ID:** `V-258868`

### Rule: The Photon operating system must audit all account modifications.

**Rule ID:** `SV-258868r933665_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to modify an existing account. Auditing account modification actions provides logging that can be used for forensic purposes. To address access requirements, many operating systems can be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000239-GPOS-00089, SRG-OS-000303-GPOS-00120, SRG-OS-000467-GPOS-00211</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify an audit rule exists to audit account modifications: # auditctl -l | grep -E "(/etc/passwd|/etc/shadow|/etc/group|/etc/gshadow)" Expected result: -w /etc/passwd -p wa -k passwd -w /etc/shadow -p wa -k shadow -w /etc/group -p wa -k group -w /etc/gshadow -p wa -k gshadow If the output does not match the expected result, this is a finding. Note: This check depends on the "auditd" service to be in a running state for accurate results. The "auditd" service is enabled in control PHTN-40-000016.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-258869`

### Rule: The Photon operating system must enforce a delay of at least four seconds between logon prompts following a failed logon attempt.

**Rule ID:** `SV-258869r933668_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of logon attempts over a certain time interval reduces the chances that an unauthorized user may gain access to an account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the pam_faildelay.so module is used: # grep '^auth' /etc/pam.d/system-auth Example result: auth required pam_faillock.so preauth auth required pam_unix.so auth required pam_faillock.so authfail auth optional pam_faildelay.so delay=4000000 If the pam_faildelay.so module is not present with the delay set to at least four seconds, this is a finding. Note: The delay is configured in milliseconds.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-258870`

### Rule: The Photon operating system must configure Secure Shell (SSH) to disallow authentication with an empty password.

**Rule ID:** `SV-258870r933671_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Blank passwords are one of the first things an attacker checks for when probing a system. Even if the user somehow has a blank password on the OS, SSH must not allow that user to log in.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the running configuration of sshd: # sshd -T|&grep -i PermitEmptyPasswords Example result: permitemptypasswords no If "PermitEmptyPasswords" is not set to "no", this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-258871`

### Rule: The Photon operating system must configure Secure Shell (SSH) to disable user environment processing.

**Rule ID:** `SV-258871r933674_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Enabling user environment processing may enable users to bypass access restrictions in some configurations and must therefore be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the running configuration of sshd: # sshd -T|&grep -i PermitUserEnvironment Example result: permituserenvironment no If "PermitUserEnvironment" is not set to "no", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258872`

### Rule: The Photon operating system must create a home directory for all new local interactive user accounts.

**Rule ID:** `SV-258872r933677_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If local interactive users are not assigned a valid home directory, there is no place for the storage and control of files they should own.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify a home directory is created for all new user accounts: # grep '^CREATE_HOME' /etc/login.defs Example result: CREATE_HOME yes If the "CREATE_HOME" option is not set to "yes", is missing or commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258873`

### Rule: The Photon operating system must disable the debug-shell service.

**Rule ID:** `SV-258873r933680_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The debug-shell service is intended to diagnose systemd related boot issues with various systemctl commands. Once enabled and following a system reboot, the root shell will be available on tty9. This service must remain disabled until and unless otherwise directed by VMware support.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the debug-shell service is disabled: # systemctl status debug-shell.service If the debug-shell service is not stopped and disabled, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258874`

### Rule: The Photon operating system must configure Secure Shell (SSH) to disallow Generic Security Service Application Program Interface (GSSAPI) authentication.

**Rule ID:** `SV-258874r933683_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>GSSAPI authentication is used to provide additional authentication mechanisms to applications. Allowing GSSAPI authentication through Secure Shell (SSH) exposes the system's GSSAPI to remote hosts, increasing the attack surface of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the running configuration of sshd: # sshd -T|&grep -i GSSAPIAuthentication Example result: gssapiauthentication no If "GSSAPIAuthentication" is not set to "no", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258875`

### Rule: The Photon operating system must configure Secure Shell (SSH) to disable X11 forwarding.

**Rule ID:** `SV-258875r933686_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>X11 is an older, insecure graphics forwarding protocol. It is not used by Photon and should be disabled as a general best practice to limit attack surface area and communication channels.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the running configuration of sshd: # sshd -T|&grep -i X11Forwarding Example result: x11forwarding no If "X11Forwarding" is not set to "no", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258876`

### Rule: The Photon operating system must configure Secure Shell (SSH) to perform strict mode checking of home directory configuration files.

**Rule ID:** `SV-258876r933689_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If other users have access to modify user-specific SSH configuration files, they may be able to log on to the system as another user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the running configuration of sshd: # sshd -T|&grep -i StrictModes Example result: strictmodes yes If "StrictModes" is not set to "yes", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258877`

### Rule: The Photon operating system must configure Secure Shell (SSH) to disallow Kerberos authentication.

**Rule ID:** `SV-258877r933692_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Kerberos is enabled through SSH, sshd provides a means of access to the system's Kerberos implementation. Vulnerabilities in the system's Kerberos implementation may then be subject to exploitation. To reduce the attack surface of the system, the Kerberos authentication mechanism within SSH must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the running configuration of sshd: # sshd -T|&grep -i KerberosAuthentication Example result: kerberosauthentication no If "KerberosAuthentication" is not set to "no", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258878`

### Rule: The Photon operating system must configure Secure Shell (SSH) to disallow compression of the encrypted session stream.

**Rule ID:** `SV-258878r933695_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If compression is allowed in an SSH connection prior to authentication, vulnerabilities in the compression software could result in compromise of the system from an unauthenticated connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the running configuration of sshd: # sshd -T|&grep -i Compression Example result: compression no If there is no output or if "Compression" is not set to "delayed" or "no", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258879`

### Rule: The Photon operating system must configure Secure Shell (SSH) to display the last login immediately after authentication.

**Rule ID:** `SV-258879r933698_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Providing users with feedback on the last time they logged on via SSH facilitates user recognition and reporting of unauthorized account use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the running configuration of sshd: # sshd -T|&grep -i PrintLastLog Example result: printlastlog yes If "PrintLastLog" is not set to "yes", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258880`

### Rule: The Photon operating system must configure Secure Shell (SSH) to ignore user-specific trusted hosts lists.

**Rule ID:** `SV-258880r933701_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH trust relationships enable trivial lateral spread after a host compromise and therefore must be explicitly disabled. Individual users can have a local list of trusted remote machines, which must also be ignored while disabling host-based authentication generally.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the running configuration of sshd: # sshd -T|&grep -i IgnoreRhosts Example result: ignorerhosts yes If "IgnoreRhosts" is not set to "yes", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258881`

### Rule: The Photon operating system must configure Secure Shell (SSH) to ignore user-specific known_host files.

**Rule ID:** `SV-258881r935567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH trust relationships enable trivial lateral spread after a host compromise and therefore must be explicitly disabled. Individual users can have a local list of trusted remote machines, which must also be ignored while disabling host-based authentication generally.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the running configuration of sshd: # sshd -T|&grep -i IgnoreUserKnownHosts Expected result: ignoreuserknownhosts yes If "IgnoreUserKnownHosts" is not set to "yes", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258882`

### Rule: The Photon operating system must configure Secure Shell (SSH) to limit the number of allowed login attempts per connection.

**Rule ID:** `SV-258882r933707_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By setting the login attempt limit to a low value, an attacker will be forced to reconnect frequently, which severely limits the speed and effectiveness of brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the running configuration of sshd: # sshd -T|&grep -i MaxAuthTries Example result: maxauthtries 6 If "MaxAuthTries" is not set to "6", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258883`

### Rule: The Photon operating system must configure Secure Shell (SSH) to restrict AllowTcpForwarding.

**Rule ID:** `SV-258883r933710_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>While enabling TCP tunnels is a valuable function of sshd, this feature is not appropriate for use on single purpose appliances.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the running configuration of sshd: # sshd -T|&grep -i AllowTcpForwarding Example result: allowtcpforwarding no If "AllowTcpForwarding" is not set to "no", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258884`

### Rule: The Photon operating system must configure Secure Shell (SSH) to restrict LoginGraceTime.

**Rule ID:** `SV-258884r933713_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, SSH unauthenticated connections are left open for two minutes before being closed. This setting is too permissive as no legitimate login would need such an amount of time to complete a login. Quickly terminating idle or incomplete login attempts will free up resources and reduce the exposure any partial logon attempts may create.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the running configuration of sshd: # sshd -T|&grep -i LoginGraceTime Example result: logingracetime 30 If "LoginGraceTime" is not set to "30", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258885`

### Rule: The Photon operating system must be configured so that the x86 Ctrl-Alt-Delete key sequence is disabled on the command line.

**Rule ID:** `SV-258885r933716_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When the Ctrl-Alt-Del target is enabled, a locally logged-on user who presses Ctrl-Alt-Delete, when at the console, can reboot the system. If accidentally pressed, as could happen in the case of a mixed OS environment, this can create the risk of short-term loss of systems availability due to unintentional reboot.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the ctrl-alt-del target is disabled and masked: # systemctl status ctrl-alt-del.target --no-pager Example output: ctrl-alt-del.target Loaded: masked (Reason: Unit ctrl-alt-del.target is masked.) Active: inactive (dead) If the "ctrl-alt-del.target" is not "inactive" and "masked", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258886`

### Rule: The Photon operating system must not forward IPv4 or IPv6 source-routed packets.

**Rule ID:** `SV-258886r933719_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source routing is an Internet Protocol mechanism that allows an IP packet to carry information, a list of addresses, that tells a router the path the packet must take. There is also an option to record the hops as the route is traversed. The list of hops taken, the "route record", provides the destination with a return path to the source. This allows the source (the sending host) to specify the route, loosely or strictly, ignoring the routing tables of some or all of the routers. It can allow a user to redirect network traffic for malicious purposes and should therefore be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify source-routed packets are not forwarded: # /sbin/sysctl -a --pattern "net.ipv[4|6].conf.(all|default).accept_source_route" Expected result: net.ipv4.conf.all.accept_source_route = 0 net.ipv4.conf.default.accept_source_route = 0 net.ipv6.conf.all.accept_source_route = 0 net.ipv6.conf.default.accept_source_route = 0 If the "accept_source_route" kernel parameters are not set to "0", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258887`

### Rule: The Photon operating system must not respond to IPv4 Internet Control Message Protocol (ICMP) echoes sent to a broadcast address.

**Rule ID:** `SV-258887r933722_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Responding to broadcast (ICMP) echoes facilitates network mapping and provides a vector for amplification attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify ICMP echoes sent to a broadcast address are ignored: # /sbin/sysctl net.ipv4.icmp_echo_ignore_broadcasts Example result: net.ipv4.icmp_echo_ignore_broadcasts = 1 If the "net.ipv4.icmp_echo_ignore_broadcasts" kernel parameter is not set to "1", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258888`

### Rule: The Photon operating system must prevent IPv4 Internet Control Message Protocol (ICMP) redirect messages from being accepted.

**Rule ID:** `SV-258888r933725_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify ICMP redirects are not accepted: # /sbin/sysctl -a --pattern "net.ipv4.conf.(all|default).accept_redirects" Expected result: net.ipv4.conf.all.accept_redirects = 0 net.ipv4.conf.default.accept_redirects = 0 If the "accept_redirects" kernel parameters are not set to "0", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258889`

### Rule: The Photon operating system must prevent IPv4 Internet Control Message Protocol (ICMP) secure redirect messages from being accepted.

**Rule ID:** `SV-258889r933728_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify ICMP secure redirects are not accepted: # /sbin/sysctl -a --pattern "net.ipv4.conf.(all|default).secure_redirects" Expected result: net.ipv4.conf.all.secure_redirects = 0 net.ipv4.conf.default.secure_redirects = 0 If the "secure_redirects" kernel parameters are not set to "0", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258890`

### Rule: The Photon operating system must not send IPv4 Internet Control Message Protocol (ICMP) redirects.

**Rule ID:** `SV-258890r933731_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages contain information from the system's route table, possibly revealing portions of the network topology.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify ICMP send redirects are not accepted: # /sbin/sysctl -a --pattern "net.ipv4.conf.(all|default).send_redirects" Expected result: net.ipv4.conf.all.send_redirects = 0 net.ipv4.conf.default.send_redirects = 0 If the "send_redirects" kernel parameters are not set to "0", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258891`

### Rule: The Photon operating system must log IPv4 packets with impossible addresses.

**Rule ID:** `SV-258891r933734_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The presence of "martian" packets (which have impossible addresses) as well as spoofed packets, source-routed packets, and redirects could be a sign of nefarious network activity. Logging these packets enables this activity to be detected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify martian packets are logged: # /sbin/sysctl -a --pattern "net.ipv4.conf.(all|default).log_martians" Expected result: net.ipv4.conf.all.log_martians = 1 net.ipv4.conf.default.log_martians = 1 If the "log_martians" kernel parameters are not set to "1", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258892`

### Rule: The Photon operating system must use a reverse-path filter for IPv4 network traffic.

**Rule ID:** `SV-258892r933737_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling reverse path filtering drops packets with source addresses that should not have been able to be received on the interface they were received on. It should not be used on systems that are routers for complicated networks but is helpful for end hosts and routers serving small networks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify IPv4 traffic is using a reverse path filter: # /sbin/sysctl -a --pattern "net.ipv4.conf.(all|default).rp_filter" Expected result: net.ipv4.conf.all.rp_filter = 1 net.ipv4.conf.default.rp_filter = 1 If the "rp_filter" kernel parameters are not set to "1", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258893`

### Rule: The Photon operating system must not perform IPv4 packet forwarding.

**Rule ID:** `SV-258893r933740_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If IP forwarding is required, for example if Kubernetes is installed, this is Not Applicable. At the command line, run the following command to verify packet forwarding it disabled: # /sbin/sysctl net.ipv4.ip_forward Expected result: net.ipv4.ip_forward = 0 If the "net.ipv4.ip_forward" kernel parameter is not set to "0", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258894`

### Rule: The Photon operating system must send TCP timestamps.

**Rule ID:** `SV-258894r933743_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>TCP timestamps are used to provide protection against wrapped sequence numbers. It is possible to calculate system uptime (and boot time) by analyzing TCP timestamps. These calculated uptimes can help a bad actor in determining likely patch levels for vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify TCP timestamps are enabled: # /sbin/sysctl net.ipv4.tcp_timestamps Expected result: net.ipv4.tcp_timestamps = 1 If the "net.ipv4.tcp_timestamps" kernel parameter is not set to "1", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258895`

### Rule: The Photon operating system must be configured to protect the Secure Shell (SSH) public host key from unauthorized modification.

**Rule ID:** `SV-258895r933746_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a public host key file is modified by an unauthorized user, the SSH service may be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # stat -c "%n permissions are %a and owned by %U:%G" /etc/ssh/*key.pub Example result: /etc/ssh/ssh_host_dsa_key.pub permissions are 644 and owned by root:root /etc/ssh/ssh_host_ecdsa_key.pub permissions are 644 and owned by root:root /etc/ssh/ssh_host_ed25519_key.pub permissions are 644 and owned by root:root /etc/ssh/ssh_host_rsa_key.pub permissions are 644 and owned by root:root If any "key.pub" file listed is not owned by root or not group owned by root or does not have permissions of "0644", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258896`

### Rule: The Photon operating system must be configured to protect the Secure Shell (SSH) private host key from unauthorized access.

**Rule ID:** `SV-258896r933749_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an unauthorized user obtains the private SSH host key file, the host could be impersonated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # stat -c "%n permissions are %a and owned by %U:%G" /etc/ssh/*key Example result: /etc/ssh/ssh_host_dsa_key permissions are 600 and owned by root:root /etc/ssh/ssh_host_ecdsa_key permissions are 600 and owned by root:root /etc/ssh/ssh_host_ed25519_key permissions are 600 and owned by root:root /etc/ssh/ssh_host_rsa_key permissions are 600 and owned by root:root If any key file listed is not owned by root or not group owned by root or does not have permissions of "0600", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258897`

### Rule: The Photon operating system must enforce password complexity on the root account.

**Rule ID:** `SV-258897r933752_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity rules must apply to all accounts on the system, including root. Without specifying the enforce_for_root flag, pam_pwquality does not apply complexity rules to the root user. While root users can find ways around this requirement, given its superuser power, it is necessary to attempt to force compliance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify password complexity is enforced for the root account: # grep '^password.*pam_pwquality.so' /etc/pam.d/system-password Example result: password requisite pam_pwquality.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=15 difok=8 enforce_for_root dictcheck=1 If the "enforce_for_root" option is missing or commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258898`

### Rule: The Photon operating system must disable systemd fallback DNS.

**Rule ID:** `SV-258898r935569_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Systemd contains an ability to set fallback DNS servers, which is used for DNS lookups in the event no system level DNS servers are configured or other DNS servers are specified in the Systemd resolved.conf file. If uncommented, this configuration contains Google DNS servers by default and could result in DNS leaking info unknowingly in the event DNS is absent or misconfigured at the system level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify systemd fallback DNS is disabled: # resolvectl status | grep '^Fallback DNS' If the output indicates that Fallback DNS servers are configured, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258899`

### Rule: The Photon operating system must generate audit records for all access and modifications to the opasswd file.

**Rule ID:** `SV-258899r933758_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify an audit rule exists to audit the opasswd file: # auditctl -l | grep -E /etc/security/opasswd Expected result: -w /etc/security/opasswd -p wa -k opasswd If the opasswd file is not monitored for access or writes, this is a finding. Note: This check depends on the "auditd" service to be in a running state for accurate results. The "auditd" service is enabled in control PHTN-40-000016.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-258900`

### Rule: The Photon operating system must implement only approved Message Authentication Codes (MACs) to protect the integrity of remote access sessions.

**Rule ID:** `SV-258900r933761_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the running configuration of sshd: # sshd -T|&grep -i MACs Example result: macs hmac-sha2-512,hmac-sha2-256 If the output matches the macs in the example result or a subset thereof, this is not a finding. If the output contains any macs not listed in the example result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258901`

### Rule: The Photon operating system must enable the rsyslog service.

**Rule ID:** `SV-258901r933764_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If another package is used to offload logs, such as syslog-ng, and is properly configured, this is not applicable. At the command line, run the following command to verify rsyslog is enabled and running: # systemctl status rsyslog If the rsyslog service is not enabled and running, this is a finding.

## Group: SRG-OS-000077-GPOS-00045

**Group ID:** `V-258902`

### Rule: The Photon operating system must be configured to use the pam_pwhistory.so module.

**Rule ID:** `SV-258902r933767_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify the pam_pwhistory.so module is used: # grep '^password' /etc/pam.d/system-password Example result: password requisite pam_pwquality.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=15 difok=8 enforce_for_root dictcheck=1 password required pam_pwhistory.so remember=5 retry=3 enforce_for_root use_authtok password required pam_unix.so sha512 use_authtok shadow try_first_pass If the "pam_pwhistory.so" module is not present, this is a finding. If "use_authtok" is not present for the "pam_pwhistory.so" module, this is a finding. If "conf" or "file" are present for the "pam_pwhistory.so" module, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258903`

### Rule: The Photon operating system must enable hardlink access control protection in the kernel.

**Rule ID:** `SV-258903r933770_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By enabling the fs.protected_hardlinks kernel parameter, users can no longer create soft or hard links to files they do not own. Disallowing such hardlinks mitigate vulnerabilities based on insecure file system accessed by privileged programs, avoiding an exploitation vector exploiting unsafe use of open() or creat().</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify hardlink protection is enabled: # /sbin/sysctl fs.protected_hardlinks Example result: fs.protected_hardlinks = 1 If the "fs.protected_hardlinks" kernel parameter is not set to "1", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-258904`

### Rule: The Photon operating system must restrict core dumps.

**Rule ID:** `SV-258904r933773_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By enabling the fs.suid_dumpable kernel parameter, core dumps are not generated for setuid or otherwise protected/tainted binaries. This prevents users from potentially accessing core dumps with privileged information they would otherwise not have access to read.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to verify core dumps are restricted: # /sbin/sysctl fs.suid_dumpable Example result: fs.suid_dumpable = 0 If the "fs.suid_dumpable" kernel parameter is not set to "0", this is a finding.

