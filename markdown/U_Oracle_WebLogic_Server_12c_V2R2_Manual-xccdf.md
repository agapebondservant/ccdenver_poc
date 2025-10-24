# STIG Benchmark: Oracle WebLogic Server 12c Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000014-AS-000009

**Group ID:** `V-235928`

### Rule: Oracle WebLogic must utilize cryptography to protect the confidentiality of remote access management sessions.

**Rule ID:** `SV-235928r960759_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote management access is accomplished by leveraging common communication protocols and establishing a remote connection to the application server via a network for the purposes of managing the application server. If cryptography is not used, then the session data traversing the remote connection could be intercepted and compromised. Types of management interfaces utilized by an application server include web-based HTTPS interfaces as well as command line-based management interfaces. All application server management interfaces must utilize cryptographic encryption.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Environment' -> 'Servers' 3. From the list of servers, select one which needs check for SSL configuration verification 4. From 'Configuration' tab -> 'General' tab, ensure 'Listen Port Enabled' checkbox is deselected 5. Ensure 'SSL Listen Port Enabled' checkbox is selected and a valid port number is in 'SSL Listen Port' field, e.g., 7002 6 Repeat steps 3-5 for all servers requiring SSL configuration checking If 'Listen Port Enabled' is selected, this is a finding. If 'SSL Listen Port Enabled' is not selected, this is a finding.

## Group: SRG-APP-000015-AS-000010

**Group ID:** `V-235929`

### Rule: Oracle WebLogic must use cryptography to protect the integrity of the remote access session.

**Rule ID:** `SV-235929r960762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption is critical for protection of remote access sessions. If encryption is not being used for integrity, malicious users may gain the ability to modify the application server configuration. The use of cryptography for ensuring integrity of remote access sessions mitigates that risk. Application servers utilize a web management interface and scripted commands when allowing remote access. Web access requires the use of SSL 3.0 or TLS 1.0 and scripted access requires using ssh or some other form of approved cryptography. Application servers must have a capability to enable a secure remote admin capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Environment' -> 'Servers' 3. From the list of servers, select one which needs check for SSL configuration verification 4. From 'Configuration' tab -> 'General' tab, ensure 'Listen Port Enabled' checkbox is deselected 5. Ensure 'SSL Listen Port Enabled' checkbox is selected and a valid port number is in 'SSL Listen Port' field, e.g., 7002 6. Repeat steps 3-5 for all servers requiring SSL configuration checking If 'Listen Port Enabled' is selected, this is a finding. If 'SSL Listen Port Enabled' is not selected, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-235930`

### Rule: Oracle WebLogic must employ automated mechanisms to facilitate the monitoring and control of remote access methods.

**Rule ID:** `SV-235930r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote network access is accomplished by leveraging common communication protocols and establishing a remote connection. Application servers provide remote management access and need to provide the ability to facilitate the monitoring and control of remote user sessions. This includes the capability to directly trigger actions based on user activity or pass information to a separate application or entity that can then perform automated tasks based on the information. Examples of automated mechanisms include but are not limited to: automated monitoring of log activity associated with remote access or process monitoring tools. The application server must employ mechanisms that allow for monitoring and control of web-based and command line-based administrative remote sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'JDBC Data Sources' 3. From the list of data sources, select the one named 'opss-audit-DBDS', which connects to the IAU_APPEND schema of the audit database. Note the value in the 'JNDI name' field. 4. To verify, select 'Configuration' tab -> 'Connection Pool' tab 5. Ensure the 'URL' and 'Properties' fields contain the correct connection values for the IAU_APPEND schema 6. To test, select 'Monitoring' tab, select a server from the list and click 'Test Data Source'. Ensure test was successful. Repeat for each server in the list. 7. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Security' -> 'Security Provider Configuration' 8. Beneath 'Audit Service' section, click 'Configure' button 9. Ensure 'Data Source JNDI Name' value matches the JNDI Name value from data source in step 3 above 10. Repeat steps 2-6 for data source named 'wls-wldf-storeDS' and WLS schema If the data is not being stored for access by an external monitoring tool, this is a finding.

## Group: SRG-APP-000016-AS-000013

**Group ID:** `V-235931`

### Rule: Oracle WebLogic must ensure remote sessions for accessing security functions and security-relevant information are audited.

**Rule ID:** `SV-235931r960765_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing must be utilized in order to track system activity, assist in diagnosing system issues and provide evidence needed for forensic investigations post security incident. Remote access by administrators requires that the admin activity be audited. Application servers provide a web- and command line-based remote management capability for managing the application server. Application servers must ensure that all actions related to administrative functionality such as application server configuration are logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Security' -> 'Audit Policy' 3. Select 'Oracle Platform Security Services' from the 'Audit Component Name' dropdown 4. Beneath 'Audit Policy Settings' section, ensure that the value 'Custom' is set in the 'Audit Level' dropdown 5. Beneath 'Audit Policy Settings' section, ensure that every checkbox is selected under the 'Select For Audit' column of the policy category table If all auditable events for the 'Oracle Platform Security Services' audit component are not selected, then this is a finding.

## Group: SRG-APP-000142-AS-000014

**Group ID:** `V-235932`

### Rule: Oracle WebLogic must support the capability to disable network protocols deemed by the organization to be non-secure except for explicitly identified components in support of specific operational requirements.

**Rule ID:** `SV-235932r1043177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some networking protocols may not meet organizational security requirements to protect data and components. Application servers natively host a number of various features such as management interfaces, httpd servers, and message queues. These features all run on TCPIP ports. This creates the potential that the vendor may choose to utilize port numbers or network services that have been deemed unusable by the organization. The application server must have the capability to both reconfigure and disable the assigned ports without adversely impacting application server operation capabilities. For a list of approved ports and protocols, reference the DoD ports and protocols web site at https://cyber.mil/ppsm.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Monitoring' -> 'Port Usage' 3. In the results table, ensure values in the 'Port in Use' column match approved ports 4. In the results table, ensure values in the 'Protocol' column match approved protocols If ports or protocols are in use that the organization deems nonsecure, this is a finding.

## Group: SRG-APP-000509-AS-000234

**Group ID:** `V-235933`

### Rule: Oracle WebLogic must automatically audit account creation.

**Rule ID:** `SV-235933r961842_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application servers require user accounts for server management purposes, and if the creation of new accounts is not logged, there is limited or no capability to track or alarm on account creation. This could result in the circumvention of the normal account creation process and introduce a persistent threat. Therefore, an audit trail that documents the creation of application user accounts must exist. An application server could possibly provide the capability to utilize either a local or centralized user registry. A centralized, enterprise user registry such as AD or LDAP is more likely to already contain provisions for automated account management, whereas a localized user registry will rely upon either the underlying OS or built-in application server user management capabilities. Either way, application servers must create a log entry when accounts are created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Security Realms' 3. Select realm to configure (default is 'myrealm') 4. Select 'Providers' tab -> 'Auditing' tab 5. Ensure the list of 'Auditing Providers' contains at least one Auditing Provider 6. From 'Domain Structure', select the top-level domain link 7. Click 'Advanced' near the bottom of the page 8. Ensure 'Configuration Audit Type' is set to 'Change Log and Audit' If the 'Configuration Audit Type' is not set to 'Change Log and Audit', this is a finding.

## Group: SRG-APP-000509-AS-000234

**Group ID:** `V-235934`

### Rule: Oracle WebLogic must automatically audit account modification.

**Rule ID:** `SV-235934r961842_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, they often attempt to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply modify an existing account. Application servers have the capability to contain user information in a local user store, or they can leverage a centralized authentication mechanism like LDAP. Either way, the mechanism used by the application server must automatically log when user accounts are modified.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Security Realms' 3. Select realm to configure (default is 'myrealm') 4. Select 'Providers' tab -> 'Auditing' tab 5. Ensure the list of 'Auditing Providers' contains at least one Auditing Provider 6. From 'Domain Structure', select the top-level domain link 7. Click 'Advanced' near the bottom of the page 8. Ensure 'Configuration Audit Type' is set to 'Change Log and Audit' If the 'Configuration Audit Type' is not set to 'Change Log and Audit', this is a finding.

## Group: SRG-APP-000504-AS-000229

**Group ID:** `V-235935`

### Rule: Oracle WebLogic must provide access logging that ensures users who are granted a privileged role (or roles) have their privileged activity logged.

**Rule ID:** `SV-235935r961827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to be able to provide a forensic history of activity, the application server must ensure users who are granted a privileged role or those who utilize a separate distinct account when accessing privileged functions or data have their actions logged. If privileged activity is not logged, no forensic logs can be used to establish accountability for privileged actions that occur on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Security' -> 'Audit Policy' 3. Select 'Oracle Platform Security Services' from the 'Audit Component Name' dropdown 4. Beneath 'Audit Policy Settings' section, ensure that the comma-delimited list of privileged users (e.g., WebLogic, etc.) is set in the 'Users to Always Audit' field If all privileged users are not listed in the 'Users to Always Audit' field, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-235936`

### Rule: Oracle WebLogic must limit the number of failed login attempts to an organization-defined number of consecutive invalid attempts that occur within an organization-defined time period.

**Rule ID:** `SV-235936r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Anytime an authentication method is exposed so as to allow for the login to an application, there is a risk that attempts will be made to obtain unauthorized access. By limiting the number of failed login attempts that occur within a particular time period, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account once the number of failed attempts has been exceeded.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Security Realms' 3. Select realm to configure (default is 'myrealm') 4. Select 'Configuration' tab -> 'User Lockout' tab 5. Ensure the following field values are set: 'Lockout Threshold' = 3 'Lockout Duration' = 15 'Lockout Reset Duration' = 15 If 'Lockout Threshold' is not set to 3 or 'Lockout Duration' is not set to 15 or 'Lockout Reset Duration' is not set to 15, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-235937`

