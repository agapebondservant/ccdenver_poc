# STIG Benchmark: Microsoft IIS 10.0 Server Security Technical Implementation Guide

---

**Version:** 3

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000092-WSR-000055

**Group ID:** `V-218786`

### Rule: Both the log file and Event Tracing for Windows (ETW) for the IIS 10.0 web server must be enabled.

**Rule ID:** `SV-218786r1022652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Information Services (IIS) on Windows Server 2012 provides basic logging capabilities. However, because IIS takes some time to flush logs to disk, administrators do not have access to logging information in real-time. In addition, text-based log files can be difficult and time-consuming to process. In IIS 10.0, the administrator has the option of sending logging information to Event Tracing for Windows (ETW). This option gives the administrator the ability to use standard query tools, or create custom tools, for viewing real-time logging information in ETW. This provides a significant advantage over parsing text-based log files that are not updated in real time. Satisfies: SRG-APP-000092-WSR-000055, SRG-APP-000108-WSR-000166, SRG-APP-000358-WSR-000063</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the server is hosting WSUS, this is Not Applicable. Open the IIS 10.0 Manager. Click the IIS 10.0 server name. Click the "Logging" icon. Under Log Event Destination, verify the "Both log file and ETW event" radio button is selected. If the "Both log file and ETW event" radio button is not selected, this is a finding.

## Group: SRG-APP-000099-WSR-000061

**Group ID:** `V-218788`

### Rule: The IIS 10.0 web server must produce log records that contain sufficient information to establish the outcome (success or failure) of IIS 10.0 web server events.

**Rule ID:** `SV-218788r960903_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the success or failure of an event is important during forensic analysis. Correctly determining the outcome will add information to the overall reconstruction of the loggable event. By determining the success or failure of the event correctly, analysis of the enterprise can be undertaken to determine if events tied to the event occurred in other areas within the enterprise. Without sufficient information establishing the success or failure of the logged event, investigation into the cause of event is severely hindered. The success or failure also provides a means to measure the impact of an event and help authorized personnel determine the appropriate response. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the IIS 10.0 web server IIS Manager. Click the IIS 10.0 web server name. Under "IIS", double-click the "Logging" icon. Verify the "Format:" under "Log File" is configured to "W3C". Select the "Fields" button. Under "Custom Fields", verify the following fields have been configured: Request Header >> Connection Request Header >> Warning If any of the above fields are not selected, this is a finding.

## Group: SRG-APP-000100-WSR-000064

**Group ID:** `V-218789`

### Rule: The IIS 10.0 web server must produce log records containing sufficient information to establish the identity of any user/subject or process associated with an event.

**Rule ID:** `SV-218789r960906_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Determining user accounts, processes running on behalf of the user, and running process identifiers also enable a better understanding of the overall event. User tool identification is also helpful to determine if events are related to overall user access or specific client tools. Log record content that may be necessary to satisfy the requirement of this control includes: time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the IIS 10.0 web server IIS Manager. Click the IIS 10.0 web server name. Under "IIS", double-click the "Logging" icon. Verify the "Format:" under "Log File" is configured to "W3C". Select the "Fields" button. Under "Standard Fields", verify "User Agent", "User Name", and "Referrer" are selected. Under "Custom Fields", verify the following field has been configured: Request Header >> Authorization Response Header >> Content-Type If any of the above fields are not selected, this is a finding.

## Group: SRG-APP-000120-WSR-000070

**Group ID:** `V-218790`

### Rule: The log information from the IIS 10.0 web server must be protected from unauthorized modification or deletion.

**Rule ID:** `SV-218790r1067580_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A major tool in exploring the website use, attempted use, unusual conditions, and problems are the access and error logs. In the event of a security incident, these logs can provide the system administrator (SA) and the web manager with valuable information. Failure to protect log files could enable an attacker to modify the log file data or falsify events to mask an attacker's activity. Satisfies: SRG-APP-000120-WSR-000070, SRG-APP-000118-WSR-000068, SRG-APP-000118-WSR-000069</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check does not apply to service account IDs utilized by automated services necessary to process, manage, and store log files. Open the IIS 10.0 Manager. Click the IIS 10.0 web server name. Click the "Logging" icon. Click "Browse" and navigate to the directory where the log files are stored. Right-click the log file directory to review. Click "Properties". Click the "Security" tab. Verify log file access is restricted as follows. Otherwise, this is a finding. SYSTEM - Full Control, This folder, subfolders and files Administrators - Full Control, This folder, subfolders and files Note: A "Web Administrators", etc., type group that is an approved group of administrators is also allowed, and must be given "Full Control, This folder, subfolders and files" permissions.

## Group: SRG-APP-000125-WSR-000071

**Group ID:** `V-218791`

### Rule: The log data and records from the IIS 10.0 web server must be backed up onto a different system or media.

