# STIG Benchmark: APACHE 2.2 Server for Windows Security Technical Implementation Guide

---

**Version:** 1

**Description:**
All directives specified in this STIG must be specifically set (i.e. the server is not allowed to revert to programmed defaults for these directives). Included files should be reviewed if they are used. Procedures for reviewing included files are included in the overview document. The use of .htaccess files are not authorized for use according to the STIG. However, if they are used, there are procedures for reviewing them in the overview document. The Web Policy STIG should be used in addition to the Apache Site and Server STIGs in order to do a comprehensive web server review.

## Group: WG420

**Group ID:** `V-2230`

### Rule: Backup interactive scripts on the production web server must be prohibited.

**Rule ID:** `SV-33092r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Copies of backup files will not execute on the server, but can be read by the anonymous user if special precautions are not taken. Such backup copies contain the same sensitive information as the actual script being executed and as such are useful to malicious users. Techniques and systems exist today which search web servers for such files and are able to exploit the information contained in them. Backup copies of files are automatically created by some text editors such as emacs and edit plus. Having backup scripts on the web server provides one more opportunities for malicious persons to view these scripts and use information found in them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
This check is limited to CGI/interactive content and not static HTML. Find on all hard drives files containing the following extensions: *.bak, *.old, *.temp, *.tmp, or *.backup. If files with these extensions are found in either the document directory or the home directory of the web server, this is a finding. If files with these extensions are stored in a repository (not in the document root) as backups for the web server, this is a finding. If files with these extensions have no relationship with web activity, such as a backup batch file for operating system utility, and they are not accessible by the web application, this is not a finding.

## Group: WG050

**Group ID:** `V-2232`

### Rule: The web server service password(s) must be entrusted to the SA or Web Manager.

**Rule ID:** `SV-33048r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Normally, a service account is established for the web server. This is because a privileged account is not desirable and the server is designed to run for long uninterrupted periods of time. The SA or Web Manager will need password access to the web server to restart the service in the event of an emergency as the web server is not to restart automatically after an unscheduled interruption. If the password is not entrusted to an SA or web manager the ability to ensure the availability of the web server is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
The reviewer should make a note of the name of the account being used for the web service. There may also be other server services running related to the web server in support of a particular web application, these passwords must be entrusted to the SA or Web Manager as well. Query the SA or Web Manager to determine if they have the web service password(s). If the web services password(s) are not entrusted to the SA or Web Manager, this is a finding. NOTE: For installations that use the LocalService or NetworkService accounts, the password is OS generated, so the SA or Web Manager having an Admin account on the system would meet the intent of this check.

## Group: WG040

**Group ID:** `V-2234`

### Rule: Public web server resources must not be shared with private assets.

**Rule ID:** `SV-33044r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is important to segregate public web server resources from private resources located behind the DoD DMZ in order to protect private assets. When folders, drives or other resources are directly shared between the public web server and private servers the intent of data and resource segregation can be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
The reviewer should query the ISSO, the SA, or the web administrator as necessary to determine if the public web server has a two-way trusted relationship with any private asset. Private web server resources (e.g., drives, folders, printers, etc.) will not be directly mapped to or shared with public web servers. The following check indicates an inappropriate sharing of public web server resources: Navigate to the web server content folders/directories. These directories must not be shared. On the web server content folder, right-click on Properties, then select sharing. All entries must be disabled. If sharing is selected for any web folder, this is a finding. The following checks indicate inappropriate sharing of private resources with the public web server: 1. From a command prompt, type net share and Enter. This will provide a list of available shares. 2. Check to see if file and printer or file-sharing is enabled under the Network icon in the Control Panel. If private resources (e.g., drives, partitions, folders/directories, printers, etc.) are shared with the public web server, this is a finding.

## Group: WG060

**Group ID:** `V-2235`

### Rule: The service account used to run the web service must have its password changed at least annually.


**Rule ID:** `SV-36489r4_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Normally, a service account is established for the web service to run under rather than permitting it to run as part of the local system. The password on such accounts must be changed at least annually. If the password is not changed periodically, the potential for a malicious party to gain access to the web services account is greatly enhanced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSO and confirm with the SA, the Web Manager, or the individual in an equivalent role. Ask for the web server’s documented procedures and processes. Verify the documented procedures and processes identify web server related service accounts, which services are related to web server operations and include a policy requiring service account passwords to be change at least annually. If the documented procedures and processes do not identify web server related service accounts, which services are related to web server operations and include a policy requiring service account passwords to be change at least annually, this is a finding.

## Group: WG080

**Group ID:** `V-2236`

### Rule: Installation of a compiler on production web server must be prohibited.

**Rule ID:** `SV-33061r3_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The presence of a compiler on a production server facilitates the malicious user’s task of creating custom versions of programs and installing Trojan Horses or viruses. For example, the attacker’s code can be uploaded and compiled on the server under attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Using Windows Explorer, search the system for the existence of known compilers such as msc.exe, msvc.exe, Python.exe, javac.exe, Lcc-win32.exe, or equivalent. Look in all hard drives. Also, query the SA and the Web Manager to determine if a compiler is present on the server. Query the SA and the Web Manager to determine if a compiler is present on the server. If a compiler is present, this is a finding. NOTE: When Apache is part of a suite install, e.g. application server, and a compiler is needed for installation and patching of the product, document the installation of the compiler with the ISSO/ISSM and verify that the compiler is restricted to administrative users only. If documented and restricted to administrative users, this is not a finding.

## Group: WA060

**Group ID:** `V-2242`

### Rule: A public web server, if hosted on the NIPRNet, must be isolated in an accredited DoD DMZ Extension.

**Rule ID:** `SV-33012r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To minimize exposure of private assets to unnecessary risk by attackers, public web servers must be isolated from internal systems. Public web servers are by nature more vulnerable to attack from publically based sources, such as the public Internet. Once compromised, a public web server might be used as a base for further attack on private resources, unless additional layers of protection are implemented. Public web servers must be located in a DoD DMZ Extension, if hosted on the NIPRNet, with carefully controlled access. Failure to isolate resources in this way increase risk that private assets are exposed to attacks from public sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Interview the SA or web administrator to see where the public web server is logically located in the data center. Review the site’s network diagram to see how the web server is connected to the LAN. Visually check the web server hardware connections to see if it conforms to the site’s network diagram. An improperly located public web server is a potential threat to the entire network. If the web server is not isolated in an accredited DoD DMZ Extension, this is a finding.

## Group: WA070

**Group ID:** `V-2243`

### Rule: A private web server must be located on a separate controlled access subnet.

**Rule ID:** `SV-33013r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Private web servers, which host sites that serve controlled access data, must be protected from outside threats in addition to insider threats. Insider threat may be accidental or intentional but, in either case, can cause a disruption in service of the web server. To protect the private web server from these threats, it must be located on a separate controlled access subnet and must not be a part of the public DMZ that houses the public web servers. It also cannot be located inside the enclave as part of the local general population LAN.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
This check verifies that the private web server is located on a separate controlled access subnet and is not a part of the public DMZ that houses the public web servers. In addition, the private web server needs to be isolated via a controlled access mechanism from the local general population LAN. Interview the ISSO and confirm with the SA, the Web Manager, or the individual in an equivalent role. Ask for the web server’s documented procedures and processes. Verify the documented procedures and processes include verbiage and a diagram clearly showing what devices (router, switch, firewall) lie between the private web server and the Internet, showing the private web server’s location on a separate subnet dedicated to functions not intended for public access. If the documented procedures and processes do include verbiage and/or do not include a diagram clearly showing what devices (router, switch, firewall) lie between the private web server and the Internet, showing the private web server’s location on a separate subnet dedicated to functions not intended for public access, this is a finding.

## Group: WG190

**Group ID:** `V-2246`

### Rule: The web server must use a vendor-supported version of the web server software.

**Rule ID:** `SV-33068r2_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Many vulnerabilities are associated with old versions of web server software. As hot fixes and patches are issued, these solutions are included in the next version of the server software. Maintaining the web server at a current version makes the efforts of a malicious user to exploit the web service more difficult.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine the version of the Apache software that is running on the system. Use the command line interface and navigate to the directory where Apache httpd Server is installed. From the command line type the following command: httpd.exe –v. Press Enter. This will display the version of apache installed on the system. Note: There are other ways, too, of determining the version of Apache (in the service itself and Add/Remove programs). If the version of Apache is not at the following version or higher, this is a finding. Apache httpd server version 2.2 - Release 2.2.31 (July 2015)

