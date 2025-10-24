# STIG Benchmark: VMware vSphere 7.0 vCenter Appliance Photon OS Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-256478`

### Rule: The Photon operating system must audit all account creations.

**Rule ID:** `SV-256478r958368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create an account. Auditing account creation actions provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # auditctl -l | grep -E "(useradd|groupadd)" Expected result: -w /usr/sbin/useradd -p x -k useradd -w /usr/sbin/groupadd -p x -k groupadd If either "useradd" or "groupadd" are not listed with a permissions filter of at least "x", this is a finding. Note: This check depends on the "auditd" service to be in a running state for accurate results. The "auditd" service is enabled in control PHTN-30-000013.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-256479`

### Rule: The Photon operating system must automatically lock an account when three unsuccessful logon attempts occur.

**Rule ID:** `SV-256479r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following commands: # grep pam_tally2 /etc/pam.d/system-auth Expected result: auth required pam_tally2.so deny=3 onerr=fail audit even_deny_root unlock_time=900 root_unlock_time=300 # grep pam_tally2 /etc/pam.d/system-account Expected result: account required pam_tally2.so onerr=fail audit If the output does not list the "pam_tally2" options as configured in the expected results, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-256480`

### Rule: The Photon operating system must display the Standard Mandatory DOD Notice and Consent Banner before granting Secure Shell (SSH) access.

**Rule ID:** `SV-256480r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # sshd -T|&grep -i Banner Expected result: banner /etc/issue If the output does not match the expected result, this is a finding. Open "/etc/issue" with a text editor. If the file does not contain the Standard Mandatory DOD Notice and Consent Banner, this is a finding. Standard Mandatory DOD Notice and Consent Banner: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details."

## Group: SRG-OS-000027-GPOS-00008

**Group ID:** `V-256481`

### Rule: The Photon operating system must limit the number of concurrent sessions to 10 for all accounts and/or account types.

**Rule ID:** `SV-256481r958398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Operating system management includes the ability to control the number of users and user sessions that utilize an operating system. Limiting the number of allowed users and sessions per user is helpful in reducing the risks related to denial-of-service attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep "^[^#].*maxlogins.*" /etc/security/limits.conf Expected result: * hard maxlogins 10 If the output does not match the expected result, this is a finding. Note: The expected result may be repeated multiple times.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-256482`

### Rule: The Photon operating system must set a session inactivity timeout of 15 minutes or less.

**Rule ID:** `SV-256482r958402_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session timeout is an action taken when a session goes idle for any reason. Rather than relying on the user to manually disconnect their session prior to going idle, the Photon operating system must be able to identify when a session has idled and take action to terminate the session. Satisfies: SRG-OS-000029-GPOS-00010, SRG-OS-000279-GPOS-00109, SRG-OS-000126-GPOS-00066</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # cat /etc/profile.d/tmout.sh Expected result: TMOUT=900 readonly TMOUT export TMOUT mesg n 2>/dev/null If the file "tmout.sh" does not exist or the output does not look like the expected result, this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-256483`

### Rule: The Photon operating system must have the sshd SyslogFacility set to "authpriv".

**Rule ID:** `SV-256483r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automated monitoring of remote access sessions allows organizations to detect cyberattacks and ensure ongoing compliance with remote access policies by auditing connection activities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # sshd -T|&grep -i SyslogFacility Expected result: syslogfacility AUTHPRIV If there is no output or if the output does not match the expected result, this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-256484`

### Rule: The Photon operating system must have sshd authentication logging enabled.

**Rule ID:** `SV-256484r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automated monitoring of remote access sessions allows organizations to detect cyberattacks and ensure ongoing compliance with remote access policies by auditing connection activities. Shipping sshd authentication events to syslog allows organizations to use their log aggregators to correlate forensic activities among multiple systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep "^authpriv" /etc/rsyslog.conf Expected result should be similar to the following: authpriv.* /var/log/auth.log If "authpriv" is not configured to be logged, this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-256485`

### Rule: The Photon operating system must have the sshd LogLevel set to "INFO".

**Rule ID:** `SV-256485r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automated monitoring of remote access sessions allows organizations to detect cyberattacks and ensure ongoing compliance with remote access policies by auditing connection activities. The INFO LogLevel is required, at least, to ensure the capturing of failed login events.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # sshd -T|&grep -i LogLevel Expected result: LogLevel INFO If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-256486`

### Rule: The Photon operating system must configure sshd to use approved encryption algorithms.

**Rule ID:** `SV-256486r958408_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. OpenSSH on the Photon operating system is compiled with a FIPS-validated cryptographic module. The "FipsMode" setting controls whether this module is initialized and used in FIPS 140-2 mode. Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000393-GPOS-00173, SRG-OS-000396-GPOS-00176, SRG-OS-000250-GPOS-00093, SRG-OS-000423-GPOS-00187</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # sshd -T|&grep -i FipsMode Expected result: FipsMode yes If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-256487`

### Rule: The Photon operating system must configure auditd to log to disk.

**Rule ID:** `SV-256487r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content must be shipped to a central location, but it must also be logged locally. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep "^write_logs" /etc/audit/auditd.conf Expected result: write_logs = yes If there is no output, this is not a finding. If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000038-GPOS-00016

**Group ID:** `V-256488`

### Rule: The Photon operating system must configure auditd to use the correct log format.

**Rule ID:** `SV-256488r958414_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know exact, unfiltered details of the event in question.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep "^log_format" /etc/audit/auditd.conf Expected result: log_format = RAW If there is no output, this is not a finding. If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-256489`

### Rule: The Photon operating system must be configured to audit the execution of privileged functions.

**Rule ID:** `SV-256489r958422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing all actions by superusers is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # auditctl -l | grep execve Expected result: -a always,exit -F arch=b32 -S execve -C uid!=euid -F euid=0 -F key=execpriv -a always,exit -F arch=b64 -S execve -C uid!=euid -F euid=0 -F key=execpriv -a always,exit -F arch=b32 -S execve -C gid!=egid -F egid=0 -F key=execpriv -a always,exit -F arch=b64 -S execve -C gid!=egid -F egid=0 -F key=execpriv If the output does not match the expected result, this is a finding. Note: This check depends on the auditd service to be in a running state for accurate results. Enabling the auditd service is done in control PHTN-30-000013.

## Group: SRG-OS-000042-GPOS-00021

**Group ID:** `V-256490`

### Rule: The Photon operating system must have the auditd service running.

**Rule ID:** `SV-256490r958422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Event outcomes can include indicators of event success or failure and event-specific results (e.g., the security state of the information system after the event occurred). They also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response. Satisfies: SRG-OS-000042-GPOS-00021, SRG-OS-000062-GPOS-00031, SRG-OS-000255-GPOS-00096, SRG-OS-000363-GPOS-00150, SRG-OS-000365-GPOS-00152, SRG-OS-000445-GPOS-00199, SRG-OS-000446-GPOS-00200, SRG-OS-000461-GPOS-00205, SRG-OS-000467-GPOS-00211, SRG-OS-000465-GPOS-00209, SRG-OS-000474-GPOS-00219, SRG-OS-000475-GPOS-00220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # systemctl status auditd If the service is not running, this is a finding.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-256491`

