# STIG Benchmark: Tanium 7.3 Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000111

**Group ID:** `V-234031`

### Rule: Tanium must centrally review and analyze audit records from multiple components within the system.

**Rule ID:** `SV-234031r960918_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Successful incident response and auditing relies on timely, accurate system information and analysis in order to allow the organization to identify and respond to potential incidents in a proficient manner. If the application does not provide the ability to centrally review the application logs, forensic analysis is negatively impacted. Segregation of logging data to multiple disparate computer systems is counterproductive and makes log analysis and log event alarming difficult to implement and manage, particularly when the system or application has multiple logging components written to different locations or systems. Automated mechanisms for centralized reviews and analyses include, for example, Security Information Management products.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to Tanium, access the Tanium web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Connect". Review the configured sources under "Configured Sources and Destinations" section. If an "Audit Log" source does not exist, this is a finding.

## Group: SRG-APP-000379

**Group ID:** `V-234032`

### Rule: Tanium must implement organization-defined automated security responses if baseline configurations are changed in an unauthorized manner.

**Rule ID:** `SV-234032r961458_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to the system. Changes to information system configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of the application. Examples of security responses include, but are not limited to the following: halting application processing; halting selected application functions; or issuing alerts/notifications to organizational personnel when there is an unauthorized modification of a configuration item.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on the module "Integrity Monitor". Click on "Monitors" from the left menu. Ensure "Monitors" are deployed with applicable Watchlists and Endpoints. Record any that have a number greater than "0" otherwise, this is a finding. If using third party integrity monitoring tools, this is Not Applicable.

## Group: SRG-APP-000386

**Group ID:** `V-234033`

### Rule: Tanium must employ a deny-all, permit-by-exception (whitelist) policy to allow the execution of authorized software programs.

**Rule ID:** `SV-234033r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Utilizing a whitelist provides a configuration management method for allowing the execution of only authorized software. Using only authorized software decreases risk by limiting the number of potential vulnerabilities. The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. Verification of whitelisted software can occur either prior to execution or at system startup. This requirement applies to configuration management applications or similar types of applications designed to manage system processes and configurations (e.g., HBSS and software wrappers).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system, which has connectivity to the Tanium Server, access the Tanium Server web user interface (UI) and log on with CAC. Click on the navigation button (menu) on the top left of the console. Click on the "Protect Workbench". Select the arrow on the left-hand side to expand the menu. Click on "Policies". Click on the Policy with Policy Type named "AppLocker". If there is no policy type defined for "AppLocker", this is a finding. Ensure the computer group containing the Tanium server is showing as online and enforced. If the "AppLocker" policy enforcement does not contain the Tanium Server, then this is a finding. Under Policy Details ensure the Mode is set to "Blocking". If Mode is not set to "Blocking", this is a finding. Under "Policy Details" expand the arrow next to "Everyone". If all files are allowed, this is a finding. If additional paths are found, such as %PROGRAMFILES%\", "%WINDIR%" and "?:\Program Files\Tanium Server\", they must be documented. If additional file paths are found and have not been documented, this is a finding. If Tanium Protect is not available, this is not applicable.

## Group: SRG-APP-000414

**Group ID:** `V-234034`

### Rule: The vulnerability scanning application must implement privileged access authorization to all Tanium information systems and infrastructure components for selected organization-defined vulnerability scanning activities.

**Rule ID:** `SV-234034r961563_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, the nature of the vulnerability scanning may be more intrusive, or the information system component that is the subject of the scanning may contain highly sensitive information. Privileged access authorization to selected system components facilitates more thorough vulnerability scanning and also protects the sensitive nature of such scanning. The vulnerability scanning application must utilize privileged access authorization for the scanning account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to review the documented list of Tanium users. If any users have access to Tanium Comply and are not on the list of documented users, this is a finding. If Tanium Comply is not installed, this check is Not Applicable.

## Group: SRG-APP-000015

**Group ID:** `V-234035`

### Rule: The Tanium endpoint must have the Tanium Servers public key in its installation.

**Rule ID:** `SV-234035r960762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. Satisfies: SRG-APP-000015, SRG-APP-000158, SRG-APP-000394</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Tanium endpoint makes a connection to the Tanium Server; the endpoint's copy of the Tanium Server's public key is used to verify the validity of the registration day coming from the Tanium Server. If any endpoint systems do not have the correct Tanium Server public key in its configuration, they will not perform any instructions from the Tanium Server and a record of those endpoints will be listed in the Tanium Server's System Status. To validate, Click on the navigation button (hamburger menu) on the top left of the console. Click on "Administration". Select the "System Status" tab. Change "Show systems that have reported in the last:", enter "7" in the first field. Select "Days" from the drop down menu in the second field to determine if any endpoints connected with an invalid key. If any systems are listed with "No" in the "Valid Key" column, this is a finding.

## Group: SRG-APP-000119

**Group ID:** `V-234036`

### Rule: Access to Tanium logs on each endpoint must be restricted by permissions.

**Rule ID:** `SV-234036r960933_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For the Tanium Client software to run without impact from external negligent or malicious changes, the permissions on the Tanium log files and their directory must be restricted. Tanium is deployed with a Client Hardening Solution. This solution, when applied, will ensure directory permissions are in place.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Actions". Click on "Scheduled Actions". Look for a scheduled action titled "Client Service Hardening - Set SYSTEM only permissions on Tanium Client directory". If a scheduled action titled "Client Service Hardening - Set SYSTEM only permissions on Tanium Client directory" does not exist, or there is a Scheduled Action contradicting the "Client Service Hardening - Set SYSTEM only permissions on Tanium Client directory" scheduled action, this is a finding. If the scheduled action exists, select it and if it is not approved (the "Approve" button at the top of the section will be displayed if not approved), this is a finding.

## Group: SRG-APP-000131

**Group ID:** `V-234037`

### Rule: The Tanium cryptographic signing capabilities must be enabled on the Tanium Clients to safeguard the authenticity of communications sessions when answering requests from the Tanium Server.

**Rule ID:** `SV-234037r960954_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All of Tanium's signing capabilities should be enabled upon install. Tanium supports the cryptographic signing and verification before execution of all Sensors, Questions, Actions, Sensor Libraries, File Shards, etc. Enabling signing does away with the ability of an attacker to conduct Man in the Middle (MitM) attacks for the purposes of remote code execution and precludes the modification of the aforementioned data elements in transit. Additionally, Tanium supports object level signing for content ingested into the Tanium platform. This allows for the detection and rejection of changes to objects (sensors, actions, etc.) by even a privileged user within Tanium. Tanium has built-in signing capabilities enabled by default when installed. Cryptographic signing and verification of all Sensors, Questions, Actions, Sensor Libraries, File Shards, etc. before execution will be enforced by Tanium. Signing will prevent MitM remote code execution attacks and will protect data element in transit. Tanium also supports object level signing for content within the Tanium platform. Satisfies: SRG-APP-000131, SRG-APP-000219</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Administration". Select the "Global Settings" tab. In the "Show Settings Containing:" search box type "AllQuestionsRequireSignatureFlag". Click "Enter". If no results are returned, this is a finding. If results are returned for "AllQuestionsRequireSignatureFlag" but the value is not "1", this is a finding.

## Group: SRG-APP-000142

**Group ID:** `V-234038`

### Rule: Firewall rules must be configured on the Tanium Endpoints for Client-to-Server communications.

**Rule ID:** `SV-234038r1043177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In addition to the client-to-server TCP communication that takes place over port 17472, Tanium Clients also communicate to other Tanium-managed computers over port 17472. The Tanium environment can perform hundreds or thousands of times faster than other security or systems management tools because the Tanium Clients communicate in secure, linearly-controlled peer-to-peer rings. Because clients dynamically communicate with other nearby agents based on proximity and latency, rings tend to form automatically to match a customer's topology--endpoints in California will form one ring while endpoints in Germany will form a separate ring. https://docs.tanium.com/platform_install/platform_install/reference_network_ports.html.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This check is performed for the Tanium Endpoints and must be validated against the HBSS desktop firewall policy applied to the Endpoints. Consult with the HBSS administration for assistance. Validate a rule exists within the HBSS HIPS firewall policies for managed clients for the following: Port Needed: Tanium Clients or Zone Clients over TCP port 17472, bi-directionally. If a host-based firewall rule does not exist to allow TCP port 17472, bi-directionally, this is a finding. Consult with the network firewall administrator and validate rules exist for the following: Allow TCP traffic on port 17472 from any computer to be managed on a local area network to any other computer to be managed on the same local area network. If a network firewall rule does not exist to allow TCP port 17472 from any managed computer to any other managed computer on the same local area network, this is a finding.

## Group: SRG-APP-000328

**Group ID:** `V-234039`

### Rule: Control of the Tanium Client service must be restricted to SYSTEM access only for all managed clients.

**Rule ID:** `SV-234039r961317_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The reliability of the Tanium client's ability to operate depends upon controlling access to the Tanium client service. By restricting access to SYSTEM access only, the non-Tanium system administrator will not have the ability to impact operability of the service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Administration". Select the "Scheduled Actions" tab. Look for a scheduled action titled "Client Service Hardening - Allow Only Local SYSTEM to Control Service". If a scheduled action titled "Client Service Hardening - Allow Only Local SYSTEM to Control Service" does not exist, this is a finding. If the scheduled action exists, select it and if it is not approved (the "Approve" button at the top of the section will be displayed if not approved), this is a finding. If the scheduled action exists and has been approved but does not restrict control of the Tanium Client service to Allow Only Local SYSTEM to Control Service, this is a finding. If the action is not configured to repeat at least once every 24 hours, this is a finding. If the scheduled action is not targeted at an "All Computers" Action Group, this is a finding.

## Group: SRG-APP-000328

**Group ID:** `V-234040`

### Rule: The ability to uninstall the Tanium Client service must be disabled on all managed clients.

**Rule ID:** `SV-234040r961317_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, end users have the ability to uninstall software on their clients. In the event the Tanium Client software is uninstalled, the Tanium Server is unable to manage the client and must redeploy to the client. Preventing the software from being displayed in the client's Add/Remove Programs will lessen the risk of the software being uninstalled by non-Tanium System Administrators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Administration". Select the "Scheduled Actions" tab. Look for a scheduled action titled "Client Service Hardening - Hide Client from Add-Remove Programs". If a scheduled action titled "Client Service Hardening - Hide Client from Add-Remove Programs" does not exist, this is a finding. If the scheduled action exists, select it and if it is not approved (the "Approve" button at the top of the section will be displayed if not approved), this is a finding. If the scheduled action exists and has been approved but does not disable the visibility of the client in Add-Remove Programs, this is a finding. If the action is not configured to repeat at least every hour, this is a finding. If the scheduled action is not targeted at an "All Computers" Action Group, this is a finding.

## Group: SRG-APP-000328

**Group ID:** `V-234041`

### Rule: The permissions on the Tanium Client directory must be restricted to only the SYSTEM account on all managed clients.

**Rule ID:** `SV-234041r961317_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By restricting access to the Tanium Client directory on managed clients, the Tanium client's ability to operate and function as designed will be protected from malicious attack and unintentional modifications by end users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Administration". Select the "Scheduled Actions" tab. Look for a scheduled action titled "Client Service Hardening - Set SYSTEM only permissions on the Tanium Client directory". If a scheduled action titled "Client Service Hardening - Set SYSTEM only permissions on the Tanium Client directory" does not exist, this is a finding. If the scheduled action exists, select it and if it is not approved (the "Approve" button at the top of the section will be displayed if not approved), this is a finding. If the scheduled action exists and has been approved but does not disable the visibility of the client in Add-Remove Programs, this is a finding. If the action is not configured to repeat at least every hour, this is a finding. If the scheduled action is not targeted at an "All Computers" Action Group, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-234042`

### Rule: Tanium endpoint files must be excluded from on-access antivirus actions.

**Rule ID:** `SV-234042r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Similar to any other host-based applications, the Tanium Client is subject to the restrictions other System-level software may place on an operating environment. That is to say that Antivirus, IPS, Encryption, or other security and management stack software may disallow the Client from working as expected. https://docs.tanium.com/platform_install/platform_install/reference_host_system_security_exceptions.html.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to determine the antivirus used on the Tanium clients. Review the settings of the antivirus software. Validate exclusions exist which exclude the Tanium program files from being scanned by antivirus on-access scans. If exclusions do not exist, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-234043`

### Rule: The Tanium Client Deployment Tool (CDT) must not be configured to use the psexec method of deployment.