## Group: WG200

**Group ID:** `V-2247`

### Rule: Administrators must be the only users allowed access to the directory tree, the shell, or other operating system functions and utilities.

**Rule ID:** `SV-36509r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>As a rule, accounts on a web server are to be kept to a minimum. Only administrators, web managers, developers, auditors, and web authors require accounts on the machine hosting the web server. This is in addition to the anonymous web user account. The resources to which these accounts have access must also be closely monitored and controlled. Only the SA needs access to all the system’s capabilities, while the web administrator and associated staff require access and control of the web content and web server configuration files. The anonymous web user account must not have access to system resources as that account could then control the server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Windows 2008 servers may be impacted by this check. If the SA or the web administrator can demonstrate that this requirement will adversely affect the web server by providing vendor documentation, this check is not applicable. Search all of the system’s hard drives for the command.com and cmd.exe files. The allowed permissions on these files are: System Full Control Administrators Full Control Examine account access and any group membership access to these files. If any non-administrator account, group membership, or service ID has any access to any command.com or cmd.exe files and the access is documented as mission critical, this is not a finding. Examine access to operating system configuration files, scripts, utilities, privileges, and functions. If any non-administrator account, group membership, or service ID has any access to any of these operating system components and the access is documented as mission critical, this is not a finding. If any non-administrator account, group membership, or service ID has undocumented access to any listed file or operating system component, this is a finding.

## Group: WG220

**Group ID:** `V-2248`

### Rule: Web administration tools must be restricted to the web manager and the web manager’s designees.

**Rule ID:** `SV-33072r4_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All automated information systems are at risk of data loss due to disaster or compromise. Failure to provide adequate protection to the administration tools creates risk of potential theft or damage that may ultimately compromise the mission. Adequate protection ensures that server administration operates with less risk of losses or operations outages. The key web service administrative and configuration tools must be accessible only by the authorized web server administrators. All users granted this authority must be documented and approved by the ISSO. Access to the IIS Manager will be limited to authorized users and administrators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Configuration of the Apache web server is accomplished by editing flat .conf files. Interview the ISSO and ask for the web server’s documented procedures and processes. Verify the documented procedures and processes explicitly document the roles and responsibilities for the web server and web site(s) management. These documented roles will be used to validate access controls for this check. For the purpose of this check, the SA is responsible for the OS platform of the webserver. The web server manager manages the Apache installation and configuration and the web master manages the web site or sites. In some environments, the SA is also the web manager/web master. In such case, the roles should still be documented. Locate the folder in which the Apache installation’s httpd.conf and supporting .conf files are located. Right-click on the folder name and select “Properties”. Select the “Security” tab and review the accounts and assigned permissions. The System Administrator(s), web manager(s) and web master(s), as identified in the organization’s documentation, may have Full Control to the installation folder and sub-folders. Non-documented administrators, non-elevated administrators and users may have Read only permissions to the installation folder and sub-folders. If any accounts other than the documented SA, web manager, or web manager designees have greater than Read permissions to the web administration tool or control files, this is a finding.

## Group: WG130

**Group ID:** `V-2251`

### Rule: All utility programs, not necessary for operations, must be removed or disabled.

**Rule ID:** `SV-33062r2_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Just as running unneeded services and protocols is a danger to the web server at the lower levels of the OSI model, running unneeded utilities and programs is also a danger at the application layer of the OSI model. Office suites, development tools, and graphical editors are examples of such programs that are troublesome. Individual productivity tools have no legitimate place or use on an enterprise, production web server and they are also prone to their own security risks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Query the ISSO, the SA, the web administrator, or developers as necessary to determine if the web server is configured with unnecessary software. Query the SA to determine if processes other than those that support the web server are loaded and/or run on the web server. Examples of software that should not be on the web server are all web development tools, office suites (unless the web server is a private web development server), compilers, and other utilities that are not part of the web server suite or the basic operating system. 1) Check the directory structure of the server and ensure that additional, unintended, or unneeded applications are not loaded on the system. 2) Start >> All Programs >> check for programs services such as: Front Page MS Access MS Excel MS Money MS Word Third-party text editors Graphics editors If, after review of the application on the system, the SA cannot provide justification for the requirement of the identified software, this is a finding.

## Group: WG270

**Group ID:** `V-2255`

### Rule: The web server’s htpasswd files (if present) must reflect proper ownership and permissions.

**Rule ID:** `SV-36561r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In addition to OS restrictions, access rights to files and directories can be set on a web site using the web server software. That is, in addition to allowing or denying all access rights, a rule can be specified that allows or denies partial access rights. For example, users can be given read-only access rights to files, to view the information but not change the files. This check verifies that the htpasswd file is only accessible by system administrators or web managers, with the account running the web service having group permissions of read and execute. Htpasswd is a utility used by Netscape and Apache to provide for password access to designated web sites. I</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Search for the htpasswd.exe file. Right click the htpasswd file, if present. Select the Properties window, select the Security tab. Examine the access rights for the file. The SA or Web Manager account should have Full Control, the account running the web service should have read and execute permissions. If entries other than Administrators, Web Manager account, or System are present, this is a finding.

## Group: WG280

**Group ID:** `V-2256`

### Rule: The access control files are owned by a privileged web server account.

**Rule ID:** `SV-6881r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This check verifies that the key web server system configuration files are owned by the SA or Web Manager controlled account. These same files which control the configuration of the web server, and thus its behavior, must also be accessible by the account which runs the web service. If these files are altered by a malicious user, the web server would no longer be under the control of its managers and owners; properties in the web server configuration could be altered to compromise the entire server platform. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If .htaccess or the .htaccess.html files are in use, the SA or Web Manager account may have Full Control, the non-privileged web server account running the web service should have read and execute permissions. Right click the .htaccess.html file, if present. Select the Properties window, select the Security tab. Examine the access rights for the file. The SA or Web Manager account should have Full Control, the account running the web service should have read and execute permissions. If entries other than Administrators, the Web Manager accounts, or System for any degree of access are present, this is a finding.

## Group: WA120

**Group ID:** `V-2257`

### Rule: Administrative users and groups that have access rights to the web server must be documented.

**Rule ID:** `SV-33017r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>There are typically several individuals and groups that are involved in running a production web site. In most cases, we can identify several types of users on a web server. These are the System Administrators (SAs), Web Managers, Auditors, Authors, Developers, and the Clients. Accounts will be restricted to those who are necessary to maintain web services, review the server’s operation, and the operating system. A detailed record of these accounts must be maintained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Proposed Questions: How many user accounts are associated with the web site operation and maintenance? Where are these accounts documented? Working with the SA or the web administrator, determine if the documentation matches an examination of the privileged IDs on the server. Using User Manager, User Manager for Domains, or Local Users and Groups, examine user accounts to verify the above information. Query the SA or the Web Manager regarding the use of each account and each group found on the server. If the documentation does not match the users and groups found on the server, this is a finding.

## Group: WG300

**Group ID:** `V-2259`

