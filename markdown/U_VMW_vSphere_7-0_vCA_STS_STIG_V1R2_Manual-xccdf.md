# STIG Benchmark: VMware vSphere 7.0 vCenter Appliance STS Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-256745`

### Rule: The Security Token Service must limit the amount of time that each Transmission Control Protocol (TCP) connection is kept alive.

**Rule ID:** `SV-256745r889205_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Denial of service (DoS) is one threat against web servers. Many DoS attacks attempt to consume web server resources in such a way that no more resources are available to satisfy legitimate requests. In Tomcat, the "connectionTimeout" attribute sets the number of milliseconds the server will wait after accepting a connection for the requested Uniform Resource Identifier (URI) line to be presented. This timeout will also be used when reading the request body (if any). This prevents idle sockets that are not sending HTTP requests from consuming system resources and potentially denying new connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/Server/Service/Connector[@port="${bio-custom.http.port}"]/@connectionTimeout' /usr/lib/vmware-sso/vmware-sts/conf/server.xml Expected result: connectionTimeout="60000" If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-256746`

### Rule: The Security Token Service must limit the number of concurrent connections permitted.

**Rule ID:** `SV-256746r889208_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Resource exhaustion can occur when an unlimited number of concurrent requests are allowed on a website, facilitating a denial-of-service attack. Unless the number of requests is controlled, the web server can consume enough system resources to cause a system crash. Mitigating this kind of attack will include limiting the number of concurrent HTTP/HTTPS requests. In Tomcat, each incoming request requires a thread for the duration of that request. If more simultaneous requests are received than can be handled by the currently available request processing threads, additional threads will be created up to the value of the "maxThreads" attribute.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/Server/Service/Executor[@name="tomcatThreadPool"]/@maxThreads' /usr/lib/vmware-sso/vmware-sts/conf/server.xml Expected result: maxThreads="150" If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-256747`

### Rule: The Security Token Service must limit the maximum size of a POST request.

**Rule ID:** `SV-256747r889211_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "maxPostSize" value is the maximum size in bytes of the POST that will be handled by the container FORM URL parameter parsing. Limit its size to reduce exposure to a denial-of-service (DoS) attack. If "maxPostSize" is not set, the default value of 2097152 (2MB) is used. Security Token Service is configured in its shipping state to not set a value for "maxPostSize".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/Server/Service/Connector[@port="${bio-custom.http.port}"]/@maxPostSize' /usr/lib/vmware-sso/vmware-sts/conf/server.xml Expected result: XPath set is empty If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000001-WSR-000002

**Group ID:** `V-256748`

### Rule: The Security Token Service must protect cookies from cross-site scripting (XSS).

**Rule ID:** `SV-256748r889214_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cookies are a common way to save session state over the HTTP(S) protocol. If an attacker can compromise session data stored in a cookie, they are better able to launch an attack against the server and its applications. When a cookie is tagged with the "HttpOnly" flag, it tells the browser that this particular cookie should only be accessed by the originating server. Any attempt to access the cookie from client script is strictly forbidden. Satisfies: SRG-APP-000001-WSR-000002, SRG-APP-000223-WSR-000011, SRG-APP-000439-WSR-000154</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-sso/vmware-sts/conf/web.xml | sed '2 s/xmlns=".*"//g' | xmllint --xpath '/web-app/session-config/cookie-config/http-only' - Expected result: <http-only>true</http-only> If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000016-WSR-000005

**Group ID:** `V-256749`

### Rule: The Security Token Service must record user access in a format that enables monitoring of remote access.

