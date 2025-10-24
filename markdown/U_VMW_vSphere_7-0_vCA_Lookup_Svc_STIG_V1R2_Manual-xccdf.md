# STIG Benchmark: VMware vSphere 7.0 vCenter Appliance Lookup Service Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-256706`

### Rule: Lookup Service must limit the amount of time that each Transport Control Protocol (TCP) connection is kept alive.

**Rule ID:** `SV-256706r888709_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Denial of service (DoS) is one threat against web servers. Many DoS attacks attempt to consume web server resources in such a way that no more resources are available to satisfy legitimate requests. In Tomcat, the "connectionTimeout" attribute sets the number of milliseconds the server will wait after accepting a connection for the request Uniform Resource Identifier (URI) line to be presented. This timeout will also be used when reading the request body (if any). This prevents idle sockets that are not sending HTTP requests from consuming system resources and potentially denying new connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/Server/Service/Connector[@port="${bio-custom.http.port}"]/@connectionTimeout' /usr/lib/vmware-lookupsvc/conf/server.xml Expected result: connectionTimeout="60000" If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-256707`

### Rule: Lookup Service must limit the number of concurrent connections permitted.

**Rule ID:** `SV-256707r888712_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Resource exhaustion can occur when an unlimited number of concurrent requests are allowed on a website, facilitating a denial-of-service attack. Unless the number of requests is controlled, the web server can consume enough system resources to cause a system crash. Mitigating this kind of attack will include limiting the number of concurrent HTTP/HTTPS requests. Each incoming request requires a thread for the duration of that request. If more simultaneous requests are received than can be handled by the currently available request processing threads, additional threads will be created up to the value of the "maxThreads" attribute.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/Server/Service/Connector[@port="${bio-custom.http.port}"]/@maxThreads' /usr/lib/vmware-lookupsvc/conf/server.xml Expected result: XPath set is empty If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-256708`

### Rule: Lookup Service must limit the maximum size of a POST request.

**Rule ID:** `SV-256708r888715_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "maxPostSize" value is the maximum size in bytes of the POST that will be handled by the container FORM URL parameter parsing. Limit its size to reduce exposure to a denial-of-service attack. If "maxPostSize" is not set, the default value of 2097152 (2MB) is used. Lookup Service is configured in its shipping state to not set a value for "maxPostSize".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/Server/Service/Connector[@port="${bio-custom.http.port}"]/@maxPostSize' /usr/lib/vmware-lookupsvc/conf/server.xml Expected result: XPath set is empty If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000001-WSR-000002

**Group ID:** `V-256709`

### Rule: Lookup Service must protect cookies from cross-site scripting (XSS).

**Rule ID:** `SV-256709r888718_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cookies are a common way to save session state over the HTTP(S) protocol. If an attacker can compromise session data stored in a cookie, they are better able to launch an attack against the server and its applications. When a cookie is tagged with the "HttpOnly" flag, it tells the browser that this particular cookie should only be accessed by the originating server. Any attempt to access the cookie from client script is strictly forbidden. Satisfies: SRG-APP-000001-WSR-000002, SRG-APP-000223-WSR-000011, SRG-APP-000439-WSR-000154</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-lookupsvc/conf/context.xml | xmllint --xpath '/Context/@useHttpOnly' - Expected result: useHttpOnly="true" If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000016-WSR-000005

**Group ID:** `V-256710`

### Rule: Lookup Service must record user access in a format that enables monitoring of remote access.

