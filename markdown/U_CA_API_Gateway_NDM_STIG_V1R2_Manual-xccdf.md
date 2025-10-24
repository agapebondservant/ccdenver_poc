# STIG Benchmark: CA API Gateway NDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255500`

### Rule: The CA API Gateway must be installed on Red Hat Enterprise Linux (RHEL) Version 6.7 or higher.

**Rule ID:** `SV-255500r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The API Gateway (Appliance version) depends on specific RHEL capabilities for the security, logging, and auditing subsystems. Installation on alternative or older RHEL versions may create vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the CA API Gateway is installed on Red Hat Enterprise Linux (RHEL) Version 6.7 or higher. If the CA API Gateway is not installed on Red Hat Enterprise Linux (RHEL) Version 6.7 or higher, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-255501`

### Rule: The CA API Gateway must employ RADIUS + LDAPS or LDAPS to centrally manage authentication settings.

**Rule ID:** `SV-255501r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of authentication servers or other centralized management servers for providing centralized authentication services is required for network device management. Maintaining local administrator accounts for daily usage on each network device without centralized management is not scalable or feasible. Without centralized management, it is likely that credentials for some network devices will be forgotten, leading to delays in administration, which itself leads to delays in remediating production problems and in addressing compromises in a timely fashion. Use of RADIUS + LDAPS or LDAPS for authentication and authorization provides the Gateway with an ability to authenticate credentials against a centralized and secured identity management system. This allows permissions for administration of the Gateway to be governed independently of the Gateway.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the CA API Gateway configuration to determine if RADIUS + LDAPS or LDAPS is employed to centrally manage authentication settings. - SSH to SSG as a member of ssgconfig. - Select: 1) Configure system settings, 6) Export configuration. - Export configuration to "file". - Go back to main menu, select 3) Use a privileged shell (root). - Navigate to /home/ssgconfig, open "file". - Check "authenticationType". If "authenticationType" is not RADIUS_WITH_LDAP or RADIUS_WITH_LDAPS, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255502`

### Rule: The CA API Gateway must shut down by default upon audit failure (unless availability is an overriding concern).

**Rule ID:** `SV-255502r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the network device is at risk of failing to process audit logs as required, it take action to mitigate the failure. Audit processing failures include: software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When availability is an overriding concern, other approved actions in response to an audit failure are as follows: (i) If the failure was caused by the lack of audit record storage capacity, the network device must continue generating audit records if possible (automatically restarting the audit service if necessary), overwriting the oldest audit records in a first-in-first-out manner. (ii) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, the network device must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/etc/audit/auditd.conf" file contains the lines: disk_full_action = HALT disk_error_action = HALT If "/etc/audit/auditd.conf" does not contain these lines, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255503`

### Rule: The CA API Gateway must forward all log audit log messages to the central log server.

**Rule ID:** `SV-255503r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Protection of log data includes assuring log data is not accidentally lost or deleted. Regularly backing up audit records to a different system or onto separate media than the system being audited helps to assure, in the event of a catastrophic system failure, the audit records will be retained. This helps to ensure a compromise of the information system being audited does not also result in a compromise of the audit records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the CA API Gateway forwards all log audit log messages to the central log server. Within the "/etc/rsyslog.conf" file, confirm a rule in the format "*.* @@loghost.log.com" is in the ruleset section. If the CA API Gateway "/etc/rsyslog.conf" file does not have a rule in the format "*.* @@loghost.log.com" in the ruleset section, this is a finding.

## Group: SRG-APP-000080-NDM-000345

**Group ID:** `V-255504`

### Rule: The CA API Gateway must not have any default manufacturer passwords when deployed.

**Rule ID:** `SV-255504r984088_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network devices not protected with strong password schemes provide the opportunity for anyone to crack the password and gain access to the device, which can result in loss of availability, confidentiality, or integrity of network traffic. Many default vendor passwords are well known or are easily guessed; therefore, not removing them prior to deploying the network device into production provides an opportunity for a malicious user to gain unauthorized access to the device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify login as "root" (at the console) and "ssgconfig" have non-default passwords. The default password for "root" is "7layer" and the default password for "ssgconfig" is "7layer". If root or ssgconfig use default passwords, this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-255505`

### Rule: In the event the authentication server is unavailable, there must be one local account of last resort.

**Rule ID:** `SV-255505r960969_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privileged-level) access to the device is required at all times. An account can be created on the device's local database for use in an emergency, such as when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is also referred to as the account of last resort since the emergency administration account is strictly intended to be used only as a last resort and immediate administrative access is absolutely necessary. The number of emergency administration accounts is restricted to at least one, but no more than operationally required as determined by the ISSO. The emergency administration account logon credentials must be stored in a sealed envelope and kept in a safe.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "root" (or its equivalent, renamed account) is listed in the password configuration files. If the "root" account is not listed in the password configuration files, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-255506`

