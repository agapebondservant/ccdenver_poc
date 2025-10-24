# STIG Benchmark: VMware vSphere 8.0 vCenter Appliance Perfcharts Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-AS-000001

**Group ID:** `V-259071`

### Rule: The vCenter Perfcharts service must limit the number of maximum concurrent connections permitted.

**Rule ID:** `SV-259071r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Resource exhaustion can occur when an unlimited number of concurrent requests are allowed on a website, facilitating a denial-of-service attack. Unless the number of requests is controlled, the web server can consume enough system resources to cause a system crash. Mitigating this kind of attack will include limiting the number of concurrent HTTP/HTTPS requests. In Tomcat, each incoming request requires a thread for the duration of that request. If more simultaneous requests are received than can be handled by the currently available request processing threads, additional threads will be created up to the value of the maxThreads attribute. Satisfies: SRG-APP-000001-AS-000001, SRG-APP-000435-AS-000163</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/Server/Service/Executor[@name="tomcatThreadPool"]/@maxThreads' /usr/lib/vmware-perfcharts/tc-instance/conf/server.xml Expected result: maxThreads="300" If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000033-AS-000024

**Group ID:** `V-259072`

### Rule: The vCenter Perfcharts service cookies must have secure flag set.

**Rule ID:** `SV-259072r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The secure flag is an option that can be set by the application server when sending a new cookie to the user within an HTTP Response. The purpose of the secure flag is to prevent cookies from being observed by unauthorized parties due to the transmission of a cookie in clear text. By setting the secure flag, the browser will prevent the transmission of a cookie over an unencrypted channel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-perfcharts/tc-instance/webapps/statsreport/WEB-INF/web.xml | sed 's/xmlns=".*"//g' | xmllint --xpath '/web-app/session-config/cookie-config/secure' - Expected result: <secure>true</secure> If the output of the command does not match the expected result, this is a finding.

## Group: SRG-APP-000092-AS-000053

**Group ID:** `V-259073`

### Rule: The vCenter Perfcharts service must initiate session logging upon startup.

**Rule ID:** `SV-259073r960888_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Logging must be started as soon as possible when a service starts and as late as possible when a service is stopped. Many forms of suspicious actions can be detected by analyzing logs for unexpected service starts and stops. Also, by starting to log immediately after a service starts, it becomes more difficult for suspicious activity to go unlogged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # grep StreamRedirectFile /etc/vmware/vmware-vmon/svcCfgfiles/perfcharts.json Expected output: "StreamRedirectFile" : "%VMWARE_LOG_DIR%/vmware/perfcharts/vmware-perfcharts-runtime.log", If no log file is specified for the "StreamRedirectFile" setting, this is a finding.

## Group: SRG-APP-000095-AS-000056

**Group ID:** `V-259074`

### Rule: The vCenter Perfcharts service must produce log records containing sufficient information regarding event details.

**Rule ID:** `SV-259074r960891_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access can be exploited by an attacker to compromise the server. By recording all remote access activities, it will be possible to determine the attacker's location, intent, and degree of success. Tomcat can be configured with an "AccessLogValve", a component that can be inserted into the request processing pipeline to provide robust access logging. The "AccessLogValve" creates log files in the same format as those created by standard web servers. When "AccessLogValve" is properly configured, log files will contain all the forensic information necessary in the case of a security incident. Satisfies: SRG-APP-000095-AS-000056, SRG-APP-000016-AS-000013, SRG-APP-000080-AS-000045, SRG-APP-000089-AS-000050, SRG-APP-000090-AS-000051, SRG-APP-000091-AS-000052, SRG-APP-000096-AS-000059, SRG-APP-000097-AS-000060, SRG-APP-000098-AS-000061, SRG-APP-000099-AS-000062, SRG-APP-000100-AS-000063, SRG-APP-000343-AS-000030, SRG-APP-000375-AS-000211, SRG-APP-000495-AS-000220, SRG-APP-000499-AS-000224, SRG-APP-000503-AS-000228</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/Server/Service/Engine/Host/Valve[@className="org.apache.catalina.valves.AccessLogValve"]/@pattern' /usr/lib/vmware-perfcharts/tc-instance/conf/server.xml Example result: pattern="%h %{X-Forwarded-For}i %l %u %t &quot;%r&quot; %s %b &quot;%{User-Agent}i&quot;" Required elements: %h %{X-Forwarded-For}i %l %t %u &quot;%r&quot; %s %b If the log pattern does not contain the required elements in any order, this is a finding.

