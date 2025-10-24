# STIG Benchmark: Red Hat Ansible Automation Controller Application Server Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-AS-000001

**Group ID:** `V-256896`

### Rule: Automation Controller must limit the number of concurrent sessions to an organization-defined number for all accounts and/or account types.

**Rule ID:** `SV-256896r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application management includes the ability to control the number of sessions that utilize an application by all accounts and/or account types. Limiting the number of allowed sessions is helpful in limiting risks related to denial-of-service attacks. Automation Controllers host and expose business logic and application processes. Automation Controller limits the maximum number of concurrent sessions in a manner that affects the entire application server or on an individual application basis. The settings must follow DOD-recommended values, but the settings should be configurable to allow for future DOD direction. While the DOD will specify recommended values, the values can be adjusted to accommodate the operational requirement of a given system. Satisfies: SRG-APP-000001-AS-000001, SRG-APP-000295-AS-000263</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a System Administrator for each Automation Controller host, navigate to the Automation Controller web administrator console: Settings >> System >> Miscellaneous Authentication settings. Verify the "Maximum Number of simultaneous logged in sessions" field is set according to policy. If this configuration setting does not match the organizationally defined maximum, or is set to -1 (negative one), this is a finding.

## Group: SRG-APP-000014-AS-000009

**Group ID:** `V-256897`

### Rule: Automation Controller must use encryption strength in accordance with the categorization of the management data during remote access management sessions.

**Rule ID:** `SV-256897r960759_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote management access is accomplished by leveraging common communication protocols and establishing a remote connection to the application server via a network for the purposes of managing Automation Controller. If cryptography is not used, then the session data traversing the remote connection could be intercepted and compromised. Automation Controller is accessed via standard HTTP (redirect)/HTTPS on standard ports, provided by NGINX. A self-signed certificate/key is installed by default; however, a user can provide a locally appropriate certificate and key per their organizational policy. SSL/TLS algorithm support is configured in the /etc./nginx/nginx.conf configuration file. Satisfies: SRG-APP-000014-AS-000009, SRG-APP-000142-AS-000014, SRG-APP-000172-AS-000120, SRG-APP-000441-AS-000258, SRG-APP-000442-AS-000259</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As an unauthenticated user, open a new web browser and go to http://<Automation Controller HOST> If not redirected to https://<Automation Controller HOST>, this is a finding.

## Group: SRG-APP-000015-AS-000010

**Group ID:** `V-256898`

### Rule: Automation Controller must implement cryptography mechanisms to protect the integrity of information.