### Rule: The CA API Gateway must enforce a minimum 15-character password length.

**Rule ID:** `SV-255506r984092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the CA API Gateway configuration files for passwords (/etc/login.defs, /etc/pam.d/password, /etc/pam.d/password-auth-ac, /etc/pam.d/system-auth, and /etc/pam.d/system-auth-ac) each have this line: PASS_MIN_LEN 15. If the CA API Gateway configuration files for passwords (/etc/login.defs, /etc/pam.d/password, /etc/pam.d/password-auth-ac, /etc/pam.d/system-auth, and /etc/pam.d/system-auth-ac) do not have the line requiring minimum 15-character password length, this is a finding.

## Group: SRG-APP-000170-NDM-000329

**Group ID:** `V-255507`

### Rule: If multifactor authentication is not supported and passwords must be used, the CA API Gateway must require that when a password is changed, the characters are changed in at least 8 of the positions within the password.

**Rule ID:** `SV-255507r984101_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the application allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the password attribute "difok" field is set to "8" in the following files: -- /etc/pam.d/password-auth -- /etc/pam.d/password-auth-ac If the password attribute "difok" field is not set to "8" in these files, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255508`

### Rule: The CA API Gateway must automatically remove or disable emergency accounts, except the emergency administration account, after 72 hours.

**Rule ID:** `SV-255508r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Emergency accounts are administrator accounts which are established in response to crisis situations where the need for rapid account activation is required. Therefore, emergency account activation may bypass normal account authorization processes. If emergency accounts remain active when no longer needed, they may be used to gain unauthorized access. The risk is greater for the network device since these accounts have elevated privileges. To mitigate this risk, automated termination of these accounts must be set upon account creation. It is important to note the difference between emergency accounts and the emergency administration account. The emergency administration account, also known as the account of last resort, is an infrequently used account used by network administrators only when network or normal logon/access is not available. The emergency administration account is not subject to automatic termination dates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify expiry of account with command: chage -l "USERNAME" and look at the "Account expires" line for expiry date. If the expiry date is more than "72" hours after emergency account creation, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255509`

### Rule: The CA API Gateway must activate a system alert message, send an alarm, and/or automatically shut down when a component failure is detected.

**Rule ID:** `SV-255509r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Predictable failure prevention requires organizational planning to address device failure issues. If components key to maintaining the device's security fail to function, the device could continue operating in an insecure state. If appropriate actions are not taken when a network device failure occurs, a denial of service condition may occur which could result in mission failure since the network would be operating without a critical security monitoring and prevention function. Upon detecting a failure of network device security components, the network device must activate a system alert message, send an alarm, or shut down.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/usr/local/bin/failtest" script exists and is executable. Verify crontab runs "/usr/local/bin/failtest" every minute by checking cron's logfile "/var/log/cron". If "/usr/local/bin/failtest" does not exist or it is not executable, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255510`

### Rule: The CA API Gateway must notify System Administrators (SAs) and Information System Security Officers (ISSMs) when accounts are created, or enabled when previously disabled.

**Rule ID:** `SV-255510r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply enable a new or disabled account. Notification of account enabling is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of application user accounts and notifies SAs and ISSMs. Such a process greatly reduces the risk that accounts will be surreptitiously enabled and provides logging that can be used for forensic purposes. In order to detect and respond to events that affect network administrator accessibility and device processing, network devices must audit account enabling actions and, as required, notify the appropriate individuals so they can investigate the event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/usr/local/bin/alerter" script exists and is executable. Verify crontab runs "/usr/local/bin/alerter" every minute by checking cron's logfile /var/log/cron. If the "/usr/local/bin/alerter" script does not exist, this is a finding. If the "/usr/local/bin/alerter" script does not run every minute as a cron job, this is a finding. An example follows. The SNMP destination host and username/password are configured by editing the shell variables near the beginning of the script. SNMPUSER should be set to the username recognized by the SNMP Management Station. SNMPENGINEID should be set to the SNMPv3 EngineID the Management Station uses for this application. SNMPHOST should be set to the hostname of the SNMP Management Station. This authentication configuration is placed in "/etc/snmp/snmp.conf": ----------------------------------- defSecurityLevel authPriv defAuthType SHA defPrivType AES defAuthPassphrase {password123} defPrivPassphrase {password123} ----------------------------------- This snmp alerter script is placed in "/usr/local/bin/alerter script": -------- #!/bin/bash # # This script implements watching for changes in a system that may indicate unauthorized # changes have been made to the system # # It is designed to be run as "alerter -w" to capture the current configuration and # then to be run out of cron on a regular basis as "alerter -c" which then compares the # current configuration to the previously captured configuration. If the configuration # has changed an SNMP TRAP is sent using the SNMPBASECMD variable as the base snmptrap command. # SNMPBASECMD will have to be configured appropriately depending on the exact SNMPv3 security # implemented on the SNMP Management Server. # # The script uses /var/run/alerter as a base directory to capture filesystem timestamps and # the installed RPM software list. SNMPUSER=myuser SNMPENGINEID=0x0102030405 SNMPHOST=rsbfreebsd.ca.com SNMPENTNUM="1.3.6.1.4.1.17304" SNMPNOTIF=".7.3.128" SNMPBASECMD="snmptrap -v 3 -n \"\" -u ${SNMPUSER} -e ${SNMPENGINEID} ${SNMPHOST} 0 ${SNMPENTNUM}.7.3.128.0 ${SNMPENTNUM}.7.3.129.0 s" ALERTER_ROOT=/var/run/alerter ACCOUNTFILES=("/etc/passwd" "/etc/shadow" "/etc/group") TSFILE=timestamps RPMFILE=rpmlist function usage { echo "$0 [-w | -c]" echo " -w - Write data" echo " -c - Compare current to data" echo " (at least one must be selected)" echo } function writeTsSummary { for file in ${ACCOUNTFILES[*]} do ts=$(stat -c '%Y' $file) echo $file $ts >> $ALERTER_ROOT/$TSFILE done } function writeRpmSummary { rpm -qa >> $ALERTER_ROOT/$RPMFILE } function writeSummaries { if [ ! -d $ALERTER_ROOT ] then mkdir $ALERTER_ROOT fi rm -f $ALERTER_ROOT/$TSFILE $ALERTER_ROOT/$RPMFILE writeTsSummary writeRpmSummary }

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255511`

### Rule: The CA API Gateway must transmit organization-defined access authorization information using organization-defined security safeguards to organization-defined information systems which enforce access control decisions.

**Rule ID:** `SV-255511r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting access authorization information (i.e., access control decisions) ensures that authorization information cannot be altered, spoofed, or otherwise compromised during transmission. In distributed information systems, authorization processes and access control decisions may occur in separate parts of the systems. In such instances, authorization information is transmitted securely so timely access control decisions can be enforced at the appropriate locations. To support the access control decisions, it may be necessary to transmit, as part of the access authorization information, supporting security attributes. This is because, in distributed information systems, there are various access control decisions that need to be made, and different entities (e.g., services) make these decisions in a serial fashion, each requiring some security attributes to make the decisions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the CA API Gateway is configured to use LDAP or RADIUS+LDAP for all administrative accounts by using the "ssgconfig" account and using menu: 1) Configure system settings >> 4) Configure authentication method. Select the appropriate ldap/ldap+radius configuration and then verify its settings by continuing the menu process until it completes. If LDAP or RADIUS+LDAP is not configured for all administrative accounts, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-255512`

### Rule: The CA API Gateway must be configured to synchronize internal information system clocks with the primary and secondary time sources located in different geographic regions using redundant authoritative time sources.

**Rule ID:** `SV-255512r987682_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must utilize an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DoD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DoD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Gateway (using "ssgconfig") is configured to use multiple ntp sources using menu: 1) Configure system settings >> 1) Configure networking and system time settings. Walk through the query process until being queried for time servers and verify the list of ntp servers is correct. If the CA API Gateway is not configured to use multiple ntp sources, this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-255513`

### Rule: The CA API Gateway must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

**Rule ID:** `SV-255513r961443_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the application include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Gateway (using ssgconfig) is configured to use multiple ntp sources using menu: 1) Configure system settings >> 1) Configure networking and system time settings. Walk through the query process until being queried for time servers and verify the list of ntp servers is correct. If the CA API Gateway is not configured to use multiple ntp sources, this is a finding.