### Rule: Web server system files must conform to minimum file permission requirements.

**Rule ID:** `SV-33078r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This check verifies that the key web server system configuration files are owned by the SA or Web Manager controlled account. These same files which control the configuration of the web server, and thus its behavior, must also be accessible by the account which runs the web service. If these files are altered by a malicious user, the web server would no longer be under the control of its managers and owners; properties in the web server configuration could be altered to compromise the entire server platform.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate and examine the httpd.conf file. Look for the section: <ServerRoot>. This section will contain the path to the configuration and binary files. Note: This check also applies to any other directory where CGI scripts are located. Permissions on this directory files should be: Administrators: Full control System: Full Control WebAdmin: Full Control WebUser: Read, Execute Apache Service Account: Read, Execute Permissions for the /config directory should be as follows: (This is a sub directory to the main apache directory identified above) Administrators: Full control System: Read WebAdmin: Modify Apache Service Account: Read Permissions for the /bin directory should be as follows: (This is a sub directory to the main apache directory identified above) Administrators: Full control System: Read, Execute WebAdmin: Modify Apache Service Account: Read, Execute Permissions for the /logs directory should be as follows: (This is a sub directory to the main apache directory identified above) Administrators: Read System: Full Control WebAdmin: Read Apache Service Account: Modify Auditors: Full Control Permissions for the /htdocs directory (DocumentRoot) should be as follows: (This is a sub directory to the main apache directory identified above) Administrators: Full control System: Read WebAdmin: Modify Apache Service Account: Read If any of the above permissions are less restrictive, this is a finding. Note: There may be additional directories based the local implementation, and permissions should apply to directories of similar content. Ex. all web content directories should follow the permissions for /htdocs.

## Group: WG330

**Group ID:** `V-2261`

### Rule: A public web server must limit e-mail to outbound only.

**Rule ID:** `SV-33082r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Incoming E-mail has been known to provide hackers with access to servers. Disabling the incoming mail service prevents this type of attacks. Additionally, Email represents the main use of the Internet. It is specialized application that requires the dedication of server resources. To combine this type of transaction processing function with the file serving role of the web server creates an inherent conflict. Supporting mail services on a web server opens the server to the risk of abuse as an email relay. This check verifies, by checking the OS, that incoming e-mail is not supported.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
This check verifies, by checking the OS, that incoming e-mail is not supported. Select START >> Programs >> Administrative Tools >> Services Scroll down and review all the entries. If there is a mail program (SMTP service), then the reviewer must run that program to see if it will accept incoming e-mail (There are too many different programs for detailed instructions). The reviewer should also check the Programs menu and sub-menus under start to see if there are any installed mail programs. The reviewer can also check the Add/Delete programs icon in the Control Panel to see if there are any e-mail programs installed. If there is an e-mail program installed and that program has been configured to accept inbound email, this is a finding.

## Group: WG470

**Group ID:** `V-2264`

### Rule: Wscript.exe and Cscript.exe must only be accessible by the SA and/or the web administrator.

**Rule ID:** `SV-33095r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Windows Scripting Host (WSH) is installed under either a Typical or Custom installation option of a Microsoft Network Server. This technology permits the execution of powerful script files from the Windows NT command line. This technology is also classified as a Category I Mobile Code. If the access to these files is not tightly controlled, a malicious user could readily compromise the server by using a form to send input to these scripting engines.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Search for instances of Wscript.exe and Cscript.exe. Move to these files, if found, and right-click on them to view their Properties. Permissions should only exist for System, the SA, and the web administrator, who may have Full Control. User accounts with access to these files that are unknown, or unintended, should be removed. If these files have permission for other than the SA, the web administrator, or the system, this is a finding.

## Group: WG440

**Group ID:** `V-2271`

### Rule: Monitoring software must include CGI or equivalent programs in its scope.

**Rule ID:** `SV-33089r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By their very nature, CGI type files permit the anonymous web user to interact with data and perhaps store data on the web server. In many cases, CGI scripts exercise system-level control over the server’s resources. These files make appealing targets for the malicious user. If these files can be modified or exploited, the web server can be compromised. These files must be monitored by a security tool that reports unauthorized changes to these files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
CGI or equivalent files must be monitored by a security tool that reports unauthorized changes. It is the purpose of such software to monitor key files for unauthorized changes to them. The reviewer should query the ISSO, the SA, and the web administrator and verify the information provided by asking to see the template file or configuration file of the software being used to accomplish this security task. Example file extensions for files considered to provide active content are, but not limited to: .cgi, .asp, .aspx, .class, .vb, .php, .pl, and .c. If the site does not have a process in place to monitor changes to CGI program files, this is a finding.

## Group: WA140

**Group ID:** `V-6485`

### Rule: Web server content and configuration files must be part of a routine backup program.

**Rule ID:** `SV-33014r2_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Backing up web server data and web server application software after upgrades or maintenance ensures that recovery can be accomplished up to the current version. It also provides a means to determine and recover from subsequent unauthorized changes to the software and data. A tested and verifiable backup strategy will be implemented for web server software as well as all web server data files. Backup and recovery procedures will be documented and the Web Manager or SA for the specific application will be responsible for the design, test, and implementation of the procedures. The site will have a contingency processing plan/disaster recovery plan that includes web servers. The contingency plan will be periodically tested in accordance with DoDI 8500.2 requirements. The site will identify an off-site storage facility in accordance with DoDI 8500.2 requirements. Off-site backups will be updated on a regular basis and the frequency will be documented in the contingency plan.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
The reviewer should query the Information Systems Security Officer (ISSO), SA, Web Manager, Webmaster or developers as necessary to determine whether or not a tested and verifiable backup strategy has been implemented for web server software as well as all web server data files. Proposed Questions: Who maintains the backup and recovery procedures? Do you have a copy of the backup and recovery procedures? Where is the off-site backup location? Is the contingency plan documented? When was the last time the contingency plan was tested? Are the test dates and results documented? If there is not a backup and recovery process for the web server, this is a finding.

## Group: WG204

**Group ID:** `V-6577`

### Rule: A web server installation must be segregated from other services.

**Rule ID:** `SV-33070r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The web server installation and configuration plan should not support the co-hosting of multiple services such as Domain Name Service (DNS), e-mail, databases, search engines, indexing, or streaming media on the same server that is providing the web publishing service. By separating these services additional defensive layers are established between the web service and the applicable application should either be compromised. Disallowed or restricted services in the context of this vulnerability applies to services that are not directly associated with the delivery of web content. An operating system that supports a web server will not provide other services (e.g., domain controller, e-mail server, database server, etc.). Only those services necessary to support the web server and its hosted sites are specifically allowed and may include, but are not limited to, operating system, logging, anti-virus, host intrusion detection, administrative maintenance, or network requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Request a copy of and review the web server’s installation and configuration plan. Ensure that the server is in compliance with this plan. If the server is not in compliance with the plan, this is a finding. Query the SA to ascertain if and where the additional services are installed. Confirm that the additional service or application is not installed on the same partition as the operating systems root, web server root, or web document root. If it is, this is a finding.

## Group: WG520

**Group ID:** `V-6724`

### Rule: Web server and/or operating system information must be protected.