**Rule ID:** `SV-256749r889217_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access can be exploited by an attacker to compromise the server. By recording all remote access activities, it will be possible to determine the attacker's location, intent, and degree of success. Tomcat can be configured with an "AccessLogValve", a component that can be inserted into the request processing pipeline to provide robust access logging. The "AccessLogValve" creates log files in the same format as those created by standard web servers. When "AccessLogValve" is properly configured, log files will contain all the forensic information necessary in the case of a security incident. Satisfies: SRG-APP-000016-WSR-000005, SRG-APP-000093-WSR-000053, SRG-APP-000095-WSR-000056, SRG-APP-000096-WSR-000057, SRG-APP-000097-WSR-000058, SRG-APP-000098-WSR-000059, SRG-APP-000098-WSR-000060, SRG-APP-000099-WSR-000061, SRG-APP-000100-WSR-000064, SRG-APP-000374-WSR-000172, SRG-APP-000375-WSR-000171</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-sso/vmware-sts/conf/server.xml | sed '2 s/xmlns=".*"//g' | xmllint --xpath '/Server/Service/Engine/Host/Valve[@className="org.apache.catalina.valves.AccessLogValve"]/@pattern' - Expected result: pattern="%t %I [RemoteIP] %{X-Forwarded-For}i %u [Request] %h:%{remote}p to local %{local}p - %H %m %U%q [Response] %s - %b bytes [Perf] process %Dms / commit %Fms / conn [%X]" If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000089-WSR-000047

**Group ID:** `V-256750`

### Rule: The Security Token Service must generate log records during Java startup and shutdown.

**Rule ID:** `SV-256750r918974_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Logging must be started as soon as possible when a service starts and as late as possible when a service is stopped. Many forms of suspicious actions can be detected by analyzing logs for unexpected service starts and stops. Also, by starting to log immediately after a service starts, it becomes more difficult for suspicious activity to go unlogged. Satisfies: SRG-APP-000089-WSR-000047, SRG-APP-000092-WSR-000055</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # grep "1catalina.org.apache.juli.FileHandler" /usr/lib/vmware-sso/vmware-sts/conf/logging.properties Expected result: handlers = 1catalina.org.apache.juli.FileHandler, 2localhost.org.apache.juli.FileHandler, 3manager.org.apache.juli.FileHandler, 4host-manager.org.apache.juli.FileHandler .handlers = 1catalina.org.apache.juli.FileHandler 1catalina.org.apache.juli.FileHandler.level = FINE 1catalina.org.apache.juli.FileHandler.directory = ${catalina.base}/logs/tomcat 1catalina.org.apache.juli.FileHandler.prefix = catalina. 1catalina.org.apache.juli.FileHandler.bufferSize = -1 1catalina.org.apache.juli.FileHandler.formatter = java.util.logging.SimpleFormatter 1catalina.org.apache.juli.FileHandler.maxDays = 10 org.apache.catalina.startup.Catalina.handlers = 1catalina.org.apache.juli.FileHandler If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000119-WSR-000069

**Group ID:** `V-256751`

### Rule: Security Token Service log files must only be modifiable by privileged users.

**Rule ID:** `SV-256751r889223_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. The accuracy of the information is always pertinent. One of the first steps an attacker will undertake is the modification or deletion of log records to cover tracks and prolong discovery. The web server must protect the log data from unauthorized modification. Security Token Service restricts all modification of log files by default, but this configuration must be verified. Satisfies: SRG-APP-000119-WSR-000069, SRG-APP-000120-WSR-000070</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # find /storage/log/vmware/sso/ -xdev -type f -a '(' -perm -o+w -o -not -user root -o -not -group root ')' -exec ls -ld {} \; If any files are returned, this is a finding.

## Group: SRG-APP-000131-WSR-000051

**Group ID:** `V-256752`

### Rule: The Security Token Service application files must be verified for their integrity.

**Rule ID:** `SV-256752r889226_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Verifying the Security Token Service application code is unchanged from its shipping state is essential for file validation and nonrepudiation of the Security Token Service. There is no reason the MD5 hash of the RPM original files should be changed after installation, excluding configuration files. Satisfies: SRG-APP-000131-WSR-000051, SRG-APP-000357-WSR-000150</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # rpm -V vmware-identity-sts|grep "^..5......"|grep -v -E "\.properties|\.xml|\.conf" If there is any output, this is a finding.

## Group: SRG-APP-000131-WSR-000073

**Group ID:** `V-256753`

### Rule: The Security Token Service must only run one webapp.

**Rule ID:** `SV-256753r889229_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>VMware ships the Security Token Service on the vCenter Server Appliance (VCSA) with one webapp, in "ROOT.war". Any other ".war" file is potentially malicious and must be removed. Satisfies: SRG-APP-000131-WSR-000073, SRG-APP-000141-WSR-000075</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # ls /usr/lib/vmware-sso/vmware-sts/webapps/*.war Expected result: /usr/lib/vmware-sso/vmware-sts/webapps/ROOT.war If the result of this command does not match the expected result, this is a finding.

## Group: SRG-APP-000141-WSR-000015

**Group ID:** `V-256754`

### Rule: The Security Token Service must not be configured with unused realms.

**Rule ID:** `SV-256754r889232_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Security Token Service performs user authentication at the application level and not through Tomcat. To eliminate unnecessary features and ensure the Security Token Service remains in its shipping state, the lack of a "UserDatabaseRealm" configuration must be confirmed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # grep UserDatabaseRealm /usr/lib/vmware-sso/vmware-sts/conf/server.xml If the command produces any output, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-256755`