## Group: SRG-APP-000375-NDM-000300

**Group ID:** `V-255514`

### Rule: The CA API Gateway must record time stamps for audit records that meet a granularity of one second for a minimum degree of precision.

**Rule ID:** `SV-255514r961446_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without sufficient granularity of time stamps, it is not possible to adequately determine the chronological order of records. Time stamps generated by the application include date and time. Granularity of time measurements refers to the degree of synchronization between information system clocks and reference clocks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Gateway (using ssgconfig) is configured to use multiple ntp sources using menu: 1) Configure system settings >> 1) Configure networking and system time settings. Walk through the query process until being queried for time servers and verify the list of ntp servers is correct. If the CA API Gateway is not configured to use multiple ntp sources, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255515`

### Rule: The CA API Gateway must generate an alert that will then be sent to the ISSO, ISSM, and other designated personnel (deemed appropriate by the local organization) when the unauthorized installation of software is detected.

**Rule ID:** `SV-255515r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized software not only increases risk by increasing the number of potential vulnerabilities, it also can contain malicious code. Sending an alert (in real time) when unauthorized software is detected allows designated personnel to take action on the installation of unauthorized software. Note that while the device must generate the alert, the notification may be done by a management server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/usr/local/bin/alerter" script exists and is executable. Verify crontab runs "/usr/local/bin/alerter" every minute by checking cron's logfile /var/log/cron. If the "/usr/local/bin/alerter" script does not exist, this is a finding. If the "/usr/local/bin/alerter" script does not run every minute as a cron job, this is a finding. An example follows. The SNMP destination host and username/password are configured by editing the shell variables near the beginning of the script. SNMPUSER should be set to the username recognized by the SNMP Management Station. SNMPENGINEID should be set to the SNMPv3 EngineID the Management Station uses for this application. SNMPHOST should be set to the hostname of the SNMP Management Station. This authentication configuration is placed in "/etc/snmp/snmp.conf": ----------------------------------- defSecurityLevel authPriv defAuthType SHA defPrivType AES defAuthPassphrase {password123} defPrivPassphrase {password123} ----------------------------------- This snmp alerter script is placed in "/usr/local/bin/alerter script": -------- #!/bin/bash # # This script implements watching for changes in a system that may indicate unauthorized # changes have been made to the system # # It is designed to be run as "alerter -w" to capture the current configuration and # then to be run out of cron on a regular basis as "alerter -c" which then compares the # current configuration to the previously captured configuration. If the configuration # has changed an SNMP TRAP is sent using the SNMPBASECMD variable as the base snmptrap command. # SNMPBASECMD will have to be configured appropriately depending on the exact SNMPv3 security # implemented on the SNMP Management Server. # # The script uses /var/run/alerter as a base directory to capture filesystem timestamps and # the installed RPM software list. SNMPUSER=myuser SNMPENGINEID=0x0102030405 SNMPHOST=rsbfreebsd.ca.com SNMPENTNUM="1.3.6.1.4.1.17304" SNMPNOTIF=".7.3.128" SNMPBASECMD="snmptrap -v 3 -n \"\" -u ${SNMPUSER} -e ${SNMPENGINEID} ${SNMPHOST} 0 ${SNMPENTNUM}.7.3.128.0 ${SNMPENTNUM}.7.3.129.0 s" ALERTER_ROOT=/var/run/alerter ACCOUNTFILES=("/etc/passwd" "/etc/shadow" "/etc/group") TSFILE=timestamps RPMFILE=rpmlist function usage { echo "$0 [-w | -c]" echo " -w - Write data" echo " -c - Compare current to data" echo " (at least one must be selected)" echo } function writeTsSummary { for file in ${ACCOUNTFILES[*]} do ts=$(stat -c '%Y' $file) echo $file $ts >> $ALERTER_ROOT/$TSFILE done } function writeRpmSummary { rpm -qa >> $ALERTER_ROOT/$RPMFILE } function writeSummaries { if [ ! -d $ALERTER_ROOT ] then mkdir $ALERTER_ROOT fi rm -f $ALERTER_ROOT/$TSFILE $ALERTER_ROOT/$RPMFILE writeTsSummary writeRpmSummary }

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-255516`