**Rule ID:** `SV-218791r960948_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of log data includes ensuring log data is not accidentally lost or deleted. Backing up log records to an unrelated system, or onto separate media than the system on which the web server is running, helps to ensure the log records will be retained in the event of a catastrophic system failure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The IIS 10.0 web server and website log files should be backed up by the system backup. To determine if log files are backed up by the system backup, determine the location of the web server log files and each website's log files. Open the IIS 10.0 Manager. Click the IIS 10.0 server name. Click the "Logging" icon. Under "Log File" >> "Directory" obtain the path of the log file. Once all locations are known, consult with the System Administrator to review the server's backup procedure and policy. Verify the paths of all log files are part of the system backup. Verify log files are backed up to an unrelated system or onto separate media on which the system the web server is running. If the paths of all log files are not part of the system backup and/or not backed up to a separate media, this is a finding.

## Group: SRG-APP-000141-WSR-000015

**Group ID:** `V-218792`

### Rule: The IIS 10.0 web server must not perform user management for hosted applications.

**Rule ID:** `SV-218792r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User management and authentication can be an essential part of any application hosted by the web server. Along with authenticating users, the user management function must perform several other tasks enterprise-wide, such as password complexity, locking users after a configurable number of failed logons, and management of temporary and emergency accounts. The web server contains a minimal user management function, but the web server user management function does not offer enterprise-wide user management, and user management is not the primary function of the web server. User management for the hosted applications should be done through a facility built for enterprise-wide user management, such as LDAP and Active Directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the System Administrator about the role of the IIS 10.0 web server. If the IIS 10.0 web server is hosting an application, have the SA provide supporting documentation on how the application's user management is accomplished outside of the IIS 10.0 web server. If the IIS 10.0 web server is not hosting an application, this is Not Applicable. If the IIS web server is performing user management for hosted applications, this is a finding. If the IIS 10.0 web server is hosting an application and the SA cannot provide supporting documentation on how the application's user management is accomplished outside of the IIS 10.0 web server, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-218793`

### Rule: The IIS 10.0 web server must only contain functions necessary for operation.

**Rule ID:** `SV-218793r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services deemed non-essential to the web server mission or that adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Click “Start”. Open Control Panel. Click “Programs”. Click “Programs and Features”. Review the installed programs. If any programs are installed other than those required for the IIS 10.0 web services, this is a finding. Note: If additional software is needed, supporting documentation must be signed by the ISSO.

## Group: SRG-APP-000141-WSR-000076

**Group ID:** `V-218794`

### Rule: The IIS 10.0 web server must not be both a website server and a proxy server.

**Rule ID:** `SV-218794r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server should be primarily a web server or a proxy server but not both, for the same reasons that other multi-use servers are not recommended. Scanning for web servers that also proxy requests into an otherwise protected network is a common attack, making the attack anonymous.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the IIS 10.0 Manager. Under the "Connections" pane on the left side of the management console, select the IIS 10.0 web server. If, under the IIS installed features "Application Request Routing Cache" is not present, this is not a finding. If, under the IIS installed features "Application Request Routing Cache" is present, double-click the icon to open the feature. From the right "Actions" pane under "Proxy", select "Server Proxy Settings...". In the "Application Request Routing" settings window, verify whether "Enable proxy" is selected. If "Enable proxy" is selected under the "Application Request Routing" settings, this is a finding. If the server has been approved to be a Proxy server, this requirement is Not Applicable.

## Group: SRG-APP-000141-WSR-000077

**Group ID:** `V-218795`

### Rule: All IIS 10.0 web server sample code, example applications, and tutorials must be removed from a production IIS 10.0 server.

**Rule ID:** `SV-218795r960963_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Web server documentation, sample code, example applications, and tutorials may be an exploitable threat to a web server. A production web server may only contain components that are operationally necessary (i.e., compiled code, scripts, web content, etc.). Delete all directories containing samples and any scripts used to execute the samples.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to the following folders: inetpub\ Program Files\Common Files\System\msadc Program Files (x86)\Common Files\System\msadc If the folder or sub-folders contain any executable sample code, example applications, or tutorials which are not explicitly used by a production website, this is a finding.

## Group: SRG-APP-000141-WSR-000078

**Group ID:** `V-218796`

### Rule: The accounts created by uninstalled features (i.e., tools, utilities, specific, etc.) must be deleted from the IIS 10.0 server.

**Rule ID:** `SV-218796r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accounts used for web server features such as documentation, sample code, example applications, tutorials, utilities, and services created when the feature is not installed, become an exploitable threat to a web server. These accounts become inactive, are not monitored through regular use, and passwords for the accounts are not created or updated. An attacker, through very little effort, can use these accounts to gain access to the web server and begin investigating ways to elevate the account privileges. The accounts used for web server features not installed must not be created and must be deleted when these features are uninstalled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the IIS 10.0 web server. Access “Apps” menu. Under “Administrative Tools”, select “Computer Management”. In the left pane, expand "Local Users and Groups" and click "Users". Review the local users listed in the middle pane. If any local accounts are present and were created by features which have been uninstalled or are not used, this is a finding.

## Group: SRG-APP-000141-WSR-000080

**Group ID:** `V-218797`

### Rule: The IIS 10.0 web server must be reviewed on a regular basis to remove any Operating System features, utility programs, plug-ins, and modules not necessary for operation.

**Rule ID:** `SV-218797r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Just as running unneeded services and protocols is a danger to the web server at the lower levels of the OSI model, running unneeded utilities and programs is a danger at the application layer of the OSI model. Office suites, development tools, and graphic editors are examples of such troublesome programs. Individual productivity tools have no legitimate place or use on an enterprise production web server and are prone to security risks. The web server installation process must provide options allowing the installer to choose which utility programs, services, and modules are to be installed or removed. By having a process for installation and removal, the web server is guaranteed to be in a more stable and secure state than if these services and programs were installed and removed manually.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the System Administrator and review all of the IIS 10.0 and Operating System features installed. Determine if any features installed are no longer necessary for operation. If any utility programs, features, or modules are installed which are not necessary for operation, this is a finding. If any unnecessary Operating System features are installed, this is a finding.

## Group: SRG-APP-000141-WSR-000081

**Group ID:** `V-218798`

### Rule: The IIS 10.0 web server must have Multipurpose Internet Mail Extensions (MIME) that invoke OS shell programs disabled.