**Rule ID:** `SV-33098r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The web server response header of an HTTP response can contain several fields of information including the requested HTML page. The information included in this response can be web server type and version, operating system and version, and ports associated with the web server. This provides the malicious user valuable information without the use of extensive tools.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the httpd.conf file. Open the httpd.conf file with an editor such as Notepad, and search for the following uncommented directive: ServerTokens The directive ServerTokens must be set to “Prod” (ex. ServerTokens Prod). This directive controls whether Server response header field that is sent back to clients that includes a description of the OS-type of the server as well as information about compiled-in modules. If the web server or operating system information is sent to the client via the server response header, this is a finding. If the directive does not exist, this would be a finding as it defaults to Full.

## Group: WA155

**Group ID:** `V-13591`

### Rule: Classified web servers will be afforded physical security commensurate with the classification of its content.

**Rule ID:** `SV-33015r2_rule`
**Severity:** high

**Description:**
<VulnDiscussion>When data of a classified nature is migrated to a web server, fundamental principles applicable to the safeguarding of classified material must be followed. A classified web server needs to be afforded physical security commensurate with the classification of its content to ensure the protection of the data it houses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Officer</Responsibility><IAControls></IAControls>

**Check Text:**
The reviewer should query the ISSO, the SA, the web administrator, or developers as necessary to determine if a classified web server is afforded physical security commensurate with the classification of its content (i.e., is located in a vault or a room approved for classified storage at the highest classification processed on that system). Ask what the classification of the web server is, and based on the classification, evaluate the location of the web server to determine if it is approved for storage of that classification level. If the web server is not appropriately physically protected based on its classification, this is a finding.

## Group: WA230

**Group ID:** `V-13613`

### Rule: The site software used with the web server must have all applicable security patches applied and documented.

**Rule ID:** `SV-33016r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The IAVM process does not address all patches that have been identified for the host operating system or, in this case, the web server software environment. Many vendors have subscription services available to notify users of known security threats. The site needs to be aware of these fixes and make determinations based on local policy and what software features are installed, if these patches need to be applied. In some cases, patches also apply to middleware and database systems. Maintaining the security of web servers requires frequent reviews of security notices. Many security notices mandate the installation of a software patch to overcome security vulnerabilities. SAs and ISSOs should regularly check the vendor support web site for patches and information related to the web server software. All applicable security patches will be applied to the operating system and to the web server software. Security patches are deemed applicable if the product is installed, even if it is not used or is disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><IAControls></IAControls>

**Check Text:**
Query the web administrator to determine if the site has a detailed process as part of its configuration management plan to stay compliant with all security-related patches. Proposed Questions: How does the SA stay current with web server vendor patches? How is the SA notified when a new security patch is issued by the vendor? (Exclude the IAVM.) What is the process followed for applying patches to the web server? If the site is not in compliance with all applicable security patches, this is a finding.

## Group: WG275

**Group ID:** `V-13619`

### Rule: The web server, although started by superuser or privileged account, must run using a non-privileged account.

**Rule ID:** `SV-36607r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Running the web server with excessive privileges presents an increased risk to the web server. In the event the web server’s services are compromised, the context by which the web server is running will determine the amount of damage that may be caused by the attacker. If the web server is run as an administrator or as an equivalent account, the attacker will gain administrative access through the web server. If, on the other hand, the web server is running with least privilege required to function, the capabilities of the attacker will be greatly decreased.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Work with the web administrator to determine the account assigned to the web server service. Once this is determined, right click on My Computer and select Manage. Then select Configuration, followed by Local Users and Groups. Examine the account that is used to run the web server service and determine the group affiliations. The Apache server account may be a member of the users group and in some cases the site may have created a separate group for the apache web server. Both of these are not findings. If the user account assigned to the web server service is a member of any other group than users or the created web server group, the SA will need to provide justification showing that these permissions are necessary for the function and operation of the web server. NOTE: The Apache account needs to have the following rights, which would not be a finding: Act as part of the Operating System & Log on as a Service.

## Group: WG355

**Group ID:** `V-13620`

### Rule: A private web server’s list of CAs in a trust hierarchy must lead to an authorized DoD PKI Root CA.

**Rule ID:** `SV-33084r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A PKI certificate is a digital identifier that establishes the identity of an individual or a platform. A server that has a certificate provides users with third-party confirmation of authenticity. Most web browsers perform server authentication automatically; the user is notified only if the authentication fails. The authentication process between the server and the client is performed using the SSL/TLS protocol. Digital certificates are authenticated, issued, and managed by a trusted Certification Authority (CA). The use of a trusted certificate validation hierarchy is crucial to the ability to control access to your server and prevent unauthorized access. This hierarchy needs to lead to the DoD PKI Root CA or to an approved External Certificate Authority (ECA) or are required for the server to function.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><IAControls></IAControls>

**Check Text:**
The reviewer will need to have the SA or Web Manager show the list of CA’s the server is trusting to authenticate users. NOTE: There are non DoD roots that must be on the server in order for it to function. Some applications, such as anti-virus programs, require root CAs to function. The location for the conf file that controls the SSL parameters may vary from installation, so the following is just an example of a default httpd-ssl.conf file. Open httpd-ssl.conf and search for the following directive: SSLCACertificateFile This directive will point to the file that contains the certificates that are used to identify the CAs that are used for client authentication. Such a file is simply the concatenation of the various PEM-encoded Certificate files, in order of preference. Examine the contents of this file to determine if the trusted CAs are DoD approved. DoD approved can include the External Certificate Authorities (ECA), if approved by the DAA. The PKE InstallRoot 3.06 System Administrator Guide (SAG), dated 8 Jul 2008, contains a complete list of DoD, ECA, and IECA CAs. If the trusted CAs that are used to authenticate users to the web site does not lead to an approved DoD CA, this is a finding.

## Group: WG385

**Group ID:** `V-13621`

### Rule: All web server documentation, sample code, example applications, and tutorials must be removed from a production web server.

**Rule ID:** `SV-33087r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Web server documentation, sample code, example applications, and tutorials may be an exploitable threat to a web server. A production web server may only contain components that are operationally necessary (e.g., compiled code, scripts, web-content, etc.). Delete all directories that contain samples and any scripts used to execute the samples. If there is a requirement to maintain these directories at the site on non-production servers for training purposes, have NTFS permissions set to only allow access to authorized users (i.e., web administrators and systems administrators). Sample applications or scripts have not been evaluated and approved for use and may introduce vulnerabilities to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance>Any sample application or sample executable script found on the production web server will be a CAT I finding. Any web server documentation or sample file found on the production web server and accessible to web users or non-administrators will be a CAT III finding. Any web server documentation or sample file found on the production web server and accessible only to SAs or to web administrators is permissible and not a finding. </SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Query the SA to determine if all directories that contain samples and any scripts used to execute the samples have been removed from the server. Each web server has its own list of sample files. This may change with the software versions, but the following are some examples of what to look for (This is not a definitive list of sample files, but only an example of the common samples that are provided with the associated web server. This list will be updated as additional information is discovered.): [Drive Letter]:/[directory path]/apache2/manual/*.* [Drive Letter]:/[directory path]/apache2/conf/extra/*.* [Drive Letter]:/[directory path]/apache2/cgi-bin/printenv [Drive Letter]:/[directory path]/apache2/cgi-bin/test-cgi If there is a requirement to maintain these directories at the site for training or other such purposes, have permissions or set the permissions to only allow access to authorized users. If any sample files are found on the web server, this is a finding.

## Group: WG145

**Group ID:** `V-13672`

### Rule: The private web server must use an approved DoD certificate validation process.

**Rule ID:** `SV-33065r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of a certificate validation process, the site is vulnerable to accepting certificates that have expired or have been revoked. This would allow unauthorized individuals access to the web server. This also defeats the purpose of the multi-factor authentication provided by the PKI process.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
The reviewer should query the ISSO, the SA, the web administrator, or developers as necessary to determine if the web server is configured to utilize an approved DoD certificate validation process. The web administrator should be questioned to determine if a validation process is being utilized on the web server. To validate this, the reviewer can ask the web administrator to describe the validation process being used. They should be able to identify either the use of certificate revocation lists (CRLs) or Online Certificate Status Protocol (OCSP). If the production web server is accessible, the SA or the web administrator should be able to demonstrate the validation of good certificates and the rejection of bad certificates. If CRLs are being used, the SA should be able to identify how often the CRL is updated and the location from which the CRL is downloaded. If the web administrator cannot identify the type of validation process being used, this is a finding.