### Rule: The Security Token Service must be configured to limit access to internal packages.

**Rule ID:** `SV-256755r889235_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "package.access" entry in the "catalina.properties" file implements access control at the package level. When properly configured, a Security Exception will be reported if an errant or malicious webapp attempts to access the listed internal classes directly or if a new class is defined under the protected packages. The Security Token Service comes preconfigured with the appropriate packages defined in "package.access", and this configuration must be maintained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # grep "package.access" /usr/lib/vmware-sso/vmware-sts/conf/catalina.properties Expected result: package.access=sun.,org.apache.catalina.,org.apache.coyote.,org.apache.tomcat.,org.apache.jasper. If the output of the command does not match the expected result, this is a finding.

## Group: SRG-APP-000141-WSR-000081

**Group ID:** `V-256756`

### Rule: The Security Token Service must have Multipurpose Internet Mail Extensions (MIME) that invoke operating system shell programs disabled.

**Rule ID:** `SV-256756r889238_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MIME mappings tell the Security Token Service what type of program various file types and extensions are and what external utilities or programs are needed to execute the file type. By ensuring various shell script MIME types are not included in "web.xml", the server is protected against malicious users tricking the server into executing shell command files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # grep -En '(x-csh<)|(x-sh<)|(x-shar<)|(x-ksh<)' /usr/lib/vmware-sso/vmware-sts/conf/web.xml If the command produces any output, this is a finding.

## Group: SRG-APP-000141-WSR-000083

**Group ID:** `V-256757`

### Rule: The Security Token Service must have mappings set for Java servlet pages.

**Rule ID:** `SV-256757r889241_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Resource mapping is the process of tying a particular file type to a process in the web server that can serve that type of file to a requesting client and identify which file types are not to be delivered to a client. By not specifying which files can and cannot be served to a user, the web server could deliver to a user web server configuration files, log files, password files, etc. As Tomcat is a Java-based web server, the main file extension used is *.jsp. This check ensures the *.jsp and *.jspx file types have been properly mapped to servlets.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-sso/vmware-sts/conf/web.xml | sed '2 s/xmlns=".*"//g' | xmllint --xpath '/web-app/servlet-mapping/servlet-name[text()="jsp"]/parent::servlet-mapping' - Expected result: <servlet-mapping> <servlet-name>jsp</servlet-name> <url-pattern>*.jsp</url-pattern> <url-pattern>*.jspx</url-pattern> </servlet-mapping> If the output of the command does not match the expected result, this is a finding.

## Group: SRG-APP-000141-WSR-000085

**Group ID:** `V-256758`

### Rule: The Security Token Service must not have the Web Distributed Authoring (WebDAV) servlet installed.

**Rule ID:** `SV-256758r889244_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>WebDAV is an extension to the HTTP protocol that, when developed, was meant to allow users to create, change, and move documents on a server, typically a web server or web share. WebDAV is not widely used and has serious security concerns because it may allow clients to modify unauthorized files on the web server and must therefore be disabled. Tomcat uses the "org.apache.catalina.servlets.WebdavServlet" servlet to provide WebDAV services. Because the WebDAV service has been found to have an excessive number of vulnerabilities, this servlet must not be installed. The Security Token Service does not configure WebDAV by default.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # grep -n 'webdav' /usr/lib/vmware-sso/vmware-sts/conf/web.xml If the command produces any output, this is a finding.

## Group: SRG-APP-000141-WSR-000086

**Group ID:** `V-256759`

### Rule: The Security Token Service must be configured with memory leak protection.

**Rule ID:** `SV-256759r889247_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Java Runtime environment can cause a memory leak or lock files under certain conditions. Without memory leak protection, the Security Token Service can continue to consume system resources which will lead to "OutOfMemoryErrors" when reloading web applications. Memory leaks occur when JRE code uses the context class loader to load a singleton. This this will cause a memory leak if a web application class loader happens to be the context class loader at the time. The "JreMemoryLeakPreventionListener" class is designed to initialize these singletons when Tomcat's common class loader is the context class loader. Proper use of JRE memory leak protection will ensure the hosted application does not consume system resources and cause an unstable environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # grep JreMemoryLeakPreventionListener /usr/lib/vmware-sso/vmware-sts/conf/server.xml Expected result: <Listener className="org.apache.catalina.core.JreMemoryLeakPreventionListener"/> If the output of the command does not match the expected result, this is a finding.

## Group: SRG-APP-000141-WSR-000087

**Group ID:** `V-256760`

### Rule: The Security Token Service must not have any symbolic links in the web content directory tree.

**Rule ID:** `SV-256760r889250_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server is designed to deliver content and execute scripts or applications on the request of a client or user. Containing user requests to files in the directory tree of the hosted web application and limiting the execution of scripts and applications guarantees the user is not accessing information protected outside the application's realm. By checking that no symbolic links exist in the document root, the web server is protected from users jumping outside the hosted application directory tree and gaining access to the other directories, including the system root.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # find /usr/lib/vmware-sso/vmware-sts/webapps/ -type l -ls If the command produces any output, this is a finding.