**Rule ID:** `SV-218798r1112381_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Controlling what a user of a hosted application can access is part of the security posture of the web server. Any time a user can access more functionality than is needed for the operation of the hosted application poses a security issue. A user with too much access can view information that is not needed for the user's job role, or the user could use the function in an unintentional manner. A MIME tells the web server the type of program, various file types, and extensions and what external utilities or programs are needed to execute the file type. A shell is a program that serves as the basic interface between the user and the operating system to ensure hosted application users do not have access to these programs. Shell programs may execute shell escapes and can perform unauthorized activities that could damage the security posture of the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the server is hosting WSUS, this is not applicable. Open the IIS 10.0 Manager. Click the IIS 10.0 web server name. Under IIS, double-click the "MIME Types" icon. From the "Group by:" drop-down list, select "Content Type". From the list of extensions under "Application", verify MIME types for OS shell program extensions have been removed, to include at a minimum, the following extensions: .exe .dll .com .bat .csh If any OS shell MIME types are configured, this is a finding.

## Group: SRG-APP-000141-WSR-000085

**Group ID:** `V-218799`

### Rule: The IIS 10.0 web server must have Web Distributed Authoring and Versioning (WebDAV) disabled.

**Rule ID:** `SV-218799r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can be installed with functionality that by its nature is not secure. Web Distributed Authoring (WebDAV) is an extension to the HTTP protocol which, when developed, was meant to allow users to create, change, and move documents on a server, typically a web server or web share. Allowing this functionality, development, and deployment is much easier for web authors. WebDAV is not widely used and has serious security concerns because it may allow clients to modify unauthorized files on the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the IIS 10.0 Manager. Click the IIS 10.0 web server name. Review the features listed under the “IIS" section. If the "WebDAV Authoring Rules" icon exists, this is a finding.

## Group: SRG-APP-000206-WSR-000128

**Group ID:** `V-218801`

### Rule: Java software installed on a production IIS 10.0 web server must be limited to .class files and the Java Virtual Machine.

**Rule ID:** `SV-218801r961083_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Mobile code in hosted applications allows the developer to add functionality and displays to hosted applications that are fluid, as opposed to a static web page. The data presentation becomes more appealing to the user, is easier to analyze, and is less complicated to navigate through the hosted application and data. Some mobile code technologies in use in today's applications are: Java, JavaScript, ActiveX, PDF, Postscript, Shockwave movies, Flash animations, and VBScript. The DoD has created policies that define the usage of mobile code on DoD systems. The usage restrictions and implementation guidance apply to both the selection and use of mobile code installed on organizational servers and mobile code downloaded and executed on individual workstations. Source code for a Java program is often stored in files with either .java or .jpp file extensions. From the .java and .jpp files the Java compiler produces a binary file with an extension of .class. The .java or .jpp file could therefore reveal sensitive information regarding an application's logic and permissions to resources on the server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Search the system for files with either .java or .jpp extensions. If files with .java or .jpp extensions are found, this is a finding.

## Group: SRG-APP-000211-WSR-000030

**Group ID:** `V-218802`

### Rule: IIS 10.0 Web server accounts accessing the directory tree, the shell, or other operating system functions and utilities must only be administrative accounts.

**Rule ID:** `SV-218802r961095_rule`
**Severity:** high

**Description:**
<VulnDiscussion>As a rule, accounts on a web server are to be kept to a minimum. Only administrators, web managers, developers, auditors, and web authors require accounts on the machine hosting the web server. This is in addition to the anonymous web user account. The resources to which these accounts have access must also be closely monitored and controlled. Only the SA needs access to all the system’s capabilities, while the web administrator and associated staff require access and control of the web content and web server configuration files. The anonymous web user account must not have access to system resources as that account could then control the server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain a list of the user accounts with access to the system, including all local and domain accounts. Review the privileges to the web server for each account. Verify with the system administrator or the ISSO that all privileged accounts are mission essential and documented. Verify with the system administrator or the ISSO that all non-administrator access to shell scripts and operating system functions are mission essential and documented. If undocumented privileged accounts are found, this is a finding. If undocumented non-administrator access to shell scripts and operating system functions are found, this is a finding. If this IIS 10 installation is supporting Microsoft Exchange, and not otherwise hosting any content, this requirement is Not Applicable.

## Group: SRG-APP-000211-WSR-000129

**Group ID:** `V-218803`

### Rule: The IIS 10.0 web server must separate the hosted applications from hosted web server management functionality.

**Rule ID:** `SV-218803r961095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The separation of user functionality from web server management can be accomplished by moving management functions to a separate IP address or port. To further separate the management functions, separate authentication methods and certificates should be used. By moving the management functionality, the possibility of accidental discovery of the management functions by non-privileged users during hosted application use is minimized.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the IIS 10.0 web server configuration with the System Administrator. Determine if the IIS 10.0 web server hosts any applications. If the IIS 10.0 web server does not host any applications, this is Not Applicable. If the IIS 10.0 web server is hosting Exchange, this is Not Applicable. If the IIS 10.0 web server hosts applications, review the application's management functionality and authentication methods with the System Administrator to determine if the management of the application is accomplished with the same functions and authentication methods as the web server management. If the IIS 10.0 web server management and the application's management functionality is not separated, this is a finding.

## Group: SRG-APP-000223-WSR-000011

**Group ID:** `V-218804`

### Rule: The IIS 10.0 web server must use cookies to track session state.

