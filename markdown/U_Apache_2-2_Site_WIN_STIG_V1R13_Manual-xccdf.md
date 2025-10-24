# STIG Benchmark: APACHE 2.2 Site for Windows Security Technical Implementation Guide

---

**Version:** 1

**Description:**
All directives specified in this STIG must be specifically set (i.e. the server is not allowed to revert to programmed defaults for these directives). Included files should be reviewed if they are used. Procedures for reviewing included files are included in the overview document. The use of .htaccess files are not authorized for use according to the STIG. However, if they are used, there are procedures for reviewing them in the overview document. The Web Policy STIG should be used in addition to the Apache Site and Server STIGs in order to do a comprehensive web server review.

## Group: WG210

**Group ID:** `V-2226`

### Rule: Web content directories must not be anonymously shared.

**Rule ID:** `SV-33109r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Sharing of web server content is a security risk when a web server is involved. Users accessing the share anonymously could experience privileged access to the content of such directories. Network sharable directories expose those directories and their contents to unnecessary access. Any unnecessary exposure increases the risk that someone could exploit that access and either compromises the web content or cause web server performance problems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. If unable to locate the file, perform a search of the system to find the location of the file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directives: DocumentRoot & ServerRoot Note the location following each enabled DocumentRoot and ServerRoot directives. Navigate to the DocumentRoot, and ServerRoot, using the path identified above. Right click on the directory to be examined. Select Properties > Select the “Sharing” tab. If either folder is shared, this is a finding. NOTE: The presence of operating system shares on the web server is not an issue as long as the shares are not part of the web content directories. The use of shares to move content from one environment to another is permitted if the following conditions are met: they are approved by the ISSM/ISSO, the shares are restricted to only allow administrators write access, the use of the shares does not bypass the sites approval process for posting new content to the web server, and developers are only permitted read access to these directories.

## Group: WG400

**Group ID:** `V-2228`

### Rule: All interactive programs must be placed in a designated directory with appropriate permissions.

**Rule ID:** `SV-36644r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>CGI scripts represents one of the most common and exploitable means of compromising a web server. By definition, CGI are executable by the operating system of the host server. While access control is provided via the web service, the execution of CGI programs is not otherwise limited unless the SA or Web Manager takes specific measures. CGI programs can access and alter data files, launch other programs and use the network. CGI programs can be written in any available programming language. C, PERL, PHP, Javascript, VBScript and shell (sh, ksh, bash) are popular choices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
To preclude access to the servers root directory, ensure the following directive is in the httpd.conf file. This entry will also stop users from setting up .htaccess files which can override security features configured in httpd.conf. <DIRECTORY /[website root dir]> AllowOverride None </DIRECTORY> If the AllowOverride None is not set, this is a finding.

## Group: WG410

**Group ID:** `V-2229`

### Rule: Interactive scripts used on a web server must have proper access controls.

**Rule ID:** `SV-28849r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of CGI scripts represent one of the most common and exploitable means of compromising a web server. By definition, CGI scripts are executable by the operating system of the host server. While access control is provided via the web service, the execution of CGI programs is not limited unless the SA or the Web Manager takes specific measures. CGI programs can access and alter data files, launch other programs, and use the network. CGI programs can be written in any available programming language. C, PERL, PHP, Javascript, VBScript, and shell programs (e.g., sh, ksh, bash, etc.) are popular choices. CGI is a standard for interfacing external applications with information servers, such as HTTP or web servers. The definition of CGI as web-based applications is not to be confused with the more specific .cgi file extension. ASP, JSP, JAVA, and PERL scripts are commonly found in these circumstances. Clarification: This vulnerability, which is related to VMS vulnerability V-2228, requires that appropriate access permissions are applied to CGI files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Query the SA to determine if CGI scripts are used as part of the web site. If interactive scripts are being used, check the permissions of these files to ensure they meet the following permissions: interactive script files Administrators Full Control WebManagers Modify System Read/Execute Webserver Account Read/Execute If the interactive scripts do not meet the above permissions or are less restrictive, this is a finding.

## Group: WG110

**Group ID:** `V-2240`

### Rule: The number of allowed simultaneous requests must be set.

**Rule ID:** `SV-33105r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Resource exhaustion can occur when an unlimited number of concurrent requests are allowed on a web site, facilitating a denial of service attack. Mitigating this kind of attack will include limiting the number of concurrent HTTP/HTTPS requests per IP address and may include, where feasible, limiting parameter values associated with keepalive, (i.e., a parameter used to limit the amount of time a connection may be inactive).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
NOTE: This setting must be explicitly set. Locate the Apache httpd.conf file. If unable to locate the file, perform a search of the system to find the location of the file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directive: MaxKeepAliveRequests Every enabled MaxKeepAliveRequests value needs to be 100 or greater. If any directive is less than 100, this is a finding.