**Rule ID:** `SV-234043r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When using the Tanium Client Deployment Tool (CDT), using psexec represents an increased vulnerability as the NTLM hash and clear text passwords of the authenticating user is exposed in the memory of the remote system. To mitigate this vulnerability, the psexec method of deployment must not be used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium Module Server interactively. Log on to the server with an account that has administrative privileges. Navigate to Program Files(x86) >> Tanium >> Tanium Client Deployment Tool. If the file "psexec.exe" exists, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-234044`

### Rule: Tanium endpoint files must be protected from file encryption actions.

**Rule ID:** `SV-234044r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Similar to any other host-based applications, the Tanium Client is subject to the restrictions other System-level software may place on an operating environment. That is to say that Antivirus, Encryption, or other security and management stack software may disallow the Client from working as expected. https://docs.tanium.com/platform_install/platform_install/reference_host_system_security_exceptions.html.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to determine the file-based encryption software used on the Tanium clients. Review the settings for the file-based encryption software. Validate exclusions exist which exclude the Tanium program files from being encrypted by the file-based encryption software. If exclusions do not exist, this is a finding.

## Group: SRG-APP-000246

**Group ID:** `V-234045`

### Rule: The Tanium application must restrict the ability of individuals to place too much impact upon the network, which might result in a Denial of Service (DoS) event on the network by using RandomSensorDelayInSeconds.

**Rule ID:** `SV-234045r961152_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition where a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Individuals of concern can include hostile insiders or external adversaries that have successfully breached the information system and are using the system as a platform to launch cyberattacks on third-parties. Applications and application developers must take the steps needed to ensure users cannot use an authorized application to launch DoS attacks against other systems and networks. For example, applications may include mechanisms that throttle network traffic so users are not able to generate unlimited network traffic via the application. Limiting system resources that are allocated to any user to a bare minimum may also reduce the ability of users to launch some DoS attacks. The methods employed to counter this risk will be dependent upon the application layer methods that can be used to exploit it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Administration". Select the "Global Settings" tab. In the "Show Settings Containing:" search box type "RandomSensorDelayInSeconds". Click "Enter". If no results are returned, this is a finding. If results are returned for "RandomSensorDelayInSeconds", but do not match the defined value in the system documentation, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-234046`

### Rule: Tanium endpoint files must be excluded from host-based intrusion prevention intervention.

**Rule ID:** `SV-234046r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Similar to any other host-based applications, the Tanium Client is subject to the restrictions other System-level software may place on an operating environment. Antivirus, IPS, Encryption, or other security and management stack software may disallow the Tanium Server from working as expected. https://docs.tanium.com/platform_install/platform_install/reference_host_system_security_exceptions.html.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to determine the HIPS software used on the Tanium Clients. Review the settings of the HIPS software. Validate exclusions exist which exclude the Tanium program files from being restricted by HIPS. If exclusions do not exist, this is a finding.

## Group: SRG-APP-000002

**Group ID:** `V-234047`

### Rule: The Tanium application must retain the session lock until the user reestablishes access using established identification and authentication procedures.

**Rule ID:** `SV-234047r960738_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system, but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. This is typically determined and performed at the operating system-level, but in some instances it may be at the application-level. Regardless of where the session lock is determined and implemented, once invoked the session lock shall remain in place until the user re-authenticates. No other system or application activity aside from re-authentication shall unlock the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium Server interactively. Log on to the server with an account that has administrative privileges. Run regedit as Administrator. Navigate to HKEY_LOCAL_MACHINE >> SOFTWARE >> Wow6432Node >> Tanium >> Tanium Server. Validate the value for REG_DWORD "ForceSOAPSSLClientCert" is set to "1". Navigate to HKEY_LOCAL_MACHINE >> SOFTWARE >> Wow6432Node >> Tanium >> Tanium Server. Validate the following keys exist and are configured: REG_SZ "ClientCertificateAuthField" For example: X509v3 Subject Alternative Name. REG_SZ "ClientCertificateAuthRegex" For example-DoD: .*\:\s*([^@]+)@.* $Note: This regedit should be valid for any Subject Alternative Name entry. REG_SZ "ClientCertificateAuth" Note: This registry value defines which certificate file to use for authentication. For example: C:\Program Files\Tanium\Tanium Server\dod.pem REG_SZ "cac_ldap_server_url" Note: This registry value requires that Tanium validate every CAC/PIV authentication attempt with AD to determine the state of the account that is logging in. It must use the syntax similar to LDAP://<AD instance FQDN> If the value for REG_DWORD "ForceSOAPSSLClientCert" is not set to "1" and the remaining registry values are not configured, this is a finding.

## Group: SRG-APP-000233

**Group ID:** `V-234048`

### Rule: The Tanium Application Server must be configured with a connector to sync to Microsoft Active Directory for account management functions.

**Rule ID:** `SV-234048r961131_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By restricting access to the Tanium Server to only Microsoft Active Directory, user accounts and related permissions can be strictly monitored. Account management will be under the operational responsibility of the System Administrator for the Windows Operation System Active Directory. Satisfies: SRG-APP-000233, SRG-APP-000317</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI) and log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console, then click on "Configuration". Click the down arrow to view Apps. Find "LDAP Sync". Verify a sync exists under "Enabled Servers". If no sync exists, this is a finding. If sync exists under "Disabled Servers", this is a finding.

## Group: SRG-APP-000023

**Group ID:** `V-234049`

### Rule: The Tanium Application Server must be configured to only use Microsoft Active Directory for account management functions.

**Rule ID:** `SV-234049r1043176_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By restricting access to the Tanium Server to only Microsoft Active Directory, user accounts and related permissions can be strictly monitored. Account management will be under the operational responsibility of the System Administrator for the Windows Operation System Active Directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Administration". Select the "Users" tab. Consult with the Tanium System Administrator to review the documented list of Tanium users. Compare the list of Tanium users versus the users found in the appropriate Active Directory security groups for the User Roles. If there are any console users who are listed in the Tanium console that are not found in a synced Active Directory security group, this is a finding. Alternatively, the ISSO can document the non-synced Active Directory security group users and accept the risk for the users. If this is the case, this would no longer be a finding.

## Group: SRG-APP-000033

**Group ID:** `V-234050`

### Rule: Tanium Computer Groups must be used to restrict console users from affecting changes to unauthorized computers.

**Rule ID:** `SV-234050r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Computer Groups allow a site running Tanium to assign responsibility of specific Computer Groups to specific Tanium console users. By doing so, a desktop administrator, for example, will not have the ability to enforce an action against a high visibility server. For large sites, it is crucial to have the Computer Groups and while a smaller site might not seem to require Computer Groups, creating them provides for a cleaner implementation. All sites will be required to have some kind of Computer Groups configured other than the default "All Computers".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Administration". Select the "Computer Groups" tab. Under the "Name" column, verify specific groups exist other than the default "All Computers" and "No Computers". If site or organization specific computer groups do not exist, this is a finding.

## Group: SRG-APP-000033

**Group ID:** `V-234051`

### Rule: Documentation identifying Tanium console users, their respective functional roles, and computer groups must be maintained.

**Rule ID:** `SV-234051r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System access should be reviewed periodically to verify that all Tanium users are assigned the appropriate functional role, with the least privileged access possible to perform assigned tasks being the recommended best practice. Users who have been removed from the documentation should no longer be configured as a Tanium Console User. Consider removing users that have not logged onto the system within a predetermined time frame. When using Active Directory synchronization, as is required by this STIG, User Roles assignments are via the LDAP Sync. To change a Tanium user's functional role, their Active Directory account needs to be assigned to the AD security group, which correlates with the applicable functional role.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to review the documented list of Tanium users. The users' functional roles, computer groups, and correlated Active Directory security groups must be documented. If the site does not have the Tanium users and their respective functional roles, computer groups, and correlated Active Directory security groups documented, this is a finding.

## Group: SRG-APP-000033

**Group ID:** `V-234052`

### Rule: Role-based system access must be configured to least privileged access to Tanium Server functions through the Tanium interface.

**Rule ID:** `SV-234052r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>User accessibility to various Tanium Server functions performed via the console can be restricted by functional roles, a combination of User Role(s), and Content Set(s) assigned through User Group membership. Functional roles are assigned to users via Active Directory Group membership. System access should be reviewed periodically to verify that all Tanium users are assigned the appropriate functional role, with the least privileged access possible to perform assigned tasks being the recommended best practice. Consider removing users that have not logged onto the system within a predetermined time frame.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to review the documented list of Tanium users. Analyze the users configured in the Tanium interface. Review the users' respective approved roles, as well as the correlated Active Directory Group for the Tanium functional roles. Validate Active Directory Groups/Tanium functional roles are documented to assign least privileged access to the functions of the Tanium Server through the Tanium interface. If the documentation does not reflect a granular, least privileged access approach to the Active Directory Groups/Tanium functional roles assignment, this is a finding.

## Group: SRG-APP-000033

**Group ID:** `V-234053`

### Rule: Tanium console users User Roles must be validated against the documentation for User Roles.

**Rule ID:** `SV-234053r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System access should be reviewed periodically to verify that all Tanium users are assigned the appropriate role, with the least privileged access possible to perform assigned tasks being the recommended best practice. Users who have been removed from the documentation should no longer be configured as a Tanium Console User. Consider removing users that have not logged onto the system within a predetermined time frame. When using Active Directory synchronization, as is required by this STIG, User Roles assignments are via the LDAP Sync, AD security groups correlate, one to one, to Tanium User Roles. To change a Tanium user's User Role, their Active Directory account needs to be moved to the AD security group, which correlates with the applicable User Role.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Administration". Select the "Users" tab. Verify each user against the Tanium-approved users list. Review the assigned roles for each user against the "User Functional Role" column. If any user exists in Tanium but is not on the Tanium-approved users list and/or if any user exists in Tanium at a more elevated User Functional Role than that documented on the list, this is a finding.

## Group: SRG-APP-000033

**Group ID:** `V-234054`

### Rule: Documentation identifying Tanium console users and their respective Computer Group rights must be maintained.

**Rule ID:** `SV-234054r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System access should be reviewed periodically to verify that all Tanium users are assigned the appropriate role, with the least privileged access possible to perform assigned tasks being the recommended best practice. Users who have been removed from the documentation should no longer be configured as a Tanium Console User. Consider removing users that have not logged onto the system within a predetermined time frame.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to review the documented list of Tanium users and their respective, approved Computer Group rights. If the documented list does not have the Tanium users and their respective, approved Computer Group rights documented, this is a finding.

## Group: SRG-APP-000033

**Group ID:** `V-234055`

### Rule: Tanium console users Computer Group rights must be validated against the documentation for Computer Group rights.

**Rule ID:** `SV-234055r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System access should be reviewed periodically to verify that all Tanium users are assigned the appropriate role, with the least privileged access possible to perform assigned tasks being the recommended best practice. Users who have been removed from the documentation should no longer be configured as a Tanium Console User. Consider removing users that have not logged onto the system within a predetermined time frame.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Administration". Select the "Users" tab. Verify each user against the approved users list. Review the assigned Computer Groups for each user by selecting the user then clicking view user. View Computer Groups for the user. If any user exists in Tanium but is not on the Tanium-approved users list and/or if any user exists in Tanium with more Computer Groups than documented, this is a finding.

## Group: SRG-APP-000149

**Group ID:** `V-234056`

### Rule: Common Access Card (CAC)-based authentication must be enabled on the Tanium Server for network access with privileged accounts.