### Rule: Oracle WebLogic must enforce the organization-defined time period during which the limit of consecutive invalid access attempts by a user is counted.

**Rule ID:** `SV-235937r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via automated user password guessing, otherwise known as brute-forcing, is reduced. Best practice requires a time period be applied in which the number of failed attempts is counted (Example: 5 failed attempts within 5 minutes). Limits are imposed by locking the account. Application servers provide a management capability that allows a user to login via a web interface or a command shell. Application servers also utilize either a local user store or a centralized user store such as an LDAP server. As such, the authentication method employed by the application server must be able to limit the number of consecutive invalid access attempts within the specified time period regardless of access method or user store utilized.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Security Realms' 3. Select realm to configure (default is 'myrealm') 4. Select 'Configuration' tab -> 'User Lockout' tab 5. Ensure the following field values are set: 'Lockout Threshold' = 3 'Lockout Duration' = 15 'Lockout Reset Duration' = 15 If 'Lockout Threshold' is not set to 3 or 'Lockout Duration' is not set to 15 or 'Lockout Reset Duration' is not set to 15, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-235938`

### Rule: Oracle WebLogic must automatically lock accounts when the maximum number of unsuccessful login attempts is exceeded for an organization-defined time period or until the account is unlocked by an administrator.

**Rule ID:** `SV-235938r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Anytime an authentication method is exposed so as to allow for the utilization of an application interface, there is a risk that attempts will be made to obtain unauthorized access. By locking the account when the pre-defined number of failed login attempts has been exceeded, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Specifying a time period in which the account is to remain locked serves to obstruct the operation of automated password guessing tools while allowing a valid user to reinitiate login attempts after the expiration of the time period without administrative assistance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Security Realms' 3. Select realm to configure (default is 'myrealm') 4. Select 'Configuration' tab -> 'User Lockout' tab 5. Ensure the following field values are set: 'Lockout Threshold' = 3 'Lockout Duration' = 15 'Lockout Reset Duration' = 15 If 'Lockout Threshold' is not set to 3 or 'Lockout Duration' is not set to 15 or 'Lockout Reset Duration' is not set to 15, this is a finding.

## Group: SRG-APP-000080-AS-000045

**Group ID:** `V-235939`

### Rule: Oracle WebLogic must protect against an individual falsely denying having performed a particular action.

**Rule ID:** `SV-235939r960864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-repudiation of actions taken is required in order to maintain application integrity. Examples of particular actions taken by individuals include creating information, sending a message, approving information (e.g., indicating concurrence or signing a contract), and receiving a message. Non-repudiation protects individuals against later claims by an author of not having authored a particular document, a sender of not having transmitted a message, a receiver of not having received a message, or a signatory of not having signed a document. Typical application server actions requiring non-repudiation will be related to application deployment among developer/users and administrative actions taken by admin personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Security' -> 'Audit Policy' 3. Select 'Oracle Platform Security Services' from the 'Audit Component Name' dropdown 4. Beneath 'Audit Policy Settings' section, ensure that the value 'Custom' is set in the 'Audit Level' dropdown 5. Beneath 'Audit Policy Settings' section, ensure that every checkbox is selected under the 'Select For Audit' column of the policy category table 6. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Logs' -> 'View Log Messages' 7. Within the 'Search' panel, expand 'Selected Targets' 8. Click 'Target Log Files' icon for any of the managed server or 'Application Deployment' type targets (not AdminServer) 9. From the list of log files, select '<server-name>.log', 'access.log' or '<server-name>-diagnostic.log' and click 'View Log File' button 10. User or process associated with audit event will be displayed in 'User' column 11. If 'User' column does not appear, use 'View' button -> 'Columns' list to add 'User' field, or select individual message in log message table and view the message detail (beneath the table) 12. Repeat steps 6-11 for each target If the user is not part of the audit events, this is a finding.

## Group: SRG-APP-000086-AS-000048

**Group ID:** `V-235940`

### Rule: Oracle WebLogic must compile audit records from multiple components within the system into a system-wide (logical or physical) audit trail that is time-correlated to within an organization-defined level of tolerance.

**Rule ID:** `SV-235940r960873_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Audit generation and audit records can be generated from various components within the application server. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records (e.g., auditable events, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked). The events occurring must be time-correlated in order to conduct accurate forensic analysis. In addition, the correlation must meet a certain tolerance criteria. For instance, DoD may define that the time stamps of different audited events must not differ by any amount greater than ten seconds. It is also acceptable for the application server to utilize an external auditing tool that provides this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'JDBC Data Sources' 3. From the list of data sources, select the one named 'opss-audit-DBDS', which connects to the IAU_APPEND schema of the audit database. Note the value in the 'JNDI name' field. 4. To verify, select 'Configuration' tab -> 'Connection Pool' tab 5. Ensure the 'URL' and 'Properties' fields contain the correct connection values for the IAU_APPEND schema 6. To test, select 'Monitoring' tab, select a server from the list and click 'Test Data Source'. Ensure test was successful. Repeat for each server in the list 7. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Security' -> 'Security Provider Configuration' 8. Beneath 'Audit Service' section, click 'Configure' button 9. Ensure 'Data Source JNDI Name' value matches the JNDI Name value from data source in step 3 above 10. Repeat steps 2-6 for data source named 'wls-wldf-storeDS' and WLS schema 11. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Logs' -> 'View Log Messages' 12. Within the 'Search' panel, expand 'Selected Targets' 13. Use the list of targets to navigate and drill into the log files across the domain If any of the targets are not being logged, this is a finding.

## Group: SRG-APP-000091-AS-000052

**Group ID:** `V-235941`

### Rule: Oracle WebLogic must generate audit records for the DoD-selected list of auditable events.

**Rule ID:** `SV-235941r960885_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Audit records can be generated from various components within the application server. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records (e.g., auditable events, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked). The DoD-required auditable events are events that assist in intrusion detection and forensic analysis. Failure to capture them increases the likelihood that an adversary can breach the system without detection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Logs' -> 'View Log Messages' 3. Within the 'Search' panel, expand 'Selected Targets' 4. Click 'Target Log Files' icon for 'AdminServer' target 5. From the list of log files, select 'access.log' and click 'View Log File' button 6. All HTTPD, JVM, AS process event and other logging of the AdminServer will be displayed 7. Repeat for each managed server If there are no events being logged for any of the managed servers or the AdminServer, this is a finding.

## Group: SRG-APP-000095-AS-000056

**Group ID:** `V-235942`

### Rule: Oracle WebLogic must produce process events and severity levels to establish what type of HTTPD-related events and severity levels occurred.

**Rule ID:** `SV-235942r960891_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Audit record content that may be necessary to satisfy the requirement of this control includes time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Application servers must log all relevant log data that pertains to application server functionality. Examples of relevant data include, but are not limited to Java Virtual Machine (JVM) activity, HTTPD/Web server activity and application server-related system process activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Logs' -> 'View Log Messages' 3. Within the 'Search' panel, expand 'Selected Targets' 4. Click 'Target Log Files' icon for 'AdminServer' target 5. From the list of log files, select 'access.log' and click 'View Log File' button 6. All HTTPD logging of the AdminServer will be displayed 7. Repeat for each managed server If any managed server or the AdminServer does not have HTTPD events within the access.log file, this is a finding.

## Group: SRG-APP-000095-AS-000056

**Group ID:** `V-235943`

### Rule: Oracle WebLogic must produce audit records containing sufficient information to establish what type of JVM-related events and severity levels occurred.

**Rule ID:** `SV-235943r960891_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Audit record content that may be necessary to satisfy the requirement of this control, includes: time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Application servers must log all relevant log data that pertains to application server functionality. Examples of relevant data include, but are not limited to, Java Virtual Machine (JVM) activity, HTTPD activity and application server-related system process activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Logs' -> 'View Log Messages' 3. Within the 'Search' panel, expand 'Selected Targets' 4. Click 'Target Log Files' icon for 'AdminServer' target 5. From the list of log files, select '<server-name>-diagnostic.log' and click 'View Log File' button 6. All JVM logging of the AdminServer will be displayed 7. Repeat for each managed server If there are no JVM-related events for the managed servers or the AdminServer, this is a finding.

## Group: SRG-APP-000095-AS-000056

**Group ID:** `V-235944`

### Rule: Oracle WebLogic must produce process events and security levels to establish what type of Oracle WebLogic process events and severity levels occurred.

**Rule ID:** `SV-235944r960891_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Audit record content that may be necessary to satisfy the requirement of this control, includes: time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Application servers must log all relevant log data that pertains to application server functionality. Examples of relevant data include, but are not limited to, Java Virtual Machine (JVM) activity, HTTPD activity and application server-related system process activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Logs' -> 'View Log Messages' 3. Within the 'Search' panel, expand 'Selected Targets' 4. Click 'Target Log Files' icon for 'AdminServer' target 5. From the list of log files, select '<server-name>.log' and click 'View Log File' button 6. All AS process logging of the AdminServer will be displayed 7. Repeat for each managed server If the managed servers or AdminServer does not have process events, this is a finding.

## Group: SRG-APP-000096-AS-000059

**Group ID:** `V-235945`

### Rule: Oracle WebLogic must produce audit records containing sufficient information to establish when (date and time) the events occurred.

**Rule ID:** `SV-235945r960894_rule`
**Severity:** low

**Description:**
<VulnDiscussion> Information system auditing capability is critical for accurate forensic analysis. Audit record content that may be necessary to satisfy the requirement of this control includes time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. In addition to logging event information, application servers must also log the corresponding dates and times of these events. Examples of event data include, but are not limited to, Java Virtual Machine (JVM) activity, HTTPD activity and application server-related system process activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Logs' -> 'View Log Messages' 3. Within the 'Search' panel, expand 'Selected Targets' 4. Click 'Target Log Files' icon for any of the managed server or 'Application Deployment' type targets (not AdminServer) 5. From the list of log files, select '<server-name>.log', 'access.log' or '<server-name>-diagnostic.log' and click 'View Log File' button 6. Time stamp of audit event will be displayed in 'Time' column 7. If 'Time' column does not appear, use 'View' button -> 'Columns' list to add 'Time' field, or select individual message in log message table and view the message detail (beneath the table) 8. Repeat for each target If any of the targets generate audit records without date and time data, this is a finding.

## Group: SRG-APP-000097-AS-000060

**Group ID:** `V-235946`

### Rule: Oracle WebLogic must produce audit records containing sufficient information to establish where the events occurred.

**Rule ID:** `SV-235946r960897_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Audit record content that may be necessary to satisfy the requirement of this control includes time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Without sufficient information establishing where the audit events occurred, investigation into the cause of events is severely hindered. In addition to logging relevant data, application servers must also log information to indicate the location of these events. Examples of relevant data include, but are not limited to, Java Virtual Machine (JVM) activity, HTTPD activity and application server-related system process activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Logs' -> 'View Log Messages' 3. Within the 'Search' panel, expand 'Selected Targets' 4. Click 'Target Log Files' icon for any of the managed server or 'Application Deployment' type targets (not AdminServer) 5. From the list of log files, select '<server-name>.log', 'access.log' or '<server-name>-diagnostic.log' and click 'View Log File' button 6. Select any record which appears in the log message table 7. Location of audit event will be displayed in 'Component' and 'Module' fields of the message detail (beneath the table) 8. Repeat for each target If any of the targets generate audit records without sufficient information to establish where the event occurred, this is a finding.

