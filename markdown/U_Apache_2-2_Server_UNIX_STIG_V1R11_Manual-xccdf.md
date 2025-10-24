# STIG Benchmark: APACHE 2.2 Server for UNIX Security Technical Implementation Guide

---

**Version:** 1

**Description:**
All directives specified in this STIG must be specifically set (i.e. the server is not allowed to revert to programmed defaults for these directives). Included files should be reviewed if they are used. Procedures for reviewing included files are included in the overview document. The use of .htaccess files are not authorized for use according to the STIG. However, if they are used, there are procedures for reviewing them in the overview document. The Web Policy STIG should be used in addition to the Apache Site and Server STIGs in order to do a comprehensive web server review.

## Group: WG370

**Group ID:** `V-2225`

### Rule: MIME types for csh or sh shell programs must be disabled.

**Rule ID:** `SV-36309r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Users must not be allowed to access the shell programs. Shell programs might execute shell escapes and could then perform unauthorized activities that could damage the security posture of the web server. A shell is a program that serves as the basic interface between the user and the operating system. In this regard, there are shells that are security risks in the context of a web server and shells that are unauthorized in the context of the Security Features User's Guide.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Enter the following commands: grep "Action" /usr/local/apache2/conf/httpd.conf grep "AddHandler" /usr/local/apache2/conf/httpd.conf If either of these exist and they configure /bin/csh, or any other shell as a viewer for documents, this is a finding.

## Group: WG420

**Group ID:** `V-2230`

### Rule: Backup interactive scripts on the production web server are prohibited.

**Rule ID:** `SV-6930r2_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Copies of backup files will not execute on the server, but they can be read by the anonymous user if special precautions are not taken. Such backup copies contain the same sensitive information as the actual script being executed and, as such, are useful to malicious users. Techniques and systems exist today that search web servers for such files and are able to exploit the information contained in them. Backup copies of files are automatically created by some text editors such as emacs and edit plus. The emacs editor will write a backup file with an extension ~ added to the name of the original file. The edit plus editor will create a .bak file. Of course, this would imply the presence and use of development tools on the web server, which is a finding under WG130. Having backup scripts on the web server provides one more opportunity for malicious persons to view these scripts and use the information found in them. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
This check is limited to CGI/interactive content and not static HTML. Search for backup copies of CGI scripts on the web server or ask the SA or the Web Administrator if they keep backup copies of CGI scripts on the web server. Common backup file extensions are: *.bak, *.old, *.temp, *.tmp, *.backup, *.??0. This would also apply to .jsp files. UNIX: find / -name “*.bak” –print find / -name “*.*~” –print find / -name “*.old” –print If files with these extensions are found in either the document directory or the home directory of the web server, this is a finding. If files with these extensions are stored in a repository (not in the document root) as backups for the web server, this is a finding. If files with these extensions have no relationship with web activity, such as a backup batch file for operating system utility, and they are not accessible by the web application, this is not a finding.

## Group: WG050

**Group ID:** `V-2232`

### Rule: The web server password(s) must be entrusted to the SA or Web Manager. 

**Rule ID:** `SV-32788r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Normally, a service account is established for the web server. This is because a privileged account is not desirable and the server is designed to run for long uninterrupted periods of time. The SA or Web Manager will need password access to the web server to restart the service in the event of an emergency as the web server is not to restart automatically after an unscheduled interruption. If the password is not entrusted to an SA or web manager the ability to ensure the availability of the web server is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
The reviewer should make a note of the name of the account being used for the web service. This information may be needed later in the SRR. There may also be other server services running related to the web server in support of a particular web application, these passwords must be entrusted to the SA or Web Manager as well. Query the SA or Web Manager to determine if they have the web service password(s). If the web services password(s) are not entrusted to the SA or Web Manager, this is a finding. NOTE: For installations that run as a service, or without a password, the SA or Web Manager having an Admin account on the system would meet the intent of this check.

## Group: WG040

**Group ID:** `V-2234`

### Rule: Public web server resources must not be shared with private assets.

**Rule ID:** `SV-32957r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is important to segregate public web server resources from private resources located behind the DoD DMZ in order to protect private assets. When folders, drives or other resources are directly shared between the public web server and private servers the intent of data and resource segregation can be compromised. In addition to the requirements of the DoD Internet-NIPRNet DMZ STIG that isolates inbound traffic from the external network to the internal network, resources such as printers, files, and folders/directories will not be shared between public web servers and assets located within the internal network. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine whether the public web server has a two-way trusted relationship with any private asset located within the network. Private web server resources (e.g., drives, folders, printers, etc.) will not be directly mapped to or shared with public web servers. If sharing is selected for any web folder, this is a finding. The following checks indicate inappropriate sharing of private resources with the public web server: If private resources (e.g., drives, partitions, folders/directories, printers, etc.) are shared with the public web server, then this is a finding.

## Group: WG080

**Group ID:** `V-2236`

### Rule: Installation of a compiler on production web server is prohibited.

**Rule ID:** `SV-32956r3_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The presence of a compiler on a production server facilitates the malicious user’s task of creating custom versions of programs and installing Trojan Horses or viruses. For example, the attacker’s code can be uploaded and compiled on the server under attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Query the SA and the Web Manager to determine if a compiler is present on the server. If a compiler is present, this is a finding. NOTE: If the web server is part of an application suite and a compiler is needed for installation, patching, and upgrading of the suite or if the compiler is embedded and can't be removed without breaking the suite, document the installation of the compiler with the ISSO/ISSM and verify that the compiler is restricted to administrative users only. If documented and restricted to administrative users, this is not a finding.

## Group: WA060

**Group ID:** `V-2242`

### Rule: A public web server, if hosted on the NIPRNet, must be isolated in an accredited DoD DMZ Extension.

**Rule ID:** `SV-32932r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To minimize exposure of private assets to unnecessary risk by attackers, public web servers must be isolated from internal systems. Public web servers are by nature more vulnerable to attack from publically based sources, such as the public Internet. Once compromised, a public web server might be used as a base for further attack on private resources, unless additional layers of protection are implemented. Public web servers must be located in a DoD DMZ Extension, if hosted on the NIPRNet, with carefully controlled access. Failure to isolate resources in this way increase risk that private assets are exposed to attacks from public sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Officer</Responsibility><IAControls></IAControls>

**Check Text:**
Interview the SA or web administrator to see where the public web server is logically located in the data center. Review the site’s network diagram to see how the web server is connected to the LAN. Visually check the web server hardware connections to see if it conforms to the site’s network diagram. An improperly located public web server is a potential threat to the entire network. If the web server is not isolated in an accredited DoD DMZ Extension, this is a finding.

## Group: WA070

**Group ID:** `V-2243`

### Rule: A private web server must be located on a separate controlled access subnet.