### Rule: The Photon operating system audit log must log space limit problems to syslog.

**Rule ID:** `SV-256491r958424_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Satisfies: SRG-OS-000046-GPOS-00022, SRG-OS-000344-GPOS-00135</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep "^space_left_action" /etc/audit/auditd.conf Expected result: space_left_action = SYSLOG If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-256492`

### Rule: The Photon operating system audit log must attempt to log audit failures to syslog.

**Rule ID:** `SV-256492r1038966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep -E "^disk_full_action|^disk_error_action|^admin_space_left_action" /etc/audit/auditd.conf If any of the above parameters are not set to "SYSLOG" or are missing, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-256493`

### Rule: The Photon operating system audit log must have correct permissions.

**Rule ID:** `SV-256493r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # (audit_log_file=$(grep "^log_file" /etc/audit/auditd.conf|sed s/^[^\/]*//) && if [ -f "${audit_log_file}" ] ; then printf "Log(s) found in "${audit_log_file%/*}":\n"; stat -c "%n permissions are %a" ${audit_log_file%}*; else printf "audit log file(s) not found\n"; fi) If the permissions on any audit log file are more permissive than "0600", this is a finding.

## Group: SRG-OS-000058-GPOS-00028

**Group ID:** `V-256494`

### Rule: The Photon operating system audit log must be owned by root.

**Rule ID:** `SV-256494r958436_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # (audit_log_file=$(grep "^log_file" /etc/audit/auditd.conf|sed s/^[^\/]*//) && if [ -f "${audit_log_file}" ] ; then printf "Log(s) found in "${audit_log_file%/*}":\n"; stat -c "%n is owned by %U" ${audit_log_file%}*; else printf "audit log file(s) not found\n"; fi) If any audit log file is not owned by root, this is a finding.

## Group: SRG-OS-000059-GPOS-00029

**Group ID:** `V-256495`

### Rule: The Photon operating system audit log must be group-owned by root.

**Rule ID:** `SV-256495r958438_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # (audit_log_file=$(grep "^log_file" /etc/audit/auditd.conf|sed s/^[^\/]*//) && if [ -f "${audit_log_file}" ] ; then printf "Log(s) found in "${audit_log_file%/*}":\n"; stat -c "%n is group owned by %G" ${audit_log_file%}*; else printf "audit log file(s) not found\n"; fi) If any audit log file is not group owned by root, this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-256496`

### Rule: The Photon operating system must allow only the information system security manager (ISSM) (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited.

**Rule ID:** `SV-256496r958444_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict the roles and individuals that can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # find /etc/audit/* -type f -exec stat -c "%n permissions are %a" {} $1\; If the permissions of any files are more permissive than "640", this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-256497`

### Rule: The Photon operating system must generate audit records when successful/unsuccessful attempts to access privileges occur.

**Rule ID:** `SV-256497r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000466-GPOS-00210, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # auditctl -l | grep chmod Expected result: -a always,exit -F arch=b64 -S chmod,fchmod,chown,fchown,fchownat,fchmodat -F auid>=1000 -F auid!=4294967295 -F key=perm_mod -a always,exit -F arch=b64 -S chmod,fchmod,chown,fchown,lchown,setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr,fchownat,fchmodat -F key=perm_mod -a always,exit -F arch=b32 -S chmod,fchmod,fchown,chown,fchownat,fchmodat -F auid>=1000 -F auid!=4294967295 -F key=perm_mod -a always,exit -F arch=b32 -S chmod,lchown,fchmod,fchown,chown,setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr,fchownat,fchmodat -F key=perm_mod If the output does not match the expected result, this is a finding. Note: The auid!= parameter may display as 4294967295 or -1, which are equivalent. Note: This check depends on the auditd service to be in a running state for accurate results. The auditd service is enabled in control PHTN-30-000013.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-256498`

### Rule: The Photon operating system must enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-256498r982195_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep pam_cracklib /etc/pam.d/system-password|grep --color=always "ucredit=.." Expected result: password requisite pam_cracklib.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=8 minclass=4 difok=4 retry=3 maxsequence=0 enforce_for_root If the output does not include ucredit= <= -1, this is a finding.

## Group: SRG-OS-000070-GPOS-00038

**Group ID:** `V-256499`

### Rule: The Photon operating system must enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-256499r982196_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep pam_cracklib /etc/pam.d/system-password|grep --color=always "lcredit=.." Expected result: password requisite pam_cracklib.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=8 minclass=4 difok=4 retry=3 maxsequence=0 enforce_for_root If the output does not include lcredit= <= -1, this is a finding.

## Group: SRG-OS-000071-GPOS-00039

**Group ID:** `V-256500`

### Rule: The Photon operating system must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-256500r982197_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep pam_cracklib /etc/pam.d/system-password|grep --color=always "dcredit=.." Expected result: password requisite pam_cracklib.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=8 minclass=4 difok=4 retry=3 maxsequence=0 enforce_for_root If the output does not include dcredit= <= -1, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-256501`

### Rule: The Photon operating system must require that new passwords are at least four characters different from the old password.

**Rule ID:** `SV-256501r982198_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep pam_cracklib /etc/pam.d/system-password|grep --color=always "difok=." Expected result: password requisite pam_cracklib.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=8 minclass=4 difok=4 retry=3 maxsequence=0 enforce_for_root If the output does not include difok >= 4, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-256502`

### Rule: The Photon operating system must store only encrypted representations of passwords.

**Rule ID:** `SV-256502r982199_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep SHA512 /etc/login.defs|grep -v "#" Expected result: ENCRYPT_METHOD SHA512 If there is no output or if the output does match the expected result, this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-256503`

### Rule: The Photon operating system must use an OpenSSH server version that does not support protocol 1.

**Rule ID:** `SV-256503r987796_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the operating system. Authentication sessions between the authenticator and the operating system validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. A privileged account is any information system account with authorizations of a privileged user. Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., TLS, WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators. Satisfies: SRG-OS-000074-GPOS-00042, SRG-OS-000112-GPOS-00057, SRG-OS-000113-GPOS-00058, SRG-OS-000120-GPOS-00061, SRG-OS-000125-GPOS-00065, SRG-OS-000395-GPOS-00175, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # rpm -qa|grep openssh If there is no output or openssh is not >= version 7.4, this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-256504`

### Rule: The Photon operating system must be configured so that passwords for new users are restricted to a 24-hour minimum lifetime.

**Rule ID:** `SV-256504r982188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep "^PASS_MIN_DAYS" /etc/login.defs If "PASS_MIN_DAYS" is not set to "1", this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-256505`

### Rule: The Photon operating system must be configured so that passwords for new users are restricted to a 90-day maximum lifetime.

**Rule ID:** `SV-256505r1038967_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If the operating system does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the operating system passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep "^PASS_MAX_DAYS" /etc/login.defs If the value of "PASS_MAX_DAYS" is greater than "90", this is a finding.

## Group: SRG-OS-000077-GPOS-00045

**Group ID:** `V-256506`

### Rule: The Photon operating system must prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-256506r982201_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the result is a password that is not changed per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep pam_pwhistory /etc/pam.d/system-password|grep --color=always "remember=." Expected result: password requisite pam_pwhistory.so enforce_for_root use_authtok remember=5 retry=3 If the output does not include the "remember=5" setting as shown in the expected result, this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-256507`