**Rule ID:** `SV-256710r888721_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access can be exploited by an attacker to compromise the server. By recording all remote access activities, it will be possible to determine the attacker's location, intent, and degree of success. Tomcat can be configured with an "AccessLogValve", a component that can be inserted into the request processing pipeline to provide robust access logging. The "AccessLogValve" creates log files in the same format as those created by standard web servers. When "AccessLogValve" is properly configured, log files will contain all the forensic information necessary in the case of a security incident. Satisfies: SRG-APP-000016-WSR-000005, SRG-APP-000093-WSR-000053, SRG-APP-000095-WSR-000056, SRG-APP-000096-WSR-000057, SRG-APP-000097-WSR-000058, SRG-APP-000098-WSR-000059, SRG-APP-000098-WSR-000060, SRG-APP-000099-WSR-000061, SRG-APP-000100-WSR-000064, SRG-APP-000375-WSR-000171, SRG-APP-000374-WSR-000172</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/Server/Service/Engine/Host/Valve[@className="org.apache.catalina.valves.AccessLogValve"]/@pattern' /usr/lib/vmware-lookupsvc/conf/server.xml Expected result: pattern="%t %I [RemoteIP] %{X-Forwarded-For}i %u [Request] %h:%{remote}p to local %{local}p - %H %m %U%q [Response] %s - %b bytes [Perf] process %Dms / commit %Fms / conn [%X]" If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000089-WSR-000047

**Group ID:** `V-256711`

### Rule: Lookup Service must generate log records for system startup and shutdown.

**Rule ID:** `SV-256711r888724_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Logging must be started as soon as possible when a service starts and when a service is stopped. Many forms of suspicious actions can be detected by analyzing logs for unexpected service starts and stops. Also, by starting to log immediately after a service starts, it becomes more difficult for suspicious activity to go unlogged. On the vCenter Server Appliance (VCSA), the "vmware-vmon" service starts up the Java virtual machines (JVMs) for various vCenter processes, including Lookup Service, and the individual json configuration files control the early JVM logging. Ensuring these json files are configured correctly enables early Java "stdout" and "stderr" logging. Satisfies: SRG-APP-000089-WSR-000047, SRG-APP-000092-WSR-000055</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # grep StreamRedirectFile /etc/vmware/vmware-vmon/svcCfgfiles/lookupsvc.json Expected result: "StreamRedirectFile": "%VMWARE_LOG_DIR%/vmware/lookupsvc/lookupsvc_stream.log", If no log file is specified for the "StreamRedirectFile" setting, this is a finding.

## Group: SRG-APP-000118-WSR-000068

**Group ID:** `V-256712`

### Rule: Lookup Service log files must only be accessible by privileged users.

**Rule ID:** `SV-256712r918958_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. If log data were to become compromised, competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could use to their advantage because each event record might contain communication ports, protocols, services, trust relationships, usernames, etc. The Lookup Service restricts all access to log files by default, but this configuration must be verified. Satisfies: SRG-APP-000118-WSR-000068, SRG-APP-000119-WSR-000069, SRG-APP-000120-WSR-000070</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # find /var/log/vmware/lookupsvc -xdev -type f ! -name lookupsvc-init.log -a '(' -perm -o+w -o -not -user lookupsvc -o -not -group lookupsvc ')' -exec ls -ld {} \; If any files are returned, this is a finding. Note: Prior to Update 3h, the user and group should be root.

## Group: SRG-APP-000131-WSR-000051

**Group ID:** `V-256713`

### Rule: Lookup Service application files must be verified for their integrity.

**Rule ID:** `SV-256713r888730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Verifying the Lookup Service application code is unchanged from its shipping state is essential for file validation and nonrepudiation of the Lookup Service. There is no reason the MD5 hash of the RPM original files should be changed after installation, excluding configuration files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # rpm -V vmware-lookupsvc|grep "^..5......"|grep -E "\.war|\.jar|\.sh|\.py" If there is any output, this is a finding.

## Group: SRG-APP-000131-WSR-000073

**Group ID:** `V-256714`

### Rule: Lookup Service must only run one webapp.

**Rule ID:** `SV-256714r888733_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>VMware ships Lookup Service on the vCenter Server Appliance (VCSA) with one webapp. Any other path is potentially malicious and must be removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # ls -A /usr/lib/vmware-lookupsvc/webapps/*.war Expected result: /usr/lib/vmware-lookupsvc/webapps/ROOT.war If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000141-WSR-000015

**Group ID:** `V-256715`

### Rule: Lookup Service must not be configured with the "UserDatabaseRealm" enabled.

**Rule ID:** `SV-256715r888736_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Lookup Service performs user authentication at the application level and not through Tomcat. By default, there is no configuration for the "UserDatabaseRealm" Tomcat authentication mechanism. As part of eliminating unnecessary features and to ensure the Lookup Service remains in its shipping state, the lack of a "UserDatabaseRealm" configuration must be confirmed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # grep UserDatabaseRealm /usr/lib/vmware-lookupsvc/conf/server.xml If the command produces any output, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-256716`