**Rule ID:** `SV-32935r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Private web servers, which host sites that serve controlled access data, must be protected from outside threats in addition to insider threats. Insider threat may be accidental or intentional but, in either case, can cause a disruption in service of the web server. To protect the private web server from these threats, it must be located on a separate controlled access subnet and must not be a part of the public DMZ that houses the public web servers. It also cannot be located inside the enclave as part of the local general population LAN.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Officer</Responsibility><IAControls></IAControls>

**Check Text:**
Verify the site’s network diagram and visually check the web server, to ensure that the private web server is located on a separate controlled access subnet and is not a part of the public DMZ that houses the public web servers. In addition, the private web server needs to be isolated via a controlled access mechanism from the local general population LAN.

## Group: WG190

**Group ID:** `V-2246`

### Rule: Web server software must be a vendor-supported version.

**Rule ID:** `SV-36441r2_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Many vulnerabilities are associated with older versions of web server software. As hot fixes and patches are issued, these solutions are included in the next version of the server software. Maintaining the web server at a current version makes the efforts of a malicious user to exploit the web service more difficult.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
To determine the version of the Apache software that is running on the system. Use the command: httpd –v httpd2 –v If the version of Apache is not at the following version or higher, this is a finding. Apache httpd server version 2.2 - Release 2.2.31 (July 2015) Note: In some situations, the Apache software that is being used is supported by another vendor, such as Oracle in the case of the Oracle Application Server or IBMs HTTP Server. The versions of the software in these cases may not match the above mentioned version numbers. If the site can provide vendor documentation showing the version of the web server is supported, this would not be a finding.

## Group: WG200

**Group ID:** `V-2247`

### Rule: Administrators must be the only users allowed access to the directory tree, the shell, or other operating system functions and utilities.

**Rule ID:** `SV-36456r2_rule`
**Severity:** high

**Description:**
<VulnDiscussion>As a rule, accounts on a web server are to be kept to a minimum. Only administrators, web managers, developers, auditors, and web authors require accounts on the machine hosting the web server. This is in addition to the anonymous web user account. The resources to which these accounts have access must also be closely monitored and controlled. Only the SA needs access to all the system’s capabilities, while the web administrator and associated staff require access and control of the web content and web server configuration files. The anonymous web user account must not have access to system resources as that account could then control the server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Obtain a list of the user accounts for the system, noting the priviledges for each account. Verify with the system administrator or the ISSO that all privileged accounts are mission essential and documented. Verify with the system administrator or the ISSO that all non-administrator access to shell scripts and operating system functions are mission essential and documented. If undocumented privileged accounts are found, this is a finding. If undocumented access to shell scripts or operating system functions is found, this is a finding.

## Group: WG220

**Group ID:** `V-2248`

### Rule: Web administration tools must be restricted to the web manager and the web manager’s designees.

**Rule ID:** `SV-32948r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All automated information systems are at risk of data loss due to disaster or compromise. Failure to provide adequate protection to the administration tools creates risk of potential theft or damage that may ultimately compromise the mission. Adequate protection ensures that server administration operates with less risk of losses or operations outages. The key web service administrative and configuration tools must be accessible only by the authorized web server administrators. All users granted this authority must be documented and approved by the ISSO. Access to the IIS Manager will be limited to authorized users and administrators. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine which tool or control file is used to control the configuration of the web server. If the control of the web server is done via control files, verify who has update access to them. If tools are being used to configure the web server, determine who has access to execute the tools. If accounts other than the SA, the web manager, or the web manager designees have access to the web administration tool or control files, this is a finding.

## Group: WG130

**Group ID:** `V-2251`

### Rule: All utility programs, not necessary for operations, must be removed or disabled. 

**Rule ID:** `SV-32955r2_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Just as running unneeded services and protocols is a danger to the web server at the lower levels of the OSI model, running unneeded utilities and programs is also a danger at the application layer of the OSI model. Office suites, development tools, and graphical editors are examples of such programs that are troublesome. Individual productivity tools have no legitimate place or use on an enterprise, production web server and they are also prone to their own security risks. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If the site requires the use of a particular piece of software, the ISSO will need to maintain documentation identifying this software as necessary for operations. The software must be operated at the vendor’s current patch level and must be a supported vendor release. If programs or utilities that meet the above criteria are installed on the Web Server, and appropriate documentation and signatures are in evidence, this is not a finding. Determine whether the web server is configured with unnecessary software. Determine whether processes other than those that support the web server are loaded and/or run on the web server. Examples of software that should not be on the web server are all web development tools, office suites (unless the web server is a private web development server), compilers, and other utilities that are not part of the web server suite or the basic operating system. Check the directory structure of the server and ensure that additional, unintended, or unneeded applications are not loaded on the system. If, after review of the application on the system, there is no justification for the identified software, this is a finding.

## Group: WG270

**Group ID:** `V-2255`

### Rule: The web server’s htpasswd files (if present) must reflect proper ownership and permissions

**Rule ID:** `SV-36478r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In addition to OS restrictions, access rights to files and directories can be set on a web site using the web server software. That is, in addition to allowing or denying all access rights, a rule can be specified that allows or denies partial access rights. For example, users can be given read-only access rights to files, to view the information but not change the files. This check verifies that the htpasswd file is only accessible by system administrators or web managers, with the account running the web service having group permissions of read and execute. htpasswd is a utility used by Netscape and Apache to provide for password access to designated web sites. I</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
To locate the htpasswd file enter the following command: Find / -name htpasswd Permissions should be r-x r - x - - - (550) If permissions on htpasswd are greater than 550, this is a finding. Owner should be the SA or Web Manager account, if another account has access to this file, this is a finding.

## Group: WG280

**Group ID:** `V-2256`

### Rule: The access control files are owned by a privileged web server account.

**Rule ID:** `SV-6880r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This check verifies that the key web server system configuration files are owned by the SA or Web Manager controlled account. These same files which control the configuration of the web server, and thus its behavior, must also be accessible by the account which runs the web service. If these files are altered by a malicious user, the web server would no longer be under the control of its managers and owners; properties in the web server configuration could be altered to compromise the entire server platform. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
This check verifies that the SA or Web Manager controlled account owns the key web server files. These same files, which control the configuration of the web server, and thus its behavior, must also be accessible by the account that runs the web service process. If it exists, the following file need to be owned by a privileged account. .htaccess httpd.conf Use the command find / -name httpd.conf to find the file Change to the Directory that contains the httpd.conf file Use the command ls -l httpd.conf to determine ownership of the file -The Web Manager or the SA should own all the system files and directories. -The configurable directories can be owned by the WebManager or equivalent user. Permissions on these files should be 660 or more restrictive. If root or an authorized user does not own the web system files and the permission are not correct, this is a finding.

## Group: WA120

**Group ID:** `V-2257`

### Rule: Administrative users and groups that have access rights to the web server must be documented.