**Rule ID:** `SV-218804r1043180_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cookies are used to exchange data between the web server and the client. Cookies, such as a session cookie, may contain session information and user credentials used to maintain a persistent connection between the user and the hosted application since HTTP/HTTPS is a stateless protocol. Using URI will embed the session ID as a query string in the Uniform Resource Identifier (URI) request and then the URI is redirected to the originally requested URL. The changed URI request is used for the duration of the session, so no cookie is necessary. By requiring expired session IDs to be regenerated while using URI, potential attackers have less time to capture a cookie and gain access to the Web server content. Satisfies: SRG-APP-000223-WSR-000011, SRG-APP-000220-WSR-000201</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If ASP.NET is not installed, this is Not Applicable. Open the IIS 10.0 Manager. Click the IIS 10.0 web server name. Under "ASP.Net", double-click the "Session State" icon. Under "Cookie Settings", verify the "Mode" has "Use Cookies" selected from the drop-down list. If the "Cookie Settings" "Mode" is not set to "Use Cookies", this is a finding. Alternative method: Click the site name. Select "Configuration Editor" under the "Management" section. From the "Section:" drop-down list at the top of the configuration editor, locate "system.web/sessionState". Verify the "cookieless" is set to "UseCookies". If the "cookieless" is not set to "UseCookies", this is a finding. Note: If IIS 10.0 server/site is used only for system-to-system maintenance, does not allow users to connect to interface, and is restricted to specific system IPs, this is Not Applicable.

## Group: SRG-APP-000223-WSR-000145

**Group ID:** `V-218805`

### Rule: The IIS 10.0 web server must accept only system-generated session identifiers.

**Rule ID:** `SV-218805r1067583_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ASP.NET provides a session state, which is available as the HttpSessionState class, as a method of storing session-specific information that is visible only within the session. ASP.NET session state identifies requests from the same browser during a limited time window as a session and provides the ability to persist variable values for the duration of that session. When using the URI mode for cookie settings under session state, IIS will reject and reissue session IDs that do not have active sessions. Configuring IIS to expire session IDs and regenerate tokens gives a potential attacker less time to capture a cookie and gain access to server content.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If ASP.NET is not installed, this is Not Applicable. Open the IIS 10.0 Manager. Click the IIS 10.0 web server name. Under the "ASP.NET" section, select "Session State". Under "Cookie Settings", verify the "Use Cookies" mode is selected from the "Mode:" drop-down list. Under "Time-out (in minutes)", verify a maximum of 15 minutes is entered. If the "Use Cookies" mode is selected and Time-out (in minutes) is configured for "15 minutes" (or less), this is not a finding. Alternative method: Click the site name. Select "Configuration Editor" under the "Management" section. From the "Section:" drop-down list at the top of the configuration editor, locate "system.web/sessionState". Verify the "cookieless" is set to "UseCookies". If the "cookieless" is not set to "UseCookies", this is a finding. Note: If IIS 10.0 server/site is used only for system-to-system maintenance, does not allow users to connect to interface, and is restricted to specific system IPs, this is Not Applicable.

## Group: SRG-APP-000225-WSR-000074

**Group ID:** `V-218806`

### Rule: The IIS 10.0 web server must augment re-creation to a stable and known baseline.

**Rule ID:** `SV-218806r961122_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Making certain that the web server has not been updated by an unauthorized user is always a concern. Adding patches, functions, and modules that are untested and not part of the baseline opens the possibility for security risks. The web server must offer, and not hinder, a method that allows for the quick and easy reinstallation of a verified and patched baseline to guarantee the production web server is up-to-date and has not been modified to add functionality or expose security risks. When the web server does not offer a method to roll back to a clean baseline, external methods, such as a baseline snapshot or virtualizing the web server, can be used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the System Administrator for the IIS 10.0 web server. Ask for documentation on the disaster recovery methods tested and planned for the IIS 10.0 web server in the event of the necessity for rollback. If documentation for a disaster recovery has not been established, this is a finding.

## Group: SRG-APP-000231-WSR-000144

**Group ID:** `V-218807`

### Rule: The production IIS 10.0 web server must utilize SHA2 encryption for the Machine Key.

**Rule ID:** `SV-218807r1067586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Machine Key element of the ASP.NET web.config specifies the algorithm and keys that ASP.NET will use for encryption. The Machine Key feature can be managed to specify hashing and encryption settings for application services such as view state, forms authentication, membership and roles, and anonymous identification. Ensuring a strong encryption method can mitigate the risk of data tampering in crucial functional areas such as forms authentication cookies, or view state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If ASP.NET is not installed, this is Not Applicable. Note: If the IIS 10.0 web server is hosting Exchange, this is Not Applicable. Open the IIS 10.0 Manager. Click the IIS 10.0 web server name. Double-click the "Machine Key" icon in the website Home Pane. Verify "HMACSHA256" or stronger encryption is selected for the Validation method and "Auto" is selected for the Encryption method. If "HMACSHA256" or stronger encryption is not selected for the Validation method and/or "Auto" is not selected for the Encryption method, this is a finding. If .NET is not installed, this is Not Applicable.

## Group: SRG-APP-000251-WSR-000157

**Group ID:** `V-218808`

### Rule: Directory Browsing on the IIS 10.0 web server must be disabled.

**Rule ID:** `SV-218808r961158_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Directory browsing allows the contents of a directory to be displayed upon request from a web client. If directory browsing is enabled for a directory in IIS, users could receive a web page listing the contents of the directory. If directory browsing is enabled, the risk of inadvertently disclosing sensitive content is increased.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the IIS 10.0 Manager. Click the IIS 10.0 web server name. Double-click the "Directory Browsing" icon. Under the “Actions” pane verify "Directory Browsing" is disabled. If “Directory Browsing” is not disabled, this is a finding.

## Group: SRG-APP-000266-WSR-000142

**Group ID:** `V-218809`

### Rule: The IIS 10.0 web server Indexing must only index web content.

**Rule ID:** `SV-218809r961167_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The indexing service can be used to facilitate a search function for websites. Enabling indexing may facilitate a directory traversal exploit and reveal unwanted information to a malicious user. Indexing must be limited to web document directories only.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the IIS 10.0 Web Server. Access an administrator command prompt and type "regedit <enter>" to access the server's registry. Navigate to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ContentIndex\Catalogs\. If this key exists, then indexing is enabled. If the key does not exist, this check is Not Applicable. Review the Catalog keys to determine if directories other than web document directories are being indexed. If so, this is a finding.

