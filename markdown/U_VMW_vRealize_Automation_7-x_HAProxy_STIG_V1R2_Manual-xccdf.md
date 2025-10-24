# STIG Benchmark: VMW vRealize Automation 7.x HA Proxy Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-240039`

### Rule: HAProxy must limit the amount of time that an http request can be received.

**Rule ID:** `SV-240039r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Resource exhaustion can occur when an unlimited number of concurrent requests are allowed on a web site, facilitating a denial of service attack. Mitigating this kind of attack will include limiting the parameter values associated with keepalive, (i.e., a parameter used to limit the amount of time a connection may be inactive). HAProxy provides an http-request timeout parameter that set the maximum allowed time to wait for a complete HTTP request. Setting this parameter will mitigate slowloris DoS attacks. Slowloris tries to keep many connections to the target web server open and hold them open as long as possible. It accomplishes this by opening connections to the target web server and sending a partial request. Periodically, it will send subsequent HTTP headers, adding to—but never completing—the request.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'timeout http-request' /etc/haproxy/haproxy.cfg If the value of ''timeout http-request" is not set to "5000", is commented out, or is missing, this is a finding.

## Group: SRG-APP-000001-WSR-000002

**Group ID:** `V-240040`

### Rule: HAProxy must enable cookie-based persistence in a backend.

**Rule ID:** `SV-240040r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Session management is the practice of protecting the bulk of the user authorization and identity information. As a load balancer, HAProxy must participate in session management in order to set the session management cookie. Additionally, HAProxy must also ensure that the backend server which started the session with the client is forwarded subsequent requests from the client.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open the following files: /etc/haproxy/conf.d/20-vcac.cfg /etc/haproxy/conf.d/30-vro-config.cfg Verify that each backend is configured with the following: cookie JSESSIONID prefix If "cookie" is not set for each backend, this is a finding.

## Group: SRG-APP-000014-WSR-000006

**Group ID:** `V-240041`

### Rule: HAProxy must be configured with FIPS 140-2 compliant ciphers for https connections.

**Rule ID:** `SV-240041r879519_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Transport Layer Security (TLS) is optional for a public web server. However, if authentication is being performed, then the use of the TLS protocol is required. Without the use of TLS, the authentication data would be transmitted unencrypted and would become vulnerable to disclosure. Using TLS along with DoD PKI certificates for encryption of the authentication data protects the information from being accessed by all parties on the network. To further protect the authentication data, the web server must use a FIPS 140-2 approved TLS version and all non-FIPS-approved SSL versions must be disabled. FIPS 140-2 approved TLS versions include TLS V1.0 or greater. NIST SP 800-52 specifies the preferred configurations for government systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open the following files: /etc/haproxy/conf.d/20-vcac.cfg /etc/haproxy/conf.d/30-vro-config.cfg Verify that each frontend is configured with the following: bind :<port> ssl crt <pemfile> ciphers FIPS:+3DES:!aNULL no-sslv3 Note: <port> and <pemfile> will be different for each frontend. If the ciphers listed are not as shown above, this is a finding.

## Group: SRG-APP-000015-WSR-000014

**Group ID:** `V-240042`

### Rule: HAProxy must be configured to use TLS for https connections.

**Rule ID:** `SV-240042r879520_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data exchanged between the user and the web server can range from static display data to credentials used to log into the hosted application. Even when data appears to be static, the non-displayed logic in a web page may expose business logic or trusted system relationships. The integrity of all the data being exchanged between the user and web server must always be trusted. To protect the integrity and trust, encryption methods should be used to protect the complete communication session. In order to protect the integrity and confidentiality of the remote sessions, HAProxy uses SSL/TLS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open the following files: /etc/haproxy/conf.d/20-vcac.cfg /etc/haproxy/conf.d/30-vro-config.cfg Verify that each frontend is configured with the following: bind :<port> ssl crt <pemfile> ciphers FIPS:+3DES:!aNULL no-sslv3 Note: <port> and <pemfile> will be different for each frontend. If "ssl" is not set for the bind option for each frontend, this is a finding.

## Group: SRG-APP-000016-WSR-000005

**Group ID:** `V-240043`

### Rule: HAProxy must be configured to use syslog.

**Rule ID:** `SV-240043r879521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. By providing remote access information to an external monitoring system, the organization can monitor for cyber attacks and monitor compliance with remote access policies. The organization can also look at data organization wide and determine an attack or anomaly is occurring on the organization which might not be noticed if the data were kept local to the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /etc/haproxy/haproxy.cfg Navigate to the globals section. Verify that the globals section contains the log keyword, and that the log option contains the local0 syslog facility as its parameter. If properly configured, the globals section will contain the following: global log 127.0.0.1 local0 If the local0 syslog facility is not configured, this is a finding. Navigate to the defaults section. Verify that the defaults section contains the log keyword with the global value. Verify that an option keyword has been configured with the httplog value. If properly configured, the "globals" section will contain the following: defaults log global option httplog Navigate to and open the following files: /etc/haproxy/conf.d/30-vro-config.cfg /etc/haproxy/conf.d/20-vcac.cfg Navigate to the each frontend section. Verify that the log keyword has not been set for each frontend. If the log keyword is resent in a frontend, this is a finding. Navigate to and open /etc/rsyslog.d/vcac.conf. Review the configured syslog facilities and determine the location of the log file for the local0 syslog facility. If the local0 syslog facility does not refer to a valid log file, this is a finding. Navigate to and open the local0 syslog log file. Verify that HAProxy is logging start and stop events to the log file. If the log file is not recording HAProxy start and stop events, this is a finding.

## Group: SRG-APP-000089-WSR-000047

**Group ID:** `V-240044`

### Rule: HAProxy must generate log records for system startup and shutdown.

**Rule ID:** `SV-240044r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Logging must be comprehensive to be useful for both intrusion monitoring and security investigations. Recording the start and stop events of HAProxy will provide useful information to investigators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /etc/haproxy/haproxy.cfg Navigate to the globals section. Verify that the globals section contains the log keyword, and that the log option contains the local0 syslog facility as its parameter. If properly configured, the globals section will contain the following: global log 127.0.0.1 local0 If the local0 syslog facility is not configured, this is a finding. Navigate to the defaults section. Verify that the defaults section contains the log keyword with the global value. Verify that an option keyword has been configured with the httplog value. If properly configured, the globals section will contain the following: defaults log global option httplog Navigate to and open /etc/rsyslog.d/vcac.conf. Review the configured syslog facilities and determine the location of the log file for the local0 syslog facility. If the local0 syslog facility does not refer to a valid log file, this is a finding. Navigate to and open the local0 syslog log file. Verify that HAProxy is logging start and stop events to the log file. If the log file is not recording HAProxy start and stop events, this is a finding.