**Rule ID:** `SV-32951r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>There are typically several individuals and groups that are involved in running a production web server. These accounts must be restricted to only those necessary to maintain web services, review the server’s operation, and the operating system. By minimizing the amount of user and group accounts on a web server the total attack surface of the server is minimized. Additionally, if the required accounts aren’t documented no known standard is created. Without a known standard the ability to identify required accounts is diminished, increasing the opportunity for error when such a standard is needed (i.e. COOP, IR, etc.).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Manager</Responsibility><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Proposed Questions: How many user accounts are associated with the Web server operation and maintenance? Where are these accounts documented? Use the command line utility more /etc/passwd to identify the accounts on the web server. Query the SA or Web Manager regarding the use of each account and each group. If the documentation does not match the users and groups found on the server, this is a finding.

## Group: WG300

**Group ID:** `V-2259`

### Rule: Web server system files must conform to minimum file permission requirements.

**Rule ID:** `SV-32938r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This check verifies that the key web server system configuration files are owned by the SA or the web administrator controlled account. These same files that control the configuration of the web server, and thus its behavior, must also be accessible by the account that runs the web service. If these files are altered by a malicious user, the web server would no longer be under the control of its managers and owners; properties in the web server configuration could be altered to compromise the entire server platform.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Apache directory and file permissions and ownership should be set per the following table.. The installation directories may vary from one installation to the next. If used, the WebAmins group should contain only accounts of persons authorized to manage the web server configuration, otherwise the root group should own all Apache files and directories. Note: This check also applies to any other directory where CGI scripts are located. There may be additional directories based the local implementation, and permissions should apply to directories of similar content. Ex. all web content directories should follow the permissions for /htdocs. If the files and directories are not set to the following permissions or more restrictive, this is a finding. To locate the ServerRoot directory enter the following command. grep ^ ServerRoot /usr/local/apache2/conf/httpd.conf /Server root dir apache root WebAdmin 771/660 /apache/cgi-bin root WebAdmin 775/775 /apache/bin root WebAdmin 550/550 /apache/config root WebAdmin 770/660 /apache/htdocs root WebAdmin 775/664 /apache/logs root WebAdmin 750/640 NOTE: The permissions are noted as directories / files.

## Group: WG330

**Group ID:** `V-2261`

### Rule: A public web server must limit email to outbound only.

**Rule ID:** `SV-32937r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Incoming E-mail has been known to provide hackers with access to servers. Disabling the incoming mail service prevents this type of attacks. Additionally, Email represents the main use of the Internet. It is specialized application that requires the dedication of server resources. To combine this type of transaction processing function with the file serving role of the web server creates an inherent conflict. Supporting mail services on a web server opens the server to the risk of abuse as an email relay. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
"To determine if email applications are excepting incoming connections (on standard ports)enter the following command: telnet localhost 25 review the command results, If an e-mail program is installed and that program has been configured to accept inbound email, this is a finding."

## Group: WG440

**Group ID:** `V-2271`

### Rule: Monitoring software must include CGI or equivalent programs in its scope.

**Rule ID:** `SV-32927r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By their very nature, CGI type files permit the anonymous web user to interact with data and perhaps store data on the web server. In many cases, CGI scripts exercise system-level control over the server’s resources. These files make appealing targets for the malicious user. If these files can be modified or exploited, the web server can be compromised. These files must be monitored by a security tool that reports unauthorized changes to these files. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
CGI or equivalent files must be monitored by a security tool that reports unauthorized changes. It is the purpose of such software to monitor key files for unauthorized changes to them. The reviewer should query the ISSO, the SA, and the web administrator and verify the information provided by asking to see the template file or configuration file of the software being used to accomplish this security task. Example file extensions for files considered to provide active content are, but not limited to, .cgi, .asp, .aspx, .class, .vb, .php, .pl, and .c. If the site does not have a process in place to monitor changes to CGI program files, this is a finding.

## Group: WA140

**Group ID:** `V-6485`

### Rule: Web server content and configuration files must be part of a routine backup program.

**Rule ID:** `SV-32964r2_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Backing up web server data and web server application software after upgrades or maintenance ensures that recovery can be accomplished up to the current version. It also provides a means to determine and recover from subsequent unauthorized changes to the software and data. A tested and verifiable backup strategy will be implemented for web server software as well as all web server data files. Backup and recovery procedures will be documented and the Web Manager or SA for the specific application will be responsible for the design, test, and implementation of the procedures. The site will have a contingency processing plan/disaster recovery plan that includes web servers. The contingency plan will be periodically tested in accordance with DoDI 8500.2 requirements. The site will identify an off-site storage facility in accordance with DoDI 8500.2 requirements. Off-site backups will be updated on a regular basis and the frequency will be documented in the contingency plan. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Interview the Information Systems Security Officer (ISSO), SA, Web Manager, Webmaster or developers as necessary to determine whether or not a tested and verifiable backup strategy has been implemented for web server software as well as all web server data files. Proposed Questions: Who maintains the backup and recovery procedures? Do you have a copy of the backup and recovery procedures? Where is the off-site backup location? Is the contingency plan documented? When was the last time the contingency plan was tested? Are the test dates and results documented? If there is not a backup and recovery process for the web server, this is a finding.

## Group: WG204

**Group ID:** `V-6577`

### Rule: A web server must be segregated from other services.

**Rule ID:** `SV-32950r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The web server installation and configuration plan should not support the co-hosting of multiple services such as Domain Name Service (DNS), e-mail, databases, search engines, indexing, or streaming media on the same server that is providing the web publishing service. By separating these services additional defensive layers are established between the web service and the applicable application should either be compromised. Disallowed or restricted services in the context of this vulnerability applies to services that are not directly associated with the delivery of web content. An operating system that supports a web server will not provide other services (e.g., domain controller, e-mail server, database server, etc.). Only those services necessary to support the web server and its hosted sites are specifically allowed and may include, but are not limited to, operating system, logging, anti-virus, host intrusion detection, administrative maintenance, or network requirements. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Request a copy of and review the web server’s installation and configuration plan. Ensure that the server is in compliance with this plan. If the server is not in compliance with the plan, this is a finding. Query the SA to ascertain if and where the additional services are installed. Confirm that the additional service or application is not installed on the same partition as the operating systems root directory or the web document root. If it is, this is a finding.

## Group: WG520

**Group ID:** `V-6724`

### Rule: Web server and/or operating system information must be protected.



**Rule ID:** `SV-36672r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The web server response header of an HTTP response can contain several fields of information including the requested HTML page. The information included in this response can be web server type and version, operating system and version, and ports associated with the web server. This provides the malicious user valuable information without the use of extensive tools.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Enter the following command: grep "ServerTokens" /usr/local/apache2/conf/httpd.conf The directive ServerTokens must be set to “Prod” (ex. ServerTokens Prod). This directive controls whether Server response header field that is sent back to clients that includes a description of the OS-type of the server as well as information about compiled-in modules. If the web server or operating system information are sent to the client via the server response header or the directive does not exist, this is a finding. Note: The default value is set to Full.

## Group: WA230

**Group ID:** `V-13613`

### Rule: The Web site software used with the web server must have all applicable security patches applied and documented.

**Rule ID:** `SV-32969r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The IAVM process does not address all patches that have been identified for the host operating system or, in this case, the web server software environment. Many vendors have subscription services available to notify users of known security threats. The site needs to be aware of these fixes and make determinations based on local policy and what software features are installed, if these patches need to be applied. In some cases, patches also apply to middleware and database systems. Maintaining the security of web servers requires frequent reviews of security notices. Many security notices mandate the installation of a software patch to overcome security vulnerabilities. SAs and ISSOs should regularly check the vendor support web site for patches and information related to the web server software. All applicable security patches will be applied to the operating system and to the web server software. Security patches are deemed applicable if the product is installed, even if it is not used or is disabled. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><IAControls></IAControls>

**Check Text:**
Query the web administrator to determine if the site has a detailed process as part of its configuration management plan to stay compliant with all security-related patches. Proposed Questions: How does the SA stay current with web server vendor patches? How is the SA notified when a new security patch is issued by the vendor? (Exclude the IAVM.) What is the process followed for applying patches to the web server? If the site is not in compliance with all applicable security patches, this is a finding.