## Group: SRG-APP-000098-AS-000061

**Group ID:** `V-235947`

### Rule: Oracle WebLogic must produce audit records containing sufficient information to establish the sources of the events.

**Rule ID:** `SV-235947r960900_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Audit record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application specific events, success/fail indications, filenames involved, access control or flow control rules invoked. Without information establishing the source of activity, the value of audit records from a forensics perspective is questionable. Examples of activity sources include, but are not limited to, application process sources such as one process affecting another process, user-related activity, and activity resulting from remote network system access (IP addresses).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Logs' -> 'View Log Messages' 3. Within the 'Search' panel, expand 'Selected Targets' 4. Click 'Target Log Files' icon for any of the managed server or 'Application Deployment' type targets (not AdminServer) 5. From the list of log files, select '<server-name>.log', 'access.log' or '<server-name>-diagnostic.log' and click 'View Log File' button 6. Select any record which appears in the log message table 7. Source of audit event will be displayed in 'Host', 'Host IP Address', 'Thread ID', 'REMOTE_HOST' fields of the message detail (beneath the table), depending on which logfile and target type is selected 8. Repeat for each target If any of the targets generate audit records without sufficient information to establish the source of the events, this is a finding.

## Group: SRG-APP-000099-AS-000062

**Group ID:** `V-235948`

### Rule: Oracle WebLogic must produce audit records that contain sufficient information to establish the outcome (success or failure) of application server and application events.

**Rule ID:** `SV-235948r960903_rule`
**Severity:** low

**Description:**
<VulnDiscussion> Information system auditing capability is critical for accurate forensic analysis. Audit record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application specific events, success/fail indications, filenames involved, access control or flow control rules invoked. Success and failure indicators ascertain the outcome of a particular application server event of function. As such, they also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Logs' -> 'View Log Messages' 3. Within the 'Search' panel, expand 'Selected Targets' 4. Click 'Target Log Files' icon for any of the managed server or 'Application Deployment' type targets (not AdminServer) 5. From the list of log files, select '<server-name>.log', 'access.log' or '<server-name>-diagnostic.log' and click 'View Log File' button 6. Outcome of audit event will be displayed in 'Message Type' column. 'Error' or 'Exception' indicates failures, others message types indicate success 7. If 'Message Type' column does not appear, use 'View' button -> 'Columns' list to add 'Message Type' field, or select individual message in log message table and view the message detail (beneath the table) 8. Repeat for each target If any of the targets generate audit records without sufficient information to establish the outcome of the event, this is a finding.

## Group: SRG-APP-000100-AS-000063

**Group ID:** `V-235949`

### Rule: Oracle WebLogic must produce audit records containing sufficient information to establish the identity of any user/subject or process associated with the event.

**Rule ID:** `SV-235949r960906_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Audit record content that may be necessary to satisfy the requirement of this control, includes: time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Application servers have differing levels of logging capabilities which can be specified by setting a verbosity level. The application server must, at a minimum, be capable of establishing the identity of any user or process that is associated with any particular event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Logs' -> 'View Log Messages' 3. Within the 'Search' panel, expand 'Selected Targets' 4. Click 'Target Log Files' icon for any of the managed server or 'Application Deployment' type targets (not AdminServer) 5. From the list of log files, select '<server-name>.log', 'access.log' or '<server-name>-diagnostic.log' and click 'View Log File' button 6. User or process associated with audit event will be displayed in 'User' column 7. If 'User' column does not appear, use 'View' button -> 'Columns' list to add 'User' field, or select individual message in log message table and view the message detail (beneath the table) 8. Repeat for each target If any of the targets generate audit records without sufficient information to establish the identity of any user/subject or process, this is a finding.

## Group: SRG-APP-000515-AS-000203

**Group ID:** `V-235950`

### Rule: Oracle WebLogic must provide the ability to write specified audit record content to an audit log server.

**Rule ID:** `SV-235950r961860_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> Information system auditing capability is critical for accurate forensic analysis. Audit record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application specific events, success/fail indications, filenames involved, access control or flow control rules invoked. Centralized management of audit records and logs provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. Application servers and their related components are required to be capable of writing logs to centralized audit log servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'JDBC Data Sources' 3. From the list of data sources, select the one named 'opss-audit-DBDS', which connects to the IAU_APPEND schema of the audit database. Note the value in the 'JNDI name' field 4. To verify, select 'Configuration' tab -> 'Connection Pool' tab 5. Ensure the 'URL' and 'Properties' fields contain the correct connection values for the IAU_APPEND schema 6. To test, select 'Monitoring' tab, select a server from the list and click 'Test Data Source'. Ensure test was successful. Repeat for each server in the list 7. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Security' -> 'Security Provider Configuration' 8. Beneath 'Audit Service' section, click 'Configure' button 9. Ensure 'Data Source JNDI Name' value matches the JNDI Name value from data source in step 3 above 10. Repeat steps 2-6 for data source named 'wls-wldf-storeDS' and WLS schema If the location for audit data is not an audit log server, this is a finding.

## Group: SRG-APP-000108-AS-000067

**Group ID:** `V-235951`

### Rule: Oracle WebLogic must provide a real-time alert when organization-defined audit failure events occur.

**Rule ID:** `SV-235951r960912_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. Notification of the failure event will allow administrators to take actions so that logs are not lost.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Diagnostics' -> 'Diagnostic Modules' 3. Select 'Module-HealthState' from 'Diagnostic System Modules' list 4. Select 'Configuration' tab -> 'Watches and Notifications' tab. Select the 'Watches' tab from the bottom of page 5. Ensure 'ServerHealthWatch' row has 'Enabled' column value set to 'true' 6. Select 'Configuration' tab -> 'Watches and Notifications' tab. Select the 'Notifications' tab from the bottom of page 7. Ensure 'ServerHealthNotification' row has 'Enable Notification' column value set to 'true' If 'ServerHealthNotification' row has 'Enable Notification' column value is not set to 'true', this is a finding.

## Group: SRG-APP-000108-AS-000067

**Group ID:** `V-235952`

### Rule: Oracle WebLogic must alert designated individual organizational officials in the event of an audit processing failure.

**Rule ID:** `SV-235952r960912_rule`
**Severity:** low

**Description:**
<VulnDiscussion> Audit processing failures include, but are not limited to, failures in the application server log capturing mechanisms or audit storage capacity being reached or exceeded. In some instances, it is preferred to send alarms to individuals rather than to an entire group. Application servers must be able to trigger an alarm and send that alert to designated individuals in the event there is an application server audit processing failure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Diagnostics' -> 'Diagnostic Modules' 3. Select 'Module-HealthState' from 'Diagnostic System Modules' list 4. Select 'Configuration' tab -> 'Watches and Notifications' tab. Select the 'Watches' tab from the bottom of page 5. Ensure 'ServerHealthWatch' row has 'Enabled' column value set to 'true' 6. Select 'Configuration' tab -> 'Watches and Notifications' tab. Select the 'Notifications' tab from the bottom of page 7. Ensure 'ServerHealthNotification' row has 'Enable Notification' column value set to 'true' If 'ServerHealthNotification' row has 'Enable Notification' column value is not set to 'true', this is a finding.

## Group: SRG-APP-000108-AS-000067

**Group ID:** `V-235953`

### Rule: Oracle WebLogic must notify administrative personnel as a group in the event of audit processing failure.

**Rule ID:** `SV-235953r960912_rule`
**Severity:** low

**Description:**
<VulnDiscussion> Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. To ensure flexibility and ease of use, application servers must be capable of notifying a group of administrative personnel upon detection of an application audit log processing failure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Diagnostics' -> 'Diagnostic Modules' 3. Select 'Module-HealthState' from 'Diagnostic System Modules' list 4. Select 'Configuration' tab -> 'Watches and Notifications' tab. Select the 'Watches' tab from the bottom of page 5. Ensure 'ServerHealthWatch' row has 'Enabled' column value set to 'true' 6. Select 'Configuration' tab -> 'Watches and Notifications' tab. Select the 'Notifications' tab from the bottom of page 7. Ensure 'ServerHealthNotification' row has 'Enable Notification' column value set to 'true' If 'ServerHealthNotification' row has 'Enable Notification' column value not set to 'true', this is a finding.

## Group: SRG-APP-000116-AS-000076

**Group ID:** `V-235954`

### Rule: Oracle WebLogic must use internal system clocks to generate time stamps for audit records.

