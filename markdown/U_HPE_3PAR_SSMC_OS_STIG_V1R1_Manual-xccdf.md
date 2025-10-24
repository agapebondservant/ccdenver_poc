# STIG Benchmark: HPE 3PAR SSMC Operating System Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-255237`

### Rule: Any publicly accessible connection to SSMC must display the Standard Mandatory DOD Notice and Consent Banner before granting access to the system.

**Rule ID:** `SV-255237r869861_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the system by following below steps: 1. Log on to SSMC Web Administrator console GUI as "ssmcadmin". 2. Navigate to Actions >> Preferences >> Application. 3. Check if the login banner slider is toggled to "yes" and the desired text in English is set in the textbox adjacent to the control. If the custom banner text is not set to the Standard Mandatory DOD Notice and Consent Banner, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-255238`

### Rule: SSMC must display the Standard Mandatory DOD Notice and Consent Banner before granting local or remote access to the system.

**Rule ID:** `SV-255238r869864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to SSMC ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC displays the full text of the Standard Mandatory DOD Notice and Consent Banner before granting access to the system. 1. Access the SSMC web application by submitting the URL https://<ssmc_ip_or_fqdn>:8443/. 2. Log on to SSMC admin console as ssmcadmin. 3. Navigate to Action >> Preferences. Verify that the full text of the Standard Mandatory DOD Notice and consent banner is seen as stored against Custom Banner field. The DOD Notice and consent banner message should read as follows in all of steps 1, 2 and 3 above: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the full text of the Standard Mandatory DOD Notice and Consent Banner is not displayed, this is a finding.

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-255239`

### Rule: SSMC must employ strong authenticators in the establishment of nonlocal maintenance and diagnostic sessions.

**Rule ID:** `SV-255239r869867_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If maintenance tools are used by unauthorized personnel, they may accidentally or intentionally damage or compromise the system. The act of managing systems and applications includes the ability to access sensitive application information, such as system configuration details, diagnostic information, user information, and potentially sensitive application data. Some maintenance and test tools are either standalone devices with their own operating systems or are applications bundled with an operating system. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. Typically, strong authentication requires authenticators that are resistant to replay attacks and employ multifactor authentication. Strong authenticators include, for example, PKI where certificates are stored on a token protected by a password, passphrase, or biometric. Satisfies: SRG-OS-000125-GPOS-00065, SRG-OS-000396-GPOS-00176, SRG-OS-000424-GPOS-00188, SRG-OS-000394-GPOS-00174, SRG-OS-000250-GPOS-00093, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190, SRG-OS-000423-GPOS-00187</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC is configured to strong SSH ciphers to protect the integrity of remote access sessions by doing the following: Log on to SSMC appliance as ssmcadmin via SSH, press "X" to escape to general bash shell from the TUI menu, and issue the following command: $ sudo /ssmc/bin/config_security.sh -o cnsa_mode_appliance -a status If the output does not read as "Appliance CNSA mode is enabled", this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-255240`

### Rule: SSMC must enforce a delay of at least four seconds between logon prompts following a failed logon attempt.

**Rule ID:** `SV-255240r869870_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of logon attempts over a certain time interval reduces the chances that an unauthorized user may gain access to an account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC enforces a delay of at least four seconds between logon prompts following a failed logon attempt. To do so, perform the following steps. 1. Log on to SSMC appliance as ssmcadmin. Press "X" to escape to general bash shell. 2. Execute the following command: $ sudo /ssmc/bin/config_security.sh -o config_failedlogin_delay -a status Failed login delay is enabled If the command output does not read "Failed login delay is enabled", this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-255241`

### Rule: SSMC must enforce a minimum 15-character password length.

**Rule ID:** `SV-255241r869873_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that the 15-character minimum password length policy is set, do the following: 1. Log on to SSMC appliance as ssmcadmin. Press "X" to escape to shell. 2. Execute the following command: $ sudo /ssmc/bin/config_security.sh -o long_password_policy -a status Long password policy is enabled If the status does not read "enabled", this is a finding.

## Group: SRG-OS-000205-GPOS-00083

**Group ID:** `V-255242`

### Rule: SSMC must generate error messages that provide information necessary for corrective actions without revealing information that could be exploited by adversaries.

**Rule ID:** `SV-255242r869876_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> Any operating system providing too much information in error messages risks compromising the data and security of the structure, and content of error messages needs to be carefully considered by the organization. Organizations carefully consider the structure/content of error messages. The extent to which information systems are able to identify and handle error conditions is guided by organizational policy and operational requirements. Information that could be exploited by adversaries includes, for example, erroneous logon attempts with passwords entered by mistake as the username, mission/business information that can be derived from (if not stated explicitly by) information recorded, and personal information, such as account numbers, social security numbers, and credit card numbers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that SSMC is configured to prevent exfiltration of sensitive information, do the following: 1. Log on to SSMC appliance as ssmcadmin. Press "X" to escape to general bash shell. 2. Execute the following command: $ grep ^ssmc.management.notification.disable /opt/hpe/ssmc/ssmcbase/resources/ssmc.properties ssmc.management.notification.disable=false If the command output does not print "ssmc.management.notification.disable=false", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-255243`

### Rule: SSMC must be configured to offload logs to a SIEM that is configured to alert the ISSO or SA when the local built-in admin account (ssmcadmin) is accessed.

**Rule ID:** `SV-255243r870274_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DOD that reflects the most restrictive security posture consistent with operational requirements. The ssmcadmin account is an emergency group account used to administer ssmc. This is a privileged account that can Log on to the SSMC appliance. The ssmcaudit account is a nonprivileged group user account that can be enabled/disabled by ssmcadmin for CVE scanning via TUI. This is the other group account that can log on to the appliance. By alerting to the use of ssmcadmin account, the information assurance team can mitigate the risks involved in using this group account. These alerts must be used to ensure that the use of this account is warranted and documented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC is configured to offload logs to a SIEM that is set up to alert the ISSO or SA when the ssmcadmin account is accessed by performing the following: 1. Log on to SIEM where the logs are being offloaded. 2. Log on to SSMC with the ssmcadmin account. 3. Return to the SIEM to see that an alert has been generated based on the access of the ssmcadmin account. If the SIEM does not generate an alert for the ISSO or SA, this is a finding.