## Group: WG237

**Group ID:** `V-13687`

### Rule: Remote authors or content providers must have all files scanned for malware before uploading files to the Document Root directory.

**Rule ID:** `SV-40826r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote web authors should not be able to upload files to the DocumentRoot directory structure without virus checking and checking for malicious or mobile code. A remote web user whose agency has a Memorandum of Agreement (MOA) with the hosting agency and has submitted a DoD form 2875 (System Authorization Access Request (SAAR)) or an equivalent document will be allowed to post files to a temporary location on the server. All posted files to this temporary location will be scanned for viruses and content checked for malicious or mobile code. Only files free of viruses and malicious or mobile code will be posted to the appropriate Document Root directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Remote web authors should not be able to upload files to the Document Root directory structure without virus checking and checking for malicious or mobile code. Query the SA to determine if there is anti-virus software active on the server with auto-protect enabled, or if there is another process in place for the scanning of files being posted by remote authors. If there is no virus software on the system with auto-protect enabled, or if there is not a process in place to ensure all files being posted are being virus scanned before being saved to the document root, this is a finding.

## Group: WA000-WWA020

**Group ID:** `V-13724`

### Rule: The Timeout directive must be properly set.

**Rule ID:** `SV-32980r3_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>These Timeout requirements are set to mitigate the effects of several types of denial of service attacks. Although there is some latitude concerning the settings themselves, the requirements attempt to provide reasonable limits for the protection of the web server. If necessary, these limits can be adjusted to accommodate the operational requirement of a given system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
NOTE: This setting must be explicitly set. Locate the Apache httpd.conf file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directive: Timeout Every enabled Timeout directive value needs to be 300 or less. If any directive is set improperly, this is a finding. NOTE: This vulnerability can be documented locally with the ISSM/ISSO if the site has an operational reason for the use of an increased value. If the site has this documented, this should be marked as Not a Finding.

## Group: WA000-WWA022

**Group ID:** `V-13725`

### Rule: The KeepAlive directive must be enabled.

**Rule ID:** `SV-32987r3_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The KeepAlive extension to HTTP/1.0 and the persistent connection feature of HTTP/1.1 provide long lived HTTP sessions which allow multiple requests to be sent over the same connection. These requirements are set to mitigate the effects of several types of denial of service attacks. Although there is some latitude concerning the settings themselves, the requirements attempt to provide reasonable limits for the protection of the web server. If necessary, these limits can be adjusted to accommodate the operational requirement of a given system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
NOTE: This setting must be explicitly set. Locate the Apache httpd.conf file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directive: KeepAlive Every enabled KeepAlive value needs to be set to “On”. If any directive is set improperly, this is a finding. If any directive is set to “Off”, this is a finding. NOTE: This vulnerability can be documented locally with the ISSM/ISSO if the site has an operational reason for not using persistent connections. If the site has this documented, this should be marked as Not a Finding.

## Group: WA000-WWA024

**Group ID:** `V-13726`

### Rule: The KeepAliveTimeout directive must be defined.

**Rule ID:** `SV-32880r3_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The number of seconds Apache will wait for a subsequent request before closing the connection. Once a request has been received, the timeout value specified by the Timeout directive applies. Setting KeepAliveTimeout to a high value may cause performance problems in heavily loaded servers. The higher the timeout, the more server processes will be kept occupied waiting on connections with idle clients. These requirements are set to mitigate the effects of several types of denial of service attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
NOTE: This setting must be explicitly set. Locate the Apache httpd.conf file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directive: KeepAliveTimeout If any directive is not set to 15 or less, this is a finding. NOTE: This vulnerability can be documented locally with the ISSM/ISSO if the site has an operational reason for not using persistent connections. If the site has this documented, this should be marked as Not a Finding.

## Group: WA000-WWA050

**Group ID:** `V-13731`

### Rule: All interactive programs must be placed in a designated directory with appropriate permissions.

**Rule ID:** `SV-32998r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>CGI scripts are one of the most exploited vulnerabilities on web servers. CGI script execution in Apache can be accomplished via two methods. The first method uses the ScriptAlias directive to tell the server everything in that directory is a CGI script. The second method uses a combination of the Options directive and AddHandler or SetHandler directives. For situations where the combination of the Options directive and Handler directives are used, the ability to centrally manage scripts is lost, creating vulnerability on the web server. It is best to manage scripts using the ScriptAlias directive.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directives: SetHandler, AddHandler, and Options. For all occurrences of the SetHandler and AddHandler directives query the Web Administrator to determine if the directives are allowing CGI scripts to be used. If CGI Scripts are used via the SetHandler or AddHandler directives, this is a finding. For all occurrences of the Options directive that are using +ExecCGI or ExecCGI, this is a finding. If the Options directive is found with -ExecCGI, this is not a finding. If the value does not exist, this would be a finding unless the Options statement is set to “None”.

## Group: WA000-WWA052

**Group ID:** `V-13732`

### Rule: The FollowSymLinks setting must be disabled.

**Rule ID:** `SV-33001r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Options directive configures the web server features that are available in particular directories. The FollowSymLinks option controls the ability of the server to follow symbolic links. A symbolic link allows a file or a directory to be referenced using a symbolic name raising a potential hazard if symbolic linkage is made to a sensitive area. When web scripts are executed and symbolic links are allowed, the web user could be allowed to access locations on the web server that are outside the scope of the web document root or home directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directive: Options Review all uncommented Options statements for the following value: -FollowSymLinks If the value is found with an Options statement, and it does not have a preceding “-”, this is a finding. Notes: - If the value does NOT exist, this is a finding. - If all enabled Options statement are set to None this is not a finding.

## Group: WA000-WWA054

**Group ID:** `V-13733`

### Rule: Server side includes (SSIs) must run with execution capability disabled.

**Rule ID:** `SV-33003r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Options directive configures the web server features that are available in particular directories. The IncludesNOEXEC feature controls the ability of the server to utilize SSIs while disabling the exec command, which is used to execute external scripts. If the full includes feature is used it could allow the execution of malware leading to a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. If unable to locate the file, perform a search of the system to find the location of the file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directive: Options Review all uncommented Options statements for the following values: +IncludesNoExec, -IncludesNoExec, or -Includes If these values are found on an enabled Options statement, this is not a finding. If these values do not exist at all, this would be a finding unless the enabled Options statement is set to “None”. If any enabled Options statement has "Includes” or "+Includes” as part of its statement, this is a finding.

## Group: WA000-WWA056

**Group ID:** `V-13734`

### Rule: The MultiViews directive must be disabled.

**Rule ID:** `SV-33004r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Apache HTTPD supports content negotiation as described in the HTTP/1.1 specification. It can choose the best representation of a resource based on the browser-supplied preferences for media type, languages, character set and encoding. It also implements a couple of features to give more intelligent handling of requests from browsers that send incomplete negotiation information. Content negotiation, or more accurately content selection, is the selection of the document that best matches the clients capabilities, from one of several available documents. There are two implementations of this. • A type map (a file with the handler type-map) which explicitly lists the files containing the variants. • A Multiviews search (enabled by the Multiviews Options), where the server does an implicit filename pattern match, and choose from amongst the results. A MultiViews search is where the server does an implicit filename pattern match, and chooses from the results. For example, if you have a file called configuration.php (or other extension) in root folder and you set up a rule in your htaccess for a virtual folder called configuration/ then you'll have a problem with your rule because the server will choose configuration.php automatically if MultiViews is enabled. An attacker can use the MultiViews functionality to aid in finding hidden file processes on the directory and potentially gather further sensitive information. MultiViews is a per-directory option, meaning it can be set, or explicitly disabled, with an Options directive within a <Directory>, <Location> or <Files> section in httpd.conf, or (if AllowOverride is properly set) in .htaccess files. To explicitly disable an Options functionality, the option must be listed on every uncommented Options directive with a preceding the option. The "-" preceding the option configures Apache to explicitly disable the option. An Options directive with "none" will also disable the functionality. If the option is listed on an Options directive line without a preceding - or without anything preceding it or with a "+" preceding it or not configured at all, the MultiViews option is enabled and is vulnerable. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. Open the httpd.conf file with an editor such as Notepad, and search for all occurrences of the following directive: Options. This check validates occurrences of the Options directive which are uncommented. Review all uncommented Options statements for "-MultiViews"and validate a preceding "-" to the MultiViews option exists. If the value is found on the Options statement, and it does not have a preceding "-", this is a finding. If the value does not exist at all, this would be a finding unless the enabled Options statement is set to "none".

