# STIG Benchmark: Jamf Pro v10.x EMM Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: PP-MDM-412003

**Group ID:** `V-241790`

### Rule: When the Jamf Pro EMM server cannot establish a connection to determine the validity of a certificate, the server must not have the option to accept the certificate.

**Rule ID:** `SV-241790r879612_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a Jamf Pro EMM server accepts an unverified certificate, it may be trusting a malicious actor. For example, messages signed with an invalid certificate may contain links to malware, which could lead to the installation or distribution of that malware on DoD information systems, leading to compromise of DoD sensitive information and other attacks. SFR ID: FIA_X509_EXT.2.2</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Validate the Jamf Pro EMM server has been configured to not accept a certificate if the certificate cannot be validated. 1. Open the Jamf Pro EMM console. 2. Open "Settings". 3. Select "User-Initiated Enrollment". 4. Under the General tab, verify "Use a third-party signing certificate" is selected. 5. Verify the name and certificate extension of the DoD p12 certificate is listed. If the Jamf Pro EMM server has been not been configured to not accept a certificate if the certificate cannot be validated, this is a finding.

## Group: PP-MDM-411047

**Group ID:** `V-241791`

### Rule: The Jamf Pro EMM server or platform must be configured to initiate a session lock after a 15-minute period of inactivity.

**Rule ID:** `SV-241791r879513_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user (MDM system administrator) stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their application session prior to vacating the vicinity, applications need to be able to identify when a user's application session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. This is typically at the operating system level and results in a system lock but may be at the application level where the application interface window is secured instead. SFR ID: FMT_SMF.1.1(2) i</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Jamf Pro EMM server or platform is configured to initiate a session lock after a 15-minute period of inactivity. Review the variable in the Jamf Pro web.xml file. On the Jamf Pro host server, open the web.xml file: If using macOS, the web.xml file is located at the following filepath: /Library/JSS/Tomcat/webapps/ROOT/WEB-INF/ If using Windows, the web.xml file is located at the following filepath: C:\Program Files\JSS\Tomcat\webapps\ROOT\WEB-INF\ If using Linux, the web.xml file is located at the following filepath: /usr/local/jss/tomcat/webapps/ROOT/WEB-INF/ Locate the following setting: <session-config> <session-timeout>15</session-timeout> </session-config> Ensure that the code is not commented out. If the code is commented out, remove the comment tags <!-- --> that encase the code. Note: Session timeout is in minutes. If the code is commented out or session-timeout is not configured to "15" minutes or less, this is a finding.

## Group: PP-MDM-411051

**Group ID:** `V-241792`

### Rule: The Jamf Pro EMM server must be configured with an enterprise certificate for signing policies (if function is not automatically implemented during Jamf Pro EMM server install).

**Rule ID:** `SV-241792r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that only authorized certificates are used for key activities such as code signing for system software updates, code signing for integrity verification, and policy signing. Otherwise, there is no assurance that a malicious actor has not inserted itself in the process of packaging the code or policy. For example, messages signed with an invalid certificate may contain links to malware, which could lead to the installation or distribution of that malware on DoD information systems, leading to compromise of DoD sensitive information and other attacks. Therefore, the Jamf Pro EMM server must have the capability to configure the enterprise certificate. SFR ID: FMT_SMF.1.1(2) i, FMT_POL_EXT.1.1</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Jamf Pro is utilizing an External CA for signing communication to mobile devices: 1. Open Jamf Pro server. 2. Open "Settings". 3. Select "PKI Certificates". 4. Select "Management Certificate Template". 5. Select "External CA" tab. 6. Verify the "Use a SCEP-enabled external CA for computer and mobile device enrollment" is enabled. 7. Verify that the Signing Certificate is listed at the bottom of the page. If these settings are confirmed, Jamf Pro is set to use an external CA. If Jamf Pro is not configured to use an External CA for signing communication to mobile devices, this is a finding.

## Group: PP-MDM-411054

**Group ID:** `V-241793`

### Rule: The Jamf Pro EMM server must be configured to transfer Jamf Pro EMM server logs to another server for storage, analysis, and reporting.

Note: Jamf Pro EMM server logs include logs of MDM events and logs transferred to the Jamf Pro EMM server by MDM agents of managed devices.

**Rule ID:** `SV-241793r879731_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit logs enable monitoring of security-relevant events and subsequent forensics when breaches occur. Since the Jamf Pro EMM server has limited capability to store mobile device log files and perform analysis and reporting of mobile device log files, the Jamf Pro EMM server must have the capability to transfer log files to an audit log management server. SFR ID: FMT_SMF.1.1(2) i, FAU_STG_EXT.1.1(1)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Jamf Pro EMM server is enabled to push syslog: 1. Open Jamf Pro server. 2. Open "Settings". 3. Select "Change Management". 4. Verify the settings for Syslog Server (log file transfer to the syslog server). If the Jamf Pro EMM server is not configured to enable syslog, this is a finding.