## Group: SRG-APP-000211-WSR-000030

**Group ID:** `V-256761`

### Rule: The Security Token Service directory tree must have permissions in an out-of-the-box state.

**Rule ID:** `SV-256761r889253_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>As a rule, accounts on a web server are to be kept to a minimum. Only administrators, web managers, developers, auditors, and web authors require accounts on the machine hosting the web server. The resources to which these accounts have access must also be closely monitored and controlled. The Security Token Service files must be adequately protected with correct permissions as applied out of the box. Satisfies: SRG-APP-000211-WSR-000030, SRG-APP-000380-WSR-000072</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # find /usr/lib/vmware-sso/vmware-sts/ -xdev -type f -a '(' -not -user root -o -not -group root ')' -exec ls -ld {} \; If the command produces any output, this is a finding.

## Group: SRG-APP-000225-WSR-000140

**Group ID:** `V-256762`

### Rule: The Security Token Service must fail to a known safe state if system initialization fails, shutdown fails, or aborts fail.

**Rule ID:** `SV-256762r889256_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Determining a safe state for failure and weighing that against a potential denial of service for users depends on what type of application the web server is hosting. For the Security Token Service, it is preferable that the service abort startup on any initialization failure rather than continuing in a degraded, and potentially insecure, state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep EXIT_ON_INIT_FAILURE /usr/lib/vmware-sso/vmware-sts/conf/catalina.properties Expected result: org.apache.catalina.startup.EXIT_ON_INIT_FAILURE=true If the output of the command does not match the expected result, this is a finding.

## Group: SRG-APP-000246-WSR-000149

**Group ID:** `V-256763`

### Rule: The Security Token Service must limit the number of allowed connections.

**Rule ID:** `SV-256763r889259_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of established connections to the Security Token Service is a basic denial-of-service protection. Servers where the limit is too high or unlimited can potentially run out of system resources and negatively affect system availability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/Server/Service/Connector[@port="${bio-custom.http.port}"]/@acceptCount' /usr/lib/vmware-sso/vmware-sts/conf/server.xml Expected result: acceptCount="100" If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000251-WSR-000157

**Group ID:** `V-256764`

### Rule: The Security Token Service must set "URIEncoding" to UTF-8.

**Rule ID:** `SV-256764r889262_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into a hosted application's data entry field and the hosted application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. An attacker can also enter Unicode characters into hosted applications in an effort to break out of the document home or root home directory or bypass security checks. The Security Token Service must be configured to use a consistent character set via the "URIEncoding" attribute on the Connector nodes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/Server/Service/Connector[@port="${bio-custom.http.port}"]/@URIEncoding' /usr/lib/vmware-sso/vmware-sts/conf/server.xml Expected result: URIEncoding="UTF-8" If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000251-WSR-000157

**Group ID:** `V-256765`

### Rule: The Security Token Service must use the "setCharacterEncodingFilter" filter.