## Group: SRG-APP-000095-WSR-000056

**Group ID:** `V-240045`

### Rule: HAProxy must log what type of events occurred.

**Rule ID:** `SV-240045r879563_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ascertaining the correct type of event that occurred is important during forensic analysis. The correct determination of the event and when it occurred is important in relation to other events that happened at that same time. Without sufficient information establishing what type of log event occurred, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked. When configured for httplog, HAProxy logs uses the Common Log Format (CLF). The CLF format, a World Wide Web Consortium standard, captures the type of web server event in addition to other useful information. This will enable forensic analysis of server events in case of a malicious event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /etc/haproxy/haproxy.cfg Navigate to the globals section. Verify that the globals section contains the log keyword, and that the log option contains the local0 syslog facility as its parameter. If properly configured, the globals section will contain the following: global log 127.0.0.1 local0 If the local0 syslog facility is not configured, this is a finding. Navigate to the defaults section. Verify that the defaults section contains the log keyword with the global value. Verify that an option keyword has been configured with the httplog value. If properly configured, the globals section will contain the following: defaults log global option httplog Navigate to and open /etc/rsyslog.d/vcac.conf. Review the configured syslog facilities and determine the location of the log file for the local0 syslog facility. If the local0 syslog facility does not refer to a valid log file, this is a finding. Navigate to and open the local0 syslog log file. Verify that HAProxy is logging the type of events to the log file. If the log file is not recording the type of events, this is a finding.

## Group: SRG-APP-000096-WSR-000057

**Group ID:** `V-240046`

### Rule: HAProxy must log when events occurred.

**Rule ID:** `SV-240046r879564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ascertaining when an event occurred is important during forensic analysis. The correct determination of the event and when it occurred is important in relation to other events that happened at that same time. Without sufficient information establishing when an event occurred, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked. When configured for httplog, HAProxy logs uses the Common Log Format (CLF). The CLF format, a World Wide Web Consortium standard, captures the time of a web server event in addition to other useful information. This will enable forensic analysis of server events in case of a malicious event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /etc/haproxy/haproxy.cfg Navigate to the globals section. Verify that the globals section contains the log keyword, and that the log option contains the local0 syslog facility as its parameter. If properly configured, the globals section will contain the following: global log 127.0.0.1 local0 If the local0 syslog facility is not configured, this is a finding. Navigate to the defaults section. Verify that the defaults section contains the log keyword with the global value. Verify that an option keyword has been configured with the httplog value. If properly configured, the globals section will contain the following: defaults log global option httplog Navigate to and open /etc/rsyslog.d/vcac.conf. Review the configured syslog facilities and determine the location of the log file for the local0 syslog facility. If the local0 syslog facility does not refer to a valid log file, this is a finding. Navigate to and open the local0 syslog log file. Verify that HAProxy is logging the time of events to the log file. If the log file is not recording the time of events, this is a finding.

## Group: SRG-APP-000097-WSR-000058

**Group ID:** `V-240047`

### Rule: HAProxy must log where events occurred.

**Rule ID:** `SV-240047r879565_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ascertaining where an event occurred is important during forensic analysis. The correct determination of the event and where on the web server it occurred is important in relation to other events that happened at that same time. Without sufficient information establishing where an event occurred, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked. When configured for httplog, HAProxy logs uses the Common Log Format (CLF). The CLF format, a World Wide Web Consortium standard, captures the local resource that was the target of a web server event in addition to other useful information. This will enable forensic analysis of server events in case of a malicious event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /etc/haproxy/haproxy.cfg Navigate to the globals section. Verify that the globals section contains the log keyword, and that the log option contains the local0 syslog facility as its parameter. If properly configured, the globals section will contain the following: global log 127.0.0.1 local0 If the local0 syslog facility is not configured, this is a finding. Navigate to the defaults section. Verify that the defaults section contains the log keyword with the global value. Verify that an option keyword has been configured with the httplog value. If properly configured, the globals section will contain the following: defaults log global option httplog Navigate to and open /etc/rsyslog.d/vcac.conf. Review the configured syslog facilities and determine the location of the log file for the local0 syslog facility. If the local0 syslog facility does not refer to a valid log file, this is a finding. Navigate to and open the local0 syslog log file. Verify that HAProxy is logging where on the web server resources were requested to the log file. If the log file is not recording where the events occurred, this is a finding.

## Group: SRG-APP-000098-WSR-000059

**Group ID:** `V-240048`

### Rule: HAProxy must log the source of events.

**Rule ID:** `SV-240048r879566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ascertaining the source of an event is important during forensic analysis. The correct determination of the event and what client requested the resource is important in relation to other events that happened at that same time. Without sufficient information establishing the source of an event, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked. When configured for httplog, HAProxy logs uses the Common Log Format (CLF). The CLF format, a World Wide Web Consortium standard, captures the client IP address that requested the web server event in addition to other useful information. This will enable forensic analysis of server events in case of a malicious event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /etc/haproxy/haproxy.cfg Navigate to the globals section. Verify that the globals section contains the log keyword, and that the log option contains the local0 syslog facility as its parameter. If properly configured, the globals section will contain the following: global log 127.0.0.1 local0 If the local0 syslog facility is not configured, this is a finding. Navigate to the defaults section. Verify that the defaults section contains the log keyword with the global value. Verify that an option keyword has been configured with the httplog value. If properly configured, the globals section will contain the following: defaults log global option httplog Navigate to and open /etc/rsyslog.d/vcac.conf. Review the configured syslog facilities and determine the location of the log file for the local0 syslog facility. If the local0 syslog facility does not refer to a valid log file, this is a finding. Navigate to and open the local0 syslog log file. Verify that HAProxy is logging the source of the event to the log file. If the log file is not recording the source of the event, this is a finding.