## Group: WG355

**Group ID:** `V-13620`

### Rule: A private web server’s list of CAs in a trust hierarchy must lead to an authorized  DoD PKI Root CA.

**Rule ID:** `SV-32936r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A PKI certificate is a digital identifier that establishes the identity of an individual or a platform. A server that has a certificate provides users with third-party confirmation of authenticity. Most web browsers perform server authentication automatically and the user is notified only if the authentication fails. The authentication process between the server and the client is performed using the SSL/TLS protocol. Digital certificates are authenticated, issued, and managed by a trusted Certificate Authority (CA). The use of a trusted certificate validation hierarchy is crucial to the ability to control access to a site’s server and to prevent unauthorized access. Only DoD-approved PKIs will be utilized. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Enter the following command: find / -name ssl.conf note the path of the file. grep "SSLCACertificateFile" /path/of/ssl.conf Review the results to determine the path of the SSLCACertificateFile. more /path/of/ca-bundle.crt Examine the contents of this file to determine if the trusted CAs are DoD approved. If the trusted CA that is used to authenticate users to the web site does not lead to an approved DoD CA, this is a finding. NOTE: There are non DoD roots that must be on the server in order for it to function. Some applications, such as anti-virus programs, require root CAs to function. DoD approved certificate can include the External Certificate Authorities (ECA), if approved by the DAA. The PKE InstallRoot 3.06 System Administrator Guide (SAG), dated 8 Jul 2008, contains a complete list of DoD, ECA, and IECA CAs.

## Group: WG385

**Group ID:** `V-13621`

### Rule: All web server documentation, sample code, example applications, and tutorials must be removed from a production web server.

**Rule ID:** `SV-32933r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Web server documentation, sample code, example applications, and tutorials may be an exploitable threat to a web server. A production web server may only contain components that are operationally necessary (e.g., compiled code, scripts, web-content, etc.). Delete all directories that contain samples and any scripts used to execute the samples. If there is a requirement to maintain these directories at the site on non-production servers for training purposes, have NTFS permissions set to only allow access to authorized users (i.e., web administrators and systems administrators). Sample applications or scripts have not been evaluated and approved for use and may introduce vulnerabilities to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance>Any sample application or sample executable script found on the production web server will be a CAT I finding. Any web server documentation or sample file found on the production web server and accessible to web users or non-administrators will be a CAT III finding. Any web server documentation or sample file found on the production web server and accessible only to SAs or to web administrators is permissible and not a finding. </SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Query the SA to determine if all directories that contain samples and any scripts used to execute the samples have been removed from the server. Each web server has its own list of sample files. This may change with the software versions, but the following are some examples of what to look for (This should not be the definitive list of sample files, but only an example of the common samples that are provided with the associated web server. This list will be updated as additional information is discovered.): ls -Ll /usr/local/apache2/manual. If there is a requirement to maintain these directories at the site for training or other such purposes, have permissions or set the permissions to only allow access to authorized users. If any sample files are found on the web server, this is a finding.

## Group: WG145

**Group ID:** `V-13672`

### Rule: The private web server must use an approved DoD certificate validation process.

**Rule ID:** `SV-32954r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of a certificate validation process, the site is vulnerable to accepting certificates that have expired or have been revoked. This would allow unauthorized individuals access to the web server. This also defeats the purpose of the multi-factor authentication provided by the PKI process. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
The reviewer should query the ISSO, the SA, the web administrator, or developers as necessary to determine if the web server is configured to utilize an approved DoD certificate validation process. The web administrator should be questioned to determine if a validation process is being utilized on the web server. To validate this, the reviewer can ask the web administrator to describe the validation process being used. They should be able to identify either the use of certificate revocation lists (CRLs) or Online Certificate Status Protocol (OCSP). If the production web server is accessible, the SA or the web administrator should be able to demonstrate the validation of good certificates and the rejection of bad certificates. If CRLs are being used, the SA should be able to identify how often the CRL is updated and the location from which the CRL is downloaded. If the web administrator cannot identify the type of validation process being used, this is a finding.

## Group: WA000-WWA020

**Group ID:** `V-13724`

### Rule: The Timeout directive must be properly set.

**Rule ID:** `SV-32977r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Timeout requirements are set to mitigate the effects of several types of denial of service attacks. Although there is some latitude concerning the settings themselves, the requirements attempt to provide reasonable limits for the protection of the web server. If necessary, these limits can be adjusted to accommodate the operational requirement of a given system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
To view the Timeout value enter the following command: grep "Timeout" /usr/local/apache2/conf/httpd.conf. Verify the value is 300 or less if not, this is a finding. Note:If the directive does not exist, this is not a finding because it will default to 300. It is recommended that the directive be explicitly set to prevent unexpected results should the defaults for any reason be changed (i.e. software update).

## Group: WA000-WWA022

**Group ID:** `V-13725`

### Rule: The KeepAlive directive must be enabled.

**Rule ID:** `SV-32844r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The KeepAlive extension to HTTP/1.0 and the persistent connection feature of HTTP/1.1 provide long lived HTTP sessions which allow multiple requests to be sent over the same connection. These requirements are set to mitigate the effects of several types of denial of service attacks. Although there is some latitude concerning the settings themselves, the requirements attempt to provide reasonable limits for the protection of the web server. If necessary, these limits can be adjusted to accommodate the operational requirement of a given system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
To view the KeepAlive value enter the following command: grep "KeepAlive" /usr/local/apache2/conf/httpd.conf. Verify the Value of KeepAlive is set to “On” If not, this is a finding. NOTE: This vulnerability can be documented locally with the ISSM/ISSO if the site has operational reasons for not using persistent connections. If the site has this documentation, this should be marked as Not a Finding.

## Group: WA000-WWA024

**Group ID:** `V-13726`

### Rule: The KeepAliveTimeout directive must be defined.

**Rule ID:** `SV-32877r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The number of seconds Apache will wait for a subsequent request before closing the connection. Once a request has been received, the timeout value specified by the Timeout directive applies. Setting KeepAliveTimeout to a high value may cause performance problems in heavily loaded servers. The higher the timeout, the more server processes will be kept occupied waiting on connections with idle clients. These requirements are set to mitigate the effects of several types of denial of service attacks. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
To view the KeepAliveTimeout value enter the following command: grep "KeepAliveTimeout" /usr/local/apache2/conf/httpd.conf. If the value of "KeepAliveTimeout" is not set to 15 or less, this is a finding. Note: If the directive does not exist, this is not a finding because it will default to 5. It is recommended that the directive be explicitly set to prevent unexpected results should the defaults for any reason change(i.e. software update).

## Group: WA000-WWA026

**Group ID:** `V-13727`

### Rule: The httpd.conf StartServers directive must be set properly.