## Group: PP-MDM-411056

**Group ID:** `V-241794`

### Rule: The Jamf Pro EMM server must be configured to display the required DoD warning banner upon administrator logon.

Note: This requirement is not applicable if the TOE platform is selected in FTA_TAB.1.1 in the Security Target (ST).

**Rule ID:** `SV-241794r879547_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Note: The advisory notice and consent warning message is not required if the general purpose OS or network device displays an advisory notice and consent warning message when the administrator logs on to the general purpose OS or network device prior to accessing the Jamf Pro EMM server or Jamf Pro EMM server platform. Before granting access to the system, the Jamf Pro EMM server/server platform is required to display the DoD-approved system use notification message or banner that provides privacy and security notices consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. This ensures the legal requirements for auditing and monitoring are met. The approved DoD text must be used as specified in the KS referenced in DoDI 8500.01. The non-bracketed text below must be used without any changes as the warning banner. [A. Use this banner for desktops, laptops, and other devices accommodating banners of 1300 characters. The banner shall be implemented as a click-through banner at logon (to the extent permitted by the operating system), meaning it prevents further activity on the information system unless and until the user executes a positive action to manifest agreement by clicking on a box indicating “OK.”] You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. SFR ID: FMT_SMF.1.1(2) d</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Jamf Pro EMM server for customized login page: Go to /path/to/JSS/Tomcat/webapps/ROOT/WEB-INF/frontend folder. Find the login.jsp. Locate new <body> content related to customized text for DoD classification. Verify the DoD warning banner text is correct. If the Jamf Pro EMM server is not configured to display DoD warning banner when the system administrator logs on to the server, this is a finding.

## Group: PP-MDM-411058

**Group ID:** `V-241795`

### Rule: The Jamf Pro EMM server must be configured to have at least one user in the following Administrator roles: Server primary administrator, security configuration administrator, device user group administrator, auditor.

**Rule ID:** `SV-241795r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Having several administrative roles for the Jamf Pro EMM server supports separation of duties. This allows administrator-level privileges to be granted granularly, such as giving application management privileges to one group and security policy privileges to another group. This helps prevent administrators from intentionally or inadvertently altering other settings and configurations they may not understand or approve of, which can weaken overall security and increase the risk of compromise. - Server primary administrator: Responsible for server installation, initial configuration, and maintenance functions. Responsible for the setup and maintenance of security configuration administrator and auditor accounts. Responsible for the maintenance of applications in the MAS. - Security configuration administrator: Responsible for security configuration of the server, defining device user groups, setup and maintenance of device user group administrator accounts, and defining privileges of device user group administrators. - Device user group administrator: Responsible for maintenance of mobile device accounts, including setup, change of account configurations, and account deletion. Responsible for defining which apps user groups or individual users have access to in the MAS. Can only perform administrative functions assigned by the security configuration administrator. - Auditor: Responsible for reviewing and maintaining server and mobile device audit logs. SFR ID: FMT_SMR.1.1(1)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Administrator and Audit level permission groups are configured by default within Jamf Pro server. Verify the additional group permissions by: 1. Open Jamf Pro server. 2. Open "Settings". 3. Select "Jamf Pro User Accounts and Groups". 4. View the necessary information for each group has been created with appropriate privilege sets. Jamf Pro EMM server will have the appropriate group level permissions available for applying to individual user accounts or AD groups. If required administrator roles have not been set up on the server, this is a finding.

## Group: PP-MDM-414002

**Group ID:** `V-241796`

### Rule: The Jamf Pro EMM server must be configured to leverage the MDM platform user accounts and groups for Jamf Pro EMM server user identification and CAC authentication.