## Group: SRG-APP-000099-WSR-000061

**Group ID:** `V-240049`

### Rule: HAProxy must log the outcome of events.

**Rule ID:** `SV-240049r879567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ascertaining the outcome of an event is important during forensic analysis. The correct determination of the event and its outcome is important in relation to other events that happened at that same time. Without sufficient information establishing the outcome of an event, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked. When configured for httplog, HAProxy logs uses the Common Log Format (CLF). The CLF format, a World Wide Web Consortium standard, captures the success or failure of the web server event in addition to other useful information. This will enable forensic analysis of server events in case of a malicious event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /etc/haproxy/haproxy.cfg Navigate to the globals section. Verify that the globals section contains the log keyword, and that the log option contains the local0 syslog facility as its parameter. If properly configured, the globals section will contain the following: global log 127.0.0.1 local0 If the local0 syslog facility is not configured, this is a finding. Navigate to the defaults section. Verify that the defaults section contains the log keyword with the global value. Verify that an option keyword has been configured with the httplog value. If properly configured, the globals section will contain the following: defaults log global option httplog Navigate to and open /etc/rsyslog.d/vcac.conf. Review the configured syslog facilities and determine the location of the log file for the local0 syslog facility. If the local0 syslog facility does not refer to a valid log file, this is a finding. Navigate to and open the local0 syslog log file. Verify that HAProxy is logging the outcome of web server events to the log file. If the log file is not recording the outcome of events, this is a finding.

## Group: SRG-APP-000100-WSR-000064

**Group ID:** `V-240050`

### Rule: HAProxy must log the session ID from the request headers.

**Rule ID:** `SV-240050r879568_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ascertaining the identity of the requestor of an event is important during forensic analysis. The correct determination of identity of the requestor of the event and its outcome is important in relation to other events that happened at that same time. Without sufficient information establishing the identity of the requestor of an event, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked. When configured for httplog, HAProxy logs uses the Common Log Format (CLF). The CLF format, a World Wide Web Consortium standard, captures the request headers of the web server event in addition to other useful information. This will enable forensic analysis of server events in case of a malicious event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /etc/haproxy/haproxy.cfg Navigate to the globals section. Verify that the globals section contains the log keyword, and that the log option contains the local0 syslog facility as its parameter. If properly configured, the globals section will contain the following: global log 127.0.0.1 local0 If the local0 syslog facility is not configured, this is a finding. Navigate to the defaults section. Verify that the defaults section contains the log keyword with the global value. Verify that an option keyword has been configured with the httplog value. If properly configured, the globals section will contain the following: defaults log global option httplog Navigate to and open /etc/rsyslog.d/vcac.conf. Review the configured syslog facilities and determine the location of the log file for the local0 syslog facility. If the local0 syslog facility does not refer to a valid log file, this is a finding. Navigate to and open the local0 syslog log file. Verify that HAProxy is logging request headers to include session ID to the log file. If the log file is not recording the session ID from the request headers, this is a finding.

## Group: SRG-APP-000108-WSR-000166

**Group ID:** `V-240051`

### Rule: HAProxy must use a logging mechanism that is configured to alert the ISSO and SA in the event of a processing failure.

**Rule ID:** `SV-240051r879570_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An accurate and current audit trail is essential for maintaining a record of system activity. If the logging system fails, the SA must be notified and must take prompt action to correct the problem. Minimally, the system must log this event and the SA will receive this notification during the daily system log review. If feasible, active alerting (such as e-mail or paging) should be employed consistent with the site's established operations management systems and procedures.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSO. Determine if logging failure events are monitored, and warnings provided to the ISSO. If logging failure events do not provide warnings in accordance with organization policies, this is a finding. If alerts are not sent or the web server is not configured to use a dedicated logging tool that meets this requirement, this is a finding.

## Group: SRG-APP-000118-WSR-000068

**Group ID:** `V-240052`

### Rule: HAProxy log files must not be accessible to unauthorized users.

**Rule ID:** `SV-240052r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The HAProxy log files provide audit data useful to the discovery of suspicious behavior. The log files may contain usernames and passwords in clear text as well as other information that could aid a malicious user with unauthorized access attempts to the database. Generation and protection of these files helps support security monitoring efforts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -la /var/log/vmware/vcac/vcac-config.log If the log file has permissions more permissive than "640", this is a finding.

## Group: SRG-APP-000119-WSR-000069

**Group ID:** `V-240053`

### Rule: HAProxy log files must be protected from unauthorized modification.

**Rule ID:** `SV-240053r879577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to their advantage since each event record might contain communication ports, protocols, services, trust relationships, user names, etc.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -la /var/log/vmware/vcac/vcac-config.log If the log file has permissions more permissive than "640", this is a finding.

## Group: SRG-APP-000120-WSR-000070

**Group ID:** `V-240054`

### Rule: HAProxy log files must be protected from unauthorized deletion.

**Rule ID:** `SV-240054r879578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to their advantage since each event record might contain communication ports, protocols, services, trust relationships, user names, etc.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -la /var/log/vmware/vcac/vcac-config.log If the log file has permissions more permissive than "640", this is a finding.

## Group: SRG-APP-000125-WSR-000071

**Group ID:** `V-240055`

### Rule: HAProxy log files must be backed up onto a different system or media.

**Rule ID:** `SV-240055r879582_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to their advantage since each event record might contain communication ports, protocols, services, trust relationships, user names, etc.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSO. Determine whether log data and records are being backed up to a different system or separate media. If log data and records are not being backed up to a different system or separate media, this is a finding.

## Group: SRG-APP-000131-WSR-000051

**Group ID:** `V-240056`

### Rule: HAProxy files must be verified for their integrity (checksums) before being added to the build systems.

**Rule ID:** `SV-240056r879584_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Being able to verify that a patch, upgrade, certificate, etc., being added to the web server is unchanged from the producer of the file is essential for file validation and non-repudiation of the information. The HAProxy web server files on vRA must be part of a documented build process. Checksums of the production files must be available to verify their integrity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSO. Determine whether web server files are verified/validated before being implemented into the production environment. If the web server files are not verified or validated before being implemented into the production environment, this is a finding.