**Rule ID:** `SV-235954r960927_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without the use of an approved and synchronized time source, configured on the systems, events cannot be accurately correlated and analyzed to determine what is transpiring within the application server. If an event has been triggered on the network, and the application server is not configured with the correct time, the event may be seen as insignificant, when in reality the events are related and may have a larger impact across the network. Synchronization of system clocks is needed in order to correctly correlate the timing of events that occur across multiple systems. Determining the correct time a particular event occurred on a system, via time stamps, is critical when conducting forensic analysis and investigating system events. Application servers must utilize the internal system clock when generating time stamps and audit records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Security' -> 'Security Provider Configuration' 3. Beneath 'Audit Service' section, click 'Configure' button 4. Ensure the 'Timezone Settings' radio button is set to 'UTC' so audit logs will be time stamped in Coordinated Universal Time regardless of the time zone of the underlying physical or virtual machine 5. The time stamp will be recorded according to the operating system's set time If the 'Timezone Settings' radio button is not set to 'UTC', this is a finding.

## Group: SRG-APP-000372-AS-000212

**Group ID:** `V-235955`

### Rule: Oracle WebLogic must synchronize with internal information system clocks which, in turn, are synchronized on an organization-defined frequency with an organization-defined authoritative time source.

**Rule ID:** `SV-235955r981686_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Determining the correct time a particular application event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronization of system clocks is needed in order to correctly correlate the timing of events that occur across multiple systems. To meet that requirement the organization will define an authoritative time source and frequency to which each system will synchronize its internal clock. Application servers must defer accurate timekeeping services to the operating system upon which the application server is installed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Security' -> 'Security Provider Configuration' 3. Beneath 'Audit Service' section, click 'Configure' button 4. Ensure the 'Timezone Settings' radio button is set to 'UTC' so audit logs will be time stamped in Coordinated Universal Time regardless of the time zone of the underlying physical or virtual machine 5. The time stamp will be recorded according to the operating system's set time If the 'Timezone Settings' radio button is not set to 'UTC', this is a finding.

## Group: SRG-APP-000118-AS-000078

**Group ID:** `V-235956`

### Rule: Oracle WebLogic must protect audit information from any type of unauthorized read access.

**Rule ID:** `SV-235956r960930_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to audit records provides information an attacker could potentially use to his or her advantage. Application servers contain admin interfaces that allow reading and manipulation of audit records. Therefore, these interfaces should not allow for unfettered access to those records. Application servers also write audit data to log files which are stored on the OS, so appropriate file permissions must also be used to restrict access. Audit information includes all information (e.g., audit records, audit settings, transaction logs, and audit reports) needed to successfully audit information system activity. Application servers must protect audit information from unauthorized read access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Security Realms' 3. Select realm to configure (default is 'myrealm') 4. Select 'Users and Groups' tab -> 'Users' tab 5. From 'Users' table, select a user that must not have audit read access 6. From users settings page, select 'Groups' tab 7. Ensure the 'Chosen' table does not contain any of the following roles - 'Admin', 'Deployer', 'Monitor', 'Operator' 8. Repeat steps 5-7 for all users that must not have audit read access If any users that should not have access to read audit information contain any of the roles of 'Admin', 'Deployer', 'Monitor' or 'Operator', this is a finding.

## Group: SRG-APP-000121-AS-000081

**Group ID:** `V-235957`

### Rule: Oracle WebLogic must protect audit tools from unauthorized access.

**Rule ID:** `SV-235957r960939_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Depending upon the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. It is, therefore, imperative that access to audit tools be controlled and protected from unauthorized access. Application servers provide a web and/or a command line-based management functionality for managing the application server audit capabilities. In addition, subsets of audit tool components may be stored on the file system as jar or xml configuration files. The application server must ensure that in addition to protecting any web based audit tools, any file system-based tools are protected as well.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Security Realms' 3. Select realm to configure (default is 'myrealm') 4. Select 'Users and Groups' tab -> 'Users' tab 5. From 'Users' table, select a user that must not have audit tool configuration access 6. From users settings page, select 'Groups' tab 7. Ensure the 'Chosen' table does not contain the role - 'Admin' 8. Repeat steps 5-7 for all users that must not have audit tool configuration access If any users that should not have access to the audit tools contains the role of 'Admin', this is a finding.

## Group: SRG-APP-000122-AS-000082

**Group ID:** `V-235958`

### Rule: Oracle WebLogic must protect audit tools from unauthorized modification.

**Rule ID:** `SV-235958r960942_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Depending upon the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. It is, therefore, imperative that access to audit tools be controlled and protected from unauthorized modification. If an attacker were to modify audit tools, he could also manipulate logs to hide evidence of malicious activity. Application servers provide a web- and/or a command line-based management functionality for managing the application server audit capabilities. In addition, subsets of audit tool components may be stored on the file system as jar or xml configuration files. The application server must ensure that in addition to protecting any web-based audit tools, any file system-based tools are protected as well.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Security Realms' 3. Select realm to configure (default is 'myrealm') 4. Select 'Users and Groups' tab -> 'Users' tab 5. From 'Users' table, select a user that must not have audit tool configuration access 6. From users settings page, select 'Groups' tab 7. Ensure the 'Chosen' table does not contain the role - 'Admin' 8. Repeat steps 5-7 for all users that must not have audit tool configuration access If any users that should not have access to the audit tools contains the role of 'Admin', this is a finding.

## Group: SRG-APP-000123-AS-000083

**Group ID:** `V-235959`

### Rule: Oracle WebLogic must protect audit tools from unauthorized deletion.

**Rule ID:** `SV-235959r960945_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Depending upon the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. It is, therefore, imperative that access to audit tools be controlled and protected from unauthorized modification. If an attacker were to delete audit tools the application server administrators would have no way of managing or viewing the logs. Application servers provide a web- and/or a command line-based management functionality for managing the application server audit capabilities. In addition, subsets of audit tool components may be stored on the file system as jar, class, or xml configuration files. The application server must ensure that in addition to protecting any web-based audit tools, any file system-based tools are protected from unauthorized deletion as well.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Security Realms' 3. Select realm to configure (default is 'myrealm') 4. Select 'Users and Groups' tab -> 'Users' tab 5. From 'Users' table, select a user that must not have audit tool configuration access 6. From users settings page, select 'Groups' tab 7. Ensure the 'Chosen' table does not contain the role - 'Admin' 8. Repeat steps 5-7 for all users that must not have audit tool configuration access If any users that should not have access to the audit tools contains the role of 'Admin', this is a finding.

## Group: SRG-APP-000133-AS-000092

**Group ID:** `V-235960`

### Rule: Oracle WebLogic must limit privileges to change the software resident within software libraries (including privileged programs).

**Rule ID:** `SV-235960r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application servers have the ability to specify that the hosted applications utilize shared libraries. The application server must have a capability to divide roles based upon duties wherein one project user (such as a developer) cannot modify the shared library code of another project user. The application server must also be able to specify that non-privileged users cannot modify any shared library code at all.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Security Realms' 3. Select realm to configure (default is 'myrealm') 4. Select 'Users and Groups' tab -> 'Users' tab 5. From 'Users' table, select a user that must not have shared library modification access 6. From users settings page, select 'Groups' tab 7. Ensure the 'Chosen' table does not contain the roles - 'Admin', 'Deployer' 8. Repeat steps 5-7 for all users that must not have shared library modification access If any users that are not permitted to change the software resident within software libraries (including privileged programs) have the role of 'Admin' or 'Deployer', this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-235961`

### Rule: Oracle WebLogic must adhere to the principles of least functionality by providing only essential capabilities.

**Rule ID:** `SV-235961r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> Application servers provide a myriad of differing processes, features and functionalities. Some of these processes may be deemed to be unnecessary or too insecure to run on a production DoD system. Application servers must provide the capability to disable or deactivate functionality and services that are deemed to be non-essential to the server mission or can adversely impact server performance, for example, disabling dynamic JSP reloading on production application servers as a best practice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Deployments' 3. Select a deployment of type 'Web Application' from list of deployments 4. Select 'Configuration' tab -> 'General' tab 5. Ensure 'JSP Page Check' field value is set to '-1', which indicates JSP reloading is disabled within this deployment. Repeat steps 3-5 for all 'Web Application' type deployments 6. For every WebLogic resource within the domain, the 'Configuration' tab and associated subtabs provide the ability to disable or deactivate functionality and services that are deemed to be non-essential to the server mission or can adversely impact server performance If the 'JSP Page Check' field is not set to '-1' or other services or functionality deemed to be non-essential to the server mission is not set to '-1', this is a finding.

## Group: SRG-APP-000142-AS-000014

**Group ID:** `V-235962`

### Rule: Oracle WebLogic must prohibit or restrict the use of unauthorized functions, ports, protocols, and/or services.

**Rule ID:** `SV-235962r1043177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application servers provide numerous processes, features, and functionalities that utilize TCP/IP ports. Some of these processes may be deemed to be unnecessary or too insecure to run on a production system. The application server must provide the capability to disable or deactivate network-related services that are deemed to be non-essential to the server mission, for example, disabling a protocol or feature that opens a listening port that is prohibited by DoD ports and protocols. For a list of approved ports and protocols reference the DoD ports and protocols web site at https://cyber.mil/ppsm.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Monitoring' -> 'Port Usage' 3. In the results table, ensure values in the 'Port in Use' column match approved ports 4. In the results table, ensure values in the 'Protocol' column match approved protocols If any ports listed in the 'Port in Use' column is an unauthorized port or any protocols listed in the 'Protocol' column is an unauthorized protocol, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-235963`

### Rule: Oracle WebLogic must utilize automated mechanisms to prevent program execution on the information system.