**Rule ID:** `SV-241796r879522_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A comprehensive account management process that includes automation helps to ensure the accounts designated as requiring attention are consistently and promptly addressed. If an attacker compromises an account, the entire Jamf Pro EMM server infrastructure is at risk. Providing automated support functions for the management of accounts will ensure only active accounts will be granted access with the proper authorization levels. These objectives are best achieved by configuring the Jamf Pro EMM server to leverage an enterprise authentication mechanism (e.g., Microsoft Active Directory Kerberos). SFR ID: FIA</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the site ISSM. Determine if the site has connected Jamf Pro EMM to an Authentication Gateway Service (AGS) which connects to the DoD Identity Access Management (IdAM) environment that uses CAC authentication. - If YES, verify the AGS implementation has been reviewed using the Application Layer Gateway SRG. Verify the Jamf Pro EMM server is configured to connect to the AGS: 1. Go to the server console. 2. Open "Settings". 3. Select "SSO" (Single Sign-on). 4. Verify Single Sign-on Authentication is enabled and connection to the AGS using SAML-based protocol is set up. - If NO, verify strong password controls for the administrator local accounts are in place. (Verified by JAMF-10-100700 to JAMF-10-100820.) If Jamf Pro EMM is not connected Jamf Pro EMM to an Authentication Gateway Service (AGS) which connects to your DoD Identity Access Management (IdAM) environment that utilizes CAC authentication or has not been configured to use strong password controls for the administrator local accounts, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-241797`

### Rule: Authentication of Jamf Pro EMM server accounts must be configured so they are implemented either via an Authentication Gateway Service (AGS) which connects to the site DoD Identity Access Management (IdAM) environment that utilizes CAC authentication or via strong password controls for the administrator local accounts.

**Rule ID:** `SV-241797r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A comprehensive account management process that includes automation helps to ensure the accounts designated as requiring attention are consistently and promptly addressed. If an attacker compromises an account, the entire Jamf Pro EMM server infrastructure is at risk. Providing automated support functions for the management of accounts will ensure only active accounts will be granted access with the proper authorization levels. These objectives are best achieved by configuring the Jamf Pro EMM server to leverage an enterprise authentication mechanism (e.g., Microsoft Active Directory Kerberos). SFR ID: FIA</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the site ISSM. Determine if the site has connected Jamf Pro EMM to an Authentication Gateway Service (AGS) which connects to the DoD Identity Access Management (IdAM) environment that uses CAC authentication. - If YES, verify the AGS implementation has been reviewed using the Application Layer Gateway SRG. Verify the Jamf Pro EMM server is configured to connect to the AGS: 1. Go to the server console. 2. Open "Settings". 3. Select "SSO" (Single Sign-on). 4. Verify Single Sign-on Authentication is enabled and connection to the AGS using SAML-based protocol is set up. - If NO, verify strong password controls for the administrator local accounts are in place. (Verified by JAMF-10-100700 to JAMF-10-100820.) If Jamf Pro EMM is not connected to an Authentication Gateway Service (AGS) which connects to the DoD Identity Access Management (IdAM) environment that uses CAC authentication or has not been configured to use strong password controls for the administrator local accounts, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-241798`

### Rule: Jamf Pro EMM must be maintained at a supported version.

**Rule ID:** `SV-241798r879887_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The MDM/EMM vendor maintains specific product versions for a specific period of time. MDM/EMM server versions no longer supported by the vendor will not receive security updates for new vulnerabilities which leaves them subject to exploitation. SFR ID: FPT_TUD_EXT.1.1, FPT_TUD_EXT.1.2</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the installed version of Jamf Pro EMM is currently supported. On the Jamf Pro console do the following to determine the version number of the server: 1. Log in to the console. 2. View the version number listed in the upper left corner. List of current supported versions: v10.18 (End of Support Date: TBD v10.17 (TBD) v10.16 (TBD) v10.15 (TBD) v10.14 (TBD) v10.13.1 (TBD) If the displayed Jamf Pro server version is not currently supported or is not a newer version than on the list above, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-241799`

### Rule: The default mysql_secure_installation must be installed.