**Rule ID:** `SV-234056r960972_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses, except the following: (i) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and (ii) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. This not only meets a common requirement in the Federal space but adds a critical layer of security to the user authentication process. Satisfies: SRG-APP-000149, SRG-APP-000151</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium Server interactively. Log on to the server with an account that has administrative privileges. Run regedit as Administrator. Navigate to HKEY_LOCAL_MACHINE >> SOFTWARE >> Wow6432Node >> Tanium >> Tanium Server. Validate the value for REG_DWORD "ForceSOAPSSLClientCert" is set to "1". Navigate to HKEY_LOCAL_MACHINE >> SOFTWARE >> Wow6432Node >> Tanium >> Tanium Server. Validate the following keys exist and are configured: REG_SZ "ClientCertificateAuthField" For example: X509v3 Subject Alternative Name. REG_SZ "ClientCertificateAuthRegex" For example-DoD: .*\:\s*([^@]+)@.* $Note: This regedit should be valid for any Subject Alternative Name entry. REG_SZ "ClientCertificateAuth" Note: This registry value defines which certificate file to use for authentication. For example: C:\Program Files\Tanium\Tanium Server\dod.pem REG_SZ "cac_ldap_server_url" Note: This registry value requires that Tanium validate every CAC/PIV authentication attempt with AD to determine the state of the account that is logging on. It must use the syntax similar to LDAP://<AD instance FQDN>. If the value for REG_DWORD "ForceSOAPSSLClientCert" is not set to "1" and the remaining registry values are not configured, this is a finding.

## Group: SRG-APP-000383

**Group ID:** `V-234057`

### Rule: Firewall rules must be configured on the Tanium Server for Console-to-Server communications.

**Rule ID:** `SV-234057r961470_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An HTML5 based application, the Tanium Console runs from any device with a browser that supports HTML5. For security, the HTTP and SOAP communication to the Tanium Server is SSL encrypted, so the Tanium Server installer configures the server to listen for HTTP and SOAP requests on port 443. Without a proper connection to the Tanium Server, access to the system capabilities could be denied. Port Needed: To Tanium Server over TCP port 443. Network firewall rules: Allow HTTP traffic on TCP port 443 from any computer on the internal network to the Tanium Server device. https://docs.tanium.com/platform_install/platform_install/reference_network_ports.html.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to verify which firewall is being used as a host-based firewall on the Tanium Server. Access the host-based firewall configuration on the Tanium Server. Validate a rule exists for the following: Port Needed: From only designated Tanium console user clients to Tanium Server over TCP port 443. If a host-based firewall rule does not exist to allow only designated Tanium console user clients to Tanium Server over TCP port 443, this is a finding. Consult with the network firewall administrator and validate rules exist for the following: Allow TCP traffic from only designated Tanium console user clients to Tanium Server over TCP ports 443. If a network firewall rule does not exist to allow traffic from only designated Tanium console user clients to Tanium Server over TCP port 443, this is a finding.

## Group: SRG-APP-000070

**Group ID:** `V-234058`

### Rule: The publicly accessible Tanium application must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the application.

**Rule ID:** `SV-234058r960849_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible application ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with DTM-08-060. Use the following verbiage for desktops, laptops, and other devices accommodating banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." Satisfies: SRG-APP-000070, SRG-APP-000068, SRG-APP-000069</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). If a DoD-approved use notification banner does not display prior to logon, this is a finding.

## Group: SRG-APP-000108

**Group ID:** `V-234059`

### Rule: Tanium must alert the ISSO and SA (at a minimum) in the event of an audit processing failure.

**Rule ID:** `SV-234059r960912_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Connect". Review the configured Sources. If no "Sources" exist to send audit logs from the Tanium SQL Server to a SIEM tool, this is a finding. Work with the SIEM administrator to determine if an alert is configured when audit data is no longer received as expected. If there is no alert configured, this is a finding.

## Group: SRG-APP-000270

**Group ID:** `V-234060`

### Rule: Flaw remediation Tanium applications must employ automated mechanisms to determine the state of information system components with regard to flaw remediation using the following frequency: continuously, where HBSS is used; 30 days, for any additional internal network scans not covered by HBSS; and annually, for external scans by Computer Network Defense Service Provider (CNDSP).

**Rule ID:** `SV-234060r961176_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of automated mechanisms to scan for security flaws on a continuous and/or periodic basis, the system components may remain vulnerable to the exploits presented by undetected software flaws. To support this requirement, the flaw remediation application may have automated mechanisms that perform automated scans for security-relevant software updates (e.g., patches, service packs, and hot fixes) and security vulnerabilities of the information system components being monitored. For example, a method of compliance would be an integrated solution incorporating continuous scanning using HBSS and periodic scanning using other tools as specified in the requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Administration". Select the "Scheduled Actions" tab. Look for a scheduled action targeting all machines that is titled either "Patch - Distribute Scan Configuration" or "Patch Management - Run Patch Scan". If there is no Scheduled Action for patching or the Scheduled Action is less frequent than every "30" days, this is a finding.

## Group: SRG-APP-000291

**Group ID:** `V-234061`

### Rule: Tanium must notify SA and ISSO when accounts are created.

**Rule ID:** `SV-234061r961209_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of re-establishing access. One way to accomplish this is for the attacker to simply create a new account. Notification of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail, which documents the creation of application user accounts and notifies administrators and Information System Security Officers (ISSO) exists. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Connect". Review the configured sources. If no sources exists to send audit logs from Tanium to a SIEM tool or Email Destination, this is a finding. Work with the SIEM administrator to determine if an alert is configured when accounts are created. If there is no alert configured, this is a finding.

## Group: SRG-APP-000292

**Group ID:** `V-234062`

### Rule: Tanium must notify SA and ISSO when accounts are modified.

**Rule ID:** `SV-234062r961212_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of re-establishing access. One way to accomplish this is for the attacker to simply modify an existing account. Notification of account modification is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail, which documents the creation of application user accounts and notifies administrators and Information System Security Officers (ISSO) exists. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Connect". Review the configured sources. If no sources exists to send audit logs from the Tanium SQL Server to a SIEM tool or Email Destination, this is a finding. Work with the SIEM administrator to determine if an alert is configured when accounts are modified. If there is no alert configured, this is a finding.

## Group: SRG-APP-000320

**Group ID:** `V-234063`

### Rule: The Tanium application must notify SA and ISSO of account enabling actions.

**Rule ID:** `SV-234063r961293_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of re-establishing access. One way to accomplish this is for the attacker to simply enable a new or disabled account. Notification of account enabling is one method for mitigating this risk. A comprehensive account management process will ensure the existence of an audit trail, which documents the creation of application user accounts and notifies administrators and ISSOs. Such a process greatly reduces the risk that accounts will be surreptitiously enabled and provides logging that can be used for forensic purposes. In order to detect and respond to events that affect user accessibility and application processing, applications must audit account enabling actions and, as required, notify the appropriate individuals so they can investigate the event. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Connect". Review the configured sources. If no sources exists to send audit logs from the Tanium SQL Server to a SIEM tool or Email Destination, this is a finding. Work with the SIEM administrator to determine if an alert is configured when account-enabling actions are performed. If there is no alert configured, this is a finding.

## Group: SRG-APP-000359

**Group ID:** `V-234064`

### Rule: The Tanium application must provide an immediate warning to the SA and ISSO (at a minimum) when allocated audit record storage volume reaches 75% of repository maximum audit record storage capacity.

**Rule ID:** `SV-234064r961398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately upon storage volume utilization reaching 75%, they are unable to plan for storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium system administrator or database administrator to determine the volume on which the Tanium SQL databases are installed. Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Connect". Review the configured Sources. If none exist to send Disk Free Space of the Tanium SQL Server, this is a finding. Work with the SIEM administrator to determine if an alert is configured when Disk Free Space of the Tanium SQL Server reaches below 25%. If there is no alert configured, this is a finding.

## Group: SRG-APP-000360

**Group ID:** `V-234065`

### Rule: The Tanium enterprise audit log reduction option must be configured to provide alerts based off Tanium audit data.

**Rule ID:** `SV-234065r961401_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Connect". Review the configured Tanium Sources listed. If an "Audit Log" source does not exist, this is a finding. Select the "Audit Log" source. Select the audit connection found in the lower half of the screen. Verify the "Destination Type" is a SIEM tool. If the "Destination Type" is not a SIEM tool, this is a finding.

## Group: SRG-APP-000148

**Group ID:** `V-234066`

### Rule: Common Access Card (CAC)-based authentication must be enabled and enforced on the Tanium Server for all access and all accounts.

**Rule ID:** `SV-234066r1051115_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses, except the following: (i) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and (ii) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. Satisfies: SRG-APP-000148, SRG-APP-000005, SRG-APP-000150, SRG-APP-000152, SRG-APP-000080, SRG-APP-000156, SRG-APP-000177, SRG-APP-000185, SRG-APP-000186, SRG-APP-000190, SRG-APP-000315, SRG-APP-000316, SRG-APP-000391, SRG-APP-000392, SRG-APP-000402, SRG-APP-000403</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium Server interactively. Log on to the server with an account that has administrative privileges. Run regedit as Administrator. Navigate to HKEY_LOCAL_MACHINE >> SOFTWARE >> Wow6432Node >> Tanium >> Tanium Server. Validate the value for REG_DWORD "ForceSOAPSSLClientCert" is set to "1". Navigate to HKEY_LOCAL_MACHINE >> SOFTWARE >> Wow6432Node >> Tanium >> Tanium Server. Validate the following keys exist and are configured: REG_SZ "ClientCertificateAuthField" For example: X509v3 Subject Alternative Name REG_SZ "ClientCertificateAuthRegex" For example-DoD: .*\:\s*([^@]+)@.* $Note: This regedit should be valid for any Subject Alternative Name entry. REG_SZ "ClientCertificateAuth" Note: This registry value defines which certificate file to use for authentication. For example: C:\Program Files\Tanium\Tanium Server\dod.pem REG_SZ "cac_ldap_server_url" Note: This registry value requires that Tanium validate every CAC/PIV authentication attempt with AD to determine the state of the account that is logging on. It must use the syntax similar to LDAP://<AD instance FQDN>. If the value for REG_DWORD "ForceSOAPSSLClientCert" is not set to "1" and the remaining registry values are not configured, this is a finding.

## Group: SRG-APP-000293

**Group ID:** `V-234067`

### Rule: Tanium must notify SA and ISSO for account disabling actions.

**Rule ID:** `SV-234067r961215_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When application accounts are disabled, user accessibility is affected. Accounts are utilized for identifying individual application users or for identifying the application processes themselves. In order to detect and respond to events that affect user accessibility and application processing, applications must audit account disabling actions and, as required, notify the appropriate individuals so they can investigate the event. Such a capability greatly reduces the risk that application accessibility will be negatively affected for extended periods of time and also provides logging that can be used for forensic purposes. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Connect". Review the configured sources. If no sources exists to send audit logs from the Tanium SQL Server to a SIEM tool or Email Destination, this is a finding. Work with the SIEM administrator to determine if an alert is configured when accounts are disabled. If there is no alert configured, this is a finding.

## Group: SRG-APP-000294

**Group ID:** `V-234068`

### Rule: Tanium must notify SA and ISSO for account removal actions.

**Rule ID:** `SV-234068r961218_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When application accounts are removed, user accessibility is affected. Accounts are utilized for identifying individual application users or for identifying the application processes themselves. In order to detect and respond to events that affect user accessibility and application processing, applications must audit account removal actions and, as required, notify the appropriate individuals so they can investigate the event. Such a capability greatly reduces the risk that application accessibility will be negatively affected for extended periods of time and also provides logging that can be used for forensic purposes. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Connect". Review the configured sources. If no sources exists to send audit logs from the Tanium SQL Server to a SIEM tool or Email Destination, this is a finding. Work with the SIEM administrator to determine if an alert is configured when accounts are deleted. If there is no alert configured, this is a finding.

## Group: SRG-APP-000378

**Group ID:** `V-234069`

### Rule: The Tanium application must prohibit user installation of software without explicit privileged status.

**Rule ID:** `SV-234069r961455_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing regular users to install software, without explicit privileges, creates the risk that untested or potentially malicious software will be installed on the system. Explicit privileges (escalated or administrative privileges) provide the regular user with explicit capabilities and control that exceeds the rights of a regular user. Application functionality will vary, and while users are not permitted to install unapproved applications, there may be instances where the organization allows the user to install approved software packages such as from an approved software repository. The application must enforce software installation by users based upon what types of software installations are permitted (e.g., updates and security patches to existing software) and what types of installations are prohibited (e.g., software whose pedigree with regard to being potentially malicious is unknown or suspect) by the organization. This requirement applies, for example, to applications that provide the ability to extend application functionality (e.g., plug-ins, add-ons) and software management applications. Satisfies: SRG-APP-000378, SRG-APP-000380, SRG-APP-000121, SRG-APP-000122, SRG-APP-000123</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to review the documented list of Tanium users. Review the users' respective approved roles, as well as the correlated Active Directory security group for the User Roles. Validate Active Directory security groups/Tanium roles are documented to assign least privileged access to the functions of the Tanium Server through the Tanium interface. If the documentation does not reflect a granular, least privileged access approach to the Active Directory Groups/Tanium Roles assignment, this is a finding.

## Group: SRG-APP-000033

**Group ID:** `V-234070`

### Rule: Documentation defining Tanium functional roles must be maintained.

**Rule ID:** `SV-234070r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System access should be reviewed periodically to verify that all Tanium users are assigned the appropriate role, with the least privileged access possible to perform assigned tasks being the recommended best practice. Users who have been removed from the documentation should no longer be configured as a Tanium Console User. Consider removing users that have not logged onto the system within a predetermined time frame.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to review the documented list of Tanium functional roles. If the documentation does not define functional roles, this is a finding.

## Group: SRG-APP-000323

**Group ID:** `V-234071`

### Rule: The Tanium database(s) must be installed on a separate system.

**Rule ID:** `SV-234071r961302_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to protect organizational information from data mining may result in a compromise of information. Data storage objects include, for example, databases, database records, and database fields. Data mining prevention and detection techniques include, for example: limiting the types of responses provided to database queries, limiting the number/frequency of database queries to increase the work factor needed to determine the contents of such databases, and notifying organizational personnel when atypical database queries or accesses occur.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to determine the server to which the database has been installed and is configured. If the customer is using a Tanium Appliance, this is Not Applicable. If the database is installed on the same server as the Tanium Server or Tanium Module Server, this is a finding.