**Rule ID:** `SV-256898r1107643_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Encryption is critical for protection of remote access sessions. If encryption is not being used for integrity, malicious users may gain the ability to modify Automation Controller configuration. The use of cryptography for ensuring integrity of remote access sessions mitigates that risk. Automation Controller utilizes a web management interface and scripted commands when allowing remote access. Web access requires the use of TLS and scripted access requires using SSH or some other form of approved cryptography. Automation Controller must have the ability to enable a secure remote admin capability. FIPS 140-2 approved TLS versions must be enabled and non-FIPS-approved SSL versions must be disabled. Automation Controller requires the use of Red Hat Enterprise Linux as an operating system and its underlying FIPS-validated cryptographic modules to ensure it meets FIPS 140-2 criteria. Satisfies: SRG-APP-000015-AS-000010, SRG-APP-000179-AS-000129, SRG-APP-000224-AS-000152, SRG-APP-000231-AS-000133, SRG-APP-000231-AS-000156, SRG-APP-000416-AS-000140, SRG-APP-000428-AS-000265, SRG-APP-000429-AS-000157, SRG-APP-000439-AS-000274, SRG-APP-000440-AS-000167, SRG-APP-000514-AS-000136</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a system administrator for each Automation Controller host, check if the operating system is FIPS-enabled: sysctl crypto.fips_enabled If "fips_enabled" is not "1", this is a finding. Verify the installed volume for Automation Controller is on a LUKS encrypted volume command: AAPROOT='/var/lib/awx' && cryptsetup status `df -T ${AAPROOT} | cut -d ' ' -f 1 | tail -n 1 ` | grep type | grep -i luks || echo "FAILED" If "FAILED" is displayed, this is a finding. Verify this LUKS encrypted volume is using FIPS-compliant cryptographic functions command: allowed_FIPS_ciphers=('aes.*\(256\|384\|512\)') ; echo "${allowed_FIPS_ciphers[*]}" | tr ' ' '\n' >tempfile && cryptsetup status `df -T ${AAPROOT} | cut -d ' ' -f 1 | tail -n 1 ` | grep -e '\(cipher\|keysize\)' | awk '{print $2}' | paste -s -d '-' | grep -f tempfile 1>/dev/null || echo "FAILED" && rm -f tempfile If "FAILED" is displayed, this is a finding.

## Group: SRG-APP-000068-AS-000035

**Group ID:** `V-256899`

### Rule: The Automation Controller management interface must display the Standard Mandatory DOD Notice and Consent Banner before granting access to the system.

**Rule ID:** `SV-256899r960843_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automation Controller is required to display the Standard Mandatory DOD Notice and Consent Banner before granting access to the system management interface, providing privacy and security notices consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance that states that: (i) users are accessing a U.S. Government information system; (ii) system usage may be monitored, recorded, and subject to audit; (iii) unauthorized use of the system is prohibited and subject to criminal and civil penalties; and (iv) the use of the system indicates consent to monitoring and recording. System use notification messages can be implemented in the form of warning banners displayed when individuals log on to the information system. System use notification is intended only for information system access including an interactive logon interface with a human user, and is not required when an interactive interface does not exist. Automation Controller supports displaying the Standard Mandatory DOD Notice and Consent Banner prior to logging in via the web console. Satisfies: SRG-APP-000068-AS-000035, SRG-APP-000069-AS-000036</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to the Automation Controller login page. Verify that the Standard Mandatory DOD Notice and Consent Banner is displayed with the following text: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the required DOD banner is not displayed on the login page or the CUSTOM_LOGIN_INFO does not contain the correct text, this is a finding. Alternatively, verify the setting CUSTOM_LOGIN_INFO setting in the REST API at /api/v2/settings/ui by running the following command: curl https://<Automation Controller HOST>/api/v2/settings/ui

## Group: SRG-APP-000080-AS-000045

**Group ID:** `V-256900`

### Rule: Automation Controller must use external log providers that can collect user activity logs in independent, protected repositories to prevent modification or repudiation.