**Rule ID:** `SV-36645r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>These requirements are set to mitigate the effects of several types of denial of service attacks. Although there is some latitude concerning the settings themselves, the requirements attempt to provide reasonable limits for the protection of the web server. If necessary, these limits can be adjusted to accommodate the operational requirement of a given system. From Apache.org: The StartServers directive sets the number of child server processes created on startup. As the number of processes is dynamically controlled depending on the load, there is usually little reason to adjust this parameter. The default value differs from MPM to MPM. For worker the default is StartServers 3. For prefork defaults to 5 and for mpmt_os2 to 2.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. If you cannot locate the file, you can do a search of the drive to find the location of the file. Open the httpd.conf file with an editor and search for the following directive: StartServers The value needs to be between 5 and 10 If the directive is set improperly, this is a finding. If the directive does not exist, this is NOT a finding because it will default to 5. It is recommended that the directive be explicitly set to prevent unexpected results if the defaults change with updated software. NOTE: This vulnerability can be documented locally with the ISSM/ISSO if the site has operational reasons for the use of increased or decreased value. If the site has this documentation, this should be marked as Not a Finding.

## Group: WA000-WWA028

**Group ID:** `V-13728`

### Rule: The httpd.conf MinSpareServers directive must be set properly. 

**Rule ID:** `SV-36646r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>These requirements are set to mitigate the effects of several types of denial of service attacks. Although there is some latitude concerning the settings themselves, the requirements attempt to provide reasonable limits for the protection of the web server. If necessary, these limits can be adjusted to accommodate the operational requirement of a given system. From Apache.org: The MinSpareServers directive sets the desired minimum number of idle child server processes. An idle process is one which is not handling a request. If there are fewer than MinSpareServers idle, then the parent process creates new children at a maximum rate of 1 per second. Tuning of this parameter should only be necessary on very busy sites. Setting this parameter to a large number is almost always a bad idea.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Open the httpd.conf file with an editor and search for the following directive: MinSpareServers The value needs to be between 5 and 10 If the directive is set improperly, this is a finding. If the directive is not found, you will need to review the httpd.conf file to see if there are other .conf files that are included of "linked" to the httpd.conf. The other conf files may contain these directives. If the directive does not exist, this is NOT a finding because it will default to 5. It is recommended that the directive be explicitly set to prevent unexpected results if the defaults change with updated software. NOTE: This vulnerability can be documented locally with the ISSM/ISSO if the site has operational reasons for the use of increased or decreased value. If the site has this documentation, this should be marked as Not a Finding.

## Group: WA000-WWA030

**Group ID:** `V-13729`

### Rule: The httpd.conf MaxSpareServers directive must be set properly. 

**Rule ID:** `SV-36648r2_rule`
**Severity:** low

**Description:**
<VulnDiscussion>These requirements are set to mitigate the effects of several types of denial of service attacks. Although there is some latitude concerning the settings themselves, the requirements attempt to provide reasonable limits for the protection of the web server. If necessary, these limits can be adjusted to accommodate the operational requirement of a given system. From Apache.org:The MaxSpareServers directive sets the desired maximum number of idle child server processes. An idle process is one which is not handling a request. If there are more than MaxSpareServers idle, then the parent process will kill off the excess processes. Tuning of this parameter should only be necessary on very busy sites. Setting this parameter to a large number is almost always a bad idea. If you are trying to set the value equal to or lower than MinSpareServers, Apache will automatically adjust it to MinSpareServers + 1.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Open the httpd.conf file with an editor and search for the following directive: MaxSpareServers The value needs to be 10 or less If the directive is set improperly, this is a finding. If the directive is not found, you will need to review the httpd.conf file to see if there are other .conf files that are included of "linked" to the httpd.conf. The other conf files may contain these directives. If the directive does not exist, this is NOT a finding because it will default to 10. It is recommended that the directive be explicitly set to prevent unexpected results if the defaults change with updated software. NOTE: This vulnerability can be documented locally with the ISSM/ISSO if the site has operational reasons for the use of increased value. If the site has this documentation, this should be marked as Not a Finding.

## Group: WA000-WWA032

**Group ID:** `V-13730`

### Rule: The httpd.conf MaxClients directive must be set properly.

**Rule ID:** `SV-36649r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>These requirements are set to mitigate the effects of several types of denial of service attacks. Although there is some latitude concerning the settings themselves, the requirements attempt to provide reasonable limits for the protection of the web server. If necessary, these limits can be adjusted to accommodate the operational requirement of a given system. From Apache.org: The MaxClients directive sets the limit on the number of simultaneous requests that will be served. Any connection attempts over the MaxClients limit will normally be queued, up to a number based on the ListenBacklog directive. Once a child process is freed at the end of a different request, the connection will then be serviced. For non-threaded servers (i.e., prefork), MaxClients translates into the maximum number of child processes that will be launched to serve requests. The default value is 256; to increase it, you must also raise ServerLimit. For threaded and hybrid servers (e.g. beos or worker) MaxClients restricts the total number of threads that will be available to serve clients. The default value for beos is 50. For hybrid MPMs the default value is 16 (ServerLimit) multiplied by the value of 25 (ThreadsPerChild). Therefore, to increase MaxClients to a value that requires more than 16 processes, you must also raise ServerLimit.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Open the httpd.conf file with an editor and search for the following directive: MaxClients The value needs to be 256 or less If the directive is set improperly, this is a finding. If the directive does not exist, this is NOT a finding because it will default to 256. It is recommended that the directive be explicitly set to prevent unexpected results if the defaults change with updated software. NOTE: This vulnerability can be documented locally with the ISSM/ISSO if the site has operational reasons for the use of increased value. If the site has this documentation, this should be marked as Not a Finding.

## Group: WA000-WWA050

**Group ID:** `V-13731`

### Rule: All interactive programs must be placed in a designated directory with appropriate permissions.

**Rule ID:** `SV-32763r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Directory options directives are directives that can be applied to further restrict access to file and directories. The Options directive controls which server features are available in a particular directory. The ExecCGI option controls the execution of CGI scripts using mod_cgi. This needs to be restricted to only the directory intended for script execution.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Search for the unnecessary CGI programs which may be found in the directories configured with ScriptAlias, Script or other Script* directives. Often, CGI directories are named cgi-bin. Also, CGI AddHandler or SetHandler directives may also be in use for specific handlers such as perl, python and PHP. To search the http.conf file for Options enter the following command: grep "Options" /usr/local/apache2/conf/httpd.conf. For every instance of “Options” in the httpd.conf file other than where CGI files are specifically located, the “ExecCGI” must be explicitly disabled (-ExecCGI). If the value for Options is not returned with a “-ExecCGI” , this is a finding.

## Group: WA000-WWA052

**Group ID:** `V-13732`

### Rule: The "–FollowSymLinks” setting must be disabled.



**Rule ID:** `SV-40129r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Options directive configures the web server features that are available in particular directories. The FollowSymLinks option controls the ability of the server to follow symbolic links. A symbolic link allows a file or a directory to be referenced using a symbolic name raising a potential hazard if symbolic linkage is made to a sensitive area. When web scripts are executed and symbolic links are allowed, the web user could be allowed to access locations on the web server that are outside the scope of the web document root or home directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
To view the Options value enter the following command: grep "Options" /usr/local/apache2/conf/httpd.conf. Review all uncommented Options statements for the following value: -FollowSymLinks If the value is found with an Options statement, and it does not have a preceding ‘-‘, this is a finding. Notes: - If the value does NOT exist, this is a finding. - If all enabled Options statement are set to None this is not a finding.

## Group: WA000-WWA054

**Group ID:** `V-13733`

### Rule: Server side includes (SSIs) must run with execution capability disabled.

**Rule ID:** `SV-32753r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Options directive configures the web server features that are available in particular directories. The IncludesNOEXEC feature controls the ability of the server to utilize SSIs while disabling the exec command, which is used to execute external scripts. If the full includes feature is used it could allow the execution of malware leading to a system compromise. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
To view the Options value enter the following command: grep "Options" /usr/local/apache2/conf/httpd.conf. Review all uncommented Options statements for the following values: +IncludesNoExec -IncludesNoExec -Includes If these values don’t exist this is a finding. Notes: - If the value does NOT exist, this is a finding. - If all enabled Options statement are set to None this is not a finding.

