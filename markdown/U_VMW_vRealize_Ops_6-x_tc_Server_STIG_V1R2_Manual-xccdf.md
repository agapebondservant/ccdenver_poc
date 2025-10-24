# STIG Benchmark: VMware vRealize Operations Manager 6.x tc Server Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-241573`

### Rule: tc Server UI must limit the number of maximum concurrent connections permitted.

**Rule ID:** `SV-241573r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Resource exhaustion can occur when an unlimited number of concurrent requests are allowed on a website, facilitating a denial-of-service attack. Mitigating this kind of attack will include limiting the number of concurrent HTTP/HTTPS requests. Mitigating this kind of attack will include limiting the number of concurrent HTTP/HTTPS requests. Each incoming request requires a thread for the duration of that request. If more simultaneous requests are received than can be handled by the currently available request processing threads, additional threads will be created up to the value of the “maxThreads” attribute.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep maxThreads /usr/lib/vmware-vcops/tomcat-web-app/conf/server.xml If the value of “maxThreads” is not “300” or is missing, this is a finding.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-241574`

### Rule: tc Server CaSa must limit the number of maximum concurrent connections permitted.

**Rule ID:** `SV-241574r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Resource exhaustion can occur when an unlimited number of concurrent requests are allowed on a website, facilitating a denial-of-service attack. Mitigating this kind of attack will include limiting the number of concurrent HTTP/HTTPS requests. Mitigating this kind of attack will include limiting the number of concurrent HTTP/HTTPS requests. Each incoming request requires a thread for the duration of that request. If more simultaneous requests are received than can be handled by the currently available request processing threads, additional threads will be created up to the value of the “maxThreads” attribute.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep maxThreads /usr/lib/vmware-casa/casa-webapp/conf/server.xml If the value of “maxThreads” is not “300” or is missing, this is a finding.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-241575`

### Rule: tc Server API must limit the number of maximum concurrent connections permitted.

**Rule ID:** `SV-241575r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Resource exhaustion can occur when an unlimited number of concurrent requests are allowed on a website, facilitating a denial-of-service attack. Mitigating this kind of attack will include limiting the number of concurrent HTTP/HTTPS requests. Mitigating this kind of attack will include limiting the number of concurrent HTTP/HTTPS requests. Each incoming request requires a thread for the duration of that request. If more simultaneous requests are received than can be handled by the currently available request processing threads, additional threads will be created up to the value of the “maxThreads” attribute.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep maxThreads /usr/lib/vmware-vcops/tomcat-enterprise/conf/server.xml If the value of “maxThreads” is not “300” or is missing, this is a finding.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-241576`

### Rule: tc Server UI must limit the amount of time that each TCP connection is kept alive.

**Rule ID:** `SV-241576r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Denial of Service is one threat against web servers. Many DoS attacks attempt to consume web server resources in such a way that no more resources are available to satisfy legitimate requests. Mitigation against these threats is to take steps to limit the number of resources that can be consumed in certain ways. tc Server provides the “connectionTimeout” attribute. This sets the number of milliseconds tc Server will wait, after accepting a connection, for the request URI line to be presented. This timeout will also be used when reading the request body (if any).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-web-app/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “connectionTimeout” is not set to “20000” or is missing, this is a finding.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-241577`

### Rule: tc Server CaSa must limit the amount of time that each TCP connection is kept alive.

**Rule ID:** `SV-241577r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Denial of Service is one threat against web servers. Many DoS attacks attempt to consume web server resources in such a way that no more resources are available to satisfy legitimate requests. Mitigation against these threats is to take steps to limit the number of resources that can be consumed in certain ways. tc Server provides the “connectionTimeout” attribute. This sets the number of milliseconds tc Server will wait, after accepting a connection, for the request URI line to be presented. This timeout will also be used when reading the request body (if any).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-casa/casa-webapp/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “connectionTimeout” is not set to “20000” or is missing, this is a finding.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-241578`

### Rule: tc Server API must limit the amount of time that each TCP connection is kept alive.

**Rule ID:** `SV-241578r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Denial of Service is one threat against web servers. Many DoS attacks attempt to consume web server resources in such a way that no more resources are available to satisfy legitimate requests. Mitigation against these threats is to take steps to limit the number of resources that can be consumed in certain ways. tc Server provides the “connectionTimeout” attribute. This sets the number of milliseconds tc Server will wait, after accepting a connection, for the request URI line to be presented. This timeout will also be used when reading the request body (if any).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-enterprise/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “connectionTimeout” is not set to “20000” or is missing, this is a finding.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-241579`

### Rule: tc Server UI must limit the number of times that each TCP connection is kept alive.

**Rule ID:** `SV-241579r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>KeepAlive provides long-lived HTTP sessions that allow multiple requests to be sent over the same connection. Enabling KeepAlive mitigates the effects of several types of denial-of-service attacks. An advantage of KeepAlive is the reduced latency in subsequent requests (no handshaking). However, a disadvantage is that server resources are not available to handle other requests while a connection is maintained between the server and the client. tc Server can be configured to limit the number of subsequent requests that one client can submit to the server over an established connection. This limit helps provide a balance between the advantages of KeepAlive, while not allowing any one connection being held too long by any one client. “maxKeepAliveRequests” is the tc Server attribute which sets this limit.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-web-app/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “maxKeepAliveRequests” is not set to “15” or is missing, this is a finding.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-241580`

### Rule: tc Server CaSa must limit the number of times that each TCP connection is kept alive.

**Rule ID:** `SV-241580r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>KeepAlive provides long-lived HTTP sessions that allow multiple requests to be sent over the same connection. Enabling KeepAlive mitigates the effects of several types of denial-of-service attacks. An advantage of KeepAlive is the reduced latency in subsequent requests (no handshaking). However, a disadvantage is that server resources are not available to handle other requests while a connection is maintained between the server and the client. tc Server can be configured to limit the number of subsequent requests that one client can submit to the server over an established connection. This limit helps provide a balance between the advantages of KeepAlive, while not allowing any one connection being held too long by any one client. “maxKeepAliveRequests” is the tc Server attribute that sets this limit.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-casa/casa-webapp/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “maxKeepAliveRequests” is not set to “15” or is missing, this is a finding.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-241581`

### Rule: tc Server API must limit the number of times that each TCP connection is kept alive.

**Rule ID:** `SV-241581r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>KeepAlive provides long-lived HTTP sessions that allow multiple requests to be sent over the same connection. Enabling KeepAlive mitigates the effects of several types of denial-of-service attacks. An advantage of KeepAlive is the reduced latency in subsequent requests (no handshaking). However, a disadvantage is that server resources are not available to handle other requests while a connection is maintained between the server and the client. tc Server can be configured to limit the number of subsequent requests that one client can submit to the server over an established connection. This limit helps provide a balance between the advantages of KeepAlive, while not allowing any one connection being held too long by any one client. “maxKeepAliveRequests” is the tc Server attribute that sets this limit.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-enterprise/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “maxKeepAliveRequests” is not set to “15” or is missing, this is a finding.

## Group: SRG-APP-000001-WSR-000002

**Group ID:** `V-241582`

### Rule: tc Server UI must perform server-side session management.

**Rule ID:** `SV-241582r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cookies are a common way to save session state over the HTTP(S) protocol. If an attacker can compromise session data stored in a cookie, they are better able to launch an attack against the server and its applications. Session cookies stored on the server are more secure than cookies stored on the client. Therefore, tc Server must be configured correctly in order to generate and manage session cookies on the server. Managing cookies on the server provides a layer of defense to vRealize Operations. By default, tc Server is designed to manage cookies on the server. However, incorrect configuration can turn off the default feature.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -E 'cookies=.false' /usr/lib/vmware-vcops/tomcat-web-app/conf/context.xml If the command produces any output, this is a finding.

## Group: SRG-APP-000001-WSR-000002

**Group ID:** `V-241583`

### Rule: tc Server CaSa must perform server-side session management.

**Rule ID:** `SV-241583r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cookies are a common way to save session state over the HTTP(S) protocol. If an attacker can compromise session data stored in a cookie, they are better able to launch an attack against the server and its applications. Session cookies stored on the server are more secure than cookies stored on the client. Therefore, tc Server must be configured correctly in order to generate and manage session cookies on the server. Managing cookies on the server provides a layer of defense to vRealize Automation. By default, tc Server is designed to manage cookies on the server. However, incorrect configuration can turn off the default feature.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -E 'cookies=.false' /usr/lib/vmware-casa/casa-webapp/conf/context.xml If the command produces any output, this is a finding.

## Group: SRG-APP-000001-WSR-000002

**Group ID:** `V-241584`

### Rule: tc Server API must perform server-side session management.

**Rule ID:** `SV-241584r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cookies are a common way to save session state over the HTTP(S) protocol. If an attacker can compromise session data stored in a cookie, they are better able to launch an attack against the server and its applications. Session cookies stored on the server are more secure than cookies stored on the client. Therefore, tc Server must be configured correctly in order to generate and manage session cookies on the server. Managing cookies on the server provides a layer of defense to vRealize Automation. By default, tc Server is designed to manage cookies on the server. However, incorrect configuration can turn off the default feature.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -E 'cookies=.false' /usr/lib/vmware-vcops/tomcat-enterprise/conf/context.xml If the command produces any output, this is a finding.

## Group: SRG-APP-000014-WSR-000006

**Group ID:** `V-241585`

### Rule: tc Server UI must be configured with FIPS 140-2 compliant ciphers for HTTPS connections.

**Rule ID:** `SV-241585r879519_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption of data-in-flight is an essential element of protecting information confidentiality. If a web server uses weak or outdated encryption algorithms, then the server's communications can potentially be compromised. The US Federal Information Processing Standards (FIPS) publication 140-2, Security Requirements for Cryptographic Modules (FIPS 140-2) identifies eleven areas for a cryptographic module used inside a security system that protects information. FIPS 140-2- approved ciphers provide the maximum level of encryption possible for a private web server. Configuration of ciphers used by tc Server are set in the “catalina.properties” file. Only those ciphers specified in the configuration file, and which are available in the installed OpenSSL library, will be used by tc Server while encrypting data for transmission.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep vmware-ssl.ssl.ciphers.list /usr/lib/vmware-vcops/tomcat-web-app/conf/catalina.properties If the value of “vmware-ssl.ssl.ciphers.list” does not match the list of FIPS 140-2 ciphers or is missing, this is a finding. Note: To view a list of FIPS 140-2 ciphers, at the command prompt execute the following command: openssl ciphers 'FIPS'

## Group: SRG-APP-000014-WSR-000006

**Group ID:** `V-241586`

### Rule: tc Server CaSa must be configured with FIPS 140-2 compliant ciphers for HTTPS connections.

**Rule ID:** `SV-241586r879519_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption of data-in-flight is an essential element of protecting information confidentiality. If a web server uses weak or outdated encryption algorithms, then the server's communications can potentially be compromised. The US Federal Information Processing Standards (FIPS) publication 140-2, Security Requirements for Cryptographic Modules (FIPS 140-2) identifies eleven areas for a cryptographic module used inside a security system that protects information. FIPS 140-2- approved ciphers provide the maximum level of encryption possible for a private web server. Configuration of ciphers used by tc Server are set in the “catalina.properties” file. Only those ciphers specified in the configuration file, and which are available in the installed OpenSSL library, will be used by tc Server while encrypting data for transmission.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -A 10 vmware-casa.ssl.ciphers.list /usr/lib/vmware-casa/casa-webapp/conf/catalina.properties If the value of “vmware-casa.ssl.ciphers.list” does not match the list of FIPS 140-2 ciphers or is missing, this is a finding. Note: To view a list of FIPS 140-2 ciphers, at the command prompt execute the following command: openssl ciphers 'FIPS'

## Group: SRG-APP-000014-WSR-000006

**Group ID:** `V-241587`

### Rule: tc Server API must be configured with FIPS 140-2 compliant ciphers for HTTPS connections.

**Rule ID:** `SV-241587r879519_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption of data-in-flight is an essential element of protecting information confidentiality. If a web server uses weak or outdated encryption algorithms, then the server's communications can potentially be compromised. The US Federal Information Processing Standards (FIPS) publication 140-2, Security Requirements for Cryptographic Modules (FIPS 140-2) identifies eleven areas for a cryptographic module used inside a security system that protects information. FIPS 140-2-approved ciphers provide the maximum level of encryption possible for a private web server. Configuration of ciphers used by tc Server are set in the “catalina.properties” file. Only those ciphers specified in the configuration file, and which are available in the installed OpenSSL library, will be used by tc Server while encrypting data for transmission.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep vmware-ssl.ssl.ciphers.list /usr/lib/vmware-vcops/tomcat-enterprise/conf/catalina.properties If the value of “vmware-ssl.ssl.ciphers.list” does not match the list of FIPS 140-2 ciphers or is missing, this is a finding. Note: To view a list of FIPS 140-2 ciphers, at the command prompt execute the following command: openssl ciphers 'FIPS'

## Group: SRG-APP-000015-WSR-000014

**Group ID:** `V-241588`

### Rule: tc Server UI must use cryptography to protect the integrity of remote sessions.

**Rule ID:** `SV-241588r879520_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data exchanged between the user and the web server can range from static display data to credentials used to log into the hosted application. Even when data appears to be static, the non-displayed logic in a web page may expose business logic or trusted system relationships. The integrity of all the data being exchanged between the user and web server must always be trusted. To protect the integrity and trust, encryption methods should be used to protect the complete communication session. HTTP connections in tc Server are managed through the Connector object. Setting the Connector's “SSLEnabled” flag, SSL handshake/encryption/decryption is enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-web-app/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “SSLEnabled” is not set to “true” or is missing, this is a finding.

## Group: SRG-APP-000015-WSR-000014

**Group ID:** `V-241589`

### Rule: tc Server CaSa must use cryptography to protect the integrity of remote sessions.

**Rule ID:** `SV-241589r879520_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data exchanged between the user and the web server can range from static display data to credentials used to log into the hosted application. Even when data appears to be static, the non-displayed logic in a web page may expose business logic or trusted system relationships. The integrity of all the data being exchanged between the user and web server must always be trusted. To protect the integrity and trust, encryption methods should be used to protect the complete communication session. HTTP connections in tc Server are managed through the Connector object. Setting the Connector's “SSLEnabled” flag, SSL handshake/encryption/decryption is enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-casa/casa-webapp/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “SSLEnabled” is not set to “true” or is missing, this is a finding.

## Group: SRG-APP-000015-WSR-000014

**Group ID:** `V-241590`

### Rule: tc Server API must use cryptography to protect the integrity of remote sessions.

**Rule ID:** `SV-241590r879520_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data exchanged between the user and the web server can range from static display data to credentials used to log into the hosted application. Even when data appears to be static, the non-displayed logic in a web page may expose business logic or trusted system relationships. The integrity of all the data being exchanged between the user and web server must always be trusted. To protect the integrity and trust, encryption methods should be used to protect the complete communication session. HTTP connections in tc Server are managed through the Connector object. Setting the Connector's “SSLEnabled” flag, SSL handshake/encryption/decryption is enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-enterprise/conf/server.xml. Navigate to the <Connector> node that contains 'port="${vmware-ssl.https.port}"'. If the value of “SSLEnabled” is not set to “true” or is missing, this is a finding.

## Group: SRG-APP-000016-WSR-000005

**Group ID:** `V-241591`

### Rule: tc Server UI must record user access in a format that enables monitoring of remote access.

**Rule ID:** `SV-241591r879521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access can be exploited by an attacker to compromise the server. By recording all remote access activities, it will be possible to determine the attacker's location, intent, and degree of success. As a Tomcat derivative, tc Server can be configured with an “AccessLogValve”. A Valve element represents a component that can be inserted into the request processing pipeline. The Access Log Valve creates log files in the same format as those created by standard web servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-web-app/conf/server.xml. Navigate to the <Host> node. Verify that the node contains a <Valve className="org.apache.catalina.valves.AccessLogValve"> node. If an “AccessLogValve” is not configured correctly or is missing, this is a finding. Note: The “AccessLogValve” should be configured as follows: <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs" pattern="%h %l %u %t &quot;%r&quot; %s %b" prefix="localhost_access_log." suffix=".txt"/>

## Group: SRG-APP-000016-WSR-000005

**Group ID:** `V-241592`

### Rule: tc Server CaSa must record user access in a format that enables monitoring of remote access.

**Rule ID:** `SV-241592r879521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access can be exploited by an attacker to compromise the server. By recording all remote access activities, it will be possible to determine the attacker's location, intent, and degree of success. As a Tomcat derivative, tc Server can be configured with an “AccessLogValve”. A Valve element represents a component that can be inserted into the request processing pipeline. The Access Log Valve creates log files in the same format as those created by standard web servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-casa/casa-webapp/conf/server.xml. Navigate to the <Host> node. Verify that the node contains a <Valve className="org.apache.catalina.valves.AccessLogValve"> node. If an “AccessLogValve” is not configured correctly or is missing, this is a finding. Note: The “AccessLogValve” should be configured as follows: <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs" pattern="%h %l %u %t &quot;%r&quot; %s %b" prefix="localhost_access_log." suffix=".txt"/>

## Group: SRG-APP-000016-WSR-000005

**Group ID:** `V-241593`

### Rule: tc Server API must record user access in a format that enables monitoring of remote access.

**Rule ID:** `SV-241593r879521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access can be exploited by an attacker to compromise the server. By recording all remote access activities, it will be possible to determine the attacker's location, intent, and degree of success. As a Tomcat derivative, tc Server can be configured with an “AccessLogValve”. A Valve element represents a component that can be inserted into the request processing pipeline. The Access Log Valve creates log files in the same format as those created by standard web servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-enterprise/conf/server.xml. Navigate to the <Host> node. Verify that the node contains a <Valve className="org.apache.catalina.valves.AccessLogValve"> node. If an “AccessLogValve” is not configured correctly or is missing, this is a finding. Note: The “AccessLogValve” should be configured as follows: <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs" pattern="%h %l %u %t &quot;%r&quot; %s %b" prefix="localhost_access_log." suffix=".txt"/>

## Group: SRG-APP-000089-WSR-000047

**Group ID:** `V-241594`

### Rule: tc Server ALL must generate log records for system startup and shutdown.

**Rule ID:** `SV-241594r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Logging must be started as soon as possible when a service starts and when a service is stopped. Many forms of suspicious actions can be detected by analyzing logs for unexpected service starts and stops. Also, by starting to log immediately after a service starts, it becomes more difficult for suspicious activity to go un-logged. During start, tc Server reports system messages onto STDOUT and STDERR. These messages will be logged if the initialization script is configured correctly. For historical reasons, the standard log file for this is called “catalina.out”.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: more /storage/log/vcops/log/product-ui/catalina.out Verify that tc Server start and stop events are being logged. If the tc Server start and stop events are not being recorded, this is a finding. Note: The tc Server service is referred to as Catalina in the log.