### Rule: The CA API Gateway must authenticate NTP endpoint devices before establishing a network connection using bidirectional authentication that is cryptographically based.

**Rule ID:** `SV-255516r961506_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, Internet). A remote connection is any connection with a device communicating through an external network (e.g., the Internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability. For network device management, this has been determined to be network management device addresses, SNMP authentication, and NTP authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "server" lines in the "/etc/ntp.conf" file are all marked with "autokey". Perform the command "ntpq -p" to show peer functioning. If the "server" lines in the "/etc/ntp.conf" file are not marked with "autokey", this is a finding. If the command "ntpq -p" does not show peers functioning, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-255517`

### Rule: The CA API Gateway must authenticate SNMP endpoint devices before establishing a network connection using bidirectional authentication that is cryptographically based.

**Rule ID:** `SV-255517r961506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, Internet). A remote connection is any connection with a device communicating through an external network (e.g., the Internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability. For network device management, this has been determined to be network management device addresses, SNMP authentication, and NTP authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "snmptrap" shell command used to emit SNMP TRAPS to the Network Management Station is using Version 3 with User Authentication for each potential trap source identified in this document. "snmptrap -v 3 -a SHA -A mypassword -x AES -X mypassword -l authPriv -u traptest -e 0x8000000001020304 localhost REQUIRED_TRAP_OID" If SNMP Version 3 is not being used, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-255518`