## Group: WA000-WWA056

**Group ID:** `V-13734`

### Rule: The MultiViews directive must be disabled.

**Rule ID:** `SV-32754r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Directory options directives are directives that can be applied to further restrict access to file and directories. MultiViews is a per-directory option, meaning it can be set with an Options directive within a <Directory>, <Location> or <Files> section in httpd.conf, or (if AllowOverride is properly set) in .htaccess files. The effect of MultiViews is as follows: if the server receives a request for /some/dir/foo, if /some/dir has MultiViews enabled, and /some/dir/foo does not exist, then the server reads the directory looking for files named foo.*, and effectively fakes up a type map which names all those files, assigning them the same media types and content-encodings it would have if the client had asked for one of them by name. It then chooses the best match to the client's requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
To view the MultiViews value enter the following command: grep "MultiView" /usr/local/apache2/conf/httpd.conf. Review all uncommented Options statements for the following value: -MultiViews If the value is found on the Options statement, and it does not have a preceding ‘-‘, this is a finding. Notes: - If the value does NOT exist, this is a finding. - If all enabled Options statement are set to None this is not a finding.

## Group: WA000-WWA058

**Group ID:** `V-13735`

### Rule: Directory indexing must be disabled on directories not containing index files.

**Rule ID:** `SV-32755r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Directory options directives are directives that can be applied to further restrict access to file and directories. If a URL which maps to a directory is requested, and there is no DirectoryIndex (e.g., index.html) in that directory, then mod_autoindex will return a formatted listing of the directory which is not acceptable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
To view the Indexes value enter the following command: grep "Indexes" /usr/local/apache2/conf/httpd.conf. Review all uncommented Options statements for the following value: -Indexes If the value is found on the Options statement, and it does not have a preceding ‘-‘, this is a finding. Notes: - If the value does NOT exist, this is a finding. - If all enabled Options statement are set to None this is not a finding.

## Group: WA000-WWA060

**Group ID:** `V-13736`

### Rule: The HTTP request message body size must be limited.

**Rule ID:** `SV-32756r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Buffer overflow attacks are carried out by a malicious attacker sending amounts of data that the web server cannot store in a given size buffer. The eventual overflow of this buffer can overwrite system memory. Subsequently an attacker may be able to elevate privileges and take control of the server. The Apache directives listed below limit the size of the various HTTP header sizes thereby limiting the chances for a buffer overflow. The LimitRequestBody directive allows the user to set a limit on the allowed size of an HTTP request message body within the context in which the directive is given (server, per-directory, per-file or per-location). If the client request exceeds that limit, the server will return an error response instead of servicing the request. The size of a normal request message body will vary greatly depending on the nature of the resource and the methods allowed on that resource. CGI scripts typically use the message body for retrieving form information. Implementations of the PUT method will require a value at least as large as any representation that the server wishes to accept for that resource. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
To view the LimitRequestBody value enter the following command: grep "LimitRequestBody" /usr/local/apache2/conf/httpd.conf. If the value of LimitRequestBody is not set to 1 or greater or does not exist, this is a finding. Note: The default value is set to unlimited. It is recommended that the directive be explicitly set to prevent unexpected results should the defaults change with updated software.

## Group: WA000-WWA062

**Group ID:** `V-13737`

### Rule: The HTTP request header fields must be limited. 

**Rule ID:** `SV-32757r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Buffer overflow attacks are carried out by a malicious attacker sending amounts of data that the web server cannot store in a given size buffer. The eventual overflow of this buffer can overwrite system memory. Subsequently an attacker may be able to elevate privileges and take control of the server. This Apache directives limits the size of the various HTTP header sizes thereby limiting the chances for a buffer overflow. The LimitRequestFields directive allows the server administrator to modify the limit on the number of request header fields allowed in an HTTP request. A server needs this value to be larger than the number of fields that a normal client request might include. The number of request header fields used by a client rarely exceeds 20, but this may vary among different client implementations, often depending upon the extent to which a user has configured their browser to support detailed content negotiation. Optional HTTP extensions are often expressed using request header fields. This directive gives the server administrator greater control over abnormal client request behavior, which may be useful for avoiding some forms of denial-of-service attacks. The value should be increased if normal clients see an error response from the server that indicates too many fields were sent in the request. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
To view the LimitRequestFields value enter the following command: grep "LimitRequestFields" /usr/local/apache2/conf/httpd.conf. If the value of LimitRequestFields is not set to a value greater than 0, this is a finding.

## Group: WA000-WWA064

**Group ID:** `V-13738`

### Rule: The HTTP request header field size must be limited.

**Rule ID:** `SV-32766r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Buffer overflow attacks are carried out by a malicious attacker sending amounts of data that the web server cannot store in a given size buffer. The eventual overflow of this buffer can overwrite system memory. Subsequently an attacker may be able to elevate privileges and take control of the server. This Apache directives limits the size of the various HTTP header sizes thereby limiting the chances for a buffer overflow. The LimitRequestFieldSize directive allows the server administrator to reduce or increase the limit on the allowed size of an HTTP request header field. A server needs this value to be large enough to hold any one header field from a normal client request. The size of a normal request header field will vary greatly among different client implementations, often depending upon the extent to which a user has configured their browser to support detailed content negotiation. SPNEGO authentication headers can be up to 12392 bytes. This directive gives the server administrator greater control over abnormal client request behavior, which may be useful for avoiding some forms of denial-of-service attacks. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
To view the LimitRequestFieldSize value enter the following command: grep "LimitRequestFieldSize" /usr/local/apache2/conf/httpd.conf. If no LimitRequestFieldSize directives exist, this is a Finding. Although the default value is 8190, this directive must be explicitly set. If the value of LimitRequestFieldSize is not set to 8190, this is a finding.

## Group: WA000-WWA066

**Group ID:** `V-13739`

### Rule: The HTTP request line must be limited.

**Rule ID:** `SV-32768r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Buffer overflow attacks are carried out by a malicious attacker sending amounts of data that the web server cannot store in a given size buffer. The eventual overflow of this buffer can overwrite system memory. Subsequently an attacker may be able to elevate privileges and take control of the server. This Apache directives limits the size of the various HTTP header sizes thereby limiting the chances for a buffer overflow. The LimitRequestLine directive allows the server administrator to reduce or increase the limit on the allowed size of a client's HTTP request-line. Since the request-line consists of the HTTP method, URI, and protocol version, the LimitRequestLine directive places a restriction on the length of a request-URI allowed for a request on the server. A server needs this value to be large enough to hold any of its resource names, including any information that might be passed in the query part of a GET request. This directive gives the server administrator greater control over abnormal client request behavior, which may be useful for avoiding some forms of denial-of-service attacks. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
To view the LimitRequestLine value enter the following command: grep "LimitRequestLine" /usr/local/apache2/conf/httpd.conf. If the value of LimitRequestLine is not set to 8190, this is a finding. If no LimitRequestLine directives exist, this is a Finding. Although the default value is 8190, this directive must be explicitly set.