## Group: WA000-WWA058

**Group ID:** `V-13735`

### Rule: Directory indexing must be disabled on directories not containing index files.

**Rule ID:** `SV-33006r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Directory options directives are directives that can be applied to further restrict access to file and directories. If a URL which maps to a directory is requested, and there is no DirectoryIndex (e.g., index.html) in that directory, then mod_autoindex will return a formatted listing of the directory. The Indexes option allows for the functionality of presenting a formatted listing of the directory. Returning a formatted listing of the directory represents a vulnerability since it will allow an attacker to have knowledge of the directory contents and potentially gather sensitive information. To explicitly disable an Options functionality, the option must be listed on every uncommented Options directive with a preceding the option. The "-" preceding the option configures Apache to explicitly disable the option. An Options directive with "none" will also disable the functionality. If the option is listed on an Options directive line without a preceding - or without anything preceding it or with a "+" preceding it or not configured at all, the Indexes option is enabled and is vulnerable. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Open the httpd.conf file with an editor such as Notepad, and search for all occurrences of the following directive: Options. This check validates occurrences of the Options directive which are uncommented. Review all uncommented Options statements for "-Indexes" and validate a preceding "-" to the Indexes option exists. If the value is found on the Options statement, and it does not have a preceding "-", this is a finding. If the value does not exist at all, this would be a finding unless the enabled Options statement is set to "none".

## Group: WA000-WWA060

**Group ID:** `V-13736`

### Rule: The HTTP request message body size must be limited.

**Rule ID:** `SV-33008r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Buffer overflow attacks are carried out by a malicious attacker sending amounts of data that the web server cannot store in a given size buffer. The eventual overflow of this buffer can overwrite system memory. Subsequently an attacker may be able to elevate privileges and take control of the server. The Apache directives listed below limit the size of the various HTTP header sizes thereby limiting the chances for a buffer overflow. The LimitRequestBody directive allows the user to set a limit on the allowed size of an HTTP request message body within the context in which the directive is given (server, per-directory, per-file or per-location). If the client request exceeds that limit, the server will return an error response instead of servicing the request. The size of a normal request message body will vary greatly depending on the nature of the resource and the methods allowed on that resource. CGI scripts typically use the message body for retrieving form information. Implementations of the PUT method will require a value at least as large as any representation that the server wishes to accept for that resource. This directive gives the server administrator greater control over abnormal client request behavior, which may be useful for avoiding some forms of denial-of-service attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directive: LimitRequestBody If the value of LimitRequestBody is not greater than 0 or does not exist, this is a finding.

## Group: WA000-WWA062

**Group ID:** `V-13737`

### Rule: The HTTP request header fields must be limited.

**Rule ID:** `SV-33009r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Buffer overflow attacks are carried out by a malicious attacker sending amounts of data that the web server cannot store in a given size buffer. The eventual overflow of this buffer can overwrite system memory. Subsequently an attacker may be able to elevate privileges and take control of the server. This Apache directive limits the size of the various HTTP header sizes, thereby limiting the chances for a buffer overflow. The LimitRequestFields directive allows the server administrator to modify the limit on the number of request header fields allowed in an HTTP request. A server needs this value to be larger than the number of fields that a normal client request might include. The number of request header fields used by a client rarely exceeds 20, but this may vary among different client implementations, often depending upon the extent to which a user has configured their browser to support detailed content negotiation. Optional HTTP extensions are often expressed using request header fields. This directive gives the server administrator greater control over abnormal client request behavior, which may be useful for avoiding some forms of denial-of-service attacks. The value should be increased if normal clients see an error response from the server that indicates too many fields were sent in the request.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. If unable to locate the file, perform a search of the system to find the location of the file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directive: LimitRequestFields Every enabled LimitRequestFields value needs to be greater than 0. If any directive is set improperly, this is a finding. Note: This can be set to a really high number (Current max is 32767), it just cannot be unspecified.

## Group: WA000-WWA064

**Group ID:** `V-13738`

### Rule: The HTTP request header field size must be limited.

**Rule ID:** `SV-33010r3_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Buffer overflow attacks are carried out by a malicious attacker sending amounts of data that the web server cannot store in a given size buffer. The eventual overflow of this buffer can overwrite system memory. Subsequently an attacker may be able to elevate privileges and take control of the server. This Apache directive limits the size of the various HTTP header sizes, thereby limiting the chances for a buffer overflow. The LimitRequestFieldSize directive allows the server administrator to reduce or increase the limit on the allowed size of an HTTP request header field. A server needs this value to be large enough to hold any one header field from a normal client request. The size of a normal request header field will vary greatly among different client implementations, often depending upon the extent to which a user has configured their browser to support detailed content negotiation. SPNEGO authentication headers can be up to 12392 bytes. This directive gives the server administrator greater control over abnormal client request behavior, which may be useful for avoiding some forms of denial-of-service attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directive: LimitRequestFieldSize If no LimitRequestFieldSize directives exist, this is a Finding. Although the default value is 8190, this directive must be explicitly set. For every LimitRequestFieldSize directive found, the value needs to be 8190. If any directive is set improperly, this is a finding. NOTE: This value may vary in size based on the application that is being supported by the web server. This vulnerability can be documented locally by the ISSM/ISSO if the site has operational reasons for an increased or decreased value. If the ISSM/ISSO has approved this change in writing, this should be marked as Not a Finding.

## Group: WA000-WWA066

**Group ID:** `V-13739`

### Rule: The HTTP request line must be limited.

**Rule ID:** `SV-33011r3_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Buffer overflow attacks are carried out by a malicious attacker sending amounts of data that the web server cannot store in a given size buffer. The eventual overflow of this buffer can overwrite system memory. Subsequently an attacker may be able to elevate privileges and take control of the server. This Apache directive limits the size of the various HTTP header sizes, thereby limiting the chances for a buffer overflow. The LimitRequestLine directive allows the server administrator to reduce or increase the limit on the allowed size of a client's HTTP request-line. Since the request-line consists of the HTTP method, URI, and protocol version, the LimitRequestLine directive places a restriction on the length of a request-URI allowed for a request on the server. A server needs this value to be large enough to hold any of its resource names, including any information that might be passed in the query part of a GET request. This directive gives the server administrator greater control over abnormal client request behavior, which may be useful for avoiding some forms of denial-of-service attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directive: LimitRequestLine Every enabled LimitRequestLine value needs to be 8190. If any directive is set improperly, this is a Finding. If no LimitRequestLine directives exist, this is a Finding. Although the default value is 8190, this directive must be explicitly set. NOTE: This value may vary in size based on the application that is being supported by the web server. This vulnerability can be documented locally by the ISSM/ISSO if the site has operational reasons for an increased or decreased value. If the ISSM/ISSO has approved this change in writing, this should be marked as Not a Finding.

## Group: WA00500

**Group ID:** `V-26285`

### Rule: Active software modules must be minimized.

**Rule ID:** `SV-33167r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Modules are the source of Apache httpd servers core and dynamic capabilities. Thus not every module available is needed for operation. Most installations only need a small subset of the modules available. By minimizing the enabled modules to only those that are required, we reduce the number of doors and have therefore reduced the attack surface of the web site. Likewise having fewer modules means less software that could have vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Open a command prompt window. Navigate to the “bin” directory (in many cases this may be [Drive Letter]:\[directory path]\Apache Software Foundation\Apache2.2\bin>). Enter the following command and press Enter: httpd –M This will provide a list of the loaded modules. Discuss with the web administrator why all displayed modules are required for operation. If any module is not required for operation, this is a finding. Note: The following modules do not need to be discussed: core_module, win32_module, mpm_winnt_module, http_module, so_module.