## Group: SRG-APP-000118-AS-000078

**Group ID:** `V-259075`

### Rule: The vCenter Perfcharts service logs folder permissions must be set correctly.

**Rule ID:** `SV-259075r960930_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. The accuracy of the information is always pertinent. One of the first steps an attacker will take is the modification or deletion of log records to cover tracks and prolong discovery. The web server must protect the log data from unauthorized modification. Satisfies: SRG-APP-000118-AS-000078, SRG-APP-000119-AS-000079, SRG-APP-000120-AS-000080</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # find /var/log/vmware/perfcharts/ -xdev -type f -a '(' -perm -o+w -o -not -user perfcharts -o -not -group users ')' -exec ls -ld {} \; If any files are returned, this is a finding.

## Group: SRG-APP-000133-AS-000092

**Group ID:** `V-259076`

### Rule: The vCenter Perfcharts service must limit privileges for creating or modifying hosted application shared files.

**Rule ID:** `SV-259076r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application servers have the ability to specify that the hosted applications use shared libraries. The application server must have a capability to divide roles based upon duties wherein one project user (such as a developer) cannot modify the shared library code of another project user. The application server must also be able to specify that nonprivileged users cannot modify any shared library code at all. Ensuring the Security Lifecycle Listener element is uncommented and sets a minimum Umask value will allow the server to perform a number of security checks when starting and prevent the service from starting if they fail.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/Server/Listener[@className="org.apache.catalina.security.SecurityListener"]' /usr/lib/vmware-perfcharts/tc-instance/conf/server.xml Example result: <Listener className="org.apache.catalina.security.SecurityListener"/> If the "org.apache.catalina.security.SecurityListener" listener is not present, this is a finding. If the "org.apache.catalina.security.SecurityListener" listener is configured with a "minimumUmask" and is not "0007", this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-259077`

### Rule: The vCenter Perfcharts service must disable stack tracing.

**Rule ID:** `SV-259077r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Stack tracing provides debugging information from the application call stacks when a runtime error is encountered. If stack tracing is left enabled, Tomcat will provide this call stack information to the requestor, which could result in the loss of sensitive information or data that could be used to compromise the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath "//Connector[@allowTrace = 'true']" /usr/lib/vmware-perfcharts/tc-instance/conf/server.xml Expected result: XPath set is empty If any connectors are returned, this is a finding.

## Group: SRG-APP-000142-AS-000014

**Group ID:** `V-259078`

### Rule: The vCenter Perfcharts service must be configured to use a specified IP address and port.

**Rule ID:** `SV-259078r960966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The server must be configured to listen on a specified IP address and port. Without specifying an IP address and port for server to use, the server will listen on all IP addresses available. Accessing the hosted application through an IP address normally used for nonapplication functions opens the possibility of user access to resources, utilities, files, ports, and protocols that are protected on the desired application IP address.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath "//Connector[(@port = '0') or not(@address)]" /usr/lib/vmware-perfcharts/tc-instance/conf/server.xml Expected result: XPath set is empty If any connectors are returned, this is a finding.

## Group: SRG-APP-000223-AS-000150

**Group ID:** `V-259079`

### Rule: The vCenter Perfcharts service must be configured to limit data exposure between applications.

**Rule ID:** `SV-259079r961116_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If RECYCLE_FACADES is true or if a security manager is in use, a new facade object will be created for each request. This reduces the chances that a bug in an application might expose data from one request to another.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep RECYCLE_FACADES /usr/lib/vmware-perfcharts/tc-instance/conf/catalina.properties Example result: org.apache.catalina.connector.RECYCLE_FACADES=true If "org.apache.catalina.connector.RECYCLE_FACADES" is not set to "true", this is a finding. If the "org.apache.catalina.connector.RECYCLE_FACADES" setting does not exist, this is not a finding.

## Group: SRG-APP-000225-AS-000166

**Group ID:** `V-259080`

### Rule: The vCenter Perfcharts service must be configured to fail to a known safe state if system initialization fails.

**Rule ID:** `SV-259080r961122_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Determining a safe state for failure and weighing that against a potential denial of service for users depends on what type of application the web server is hosting. It is preferable that the service abort startup on any initialization failure rather than continuing in a degraded, and potentially insecure, state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep EXIT_ON_INIT_FAILURE /usr/lib/vmware-perfcharts/tc-instance/conf/catalina.properties Example result: org.apache.catalina.startup.EXIT_ON_INIT_FAILURE=true If there are no results, or if the "org.apache.catalina.startup.EXIT_ON_INIT_FAILURE" is not set to "true", this is a finding.