## Group: SRG-APP-000266-WSR-000159

**Group ID:** `V-218810`

### Rule: Warning and error messages displayed to clients must be modified to minimize the identity of the IIS 10.0 web server, patches, loaded modules, and directory paths.

**Rule ID:** `SV-218810r1022657_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>HTTP error pages contain information that could enable an attacker to gain access to an information system. Failure to prevent the sending of HTTP error pages with full information to remote requesters exposes internal configuration information to potential attackers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the server is hosting WSUS, this is Not Applicable. Open the IIS 10.0 Manager. Click the IIS 10.0 web server name. Double-click the "Error Pages" icon. Click any error message, and then click "Edit Feature Setting" from the "Actions" Pane. This will apply to all error messages. If the feature setting is not set to "Detailed errors for local requests and custom error pages for remote requests", or "Custom error pages" this is a finding.

## Group: SRG-APP-000315-WSR-000004

**Group ID:** `V-218812`

### Rule: The IIS 10.0 web server must restrict inbound connections from non-secure zones.

**Rule ID:** `SV-218812r961278_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. A web server can be accessed remotely and must be capable of restricting access from what the DoD defines as non-secure zones. Non-secure zones are defined as any IP, subnet, or region defined as a threat to the organization. The non-secure zones must be defined for public web servers logically located in a DMZ, as well as private web servers with perimeter protection devices. By restricting access from non-secure zones through internal web server access lists, the web server can stop or slow denial of service (DoS) attacks on the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement applies to the Web Management Service. If the Web Management Service is not installed, this is Not Applicable. Open the IIS 10.0 Manager. Click the IIS 10.0 web server name. Under "Management", double-click "Management Service". If "Enable remote connections" is not selected, this is Not Applicable. If "Enable remote connections" is selected, review the entries under "IP Address Restrictions". Verify only known, secure IP ranges are configured as "Allow". If "IP Address Restrictions" are not configured or IP ranges configured to "Allow" are not restrictive enough to prevent connections from nonsecure zones, this is a finding.

## Group: SRG-APP-000316-WSR-000170

**Group ID:** `V-218813`

### Rule: The IIS 10.0 web server must provide the capability to immediately disconnect or disable remote access to the hosted applications.

**Rule ID:** `SV-218813r961281_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>During an attack on the web server or any of the hosted applications, the system administrator may need to disconnect or disable access by users to stop the attack. The web server must provide a capability to disconnect users to a hosted application without compromising other hosted applications unless deemed necessary to stop the attack. Methods to disconnect or disable connections are to stop the application service for a specified hosted application, stop the web server, or block all connections through web server access list. The web server capabilities used to disconnect or disable users from connecting to hosted applications and the web server must be documented to make certain that, during an attack, the proper action is taken to conserve connectivity to any other hosted application if possible and to make certain log data is conserved for later forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the System Administrator and Web Manager. Ask for documentation for the IIS 10.0 web server administration. Verify there are documented procedures for shutting down an IIS 10.0 website in the event of an attack. The procedure should, at a minimum, provide the following steps: Determine the respective website for the application at risk of an attack. Access the IIS 10.0 web server IIS Manager. Select the respective website. In the "Actions" pane, under "Manage Website", click "Stop". If necessary, stop all websites. If necessary, stop the IIS 10.0 web server by selecting the web server in the IIS Manager. In the "Actions" pane, under "Manage Server", click "Stop". If the web server is not capable or cannot be configured to disconnect or disable remote access to the hosted applications when necessary, this is a finding.

## Group: SRG-APP-000340-WSR-000029

**Group ID:** `V-218814`

### Rule: IIS 10.0 web server system files must conform to minimum file permission requirements.

**Rule ID:** `SV-218814r1067589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This check verifies the key web server system configuration files are owned by the SA or the web administrator controlled account. These same files that control the configuration of the web server, and thus its behavior, must also be accessible by the account running the web service. If these files are altered by a malicious user, the web server would no longer be under the control of its managers and owners; properties in the web server configuration could be altered to compromise the entire server platform.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open Explorer and navigate to the inetpub directory. Right-click "inetpub" and select "Properties". Click the "Security" tab. Verify the permissions for the following users; if the permissions are less restrictive, this is a finding. System: Full control Administrators: Full control TrustedInstaller: Full control ALL APPLICATION PACKAGES (built-in security group): Read and execute, This folder, subfolders and files ALL RESTRICTED APPLICATION PACKAGES (built-in security group): Read and execute, This folder, subfolders and files Users: Read and execute, list folder contents CREATOR OWNER: Full Control, Subfolders and files only

## Group: SRG-APP-000357-WSR-000150

**Group ID:** `V-218815`

### Rule: The IIS 10.0 web server must use a logging mechanism configured to allocate log record storage capacity large enough to accommodate the logging requirements of the IIS 10.0 web server.