### Rule: The CA API Gateway must authenticate RADIUS endpoint devices before establishing a network connection using bidirectional authentication that is cryptographically based.

**Rule ID:** `SV-255518r961506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, Internet). A remote connection is any connection with a device communicating through an external network (e.g., the Internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability. For network device management, this has been determined to be network management device addresses, SNMP authentication, and NTP authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using the "ssgconfig" menu subsystem, confirm RADIUS has been configured via 1) Configure system settings >> 4) Configure authentication method item 3 or 4. Confirm password is set to "Enter the RADIUS shared secret [<Hidden>]". If RADIUS is not correctly configured, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-255519`

### Rule: The CA API Gateway must authenticate LDAPS endpoint devices before establishing a network connection using bidirectional authentication that is cryptographically based.

**Rule ID:** `SV-255519r961506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, Internet). A remote connection is any connection with a device communicating through an external network (e.g., the Internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability. For network device management, this has been determined to be network management device addresses, SNMP authentication, and NTP authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using the "ssgconfig" menu subsystem, confirm LDAP (Secure) has been configured via 1) Configure system settings >> 4) Configure authentication method item 2 or 4. Confirm the answer to the question "Do you want to specify the URL to a PEM containing the certificate (y/n) [y]:" is "y". Ensure the answer to question "Specify the URL where the PEM formatted CA certificate can be located [ldaps://smldap.l7tech.com:636]:" is a trusted source of the certificate. If the LDAP is not correctly configured, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-255520`

### Rule: The CA API Gateway must obtain LDAPS server certificates securely to use bidirectional authentication that is cryptographically based.