## Group: SRG-APP-000131-WSR-000073

**Group ID:** `V-240057`

### Rule: HAProxy expansion modules must be verified for their integrity (checksums) before being added to the build systems.

**Rule ID:** `SV-240057r879584_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Being able to verify that a patch, upgrade, certificate, etc., being added to the web server is unchanged from the producer of the file is essential for file validation and non-repudiation of the information. Expansion that are installed on the production HAProxy web server on vRA must be part of a documented build process. Checksums of the production files must be available to verify their integrity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSO. Determine whether expansion modules are being fully reviewed, tested, and signed before being implemented into the production environment. If the expansion modules are not being fully reviewed, tested, and signed before being implemented into the production environment, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-240058`

### Rule: HAProxy must limit access to the statistics feature.

**Rule ID:** `SV-240058r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to be accessible on a production DoD system. HAProxy provide a statistics page, which will display web browser statistics from any web browser if HAProxy has not been configured to connect the server statistics to a UNIX socket.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'stats socket' /etc/haproxy/haproxy.cfg If the command does not return the line below, this is a finding. stats socket /var/run/haproxy.sock mode 600 level admin

## Group: SRG-APP-000141-WSR-000077

**Group ID:** `V-240059`

### Rule: HAProxy must not contain any documentation, sample code, example applications, and tutorials.

**Rule ID:** `SV-240059r879587_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Web server documentation, sample code, example applications, and tutorials may be an exploitable threat to a web server because this type of code has not been evaluated and approved. A production web server must only contain components that are operationally necessary (e.g., compiled code, scripts, web-content, etc.). Any documentation, sample code, example applications, and tutorials must be removed from a production web server. To make certain that the documentation and code are not installed or uninstalled completely; the web server must offer an option as part of the installation process to exclude these packages or to uninstall the packages if necessary.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls /usr/share/doc/packages/haproxy The command should report that there is no such file or directory. If the command shows any files or directories, this is a finding.

## Group: SRG-APP-000141-WSR-000086

**Group ID:** `V-240060`

### Rule: HAProxy must be run in a chroot jail.

**Rule ID:** `SV-240060r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Chroot is an operation that changes the apparent root directory for the current running process and their children. A program that is run in such a modified environment cannot access files and commands outside that environmental directory tree. This modified environment is called a chroot jail.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'chroot' /etc/haproxy/haproxy.cfg If the value "/var/lib/haproxy" is not listed, this is a finding.

## Group: SRG-APP-000142-WSR-000089

**Group ID:** `V-240061`

### Rule: HAProxy frontend servers must be bound to a specific port.

**Rule ID:** `SV-240061r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The web server must be configured to listen on a specified IP address and port. Without specifying an IP address and port for the web server to utilize, the web server will listen on all IP addresses available to the hosting server. If the web server has multiple IP addresses, i.e., a management IP address, the web server will also accept connections on the management IP address. Accessing the hosted application through an IP address normally used for non-application functions opens the possibility of user access to resources, utilities, files, ports, and protocols that are protected on the desired application IP address.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open the following files: /etc/haproxy/conf.d/20-vcac.cfg /etc/haproxy/conf.d/30-vro-config.cfg Verify that each frontend is bound to at least one port. Below is an example binding: frontend https-in-vro-config bind :8283 If each frontend is not bound to at least one port, this is a finding.

## Group: SRG-APP-000172-WSR-000104

**Group ID:** `V-240062`

### Rule: HAProxy must use SSL/TLS protocols in order to secure passwords during transmission from the client.

**Rule ID:** `SV-240062r879609_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data used to authenticate, especially passwords, needs to be protected at all times, and encryption is the standard method for protecting authentication data during transmission. Even when data is passed through a load balancer, data used to authenticate users must be sent via SSL/TLS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line execute the following command: cat /etc/haproxy/conf.d/20-vcac.cfg | awk '$0 ~ /bind.*:80/ || $0 ~ /redirect.*ssl_fc/ {print}' If the command does not return the two lines below, this is a finding. bind 0.0.0.0:80 redirect scheme https if !{ ssl_fc }

## Group: SRG-APP-000175-WSR-000095

**Group ID:** `V-240063`

### Rule: HAProxy must perform RFC 5280-compliant certification path validation if PKI is being used.

**Rule ID:** `SV-240063r879612_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. A certificate’s certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSO. Review HAProxy configuration to verify that certificates being provided by the web server are validated, RFC 5280-compliant certificates. If PKI is not being used, this is NA. If certificates are not validated, RFC 5280-compliant certificates, this is a finding.

## Group: SRG-APP-000176-WSR-000096

**Group ID:** `V-240064`

### Rule: HAProxys private key must have access restricted.

**Rule ID:** `SV-240064r879613_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>HAProxy's private key is used to prove the identity of the server to clients and securely exchange the shared secret key used to encrypt communications between the web server and clients. Only authenticated system administrators or the designated PKI Sponsor for the web server must have access to the web server's private key. By gaining access to the private key, an attacker can pretend to be an authorized server and decrypt the encrypted traffic between a client and the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -al /etc/apache2/server.pem If the permissions on the file are not "600", this is a finding.

## Group: SRG-APP-000179-WSR-000111

**Group ID:** `V-240065`

### Rule: HAProxy must be configured to use only FIPS 140-2 approved ciphers.

**Rule ID:** `SV-240065r879616_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of cryptography to provide confidentiality and non-repudiation is not effective unless strong methods are employed with its use. Many earlier encryption methods and modules have been broken and/or overtaken by increasing computing power. The NIST FIPS 140-2 cryptographic standards provide proven methods and strengths to employ cryptography effectively.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -E 'bind.*ssl' /etc/haproxy/conf.d/30-vro-config.cfg /etc/haproxy/conf.d/20-vcac.cfg If the return value for SSL cipher list is not set to "FIPS: +3DES:!aNULL", this is a finding.

## Group: SRG-APP-000211-WSR-000031

**Group ID:** `V-240066`

### Rule: HAProxy must prohibit anonymous users from editing system files.