## Group: SRG-APP-000323

**Group ID:** `V-234072`

### Rule: The Tanium application database must be dedicated to only the Tanium application.

**Rule ID:** `SV-234072r961302_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to protect organizational information from data mining may result in a compromise of information. Data storage objects include, for example, databases, database records, and database fields. Data mining prevention and detection techniques include, for example: limiting the types of responses provided to database queries; limiting the number/frequency of database queries to increase the work factor needed to determine the contents of such databases; and notifying organizational personnel when atypical database queries or accesses occur.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
With the Tanium System Administrator's assistance, access the server on which the Tanium database(s) is installed. Review the Tanium database(s). If databases related to products other than Tanium exist in the Tanium database, this is a finding.

## Group: SRG-APP-000381

**Group ID:** `V-234073`

### Rule: The access to the Tanium SQL database must be restricted. Only the designated database administrator(s) can have elevated privileges to the Tanium SQL database.

**Rule ID:** `SV-234073r961464_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>After the Tanium Server has been installed and the Tanium databases created, only the Tanium Receiver, Tanium Module, and Tanium connection manager (ad sync) service needs to access the SQL Server database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium SQL server interactively. Log on to the server with an account that has administrative privileges. Open SQL Server Management Studio. Connect to a Tanium instance of SQL Server. In the left pane, click "Databases". Select the Tanium database. Click "Security". Click "Users". In the "Users" pane, review the roles assigned to the user accounts. (Note: This does not apply to service accounts.) If any user account has an elevated privilege role other than the assigned database administrators, this is a finding.

## Group: SRG-APP-000381

**Group ID:** `V-234074`

### Rule: The Tanium Server installers account database permissions must be reduced to an appropriate level.

**Rule ID:** `SV-234074r961464_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Creating the tanium and tanium_archive databases through the Tanium Server installer program or using the database create SQL scripts requires Sysadmin-level permissions. Once the databases have been created, the Tanium Server and Apache services must be configured to execute under an account that holds at least the dbo role on both databases. Post-installation, if the account used to configure the Tanium Server services to access the remote SQL database server holds only the Database Owner role, rather than the sysadmin role, consider granting this account the View Server State permission on the SQL Server. While not strictly necessary, this dynamic management view enables the Tanium Server to access data faster than the dbo role alone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium SQL server interactively. Log on to the server with an account that has administrative privileges. Open SQL Server Management Studio. Connect to Tanium instance of SQL Server. In the left pane, click "Databases". Select the Tanium database. Click "Security". Click "Users". In the "Users" pane, review the role assigned to the Tanium Server service user account. If the role assigned to the Tanium Server service account is not "db_owner", this is a finding. If using Postgres: Only owners of objects can change them. To view all functions, triggers, and trigger procedures, their ownership and source, as the database administrator (shown here as "postgres") run the following SQL: $ sudo su - postgres $ psql -x -c "\df+"

## Group: SRG-APP-000383

**Group ID:** `V-234075`

### Rule: Firewall rules must be configured on the Tanium Server for Server-to-Database communications.

**Rule ID:** `SV-234075r961470_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Tanium Server can use either a SQL Server RDBMS installed locally to the same device as the Tanium Server application or a remote dedicated or shared SQL Server instance. Using a local SQL Server database typically requires no changes to network firewall rules since all communication remains on the Tanium application server device. To access database resources installed to a remote device, however, the Tanium Server service communicates over the port reserved for SQL, by default port 1433, to the database. Port Needed: Tanium Server to Remote SQL Server over TCP port 1433. Network firewall rules: Allow TCP traffic on port 1433 from the Tanium Server device to the remote device hosting the SQL Server RDBMS. https://docs.tanium.com/platform_install/platform_install/reference_network_ports.html.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to verify which firewall is being used as a host-based firewall on the Tanium Server. Access the host-based firewall configuration on the Tanium Server. Validate a rule exists for the following: Port Needed: Tanium Server to Remote SQL Server over TCP port 1433. If a host-based firewall rule does not exist to allow Tanium Server to Remote SQL Server over TCP port 1433, this is a finding. Consult with the network firewall administrator and validate rules exist for the following: Allow traffic from Tanium Server to Remote SQL Server over TCP port 1433. If a network firewall rule does not exist to allow traffic from Tanium Server to Remote SQL Server over TCP port 1433, this is a finding.

## Group: SRG-APP-000454

**Group ID:** `V-234076`

### Rule: SQL stored queries or procedures installed during Tanium installation must be removed from the Tanium Server.

**Rule ID:** `SV-234076r961677_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to protect organizational information from data mining may result in a compromise of information. Data storage objects include, for example, databases, database records, and database fields. Data mining prevention and detection techniques include, for example: limiting the types of responses provided to database queries; limiting the number/frequency of database queries to increase the work factor needed to determine the contents of such databases; and notifying organizational personnel when atypical database queries or accesses occur.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium Server interactively. Log on to the server with an account that has administrative privileges. Navigate to Program Files >> Tanium >> Tanium Server. If any SQL stored queries (.sql files) or procedures are found, this is a finding.

## Group: SRG-APP-000429

**Group ID:** `V-234077`

### Rule: The Tanium Server must protect the confidentiality and integrity of transmitted information, in preparation to be transmitted and data at rest, with cryptographic signing capabilities enabled to protect the authenticity of communications sessions when making requests from Tanium Clients.

**Rule ID:** `SV-234077r961602_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised since unprotected communications can be intercepted and either read or altered. This requirement applies only to those applications that are either distributed or can allow access to data non-locally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, applications need to leverage transmission protection mechanisms, such as TLS, SSL VPNs, or IPsec. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. Satisfies: SRG-APP-000429, SRG-APP-000440, SRG-APP-000441</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system, which has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Administration". Select the "Global Settings" tab. In the "Show Settings Containing:" search box type "ReportingTLSMode". Enter. If no results are returned, this is a finding. In the "Show Settings Containing:" search box type "StateProtectedFlag". Enter. If no results are returned or "StateProtectedFlag = 0", this is a finding. If results are returned for "ReportingTLSMode" but the value is "0", this is a finding.

## Group: SRG-APP-000003

**Group ID:** `V-234078`

### Rule: The Tanium Application Server console must be configured to initiate a session lock after a 15-minute period of inactivity.

**Rule ID:** `SV-234078r960741_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Tanium Console, when CAC is enabled, will initiate a session lock based upon the ActivClient or other Smart Card software. By initiating the session lock, the console will be locked and not allow unauthorized access by anyone other than the original user. Although this setting does not apply when CAC is enabled, it should be explicitly disabled in the event CAC authentication is ever broken or removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI) and log on with CAC. After logging in, in the top right corner of the UI select the drop down arrow and click on "Preferences". Verify the "Suspend console automatically if no activity detected for:" is configured to a value of "15" minutes or less. If the "Suspend console automatically if no activity detected for:" is not configured to a value of "15" minutes or less, this is a finding.

## Group: SRG-APP-000015

**Group ID:** `V-234079`

### Rule: Tanium Trusted Content providers must be documented.

**Rule ID:** `SV-234079r960762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A Tanium Sensor, also called content, enables an organization to gather real-time inventory, configuration, and compliance data elements from managed computers. Sensors gather specific information from the local device and then write the results to the computer's standard output channel. The Tanium Client captures that output and forwards the results through the platform's unique "ring" architecture for display in the Tanium Console. The language used for Sensor development is based on the scripting engine available on the largest number of devices under management as well as the scripting experience and background of the people who will be responsible for creating new Sensors. VBScript and PowerShell are examples of common scripting languages used for developing sensors. Because errors in scripting can and will provide errant feedback at best and will impact functionality of the endpoint to which the content is directed, it is imperative to ensure content is only accepted from trusted sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If only using Tanium provided content and not accepting content from any other content providers, this is Not Applicable. Consult with the Tanium System Administrator to review the documented list of trusted content providers along with the Hash for their respective public keys. If the site does not have the Tanium trusted content providers documented along with the SHA-256 Hash for their respective public keys, this is a finding.

## Group: SRG-APP-000015

**Group ID:** `V-234080`

### Rule: Content providers must provide their public key to the Tanium administrator to import for validating signed content.

**Rule ID:** `SV-234080r960762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A Tanium Sensor, also called content, enables an organization to gather real-time inventory, configuration, and compliance data elements from managed computers. Sensors gather specific information from the local device and then write the results to the computer's standard output channel. The Tanium Client captures that output and forwards the results through the platform's unique "ring" architecture for display in the Tanium Console. The language used for Sensor development is based on the scripting engine available on the largest number of devices under management as well as the scripting experience and background of the people who will be responsible for creating new Sensors. VBScript and PowerShell are examples of common scripting languages used for developing sensors. Because errors in scripting can and will provide errant feedback at best and will impact functionality of the endpoint to which the content is directed, it is imperative to ensure content is only accepted from trusted sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If only using Tanium provided content and not accepting content from any other content providers, this is Not Applicable. Obtain documentation from the Tanium System Administrator that contains the public key validation data. Access the Tanium Server interactively. Log on to the server with an account that has administrative privileges. Open an Explorer window. Navigate to the following folder: Program Files >> Tanium >> Tanium Server >> content_public_keys >> content folder. If the Tanium default content-release.pub key is the only key in the folder, this is not a finding. If there are documented content provider keys in the content folder, this is not a finding. If non-documented content provider keys are found in the content folder, this is a finding.

## Group: SRG-APP-000015

**Group ID:** `V-234081`

### Rule: Tanium public keys of content providers must be validated against documented trusted content providers.

**Rule ID:** `SV-234081r960762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A Tanium Sensor, also called content, enables an organization to gather real-time inventory, configuration, and compliance data elements from managed computers. Sensors gather specific information from the local device and then write the results to the computer's standard output channel. The Tanium Client captures that output and forwards the results through the platform's unique "ring" architecture for display in the Tanium Console. The language used for Sensor development is based on the scripting engine available on the largest number of devices under management as well as the scripting experience and background of the people who will be responsible for creating new Sensors. VBScript and PowerShell are examples of common scripting languages used for developing sensors. Because errors in scripting can and will provide errant feedback at best and will impact functionality of the endpoint to which the content is directed, it is imperative to ensure content is only accepted from trusted sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If only using Tanium provided content and not accepting content from any other content providers, this is Not Applicable. Obtain documentation from the Tanium System Administrator that contains the public key validation data. Access the Tanium Server interactively. Log on to the server with an account that has administrative privileges. Open an "Explorer" window. Navigate to the following folder: Program Files >> Tanium >> Tanium Server >> content_public_keys >> content folder. Ensure the public keys listed in the content folder are documented. If a public key, other than the default Tanium public key, resides in the content folder and is not documented, this is a finding.

## Group: SRG-APP-000033

**Group ID:** `V-234082`

### Rule: The Tanium Action Approval feature must be enabled for two-person integrity when deploying actions to endpoints.

**Rule ID:** `SV-234082r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Tanium Action Approval feature provides a "four eyes" control mechanism designed to achieve a high-level of security and reduce the possibility of error for critical operations. When this feature is enabled, an action configured by one Tanium console user will require a second Tanium console user with a role of Action Approver (or higher) to approve the action before it is deployed to targeted computers. While this system slows workflow, the reliability of actions deployed will be greater on the Packaging and Targeting.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI) and log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console then click on "Administration". Select the "Global Settings" tab. In the "Show Settings Containing:" search box type "require_action_approval". Click “Enter”. If no results are returned, this is a finding. If results are returned for "require_action_approval", but the value is not "1", this is a finding.

## Group: SRG-APP-000039

**Group ID:** `V-234083`

### Rule: The Tanium documentation identifying recognized and trusted Intel streams must be maintained.

**Rule ID:** `SV-234083r960804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An IOC stream is a series or stream of IOCs that are imported from a vendor based on a subscription service. An IOC stream can be downloaded manually or on a scheduled basis. The items in an IOC stream can be separately manipulated after they are imported.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to determine if the "Tanium Detect" module is being used, if not this is Not Applicable. Review the documented list of IOC trusted stream sources. If the site does use an external source for IOCs and the IOC trusted stream source is not documented, this is a finding.

## Group: SRG-APP-000039

**Group ID:** `V-234084`