### Rule: Lookup Service must be configured to limit access to internal packages.

**Rule ID:** `SV-256716r888739_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "package.access" entry in the "catalina.properties" file implements access control at the package level. When properly configured, a Security Exception will be reported if an errant or malicious webapp attempts to access the listed internal classes directly or if a new class is defined under the protected packages. The Lookup Service comes preconfigured with the appropriate packages defined in "package.access", and this configuration must be maintained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # grep "package.access" /usr/lib/vmware-lookupsvc/conf/catalina.properties Expected result: package.access=sun.,org.apache.catalina.,org.apache.coyote.,org.apache.tomcat.,org.apache.jasper. If the output of the command does not match the expected result, this is a finding.

## Group: SRG-APP-000141-WSR-000081

**Group ID:** `V-256717`

### Rule: Lookup Service must have Multipurpose Internet Mail Extensions (MIMEs) that invoke operating system shell programs disabled.

**Rule ID:** `SV-256717r888742_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MIME mappings tell the Lookup Service what type of program various file types and extensions are and what external utilities or programs are needed to execute the file type. By ensuring that various shell script MIME types are not included in "web.xml", the server is protected against malicious users tricking the server into executing shell command files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # grep -En '(x-csh<)|(x-sh<)|(x-shar<)|(x-ksh<)' /usr/lib/vmware-lookupsvc/conf/web.xml If the command produces any output, this is a finding.

## Group: SRG-APP-000141-WSR-000083

**Group ID:** `V-256718`

### Rule: Lookup Service must have mappings set for Java servlet pages.

**Rule ID:** `SV-256718r888745_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Resource mapping is the process of tying a particular file type to a process in the web server that can serve that type of file to a requesting client and identify which file types are not to be delivered to a client. By not specifying which files can and cannot be served to a user, the web server could deliver to a user web server configuration files, log files, password files, etc. Because Tomcat is a Java-based web server, the main file extension used is *.jsp. This check ensures the *.jsp and *.jspx file types has been properly mapped to servlets.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-lookupsvc/conf/web.xml | sed 's/xmlns=".*"//g' | xmllint --xpath '/web-app/servlet-mapping/servlet-name[text()="jsp"]/parent::servlet-mapping' - Expected result: <servlet-mapping> <servlet-name>jsp</servlet-name> <url-pattern>*.jsp</url-pattern> <url-pattern>*.jspx</url-pattern> </servlet-mapping> If the .jsp and .jspx file url-patterns are not configured as in the expected result, this is a finding.

## Group: SRG-APP-000141-WSR-000085

**Group ID:** `V-256719`

### Rule: Lookup Service must not have the Web Distributed Authoring (WebDAV) servlet installed.

**Rule ID:** `SV-256719r888748_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>WebDAV is an extension to the HTTP protocol that, when developed, was meant to allow users to create, change, and move documents on a server, typically a web server or web share. WebDAV is not widely used and has serious security concerns because it may allow clients to modify unauthorized files on the web server and must therefore be disabled. Tomcat uses the "org.apache.catalina.servlets.WebdavServlet" servlet to provide WebDAV services. Because the WebDAV service has been found to have an excessive number of vulnerabilities, this servlet must not be installed. Lookup Service does not configure WebDAV by default.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # grep -n 'webdav' /usr/lib/vmware-lookupsvc/conf/web.xml If the command produces any output, this is a finding.

## Group: SRG-APP-000141-WSR-000086

**Group ID:** `V-256720`

### Rule: Lookup Service must be configured with memory leak protection.