**Rule ID:** `SV-235963r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The application server must provide a capability to halt or otherwise disable the automatic execution of deployed applications until such time that the application is considered part of the established application server baseline. Deployment to the application server should not provide a means for automatic application start-up should the application server itself encounter a restart condition.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select the top-level domain 3. Select 'Configuration' tab -> 'General' tab 4. Ensure 'Production Mode' checkbox is selected If the 'Production Mode' checkbox is not selected, this is a finding.

## Group: SRG-APP-000148-AS-000101

**Group ID:** `V-235964`

### Rule: Oracle WebLogic must uniquely identify and authenticate users (or processes acting on behalf of users).

**Rule ID:** `SV-235964r1051118_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthorized access, application server users must be uniquely identified and authenticated. The application server must uniquely identify and authenticate application server users or processes acting on behalf of users. This is typically accomplished via the use of a user store which is either local (OS-based) or centralized (LDAP) in nature.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Security Realms' 3. Select realm to configure (default is 'myrealm') 4. Select 'Providers' tab -> 'Authentication' tab 5. Ensure the list of 'Authentication Providers' contains at least one non-Default Authentication Provider 6. If the Authentication Provider is perimeter-based, ensure the list contains at least one non-Default IdentityAsserter If the list of 'Authentication Providers' does not contain at least one non-Default Authentication Provider, this is a finding. If the Authentication Provider is perimeter-based and the list of 'Authentication Providers' does not contain at least one non-Default IdentityAsserter, this is a finding.

## Group: SRG-APP-000153-AS-000104

**Group ID:** `V-235965`

### Rule: Oracle WebLogic must authenticate users individually prior to using a group authenticator.

**Rule ID:** `SV-235965r981680_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To assure individual accountability and prevent unauthorized access, application server users (and any processes acting on behalf of application server users) must be individually identified and authenticated. A group authenticator is a generic account used by multiple individuals. Use of a group authenticator alone does not uniquely identify individual users. Application servers must ensure that individual users are authenticated prior to authenticating via role or group authentication. This is to ensure that there is non-repudiation for actions taken.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Security Realms' 3. Select realm to configure (default is 'myrealm') 4. Select 'Providers' tab -> 'Authentication' tab 5. Ensure the list of 'Authentication Providers' contains at least one non-Default Authentication Provider 6. If the Authentication Provider is perimeter-based, ensure the list contains at least one non-Default IdentityAsserter If the list of 'Authentication Providers' does not contain at least one non-Default Authentication Provider, this is a finding. If the Authentication Provider is perimeter-based and the list of 'Authentication Providers' does not contain at least one non-Default IdentityAsserter, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-235966`

### Rule: Oracle WebLogic must enforce minimum password length.

**Rule ID:** `SV-235966r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one of several factors that helps to determine strength and how long it takes to crack a password. The shorter the password is, the lower the number of possible combinations that need to be tested before the password is compromised. Application servers either provide a local user store, or they integrate with enterprise user stores like LDAP. When the application server provides the user store and enforces authentication, the application server must enforce minimum password length.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Security Realms' 3. Select realm to configure (default is 'myrealm') 4. Select 'Providers' tab -> 'Password Validation' subtab 5. Select 'SystemPasswordValidator' 6. Select 'Configuration' tab -> 'Provider Specific' subtab 7. Ensure 'Minimum Password Length' field value is set to '15' If the 'Minimum Password Length' field is not set to '15', this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-235967`

### Rule: Oracle WebLogic must enforce password complexity by the number of upper-case characters used.

**Rule ID:** `SV-235967r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Use of a complex password helps to increase the time and resources required to compromise the password. Application servers either provide a local user store, or they integrate with enterprise user stores like LDAP. When the application server provides the user store and enforces authentication, the application server must enforce the organization's password complexity requirements, which includes the requirement to use a specific number of upper-case characters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Security Realms' 3. Select realm to configure (default is 'myrealm') 4. Select 'Providers' tab -> 'Password Validation' subtab 5. Select 'SystemPasswordValidator' 6. Select 'Configuration' tab -> 'Provider Specific' subtab 7. Ensure 'Minimum Number of Upper Case Characters' field value is set to '1' or higher If the 'Minimum Number of Upper Case Characters' field value is not set to '1' or higher, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-235968`

### Rule: Oracle WebLogic must enforce password complexity by the number of lower-case characters used.

**Rule ID:** `SV-235968r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Use of a complex password helps to increase the time and resources required to compromise the password. Application servers either provide a local user store, or they integrate with enterprise user stores like LDAP. When the application server provides the user store and enforces authentication, the application server must enforce the organization's password complexity requirements, which include the requirement to use a specific number of lower-case characters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Security Realms' 3. Select realm to configure (default is 'myrealm') 4. Select 'Providers' tab -> 'Password Validation' subtab 5. Select 'SystemPasswordValidator' 6. Select 'Configuration' tab -> 'Provider Specific' subtab 7. Ensure 'Minimum Number of Lower Case Characters' field value is set to '1' or higher If the 'Minimum Number of Lower Case Characters' field value is not set to '1' or higher, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-235969`

### Rule: Oracle WebLogic must enforce password complexity by the number of numeric characters used.

**Rule ID:** `SV-235969r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Use of a complex password helps to increase the time and resources required to compromise the password. Application servers provide either a local user store or they integrate with enterprise user stores like LDAP. When the application server provides the user store and enforces authentication, the application server must enforce the organization's password complexity requirements that include the requirement to use a specific number of numeric characters when passwords are created or changed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Security Realms' 3. Select realm to configure (default is 'myrealm') 4. Select 'Providers' tab -> 'Password Validation' subtab 5. Select 'SystemPasswordValidator' 6. Select 'Configuration' tab -> 'Provider Specific' subtab 7. Ensure 'Minimum Number of Numeric Characters' field value is set to '1' or higher If the 'Minimum Number of Numeric Characters' field value is not set to '1' or higher, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-235970`

### Rule: Oracle WebLogic must enforce password complexity by the number of special characters used.

**Rule ID:** `SV-235970r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Use of a complex password helps to increase the time and resources required to compromise the password. Application servers either provide a local user store, or they integrate with enterprise user stores like LDAP. When the application server provides the user store and enforces authentication, the application server must enforce the organization's password complexity requirements that include the requirement to use a specific number of special characters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Security Realms' 3. Select realm to configure (default is 'myrealm') 4. Select 'Providers' tab -> 'Password Validation' subtab 5. Select 'SystemPasswordValidator' 6. Select 'Configuration' tab -> 'Provider Specific' subtab 7. Ensure 'Minimum Number of Non-Alphanumeric Characters' field value is set to '1' or higher If the 'Minimum Number of Non-Alphanumeric Characters' field value is not set to '1' or higher, this is a finding.

## Group: SRG-APP-000172-AS-000120

**Group ID:** `V-235971`

### Rule: Oracle WebLogic must encrypt passwords during transmission.

**Rule ID:** `SV-235971r961029_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords during transmission. Application servers have the capability to utilize either certificates (tokens) or user IDs and passwords in order to authenticate. When the application server transmits or receives passwords, the passwords must be encrypted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Security Realms' 3. Select realm to configure (default is 'myrealm') 4. Select 'Providers' tab -> 'Authentication' tab 5. Ensure the list of 'Authentication Providers' contains at least one non-Default Authentication Provider 6. If the Authentication Provider is perimeter-based, ensure the list contains at least one non-Default IdentityAsserter If the list of 'Authentication Providers' does not contain at least one non-Default Authentication Provider, this is a finding. If the Authentication Provider is perimeter-based and the list of 'Authentication Providers' does not contain at least one non-Default IdentityAsserter, this is a finding.

## Group: SRG-APP-000172-AS-000121

**Group ID:** `V-235972`

### Rule: Oracle WebLogic must utilize encryption when using LDAP for authentication.

**Rule ID:** `SV-235972r961029_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords during transmission. Application servers have the capability to utilize LDAP directories for authentication. If LDAP connections are not protected during transmission, sensitive authentication credentials can be stolen. When the application server utilizes LDAP, the LDAP traffic must be encrypted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Monitoring' -> 'Port Usage' 3. In the results table, ensure the 'Protocol' column does not contain the value 'LDAP' (only 'LDAPS') If LDAP is being used and the 'Protocol' column contains the value 'LDAP', this is a finding.

## Group: SRG-APP-000175-AS-000124

**Group ID:** `V-235973`

### Rule: Oracle WebLogic, when utilizing PKI-based authentication, must validate certificates by constructing a certification path with status information to an accepted trust anchor.

**Rule ID:** `SV-235973r961038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes, certificate revocation lists or online certificate status protocol responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Environment' -> 'Servers' 3. From the list of servers, select one which needs check for SSL configuration verification 4. From 'Configuration' tab -> 'General' tab, ensure 'Listen Port Enabled' checkbox is deselected 5. Ensure 'SSL Listen Port Enabled' checkbox is selected and a valid port number is in 'SSL Listen Port' field, e.g., 7002 6. Repeat steps 3-5 for all servers requiring SSL configuration checking If any servers utilizing PKI-based authentication does not have the 'SSL Listen Port Enabled' selected, this is a finding.

## Group: SRG-APP-000177-AS-000126

**Group ID:** `V-235974`

### Rule: Oracle WebLogic must map the PKI-based authentication identity to the user account.