## Group: SRG-APP-000251-AS-000165

**Group ID:** `V-259081`

### Rule: The vCenter Perfcharts service must set URIEncoding to UTF-8.

**Rule ID:** `SV-259081r961158_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into a hosted application's data entry field and the hosted application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. An attacker can also enter Unicode characters into hosted applications in an effort to break out of the document home or root home directory or bypass security checks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath "//Connector[@URIEncoding != 'UTF-8'] | //Connector[not[@URIEncoding]]" /usr/lib/vmware-perfcharts/tc-instance/conf/server.xml Expected result: XPath set is empty If any connectors are returned, this is a finding.

## Group: SRG-APP-000266-AS-000169

**Group ID:** `V-259082`

### Rule: The vCenter Perfcharts service "ErrorReportValve showServerInfo" must be set to "false".

**Rule ID:** `SV-259082r961167_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Error Report Valve is a simple error handler for HTTP status codes that will generate and return HTML error pages. It can also be configured to return predefined static HTML pages for specific status codes and/or exception types. Disabling "showServerInfo" will only return the HTTP status code and remove all CSS from the default nonerror-related HTTP responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath '/Server/Service/Engine/Host/Valve[@className="org.apache.catalina.valves.ErrorReportValve"]' /usr/lib/vmware-perfcharts/tc-instance/conf/server.xml Example result: <Valve className="org.apache.catalina.valves.ErrorReportValve" showServerInfo="false" showReport="false"/> If the "ErrorReportValve" element is not defined or "showServerInfo" is not set to "false", this is a finding.

## Group: SRG-APP-000295-AS-000263

**Group ID:** `V-259083`

### Rule: The vCenter Perfcharts service must set an inactive timeout for sessions.

**Rule ID:** `SV-259083r1003623_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Leaving sessions open indefinitely is a major security risk. An attacker can easily use an already authenticated session to access the hosted application as the previously authenticated user. By closing sessions after a set period of inactivity, the web server can make certain that those sessions that are not closed through the user logging out of an application are eventually closed. Satisfies: SRG-APP-000295-AS-000263, SRG-APP-000389-AS-000253</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-perfcharts/tc-instance/webapps/statsreport/WEB-INF/web.xml | sed 's/xmlns=".*"//g' | xmllint --xpath '/web-app/session-config/session-timeout' - Example result: <session-timeout>6</session-timeout> If the value of "session-timeout" is not "30" or less, or is missing, this is a finding.

## Group: SRG-APP-000358-AS-000064

**Group ID:** `V-259084`

### Rule: The vCenter Perfcharts service must offload log records onto a different system or media from the system being logged.

**Rule ID:** `SV-259084r961395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system logging capability is critical for accurate forensic analysis. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, filenames involved, and access control or flow control rules invoked. Offloading is a common process in information systems with limited log storage capacity. Centralized management of log records provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. Application servers and their related components are required to offload log records onto a different system or media than the system being logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
By default, a vmware-services-perfcharts.conf rsyslog configuration file includes the service logs when syslog is configured on vCenter, but it must be verified. At the command prompt, run the following command: # cat /etc/vmware-syslog/vmware-services-perfcharts.conf Expected result: #stats input(type="imfile" File="/var/log/vmware/perfcharts/stats.log" Tag="perfcharts-stats" Severity="info" Facility="local0") #localhost_access_log input(type="imfile" File="/var/log/vmware/perfcharts/localhost_access_log.txt" Tag="perfcharts-localhost_access" Severity="info" Facility="local0") #vmware-perfcharts-gc.log input(type="imfile" File="/var/log/vmware/perfcharts/vmware-perfcharts-gc.log.*.current" Tag="perfcharts-gc" Severity="info" Facility="local0") #vmware-perfcharts-runtime.log input(type="imfile" File="/var/log/vmware/perfcharts/vmware-perfcharts-runtime.log.std*" Tag="perfcharts-runtime" Severity="info" Facility="local0") #tomcat/catalina_log input(type="imfile" File="/var/log/vmware/perfcharts/tomcat/catalina.*.log" Tag="perfcharts-tomcat-catalina" Severity="info" Facility="local0") #tomcat/localhost_log input(type="imfile" File="/var/log/vmware/perfcharts/tomcat/localhost.*.log" Tag="perfcharts-tomcat-localhost" Severity="info" Facility="local0") If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-259085`