## Group: WG170

**Group ID:** `V-2245`

### Rule: Each readable web document directory must contain either a default, home, index, or equivalent file.

**Rule ID:** `SV-33107r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The goal is to completely control the web users experience in navigating any portion of the web document root directories. Ensuring all web content directories have indexing turned off or at least the equivalent of an index.html file is a significant factor to accomplish this end. Enumeration techniques, such as URL parameter manipulation, rely upon the ability to obtain information about the web server’s directory structure through locating directories without default pages.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. If unable to locate the file, perform a search of the system to find the location of the file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directive: DocumentRoot Note the name of the DocumentRoot directory. Review the results for each document root directory and its subdirectories. If a directory does not contain an index.html or equivalent default document, this is a finding.

## Group: WG230

**Group ID:** `V-2249`

### Rule: Web server administration must be performed over a secure path or at the local console.

**Rule ID:** `SV-33110r3_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Logging into a web server remotely using an unencrypted protocol or service when performing updates and maintenance is a major risk. Data, such as user account, is transmitted in plaintext and can easily be compromised. When performing remote administrative tasks, a protocol or service that encrypts the communication channel must be used. An alternative to remote administration of the web server is to perform web server administration locally at the console. Local administration at the console implies physical access to the server. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
If web administration is performed at the console, this check is N/A. If web administration is performed remotely the following checks will apply: 1. If administration of the server is performed remotely, it will only be performed securely by system administrators. 2. If web site administration or web application administration has been delegated, those users will be documented and approved by the ISSO. 3. Remote administration must be in compliance with any requirements contained within the Windows Server STIGs, and any applicable network STIGs. 4. Remote administration of any kind will be restricted to documented and authorized personnel. 5. All users performing remote administration must be authenticated. 6. All remote sessions will be encrypted and they will utilize FIPS 140-2 approved protocols. FIPS 140-2 approved TLS versions include TLS V1.0 or greater. Review with site management how remote administration, if applicable, is configured on the web site. If remote management meets the criteria listed above, this is not a finding. If remote management is utilized and does not meet the criteria listed above, this is a finding.

## Group: WG240

**Group ID:** `V-2250`

### Rule: Logs of web server access and errors must be established and maintained.

**Rule ID:** `SV-33132r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A major tool in exploring the web site use, attempted use, unusual conditions, and problems are reported in the access and error logs. In the event of a security incident, these logs can provide the SA and the web manager with valuable information. Without these log files, SAs and web managers are seriously hindered in their efforts to respond appropriately to suspicious or criminal actions targeted at the web site.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Open a command prompt window. Navigate to the “bin” directory (in many cases this may be [Drive Letter]:\[directory path]\Apache Software Foundation\Apache2.2\bin>). Enter the following command and press Enter: httpd –M This will provide a list of all loaded modules. If the following module is not found this is a finding: log_config_module.

## Group: WG250

**Group ID:** `V-2252`

### Rule: Log file access must be restricted to System Administrators, Web Administrators or Auditors.

**Rule ID:** `SV-33135r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A major tool in exploring the web site use, attempted use, unusual conditions and problems are the access and error logs. In the event of a security incident, these logs can provide the SA and Web Manager with valuable information. To ensure the integrity of the log files and protect the SA and Web Manager from a conflict of interest related to the maintenance of these files, only the members of the Auditors group will be granted permissions to move, copy and delete these files in the course of their duties related to the archiving of these files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. If unable to locate the file, perform a search of the system to find the location of the file. Open the httpd.conf file with an editor such as Notepad, and search for the following uncommented directives: ErrorLog & CustomLog Navigate to the location of the file specified after each enabled ErrorLog & CustomLog directive and verify the permissions assigned to these files. Right click on the file to be examined. Select Properties > Select the “Security” tab. Permissions greater than Read & Execute should be allowed for only the account assigned to the Apache server service, and the Auditors Group. If the SA, Web Manager or users other than the Auditors group have greater than read access to the log files, this is a finding. If anyone other than the Auditors, Administrators, Web Managers, or the account assigned to the Apache server service has access to the log files, this is a finding.