### Rule: The Tanium Detect must be configured to receive IOC streams only from trusted sources.

**Rule ID:** `SV-234084r960804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An IOC stream is a series or stream of intel that are imported from a vendor based on a subscription service or manually downloaded and placed in a folder. Detect can be configured to retrieve the IOC content on a regularly scheduled basis. The items in an IOC stream can be separately manipulated after they are imported.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to determine if the "Tanium Detect" module is being used, if not this is Not Applicable. Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Detect". Expand the left menu. Click the "Management" tab. Select "Sources". Verify all configured Detect Streams are configured to a documented trusted source. If any configured Detect Stream is configured to a stream that has not been documented as trusted, this is a finding.

## Group: SRG-APP-000115

**Group ID:** `V-234085`

### Rule: The Tanium Connect module must be configured to forward Tanium Detect events to identified destinations.

**Rule ID:** `SV-234085r960924_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Indicators of Compromise (IOC) are artifacts, which are observed on the network or system that indicates computer intrusion. The Tanium Detect module detects, manages, and analyzes systems intrusion in real time. The module also responds to those detections. By forwarding Detect events using Tanium Connect, the necessary forensic evidence supporting a compromise is retained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to determine if the "Tanium Detect" module is being used. If it is not, this is Not Applicable. Using a web browser on a system that has connectivity to Tanium, access the Tanium web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Connect". Click "Events" under "Sources". Verify the "Tanium IOC Detect" event is being sent to an identified destination. If there is no "Tanium IOC Detect" event source, this is a finding.

## Group: SRG-APP-000131

**Group ID:** `V-234086`

### Rule: The Tanium cryptographic signing capabilities must be enabled on the Tanium Server.

**Rule ID:** `SV-234086r960954_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All of Tanium's signing capabilities should be enabled upon install. Tanium supports the cryptographic signing and verification before execution of all Sensors, Questions, Actions, Sensor Libraries, File Shards, etc. Enabling signing does away with the ability of an attacker to conduct Man in the Middle (MitM) attacks for the purposes of remote code execution and precludes the modification of the aforementioned data elements in transit. Additionally, Tanium supports object level signing for content ingested into the Tanium platform. This allows for the detection and rejection of changes to objects (sensors, actions, etc.) by even a privileged user within Tanium. Tanium has built-in signing capabilities enabled by default when installed. Cryptographic signing and verification of all Sensors, Questions, Actions, Sensor Libraries, File Shards, etc. before execution will be enforced by Tanium. Signing will prevent MitM remote code execution attacks and will protect data element in transit. Tanium also supports object level signing for content within the Tanium platform. Satisfies: SRG-APP-000131, SRG-APP-000233, SRG-APP-000317</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Administration". Select the "Global Settings" tab. In the "Show Settings Containing:" search box type "sign_all_questions_flag". Click "Enter". If no results are returned, this is a finding. If results are returned for "sign_all_questions_flag" but the value is not "1", this is a finding.

## Group: SRG-APP-000131

**Group ID:** `V-234087`

### Rule: The Tanium Server must be configured to only allow signed content to be imported.

**Rule ID:** `SV-234087r960954_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the application. Verifying software components have been digitally signed using a certificate that is recognized and approved by the organization ensures the software has not been tampered with and that it has been provided by a trusted vendor. Accordingly, patches, service packs, or application components must be signed with a certificate recognized and approved by the organization. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. The application should not have to verify the software again. This requirement does not mandate DoD certificates for this purpose; however, the certificate used to verify the software must be from an approved CA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement only applies to Tanium implementations in production. If implementation being evaluated is in development, this requirement is Not Applicable. Access the Tanium Server through interactive logon. Drill to Program Files >> Tanium >> Tanium Server. Open the "tanium.license" in Notepad and search for "allow_unsigned_import". If "allow unsigned_import" is followed by ":true", this is a finding.

## Group: SRG-APP-000133

**Group ID:** `V-234088`

### Rule: All installation files originally downloaded to the Tanium Server must be configured to download to a location other than the Tanium Server directory.

**Rule ID:** `SV-234088r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Typically, the Tanium Server stores the Package Source Files that it downloads from the Internet and server shares or files uploaded through the Tanium Console in a subdirectory of the server's installation directory called Downloads. To ensure package files are not accessible to non-authorized functions, the files must be re-located to outside of the server's installation directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium Server interactively. Log on to the server with an account that has administrative privileges. Run regedit as Administrator. Navigate to HKEY_LOCAL_MACHINE >> SOFTWARE >> Wow6432Node >> Tanium >> Tanium Server. Validate the "DownloadPath REG_SZ" value does not point to a location within the Tanium Server directory. If the "DownloadPath REG_SZ" value points to a location within the Tanium Server directory, this is a finding.

## Group: SRG-APP-000142

**Group ID:** `V-234089`

### Rule: Firewall rules must be configured on the Tanium Server for Client-to-Server communications.

**Rule ID:** `SV-234089r1043177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In addition to the client-to-server TCP communication that takes place over port 17472, Tanium Clients also communicate to other Tanium-managed computers over port 17472. The Tanium environment can perform hundreds or thousands of times faster than other security or systems management tools because the Tanium Clients communicate in secure, linearly-controlled peer-to-peer rings. Because clients dynamically communicate with other nearby agents based on proximity and latency, rings tend to form automatically to match a customer's topology--endpoints in California will form one ring while endpoints in Germany will form a separate ring. https://docs.tanium.com/platform_install/platform_install/reference_network_ports.html</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to verify which firewall is being used as a host-based firewall on the Tanium Server. Access the host-based firewall configuration on the Tanium Server. Validate rules exist, as required, to include: Between Tanium Clients or Zone Clients over TCP port 17472, bi-directionally. If a host-based firewall rule does not exist to allow TCP port 17472, bi-directionally, this is a finding. Consult with the network firewall administrator and validate rules exist for the following: Allow TCP traffic on port 17472 from any computer to be managed on a local area network to any other computer to be managed on the same local area network. If a network firewall rule does not exist to allow TCP port 17472 from any managed computer to any other managed computer on the same local area network, this is a finding.

## Group: SRG-APP-000142

**Group ID:** `V-234090`

### Rule: Firewall rules must be configured on the Tanium Zone Server for Client-to-Zone Server communications.

**Rule ID:** `SV-234090r1043177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In customer environments using the Tanium Zone Server, a Tanium Client may be configured to point to a Zone Server instead of a Tanium Server. The communication requirements for these Clients are identical to the Server-to-Client requirements. https://docs.tanium.com/platform_install/platform_install/reference_network_ports.html</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If a Zone Server is not being used, this is Not Applicable. Consult with the Tanium System Administrator to verify which firewall is being used as a host-based firewall on the Tanium Zone Server. Access the host-based firewall configuration on the Tanium Zone Server. Validate a rule exists for the following: Port Needed: Tanium Clients to Zone Server over TCP port 17472. If a host-based firewall rule does not exist to allow TCP port 17472, bi-directionally, from Tanium Clients to the Tanium Zone Server, this is a finding.

## Group: SRG-APP-000142

**Group ID:** `V-234091`

### Rule: The Tanium Application Server must be configured to prohibit or restrict the use of organization-defined functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-234091r1043177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the PPSM CAL to ensure Tanium has been registered with all of the TCP ports required for functionality to include (but not limited to) TCP 17472, 17477, 17440, 17441, 443, and 1433. If any TCP ports are being used on the Tanium Server that have been deemed as restricted by the PPSM CAL, this is a finding.

## Group: SRG-APP-000175

**Group ID:** `V-234092`

### Rule: The Tanium Server certificates must have Extended Key Usage entries for the serverAuth object TLS Web Server Authentication and the clientAuth object TLS Web Client Authentication.

**Rule ID:** `SV-234092r961038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. This requirement applies only to those applications that are either distributed or can allow access to data non-locally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When receiving data, applications need to leverage protection mechanisms, such as TLS, SSL VPNs, or IPsec.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium Application server interactively. Log on to the server with an account that has administrative privileges. Navigate to Program Files >> Tanium >> Tanium Server. Locate the "SOAPServer.crt" file. Double-click on the file to open the certificate. Select the "Details" tab. Scroll down through the details to find and select the "Enhanced Key Usage" field. If there is no "Enhanced Key Usage" field, this is a finding. In the bottom screen, verify "Server Authentication" and "Client Authentication" are both identified. If "Server Authentication" and "Client Authentication" are not both identified, this is a finding.

## Group: SRG-APP-000176

**Group ID:** `V-234093`

### Rule: The Tanium Server certificate and private/public keys directory must be protected with appropriate permissions.

**Rule ID:** `SV-234093r961041_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If the private key is discovered, an attacker can use the key to authenticate as an authorized user and gain access to the network infrastructure. The cornerstone of the PKI is the private key used to encrypt or digitally sign information. If the private key is stolen, this will lead to the compromise of the authentication and non-repudiation gained through PKI because the attacker can use the private key to digitally sign documents and pretend to be the authorized user. Both the holders of a digital certificate and the issuing authority must protect the computers, storage devices, or whatever they use to keep the private keys.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium Server interactively. Log on to the server with an account that has administrative privileges. Open an Explorer window. Navigate to >> Program Files >> Tanium >> Tanium Server. Right-click on the "Certs" folder. Choose "Properties". Select the "Security" tab. Click on the "Advanced" button. Validate the owner of the directory is the [Tanium service account]. Validate System has "Read Only" permissions. Validate the [Tanium service account] has "Read Only" permissions. Validate [Tanium Admins group] has Full permissions. If the owner of the directory is not the [Tanium service account] and/or System and the [Tanium service account] has more privileges than "Read Only" and/or the [Tanium Admins group] has less than Full permissions, this is a finding. Navigate to Program Files >> Tanium >> Tanium Server >> Certs. Right-click on each of the following files: Select "Properties". Select the "Security" tab. Click on the "Advanced" button. Installedcacert.crt Installed-server.crt Installed-server.key SOAPServer.crt SOAPServer.key Validate System and the [Tanium service account] have "Read-Only" permissions to each of the individual files, and the [Tanium Admin group] has Full permissions to each of the individual files. If System and the [Tanium service account] have more than "Read-Only" permissions to any of the individual files and/or the [Tanium Admin group] has less than Full permissions to any of the individual files, this is a finding. Navigate to Program Files >> Tanium >> Tanium Server >> content_public_keys. Right-click on each of the following files: Select "Properties". Select the "Security" tab. Click on the "Advanced" button. Validate System has "Read-Only" permissions and is applied to child objects. Validate [Tanium service account] has "Read-Only" permissions and is applied to child objects. Validate [Tanium Admin Group] has Full permissions and is applied to child objects. If the [Tanium service account] and system permissions to the \content_public_keys folder is greater than "Read-Only" and/or the "Read-Only" permissions have not been applied to child objects and/or the [Tanium Admin Group] has less than Full permissions, this is a finding.

## Group: SRG-APP-000211

**Group ID:** `V-234094`

### Rule: The Tanium Module server must be installed on a separate system.

**Rule ID:** `SV-234094r961095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized access to the Tanium Server is protected by disabling the Module Server service on the Tanium Server and by configuring the Module Server on a separate system. When X509 smartcard certificates (CAC or PIV tokens) are used for access to the Tanium Server, the Tanium Module server must be on a separate system. In order to restrict access to the Tanium Server resulting from an attack on the Module Server, it is recommended that the Tanium Module Server be installed on a separate system or VM from the Tanium Server. Adding to this recommendation, if the Tanium Server is configured to accept X509 Smartcard certificates (also referred to as CAC or PIV tokens) in lieu of username/password logon, the requirement becomes explicit and the Tanium Module Server must be installed on a separate system or VM.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the server being validated is the Module server, this check is Not Applicable. Access the Tanium Server interactively. Log on to the server with an account that has administrative privileges. Click "Start". Access the Server Manager. Select Local Server. In upper right corner, click "Tools". Select "Services". If the Tanium Module Server service is "Running", this is a finding.

## Group: SRG-APP-000328

**Group ID:** `V-234095`

### Rule: The Tanium Server directory must be restricted with appropriate permissions.