### Rule: The Photon operating system must enforce a minimum eight-character password length.

**Rule ID:** `SV-256507r982202_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep pam_cracklib /etc/pam.d/system-password|grep --color=always "minlen=.." Example result: password requisite pam_cracklib.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=8 minclass=4 difok=4 retry=3 maxsequence=0 enforce_for_root If the output does not include minlen >= 8, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-256508`

### Rule: The Photon operating system must require authentication upon booting into single-user and maintenance modes.

**Rule ID:** `SV-256508r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If the system does not require authentication before it boots into single-user mode, anyone with console access to the system can trivially access all files on the system. GRUB2 is the boot loader for Photon OS and can be configured to require a password to boot into single-user mode or make modifications to the boot menu. Note: Photon does not support building grub changes via grub2-mkconfig.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep -i ^password_pbkdf2 /boot/grub2/grub.cfg If there is not output, this is a finding. If the output does not begin with "password_pbkdf2 root", this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-256509`

### Rule: The Photon operating system must disable the loading of unnecessary kernel modules.

**Rule ID:** `SV-256509r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To support the requirements and principles of least functionality, the operating system must provide only essential capabilities and limit the use of modules, protocols, and/or services to only those required for the proper functioning of the product. Satisfies: SRG-OS-000096-GPOS-00050, SRG-OS-000114-GPOS-00059</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # modprobe --showconfig | grep "^install" | grep "/bin" Expected result: install sctp /bin/false install dccp /bin/false install dccp_ipv4 /bin/false install dccp_ipv6 /bin/false install ipx /bin/false install appletalk /bin/false install decnet /bin/false install rds /bin/false install tipc /bin/false install bluetooth /bin/false install usb_storage /bin/false install ieee1394 /bin/false install cramfs /bin/false install freevxfs /bin/false install jffs2 /bin/false install hfs /bin/false install hfsplus /bin/false install squashfs /bin/false install udf /bin/false The output may include other statements outside of the expected result. If the output does not include at least every statement in the expected result, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-256510`

### Rule: The Photon operating system must not have duplicate User IDs (UIDs).

**Rule ID:** `SV-256510r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational users must be uniquely identified and authenticated to prevent potential misuse and provide for nonrepudiation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # awk -F ":" 'list[$3]++{print $1, $3}' /etc/passwd If any lines are returned, this is a finding.

## Group: SRG-OS-000118-GPOS-00060

**Group ID:** `V-256511`

### Rule: The Photon operating system must disable new accounts immediately upon password expiration.

**Rule ID:** `SV-256511r982189_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. Disabling inactive accounts ensures accounts that may not have been responsibly removed are not available to attackers who may have compromised their credentials.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep INACTIVE /etc/default/useradd Expected result: INACTIVE=0 If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000142-GPOS-00071

**Group ID:** `V-256512`

### Rule: The Photon operating system must use Transmission Control Protocol (TCP) syncookies.

**Rule ID:** `SV-256512r958528_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A TCP SYN flood attack can cause a denial of service by filling a system's TCP connection table with connections in the SYN_RCVD state. Syncookies can be used to track a connection when a subsequent ACK is received, verifying the initiator is attempting a valid connection and is not a flood source. This feature is activated when a flood condition is detected and enables the system to continue servicing valid connection requests. Satisfies: SRG-OS-000142-GPOS-00071, SRG-OS-000420-GPOS-00186</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # /sbin/sysctl -a --pattern tcp_syncookies Expected result: net.ipv4.tcp_syncookies = 1 If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-256513`

### Rule: The Photon operating system must configure sshd to disconnect idle Secure Shell (SSH) sessions.

**Rule ID:** `SV-256513r970703_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on a console or console port that has been left unattended.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # sshd -T|&grep -i ClientAliveInterval Expected result: ClientAliveInterval 900 If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-256514`

### Rule: The Photon operating system must configure sshd to disconnect idle Secure Shell (SSH) sessions.

**Rule ID:** `SV-256514r970703_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on a console or console port that has been left unattended.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # sshd -T|&grep -i ClientAliveCountMax Expected result: ClientAliveCountMax 0 If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-256515`

### Rule: The Photon operating system "/var/log" directory must be owned by root.

**Rule ID:** `SV-256515r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state and can provide sensitive information to an unprivileged attacker.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # stat -c "%n is owned by %U and group owned by %G" /var/log If the "/var/log directory" is not owned by root, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-256516`

### Rule: The Photon operating system messages file must have the correct ownership and file permissions.

**Rule ID:** `SV-256516r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state and can provide sensitive information to an unprivileged attacker.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # stat -c "%n is owned by %U and group owned by %G with %a permissions" /var/log/messages If the "/var/log/messages" directory is not owned by root or not group owned by root, or the file permissions are more permission than "640", this is a finding.

## Group: SRG-OS-000239-GPOS-00089

**Group ID:** `V-256517`

### Rule: The Photon operating system must audit all account modifications.

**Rule ID:** `SV-256517r991551_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to modify an existing account. Auditing account modification actions provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # auditctl -l | grep -E "(usermod|groupmod)" Expected result: -w /usr/sbin/usermod -p x -k usermod -w /usr/sbin/groupmod -p x -k groupmod If the output does not match the expected result, this is a finding. Note: This check depends on the auditd service to be in a running state for accurate results. The auditd service is enabled in control PHTN-30-000013.

## Group: SRG-OS-000239-GPOS-00089

**Group ID:** `V-256518`

### Rule: The Photon operating system must audit all account modifications.

**Rule ID:** `SV-256518r991551_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to modify an existing account. Auditing account modification actions provides logging that can be used for forensic purposes. Satisfies: SRG-OS-000239-GPOS-00089, SRG-OS-000303-GPOS-00120</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # auditctl -l | grep -E "(/etc/passwd|/etc/shadow|/etc/group|/etc/gshadow)" Expected result: -w /etc/passwd -p wa -k passwd -w /etc/shadow -p wa -k shadow -w /etc/group -p wa -k group -w /etc/gshadow -p wa -k gshadow If the output does not match the expected result, this is a finding. Note: This check depends on the auditd service to be in a running state for accurate results. The auditd service is enabled in control PHTN-30-000013.

## Group: SRG-OS-000240-GPOS-00090

**Group ID:** `V-256519`

### Rule: The Photon operating system must audit all account disabling actions.

**Rule ID:** `SV-256519r991552_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When operating system accounts are disabled, user accessibility is affected. Accounts are used for identifying individual users or operating system processes. To detect and respond to events affecting user accessibility and system processing, operating systems must audit account disabling actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # auditctl -l | grep "w /usr/bin/passwd" Expected result: -w /usr/bin/passwd -p x -k passwd If the output does not match the expected result, this is a finding. Note: This check depends on the auditd service to be in a running state for accurate results. The auditd service is enabled in control PHTN-30-000013.

## Group: SRG-OS-000241-GPOS-00091

**Group ID:** `V-256520`

### Rule: The Photon operating system must audit all account removal actions.