## Group: SRG-APP-000089-WSR-000047

**Group ID:** `V-241595`

### Rule: tc Server UI must generate log records for user access and authentication events.

**Rule ID:** `SV-241595r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log records can be generated from various components within the web server (e.g., httpd, plug-ins to external backends, etc.). From a web server perspective, certain specific web server functionalities may be logged as well. The web server must allow the definition of what events are to be logged. As conditions change, the number and types of events to be logged may change, and the web server must be able to facilitate these changes. As a Tomcat derivative, tc Server can be configured with an “AccessLogValve”. A Valve element represents a component that can be inserted into the request processing pipeline. The pattern attribute of the “AccessLogValve” controls which data gets logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-web-app/conf/server.xml. Navigate to the <Host> node. Verify that the node contains a <Valve className="org.apache.catalina.valves.AccessLogValve"> node. If an “AccessLogValve” is not configured correctly or is missing, this is a finding. Note: The “AccessLogValve” should be configured as follows: <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs" pattern="%h %l %u %t &quot;%r&quot; %s %b" prefix="localhost_access_log." suffix=".txt"/>

## Group: SRG-APP-000089-WSR-000047

**Group ID:** `V-241596`

### Rule: tc Server CaSa must generate log records for user access and authentication events.

**Rule ID:** `SV-241596r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log records can be generated from various components within the web server (e.g., httpd, plug-ins to external backends, etc.). From a web server perspective, certain specific web server functionalities may be logged as well. The web server must allow the definition of what events are to be logged. As conditions change, the number and types of events to be logged may change, and the web server must be able to facilitate these changes. As a Tomcat derivative, tc Server can be configured with an “AccessLogValve”. A Valve element represents a component that can be inserted into the request processing pipeline. The pattern attribute of the “AccessLogValve” controls which data gets logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-casa/casa-webapp/conf/server.xml. Navigate to the <Host> node. Verify that the node contains a <Valve className="org.apache.catalina.valves.AccessLogValve"> node. If an “AccessLogValve” is not configured correctly or is missing, this is a finding. Note: The “AccessLogValve” should be configured as follows: <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs" pattern="%h %l %u %t &quot;%r&quot; %s %b" prefix="localhost_access_log." suffix=".txt"/>

## Group: SRG-APP-000089-WSR-000047

**Group ID:** `V-241597`

### Rule: tc Server API must generate log records for user access and authentication events.

**Rule ID:** `SV-241597r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log records can be generated from various components within the web server (e.g., httpd, plug-ins to external backends, etc.). From a web server perspective, certain specific web server functionalities may be logged as well. The web server must allow the definition of what events are to be logged. As conditions change, the number and types of events to be logged may change, and the web server must be able to facilitate these changes. As a Tomcat derivative, tc Server can be configured with an “AccessLogValve”. A Valve element represents a component that can be inserted into the request processing pipeline. The pattern attribute of the “AccessLogValve” controls which data gets logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-enterprise/conf/server.xml. Navigate to the <Host> node. Verify that the node contains a <Valve className="org.apache.catalina.valves.AccessLogValve"> node. If an “AccessLogValve” is not configured correctly or is missing, this is a finding. Note: The “AccessLogValve” should be configured as follows: <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs" pattern="%h %l %u %t &quot;%r&quot; %s %b" prefix="localhost_access_log." suffix=".txt"/>

## Group: SRG-APP-000092-WSR-000055

**Group ID:** `V-241598`

### Rule: tc Server ALL must initiate logging during service start-up.

**Rule ID:** `SV-241598r879562_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An attacker can compromise a web server during the startup process. If logging is not initiated until all the web server processes are started, key information may be missed and not available during a forensic investigation. To assure all logable events are captured, the web server must begin logging once the first web server process is initiated. During start, tc Server reports system messages onto STDOUT and STDERR. These messages will be logged if the initialization script is configured correctly. For historical reasons, the standard log file for this is called “catalina.out”.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: more /opt/pivotal/pivotal-tc-server-standard/tomcat-7.0.57.B.RELEASE/bin/catalina.sh Type /touch "$CATALINA_OUT" Verify that the start command contains the command ">> "$CATALINA_OUT" 2>&1 "&"" If the command is not correct or is missing, this is a finding. Note: Use the Enter key to scroll down after typing /touch "$CATALINA_OUT"

## Group: SRG-APP-000095-WSR-000056

**Group ID:** `V-241599`

### Rule: tc Server UI must produce log records containing sufficient information to establish what type of events occurred.

**Rule ID:** `SV-241599r879563_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>After a security incident has occurred, investigators will often review log files to determine what happened. Understanding what type of event occurred is critical for investigation of a suspicious event. Like all servers, tc Server will typically process “GET” and “POST” requests clients. These will help investigators understand what happened.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/product-ui/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If HTTP "GET" and/or "POST" events are not being recorded, this is a finding.

## Group: SRG-APP-000095-WSR-000056

**Group ID:** `V-241600`

### Rule: tc Server CaSa must produce log records containing sufficient information to establish what type of events occurred.

**Rule ID:** `SV-241600r879563_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>After a security incident has occurred, investigators will often review log files to determine what happened. Understanding what type of event occurred is critical for investigation of a suspicious event. Like all servers, tc Server will typically process “GET” and “POST” requests clients. These will help investigators understand what happened.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/casa/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If HTTP "GET" and/or "POST" events are not being recorded, this is a finding.

## Group: SRG-APP-000095-WSR-000056

**Group ID:** `V-241601`

### Rule: tc Server API must produce log records containing sufficient information to establish what type of events occurred.

**Rule ID:** `SV-241601r879563_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>After a security incident has occurred, investigators will often review log files to determine what happened. Understanding what type of event occurred is critical for investigation of a suspicious event. Like all servers, tc Server will typically process “GET” and “POST” requests clients. These will help investigators understand what happened.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/suite-api/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If HTTP "GET" and/or "POST" events are not being recorded, this is a finding.

## Group: SRG-APP-000096-WSR-000057

**Group ID:** `V-241602`

### Rule: tc Server UI must produce log records containing sufficient information to establish when (date and time) events occurred.

**Rule ID:** `SV-241602r879564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>After a security incident has occurred, investigators will often review log files to determine when events occurred. Understanding the precise sequence of events is critical for investigation of a suspicious event. As a Tomcat derivative, tc Server can be configured with an “AccessLogValve. A Valve element represents a component that can be inserted into the request processing pipeline. The pattern attribute of the “AccessLogValve” controls which data gets logged. The “%t” parameter specifies that the system time should be recorded.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/product-ui/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If the time and date of events are not being recorded, this is a finding.

## Group: SRG-APP-000096-WSR-000057

**Group ID:** `V-241603`

### Rule: tc Server CaSa must produce log records containing sufficient information to establish when (date and time) events occurred.

**Rule ID:** `SV-241603r879564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>After a security incident has occurred, investigators will often review log files to determine when events occurred. Understanding the precise sequence of events is critical for investigation of a suspicious event. As a Tomcat derivative, tc Server can be configured with an “AccessLogValve”. A Valve element represents a component that can be inserted into the request processing pipeline. The pattern attribute of the “AccessLogValve” controls which data gets logged. The “%t” parameter specifies that the system time should be recorded.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/casa/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If the time and date of events are not being recorded, this is a finding.

## Group: SRG-APP-000096-WSR-000057

**Group ID:** `V-241604`

### Rule: tc Server API must produce log records containing sufficient information to establish when (date and time) events occurred.

**Rule ID:** `SV-241604r879564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>After a security incident has occurred, investigators will often review log files to determine when events occurred. Understanding the precise sequence of events is critical for investigation of a suspicious event. As a Tomcat derivative, tc Server can be configured with an “AccessLogValve”. A Valve element represents a component that can be inserted into the request processing pipeline. The pattern attribute of the “AccessLogValve” controls which data gets logged. The “%t” parameter specifies that the system time should be recorded.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/suite-api/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If the time and date of events are not being recorded, this is a finding.

## Group: SRG-APP-000097-WSR-000058

**Group ID:** `V-241605`

### Rule: tc Server UI must produce log records containing sufficient information to establish where within the web server the events occurred.

**Rule ID:** `SV-241605r879565_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>After a security incident has occurred, investigators will often review log files to determine what happened. tc Server HORIZON must create a log entry when a user accesses the system and the system authenticates users. The logs must contain information about user sessions to include what type of event occurred, when (date and time) events occurred, where within the server the events occurred, the client source of the events, the outcome (success or failure) of the event, the identity of the user/subject/process associated with the event. Like all web servers, tc Server will log the requested URL and the parameters, if any, sent in the request. This information will enable investigators to determine where in the server an action was requested.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/product-ui/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If the location of events are not being recorded, this is a finding.

## Group: SRG-APP-000097-WSR-000058

**Group ID:** `V-241606`

### Rule: tc Server CaSa must produce log records containing sufficient information to establish where within the web server the events occurred.

**Rule ID:** `SV-241606r879565_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>After a security incident has occurred, investigators will often review log files to determine what happened. tc Server HORIZON must create a log entry when a user accesses the system and the system authenticates users. The logs must contain information about user sessions to include what type of event occurred, when (date and time) events occurred, where within the server the events occurred, the client source of the events, the outcome (success or failure) of the event, the identity of the user/subject/process associated with the event. Like all web servers, tc Server will log the requested URL and the parameters, if any, sent in the request. This information will enable investigators to determine where in the server an action was requested.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/casa/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If the location of events are not being recorded, this is a finding.

## Group: SRG-APP-000097-WSR-000058

**Group ID:** `V-241607`

### Rule: tc Server API must produce log records containing sufficient information to establish where within the web server the events occurred.

**Rule ID:** `SV-241607r879565_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>After a security incident has occurred, investigators will often review log files to determine what happened. tc Server HORIZON must create a log entry when a user accesses the system and the system authenticates users. The logs must contain information about user sessions to include what type of event occurred, when (date and time) events occurred, where within the server the events occurred, the client source of the events, the outcome (success or failure) of the event, the identity of the user/subject/process associated with the event. Like all web servers, tc Server will log the requested URL and the parameters, if any, sent in the request. This information will enable investigators to determine where in the server an action was requested.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/suite-api/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If the location of events are not being recorded, this is a finding.

## Group: SRG-APP-000098-WSR-000059

**Group ID:** `V-241608`

### Rule: tc Server UI must produce log records containing sufficient information to establish the source of events.

**Rule ID:** `SV-241608r879566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>After a security incident has occurred, investigators will often review log files to determine what happened. tc Server HORIZON must create a log entry when a user accesses the system and the system authenticates users. The logs must contain information about user sessions to include what type of event occurred, when (date and time) events occurred, where within the server the events occurred, the client source of the events, the outcome (success or failure) of the event, the identity of the user/subject/process associated with the event. As a Tomcat derivative, tc Server can be configured with an “AccessLogValve”. A Valve element represents a component that can be inserted into the request processing pipeline. The pattern attribute of the “AccessLogValve” controls which data gets logged. The “%h” parameter will record the remote hostname or IP address that sent the request; i.e. the source of the event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -v 127.0 /storage/log/vcops/log/product-ui/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If the source IP of events are not being recorded, this is a finding.

## Group: SRG-APP-000098-WSR-000059

**Group ID:** `V-241609`

### Rule: tc Server CaSa must produce log records containing sufficient information to establish the source of events.

**Rule ID:** `SV-241609r879566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>After a security incident has occurred, investigators will often review log files to determine what happened. tc Server HORIZON must create a log entry when a user accesses the system and the system authenticates users. The logs must contain information about user sessions to include what type of event occurred, when (date and time) events occurred, where within the server the events occurred, the client source of the events, the outcome (success or failure) of the event, the identity of the user/subject/process associated with the event. As a Tomcat derivative, tc Server can be configured with an “AccessLogValve”. A Valve element represents a component that can be inserted into the request processing pipeline. The pattern attribute of the “AccessLogValve” controls which data gets logged. The “%h” parameter will record the remote hostname or IP address that sent the request; i.e. the source of the event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -v 127.0 /storage/log/vcops/log/casa/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If the source IP of events are not being recorded, this is a finding.

## Group: SRG-APP-000098-WSR-000059

**Group ID:** `V-241610`

### Rule: tc Server API must produce log records containing sufficient information to establish the source of events.

**Rule ID:** `SV-241610r879566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>After a security incident has occurred, investigators will often review log files to determine what happened. tc Server HORIZON must create a log entry when a user accesses the system and the system authenticates users. The logs must contain information about user sessions to include what type of event occurred, when (date and time) events occurred, where within the server the events occurred, the client source of the events, the outcome (success or failure) of the event, the identity of the user/subject/process associated with the event. As a Tomcat derivative, tc Server can be configured with an “AccessLogValve”. A Valve element represents a component that can be inserted into the request processing pipeline. The pattern attribute of the “AccessLogValve” controls which data gets logged. The “%h” parameter will record the remote hostname or IP address that sent the request; i.e. the source of the event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -v 127.0 /storage/log/vcops/log/suite-api/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If the source IP of events are not being recorded, this is a finding.

## Group: SRG-APP-000098-WSR-000060

**Group ID:** `V-241611`

### Rule: tc Server UI must be configured with the RemoteIpValve in order to produce log records containing the client IP information as the source and destination and not the load balancer or proxy IP information with each event.

**Rule ID:** `SV-241611r879566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>tc Server HORIZON logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct source, e.g. source IP, of the events is important during forensic analysis. Correctly determining the source of events will add information to the overall reconstruction of the logable event. By determining the source of the event correctly, analysis of the enterprise can be undertaken to determine if events tied to the source occurred in other areas within the enterprise. tc Server HORIZON must be configured with the “RemoteIpValve” element in order to record the Client source vice the load balancer or proxy server as the source of every logable event. The “RemoteIpValve” enables the “x-forward-* HTTP” properties, which are used by the load balance to provide the client source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -v 127.0 /storage/log/vcops/log/product-ui/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If actual client IP information, not load balancer or proxy server, is not being recorded, this is a finding.

## Group: SRG-APP-000098-WSR-000060

**Group ID:** `V-241612`

### Rule: tc Server CaSa must be configured with the RemoteIpValve in order to produce log records containing the client IP information as the source and destination and not the load balancer or proxy IP information with each event.

**Rule ID:** `SV-241612r879566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>tc Server HORIZON logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct source, e.g. source IP, of the events is important during forensic analysis. Correctly determining the source of events will add information to the overall reconstruction of the logable event. By determining the source of the event correctly, analysis of the enterprise can be undertaken to determine if events tied to the source occurred in other areas within the enterprise. tc Server HORIZON must be configured with the “RemoteIpValve” element in order to record the Client source vice the load balancer or proxy server as the source of every logable event. The “RemoteIpValve” enables the “x-forward-* HTTP” properties, which are used by the load balance to provide the client source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -v 127.0 /storage/log/vcops/log/casa/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If actual client IP information, not load balancer or proxy server, is not being recorded, this is a finding.

## Group: SRG-APP-000098-WSR-000060

**Group ID:** `V-241613`

### Rule: tc Server API must be configured with the RemoteIpValve in order to produce log records containing the client IP information as the source and destination and not the load balancer or proxy IP information with each event.

**Rule ID:** `SV-241613r879566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>tc Server HORIZON logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct source, e.g. source IP, of the events is important during forensic analysis. Correctly determining the source of events will add information to the overall reconstruction of the logable event. By determining the source of the event correctly, analysis of the enterprise can be undertaken to determine if events tied to the source occurred in other areas within the enterprise. tc Server HORIZON must be configured with the “RemoteIpValve” element in order to record the Client source vice the load balancer or proxy server as the source of every logable event. The “RemoteIpValve” enables the “x-forward-* HTTP” properties, which are used by the load balance to provide the client source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -v 127.0 /storage/log/vcops/log/suite-api/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If actual client IP information, not load balancer or proxy server, is not being recorded, this is a finding.

## Group: SRG-APP-000099-WSR-000061

**Group ID:** `V-241614`

### Rule: tc Server UI must produce log records that contain sufficient information to establish the outcome (success or failure) of events.

**Rule ID:** `SV-241614r879567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>After a security incident has occurred, investigators will often review log files to determine what happened. tc Server HORIZON must create a log entry when a user accesses the system and the system authenticates users. The logs must contain information about user sessions to include what type of event occurred, when (date and time) events occurred, where within the server the events occurred, the client source of the events, the outcome (success or failure) of the event, the identity of the user/subject/process associated with the event. Like all web servers, tc Server generates HTTP status codes. The status code is a three-digit indicator of the outcome of the server's response to the request.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/product-ui/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If the HTTP status codes are not being recorded, this is a finding. Note: HTTP status codes are 3-digit codes, which are recorded immediately after "HTTP/1.1"

## Group: SRG-APP-000099-WSR-000061

**Group ID:** `V-241615`

### Rule: tc Server CaSa must produce log records that contain sufficient information to establish the outcome (success or failure) of events.

**Rule ID:** `SV-241615r879567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>After a security incident has occurred, investigators will often review log files to determine what happened. tc Server HORIZON must create a log entry when a user accesses the system and the system authenticates users. The logs must contain information about user sessions to include what type of event occurred, when (date and time) events occurred, where within the server the events occurred, the client source of the events, the outcome (success or failure) of the event, the identity of the user/subject/process associated with the event. Like all web servers, tc Server generates HTTP status codes. The status code is a three-digit indicator of the outcome of the server's response to the request.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/casa/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If the HTTP status codes are not being recorded, this is a finding. Note: HTTP status codes are 3-digit codes, which are recorded immediately after "HTTP/1.1"

## Group: SRG-APP-000099-WSR-000061

**Group ID:** `V-241616`

### Rule: tc Server API must produce log records that contain sufficient information to establish the outcome (success or failure) of events.

**Rule ID:** `SV-241616r879567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>After a security incident has occurred, investigators will often review log files to determine what happened. tc Server HORIZON must create a log entry when a user accesses the system and the system authenticates users. The logs must contain information about user sessions to include what type of event occurred, when (date and time) events occurred, where within the server the events occurred, the client source of the events, the outcome (success or failure) of the event, the identity of the user/subject/process associated with the event. Like all web servers, tc Server generates HTTP status codes. The status code is a three-digit indicator of the outcome of the server's response to the request.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/suite-api/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If the HTTP status codes are not being recorded, this is a finding. Note: HTTP status codes are three-digit codes, which are recorded immediately after "HTTP/1.1"