**Rule ID:** `SV-235974r961044_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The cornerstone of the PKI is the private key used to encrypt or digitally sign information. The key by itself is a cryptographic value that does not contain specific user information. Application servers must provide the capability to utilize and meet requirements of the DoD Enterprise PKI infrastructure for application authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Security Realms' 3. Select realm to configure (default is 'myrealm') 4. Select 'Providers' tab -> 'Authentication' tab 5. Ensure the list of 'Authentication Providers' contains at least one non-Default Authentication Provider 6. If the Authentication Provider is perimeter-based, ensure the list contains at least one non-Default IdentityAsserter If PKI-based authentication is being used and the list of 'Authentication Providers' does not contain at least one non-Default Authentication Provider, this is a finding. If PKI-based authentication is being used and the Authentication Provider is perimeter-based and the list of 'Authentication Providers' does not contain at least one non-Default IdentityAsserter, this is a finding.

## Group: SRG-APP-000179-AS-000129

**Group ID:** `V-235975`

### Rule: Oracle WebLogic must use cryptographic modules that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance when encrypting stored data.

**Rule ID:** `SV-235975r961050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified and cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised due to weak algorithms. FIPS 140-2 is the current standard for validating cryptographic modules, and NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified hardware-based encryption modules. Application servers must provide FIPS-compliant encryption modules when storing encrypted data and configuration settings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Logs' -> 'View Log Messages' 3. Within the 'Search' panel, expand 'Selected Targets' 4. Click 'Target Log Files' icon for 'AdminServer' target 5. From the list of log files, select 'AdminServer.log' and click 'View Log File' button 6. Within the search criteria, enter the value 'FIPS' for the 'Message contains' field, and select the appropriate 'Start Date' and 'End Date' range. Click 'Search' 7. Check for the following log entry: "Changing the default Random Number Generator in RSA CryptoJ ... to FIPS186PRNG" or "Changing the default Random Number Generator in RSA CryptoJ from ECDRBG128 to HMACDRBG." If either of these log entries are found, this is not a finding. If a log entry cannot be found, navigate to the DOMAIN_HOME directory: 8. View the contents of the appropriate WebLogic server start script: On UNIX operating systems: startWebLogic.sh On Microsoft Windows operating systems: startWebLogic.cmd 9. Ensure the JAVA_OPTIONS variable is set: On UNIX operating systems: JAVA_OPTIONS=" -Djava.security.properties==/<mylocation>/java.security ${JAVA_OPTIONS}" On Microsoft Windows operating systems: set JAVA_OPTIONS= -Djava.security.properties==C:\<mylocation>\java.security %JAVA_OPTIONS% 10. Ensure the <mylocation> path specified above contains a valid java.security file (Refer to section 2.2.4 of the Overview document) 11. Ensure the PRE_CLASSPATH variable is set: On UNIX operating systems: PRE_CLASSPATH="%MW_HOME%\wlserver\server\lib\jcmFIPS.jar;%MW_HOME%\wlserver\server\lib\sslj.jar ${PRE_CLASSPATH}" On Microsoft Windows operating systems: set PRE_CLASSPATH= %MW_HOME%\wlserver\server\lib\jcmFIPS.jar;%MW_HOME%\wlserver\server\lib\sslj.jar;%PRE_CLASSPATH% If the java options are not set correctly, this is a finding.

## Group: SRG-APP-000179-AS-000129

**Group ID:** `V-235976`

### Rule: Oracle WebLogic must utilize FIPS 140-2 approved encryption modules when authenticating users and processes.

**Rule ID:** `SV-235976r961050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified and cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised due to weak algorithms. FIPS 140-2 is the current standard for validating cryptographic modules, and NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified hardware-based encryption modules. Application servers must provide FIPS-compliant encryption modules when authenticating users and processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Logs' -> 'View Log Messages' 3. Within the 'Search' panel, expand 'Selected Targets' 4. Click 'Target Log Files' icon for 'AdminServer' target 5. From the list of log files, select 'AdminServer.log' and click 'View Log File' button 6. Within the search criteria, enter the value 'FIPS' for the 'Message contains' field, and select the appropriate 'Start Date' and 'End Date' range. Click 'Search' 7. Check for the following log entry: "Changing the default Random Number Generator in RSA CryptoJ ... to FIPS186PRNG" or "Changing the default Random Number Generator in RSA CryptoJ from ECDRBG128 to HMACDRBG." If either of these log entries are found, this is not a finding. If a log entry cannot be found, navigate to the DOMAIN_HOME directory: 8. View the contents of the appropriate WebLogic server start script: On UNIX operating systems: startWebLogic.sh On Microsoft Windows operating systems: startWebLogic.cmd 9. Ensure the JAVA_OPTIONS variable is set: On UNIX operating systems: JAVA_OPTIONS=" -Djava.security.properties==/<mylocation>/java.security ${JAVA_OPTIONS}" On Microsoft Windows operating systems: set JAVA_OPTIONS= -Djava.security.properties==C:\<mylocation>\java.security %JAVA_OPTIONS% 10. Ensure the <mylocation> path specified above contains a valid java.security file (Refer to section 2.2.4 of the Overview document) 11. Ensure the PRE_CLASSPATH variable is set: On UNIX operating systems: PRE_CLASSPATH="%MW_HOME%\wlserver\server\lib\jcmFIPS.jar;%MW_HOME%\wlserver\server\lib\sslj.jar ${PRE_CLASSPATH}" On Microsoft Windows operating systems: set PRE_CLASSPATH= %MW_HOME%\wlserver\server\lib\jcmFIPS.jar;%MW_HOME%\wlserver\server\lib\sslj.jar;%PRE_CLASSPATH% If the java options are not set correctly, this is a finding.

## Group: SRG-APP-000440-AS-000167

**Group ID:** `V-235977`

### Rule: Oracle WebLogic must employ cryptographic encryption to protect the integrity and confidentiality of nonlocal maintenance and diagnostic communications.

**Rule ID:** `SV-235977r961635_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Application servers provide an HTTP-oriented remote management capability that is used for managing the application server as well as uploading and deleting applications that are hosted on the application server. Application servers need to ensure the communication channels used to remotely access the system utilize cryptographic mechanisms such as TLS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Environment' -> 'Servers' 3. From the list of servers, select one which needs check for SSL configuration verification 4. From 'Configuration' tab -> 'General' tab, ensure 'Listen Port Enabled' checkbox is deselected 5. Ensure 'SSL Listen Port Enabled' checkbox is selected and a valid port number is in 'SSL Listen Port' field, e.g., 7002 6. Repeat steps 3-5 for all servers requiring SSL configuration checking If any of the servers requiring SSL have the 'Listen Port Enabled' selected or 'SSL Listen Port Enable' not selected, this is a finding.

## Group: SRG-APP-000149-AS-000102

**Group ID:** `V-235978`

### Rule: Oracle WebLogic must employ strong identification and authentication techniques when establishing nonlocal maintenance and diagnostic sessions.

**Rule ID:** `SV-235978r960972_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Application servers will typically utilize an HTTP interface for providing both local and remote maintenance and diagnostic sessions. In these instances, an acceptable strong identification and authentication technique consists of utilizing two-factor authentication via secured HTTPS connections. If the application server also provides maintenance and diagnostic access via a fat client or other client-based connection, then that client must also utilize two-factor authentication and use FIPS-approved encryption modules for establishing transport connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Environment' -> 'Servers' 3. From the list of servers, select one which needs check for SSL configuration verification 4. From 'Configuration' tab -> 'General' tab, ensure 'Listen Port Enabled' checkbox is deselected 5. Ensure 'SSL Listen Port Enabled' checkbox is selected and a valid port number is in 'SSL Listen Port' field, e.g., 7002 6. Repeat steps 3-5 for all servers requiring SSL configuration checking If any of the servers requiring SSL have the 'Listen Port Enabled' selected or 'SSL Listen Port Enable' not selected, this is a finding.

## Group: SRG-APP-000295-AS-000263

**Group ID:** `V-235979`

### Rule: Oracle WebLogic must terminate the network connection associated with a communications session at the end of the session or after a DoD-defined time period of inactivity.

**Rule ID:** `SV-235979r1043182_rule`
**Severity:** low

**Description:**
<VulnDiscussion> If communications sessions remain open for extended periods of time even when unused, there is the potential for an adversary to hijack the session and use it to gain access to the device or networks to which it is attached. Terminating sessions after a certain period of inactivity is a method for mitigating the risk of this vulnerability. The application server must provide a mechanism for timing out or otherwise terminating inactive web sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Deployments' 3. Sort 'Deployments' table by 'Type' by click the column header 4. Select an 'Enterprise Application' or 'Web Application' to check the session timeout setting 5. Select 'Configuration' tab -> 'Application' tab for deployments of 'Enterprise Application' type Select 'Configuration' tab -> 'General' tab for deployments of 'Web Application' type 6. Ensure 'Session Timeout' field value is set to '900' (seconds) If the 'Session Timeout' field is not set '900', this is a finding.

## Group: SRG-APP-000440-AS-000167

**Group ID:** `V-235980`

### Rule: Oracle WebLogic must establish a trusted communications path between the user and organization-defined security functions within the information system.

**Rule ID:** `SV-235980r961635_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without a trusted communication path, the application server is vulnerable to a man-in-the-middle attack. Application server user interfaces are used for management of the application server so the communications path between client and server must be trusted or management of the server may be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Environment' -> 'Servers' 3. From the list of servers, select one which needs check for SSL configuration verification 4. From 'Configuration' tab -> 'General' tab, ensure 'Listen Port Enabled' checkbox is deselected 5. Ensure 'SSL Listen Port Enabled' checkbox is selected and a valid port number is in 'SSL Listen Port' field, e.g., 7002 6. Repeat steps 3-5 for all servers requiring SSL configuration checking If any of the servers requiring SSL have the 'Listen Port Enabled' selected or 'SSL Listen Port Enable' not selected, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-235981`

### Rule: Oracle WebLogic must utilize NSA-approved cryptography when protecting classified compartmentalized data.