**Rule ID:** `SV-256900r960864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automation Controller must be configured to use external logging to compile log records from multiple components within the server. The events occurring must be time-correlated in order to conduct accurate forensic analysis. In addition, the correlation must meet certain tolerance criteria. For instance, DOD may define that the time stamps of different logged events must not differ by any amount greater than ten seconds. Automation Controller must utilize an external logging tool that provides this capability. Satisfies: SRG-APP-000080-AS-000045, SRG-APP-000086-AS-000048, SRG-APP-000108-AS-000067, SRG-APP-000125-AS-000084, SRG-APP-000181-AS-000255, SRG-APP-000358-AS-000064, SRG-APP-000505-AS-000230, SRG-APP-000506-AS-000231, SRG-APP-000515-AS-000203</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to Automation Controller as an administrator. Navigate to Settings >> System >> Logging setting. The following parameters must be set: Enable External Logging = On Logging Aggregator Level Threshold = DEBUG TCP Connection Timeout = 5 (default) or the organizational timeout Enable/disable HTTPS certificate verification = On Logging Aggregator <> (Default) "Not configured" If any of these settings are incorrect, this is a finding.

## Group: SRG-APP-000109-AS-000068

**Group ID:** `V-256901`

### Rule: Automation Controller must allocate log record storage capacity and shut down by default upon log failure (unless availability is an overriding concern).

**Rule ID:** `SV-256901r1043188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when a system is at risk of failing to process logs, it detects and takes action to mitigate the failure. Log processing failures include software/hardware errors, failures in the log capturing mechanisms, and log storage capacity being reached or exceeded. During a failure, the application server must be configured to shut down unless the application server is part of a high availability system. When availability is an overriding concern, other approved actions in response to a log failure are as follows: (i) If the failure was caused by the lack of log record storage capacity, the application must continue generating log records if possible (automatically restarting the log service if necessary), overwriting the oldest log records in a first-in-first-out manner. (ii) If log records are sent to a centralized collection server and communication with this server is lost or the server fails, the application must queue log records locally until communication is restored or until the log records are retrieved manually. Upon restoration of the connection to the centralized collection server, action must be taken to synchronize the local log data with the collection server. Satisfies: SRG-APP-000109-AS-000068, SRG-APP-000357-AS-000038</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Administrator must check, for each Automation Controller host, the rsyslog configuration to verify the log rollover against an organizationally defined log capture size. Check LOG_AGGREGATOR_MAX_DISK_USAGE_GB field in the Automation Controller configuration. On the host, execute: awx-manage print_settings LOG_AGGREGATOR_MAX_DISK_USAGE_GB If this field is not set to the organizationally defined log capture size, this is a finding. Check LOG_AGGREGATOR_MAX_DISK_USAGE_PATH field in the Automation Controller configuration for the log file location to "/var/lib/awx". On the host, execute: awx-manage print_settings LOG_AGGREGATOR_MAX_DISK_USAGE_PATH If this field is not set to "/var/lib/awx", this is a finding.

## Group: SRG-APP-000109-AS-000070

**Group ID:** `V-256902`

### Rule: Automation Controller must be configured to fail over to another system in the event of log subsystem failure.

**Rule ID:** `SV-256902r1043188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automation Controller hosts must be capable of failing over to another Automation Controller host which can handle application and logging functions upon detection of an application log processing failure. This will allow continual operation of the application and logging functions while minimizing the loss of operation for the users and loss of log data. Satisfies: SRG-APP-000109-AS-000070, SRG-APP-000225-AS-000154, SRG-APP-000435-AS-000069</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Administrator must check the Automation Controller is deployed in an HA configuration. Administrator must check Automation Controller host via the REST API at api/v2/ping/ HA field for HA configuration. If this field is not true, indicating Automation Controller is in an HA configuration, this is a finding.

## Group: SRG-APP-000118-AS-000078

**Group ID:** `V-256903`

### Rule: Automation Controller's log files must be accessible by explicitly defined privilege.

**Rule ID:** `SV-256903r960930_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A failure of the confidentiality of Automation Controller log files would enable an attacker to identify key information about the system that they might not otherwise be able to obtain that would enable them to enumerate more information to enable escalation or lateral movement. Satisfies: SRG-APP-000118-AS-000078, SRG-APP-000119-AS-000079, SRG-APP-000120-AS-000080, SRG-APP-000121-AS-000081, SRG-APP-000122-AS-000082, SRG-APP-000123-AS-000083, SRG-APP-000267-AS-000170</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As an administrator, log into each Automation Controller host. Inspect the current permissions and owner of Automation Controller's NGINX log directory: stat -c "%a %U %G" /var/log/nginx/ | grep "770 nginx root" || echo "FAILED" If "FAILED" is displayed, this is a finding. Inspect the current permissions and owner of Automation Controller's log directory: $ stat -c "%a %U %G" /var/log/tower/ | grep "750 awx awx" || echo "FAILED" If "FAILED" is displayed, this is a finding. Inspect the current permissions and owner of Automation Controller's supervisor log directory: stat -c "%a %U %G" /var/log/supervisor/ | grep "770 root root" || echo "FAILED" If "FAILED" is displayed, this is a finding.

## Group: SRG-APP-000133-AS-000093

**Group ID:** `V-256904`

### Rule: Automation Controller must be capable of reverting to the last known good configuration in the event of failed installations and upgrades.