**Rule ID:** `SV-256720r888751_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Java Runtime environment can cause a memory leak or lock files under certain conditions. Without memory leak protection, Lookup Service can continue to consume system resources, which will lead to "OutOfMemoryErrors" when reloading web applications. Memory leaks occur when JRE code uses the context class loader to load a singleton as this will cause a memory leak if a web application class loader happens to be the context class loader at the time. The "JreMemoryLeakPreventionListener" class is designed to initialize these singletons when Tomcat's common class loader is the context class loader. Proper use of JRE memory leak protection will ensure that the hosted application does not consume system resources and cause an unstable environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # grep JreMemoryLeakPreventionListener /usr/lib/vmware-lookupsvc/conf/server.xml Expected result: <Listener className="org.apache.catalina.core.JreMemoryLeakPreventionListener"/> If the output of the command does not match the expected result, this is a finding.

## Group: SRG-APP-000141-WSR-000087

**Group ID:** `V-256721`

### Rule: Lookup Service must not have any symbolic links in the web content directory tree.

**Rule ID:** `SV-256721r888754_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server is designed to deliver content and execute scripts or applications on the request of a client or user. Containing user requests to files in the directory tree of the hosted web application and limiting the execution of scripts and applications guarantees the user is not accessing information protected outside the application's realm. By checking that no symbolic links exist in the document root, the web server is protected from users jumping outside the hosted application directory tree and gaining access to the other directories, including the system root.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # find /usr/lib/vmware-vsphere-ui/server/static/ -type l -ls If the command produces any output, this is a finding.

## Group: SRG-APP-000211-WSR-000030

**Group ID:** `V-256722`

### Rule: Lookup Service directory tree must have permissions in an out-of-the-box state.

**Rule ID:** `SV-256722r888757_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>As a rule, accounts on a web server are to be kept to a minimum. Only administrators, web managers, developers, auditors, and web authors require accounts on the machine hosting the web server. The resources to which these accounts have access must also be closely monitored and controlled. Lookup Service files must be adequately protected with correct permissions as applied out of the box. Satisfies: SRG-APP-000211-WSR-000030, SRG-APP-000380-WSR-000072</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # find /usr/lib/vmware-lookupsvc/lib /usr/lib/vmware-lookupsvc/conf -xdev -type f -a '(' -perm -o+w -o -not -user root -o -not -group root ')' -exec ls -ld {} \; If the command produces any output, this is a finding.

## Group: SRG-APP-000225-WSR-000140

**Group ID:** `V-256723`

### Rule: Lookup Service must fail to a known safe state if system initialization fails, shutdown fails, or aborts fail.

**Rule ID:** `SV-256723r888760_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Determining a safe state for failure and weighing that against a potential denial of service for users depends on what type of application the web server is hosting. For the Lookup Service, it is preferable that the service abort startup on any initialization failure rather than continuing in a degraded, and potentially insecure, state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep EXIT_ON_INIT_FAILURE /usr/lib/vmware-lookupsvc/conf/catalina.properties Expected result: org.apache.catalina.startup.EXIT_ON_INIT_FAILURE=true If the output of the command does not match the expected result, this is a finding.

## Group: SRG-APP-000246-WSR-000149

**Group ID:** `V-256724`

### Rule: Lookup Service must limit the number of allowed connections.

**Rule ID:** `SV-256724r888763_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of established connections is a basic denial-of-service protection and a best practice. Servers where the limit is too high or unlimited could run out of system resources and negatively affect system availability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/Server/Service/Connector[@port="${bio-custom.http.port}"]/@acceptCount' /usr/lib/vmware-lookupsvc/conf/server.xml Expected result: acceptCount="100" If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000251-WSR-000157

**Group ID:** `V-256725`

### Rule: Lookup Service must set URIEncoding to UTF-8.

**Rule ID:** `SV-256725r888766_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into a hosted application's data entry field and the hosted application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. An attacker can also enter Unicode characters into hosted applications in an effort to break out of the document home or root home directory or to bypass security checks. Lookup Service must be configured to use a consistent character set via the "URIEncoding" attribute on the Connector nodes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/Server/Service/Connector[@port="${bio-custom.http.port}"]/@URIEncoding' /usr/lib/vmware-lookupsvc/conf/server.xml Expected result: URIEncoding="UTF-8" If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000266-WSR-000142

**Group ID:** `V-256726`

### Rule: Lookup Service must set the welcome-file node to a default web page.