### Rule: The vCenter Perfcharts service must enable "STRICT_SERVLET_COMPLIANCE".

**Rule ID:** `SV-259085r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Strict Servlet Compliance forces Tomcat to adhere to standards specifications including but not limited to RFC2109. RFC2109 sets the standard for HTTP session management. This setting affects several other settings that primarily pertain to cookie headers, cookie values, and sessions. Cookies will be parsed for strict adherence to specifications. Note that changing a number of these default settings may break some systems, as some browsers are unable to correctly handle the cookie headers that result from a strict adherence to the specifications. This one setting changes the default values for the following settings: org.apache.catalina.core.ApplicationContext.GET_RESOURCE_REQUIRE_SLASH org.apache.catalina.core.ApplicationDispatcher.WRAP_SAME_OBJECT org.apache.catalina.core.StandardHostValve.ACCESS_SESSION org.apache.catalina.session.StandardSession.ACTIVITY_CHECK org.apache.catalina.session.StandardSession.LAST_ACCESS_AT_START org.apache.tomcat.util.http.ServerCookie.ALWAYS_ADD_EXPIRES org.apache.tomcat.util.http.ServerCookie.FWD_SLASH_IS_SEPARATOR org.apache.tomcat.util.http.ServerCookie.PRESERVE_COOKIE_HEADER org.apache.tomcat.util.http.ServerCookie.STRICT_NAMING The "resourceOnlyServlets" attribute of any Context element. The "tldValidation" attribute of any Context element. The "useRelativeRedirects" attribute of any Context element. The "xmlNamespaceAware" attribute of any Context element. The "xmlValidation" attribute of any Context element.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep STRICT_SERVLET_COMPLIANCE /usr/lib/vmware-perfcharts/tc-instance/conf/catalina.properties Example result: org.apache.catalina.STRICT_SERVLET_COMPLIANCE=true If there are no results, or if the "org.apache.catalina.STRICT_SERVLET_COMPLIANCE" is not set to "true", this is a finding.

## Group: SRG-APP-000001-AS-000001

**Group ID:** `V-259086`

### Rule: The vCenter Perfcharts service must limit the amount of time that each Transmission Control Protocol (TCP) connection is kept alive.

**Rule ID:** `SV-259086r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Denial of service (DoS) is one threat against web servers. Many DoS attacks attempt to consume web server resources in such a way that no more resources are available to satisfy legitimate requests. In Tomcat, the "connectionTimeout" attribute sets the number of milliseconds the server will wait after accepting a connection for the request Uniform Resource Identifier (URI) line to be presented. This timeout will also be used when reading the request body (if any). This prevents idle sockets that are not sending HTTP requests from consuming system resources and potentially denying new connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The connection timeout should not be disabled by setting it to "-1". At the command prompt, run the following command: # xmllint --xpath "//Connector[@connectionTimeout = '-1']" /usr/lib/vmware-perfcharts/tc-instance/conf/server.xml Expected result: XPath set is empty If any connectors are returned, this is a finding.

## Group: SRG-APP-000001-AS-000001

**Group ID:** `V-259087`

### Rule: The vCenter Perfcharts service must limit the number of times that each Transmission Control Protocol (TCP) connection is kept alive.