**Rule ID:** `SV-234095r961317_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user controlled file permissions. When discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside of the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium Server interactively. Log on to the server with an account that has administrative privileges. Open an Explorer window. Navigate to Program Files >> Tanium. Right-click on the "Tanium Server" folder. Select "Properties". Select the "Security" tab. Click on the "Advanced" button. Validate the owner of the "Tanium Server" folder is the service account [Tanium service account]. Validate the [Tanium service account] has full permissions to the "Tanium Server" folder. Validate the [Tanium Admins] group has full permissions to the "Tanium Server" folder. Validate Users have no permissions to the "Tanium Server" folder. If any accounts other than the [Tanium service account] and the [Tanium Admins] group have any permission to the "Tanium Server" folder, this is a finding. If the [Tanium service account] is not the owner of the "Tanium Server" folder, this is a finding.

## Group: SRG-APP-000328

**Group ID:** `V-234096`

### Rule: The Tanium Server http directory and sub-directories must be restricted with appropriate permissions.

**Rule ID:** `SV-234096r961317_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user controlled file permissions. When discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside of the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium Server interactively. Log on to the server with an account that has administrative privileges. Open an Explorer window. Navigate to Program Files >> Tanium >> Tanium Server. Right-click on the "Tanium Server\http" folder. Select "Properties". Select the "Security" tab. Click on the "Advanced" button. Validate Folder Inheritance is disabled. Validate the owner of the directory is the [Tanium service account]. Validate the [Tanium Admins] group has full permissions. Validate System has Read-Only permissions. Right-click on the "Tanium Server\http\libraries" folder. Select the "Security" tab. Click on the "Advanced" button. Validate Folder Inheritance is disabled. Validate the owner of the directory is the [Tanium service account]. Validate System has Read-Only permissions. Validate the [Tanium service account] has Read-Only permissions. Validate the [Tanium Admins] group has full permissions. Right-click on the "Tanium Server\http\taniumjs" folder. Select the "Security" tab. Click on the "Advanced" button. Validate Folder Inheritance is disabled. Validate the owner of the directory is the [Tanium service account]. Validate System has "Read-Only" permissions. Validate the [Tanium service account] has "Read-Only" permissions. Validate the [Tanium Admins] group has full permissions. Right-click on the "Tanium Server\http\tux" folder. Select the "Security" tab. Click on the "Advanced" button. Validate Folder Inheritance is disabled. Validate the owner of the directory is the [Tanium service account]. Validate System has "Read-Only" permissions. Validate the [Tanium service account] has "Read Only" permissions. Validate the [Tanium Admins] group has full permissions. Right-click on the "Tanium Server\http\tux-console" folder. Select the "Security" tab. Click on the "Advanced" button. Validate Folder Inheritance is disabled. Validate the owner of the directory is the [Tanium service account]. Validate System has "Read-Only" permissions. Validate the [Tanium service account] has "Read-Only" permissions. Validate the [Tanium Admins] group has full permissions. Right-click on the "Tanium Server\Logs" folder. Select "Properties". Select the "Security" tab. Click on the "Advanced" button. Validate Folder Inheritance is disabled. Validate the owner of the directory is the [Tanium service account]. Validate the [Tanium Service Account] has only "Modify" permissions. Validate the [Tanium Admins] group has full permissions. Right-click on the "Tanium Server\TDL_Logs" folder. Select "Properties". Select the "Security" tab. Click on the "Advanced" button. Validate Folder Inheritance is disabled. Validate the owner of the directory is the [Tanium service account]. Validate the [Tanium Service Account] has only "Modify" permissions. Validate the [Tanium Admins] group has full permissions. Right-click on the "Tanium Server\Certs" folder. Select "Properties". Select the "Security" tab. Click on the "Advanced" button. Validate Folder Inheritance is disabled. Validate the owner of the directory is the [Tanium service account]. Validate System has "Read-Only" permissions. Validate the [Tanium Admins] group has full permissions. Navigate to Tanium Server >> Certs. For the following files verify System and [Tanium Service Account] have "Read-Only" permissions: installedcacert.crt installed-server.crt installed-server.key SOAPServer.crt SOAPServer.key Right-click on the "Tanium Server\content_public_keys" folder. Select "Properties". Select the "Security" tab. Click on the "Advanced" button. Validate Folder Inheritance is disabled. Validate the owner of the directory is the [Tanium service account]. Validate System has "Read-Only" permissions. Validate the [Tanium Service Account] has "Read-Only" permissions. Validate the [Tanium Admins] group has full permissions. If any of the above permissions are not configured correctly, this is a finding.

## Group: SRG-APP-000328

**Group ID:** `V-234097`

### Rule: The permissions on the Tanium Server registry keys must be restricted to only the Tanium service account and the [Tanium Admins] group.

**Rule ID:** `SV-234097r961317_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user controlled file permissions. When discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside of the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium Server interactively. Log on to the server with an account that has administrative privileges. Run regedit as Administrator. Navigate to HKEY_LOCAL_MACHINE >> SOFTWARE >> Wow6432Node >> Tanium >> Tanium Server. Right-click on "Tanium Server". Select "Permissions". Click on the "Security" tab. Click on the "Advanced" button. Validate the [Tanium service account] has full permissions. Validate the [Tanium Admins] group has full permissions. Validate the SYSTEM account has full permissions. Validate the User accounts do not have any permissions. If any other account has full permissions and/or the User account has any permissions, this is a finding.

## Group: SRG-APP-000328

**Group ID:** `V-234098`

### Rule: The Tanium Server Logs and TDL_Logs directories must be restricted with appropriate permissions.

**Rule ID:** `SV-234098r961317_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user controlled file permissions. When discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside of the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium Server interactively. Log on to the server with an account that has administrative privileges. Open an Explorer window. Navigate to Program Files >> Tanium >> Tanium Server. Right-click on the "Logs" folder. Select "Properties". Click on the "Security" tab. Click on the "Advanced" button. Validate the owner of the directory is the [Tanium service account]. Validate the [Tanium service account] privileges is only account with modify permissions on the directory. Validate the [Tanium Administrators] group has full permissions on the directory. Right-click on the "TDL_Logs" folder. Select "Properties". Click on the "Security" tab. Click on the "Advanced" button. Validate the owner of the directory is the [Tanium service account]. Validate the [Tanium service account] privileges is the only account with modify permissions on the directory. Validate the [Tanium Administrators] group has full permissions on the directory. If any of the specified permissions are not set as required, this is a finding.

## Group: SRG-APP-000340

**Group ID:** `V-234099`

### Rule: All Active Directory accounts synchronized with Tanium for non-privileged functions must be non-privileged domain accounts.

**Rule ID:** `SV-234099r961353_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Tanium has the ability to synchronize with Active Directory for Tanium account management. Tanium advises that all replicated accounts for non-privileged level functions should be non-privileged domain accounts. In doing so, should a vulnerability in the industry standard OpenSSL libraries used by Tanium ever come to light, no privileged account information could be gained by an attacker. This is simply good housekeeping and should be exercised with any such platform product.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Administration". Select the "Users" tab. Review each of the users listed and determine their Active Directory synced account. Access one of the domain's Active Directory Domain Controller servers with a Domain Administrator account. Review each of the Users for which a synced account is in the Tanium console as a user. Validate whether any of the users are considered to be non-privileged in Active Directory, yet have privileged capabilities in Tanium. If any of the non-privileged Active Directory accounts have elevated privileges and are synced as a Tanium privileged account, this is a finding.

## Group: SRG-APP-000358

**Group ID:** `V-234100`

### Rule: A Tanium connector must be configured to send log data to an external audit log reduction capable system.

**Rule ID:** `SV-234100r961395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>While the Tanium Server records audit log entries to the Tanium SQL database, retrieval and aggregation of log data through the Tanium console is not efficient. The Tanium Connect module allows for SIEM connectors in order to facilitate forensic data retrieval and aggregation efficiently. Consult documentation at https://docs.tanium.com/connect/connect/index.html for supported Connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Connect". Review the configured Tanium Sources listed. If an "Audit Log" source does not exist, this is a finding. Select the "Audit Log" source. Select the audit connection found in the lower half of the screen. Verify the "Destination Type" is a SIEM tool. If the "Destination Type" is not a SIEM tool, this is a finding.

## Group: SRG-APP-000377

**Group ID:** `V-234101`

### Rule: File integrity monitoring of critical executables that Tanium uses must be configured.

**Rule ID:** `SV-234101r961452_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Tanium inherently watches files and their respective hash values for change but while Tanium can do file integrity checks of critical executables, it is important to conduct File Integrity Monitoring (FIM) via an outside service such as Host Based Security System (HBSS) or similar security suites with FIM capability. These technologies provide independent monitoring of critical Tanium and system binaries.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the site is using Tanium Integrity Monitor, Tanium Integrity Monitor should be used to monitor the file integrity of Tanium critical files. If Tanium Integrity Monitor is not installed, a third-party file integrity-monitoring tool must be used to monitor Tanium critical executables, defined files within the Tanium Server directory path. If the file integrity of Tanium critical executables is not monitored, this is a finding.

## Group: SRG-APP-000383

**Group ID:** `V-234102`

### Rule: Firewall rules must be configured on the Tanium module server to allow Server-to-Module Server communications from the Tanium Server.

**Rule ID:** `SV-234102r961470_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Tanium Module Server is used to extend the functionality of Tanium through the use of various workbenches. The Tanium Module Server requires communication with the Tanium Server on port 17477. Without a proper connection from the Tanium Server to the Tanium Module Server, access to the system capabilities could be denied. https://docs.tanium.com/platform_install/platform_install/reference_network_ports.html.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to verify which firewall is being used as a host-based firewall on the Tanium Module Server. Access the host-based firewall configuration on the Tanium Module Server. Validate a rule exists for the following: Port Needed: Tanium Server to Tanium Module Server over TCP port 17477. If a host-based firewall rule does not exist to allow TCP port 17477, from the Tanium Server to the Tanium Module Server, this is a finding. Consult with the network firewall administrator and validate rules exist for the following: Allow TCP traffic on port 17477 from the Tanium Server to the Tanium Module Server. If a network firewall rule does not exist to allow TCP traffic on port 17477 from the Tanium Server to the Tanium Module Server, this is a finding.

## Group: SRG-APP-000383

**Group ID:** `V-234103`

### Rule: Firewall rules must be configured on the Tanium Server for Server-to-Module Server communications.

**Rule ID:** `SV-234103r961470_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Tanium Module Server is used to extend the functionality of Tanium through the use of various workbenches. The Tanium Module Server requires communication with the Tanium Server on port 17477. Without a proper connection from the Tanium Server to the Tanium Module Server, access to the system capabilities could be denied. https://docs.tanium.com/platform_install/platform_install/reference_network_ports.html.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to verify which firewall is being used as a host-based firewall on the Tanium Server. Access the host-based firewall configuration on the Tanium Server. Validate a rule exists for the following: Port Needed: Tanium Server to Tanium Module Server over TCP port 17477. If a host-based firewall rule does not exist to allow TCP port 17477, from the Tanium Server to the Tanium Module Server, this is a finding. Consult with the network firewall administrator and validate rules exist for the following: Allow TCP traffic on port 17477 from the Tanium Server to the Tanium Module Server. If a network firewall rule does not exist to allow TCP traffic on port 17477 from the Tanium Server to the Tanium Module Server, this is a finding.

## Group: SRG-APP-000383

**Group ID:** `V-234104`

### Rule: Firewall rules must be configured on the Tanium Server for Server-to-Zone Server communications.

**Rule ID:** `SV-234104r961470_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If you are using the Tanium Zone Server to proxy traffic from Tanium-managed computers on less trusted network segments to the Tanium Server on the core network, then the Tanium Zone Server Hub, typically installed to the Tanium Server device, must be able to connect to the Zone Server(s) in the DMZ. This is the only configuration that requires you to allow outbound traffic on port 17472 from the Tanium Server device. The ZoneServerList.txt configuration file located in the Tanium Zone Server Hub's installation folder identifies the addresses of the destination Zone Servers. See the Zone Server Configuration page for more details. Port Needed: Tanium Server to Zone Server over TCP port 17472. Network firewall rules: Allow TCP traffic on port 17472 from the Zone Server Hub, usually the Tanium Server device, to the destination DMZ devices(s) hosting the Zone Server(s). Endpoint firewall rules - for additional security, configure the following endpoint firewall rules: Allow TCP traffic outbound on port 17472 from only the Zone Server Hub process running on the Tanium Server device. Allow TCP traffic inbound on port 17472 to only the Zone Server process running on the designated Zone Server device(s). https://docs.tanium.com/platform_install/platform_install/reference_network_ports.html.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If a Zone Server is not being used, this is Not Applicable. Consult with the Tanium System Administrator to verify which firewall is being used as a host-based firewall on the Tanium Server. Access the host-based firewall configuration on the Tanium Server. Validate a rule exists for the following: Port Needed: Tanium Server to Zone Server over TCP port 17472. If a host-based firewall rule does not exist to allow TCP port 17472, bi-directionally, from Tanium Server to the Tanium Zone Server, this is a finding.

## Group: SRG-APP-000416

**Group ID:** `V-234105`

### Rule: The SSLHonorCipherOrder must be configured to disable weak encryption algorithms on the Tanium Server.