**Rule ID:** `SV-241799r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The mysql_secure_installation configuration of MySQL adds several important configuration settings that block several attack vectors. The My SQL application could be exploited by an adversary without mysql_secure_installation. SFR ID: FMT_SMF.1(2)b. / CM-7(1)(b) Satisfies: SRG-APP-000383</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the mysql_secure_installation has been installed on the Jamf host server. 1. Log in to MySQL. Execute the "show databases;" command. - Verify that the database named "Test" is not shown in output of the command. 2. Verify the root account has a string representing the password and not a blank value. - select * from mysql.user; 3. Verify the anonymous users have been removed and verify the user field contains a user name. - select * from mysql.user; All three steps must be correct to indicate mysql_secure_installation has been executed. If the mysql_secure_installation has not been installed on the Jamf host server, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-241800`

### Rule: A unique database name and a unique MySQL user with a secure password must be created for use in Jamf Pro EMM.

**Rule ID:** `SV-241800r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the default MySQL database name and password are not changed an adversary could gain unauthorized access to the application which could lead to the compromise of sensitive DoD data. SFR ID: FMT_SMF.1(2)b. / IA-5(1)(c) Satisfies: SRG-APP-000171</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify a unique database name and a unique MySQL user with a secure password have been created for use in Jamf Pro EMM. 1. Execute the show databases command. - Ensure at least one database name other than the default databases exits. The default databases are: infomation_schema mysql performance_schema sys 2. Verify there is a unique MySQL user. - In MySQL, run select * mysql.user; - Look for a user that is not Root or one of the other MySQL service accounts. Both of these steps must be correct. If a unique database name and a unique MySQL user with a secure password have not been created, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-241801`

### Rule: Separate MySQL user accounts with limited privileges must be created within Jamf Pro EMM.

**Rule ID:** `SV-241801r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If separate MySQL accounts with limited privileges are not created an adversary could gain unauthorized access to the application or gain access unauthorized features which could lead to the compromise of sensitive DoD data. SFR ID: FMT_SMF.1(2)b. / CM-6 b Satisfies: SRG-APP-000516</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify separate MySQL user accounts with limited privileges have been created within Jamf Pro EMM. In MySQL, execute the following command: show grants for username@localhost; Verify the privileges match what is in the Jamf Knowledge Base article. If separate MySQL user accounts with limited privileges have not been created within Jamf Pro EMM, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-241802`

### Rule: MySQL database backups must be scheduled in Jamf Pro EMM.

**Rule ID:** `SV-241802r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Database backups are a recognized best practice to protect against key data loss and possible adverse impacts to the mission of the organization. SFR ID: FMT_SMF.1(2)b. / CM-6 b Satisfies: SRG-APP-000516</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify MySQL of database backups have been scheduled in Jamf Pro EMM. 1. Open "Jamf Server Tools". 2. Click "Scheduled Backups" in the sidebar. 3. Verify backups are scheduled. If MySQL of database backups have not been scheduled in Jamf Pro EMM, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-241803`

### Rule: The MySQL DatabasePassword key must be removed or set to a blank value in the database configuration file in Jamf Pro EMM.

**Rule ID:** `SV-241803r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the database password is not removed or set to a blank value in the configuration file, the user is not forced to enter the password, which would allow an adversary to access to access the database. SFR ID: FMT_SMF.1(2)b. / CM-5(10) Satisfies: SRG-APP-000380</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the MySQL <DatabasePassword> key has been removed or set to a blank value in Jamf Pro EMM. 1. On the Jamf Pro server, navigate to the JSS/Tomcat/webapps/ROOT/WEB-INF/xml. 2. Find the "Database.xml" file and open it in a text editor. 3. Find the <DatabasePassword>. 4. Verify that there is no password. If the MySQL <DatabasePassword> key has not been removed or not set to a blank value, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-241804`

### Rule: The Jamf Pro EMM local accounts password must be configured with length of 15 characters.

**Rule ID:** `SV-241804r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password. SFR ID: FMT_SMF.1(2)b. / IA-5 (1) (a) Satisfies: SRG-APP-000164</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the length of the local accounts password, do the following: 1. Open the Jamf Pro EMM console. 2. Click "Settings". 3. Click "System Settings". 4. Click "Jamf Pro System User Accounts & Groups". 5. Click "Password Policy". 6. Verify "Minimum Password Length" is set to "15". If the "Minimum Password Length" is not set to "15", this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-241805`

### Rule: The Jamf Pro EMM local accounts must be configured with at least one lowercase character.