**Rule ID:** `SV-235981r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cryptography is only as strong as the encryption modules/algorithms employed to encrypt the data. Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. Encryption modules/algorithms are the mathematical procedures used for encrypting data. NSA has developed Type 1 algorithms for protecting classified information. The Committee on National Security Systems (CNSS) National Information Assurance Glossary (CNSS Instruction No. 4009) defines Type 1 products as: "Cryptographic equipment, assembly or component classified or certified by NSA for encrypting and decrypting classified and sensitive national security information when appropriately keyed. Developed using established NSA business processes and containing NSA-approved algorithms. Used to protect systems requiring the most stringent protection mechanisms." Although persons may have a security clearance, they may not have a "need to know" and are required to be separated from the information in question. The application server must employ NSA-approved cryptography to protect classified information from those individuals who have no "need to know" or when encryption of compartmentalized data is required by data classification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Logs' -> 'View Log Messages' 3. Within the 'Search' panel, expand 'Selected Targets' 4. Click 'Target Log Files' icon for 'AdminServer' target 5. From the list of log files, select 'AdminServer.log' and click 'View Log File' button 6. Within the search criteria, enter the value 'FIPS' for the 'Message contains' field, and select the appropriate 'Start Date' and 'End Date' range. Click 'Search' 7. Check for the following log entry: "Changing the default Random Number Generator in RSA CryptoJ ... to FIPS186PRNG" or "Changing the default Random Number Generator in RSA CryptoJ from ECDRBG128 to HMACDRBG." If either of these log entries are found, this is not a finding. If a log entry cannot be found, navigate to the DOMAIN_HOME directory: 8. View the contents of the appropriate WebLogic server start script: On UNIX operating systems: startWebLogic.sh On Microsoft Windows operating systems: startWebLogic.cmd 9. Ensure the JAVA_OPTIONS variable is set: On UNIX operating systems: JAVA_OPTIONS=" -Djava.security.properties==/<mylocation>/java.security ${JAVA_OPTIONS}" On Microsoft Windows operating systems: set JAVA_OPTIONS= -Djava.security.properties==C:\<mylocation>\java.security %JAVA_OPTIONS% 10. Ensure the <mylocation> path specified above contains a valid java.security file (Refer to section 2.2.4 of the Overview document) 11. Ensure the PRE_CLASSPATH variable is set: On UNIX operating systems: PRE_CLASSPATH="%MW_HOME%\wlserver\server\lib\jcmFIPS.jar;%MW_HOME%\wlserver\server\lib\sslj.jar ${PRE_CLASSPATH}" On Microsoft Windows operating systems: set PRE_CLASSPATH= %MW_HOME%\wlserver\server\lib\jcmFIPS.jar;%MW_HOME%\wlserver\server\lib\sslj.jar;%PRE_CLASSPATH% If the java options are not set correctly, this is a finding.

## Group: SRG-APP-000435-AS-000069

**Group ID:** `V-235982`

### Rule: Oracle WebLogic must protect the integrity and availability of publicly available information and applications.

**Rule ID:** `SV-235982r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> The purpose of this control is to ensure organizations explicitly address the protection needs for public information and applications, with such protection likely being implemented as part of other security controls. Application servers must protect the integrity of publicly available information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Deployments' 3. Select a deployed component which contains publicly available information and/or applications 4. Select 'Targets' tab 5. Ensure one or more of the selected targets for this deployment is a cluster of managed servers If the information requires clustering of managed server and the managed servers are not clustered, this is a finding.

## Group: SRG-APP-000211-AS-000146

**Group ID:** `V-235983`

### Rule: Oracle WebLogic must separate hosted application functionality from Oracle WebLogic management functionality.

**Rule ID:** `SV-235983r961095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application server management functionality includes functions necessary to administer the application server and requires privileged access via one of the accounts assigned to a management role. The separation of application server administration functionality from hosted application functionality is either physical or logical and is accomplished by using different computers, different central processing units, different instances of the operating system, network addresses, network ports, or combinations of these methods, as appropriate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Environment' -> 'Servers' 3. A single server in the list will be named 'Admin Server' and this is the server which hosts AS management functionality, such as the AdminConsole application 4. All remaining servers in the list are 'Managed Servers' and these are the individual or clustered servers which will host the actual applications 5. Ensure no applications are deployed on the Admin server, rather, only on the Managed servers If any applications are deployed on the Admin server, this is a finding.

## Group: SRG-APP-000219-AS-000147

**Group ID:** `V-235984`

### Rule: Oracle WebLogic must ensure authentication of both client and server during the entire session.

**Rule ID:** `SV-235984r1043178_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This control focuses on communications protection at the session, versus packet level. At the application layer, session IDs are tokens generated by web applications to uniquely identify an application user's session. Web applications utilize session tokens or session IDs in order to establish application user identity. Proper use of session IDs addresses man-in-the-middle attacks, including session hijacking or insertion of false information into a session. Application servers must provide the capability to perform mutual authentication. Mutual authentication is when both the client and the server authenticate each other.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Environment' -> 'Servers' 3. From the list of servers, select one which needs check for Mutual Authentication configuration verification 4. From 'Configuration' tab -> 'General' tab, ensure 'Listen Port Enabled' checkbox is deselected 5. Ensure 'SSL Listen Port Enabled' checkbox is selected and a valid port number is in 'SSL Listen Port' field, e.g., 7002 6. From 'Configuration' tab -> 'SSL' tab, click 'Advanced' link 7. Ensure 'Two Way Client Cert Behavior' field value is set to 'Client Certs Requested And Enforced' 8. Repeat steps 3-7 for all servers requiring Mutual Authentication configuration checking If any servers requiring Mutual Authentication do not have the 'SSL Listen Port Enabled' checkbox selected or the 'Two Way Client Cert Behavior' field value set to 'Client Certs Requested And Enforced', this is a finding.

## Group: SRG-APP-000220-AS-000148

**Group ID:** `V-235985`

### Rule: Oracle WebLogic must terminate user sessions upon user logout or any other organization- or policy-defined session termination events such as idle time limit exceeded.

**Rule ID:** `SV-235985r1043179_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> If communications sessions remain open for extended periods of time even when unused, there is the potential for an adversary to hijack the session and use it to gain access to the device or networks to which it is attached. Terminating sessions after a logout event or after a certain period of inactivity is a method for mitigating the risk of this vulnerability. When a user management session becomes idle, or when a user logs out of the management interface, the application server must terminate the session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Deployments' 3. Sort 'Deployments' table by 'Type' by click the column header 4. Select an 'Enterprise Application' or 'Web Application' to check the session timeout setting 5. Select 'Configuration' tab -> 'Application' tab for deployments of 'Enterprise Application' type Select 'Configuration' tab -> 'General' tab for deployments of 'Web Application' type 6. Ensure 'Session Timeout' field value is set to organization- or policy-defined session idle time limit If the 'Session Timeout' field value is not set to an organization- or policy-defined session idle time limit, this is a finding.

## Group: SRG-APP-000225-AS-000153

**Group ID:** `V-235986`

### Rule: Oracle WebLogic must be configured to perform complete application deployments.

**Rule ID:** `SV-235986r961122_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. When an application is deployed to the application server, if the deployment process does not complete properly and without errors, there is the potential that some application files may not be deployed or may be corrupted and an application error may occur during runtime. The application server must be able to perform complete application deployments. A partial deployment can leave the server in an inconsistent state. Application servers may provide a transaction rollback function to address this issue.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select the top-level domain 3. Select 'Configuration' tab -> 'General' tab 4. Ensure 'Production Mode' checkbox is selected If the 'Production Mode' checkbox is not selected, this is a finding.

## Group: SRG-APP-000440-AS-000167

**Group ID:** `V-235987`

### Rule: Oracle WebLogic must protect the confidentiality of applications and leverage transmission protection mechanisms, such as TLS and SSL VPN, when deploying applications.

**Rule ID:** `SV-235987r961635_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that applications take measures to employ some form of cryptographic mechanism in order to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS), SSL VPN, or IPSEC tunnel. If the application server does not protect the application files that are created before and during the application deployment process, there is a risk that the application could be compromised prior to deployment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Environment' -> 'Servers' 3. From the list of servers, select the AdminServer 4. From 'Configuration' tab -> 'General' tab, ensure 'Listen Port Enabled' checkbox is deselected 5. Ensure 'SSL Listen Port Enabled' checkbox is selected and a valid port number is in 'SSL Listen Port' field, e.g., 7002 If the field 'SSL Listen Port Enabled' is not selected or 'Listen Port Enabled' is selected, this is a finding.

## Group: SRG-APP-000435-AS-000069

**Group ID:** `V-235988`

### Rule: Oracle WebLogic must protect the integrity of applications during the processes of data aggregation, packaging, and transformation in preparation for deployment.

**Rule ID:** `SV-235988r961620_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information can be subjected to unauthorized changes (e.g., malicious and/or unintentional modification) at information aggregation or protocol transformation points. It is therefore imperative the application take steps to validate and assure the integrity of data while at these stages of processing. The application server must ensure the integrity of data that is pending transfer for deployment is maintained. If the application were to simply transmit aggregated, packaged, or transformed data without ensuring the data was not manipulated during these processes, then the integrity of the data and the application itself may be called into question.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select the top-level domain 3. Select 'Configuration' tab -> 'General' tab 4. Ensure 'Production Mode' checkbox is selected If the 'Production Mode' checkbox is not selected, this is a finding.

## Group: SRG-APP-000435-AS-000163

**Group ID:** `V-235989`

### Rule: Oracle WebLogic must protect against or limit the effects of HTTP types of Denial of Service (DoS) attacks.