## Group: WA00505

**Group ID:** `V-26287`

### Rule: Web Distributed Authoring and Versioning (WebDAV) must be disabled.

**Rule ID:** `SV-33169r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Apache mod_dav and mod_dav_fs modules support WebDAV ('Web-based Distributed Authoring and Versioning') functionality for Apache. WebDAV is an extension to the HTTP protocol which allows clients to create, move, and delete files and resources on the web server. WebDAV is not widely used, and has serious security concerns as it may allow clients to modify unauthorized files on the web server. Therefore, the WebDav modules mod_dav and mod_dav_fs should be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Open a command prompt window. Navigate to the “bin” directory (in many cases this may be [Drive Letter]:\[directory path]\Apache Software Foundation\Apache2.2\bin>). Enter the following command: httpd –M <enter> NOTE: Some installations may be running under apache.exe. In such case, validate by running the following command: apache -M <enter> This will provide a list of all loaded modules. If any of the following modules are found this is a finding: dav_module, dav_fs_module, or dav_lock_module.

## Group: WA00510

**Group ID:** `V-26294`

### Rule: Web server status module must be disabled.

**Rule ID:** `SV-33171r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Apache mod_info module provides information on the server configuration via access to a /server-info URL location, while the mod_status module provides current server performance statistics. While having server configuration and status information available as a web page may be convenient, it is recommended that these modules not be enabled: Once mod_info is loaded into the server, its handler capability is available in per-directory .htaccess files and can leak sensitive information from the configuration directives of other Apache modules such as system paths, usernames/passwords, database names, etc. If mod_status is loaded into the server, its handler capability is available in all configuration files, including per-directory files (e.g., .htaccess) and may have security-related ramifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Open a command prompt window. Navigate to the “bin” directory (in many cases this may be [Drive Letter]:\[directory path]\Apache Software Foundation\Apache2.2\bin>). Enter the following command: httpd –M <enter> NOTE: Some installations may be running under apache.exe. In such case, validate by running the following command: apache -M <enter> This will provide a list of all loaded modules. If any of the following modules are found this is a finding: info_module & status_module.

## Group: WA00520

**Group ID:** `V-26299`

### Rule: The web server must not be configured as a proxy server.

**Rule ID:** `SV-33173r3_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Apache proxy modules allow the server to act as a proxy (either forward or reverse proxy) of http and other protocols with additional proxy modules loaded. If the Apache installation is not intended to proxy requests to or from another network then the proxy module should not be loaded. Proxy servers can act as an important security control when properly configured, however a secure proxy server is not within the scope of this STIG. A web server should be primarily a web server or a proxy server but not both, for the same reasons that other multi-use servers are not recommended. Scanning for web servers that will also proxy requests is a very common attack, as proxy servers are useful for anonymizing attacks on other servers, or possibly proxying requests into an otherwise protected network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the Apache web server is only performing in a proxy server role and does not host any websites nor support any applications, this check is Not Applicable. Open a command prompt window. Navigate to the “bin” directory (in many cases this may be [Drive Letter]:\[directory path]\Apache Software Foundation\Apache2.2\bin>). Enter the following command: httpd –M <enter> Note: Some installations may be running under apache.exe. In such case, validate by running the following command: apache -M <enter> This will provide a list of all loaded modules. If any of the following modules are found this is a finding: proxy_module, proxy_ajp_module, proxy_balancer_module, proxy_ftp_module, proxy_http_module, or proxy_connect_module.

## Group: WA00525

**Group ID:** `V-26302`

### Rule: User specific directories must not be globally enabled.

**Rule ID:** `SV-33175r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The UserDir directive must be disabled so that user home directories are not accessed via the web site with a tilde (~) preceding the username. The directive also sets the path name of the directory that will be accessed. The user directories should not be globally enabled since it allows anonymous access to anything users may want to share with other users on the network. Also consider that every time a new account is created on the system, there is potentially new content available via the web site.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Open a command prompt window. Navigate to the “bin” directory (in many cases this may be [Drive Letter]:\[directory path]\Apache Software Foundation\Apache2.2\bin>). Enter the following command: httpd –M <enter> NOTE: Some installations may be running under apache.exe. In such case, validate by running the following command: apache -M <enter> This will provide a list of all loaded modules. If the following module is found this is a finding: userdir_module.

## Group: WA00530

**Group ID:** `V-26305`

### Rule: The process ID (PID) file must be properly secured.

**Rule ID:** `SV-33177r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The PidFile directive sets the path to the process ID file to which the server records the process ID of the server, which is useful for sending a signal to the server process or for checking on the health of the process. If the PidFile is placed in a writable directory, other accounts could create a denial of service attack and prevent the server from starting by creating a PID file with the same name.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. Open the httpd.conf file with an editor such as Notepad, and search for the following directive: PidFile Note the location and name of the PID file If the PID file location is not specified in the conf file, use the \logs directory as the PID file location. Verify the permissions on the folder containing the PID file. If any user accounts other than administrator, auditor, or the account used to run the web server has permission to this file, this is a finding. If the PID file is located in the web server DocumentRoot this is a finding.

## Group: WA00535

**Group ID:** `V-26322`

### Rule: The ScoreBoard file must be properly secured.

**Rule ID:** `SV-33178r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ScoreBoardFile directive sets a file path which the server will use for Inter-Process Communication (IPC) among the Apache processes. If the directive is specified, then Apache will use the configured file for the inter-process communication. Therefore if it is specified it needs to be located in a secure directory. If the ScoreBoard file is placed in openly writable directory, other accounts could create a denial of service attack and prevent the server from starting by creating a file with the same name, and or users could monitor and disrupt the communication between the processes by reading and writing to the file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directive: ScoreBoardFile If the ScoreBoardFile directive is found uncommented note the directory specified in the directive statement that holds the Scoreboard file. If the ScoreBoardFile directive is not found enabled in the conf file use \logs as the directory containing the Scoreboard file. If any users other than administrator or the account used to run the web server has permission to the scoreboard file directory, this is a finding. If the ScoreBoard file is located in the web server document root this is finding.

## Group: WA00540

**Group ID:** `V-26323`

### Rule: The web server must be configured to explicitly deny access to the OS root.