**Rule ID:** `SV-259087r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>KeepAlive provides long lived HTTP sessions that allow multiple requests to be sent over the same connection. Enabling KeepAlive mitigates the effects of several types of denial-of-service attacks. An advantage of KeepAlive is the reduced latency in subsequent requests (no handshaking). However, a disadvantage is that server resources are not available to handle other requests while a connection is maintained between the server and the client. Tomcat can be configured to limit the number of subsequent requests that one client can submit to the server over an established connection. This limit helps provide a balance between the advantages of KeepAlive, while not allowing any one connection being held too long by any one client.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The connection timeout should not be unlimited by setting it to "-1". At the command prompt, run the following command: # xmllint --xpath "//Connector[@maxKeepAliveRequests = '-1']" /usr/lib/vmware-perfcharts/tc-instance/conf/server.xml Expected result: XPath set is empty If any connectors are returned, this is a finding.

## Group: SRG-APP-000251-AS-000165

**Group ID:** `V-259088`

### Rule: The vCenter Perfcharts service must configure the "setCharacterEncodingFilter" filter.

**Rule ID:** `SV-259088r961158_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into a hosted application's data entry field and the hosted application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. An attacker can also enter Unicode characters into hosted applications in an effort to break out of the document home or root home directory or to bypass security checks. VMware uses the standard Tomcat "SetCharacterEncodingFilter" to provide a layer of defense against character encoding attacks. Filters are Java objects that perform filtering tasks on the request to a resource (a servlet or static content), on the response from a resource, or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath "//*[contains(text(), 'setCharacterEncodingFilter')]/parent::*" /usr/lib/vmware-perfcharts/tc-instance/webapps/statsreport/WEB-INF/web.xml Expected result: <filter-mapping> <filter-name>setCharacterEncodingFilter</filter-name> <url-pattern>/*</url-pattern> </filter-mapping> <filter> <filter-name>setCharacterEncodingFilter</filter-name> <filter-class>org.apache.catalina.filters.SetCharacterEncodingFilter</filter-class> <async-supported>true</async-supported> <init-param> <param-name>encoding</param-name> <param-value>UTF-8</param-value> </init-param> <init-param> <param-name>ignore</param-name> <param-value>true</param-value> </init-param> </filter> If the output is does not match the expected result, this is a finding.

## Group: SRG-APP-000033-AS-000024

**Group ID:** `V-259089`

### Rule: The vCenter Perfcharts service cookies must have "http-only" flag set.

**Rule ID:** `SV-259089r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cookies are a common way to save session state over the HTTP(S) protocol. If attackers can compromise session data stored in a cookie, they are better able to launch an attack against the server and its applications. When a cookie is tagged with the "HttpOnly" flag, it tells the browser this particular cookie should only be accessed by the originating server. Any attempt to access the cookie from client script is strictly forbidden.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-perfcharts/tc-instance/webapps/statsreport/WEB-INF/web.xml | sed 's/xmlns=".*"//g' | xmllint --xpath '/web-app/session-config/cookie-config/http-only' - Expected result: <http-only>true</http-only> If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000033-AS-000024

**Group ID:** `V-259090`

### Rule: The vCenter Perfcharts service DefaultServlet must be set to "readonly" for "PUT" and "DELETE" commands.

**Rule ID:** `SV-259090r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The default servlet (or DefaultServlet) is a special servlet provided with Tomcat that is called when no other suitable page is found in a particular folder. The DefaultServlet serves static resources as well as directory listings. The DefaultServlet is configured by default with the "readonly" parameter set to "true" where HTTP commands such as PUT and DELETE are rejected. Changing this to "false" allows clients to delete or modify static resources on the server and to upload new resources. DefaultServlet "readonly" must be set to "true", either literally or by absence (default).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath "//*[contains(text(), 'DefaultServlet')]/parent::*" /usr/lib/vmware-perfcharts/tc-instance/webapps/statsreport/WEB-INF/web.xml Example output: <servlet> <description>File servlet</description> <servlet-name>FileServlet</servlet-name> <servlet-class>org.apache.catalina.servlets.DefaultServlet</servlet-class> </servlet> If the "readOnly" param-value for the "DefaultServlet" servlet class is set to "false", this is a finding. If the "readOnly" param-value does not exist, this is not a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-259091`

### Rule: The vCenter Perfcharts service shutdown port must be disabled.

**Rule ID:** `SV-259091r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Tomcat by default listens on TCP port 8005 to accept shutdown requests. By connecting to this port and sending the SHUTDOWN command, all applications within Tomcat are halted. The shutdown port is not exposed to the network as it is bound to the loopback interface. Setting the port to "-1" in $CATALINA_BASE/conf/server.xml instructs Tomcat to not listen for the shutdown command.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following commands: # xmllint --xpath "//Server/@port" /usr/lib/vmware-perfcharts/tc-instance/conf/server.xml # grep 'base.shutdown.port' /usr/lib/vmware-perfcharts/tc-instance/conf/catalina.properties Example results: port="${base.shutdown.port}" base.shutdown.port=-1 If "port" does not equal "${base.shutdown.port}", this is a finding. If "base.shutdown.port" does not equal "-1", this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-259092`