## Group: SRG-OS-000356-GPOS-00144

**Group ID:** `V-255244`

### Rule: SSMC must synchronize internal information system clocks to the authoritative time source when the time difference is greater than one second.

**Rule ID:** `SV-255244r869882_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider setting time periods for different types of systems (e.g., financial, legal, or mission-critical systems). Organizations should also consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). This requirement is related to the comparison done every 24 hours in SRG-OS-000355 because a comparison must be done in order to determine the time difference. Satisfies: SRG-OS-000356-GPOS-00144, SRG-OS-000355-GPOS-00143</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SSMC synchronizes system clocks to the authoritative time source by performing the following: 1. Log on to SSMC appliance as ssmcadmin. Press "X" to escape to general bash shell. 2. Execute the following command: $ sudo /ssmc/bin/config_security.sh -o configure_ntp -a status NTP service is configured If the NTP service is not configured, this is a finding.

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-255245`

### Rule: For PKI-based authentication, SSMC must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

**Rule ID:** `SV-255245r869885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that the remote syslog connection is configured to use "x509/certvalid" or "x509/name" as authentication mode: $ sudo /ssmc/bin/config_security.sh -o remote_syslog_appliance -a status | grep ssmc.rsyslog.server.authMode Expected: ssmc.rsyslog.server.authMode=x509/name OR ssmc.rsyslog.server.authMode=x509/certvalid If the output does not match either of the expected strings, it is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-255246`

### Rule: SSMC must enforce the limit of three consecutive invalid logon attempts by a nonadministrative user.

**Rule ID:** `SV-255246r869888_rule`
**Severity:** low

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if SSMC is configured to limit consecutive invalid logon attempts for ssmcaudit user to three times by executing the following command: $ sudo /ssmc/bin/config_security.sh -o session_lock -a status Session lock is enabled If the output of this command does not read "Session lock is enabled", this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-255247`

### Rule: SSMC must terminate all network connections associated with a communications session at the end of the session, or as follows: for in-band management sessions (privileged sessions), the session must be terminated after 10 minutes of inactivity.

**Rule ID:** `SV-255247r869891_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level, and deallocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that the operating system terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session. Satisfies: SRG-OS-000163-GPOS-00072, SRG-OS-000279-GPOS-00109</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC web server is configured to close inactive sessions after 10 minutes by doing the following: 1. Log on to the SSMC appliance as ssmcadmin. Press "X" to escape to general bash shell. 2. Execute the command: $ grep ^server.session.timeout /opt/hpe/ssmc/ssmcbase/resources/ssmc.properties server.session.timeout=10 If the value is not set to 10 minutes, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-255248`

### Rule: SSMC must prevent nonprivileged users from executing privileged functions to include disabling, circumventing, or altering implemented security safeguards/countermeasures.

**Rule ID:** `SV-255248r869894_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing nonprivileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Privileged functions include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Nonprivileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from nonprivileged users. Satisfies: SRG-OS-000324-GPOS-00125, SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00158</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC prevents nonprivileged users from executing privileged functions by doing the following: 1. Log on to SSMC appliance as ssmcadmin. Press "X" to escape to general bash shell. 2. Execute the following commands: $ sudo /ssmc/bin/config_security.sh -o sudo_password -a status Sudo password is enabled If the command output does not read "Sudo password is enabled", this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-255249`

### Rule: SSMC must provide audit record generation capability for DOD-defined auditable events for all operating system components.

**Rule ID:** `SV-255249r869897_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DOD has defined the list of events for which the operating system will provide an audit record generation capability as the following: 1. Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2. Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3. All account creations, modifications, disabling, and terminations; and 4. All kernel module load, unload, and restart actions. Satisfies: SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC provides audit record generation capability for DOD-defined auditable events for all operating system components, by executing the following command: $ sudo /ssmc/bin/config_security.sh -o verbose_shell_session_logs -a status Verbose shell session log is enabled If the command outputs do not read as "enabled", this is a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-255250`

### Rule: SSMC must allocate audit record storage capacity to store at least one weeks' worth of audit records, when audit records are not immediately sent to a central audit record storage facility.

**Rule ID:** `SV-255250r869900_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure operating systems have a sufficient storage capacity in which to write the audit logs, operating systems need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial installation of the operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SSMC allocates audit record storage capacity to store at least one weeks' worth of audit records, when audit records are not immediately sent to remote logging server by doing the following: 1. Log on to SSMC appliance as ssmcadmin. Press "X" to escape to general bash shell. 2. Execute the following command: $ sudo /ssmc/bin/config_security.sh -o remote_syslog_appliance -a status | grep ssmc.rsyslog.queue.maxdiskspace ssmc.rsyslog.queue.maxdiskspace=6 If the command output does not read "ssmc.rsyslog.queue.maxdiskspace=6", this is a finding.