**Rule ID:** `SV-33180r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Apache Directory directive allows for directory specific configuration of access controls and many other features and options. One important usage is to create a default deny policy that does not allow access to Operating System directories and files, except for those specifically allowed. This is done, with denying access to the OS root directory. One aspect of Apache, which is occasionally misunderstood, is the feature of default access. That is, unless you take steps to change it, if the server can find its way to a file through normal URL mapping rules, it can and will serve it to clients. Having a default deny is a predominate security principal, and then helps prevent the unintended access, and we do that in this case by denying access to the OS root directory. The Order directive is important as it provides for other Allow directives to override the default deny.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directive: Directory For every root directory entry (i.e. <Directory />) ensure the following exists after it: Order deny,allow Deny from all If the statement above is not found in the root directory statement, this is a finding. If Allow directives are included in the root directory statement, this is a finding. If the root directory statement isn't found at all, this is a finding.

## Group: WA00545

**Group ID:** `V-26324`

### Rule: Web server options for the OS root must be disabled.

**Rule ID:** `SV-33182r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Apache Options directive allows for specific configuration of options, including execution of CGI, following symbolic links, server side includes, and content negotiation. The Options directive for the root OS level is used to create a default minimal options policy that allows only the minimal options at the root directory level. Then for specific web sites or portions of the web site, options may be enabled as needed and appropriate. No options should be enabled and the value for the Options Directive should be None.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directive: Directory For every root directory entry (i.e. <Directory />) ensure the following entry exists after it: Options None If the statement above is not found in the root directory statement, this is a finding. If Allow directives are included in the root directory statement, this is a finding. If the root directory statement is not found at all, this is a finding.

## Group: WA00550

**Group ID:** `V-26325`

### Rule: The TRACE  method must be disabled.

**Rule ID:** `SV-33183r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> Use the Apache TraceEnable directive to disable the HTTP TRACE request method. Refer to the Apache documentation for more details http://httpd.apache.org/docs/2.2/mod/core.html#traceenable. The HTTP 1.1 protocol requires support for the TRACE request method which reflects the request back as a response and was intended for diagnostics purposes. The TRACE method is not needed and is easily subject to abuse and should be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. Open the httpd.conf file with an editor such as Notepad, and search for the following uncommented directive: TraceEnable For any enabled TraceEnable directives ensure they are part of the server level configuration (i.e. not nested in a <Directory> or <Location> directive). Also ensure that the TraceEnable directive is set to “Off”. If the TraceEnable directive is not part of the server level configuration and/or is not set to “off” this is a finding. If the directive does not exist in the conf file this is a finding as the default value is "On".

## Group: WA00555

**Group ID:** `V-26326`

### Rule: The web server must be configured to listen on a specific IP address and port.

**Rule ID:** `SV-33184r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Apache Listen directive specifies the IP addresses and port numbers the Apache web server will listen for requests. Rather than be unrestricted to listen on all IP addresses available to the system, the specific IP address or addresses intended must be explicitly specified. Specifically a Listen directive with no IP address specified, or with an IP address of zero’s should not be used. Having multiple interfaces on web servers is fairly common, and without explicit Listen directives, the web server is likely to be listening on an inappropriate IP address / interface that was not intended for the web server. Single homed system with a single IP addressed are also required to have an explicit IP address in the Listen directive, in case additional interfaces are added to the system at a later date.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directive: Listen For any enabled Listen directives ensure they specify both an IP address and port number. If the Listen directive is found with only an IP address, or only a port number specified, this is finding. If the IP address is all zeros (i.e. 0.0.0.0:80 or [::ffff:0.0.0.0]:80, this is a finding. If the Listen directive does not exist, this is a finding.

## Group: WA00560

**Group ID:** `V-26327`

### Rule: The URL-path name must be set to the file path name or the directory path name.

**Rule ID:** `SV-33185r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ScriptAlias directive controls which directories the Apache server "sees" as containing scripts. If the directive uses a URL-path name that is different than the actual file system path, the potential exists to expose the script source code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. Open the httpd.conf file with an editor such as Notepad, and search for the following uncommented directive: ScriptAlias If any enabled ScriptAlias directive does not have matching URL-path and file-path/directory-path entries, this is a finding. Example: Not a finding: ScriptAlias /cgi-bin/ “[Drive Letter]:/[directory path]/cgi-bin/ A finding: ScriptAlias /script-cgi-bin/ “[Drive Letter]:/[directory path]/cgi-bin/

## Group: WA00515

**Group ID:** `V-26368`

### Rule: Automatic directory indexing must be disabled.

**Rule ID:** `SV-33225r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To identify the type of web servers and versions software installed it is common for attackers to scan for icons or special content specific to the server type and version. A simple request like http://example.com/icons/apache_pb2.png may tell the attacker that the server is Apache 2.2 as shown below. The many icons are used primary for auto indexing, which is recommended to be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Open a command prompt window. Navigate to the “bin” directory (in many cases this may be [Drive Letter]:\[directory path]\Apache Software Foundation\Apache2.2\bin>). Enter the following command and press Enter: httpd –M This will provide a list of all loaded modules. If the following module is found this is a finding: autoindex_module.

## Group: WA00547

**Group ID:** `V-26393`

### Rule: The ability to override the access configuration for the OS root directory must be disabled.

**Rule ID:** `SV-33237r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Apache OverRide directive allows for .htaccess files to be used to override much of the configuration, including authentication, handling of document types, auto generated indexes, access control, and options. When the server finds an .htaccess file (as specified by AccessFileName) it needs to know which directives declared in that file can override earlier access information. When this directive is set to None, then .htaccess files are completely ignored. In this case, the server will not even attempt to read .htaccess files in the file system. When this directive is set to All, then any directive which has the .htaccess Context is allowed in .htaccess files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directive: Directory For every root directory entry (i.e. <Directory />) ensure the following entry exists after it: AllowOverride None If the statement above is not found in the root directory statement, this is a finding. If Allow directives are included in the root directory statement, this is a finding. If the root directory statement is not found at all, this is a finding.

## Group: WA00565 

**Group ID:** `V-26396`

### Rule: HTTP request methods must be limited.

**Rule ID:** `SV-33238r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The HTTP 1.1 protocol supports several request methods which are rarely used and potentially high risk. For example, methods such as PUT and DELETE are rarely used and should be disabled in keeping with the primary security principal of minimize features and options. Also since the usage of these methods is typically to modify resources on the web server, they should be explicitly disallowed. For normal web server operation, you will typically need to allow only the GET, HEAD and POST request methods. This will allow for downloading of web pages and submitting information to web forms. The OPTIONS request method will also be allowed as it is used to request which HTTP request methods are allowed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Note: If HTTP commands (GET, PUT, POST, DELETE) are not being used and the server is solely configured as a proxy server, this is Not Applicable. Locate the Apache httpd.conf file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directive: Directory For every enabled Directory directive (except root), ensure the following entry exists: Order allow,deny <LimitExcept GET POST OPTIONS> Deny from all </LimitExcept> If the statement above is found in the root directory statement (i.e. <Directory />), this is a finding. If the statement above is found enabled but without the appropriate LimitExcept or Order statement, this is a finding. If the statement is not found at all inside an enabled Directory directive, this is a finding. Note: If the LimitExcept statement above is operationally limiting. This should be explicitly documented with the Web Manager, at which point this can be considered not a finding.

## Group: WG345

**Group ID:** `V-60709`

### Rule: The web server must remove all export ciphers from the cipher suite.

**Rule ID:** `SV-75161r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>During the initial setup of a Transport Layer Security (TLS) connection to the web server, the client sends a list of supported cipher suites in order of preference. The web server will reply with the cipher suite it will use for communication from the client list. If an attacker can intercept the submission of cipher suites to the web server and place, as the preferred cipher suite, a weak export suite, the encryption used for the session becomes easy for the attacker to break, often within minutes to hours.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf and ssl.conf file if available. Open the httpd.conf and ssl.conf file with an editor and search for the following uncommented directive: SSLCipherSuite For all enabled SSLCipherSuite directives, ensure the cipher specification string contains the kill cipher from list option for all export cipher suites, i.e., !EXPORT, which may be abbreviated !EXP. If the SSLCipherSuite directive does not contain !EXPORT or there are no enabled SSLCipherSuite directives, this is a finding.