## Group: SRG-APP-000100-WSR-000064

**Group ID:** `V-241617`

### Rule: tc Server UI must produce log records containing sufficient information to establish the identity of any user/subject or process associated with an event.

**Rule ID:** `SV-241617r879568_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>After a security incident has occurred, investigators will often review log files to determine what happened. tc Server HORIZON must create a log entry when a user accesses the system and the system authenticates users. The logs must contain information about user sessions to include what type of event occurred, when (date and time) events occurred, where within the server the events occurred, the client source of the events, the outcome (success or failure) of the event, the identity of the user/subject/process associated with the event. As a Tomcat derivative, tc Server can be configured with an “AccessLogValve”. A Valve element represents a component that can be inserted into the request processing pipeline. The pattern attribute of the “AccessLogValve” controls which data gets logged. The “%u” parameter will record the remote user that was authenticated. Knowing the authenticated user could be crucial to know in an investigation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/product-ui/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If the identity of the user is not being recorded, this is a finding.

## Group: SRG-APP-000100-WSR-000064

**Group ID:** `V-241618`

### Rule: tc Server CaSa must produce log records containing sufficient information to establish the identity of any user/subject or process associated with an event.

**Rule ID:** `SV-241618r879568_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>After a security incident has occurred, investigators will often review log files to determine what happened. tc Server HORIZON must create a log entry when a user accesses the system and the system authenticates users. The logs must contain information about user sessions to include what type of event occurred, when (date and time) events occurred, where within the server the events occurred, the client source of the events, the outcome (success or failure) of the event, the identity of the user/subject/process associated with the event. As a Tomcat derivative, tc Server can be configured with an “AccessLogValve”. A Valve element represents a component that can be inserted into the request processing pipeline. The pattern attribute of the “AccessLogValve” controls which data gets logged. The “%u” parameter will record the remote user that was authenticated. Knowing the authenticated user could be crucial to know in an investigation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/casa/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If the identity of the user is not being recorded, this is a finding.

## Group: SRG-APP-000100-WSR-000064

**Group ID:** `V-241619`

### Rule: tc Server API must produce log records containing sufficient information to establish the identity of any user/subject or process associated with an event.

**Rule ID:** `SV-241619r879568_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>After a security incident has occurred, investigators will often review log files to determine what happened. tc Server HORIZON must create a log entry when a user accesses the system and the system authenticates users. The logs must contain information about user sessions to include what type of event occurred, when (date and time) events occurred, where within the server the events occurred, the client source of the events, the outcome (success or failure) of the event, the identity of the user/subject/process associated with the event. As a Tomcat derivative, tc Server can be configured with an “AccessLogValve”. A Valve element represents a component that can be inserted into the request processing pipeline. The pattern attribute of the “AccessLogValve” controls which data gets logged. The “%u” parameter will record the remote user that was authenticated. Knowing the authenticated user could be crucial to know in an investigation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/suite-api/localhost_access_log.YYYY-MM-dd.txt Note: Substitute the actual date in the file name. If the identity of the user is not being recorded, this is a finding.

## Group: SRG-APP-000108-WSR-000166

**Group ID:** `V-241620`

### Rule: tc Server ALL must use a logging mechanism that is configured to alert the ISSO and SA in the event of a processing failure.

**Rule ID:** `SV-241620r879570_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reviewing log data allows an investigator to recreate the path of an attacker and to capture forensic data for later use. Log data is also essential to system administrators in their daily administrative duties on the hosted system or within the hosted applications. If the logging system begins to fail, events will not be recorded. Organizations must define logging failure events, at which time the application or the logging mechanism the application utilizes will provide a warning to the ISSO and SA at a minimum.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Determine if log data and records are configured to alert the ISSO and SA in the event of processing failure. If log data and records are not configured to alert the ISSO and SA in the event of processing failure, this is a finding.

## Group: SRG-APP-000118-WSR-000068

**Group ID:** `V-241621`

### Rule: tc Server UI log files must only be accessible by privileged users.