**Rule ID:** `SV-256520r991553_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When operating system accounts are removed, user accessibility is affected. Accounts are used for identifying individual users or operating system processes. To detect and respond to events affecting user accessibility and system processing, operating systems must audit account removal actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # auditctl -l | grep -E "(userdel|groupdel)" Expected result: -w /usr/sbin/userdel -p x -k userdel -w /usr/sbin/groupdel -p x -k groupdel If the output does not match the expected result, this is a finding. Note: This check depends on the auditd service to be in a running state for accurate results. Enabling the auditd service is done in control PHTN-30-000013.

## Group: SRG-OS-000254-GPOS-00095

**Group ID:** `V-256521`

### Rule: The Photon operating system must initiate auditing as part of the boot process.

**Rule ID:** `SV-256521r991555_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Each process on the system carries an "auditable" flag, which indicates whether its activities can be audited. Although auditd takes care of enabling this for all processes that launch after it starts, adding the kernel argument ensures the flag is set at boot for every process on the system. This includes processes created before auditd starts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep "audit=1" /proc/cmdline If no results are returned, this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-256522`

### Rule: The Photon operating system audit files and directories must have correct permissions.

**Rule ID:** `SV-256522r991557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operations on audit information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # stat -c "%n is owned by %U and group owned by %G" /etc/audit/auditd.conf If "auditd.conf" is not owned by root and group owned by root, this is a finding.

## Group: SRG-OS-000257-GPOS-00098

**Group ID:** `V-256523`

### Rule: The Photon operating system must protect audit tools from unauthorized modification and deletion.

**Rule ID:** `SV-256523r991558_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operations on audit information. Satisfies: SRG-OS-000257-GPOS-00098, SRG-OS-000258-GPOS-00099</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # stat -c "%n is owned by %U and group owned by %G and permissions are %a" /usr/sbin/auditctl /usr/sbin/auditd /usr/sbin/aureport /usr/sbin/ausearch /usr/sbin/autrace If any file is not owned by root or group-owned by root or permissions are more permissive than "750", this is a finding.

## Group: SRG-OS-000266-GPOS-00101

**Group ID:** `V-256524`

### Rule: The Photon operating system must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-256524r991561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep pam_cracklib /etc/pam.d/system-password|grep --color=always "ocredit=.." Expected result: password requisite pam_cracklib.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=8 minclass=4 difok=4 retry=3 maxsequence=0 enforce_for_root If the output does not include ocredit= <= -1, this is a finding.

## Group: SRG-OS-000278-GPOS-00108

**Group ID:** `V-256525`

### Rule: The Photon operating system package files must not be modified.

**Rule ID:** `SV-256525r991567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting the integrity of the tools used for auditing purposes is a critical step toward ensuring the integrity of audit information. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Without confidence in the integrity of the auditing system and tools, the information it provides cannot be trusted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the verification capability of rpm to check the MD5 hashes of the audit files on disk versus the expected ones from the installation package. At the command line, run the following command: # rpm -V audit | grep "^..5" | grep -v "^...........c" If there is any output, this is a finding.

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-256526`

### Rule: The Photon operating system must audit the execution of privileged functions.

**Rule ID:** `SV-256526r958732_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command to obtain a list of setuid files: # find / -xdev -path /var/lib/containerd -prune -o \( -perm -4000 -type f -o -perm -2000 \) -type f -print | sort Run the following command for each setuid file found in the first command: # auditctl -l | grep <setuid_path> Replace <setuid_path> with each path found in the first command. If each <setuid_path> does not have a corresponding line in the audit rules, this is a finding. A typical corresponding line will look like the following: -a always,exit -S all -F path=<setuid_path> -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged Note: The auid!= parameter may display as 4294967295 or -1, which are equivalent. Note: This check depends on the auditd service to be in a running state for accurate results. The auditd service is enabled in control PHTN-30-000013.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-256527`

### Rule: The Photon operating system must configure auditd to keep five rotated log files.

**Rule ID:** `SV-256527r958752_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit logs are most useful when accessible by date, rather than size. This can be accomplished through a combination of an audit log rotation cron job, setting a reasonable number of logs to keep, and configuring auditd to not rotate the logs on its own. This ensures audit logs are accessible to the information system security officer (ISSO) in the event of a central log processing failure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep "^num_logs" /etc/audit/auditd.conf Expected result: num_logs = 5 If the output of the command does not match the expected result, this is a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-256528`

### Rule: The Photon operating system must configure auditd to keep logging in the event max log file size is reached.

**Rule ID:** `SV-256528r958752_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit logs are most useful when accessible by date, rather than size. This can be accomplished through a combination of an audit log rotation cron job, setting a reasonable number of logs to keep, and configuring auditd to not rotate the logs on its own. This ensures audit logs are accessible to the information system security officer (ISSO) in the event of a central log processing failure. If another solution is not used to rotate auditd logs, auditd can be configured to rotate logs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep "^max_log_file_action" /etc/audit/auditd.conf Example result: max_log_file_action = IGNORE If logs are rotated outside of auditd with a tool such as logrotated, and this setting is not set to "IGNORE", this is a finding. If logs are NOT rotated outside of auditd, and this setting is not set to "ROTATE", this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-256529`

### Rule: The Photon operating system must configure auditd to log space limit problems to syslog.

**Rule ID:** `SV-256529r971542_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches 75 percent utilization, they are unable to plan for audit record storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep "^space_left " /etc/audit/auditd.conf Expected result: space_left = 75 If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-256530`

### Rule: The Photon operating system RPM package management tool must cryptographically verify the authenticity of all software packages during installation.

**Rule ID:** `SV-256530r982212_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Installation of any nontrusted software, patches, service packs, device drivers, or operating system components can significantly affect the overall security of the operating system. Ensuring all packages' cryptographic signatures are valid prior to installation ensures the provenance of the software and protects against malicious tampering.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep -s nosignature /usr/lib/rpm/rpmrc /etc/rpmrc ~root/.rpmrc If the command returns any output, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-256531`

### Rule: The Photon operating system RPM package management tool must cryptographically verify the authenticity of all software packages during installation.

**Rule ID:** `SV-256531r982212_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Installation of any nontrusted software, patches, service packs, device drivers, or operating system components can significantly affect the overall security of the operating system. Cryptographically verifying the authenticity of all software packages during installation ensures the software has not been tampered with and has been provided by a trusted vendor.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep "^gpgcheck" /etc/tdnf/tdnf.conf If "gpgcheck" is not set to "1", this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-256532`

### Rule: The  Photon operating system YUM repository must cryptographically verify the authenticity of all software packages during installation.

**Rule ID:** `SV-256532r982212_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Installation of any nontrusted software, patches, service packs, device drivers, or operating system components can significantly affect the overall security of the operating system. Cryptographically verifying the authenticity of all software packages during installation ensures the software has not been tampered with and has been provided by a trusted vendor.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep gpgcheck /etc/yum.repos.d/* If "gpgcheck" is not set to "1" in any returned file, this is a finding.

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-256533`

### Rule: The Photon operating system must require users to reauthenticate for privilege escalation.