**Rule ID:** `SV-255520r961506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, Internet). A remote connection is any connection with a device communicating through an external network (e.g., the Internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability. For network device management, this has been determined to be network management device addresses, SNMP authentication, and NTP authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the LDAPS server certificate is in "/etc/openldap/cacerts". Verify TLS_REQCERT is set to demand in "/etc/openldap/ldap.conf". If the LDAPS server certificate is not in "/etc/openldap/cacerts", this is a finding. If "TLS_REQCERT" is not set to demand in "/etc/openldap/ldap.conf", this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-255521`

### Rule: The CA API Gateway must protect against or limit the effects of all known types of Denial of Service (DoS) attacks on the CA API Gateway management network by employing organization-defined security safeguards.

**Rule ID:** `SV-255521r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of network devices to mitigate the impact of DoS attacks that have occurred or are ongoing on device availability. For each network device, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the device opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks. The security safeguards cannot be defined at the DoD level because they vary according to the capabilities of the individual network devices and the security controls applied on the adjacent networks (for example, firewalls performing packet filtering to block DoS attacks).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the CA API Gateway drops packets by default and only puts non-Gateway services on trusted interfaces. Check for the following lines in "/etc/sysconfig/iptables": :INPUT DROP [0:0] :FORWARD DROP [0:0] [0:0] -A INPUT -i eth0 -p udp -m udp --dport 53 -j ACCEPT [0:0] -A INPUT -i eth2 -p udp -m udp --dport 53 -j ACCEPT [0:0] -A INPUT -i eth3 -p udp -m udp --dport 53 -j ACCEPT [0:0] -A INPUT -i eth0 -p udp -m udp --dport 123 -j ACCEPT [0:0] -A INPUT -i eth2 -p udp -m udp --dport 123 -j ACCEPT [0:0] -A INPUT -i eth3 -p udp -m udp --dport 123 -j ACCEPT [0:0] -A INPUT -i eth0 -p tcp -m tcp --dport 3306 -j ACCEPT [0:0] -A INPUT -i eth0 -p tcp -m tcp --dport 22 -j ACCEPT Check for the following lines in "/etc/sysconfig/ip6tables": :INPUT DROP [0:0] [0:0] -A INPUT -i eth0 -p udp -m udp --dport 53 -j ACCEPT [0:0] -A INPUT -i eth2 -p udp -m udp --dport 53 -j ACCEPT [0:0] -A INPUT -i eth3 -p udp -m udp --dport 53 -j ACCEPT [0:0] -A INPUT -i eth0 -p udp -m udp --dport 123 -j ACCEPT [0:0] -A INPUT -i eth2 -p udp -m udp --dport 123 -j ACCEPT [0:0] -A INPUT -i eth3 -p udp -m udp --dport 123 -j ACCEPT [0:0] -A INPUT -i eth0 -p tcp -m tcp --dport 3306 -j ACCEPT [0:0] -A INPUT -i eth0 -p tcp -m tcp --dport 22 -j ACCEPT If the CA API Gateway does not drop packets by default or puts non-Gateway services on untrusted interfaces, this is a finding. Verify the CA API Gateway logs and drops TCP packets with bad flags. Check for the following lines in "/etc/sysconfig/iptables": [0:0] -A INPUT -p tcp -m tcp --tcp-flags FIN,SYN,RST,PSH,ACK,URG FIN,PSH,URG -j badflags [0:0] -A INPUT -p tcp -m tcp --tcp-flags FIN,SYN,RST,PSH,ACK,URG FIN,SYN,RST,PSH,ACK,URG -j badflags [0:0] -A INPUT -p tcp -m tcp --tcp-flags FIN,SYN,RST,PSH,ACK,URG FIN,SYN,RST,ACK,URG -j badflags [0:0] -A INPUT -p tcp -m tcp --tcp-flags FIN,SYN,RST,PSH,ACK,URG NONE -j badflags [0:0] -A INPUT -p tcp -m tcp --tcp-flags SYN,RST SYN,RST -j badflags [0:0] -A INPUT -p tcp -m tcp --tcp-flags FIN,SYN FIN,SYN -j badflags [0:0] -A badflags -m limit --limit 15/min -j LOG --log-prefix "Badflags:" [0:0] -A badflags -j DROP Check for the following lines in "/etc/sysconfig/ip6tables": [0:0] -A INPUT -p tcp -m tcp --tcp-flags FIN,SYN,RST,PSH,ACK,URG FIN,PSH,URG -j badflags6 [0:0] -A INPUT -p tcp -m tcp --tcp-flags FIN,SYN,RST,PSH,ACK,URG FIN,SYN,RST,PSH,ACK,URG -j badflags6 [0:0] -A INPUT -p tcp -m tcp --tcp-flags FIN,SYN,RST,PSH,ACK,URG FIN,SYN,RST,ACK,URG -j badflags6 [0:0] -A INPUT -p tcp -m tcp --tcp-flags FIN,SYN,RST,PSH,ACK,URG NONE -j badflags6 [0:0] -A INPUT -p tcp -m tcp --tcp-flags SYN,RST SYN,RST -j badflags6 [0:0] -A INPUT -p tcp -m tcp --tcp-flags FIN,SYN FIN,SYN -j badflags6 [0:0] -A badflags6 -m limit --limit 15/min -j LOG --log-prefix "Badflags6:" [0:0] -A badflags6 -j DROP If the CA API Gateway does not log and drop TCP packets with bad flags, this is a finding. Verify the CA API Gateway only allows certain ICMPs and rate limits pings. Check for the following lines in "/etc/sysconfig/iptables": [0:0] -A INPUT -p icmp -m icmp --icmp-type 0 -j ACCEPT [0:0] -A INPUT -p icmp -m icmp --icmp-type 3 -j ACCEPT [0:0] -A INPUT -p icmp -m icmp --icmp-type 11 -j ACCEPT [0:0] -A INPUT -p icmp -m icmp --icmp-type 8 -m limit --limit 2/sec -j ACCEPT [0:0] -A INPUT -p icmp -j badflags [0:0] -A OUTPUT -p icmp -m state --state INVALID -j DROP Check for the following lines in "/etc/sysconfig/ip6tables": [0:0] -A INPUT -p icmpv6 -m icmpv6 --icmpv6-type 1 -j ACCEPT [0:0] -A INPUT -p icmpv6 -m icmpv6 --icmpv6-type 3 -j ACCEPT [0:0] -A INPUT -p icmpv6 -m icmpv6 --icmpv6-type 129 -j ACCEPT [0:0] -A INPUT -p icmpv6 -m icmpv6 --icmpv6-type 128 -m limit --limit 2/sec -j ACCEPT [0:0] -A INPUT -p icmpv6 -m icmpv6 --icmpv6-type 133 -j ACCEPT [0:0] -A INPUT -p icmpv6 -m icmpv6 --icmpv6-type 134 -j ACCEPT [0:0] -A INPUT -p icmpv6 -m icmpv6 --icmpv6-type 135 -j ACCEPT [0:0] -A INPUT -p icmpv6 -m icmpv6 --icmpv6-type 136 -j ACCEPT [0:0] -A INPUT -p icmpv6 -m icmpv6 --icmpv6-type 137 -j ACCEPT [0:0] -A INPUT -p icmpv6 -j badflags6 If the CA API Gateway does not only allow certain ICMPs and rate limits pings, this is a finding.

## Group: SRG-APP-000503-NDM-000320

**Group ID:** `V-255522`

### Rule: The CA API Gateway must generate audit records when successful/unsuccessful logon attempts occur.

**Rule ID:** `SV-255522r961824_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm the CA API Gateway file "/etc/audit/audit.rules" is the file as distributed using command: rpm -Vf /etc/audit/audit.rules If the string returned contains a "5" (ok: .......T., failure: S.5....T.), this is a finding.