## Group: WA00500

**Group ID:** `V-26285`

### Rule: Active software modules must be minimized.

**Rule ID:** `SV-33215r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Modules are the source of Apache httpd servers core and dynamic capabilities. Thus not every module available is needed for operation. Most installations only need a small subset of the modules available. By minimizing the enabled modules to only those that are required, we reduce the number of doors and have therefore reduced the attack surface of the web site. Likewise having fewer modules means less software that could have vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Enter the following command: /usr/local/Apache2.2/bin/httpd –M This will provide a list of the loaded modules. Validate that all displayed modules are required for operations. If any module is not required for operation, this is a finding. Note: The following modules are needed for basic web function and do not need to be reviewed: core_module http_module so_module mpm_prefork_module

## Group: WA00505

**Group ID:** `V-26287`

### Rule: Web Distributed Authoring and Versioning (WebDAV) must be disabled.

**Rule ID:** `SV-33216r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Apache mod_dav and mod_dav_fs modules support WebDAV ('Web-based Distributed Authoring and Versioning') functionality for Apache. WebDAV is an extension to the HTTP protocol which allows clients to create, move, and delete files and resources on the web server. WebDAV is not widely used, and has serious security concerns as it may allow clients to modify unauthorized files on the web server. Therefore, the WebDav modules mod_dav and mod_dav_fs should be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Enter the following command: /usr/local/Apache2.2/bin/httpd –M. This will provide a list of all loaded modules. If any of the following modules are found, this is a finding. dav_module dav_fs_module dav_lock_module

## Group: WA00510

**Group ID:** `V-26294`

### Rule: Web server status module must be disabled.

**Rule ID:** `SV-33218r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Apache mod_info module provides information on the server configuration via access to a /server-info URL location, while the mod_status module provides current server performance statistics. While having server configuration and status information available as a web page may be convenient, it is recommended that these modules not be enabled: Once mod_info is loaded into the server, its handler capability is available in per-directory .htaccess files and can leak sensitive information from the configuration directives of other Apache modules such as system paths, usernames/passwords, database names, etc. If mod_status is loaded into the server, its handler capability is available in all configuration files, including per-directory files (e.g., .htaccess) and may have security-related ramifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Enter the following command: /usr/local/Apache2.2/bin/httpd –M. This will provide a list of all loaded modules. If any of the following modules are found, this is a finding. info_module status_module

## Group: WA00520

**Group ID:** `V-26299`

### Rule: The web server must not be configured as a proxy server.

**Rule ID:** `SV-33220r3_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Apache proxy modules allow the server to act as a proxy (either forward or reverse proxy) of http and other protocols with additional proxy modules loaded. If the Apache installation is not intended to proxy requests to or from another network then the proxy module should not be loaded. Proxy servers can act as an important security control when properly configured, however a secure proxy server is not within the scope of this STIG. A web server should be primarily a web server or a proxy server but not both, for the same reasons that other multi-use servers are not recommended. Scanning for web servers that will also proxy requests is a very common attack, as proxy servers are useful for anonymizing attacks on other servers, or possibly proxying requests into an otherwise protected network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the Apache web server is only performing in a proxy server role and does not host any websites nor support any applications, this check is Not Applicable. Enter the following command: /usr/local/Apache2.2/bin/httpd –M. This will provide a list of all loaded modules. If any of the following modules are found, this is a finding: proxy_module proxy_ajp_module proxy_balancer_module proxy_ftp_module proxy_http_module proxy_connect_module

## Group: WA00525

**Group ID:** `V-26302`

### Rule: User specific directories must not be globally enabled.

**Rule ID:** `SV-33221r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The UserDir directive must be disabled so that user home directories are not accessed via the web site with a tilde (~) preceding the username. The directive also sets the path name of the directory that will be accessed. The user directories should not be globally enabled since it allows anonymous access to anything users may want to share with other users on the network. Also consider that every time a new account is created on the system, there is potentially new content available via the web site.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Enter the following command: /usr/local/Apache2.2/bin/httpd –M. This will provide a list of all loaded modules. If userdir_module is listed, this is a finding.

## Group: WA00530

**Group ID:** `V-26305`

### Rule: The process ID (PID) file must be properly secured.

**Rule ID:** `SV-33222r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The PidFile directive sets the file path to the process ID file to which the server records the process id of the server, which is useful for sending a signal to the server process or for checking on the health of the process. If the PidFile is placed in a writable directory, other accounts could create a denial of service attack and prevent the server from starting by creating a PID file with the same name.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Enter the following command: more /usr/local/Apache2.2/conf/httpd.conf. Review the httpd.conf file and search for the following uncommented directive: PidFile Note the location and name of the PID file. If the PidFile directive is not found enabled in the conf file, use /logs as the directory containing the Scoreboard file. Verify the permissions and ownership on the folder containing the PID file. If any user accounts other than root, auditor, or the account used to run the web server have permission to, or ownership of, this folder, this is a finding. If the PID file is located in the web server DocumentRoot this is a finding.

## Group: WA00535

**Group ID:** `V-26322`

### Rule: The score board file must be properly secured.


**Rule ID:** `SV-33223r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ScoreBoardfile directive sets a file path which the server will use for Inter-Process Communication (IPC) among the Apache processes. If the directive is specified, then Apache will use the configured file for the inter-process communication. Therefore if it is specified it needs to be located in a secure directory. If the ScoreBoardfile is placed in a writable directory, other accounts could create a denial of service attack and prevent the server from starting by creating a file with the same name, and or users could monitor and disrupt the communication between the processes by reading and writing to the file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
To determine the location of the file enter the following command: find / -name ScoreBoard. To view the permissions on the file enter the following command: ls -lL /path/of/ScoreBoard. If the permissions on the file are not set to 644 or is configured to be less restrictive, this is a finding.

## Group: WA00540

**Group ID:** `V-26323`

### Rule: The web server must be configured to explicitly deny access to the OS root.

**Rule ID:** `SV-33226r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Apache Directory directive allows for directory specific configuration of access controls and many other features and options. One important usage is to create a default deny policy that does not allow access to Operating System directories and files, except for those specifically allowed. This is done, with denying access to the OS root directory. One aspect of Apache, which is occasionally misunderstood, is the feature of default access. That is, unless you take steps to change it, if the server can find its way to a file through normal URL mapping rules, it can and will serve it to clients. Having a default deny is a predominate security principal, and then helps prevent the unintended access, and we do that in this case by denying access to the OS root directory. The Order directive is important as it provides for other Allow directives to override the default deny.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Enter the following command: more /usr/local/Apache2.2/conf/httpd.conf. Review the httpd.conf file and search for the following directive: Directory For every root directory entry (i.e. <Directory />) ensure the following exists; if not, this is a finding. Order deny,allow Deny from all If the statement above is not found in the root directory statement, this is a finding. If Allow directives are included in the root directory statement, this is a finding.

## Group: WA00545

**Group ID:** `V-26324`

### Rule: Web server options for the OS root must be disabled.