**Rule ID:** `SV-256533r1050789_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the user reauthenticate. Satisfies: SRG-OS-000373-GPOS-00156, SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00158</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following commands: # grep -ihs nopasswd /etc/sudoers /etc/sudoers.d/*|grep -v "^#"|grep -v "^%"|awk '{print $1}' # awk -F: '($2 != "x" && $2 != "!") {print $1}' /etc/shadow If any account listed in the first output is also listed in the second output and is not documented, this is a finding.

## Group: SRG-OS-000394-GPOS-00174

**Group ID:** `V-256534`

### Rule: The Photon operating system must configure sshd to use FIPS 140-2 ciphers.

**Rule ID:** `SV-256534r958850_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Privileged access contains control and configuration information and is particularly sensitive, so additional protections are necessary. This is maintained by using cryptographic mechanisms such as encryption to protect confidentiality. Nonlocal maintenance and diagnostic activities are conducted by individuals communicating through an external network (e.g., the internet) or internal network. Local maintenance and diagnostic activities are carried out by individuals physically present at the information system or information system component and not communicating across a network connection. This requirement applies to hardware/software diagnostic test equipment or tools. It does not cover hardware/software components that may support information system maintenance, yet are a part of the system (e.g., the software implementing "ping," "ls," "ipconfig," or the hardware and software implementing the monitoring port of an Ethernet switch). The operating system can meet this requirement by leveraging a cryptographic module. Satisfies: SRG-OS-000394-GPOS-00174, SRG-OS-000424-GPOS-00188</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # sshd -T|&grep -i Ciphers Expected result: ciphers aes128-ctr,aes128-gcm@openssh.com,aes192-ctr,aes256-gcm@openssh.com,aes256-ctr If the output matches the ciphers in the expected result or a subset thereof, this is not a finding. If the ciphers in the output contain any ciphers not listed in the expected result, this is a finding.

## Group: SRG-OS-000433-GPOS-00193

**Group ID:** `V-256535`

### Rule: The Photon operating system must implement address space layout randomization (ASLR) to protect its memory from unauthorized code execution.

**Rule ID:** `SV-256535r958928_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ASLR makes it more difficult for an attacker to predict the location of attack code they have introduced into a process's address space during an attempt at exploitation. ASLR also makes it more difficult for an attacker to know the location of existing code to repurpose it using return-oriented programming (ROP) techniques.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # cat /proc/sys/kernel/randomize_va_space If the value of "randomize_va_space" is not "2", this is a finding.

## Group: SRG-OS-000437-GPOS-00194

**Group ID:** `V-256536`

### Rule: The Photon operating system must remove all software components after updated versions have been installed.

**Rule ID:** `SV-256536r958936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Previous versions of software components that are not removed from the information system after updates have been installed may be exploited by adversaries. Some information technology products may remove older versions of software automatically from the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep -i "^clean_requirements_on_remove" /etc/tdnf/tdnf.conf Expected result: clean_requirements_on_remove=true If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000458-GPOS-00203

**Group ID:** `V-256537`

### Rule: The Photon operating system must generate audit records when the sudo command is used.

**Rule ID:** `SV-256537r991570_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # auditctl -l | grep sudo Expected result: -a always,exit -S all -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged If the output does not match the expected result, this is a finding. Note: The auid!= parameter may display as 4294967295 or -1, which are equivalent. Note: This check depends on the auditd service to be in a running state for accurate results. The auditd service is enabled in control PHTN-30-000013.

## Group: SRG-OS-000470-GPOS-00214

**Group ID:** `V-256538`

### Rule: The Photon operating system must generate audit records when successful/unsuccessful logon attempts occur.

**Rule ID:** `SV-256538r991578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000470-GPOS-00214, SRG-OS-000472-GPOS-00217, SRG-OS-000473-GPOS-00218</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # auditctl -l | grep -E "faillog|lastlog|tallylog" Expected result: -w /var/log/faillog -p wa -w /var/log/lastlog -p wa -w /var/log/tallylog -p wa If the output does not match the expected result, this is a finding. Note: This check depends on the auditd service to be in a running state for accurate results. The auditd service is enabled in control PHTN-30-000013.

## Group: SRG-OS-000471-GPOS-00216

**Group ID:** `V-256539`

### Rule: The Photon operating system must audit the "insmod" module.

**Rule ID:** `SV-256539r991580_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000471-GPOS-00216, SRG-OS-000477-GPOS-00222</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # auditctl -l | grep "/sbin/insmod" Expected result: -w /sbin/insmod -p x If the output does not match the expected result, this is a finding. Note: This check depends on the auditd service to be in a running state for accurate results. The auditd service is enabled in control PHTN-30-000013.

## Group: SRG-OS-000476-GPOS-00221

**Group ID:** `V-256540`

### Rule: The Photon operating system auditd service must generate audit records for all account creations, modifications, disabling, and termination events.

**Rule ID:** `SV-256540r991585_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # auditctl -l | grep -E /etc/security/opasswd If any of these are not listed with a permissions filter of at least "w", this is a finding. Note: This check depends on the auditd service to be in a running state for accurate results. The auditd service is enabled in control PHTN-30-000013.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-256541`

### Rule: The Photon operating system must use the "pam_cracklib" module.

**Rule ID:** `SV-256541r991587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system allows the user to select passwords based on dictionary words, this increases the chances of password compromise by increasing the opportunity for successful guesses and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep pam_cracklib /etc/pam.d/system-password If the output does not return at least "password requisite pam_cracklib.so", this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-256542`

### Rule: The Photon operating system must set the "FAIL_DELAY" parameter.

**Rule ID:** `SV-256542r991588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of logon attempts over a certain time interval reduces the chances that an unauthorized user may gain access to an account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep FAIL_DELAY /etc/login.defs Expected result: FAIL_DELAY 4 If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-256543`

### Rule: The Photon operating system must enforce a delay of at least four seconds between logon prompts following a failed logon attempt.

**Rule ID:** `SV-256543r991588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of logon attempts over a certain time interval reduces the chances that an unauthorized user may gain access to an account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep pam_faildelay /etc/pam.d/system-auth|grep --color=always "delay=" Expected result: auth optional pam_faildelay.so delay=4000000 If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256544`

### Rule: The Photon operating system must ensure audit events are flushed to disk at proper intervals.

**Rule ID:** `SV-256544r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without setting a balance between performance and ensuring all audit events are written to disk, performance of the system may suffer or the risk of missing audit entries may be too high.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep -E "freq|flush" /etc/audit/auditd.conf Expected result: flush = INCREMENTAL_ASYNC freq = 50 If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256545`

### Rule: The Photon operating system must create a home directory for all new local interactive user accounts.

**Rule ID:** `SV-256545r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If local interactive users are not assigned a valid home directory, there is no place for the storage and control of files they should own.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep -i "^create_home" /etc/login.defs If there is no output or the output does not equal "CREATE_HOME yes", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256546`

### Rule: The Photon operating system must disable the debug-shell service.

**Rule ID:** `SV-256546r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The debug-shell service is intended to diagnose systemd-related boot issues with various "systemctl" commands. Once enabled and following a system reboot, the root shell will be available on tty9. This service must remain disabled until and unless otherwise directed by VMware support.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # systemctl status debug-shell.service|grep -E --color=always disabled If the debug-shell service is not disabled, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256547`

### Rule: The Photon operating system must configure sshd to disallow Generic Security Service Application Program Interface (GSSAPI) authentication.