**Rule ID:** `SV-240066r879631_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Allowing anonymous users the capability to change the web server or the hosted application will not generate proper log information that can then be used for forensic reporting in the case of a security issue. Allowing anonymous users to make changes will also grant change capabilities to anybody without forcing a user to authenticate before the changes can be made.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -alR /etc/haproxy /var/lib/haproxy /usr/sbin/haproxy | grep -E '^-' | awk '{print $1}' | cut -c9 | grep w If the command returns any value, this is a finding.

## Group: SRG-APP-000225-WSR-000074

**Group ID:** `V-240067`

### Rule: The HAProxy baseline must be documented and maintained.

**Rule ID:** `SV-240067r879640_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without maintenance of a baseline of current HAProxy software, monitoring for changes cannot be complete and unauthorized changes to the software can go undetected. Changes to HAProxy could be the result of intentional or unintentional actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the appliance administrator and/or ISSO provide the HAProxy software baseline procedures, implementation evidence, and a list of files and directories included in the baseline procedure for completeness. If baseline procedures do not exist, not implemented reliably, or are not complete, this is a finding.

## Group: SRG-APP-000225-WSR-000140

**Group ID:** `V-240068`

### Rule: HAProxy must be configured to validate the configuration files during start and restart events.

**Rule ID:** `SV-240068r879640_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure in a known state can address safety or security in accordance with the mission/business needs of the organization. Failure in a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. Failure in a known safe state helps prevent systems from failing to a state that may cause loss of data or unauthorized access to system resources. Applications or systems that fail suddenly and with no incorporated failure state planning may leave the hosting system available but with a reduced security protection capability. Preserving information system state information also facilitates system restart and return to the operational mode of the organization with less disruption of mission/business processes. An example is a firewall that blocks all traffic rather than allowing all traffic when a firewall component fails. This prevents an attacker from forcing a failure of the system in order to obtain access. Web servers must fail to a known consistent state. Validating the server's configuration file during start and restart events can help to minimize the risk of an unexpected server failure during system start.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -E '\s(start|restart)\)' -A 7 /etc/init.d/haproxy If the command "haproxy_check" is not shown in the "start)" and the "restart)" code blocks, this is a finding.

## Group: SRG-APP-000246-WSR-000149

**Group ID:** `V-240069`

### Rule: HAProxy must limit the amount of time that half-open connections are kept alive.

**Rule ID:** `SV-240069r879650_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can limit the ability of the web server being used in a DoS attack through several methods. The methods employed will depend upon the hosted applications and their resource needs for proper operation. An example setting that could be used to limit the ability of the web server being used in a DoS attack is to limit the amount of time that a half-open connection is kept alive.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'timeout client-fin' /etc/haproxy/haproxy.cfg If the return value for "timeout client-fin" list is not set to "30s", this is a finding.

## Group: SRG-APP-000266-WSR-000159

**Group ID:** `V-240070`

### Rule: HAProxy must provide default error files.

**Rule ID:** `SV-240070r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information needed by an attacker to begin looking for possible vulnerabilities in a web server includes any information about the web server, backend systems being accessed, and plug-ins or modules being used. Web servers will often display error messages to client users displaying enough information to aid in the debugging of the error. The information given back in error messages may display the web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage. This information could be used by an attacker to blueprint what type of attacks might be successful. The information given to users must be minimized to not aid in the blueprinting of the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'errorfile' /etc/haproxy/haproxy.cfg If the return value for "errorfile" does not list error pages for the following HTTP status codes, this is a finding. 400, 403, 408, 500, 502, 503, 504

## Group: SRG-APP-000266-WSR-000160

**Group ID:** `V-240071`

### Rule: HAProxy must not be started with the debug switch.

**Rule ID:** `SV-240071r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information needed by an attacker to begin looking for possible vulnerabilities in a web server includes any information about the web server and plug-ins or modules being used. When debugging or trace information is enabled in a production web server, information about the web server, such as web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage may be displayed. Since this information may be placed in logs and general messages during normal operation of the web server, an attacker does not need to cause an error condition to gain this information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ps aux | grep '[h]aproxy' | grep '\s\-d\s' If the command returns any value, this is a finding.

## Group: SRG-APP-000295-WSR-000012

**Group ID:** `V-240072`

### Rule: HAProxy must set an absolute timeout on sessions.

**Rule ID:** `SV-240072r879673_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Leaving sessions open indefinitely is a major security risk. An attacker can easily use an already authenticated session to access the hosted application as the previously authenticated user. By closing sessions after an absolute period of time, the user is forced to re-authenticate guaranteeing the session is still in use. Enabling an absolute timeout for sessions closes sessions that are still active. Examples would be a runaway process accessing the web server or an attacker using a hijacked session to slowly probe the web server. HAProxy provides a 'tune.ssl.lifetime' parameter, which will set an absolute timeout on SSL sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'tune.ssl.lifetime' /etc/haproxy/haproxy.cfg If the command returns any value, this is a finding.

## Group: SRG-APP-000295-WSR-000134

**Group ID:** `V-240073`

### Rule: HAProxy must set an inactive timeout on sessions.

**Rule ID:** `SV-240073r879673_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Leaving sessions open indefinitely is a major security risk. An attacker can easily use an already authenticated session to access the hosted application as the previously authenticated user. By closing sessions after a set period of inactivity, the web server can make certain that those sessions that are not closed through the user logging out of an application are eventually closed. Acceptable values are "5" minutes for high-value applications, "10" minutes for medium-value applications, and "20" minutes for low-value applications. HAProxy provides an appsession parameter, which will invalidate an inactive cookie after a configurable amount of time.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open the following files: /etc/haproxy/conf.d/20-vcac.cfg /etc/haproxy/conf.d/30-vro-config.cfg Verify that each backend that sets a cookie is configured with the following: appsession <cookie> len 64 timeout 5m Note: The value for <cookie> is defined in the "cookie" option for each backend and may be different. If the "appsession" option is not present or is not configured as shown, this is a finding.

## Group: SRG-APP-000315-WSR-000003

**Group ID:** `V-240074`

### Rule: HAProxy must redirect all http traffic to use https.