**Rule ID:** `SV-241805r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. SFR ID: FMT_SMF.1(2)b. / IA-5 (1) (a) Satisfies: SRG-APP-000167</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the "Require lowercase character" of the local accounts password is selected, do the following: 1. Open the Jamf Pro EMM console. 2. Click "Settings". 3. Click "System Settings". 4. Click "Jamf Pro System User Accounts & Groups". 5. Click "Password Policy". 6. Verify "Require lowercase character" is selected. If "Require lowercase character" is not selected, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-241806`

### Rule: The Jamf Pro EMM local accounts must be configured with at least one uppercase character.

**Rule ID:** `SV-241806r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. SFR ID: FMT_SMF.1(2)b. / IA-5 (1) (a) Satisfies: SRG-APP-000166</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the "Require uppercase character" of the local accounts password is selected, do the following: 1. Open the Jamf Pro EMM console. 2. Click "Settings". 3. Click "System Settings". 4. Click "Jamf Pro System User Accounts & Groups". 5. Click "Password Policy". 6. Verify "Require uppercase character" is selected. If "Require uppercase character" is not selected, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-241807`

### Rule: The Jamf Pro EMM local accounts must be configured with at least one number.

**Rule ID:** `SV-241807r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. SFR ID: FMT_SMF.1(2)b. / IA-5 (1) (a) Satisfies: SRG-APP-000168</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the "Require number" of the local accounts password is selected, do the following: 1. Open the Jamf Pro EMM console. 2. Click "Settings". 3. Click "System Settings". 4. Click "Jamf Pro System User Accounts & Groups". 5. Click "Password Policy". 6. Verify "Require number" is selected. If "Require number" is not selected, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-241808`

### Rule: The Jamf Pro EMM local accounts must be configured with at least one special character.

**Rule ID:** `SV-241808r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor in determining how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Special characters are those characters that are not alphanumeric. Examples include: ~ ! @ # $ % ^ *. SFR ID: FMT_SMF.1(2)b. / IA-5 (1) (a) Satisfies: SRG-APP-000169</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the "Require special character" of the local accounts password is selected, do the following: 1. Open the Jamf Pro EMM console. 2. Click "Settings". 3. Click "System Settings". 4. Click "Jamf Pro System User Accounts & Groups". 5. Click "Password Policy". 6. Verify "Require special character" is selected. If "Require special character" is not selected, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-241809`

### Rule: The Jamf Pro EMM local accounts must be configured with password minimum lifetime of 24 hours.

**Rule ID:** `SV-241809r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps prevent repeated password changes to defeat the password reuse or history enforcement requirement. Restricting this setting limits the user's ability to change their password. Passwords need to be changed at specific policy based intervals; however, if the application allows the user to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse. SFR ID: FMT_SMF.1(2)b. / IA-5 (1) (d) Satisfies: SRG-APP-000173</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the "Minimum password Age" of "1" day for the local accounts password is set, do the following: 1. Open the Jamf Pro EMM console. 2. Click "Settings". 3. Click "System Settings". 4. Click "Jamf Pro System User Accounts & Groups". 5. Click "Password Policy". 6. Verify "Minimum Password Age" is set to "1" day. If the "Minimum Password Age" is not set to "1" day, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-241810`

### Rule: The Jamf Pro EMM local accounts must be configured with password maximum lifetime of 3 months.

**Rule ID:** `SV-241810r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed at specific intervals. One method of minimizing this risk is to use complex passwords and periodically change them. If the application does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the system and/or application passwords could be compromised. This requirement does not include emergency administration accounts which are meant for access to the application in case of failure. These accounts are not required to have maximum password lifetime restrictions. SFR ID: FMT_SMF.1(2)b. / IA-5 (1) (d) Satisfies: SRG-APP-000174</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the "password maximum lifetime" of "3" months for the local account's password is set, do the following: 1. Open the Jamf Pro EMM console. 2. Click "Settings". 3. Click "System Settings". 4. Click "Jamf Pro System User Accounts & Groups". 5. Click "Password Policy". 6. Verify "password maximum lifetime" of "3" months. If the "password maximum lifetime" for local account's password is not set to "3" months, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-241811`