**Rule ID:** `SV-256726r888769_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enumeration techniques, such as URL parameter manipulation, rely on being able to obtain information about the web server's directory structure by locating directories without default pages. In this scenario, the web server will display to the user a listing of the files in the directory being accessed. By having a default hosted application web page, the anonymous web user will not obtain directory browsing information or an error message that reveals the server type and version. Ensuring that every document directory has an "index.jsp" (or equivalent) file is one approach to mitigating the vulnerability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-lookupsvc/conf/web.xml | sed 's/xmlns=".*"//g' | xmllint --xpath '/web-app/welcome-file-list' - Expected result: <welcome-file-list> <welcome-file>index.html</welcome-file> <welcome-file>index.htm</welcome-file> <welcome-file>index.jsp</welcome-file> </welcome-file-list> If the output of the command does not match the expected result, this is a finding.

## Group: SRG-APP-000266-WSR-000142

**Group ID:** `V-256727`

### Rule: The Lookup Service must not show directory listings.

**Rule ID:** `SV-256727r888772_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enumeration techniques, such as URL parameter manipulation, rely on being able to obtain information about the web server's directory structure by locating directories without default pages. In this scenario, the web server will display to the user a listing of the files in the directory being accessed. Ensuring that directory listing is disabled is one approach to mitigating the vulnerability. In Tomcat, directory listing is disabled by default but can be enabled via the "listings" parameter. Ensure this node is not present to have the default effect.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-lookupsvc/conf/web.xml | sed 's/xmlns=".*"//g' | xmllint --xpath '//param-name[text()="listings"]/..' - Expected result: <init-param> <param-name>listings</param-name> <param-value>false</param-value> </init-param> If the output of the command does not match the expected result, this is a finding.

## Group: SRG-APP-000266-WSR-000159

**Group ID:** `V-256728`

### Rule: Lookup Service must be configured to hide the server version.

**Rule ID:** `SV-256728r888775_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web servers will often display error messages to client users, including enough information to aid in the debugging of the error. The information given back in error messages may display the web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage. This information could be used by an attacker to blueprint what type of attacks might be successful. Therefore, Lookup Service must be configured to hide the server version at all times.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/Server/Service/Connector[@port="${bio-custom.http.port}"]/@server' /usr/lib/vmware-lookupsvc/conf/server.xml Expected result: server="Anonymous" If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000266-WSR-000159

**Group ID:** `V-256729`

### Rule: Lookup Service must be configured to show error pages with minimal information.

**Rule ID:** `SV-256729r888778_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web servers will often display error messages to client users, including enough information to aid in the debugging of the error. The information given back in error messages may display the web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage. This information could be used by an attacker to blueprint what type of attacks might be successful. Therefore, the Lookup Service must be configured with a catchall error handler that redirects to a standard "error.jsp".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/Server/Service/Engine/Host/Valve[@className="org.apache.catalina.valves.ErrorReportValve"]' /usr/lib/vmware-lookupsvc/conf/server.xml Expected result: <Valve className="org.apache.catalina.valves.ErrorReportValve" showServerInfo="false" showReport="false"/> If the output of the command does not match the expected result, this is a finding.

## Group: SRG-APP-000266-WSR-000160

**Group ID:** `V-256730`

### Rule: Lookup Service must not enable support for TRACE requests.

**Rule ID:** `SV-256730r888781_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>"TRACE" is a technique for a user to request internal information about Tomcat. This is useful during product development but should not be enabled in production. Allowing an attacker to conduct a TRACE operation against the service will expose information that would be useful to perform a more targeted attack. Lookup Service provides the "allowTrace" parameter as means to disable responding to TRACE requests.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # grep allowTrace /usr/lib/vmware-lookupsvc/conf/server.xml If "allowTrace" is set to "true", this is a finding. If no line is returned, this is not a finding.

## Group: SRG-APP-000266-WSR-000160

**Group ID:** `V-256731`

### Rule: Lookup Service must have the debug option turned off.

**Rule ID:** `SV-256731r888784_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information needed by an attacker to begin looking for possible vulnerabilities in a web server includes any information about the web server and plug-ins or modules being used. When debugging or trace information is enabled in a production web server, information about the web server, such as web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage may be displayed. Because this information may be placed in logs and general messages during normal operation of the web server, an attacker does not need to cause an error condition to gain this information. Lookup Service can be configured to set the debugging level. By setting the debugging level to zero (0), no debugging information will be provided to a malicious user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-lookupsvc/conf/web.xml | sed 's/xmlns=".*"//g' | xmllint --xpath '//param-name[text()="debug"]/..' - Expected result: <init-param> <param-name>debug</param-name> <param-value>0</param-value> </init-param> If the output of the command does not match the expected result, this is a finding.