**Rule ID:** `SV-240074r879692_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. A web server can be accessed remotely and must be able to enforce remote access policy requirements or work in conjunction with enterprise tools designed to enforce policy requirements. vRA can be configured to redirect unencrypted, http port 80, traffic to use the encrypted, https port 443.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'redirect scheme https' /etc/haproxy/conf.d/20-vcac.cfg Note: the command should return this line: 'redirect scheme https if !{ ssl_fc }' If the command does not return the expected line, this is a finding.

## Group: SRG-APP-000315-WSR-000004

**Group ID:** `V-240075`

### Rule: HAProxy must restrict inbound connections from nonsecure zones.

**Rule ID:** `SV-240075r879692_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. A web server can be accessed remotely and must be capable of restricting access from what the DoD defines as nonsecure zones. Nonsecure zones are defined as any IP, subnet, or region that is defined as a threat to the organization. The nonsecure zones must be defined for public web servers logically located in a DMZ, as well as private web servers with perimeter protection devices. By restricting access from nonsecure zones, through internal web server access list, the web server can stop or slow denial of service (DoS) attacks on the web server. As the web server for the vRA Virtual Appliance Management Interface (vAMI), Lighttpd is the primary remote access management system for vRA. Lighttpd must be configured to restrict inbound connections from nonsecure zones. To accomplish this, the SSL engine must be enabled. The SSL engine forces Lighttpd to only listen via secure protocols.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /etc/haproxy/conf.d/20-vcac.cfg Navigate to the "frontend https-in" section. Review the "frontend https-in" section. Verify that the port 443 binding has the "ssl" keyword. Verify that port 80 is binded. Verify that non-ssl traffic is redirected to port 443. Note: Ports are binded with this statement: 'bind 0.0.0.0:<port>', where <port> is the binded port. Note: Non-ssl traffic is redirected with this statement: 'redirect scheme https if !{ ssl_fc }' Note: Ensure the redirection statement appears before all 'acl' statements. If the port 443 binding is missing the "ssl" keyword, OR port 80 is NOT binded, OR non-ssl traffic is NOT being redirected to port 443, this is a finding.

## Group: SRG-APP-000357-WSR-000150

**Group ID:** `V-240076`

### Rule: HAProxy must be configured to use syslog.

**Rule ID:** `SV-240076r879730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>There are many aspects of appropriate web server logging for security. Storage capacity must be adequate. ISSO and SA must receive warnings and alerts when storage capacity is filled to 75%. Writing events to a centralized management audit system offers many benefits to the enterprise over having dispersed logs. Centralized management of audit records and logs provides for efficiency in maintenance and management of records, enterprise analysis of events, and backup and archiving of event records enterprise-wide. The web server and related components are required to be capable of writing logs to centralized audit log servers. This requirement can be met by configuring the web server to utilize a dedicated log tool that meets this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /etc/haproxy/haproxy.cfg Navigate to the "globals" section. Verify that the "globals" section contains the "log" keyword, and that the "log" option contains the local0 syslog facility as its parameter. If properly configured, the "globals" section will contain the following: global log 127.0.0.1 local0 If the local0 syslog facility is not configured, this is a finding. Navigate to the "defaults" section. Verify that the "defaults" section contains the "log" keyword with the global value. Verify that an option keyword has been configured with the "httplog" value. If properly configured, the "defaults" section will contain the following: defaults log global option httplog Navigate to and open the following files: /etc/haproxy/conf.d/30-vro-config.cfg /etc/haproxy/conf.d/20-vcac.cfg Navigate to the each frontend section. Verify that the "log" keyword has not been set for each frontend. If the "log" keyword is present in a frontend, this is a finding. Navigate to and open /etc/rsyslog.d/vcac.conf. Review the configured syslog facilities and determine the location of the log file for the local0 syslog facility. If the local0 syslog facility does not refer to a valid log file, this is a finding. Navigate to and open the local0 syslog log file. Verify that HAProxy is logging start and stop events to the log file. If the log file is not recording HAProxy start and stop events, this is a finding.

## Group: SRG-APP-000358-WSR-000063

**Group ID:** `V-240077`

### Rule: HAProxy must not impede the ability to write specified log record content to an audit log server.

**Rule ID:** `SV-240077r879731_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Writing events to a centralized management audit system offers many benefits to the enterprise over having dispersed logs. Centralized management of audit records and logs provides for efficiency in maintenance and management of records, enterprise analysis of events, and backup and archiving of event records enterprise-wide. The web server and related components are required to be capable of writing logs to centralized audit log servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /etc/haproxy/haproxy.cfg Navigate to the "globals" section. Verify that the "globals" section contains the "log" keyword, and that the "log" option contains the local0 syslog facility as its parameter. If properly configured, the "globals" section will contain the following: global log 127.0.0.1 local0 If the local0 syslog facility is not configured, this is a finding. Navigate to the "defaults" section. Verify that the "defaults" section contains the "log" keyword with the global value. Verify that an option keyword has been configured with the "httplog" value. If properly configured, the "defaults" section will contain the following: defaults log global option httplog Navigate to and open the following files: /etc/haproxy/conf.d/30-vro-config.cfg /etc/haproxy/conf.d/20-vcac.cfg Navigate to the each frontend section. Verify that the "log" keyword has not been set for each frontend. If the "log" keyword is present in a frontend, this is a finding. Navigate to and open /etc/rsyslog.d/vcac.conf. Review the configured syslog facilities and determine the location of the log file for the local0 syslog facility. If the local0 syslog facility does not refer to a valid log file, this is a finding. Navigate to and open the local0 syslog log file. Verify that HAProxy is logging start and stop events to the log file. If the log file is not recording HAProxy start and stop events, this is a finding.

## Group: SRG-APP-000358-WSR-000163

**Group ID:** `V-240078`

### Rule: HAProxy must be configurable to integrate with an organizations security infrastructure.