### Rule: The Jamf Pro EMM local accounts must prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-241811r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. To meet password policy requirements, passwords need to be changed at specific policy-based intervals. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements. SFR ID: FMT_SMF.1(2)b. / IA-5 (1) (e) Satisfies: SRG-APP-000165</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the local accounts "Password History" is set to a minimum of "5" generations, do the following: 1. Open the Jamf Pro EMM console. 2. Click "Settings". 3. Click "System Settings". 4. Click "Jamf Pro System User Accounts & Groups". 5. Click "Password Policy". 6. Verify "Password History" to "5" or more. If "Password History" is not set to "5" or more, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-241812`

### Rule: The Jamf Pro EMM must automatically disable accounts after a 35 day period of account inactivity (local accounts).

**Rule ID:** `SV-241812r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Attackers that are able to exploit an inactive account can potentially obtain and maintain undetected access to an application. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. Applications need to track periods of user inactivity and disable accounts after 35 days of inactivity. Such a process greatly reduces the risk that accounts will be hijacked, leading to a data compromise. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality. This policy does not apply to either emergency accounts or infrequently used accounts. Infrequently used accounts are local login administrator accounts used by system administrators when network or normal logon/access is not available. Emergency accounts are administrator accounts created in response to crisis situations. SFR ID: FMT_SMF.1(2)b. / AC-2(3) Satisfies: SRG-APP-000025</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the site Jamf Pro EMM system administrator. Confirm a script is used to periodically check when each local account was last accessed by the user and disable the account if there is a 35-day or more period of account inactivity. If a script is not used to periodically check when each local account was last accessed by the user and disable the account or if there is a 35-day or more period of account inactivity, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-241813`

### Rule: The Jamf Pro EMM must enforce the limit of three consecutive invalid logon attempts by a user.

**Rule ID:** `SV-241813r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. Limits are imposed by locking the account. SFR ID: FMT_SMF.1(2)b. / IA-7-a Satisfies: SRG-APP-000065</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the Jamf Pro EMM enforces a limit of three consecutive invalid logon attempts by a user, do the following: 1. Log in to the Jamf Pro EMM console. 2. Open "Settings". 3. Select "Jamf Pro User Accounts & Groups". 4. Select "Password Policy" in the upper right corner. 5. Verify that under "Account Lockout" the number of failed attempts before lockout is set to "3" or less. If the Jamf Pro EMM does not limit the number of consecutive invalid logon attempts by a user to "3" or less, this is a finding.

## Group: PP-MDM-431004

**Group ID:** `V-241814`

### Rule: The Jamf Pro EMM server platform must be protected by a DoD-approved firewall.

**Rule ID:** `SV-241814r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Most information systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Unneeded services and processes provide additional threat vectors and avenues of attack to the information system. The MDM server is a critical component of the mobility architecture and must be configured to enable only those ports, protocols, and services (PPS) necessary to support functionality. All others must be expressly disabled or removed. A DoD-approved firewall implements the required network restrictions. A host-based firewall is appropriate where the MDM server runs on a standalone platform. Network firewalls or other architectures may be preferred where the MDM server runs in a cloud or virtualized solution. SFR ID: FMT_SMF.1.1(2) b / CM-7b Satisfies: SRG-APP-000142</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Jamf Pro EMM server platform configuration to determine whether a DoD-approved firewall is installed or if the platform operating system provides a firewall service that can restrict both inbound and outbound traffic by TCP/UDP port and IP address. If there is not a host-based firewall present on the Jamf Pro EMM server platform, this is a finding.

## Group: PP-MDM-431005

**Group ID:** `V-241815`

### Rule: The firewall protecting the Jamf Pro EMM server platform must be configured to restrict all network traffic to and from all addresses with the exception of ports, protocols, and IP address ranges required to support Jamf Pro EMM server and platform functions.