**Rule ID:** `SV-256765r889265_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into a hosted application's data entry field and the hosted application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. An attacker can also enter Unicode characters into hosted applications in an effort to break out of the document home or root home directory or to bypass security checks. VMware uses the standard Tomcat "SetCharacterEncodingFilter" to provide a layer of defense against character encoding attacks. Filters are Java objects that perform filtering tasks on the request to a resource (a servlet or static content), on the response from a resource, or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-sso/vmware-sts/conf/web.xml | sed '2 s/xmlns=".*"//g' | xmllint --xpath '/web-app/filter-mapping/filter-name[text()="setCharacterEncodingFilter"]/parent::filter-mapping' - Expected result: <filter-mapping> <filter-name>setCharacterEncodingFilter</filter-name> <url-pattern>/*</url-pattern> </filter-mapping> If the output is does not match the expected result, this is a finding. At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-sso/vmware-sts/conf/web.xml | sed '2 s/xmlns=".*"//g' | xmllint --xpath '/web-app/filter/filter-name[text()="setCharacterEncodingFilter"]/parent::filter' - Expected result: <filter> <filter-name>setCharacterEncodingFilter</filter-name> <filter-class> org.apache.catalina.filters.SetCharacterEncodingFilter </filter-class> <init-param> <param-name>encoding</param-name> <param-value>UTF-8</param-value> </init-param> <init-param> <param-name>ignore</param-name> <param-value>true</param-value> </init-param> <async-supported>true</async-supported> </filter> If the output is does not match the expected result, this is a finding.

## Group: SRG-APP-000266-WSR-000142

**Group ID:** `V-256766`

### Rule: The Security Token Service must set the welcome-file node to a default web page.

**Rule ID:** `SV-256766r889268_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enumeration techniques, such as Uniform Resource Locator (URL) parameter manipulation, rely on being able to obtain information about the web server's directory structure by locating directories without default pages. In this scenario, the web server will display to the user a listing of the files in the directory being accessed. By having a default hosted application web page, the anonymous web user will not obtain directory browsing information or an error message that reveals the server type and version. Ensuring every document directory has an "index.jsp" (or equivalent) file is one approach to mitigating the vulnerability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-sso/vmware-sts/conf/web.xml | sed '2 s/xmlns=".*"//g' | xmllint --xpath '/web-app/welcome-file-list' - Expected result: <welcome-file-list> <welcome-file>index.html</welcome-file> <welcome-file>index.htm</welcome-file> <welcome-file>index.jsp</welcome-file> </welcome-file-list> If the output of the command does not match the expected result, this is a finding.

## Group: SRG-APP-000266-WSR-000142

**Group ID:** `V-256767`

### Rule: The Security Token Service must not show directory listings.

**Rule ID:** `SV-256767r889271_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enumeration techniques, such as Uniform Resource Locator (URL) parameter manipulation, rely on being able to obtain information about the web server's directory structure by locating directories without default pages. In this scenario, the web server will display to the user a listing of the files in the directory being accessed. Ensuring directory listing is disabled is one approach to mitigating the vulnerability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-sso/vmware-sts/conf/web.xml | sed '2 s/xmlns=".*"//g' | xmllint --xpath '//param-name[text()="listings"]/parent::init-param' - Expected result: <init-param> <param-name>listings</param-name> <param-value>false</param-value> </init-param> If the output of the command does not match the expected result, this is a finding.

## Group: SRG-APP-000266-WSR-000159

**Group ID:** `V-256768`

### Rule: The Security Token Service must be configured to not show error reports.

**Rule ID:** `SV-256768r889274_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web servers will often display error messages to client users, displaying enough information to aid in the debugging of the error. The information given back in error messages may display the web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage. This information could be used by an attacker to blueprint what type of attacks might be successful. Therefore, the Security Token Service must be configured to not show server version information in error messages.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/Server/Service/Engine/Host/Valve[@className="org.apache.catalina.valves.ErrorReportValve"]' /usr/lib/vmware-sso/vmware-sts/conf/server.xml Expected result: <Valve className="org.apache.catalina.valves.ErrorReportValve" showReport="false" showServerInfo="false"/> If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000266-WSR-000160

**Group ID:** `V-256769`

### Rule: The Security Token Service must not enable support for TRACE requests.

**Rule ID:** `SV-256769r889277_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>"TRACE" is a technique for a user to request internal information about Tomcat. This is useful during product development but should not be enabled in production. Allowing an attacker to conduct a TRACE operation against the Security Token Service will expose information that would be useful to perform a more targeted attack. The Security Token Service provides the "allowTrace" parameter as means to disable responding to TRACE requests.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # grep allowTrace /usr/lib/vmware-sso/vmware-sts/conf/server.xml If "allowTrace" is set to "true", this is a finding. If no line is returned, this is not a finding.

## Group: SRG-APP-000266-WSR-000160

**Group ID:** `V-256770`

### Rule: The Security Token Service must have the debug option disabled.

**Rule ID:** `SV-256770r918976_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information needed by an attacker to begin looking for possible vulnerabilities in a web server includes any information about the web server and plug-ins or modules being used. When debugging or trace information is enabled in a production web server, information about the web server, such as web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage may be displayed. Because this information may be placed in logs and general messages during normal operation of the web server, an attacker does not need to cause an error condition to gain this information. The Security Token Service can be configured to set the debugging level. By setting the debugging level to zero, no debugging information will be provided to a malicious user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-sso/vmware-sts/conf/web.xml | sed '2 s/xmlns=".*"//g' | xmllint --xpath '//param-name[text()="debug"]/parent::init-param' - Expected result: <init-param> <param-name>debug</param-name> <param-value>0</param-value> </init-param> If the output of the command does not match the expected result, this is a finding. If no lines are returned, this is not a finding.