**Rule ID:** `SV-218815r961392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure the logging mechanism used by the web server has sufficient storage capacity in which to write the logs, the logging mechanism must be able to allocate log record storage capacity. The task of allocating log record storage capacity is usually performed during initial installation of the logging mechanism. The system administrator will usually coordinate the allocation of physical drive space with the web server administrator along with the physical location of the partition and disk. Refer to NIST SP 800-92 for specific requirements on log rotation and storage dependent on the impact of the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the IIS 10.0 Manager. Click the IIS 10.0 web server name. Under "IIS" double-click the "Logging" icon. In the "Logging" configuration box, determine the "Directory:" to which the "W3C" logging is being written. Confirm with the System Administrator that the designated log path is of sufficient size to maintain the logging. Under "Log File Rollover", verify "Do not create new log files" is not selected. Verify a schedule is configured to rollover log files on a regular basis. Consult with the System Administrator to determine if there is a documented process for moving the log files off of the IIS 10.0 web server to another logging device. If the designated logging path device is not of sufficient space to maintain all log files, and there is not a schedule to rollover files on a regular basis, this is a finding.

## Group: SRG-APP-000380-WSR-000072

**Group ID:** `V-218816`

### Rule: Access to web administration tools must be restricted to the web manager and the web managers designees.

**Rule ID:** `SV-218816r1067591_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can be modified through parameter modification, patch installation, upgrades to the web server or modules, and security parameter changes. With each of these changes, there is the potential for an adverse effect such as a DoS, web server instability, or hosted application instability. To limit changes to the web server and limit exposure to any adverse effects from the changes, files such as the web server application files, libraries, and configuration files must have permissions and ownership set properly to only allow privileged users access. The key web service administrative and configuration tools must only be accessible by the web server staff. All users granted this authority will be documented and approved by the ISSO. Access to the IIS Manager will be limited to authorized users and administrators. Satisfies: SRG-APP-000380-WSR-000072, SRG-APP-000435-WSR-000147, SRG-APP-000033-WSR-000169</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Right-click "InetMgr.exe", then click "Properties" from the "Context" menu. Select the "Security" tab. Review the groups and user names. The following accounts may have Full control privileges: TrustedInstaller Web Managers Web Manager designees CREATOR OWNER The following accounts may have read and execute, or read permissions: Non Web Manager Administrators ALL APPLICATION PACKAGES (built-in security group) ALL RESTRICTED APPLICATION PACKAGES (built-in security group) SYSTEM Users Specific users may be granted read and execute and read permissions. Compare the local documentation authorizing specific users, against the users observed when reviewing the groups and users. If any other access is observed, this is a finding.

## Group: SRG-APP-000383-WSR-000175

**Group ID:** `V-218817`

### Rule: The IIS 10.0 web server must not be running on a system providing any other role.

**Rule ID:** `SV-218817r961470_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web servers provide numerous processes, features, and functionalities that utilize TCP/IP ports. Some of these processes may be deemed unnecessary or too unsecure to run on a production system. The web server must provide the capability to disable or deactivate network-related services deemed non-essential to the server mission, are too unsecure, or are prohibited by the PPSM CAL and vulnerability assessments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review programs installed on the OS. Open Control Panel. Open Programs and Features. The following programs may be installed without any additional documentation: Administration Pack for IIS IIS Search Engine Optimization Toolkit Microsoft .NET Framework version 3.5 SP1 or greater Microsoft Web Platform Installer version 3.x or greater Virtual Machine Additions Review the installed programs, if any programs are installed other than those listed above, this is a finding. Note: If additional software is needed and has supporting documentation signed by the ISSO, this is not a finding.

## Group: SRG-APP-000383-WSR-000175

**Group ID:** `V-218818`

### Rule: The Internet Printing Protocol (IPP) must be disabled on the IIS 10.0 web server.

**Rule ID:** `SV-218818r961470_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of IPP on an IIS web server allows client access to shared printers. This privileged access could allow remote code execution by increasing the web servers attack surface. Additionally, since IPP does not support SSL, it is considered a risk and will not be deployed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Print Services role and the Internet Printing role are not installed, this check is Not Applicable. Navigate to the following directory: %windir%\web\printers If this folder exists, this is a finding. Determine whether Internet Printing is enabled: Click “Start”, click “Administrative Tools”, and then click “Server Manager”. Expand the roles node, right-click “Print Services”, and then select “Remove Roles Services”. If the Internet Printing option is enabled, this is a finding.

## Group: SRG-APP-000435-WSR-000148

**Group ID:** `V-218819`

### Rule: The IIS 10.0 web server must be tuned to handle the operational requirements of the hosted application.

**Rule ID:** `SV-218819r1022659_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A Denial of Service (DoS) can occur when the web server is overwhelmed and can no longer respond to additional requests. A web server not properly tuned may become overwhelmed and cause a DoS condition even with expected traffic from users. To avoid a DoS, the web server must be tuned to handle the expected traffic for the hosted applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IIS 10.0 web server is not hosting any applications, this is Not Applicable. If the IIS 10.0 web server is hosting applications, consult with the system administrator to determine risk analysis performed when the application was written and deployed to the IIS 10.0 web server. Obtain documentation on the configuration. Verify, at a minimum, the following tuning settings in the registry. Access the IIS 10.0 web server registry. Verify the following keys are present and configured. The required setting depends upon the requirements of the application. Recommended settings are not provided as these settings must be explicitly configured to show a conscientious tuning has been made. Navigate to HKLM\SYSTEM\CurrentControlSet\Services\HTTP\Parameters\ REG_DWORD "URIEnableCache" REG_DWORD "UriMaxUriBytes" REG_DWORD "UriScavengerPeriod" If explicit settings are not configured for "URIEnableCache", "UriMaxUriBytes" and "UriScavengerPeriod", this is a finding.

## Group: SRG-APP-000439-WSR-000152

**Group ID:** `V-218820`

### Rule: IIS 10.0 web server session IDs must be sent to the client using TLS.

**Rule ID:** `SV-218820r961632_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The HTTP protocol is a stateless protocol. To maintain a session, a session identifier is used. The session identifier is a piece of data used to identify a session and a user. If the session identifier is compromised by an attacker, the session can be hijacked. By encrypting the session identifier, the identifier becomes more difficult for an attacker to hijack, decrypt, and use before the session has expired.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the IIS 10.0 Manager. Click the IIS 10.0 web server name. Under the "Management" section, double-click the "Configuration Editor" icon. From the "Section:" drop-down list, select "system.webServer/asp". Expand the "session" section. Verify the "keepSessionIdSecure" is set to "True". If the "keepSessionIdSecure" is not set to "True", this is a finding.