## Group: WG260

**Group ID:** `V-2254`

### Rule: Only web sites that have been fully reviewed and tested must exist on a production web server.

**Rule ID:** `SV-33134r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In the case of a production web server, areas for content development and testing will not exist, as this type of content is only permissible on a development web site. The process of developing on a functional production web site entails a degree of trial and error and repeated testing. This process is often accomplished in an environment where debugging, sequencing, and formatting of content are the main goals. The opportunity for a malicious user to obtain files that reveal business logic and login schemes is high in this situation. The existence of such immature content on a web server represents a significant security risk that is totally avoidable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Query the ISSO, the SA, and the web administrator to find out if development web sites are being housed on production web servers. Definition: A production web server is any web server connected to a production network, regardless of its role. Proposed Questions: Do you have development sites on your production web server? What is your process to get development web sites / content posted to the production server? Do you use under construction notices on production web pages? The reviewer can also do a manual check or perform a navigation of the web site via a browser to confirm the information provided from interviewing the web staff. Graphics or texts which proclaim Under Construction or Under Development are frequently used to mark folders or directories in that status. If Under Construction or Under Development web content is discovered on the production web server, this is a finding.

## Group: WG290

**Group ID:** `V-2258`

### Rule: The web client account access to the content and scripts directories must be limited to read and execute.

**Rule ID:** `SV-33136r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Excessive permissions for the anonymous web user account are one of the most common faults contributing to the compromise of a web server. If this user is able to upload and execute files on the web server, the organization or owner of the server will no longer have control of the asset.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. If unable to locate the file, perform a search of the system to find the location of the file. Open the httpd.conf file with an editor such as Notepad, and search for the following uncommented directives: DocumentRoot, Alias, ScriptAlias, & ScriptAliasMatch Navigate to the locations specified after each enabled DocumentRoot, Alias, ScriptAlias, & ScriptAliasMatch directives. Right click on the file or directory to be examined. Select Properties. Select the “Security” tab. The only accounts listed should be the web administrator, developers, and the account assigned to run the apache server service. If accounts that do not need access to these directories are listed, this is a finding. If the permissions assigned to the Apache web server service are greater than Read for locations associated with the DocumentRoot and Alias directives, this is a finding. If the permissions assigned to the Apache web server service are greater than Read & Execute for locations associated with ScriptAlias and ScriptAliasMatch, this is a finding.

## Group: WG310

**Group ID:** `V-2260`

### Rule: A web site must not contain a robots.txt file.