**Rule ID:** `SV-234105r962034_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium Server interactively. Log on to the server with an account that has administrative privileges. Access the server's registry by typing: regedit <enter>. Navigate to HKEY_LOCAL_MACHINE >> SOFTWARE >> Wow6432Node >> Tanium >> Tanium Server. Verify the existence of a DWORD "SSLHonorCipherOrder" with a value of "0x00000001" (hex). If the DWORD "SSLHonorCipherOrder" does not exist with a value of "0x00000001" (hex), this is a finding.

## Group: SRG-APP-000427

**Group ID:** `V-234106`

### Rule: The Tanium Server certificate must be signed by a DoD Certificate Authority.

**Rule ID:** `SV-234106r961596_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Tanium Server has the option to use a "self-signed" certificate or a Trusted Certificate Authority signed certificate for SSL connections. During evaluations of Tanium in Lab settings, customers often conclude that a "self-signed" certificate is an acceptable risk. However, in production environments it is critical that a SSL certificate signed by a Trusted Certificate Authority be used on the Tanium Server in lieu of an untrusted and insecure "self-signed" certificate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system, which has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. When connected, review the Certificate for the Tanium Server: In Internet Explorer, right-click on the page. Select "Properties". Click on the "Certificates" tab. On the "General" tab, validate the Certificate shows as issued by a DOD Root CA. On Certification "Path" tab, validate the path top-level is a DoD Root CA. If the certificate authority is not DoD Root CA, this is a finding.

## Group: SRG-APP-000442

**Group ID:** `V-234107`

### Rule: Any Tanium configured EMAIL RESULTS connectors must be configured to enable TLS/SSL to encrypt communications.

**Rule ID:** `SV-234107r961641_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. This requirement applies only to those applications that are either distributed or can allow access to data non-locally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, applications need to leverage transmission protection mechanisms, such as TLS, SSL VPNs, or IPsec. An example of this would be the SMTP queue. The SMTP mail protocol places email messages into a centralized queue prior to transmission. If someone were to modify an email message contained in the queue and the SMTP protocol did not check to ensure the email message was not modified while it was stored in the queue, a modified email could be sent.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Connect". Review the configured Destinations listed. If an "Email" Destination does not exist, this is not a finding. Select "Email" destination. Select each Connection found in the lower half of the screen. Verify "Enable TLS" is "true". If "Enable TLS" is "false", this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-234108`

### Rule: Tanium Server files must be excluded from on-access antivirus actions.

**Rule ID:** `SV-234108r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Similar to any other host-based applications, the Tanium Server is subject to the restrictions other System-level software may place on an operating environment. Antivirus, IPS, Encryption, or other security and management stack software may disallow the Tanium Server from working as expected. https://docs.tanium.com/platform_install/platform_install/reference_host_system_security_exceptions.html.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to determine the antivirus software used on the Tanium Server. Review the settings of the antivirus software. Validate exclusions exist which exclude the Tanium program files from being scanned by antivirus on-access scans. If exclusions do not exist, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-234109`

### Rule: Tanium Server files must be protected from file encryption actions.

**Rule ID:** `SV-234109r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Similar to any other host-based applications, the Tanium Server is subject to the restrictions other System-level software may place on an operating environment. Antivirus, Encryption, or other security and management stack software may disallow the Tanium Server from working as expected. https://docs.tanium.com/platform_install/platform_install/reference_host_system_security_exceptions.html.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to determine the file-level encryption software used on the Tanium Server. Review the settings for the file-level encryption software. Validate exclusions exist which exclude the Tanium program files from being encrypted by the file-level encryption software. If exclusions do not exist, this is a finding.

## Group: SRG-APP-000416

**Group ID:** `V-234110`

### Rule: The SSLCipherSuite must be configured to disable weak encryption algorithms on the Tanium Server.

**Rule ID:** `SV-234110r962034_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium Server interactively. Log on to the server with an account that has administrative privileges. Access the server's registry by typing: "regedit". Click "Enter". Navigate to HKEY_LOCAL_MACHINE >> SOFTWARE >> Wow6432Node >> Tanium >> Tanium Server. Verify the existence of a String "SSLCipherSuite" with a value of: ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK If the String "SSLCipherSuite" does not exist with the appropriate list values, this is a finding.

## Group: SRG-APP-000001

**Group ID:** `V-234111`

### Rule: The Tanium max_soap_sessions_total setting must be explicitly enabled to limit the number of simultaneous sessions.

**Rule ID:** `SV-234111r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application management includes the ability to control the number of users and user sessions that utilize an application. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to DoS attacks. This requirement may be met via the application or by utilizing information system, session control provided by a web server with specialized session management capabilities. If it has been specified that this requirement will be handled by the application, the capability to limit the maximum number of concurrent single user sessions must be designed and built into the application. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system, which has connectivity to the Tanium Application, access the Tanium Application web user interface (UI) and log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Administration". Select the "Global Settings" tab. In the "Show Settings Containing:" search box type "max_soap_sessions_total". Click "Enter". If no results are returned, this is a finding. If results are returned for "max_soap_sessions_total", but the value is not the value defined in the system documentation, this is a finding.

## Group: SRG-APP-000001

**Group ID:** `V-234112`

### Rule: The Tanium max_soap_sessions_per_user setting must be explicitly enabled to limit the number of simultaneous sessions.

**Rule ID:** `SV-234112r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application management includes the ability to control the number of users and user sessions that utilize an application. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to DoS attacks. This requirement may be met via the application or by utilizing information system session control provided by a web server with specialized session management capabilities. If it has been specified that this requirement will be handled by the application, the capability to limit the maximum number of concurrent single user sessions must be designed and built into the application. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system, which has connectivity to the Tanium Application, access the Tanium Application web user interface (UI) and log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Administration". Select the "Global Settings" tab. In the "Show Settings Containing:" search box type "max_soap_sessions_per_user". Click "Enter". If no results are returned, this is a finding. If results are returned for "max_soap_sessions_per_user", but the value is not the value defined in the system documentation, this is a finding.

## Group: SRG-APP-000001

**Group ID:** `V-234113`

### Rule: The Tanium soap_max_keep_alive setting must be explicitly enabled to limit the number of simultaneous sessions.

**Rule ID:** `SV-234113r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application management includes the ability to control the number of users and user sessions that utilize an application. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to DoS attacks. This requirement may be met via the application or by utilizing information system session control provided by a web server with specialized session management capabilities. If it has been specified that this requirement will be handled by the application, the capability to limit the maximum number of concurrent single user sessions must be designed and built into the application. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system, which has connectivity to the Tanium Application, access the Tanium Application web user interface (UI) and log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Administration". Select the "Global Settings" tab. In the "Show Settings Containing:" search box type "soap_max_keep_alive". Click "Enter". If no results are returned, this is a finding. If results are returned for "soap_max_keep_alive ", but the value is not the value defined in the system documentation, this is a finding.

## Group: SRG-APP-000039

**Group ID:** `V-234114`

### Rule: The Tanium documentation identifying recognized and trusted folders for Detect Local Directory Source must be maintained.

**Rule ID:** `SV-234114r960804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An IOC stream is a series or "stream" of IOCs that are imported from a vendor based on a subscription service or manually downloaded and placed in a folder. Detect can be configured to retrieve the IOC content on a regularly scheduled basis. The items in an IOC stream can be separately manipulated after they are imported.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to review the documented list of folder maintainers for Detect Local Directory Source. If the site does not leverage Local Directory Source to import IOCs, this finding is Not Applicable. If the site does use Local Directory Source to import IOCs and the folder maintainers are not documented, this is a finding.

## Group: SRG-APP-000039

**Group ID:** `V-234115`

### Rule: The Tanium Detect Local Directory Source must be configured to restrict access to only authorized maintainers of Intel.

**Rule ID:** `SV-234115r960804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An IOC stream is a series or ""stream"" of intel that are imported from a vendor based on a subscription service or manually downloaded and placed in a folder. Detect can be configured to retrieve the IOC content on a regularly scheduled basis. The items in an IOC stream can be separately manipulated after they are imported.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to determine if the Tanium Detect module is being used, if not then this finding is Not Applicable. If being used then determine where they get their IOC Stream. Access the Tanium Module Server interactively. Log on to the server with an account that has administrative privileges. Open an Explorer window. Navigate to Program Files >> Tanium >> Tanium Module Server >> services >> detect3-files Right-click on the folder and choose "Properties". Select the "Security" tab. Click on the "Advanced" button. If the accounts listed in the "Security" tab do not match the list of accounts found in the Tanium documentation, this is a finding.

## Group: SRG-APP-000039

**Group ID:** `V-234116`

### Rule: The Tanium documentation identifying recognized and trusted SCAP sources must be maintained.

**Rule ID:** `SV-234116r960804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>NIST validated SCAP XML documents are provided from several possible sources such as DISA, NIST, and the other non-government entities. These documents are used as the basis of compliance definitions leveraged to automate compliance auditing of systems. These documents are updated on different frequencies and must be manually downloaded on regular intervals and imported in order to be current. Non-approved SCAP definitions lead to a false sense of security when evaluating an enterprise environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to review the documented list of trusted SCAP sources. If the site does not have "Tanium Comply" module, or does not use "Tanium Comply" for compliance validation, this finding is Not Applicable. If the site does use "Tanium Comply" and the source for SCAP content is not documented, this is a finding.

## Group: SRG-APP-000039

**Group ID:** `V-234117`

### Rule: The Tanium documentation identifying recognized and trusted OVAL feeds must be maintained.

**Rule ID:** `SV-234117r960804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OVAL XML documents are provided from several possible sources such as the CIS open source repository, or any number of vendor/3rd party paid repositories. These documents are used to automate the passive validation of vulnerabilities on systems and therefore require a reasonable level of confidence in their origin. Non-approved OVAL definitions lead to a false sense of security when evaluating an enterprise environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to review the documented list of trusted OVAL feeds. If the site does not have "Tanium Comply" module, or does not use "Tanium Comply" for passive vulnerability scanning, this finding is Not Applicable. Otherwise, if the site does use "Tanium Comply" and the source for OVAL content is not documented, this is a finding.

## Group: SRG-APP-000039

**Group ID:** `V-234118`

### Rule: Tanium Comply must be configured to receive SCAP content only from trusted sources.

**Rule ID:** `SV-234118r960804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>NIST-validated SCAP XML documents are provided from several possible sources such as DISA, NIST, and the other non-government entities. These documents are used as the basis of compliance definitions leveraged to automate compliance auditing of systems. These documents are updated on different frequencies and must be manually downloaded on regular intervals and imported in order to be current. Non-approved SCAP definitions lead to a false sense of security when evaluating an enterprise environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI) and log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Comply". Along the left side of the interface, click on "Benchmarks". Select "Configuration Compliance". Verify all imported compliance benchmarks are from a documented trusted source. If any compliance benchmark is found that does not come from a documented trusted source, this is a finding.

## Group: SRG-APP-000039

**Group ID:** `V-234119`

### Rule: Tanium Comply must be configured to receive OVAL feeds only from trusted sources.

**Rule ID:** `SV-234119r960804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OVAL XML documents are provided from several possible sources such as the CIS open source repository, or any number of vendor/3rd party paid repositories. These documents are used to automate the passive validation of vulnerabilities on systems and therefore require a reasonable level of confidence in their origin. Non-approved OVAL definitions lead to a false sense of security when evaluating an enterprise environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Comply". Along the left side of the interface, click on "Benchmarks". Select "Vulnerability". Verify all imported vulnerability sources are from a documented trusted source. If any vulnerability sources found do not match a documented trusted source, this is a finding.

## Group: SRG-APP-000226

**Group ID:** `V-234120`

### Rule: The Tanium application must be configured in a High-Availability (HA) setup to ensure minimal loss of data and minimal disruption to mission processes in the event of a system failure.

**Rule ID:** `SV-234120r961125_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known state can address safety or security in accordance with the mission/business needs of the organization. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. Preserving application state information helps to facilitate application restart and return to the operational mode of the organization with less disruption to mission-essential processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is not considered mission critical, this is Not Applicable. Using a web browser on a system that has connectivity to the Tanium Application, access the Tanium Application web user interface (UI). Log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Packages". Browse to the package called "Distribute Tanium Standard Utilities". Select it. Press "Status". Observe the text underneath a package file indicating the file cache status. If the cache status represents only one Tanium Server, this is a finding.

## Group: SRG-APP-000247

**Group ID:** `V-234121`

### Rule: The bandwidth consumption for the Tanium Application server must be limited.