**Rule ID:** `SV-256547r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>GSSAPI authentication is used to provide additional authentication mechanisms to applications. Allowing GSSAPI authentication through Secure Shell (SSH) exposes the system's GSSAPI to remote hosts, increasing the attack surface of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # sshd -T|&grep -i GSSAPIAuthentication Expected result: GSSAPIAuthentication no If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256548`

### Rule: The Photon operating system must configure sshd to disable environment processing.

**Rule ID:** `SV-256548r1051424_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling environment processing may enable users to bypass access restrictions in some configurations and must therefore be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: #sshd -T|&grep -i PermitUserEnvironment Expected result: PermitUserEnvironment no If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256549`

### Rule: The Photon operating system must configure sshd to disable X11 forwarding.

**Rule ID:** `SV-256549r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>X11 is an older, insecure graphics forwarding protocol. It is not used by Photon and should be disabled as a general best practice to limit attack surface area and communication channels.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # sshd -T|&grep -i X11Forwarding Expected result: X11Forwarding no If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256550`

### Rule: The Photon operating system must configure sshd to perform strict mode checking of home directory configuration files.

**Rule ID:** `SV-256550r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If other users have access to modify user-specific Secure Shell (SSH) configuration files, they may be able to log on to the system as another user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # sshd -T|&grep -i StrictModes Expected result: StrictModes yes If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256551`

### Rule: The Photon operating system must configure sshd to disallow Kerberos authentication.

**Rule ID:** `SV-256551r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Kerberos is enabled through Secure Shell (SSH), sshd provides a means of access to the system's Kerberos implementation. Vulnerabilities in the system's Kerberos implementation may then be subject to exploitation. To reduce the attack surface of the system, the Kerberos authentication mechanism within SSH must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # sshd -T|&grep -i KerberosAuthentication Expected result: KerberosAuthentication no If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256552`

### Rule: The Photon operating system must configure sshd to disallow authentication with an empty password.

**Rule ID:** `SV-256552r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Blank passwords are one of the first things an attacker checks for when probing a system. Even is the user somehow has a blank password on the operating system, sshd must not allow that user to log in.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # sshd -T|&grep -i PermitEmptyPasswords Expected result: PermitEmptyPasswords no If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256553`

### Rule: The Photon operating system must configure sshd to disallow compression of the encrypted session stream.

**Rule ID:** `SV-256553r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If compression is allowed in a Secure Shell (SSH) connection prior to authentication, vulnerabilities in the compression software could result in compromise of the system from an unauthenticated connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # sshd -T|&grep -i Compression Expected result: Compression no If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256554`

### Rule: The Photon operating system must configure sshd to display the last login immediately after authentication.

**Rule ID:** `SV-256554r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Providing users with feedback on the last time they logged on via Secure Shell (SSH) facilitates user recognition and reporting of unauthorized account use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # sshd -T|&grep -i PrintLastLog Expected result: PrintLastLog yes If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256555`

### Rule: The Photon operating system must configure sshd to ignore user-specific trusted hosts lists.

**Rule ID:** `SV-256555r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Secure Shell (SSH) trust relationships enable trivial lateral spread after a host compromise and therefore must be explicitly disabled. Individual users can have a local list of trusted remote machines, which must also be ignored while disabling host-based authentication generally.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # sshd -T|&grep -i IgnoreRhosts Expected result: IgnoreRhosts yes If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256556`

### Rule: The Photon operating system must configure sshd to ignore user-specific "known_host" files.

**Rule ID:** `SV-256556r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Secure Shell (SSH) trust relationships enable trivial lateral spread after a host compromise and therefore must be explicitly disabled. Individual users can have a local list of trusted remote machines that must also be ignored while disabling host-based authentication generally.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # sshd -T|&grep -i IgnoreUserKnownHosts Expected result: IgnoreUserKnownHosts yes If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256557`

### Rule: The Photon operating system must configure sshd to limit the number of allowed login attempts per connection.

**Rule ID:** `SV-256557r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By setting the login attempt limit to a low value, an attacker will be forced to reconnect frequently, which severely limits the speed and effectiveness of brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # sshd -T|&grep -i MaxAuthTries Expected result: MaxAuthTries 6 If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256558`

### Rule: The Photon operating system must be configured so the x86 Ctrl-Alt-Delete key sequence is disabled on the command line.

**Rule ID:** `SV-256558r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When the Ctrl-Alt-Del target is enabled, a locally logged-on user who presses Ctrl-Alt-Delete, when at the console, can reboot the system. If accidentally pressed, as could happen in the case of a mixed operating system environment, this can create the risk of short-term loss of systems availability due to unintentional reboot.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # systemctl status ctrl-alt-del.target Expected result: ctrl-alt-del.target Loaded: masked (Reason: Unit ctrl-alt-del.target is masked.) Active: inactive (dead) If the "ctrl-alt-del.target" is not "inactive" and "masked", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256559`

### Rule: The Photon operating system must be configured so the "/etc/skel" default scripts are protected from unauthorized modification.

**Rule ID:** `SV-256559r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the skeleton files are not protected, unauthorized personnel could change user startup parameters and possibly jeopardize user files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # stat -c "%n permissions are %a and owned by %U:%G" /etc/skel/.[^.]* Expected result: /etc/skel/.bash_logout permissions are 750 and owned by root:root /etc/skel/.bash_profile permissions are 644 and owned by root:root /etc/skel/.bashrc permissions are 750 and owned by root:root If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256560`

### Rule: The Photon operating system must be configured so the "/root" path is protected from unauthorized access.

**Rule ID:** `SV-256560r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the "/root" path is accessible to users other than root, unauthorized users could change the root partitions files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # stat -c "%n permissions are %a and owned by %U:%G" /root Expected result: /root permissions are 700 and owned by root:root If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256561`

### Rule: The Photon operating system must be configured so that all global initialization scripts are protected from unauthorized modification.

**Rule ID:** `SV-256561r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Local initialization files are used to configure the user's shell environment upon login. Malicious modification of these files could compromise accounts upon login.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # find /etc/bash.bashrc /etc/profile /etc/profile.d/ -xdev -type f -a '(' -perm -002 -o -not -user root -o -not -group root ')' -exec ls -ld {} \; If any files are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256562`

### Rule: The Photon operating system must be configured so that all system startup scripts are protected from unauthorized modification.

**Rule ID:** `SV-256562r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If system startup scripts are accessible to unauthorized modification, this could compromise the system on startup.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # find /etc/rc.d/* -xdev -type f -a '(' -perm -002 -o -not -user root -o -not -group root ')' -exec ls -ld {} \; If any files are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256563`

### Rule: The Photon operating system must be configured so that all files have a valid owner and group owner.

**Rule ID:** `SV-256563r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If files do not have valid user and group owners, unintended access to files could occur.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # find / -fstype ext4 -nouser -o -nogroup -exec ls -ld {} \; 2>/dev/null If any files are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256564`

### Rule: The Photon operating system must be configured so the "/etc/cron.allow" file is protected from unauthorized modification.

**Rule ID:** `SV-256564r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cron files and folders are accessible to unauthorized users, malicious jobs may be created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # stat -c "%n permissions are %a and owned by %U:%G" /etc/cron.allow Expected result: /etc/cron.allow permissions are 600 and owned by root:root If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256565`