**Rule ID:** `SV-241815r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Most information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations. Since MDM server is a critical component of the mobility architecture and must be configured to enable only those ports, protocols, and services (PPS) necessary to support functionality, all others must be expressly disabled or removed. A firewall installed on the MDM server provides a protection mechanism to ensure unwanted service requests do not reach the MDM server and outbound traffic is limited to only MDM server functionality. SFR ID: FMT_SMF.1.1(2) b / CM-7b Satisfies: SRG-APP-000142</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Jamf Pro EMM server administrator for a list of ports, protocols, and IP address ranges necessary to support Jamf Pro EMM server and platform functionality. A list can usually be found in the STIG Supplemental document or Jamf Pro EMM product documentation. Compare the list against the configuration of the firewall and identify discrepancies. If the host-based firewall is not configured to support only those ports, protocols, and IP address ranges necessary for operation, this is a finding.

## Group: PP-MDM-431006

**Group ID:** `V-241816`

### Rule: The firewall protecting the Jamf Pro EMM server platform must be configured so that only DoD-approved ports, protocols, and services are enabled. (See the DoD Ports, Protocols, Services Management [PPSM] Category Assurance Levels [CAL] list for DoD-approved ports, protocols, and services).

**Rule ID:** `SV-241816r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All ports, protocols, and services used on DoD networks must be approved and registered via the DoD PPSM process. This is to ensure that a risk assessment has been completed before a new port, protocol, or service is configured on a DoD network and has been approved by proper DoD authorities. Otherwise, the new port, protocol, or service could cause a vulnerability to the DoD network, which could be exploited by an adversary. SFR ID: FMT_SMF.1.1(2) b / CM-7b Satisfies: SRG-APP-000142</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Jamf Pro EMM server administrator for a list of ports, protocols, and services that have been configured on the host-based firewall of the Jamf Pro EMM server or generate the list by inspecting the firewall. Verify all allowed ports, protocols, and services are included on the DoD PPSM CAL list. If any allowed ports, protocols, and services on the Jamf Pro EMM server host-based firewall are not included on the DoD PPSM CAL list, this is a finding.

## Group: PP-MDM-431007

**Group ID:** `V-241817`

### Rule: All Jamf Pro EMM server local accounts created during application installation and configuration must be disabled.

**Rule ID:** `SV-241817r879589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A comprehensive account management process that includes automation helps to ensure the accounts designated as requiring attention are consistently and promptly addressed. If an attacker compromises an account, the entire Jamf Pro EMM server infrastructure is at risk. Providing automated support functions for the management of accounts will ensure only active accounts will be granted access with the proper authorization levels. These objectives are best achieved by configuring the Jamf Pro EMM server to leverage an enterprise authentication mechanism (e.g., Microsoft Active Directory Kerberos). SFR ID: FMT_SMF.1.1(2) b / IA-5(1)(a) Satisfies: SRG-APP-000148</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all local accounts on the Jamf Pro EMM server have been disabled. Note: the server service account is not disabled. 1. Log in to the Jamf pro EMM console. 2. Open "Settings". 3. Verify all Jamf Pro User Accounts & Groups have been disabled. If all local accounts on the Jamf Pro EMM server have not been disabled, this is a finding.

## Group: PP-MDM-431009

**Group ID:** `V-241818`

### Rule: The Jamf Pro EMM server must connect to [Authentication Gateway Service (AGS)] with an authenticated and secure (encrypted) connection to protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-241818r916416_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised since unprotected communications can be intercepted and either read or altered. This requirement applies only to those applications that are either distributed or can allow access to data non-locally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, applications need to leverage transmission protection mechanisms, such as TLS, TLS VPNs, or IPsec. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. SFR ID: FMT_SMF.1.1(2) b / SC-8, SC-8 (1), SC-8 (2) Satisfies: SRG-APP-000439, SRG-APP-000440</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Talk to the site Administrator to confirm the AGS has been configured to connect to the Jamf Pro EMM server using the TLS connection or confirm during a review of the AGS. If the AGS has not been configured to connect to the Jamf Pro EMM server using a TLS connection, this is a finding.

## Group: PP-MDM-411046

**Group ID:** `V-257255`

### Rule: The Jamf Pro EMM server must configure the MDM Agent/platform to enable the DOD required device enrollment restrictions allowed for enrollment [specific device model].

**Rule ID:** `SV-257255r916639_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Good configuration management of a mobile device is a key capability for maintaining the mobile device’s security baseline. Restricting network access to only authorized devices is a key configuration management attribute. Device type is a key way to specify mobile devices that can be adequately secured. SFR ID: FMT_SMF.1.1(2) b, FIA_ENR_EXT.1.2</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify device enrollment restrictions are set up to limit enrollment by iOS device. 1. Open Jamf Pro admin interface. 2. Select "Devices". 3. Select "Smart Device Groups". 4. Select desired device group. 5. Verify approved model numbers are listed. If device enrollment restrictions are not set up, this is a finding.