**Rule ID:** `SV-234121r961155_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. In the case of application DoS attacks, care must be taken when designing the application to ensure the application makes the best use of system resources. SQL queries have the potential to consume large amounts of CPU cycles if they are not tuned for optimal performance. Web services containing complex calculations requiring large amounts of time to complete can bog down if too many requests for the service are encountered within a short period of time. The methods employed to meet this requirement will vary depending upon the technology the application utilizes. However, a variety of technologies exist to limit or, in some cases, eliminate the effects of application related DoS attacks. Employing increased capacity and bandwidth combined with specialized application layer protection devices and service redundancy may reduce the susceptibility to some DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium Server interactively. Log on to the server with an account that has administrative privileges. Access the server's registry by typing: regedit <enter>. Navigate to HKEY_LOCAL_MACHINE >> SOFTWARE >> Wow6432Node >> Tanium >> Tanium Server. Verify the existence of a DWORD "DownloadBytesPerSecondLimit". If the DWORD "DownloadBytesPerSecondLimit" does not exist with a value equal to the value recorded in the system documentation, this is a finding. Consult with your TAM for an appropriate value and record this in the system documentation. If this setting is not documented, this is a finding.

## Group: SRG-APP-000357

**Group ID:** `V-234122`

### Rule: The Tanium SQL Server RDBMS must be configured with sufficient free space to ensure audit logging is not impacted.

**Rule ID:** `SV-234122r961392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure Tanium has sufficient storage capacity in which to write the audit logs, the SQL Server RDMBS must be configured with sufficient free space. Consult the server sizing documents located at https://docs.tanium.com/platform_install/platform_install/reference_host_system_sizing_guidelines.html to determine how much free space should be allocated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium SQL Server interactively. Log on to their server with an account that has administrative privileges. Consult server sizing documentation at https://docs.tanium.com/platform_install/platform_install/reference_host_system_sizing_guidelines.html and the Tanium system administrator to determine the recommended disk space sizing for the size of the Tanium deployment. Launch File Explorer. Check the total disk space allocated to the hard drive allocated for the Tanium SQL databases. Compare the allocated size against the recommended disk space sizing for the size of the Tanium deployment. If the allocated size is less than the recommended disk space, this is a finding.

## Group: SRG-APP-000435

**Group ID:** `V-234123`

### Rule: The Tanium application must limit the bandwidth used in communicating with endpoints to prevent a Denial of Service (DoS) condition at the server.

**Rule ID:** `SV-234123r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of applications to mitigate the impact of DoS attacks that have occurred or are ongoing on application availability. For each application, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the application opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium Server interactively. Log on to the server with an account that has administrative privileges. Access the server's registry by typing: regedit <enter>. Navigate to HKEY_LOCAL_MACHINE >> SOFTWARE >> Wow6432Node >> Tanium >> Tanium Server. Verify the existence of a DWORD "DownloadBytesPerSecondLimit" with a value matching what is in the system documentation. If the DWORD "DownloadBytesPerSecondLimit" does not exist with the correct value, this is a finding.

## Group: SRG-APP-000456

**Group ID:** `V-234124`

### Rule: The Tanium Application Server must install security-relevant software updates within the time period directed by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).

**Rule ID:** `SV-234124r1067646_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period utilized must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the information assurance vulnerability management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This STIG is sunset and no longer maintained. Check that the version in use is still supported by the vendor. If the version in use is not supported by the vendor, this is a finding. Consult with the Tanium system administrator to review the documented time window designated for updates. If a window of time is not defined, or does not specify a reoccurring frequency, this is a finding. Using a web browser on a system that has connectivity to the Tanium application, access the Tanium application web user interface (UI). Log on with CAC. Click the navigation button (hamburger menu) on the top left of the console. Click "Tanium Solutions". If any module has the text "Upgrade to" a newer (greater) version number compared to the Installed version number in the Tanium Modules section of the page, this is a finding. If the Tanium install is an air gap install, work with the Tanium technical account manager (TAM) to determine if the modules are up to date.

## Group: SRG-APP-000516

**Group ID:** `V-234125`

### Rule: Tanium Server files must be excluded from host-based intrusion prevention intervention.

**Rule ID:** `SV-234125r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Similar to any other host-based applications, the Tanium Server is subject to the restrictions other System-level software may place on an operating environment. Antivirus, IPS, Encryption, or other security and management stack software may disallow the Tanium Server from working as expected. https://docs.tanium.com/platform_install/platform_install/reference_host_system_security_exceptions.html.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the Tanium System Administrator to determine the HIPS software used on the Tanium Server. Review the settings of the HIPS software. Validate exclusions exist which exclude the Tanium program files from being restricted by HIPS. If exclusions do not exist, this is a finding.

## Group: SRG-APP-000295

**Group ID:** `V-234126`

### Rule: The Tanium application must set an absolute timeout for sessions.

**Rule ID:** `SV-234126r1043182_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination terminates all processes associated with a user's logical session except those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific application system functionality where the system owner, data owner, or organization requires additional assurance. Based upon requirements and events specified by the data or application owner, the application developer must incorporate logic into the application that will provide a control mechanism that disconnects users upon the defined event trigger. The methods for incorporating this requirement will be determined and specified on a case-by-case basis during the application design and development stages. Leaving sessions open indefinitely is a major security risk. An attacker can easily use an already authenticated session to access the hosted application as the previously authenticated user. By closing sessions after an absolute period of time, the user is forced to re-authenticate, guaranteeing the session is still in use. Enabling an absolute timeout for sessions closes sessions that are still active.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium application, access the Tanium application web user interface (UI) and log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Administration". Select the "Global Settings" tab. In the "Show Settings Containing:" search box, type "session_expiration_seconds". Click "Enter". If no results are returned, this is a finding. If results are returned for "session_expiration_seconds", but the value is not "900" or less, this is a finding.

## Group: SRG-APP-000295

**Group ID:** `V-234127`

### Rule: The Tanium application must set an inactive timeout for sessions.

**Rule ID:** `SV-234127r1043182_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Leaving sessions open indefinitely is a major security risk. An attacker can easily use an already authenticated session to access the hosted application as the previously authenticated user. By closing sessions after a set period of inactivity, the web server can make certain that sessions that are not closed through the user logging out of an application are eventually closed. Acceptable values are 5 minutes for high-value applications, 10 minutes for medium-value applications, and 20 minutes for low-value applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser on a system that has connectivity to the Tanium application, access the Tanium application web user interface (UI) and log on with CAC. Click on the navigation button (hamburger menu) on the top left of the console. Click on "Administration". Select the "Global Settings" tab. In the "Show Settings Containing:" search box, type "max_console_idle_seconds". Click "Enter". If no results are returned, this is a finding. If results are returned for "max_console_idle_seconds", but the value is not "900" or less, this is a finding.

## Group: SRG-APP-000435

**Group ID:** `V-234128`

### Rule: The Tanium application service must be protected from being stopped by a non-privileged user.

**Rule ID:** `SV-234128r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of applications to mitigate the impact of DoS attacks that have occurred or are ongoing on application availability. For each application, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the application opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks. A web server not properly tuned may become overwhelmed and cause a DoS condition even with expected traffic from users. To avoid a DoS, the web server must be tuned to handle the expected traffic for the hosted applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that to prevent a non-privileged user from affecting the Tanium Server's ability to operate, the control of the service is restricted to the Local Administrators. Log on interactively to the Tanium Server. Open the CMD prompt as admin. Run "sc sdshow "Tanium Server"". If the string does not match "D:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCLCSWLOCRRC;;;AU)S:(AU;FA;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;WD)", this is a finding. Run the above on all other Tanium Servers, to include Tanium Servers in an Active-Active pair.

## Group: SRG-APP-000435

**Group ID:** `V-234129`

### Rule: The Tanium web server must be tuned to handle the operational requirements of the hosted application.

**Rule ID:** `SV-234129r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of applications to mitigate the impact of DoS attacks that have occurred or are ongoing on application availability. For each application, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the application opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks. An attacker has at least two reasons to stop a web server. The first is to cause a Denial of Service (DoS), and the second is to put in place changes the attacker made to the web server configuration. To prohibit an attacker from stopping the web server, the process ID (pid) of the web server and the utilities used to start/stop the web server must be protected from access by non-privileged users. By knowing the pid and having access to the web server utilities, a non-privileged user has a greater capability of stopping the server, whether intentionally or unintentionally.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As part of any Tanium install, Tanium has a tuning process that takes into account customer-provided inputs on the size of the deployment as well as characteristics of the network. Obtain from Tanium the document that states the tuning settings for the particular installation. If the organization cannot provide a server-tuning document from the vendor, this is a finding.

## Group: SRG-APP-000439

**Group ID:** `V-234130`

### Rule: The Tanium application, SQL and Module servers must all be configured to communicate using TLS 1.2 Strict Only.

**Rule ID:** `SV-234130r961632_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised since unprotected communications can be intercepted and either read or altered. This requirement applies only to those applications that are either distributed or can allow access to data non-locally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, applications need to leverage transmission protection mechanisms, such as TLS, SSL VPNs, or IPsec. FIPS 140-2 approved TLS versions must be enabled, and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 defines the approved TLS versions for government applications. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium Servers (Application, SQL and Module) interactively. Log on to the server with an account that has administrative privileges. Access the server's registry by typing: "regedit". Press "Enter". Navigate to: HKEY_LOCAL_MACHINE >> SYSTEM >> CurrentControlSet >> Control >> SecurityProviders >> SCHANNEL >> Protocols >> SSL 2.0 >> Client for Module server. Navigate to: HKEY_LOCAL_MACHINE >> SYSTEM >> CurrentControlSet >> Control >> SecurityProviders >> SCHANNEL >> Protocols >> SSL 2.0 >> Server for Application server and SQL server. Name: DisabledByDefault Type: REG_DWORD Data: 0x0000001 (hex) If the value for "DisabledByDefault" is not set to "1" and "Type" is not configured to "REG_DWORD" or does not exist, this is a finding. Name: Enabled Type: REG_DWORD Data: 0x00000000 (hex) If the value for "Enabled" is not set to "0" and "Type" is not configured to "REG_DWORD" or does not exist, this is a finding.

## Group: SRG-APP-000439

**Group ID:** `V-234131`

### Rule: The Tanium application must be configured to communicate using TLS 1.2 Strict Only.

**Rule ID:** `SV-234131r961632_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised since unprotected communications can be intercepted and either read or altered. This requirement applies only to those applications that are either distributed or can allow access to data non-locally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, applications need to leverage transmission protection mechanisms, such as TLS, SSL VPNs, or IPsec. FIPS 140-2 approved TLS versions must be enabled, and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 defines the approved TLS versions for government applications. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium Server, Tanium Module Server and Tanium SQL Server interactively. Log on to the server with an account that has administrative privileges. Access the server's registry by typing: "regedit". Press "Enter". Navigate to: HKEY_LOCAL_MACHINE >> SOFTWARE >> Wow6432Node >> Microsoft >> .NETFramework >> v4.0.xxxxx (the sub-version number may vary, but it is a 4.0 version; example: 4.0.30319) for Tanium Application Server. Navigate to: HKEY_LOCAL_MACHINE >> SOFTWARE >> Microsoft >> .NETFramework >> v4.0.xxxxx (the sub-version number may vary, but it is a 4.0 version; example: 4.0.30319) for Tanium SQL Server. Navigate to: HKEY_LOCAL_MACHINE >> SOFTWARE >> Microsoft >> .NETFramework >> v4.0.xxxxx (the sub-version number may vary, but it is a 4.0 version; example: 4.0.30319) for Tanium Module Server. Name: SchUseStrongCrypto Type: REG_DWORD Data: 0x0000001 (hex) If the value for "SchUseStrongCrypto" is not set to "0x00000001" (hex) and "Type" is not configured to "REG_DWORD" or does not exist, this is a finding.

## Group: SRG-APP-000439

**Group ID:** `V-234132`

### Rule: The Tanium application must be configured to communicate using TLS 1.2 Strict Only.

**Rule ID:** `SV-234132r961632_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised since unprotected communications can be intercepted and either read or altered. This requirement applies only to those applications that are either distributed or can allow access to data non-locally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, applications need to leverage transmission protection mechanisms, such as TLS, SSL VPNs, or IPsec. FIPS 140-2 approved TLS versions must be enabled, and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 defines the approved TLS versions for government applications. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Tanium Server interactively. Log on to the server with an account that has administrative privileges. Access the server's registry by typing: "regedit". Press "Enter". Navigate to: HKEY_LOCAL_MACHINE >> SOFTWARE >> Wow6432Node >> Tanium >> Tanium Server. Name: SSLCipherSuite Type: String Value:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSAAES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK If the String "SSLCipherSuite" does not exist with the appropriate list values, this is a finding.