### Rule: The Photon operating system must be configured so that all cron jobs are protected from unauthorized modification.

**Rule ID:** `SV-256565r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cron files and folders are accessible to unauthorized users, malicious jobs may be created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # find /etc/cron.d/ /etc/cron.daily/ /etc/cron.hourly/ /etc/cron.monthly/ /etc/cron.weekly/ -xdev -type f -a '(' -perm -022 -o -not -user root ')' -exec ls -ld {} \; If any files are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256566`

### Rule: The Photon operating system must be configured so that all cron paths are protected from unauthorized modification.

**Rule ID:** `SV-256566r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cron files and folders are accessible to unauthorized users, malicious jobs may be created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # stat -c "%n permissions are %a and owned by %U:%G" /etc/cron.d /etc/cron.daily /etc/cron.hourly /etc/cron.monthly /etc/cron.weekly Expected result: /etc/cron.d permissions are 755 and owned by root:root /etc/cron.daily permissions are 755 and owned by root:root /etc/cron.hourly permissions are 755 and owned by root:root /etc/cron.monthly permissions are 755 and owned by root:root /etc/cron.weekly permissions are 755 and owned by root:root If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256567`

### Rule: The Photon operating system must not forward IPv4 or IPv6 source-routed packets.

**Rule ID:** `SV-256567r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source routing is an Internet Protocol mechanism that allows an IP packet to carry information, a list of addresses, that tells a router the path the packet must take. There is also an option to record the hops as the route is traversed. The list of hops taken, the "route record", provides the destination with a return path to the source. This allows the source (the sending host) to specify the route, loosely or strictly, ignoring the routing tables of some or all of the routers. It can allow a user to redirect network traffic for malicious purposes and should therefore be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # /sbin/sysctl -a --pattern "net.ipv[4|6].conf.(all|default|eth.*).accept_source_route" Expected result: net.ipv4.conf.all.accept_source_route = 0 net.ipv4.conf.default.accept_source_route = 0 net.ipv4.conf.eth0.accept_source_route = 0 net.ipv6.conf.all.accept_source_route = 0 net.ipv6.conf.default.accept_source_route = 0 net.ipv6.conf.eth0.accept_source_route = 0 If the output does not match the expected result, this is a finding. Note: The number of "ethx" lines returned is dependent on the number of interfaces. Every "ethx" entry must be set to "0".

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256568`

### Rule: The Photon operating system must not respond to IPv4 Internet Control Message Protocol (ICMP) echoes sent to a broadcast address.

**Rule ID:** `SV-256568r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Responding to broadcast (ICMP) echoes facilitates network mapping and provides a vector for amplification attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # /sbin/sysctl -a --pattern ignore_broadcasts Expected result: net.ipv4.icmp_echo_ignore_broadcasts = 1 If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256569`

### Rule: The Photon operating system must prevent IPv4 Internet Control Message Protocol (ICMP) redirect messages from being accepted.

**Rule ID:** `SV-256569r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # /sbin/sysctl -a --pattern "net.ipv4.conf.(all|default|eth.*).accept_redirects" Expected result: net.ipv4.conf.all.accept_redirects = 0 net.ipv4.conf.default.accept_redirects = 0 net.ipv4.conf.eth0.accept_redirects = 0 If the output does not match the expected result, this is a finding. Note: The number of "ethx" lines returned is dependent on the number of interfaces. Every "ethx" entry must be set to "0".

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256570`

### Rule: The Photon operating system must prevent IPv4 Internet Control Message Protocol (ICMP) secure redirect messages from being accepted.

**Rule ID:** `SV-256570r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # /sbin/sysctl -a --pattern "net.ipv4.conf.(all|default|eth.*).secure_redirects" Expected result: net.ipv4.conf.all.secure_redirects = 0 net.ipv4.conf.default.secure_redirects = 0 net.ipv4.conf.eth0.secure_redirects = 0 If the output does not match the expected result, this is a finding. Note: The number of "ethx" lines returned is dependent on the number of interfaces. Every "ethx" entry must be set to "0".

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256571`

### Rule: The Photon operating system must not send IPv4 Internet Control Message Protocol (ICMP) redirects.

**Rule ID:** `SV-256571r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages contain information from the system's route table, possibly revealing portions of the network topology.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # /sbin/sysctl -a --pattern "net.ipv4.conf.(all|default|eth.*).send_redirects" Expected result: net.ipv4.conf.all.send_redirects = 0 net.ipv4.conf.default.send_redirects = 0 net.ipv4.conf.eth0.send_redirects = 0 If the output does not match the expected result, this is a finding. Note: The number of "ethx" lines returned is dependent on the number of interfaces. Every "ethx" entry must be set to "0".

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256572`

### Rule: The Photon operating system must log IPv4 packets with impossible addresses.

**Rule ID:** `SV-256572r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The presence of "martian" packets (which have impossible addresses) as well as spoofed packets, source-routed packets, and redirects could be a sign of nefarious network activity. Logging these packets enables this activity to be detected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # /sbin/sysctl -a --pattern "net.ipv4.conf.(all|default|eth.*).log_martians" Expected result: net.ipv4.conf.all.log_martians = 1 net.ipv4.conf.default.log_martians = 1 net.ipv4.conf.eth0.log_martians = 1 If the output does not match the expected result, this is a finding. Note: The number of "ethx" lines returned is dependent on the number of interfaces. Every "ethx" entry must be set to "1".

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256573`

### Rule: The Photon operating system must use a reverse-path filter for IPv4 network traffic.

**Rule ID:** `SV-256573r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling reverse path filtering drops packets with source addresses that should not have been able to be received on the interface they were received on. It should not be used on systems that are routers for complicated networks but is helpful for end hosts and routers serving small networks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # /sbin/sysctl -a --pattern "net.ipv4.conf.(all|default|eth.*)\.rp_filter" Expected result: net.ipv4.conf.all.rp_filter = 1 net.ipv4.conf.default.rp_filter = 1 net.ipv4.conf.eth0.rp_filter = 1 If the output does not match the expected result, this is a finding. Note: The number of "ethx" lines returned is dependent on the number of interfaces. Every "ethx" entry must be set to "1".

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256574`

### Rule: The Photon operating system must not perform multicast packet forwarding.

**Rule ID:** `SV-256574r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # /sbin/sysctl -a --pattern "net.ipv[4|6].conf.(all|default|eth.*).mc_forwarding" Expected result: net.ipv4.conf.all.mc_forwarding = 0 net.ipv4.conf.default.mc_forwarding = 0 net.ipv4.conf.eth0.mc_forwarding = 0 net.ipv6.conf.all.mc_forwarding = 0 net.ipv6.conf.default.mc_forwarding = 0 net.ipv6.conf.eth0.mc_forwarding = 0 If the output does not match the expected result, this is a finding. Note: The number of "ethx" lines returned is dependent on the number of interfaces. Every "ethx" entry must be set to "0".

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256575`

### Rule: The Photon operating system must not perform IPv4 packet forwarding.

**Rule ID:** `SV-256575r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # /sbin/sysctl -a --pattern "net.ipv4.ip_forward$" Expected result: net.ipv4.ip_forward = 0 If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256576`