**Rule ID:** `SV-256904r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any changes to the components of Automation Controller can have significant effects on the overall security of the system. In order to ensure a prompt response to failed application installations and application server upgrades, Automation Controller must provide an automated rollback capability that allows Automation Controller to be restored to a previous known good configuration state prior to the application installation or application server upgrade.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The administrator must make a backup of the last known good configuration of the Automation Controller on each host. Locate the installer bundle directory that contains the inventory file used to install Ansible Automation Platform. Verify a backup of the last known good configuration has been made and stored in accordance with the Automation Controller Documentation and organizationally defined policy: https://docs.ansible.com/automation-controller/latest/html/administration/backup_restore.html If no such backup has been made, this is a finding.

## Group: SRG-APP-000148-AS-000101

**Group ID:** `V-256905`

### Rule: Automation Controller must be configured to use an enterprise user management system.

**Rule ID:** `SV-256905r1051118_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthenticated application servers render the organization subject to exploitation. Therefore, application servers must be uniquely identified and authenticated to prevent unauthorized access. Satisfies: SRG-APP-000148-AS-000101, SRG-APP-000149-AS-000102, SRG-APP-000151-AS-000103, SRG-APP-000177-AS-000126, SRG-APP-000389-AS-000253, SRG-APP-000390-AS-000254, SRG-APP-000391-AS-000239, SRG-APP-000392-AS-000240, SRG-APP-000400-AS-000246, SRG-APP-000401-AS-000243, SRG-APP-000402-AS-000247, SRG-APP-000403-AS-000248, SRG-APP-000404-AS-000249, SRG-APP-000405-AS-000250</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Administrator must check the Automation Controller web administrator console and verify the appropriate authentication provider is configured and the associated fields are complete and accurate. Log in to Automation Controller as an administrator and navigate to Settings >> Authentication. If the organization-defined identity provider is not configured, or any associated fields are incomplete or inaccurate, this is a finding.

## Group: SRG-APP-000153-AS-000104

**Group ID:** `V-256906`

### Rule: Automation Controller must be configured to authenticate users individually, prior to using a group authenticator.

**Rule ID:** `SV-256906r1015790_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Default superuser accounts, such as "root", are considered group authenticators. In the case of Automation Controller this is the "admin" account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the Automation Controller web console as an administrator and navigate to Access >> Users. The only local user allowed is the default/breakglass "admin". All other users need to come from an external authentication source. If any other local users exist, this is a finding.

## Group: SRG-APP-000172-AS-000121

**Group ID:** `V-256907`

### Rule: Automation Controller must utilize encryption when using LDAP for authentication.

**Rule ID:** `SV-256907r961029_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To avoid access with malicious intent, passwords will need to be protected at all times. This includes transmission where passwords must be encrypted for security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to Automation Controller as an administrator and navigate to Settings >> Authentication >> LDAP settings. If an LDAP server is configured but the "LDAP SERVER URI" field does not start with "ldaps://", this is a finding.

## Group: SRG-APP-000290-AS-000174

**Group ID:** `V-256908`

### Rule: Automation Controller must use cryptographic mechanisms to protect the integrity of log tools.