**Rule ID:** `SV-28798r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Search engines are constantly at work on the Internet. Search engines are augmented by agents, often referred to as spiders or bots, which endeavor to capture and catalog web-site content. In turn, these search engines make the content they obtain and catalog available to any public web user. To request that a well behaved search engine not crawl and catalog a site, the web site may contain a file called robots.txt. This file contains directories and files that the web server SA desires not be crawled or cataloged, but this file can also be used, by an attacker or poorly coded search engine, as a directory and file index to a site. This information may be used to reduce an attacker’s time searching and traversing the web site to find files that might be relevant. If information on the web site needs to be protected from search engines and public view, other methods must be used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. If unable to locate the file, perform a search of the system to find the location of the file. Open the httpd.conf file with an editor and search for the following uncommented directives: DocumentRoot & Alias Navigate to the location(s) specified in the Include statement(s), and review each file for the following uncommented directives: DocumentRoot & Alias At the top level of the directories identified after the enabled DocumentRoot & Alias directives, verify that a “robots.txt” file does not exist. If the file does exist, this is a finding.

## Group: WG340

**Group ID:** `V-2262`

### Rule: A private web server must utilize an approved TLS version.

**Rule ID:** `SV-14297r3_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Transport Layer Security (TLS) encryption is a required security setting for a private web server. Encryption of private information is essential to ensuring data confidentiality. If private information is not encrypted, it can be intercepted and easily read by an unauthorized party. A private web server must use a FIPS 140-2 approved TLS version, and all non-FIPS-approved SSL versions must be disabled. FIPS 140-2 approved TLS versions include TLS V1.0 or greater. NIST SP 800-52 specifies the preferred configurations for government systems. The SSLProtocol directive enables or disables SSL/TLS protocols. “SSLProtocol ALL” is a shortcut for enabling SSLv3 and TLSv1 but does not disable lower versions of SSL. Since some Apache versions enable SSL by default, SSL needs to be explicitly disabled, while also enabling TLS. To disable specific SSL Protocols, the –SSLv3 –SSLv2 switches are used with the SSLProtocol directive. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the ssl module is loaded. Open a command prompt and run the following command from the directory where httpd.exe is located: httpd –M This will provide a list of all the loaded modules. Verify that the “ssl_module” is loaded. If this module is not found, this is a finding. After determining that the ssl module is active, locate the Apache httpd.conf file. If unable to locate the file, perform a search of the system to find the file. Open the httpd.conf file with an editor such as Notepad and search for the following uncommented directives: SSLProtocol and SSLEngine For all enabled SSLProtocol directives, ensure the “-SSLv2 -SSLv3” switches to disable SSL are included in the directive. If the SSLProtocol directive is not set to explicitly disable SSLv2 and SSLv3, this is a finding. Note: For Apache 2.2.22 and older, all enabled SSLProtocol directives must be set to "TLSv1" or higher or this is a finding. For all enabled SSLEngine directives, ensure they are set to “on”. Both the SSLProtocol and SSLEngine directives must be set correctly or this is a finding. Note: In some cases web servers are configured in an environment to support load balancing. This configuration most likely uses a content switch to control traffic to the various web servers. In this situation, the TLS certificate for the websites may be installed on the content switch versus the individual websites. This solution is acceptable as long as the web servers are isolated from the general population LAN. Users must not have the ability to bypass the content switch to access the websites.

## Group: WG350

**Group ID:** `V-2263`

### Rule: A private web server must have a valid DoD server certificate.

**Rule ID:** `SV-33141r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This check verifies that DoD is a hosted web site's CA. The certificate is actually a DoD-issued server certificate used by the organization being reviewed. This is used to verify the authenticity of the web site to the user. If the certificate is not for the server (Certificate belongs to), if the certificate is not issued by DoD (Certificate was issued by), or if the current date is not included in the valid date (Certificate is valid from), then there is no assurance that the use of the certificate is valid. The entire purpose of using a certificate is, therefore, compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Open browser window and browse to the appropriate site. Before entry to the site, you should be presented with the server's DoD PKI credentials. Review these credentials for authenticity. Find an entry which cites: Issuer: CN = DOD CLASS 3 CA-3 OU = PKI OU = DoD O = U.S. Government C = US If the server is running as a public web server, this finding should be Not Applicable. NOTE: In some cases, the web servers are configured in an environment to support load balancing. This configuration most likely utilizes a content switch to control traffic to the various web servers. In this situation, the SSL certificate for the web sites may be installed on the content switch vs. the individual web sites. This solution is acceptable as long as the web servers are isolated from the general population LAN. Users should not have the ability to bypass the content switch to access the web sites.

## Group: WG490

**Group ID:** `V-2265`

### Rule: Java software on production web servers must be limited to class files and the JAVA virtual machine.

**Rule ID:** `SV-33143r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>From the source code in a .java or a .jpp file, the Java compiler produces a binary file with an extension of .class. The .java or .jpp file would, therefore, reveal sensitive information regarding an application’s logic and permissions to resources on the server. By contrast, the .class file, because it is intended to be machine independent, is referred to as bytecode. Bytecodes are run by the Java Virtual Machine (JVM), or the Java Runtime Environment (JRE), via a browser configured to permit Java code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Search the web content and scripts directories (found in check WG290) for .java and .jpp files. If either file type is found, this is a finding. Note: Executables such as java.exe, jre.exe, and jrew.exe are permitted.