**Rule ID:** `SV-235989r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Employing increased capacity and bandwidth combined with service redundancy can reduce the susceptibility to some DoS attacks. When utilizing an application server in a high risk environment (such as a DMZ), the amount of access to the system from various sources usually increases, as does the system's risk of becoming more susceptible to DoS attacks. The application server must be able to be configured to withstand or minimize the risk of DoS attacks. This can be partially achieved if the application server provides configuration options that limit the number of allowed concurrent HTTP connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Deployments' 3. Sort 'Deployments' table by 'Type' by click the column header 4. Select an 'Enterprise Application' or 'Web Application' to check the session timeout setting 5. Select 'Configuration' tab -> 'Application' tab for deployments of 'Enterprise Application' type Select 'Configuration' tab -> 'General' tab for deployments of 'Web Application' type 6. Ensure 'Maximum in-memory Session' field value is set to an integer value at or lower than an acceptable maximum number of HTTP sessions If a value is not set in the 'Maximum in-memory Session' field for all deployments, this is a finding.

## Group: SRG-APP-000435-AS-000163

**Group ID:** `V-235990`

### Rule: Oracle WebLogic must limit the use of resources by priority and not impede the host from servicing processes designated as a higher-priority.

**Rule ID:** `SV-235990r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Priority protection helps the application server prevent a lower-priority application process from delaying or interfering with any higher-priority application processes. If the application server is not capable of managing application resource requests, the application server could become overwhelmed by a high volume of low-priority resource requests which can cause an availability issue. This requirement only applies to Mission Assurance Category 1 systems and does not apply to information systems with a Mission Assurance Category of 2 or 3.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Environment' -> 'Work Managers' 3. Existing Work Managers will appear in the list If Work Managers are not created to allow prioritization of resources, this is a finding.

## Group: SRG-APP-000225-AS-000166

**Group ID:** `V-235991`

### Rule: Oracle WebLogic must fail securely in the event of an operational failure.

**Rule ID:** `SV-235991r961122_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> Fail secure is a condition achieved by the application server in order to ensure that in the event of an operational failure, the system does not enter into an unsecure state where intended security properties no longer hold. An example of secure failure is when an application server is configured for secure LDAP (LDAPS) authentication. If the application server fails to make a successful LDAPS connection it does not try to use unencrypted LDAP instead.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Monitoring' -> 'Port Usage' 3. In the results table, ensure values in the 'Protocol' column each end with 's' (secure) If the protocols are not secure, this is a finding.

## Group: SRG-APP-000440-AS-000167

**Group ID:** `V-235992`

### Rule: Oracle WebLogic must employ approved cryptographic mechanisms when transmitting sensitive data.

**Rule ID:** `SV-235992r961635_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that application servers take measures to employ approved cryptography in order to protect the information during transmission over the network. This is usually achieved through the use of Transport Layer Security (TLS), SSL VPN, or IPSEC tunnel. If data in transit is unencrypted, it is vulnerable to disclosure. If approved cryptographic algorithms are not used, encryption strength cannot be assured. The application server must utilize approved encryption when transmitting sensitive data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Environment' -> 'Servers' 3. From the list of servers, select one which needs check for SSL configuration verification 4. From 'Configuration' tab -> 'General' tab, ensure 'Listen Port Enabled' checkbox is deselected 5. Ensure 'SSL Listen Port Enabled' checkbox is selected and a valid port number is in 'SSL Listen Port' field, e.g., 7002 6. Repeat steps 3-5 for all servers requiring SSL configuration checking If any of the servers requiring cryptographic mechanisms does not have 'SSL List Port Enabled', this is a finding.

## Group: SRG-APP-000266-AS-000168

**Group ID:** `V-235993`

### Rule: Oracle WebLogic must identify potentially security-relevant error conditions.

**Rule ID:** `SV-235993r961167_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The structure and content of error messages need to be carefully considered by the organization and development team. The extent to which the application server is able to identify and handle error conditions is guided by organizational policy and operational requirements. Adequate logging levels and system performance capabilities need to be balanced with data protection requirements. Application servers must have the capability to log at various levels which can provide log entries for potential security-related error events. An example is the capability for the application server to assign a criticality level to a failed login attempt error message, a security-related error message being of a higher criticality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Expand the domain from the navigation tree, and select the AdminServer 3. Use the dropdown to select 'WebLogic Server' -> 'Logs' -> 'Log Configuration' 4. Select the 'Log Levels' tab, and within the table, expand 'Root Logger' node 5. Log levels for system-related events can be set here 6. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Security' -> 'Audit Policy' 7. Select 'Oracle Platform Security Services' from the 'Audit Component Name' dropdown 8. Log levels for security-related events can be set here If security-related events are not set properly, this is a finding.

## Group: SRG-APP-000266-AS-000169

**Group ID:** `V-235994`

### Rule: Oracle WebLogic must only generate error messages that provide information necessary for corrective actions without revealing sensitive or potentially harmful information in error logs and administrative messages.

**Rule ID:** `SV-235994r961167_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any application providing too much information in error logs and in administrative messages to the screen risks compromising the data and security of the application and system. The structure and content of error messages needs to be carefully considered by the organization and development team. The application server must not log sensitive information such as passwords, private keys, or other sensitive data. This requirement pertains to logs that are generated by the application server and application server processes, not the applications that may reside on the application server. Those errors are out of the scope of these requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access EM 2. Select the domain from the navigation tree, and use the dropdown to select 'WebLogic Domain' -> 'Logs' -> 'View Log Messages' 3. Within the search criteria, click 'Add Fields' button 4. Notice the list of available fields do not contain sensitive data If sensitive or potentially harmful information, such as passwords, private keys or other sensitive data, is part of the error logs or administrative messages, this is a finding.

## Group: SRG-APP-000267-AS-000170

**Group ID:** `V-235995`

### Rule: Oracle WebLogic must restrict error messages so only authorized personnel may view them.

**Rule ID:** `SV-235995r961170_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the application provides too much information in error logs and administrative messages to the screen, this could lead to compromise. The structure and content of error messages need to be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements. Application servers must protect the error messages that are created by the application server. All application server users' accounts are used for the management of the server and the applications residing on the application server. All accounts are assigned to a certain role with corresponding access rights. The application server must restrict access to error messages so only authorized personnel may view them. Error messages are usually written to logs contained on the file system. The application server will usually create new log files as needed and must take steps to ensure that the proper file permissions are utilized when the log files are created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Security Realms' 3. Select realm to configure (default is 'myrealm') 4. Select 'Users and Groups' tab -> 'Users' tab 5. From 'Users' table, select a user that must not have access to view error messages 6. From users settings page, select 'Groups' tab 7. Ensure the 'Chosen' table does not contain any of the following roles - 'Admin', 'Deployer', 'Monitor', 'Operator' 8. Repeat steps 5-7 for all users that must not have access to view error messages If any user that should not be able to view error messages has the roles of 'Admin', 'Deployer', 'Monitor' or 'Operator', this is a finding.

## Group: SRG-APP-000108-AS-000067

**Group ID:** `V-235996`

### Rule: Oracle WebLogic must provide system notifications to a list of response personnel who are identified by name and/or role.

**Rule ID:** `SV-235996r960912_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Incident response applications are, by their nature, designed to monitor, detect, and alarm on defined events occurring on the system or on the network. A large part of their functionality is the accurate and timely notification of events. Application servers can act as a resource for incident responders by providing information and notifications needed for support personnel to respond to application server incidents. Notifications can be made more efficient by the utilization of groups containing the members who would be responding to a particular alarm or event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access AC 2. From 'Domain Structure', select 'Diagnostics' -> 'Diagnostic Modules' 3. Select 'Module-HealthState' from 'Diagnostic System Modules' list 4. Select 'Configuration' tab -> 'Watches and Notifications' tab. Select the 'Watches' tab from the bottom of page 5. Ensure 'ServerHealthWatch' row has 'Enabled' column value set to 'true' 6. Select 'Configuration' tab -> 'Watches and Notifications' tab. Select the 'Notifications' tab from the bottom of page 7. Ensure 'ServerHealthNotification' row has 'Enable Notification' column value set to 'true' If 'ServerHealthNotification' is set to false, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-235997`

### Rule: Oracle WebLogic must be integrated with a tool to monitor audit subsystem failure notification information that is sent out (e.g., the recipients of the message and the nature of the failure).

**Rule ID:** `SV-235997r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> It is critical that, when a system is at risk of failing to process audit logs, it detects and takes action to mitigate the failure. As part of the mitigation, the system must send a notification to designated individuals that auditing is failing, log the notification message and the individuals who received the notification. When the system is not capable of notification and notification logging, an external software package, such as Oracle Diagnostic Framework, must be used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of Oracle WebLogic to determine if a tool, such as Oracle Diagnostic Framework, is in place to monitor audit subsystem failure notification information that is sent out. If a tool is not in place to monitor audit subsystem failure notification information that is sent, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-235998`

### Rule: Oracle WebLogic must be managed through a centralized enterprise tool.

**Rule ID:** `SV-235998r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The application server can host multiple applications which require different functions to operate successfully but many of the functions are capabilities that are needed for all the hosted applications and should be managed through a common interface. Examples of enterprise wide functions are automated rollback of changes, failover and patching. These functions are often outside the domain of the application server and so the application server must be integrated with a tool, such as Oracle Enterprise Manager, which is specific built to handle these requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Oracle WebLogic configuration to determine if a tool, such as Oracle Enterprise Manager, is in place to centrally manage enterprise functionality needed for Oracle WebLogic. If a tool is not in place to centrally manage enterprise functionality, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-235999`

### Rule: Oracle WebLogic must be integrated with a tool to implement multi-factor user authentication.

**Rule ID:** `SV-235999r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Multifactor authentication is defined as: using two or more factors to achieve authentication. Factors include: (i) something a user knows (e.g., password/PIN); (ii) something a user has (e.g., cryptographic identification device, token); or (iii) something a user is (e.g., biometric). A CAC meets this definition. Implementing a tool, such as Oracle Access Manager, will implement multi-factor authentication to the application server and tie the authenticated user to a user account (i.e. roles and privileges) assigned to the authenticated user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the WebLogic configuration to determine if a tool, such as Oracle Access Manager, is in place to implement multi-factor authentication for the users. If a tool is not in place to implement multi-factor authentication, this is a finding.

## Group: SRG-APP-000456-AS-000266

**Group ID:** `V-270883`

### Rule: The version of Oracle WebLogic running on the system must be a supported version.

**Rule ID:** `SV-270883r1051416_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Oracle WebLogic 12c is no longer supported by the vendor. If the system is running Oracle WebLogic 12c, this is a finding.