### Rule: The vCenter Perfcharts service debug parameter must be disabled.

**Rule ID:** `SV-259092r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information needed by an attacker to begin looking for possible vulnerabilities in a web server includes any information about the web server and plug-ins or modules being used. When debugging or trace information is enabled in a production web server, information about the web server, such as web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage may be displayed. Because this information may be placed in logs and general messages during normal operation of the web server, an attacker does not need to cause an error condition to gain this information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-perfcharts/tc-instance/webapps/statsreport/WEB-INF/web.xml | sed 's/xmlns=".*"//g' | xmllint --xpath '//param-name[text()="debug"]/parent::init-param' - Example result: <init-param> <param-name>debug</param-name> <param-value>0</param-value> </init-param> If the "debug" parameter is specified and is not "0", this is a finding. If the "debug" parameter does not exist, this is not a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-259093`

### Rule: The vCenter Perfcharts service directory listings parameter must be disabled.

**Rule ID:** `SV-259093r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enumeration techniques, such as URL parameter manipulation, rely on being able to obtain information about the web server's directory structure by locating directories without default pages. In this scenario, the web server will display to the user a listing of the files in the directory being accessed. Ensuring that directory listing is disabled is one approach to mitigating the vulnerability. In Tomcat, directory listing is disabled by default but can be enabled via the "listings" parameter. Ensure this node is not present to have the default effect.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --format /usr/lib/vmware-perfcharts/tc-instance/webapps/statsreport/WEB-INF/web.xml | sed 's/xmlns=".*"//g' | xmllint --xpath '//param-name[text()="listings"]/parent::init-param' - Example result: XPath set is empty If the "listings" parameter is specified and is not "false", this is a finding. If the "listings" parameter does not exist, this is not a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-259094`

### Rule: The vCenter Perfcharts service deployXML attribute must be disabled.

**Rule ID:** `SV-259094r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Host element controls deployment. Automatic deployment allows for simpler management but also makes it easier for an attacker to deploy a malicious application. Automatic deployment is controlled by the autoDeploy and deployOnStartup attributes. If both are false, only Contexts defined in server.xml will be deployed, and any changes will require a Tomcat restart. In a hosted environment where web applications may not be trusted, set the deployXML attribute to "false" to ignore any context.xml packaged with the web application that may try to assign increased privileges to the web application. Note that if the security manager is enabled, the deployXML attribute will default to false.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath "//Host/@deployXML" /usr/lib/vmware-perfcharts/tc-instance/conf/server.xml Expected result: deployXML="false" If "deployXML" does not equal "false", this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-259095`

### Rule: The vCenter Perfcharts service must have Autodeploy disabled.

**Rule ID:** `SV-259095r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Tomcat allows auto-deployment of applications while it is running. This can allow untested or malicious applications to be automatically loaded into production. Autodeploy must be disabled in production.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath "//Host/@autoDeploy" /usr/lib/vmware-perfcharts/tc-instance/conf/server.xml Expected result: autoDeploy="false" If "autoDeploy" does not equal "false", this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-259096`

### Rule: The vCenter Perfcharts service xpoweredBy attribute must be disabled.

**Rule ID:** `SV-259096r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Individual connectors can be configured to display the Tomcat information to clients. This information can be used to identify server versions that can be useful to attackers for identifying vulnerable versions of Tomcat. Individual connectors must be checked for the xpoweredBy attribute to ensure they do not pass server information to clients. The default value for xpoweredBy is "false".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # xmllint --xpath "//Connector/@xpoweredBy" /usr/lib/vmware-perfcharts/tc-instance/conf/server.xml Example result: XPath set is empty If the "xpoweredBy" parameter is specified and is not "false", this is a finding. If the "xpoweredBy" parameter does not exist, this is not a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-259097`