## Group: WG430

**Group ID:** `V-2270`

### Rule: Anonymous FTP user access to interactive scripts must be prohibited.

**Rule ID:** `SV-36714r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The directories containing the CGI scripts, such as PERL, must not be accessible to anonymous users via FTP. This applies to all directories that contain scripts that can dynamically produce web pages in an interactive manner (i.e., scripts based upon user-provided input). Such scripts contain information that could be used to compromise a web service, access system resources, or deface a web site.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the directories containing the CGI scripts. These directories should be language-specific (e.g., PERL, ASP, JS, JSP, etc.). Right-click on the web content directory and the related CGI directories. On the Properties tab, examine the access rights for the CGI, cgi-bin, or cgi-shl directories. Anonymous FTP users must not have access to these directories. If the CGI, the cgi-bin, or the cgi-shl directories can be accessed by any group that does not require access, this is a finding.

## Group: WG460

**Group ID:** `V-2272`

### Rule: PERL scripts must use the TAINT option.

**Rule ID:** `SV-33144r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>PERL (Practical Extraction and Report Language) is an interpreted language optimized for scanning arbitrary text files, extracting information from those text files, and printing reports based on that information. The language is often used in shell scripting and is intended to be practical, easy to use, and efficient means of generating interactive web pages for the user. Unfortunately, many widely available freeware PERL programs (scripts) are extremely insecure. This is most readily accomplished by a malicious user substituting input to a PERL script during a POST or a GET operation. Consequently, the founders of PERL have developed a mechanism named TAINT that protects the system from malicious input sent from outside the program. When the data is tainted, it cannot be used in programs or functions such as eval(), system(), exec(), pipes, or popen(). The script will exit with a warning message.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations>WG460 - General</Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl>If the TAINT option cannot be used for any reason, this finding can be mitigated by the use of a third-party input validation mechanism or input validation will be included as part of the script in use. This must be documented.</MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. If unable to locate the file, perform a search of the system to find the location of the file. Open the httpd.conf file with an editor such as Notepad, and search for the following uncommented directive: ScriptInterpreterSource For any enabled ScriptInterpreterSource directives the only authorized entries are Registry-Strict or Script. If any other entry (i.e. Registry) is found, this is a finding. For all enabled ScriptInterpreterSource directives set to Registry-Strict: open regedit then Navigate to the following location: HKEY_CLASSES_ROOT\.pl\Shell\ExecCGI\Command\(Default) => C:\Perl\bin\perl.exe –T (This entry should specify the location of the Perl.exe file). If this entry is not found, this is a finding. For all enabled ScriptInterpreterSource directive set to Script: Search the system for all files ending with “.pl”. Open all files found with a text editor and ensure the following entry is found - #![Drive Letter]:/[Path to Perl install directory]/bin/perl.exe –T. If this entry is not found, this is a finding. NOTE: This applies to PERL scripts that are used as part of the web server and not all PERL scripts that are on the system. NOTE: If the mod_perl module is installed, and the directive “PerlTaintCheck on” is entered in the httpd.conf, this satisfies the requirement.

## Group: WG205

**Group ID:** `V-3333`

### Rule: The web document (home) directory must be in a separate partition from the web server’s system files.