## Group: SRG-APP-000505-NDM-000322

**Group ID:** `V-255523`

### Rule: The CA API Gateway must generate audit records showing starting and ending time for administrator access to the system.

**Rule ID:** `SV-255523r961830_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm the CA API Gateway file "/etc/audit/audit.rules" is the file as distributed using command: rpm -Vf /etc/audit/audit.rules If the string returned contains a "5" (ok: .......T., failure: S.5....T.), this is a finding.

## Group: SRG-APP-000506-NDM-000323

**Group ID:** `V-255524`

### Rule: The CA API Gateway must generate audit records when concurrent logons from different workstations occur.

**Rule ID:** `SV-255524r961833_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm the CA API Gateway file "/etc/audit/audit.rules" is the file as distributed using command: rpm -Vf /etc/audit/audit.rules If the string returned contains a "5" (ok: .......T., failure: S.5....T.), this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-255525`

### Rule: The CA API Gateway must off-load audit records onto a different system or media than the system being audited.

**Rule ID:** `SV-255525r961860_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify by confirming the following lines are part of "rsyslogd.conf": # auditd audit.log $ModLoad imfile $InputFileName /var/log/audit/audit.log $InputFileTag tag_audit_log: $InputFileStateFile audit_log $InputFileSeverity info $InputFileFacility local6 $InputRunFileMonitor Further verify that this line is also part of the rsyslogd.conf file: local6.* @@loghost.ca.com If "rsyslogd.conf" does not contain the above lines, this is a finding.