### Rule: The vCenter Perfcharts service example applications must be removed.

**Rule ID:** `SV-259097r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Tomcat provides example applications, documentation, and other directories in the default installation that do not serve a production use. These files must be deleted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # ls -l /usr/lib/vmware-perfcharts/tc-instance/webapps/examples If the examples folder exists or contains any content, this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-259098`

### Rule: The vCenter Perfcharts service default documentation must be removed.

**Rule ID:** `SV-259098r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Tomcat provides documentation and other directories in the default installation that do not serve a production use. These files must be deleted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # ls -l /usr/lib/vmware-perfcharts/tc-instance/webapps/docs If the "docs" folder exists or contains any content, this is a finding.

## Group: SRG-APP-000380-AS-000088

**Group ID:** `V-259099`

### Rule: The vCenter Perfcharts service files must have permissions in an out-of-the-box state.

**Rule ID:** `SV-259099r961461_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>As a rule, accounts on a web server are to be kept to a minimum. Only administrators, web managers, developers, auditors, and web authors require accounts on the machine hosting the web server. The resources to which these accounts have access must also be closely monitored and controlled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # find /usr/lib/vmware-perfcharts/ -xdev -type f -a '(' -perm -o+w -o -not -user root -o -not -group root ')' -exec ls -ld {} \; If any files are returned, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-259100`

### Rule: The vCenter Perfcharts service must disable "ALLOW_BACKSLASH".

**Rule ID:** `SV-259100r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When Tomcat is installed behind a proxy configured to only allow access to certain contexts (web applications), an HTTP request containing "/\../" may allow attackers to work around the proxy restrictions using directory traversal attack methods. If "allow_backslash" is "true", the "\" character will be permitted as a path delimiter. The default value for the setting is "false", but Tomcat must always be configured as if no proxy restricting context access was used, and "allow_backslash" should be set to "false" to prevent directory-traversal-style attacks. This setting can create operability issues with noncompliant clients.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep ALLOW_BACKSLASH /usr/lib/vmware-perfcharts/tc-instance/conf/catalina.properties Example result: org.apache.catalina.connector.ALLOW_BACKSLASH=false If "org.apache.catalina.connector.ALLOW_BACKSLASH" is not set to "false", this is a finding. If the "org.apache.catalina.connector.ALLOW_BACKSLASH" setting does not exist, this is not a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-259101`

### Rule: The vCenter Perfcharts service must enable "ENFORCE_ENCODING_IN_GET_WRITER".

**Rule ID:** `SV-259101r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some clients try to guess the character encoding of text media when the mandated default of ISO-8859-1 should be used. Some browsers will interpret as UTF-7 when the characters are safe for ISO-8859-1. This can create the potential for a XSS attack. To defend against this, enforce_encoding_in_get_writer must be set to true.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, run the following command: # grep ENFORCE_ENCODING_IN_GET_WRITER /usr/lib/vmware-perfcharts/tc-instance/conf/catalina.properties Example result: org.apache.catalina.connector.response.ENFORCE_ENCODING_IN_GET_WRITER=true If "org.apache.catalina.connector.response.ENFORCE_ENCODING_IN_GET_WRITER" is not set to "true", this is a finding. If the "org.apache.catalina.connector.response.ENFORCE_ENCODING_IN_GET_WRITER" setting does not exist, this is not a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-259102`

### Rule: The vCenter Perfcharts service manager webapp must be removed.

**Rule ID:** `SV-259102r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Tomcat provides management functionality through either a default manager webapp or through local editing of the configuration files. The manager webapp files must be deleted, and administration must be performed through the local editing of the configuration files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # ls -l /usr/lib/vmware-perfcharts/tc-instance/webapps/manager If the manager folder exists or contains any content, this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-259103`

### Rule: The vCenter Perfcharts service host-manager webapp must be removed.

**Rule ID:** `SV-259103r1003625_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Tomcat provides host management functionality through either a default host-manager webapp or through local editing of the configuration files. The host-manager webapp files must be deleted, and administration must be performed through the local editing of the configuration files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # ls -l /usr/lib/vmware-perfcharts/tc-instance/webapps/host-manager If the host-manager folder exists or contains any content, this is a finding.