**Rule ID:** `SV-33108r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application partitioning enables an additional security measure by securing user traffic under one security context, while managing system and application files under another. Web content is accessible to an anonymous web user. For such an account to have access to system files of any type is a major security risk that is avoidable and desirable. Failure to partition the system files from the web site documents increases risk of attack via directory traversal, or impede web site availability due to drive space exhaustion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify that installation directories for Apache HTTP server are located on another partition, other than the OS partition. Locate the Apache httpd.conf file. If unable to locate the file, perform a search of the system to find the location of the file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directives: DocumentRoot, ErrorLog, CustomLog Note the location specified for each of the directives. If the path for any of the directives is on the same partition as the web server operating system files, this is a finding.

## Group: WG265

**Group ID:** `V-6373`

### Rule: The required DoD banner page must be displayed to authenticated users accessing a DoD private website.

**Rule ID:** `SV-33137r2_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A consent banner will be in place to make prospective entrants aware that the website they are about to enter is a DoD web site and their activity is subject to monitoring. The document, DoDI 8500.01, establishes the policy on the use of DoD information systems. It requires the use of a standard Notice and Consent Banner and standard text to be included in user agreements. The requirement for the banner is for websites with security and access controls. These are restricted and not publicly accessible. If the website does not require authentication/authorization for use, then the banner does not need to be present. A manual check of the document root directory for a banner page file (such as banner.html) or navigation to the website via a browser can be used to confirm the information provided from interviewing the web staff.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
The document, DoDI 8500.01, establishes the policy on the use of DoD information systems. It requires the use of a standard Notice and Consent Banner and standard text to be included in user agreements. The requirement for the banner is for websites with security and access controls. These are restricted and not publicly accessible. If the website does not require authentication/authorization for use, then the banner does not need to be present. If a banner is required, the following banner page must be in place: “You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. - At any time, the USG may inspect and seize data stored on this IS. - Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. - This IS includes security measures (e.g., authentication and access controls) to protect USG interests—not for your personal benefit or privacy. - Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details.” OR If your system cannot meet the character limits to store this amount of text in the banner, the following is another option for the warning banner: "I've read & consent to terms in IS user agreem't." NOTE: While DoDI 8500.01 does not contain a copy of the banner to be used, it does point to the RMF Knowledge Service for a copy of the required text. It is also noted that the banner is to be displayed only once when the individual enters the site and not for each page. If the access-controlled website does not display this banner page before entry, this is a finding.

## Group: WG140

**Group ID:** `V-6531`

### Rule: Private web servers must require certificates issued from a DoD-authorized Certificate Authority.

**Rule ID:** `SV-33106r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web sites requiring authentication within the DoD must utilize PKI as an authentication mechanism for web users. Information systems residing behind web servers requiring authorization based on individual identity must use the identity provided by certificate-based authentication to support access control decisions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. If unable to locate the file, perform a search of the system to find the location of the file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directive: SSLVerifyClient If SSLVerifyClient is not set to “require” this is a finding as the client is not required to present a valid certificate.

## Group: WG235

**Group ID:** `V-13686`

### Rule: Web Administrators must only use encrypted connections for Document Root directory uploads.

**Rule ID:** `SV-33131r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Logging in to a web server via an unencrypted protocol or service, to upload documents to the web site, is a risk if proper encryption is not utilized to protect the data being transmitted. An encrypted protocol or service must be used for remote access to web administration tasks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Query the SA to determine if there is a process for the uploading of files to the web site. This process should include the requirement for the use of a secure encrypted logon and secure encrypted connection. If the remote users are uploading files without utilizing approved encryption methods, this is a finding.

## Group: WG242

**Group ID:** `V-13688`

### Rule: Log file data must contain required data elements.