**Rule ID:** `SV-241621r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to their advantage since each event record might contain communication ports, protocols, services, trust relationships, user names, etc. The web server must protect the log data from unauthorized read, write, copy, etc. This can be done by the web server if the web server is also doing the logging function. The web server may also use an external log system. In either case, the logs must be protected from access by non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: stat -c "%a %n" /storage/log/vcops/log/product-ui/* | awk '$1 !~ /^640/ && $2 ~ /(\.txt)|(\.log)/ {print}' If the command produces any output, this is a finding.

## Group: SRG-APP-000118-WSR-000068

**Group ID:** `V-241622`

### Rule: tc Server CaSa log files must only be accessible by privileged users.

**Rule ID:** `SV-241622r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to their advantage since each event record might contain communication ports, protocols, services, trust relationships, user names, etc. The web server must protect the log data from unauthorized read, write, copy, etc. This can be done by the web server if the web server is also doing the logging function. The web server may also use an external log system. In either case, the logs must be protected from access by non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: stat -c "%a %n" /storage/log/vcops/log/casa/* | awk '$1 !~ /^640/ && $2 ~ /(\.txt)|(\.log)/ {print}' If the command produces any output, this is a finding.

## Group: SRG-APP-000118-WSR-000068

**Group ID:** `V-241623`

### Rule: tc Server API log files must only be accessible by privileged users.

**Rule ID:** `SV-241623r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to their advantage since each event record might contain communication ports, protocols, services, trust relationships, user names, etc. The web server must protect the log data from unauthorized read, write, copy, etc. This can be done by the web server if the web server is also doing the logging function. The web server may also use an external log system. In either case, the logs must be protected from access by non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: stat -c "%a %n" /storage/log/vcops/log/suite-api/* | awk '$1 !~ /^640/ && $2 ~ /(\.txt)|(\.log)/ {print}' If the command produces any output, this is a finding.

## Group: SRG-APP-000119-WSR-000069

**Group ID:** `V-241624`

### Rule: tc Server UI log files must be protected from unauthorized modification.

**Rule ID:** `SV-241624r879577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. The accuracy of the information is always pertinent. Information that is not accurate does not help in the revealing of potential security risks and may hinder the early discovery of a system compromise. One of the first steps an attacker will undertake is the modification or deletion of log records to cover his tracks and prolong discovery. The web server must protect the log data from unauthorized modification. This can be done by the web server if the web server is also doing the logging function. The web server may also use an external log system. In either case, the logs must be protected from modification by non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Find any files that are not owned by admin or not group owned by admin, execute the following command: ls -lR /storage/log/vcops/log/product-ui/* | grep -vE 'pid$' | awk '$3 !~ /^admin/ {print}' If the command produces any output, this is a finding.

## Group: SRG-APP-000119-WSR-000069

**Group ID:** `V-241625`

### Rule: tc Server CaSa log files must be protected from unauthorized modification.

**Rule ID:** `SV-241625r879577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. The accuracy of the information is always pertinent. Information that is not accurate does not help in the revealing of potential security risks and may hinder the early discovery of a system compromise. One of the first steps an attacker will undertake is the modification or deletion of log records to cover his tracks and prolong discovery. The web server must protect the log data from unauthorized modification. This can be done by the web server if the web server is also doing the logging function. The web server may also use an external log system. In either case, the logs must be protected from modification by non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -lR /storage/log/vcops/log/casa/* | grep -vE '(pid$)|ntp' | awk '$3 !~ /^admin/ {print}' If the command produces any output, this is a finding.

## Group: SRG-APP-000119-WSR-000069

**Group ID:** `V-241626`

### Rule: tc Server API log files must be protected from unauthorized modification.

**Rule ID:** `SV-241626r879577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. The accuracy of the information is always pertinent. Information that is not accurate does not help in the revealing of potential security risks and may hinder the early discovery of a system compromise. One of the first steps an attacker will undertake is the modification or deletion of log records to cover his tracks and prolong discovery. The web server must protect the log data from unauthorized modification. This can be done by the web server if the web server is also doing the logging function. The web server may also use an external log system. In either case, the logs must be protected from modification by non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Find any files that are not owned by admin or not group owned by admin, execute the following command: ls -lR /storage/log/vcops/log/suite-api/* | grep -vE 'pid$' | awk '$3 !~ /^admin/ {print}' If the command produces any output, this is a finding.

## Group: SRG-APP-000120-WSR-000070

**Group ID:** `V-241627`

### Rule: tc Server UI log files must be protected from unauthorized deletion.

**Rule ID:** `SV-241627r879578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. The accuracy of the information is always pertinent. Information that is not accurate does not help in the revealing of potential security risks and may hinder the early discovery of a system compromise. One of the first steps an attacker will undertake is the modification or deletion of audit records to cover his tracks and prolong discovery. The web server must protect the log data from unauthorized deletion. This can be done by the web server if the web server is also doing the logging function. The web server may also use an external log system. In either case, the logs must be protected from deletion by non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -lR /storage/log/vcops/log/product-ui/* | grep -vE 'pid$' | awk '$3 !~ /^admin/ {print}' If the command produces any output, this is a finding.

## Group: SRG-APP-000120-WSR-000070

**Group ID:** `V-241628`

### Rule: tc Server CaSa log files must be protected from unauthorized deletion.

**Rule ID:** `SV-241628r879578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. The accuracy of the information is always pertinent. Information that is not accurate does not help in the revealing of potential security risks and may hinder the early discovery of a system compromise. One of the first steps an attacker will undertake is the modification or deletion of audit records to cover his tracks and prolong discovery. The web server must protect the log data from unauthorized deletion. This can be done by the web server if the web server is also doing the logging function. The web server may also use an external log system. In either case, the logs must be protected from deletion by non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -lR /storage/log/vcops/log/casa/* | grep -vE '(pid$)|ntp' | awk '$3 !~ /^admin/ {print}' If the command produces any output, this is a finding.

## Group: SRG-APP-000120-WSR-000070

**Group ID:** `V-241629`

### Rule: tc Server API log files must be protected from unauthorized deletion.

**Rule ID:** `SV-241629r879578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. The accuracy of the information is always pertinent. Information that is not accurate does not help in the revealing of potential security risks and may hinder the early discovery of a system compromise. One of the first steps an attacker will undertake is the modification or deletion of audit records to cover his tracks and prolong discovery. The web server must protect the log data from unauthorized deletion. This can be done by the web server if the web server is also doing the logging function. The web server may also use an external log system. In either case, the logs must be protected from deletion by non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -lR /storage/log/vcops/log/suite-api/* | grep -vE 'pid$' | awk '$3 !~ /^admin/ {print}' If the command produces any output, this is a finding.

## Group: SRG-APP-000125-WSR-000071

**Group ID:** `V-241630`

### Rule: tc Server ALL log data and records must be backed up onto a different system or media.

**Rule ID:** `SV-241630r879582_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of tc Server ALL log data includes assuring log data is not accidentally lost or deleted. Backing up tc Server ALL log records to an unrelated system or onto separate media than the system the web server is actually running on helps to assure that, in the event of a catastrophic system failure, the log records will be retained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Determine if log data and records are not being backed up onto a different system or media. If log data and records are not being backed up onto a different system or media, this is a finding.

## Group: SRG-APP-000131-WSR-000051

**Group ID:** `V-241631`

### Rule: tc Server ALL server files must be verified for their integrity (e.g., checksums and hashes) before becoming part of the production web server.

**Rule ID:** `SV-241631r879584_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Being able to verify that a patch, upgrade, certificate, etc., being added to the web server is unchanged from the producer of the file is essential for file validation and non-repudiation of the information. VMware delivers product updates and patches regularly. It is crucial that system administrators coordinate installation of product updates with the site ISSO to ensure that only valid files are uploaded onto the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Determine whether web server files are being fully reviewed, tested, and signed before being implemented into the production environment. If the web server files are not being fully reviewed, tested, and signed before being implemented into the production environment, this is a finding.

## Group: SRG-APP-000131-WSR-000073

**Group ID:** `V-241632`

### Rule: tc Server ALL expansion modules must be fully reviewed, tested, and signed before they can exist on a production web server.

**Rule ID:** `SV-241632r879584_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In the case of a production web server, areas for content development and testing will not exist, as this type of content is only permissible on a development website. The process of developing on a functional production website entails a degree of trial and error and repeated testing. This process is often accomplished in an environment where debugging, sequencing, and formatting of content are the main goals. The opportunity for a malicious user to obtain files that reveal business logic and login schemes is high in this situation. The existence of such immature content on a web server represents a significant security risk that is totally avoidable. VMware delivers product updates and patches regularly. It is crucial that system administrators coordinate installation of product updates with the site ISSO to ensure that only valid files are uploaded onto the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Determine whether expansion modules are being fully reviewed, tested, and signed before being implemented into the production environment. If the expansion modules are not being fully reviewed, tested, and signed before being implemented into the production environment, this is a finding.

## Group: SRG-APP-000141-WSR-000015

**Group ID:** `V-241633`

### Rule: tc Server UI must not use the tomcat-users XML database for user management.

**Rule ID:** `SV-241633r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User management and authentication can be an essential part of any application hosted by the web server. Along with authenticating users, the user management function must perform several other tasks like password complexity, locking users after a configurable number of failed logins, and management of temporary and emergency accounts; and all of this must be done enterprise-wide. For historical reasons, tc Server contains a tomcat-users.xml file in the configuration directory. This file was originally used by standalone applications that did not authenticate against an LDAP or other enterprise mechanism. vROps does not use this file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: cat /usr/lib/vmware-vcops/tomcat-web-app/conf/tomcat-users.xml If “tomcat-users.xml” file contains any user information, this is a finding.

## Group: SRG-APP-000141-WSR-000015

**Group ID:** `V-241634`

### Rule: tc Server CaSa must not use the tomcat-users XML database for user management.

**Rule ID:** `SV-241634r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User management and authentication can be an essential part of any application hosted by the web server. Along with authenticating users, the user management function must perform several other tasks like password complexity, locking users after a configurable number of failed logins, and management of temporary and emergency accounts; and all of this must be done enterprise-wide. For historical reasons, tc Server contains a “tomcat-users.xml” file in the configuration directory. This file was originally used by standalone applications that did not authenticate against an LDAP or other enterprise mechanism. vROps does not use this file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: cat /usr/lib/vmware-casa/casa-webapp/conf/tomcat-users.xml If “tomcat-users.xml” file contains any user information, this is a finding.

## Group: SRG-APP-000141-WSR-000015

**Group ID:** `V-241635`

### Rule: tc Server API must not use the tomcat-users XML database for user management.

**Rule ID:** `SV-241635r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User management and authentication can be an essential part of any application hosted by the web server. Along with authenticating users, the user management function must perform several other tasks like password complexity, locking users after a configurable number of failed logins, and management of temporary and emergency accounts; and all of this must be done enterprise-wide. For historical reasons, tc Server contains a “tomcat-users.xml” file in the configuration directory. This file was originally used by standalone applications that did not authenticate against an LDAP or other enterprise mechanism. vROps does not use this file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: cat /usr/lib/vmware-vcops/tomcat-enterprise/conf/tomcat-users.xml If “tomcat-users.xml” file contains any user information, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-241636`

### Rule: tc Server ALL must only contain services and functions necessary for operation.

**Rule ID:** `SV-241636r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Review the web server documentation and deployed configuration to determine if web server features, services, and processes are installed that are not needed for hosted application deployment. If excessive features, services, and processes are installed, this is a finding.

## Group: SRG-APP-000141-WSR-000077

**Group ID:** `V-241637`

### Rule: tc Server ALL must exclude documentation, sample code, example applications, and tutorials.

**Rule ID:** `SV-241637r879587_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Web server documentation, sample code, example applications, and tutorials may be an exploitable threat to a web server because this type of code has not been evaluated and approved. A production web server must only contain components that are operationally necessary (e.g., compiled code, scripts, web-content, etc.). Any documentation, sample code, example applications, and tutorials must be removed from a production web server. Because tc Server is installed as part of the entire vROps application, and not installed separately, VMware has ensured that all documentation, sample code, example applications, and tutorials have been removed from tc Server as part of the build process.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Review the web server documentation and deployed configuration to determine if documentation, sample code, example applications, and tutorials have been removed. If documentation, sample code, example applications, and tutorials have not been removed, this is a finding.

## Group: SRG-APP-000141-WSR-000080

**Group ID:** `V-241638`

### Rule: tc Server ALL must exclude installation of utility programs, services, plug-ins, and modules not necessary for operation.

**Rule ID:** `SV-241638r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Just as running unneeded services and protocols is a danger to the web server at the lower levels of the OSI model, running unneeded utilities and programs is also a danger at the application layer of the OSI model. Office suites, development tools, and graphical editors are examples of such programs that are troublesome. Because tc Server is installed as part of the entire vROps application, and not installed separately, VMware has ensured that no unnecessary utilities and programs have been included in tc Server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Review the web server documentation and deployed configuration to determine if utility programs, services, plug-ins, and modules not necessary for operation have been removed. If utility programs, services, plug-ins, and modules not necessary for operation have not been removed, this is a finding.

## Group: SRG-APP-000141-WSR-000081

**Group ID:** `V-241639`

### Rule: tc Server ALL must have Multipurpose Internet Mail Extensions (MIME) that invoke OS shell programs disabled.

**Rule ID:** `SV-241639r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Controlling what a user of a hosted application can access is part of the security posture of the web server. Any time a user can access more functionality than is needed for the operation of the hosted application poses a security issue. A user with too much access can view information that is not needed for the user's job role, or the user could use the function in an unintentional manner. A MIME tells the web server what type of program various file types and extensions are and what external utilities or programs are needed to execute the file type. tc Server configures MIME types in the web.xml file. By ensuring that “sh”, “csh”, and “shar” MIME types are not included in web.xml, the server is protected against malicious users tricking the server into executing shell command files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: find / -name 'web.xml' -print0 | xargs -0r grep -HEn '(x-csh<)|(x-sh<)|(x-shar<)|(x-ksh<)' If the command produces any output, this is a finding.

## Group: SRG-APP-000141-WSR-000082

**Group ID:** `V-241640`

### Rule: tc Server ALL must have all mappings to unused and vulnerable scripts to be removed.

**Rule ID:** `SV-241640r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Scripts allow server side processing on behalf of the hosted application user or as processes needed in the implementation of hosted applications. Removing scripts not needed for application operation or deemed vulnerable helps to secure the web server. To assure scripts are not added to the web server and run maliciously, those script mappings that are not needed or used by the web server for hosted application operation must be removed. Because tc Server is installed as part of the entire vROps application, and not installed separately, VMware has ensured that scripts not needed for application operation or deemed vulnerable have been removed from tc Server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Review the web server documentation and deployed configuration to determine if all mappings to unused and vulnerable scripts to be removed. If all mappings to unused and vulnerable scripts have not been removed, this is a finding.

## Group: SRG-APP-000141-WSR-000083

**Group ID:** `V-241641`

### Rule: tc Server UI must have mappings set for Java Servlet Pages.

**Rule ID:** `SV-241641r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Resource mapping is the process of tying a particular file type to a process in the web server that can serve that type of file to a requesting client and to identify which file types are not to be delivered to a client. By not specifying which files can and which files cannot be served to a user, the web server could deliver to a user web server configuration files, log files, password files, etc. As a derivative of the Apache Tomcat project, tc Server is a java-based web server. As a result, the main file extension used by tc Server is “*.jsp”. This check ensures that the “*.jsp” file type has been properly mapped to servlets.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -E '<url-pattern>\*\.jsp</url-pattern>' -B 2 -A 2 /usr/lib/vmware-vcops/tomcat-web-app/conf/web.xml If the “jsp” and “jspx” file extensions have not been mapped to the JSP servlet, this is a finding.

## Group: SRG-APP-000141-WSR-000083

**Group ID:** `V-241642`

### Rule: tc Server CaSa must have mappings set for Java Servlet Pages.

**Rule ID:** `SV-241642r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Resource mapping is the process of tying a particular file type to a process in the web server that can serve that type of file to a requesting client and to identify which file types are not to be delivered to a client. By not specifying which files can and which files cannot be served to a user, the web server could deliver to a user web server configuration files, log files, password files, etc. As a derivative of the Apache Tomcat project, tc Server is a java-based web server. As a result, the main file extension used by tc Server is “*.jsp”. This check ensures that the “*.jsp” file type has been properly mapped to servlets.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -E '<url-pattern>\*\.jsp</url-pattern>' -B 2 -A 2 /usr/lib/vmware-casa/casa-webapp/conf/web.xml If the “jsp” and “jspx” file extensions have not been mapped to the JSP servlet, this is a finding.

## Group: SRG-APP-000141-WSR-000083

**Group ID:** `V-241643`

### Rule: tc Server API must have mappings set for Java Servlet Pages.

**Rule ID:** `SV-241643r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Resource mapping is the process of tying a particular file type to a process in the web server that can serve that type of file to a requesting client and to identify which file types are not to be delivered to a client. By not specifying which files can and which files cannot be served to a user, the web server could deliver to a user web server configuration files, log files, password files, etc. As a derivative of the Apache Tomcat project, tc Server is a java-based web server. As a result, the main file extension used by tc Server is “*.jsp”. This check ensures that the “*.jsp” file type has been properly mapped to servlets.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -E '<url-pattern>\*\.jsp</url-pattern>' -B 2 -A 2 /usr/lib/vmware-vcops/tomcat-enterprise/conf/web.xml If the “jsp” and “jspx” file extensions have not been mapped to the JSP servlet, this is a finding.

## Group: SRG-APP-000141-WSR-000085

**Group ID:** `V-241644`

### Rule: tc Server ALL must not have the Web Distributed Authoring (WebDAV) servlet installed.

**Rule ID:** `SV-241644r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can be installed with functionality that, just by its nature, is not secure. Web Distributed Authoring (WebDAV) is an extension to the HTTP protocol that, when developed, was meant to allow users to create, change, and move documents on a server, typically a web server or web share. Allowing this functionality, development, and deployment is much easier for web authors. WebDAV is not widely used and has serious security concerns because it may allow clients to modify unauthorized files on the web server. As an extension to Tomcat, tc Server uses the “org.apache.catalina.servlets.WebdavServlet” servlet to provide WebDAV services. Because the WebDAV service has been found to have an excessive number of vulnerabilities, this servlet must not be installed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: find / -name 'web.xml' -print0 | xargs -0r grep -HEn 'webdav' If the command produces any output, this is a finding.

## Group: SRG-APP-000141-WSR-000086

**Group ID:** `V-241645`

### Rule: tc Server UI must be configured with memory leak protection.

**Rule ID:** `SV-241645r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Java Runtime environment can cause a memory leak or lock files under certain conditions. Without memory leak protection, tc Server HORIZON can continue to consume system resources which will lead to OutOfMemoryErrors when re-loading web applications. Memory leaks occur when JRE code uses the context class loader to load a singleton as this will cause a memory leak if a web application class loader happens to be the context class loader at the time. The JreMemoryLeakPreventionListener class is designed to initialize these singletons when Tomcat's common class loader is the context class loader. Proper use of JRE memory leak protection will ensure that the hosted application does not consume system resources and cause an unstable environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep JreMemoryLeakPreventionListener /usr/lib/vmware-vcops/tomcat-web-app/conf/server.xml If the JreMemoryLeakPreventionListener <Listener> node is not listed, this is a finding.

## Group: SRG-APP-000141-WSR-000086

**Group ID:** `V-241646`

### Rule: tc Server CaSa must be configured with memory leak protection.

**Rule ID:** `SV-241646r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Java Runtime environment can cause a memory leak or lock files under certain conditions. Without memory leak protection, tc Server HORIZON can continue to consume system resources which will lead to OutOfMemoryErrors when re-loading web applications. Memory leaks occur when JRE code uses the context class loader to load a singleton as this will cause a memory leak if a web application class loader happens to be the context class loader at the time. The JreMemoryLeakPreventionListener class is designed to initialize these singletons when Tomcat's common class loader is the context class loader. Proper use of JRE memory leak protection will ensure that the hosted application does not consume system resources and cause an unstable environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep JreMemoryLeakPreventionListener /usr/lib/vmware-casa/casa-webapp/conf/server.xml If the JreMemoryLeakPreventionListener <Listener> node is not listed, this is a finding.

## Group: SRG-APP-000141-WSR-000086

**Group ID:** `V-241647`

### Rule: tc Server API must be configured with memory leak protection.

**Rule ID:** `SV-241647r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Java Runtime environment can cause a memory leak or lock files under certain conditions. Without memory leak protection, tc Server HORIZON can continue to consume system resources which will lead to OutOfMemoryErrors when re-loading web applications. Memory leaks occur when JRE code uses the context class loader to load a singleton as this will cause a memory leak if a web application class loader happens to be the context class loader at the time. The JreMemoryLeakPreventionListener class is designed to initialize these singletons when Tomcat's common class loader is the context class loader. Proper use of JRE memory leak protection will ensure that the hosted application does not consume system resources and cause an unstable environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep JreMemoryLeakPreventionListener /usr/lib/vmware-vcops/tomcat-enterprise/conf/server.xml If the JreMemoryLeakPreventionListener <Listener> node is not listed, this is a finding.

## Group: SRG-APP-000141-WSR-000087

**Group ID:** `V-241648`

### Rule: tc Server UI must not have any symbolic links in the web content directory tree.

**Rule ID:** `SV-241648r879587_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A web server is designed to deliver content and execute scripts or applications on the request of a client or user. Containing user requests to files in the directory tree of the hosted web application and limiting the execution of scripts and applications guarantees that the user is not accessing information protected outside the application's realm. By checking that no symbolic links exist in the document root, the web server is protected from users jumping outside the hosted application directory tree and gaining access to the other directories, including the system root.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -lR /usr/lib/vmware-vcops/tomcat-web-app | grep '^l' If the command produces any output other than the expected result below, this is a finding. Expected Result: lrwxrwxrwx 1 admin admin 33 Mar 6 03:37 logs -> /storage/log/vcops/log/product-ui lrwxrwxrwx 1 admin admin 47 Mar 6 03:37 vcops-web-ent -> /usr/lib/vmware-vcops/tomcat-web-app/webapps/ui

## Group: SRG-APP-000141-WSR-000087

**Group ID:** `V-241649`

### Rule: tc Server CaSa must not have any symbolic links in the web content directory tree.

**Rule ID:** `SV-241649r879587_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A web server is designed to deliver content and execute scripts or applications on the request of a client or user. Containing user requests to files in the directory tree of the hosted web application and limiting the execution of scripts and applications guarantees that the user is not accessing information protected outside the application's realm. By checking that no symbolic links exist in the document root, the web server is protected from users jumping outside the hosted application directory tree and gaining access to the other directories, including the system root.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -lR /usr/lib/vmware-casa/casa-webapp | grep '^l' If the command produces any output other than the expected result below, this is a finding. Expected Result: lrwxrwxrwx 1 admin admin 27 Mar 6 03:37 logs -> /storage/log/vcops/log/casa

## Group: SRG-APP-000141-WSR-000087

**Group ID:** `V-241650`

### Rule: tc Server API must not have any symbolic links in the web content directory tree.

**Rule ID:** `SV-241650r879587_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A web server is designed to deliver content and execute scripts or applications on the request of a client or user. Containing user requests to files in the directory tree of the hosted web application and limiting the execution of scripts and applications guarantees that the user is not accessing information protected outside the application's realm. By checking that no symbolic links exist in the document root, the web server is protected from users jumping outside the hosted application directory tree and gaining access to the other directories, including the system root.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -lR /usr/lib/vmware-vcops/tomcat-enterprise | grep '^l' If the command produces any output, this is a finding.

## Group: SRG-APP-000142-WSR-000089

**Group ID:** `V-241651`

### Rule: tc Server UI must be configured to use a specified IP address and port.

**Rule ID:** `SV-241651r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The web server must be configured to listen on a specified IP address and port. Without specifying an IP address and port for the web server to utilize, the web server will listen on all IP addresses available to the hosting server. If the web server has multiple IP addresses, i.e., a management IP address, the web server will also accept connections on the management IP address. Accessing the hosted application through an IP address normally used for non-application functions opens the possibility of user access to resources, utilities, files, ports, and protocols that are protected on the desired application IP address.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-web-app/conf/server.xml. Navigate to each of the <Connector> nodes. If either the IP address or the port is not specified for each <Connector>, this is a finding.

## Group: SRG-APP-000142-WSR-000089

**Group ID:** `V-241652`

### Rule: tc Server CaSa must be configured to use a specified IP address and port.

**Rule ID:** `SV-241652r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The web server must be configured to listen on a specified IP address and port. Without specifying an IP address and port for the web server to utilize, the web server will listen on all IP addresses available to the hosting server. If the web server has multiple IP addresses, i.e., a management IP address, the web server will also accept connections on the management IP address. Accessing the hosted application through an IP address normally used for non-application functions opens the possibility of user access to resources, utilities, files, ports, and protocols that are protected on the desired application IP address.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-casa/casa-webapp/conf/server.xml. Navigate to each of the <Connector> nodes. If either the IP address or the port is not specified for each <Connector>, this is a finding.

## Group: SRG-APP-000142-WSR-000089

**Group ID:** `V-241653`

### Rule: tc Server API must be configured to use a specified IP address and port.

**Rule ID:** `SV-241653r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The web server must be configured to listen on a specified IP address and port. Without specifying an IP address and port for the web server to utilize, the web server will listen on all IP addresses available to the hosting server. If the web server has multiple IP addresses, i.e., a management IP address, the web server will also accept connections on the management IP address. Accessing the hosted application through an IP address normally used for non-application functions opens the possibility of user access to resources, utilities, files, ports, and protocols that are protected on the desired application IP address.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-enterprise/conf/server.xml. Navigate to each of the <Connector> nodes. If either the IP address or the port is not specified for each <Connector>, this is a finding.

## Group: SRG-APP-000172-WSR-000104

**Group ID:** `V-241654`

### Rule: tc Server UI must encrypt passwords during transmission.

**Rule ID:** `SV-241654r879609_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data used to authenticate, especially passwords, needs to be protected at all times, and encryption is the standard method for protecting authentication data during transmission. Data used to authenticate can be passed to and from the web server for many reasons. Examples include data passed from a user to the web server through an HTTPS connection for authentication, the web server authenticating to a backend database for data retrieval and posting, and the web server authenticating to a clustered web server manager for an update. HTTP connections in tc Server are managed through the Connector object. Setting the Connector's “SSLEnabled” flag, SSL handshake/encryption/decryption is enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-web-app/conf/server.xml. Navigate to the <Connector> node that contains 'port="${vmware-ssl.https.port}"' If the value of “SSLEnabled” is not set to “true” or is missing, this is a finding.

## Group: SRG-APP-000172-WSR-000104

**Group ID:** `V-241655`

### Rule: tc Server CaSa must encrypt passwords during transmission.

**Rule ID:** `SV-241655r879609_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data used to authenticate, especially passwords, needs to be protected at all times, and encryption is the standard method for protecting authentication data during transmission. Data used to authenticate can be passed to and from the web server for many reasons. Examples include data passed from a user to the web server through an HTTPS connection for authentication, the web server authenticating to a backend database for data retrieval and posting, and the web server authenticating to a clustered web server manager for an update. HTTP connections in tc Server are managed through the Connector object. Setting the Connector's “SSLEnabled” flag, SSL handshake/encryption/decryption is enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-casa/casa-webapp/conf/server.xml. Navigate to the <Connector> node that contains 'port="${vmware-ssl.https.port}"'. If the value of “SSLEnabled” is not set to “true” or is missing, this is a finding.

## Group: SRG-APP-000172-WSR-000104

**Group ID:** `V-241656`

### Rule: tc Server API must encrypt passwords during transmission.

**Rule ID:** `SV-241656r879609_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data used to authenticate, especially passwords, needs to be protected at all times, and encryption is the standard method for protecting authentication data during transmission. Data used to authenticate can be passed to and from the web server for many reasons. Examples include data passed from a user to the web server through an HTTPS connection for authentication, the web server authenticating to a backend database for data retrieval and posting, and the web server authenticating to a clustered web server manager for an update. HTTP connections in tc Server are managed through the Connector object. Setting the Connector's “SSLEnabled” flag, SSL handshake/encryption/decryption is enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-enterprise/conf/server.xml. Navigate to the <Connector> node that contains 'port="${vmware-ssl.https.port}"'. If the value of “SSLEnabled” is not set to “true” or is missing, this is a finding.

## Group: SRG-APP-000175-WSR-000095

**Group ID:** `V-241657`

### Rule: tc Server ALL must validate client certificates, to include all intermediary CAs, to ensure the client-presented certificates are valid and that the entire trust chain is valid.  If PKI is not being used, this check is Not Applicable.

**Rule ID:** `SV-241657r879612_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. A certificate’s certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Review tc Server ALL configuration to verify that certificates being provided by the client are being validated in accordance with RFC 5280. If PKI is not being used, this is NA. If certificates are not being validated in accordance with RFC 5280, this is a finding.

## Group: SRG-APP-000176-WSR-000096

**Group ID:** `V-241658`

### Rule: tc Server ALL must only allow authenticated system administrators to have access to the keystore.

**Rule ID:** `SV-241658r879613_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The web server's private key is used to prove the identity of the server to clients and securely exchange the shared secret key used to encrypt communications between the web server and clients. By gaining access to the private key, an attacker can pretend to be an authorized server and decrypt the SSL traffic between a client and the web server. tc Server stores the server's private key in a keystore file. The vROps keystore file is “tcserver.keystore”, and this file must be protected to only allow system administrators and other authorized users to have access to it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -al /storage/vcops/user/conf/ssl/tcserver.keystore Verify that file permissions are set to “640” or more restrictive. Verify that the owner and group-owner are set to admin. If either of these conditions are not met, this is a finding.

## Group: SRG-APP-000176-WSR-000096

**Group ID:** `V-241659`

### Rule: tc Server ALL must only allow authenticated system administrators to have access to the truststore.

**Rule ID:** `SV-241659r879613_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The web server's private key is used to prove the identity of the server to clients and securely exchange the shared secret key used to encrypt communications between the web server and clients. By gaining access to the private key, an attacker can pretend to be an authorized server and decrypt the SSL traffic between a client and the web server. As a Tomcat derivative tc Server is designed to store the server's private key in a keystore file. An important vROps keystore file is “tcserver.truststore”, and this file must be protected to only allow system administrators and other authorized users to have access to it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -al /storage/vcops/user/conf/ssl/tcserver.truststore Verify that file permissions are set to “640” or more restrictive. Verify that the owner and group-owner are set to admin. If either of these conditions are not met, this is a finding.

## Group: SRG-APP-000179-WSR-000111

**Group ID:** `V-241660`

### Rule: tc Server UI must use cryptographic modules that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance when authenticating users and processes.

**Rule ID:** `SV-241660r879616_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified and cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised due to weak algorithms. FIPS 140-2 is the current standard for validating cryptographic modules and NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. vROps relies upon the OpenSSL suite of encryption libraries. A special carefully defined software component called the OpenSSL FIPS Object Module has been created from the OpenSSL libraries to provide FIPS 140-2 validated encryption. This Module was designed for compatibility with OpenSSL so that products using the OpenSSL API can be converted to use validated cryptography with minimal effort.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep vmware-ssl.ssl.ciphers.list /usr/lib/vmware-vcops/tomcat-web-app/conf/catalina.properties If the value of “vmware-ssl.ssl.ciphers.list” does not match the list of FIPS 140-2 ciphers or is missing, this is a finding. Note: To view a list of FIPS 140-2 ciphers, at the command prompt execute the following command: openssl ciphers 'FIPS'

## Group: SRG-APP-000179-WSR-000111

**Group ID:** `V-241661`

### Rule: tc Server CaSa must use cryptographic modules that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance when authenticating users and processes.

**Rule ID:** `SV-241661r879616_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified and cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised due to weak algorithms. FIPS 140-2 is the current standard for validating cryptographic modules and NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. vROps relies upon the OpenSSL suite of encryption libraries. A special carefully defined software component called the OpenSSL FIPS Object Module has been created from the OpenSSL libraries to provide FIPS 140-2 validated encryption. This Module was designed for compatibility with OpenSSL so that products using the OpenSSL API can be converted to use validated cryptography with minimal effort.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -A 10 vmware-casa.ssl.ciphers.list /usr/lib/vmware-casa/casa-webapp/conf/catalina.properties If the value of “vmware-casa.ssl.ciphers.list” does not match the list of FIPS 140-2 ciphers or is missing, this is a finding. Note: To view a list of FIPS 140-2 ciphers, at the command prompt execute the following command: openssl ciphers 'FIPS'

## Group: SRG-APP-000179-WSR-000111

**Group ID:** `V-241662`

### Rule: tc Server API must use cryptographic modules that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance when authenticating users and processes.

**Rule ID:** `SV-241662r879616_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified and cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised due to weak algorithms. FIPS 140-2 is the current standard for validating cryptographic modules and NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. vROps relies upon the OpenSSL suite of encryption libraries. A special carefully defined software component called the OpenSSL FIPS Object Module has been created from the OpenSSL libraries to provide FIPS 140-2 validated encryption. This Module was designed for compatibility with OpenSSL so that products using the OpenSSL API can be converted to use validated cryptography with minimal effort.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep vmware-ssl.ssl.ciphers.list /usr/lib/vmware-vcops/tomcat-enterprise/conf/catalina.properties If the value of “vmware-ssl.ssl.ciphers.list” does not match the list of FIPS 140-2 ciphers or is missing, this is a finding. Note: To view a list of FIPS 140-2 ciphers, at the command prompt execute the following command: openssl ciphers 'FIPS'

## Group: SRG-APP-000211-WSR-000030

**Group ID:** `V-241663`

### Rule: tc Server UI accounts accessing the directory tree, the shell, or other operating system functions and utilities must be administrative accounts.

**Rule ID:** `SV-241663r879631_rule`
**Severity:** high

**Description:**
<VulnDiscussion>As a rule, accounts on a web server are to be kept to a minimum. Only administrators, web managers, developers, auditors, and web authors require accounts on the machine hosting the web server. The resources to which these accounts have access must also be closely monitored and controlled. Only the system administrator needs access to all the system's capabilities, while the web administrator and associated staff require access and control of the web content and web server configuration files. As with all secure web server installations, tc Server files and directories must be adequately protected with correct permissions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following commands: cd /usr/lib/vmware-vcops/tomcat-web-app ls -alR bin lib conf | grep -E '^-' | awk '$3 !~ /admin/ {print}' If the command produces any output, this is a finding.

## Group: SRG-APP-000211-WSR-000030

**Group ID:** `V-241664`

### Rule: tc Server CaSa accounts accessing the directory tree, the shell, or other operating system functions and utilities must be administrative accounts.

**Rule ID:** `SV-241664r879631_rule`
**Severity:** high

**Description:**
<VulnDiscussion>As a rule, accounts on a web server are to be kept to a minimum. Only administrators, web managers, developers, auditors, and web authors require accounts on the machine hosting the web server. The resources to which these accounts have access must also be closely monitored and controlled. Only the system administrator needs access to all the system's capabilities, while the web administrator and associated staff require access and control of the web content and web server configuration files. As with all secure web server installations, tc Server files and directories must be adequately protected with correct permissions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following commands: cd /usr/lib/vmware-casa/casa-webapp ls -alR bin lib conf | grep -E '^-' | awk '$3 !~ /admin/ {print}' If the command produces any output, this is a finding.

## Group: SRG-APP-000211-WSR-000030

**Group ID:** `V-241665`

### Rule: tc Server API accounts accessing the directory tree, the shell, or other operating system functions and utilities must be administrative accounts.

**Rule ID:** `SV-241665r879631_rule`
**Severity:** high

**Description:**
<VulnDiscussion>As a rule, accounts on a web server are to be kept to a minimum. Only administrators, web managers, developers, auditors, and web authors require accounts on the machine hosting the web server. The resources to which these accounts have access must also be closely monitored and controlled. Only the system administrator needs access to all the system's capabilities, while the web administrator and associated staff require access and control of the web content and web server configuration files. As with all secure web server installations, tc Server files and directories must be adequately protected with correct permissions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Find any files that are not owned by admin or not group owned by admin, execute the following command: cd /usr/lib/vmware-vcops/tomcat-enterprise ls -alR bin conf | grep -E '^-' | awk '$3 !~ /admin/ {print}' If the command produces any output, this is a finding.

## Group: SRG-APP-000211-WSR-000031

**Group ID:** `V-241666`

### Rule: tc Server UI web server application directories must not be accessible to anonymous user.

**Rule ID:** `SV-241666r879631_rule`
**Severity:** high

**Description:**
<VulnDiscussion>In order to properly monitor the changes to the web server and the hosted applications, logging must be enabled. Along with logging being enabled, each record must properly contain the changes made and the names of those who made the changes. Allowing anonymous users the capability to change the web server or the hosted application will not generate proper log information that can then be used for forensic reporting in the case of a security issue. Allowing anonymous users to make changes will also grant change capabilities to anybody without forcing a user to authenticate before the changes can be made.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following commands: cd /usr/lib/vmware-vcops/tomcat-web-app ls -alR bin lib conf | grep -E '^-' | awk '$1 !~ /---$/ {print}' If the command produces any output, this is a finding.

## Group: SRG-APP-000211-WSR-000031

**Group ID:** `V-241667`

### Rule: tc Server CaSa web server application directories must not be accessible to anonymous user.

**Rule ID:** `SV-241667r879631_rule`
**Severity:** high

**Description:**
<VulnDiscussion>In order to properly monitor the changes to the web server and the hosted applications, logging must be enabled. Along with logging being enabled, each record must properly contain the changes made and the names of those who made the changes. Allowing anonymous users the capability to change the web server or the hosted application will not generate proper log information that can then be used for forensic reporting in the case of a security issue. Allowing anonymous users to make changes will also grant change capabilities to anybody without forcing a user to authenticate before the changes can be made.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following commands: cd /usr/lib/vmware-casa/casa-webapp ls -alR bin lib conf | grep -E '^-' | awk '$1 !~ /---$/ {print}' If the command produces any output, this is a finding.

## Group: SRG-APP-000211-WSR-000031

**Group ID:** `V-241668`

### Rule: tc Server API web server application directories must not be accessible to anonymous user.

**Rule ID:** `SV-241668r879631_rule`
**Severity:** high

**Description:**
<VulnDiscussion>In order to properly monitor the changes to the web server and the hosted applications, logging must be enabled. Along with logging being enabled, each record must properly contain the changes made and the names of those who made the changes. Allowing anonymous users the capability to change the web server or the hosted application will not generate proper log information that can then be used for forensic reporting in the case of a security issue. Allowing anonymous users to make changes will also grant change capabilities to anybody without forcing a user to authenticate before the changes can be made.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, find any world accessible files by executing the following commands: ls -alR /usr/lib/vmware-vcops/tomcat-enterprise/bin /usr/lib/vmware-vcops/tomcat-enterprise/conf | grep -E '^-' | awk '$1 !~ /---$/ {print}' If the command produces any output, this is a finding.

## Group: SRG-APP-000225-WSR-000074

**Group ID:** `V-241669`

### Rule: tc Server ALL baseline must be documented and maintained.

**Rule ID:** `SV-241669r879640_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Making certain that the web server has not been updated by an unauthorized user is always a concern. Adding patches, functions, and modules that are untested and not part of the baseline opens the possibility for security risks. The web server must offer, and not hinder, a method that allows for the quick and easy reinstallation of a verified and patched baseline to guarantee the production web server is up-to-date and has not been modified to add functionality or expose security risks. Because tc Server is installed as part of the entire vROps application, and not installed separately, VMware has ensured that all updates, upgrades, and patches have been thoroughly tested before becoming part of the production build process.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Review the web server documentation and deployed configuration to determine if the tc Server code baseline is documented and maintained. If the tc Server code baseline is not documented and maintained, this is a finding.

## Group: SRG-APP-000225-WSR-000140

**Group ID:** `V-241670`

### Rule: tc Server UI must be built to fail to a known safe state if system initialization fails, shutdown fails, or aborts fail.

**Rule ID:** `SV-241670r879640_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Determining a safe state for failure and weighing that against a potential DoS for users depends on what type of application the web server is hosting. For an application presenting publicly available information that is not critical, a safe state for failure might be to shut down for any type of failure; but for an application that presents critical and timely information, a shutdown might not be the best state for all failures. Performing a proper risk analysis of the hosted applications and configuring the web server according to what actions to take for each failure condition will provide a known fail safe state for the web server. The VMware engineering process includes regression testing of new and modified components before they become part of the production build process.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, execute the following command: grep EXIT_ON_INIT_FAILURE /usr/lib/vmware-vcops/tomcat-web-app/conf/catalina.properties If the “org.apache.catalina.startup.EXIT_ON_INIT_FAILURE” setting is not set to "true" or is missing, this is a finding.

## Group: SRG-APP-000225-WSR-000140

**Group ID:** `V-241671`

### Rule: tc Server CaSa must be built to fail to a known safe state if system initialization fails, shutdown fails, or aborts fail.

**Rule ID:** `SV-241671r879640_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Determining a safe state for failure and weighing that against a potential DoS for users depends on what type of application the web server is hosting. For an application presenting publicly available information that is not critical, a safe state for failure might be to shut down for any type of failure; but for an application that presents critical and timely information, a shutdown might not be the best state for all failures. Performing a proper risk analysis of the hosted applications and configuring the web server according to what actions to take for each failure condition will provide a known fail safe state for the web server. The VMware engineering process includes regression testing of new and modified components before they become part of the production build process.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, execute the following command: grep EXIT_ON_INIT_FAILURE /usr/lib/vmware-casa/casa-webapp/conf/catalina.properties If the “org.apache.catalina.startup.EXIT_ON_INIT_FAILURE” setting is not set to "true" or is missing, this is a finding.

## Group: SRG-APP-000225-WSR-000140

**Group ID:** `V-241672`

### Rule: tc Server API must be built to fail to a known safe state if system initialization fails, shutdown fails, or aborts fail.

**Rule ID:** `SV-241672r879640_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Determining a safe state for failure and weighing that against a potential DoS for users depends on what type of application the web server is hosting. For an application presenting publicly available information that is not critical, a safe state for failure might be to shut down for any type of failure; but for an application that presents critical and timely information, a shutdown might not be the best state for all failures. Performing a proper risk analysis of the hosted applications and configuring the web server according to what actions to take for each failure condition will provide a known fail safe state for the web server. The VMware engineering process includes regression testing of new and modified components before they become part of the production build process.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command line, execute the following command: grep EXIT_ON_INIT_FAILURE /usr/lib/vmware-vcops/tomcat-enterprise/conf/catalina.properties If the “org.apache.catalina.startup.EXIT_ON_INIT_FAILURE” setting is not set to "true" or is missing, this is a finding.

## Group: SRG-APP-000233-WSR-000146

**Group ID:** `V-241673`

### Rule: tc Server UI document directory must be in a separate partition from the web servers system files.

**Rule ID:** `SV-241673r879643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server is used to deliver content on the request of a client. The content delivered to a client must be controlled, allowing only hosted application files to be accessed and delivered. To allow a client access to system files of any type is a major security risk that is entirely avoidable. Obtaining such access is the goal of directory traversal and URL manipulation vulnerabilities. To facilitate such access by misconfiguring the web document (home) directory is a serious error. In addition, having the path on the same drive as the system folder compounds potential attacks such as drive space exhaustion. As a Tomcat derivative, tc Server stores the web applications in a special “webapps” folder. The Java engine, however, is stored in a separate are of the OS directory structure. For greatest security it is important to verify that the “webapps” and the Java directories remain separated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following commands: df -k /usr/java/default/bin/java df -k /usr/lib/vmware-vcops/tomcat-web-app/webapps If the two directories above are on the same partition, this is a finding.

## Group: SRG-APP-000233-WSR-000146

**Group ID:** `V-241674`

### Rule: tc Server CaSa document directory must be in a separate partition from the web servers system files.

**Rule ID:** `SV-241674r879643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server is used to deliver content on the request of a client. The content delivered to a client must be controlled, allowing only hosted application files to be accessed and delivered. To allow a client access to system files of any type is a major security risk that is entirely avoidable. Obtaining such access is the goal of directory traversal and URL manipulation vulnerabilities. To facilitate such access by misconfiguring the web document (home) directory is a serious error. In addition, having the path on the same drive as the system folder compounds potential attacks such as drive space exhaustion. As a Tomcat derivative, tc Server stores the web applications in a special “webapps” folder. The Java engine, however, is stored in a separate are of the OS directory structure. For greatest security it is important to verify that the “webapps” and the Java directories remain separated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following commands: df -k /usr/java/default/bin/java df -k /usr/lib/vmware-casa/casa-webapp/webapps If the two directories above are on the same partition, this is a finding

## Group: SRG-APP-000233-WSR-000146

**Group ID:** `V-241675`

### Rule: tc Server API document directory must be in a separate partition from the web servers system files.

**Rule ID:** `SV-241675r879643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server is used to deliver content on the request of a client. The content delivered to a client must be controlled, allowing only hosted application files to be accessed and delivered. To allow a client access to system files of any type is a major security risk that is entirely avoidable. Obtaining such access is the goal of directory traversal and URL manipulation vulnerabilities. To facilitate such access by misconfiguring the web document (home) directory is a serious error. In addition, having the path on the same drive as the system folder compounds potential attacks such as drive space exhaustion. As a Tomcat derivative, tc Server stores the web applications in a special “webapps” folder. The Java engine, however, is stored in a separate are of the OS directory structure. For greatest security it is important to verify that the “webapps” and the Java directories remain separated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following commands: df -k /usr/java/default/bin/java df -k /usr/lib/vmware-vcops/tomcat-enterprise/webapps If the two directories above are on the same partition, this is a finding

## Group: SRG-APP-000246-WSR-000149

**Group ID:** `V-241676`

### Rule: tc Server UI must be configured with a cross-site scripting (XSS) filter.

**Rule ID:** `SV-241676r879650_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cross-site scripting (XSS) is a type of computer security vulnerability typically found in web applications. XSS enables attackers to inject client-side scripts into web pages viewed by other users. A cross-site scripting vulnerability may be used by attackers to bypass access controls such as the same-origin policy. As a web server, tc Server can be vulnerable to XSS if steps are not taken to mitigate the threat. VMware provides the XssFilter component to provide a layer of defense against XSS. Filters are Java objects that performs filtering tasks on either the request to a resource (a servlet or static content), or on the response from a resource, or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -B 2 -A 7 XssFilter /usr/lib/vmware-vcops/tomcat-web-app/webapps/ui/WEB-INF/web.xml If the XSS filter is not present, this is a finding.

## Group: SRG-APP-000246-WSR-000149

**Group ID:** `V-241677`

### Rule: tc Server CaSa must be configured with a cross-site scripting (XSS) filter.

**Rule ID:** `SV-241677r879650_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cross-site scripting (XSS) is a type of computer security vulnerability typically found in web applications. XSS enables attackers to inject client-side scripts into web pages viewed by other users. A cross-site scripting vulnerability may be used by attackers to bypass access controls such as the same-origin policy. As a web server, tc Server can be vulnerable to XSS if steps are not taken to mitigate the threat. VMware provides the XssFilter component to provide a layer of defense against XSS. Filters are Java objects that performs filtering tasks on either the request to a resource (a servlet or static content), or on the response from a resource, or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -B 2 -A 7 XssFilter /usr/lib/vmware-casa/casa-webapp/webapps/admin/WEB-INF/web.xml If the XSS filter is not present and there is no result returned, then this is a finding.

## Group: SRG-APP-000246-WSR-000149

**Group ID:** `V-241678`

### Rule: tc Server API must be configured with a cross-site scripting (XSS) filter.

**Rule ID:** `SV-241678r879650_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cross-site scripting (XSS) is a type of computer security vulnerability typically found in web applications. XSS enables attackers to inject client-side scripts into web pages viewed by other users. A cross-site scripting vulnerability may be used by attackers to bypass access controls such as the same-origin policy. As a web server, tc Server can be vulnerable to XSS if steps are not taken to mitigate the threat. VMware provides the XssFilter component to provide a layer of defense against XSS. Filters are Java objects that performs filtering tasks on either the request to a resource (a servlet or static content), or on the response from a resource, or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -B 2 -A 7 XssFilter /usr/lib/vmware-vcops/tomcat-enterprise/webapps/suite-api/WEB-INF/web.xml If the XSS filter is not present and there is no result returned, then this is a finding.

## Group: SRG-APP-000251-WSR-000157

**Group ID:** `V-241679`

### Rule: tc Server UI must set URIEncoding to UTF-8.

**Rule ID:** `SV-241679r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into a hosted application's data entry field and the hosted application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. An attacker can also enter Unicode into hosted applications in an effort to break out of the document home or root home directory or to bypass security checks. To mitigate against many types of character-based vulnerabilities, tc Server should be configured to use a consistent character set. The “URIEncoding” attribute on the Connector nodes provides the means for tc Server to enforce a consistent character set encoding.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-web-app/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “URIEncoding” is not set to “UTF-8” or is missing, this is a finding.

## Group: SRG-APP-000251-WSR-000157

**Group ID:** `V-241680`

### Rule: tc Server CaSa must set URIEncoding to UTF-8.

**Rule ID:** `SV-241680r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into a hosted application's data entry field and the hosted application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. An attacker can also enter Unicode into hosted applications in an effort to break out of the document home or root home directory or to bypass security checks. To mitigate against many types of character-based vulnerabilities, tc Server should be configured to use a consistent character set. The “URIEncoding” attribute on the Connector nodes provides the means for tc Server to enforce a consistent character set encoding.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-casa/casa-webapp/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “URIEncoding” is not set to “UTF-8” or is missing, this is a finding.

## Group: SRG-APP-000251-WSR-000157

**Group ID:** `V-241681`

### Rule: tc Server API must set URIEncoding to UTF-8.

**Rule ID:** `SV-241681r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into a hosted application's data entry field and the hosted application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. An attacker can also enter Unicode into hosted applications in an effort to break out of the document home or root home directory or to bypass security checks. To mitigate against many types of character-based vulnerabilities, tc Server should be configured to use a consistent character set. The “URIEncoding” attribute on the Connector nodes provides the means for tc Server to enforce a consistent character set encoding.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-enterprise/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “URIEncoding” is not set to “UTF-8” or is missing, this is a finding.

## Group: SRG-APP-000251-WSR-000157

**Group ID:** `V-241682`

### Rule: tc Server UI must use the setCharacterEncodingFilter filter.

**Rule ID:** `SV-241682r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into a hosted application's data entry field and the hosted application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. An attacker can also enter Unicode into hosted applications in an effort to break out of the document home or root home directory or to bypass security checks. As a web server, tc Server can be vulnerable to character encoding attacks if steps are not taken to mitigate the threat. VMware utilizes the standard Tomcat “setCharacterEncodingFilter” filter to provide a layer of defense against character encoding attacks. Filters are Java objects that performs filtering tasks on either the request to a resource (a servlet or static content), or on the response from a resource, or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-web-app/conf/web.xml. Verify that the 'setCharacterEncodingFilter' <filter> has been specified with the following command: grep -B 2 -A 7 setCharacterEncodingFilter /usr/lib/vmware-vcops/tomcat-web-app/conf/web.xml If the “setCharacterEncodingFilter” filter has not been specified or is commented out, this is a finding.

## Group: SRG-APP-000251-WSR-000157

**Group ID:** `V-241683`

### Rule: tc Server CaSa must use the setCharacterEncodingFilter filter.

**Rule ID:** `SV-241683r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into a hosted application's data entry field and the hosted application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. An attacker can also enter Unicode into hosted applications in an effort to break out of the document home or root home directory or to bypass security checks. As a web server, tc Server can be vulnerable to character encoding attacks if steps are not taken to mitigate the threat. VMware utilizes the standard Tomcat setCharacterEncodingFilter filter to provide a layer of defense against character encoding attacks. Filters are Java objects that performs filtering tasks on either the request to a resource (a servlet or static content), or on the response from a resource, or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-casa/casa-webapp/conf/web.xml. Verify that the 'setCharacterEncodingFilter' <filter> has been specified with the following command: grep -B 2 -A 7 setCharacterEncodingFilter /usr/lib/vmware-casa/casa-webapp/conf/web.xml If the “setCharacterEncodingFilter” filter has not been specified or is commented out, this is a finding.

## Group: SRG-APP-000251-WSR-000157

**Group ID:** `V-241684`

### Rule: tc Server API must use the setCharacterEncodingFilter filter.

**Rule ID:** `SV-241684r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into a hosted application's data entry field and the hosted application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. An attacker can also enter Unicode into hosted applications in an effort to break out of the document home or root home directory or to bypass security checks. As a web server, tc Server can be vulnerable to character encoding attacks if steps are not taken to mitigate the threat. VMware utilizes the standard Tomcat setCharacterEncodingFilter filter to provide a layer of defense against character encoding attacks. Filters are Java objects that performs filtering tasks on either the request to a resource (a servlet or static content), or on the response from a resource, or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-enterprise/conf/web.xml. Verify that the 'setCharacterEncodingFilter' <filter> has been specified with the following command: grep -B 2 -A 7 setCharacterEncodingFilter /usr/lib/vmware-vcops/tomcat-enterprise/conf/web.xml If the “setCharacterEncodingFilter” filter has not been specified or is commented out, this is a finding.

## Group: SRG-APP-000266-WSR-000142

**Group ID:** `V-241685`

### Rule: tc Server UI must set the welcome-file node to a default web page.

**Rule ID:** `SV-241685r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The goal is to completely control the web user's experience in navigating any portion of the web document root directories. Ensuring all web content directories have at least the equivalent of an index.html file is a significant factor to accomplish this end. Enumeration techniques, such as URL parameter manipulation, rely upon being able to obtain information about the web server's directory structure by locating directories without default pages. In the scenario, the web server will display to the user a listing of the files in the directory being accessed. By having a default hosted application web page, the anonymous web user will not obtain directory browsing information or an error message that reveals the server type and version. As a web server, tc Server can be vulnerable to enumeration techniques if steps are not taken to mitigate the vulnerability. Ensuring that every document directory has an “index.jsp” (or equivalent) file is one common sense approach to mitigating the vulnerability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -E -A 4 '<welcome-file-list' /usr/lib/vmware-vcops/tomcat-web-app/conf/web.xml If a <welcome-file> node is not set to a default web page, this is a finding.

## Group: SRG-APP-000266-WSR-000142

**Group ID:** `V-241686`

### Rule: tc Server CaSa must set the welcome-file node to a default web page.

**Rule ID:** `SV-241686r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The goal is to completely control the web user's experience in navigating any portion of the web document root directories. Ensuring all web content directories have at least the equivalent of an index.html file is a significant factor to accomplish this end. Enumeration techniques, such as URL parameter manipulation, rely upon being able to obtain information about the web server's directory structure by locating directories without default pages. In the scenario, the web server will display to the user a listing of the files in the directory being accessed. By having a default hosted application web page, the anonymous web user will not obtain directory browsing information or an error message that reveals the server type and version. As a web server, tc Server can be vulnerable to enumeration techniques if steps are not taken to mitigate the vulnerability. Ensuring that every document directory has an “index.jsp” (or equivalent) file is one common sense approach to mitigating the vulnerability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -E -A 4 '<welcome-file-list' /usr/lib/vmware-casa/casa-webapp/conf/web.xml If a <welcome-file> node is not set to a default web page, this is a finding.

## Group: SRG-APP-000266-WSR-000142

**Group ID:** `V-241687`

### Rule: tc Server API must set the welcome-file node to a default web page.

**Rule ID:** `SV-241687r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The goal is to completely control the web user's experience in navigating any portion of the web document root directories. Ensuring all web content directories have at least the equivalent of an index.html file is a significant factor to accomplish this end. Enumeration techniques, such as URL parameter manipulation, rely upon being able to obtain information about the web server's directory structure by locating directories without default pages. In the scenario, the web server will display to the user a listing of the files in the directory being accessed. By having a default hosted application web page, the anonymous web user will not obtain directory browsing information or an error message that reveals the server type and version. As a web server, tc Server can be vulnerable to enumeration techniques if steps are not taken to mitigate the vulnerability. Ensuring that every document directory has an “index.jsp” (or equivalent) file is one common sense approach to mitigating the vulnerability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -E -A 4 '<welcome-file-list' /usr/lib/vmware-vcops/tomcat-enterprise/conf/web.xml If a <welcome-file> node is not set to a default web page, this is a finding.

## Group: SRG-APP-000266-WSR-000160

**Group ID:** `V-241688`

### Rule: tc Server UI must have the allowTrace parameter set to false.

**Rule ID:** `SV-241688r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web servers will often display error messages to client users displaying enough information to aid in the debugging of the error. The information given back in error messages may display the web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep allowTrace /usr/lib/vmware-vcops/tomcat-web-app/conf/server.xml If “allowTrace” is set to "true", this is a finding. Note: If no line is returned this is NOT a finding.

## Group: SRG-APP-000266-WSR-000160

**Group ID:** `V-241689`

### Rule: tc Server CaSa must have the allowTrace parameter set to false.

**Rule ID:** `SV-241689r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web servers will often display error messages to client users displaying enough information to aid in the debugging of the error. The information given back in error messages may display the web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep allowTrace /usr/lib/vmware-casa/casa-webapp/conf/server.xml If “allowTrace” is set to "true", this is a finding. Note: If no line is returned this is NOT a finding.

## Group: SRG-APP-000266-WSR-000160

**Group ID:** `V-241690`

### Rule: tc Server API must have the allowTrace parameter set to false.

**Rule ID:** `SV-241690r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web servers will often display error messages to client users displaying enough information to aid in the debugging of the error. The information given back in error messages may display the web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep allowTrace /usr/lib/vmware-vcops/tomcat-enterprise/conf/server.xml If “allowTrace” is set to "true", this is a finding. Note: If no line is returned this is NOT a finding.

## Group: SRG-APP-000266-WSR-000160

**Group ID:** `V-241691`

### Rule: tc Server UI must have the debug option turned off.

**Rule ID:** `SV-241691r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information needed by an attacker to begin looking for possible vulnerabilities in a web server includes any information about the web server and plug-ins or modules being used. When debugging or trace information is enabled in a production web server, information about the web server, such as web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage may be displayed. Since this information may be placed in logs and general messages during normal operation of the web server, an attacker does not need to cause an error condition to gain this information. As a Tomcat derivative, tc Server can be configured to set the debugging level. By setting the debugging level to zero (0), no debugging information will be provided to a malicious user. This provides a layer of defense to vROps.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -En -A 2 -B 1 '<param-name>debug</param-name>' /usr/lib/vmware-vcops/tomcat-web-app/conf/web.xml If all instances of the debug parameter are not set to "0", this is a finding.

## Group: SRG-APP-000266-WSR-000160

**Group ID:** `V-241692`

### Rule: tc Server CaSa must have the debug option turned off.

**Rule ID:** `SV-241692r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information needed by an attacker to begin looking for possible vulnerabilities in a web server includes any information about the web server and plug-ins or modules being used. When debugging or trace information is enabled in a production web server, information about the web server, such as web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage may be displayed. Since this information may be placed in logs and general messages during normal operation of the web server, an attacker does not need to cause an error condition to gain this information. As a Tomcat derivative, tc Server can be configured to set the debugging level. By setting the debugging level to zero (0), no debugging information will be provided to a malicious user. This provides a layer of defense to vROps.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -En -A 2 -B 1 '<param-name>debug</param-name>' /usr/lib/vmware-casa/casa-webapp/conf/web.xml If all instances of the debug parameter are not set to "0", this is a finding.

## Group: SRG-APP-000266-WSR-000160

**Group ID:** `V-241693`

### Rule: tc Server API must have the debug option turned off.

**Rule ID:** `SV-241693r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information needed by an attacker to begin looking for possible vulnerabilities in a web server includes any information about the web server and plug-ins or modules being used. When debugging or trace information is enabled in a production web server, information about the web server, such as web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage may be displayed. Since this information may be placed in logs and general messages during normal operation of the web server, an attacker does not need to cause an error condition to gain this information. As a Tomcat derivative, tc Server can be configured to set the debugging level. By setting the debugging level to zero (0), no debugging information will be provided to a malicious user. This provides a layer of defense to vROps.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -En -A 2 -B 1 '<param-name>debug</param-name>' /usr/lib/vmware-vcops/tomcat-enterprise/conf/web.xml If all instances of the debug parameter are not set to "0", this is a finding.

## Group: SRG-APP-000295-WSR-000134

**Group ID:** `V-241694`

### Rule: tc Server UI must set an inactive timeout for sessions.

**Rule ID:** `SV-241694r879673_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Leaving sessions open indefinitely is a major security risk. An attacker can easily use an already authenticated session to access the hosted application as the previously authenticated user. By closing sessions after a set period of inactivity, the web server can make certain that those sessions that are not closed through the user logging out of an application are eventually closed. tc Server provides a session timeout parameter in the web.xml configuration file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep session-timeout /usr/lib/vmware-vcops/tomcat-web-app/webapps/ui/WEB-INF/web.xml If the value of <session-timeout> is not “30” or is missing, this is a finding.

## Group: SRG-APP-000295-WSR-000134

**Group ID:** `V-241695`

### Rule: tc Server CaSa must set an inactive timeout for sessions.

**Rule ID:** `SV-241695r879673_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Leaving sessions open indefinitely is a major security risk. An attacker can easily use an already authenticated session to access the hosted application as the previously authenticated user. By closing sessions after a set period of inactivity, the web server can make certain that those sessions that are not closed through the user logging out of an application are eventually closed. tc Server provides a session timeout parameter in the web.xml configuration file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep session-timeout /usr/lib/vmware-casa/casa-webapp/webapps/admin/WEB-INF/web.xml If the value of <session-timeout> is not “30” or is missing, this is a finding.

## Group: SRG-APP-000295-WSR-000134

**Group ID:** `V-241696`

### Rule: tc Server API must set an inactive timeout for sessions.

**Rule ID:** `SV-241696r879673_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Leaving sessions open indefinitely is a major security risk. An attacker can easily use an already authenticated session to access the hosted application as the previously authenticated user. By closing sessions after a set period of inactivity, the web server can make certain that those sessions that are not closed through the user logging out of an application are eventually closed. tc Server provides a session timeout parameter in the web.xml configuration file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep session-timeout /usr/lib/vmware-vcops/tomcat-enterprise/conf/web.xml If the value of <session-timeout> is not “30” or is missing, this is a finding.

## Group: SRG-APP-000315-WSR-000003

**Group ID:** `V-241697`

### Rule: tc Server ALL must be configured to the correct user authentication source.

**Rule ID:** `SV-241697r879692_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. A web server can be accessed remotely and must be able to enforce remote access policy requirements or work in conjunction with enterprise tools designed to enforce policy requirements. vRealize Operations can be configured with a variety of authentication sources. Site policies and procedures will dictate the appropriate authentication mechanism.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the correct configuration data for the Authentication Source from the ISSO. Open a web browser, and put in the vROps URL. 1. Log into the Administration Portal 2. Click on Administration >> Authentication Sources 3. Click on Authentication Source 4. Verify that User Authentication is configured correctly If the Authentication Source is not configured in accordance with site policy, this is a finding.

## Group: SRG-APP-000315-WSR-000004

**Group ID:** `V-241698`

### Rule: tc Server UI must be configured to use the https scheme.

**Rule ID:** `SV-241698r879692_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. tc Server connections are managed by the Connector object class. By configuring external Connector objects to use the HTTPS scheme, vROps's information in flight will be protected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-web-app/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “scheme” is not set to “https” or is missing, this is a finding.

## Group: SRG-APP-000315-WSR-000004

**Group ID:** `V-241699`

### Rule: tc Server CaSa must be configured to use the https scheme.

**Rule ID:** `SV-241699r879692_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. tc Server connections are managed by the Connector object class. By configuring external Connector objects to use the HTTPS scheme, vROps's information in flight will be protected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-casa/casa-webapp/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “scheme” is not set to “https” or is missing, this is a finding.

## Group: SRG-APP-000315-WSR-000004

**Group ID:** `V-241700`

### Rule: tc Server API must be configured to use the https scheme.

**Rule ID:** `SV-241700r879692_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. tc Server connections are managed by the Connector object class. By configuring external Connector objects to use the HTTPS scheme, vROps's information in flight will be protected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-enterprise/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “scheme” is not set to “https” or is missing, this is a finding.

## Group: SRG-APP-000357-WSR-000150

**Group ID:** `V-241701`

### Rule: tc Server ALL must use a logging mechanism that is configured to allocate log record storage capacity large enough to accommodate the logging requirements of the web server.

**Rule ID:** `SV-241701r879730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to make certain that the logging mechanism used by the web server has sufficient storage capacity in which to write the logs, the logging mechanism needs to be able to allocate log record storage capacity. The task of allocating log record storage capacity is usually performed during initial installation of the logging mechanism. The system administrator will usually coordinate the allocation of physical drive space with the web server administrator along with the physical location of the partition and disk. Refer to NIST SP 800-92 for specific requirements on log rotation and storage dependent on the impact of the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Determine if tc Server ALL is using a logging mechanism that is configured to have a capacity large enough to accommodate logging requirements. If the logging mechanism does not have sufficient capacity, this is a finding.

## Group: SRG-APP-000358-WSR-000163

**Group ID:** `V-241702`

### Rule: tc Server ALL log files must be moved to a permanent repository in accordance with site policy.

**Rule ID:** `SV-241702r879731_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server will typically utilize logging mechanisms for maintaining a historical log of activity that occurs within a hosted application. This information can then be used for diagnostic purposes, forensics purposes, or other purposes relevant to ensuring the availability and integrity of the hosted application. Log files must be periodically moved from the web server to a permanent storage location. This serves two beneficial purposes. First, the web server's resources are freed up for productions. Also, this ensures that the site has, and enforces, policies designed to preserve the integrity of historical logs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Review the site policy for moving log files from the web server to a permanent repository. Ensure that log files are being moved from the web server in accordance with the site policy. If the site does not have a policy for periodically moving log files to an archive repository or such policy is not being enforced, this is a finding.

## Group: SRG-APP-000359-WSR-000065

**Group ID:** `V-241703`

### Rule: tc Server ALL must use a logging mechanism that is configured to provide a warning to the ISSO and SA when allocated record storage volume reaches 75% of maximum log record storage capacity.

**Rule ID:** `SV-241703r879732_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process logs as required. Log processing failures include: software/hardware errors, failures in the log capturing mechanisms, and log storage capacity being reached or exceeded. If log capacity were to be exceeded, then events subsequently occurring would not be recorded. Organizations must define a maximum allowable percentage of storage capacity serving as an alarming threshold (e.g., web server has exceeded 75% of log storage capacity allocated), at which time the web server or the logging mechanism the web server utilizes will provide a warning to the ISSO and SA at a minimum. This requirement can be met by configuring the web server to utilize a dedicated log tool that meets this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Review site documentation and system configuration. Determine if the system has a logging mechanism that will provide a warning to the ISSO and SA when allocated record storage volume reaches 75% of maximum log record storage capacity. If such an alert mechanism is not in use, this is a finding.

## Group: SRG-APP-000374-WSR-000172

**Group ID:** `V-241704`

### Rule: tc Server UI must generate log records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

**Rule ID:** `SV-241704r879747_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis across multiple devices and log records. Time stamps generated by the web server include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC. Like all web servers, tc Server logs can be configured to produce a Common Log Format (CLF). The tc Server component known as an “AccessLogValve”, which represents a component that can be inserted into the request processing pipeline to capture user interaction. The “Access Log Valve” creates log files in the same format as those created by standard web servers including GMT offset.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/product-ui/localhost_access_log.YYYY-MM-dd.txt If the timestamp does not contain a time zone mapping, this is a finding. Note: Substitute the actual date in the file name. Note: In Common Log Format, a timestamp will look like [06/Feb/2016:23:12:57 +0000]. The “+0000” part is the time zone mapping.

## Group: SRG-APP-000374-WSR-000172

**Group ID:** `V-241705`

### Rule: tc Server CaSa must generate log records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

**Rule ID:** `SV-241705r879747_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis across multiple devices and log records. Time stamps generated by the web server include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC. Like all web servers, tc Server logs can be configured to produce a Common Log Format (CLF). The tc Server component known as an “AccessLogValve”, which represents a component that can be inserted into the request processing pipeline to capture user interaction. The “Access Log Valve” creates log files in the same format as those created by standard web servers including GMT offset.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/casa/localhost_access_log.YYYY-MM-dd.txt If the timestamp does not contain a time zone mapping, this is a finding. Note: Substitute the actual date in the file name. Note: In Common Log Format, a timestamp will look like [06/Feb/2016:23:12:57 +0000]. The “+0000” part is the time zone mapping.

## Group: SRG-APP-000374-WSR-000172

**Group ID:** `V-241706`

### Rule: tc Server API must generate log records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

**Rule ID:** `SV-241706r879747_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis across multiple devices and log records. Time stamps generated by the web server include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC. Like all web servers, tc Server logs can be configured to produce a Common Log Format (CLF). The tc Server component known as an “AccessLogValve”, which represents a component that can be inserted into the request processing pipeline to capture user interaction. The “Access Log Valve” creates log files in the same format as those created by standard web servers including GMT offset.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/suite-api/localhost_access_log.YYYY-MM-dd.txt If the timestamp does not contain a time zone mapping, this is a finding. Note: Substitute the actual date in the file name. Note: In Common Log Format, a timestamp will look like [06/Feb/2016:23:12:57 +0000]. The “+0000” part is the time zone mapping.

## Group: SRG-APP-000375-WSR-000171

**Group ID:** `V-241707`

### Rule: tc Server UI must record time stamps for log records to a minimum granularity of one second.

**Rule ID:** `SV-241707r879748_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without sufficient granularity of time stamps, it is not possible to adequately determine the chronological order of records. Time stamps generated by the web server include date and time and must be to a granularity of one second. Like all web servers, tc Server logs can be configured to produce a Common Log Format (CLF). The tc Server component known as an “AccessLogValve”, which represents a component that can be inserted into the request processing pipeline to capture user interaction. The “Access Log Valve” should be configured to ensure that investigators have sufficient information to conduct an appropriate audit.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/product-ui/localhost_access_log.YYYY-MM-dd.txt If the timestamp does not contain a minimum granularity of one second, this is a finding. Note: Substitute the actual date in the file name. Note: In Common Log Format, a timestamp will look like [06/Feb/2016:23:12:57 +0000]. The “57” part is the “seconds” part of the timestamp.

## Group: SRG-APP-000375-WSR-000171

**Group ID:** `V-241708`

### Rule: tc Server CaSa must record time stamps for log records to a minimum granularity of one second.

**Rule ID:** `SV-241708r879748_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without sufficient granularity of time stamps, it is not possible to adequately determine the chronological order of records. Time stamps generated by the web server include date and time and must be to a granularity of one second. Like all web servers, tc Server logs can be configured to produce a Common Log Format (CLF). The tc Server component known as an “AccessLogValve”, which represents a component that can be inserted into the request processing pipeline to capture user interaction. The “Access Log Valve” should be configured to ensure that investigators have sufficient information to conduct an appropriate audit.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/casa/localhost_access_log.YYYY-MM-dd.txt If the timestamp does not contain a minimum granularity of one second, this is a finding. Note: Substitute the actual date in the file name. Note: In Common Log Format, a timestamp will look like [06/Feb/2016:23:12:57 +0000]. The “57” part is the “seconds” part of the timestamp.

## Group: SRG-APP-000375-WSR-000171

**Group ID:** `V-241709`

### Rule: tc Server API must record time stamps for log records to a minimum granularity of one second.

**Rule ID:** `SV-241709r879748_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without sufficient granularity of time stamps, it is not possible to adequately determine the chronological order of records. Time stamps generated by the web server include date and time and must be to a granularity of one second. Like all web servers, tc Server logs can be configured to produce a Common Log Format (CLF). The tc Server component known as an AccessLogValve, which represents a component that can be inserted into the request processing pipeline to capture user interaction. The Access Log Valve should be configured to ensure that investigators have sufficient information to conduct an appropriate audit.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: tail /storage/log/vcops/log/suite-api/localhost_access_log.YYYY-MM-dd.txt If the timestamp does not contain a minimum granularity of one second, this is a finding. Note: Substitute the actual date in the file name. Note: In Common Log Format, a timestamp will look like [06/Feb/2016:23:12:57 +0000]. The “57” part is the “seconds” part of the timestamp.

## Group: SRG-APP-000380-WSR-000072

**Group ID:** `V-241710`

### Rule: tc Server UI application, libraries, and configuration files must only be accessible to privileged users.

**Rule ID:** `SV-241710r879753_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can be modified through parameter modification, patch installation, upgrades to the web server or modules, and security parameter changes. With each of these changes, there is the potential for an adverse effect such as a DoS, web server instability, or hosted application instability. To limit changes to the web server and limit exposure to any adverse effects from the changes, files such as the web server application files, libraries, and configuration files must have permissions and ownership set properly to only allow privileged users access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following commands: cd /usr/lib/vmware-vcops/tomcat-web-app ls -alR bin lib conf | grep -E '^-' | awk '$1 !~ /---$/ {print}' If the command produces any output, this is a finding.

## Group: SRG-APP-000380-WSR-000072

**Group ID:** `V-241711`

### Rule: tc Server CaSa application, libraries, and configuration files must only be accessible to privileged users.

**Rule ID:** `SV-241711r879753_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can be modified through parameter modification, patch installation, upgrades to the web server or modules, and security parameter changes. With each of these changes, there is the potential for an adverse effect such as a DoS, web server instability, or hosted application instability. To limit changes to the web server and limit exposure to any adverse effects from the changes, files such as the web server application files, libraries, and configuration files must have permissions and ownership set properly to only allow privileged users access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following commands: cd /usr/lib/vmware-casa/casa-webapp ls -alR bin lib conf | grep -E '^-' | awk '$1 !~ /---$/ {print}' If the command produces any output, this is a finding.

## Group: SRG-APP-000380-WSR-000072

**Group ID:** `V-241712`

### Rule: tc Server API application, libraries, and configuration files must only be accessible to privileged users.

**Rule ID:** `SV-241712r879753_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can be modified through parameter modification, patch installation, upgrades to the web server or modules, and security parameter changes. With each of these changes, there is the potential for an adverse effect such as a DoS, web server instability, or hosted application instability. To limit changes to the web server and limit exposure to any adverse effects from the changes, files such as the web server application files, libraries, and configuration files must have permissions and ownership set properly to only allow privileged users access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following commands: cd /usr/lib/vmware-vcops/tomcat-enterprise ls -alR bin conf | grep -E '^-' | awk '$1 !~ /---$/ {print}' If the command produces any output, this is a finding.

## Group: SRG-APP-000383-WSR-000175

**Group ID:** `V-241713`

### Rule: tc Server UI must be configured with the appropriate ports.

**Rule ID:** `SV-241713r879756_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web servers provide numerous processes, features, and functionalities that utilize TCP/IP ports. Some of these processes may be deemed unnecessary or too unsecure to run on a production system. The web server must provide the capability to disable or deactivate network-related services that are deemed to be non-essential to the server mission, are too unsecure, or are prohibited by the PPSM CAL and vulnerability assessments. An essential configuration file for tc Server is “catalina.properties”. The ports that tc Server listens to will be configured in that file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: cat /usr/lib/vmware-vcops/tomcat-web-app/conf/catalina.properties | grep -E '\.port' Review the listed ports. Verify that they match the list below of tc Server UI ports. base.shutdown.port=-1 base.jmx.port=6969 vmware-ssl.https.port=8443 vmware-ajp13.jk.port=8009 vmware-ajp13.https.port=8443 vmware-bio.http.port=8080 vmware-bio.https.port=8443 If the ports are not as listed, this is a finding.

## Group: SRG-APP-000383-WSR-000175

**Group ID:** `V-241714`

### Rule: tc Server CaSa must be configured with the appropriate ports.

**Rule ID:** `SV-241714r879756_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web servers provide numerous processes, features, and functionalities that utilize TCP/IP ports. Some of these processes may be deemed unnecessary or too unsecure to run on a production system. The web server must provide the capability to disable or deactivate network-related services that are deemed to be non-essential to the server mission, are too unsecure, or are prohibited by the PPSM CAL and vulnerability assessments. An essential configuration file for tc Server is “catalina.properties”. The ports that tc Server listens to will be configured in that file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: cat /usr/lib/vmware-casa/casa-webapp/conf/catalina.properties | grep -E '\.port' Review the listed ports. Verify that they match the list below of tc Server CaSa ports. base.shutdown.port=-1 base.jmx.port=6968 vmware-ajp13.jk.port=8011 vmware-ajp13.https.port=8445 vmware-casa.https.port=8445 vmware-casa.client.auth.port=8447 vmware-bio.http.port=8082 vmware-bio.https.port=8445 If the ports are not as listed, this is a finding.

## Group: SRG-APP-000383-WSR-000175

**Group ID:** `V-241715`

### Rule: tc Server API must be configured with the appropriate ports.

**Rule ID:** `SV-241715r879756_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web servers provide numerous processes, features, and functionalities that utilize TCP/IP ports. Some of these processes may be deemed unnecessary or too unsecure to run on a production system. The web server must provide the capability to disable or deactivate network-related services that are deemed to be non-essential to the server mission, are too unsecure, or are prohibited by the PPSM CAL and vulnerability assessments. An essential configuration file for tc Server is “catalina.properties”. The ports that tc Server listens to will be configured in that file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: cat /usr/lib/vmware-vcops/tomcat-enterprise/conf/catalina.properties | grep -E '\.port' Review the listed ports. Verify that they match the list below of tc Server API ports. base.shutdown.port=-1 bio-ssl.https.port=8440 bio.http.port=8081 bio.https.port=8440 jk.port=8010 vmware-ajp13.jk.port=8010 vmware-ajp13.https.port=8440 vmware-ssl.https.port=8440 vmware-ajp13.jk.port=8010 vmware-ajp13.https.port=8440 If the ports are not as listed, this is a finding.

## Group: SRG-APP-000416-WSR-000118

**Group ID:** `V-241716`

### Rule: tc Server UI must use NSA Suite A cryptography when encrypting data that must be compartmentalized.

**Rule ID:** `SV-241716r879944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cryptography is only as strong as the encryption modules/algorithms employed to encrypt the data. Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. NSA has developed Type 1 algorithms for protecting classified information. The Committee on National Security Systems (CNSS) National Information Assurance Glossary (CNSS Instruction No. 4009) defines Type 1 products as: "Cryptographic equipment, assembly or component classified or certified by NSA for encrypting and decrypting classified and sensitive national security information when appropriately keyed. Developed using established NSA business processes and containing NSA-approved algorithms are used to protect systems requiring the most stringent protection mechanisms." Although persons may have a security clearance, they may not have a "need-to-know" and are required to be separated from the information in question. The web server must employ NSA-approved cryptography to protect classified information from those individuals who have no "need-to-know" or when encryption of compartmentalized data is required by data classification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is not implemented to process compartmentalized information, this requirement is Not Applicable. At the command prompt, execute the following command: grep vmware-ssl.ssl.ciphers.list /usr/lib/vmware-vcops/tomcat-web-app/conf/catalina.properties If the value of "vmware-ssl.ssl.ciphers.list" does not match the list of NSA Suite A ciphers or is missing, this is a finding.

## Group: SRG-APP-000416-WSR-000118

**Group ID:** `V-241717`

### Rule: tc Server CaSa must use NSA Suite A cryptography when encrypting data that must be compartmentalized.

**Rule ID:** `SV-241717r879944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cryptography is only as strong as the encryption modules/algorithms employed to encrypt the data. Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. NSA has developed Type 1 algorithms for protecting classified information. The Committee on National Security Systems (CNSS) National Information Assurance Glossary (CNSS Instruction No. 4009) defines Type 1 products as: "Cryptographic equipment, assembly or component classified or certified by NSA for encrypting and decrypting classified and sensitive national security information when appropriately keyed. Developed using established NSA business processes and containing NSA-approved algorithms are used to protect systems requiring the most stringent protection mechanisms." Although persons may have a security clearance, they may not have a "need-to-know" and are required to be separated from the information in question. The web server must employ NSA-approved cryptography to protect classified information from those individuals who have no "need-to-know" or when encryption of compartmentalized data is required by data classification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is not implemented to process compartmentalized information, this requirement is Not Applicable. At the command prompt, execute the following command: grep -A 10 vmware-casa.ssl.ciphers.list /usr/lib/vmware-casa/casa-webapp/conf/catalina.properties If the value of "vmware-casa.ssl.ciphers.list" does not match the list of NSA Suite A ciphers or is missing, this is a finding.

## Group: SRG-APP-000416-WSR-000118

**Group ID:** `V-241718`

### Rule: tc Server API must use NSA Suite A cryptography when encrypting data that must be compartmentalized.

**Rule ID:** `SV-241718r879944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cryptography is only as strong as the encryption modules/algorithms employed to encrypt the data. Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. NSA has developed Type 1 algorithms for protecting classified information. The Committee on National Security Systems (CNSS) National Information Assurance Glossary (CNSS Instruction No. 4009) defines Type 1 products as: "Cryptographic equipment, assembly or component classified or certified by NSA for encrypting and decrypting classified and sensitive national security information when appropriately keyed. Developed using established NSA business processes and containing NSA-approved algorithms are used to protect systems requiring the most stringent protection mechanisms." Although persons may have a security clearance, they may not have a "need-to-know" and are required to be separated from the information in question. The web server must employ NSA-approved cryptography to protect classified information from those individuals who have no "need-to-know" or when encryption of compartmentalized data is required by data classification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is not implemented to process compartmentalized information, this requirement is Not Applicable. At the command prompt, execute the following command: grep vmware-ssl.ssl.ciphers.list /usr/lib/vmware-vcops/tomcat-enterprise/conf/catalina.properties If the value of "vmware-ssl.ssl.ciphers.list" does not match the list of NSA Suite A ciphers or is missing, this is a finding.

## Group: SRG-APP-000435-WSR-000147

**Group ID:** `V-241719`

### Rule: tc Server UI must disable the shutdown port.

**Rule ID:** `SV-241719r879806_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An attacker has at least two reasons to stop a web server. The first is to cause a DoS, and the second is to put in place changes the attacker made to the web server configuration. As a Tomcat derivative, tc Server uses a port (defaults to 8005) as a shutdown port. If enabled, a shutdown signal can be sent to tc Server through this port. To ensure availability, the shutdown port should be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep base.shutdown.port /usr/lib/vmware-vcops/tomcat-web-app/conf/catalina.properties If the value of "base.shutdown.port" is not set to "-1" or is missing, this is a finding.

## Group: SRG-APP-000435-WSR-000147

**Group ID:** `V-241720`

### Rule: tc Server CaSa must disable the shutdown port.

**Rule ID:** `SV-241720r879806_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An attacker has at least two reasons to stop a web server. The first is to cause a DoS, and the second is to put in place changes the attacker made to the web server configuration. As a Tomcat derivative, tc Server uses a port (defaults to 8005) as a shutdown port. If enabled, a shutdown signal can be sent to tc Server through this port. To ensure availability, the shutdown port should be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep base.shutdown.port /usr/lib/vmware-casa/casa-webapp/conf/catalina.properties If the value of "base.shutdown.port" is not set to "-1" or is missing, this is a finding.

## Group: SRG-APP-000435-WSR-000147

**Group ID:** `V-241721`

### Rule: tc Server API must disable the shutdown port.

**Rule ID:** `SV-241721r879806_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An attacker has at least two reasons to stop a web server. The first is to cause a DoS, and the second is to put in place changes the attacker made to the web server configuration. As a Tomcat derivative, tc Server uses a port (defaults to 8005) as a shutdown port. If enabled, a shutdown signal can be sent to tc Server through this port. To ensure availability, the shutdown port should be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep base.shutdown.port /usr/lib/vmware-vcops/tomcat-enterprise/conf/catalina.properties If the value of "base.shutdown.port" is not set to "-1" or is missing, this is a finding.

## Group: SRG-APP-000439-WSR-000151

**Group ID:** `V-241722`

### Rule: tc Server UI must employ cryptographic mechanisms (TLS/DTLS/SSL) preventing the unauthorized disclosure of information during transmission.

**Rule ID:** `SV-241722r928837_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that the web server take measures to employ some form of cryptographic mechanism in order to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS). Transmission of data can take place between the web server and a large number of devices/applications external to the web server. Examples are a web client used by a user, a backend database, an audit server, or other web servers in a web cluster. tc Server connections are managed by the Connector object class. The Connector object can be configured to use a range of transport encryption methods. Many older transport encryption methods have been proven to be weak. vROps should be configured to use modern, secure forms of transport encryption.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-web-app/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “sslProtocol” is not set to “TLS” or is missing, this is a finding.

## Group: SRG-APP-000439-WSR-000151

**Group ID:** `V-241723`

### Rule: tc Server CaSa must employ cryptographic mechanisms (TLS/DTLS/SSL) preventing the unauthorized disclosure of information during transmission.

**Rule ID:** `SV-241723r928837_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that the web server take measures to employ some form of cryptographic mechanism in order to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS). Transmission of data can take place between the web server and a large number of devices/applications external to the web server. Examples are a web client used by a user, a backend database, an audit server, or other web servers in a web cluster. tc Server connections are managed by the Connector object class. The Connector object can be configured to use a range of transport encryption methods. Many older transport encryption methods have been proven to be weak. vROps should be configured to use modern, secure forms of transport encryption.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-casa/casa-webapp/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “sslProtocol” is not set to “TLS’ or is missing, this is a finding.

## Group: SRG-APP-000439-WSR-000151

**Group ID:** `V-241724`

### Rule: tc Server API must employ cryptographic mechanisms (TLS/DTLS/SSL) preventing the unauthorized disclosure of information during transmission.

**Rule ID:** `SV-241724r928837_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that the web server take measures to employ some form of cryptographic mechanism in order to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS). Transmission of data can take place between the web server and a large number of devices/applications external to the web server. Examples are a web client used by a user, a backend database, an audit server, or other web servers in a web cluster. tc Server connections are managed by the Connector object class. The Connector object can be configured to use a range of transport encryption methods. Many older transport encryption methods have been proven to be weak. vROps should be configured to use modern, secure forms of transport encryption.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-enterprise/conf/server.xml. Navigate to the <Connector> node that contains [port="${vmware-ssl.https.port}"]. If the value of “sslProtocol” is not set to “TLS” or is missing, this is a finding.

## Group: SRG-APP-000439-WSR-000152

**Group ID:** `V-241725`

### Rule: tc Server UI session IDs must be sent to the client using SSL/TLS.

**Rule ID:** `SV-241725r879810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The HTTP protocol is a stateless protocol. To maintain a session, a session identifier is used. The session identifier is a piece of data that is used to identify a session and a user. If the session identifier is compromised by an attacker, the session can be hijacked. By encrypting the session identifier, the identifier becomes more difficult for an attacker to hijack, decrypt, and use before the session has expired. tc Server connections are managed by the Connector object class. The Connector object can be configured to use a range of transport encryption methods. Many older transport encryption methods have been proven to be weak. vROps should be configured to use modern, secure forms of transport encryption.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-web-app/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “sslProtocol” is not set to “TLS” or is missing, this is a finding.

## Group: SRG-APP-000439-WSR-000152

**Group ID:** `V-241726`

### Rule: tc Server CaSa session IDs must be sent to the client using SSL/TLS.

**Rule ID:** `SV-241726r879810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The HTTP protocol is a stateless protocol. To maintain a session, a session identifier is used. The session identifier is a piece of data that is used to identify a session and a user. If the session identifier is compromised by an attacker, the session can be hijacked. By encrypting the session identifier, the identifier becomes more difficult for an attacker to hijack, decrypt, and use before the session has expired. tc Server connections are managed by the Connector object class. The Connector object can be configured to use a range of transport encryption methods. Many older transport encryption methods have been proven to be weak. vROps should be configured to use modern, secure forms of transport encryption.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-casa/casa-webapp/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “sslProtocol” is not set to “TLS” or is missing, this is a finding.

## Group: SRG-APP-000439-WSR-000152

**Group ID:** `V-241727`

### Rule: tc Server API session IDs must be sent to the client using SSL/TLS.

**Rule ID:** `SV-241727r879810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The HTTP protocol is a stateless protocol. To maintain a session, a session identifier is used. The session identifier is a piece of data that is used to identify a session and a user. If the session identifier is compromised by an attacker, the session can be hijacked. By encrypting the session identifier, the identifier becomes more difficult for an attacker to hijack, decrypt, and use before the session has expired. tc Server connections are managed by the Connector object class. The Connector object can be configured to use a range of transport encryption methods. Many older transport encryption methods have been proven to be weak. vROps should be configured to use modern, secure forms of transport encryption.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-enterprise/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “sslProtocol” is not set to “TLS” or is missing, this is a finding.

## Group: SRG-APP-000439-WSR-000154

**Group ID:** `V-241728`

### Rule: tc Server UI must set the useHttpOnly parameter.

**Rule ID:** `SV-241728r879810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A cookie can be read by client-side scripts easily if cookie properties are not set properly. By allowing cookies to be read by the client-side scripts, information such as session identifiers could be compromised and used by an attacker who intercepts the cookie. Setting cookie properties (i.e. HttpOnly property) to disallow client-side scripts from reading cookies better protects the information inside the cookie. As a Tomcat derivative, tc Server contains a Context object, which represents a web application running within a particular virtual host. One of the configurable parameters of the Context object will prevent the tc Server cookies from being accessed by JavaScript from another site.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep useHttpOnly /usr/lib/vmware-vcops/tomcat-web-app/webapps/ui/META-INF/context.xml If the value of “useHttpOnly” is not set to "true" or is missing, this is a finding. Expected Result: <Context useHttpOnly="true">

## Group: SRG-APP-000439-WSR-000154

**Group ID:** `V-241729`

### Rule: tc Server CaSa must set the useHttpOnly parameter.

**Rule ID:** `SV-241729r879810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A cookie can be read by client-side scripts easily if cookie properties are not set properly. By allowing cookies to be read by the client-side scripts, information such as session identifiers could be compromised and used by an attacker who intercepts the cookie. Setting cookie properties (i.e. HttpOnly property) to disallow client-side scripts from reading cookies better protects the information inside the cookie. As a Tomcat derivative, tc Server contains a Context object, which represents a web application running within a particular virtual host. One of the configurable parameters of the Context object will prevent the tc Server cookies from being accessed by JavaScript from another site.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep useHttpOnly /usr/lib/vmware-casa/casa-webapp/conf/context.xml If the value of “useHttpOnly” is not set to "true" or is missing, this is a finding. Expected Result: <Context useHttpOnly="true">

## Group: SRG-APP-000439-WSR-000154

**Group ID:** `V-241730`

### Rule: tc Server API must set the useHttpOnly parameter.

**Rule ID:** `SV-241730r879810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A cookie can be read by client-side scripts easily if cookie properties are not set properly. By allowing cookies to be read by the client-side scripts, information such as session identifiers could be compromised and used by an attacker who intercepts the cookie. Setting cookie properties (i.e. HttpOnly property) to disallow client-side scripts from reading cookies better protects the information inside the cookie. As a Tomcat derivative, tc Server contains a Context object, which represents a web application running within a particular virtual host. One of the configurable parameters of the Context object will prevent the tc Server cookies from being accessed by JavaScript from another site.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep useHttpOnly /usr/lib/vmware-vcops/tomcat-enterprise/conf/context.xml If the value of “useHttpOnly” is not set to "true" or is missing, this is a finding. Expected Result: <Context useHttpOnly="true">

## Group: SRG-APP-000439-WSR-000155

**Group ID:** `V-241731`

### Rule: tc Server UI must set the secure flag for cookies.

**Rule ID:** `SV-241731r879810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cookies can be sent to a client using TLS/SSL to encrypt the cookies, but TLS/SSL is not used by every hosted application since the data being displayed does not require the encryption of the transmission. To safeguard against cookies, especially session cookies, being sent in plaintext, a cookie can be encrypted before transmission. To force a cookie to be encrypted before transmission, the cookie Secure property can be set. As a Tomcat derivative, tc Server is based in part on the Java Servlet specification. Servlet 3.0 (Java EE 6) introduced a standard way to configure secure attribute for the session cookie, this can be done by applying the correct configuration in web.xml.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -E '<secure>' /usr/lib/vmware-vcops/tomcat-web-app/webapps/ui/WEB-INF/web.xml If the value of the <secure> node is not set to "true" or is missing, this is a finding.

## Group: SRG-APP-000439-WSR-000155

**Group ID:** `V-241732`

### Rule: tc Server CaSa must set the secure flag for cookies.

**Rule ID:** `SV-241732r879810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cookies can be sent to a client using TLS/SSL to encrypt the cookies, but TLS/SSL is not used by every hosted application since the data being displayed does not require the encryption of the transmission. To safeguard against cookies, especially session cookies, being sent in plaintext, a cookie can be encrypted before transmission. To force a cookie to be encrypted before transmission, the cookie Secure property can be set. As a Tomcat derivative, tc Server is based in part on the Java Servlet specification. Servlet 3.0 (Java EE 6) introduced a standard way to configure secure attribute for the session cookie, this can be done by applying the correct configuration in web.xml.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -E '<secure>' /usr/lib/vmware-casa/casa-webapp/conf/web.xml If the value of the <secure> node is not set to "true" or is missing, this is a finding.

## Group: SRG-APP-000439-WSR-000155

**Group ID:** `V-241733`

### Rule: tc Server API must set the secure flag for cookies.

**Rule ID:** `SV-241733r879810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cookies can be sent to a client using TLS/SSL to encrypt the cookies, but TLS/SSL is not used by every hosted application since the data being displayed does not require the encryption of the transmission. To safeguard against cookies, especially session cookies, being sent in plaintext, a cookie can be encrypted before transmission. To force a cookie to be encrypted before transmission, the cookie Secure property can be set. As a Tomcat derivative, tc Server is based in part on the Java Servlet specification. Servlet 3.0 (Java EE 6) introduced a standard way to configure secure attribute for the session cookie, this can be done by applying the correct configuration in web.xml.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -E '<secure>' /usr/lib/vmware-vcops/tomcat-enterprise/conf/web.xml If the value of the <secure> node is not set to "true" or is missing, this is a finding.

## Group: SRG-APP-000439-WSR-000156

**Group ID:** `V-241734`

### Rule: tc Server UI must set sslEnabledProtocols to an approved Transport Layer Security (TLS) version.

**Rule ID:** `SV-241734r879810_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Transport Layer Security (TLS) is a required transmission protocol for a web server hosting controlled information. The use of TLS provides confidentiality of data in transit between the web server and client. FIPS 140-2 approved TLS versions must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 defines the approved TLS versions for government applications. tc Server connections are managed by the Connector object class. The Connector object can be configured to use a range of transport encryption methods. Many older transport encryption methods have been proven to be weak. vROps should be configured to use the “sslEnabledProtocols” correctly to ensure that older, less secure forms of transport security are not used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-web-app/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “sslEnabledProtocols” is not set to “TLSv1.2,TLSv1.1,TLSv1” or is missing, this is a finding.

## Group: SRG-APP-000439-WSR-000156

**Group ID:** `V-241735`

### Rule: tc Server CaSa must set sslEnabledProtocols to an approved Transport Layer Security (TLS) version.

**Rule ID:** `SV-241735r879810_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Transport Layer Security (TLS) is a required transmission protocol for a web server hosting controlled information. The use of TLS provides confidentiality of data in transit between the web server and client. FIPS 140-2 approved TLS versions must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 defines the approved TLS versions for government applications. tc Server connections are managed by the Connector object class. The Connector object can be configured to use a range of transport encryption methods. Many older transport encryption methods have been proven to be weak. vROps should be configured to use the “sslEnabledProtocols” correctly to ensure that older, less secure forms of transport security are not used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-casa/casa-webapp/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “sslEnabledProtocols” is not set to “TLSv1.2,TLSv1.1,TLSv1” or is missing, this is a finding.

## Group: SRG-APP-000439-WSR-000156

**Group ID:** `V-241736`

### Rule: tc Server API must set sslEnabledProtocols to an approved Transport Layer Security (TLS) version.

**Rule ID:** `SV-241736r879810_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Transport Layer Security (TLS) is a required transmission protocol for a web server hosting controlled information. The use of TLS provides confidentiality of data in transit between the web server and client. FIPS 140-2 approved TLS versions must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 defines the approved TLS versions for government applications. tc Server connections are managed by the Connector object class. The Connector object can be configured to use a range of transport encryption methods. Many older transport encryption methods have been proven to be weak. vROps should be configured to use the “sslEnabledProtocols” correctly to ensure that older, less secure forms of transport security are not used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-enterprise/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “sslEnabledProtocols” is not set to “TLSv1.2,TLSv1.1,TLSv1” or is missing, this is a finding.

## Group: SRG-APP-000439-WSR-000188

**Group ID:** `V-241737`

### Rule: tc Server UI must remove all export ciphers to protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-241737r879810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>During the initial setup of a Transport Layer Security (TLS) connection to the web server, the client sends a list of supported cipher suites in order of preference. The web server will reply with the cipher suite it will use for communication from the client list. If an attacker can intercept the submission of cipher suites to the web server and place, as the preferred cipher suite, a weak export suite, the encryption used for the session becomes easy for the attacker to break, often within minutes to hours. An essential configuration file for tc Server is “catalina.properties”. Properly configured, tc Server will not provide the weaker, export ciphers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep vmware-ssl.ssl.ciphers.list /usr/lib/vmware-vcops/tomcat-web-app/conf/catalina.properties If any export ciphers are listed, this is a finding. Note: To view a list of export ciphers, at the command prompt execute the following command: openssl ciphers 'EXP'

## Group: SRG-APP-000439-WSR-000188

**Group ID:** `V-241738`

### Rule: tc Server CaSa must remove all export ciphers to protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-241738r879810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>During the initial setup of a Transport Layer Security (TLS) connection to the web server, the client sends a list of supported cipher suites in order of preference. The web server will reply with the cipher suite it will use for communication from the client list. If an attacker can intercept the submission of cipher suites to the web server and place, as the preferred cipher suite, a weak export suite, the encryption used for the session becomes easy for the attacker to break, often within minutes to hours. An essential configuration file for tc Server is “catalina.properties”. Properly configured, tc Server will not provide the weaker, export ciphers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep -A 10 vmware-casa.ssl.ciphers.list /usr/lib/vmware-casa/casa-webapp/conf/catalina.properties If any export ciphers are listed, this is a finding. Note: To view a list of export ciphers, at the command prompt execute the following command: openssl ciphers 'EXP'

## Group: SRG-APP-000439-WSR-000188

**Group ID:** `V-241739`

### Rule: tc Server API must remove all export ciphers to protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-241739r879810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>During the initial setup of a Transport Layer Security (TLS) connection to the web server, the client sends a list of supported cipher suites in order of preference. The web server will reply with the cipher suite it will use for communication from the client list. If an attacker can intercept the submission of cipher suites to the web server and place, as the preferred cipher suite, a weak export suite, the encryption used for the session becomes easy for the attacker to break, often within minutes to hours. An essential configuration file for tc Server is “catalina.properties”. Properly configured, tc Server will not provide the weaker, export ciphers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep vmware-ssl.ssl.ciphers.list /usr/lib/vmware-vcops/tomcat-enterprise/conf/catalina.properties If any export ciphers are listed, this is a finding. Note: To view a list of export ciphers, at the command prompt execute the following command: openssl ciphers 'EXP'

## Group: SRG-APP-000442-WSR-000182

**Group ID:** `V-241740`

### Rule: tc Server UI must use approved Transport Layer Security (TLS) versions to maintain the confidentiality and integrity of information during reception.

**Rule ID:** `SV-241740r879813_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Protecting the confidentiality and integrity of received information requires that application servers take measures to employ approved cryptography in order to protect the information during transmission over the network. This is usually achieved through the use of Transport Layer Security (TLS), SSL VPN, or IPsec tunnel. tc Server connections are managed by the Connector object class. The Connector object can be configured to use a range of transport encryption methods. Many older transport encryption methods have been proven to be weak. vROps should be configured to use the “sslEnabledProtocols” correctly to ensure that older, less secure forms of transport security are not used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-web-app/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “sslEnabledProtocols” is not set to “TLSv1.2,TLSv1.1,TLSv1” or is missing, this is a finding.

## Group: SRG-APP-000442-WSR-000182

**Group ID:** `V-241741`

### Rule: tc Server CaSa must use approved Transport Layer Security (TLS) versions to maintain the confidentiality and integrity of information during reception.

**Rule ID:** `SV-241741r879813_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Protecting the confidentiality and integrity of received information requires that application servers take measures to employ approved cryptography in order to protect the information during transmission over the network. This is usually achieved through the use of Transport Layer Security (TLS), SSL VPN, or IPsec tunnel. tc Server connections are managed by the Connector object class. The Connector object can be configured to use a range of transport encryption methods. Many older transport encryption methods have been proven to be weak. vROps should be configured to use the “sslEnabledProtocols” correctly to ensure that older, less secure forms of transport security are not used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-casa/casa-webapp/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “sslEnabledProtocols” is not set to “TLSv1.2,TLSv1.1,TLSv1” or is missing, this is a finding.

## Group: SRG-APP-000442-WSR-000182

**Group ID:** `V-241742`

### Rule: tc Server API must use approved Transport Layer Security (TLS) versions to maintain the confidentiality and integrity of information during reception.

**Rule ID:** `SV-241742r879813_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Protecting the confidentiality and integrity of received information requires that application servers take measures to employ approved cryptography in order to protect the information during transmission over the network. This is usually achieved through the use of Transport Layer Security (TLS), SSL VPN, or IPsec tunnel. tc Server connections are managed by the Connector object class. The Connector object can be configured to use a range of transport encryption methods. Many older transport encryption methods have been proven to be weak. vROps should be configured to use the “sslEnabledProtocols” correctly to ensure that older, less secure forms of transport security are not used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to and open /usr/lib/vmware-vcops/tomcat-enterprise/conf/server.xml. Navigate to each of the <Connector> nodes. If the value of “sslEnabledProtocols” is not set to “TLSv1.2,TLSv1.1,TLSv1” or is missing, this is a finding.

## Group: SRG-APP-000456-WSR-000187

**Group ID:** `V-241743`

### Rule: tc Server ALL must have all security-relevant software updates installed within the configured time period directed by an authoritative source.

**Rule ID:** `SV-241743r879827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. The web server will be configured to check for and install security-relevant software updates from an authoritative source within an identified time period from the availability of the update. By default, this time period will be every 24 hours. VMware delivers product updates and patches regularly. It is crucial that system administrators coordinate installation of product updates with the site ISSO to ensure that updated and patched files are uploaded onto the system as soon as prescribed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Review the policies and procedures used to ensure that all security-related upgrades are being installed within the configured time period directed by an authoritative source. If all security-related upgrades are not being installed within the configured time period directed by an authoritative source, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-241744`

### Rule: tc Server ALL must be configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs.

**Rule ID:** `SV-241744r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the web server to implement organization-wide security implementation guides and security checklists guarantees compliance with federal standards and establishes a common security baseline across the DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the web server, including the parameters required to satisfy other security control requirements. VMware delivers product updates and patches regularly. It is crucial that system administrators coordinate installation of product updates with the site ISSO to ensure that updated and patched files are uploaded onto the system as soon as prescribed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain supporting documentation from the ISSO. Verify that this Security Technical Implementation Guide (STIG) is the most current STIG available for tc Server on vROps. Assess all of the organization's vROps installations to ensure that they are fully compliant with the most current tc Server STIG. If the most current version of the tc Server STIG was not used, or if the tc Server configuration is not compliant with the most current tc Server STIG, this is a finding.

## Group: SRG-APP-000456-WSR-000187

**Group ID:** `V-258459`

### Rule: The version of vRealize Operations Manager 6.x tc Server running on the system must be a supported version.

**Rule ID:** `SV-258459r928897_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions used to install patches across the enclave and to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs). </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
vRealize Operations Manager 6.x tc Server is no longer supported by the vendor. If the system is running vRealize Operations Manager 6.x tc Server, this is a finding.