**Rule ID:** `SV-240078r879731_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server will typically utilize logging mechanisms for maintaining a historical log of activity that occurs within a hosted application. This information can then be used for diagnostic purposes, forensics purposes, or other purposes relevant to ensuring the availability and integrity of the hosted application. While it is important to log events identified as being critical and relevant to security, it is equally important to notify the appropriate personnel in a timely manner so they are able to respond to events as they occur. Manual review of the web server logs may not occur in a timely manner, and each event logged is open to interpretation by a reviewer. By integrating the web server into an overall or organization-wide log review, a larger picture of events can be viewed, and analysis can be done in a timely and reliable manner.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /etc/haproxy/haproxy.cfg Navigate to the "globals" section. Verify that the "globals" section contains the "log" keyword, and that the "log" option contains the local0 syslog facility as its parameter. If properly configured, the "globals" section will contain the following: global log 127.0.0.1 local0 If the local0 syslog facility is not configured, this is a finding. Navigate to the "defaults" section. Verify that the "defaults" section contains the "log" keyword with the global value. Verify that an option keyword has been configured with the "httplog" value. If properly configured, the "defaults" section will contain the following: defaults log global option httplog Navigate to and open the following files: /etc/haproxy/conf.d/30-vro-config.cfg /etc/haproxy/conf.d/20-vcac.cfg Navigate to the each frontend section. Verify that the "log" keyword has not been set for each frontend. If the "log" keyword is present in a frontend, this is a finding. Navigate to and open /etc/rsyslog.d/vcac.conf. Review the configured syslog facilities and determine the location of the log file for the local0 syslog facility. If the local0 syslog facility does not refer to a valid log file, this is a finding. Navigate to and open the local0 syslog log file. Verify that HAProxy is logging start and stop events to the log file. If the log file is not recording HAProxy start and stop events, this is a finding.

## Group: SRG-APP-000374-WSR-000172

**Group ID:** `V-240079`

### Rule: HAProxy must use the httplog option.

**Rule ID:** `SV-240079r879747_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis across multiple devices and log records. Time stamps generated by the web server include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -E 'option\s+httplog' /etc/haproxy/haproxy.cfg If the command does not return a line, this is a finding.

## Group: SRG-APP-000380-WSR-000072

**Group ID:** `V-240080`

### Rule: HAProxy libraries, and configuration files must only be accessible to privileged users.

**Rule ID:** `SV-240080r879753_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can be modified through parameter modification, patch installation, upgrades to the web server or modules, and security parameter changes. With each of these changes, there is the potential for an adverse effect such as a DoS, web server instability, or hosted application instability. To limit changes to the web server and limit exposure to any adverse effects from the changes, files such as the web server application files, libraries, and configuration files must have permissions and ownership set properly to only allow privileged users access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -alR /etc/haproxy /etc/init.d/haproxy /usr/sbin/haproxy If any configuration or application files have permissions greater than "750" or are not owned by "root", this is a finding.

## Group: SRG-APP-000383-WSR-000175

**Group ID:** `V-240081`

### Rule: HAProxy psql-local frontend must be bound to port 5433.

**Rule ID:** `SV-240081r879756_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web servers provide numerous processes, features, and functionalities that utilize TCP/IP ports. Some of these processes may be deemed unnecessary or too unsecure to run on a production system. The HAProxy load balancer in the vRA appliance listens to port 5433 on behalf of the PostgreSQL service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'bind' /etc/haproxy/conf.d/10-psql.cfg If the value for bind is not set to 5433, this is a finding.

## Group: SRG-APP-000383-WSR-000175

**Group ID:** `V-240082`

### Rule: HAProxy vcac frontend must be bound to ports 80 and 443.

**Rule ID:** `SV-240082r879756_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web servers provide numerous processes, features, and functionalities that utilize TCP/IP ports. Some of these processes may be deemed unnecessary or too unsecure to run on a production system. The HAProxy load balancer in the vRA appliance listens to ports 80 and 443 on behalf of the vcac service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'bind' /etc/haproxy/conf.d/20-vcac.cfg If two lines are not returned, this is a finding. If the values for bind are not set to "80" and to "443", this is a finding.

## Group: SRG-APP-000383-WSR-000175

**Group ID:** `V-240083`

### Rule: HAProxy vro frontend must be bound to the correct port 8283.

**Rule ID:** `SV-240083r879756_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web servers provide numerous processes, features, and functionalities that utilize TCP/IP ports. Some of these processes may be deemed unnecessary or too unsecure to run on a production system. The HAProxy load balancer in the vRA appliance listens to ports 8283 on behalf of the vro configuration service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep 'bind' /etc/haproxy/conf.d/30-vro-config.cfg If the value for bind is not set to "8283", this is a finding.

## Group: SRG-APP-000416-WSR-000118

**Group ID:** `V-240084`

### Rule: HAProxy must be configured with FIPS 140-2 compliant ciphers for https connections.

**Rule ID:** `SV-240084r879944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Transport Layer Security (TLS) is optional for a public web server. However, if authentication is being performed, then the use of the TLS protocol is required. Without the use of TLS, the authentication data would be transmitted unencrypted and would become vulnerable to disclosure. Using TLS along with DoD PKI certificates for encryption of the authentication data protects the information from being accessed by all parties on the network. To further protect the authentication data, the web server must use a FIPS 140-2 approved TLS version and all non-FIPS-approved SSL versions must be disabled. FIPS 140-2 approved TLS versions include TLS V1.0 or greater. NIST SP 800-52 specifies the preferred configurations for government systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -En 'ciphers' /etc/haproxy/conf.d/*.cfg If two lines are not returned, this is a finding. If the values for "ciphers" are not set to "FIPS:+3DES:!aNULL", this is a finding.

## Group: SRG-APP-000435-WSR-000147

**Group ID:** `V-240085`

### Rule: HAProxy must be protected from being stopped by a non-privileged user.

**Rule ID:** `SV-240085r879806_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An attacker has at least two reasons to stop a web server. The first is to cause a DoS, and the second is to put in place changes the attacker made to the web server configuration. To prohibit an attacker from stopping the HAProxy process must be owned by "root".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ps aux -U root | grep '[h]aproxy' If the command does not return a line, this is a finding.

## Group: SRG-APP-000439-WSR-000151

**Group ID:** `V-240086`

### Rule: HAProxy must be configured to use SSL/TLS.