**Rule ID:** `SV-28654r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of log files is a critical component of the operation of the Information Systems (IS) used within the DoD, and they can provide invaluable assistance with regard to damage assessment, causation, and the recovery of both affected components and data. They may be used to monitor accidental or intentional misuse of the (IS) and may be used by law enforcement for criminal prosecutions. The use of log files is a requirement within the DoD.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
To verify the log settings: Default Windows location: :\Program Files\Apache Group\Apache2\logs\access.log or :\Program Files\Apache Software Foundation\Apache2.2\logs\access.log. If these directories do not exist, you can search the web server for the httpd.conf config file to determine the location of the logs. Items to be logged are as shown in this sample line in the httpd.conf file: LogFormat "%a %A %h %H %l %m %s %t %u %U \"%{Referer}i\" " combined If the web server is not configured to capture the required audit events for all sites and virtual directories, this is a finding.

## Group: WG255

**Group ID:** `V-13689`

### Rule: Access to the web server log files must be restricted to Administrators, the user assigned to run the web server software, Web Manager, and Auditors.

**Rule ID:** `SV-40832r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A major tool in exploring the web site use, attempted use, unusual conditions and problems are the access and error logs. In the event of a security incident, these logs can provide the SA and Web Manager with valuable information. Because of the information that is captured in the logs, it is critical that only authorized individuals have access to the logs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Determine permissions for log files Find the httpd.conf configuration file to determine the location of the log files. The location is indicated at the "ServerRoot" directive. The log directory is a sub-directory under the ServerRoot. ex. :\Apache Group\Apache2\logs or :\Apache Software Foundation\Apache2.2\logs After locating the logs, use the Explorer to move to these files and examine their properties: Properties >> Security >> Permissions. Administrators: Read Auditors: Full Control Web Managers: Read WebServer Account: Read/Write/Execute If anyone other than the Auditors, Administrators, Web Managers, or the account that runs the web server has access to the log files, this is a finding.

## Group: WG342

**Group ID:** `V-13694`

### Rule: Public web servers must use TLS if authentication is required.

**Rule ID:** `SV-28565r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Transport Layer Security (TLS) is optional for a public web server. However, if authentication is being performed, then the use of the TLS protocol is required. Without the use of TLS, the authentication data would be transmitted unencrypted and would become vulnerable to disclosure. Using TLS along with DoD PKI certificates for encryption of the authentication data protects the information from being accessed by all parties on the network. To further protect the authentication data, the web server must use a FIPS 140-2 approved TLS version and all non-FIPS-approved SSL versions must be disabled. FIPS 140-2 approved TLS versions include TLS V1.0 or greater. NIST SP 800-52 specifies the preferred configurations for government systems. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>System Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the ssl module is loaded. Open a command prompt and run the following command from the directory when httpd.exe is located: httpd –M This will provide a list of all the loaded modules. Verify that the “ssl_module” is loaded. If this module is not found, this is a finding. After determining that the ssl module is active, locate the Apache httpd.conf file. If unable to locate the file, perform a search of the system to find the location of the file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directives: SSLProtocol & SSLEngine Review the SSL sections of the httpd.conf file, all enabled SSLProtocol directives for Apache 2.2.22 and older must be set to “TLSv1”. Releases newer than Apache 2.2.22 must be set to "ALL -SSLv2 -SSLv3". If SSLProtocol is not set to the proper value, this is a finding. For all enabled SSLEngine directives ensure they are set to “on”. Both the SSLProtocol and SSLEngine directives must be set correctly or this is a finding. NOTE: In some cases web servers are configured in an environment to support load balancing. This configuration most likely utilizes a content switch to control traffic to the various web servers. In this situation, the TLS certificate for the web sites may be installed on the content switch versus the individual web sites. This solution is acceptable as long as the web servers are isolated from the general population LAN. We do not want users to have the ability to bypass the content switch to access the web sites.

## Group: WG610

**Group ID:** `V-15334`

### Rule: Web sites must utilize ports, protocols, and services according to PPSM guidelines.

**Rule ID:** `SV-34016r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Failure to comply with DoD ports, protocols, and services (PPS) requirements can result in compromise of enclave boundary protections and/or functionality of the automated information system (AIS). The IAM will ensure web servers are configured to use only authorized PPS in accordance with the Network Infrastructure STIG, DoD Instruction 8551.1, Ports, Protocols, and Services Management (PPSM), and the associated Ports, Protocols, and Services (PPS) Assurance Category Assignments List.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Information Assurance Officer</Responsibility><IAControls></IAControls>

**Check Text:**
Review the web site to determine if HTTP and HTTPs are used in accordance with well known ports (e.g., 80 and 443) or those ports and services as registered and approved for use by the DoD PPSM. Any variation in PPS will be documented, registered, and approved by the PPSM. If not, this is a finding.

## Group: WA00605

**Group ID:** `V-26279`

### Rule: Error logging must be enabled.