**Rule ID:** `SV-256908r961206_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting the integrity of the tools used for logging purposes is a critical step in ensuring the integrity of log data. Log data includes all information (e.g., log records, log settings, and log reports) needed to successfully log information system activity. It is not uncommon for attackers to replace the log tools or inject code into the existing tools for the purpose of providing the capability to hide or erase system activity from the logs. To address this risk, log tools must be cryptographically signed in order to provide the capability to identify when the log tools have been modified, manipulated, or replaced. An example is a checksum hash of the file or files. Automation Controller server log tools must use cryptographic mechanisms to protect the integrity of the tools or allow cryptographic protection mechanisms to be applied to their tools.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As an administrator, log in to each Automation Controller host. Verify the correct Red Hat RPM signing key is available on each host by listing the keys using the following command: rpm -qa gpg-pubkey* Manually inspect against publicly listed keys on https://www.redhat.com. If the keys do not match, this is a finding. Import the key using the following command: rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release Verify the signatures of installed RPMs necessary for Automation Controller: For RPM in $(rpm -qa); do rpm -K --nosignature ${RPM} | grep "NOT OK" && return 1; done ; echo "FAILED" If this outputs "FAILED", this is a finding.

## Group: SRG-APP-000371-AS-000077

**Group ID:** `V-256909`

### Rule: Automation Controller must compare internal application server clocks at least every 24 hours with an authoritative time source.

**Rule ID:** `SV-256909r1015791_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When conducting forensic analysis and investigating system events, it is critical that timestamps accurately reflect the time of application events. If timestamps are not deemed to be accurate, the integrity of the forensic analysis and the associated determinations are at stake. This leaves the organization and the system vulnerable to intrusions. Satisfies: SRG-APP-000371-AS-000077, SRG-APP-000372-AS-000212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a system administrator for each Automation Controller host, ensure the NTP client is configured to synchronize to an organizationally defined NTP server: chronyc sources If the Automation Controller host is not configured to use an organizationally defined NTP server, this is a finding. Ensure the NTP time synchronization is operational: chronyc activity | head -n 1 | grep "200 OK" >/dev/null || echo "FAILED" sudo systemctl is-active chrony > /dev/null|| echo "FAILED" If "FAILED" is displayed, this is a finding.

## Group: SRG-APP-000427-AS-000264

**Group ID:** `V-256910`

### Rule: Automation Controller must only allow the use of DOD PKI-established certificate authorities for verification of the establishment of protected sessions.

**Rule ID:** `SV-256910r961596_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An untrusted source may leave the system vulnerable to issues such as unauthorized access, reduced data integrity, loss of confidentiality, etc. Satisfies: SRG-APP-000427-AS-000264, SRG-APP-000514-AS-000137</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Administrator must check the Automation Controller configuration. Download the latest DOD PKI CA certificate bundle: curl https://dl.dod.cyber.mil/wp-content/uploads/pki-pke/zip/certificates_pkcs7_DOD.zip > /root/certificates_pkcs7_DOD.zip && gunzip /root/certificates_pkcs7_DOD.zip Check the certificate at /etc/tower/tower.cert: openssl verify -verbose -x509_strict -CAfile /root/certificates_pkcs7_DOD.pem -CApath nosuchdir <(cat /etc/tower/tower.cert >><organizationally defined intermediate certificate file in PEM format>>>) If the >><organizationally defined intermediate certificate file in PEM format>>> does not exist, this is a finding. Check the certificate at /etc/tower/tower.key: openssl verify -CAfile /root/certificates_pkcs7_DOD.pem /etc/tower/tower.cert If the >><organizationally defined intermediate certificate file in PEM format>>> does not exist, this is a finding. Check the trusted ca certificate: openssl x509 -in /etc/pki/ca-trust/tls-ca-bundle.pam custom_ca_cert If the >><organizationally defined intermediate certificate file in PEM format>>> does not exist, this is a finding. If the >><organizationally defined intermediate certificate file in PEM format>>> does not exist, this is a finding.

## Group: SRG-APP-000456-AS-000266

**Group ID:** `V-256911`

### Rule: Automation Controller must install security-relevant software updates within the time period directed by an authoritative source (e.g. IAVM, CTOs, DTMs, and STIGs).

**Rule ID:** `SV-256911r961683_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security relevant software updates must be installed within the timeframes directed by an authoritative source in order to maintain the integrity and confidentiality of the system and its organizational assets.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a system administrator for each Automation Controller host inspect the status of the DNF Automatic timer: systemctl status dnf-automatic.timer If "Active: active" is not included in the output, this is a finding. Inspect the configuration of DNF Automatic: grep apply_updates /etc/dnf/automatic.conf If "apply_updates = yes" is not displayed, this is a finding.