**Rule ID:** `SV-240086r928837_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data exchanged between the user and the web server can range from static display data to credentials used to log into the hosted application. Even when data appears to be static, the non-displayed logic in a web page may expose business logic or trusted system relationships. The integrity of all the data being exchanged between the user and web server must always be trusted. To protect the integrity and trust, encryption methods should be used to protect the complete communication session. In order to protect the integrity and confidentiality of the remote sessions, HAProxy uses SSL/TLS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line execute the following command: grep -En '\sssl\s' /etc/haproxy/conf.d/*.cfg If the command does not return the two lines below, this is a finding. /etc/haproxy/conf.d/20-vcac.cfg:4: bind 0.0.0.0:443 ssl crt /etc/apache2/server.pem ciphers FIPS:+3DES:!aNULL no-sslv3 /etc/haproxy/conf.d/30-vro-config.cfg:2: bind :8283 ssl crt /opt/vmware/etc/lighttpd/server.pem ciphers FIPS:+3DES:!aNULL no-sslv3

## Group: SRG-APP-000439-WSR-000152

**Group ID:** `V-240087`

### Rule: HAProxy session IDs must be sent to the client using SSL/TLS.

**Rule ID:** `SV-240087r879810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The HTTP protocol is a stateless protocol. To maintain a session, a session identifier is used. The session identifier is a piece of data that is used to identify a session and a user. If the session identifier is compromised by an attacker, the session can be hijacked. By encrypting the session identifier, the identifier becomes more difficult for an attacker to hijack, decrypt, and use before the session has expired. In order to protect the integrity and confidentiality of the remote sessions, HAProxy uses SSL/TLS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line execute the following command: grep -En '\sssl\s' /etc/haproxy/conf.d/*.cfg If the command does not return the two lines below, this is a finding. /etc/haproxy/conf.d/20-vcac.cfg:4: bind 0.0.0.0:443 ssl crt /etc/apache2/server.pem ciphers FIPS:+3DES:!aNULL no-sslv3 /etc/haproxy/conf.d/30-vro-config.cfg:2: bind :8283 ssl crt /opt/vmware/etc/lighttpd/server.pem ciphers FIPS:+3DES:!aNULL no-sslv3

## Group: SRG-APP-000439-WSR-000156

**Group ID:** `V-240088`

### Rule: HAProxy must set the no-sslv3 value on all client ports.

**Rule ID:** `SV-240088r879810_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Transport Layer Security (TLS) is a required transmission protocol for a web server hosting controlled information. The use of TLS provides confidentiality of data in transit between the web server and client. FIPS 140-2 approved TLS versions must be enabled and non-FIPS-approved SSL versions must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -EnR '\bbind\b.*\bssl\b' /etc/haproxy Verify that each returned line contains the no-sslv3 value. If any lines do not have this value, this is a finding.

## Group: SRG-APP-000439-WSR-000188

**Group ID:** `V-240089`

### Rule: HAProxy must remove all export ciphers.

**Rule ID:** `SV-240089r879810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>During the initial setup of a Transport Layer Security (TLS) connection to the web server, the client sends a list of supported cipher suites in order of preference. The web server will reply with the cipher suite it will use for communication from the client list. If an attacker can intercept the submission of cipher suites to the web server and place, as the preferred cipher suite, a weak export suite, the encryption used for the session becomes easy for the attacker to break, often within minutes to hours.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line execute the following command: grep -En '\sssl\s' /etc/haproxy/conf.d/*.cfg If the command does not return the two lines below, this is a finding. /etc/haproxy/conf.d/20-vcac.cfg:4: bind 0.0.0.0:443 ssl crt /etc/apache2/server.pem ciphers FIPS:+3DES:!aNULL no-sslv3 /etc/haproxy/conf.d/30-vro-config.cfg:2: bind :8283 ssl crt /opt/vmware/etc/lighttpd/server.pem ciphers FIPS:+3DES:!aNULL no-sslv3

## Group: SRG-APP-000442-WSR-000182

**Group ID:** `V-240090`

### Rule: HAProxy must maintain the confidentiality and integrity of information during reception.

**Rule ID:** `SV-240090r879813_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data exchanged between the user and the web server can range from static display data to credentials used to log into the hosted application. Even when data appears to be static, the non-displayed logic in a web page may expose business logic or trusted system relationships. The integrity of all the data being exchanged between the user and web server must always be trusted. To protect the integrity and trust, encryption methods should be used to protect the complete communication session. In order to protect the integrity and confidentiality of the remote sessions, HAProxy uses SSL/TLS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line execute the following command: grep -En '\sssl\s' /etc/haproxy/conf.d/*.cfg If the command does not return the two lines below, this is a finding. /etc/haproxy/conf.d/20-vcac.cfg:4: bind 0.0.0.0:443 ssl crt /etc/apache2/server.pem ciphers FIPS:+3DES:!aNULL no-sslv3 /etc/haproxy/conf.d/30-vro-config.cfg:2: bind :8283 ssl crt /opt/vmware/etc/lighttpd/server.pem ciphers FIPS:+3DES:!aNULL no-sslv3

## Group: SRG-APP-000456-WSR-000187

**Group ID:** `V-240091`

### Rule: HAProxy must have the latest approved security-relevant software updates installed.

**Rule ID:** `SV-240091r879827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All vRA components, to include Lighttpd, are under VMware configuration management control. The CM process ensures that all patches, functions, and modules have been thoroughly tested before being introduced into the production version. By using the most current version of Lighttpd, the Lighttpd server will always be using the most stable and known baseline.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSO. Determine whether HAProxy has the latest approved security-relevant software updates and updates are installed within the identified time period. If the latest approved security-relevant software updates are not installed or installed within the identified time period, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-240092`

### Rule: HAProxy must set the maxconn value.

**Rule ID:** `SV-240092r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the total number of connections that a server is allowed to open prevents an attacker from overloading a web server. Overloading the server will prevent it from managing other tasks besides serving web requests. This setting works together with per-client limits to mitigate against DDoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line execute the following command: grep maxconn /etc/haproxy/haproxy.cfg If the "maxconn" value is not set to "32768", this is a finding.

## Group: SRG-APP-000456-WSR-000187

**Group ID:** `V-258451`

### Rule: The version of vRealize Automation 7.x HA Proxy running on the system must be a supported version.

**Rule ID:** `SV-258451r928881_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions used to install patches across the enclave and to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs). </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
vRealize Automation 7.x HA Proxy is no longer supported by the vendor. If the system is running vRealize Automation 7.x HA Proxy, this is a finding.