**Rule ID:** `SV-33213r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Apache Options directive allows for specific configuration of options, including execution of CGI, following symbolic links, server side includes, and content negotiation. The Options directive for the root OS level is used to create a default minimal options policy that allows only the minimal options at the root directory level. Then for specific web sites or portions of the web site, options may be enabled as needed and appropriate. No options should be enabled and the value for the Options Directive should be None.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Enter the following command: more /usr/local/Apache2.2/conf/httpd.conf. Review the httpd.conf file and search for the following directive: Directory For every root directory entry (i.e. <Directory />) ensure the following entry exists: Options None If the statement above is not found in the root directory statement, this is a finding. If Allow directives are included in the root directory statement, this is a finding. If the root directory statement is not found at all, this is a finding.

## Group: WA00550

**Group ID:** `V-26325`

### Rule: The TRACE  method must be disabled.

**Rule ID:** `SV-33227r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Diagnostics help establish a history of activities, and can be useful in detecting attack attempts or determining tuning adjustments to improve server availability. Trace logs are essential to the investigation and prosecution of unauthorized access to web server software and data. However, in standard production operations, use of diagnostics may reveal undiscovered vulnerabilities and ultimately, to compromise of the data. Because of the potential for abuse, the HTTP Trace method should be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Enter the following command: grep "TraceEnable" /usr/local/apache2/conf/httpd.conf. Review the results for the following directive: TraceEnable. For any enabled TraceEnable directives ensure they are part of the server level configuration (i.e. not nested in a <Directory> or <Location> directive). Also ensure that the TraceEnable directive is set to “Off”. If the TraceEnable directive is not part of the server level configuration and/or is not set to “Off”, this is a finding. If the directive does not exist in the conf file, this is a finding because the default value is "On".

## Group: WA00555

**Group ID:** `V-26326`

### Rule: The web server must be configured to listen on a specific IP address and port.

**Rule ID:** `SV-33228r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Apache Listen directive specifies the IP addresses and port numbers the Apache web server will listen for requests. Rather than be unrestricted to listen on all IP addresses available to the system, the specific IP address or addresses intended must be explicitly specified. Specifically a Listen directive with no IP address specified, or with an IP address of zero’s should not be used. Having multiple interfaces on web servers is fairly common, and without explicit Listen directives, the web server is likely to be listening on an inappropriate IP address / interface that were not intended for the web server. Single homed system with a single IP addressed are also required to have an explicit IP address in the Listen directive, in case additional interfaces are added to the system at a later date.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Enter the following command: grep "Listen" /usr/local/apache2/conf/httpd.conf Review the results for the following directive: Listen For any enabled Listen directives ensure they specify both an IP address and port number. If the Listen directive is found with only an IP address, or only a port number specified, this is finding. If the IP address is all zeros (i.e. 0.0.0.0:80 or [::ffff:0.0.0.0]:80, this is a finding. If the Listen directive does not exist, this is a finding.

## Group: WA00560

**Group ID:** `V-26327`

### Rule: The URL-path name must be set to the file path name or the directory path name.

**Rule ID:** `SV-33229r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ScriptAlias directive controls which directories the Apache server "sees" as containing scripts. If the directive uses a URL-path name that is different than the actual file system path, the potential exists to expose the script source code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Enter the following command: grep "ScriptAlias" /usr/local/apache2/conf/httpd.conf. If any enabled ScriptAlias directive do not have matching URL-path and file-path or directory-path entries, this is a finding.

## Group: WA00515

**Group ID:** `V-26368`

### Rule: Automatic directory indexing must be disabled.

**Rule ID:** `SV-33219r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To identify the type of web servers and versions software installed it is common for attackers to scan for icons or special content specific to the server type and version. A simple request like http://example.com/icons/apache_pb2.png may tell the attacker that the server is Apache 2.2 as shown below. The many icons are used primary for auto indexing, which is recommended to be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Enter the following command: /usr/local/Apache2.2/bin/httpd –M. This will provide a list of all loaded modules. If autoindex_module is found, this is a finding.

## Group: WA00547

**Group ID:** `V-26393`

### Rule: The ability to override the access configuration for the OS root directory must be disabled.

**Rule ID:** `SV-33232r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Apache OverRide directive allows for .htaccess files to be used to override much of the configuration, including authentication, handling of document types, auto generated indexes, access control, and options. When the server finds an .htaccess file (as specified by AccessFileName) it needs to know which directives declared in that file can override earlier access information. When this directive is set to None, then .htaccess files are completely ignored. In this case, the server will not even attempt to read .htaccess files in the file system. When this directive is set to All, then any directive which has the .htaccess Context is allowed in .htaccess files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Enter the following command: more /usr/local/Apache2.2/conf/httpd.conf. Review the httpd.conf file and search for the following directive: Directory For every root directory entry (i.e. <Directory />) ensure the following entry exists: AllowOverride None If the statement above is not found in the root directory statement, this is a finding. If Allow directives are included in the root directory statement, this is a finding. If the root directory statement is not listed at all, this is a finding.

## Group: WA00565 

**Group ID:** `V-26396`

### Rule: HTTP request methods must be limited.

**Rule ID:** `SV-33236r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The HTTP 1.1 protocol supports several request methods which are rarely used and potentially high risk. For example, methods such as PUT and DELETE are rarely used and should be disabled in keeping with the primary security principal of minimize features and options. Also since the usage of these methods is typically to modify resources on the web server, they should be explicitly disallowed. For normal web server operation, you will typically need to allow only the GET, HEAD and POST request methods. This will allow for downloading of web pages and submitting information to web forms. The OPTIONS request method will also be allowed as it is used to request which HTTP request methods are allowed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Note: If HTTP commands (GET, PUT, POST, DELETE) are not being used and server is solely configured as a proxy server, this is Not Applicable. Enter the following command: more /usr/local/apache2/conf/httpd.conf For every enabled <Directory> directive (except root), ensure the following entry exists: Order allow,deny <LimitExcept GET POST OPTIONS> Deny from all </LimitExcept> If the statement above is found in the root directory statement (i.e. <Directory />), this is a finding. If the statement above is found enabled but without the appropriate LimitExcept or Order statement, this is a finding. If the statement is not found inside an enabled <Directory> directive, this is a finding. Note: If the LimitExcept statement above is operationally limiting. This should be explicitly documented with the Web Manager, at which point this can be considered not a finding.

## Group: WG345

**Group ID:** `V-60707`

### Rule: The web server must remove all export ciphers from the cipher suite.

**Rule ID:** `SV-75159r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>During the initial setup of a Transport Layer Security (TLS) connection to the web server, the client sends a list of supported cipher suites in order of preference. The web server will reply with the cipher suite it will use for communication from the client list. If an attacker can intercept the submission of cipher suites to the web server and place, as the preferred cipher suite, a weak export suite, the encryption used for the session becomes easy for the attacker to break, often within minutes to hours.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf and ssl.conf file if available. Open the httpd.conf and ssl.conf file with an editor and search for the following uncommented directive: SSLCipherSuite For all enabled SSLCipherSuite directives, ensure the cipher specification string contains the kill cipher from list option for all export cipher suites, i.e., !EXPORT, which may be abbreviated !EXP. If the SSLCipherSuite directive does not contain !EXPORT or there are no enabled SSLCipherSuite directives, this is a finding.