## Group: SRG-APP-000516-NDM-000334

**Group ID:** `V-255526`

### Rule: The CA API Gateway must generate audit log events for a locally developed list of auditable events.

**Rule ID:** `SV-255526r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. Logging the actions of specific events provides a means to investigate an attack; to recognize resource utilization or capacity thresholds; or to identify an improperly configured network device. If auditing is not comprehensive, it will not be useful for intrusion monitoring, security investigations, and forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine "/etc/audit/audit.rules" to confirm any custom developed rules are contained within the file. If the "/etc/audit/audit.rules" does not contain the custom developed rules within the file, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255527`

### Rule: The CA API Gateway must employ automated mechanisms to detect the addition of unauthorized components or devices.

**Rule ID:** `SV-255527r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement addresses configuration management of the network device. The network device must automatically detect the installation of unauthorized software or hardware onto the device itself. Monitoring may be accomplished on an ongoing basis or by periodic monitoring. Automated mechanisms can be implemented within the network device and/or in another separate information system or device. If the addition of unauthorized components or devices is not automatically detected, then such components or devices could be used for malicious purposes, such as transferring sensitive data to removable media for compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/etc/modprobe.d/ssg-harden.conf" contents are: install dccp /bin/false install sctp /bin/false install rds /bin/false install tipc /bin/false install net-pf-31 /bin/false install bluetooth /bin/false install usb-storage /bin/false options ipv6 disable=1 If the "/etc/modprobe.d/ssg-harden.conf" contents do not contain the above, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255528`

### Rule: The CA API Gateway must employ automated mechanisms to assist in the tracking of security incidents.

**Rule ID:** `SV-255528r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Despite the investment in perimeter defense technologies, enclaves are still faced with detecting, analyzing, and remediating network breaches and exploits that have made it past the network device. An automated incident response infrastructure allows network operations to immediately react to incidents by identifying, analyzing, and mitigating any network device compromise. Incident response teams can perform root cause analysis, determine how the exploit proliferated, and identify all affected nodes, as well as contain and eliminate the threat. The network device assists in the tracking of security incidents by logging detected security events. The audit log and network device application logs capture different types of events. The audit log tracks audit events occurring on the components of the network device. The application log tracks the results of the network device content filtering function. These logs must be aggregated into a centralized server and can be used as part of the organization's security incident tracking and analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the CA API Gateway forwards all log audit log messages to the central log server. Within the "/etc/rsyslog.conf" file, confirm a rule in the format "*.* @@loghost.log.com" is in the ruleset section. If the CA API Gateway "/etc/rsyslog.conf" file does not have a rule in the format "*.* @@loghost.log.com" in the ruleset section, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-264435`

### Rule: The CA API NDM must be using a version supported by the vendor.

**Rule ID:** `SV-264435r992102_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Systems running an unsupported software/firmware version lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This STIG is sunset and no longer updated. Compare the version running to the supported version by the vendor. If the system is using an unsupported version from the vendor, this is a finding.