**Rule ID:** `SV-33147r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The server error logs are invaluable because they can also be used to identify potential problems and enable proactive remediation. Log data can reveal anomalous behavior such as “not found” or “unauthorized” errors that may be an evidence of attack attempts. Failure to enable error logging can significantly reduce the ability of Web Administrators to detect or remediate problems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. If unable to locate the file, perform a search of the system to find the location of the file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directives: ErrorLog This directive specifies the name and location of the error log, if not found, this is a finding. Note: This check is applicable to every host and virtual host the web server is supporting.

## Group: WA00612

**Group ID:** `V-26280`

### Rule: The sites error logs must log the correct format.

**Rule ID:** `SV-33149r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The server error logs are invaluable because they can also be used to identify potential problems and enable proactive remediation. Log data can reveal anomalous behavior such as “not found” or “unauthorized” errors that may be an evidence of attack attempts. Failure to enable error logging can significantly reduce the ability of Web Administrators to detect or remediate problems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. If unable to locate the file, perform a search of the system to find the location of the file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directive: LogFormat The minimum items to be logged are as shown in the sample below: LogFormat "%a %A %h %H %l %m %s %t %u %U \"%{Referer}i\"" combined Verify the information following the LogFormat directive meets or exceeds the minimum requirement above. If any LogFormat directive does not meet this requirement, this is a finding.

## Group: WA00615

**Group ID:** `V-26281`

### Rule: System logging must be enabled.

**Rule ID:** `SV-33151r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The server error logs are invaluable because they can also be used to identify potential problems and enable proactive remediation. Log data can reveal anomalous behavior such as “not found” or “unauthorized” errors that may be an evidence of attack attempts. Failure to enable error logging can significantly reduce the ability of Web Administrators to detect or remediate problems. The mod_log_config module provides for flexible logging of client requests. Logs are written in a customizable format, and may be written directly to a file, or to an external program. Conditional logging is provided so that individual requests may be included or excluded from the logs based on characteristics of the request. Three directives are provided by this module: TransferLog to create a log file, LogFormat to set a custom format, and CustomLog to define a log file and format in one step. The TransferLog and CustomLogdirectives can be used multiple times in each server to cause each request to be logged to multiple files. The server error log, whose name and location is set by the ErrorLog directive, is the most important log file. This is the place where Apache httpd will send diagnostic information and record any errors that it encounters in processing requests. It is the first place to look when a problem occurs with starting the server or with the operation of the server, since it will often contain details of what went wrong and how to fix it. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. If unable to locate the file, perform a search of the system to find the location of the file. Open the httpd.conf file with an editor such as Notepad, and search for the following uncommented directives: LoadModule log_config_module modules/mod_log_config.so If the LoadModule log_config_module directive is commented out or does not exist, this is a finding. Search for both of the following uncommented directives: ErrorLog and CustomLog. If no uncommented directives for both ErrorLog and CustomLog are found, this is a finding. Note: This check is applicable to every host and virtual host the web server is supporting.

## Group: WA00620

**Group ID:** `V-26282`

### Rule: The LogLevel directive must be enabled.

**Rule ID:** `SV-33153r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The server error logs are invaluable because they can also be used to identify potential problems and enable proactive remediation. Log data can reveal anomalous behavior such as “not found” or “unauthorized” errors that may be an evidence of attack attempts. Failure to enable error logging can significantly reduce the ability of Web Administrators to detect or remediate problems. While the ErrorLog directive configures the error log file name, the LogLevel directive is used to configure the severity level for the error logs. The log level values are the standard syslog levels: emerg, alert, crit, error, warn, notice, info and debug.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility>Web Administrator</Responsibility><IAControls></IAControls>

**Check Text:**
Locate the Apache httpd.conf file. If unable to locate the file, perform a search of the system to find the location of the file. Open the httpd.conf file with an editor such as notepad, and search for the following uncommented directives: LogLevel All enabled LogLevel directives should be set to a minimum of “warn”, if not, this is a finding. Note: If LogLevel is set to error, crit, alert, or emerg which are higher thresholds this is not a finding.