## Group: SRG-APP-000357-WSR-000150

**Group ID:** `V-256732`

### Rule: Lookup Service must use a logging mechanism that is configured to allocate log record storage capacity large enough to accommodate the logging requirements of the web server.

**Rule ID:** `SV-256732r888787_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure the logging mechanism used by the web server has sufficient storage capacity in which to write the logs, the logging mechanism must be able to allocate log record storage capacity. Lookup Service configures log sizes and rotation appropriately as part of its installation routine. Verifying the logging configuration file (logging.properties) has not been modified is sufficient to determine if the logging configuration has been modified from the default.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # rpm -V vmware-lookupsvc|grep logging.properties|grep "^..5......" If the above command returns any output, this is a finding.

## Group: SRG-APP-000358-WSR-000163

**Group ID:** `V-256733`

### Rule: Lookup Service log files must be offloaded to a central log server in real time.

**Rule ID:** `SV-256733r888790_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Lookup Service produces several logs that must be offloaded from the originating system. This information can then be used for diagnostic, forensics, or other purposes relevant to ensuring the availability and integrity of the hosted application. Satisfies: SRG-APP-000358-WSR-000163, SRG-APP-000108-WSR-000166, SRG-APP-000125-WSR-000071</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # rpm -V VMware-visl-integration|grep vmware-services-lookupsvc.conf If the above command returns any output, this is a finding.

## Group: SRG-APP-000383-WSR-000175

**Group ID:** `V-256734`

### Rule: Lookup Service must be configured with the appropriate ports.

**Rule ID:** `SV-256734r888793_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web servers provide numerous processes, features, and functionalities that use TCP/IP ports. Some of these processes may be deemed unnecessary or too unsecure to run on a production system. The ports that Lookup Service listens on are configured in the "catalina.properties" file and must be verified as accurate to their shipping state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # grep '\.port' /usr/lib/vmware-lookupsvc/conf/catalina.properties Expected result: base.shutdown.port=-1 base.jmx.port=-1 bio-custom.http.port=7090 bio-custom.https.port=8443 If the output of the command does not match the expected result, this is a finding.

## Group: SRG-APP-000435-WSR-000147

**Group ID:** `V-256735`

### Rule: Lookup Service must disable the shutdown port.

**Rule ID:** `SV-256735r888796_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An attacker has at least two reasons to stop a web server. The first is to cause a denial of service, and the second is to put in place changes the attacker made to the web server configuration. If the Tomcat shutdown port feature is enabled, a shutdown signal can be sent to the Lookup Service through this port. To ensure availability, the shutdown port must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following commands: # xmllint --xpath '/Server/@port' /usr/lib/vmware-lookupsvc/conf/server.xml Expected result: port="${base.shutdown.port}" If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000439-WSR-000155

**Group ID:** `V-256736`

### Rule: Lookup Service must set the secure flag for cookies.

**Rule ID:** `SV-256736r888799_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The secure flag is an option that can be set by the application server when sending a new cookie to the user within an HTTP Response. The purpose of the secure flag is to prevent cookies from being observed by unauthorized parties due to the transmission of the cookie in clear text. By setting the secure flag, the browser will prevent the transmission of a cookie over an unencrypted channel. Lookup Service is configured to only be accessible over a Transport Layer Security (TLS) tunnel, but this cookie flag is still a recommended best practice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-lookupsvc/conf/web.xml | sed 's/xmlns=".*"//g' | xmllint --xpath '/web-app/session-config/cookie-config/secure' - Expected result: <secure>true</secure> If the output of the command does not match the expected result, this is a finding.