## Group: SRG-APP-000439-WSR-000156

**Group ID:** `V-218821`

### Rule: An IIS 10.0 web server must maintain the confidentiality of controlled information during transmission through the use of an approved Transport Layer Security (TLS) version.

**Rule ID:** `SV-218821r1067596_rule`
**Severity:** high

**Description:**
<VulnDiscussion>TLS encryption is a required security setting for a private web server. Encryption of private information is essential to ensuring data confidentiality. If private information is not encrypted, it can be intercepted and easily read by an unauthorized party. A private web server must use a FIPS 140-2-approved TLS version, and all non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 specifies the preferred configurations for government systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the IIS 10.0 Web Server. Navigate to: HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server Verify a REG_DWORD value of "0" for "DisabledByDefault". Verify a REG_DWORD value of "1" for "Enabled". Navigate to: HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Server HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0\Server Verify a REG_DWORD value of "1" for "DisabledByDefault". Verify a REG_DWORD value of "0" for "Enabled". If any of the respective registry paths do not exist or are configured with the wrong value, this is a finding. SSL 3.0 is disabled by default in newer Operating Systems. If SSL 3.0 has a registry DWORD enabled with a value of 1, this is a finding. If this key is not present, this is not a finding.

## Group: SRG-APP-000439-WSR-000156

**Group ID:** `V-218822`

### Rule: The IIS 10.0 web server must maintain the confidentiality of controlled information during transmission through the use of an approved Transport Layer Security (TLS) version.

**Rule ID:** `SV-218822r961632_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>TLS is a required transmission protocol for a web server hosting controlled information. The use of TLS provides confidentiality of data in transit between the web server and client. FIPS 140-2-approved TLS versions must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 defines the approved TLS versions for government applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the web server documentation and deployed configuration to determine which version of TLS is being used. If the TLS version is not TLS 1.2 or higher, according to NIST SP 800-52, or if non-FIPS-approved algorithms are enabled, this is a finding.

## Group: SRG-APP-000516-WSR-000079

**Group ID:** `V-218823`

### Rule: All accounts installed with the IIS 10.0 web server software and tools must have passwords assigned and default passwords changed.

**Rule ID:** `SV-218823r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>During installation of the web server software, accounts are created for the web server to operate properly. The accounts installed can have either no password installed or a default password, which will be known and documented by the vendor and the user community. The first things an attacker will try when presented with a logon screen are the default user identifiers with default passwords. Installed applications may also install accounts with no password, making the logon even easier. Once the web server is installed, the passwords for any created accounts should be changed and documented. The new passwords must meet the requirements for all passwords, i.e., upper/lower characters, numbers, special characters, time until change, reuse policy, etc. Service accounts or system accounts that have no logon capability do not need to have passwords set or changed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the IIS 10.0 web server. Access the "Apps" menu. Under "Administrative Tools", select "Computer Management". In left pane, expand "Local Users and Groups" and click "Users". Review the local users listed in the middle pane. If any local accounts are present and used by IIS 10.0, verify with System Administrator that default passwords have been changed. If passwords have not been changed from the default, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-218824`

### Rule: Unspecified file extensions on a production IIS 10.0 web server must be removed.

**Rule ID:** `SV-218824r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By allowing unspecified file extensions to execute, the web servers attack surface is significantly increased. This increased risk can be reduced by only allowing specific ISAPI extensions or CGI extensions to run on the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the IIS 10.0 Manager. Click the IIS 10.0 web server name. Double-click the "ISAPI and CGI restrictions" icon. Click “Edit Feature Settings". Verify the "Allow unspecified CGI modules" and the "Allow unspecified ISAPI modules" check boxes are NOT checked. If either or both of the "Allow unspecified CGI modules" and the "Allow unspecified ISAPI modules" check boxes are checked, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-218825`

### Rule: The IIS 10.0 web server must have a global authorization rule configured to restrict access.

**Rule ID:** `SV-218825r1067593_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authorization rules can be configured at the server, website, folder (including Virtual Directories), or file level. It is recommended that URL Authorization be configured to only grant access to the necessary security principals. Configuring a global Authorization rule that restricts access ensures inheritance of the settings down through the hierarchy of web directories. This will ensure access to current and future content is only granted to the appropriate principals, mitigating risk of unauthorized access. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If ASP.NET is not installed, this is Not Applicable. Note: If the Server is hosting Microsoft SharePoint, this is Not Applicable. Note: If the server is hosting WSUS, this is Not Applicable. Note: If the server is hosting Exchange, this is Not Applicable. Note: If the server is public facing, this is Not Applicable. Note: If the website is behind a load balancer or proxy server, this is Not Applicable. Open the IIS 10.0 Manager. Click the IIS 10.0 web server name. Double-click the ".NET Authorization Rules" icon. Ensure "All Users" is set to "Allow", and "Anonymous Users" is set to "Deny", otherwise this is a finding. If any other rules are present, this is a finding.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-218826`