### Rule: The Photon operating system must send Transmission Control Protocol (TCP) timestamps.

**Rule ID:** `SV-256576r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>TCP timestamps are used to provide protection against wrapped sequence numbers. It is possible to calculate system uptime (and boot time) by analyzing TCP timestamps. These calculated uptimes can help a bad actor in determining likely patch levels for vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # /sbin/sysctl -a --pattern "net.ipv4.tcp_timestamps$" Expected result: net.ipv4.tcp_timestamps = 1 If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256577`

### Rule: The Photon operating system must be configured to protect the Secure Shell (SSH) public host key from unauthorized modification.

**Rule ID:** `SV-256577r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a public host key file is modified by an unauthorized user, the SSH service may be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # stat -c "%n permissions are %a and owned by %U:%G" /etc/ssh/*key.pub Expected result: /etc/ssh/ssh_host_ecdsa_key.pub permissions are 644 and owned by root:root /etc/ssh/ssh_host_ed25519_key.pub permissions are 644 and owned by root:root /etc/ssh/ssh_host_rsa_key.pub permissions are 644 and owned by root:root If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256578`

### Rule: The Photon operating system must be configured to protect the Secure Shell ( SSH) private host key from unauthorized access.

**Rule ID:** `SV-256578r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an unauthorized user obtains the private SSH host key file, the host could be impersonated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # stat -c "%n permissions are %a and owned by %U:%G" /etc/ssh/*key Expected result: /etc/ssh/ssh_host_dsa_key permissions are 600 and owned by root:root /etc/ssh/ssh_host_ecdsa_key permissions are 600 and owned by root:root /etc/ssh/ssh_host_ed25519_key permissions are 600 and owned by root:root /etc/ssh/ssh_host_rsa_key permissions are 600 and owned by root:root If any key file listed is not owned by root or not group owned by root or does not have permissions of "0600", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256579`

### Rule: The Photon operating system must enforce password complexity on the root account.

**Rule ID:** `SV-256579r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity rules must apply to all accounts on the system, including root. Without specifying the "enforce_for_root flag", "pam_cracklib" does not apply complexity rules to the root user. While root users can find ways around this requirement, given its superuser power, it is necessary to attempt to force compliance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep pam_cracklib /etc/pam.d/system-password|grep --color=always "enforce_for_root" Expected result: password requisite pam_cracklib.so dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 minlen=8 minclass=4 difok=4 retry=3 maxsequence=0 enforce_for_root If the output does not include "enforce_for_root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256580`

### Rule: The Photon operating system must protect all boot configuration files from unauthorized modification.

**Rule ID:** `SV-256580r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Boot configuration files control how the system boots, including single-user mode, auditing, log levels, etc. Improper or malicious configurations can negatively affect system security and availability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # find /boot/*.cfg -xdev -type f -a '(' -perm -002 -o -not -user root -o -not -group root ')' -exec ls -ld {} \; If any files are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256581`

### Rule: The Photon operating system must protect sshd configuration from unauthorized access.

**Rule ID:** `SV-256581r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "sshd_config" file contains all the configuration items for sshd. Incorrect or malicious configuration of sshd can allow unauthorized access to the system, insecure communication, limited forensic trail, etc.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # stat -c "%n permissions are %a and owned by %U:%G" /etc/ssh/sshd_config Expected result: /etc/ssh/sshd_config permissions are 600 and owned by root:root If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256582`

### Rule: The Photon operating system must protect all "sysctl" configuration files from unauthorized access.

**Rule ID:** `SV-256582r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "sysctl" configuration file specifies values for kernel parameters to be set on boot. Incorrect or malicious configuration of these parameters can have a negative effect on system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # find /etc/sysctl.conf /etc/sysctl.d/* -xdev -type f -a '(' -perm -002 -o -not -user root -o -not -group root ')' -exec ls -ld {} \; If any files are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-256583`

### Rule: The Photon operating system must set the "umask" parameter correctly.

**Rule ID:** `SV-256583r991590_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "umask" value influences the permissions assigned to files when they are created. The "umask" setting in "login.defs" controls the permissions for a new user's home directory. By setting the proper "umask", home directories will only allow the new user to read and write files there.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep ^UMASK /etc/login.defs Example result: UMASK 077 If "UMASK" is not configured to "077", this a finding. Note: "UMASK" should only be specified once in login.defs.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-256584`

### Rule: The Photon operating system must configure sshd to disallow HostbasedAuthentication.

**Rule ID:** `SV-256584r991591_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Secure Shell (SSH) trust relationships enable trivial lateral spread after a host compromise and therefore must be explicitly disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # sshd -T|&grep -i HostbasedAuthentication Expected result: hostbasedauthentication no If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-256585`

### Rule: The Photon operating system must store only encrypted representations of passwords.

**Rule ID:** `SV-256585r982199_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords must be protected at all times via strong, one-way encryption. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. If they are encrypted with a weak cipher, those passwords are much more vulnerable to offline brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep password /etc/pam.d/system-password|grep --color=always "sha512" If the output does not include "sha512", this is a finding.

## Group: SRG-OS-000077-GPOS-00045

**Group ID:** `V-256586`

### Rule: The Photon operating system must ensure the old passwords are being stored.

**Rule ID:** `SV-256586r982201_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the result is a password that is not changed per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # ls -al /etc/security/opasswd If "/etc/security/opasswd" does not exist, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256587`

### Rule: The Photon operating system must configure sshd to restrict AllowTcpForwarding.

**Rule ID:** `SV-256587r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>While enabling Transmission Control Protocol (TCP) tunnels is a valuable function of sshd, this feature is not appropriate for use on single-purpose appliances.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # sshd -T|&grep -i AllowTcpForwarding Expected result: allowtcpforwarding no If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256588`

### Rule: The Photon operating system must configure sshd to restrict LoginGraceTime.

**Rule ID:** `SV-256588r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, sshd unauthenticated connections are left open for two minutes before being closed. This setting is too permissive as no legitimate login would need such an amount of time to complete a login. Quickly terminating idle or incomplete login attempts will free resources and reduce the exposure any partial logon attempts may create.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # sshd -T|&grep -i LoginGraceTime Expected result: logingracetime 30 If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000478-GPOS-00223

**Group ID:** `V-256589`

### Rule: The Photon operating system must implement NIST FIPS-validated cryptography for the following: to provision digital signatures, generate cryptographic hashes, and protect unclassified information requiring confidentiality and cryptographic protection in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.

**Rule ID:** `SV-256589r959006_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. The operating system must implement cryptographic modules adhering to the higher standards approved by the federal government because this provides assurance they have been tested and validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # cat /proc/sys/crypto/fips_enabled If a value of "1" is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-256590`

### Rule: The Photon operating system must disable systemd fallback Domain Name System (DNS).

**Rule ID:** `SV-256590r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Systemd contains an ability to set fallback DNS servers. This is used for DNS lookups in the event no system-level DNS servers are configured or other DNS servers are specified in the systemd "resolved.conf" file. If uncommented, this configuration contains Google DNS servers by default and could result in DNS leaking information unknowingly in the event DNS is absent or misconfigured at the system level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # resolvectl status | grep 'Fallback DNS' If the output indicates that fallback DNS servers are configured, this is a finding.