## Group: SRG-APP-000383-WSR-000175

**Group ID:** `V-256771`

### Rule: The Security Token Service must be configured with the appropriate ports.

**Rule ID:** `SV-256771r918979_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web servers provide numerous processes, features, and functionalities that use TCP/IP ports. Some of these processes may be deemed unnecessary or too unsecure to run on a production system. The ports that the Security Token Service listens on are configured in the "catalina.properties" file and must be verified as accurate to their shipping state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # grep 'bio' /usr/lib/vmware-sso/vmware-sts/conf/catalina.properties Expected result: bio-custom.http.port=7080 bio-custom.https.port=8443 bio-ssl-clientauth.https.port=3128 bio-ssl-localhost.https.port=7444 If the output of the command does not match the expected result, this is a finding. Note: Port 3128 will not be shown in the output prior to 7.0 U3i.

## Group: SRG-APP-000435-WSR-000147

**Group ID:** `V-256772`

### Rule: The Security Token Service must disable the shutdown port.

**Rule ID:** `SV-256772r889286_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An attacker has at least two reasons to stop a web server. The first is to cause a denial of service, and the second is to put in place changes the attacker made to the web server configuration. If the Tomcat shutdown port feature is enabled, a shutdown signal can be sent to the Security Token Service through this port. To ensure availability, the shutdown port must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # grep 'base.shutdown.port' /usr/lib/vmware-sso/vmware-sts/conf/catalina.properties Expected result: base.shutdown.port=-1 If the output of the command does not match the expected result, this is a finding.

## Group: SRG-APP-000439-WSR-000155

**Group ID:** `V-256773`

### Rule: The Security Token Service must set the secure flag for cookies.

**Rule ID:** `SV-256773r889289_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The secure flag is an option that can be set by the application server when sending a new cookie to the user within an HTTP Response. The purpose of the secure flag is to prevent cookies from being observed by unauthorized parties due to the transmission of the cookie in clear text. By setting the secure flag, the browser will prevent the transmission of a cookie over an unencrypted channel. The Security Token Service is configured to only be accessible over a Transport Layer Security (TLS) tunnel, but this cookie flag is still a recommended best practice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-sso/vmware-sts/conf/web.xml | sed '2 s/xmlns=".*"//g' | xmllint --xpath '/web-app/session-config/cookie-config/secure' - Expected result: <secure>true</secure> If the output of the command does not match the expected result, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-256774`

### Rule: The Security Token Service default servlet must be set to "readonly".

**Rule ID:** `SV-256774r889292_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The default servlet (or DefaultServlet) is a special servlet provided with Tomcat that is called when no other suitable page is found in a particular folder. The DefaultServlet serves static resources as well as directory listings. The DefaultServlet is configured by default with the "readonly" parameter set to "true" where HTTP commands such as PUT and DELETE are rejected. Changing this to "false" allows clients to delete or modify static resources on the server and to upload new resources. DefaultServlet readonly must be set to "true", either literally or by absence (default).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-sso/vmware-sts/conf/web.xml | sed '2 s/xmlns=".*"//g' | xmllint --xpath '/web-app/servlet/servlet-name[text()="default"]/../init-param/param-name[text()="readonly"]/../param-value[text()="false"]' - Expected result: XPath set is empty If the output of the command does not match the expected result, this is a finding.

## Group: SRG-APP-000125-WSR-000071

**Group ID:** `V-256775`

### Rule: Security Token Service log data and records must be backed up onto a different system or media.

**Rule ID:** `SV-256775r889295_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of Security Token Service log data includes ensuring log data is not accidentally lost or deleted. Backing up Security Token Service log records to an unrelated system or onto separate media than the system the web server is running on helps to ensure that, in the event of a catastrophic system failure, the log records will be retained. Satisfies: SRG-APP-000125-WSR-000071, SRG-APP-000358-WSR-000163</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # rpm -V VMware-visl-integration|grep vmware-services-sso-services.conf|grep "^..5......" If the command returns any output, this is a finding.