### Rule: The IIS 10.0 websites MaxConnections setting must be configured to limit the number of allowed simultaneous session requests.

**Rule ID:** `SV-218826r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Resource exhaustion can occur when an unlimited number of concurrent requests are allowed on a website, facilitating a Denial of Service (DoS) attack. Mitigating this kind of attack will include limiting the number of concurrent HTTP/HTTPS requests per IP address and may include, where feasible, limiting parameter values associated with keepalive (i.e., a parameter used to limit the amount of time a connection may be inactive).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the IIS 10.0 IIS Manager. Click the IIS 10.0 server. Select "Configuration Editor" under the "Management" section. From the "Section:" drop-down list at the top of the configuration editor, locate "system.applicationHost/sites". Expand "siteDefaults". Expand "limits". Review the results and verify the value is greater than zero for the "maxconnections" parameter. If the maxconnections parameter is set to zero, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-218827`

### Rule: The IIS 10.0 web server must enable HTTP Strict Transport Security (HSTS).

**Rule ID:** `SV-218827r1112380_rule`
**Severity:** low

**Description:**
<VulnDiscussion>HTTP Strict Transport Security (HSTS) ensures browsers always connect to a website over TLS. HSTS exists to remove the need for redirection configurations. HSTS relies on the browser, web server, and a public "Allowlist". If the browser does not support HSTS, it will be ignored.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the server is hosting WSUS, this is not applicable. Note: If the server is providing OCSP, and not otherwise hosting any content, this requirement is not applicable. Access the IIS 10.0 Web Server. Open IIS Manager. Click the IIS 10.0 web server name. Open on Configuration Editor under Management. For the Section, navigate to system.applicationHost/sites. Expand siteDefaults and HSTS. If enabled is not set to True, this is a finding. If includeSubDomains is not set to True, this is a finding. If max-age is not set to a value greater than 0, this is a finding. If redirectHttpToHttps is not True, this is a finding. If the website is behind a load balancer or proxy server, and HSTS enablement is handled there, this is not applicable. If the version of Windows Server does not natively support HSTS, this is not a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-228572`

### Rule: An IIS Server configured to be a SMTP relay must require authentication.

**Rule ID:** `SV-228572r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Anonymous SMTP relays are strictly prohibited. An anonymous SMTP relay can be a vector for many types of malicious activity not limited to server exploitation for the sending of SPAM mail, access to emails, phishing, DoS attacks, etc. Enabling TLS, authentication, and strictly assigning IP addresses that can communicate with the relay greatly reduce the risk of the implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the System Administrator about the role of the IIS 10.0 web server. If the IIS 10.0 web server is running SMTP relay services, have the SA provide supporting documentation on how the server is hardened. A DoD-issued certificate, and specific allowed IP address should be configured. If the IIS web server is not running SMTP relay services, this is Not Applicable. If the IIS web server running SMTP relay services without TLS enabled, this is a finding. If the IIS web server running SMTP relay services is not configured to only allow a specific IP address, from the same network as the relay, this is a finding.

## Group: SRG-APP-000266-WSR-000159

**Group ID:** `V-241788`

### Rule: HTTPAPI Server version must be removed from the HTTP Response Header information.

**Rule ID:** `SV-241788r1025160_rule`
**Severity:** low

**Description:**
<VulnDiscussion>HTTP Response Headers contain information that could enable an attacker to gain access to an information system. Failure to prevent the sending of certain HTTP Response Header information to remote requesters exposes internal configuration information to potential attackers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the server is hosting WSUS, this is Not Applicable. Open Registry Editor. Navigate to "HKLM\System\CurrentControlSet\Services\HTTP\Parameters" Verify "DisableServerHeader” is set to "2". If REG_DWORD DisableServerHeader is not set to 2, this is a finding. If the System Administrator can show that Server Version information has been removed via other means, such as using a rewrite outbound rule, this is not a finding.

## Group: SRG-APP-000266-WSR-000159

**Group ID:** `V-241789`

### Rule: ASP.NET version must be removed from the HTTP Response Header information.

**Rule ID:** `SV-241789r1022662_rule`
**Severity:** low

**Description:**
<VulnDiscussion>HTTP Response Headers contain information that could enable an attacker to gain access to an information system. Failure to prevent the sending of certain HTTP Response Header information to remote requesters exposes internal configuration information to potential attackers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If ASP.NET is not installed, this is Not Applicable. Open the IIS 10.0 Manager. Under the "Connections" pane on the left side of the management console, select the IIS 10.0 web server. Click the HTTP Response Headers button. Click to select the “X-Powered-By” HTTP Header. If “X-Powered-By” has not been removed, this is a finding.

## Group: SRG-APP-000141-WSR-000015

**Group ID:** `V-268325`

### Rule: The Request Smuggling filter must be enabled.

**Rule ID:** `SV-268325r1025163_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security scans show Request Smuggling vulnerability on IIS server. The vulnerability allows a remote attacker to perform HTTP request smuggling attack. The vulnerability exists due to the way that HTTP proxies (front-end) and web servers (back-end) that do not strictly adhere to RFC standards handle sequences of HTTP requests received from multiple sources. A remote attacker can send a specially crafted request to a targeted IIS Server, perform HTTP request smuggling attack and modify responses or retrieve information from another user's HTTP session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open Registry Editor. Navigate to "HKLM\System\CurrentControlSet\Services\HTTP\Parameters" Verify "DisableRequestSmuggling” is set to "1". If REG_DWORD DisableRequestSmuggling is not set to 1, this is a finding.

