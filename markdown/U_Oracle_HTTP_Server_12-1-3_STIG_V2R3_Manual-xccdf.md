# STIG Benchmark: Oracle HTTP Server 12.1.3 Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-221272`

### Rule: OHS must have the mpm property set to use the worker Multi-Processing Module (MPM) as the preferred means to limit the number of allowed simultaneous requests.

**Rule ID:** `SV-221272r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server management includes the ability to control the number of users and user sessions that utilize a web server. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to several types of Denial of Service attacks. Although there is some latitude concerning the settings themselves, the settings should follow DoD-recommended values, but the settings should be configurable to allow for future DoD direction. While the DoD will specify recommended values, the values can be adjusted to accommodate the operational requirement of a given system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/ohs.plugins.nodemanager.properties file with an editor. 2. Search for the "mpm" property. 3. If the "mpm" property is omitted or commented out, this is a finding. 4. If the "mpm" property is not set to "worker", this is a finding.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-221273`

### Rule: OHS must have the mpm_prefork_module directive disabled so as not conflict with the worker directive used to limit the number of allowed simultaneous requests.

**Rule ID:** `SV-221273r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server management includes the ability to control the number of users and user sessions that utilize a web server. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to several types of Denial of Service attacks. Although there is some latitude concerning the settings themselves, the settings should follow DoD-recommended values, but the settings should be configurable to allow for future DoD direction. While the DoD will specify recommended values, the values can be adjusted to accommodate the operational requirement of a given system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open the $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf file with an editor. 2. Search for the "<IfModule mpm_prefork_module>" directive at the OHS server configuration scope. 3. If this directive is found and not commented out, this is a finding.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-221274`

### Rule: OHS must have the MaxClients directive defined to limit the number of allowed simultaneous requests.

**Rule ID:** `SV-221274r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server management includes the ability to control the number of users and user sessions that utilize a web server. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to several types of Denial of Service attacks. Although there is some latitude concerning the settings themselves, the settings should follow DoD-recommended values, but the settings should be configurable to allow for future DoD direction. While the DoD will specify recommended values, the values can be adjusted to accommodate the operational requirement of a given system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open the $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf file with an editor. 2. Search for the "MaxClients" directive within "<IfModule mpm_worker_module>" directive at the OHS server configuration scope. 3. If "MaxClients" is omitted or set greater than "2000", this is a finding. Note: This vulnerability can be documented locally with the ISSM/ISSO if the site has operational reasons for the use of a higher value. If the site has this documentation, this should be marked as not a finding.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-221275`

### Rule: OHS must limit the number of threads within a worker process to limit the number of allowed simultaneous requests.

**Rule ID:** `SV-221275r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server management includes the ability to control the number of users and user sessions that utilize a web server. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to several types of Denial of Service attacks. Although there is some latitude concerning the settings themselves, the settings should follow DoD-recommended values, but the settings should be configurable to allow for future DoD direction. While the DoD will specify recommended values, the values can be adjusted to accommodate the operational requirement of a given system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open the $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf file with an editor. 2. Search for the "ThreadsPerChild" directive within "<IfModule mpm_worker_module>" directive at the OHS server configuration scope. 3. If "ThreadsPerChild" is omitted or set greater than "25", this is a finding. 4. Search for the "ThreadLimit" directive within "<IfModule mpm_worker_module>" directive at the OHS server configuration scope. 5. If "ThreadLimit" is omitted or set greater than "64", this is a finding. Note: This vulnerability can be documented locally with the ISSM/ISSO if the site has operational reasons for the use of a higher value. If the site has this documentation, this should be marked as not a finding.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-221276`

### Rule: OHS must limit the number of worker processes to limit the number of allowed simultaneous requests.

**Rule ID:** `SV-221276r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server management includes the ability to control the number of users and user sessions that utilize a web server. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to several types of Denial of Service attacks. Although there is some latitude concerning the settings themselves, the settings should follow DoD-recommended values, but the settings should be configurable to allow for future DoD direction. While the DoD will specify recommended values, the values can be adjusted to accommodate the operational requirement of a given system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open the $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf file with an editor. 2. Search for the "ServerLimit" directive within "<IfModule mpm_worker_module>" directive at the OHS server configuration scope. 3. If "ServerLimit" is omitted or set greater than the maximum of "16" and the calculation of "MaxClients"/"ThreadsPerChild", this is a finding. Note: This vulnerability can be documented locally with the ISSM/ISSO if the site has operational reasons for the use of a higher value. If the site has this documentation, this should be marked as not a finding.

## Group: SRG-APP-000014-WSR-000006

**Group ID:** `V-221277`

### Rule: OHS must have the LoadModule ossl_module directive enabled to encrypt remote connections in accordance with the categorization of data hosted by the web server.

**Rule ID:** `SV-221277r960759_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The web server has several remote communications channels. Examples are user requests via http/https, communication to a backend database, or communication to authenticate users. The encryption used to communicate must match the data that is being retrieved or presented. Methods of communication are http for publicly displayed information, https to encrypt when user data is being transmitted, VPN tunneling, or other encryption methods to a database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule ossl_module" directive at the OHS server configuration scope. 3. If the directive is omitted, this is a finding. 4. Validate that the file specified exists. If the file does not exist, this is a finding.

## Group: SRG-APP-000014-WSR-000006

**Group ID:** `V-221278`

### Rule: OHS must have the SSLFIPS directive enabled to encrypt remote connections in accordance with the categorization of data hosted by the web server.

**Rule ID:** `SV-221278r960759_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The web server has several remote communications channels. Examples are user requests via http/https, communication to a backend database, or communication to authenticate users. The encryption used to communicate must match the data that is being retrieved or presented. Methods of communication are http for publicly displayed information, https to encrypt when user data is being transmitted, VPN tunneling, or other encryption methods to a database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/ssl.conf with an editor. 2. Search for the "SSLFIPS" directive at the OHS server configuration scope. 3. If the directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000014-WSR-000006

**Group ID:** `V-221279`

### Rule: OHS must have the SSLEngine, SSLProtocol, and SSLWallet directives enabled and configured to encrypt remote connections in accordance with the categorization of data hosted by the web server.

**Rule ID:** `SV-221279r960759_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The web server has several remote communications channels. Examples are user requests via http/https, communication to a backend database, or communication to authenticate users. The encryption used to communicate must match the data that is being retrieved or presented. Methods of communication are http for publicly displayed information, https to encrypt when user data is being transmitted, VPN tunneling, or other encryption methods to a database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. Note: Does not apply to admin.conf. 2. Search for the following directive at the OHS server, virtual host, and/or directory configuration scopes: "SSLEngine" "SSLProtocol" "SSLWallet" 3. If any of these directives are omitted, this is a finding. 4. If "SSLEngine" is not set to "On", or "SSLProtocol" is not set to "TLSv1.2", this is a finding. 5. Validate that the folder specified in the "SSLWallet" directive exists. If the folder does not exist or contain a valid wallet, this is a finding.

## Group: SRG-APP-000014-WSR-000006

**Group ID:** `V-221280`

### Rule: OHS must have the SSLCipherSuite directive enabled to encrypt remote connections in accordance with the categorization of data hosted by the web server.

**Rule ID:** `SV-221280r960759_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The web server has several remote communications channels. Examples are user requests via http/https, communication to a backend database, or communication to authenticate users. The encryption used to communicate must match the data that is being retrieved or presented. Methods of communication are http for publicly displayed information, https to encrypt when user data is being transmitted, VPN tunneling, or other encryption methods to a database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. Note: Does not apply to admin.conf. 2. Search for the "SSLCipherSuite" directive at the OHS server, virtual host, and/or directory configuration scopes. 3. If the directive is omitted or set improperly, this is a finding.

## Group: SRG-APP-000015-WSR-000014

**Group ID:** `V-221281`

### Rule: OHS must have the LoadModule ossl_module directive enabled to protect the integrity of remote sessions in accordance with the categorization of data hosted by the web server.

**Rule ID:** `SV-221281r960762_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Data exchanged between the user and the web server can range from static display data to credentials used to log into the hosted application. Even when data appears to be static, the non-displayed logic in a web page may expose business logic or trusted system relationships. The integrity of all the data being exchanged between the user and web server must always be trusted. To protect the integrity and trust, encryption methods should be used to protect the complete communication session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule ossl_module" directive at the OHS server configuration scope. 3. If the directive is omitted, this is a finding. 4. Validate that the file specified exists. If the file does not exist, this is a finding.

## Group: SRG-APP-000015-WSR-000014

**Group ID:** `V-221282`

### Rule: OHS must have the SSLFIPS directive enabled to protect the integrity of remote sessions in accordance with the categorization of data hosted by the web server.

**Rule ID:** `SV-221282r960762_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Data exchanged between the user and the web server can range from static display data to credentials used to log into the hosted application. Even when data appears to be static, the non-displayed logic in a web page may expose business logic or trusted system relationships. The integrity of all the data being exchanged between the user and web server must always be trusted. To protect the integrity and trust, encryption methods should be used to protect the complete communication session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/ssl.conf with an editor. 2. Search for the "SSLFIPS" directive at the OHS server configuration scope. 3. If the directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000015-WSR-000014

**Group ID:** `V-221283`

### Rule: OHS must have the SSLEngine, SSLProtocol, and SSLWallet directives enabled and configured to protect the integrity of remote sessions in accordance with the categorization of data hosted by the web server.

**Rule ID:** `SV-221283r960762_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Data exchanged between the user and the web server can range from static display data to credentials used to log into the hosted application. Even when data appears to be static, the non-displayed logic in a web page may expose business logic or trusted system relationships. The integrity of all the data being exchanged between the user and web server must always be trusted. To protect the integrity and trust, encryption methods should be used to protect the complete communication session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. Note: Does not apply to admin.conf. 2. Search for the following directive at the OHS server, virtual host, and/or directory configuration scopes: "SSLEngine" "SSLProtocol" "SSLWallet" 3. If any of these directives are omitted, this is a finding. 4. If "SSLEngine" is not set to "On", or "SSLProtocol" is not set to "TLSv1.2", this is a finding. 5. Validate that the folder specified in the "SSLWallet" directive exists. If the folder does not exist or contain a valid wallet, this is a finding.

## Group: SRG-APP-000015-WSR-000014

**Group ID:** `V-221284`

### Rule: OHS must have the SSLCipherSuite directive enabled to protect the integrity of remote sessions in accordance with the categorization of data hosted by the web server.

**Rule ID:** `SV-221284r960762_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Data exchanged between the user and the web server can range from static display data to credentials used to log into the hosted application. Even when data appears to be static, the non-displayed logic in a web page may expose business logic or trusted system relationships. The integrity of all the data being exchanged between the user and web server must always be trusted. To protect the integrity and trust, encryption methods should be used to protect the complete communication session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. 2. Search for the "SSLCipherSuite" directive at the OHS server, virtual host, and/or directory configuration scopes. 3. If the directive is omitted or set improperly, this is a finding.

## Group: SRG-APP-000015-WSR-000014

**Group ID:** `V-221285`

### Rule: OHS must have the SecureProxy directive enabled to protect the integrity of remote sessions when integrated with WebLogic in accordance with the categorization of data hosted by the web server.

**Rule ID:** `SV-221285r960762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data exchanged between the user and the web server can range from static display data to credentials used to log into the hosted application. Even when data appears to be static, the non-displayed logic in a web page may expose business logic or trusted system relationships. The integrity of all the data being exchanged between the user and web server must always be trusted. To protect the integrity and trust, encryption methods should be used to protect the complete communication session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using the WebLogic Web Server Proxy Plugin and configuring end-to-end SSL: 1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that contains an SSL-enabled "<VirtualHost>" directive. 2. Search for the "SecureProxy" directive within an "<IfModule weblogic_module>" at the virtual host configuration scope. 3. If the directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000015-WSR-000014

**Group ID:** `V-221286`

### Rule: OHS must have the WLSSLWallet directive enabled to protect the integrity of remote sessions when integrated with WebLogic in accordance with the categorization of data hosted by the web server.

**Rule ID:** `SV-221286r960762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data exchanged between the user and the web server can range from static display data to credentials used to log into the hosted application. Even when data appears to be static, the non-displayed logic in a web page may expose business logic or trusted system relationships. The integrity of all the data being exchanged between the user and web server must always be trusted. To protect the integrity and trust, encryption methods should be used to protect the complete communication session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using the WebLogic Web Server Proxy Plugin and configuring end-to-end SSL: 1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that contains an SSL-enabled "<VirtualHost>" directive. 2. Search for the "WLSSLWallet" directive within an "<IfModule weblogic_module>" at the virtual host configuration scope. 3. If the directive is omitted or is not set to a folder containing a valid wallet, this is a finding.

## Group: SRG-APP-000015-WSR-000014

**Group ID:** `V-221287`

### Rule: OHS must have the WebLogicSSLVersion directive enabled to protect the integrity of remote sessions when integrated with WebLogic in accordance with the categorization of data hosted by the web server.

**Rule ID:** `SV-221287r960762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data exchanged between the user and the web server can range from static display data to credentials used to log into the hosted application. Even when data appears to be static, the non-displayed logic in a web page may expose business logic or trusted system relationships. The integrity of all the data being exchanged between the user and web server must always be trusted. To protect the integrity and trust, encryption methods should be used to protect the complete communication session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using the WebLogic Web Server Proxy Plugin and configuring end-to-end SSL: 1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that contains an SSL-enabled "<VirtualHost>" directive. 2. Search for the "WebLogicSSLVersion" directive within an "<IfModule weblogic_module>" at the virtual host configuration scope. 3. If the directive is omitted or is not set to "TLSv1.2", this is a finding.

## Group: SRG-APP-000015-WSR-000014

**Group ID:** `V-221288`

### Rule: OHS must have the WLProxySSL directive enabled to protect the integrity of remote sessions when integrated with WebLogic in accordance with the categorization of data hosted by the web server.

**Rule ID:** `SV-221288r960762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data exchanged between the user and the web server can range from static display data to credentials used to log into the hosted application. Even when data appears to be static, the non-displayed logic in a web page may expose business logic or trusted system relationships. The integrity of all the data being exchanged between the user and web server must always be trusted. To protect the integrity and trust, encryption methods should be used to protect the complete communication session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using the WebLogic Web Server Proxy Plugin and configuring SSL termination at OHS: 1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that contains an SSL-enabled "<VirtualHost>" directive. 2. Search for the "WLProxySSL" directive within an "<IfModule weblogic_module>" at the virtual host configuration scope. 3. If the directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000016-WSR-000005

**Group ID:** `V-221289`

### Rule: OHS must have the LoadModule log_config_module directive enabled to generate information to be used by external applications or entities to monitor and control remote access.

**Rule ID:** `SV-221289r960765_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. By providing remote access information to an external monitoring system, the organization can monitor for cyber attacks and monitor compliance with remote access policies. The organization can also look at data organization wide and determine an attack or anomaly is occurring on the organization which might not be noticed if the data were kept local to the web server. Examples of external applications used to monitor or control access would be audit log monitoring systems, dynamic firewalls, or infrastructure monitoring systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule log_config_module" directive at the OHS server configuration scope. 3. If the directive is omitted, this is a finding. 4. Validate that the file specified exists. If the file does not exist, this is a finding.

## Group: SRG-APP-000016-WSR-000005

**Group ID:** `V-221290`

### Rule: OHS must have the OraLogMode set to Oracle Diagnostic Logging text mode to generate information to be used by external applications or entities to monitor and control remote access.

**Rule ID:** `SV-221290r960765_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. By providing remote access information to an external monitoring system, the organization can monitor for cyber attacks and monitor compliance with remote access policies. The organization can also look at data organization wide and determine an attack or anomaly is occurring on the organization which might not be noticed if the data were kept local to the web server. Examples of external applications used to monitor or control access would be audit log monitoring systems, dynamic firewalls, or infrastructure monitoring systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "OraLogMode" directive at the OHS server configuration scope. 3. If the directive is omitted or is not set to "odl-text", this is a finding.

## Group: SRG-APP-000016-WSR-000005

**Group ID:** `V-221291`

### Rule: OHS must have a log directory location defined to generate information for use by external applications or entities to monitor and control remote access.

**Rule ID:** `SV-221291r960765_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. By providing remote access information to an external monitoring system, the organization can monitor for cyber attacks and monitor compliance with remote access policies. The organization can also look at data organization wide and determine an attack or anomaly is occurring on the organization which might not be noticed if the data were kept local to the web server. Examples of external applications used to monitor or control access would be audit log monitoring systems, dynamic firewalls, or infrastructure monitoring systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "OraLogDir" directive at the OHS server configuration scope. 3. If the directive is omitted, this is a finding. 4. Validate that the folder specified exists. If the folder does not exist, this is a finding.

## Group: SRG-APP-000016-WSR-000005

**Group ID:** `V-221292`

### Rule: OHS must have the OraLogSeverity directive defined to generate adequate information to be used by external applications or entities to monitor and control remote access.

**Rule ID:** `SV-221292r960765_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. By providing remote access information to an external monitoring system, the organization can monitor for cyber attacks and monitor compliance with remote access policies. The organization can also look at data organization wide and determine an attack or anomaly is occurring on the organization which might not be noticed if the data were kept local to the web server. Examples of external applications used to monitor or control access would be audit log monitoring systems, dynamic firewalls, or infrastructure monitoring systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "OraLogSeverity" directive at the OHS server configuration scope. 3. If the directive is omitted or is not set to "NOTIFICATION:32", this is a finding.

## Group: SRG-APP-000016-WSR-000005

**Group ID:** `V-221293`

### Rule: OHS must have the log rotation parameter set to allow generated information to be used by external applications or entities to monitor and control remote access.

**Rule ID:** `SV-221293r960765_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. By providing remote access information to an external monitoring system, the organization can monitor for cyber attacks and monitor compliance with remote access policies. The organization can also look at data organization wide and determine an attack or anomaly is occurring on the organization which might not be noticed if the data were kept local to the web server. Examples of external applications used to monitor or control access would be audit log monitoring systems, dynamic firewalls, or infrastructure monitoring systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "OraLogRotationParams" directive at the OHS server configuration scope. 3. If the directive is omitted or set improperly, this is a finding.

## Group: SRG-APP-000016-WSR-000005

**Group ID:** `V-221294`

### Rule: OHS must have a log format defined to generate adequate information to be used by external applications or entities to monitor and control remote access.

**Rule ID:** `SV-221294r960765_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. By providing remote access information to an external monitoring system, the organization can monitor for cyber attacks and monitor compliance with remote access policies. The organization can also look at data organization wide and determine an attack or anomaly is occurring on the organization which might not be noticed if the data were kept local to the web server. Examples of external applications used to monitor or control access would be audit log monitoring systems, dynamic firewalls, or infrastructure monitoring systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "LogFormat" directive with a nickname of "dod" at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000016-WSR-000005

**Group ID:** `V-221295`

### Rule: OHS must have a SSL log format defined to allow generated information to be used by external applications or entities to monitor and control remote access in accordance with the categorization of data hosted by the web server.

**Rule ID:** `SV-221295r960765_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. By providing remote access information to an external monitoring system, the organization can monitor for cyber attacks and monitor compliance with remote access policies. The organization can also look at data organization wide and determine an attack or anomaly is occurring on the organization which might not be noticed if the data were kept local to the web server. Examples of external applications used to monitor or control access would be audit log monitoring systems, dynamic firewalls, or infrastructure monitoring systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "LogFormat" directive with a nickname of "dod_ssl" at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000016-WSR-000005

**Group ID:** `V-221296`

### Rule: OHS must have a log file defined for each site/virtual host to capture information to be used by external applications or entities to monitor and control remote access.

**Rule ID:** `SV-221296r960765_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. By providing remote access information to an external monitoring system, the organization can monitor for cyber attacks and monitor compliance with remote access policies. The organization can also look at data organization wide and determine an attack or anomaly is occurring on the organization which might not be noticed if the data were kept local to the web server. Examples of external applications used to monitor or control access would be audit log monitoring systems, dynamic firewalls, or infrastructure monitoring systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "CustomLog" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope. 4. Validate that the folder specified exists. If the folder does not exist, this is a finding.

## Group: SRG-APP-000315-WSR-000003

**Group ID:** `V-221297`

### Rule: Remote access to OHS must follow access policy or work in conjunction with enterprise tools designed to enforce policy requirements.

**Rule ID:** `SV-221297r961278_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. A web server can be accessed remotely and must be able to enforce remote access policy requirements or work in conjunction with enterprise tools designed to enforce policy requirements. Examples of the web server enforcing a remote access policy are implementing IP filtering rules, using https instead of http for communication, implementing secure tokens, and validating users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Review the directives (e.g., "<VirtualHost>", "<Directory>", and "<Location>") at the OHS server and virtual host configuration scopes. 3. If these directives do not contain the appropriate access protection via secure authentication, SSL-associated directives, or "Order", "Deny", and "Allow" directives to secure access or prohibit access from nonsecure zones, this is a finding.

## Group: SRG-APP-000315-WSR-000004

**Group ID:** `V-221298`

### Rule: OHS must have the Order, Allow, and Deny directives set within the Directory directives set to restrict inbound connections from nonsecure zones.

**Rule ID:** `SV-221298r961278_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. A web server can be accessed remotely and must be capable of restricting access from what the DoD defines as nonsecure zones. Nonsecure zones are defined as any IP, subnet, or region that is defined as a threat to the organization. The nonsecure zones must be defined for public web servers logically located in a DMZ, as well as private web servers with perimeter protection devices. By restricting access from nonsecure zones, through internal web server access list, the web server can stop or slow denial of service (DoS) attacks on the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "<Directory>" directive at the OHS server and virtual host configuration scopes. Note: This check does not apply to the root directory, i.e. the <Directory /> directive. 3. If the "<Directory>" directive does not contain the appropriate "Order", "Deny", and "Allow" directives to prohibit access from nonsecure zones, this is a finding.

## Group: SRG-APP-000315-WSR-000004

**Group ID:** `V-221299`

### Rule: OHS must have the Order, Allow, and Deny directives set within the Files directives set to restrict inbound connections from nonsecure zones.

**Rule ID:** `SV-221299r961278_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. A web server can be accessed remotely and must be capable of restricting access from what the DoD defines as nonsecure zones. Nonsecure zones are defined as any IP, subnet, or region that is defined as a threat to the organization. The nonsecure zones must be defined for public web servers logically located in a DMZ, as well as private web servers with perimeter protection devices. By restricting access from nonsecure zones, through internal web server access list, the web server can stop or slow denial of service (DoS) attacks on the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "<Files>" directive at the OHS server, virtual host, and directory configuration scopes. 3. If the "<Files>" directive does not contain the appropriate "Order", "Deny", and "Allow" directives to prohibit access from nonsecure zones, this is a finding.

## Group: SRG-APP-000315-WSR-000004

**Group ID:** `V-221300`

### Rule: OHS must have the Order, Allow, and Deny directives set within the Location directives set to restrict inbound connections from nonsecure zones.

**Rule ID:** `SV-221300r961278_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. A web server can be accessed remotely and must be capable of restricting access from what the DoD defines as nonsecure zones. Nonsecure zones are defined as any IP, subnet, or region that is defined as a threat to the organization. The nonsecure zones must be defined for public web servers logically located in a DMZ, as well as private web servers with perimeter protection devices. By restricting access from nonsecure zones, through internal web server access list, the web server can stop or slow denial of service (DoS) attacks on the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "<Location>" directive at the OHS server and virtual host configuration scopes. 3. If the "<Location>" directive does not contain the appropriate "Order", "Deny", and "Allow" directives to prohibit access from nonsecure zones, this is a finding.

## Group: SRG-APP-000316-WSR-000170

**Group ID:** `V-221301`

### Rule: OHS must provide the capability to immediately disconnect or disable remote access to the hosted applications.

**Rule ID:** `SV-221301r961281_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>During an attack on the web server or any of the hosted applications, the system administrator may need to disconnect or disable access by users to stop the attack. The web server must provide a capability to disconnect users to a hosted application without compromising other hosted applications unless deemed necessary to stop the attack. Methods to disconnect or disable connections are to stop the application service for a specified hosted application, stop the web server, or block all connections through web server access list. The web server capabilities used to disconnect or disable users from connecting to hosted applications and the web server must be documented to make certain that, during an attack, the proper action is taken to conserve connectivity to any other hosted application if possible and to make certain log data is conserved for later forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "<Directory>", "<Files>", or "<Location>" directive serving the application/content under attack at the OHS server, virtual host, or directory configuration scope. 3. If the "<Directory>", "<Files>", or "<Location>" directive serving the application/content under attack does not contain the appropriate "Order", "Deny", and "Allow" directives to prohibit access, this is a finding.

## Group: SRG-APP-000340-WSR-000029

**Group ID:** `V-221302`

### Rule: Non-privileged accounts on the hosting system must only access OHS security-relevant information and functions through a distinct administrative account.

**Rule ID:** `SV-221302r961353_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By separating web server security functions from non-privileged users, roles can be developed that can then be used to administer the web server. Forcing users to change from a non-privileged account to a privileged account when operating on the web server or on security-relevant information forces users to only operate as a web server administrator when necessary. Operating in this manner allows for better logging of changes and better forensic information and limits accidental changes to the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Check that sudo is properly configured for the account owning the OHS software. 2. If accounts other than the account that owns the OHS software can access the OHS software, this is a finding.

## Group: SRG-APP-000089-WSR-000047

**Group ID:** `V-221303`

### Rule: OHS must have the client requests logging module loaded to generate log records for system startup and shutdown, system access, and system authentication logging.

**Rule ID:** `SV-221303r960879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log records can be generated from various components within the web server (e.g., httpd, plug-ins to external backends, etc.). From a web server perspective, certain specific web server functionalities may be logged as well. The web server must allow the definition of what events are to be logged. As conditions change, the number and types of events to be logged may change, and the web server must be able to facilitate these changes. The minimum list of logged events should be those pertaining to system startup and shutdown, system access, and system authentication events. If these events are not logged at a minimum, any type of forensic investigation would be missing pertinent information needed to replay what occurred.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule log_config_module" directive at the OHS server configuration scope. 3. If the directive is omitted, this is a finding. 4. Validate that the file specified exist. If the file does not exist, this is a finding.

## Group: SRG-APP-000089-WSR-000047

**Group ID:** `V-221304`

### Rule: OHS must have OraLogMode set to Oracle Diagnostic Logging text mode to generate log records for system startup and shutdown, system access, and system authentication logging.

**Rule ID:** `SV-221304r960879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log records can be generated from various components within the web server (e.g., httpd, plug-ins to external backends, etc.). From a web server perspective, certain specific web server functionalities may be logged as well. The web server must allow the definition of what events are to be logged. As conditions change, the number and types of events to be logged may change, and the web server must be able to facilitate these changes. The minimum list of logged events should be those pertaining to system startup and shutdown, system access, and system authentication events. If these events are not logged at a minimum, any type of forensic investigation would be missing pertinent information needed to replay what occurred.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "OraLogMode" directive at the OHS server configuration scope. 3. If the directive is omitted or is not set to "odl-text", this is a finding.

## Group: SRG-APP-000089-WSR-000047

**Group ID:** `V-221305`

### Rule: OHS must have a log directory location defined to generate log records for system startup and shutdown, system access, and system authentication logging.

**Rule ID:** `SV-221305r960879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log records can be generated from various components within the web server (e.g., httpd, plug-ins to external backends, etc.). From a web server perspective, certain specific web server functionalities may be logged as well. The web server must allow the definition of what events are to be logged. As conditions change, the number and types of events to be logged may change, and the web server must be able to facilitate these changes. The minimum list of logged events should be those pertaining to system startup and shutdown, system access, and system authentication events. If these events are not logged at a minimum, any type of forensic investigation would be missing pertinent information needed to replay what occurred.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "OraLogDir" directive at the OHS server configuration scope. 3. If the directive is omitted, this is a finding. 4. Validate that the folder specified exists. If the folder does not exist, this is a finding.

## Group: SRG-APP-000089-WSR-000047

**Group ID:** `V-221306`

### Rule: OHS must have a log level severity defined to generate adequate log records for system startup and shutdown, system access, and system authentication events.

**Rule ID:** `SV-221306r960879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log records can be generated from various components within the web server (e.g., httpd, plug-ins to external backends, etc.). From a web server perspective, certain specific web server functionalities may be logged as well. The web server must allow the definition of what events are to be logged. As conditions change, the number and types of events to be logged may change, and the web server must be able to facilitate these changes. The minimum list of logged events should be those pertaining to system startup and shutdown, system access, and system authentication events. If these events are not logged at a minimum, any type of forensic investigation would be missing pertinent information needed to replay what occurred.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "OraLogSeverity" directive at the OHS server configuration scope. 3. If the directive is omitted or is not set to "NOTIFICATION:32", this is a finding.

## Group: SRG-APP-000089-WSR-000047

**Group ID:** `V-221307`

### Rule: OHS must have the log rotation parameter set to allow for the generation log records for system startup and shutdown, system access, and system authentication events.

**Rule ID:** `SV-221307r960879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log records can be generated from various components within the web server (e.g., httpd, plug-ins to external backends, etc.). From a web server perspective, certain specific web server functionalities may be logged as well. The web server must allow the definition of what events are to be logged. As conditions change, the number and types of events to be logged may change, and the web server must be able to facilitate these changes. The minimum list of logged events should be those pertaining to system startup and shutdown, system access, and system authentication events. If these events are not logged at a minimum, any type of forensic investigation would be missing pertinent information needed to replay what occurred.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "OraLogRotationParams" directive at the OHS server configuration scope. 3. If the directive is omitted or set improperly, this is a finding.

## Group: SRG-APP-000089-WSR-000047

**Group ID:** `V-221308`

### Rule: OHS must have a log format defined to generate adequate logs by system startup and shutdown, system access, and system authentication events.

**Rule ID:** `SV-221308r960879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log records can be generated from various components within the web server (e.g., httpd, plug-ins to external backends, etc.). From a web server perspective, certain specific web server functionalities may be logged as well. The web server must allow the definition of what events are to be logged. As conditions change, the number and types of events to be logged may change, and the web server must be able to facilitate these changes. The minimum list of logged events should be those pertaining to system startup and shutdown, system access, and system authentication events. If these events are not logged at a minimum, any type of forensic investigation would be missing pertinent information needed to replay what occurred.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "LogFormat" directive with a nickname of "dod" at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000089-WSR-000047

**Group ID:** `V-221309`

### Rule: OHS must have a SSL log format defined to generate adequate logs by system startup and shutdown, system access, and system authentication events.

**Rule ID:** `SV-221309r960879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log records can be generated from various components within the web server (e.g., httpd, plug-ins to external backends, etc.). From a web server perspective, certain specific web server functionalities may be logged as well. The web server must allow the definition of what events are to be logged. As conditions change, the number and types of events to be logged may change, and the web server must be able to facilitate these changes. The minimum list of logged events should be those pertaining to system startup and shutdown, system access, and system authentication events. If these events are not logged at a minimum, any type of forensic investigation would be missing pertinent information needed to replay what occurred.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "LogFormat" directive with a nickname of "dod_ssl" at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000089-WSR-000047

**Group ID:** `V-221310`

### Rule: OHS must have a log file defined for each site/virtual host to capture logs generated by system startup and shutdown, system access, and system authentication events.

**Rule ID:** `SV-221310r960879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log records can be generated from various components within the web server (e.g., httpd, plug-ins to external backends, etc.). From a web server perspective, certain specific web server functionalities may be logged as well. The web server must allow the definition of what events are to be logged. As conditions change, the number and types of events to be logged may change, and the web server must be able to facilitate these changes. The minimum list of logged events should be those pertaining to system startup and shutdown, system access, and system authentication events. If these events are not logged at a minimum, any type of forensic investigation would be missing pertinent information needed to replay what occurred.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "CustomLog" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope. 4. Validate that the folder specified exists. If the folder does not exist, this is a finding.

## Group: SRG-APP-000095-WSR-000056

**Group ID:** `V-221312`

### Rule: OHS must have a log level severity defined to produce sufficient log records to establish what type of events occurred.

**Rule ID:** `SV-221312r962395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct type of event that occurred is important during forensic analysis. The correct determination of the event and when it occurred is important in relation to other events that happened at that same time. Without sufficient information establishing what type of log event occurred, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "OraLogSeverity" directive at the OHS server configuration scope. 3. If the directive is omitted or is not set to "NOTIFICATION:32", this is a finding.

## Group: SRG-APP-000095-WSR-000056

**Group ID:** `V-221313`

### Rule: OHS must have a log format defined for log records generated to capture sufficient information to establish what type of events occurred.

**Rule ID:** `SV-221313r962395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct type of event that occurred is important during forensic analysis. The correct determination of the event and when it occurred is important in relation to other events that happened at that same time. Without sufficient information establishing what type of log event occurred, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "LogFormat" directive with a nickname of "dod" at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000095-WSR-000056

**Group ID:** `V-221314`

### Rule: OHS must have a SSL log format defined for log records generated to capture sufficient information to establish what type of events occurred.

**Rule ID:** `SV-221314r962395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct type of event that occurred is important during forensic analysis. The correct determination of the event and when it occurred is important in relation to other events that happened at that same time. Without sufficient information establishing what type of log event occurred, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "LogFormat" directive with a nickname of "dod_ssl" at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000095-WSR-000056

**Group ID:** `V-221315`

### Rule: OHS must have a log file defined for each site/virtual host to capture sufficient information to establish what type of events occurred.

**Rule ID:** `SV-221315r962395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct type of event that occurred is important during forensic analysis. The correct determination of the event and when it occurred is important in relation to other events that happened at that same time. Without sufficient information establishing what type of log event occurred, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "CustomLog" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope. 4. Validate that the folder specified exists. If the folder does not exist, this is a finding.

## Group: SRG-APP-000096-WSR-000057

**Group ID:** `V-221316`

### Rule: OHS must have a log format defined for log records generated to capture sufficient information to establish when an event occurred.

**Rule ID:** `SV-221316r960894_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct order of the events that occurred is important during forensic analysis. Events that appear harmless by themselves might be flagged as a potential threat when properly viewed in sequence. By also establishing the event date and time, an event can be properly viewed with an enterprise tool to fully see a possible threat in its entirety. Without sufficient information establishing when the log event occurred, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "LogFormat" directive with a nickname of "dod" at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000096-WSR-000057

**Group ID:** `V-221317`

### Rule: OHS must have a SSL log format defined for log records generated to capture sufficient information to establish when an event occurred.

**Rule ID:** `SV-221317r960894_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct order of the events that occurred is important during forensic analysis. Events that appear harmless by themselves might be flagged as a potential threat when properly viewed in sequence. By also establishing the event date and time, an event can be properly viewed with an enterprise tool to fully see a possible threat in its entirety. Without sufficient information establishing when the log event occurred, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "LogFormat" directive with a nickname of "dod_ssl" at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000096-WSR-000057

**Group ID:** `V-221318`

### Rule: OHS must have a log file defined for each site/virtual host to capture logs generated that allow the establishment of when an event occurred.

**Rule ID:** `SV-221318r960894_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct order of the events that occurred is important during forensic analysis. Events that appear harmless by themselves might be flagged as a potential threat when properly viewed in sequence. By also establishing the event date and time, an event can be properly viewed with an enterprise tool to fully see a possible threat in its entirety. Without sufficient information establishing when the log event occurred, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "CustomLog" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope. 4. Validate that the folder specified exists. If the folder does not exist, this is a finding.

## Group: SRG-APP-000097-WSR-000058

**Group ID:** `V-221319`

### Rule: OHS must have a log format defined for log records that allow the establishment of where within OHS the events occurred.

**Rule ID:** `SV-221319r1022706_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct location or process within the web server where the events occurred is important during forensic analysis. Correctly determining the web service, plug-in, or module will add information to the overall reconstruction of the logged event. For example, an event that occurred during communication to a cgi module might be handled differently than an event that occurred during a communication session to a user. Without sufficient information establishing where the log event occurred within the web server, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "LogFormat" directive with a nickname of "dod" at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000097-WSR-000058

**Group ID:** `V-221320`

### Rule: OHS must have a SSL log format defined for log records that allow the establishment of where within OHS the events occurred.

**Rule ID:** `SV-221320r1022706_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct location or process within the web server where the events occurred is important during forensic analysis. Correctly determining the web service, plug-in, or module will add information to the overall reconstruction of the logged event. For example, an event that occurred during communication to a cgi module might be handled differently than an event that occurred during a communication session to a user. Without sufficient information establishing where the log event occurred within the web server, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "LogFormat" directive with a nickname of "dod_ssl" at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000097-WSR-000058

**Group ID:** `V-221321`

### Rule: OHS must have a log file defined for each site/virtual host to capture logs generated that allow the establishment of where within OHS the events occurred.

**Rule ID:** `SV-221321r1022706_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct location or process within the web server where the events occurred is important during forensic analysis. Correctly determining the web service, plug-in, or module will add information to the overall reconstruction of the logged event. For example, an event that occurred during communication to a cgi module might be handled differently than an event that occurred during a communication session to a user. Without sufficient information establishing where the log event occurred within the web server, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "CustomLog" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope. 4. Validate that the folder specified exists. If the folder does not exist, this is a finding.

## Group: SRG-APP-000098-WSR-000059

**Group ID:** `V-221322`

### Rule: OHS must have a log format defined for log records that allow the establishment of the source of events.

**Rule ID:** `SV-221322r960900_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct source, e.g., source IP, of the events is important during forensic analysis. Correctly determining the source will add information to the overall reconstruction of the logable event. By determining the source of the event correctly, analysis of the enterprise can be undertaken to determine if the event compromised other assets within the enterprise. Without sufficient information establishing the source of the logged event, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "LogFormat" directive with a nickname of "dod" at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000098-WSR-000059

**Group ID:** `V-221323`

### Rule: OHS must have a SSL log format defined for log records that allow the establishment of the source of events.

**Rule ID:** `SV-221323r960900_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct source, e.g., source IP, of the events is important during forensic analysis. Correctly determining the source will add information to the overall reconstruction of the logable event. By determining the source of the event correctly, analysis of the enterprise can be undertaken to determine if the event compromised other assets within the enterprise. Without sufficient information establishing the source of the logged event, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "LogFormat" directive with a nickname of "dod_ssl" at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000098-WSR-000059

**Group ID:** `V-221324`

### Rule: OHS must have a log file defined for each site/virtual host to capture logs generated that allow the establishment of the source of events.

**Rule ID:** `SV-221324r960900_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct source, e.g., source IP, of the events is important during forensic analysis. Correctly determining the source will add information to the overall reconstruction of the logable event. By determining the source of the event correctly, analysis of the enterprise can be undertaken to determine if the event compromised other assets within the enterprise. Without sufficient information establishing the source of the logged event, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "CustomLog" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope. 4. Validate that the folder specified exists. If the folder does not exist, this is a finding.

## Group: SRG-APP-000098-WSR-000060

**Group ID:** `V-221325`

### Rule: OHS, behind a load balancer or proxy server, must produce log records containing the client IP information as the source and destination and not the load balancer or proxy IP information with each event.

**Rule ID:** `SV-221325r960900_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct source, e.g., source IP, of the events is important during forensic analysis. Correctly determining the source of events will add information to the overall reconstruction of the logable event. By determining the source of the event correctly, analysis of the enterprise can be undertaken to determine if events tied to the source occurred in other areas within the enterprise. A web server behind a load balancer or proxy server, when not configured correctly, will record the load balancer or proxy server as the source of every logable event. When looking at the information forensically, this information is not helpful in the investigation of events. The web server must record with each event the client source of the event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "LogFormat" directive with a nickname of "dod" at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000098-WSR-000060

**Group ID:** `V-221326`

### Rule: OHS, behind a load balancer or proxy server, must have the SSL log format set correctly to produce log records containing the client IP information as the source and destination and not the load balancer or proxy IP information with each event.

**Rule ID:** `SV-221326r960900_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct source, e.g., source IP, of the events is important during forensic analysis. Correctly determining the source of events will add information to the overall reconstruction of the logable event. By determining the source of the event correctly, analysis of the enterprise can be undertaken to determine if events tied to the source occurred in other areas within the enterprise. A web server behind a load balancer or proxy server, when not configured correctly, will record the load balancer or proxy server as the source of every logable event. When looking at the information forensically, this information is not helpful in the investigation of events. The web server must record with each event the client source of the event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "LogFormat" directive with a nickname of "dod_ssl" at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000098-WSR-000060

**Group ID:** `V-221327`

### Rule: OHS, behind a load balancer or proxy server, must have a log file defined for each site/virtual host to produce log records containing the client IP information as the source and destination and not the load balancer or proxy IP information with each event.

**Rule ID:** `SV-221327r960900_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct source, e.g., source IP, of the events is important during forensic analysis. Correctly determining the source of events will add information to the overall reconstruction of the logable event. By determining the source of the event correctly, analysis of the enterprise can be undertaken to determine if events tied to the source occurred in other areas within the enterprise. A web server behind a load balancer or proxy server, when not configured correctly, will record the load balancer or proxy server as the source of every logable event. When looking at the information forensically, this information is not helpful in the investigation of events. The web server must record with each event the client source of the event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "CustomLog" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope. 4. Validate that the folder specified exists. If the folder does not exist, this is a finding.

## Group: SRG-APP-000099-WSR-000061

**Group ID:** `V-221328`

### Rule: OHS must have a log format defined to produce log records that contain sufficient information to establish the outcome (success or failure) of events.

**Rule ID:** `SV-221328r960903_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the success or failure of an event is important during forensic analysis. Correctly determining the outcome will add information to the overall reconstruction of the logable event. By determining the success or failure of the event correctly, analysis of the enterprise can be undertaken to determine if events tied to the event occurred in other areas within the enterprise. Without sufficient information establishing the success or failure of the logged event, investigation into the cause of event is severely hindered. The success or failure also provides a means to measure the impact of an event and help authorized personnel to determine the appropriate response. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "LogFormat" directive with a nickname of "dod" at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000099-WSR-000061

**Group ID:** `V-221329`

### Rule: OHS must have a SSL log format defined to produce log records that contain sufficient information to establish the outcome (success or failure) of events.

**Rule ID:** `SV-221329r960903_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the success or failure of an event is important during forensic analysis. Correctly determining the outcome will add information to the overall reconstruction of the logable event. By determining the success or failure of the event correctly, analysis of the enterprise can be undertaken to determine if events tied to the event occurred in other areas within the enterprise. Without sufficient information establishing the success or failure of the logged event, investigation into the cause of event is severely hindered. The success or failure also provides a means to measure the impact of an event and help authorized personnel to determine the appropriate response. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "LogFormat" directive with a nickname of "dod_ssl" at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000099-WSR-000061

**Group ID:** `V-221330`

### Rule: OHS must have a log file defined for each site/virtual host to produce log records that contain sufficient information to establish the outcome (success or failure) of events.

**Rule ID:** `SV-221330r960903_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the success or failure of an event is important during forensic analysis. Correctly determining the outcome will add information to the overall reconstruction of the logable event. By determining the success or failure of the event correctly, analysis of the enterprise can be undertaken to determine if events tied to the event occurred in other areas within the enterprise. Without sufficient information establishing the success or failure of the logged event, investigation into the cause of event is severely hindered. The success or failure also provides a means to measure the impact of an event and help authorized personnel to determine the appropriate response. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, file names involved, access control, or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "CustomLog" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope. 4. Validate that the folder specified exists. If the folder does not exist, this is a finding.

## Group: SRG-APP-000100-WSR-000064

**Group ID:** `V-221331`

### Rule: OHS must have a log format defined to produce log records containing sufficient information to establish the identity of any user/subject or process associated with an event.

**Rule ID:** `SV-221331r960906_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Determining user accounts, processes running on behalf of the user, and running process identifiers also enable a better understanding of the overall event. User tool identification is also helpful to determine if events are related to overall user access or specific client tools. Log record content that may be necessary to satisfy the requirement of this control includes: time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "LogFormat" directive with a nickname of "dod" at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000100-WSR-000064

**Group ID:** `V-221332`

### Rule: OHS must have a SSL log format defined to produce log records containing sufficient information to establish the identity of any user/subject or process associated with an event.

**Rule ID:** `SV-221332r960906_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Determining user accounts, processes running on behalf of the user, and running process identifiers also enable a better understanding of the overall event. User tool identification is also helpful to determine if events are related to overall user access or specific client tools. Log record content that may be necessary to satisfy the requirement of this control includes: time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "LogFormat" directive with a nickname of "dod_ssl" at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000100-WSR-000064

**Group ID:** `V-221333`

### Rule: OHS must have a log file defined for each site/virtual host to produce log records containing sufficient information to establish the identity of any user/subject or process associated with an event.

**Rule ID:** `SV-221333r960906_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Determining user accounts, processes running on behalf of the user, and running process identifiers also enable a better understanding of the overall event. User tool identification is also helpful to determine if events are related to overall user access or specific client tools. Log record content that may be necessary to satisfy the requirement of this control includes: time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "CustomLog" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope. 4. Validate that the folder specified exists. If the folder does not exist, this is a finding.

## Group: SRG-APP-000118-WSR-000068

**Group ID:** `V-221334`

### Rule: OHS log files must only be accessible by privileged users.

**Rule ID:** `SV-221334r960930_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to their advantage since each event record might contain communication ports, protocols, services, trust relationships, user names, etc. The web server must protect the log data from unauthorized read, write, copy, etc. This can be done by the web server if the web server is also doing the logging function. The web server may also use an external log system. In either case, the logs must be protected from access by non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Change to the ORACLE_HOME/user_projects/domains/base_domain/servers directory. 2. Execute the command: find . -name *.log 3. Verify that each log file that was returned has the owner and group set to the user and group used to run the web server. The user and group are typically set to Oracle. 4. Verify that each log file that was returned has the permissions on the log file set to "640" or more restrictive. If the owner, group or permissions are set incorrectly on any of the log files, this is a finding.

## Group: SRG-APP-000119-WSR-000069

**Group ID:** `V-221335`

### Rule: The log information from OHS must be protected from unauthorized modification.

**Rule ID:** `SV-221335r960933_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. The accuracy of the information is always pertinent. Information that is not accurate does not help in the revealing of potential security risks and may hinder the early discovery of a system compromise. One of the first steps an attacker will undertake is the modification or deletion of log records to cover his tracks and prolong discovery. The web server must protect the log data from unauthorized modification. This can be done by the web server if the web server is also doing the logging function. The web server may also use an external log system. In either case, the logs must be protected from modification by non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Change to the ORACLE_HOME/user_projects/domains/base_domain/servers directory. 2. Execute the command: find . -name *.log 3. Verify that each log file that was returned has the owner and group set to the user and group used to run the web server. The user and group are typically set to Oracle. 4. Verify that each log file that was returned has the permissions on the log file set to "640" or more restrictive. If the owner, group or permissions are set incorrectly on any of the log files, this is a finding.

## Group: SRG-APP-000120-WSR-000070

**Group ID:** `V-221336`

### Rule: The log information from OHS must be protected from unauthorized deletion.

**Rule ID:** `SV-221336r960936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log data is essential in the investigation of events. The accuracy of the information is always pertinent. Information that is not accurate does not help in the revealing of potential security risks and may hinder the early discovery of a system compromise. One of the first steps an attacker will undertake is the modification or deletion of audit records to cover his tracks and prolong discovery. The web server must protect the log data from unauthorized deletion. This can be done by the web server if the web server is also doing the logging function. The web server may also use an external log system. In either case, the logs must be protected from deletion by non-privileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Change to the ORACLE_HOME/user_projects/domains/base_domain/servers directory. 2. Execute the command: find . -name *.log 3. Verify that each log file that was returned has the owner and group set to the user and group used to run the web server. The user and group are typically set to Oracle. 4. Verify that each log file that was returned has the permissions on the log file set to "640" or more restrictive. If the owner, group or permissions are set incorrectly on any of the log files, this is a finding.

## Group: SRG-APP-000125-WSR-000071

**Group ID:** `V-221337`

### Rule: The log data and records from OHS must be backed up onto a different system or media.

**Rule ID:** `SV-221337r960948_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of log data includes assuring log data is not accidentally lost or deleted. Backing up log records to an unrelated system or onto separate media than the system the web server is actually running on helps to assure that, in the event of a catastrophic system failure, the log records will be retained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Verify that the System Administrator backs up the files located in the $DOMAIN_HOME/servers/<componentName>/logs directory. 2. If the files located in the $DOMAIN_HOME/servers/<componentName>/logs directory, this is a finding.

## Group: SRG-APP-000358-WSR-000163

**Group ID:** `V-221338`

### Rule: OHS must be configured to store error log files to an appropriate storage device from which other tools can be configured to reference those log files for diagnostic/forensic purposes.

**Rule ID:** `SV-221338r961395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server will typically utilize logging mechanisms for maintaining a historical log of activity that occurs within a hosted application. This information can then be used for diagnostic purposes, forensics purposes, or other purposes relevant to ensuring the availability and integrity of the hosted application. While it is important to log events identified as being critical and relevant to security, it is equally important to notify the appropriate personnel in a timely manner so they are able to respond to events as they occur. Manual review of the web server logs may not occur in a timely manner, and each event logged is open to interpretation by a reviewer. By integrating the web server into an overall or organization-wide log review, a larger picture of events can be viewed, and analysis can be done in a timely and reliable manner.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "OraLogDir" directive at the OHS server configuration scope. 3. If the directive is omitted, this is a finding. 4. Validate that the folder specified exists. If the folder does not exist, this is a finding.

## Group: SRG-APP-000358-WSR-000163

**Group ID:** `V-221339`

### Rule: OHS must be configured to store access log files to an appropriate storage device from which other tools can be configured to reference those log files for diagnostic/forensic purposes.

**Rule ID:** `SV-221339r961395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server will typically utilize logging mechanisms for maintaining a historical log of activity that occurs within a hosted application. This information can then be used for diagnostic purposes, forensics purposes, or other purposes relevant to ensuring the availability and integrity of the hosted application. While it is important to log events identified as being critical and relevant to security, it is equally important to notify the appropriate personnel in a timely manner so they are able to respond to events as they occur. Manual review of the web server logs may not occur in a timely manner, and each event logged is open to interpretation by a reviewer. By integrating the web server into an overall or organization-wide log review, a larger picture of events can be viewed, and analysis can be done in a timely and reliable manner.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "CustomLog" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope. 4. Validate that the folder specified exists. If the folder does not exist, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221340`

### Rule: OHS must have the LoadModule file_cache_module directive disabled.

**Rule ID:** `SV-221340r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule file_cache_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221341`

### Rule: OHS must have the LoadModule vhost_alias_module directive disabled.

**Rule ID:** `SV-221341r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule vhost_alias_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221342`

### Rule: OHS must have the LoadModule env_module directive disabled.

**Rule ID:** `SV-221342r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule env_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221343`

### Rule: OHS must have the LoadModule mime_magic_module directive disabled.

**Rule ID:** `SV-221343r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule mime_magic_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221344`

### Rule: OHS must have the LoadModule negotiation_module directive disabled.

**Rule ID:** `SV-221344r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule negotiation_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221345`

### Rule: OHS must not have the LanguagePriority directive enabled.

**Rule ID:** `SV-221345r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "LanguagePriority" directive. 2. Search for the "LanguagePriority" directive at the OHS server, virtual host, and directory configuration scopes. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221346`

### Rule: OHS must not have the ForceLanguagePriority directive enabled.

**Rule ID:** `SV-221346r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "ForceLanguagePriority" directive. 2. Search for the "ForceLanguagePriority" directive at the OHS server, virtual host, and directory configuration scopes. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221347`

### Rule: OHS must have the LoadModule status_module directive disabled.

**Rule ID:** `SV-221347r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule status_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221348`

### Rule: OHS must have the LoadModule info_module directive disabled.

**Rule ID:** `SV-221348r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule info_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221349`

### Rule: OHS must have the LoadModule include_module directive disabled.

**Rule ID:** `SV-221349r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule include_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221350`

### Rule: OHS must have the LoadModule autoindex_module directive disabled.

**Rule ID:** `SV-221350r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule autoindex_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221351`

### Rule: OHS must have the IndexOptions directive disabled.

**Rule ID:** `SV-221351r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains an "IndexOptions" directive. 2. Search for the "IndexOptions" directive at the OHS server, virtual host, and directory configuration scopes. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221352`

### Rule: OHS must have the AddIconByEncoding directive disabled.

**Rule ID:** `SV-221352r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains an "AddIconByEncoding" directive. 2. Search for an "AddIconByEncoding" directive at the OHS server, virtual host, and directory configuration scopes. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221353`

### Rule: OHS must have the AddIconByType directive disabled.

**Rule ID:** `SV-221353r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains an "AddIconByType" directive. 2. Search for an "AddIconByType" directive at the OHS server, virtual host, and directory configuration scopes. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221354`

### Rule: OHS must have the AddIcon directive disabled.

**Rule ID:** `SV-221354r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains an "AddIcon" directive. 2. Search for an "AddIcon" directive at the OHS server, virtual host, and directory configuration scopes. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221355`

### Rule: OHS must have the DefaultIcon directive disabled.

**Rule ID:** `SV-221355r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "DefaultIcon" directive. 2. Search for a "DefaultIcon" directive at the OHS server, virtual host, and directory configuration scopes. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221356`

### Rule: OHS must have the ReadmeName directive disabled.

**Rule ID:** `SV-221356r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "ReadmeName" directive. 2. Search for a "ReadmeName" directive at the OHS server, virtual host, and directory configuration scopes. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221357`

### Rule: OHS must have the HeaderName directive disabled.

**Rule ID:** `SV-221357r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "HeaderName" directive. 2. Search for a "HeaderName" directive at the OHS server, virtual host, and directory configuration scopes. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221358`

### Rule: OHS must have the IndexIgnore directive disabled.

**Rule ID:** `SV-221358r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains an "IndexIgnore" directive. 2. Search for an "IndexIgnore" directive at the OHS server, virtual host, and directory configuration scopes. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221359`

### Rule: OHS must have the LoadModule dir_module directive disabled.

**Rule ID:** `SV-221359r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule dir_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221360`

### Rule: OHS must have the DirectoryIndex directive disabled.

**Rule ID:** `SV-221360r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "DirectoryIndex" directive. 2. Search for the "DirectoryIndex" directive at the OHS server, virtual host, and directory configuration scopes. 3. If the directive and any surrounding "<IfModule dir_module>" directive exist and are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221361`

### Rule: OHS must have the LoadModule cgi_module directive disabled.

**Rule ID:** `SV-221361r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule cgi_module" directive within the "<IfModule mpm_prefork_module>" directive at the OHS server configuration scope. 3. If the directive and its surrounding "<IfModule mpm_prefork_module>" directive exist and are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221362`

### Rule: OHS must have the LoadModule fastcgi_module disabled.

**Rule ID:** `SV-221362r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule fastcgi_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221363`

### Rule: OHS must have the LoadModule cgid_module directive disabled for mpm workers.

**Rule ID:** `SV-221363r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule cgid_module" directive within the "<IfModule mpm_worker_module>" directive at the OHS server configuration scope. 3. If the directive and its surrounding "<IfModule mpm_worker_module>" directive exist and are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221364`

### Rule: OHS must have the IfModule cgid_module directive disabled.

**Rule ID:** `SV-221364r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<IfModule cgid_module>" directive. 2. Search for the "<IfModule cgid_module>" directive at the OHS server, virtual host, and directory configuration scope. 3. If the directive and any directives that it may contain exist and are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221365`

### Rule: OHS must have the LoadModule mpm_winnt_module directive disabled.

**Rule ID:** `SV-221365r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule cgi_module" directive within the "<IfModule mpm_winnt_module>" directive at the OHS server configuration scope. 3. If the directive and its surrounding "<IfModule mpm_winnt_module>" directive exist and are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221366`

### Rule: OHS must have the ScriptAlias directive for CGI scripts disabled.

**Rule ID:** `SV-221366r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for a "ScriptAlias /cgi-bin/" directive within a "<IfModule alias_module>" directive at the OHS server configuration scope. 3. If the directive and its surrounding "<IfModule alias_module>" directive exist and are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221367`

### Rule: OHS must have the ScriptSock directive disabled.

**Rule ID:** `SV-221367r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for a "ScriptSock" directive within a "<IfModule cgid_module>" directive at the OHS server configuration scope. Note: “ScriptSock” may appear as “Scriptsock” within the httpd.conf file. 3. If the directive and its surrounding "<IfModule cgid_module>" directive exist and are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221368`

### Rule: OHS must have the cgi-bin directory disabled.

**Rule ID:** `SV-221368r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/ssl.conf with an editor. 2. Search for a "<Directory "${ORACLE_INSTANCE}/config/fmwconfig/components/${COMPONENT_TYPE}/instances/${COMPONENT_NAME}/cgi-bin">" directive at the OHS server and virtual host configuration scopes. 3. If the directive and any directives that it contains exist and are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221369`

### Rule: OHS must have directives pertaining to certain scripting languages removed from virtual hosts.

**Rule ID:** `SV-221369r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/ssl.conf with an editor. 2. Search for a "<FilesMatch "\.(cgi|shtml|phtml|php)$">" directive at the virtual host configuration scope. 3. If the directive and any directives that it contains exist and are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221370`

### Rule: OHS must have the LoadModule asis_module directive disabled.

**Rule ID:** `SV-221370r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule asis_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221371`

### Rule: OHS must have the LoadModule imagemap_module directive disabled.

**Rule ID:** `SV-221371r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule imagemap_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221372`

### Rule: OHS must have the LoadModule actions_module directive disabled.

**Rule ID:** `SV-221372r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule actions_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221373`

### Rule: OHS must have the LoadModule speling_module directive disabled.

**Rule ID:** `SV-221373r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule speling_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221374`

### Rule: OHS must have the LoadModule userdir_module directive disabled.

**Rule ID:** `SV-221374r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule userdir_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221375`

### Rule: OHS must have the AliasMatch directive pertaining to the OHS manuals disabled.

**Rule ID:** `SV-221375r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for a "AliasMatch ^/manual(?:/(?:de|en|es|fr|ja|ko|pt-br|ru|tr))?(/.*)?$ "${PRODUCT_HOME}/manual$1"" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221376`

### Rule: OHS must have the Directory directive pointing to the OHS manuals disabled.

**Rule ID:** `SV-221376r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for a "<Directory "${PRODUCT_HOME}/manual">" directive at the OHS server configuration scope. 3. If the directive and the directives it contains exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221377`

### Rule: OHS must have the LoadModule auth_basic_module directive disabled.

**Rule ID:** `SV-221377r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule auth_basic_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221378`

### Rule: OHS must have the LoadModule authz_user_module directive disabled.

**Rule ID:** `SV-221378r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance. This module provides authorization capabilities so authenticated users can be allowed or denied access to portions of the web site. This requirement is meant to disable an unneeded service; it is not intended to restrict the use of authorization when data access restrictions specify the use of authorization. Refer to the system security plan to determine if authorization is required based on data access requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the AO approved system security plan for web server configuration specifies using the OHS authz_user_module in order to meet application architecture requirements, this requirement can be marked NA. 1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule authz_user_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221379`

### Rule: OHS must have the LoadModule authn_file_module directive disabled.

**Rule ID:** `SV-221379r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule authn_file_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221380`

### Rule: OHS must have the LoadModule authn_anon_module directive disabled.

**Rule ID:** `SV-221380r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule authn_anon_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221381`

### Rule: OHS must have the LoadModule proxy_module directive disabled.

**Rule ID:** `SV-221381r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the AO-approved system security plan for web server configuration specifies using the proxy_module directive in order to meet application architecture requirements and authentication is enforced, this requirement is NA. 1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule proxy_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221382`

### Rule: OHS must have the LoadModule proxy_http_module directive disabled.

**Rule ID:** `SV-221382r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance. The proxy_http_module requires the service of mod_proxy. It provides the features used for proxying HTTP and HTTPS requests. If proxy services are required, the proxy configuration must be approved by the AO.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the AO approved system security plan for the web server configuration specifies using the proxy_http_module directive in order to meet application architecture requirements and authentication is enforced, this requirement is NA. 1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule proxy_http_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221383`

### Rule: OHS must have the LoadModule proxy_ftp_module directive disabled.

**Rule ID:** `SV-221383r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule proxy_ftp_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221384`

### Rule: OHS must have the LoadModule proxy_connect_module directive disabled.

**Rule ID:** `SV-221384r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule proxy_connect_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221385`

### Rule: OHS must have the LoadModule proxy_balancer_module directive disabled.

**Rule ID:** `SV-221385r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule proxy_balancer_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221386`

### Rule: OHS must have the LoadModule cern_meta_module directive disabled.

**Rule ID:** `SV-221386r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule cern_meta_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221387`

### Rule: OHS must have the LoadModule expires_module directive disabled.

**Rule ID:** `SV-221387r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule expires_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221388`

### Rule: OHS must have the LoadModule usertrack_module directive disabled.

**Rule ID:** `SV-221388r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule usertrack_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221389`

### Rule: OHS must have the LoadModule uniqueid_module directive disabled.

**Rule ID:** `SV-221389r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule unique_id_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221390`

### Rule: OHS must have the LoadModule setenvif_module directive disabled.

**Rule ID:** `SV-221390r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule setenvif_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221391`

### Rule: OHS must have the BrowserMatch directive disabled.

**Rule ID:** `SV-221391r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "BrowserMatch" directive. 2. Search for the "BrowserMatch" directive at the OHS server, virtual host, and directory configuration scopes. 3. If the directive and any surrounding "BrowserMatch" directive exist and are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221392`

### Rule: OHS must have the LoadModule dumpio_module directive disabled.

**Rule ID:** `SV-221392r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule dumpio_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221393`

### Rule: OHS must have the IfModule dumpio_module directive disabled.

**Rule ID:** `SV-221393r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for a "<IfModule dumpio_module>" directive at the OHS server configuration scope. 3. If the directive and any directives that it contains exist and are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221394`

### Rule: OHS must have the Alias /icons/ directive disabled.

**Rule ID:** `SV-221394r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for an "Alias /icons/" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221395`

### Rule: OHS must have the path to the icons directory disabled.

**Rule ID:** `SV-221395r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for a "<Directory "${PRODUCT_HOME}/icons">" directive at the OHS server configuration scope. 3. If the directive exists and any directives that it contains are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221396`

### Rule: OHS must have the IfModule mpm_winnt_module directive disabled.

**Rule ID:** `SV-221396r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/ssl.conf with an editor. 2. Search for the "<IfModule mpm_winnt_module>" directive at the OHS server configuration scope. 3. If the directive and any directives it contains exist and are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000076

**Group ID:** `V-221397`

### Rule: OHS must have the LoadModule proxy_module directive disabled.

**Rule ID:** `SV-221397r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server should be primarily a web server or a proxy server but not both, for the same reasons that other multi-use servers are not recommended. Scanning for web servers that will also proxy requests into an otherwise protected network is a very common attack making the attack anonymous.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the AO-approved system security plan for the web server configuration specifies using proxy_module directive in order to meet application architecture requirements, this requirement is NA. 1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule proxy_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000076

**Group ID:** `V-221398`

### Rule: OHS must have the LoadModule proxy_http_module directive disabled.

**Rule ID:** `SV-221398r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server should be primarily a web server or a proxy server but not both, for the same reasons that other multi-use servers are not recommended. Scanning for web servers that will also proxy requests into an otherwise protected network is a very common attack making the attack anonymous.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the AO-approved system security plan for the web server configuration specifies using the proxy_http_module directive in order to meet application architecture requirements, this requirement is NA. 1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule proxy_http_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000076

**Group ID:** `V-221399`

### Rule: OHS must have the LoadModule proxy_ftp_module directive disabled.

**Rule ID:** `SV-221399r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server should be primarily a web server or a proxy server but not both, for the same reasons that other multi-use servers are not recommended. Scanning for web servers that will also proxy requests into an otherwise protected network is a very common attack making the attack anonymous.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule proxy_ftp_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000076

**Group ID:** `V-221400`

### Rule: OHS must have the LoadModule proxy_connect_module directive disabled.

**Rule ID:** `SV-221400r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server should be primarily a web server or a proxy server but not both, for the same reasons that other multi-use servers are not recommended. Scanning for web servers that will also proxy requests into an otherwise protected network is a very common attack making the attack anonymous.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule proxy_connect_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000076

**Group ID:** `V-221401`

### Rule: OHS must have the LoadModule proxy_balancer_module directive disabled.

**Rule ID:** `SV-221401r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server should be primarily a web server or a proxy server but not both, for the same reasons that other multi-use servers are not recommended. Scanning for web servers that will also proxy requests into an otherwise protected network is a very common attack making the attack anonymous.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule proxy_balancer_module" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000077

**Group ID:** `V-221402`

### Rule: OHS must disable the directive pointing to the directory containing the OHS manuals.

**Rule ID:** `SV-221402r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Web server documentation, sample code, example applications, and tutorials may be an exploitable threat to a web server because this type of code has not been evaluated and approved. A production web server must only contain components that are operationally necessary (e.g., compiled code, scripts, web-content, etc.). Any documentation, sample code, example applications, and tutorials must be removed from a production web server. To make certain that the documentation and code are not installed or uninstalled completely; the web server must offer an option as part of the installation process to exclude these packages or to uninstall the packages if necessary.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for a "<Directory "${PRODUCT_HOME}/manual">" directive at the OHS server configuration scope. 3. If the directive and the directives it contains exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000077

**Group ID:** `V-221403`

### Rule: OHS must have the AliasMatch directive disabled for the OHS manuals.

**Rule ID:** `SV-221403r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server documentation, sample code, example applications, and tutorials may be an exploitable threat to a web server because this type of code has not been evaluated and approved. A production web server must only contain components that are operationally necessary (e.g., compiled code, scripts, web-content, etc.). Any documentation, sample code, example applications, and tutorials must be removed from a production web server. To make certain that the documentation and code are not installed or uninstalled completely; the web server must offer an option as part of the installation process to exclude these packages or to uninstall the packages if necessary.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for a "AliasMatch ^/manual(?:/(?:de|en|es|fr|ja|ko|pt-br|ru|tr))?(/.*)?$ "${PRODUCT_HOME}/manual$1"" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000081

**Group ID:** `V-221404`

### Rule: OHS must have the AddHandler directive disabled.

**Rule ID:** `SV-221404r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Controlling what a user of a hosted application can access is part of the security posture of the web server. Any time a user can access more functionality than is needed for the operation of the hosted application poses a security issue. A user with too much access can view information that is not needed for the user's job role, or the user could use the function in an unintentional manner. A MIME tells the web server what type of program various file types and extensions are and what external utilities or programs are needed to execute the file type. A shell is a program that serves as the basic interface between the user and the operating system, so hosted application users must not have access to these programs. Shell programs may execute shell escapes and can then perform unauthorized activities that could damage the security posture of the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for "AddHandler" directives at the OHS server, virtual host, and directory configuration scopes. 3. If an "AddHandler" directive exists, this is a finding.

## Group: SRG-APP-000141-WSR-000082

**Group ID:** `V-221405`

### Rule: OHS must have the LoadModule cgi_module directive disabled.

**Rule ID:** `SV-221405r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Scripts allow server side processing on behalf of the hosted application user or as processes needed in the implementation of hosted applications. Removing scripts not needed for application operation or deemed vulnerable helps to secure the web server. To assure scripts are not added to the web server and run maliciously, those script mappings that are not needed or used by the web server for hosted application operation must be removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule cgi_module" directive within the "<IfModule mpm_prefork_module>" directive at the OHS server configuration scope. 3. If the directive and its surrounding "<IfModule mpm_prefork_module>" directive exist and are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000082

**Group ID:** `V-221406`

### Rule: OHS must have the LoadModule cgid_module directive disabled.

**Rule ID:** `SV-221406r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Scripts allow server side processing on behalf of the hosted application user or as processes needed in the implementation of hosted applications. Removing scripts not needed for application operation or deemed vulnerable helps to secure the web server. To assure scripts are not added to the web server and run maliciously, those script mappings that are not needed or used by the web server for hosted application operation must be removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule cgid_module" directive within the "<IfModule mpm_worker_module>" directive at the OHS server configuration scope. 3. If the directive and its surrounding "<IfModule mpm_worker_module>" directive exist and are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000082

**Group ID:** `V-221407`

### Rule: OHS must have the IfModule cgid_module directive disabled for the OHS server, virtual host, and directory configuration.

**Rule ID:** `SV-221407r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Scripts allow server side processing on behalf of the hosted application user or as processes needed in the implementation of hosted applications. Removing scripts not needed for application operation or deemed vulnerable helps to secure the web server. To assure scripts are not added to the web server and run maliciously, those script mappings that are not needed or used by the web server for hosted application operation must be removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<IfModule cgid_module>" directive. 2. Search for the "<IfModule cgid_module>" directive at the OHS server, virtual host, and directory configuration scope. 3. If the directive and any directives that it may contain exist and are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000082

**Group ID:** `V-221408`

### Rule: OHS must have the LoadModule cgi_module directive disabled within the IfModule mpm_winnt_module directive.

**Rule ID:** `SV-221408r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Scripts allow server side processing on behalf of the hosted application user or as processes needed in the implementation of hosted applications. Removing scripts not needed for application operation or deemed vulnerable helps to secure the web server. To assure scripts are not added to the web server and run maliciously, those script mappings that are not needed or used by the web server for hosted application operation must be removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule cgi_module" directive within the "<IfModule mpm_winnt_module>" directive at the OHS server configuration scope. 3. If the directive and its surrounding "<IfModule mpm_winnt_module>" directive exist and are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000082

**Group ID:** `V-221409`

### Rule: OHS must have the ScriptAlias /cgi-bin/ directive within a IfModule alias_module directive disabled.

**Rule ID:** `SV-221409r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Scripts allow server side processing on behalf of the hosted application user or as processes needed in the implementation of hosted applications. Removing scripts not needed for application operation or deemed vulnerable helps to secure the web server. To assure scripts are not added to the web server and run maliciously, those script mappings that are not needed or used by the web server for hosted application operation must be removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for a "ScriptAlias /cgi-bin/" directive within a "<IfModule alias_module>" directive at the OHS server configuration scope. 3. If the directive and its surrounding "<IfModule alias_module>" directive exist and are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000082

**Group ID:** `V-221410`

### Rule: OHS must have the ScriptSock directive within a IfModule cgid_module directive disabled.

**Rule ID:** `SV-221410r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Scripts allow server side processing on behalf of the hosted application user or as processes needed in the implementation of hosted applications. Removing scripts not needed for application operation or deemed vulnerable helps to secure the web server. To assure scripts are not added to the web server and run maliciously, those script mappings that are not needed or used by the web server for hosted application operation must be removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for a "ScriptSock" directive within a "<IfModule cgid_module>" directive at the OHS server configuration scope. 3. If the directive and its surrounding "<IfModule cgid_module>" directive exist and are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000082

**Group ID:** `V-221411`

### Rule: OHS must have the cgi-bin directory disabled.

**Rule ID:** `SV-221411r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Scripts allow server side processing on behalf of the hosted application user or as processes needed in the implementation of hosted applications. Removing scripts not needed for application operation or deemed vulnerable helps to secure the web server. To assure scripts are not added to the web server and run maliciously, those script mappings that are not needed or used by the web server for hosted application operation must be removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/ssl.conf with an editor. 2. Search for a "<Directory "${ORACLE_INSTANCE}/config/fmwconfig/components/${COMPONENT_TYPE}/instances/${COMPONENT_NAME}/cgi-bin">" directive at the OHS server and virtual host configuration scopes. 3. If the directive and any directives that it contains exist and are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000082

**Group ID:** `V-221412`

### Rule: OHS must have directives pertaining to certain scripting languages removed from virtual hosts.

**Rule ID:** `SV-221412r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Scripts allow server side processing on behalf of the hosted application user or as processes needed in the implementation of hosted applications. Removing scripts not needed for application operation or deemed vulnerable helps to secure the web server. To assure scripts are not added to the web server and run maliciously, those script mappings that are not needed or used by the web server for hosted application operation must be removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/ssl.conf with an editor. 2. Search for a "<FilesMatch "\.(cgi|shtml|phtml|php)$">" directive at the virtual host configuration scope. 3. If the directive and any directives that it contains exist and are not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000083

**Group ID:** `V-221413`

### Rule: OHS must have resource mappings set to disable the serving of certain file types.

**Rule ID:** `SV-221413r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Resource mapping is the process of tying a particular file type to a process in the web server that can serve that type of file to a requesting client and to identify which file types are not to be delivered to a client. By not specifying which files can and which files cannot be served to a user, the web server could deliver to a user web server configuration files, log files, password files, etc. The web server must only allow hosted application file types to be served to a user and all other types must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for "<FilesMatch>" directives beyond the "<FilesMatch"^\.ht">" directive at the OHS server, virtual host, and directory configuration scopes. 3. If the "<FilesMatch>" directive is omitted or it and/or any directives it contains are set improperly, this is a finding.

## Group: SRG-APP-000141-WSR-000087

**Group ID:** `V-221414`

### Rule: Users and scripts running on behalf of users must be contained to the document root or home directory tree of OHS.

**Rule ID:** `SV-221414r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server is designed to deliver content and execute scripts or applications on the request of a client or user. Containing user requests to files in the directory tree of the hosted web application and limiting the execution of scripts and applications guarantees that the user is not accessing information protected outside the application's realm. The web server must also prohibit users from jumping outside the hosted application directory tree through access to the user's home directory, symbolic links or shortcuts, or through search paths for missing files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "<Directory>" directive at OHS server and virtual host configuration scopes. 3. If the "Options" directive within the "<Directory>" directive is omitted or is set improperly, this is a finding.

## Group: SRG-APP-000142-WSR-000089

**Group ID:** `V-221415`

### Rule: OHS must be configured to use a specified IP address, port, and protocol.

**Rule ID:** `SV-221415r1043177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The web server must be configured to listen on a specified IP address and port. Without specifying an IP address and port for the web server to utilize, the web server will listen on all IP addresses available to the hosting server. If the web server has multiple IP addresses, i.e., a management IP address, the web server will also accept connections on the management IP address. Accessing the hosted application through an IP address normally used for non-application functions opens the possibility of user access to resources, utilities, files, ports, and protocols that are protected on the desired application IP address.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/ssl.conf with an editor. 2. Search for a "Listen" directive at the OHS server configuration scope. 3. If the directive is set without an IP address, port, and protocol specified, this is a finding.

## Group: SRG-APP-000516-WSR-000079

**Group ID:** `V-221416`

### Rule: The Node Manager account password associated with the installation of OHS must be in accordance with DoD guidance for length, complexity, etc.

**Rule ID:** `SV-221416r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>During installation of the web server software, accounts are created for the web server to operate properly. The accounts installed can have either no password installed or a default password, which will be known and documented by the vendor and the user community. The first things an attacker will try when presented with a login screen are the default user identifiers with default passwords. Installed applications may also install accounts with no password, making the login even easier. Once the web server is installed, the passwords for any created accounts should be changed and documented. The new passwords must meet the requirements for all passwords, i.e., upper/lower characters, numbers, special characters, time until change, reuse policy, etc. Service accounts or system accounts that have no login capability do not need to have passwords set or changed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. If the password for Node Manager does not meet DoD requirements for password complexity, this is a finding. 2. Open $DOMAIN_HOME/config/nodemanager/nm_password.properties with an editor. 3. If the "username" property and value are still present, this is a finding. 4. If the "password" property and value are still present, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221417`

### Rule: OHS must have Entity tags (ETags) disabled.

**Rule ID:** `SV-221417r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Entity tags (ETags) are used for cache management to save network bandwidth by not sending a web page to the requesting client if the cached version on the client is current. When the client only has the ETag information, the client will make a request to the server with the ETag. The server will then determine if the client can use the client cached version of the web page or if a new version is required. As part of the ETag information, the server sends to the client the index node (inode) information for the file being requested. The inode information gives an attacker sensitive information like inode number, multipart MIME boundaries and makes certain NFS attacks much simpler to execute.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "Header" and "FileETag" directives at the OHS server, virtual host, or directory configuration scope. 3. If the "Header" and "FileETag" directives are omitted or set improperly, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221418`

### Rule: The SecureListener property of the Node Manager configured to support OHS must be enabled for secure communication.

**Rule ID:** `SV-221418r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Oracle Node Manager is the utility that is used to perform common operational tasks for OHS. To protect the information being sent between WebLogic Scripting Tool and Node Manager, the Node Manager listening address must be secured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/nodemanager/nodemanager.properties with an editor. 2. Search for the "SecureListener" property. 3. If the property is not set to "True", this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221419`

### Rule: The ListenAddress property of the Node Manager configured to support OHS must match the CN of the certificate used by Node Manager.

**Rule ID:** `SV-221419r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Oracle Node Manager is the utility that is used to perform common operational tasks for OHS. For connections to be made to the Node Manager, it must listen on an assigned address. When this parameter is not set, the Node Manager will listen on all available addresses on the server. This may lead to the Node Manager listening on networks, i.e., public network space, where Node Manager may become susceptible to attack instead of being limited to listening for connections on a controlled and secure management network. It is also important that the address specified matches the CN of the Node Manager.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/nodemanager/nodemanager.properties with an editor. 2. Search for the "ListenAddress" property. 3. If the property does not exist or is not set to the CN of the Node Manager certificate, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221420`

### Rule: The AuthenticationEnabled property of the Node Manager configured to support OHS must be configured to enforce authentication.

**Rule ID:** `SV-221420r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Oracle Node Manager is the utility that is used to perform common operational tasks for OHS. To accept connections from the WebLogic Scripting Tool, the Node Manager can be setup to authenticate the connections or not. If connections are not authenticated, a hacker could connect to the Node Manager and initiate commands to OHS to gain further access, cause a DoS, or view protected information. To protect against unauthenticated connections, the "AuthenticationEnabled" directive must be set to "true".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/nodemanager/nodemanager.properties with an editor. 2. Search for the "AuthenticationEnabled" property. 3. If the property does not exist or is not set "True", this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221421`

### Rule: The KeyStores property of the Node Manager configured to support OHS must be configured for secure communication.

**Rule ID:** `SV-221421r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Oracle Node Manager is a utility that can be used to perform common operational tasks across Managed Servers. These servers can be distributed across multiple machines and geographical locations. The "KeyStores" property is used to configure the keystore configuration that will be used by Node Manager to locate its identity (private key and digital certificate) and trust (trusted CA certificates). The property must be set to "CustomIdentityAndCustomTrust", which causes Node Manager to use an identity and trust keystore created by the SA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/nodemanager/nodemanager.properties with an editor. 2. Search for the "KeyStores" property. 3. If the property does not exist or is not set to "CustomIdentityAndCustomTrust", this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221422`

### Rule: The CustomIdentityKeyStoreFileName property of the Node Manager configured to support OHS must be configured for secure communication.

**Rule ID:** `SV-221422r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Oracle Node Manager is the utility that is used to perform common operational tasks for OHS. The "CustomIdentityKeyStoreFileName" property specifies the file name of the identity keystore. This property is required when the "KeyStores" property is set to "CustomIdentityAndCustomTrust". Without specifying the "CustomIdentityKeyStoreFileName" property, the Node Manager will not operate properly and may cause the system to fail into an unsecure state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/nodemanager/nodemanager.properties with an editor. 2. Search for the "CustomIdentityKeyStoreFileName" property. 3. If the property does not exist or is set improperly, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221423`

### Rule: The CustomIdentityKeyStorePassPhrase property of the Node Manager configured to support OHS must be configured for secure communication.

**Rule ID:** `SV-221423r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Oracle Node Manager is the utility that is used to perform common operational tasks for OHS. The "CustomIdentityKeyStorePassPhrase" property is used to protect the data within the keystore. Without protection, the data within the keystore could be compromised allowing an attacker to use the certificates to gain trusted access to other systems or processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/nodemanager/nodemanager.properties with an editor. 2. Search for the "CustomIdentityKeyStorePassPhrase" property. 3. If the property does not exist or is set improperly, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221424`

### Rule: The CustomIdentityAlias property of the Node Manager configured to support OHS must be configured for secure communication.

**Rule ID:** `SV-221424r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Oracle Node Manager is the utility that is used to perform common operational tasks for OHS. The "CustomIdentityAlias" specifies the alias when loading the private key into the keystore. This property is required when the "KeyStores" property is set to "CustomIdentityAndCustomTrust". Without specifying the "CustomIdentityKeyStoreFileName" property, the Node Manager will not operate properly and may cause the system to fail into an unsecure state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/nodemanager/nodemanager.properties with an editor. 2. Search for the "CustomIdentityAlias" property. 3. If the property does not exist or is set improperly, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221425`

### Rule: The CustomIdentityPrivateKeyPassPhrase property of the Node Manager configured to support OHS must be configured for secure communication.

**Rule ID:** `SV-221425r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Oracle Node Manager is the utility that is used to perform common operational tasks for OHS. The "CustomIdentityPrivateKeyPassPhrase" is the password that protects the private key when creating certificates. If a password is not used, the private key is not protected and can be used by any user or attacker that can get access to the private key.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/nodemanager/nodemanager.properties with an editor. 2. Search for the "CustomIdentityPrivateKeyPassPhrase" property. 3. If the property does not exist or is set improperly, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221426`

### Rule: The listen-address element defined within the config.xml of the OHS Standalone domain that supports OHS must be configured for secure communication.

**Rule ID:** `SV-221426r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Oracle Node Manager is the utility that is used to perform common operational tasks for OHS. When starting an OHS instance, the WebLogic Scripting Tool reads the parameters within the config.xml file to setup the communication to the Node Manager. If the IP address to be used for communication is not specified, the WebLogic Scripting tool will not be able to setup a secure connection to Node Manager.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/config.xml with an editor. 2. Search for the "<listen-address>" element within the "<node-manager>" element. 3. If the element does not exist or is not set to the CN of the Node Manager certificate, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221427`

### Rule: The listen-port element defined within the config.xml of the OHS Standalone Domain must be configured for secure communication.

**Rule ID:** `SV-221427r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Oracle Node Manager is the utility that is used to perform common operational tasks for OHS. When starting an OHS instance, the WebLogic Scripting Tool reads the parameters within the config.xml file to setup the communication to the Node Manager. If the port to be used for communication is not specified, the WebLogic Scripting tool will not be able to setup a secure connection to Node Manager.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/config.xml with an editor. 2. Search for the "<listen-port>" element within the "<node-manager>" element. 3. If the element does not exist or is not set to the same value as the "ListenPort" property found in $DOMAIN_HOME/nodemanager/nodemanager.properties, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221428`

### Rule: The WLST_PROPERTIES environment variable defined for the OHS WebLogic Scripting Tool must be updated to reference an appropriate trust store so that it can communicate with the Node Manager supporting OHS.

**Rule ID:** `SV-221428r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Oracle Node Manager is the utility that is used to perform common operational tasks for OHS. When starting an OHS instance, the "OHS" WebLogic Scripting Tool needs to trust the certificate presented by the Node Manager in order to setup secure communication with it. If the "OHS" WLST does not trust the certificate presented by Node Manager, the "OHS" WebLogic Scripting tool will not be able to setup a secure connection to it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Check for the existence of $ORACLE_HOME/ohs/common/bin/setWlstEnv.sh. 2a. If the setWlstEnv.sh does not exist or does not contain the "WLST_PROPERTIES" environment variable set to a valid trust keystore containing the Certificate Authority and Chain of the Node Manager identity, this is a finding. 2b. If the setWlstenv.sh file does not exist, this is a finding. 2c. If the setWlstenv.sh file has permissions more permissive than 750, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221429`

### Rule: The WLST_PROPERTIES environment variable defined for the Fusion Middleware WebLogic Scripting Tool must be updated to reference an appropriate trust store so that it can communicate with the Node Manager supporting OHS.

**Rule ID:** `SV-221429r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Oracle Node Manager is the utility that is used to perform common operational tasks for OHS. When starting an OHS instance, the "Fusion Middleware" WebLogic Scripting Tool needs to trust the certificate presented by the Node Manager in order to setup secure communication with it. If the "Fusion Middleware" WLST does not trust the certificate presented by Node Manager, the "Fusion Middleware" WebLogic Scripting tool will not be able to setup a secure connection to it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Check for the existence of $ORACLE_HOME/oracle_common/common/bin/setWlstEnv.sh. 2a. If the setWlstEnv.sh does not exist or does not contain the "WLST_PROPERTIES" environment variable set to a valid trust keystore containing the Certificate Authority and Chain of the Node Manager identity, this is a finding. 2b. If the setWlstenv.sh file does not exist, this is a finding. 2c. If the setWlstenv.sh file has permissions more permissive than 750, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221430`

### Rule: OHS must limit access to the Dynamic Monitoring Service (DMS).

**Rule ID:** `SV-221430r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Oracle Dynamic Monitoring Service (DMS) enables application developers, support analysts, system administrators, and others to measure application specific performance information. If OHS allows any machine to connect and monitor performance, an attacker could connect and gather information that could be used to cause a DoS for OHS. Information that is shared could also be used to further an attack to other servers and devices through trusted relationships.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/admin.conf in it with an editor. 2. Search for the "Allow" directive within the "<Location /dms/>" directive at the virtual host configuration scope. 3. If the "Allow" directive is set to "from all", this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221431`

### Rule: OHS must have the AllowOverride directive set properly.

**Rule ID:** `SV-221431r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The property "AllowOverride" is used to allow directives to be set differently than those set for the overall architecture. When the property is not set to "None", OHS will check for directives in the htaccess files at each directory level until the requested resource is found for each URL request. Allowing parameters to be overridden at different levels of an application becomes a security risk as the overall security of the hosted application can change dependencies on the URL being accessed. Security management also becomes difficult as a misconfiguration can be mistakenly made.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "AllowOverride" directive at the directory configuration scope. 3. If the "AllowOverride" directive is omitted or is not set to "None", this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221432`

### Rule: OHS must be set to evaluate deny directives first when considering whether to serve a file.

**Rule ID:** `SV-221432r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Part of securing OHS is allowing/denying access to the web server. Deciding on the manor the allow/deny rules are evaluated can turn what was once an allowable access into being blocked if the evaluation is reversed. By ordering the access as first deny and then allow, OHS will deny all access first and then look at the allow clauses to see who may access the server. By structuring the evaluation in this manner, a misconfiguration will more likely deny a valid user than allow an illegitimate user that may compromise the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "<Directory />" directive within the OHS server configuration scope. 3. If the "Order" directive within the "<Directory />" directive is omitted or is set improperly, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221433`

### Rule: OHS must deny all access by default when considering whether to serve a file.

**Rule ID:** `SV-221433r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Part of securing OHS is allowing/denying access to the web server. Deciding on the manor the allow/deny rules are evaluated can turn what was once an allowable access into being blocked if the evaluation is reversed. By ordering the access as first deny and then allow, OHS will deny all access first and then look at the allow clauses to see who may access the server. By structuring the evaluation in this manner, a misconfiguration will more likely deny a valid user than allow an illegitimate user that may compromise the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "<Directory />" directive within the OHS server configuration scope. 3. If the "Deny" directive within the "<Directory />" directive is omitted or is set improperly, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221434`

### Rule: The OHS instance installation must not contain an .htaccess file.

**Rule ID:** `SV-221434r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>.htaccess files are used to override settings in the OHS configuration files. The placement of the .htaccess file is also important as the settings will affect the directory where the file is located and any subdirectories below. Allowing the use of .htaccess files, the hosted application security posture and overall OHS posture could change dependent on the URL being accessed. Allowing the override of parameters in .htaccess files makes it difficult to truly know the security posture of the system and it also makes it difficult to understand what the security posture may have been if an attack is successful. To thwart the overriding of parameters, .htaccess files must not be used and the "AllowOverride" parameter must be set to "none".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. cd $DOMAIN_HOME/config/fmwconfig/components/OHS 2. find . -name .htaccess -print 3. If any .htaccess files are found, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221435`

### Rule: The OHS instance configuration must not reference directories that contain an .htaccess file.

**Rule ID:** `SV-221435r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>.htaccess files are used to override settings in the OHS configuration files. The placement of the .htaccess file is also important as the settings will affect the directory where the file is located and any subdirectories below. Allowing the use of .htaccess files, the hosted application security posture and overall OHS posture could change dependent on the URL being accessed. Allowing the override of parameters in .htaccess files makes it difficult to truly know the security posture of the system and it also makes it difficult to understand what the security posture may have been if an attack is successful. To thwart the overriding of parameters, .htaccess files must not be used and the "AllowOverride" parameter must be set to "none".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "<Directory>" directives at the server and virtual host configuration scopes. 3. Go to the location specified as the value for each "<Directory>" directive (e.g., cd $DOMAIN_HOME/config/fmwconfig/components/OHS/instances/ohs1/htdocs). 4. Check for the existence of any .htaccess files in the aforementioned locations (e.g., find . -name .htaccess -print). 5. If any .htaccess files are found, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221436`

### Rule: OHS must have the HostnameLookups directive enabled.

**Rule ID:** `SV-221436r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Setting the "HostnameLookups" to "On" allows for more information to be logged in the event of an attack and subsequent investigation. This information can be added to other information gathered to narrow the attacker location. The DNS name can also be used for filtering access to the OHS hosted applications by denying particular types of hostnames.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "HostnameLookups" directive at the server, virtual host, and directory configuration scopes. 3. If the "HostnameLookups" directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221437`

### Rule: OHS must have the ServerAdmin directive set properly.

**Rule ID:** `SV-221437r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Making sure that information is given to the system administrator in a timely fashion is important. This information can be system status, warnings that may need attention before system failure or actual failure notification. Having this information sent to the system administrator when the issue arises allows for the system administrator to quickly take action and avoid potential DoS for customers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "ServerAdmin" directive at the server and virtual host configuration scopes. 3. If the "ServerAdmin" directive is omitted or is set improperly, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221438`

### Rule: OHS must restrict access methods.

**Rule ID:** `SV-221438r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The directive "<LimitExcept>" allows the system administrator to restrict what users may use which methods. An example of methods would be GET, POST and DELETE. These three are the most common used by applications and should be allowed. Methods such as TRACE, if allowed, give an attacker a way to map the system so that vulnerabilities to the system can be researched and developed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "<LimitExcept>" directive at the directory configuration scope. 3. If the "<LimitExcept>" directive is omitted (with the exception of the "<Directory />" directive) or is set improperly, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221439`

### Rule: The OHS htdocs directory must not contain any default files.

**Rule ID:** `SV-221439r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Default files from the OHS installation should not be part of the htdocs directory. These files are not always patched or supported and may become an attacker vector in the future.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. cd $DOMAIN_HOME/config/fmwconfig/components/OHS/instances/ohs1/htdocs 2. Check for the existence of the OracleHTTPServer12c_files directory (e.g., ls). 3. If there is an OracleHTTPServer12c_files directory exists, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221440`

### Rule: OHS must have the SSLSessionCacheTimeout directive set properly.

**Rule ID:** `SV-221440r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>During an SSL session, information about the session is stored in the global/inter-process SSL Session Cache, the OpenSSL internal memory cache and for sessions resumed by TLS session resumption (RFC 5077). This information must not be allowed to live forever, but expire and become invalid so that an attacker cannot hijack the session if not closed by the hosted application properly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/ssl.conf with an editor. 2. Search for the "SSLSessionCacheTimeout" directive at the OHS server configuration scope. 3. If the directive is omitted or is set greater than 60, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221441`

### Rule: OHS must have the RewriteEngine directive enabled.

**Rule ID:** `SV-221441r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The rewrite engine is used to evaluate URL requests and modify the requests on the fly. Enabling this engine gives the system administrator the capability to trap potential attacks before reaching the hosted applications or to modify the URL to fix issues in the request before forwarding to the applications. The rewrite engine becomes a pre-filtering tool to fix data issues before reaching the hosted applications where the URL format or data within the URL could cause buffer overflows, redirection or mobile code snippets that could become an issue if not filtered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "RewriteEngine" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or is not set to "On", this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221442`

### Rule: OHS must have the RewriteOptions directive set properly.

**Rule ID:** `SV-221442r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The rules for the rewrite engine can be configured to inherit those from the parent and build upon that set of rules, to copy the rules from the parent if there are none defined or to only process the rules if the input is a URL. Of these, the most secure is to inherit from the parent because of how this implemented. The rules for the current configuration, process or directory, are loaded and then the parent are overlaid. This means that the parent rule will always override the child rule. This gives the server a more consistent security configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "RewriteOptions" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or is not set to "inherit", this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221443`

### Rule: OHS must have the RewriteLogLevel directive set to the proper log level.

**Rule ID:** `SV-221443r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Logging must not contain sensitive information or more information necessary than that needed to administer the system. The log levels from the rewrite engine range from 0 to 9 where 0 is no logging and 9 being the most verbose. A log level that gives enough information for an investigation if an attack occurs of enough information to troubleshoot issues should be selected. Too much information makes the system vulnerable and may give attacker information to other resources or data within the hosted applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "RewriteLogLevel" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or is not set to "3", this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221444`

### Rule: OHS must have the RewriteLog directive set properly.

**Rule ID:** `SV-221444r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Specifying where the log files are written gives the system administrator the capability to store the files in a location other than the default, with system files or in a globally accessible location. The system administrator can also specify a location that is accessible by any enterprise tools that may use the logged data to give a picture of the overall enterprise security posture. If a file is not specified, OHS will still generate the log data, but it is not written and therefore, cannot be used to monitor the system or for forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "RewriteLog" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding unless inherited from a larger scope. 4. Validate that the folder specified exists. If the folder does not exist, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221445`

### Rule: All accounts installed with the web server software and tools must have passwords assigned and default passwords changed.

**Rule ID:** `SV-221445r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>During installation of the web server software, accounts are created for the web server to operate properly. The accounts installed can have either no password installed or a default password, which will be known and documented by the vendor and the user community. The first things an attacker will try when presented with a login screen are the default user identifiers with default passwords. Installed applications may also install accounts with no password, making the login even easier. Once the web server is installed, the passwords for any created accounts should be changed and documented. The new passwords must meet the requirements for all passwords, i.e., upper/lower characters, numbers, special characters, time until change, reuse policy, etc. Normally, a service account is established for OHS. This is because a privileged account is not desirable and the server is designed to run for long uninterrupted periods of time. The SA or Web Manager will need password access to OHS to restart the service in the event of an emergency as OHS is not to restart automatically after an unscheduled interruption. If the password is not entrusted to an SA or web manager the ability to ensure the availability of OHS is compromised. Service accounts or system accounts that have no login capability do not need to have passwords set or changed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
NOTE: Service accounts or system accounts that have no login capability do not need to have passwords set or changed. Review the web server documentation and deployment configuration to determine what non-service/system accounts were installed by the web server installation process. Verify the passwords for these accounts have been set and/or changed from the default passwords. Verify the SA/Web manager are notified of the changed password. If these accounts still have no password or have default passwords, this is a finding. If the SA/web manager does not know the changed password, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221446`

### Rule: A production OHS Installation must prohibit the installation of a compiler.

**Rule ID:** `SV-221446r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The presence of a compiler on a production server facilitates the malicious user’s task of creating custom versions of programs and installing Trojan Horses or viruses. For example, the attacker’s code can be uploaded and compiled on the server under attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Ask the System Administrator if a compiler is installed on the system. 2. If it is, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221447`

### Rule: A public OHS installation, if hosted on the NIPRNet, must be isolated in an accredited DoD DMZ Extension.

**Rule ID:** `SV-221447r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To minimize exposure of private assets to unnecessary risk by attackers, public web servers must be isolated from internal systems. Public web servers are by nature more vulnerable to attack from publically based sources, such as the public Internet. Once compromised, a public web server might be used as a base for further attack on private resources, unless additional layers of protection are implemented. Public web servers must be located in a DoD DMZ Extension, if hosted on the NIPRNet, with carefully controlled access. Failure to isolate resources in this way increase risk that private assets are exposed to attacks from public sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, confirm with the OHS Administrator that OHS is installed in a DMZ and isolated from internal systems. 2. If not, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221448`

### Rule: A private OHS installation must be located on a separate controlled access subnet.

**Rule ID:** `SV-221448r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Private web servers, which host sites that serve controlled access data, must be protected from outside threats in addition to insider threats. Insider threat may be accidental or intentional but, in either case, can cause a disruption in service of the web server. To protect the private web server from these threats, it must be located on a separate controlled access subnet and must not be a part of the public DMZ that houses the public web servers. It also cannot be located inside the enclave as part of the local general population LAN.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, confirm with the OHS Administrator that OHS is installed on a separately controlled access subnet, not part of any DMZ. 2. Confirm that the OHS server is isolated from access by the LAN's general population. 3. If not, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221449`

### Rule: The version of the OHS installation must be vendor supported.

**Rule ID:** `SV-221449r1067472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Many vulnerabilities are associated with older versions of software. As hot fixes and patches are issued, these solutions are included in the next version of the server software. Maintaining OHS at a current version makes the efforts of a malicious user to exploit the web service more difficult.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
OHS 12.1.X is no longer supported by the vendor. If the system is running OHS 12.1.X, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221450`

### Rule: OHS must be certified with accompanying Fusion Middleware products.

**Rule ID:** `SV-221450r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OHS is capable of being used with other Oracle products. For the products to work properly and not introduce vulnerabilities or errors, Oracle certifies which versions work with each other. Insisting that the certified versions be installed together in a production environment reduces the possibility of successful attacks, DoS through software system downtime and easier patch management for the SA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. If OHS is used with other Fusion Middleware products, check to see if the combination is certified per http://www.oracle.com/technetwork/middleware/fusion-middleware/documentation/fmw-1213certmatrix-2226694.xls. 2. If not a certified configuration, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221451`

### Rule: OHS tools must be restricted to the web manager and the web managers designees.

**Rule ID:** `SV-221451r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All automated information systems are at risk of data loss due to disaster or compromise. Failure to provide adequate protection to the administration tools creates risk of potential theft or damage that may ultimately compromise the mission. Adequate protection ensures that server administration operates with less risk of losses or operations outages. The key web service administrative and configuration tools must be accessible only by the authorized web server administrators. All users granted this authority must be documented and approved by the ISSO. Access to OHS must be limited to authorized users and administrators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Determine whether anyone other than the System Administrator or the OHS Administrator has inappropriate access to modify the OHS configuration. This includes the ability to use the OS account that owns OHS, root, or a tool with OHS management or monitoring capability such as Oracle Enterprise Manager (OEM). 2. If so, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221452`

### Rule: All utility programs, not necessary for operations, must be removed or disabled.

**Rule ID:** `SV-221452r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Just as running unneeded services and protocols is a danger to the web server at the lower levels of the OSI model, running unneeded utilities and programs is also a danger at the application layer of the OSI model. Office suites, development tools, and graphical editors are examples of such programs that are troublesome. Individual productivity tools have no legitimate place or use on an enterprise, production web server and they are also prone to their own security risks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Check the server for software that is unnecessary for OHS operation. 2. If the software is unnecessary for OHS, other organization requirements, or is not appropriately patched or supported, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221453`

### Rule: The OHS htpasswd files (if present) must reflect proper ownership and permissions.

**Rule ID:** `SV-221453r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In addition to OS restrictions, access rights to files and directories can be set on a web site using the web server software. That is, in addition to allowing or denying all access rights, a rule can be specified that allows or denies partial access rights. For example, users can be given read-only access rights to files, to view the information but not change the files. This check verifies that the htpasswd file is only accessible by system administrators or web managers, with the account running the web service having group permissions of read and execute. Htpasswd is a utility used by OHS to provide for password access to designated web sites.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Check the permissions of the htpasswd file. (e.g., ls -l $ORACLE_HOME/ohs/bin/htpasswd). 2. If the file has permissions beyond "-rwxr-----" (i.e., 740), this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221454`

### Rule: A public OHS installation must limit email to outbound only.

**Rule ID:** `SV-221454r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Incoming E-mail has been known to provide hackers with access to servers. Disabling the incoming mail service prevents this type of attacks. Additionally, Email represents the main use of the Internet. It is specialized application that requires the dedication of server resources. To combine this type of transaction processing function with the file serving role of the web server creates an inherent conflict. Supporting mail services on a web server opens the server to the risk of abuse as an email relay. This check verifies, by checking the OS, that incoming e-mail is not supported.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Check whether the OHS server is configured to accept SMTP connections. (e.g., telnet localhost 25). 2. If it is, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221455`

### Rule: OHS content and configuration files must be part of a routine backup program.

**Rule ID:** `SV-221455r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Backing up web server data and web server application software after upgrades or maintenance ensures that recovery can be accomplished up to the current version. It also provides a means to determine and recover from subsequent unauthorized changes to the software and data. A tested and verifiable backup strategy will be implemented for web server software as well as all web server data files. Backup and recovery procedures will be documented and the Web Manager or SA for the specific application will be responsible for the design, test, and implementation of the procedures. The site will have a contingency processing plan/disaster recovery plan that includes web servers. The contingency plan will be periodically tested in accordance with DoDI 8500.2 requirements. The site will identify an off-site storage facility in accordance with DoDI 8500.2 requirements. Off-site backups will be updated on a regular basis and the frequency will be documented in the contingency plan.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Check that the following files and directories are backed up on a regular basis: a) /etc/oraInst.loc b) Directory identified by inventory_loc parameter within /etc/oraInst.loc c) /etc/cap.ora d) $MW_HOME 2. Confirm the ability to restore the above files and directories successfully. 3. Confirm the successful operation of OHS upon a successful restoration of the files and directories. 4. If the files aren't backed up on a regular schedule or the backups haven't been tested, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221456`

### Rule: OHS must be segregated from other services.

**Rule ID:** `SV-221456r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The web server installation and configuration plan should not support the co-hosting of multiple services such as Domain Name Service (DNS), e-mail, databases, search engines, indexing, or streaming media on the same server that is providing the web publishing service. By separating these services, physically or logically, additional defensive layers are established between the web service and the applicable application should either be compromised. Disallowed or restricted services in the context of this vulnerability applies to services that are not directly associated with the delivery of web content. An operating system that supports a web server will not provide other services (e.g., domain controller, e-mail server, database server, etc.). Only those services necessary to support the web server and its hosted sites are specifically allowed and may include, but are not limited to, operating system, logging, anti-virus, host intrusion detection, administrative maintenance, or network requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Obtain a copy of the OHS installation and configuration plan. 2. Ask the System Administrator whether any additional services (e.g., database, DNS, mail, application server, etc.) are installed with OHS that do not directly support operation or management of OHS. Separation of services may be physical or logical. 3. If so, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221457`

### Rule: OHS must have all applicable patches (i.e., CPUs) applied/documented (OEM).

**Rule ID:** `SV-221457r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The IAVM process does not address all patches that have been identified for the host operating system or, in this case, the web server software environment. Many vendors have subscription services available to notify users of known security threats. The site needs to be aware of these fixes and make determinations based on local policy and what software features are installed, if these patches need to be applied. In some cases, patches also apply to middleware and database systems. Maintaining the security of web servers requires frequent reviews of security notices. Many security notices mandate the installation of a software patch to overcome security vulnerabilities. SAs and ISSOs should regularly check the vendor support web site for patches and information related to the web server software. All applicable security patches will be applied to the operating system and to the web server software. Security patches are deemed applicable if the product is installed, even if it is not used or is disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Obtain the list of patches that have been applied to OHS (e.g., $ORACLE_HOME/OPatch/opatch lsinventory). 2. In reviewing the list, also review the latest Oracle CPU at http://www.oracle.com/technetwork/topics/security/alerts-086861.html#CriticalPatchUpdates. Specifically, review the My Oracle Support note specified for Oracle Fusion Middleware to see whether there are patches available for Oracle HTTP Server 12.1.3. 3. If there are patches listed for Oracle HTTP Server 12.1.3 in the support note and they do not show in the list from Step 1 above, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221458`

### Rule: A private OHS list of CAs in a trust hierarchy must lead to an authorized DoD PKI Root CA.

**Rule ID:** `SV-221458r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A PKI certificate is a digital identifier that establishes the identity of an individual or a platform. A server that has a certificate provides users with third-party confirmation of authenticity. Most web browsers perform server authentication automatically; the user is notified only if the authentication fails. The authentication process between the server and the client is performed using the SSL/TLS protocol. Digital certificates are authenticated, issued, and managed by a trusted Certification Authority (CA). The use of a trusted certificate validation hierarchy is crucial to the ability to control access to the server and prevent unauthorized access. This hierarchy needs to lead to the DoD PKI Root CA or to an approved External Certificate Authority (ECA) or are required for the server to function.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Go to the location of the OHS keystores (e.g., cd $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/keystores). 2. For each wallet directory located there, do the following: a) Issue the command "$ORACLE_HOME/oracle_common/bin/orapki wallet display -wallet <wallet_directory>". b) Confirm that only the appropriate DoD Certificate Authorities are listed as Trusted Certificates and that the Identity Certificate has been issued by a DoD Certificate authority. 3. If any of the Trusted Certificates are not appropriate DoD Certificate Authorities or the Identity Certificate has not been issued by a DoD Certificate authority, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221459`

### Rule: OHS must have the ScoreBoardFile directive disabled.

**Rule ID:** `SV-221459r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ScoreBoardFile directive sets a file path which the server will use for Inter-Process Communication (IPC) among the Apache processes. If the directive is specified, then Apache will use the configured file for the inter-process communication. Therefore if it is specified it needs to be located in a secure directory. If the ScoreBoard file is placed in openly writable directory, other accounts could create a denial of service attack and prevent the server from starting by creating a file with the same name, and or users could monitor and disrupt the communication between the processes by reading and writing to the file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "ScoreBoardFile" directive at the server configuration scope. 3. If the "ScoreBoardFile" directive exists, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221460`

### Rule: The OHS document root directory must not be on a network share.

**Rule ID:** `SV-221460r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Sharing of web server content is a security risk when a web server is involved. Users accessing the share anonymously could experience privileged access to the content of such directories. Network sharable directories expose those directories and their contents to unnecessary access. Any unnecessary exposure increases the risk that someone could exploit that access and either compromises the web content or cause web server performance problems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "DocumentRoot" directive at the OHS server and virtual host configuration scopes. 3. If the directive value is used as a network share (e.g., ps -ef | grep nfs, ps -ef | grep smb, etc.), this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221461`

### Rule: The OHS server root directory must not be on a network share.

**Rule ID:** `SV-221461r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Sharing of the web server directory where the executables are stored is a security risk when a web server is involved. Users that have access to the share may not be administrative users. These users could make changes to the web server without going through proper change control or the users could inadvertently delete executables that are key to the proper operation of the web server. Any unnecessary exposure increases the risk that someone could exploit that access and either compromises the web server or cause web server performance problems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf. 2. Search for the "ServerRoot" directive at the OHS server configuration scope. 3. If the directive value is used as a network share (e.g., ps -ef | grep nfs, ps -ef | grep smb, etc.), this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221462`

### Rule: Symbolic links must not be used in the web content directory tree.

**Rule ID:** `SV-221462r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A symbolic link allows a file or a directory to be referenced using a symbolic name raising a potential hazard if symbolic linkage is made to a sensitive area. When web scripts are executed and symbolic links are allowed, the web user could be allowed to access locations on the web server that are outside the scope of the web document root or home directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "DocumentRoot" directive at the OHS server and virtual host configuration scopes. 3. Within the directory specified by each "DocumentRoot" directive, check recursively for any symbolic links (e.g., find . -type l -exec ls -ald {} \;). 4. If any symbolic links are found, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221463`

### Rule: OHS administration must be performed over a secure path or at the local console.

**Rule ID:** `SV-221463r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Logging into a web server remotely using an unencrypted protocol or service when performing updates and maintenance is a major risk. Data, such as user account, is transmitted in plaintext and can easily be compromised. When performing remote administrative tasks, a protocol or service that encrypts the communication channel must be used. An alternative to remote administration of the web server is to perform web server administration locally at the console. Local administration at the console implies physical access to the server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Check that if server administration is performed remotely, it will only be performed securely by system administrators. 2. Check that if OHS administration has been delegated, those users will be documented and approved by the ISSO. 3. Check that remote administration is in compliance with any requirements contained within the Unix Server STIGs and any applicable network STIGs. 4. Check that remote administration of any kind will be restricted to documented and authorized personnel and that all users performing remote administration are authenticated. 5. Check that all remote sessions will be encrypted and utilize FIPS 140-2 approved protocols. 6. If any of the above conditions are not met, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221464`

### Rule: OHS must not contain any robots.txt files.

**Rule ID:** `SV-221464r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Search engines are constantly at work on the Internet. Search engines are augmented by agents, often referred to as spiders or bots, which endeavor to capture and catalog web-site content. In turn, these search engines make the content they obtain and catalog available to any public web user. To request that a well behaved search engine not crawl and catalog a server, the web server may contain a file called robots.txt for each web site hosted. This file contains directories and files that the web server SA desires not be crawled or cataloged, but this file can also be used, by an attacker or poorly coded search engine, as a directory and file index to a site. This information may be used to reduce an attacker’s time searching and traversing the web site to find files that might be relevant. If information on hosted web sites needs to be protected from search engines and public view, other methods must be used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "DocumentRoot" directive at the OHS server and virtual host configuration scopes. 3. If the directive value specifies a directory containing a robots.txt file, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221465`

### Rule: OHS must prohibit anonymous FTP user access to interactive scripts.

**Rule ID:** `SV-221465r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The directories containing the CGI scripts, such as PERL, must not be accessible to anonymous users via FTP. This applies to all directories that contain scripts that can dynamically produce web pages in an interactive manner (i.e., scripts based upon user-provided input). Such scripts contain information that could be used to compromise a web service, access system resources, or deface a web site.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Check that all ftp access is authenticated, authorized, and secure. 2. If not, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221466`

### Rule: The OHS DocumentRoot directory must be in a separate partition from the OHS ServerRoot directory.

**Rule ID:** `SV-221466r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application partitioning enables an additional security measure by securing user traffic under one security context, while managing system and application files under another. Web content is accessible to an anonymous web user. For such an account to have access to system files of any type is a major security risk that is avoidable and desirable. Failure to partition the system files from the web site documents increases risk of attack via directory traversal, or impede web site availability due to drive space exhaustion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "DocumentRoot" directive at the OHS server and virtual host configuration scopes. 3. Search for the "ServerRoot" directive at the OHS server configuration scope. 4. If the "DocumentRoot" directive value specifies a directory on the same partition as the directory specified in the "ServerRoot" directive, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221467`

### Rule: The OHS DocumentRoot directory must be on a separate partition from OS root partition.

**Rule ID:** `SV-221467r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application partitioning enables an additional security measure by securing user traffic under one security context, while managing system and application files under another. Web content is accessible to an anonymous web user. For such an account to have access to system files of any type is a major security risk that is avoidable and desirable. Failure to partition the system files from the web site documents increases risk of attack via directory traversal, or impede web site availability due to drive space exhaustion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "DocumentRoot" directive at the OHS server and virtual host configuration scopes. 3. If the directory associated with the "DocumentRoot" directive is associated with the root partition, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221468`

### Rule: Remote authors or content providers must have all files scanned for viruses and malicious code before uploading files to the Document Root directory.

**Rule ID:** `SV-221468r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote web authors should not be able to upload files to the DocumentRoot directory structure without virus checking and checking for malicious or mobile code. A remote web user whose agency has a Memorandum of Agreement (MOA) with the hosting agency and has submitted a DoD form 2875 (System Authorization Access Request (SAAR)) or an equivalent document will be allowed to post files to a temporary location on the server. All posted files to this temporary location will be scanned for viruses and content checked for malicious or mobile code. Only files free of viruses and malicious or mobile code will be posted to the appropriate Document Root directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Check that any files uploaded to the OHS environment are checked for viruses, malicious code, and mobile code. 2. If there is not anti-virus software on the system with auto-protect enabled or if there is not a process in place to ensure all files being posted to the OHS sites are being scanned, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221469`

### Rule: A public OHS server must use TLS if authentication is required to host web sites.

**Rule ID:** `SV-221469r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Transport Layer Security (TLS) is optional for a public web server. However, if authentication is being performed, then the use of the TLS protocol is required. Without the use of TLS, the authentication data would be transmitted unencrypted and would become vulnerable to disclosure. Using TLS along with DoD PKI certificates for encryption of the authentication data protects the information from being accessed by all parties on the network. To further protect the authentication data, the web server must use a FIPS 140-2 approved TLS version and all non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 specifies the preferred configurations for government systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. Note: Does not apply to admin.conf. 2. Search for the following directive at the OHS server, virtual host, and/or directory configuration scopes: "SSLEngine" "SSLProtocol" "SSLWallet" 3. If any of these directives are omitted, this is a finding. 4. If "SSLEngine" is not set to "On", or "SSLProtocol" is not set to "TLSv1.2", this is a finding. 5. Validate that the folder specified in the "SSLWallet" directive exists. If the folder does not exist or contain a valid wallet, this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221470`

### Rule: OHS hosted web sites must utilize ports, protocols, and services according to PPSM guidelines.

**Rule ID:** `SV-221470r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Failure to comply with DoD ports, protocols, and services (PPS) requirements can result in compromise of enclave boundary protections and/or functionality of the automated information system (AIS). The ISSM will ensure web servers are configured to use only authorized PPS in accordance with the Network Infrastructure STIG, DoD Instruction 8551.1, Ports, Protocols, and Services Management (PPSM), and the associated Ports, Protocols, and Services (PPS) Assurance Category Assignments List.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "Listen" directive at the OHS server configuration scope. 3. If the "Listen" directive port specified is not "80" or "443", this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-221471`

### Rule: OHS must not have the directive PlsqlDatabasePassword set in clear text.

**Rule ID:** `SV-221471r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>OHS supports the use of the module mod_plsql, which allows applications to be hosted that are PL/SQL-based. To access the database, the module must have a valid username, password and database name. To keep the password from an attacker, the password must not be stored in plain text, but instead, obfuscated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., dads.conf) included in it with an editor. 2. Search for the "PlsqlDatabasePassword" directive. 3. If the directive is set in clear text, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221472`

### Rule: If WebLogic is not in use with OHS, OHS must have the include mod_wl_ohs.conf directive disabled at the server level.

**Rule ID:** `SV-221472r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If not using the WebLogic Web Server Proxy Plugin: 1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "include mod_wl_ohs.conf" directive at the OHS server configuration scope. 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000141-WSR-000075

**Group ID:** `V-221473`

### Rule: If mod_plsql is not in use with OHS, OHS must have the include moduleconf/* directive disabled.

**Rule ID:** `SV-221473r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can provide many features, services, and processes. Some of these may be deemed unnecessary or too unsecure to run on a production DoD system. The web server must provide the capability to disable, uninstall, or deactivate functionality and services that are deemed to be non-essential to the web server mission or can adversely impact server performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If not using mod_plsql: 1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "include moduleconf/*" directive at the OHS server configuration scope. Note: The complete line may be "include moduleconf/*.conf*". 3. If the directive exists and is not commented out, this is a finding.

## Group: SRG-APP-000172-WSR-000104

**Group ID:** `V-221474`

### Rule: OHS must have the LoadModule ossl_module directive enabled to encrypt passwords during transmission.

**Rule ID:** `SV-221474r961029_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Data used to authenticate, especially passwords, needs to be protected at all times, and encryption is the standard method for protecting authentication data during transmission. Data used to authenticate can be passed to and from the web server for many reasons. Examples include data passed from a user to the web server through an HTTPS connection for authentication, the web server authenticating to a backend database for data retrieval and posting, and the web server authenticating to a clustered web server manager for an update.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule ossl_module" directive at the OHS server configuration scope. 3. If the directive is omitted, this is a finding. 4. Validate that the file specified exists. If the file does not exist, this is a finding.

## Group: SRG-APP-000172-WSR-000104

**Group ID:** `V-221475`

### Rule: OHS must use FIPS modules to encrypt passwords during transmission.

**Rule ID:** `SV-221475r961029_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Data used to authenticate, especially passwords, needs to be protected at all times, and encryption is the standard method for protecting authentication data during transmission. Data used to authenticate can be passed to and from the web server for many reasons. Examples include data passed from a user to the web server through an HTTPS connection for authentication, the web server authenticating to a backend database for data retrieval and posting, and the web server authenticating to a clustered web server manager for an update.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/ssl.conf with an editor. 2. Search for the "SSLFIPS" directive at the OHS server configuration scope. 3. If the directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000172-WSR-000104

**Group ID:** `V-221476`

### Rule: OHS must have the SSLEngine, SSLProtocol, and SSLWallet directives enabled and configured to encrypt passwords during transmission.

**Rule ID:** `SV-221476r961029_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Data used to authenticate, especially passwords, needs to be protected at all times, and encryption is the standard method for protecting authentication data during transmission. Data used to authenticate can be passed to and from the web server for many reasons. Examples include data passed from a user to the web server through an HTTPS connection for authentication, the web server authenticating to a backend database for data retrieval and posting, and the web server authenticating to a clustered web server manager for an update.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. Note: Does not apply to admin.conf. 2. Search for the following directive at the OHS server, virtual host, and/or directory configuration scopes: "SSLEngine" "SSLProtocol" "SSLWallet" 3. If any of these directives are omitted, this is a finding. 4. If "SSLEngine" is not set to "On", or "SSLProtocol" is not set to "TLSv1.2", this is a finding. 5. Validate that the folder specified in the "SSLWallet" directive exists. If the folder does not exist or contain a valid wallet, this is a finding.

## Group: SRG-APP-000172-WSR-000104

**Group ID:** `V-221477`

### Rule: OHS must have the SSLCipherSuite directive enabled to encrypt passwords during transmission.

**Rule ID:** `SV-221477r961029_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Data used to authenticate, especially passwords, needs to be protected at all times, and encryption is the standard method for protecting authentication data during transmission. Data used to authenticate can be passed to and from the web server for many reasons. Examples include data passed from a user to the web server through an HTTPS connection for authentication, the web server authenticating to a backend database for data retrieval and posting, and the web server authenticating to a clustered web server manager for an update.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. 2. Search for the "SSLCipherSuite" directive at the OHS server, virtual host, and/or directory configuration scopes. 3. If the directive is omitted or set improperly, this is a finding.

## Group: SRG-APP-000175-WSR-000095

**Group ID:** `V-221478`

### Rule: OHS must have the LoadModule ossl_module directive enabled to perform RFC 5280-compliant certification path validation.

**Rule ID:** `SV-221478r961038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule ossl_module" directive at the OHS server configuration scope. 3. If the directive is omitted, this is a finding. 4. Validate that the file specified exists. If the file does not exist, this is a finding.

## Group: SRG-APP-000175-WSR-000095

**Group ID:** `V-221479`

### Rule: OHS must use FIPS modules to perform RFC 5280-compliant certification path validation.

**Rule ID:** `SV-221479r961038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/ssl.conf with an editor. 2. Search for the "SSLFIPS" directive at the OHS server configuration scope. 3. If the directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000175-WSR-000095

**Group ID:** `V-221480`

### Rule: OHS must have the SSLEngine, SSLProtocol, and SSLWallet directives enabled and configured to perform RFC 5280-compliant certification path validation.

**Rule ID:** `SV-221480r961038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. Note: Does not apply to admin.conf. 2. Search for the following directive at the OHS server, virtual host, and/or directory configuration scopes: "SSLEngine" "SSLProtocol" "SSLWallet" 3. If any of these directives are omitted, this is a finding. 4. If "SSLEngine" is not set to "On", or "SSLProtocol" is not set to "TLSv1.2", this is a finding. 5. Validate that the folder specified in the "SSLWallet" directive exists. If the folder does not exist or contain a valid wallet, this is a finding.

## Group: SRG-APP-000175-WSR-000095

**Group ID:** `V-221481`

### Rule: OHS must have the SSLCipherSuite directive enabled to perform RFC 5280-compliant certification path validation.

**Rule ID:** `SV-221481r961038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. 2. Search for the "SSLCipherSuite" directive at the OHS server, virtual host, and/or directory configuration scopes. 3. If the directive is omitted or set improperly, this is a finding.

## Group: SRG-APP-000175-WSR-000095

**Group ID:** `V-221482`

### Rule: OHS must have the SSLVerifyClient directive set within each SSL-enabled VirtualHost directive to perform RFC 5280-compliant certification path validation.

**Rule ID:** `SV-221482r961038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. 2. Search for the "SSLVerifyClient" directive at the OHS server, virtual host, and/or directory configuration scopes. 3. If this directive is omitted or set improperly, this is a finding.

## Group: SRG-APP-000175-WSR-000095

**Group ID:** `V-221483`

### Rule: OHS must have the SSLCARevocationFile and SSLCRLCheck directives within each SSL-enabled VirtualHost directive set to perform RFC 5280-compliant certification path validation when using single certification revocation.

**Rule ID:** `SV-221483r961038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. If using a single, certification revocation list file for revocation checks that is < 1 MB in size, open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. 2. Search for the "SSLCARevocationFile" and "SSLCRLCheck" directives at the OHS server and virtual host configuration scopes. 3. If these directives are omitted or set improperly, this is a finding.

## Group: SRG-APP-000175-WSR-000095

**Group ID:** `V-221484`

### Rule: OHS must have SSLCARevocationPath and SSLCRLCheck directives within each SSL-enabled VirtualHost directive set to perform RFC 5280-compliant certification path validation when using multiple certification revocation.

**Rule ID:** `SV-221484r961038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. If using multiple certificate revocation list files for revocation checks, open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. 2. Search for the "SSLCARevocationPath" and "SSLCRLCheck" directives at the OHS server and virtual host configuration scopes. 3. If these directives are omitted or set improperly, this is a finding.

## Group: SRG-APP-000175-WSR-000095

**Group ID:** `V-221485`

### Rule: OHS must be integrated with a tool such as Oracle Access Manager to enforce a client-side certificate revocation check through the OCSP protocol.

**Rule ID:** `SV-221485r961038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Check to see if a product such as Oracle Access Manager that could be used for authentication, could also provide OCSP validation. 2. If not, this is a finding.

## Group: SRG-APP-000179-WSR-000110

**Group ID:** `V-221486`

### Rule: OHS must have the LoadModule ossl_module directive enabled to meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance when encrypting stored data.

**Rule ID:** `SV-221486r961050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified, and cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised due to weak algorithms. FIPS 140-2 is the current standard for validating cryptographic modules and NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. The web server must provide FIPS-compliant encryption modules when storing encrypted data and configuration settings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule ossl_module" directive at the OHS server configuration scope. 3. If the directive is omitted, this is a finding. 4. Validate that the file specified exists. If the file does not exist, this is a finding.

## Group: SRG-APP-000179-WSR-000110

**Group ID:** `V-221487`

### Rule: OHS must have the SSLFIPS directive enabled to meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance when encrypting stored data.

**Rule ID:** `SV-221487r961050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified, and cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised due to weak algorithms. FIPS 140-2 is the current standard for validating cryptographic modules and NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. The web server must provide FIPS-compliant encryption modules when storing encrypted data and configuration settings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/ssl.conf with an editor. 2. Search for the "SSLFIPS" directive at the OHS server configuration scope. 3. If the directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000179-WSR-000110

**Group ID:** `V-221488`

### Rule: OHS must have the SSLEngine, SSLProtocol, and SSLWallet directives enabled to meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance when encrypting stored data.

**Rule ID:** `SV-221488r961050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified, and cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised due to weak algorithms. FIPS 140-2 is the current standard for validating cryptographic modules and NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. The web server must provide FIPS-compliant encryption modules when storing encrypted data and configuration settings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. Note: Does not apply to admin.conf. 2. Search for the following directive at the OHS server, virtual host, and/or directory configuration scopes: "SSLEngine" "SSLProtocol" "SSLWallet" 3. If any of these directives are omitted, this is a finding. 4. If "SSLEngine" is not set to "On", or "SSLProtocol" is not set to "TLSv1.2", this is a finding. 5. Validate that the folder specified in the "SSLWallet" directive exists. If the folder does not exist or contain a valid wallet, this is a finding.

## Group: SRG-APP-000179-WSR-000110

**Group ID:** `V-221489`

### Rule: OHS must have the SSLCipherSuite directive enabled to meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance when encrypting stored data.

**Rule ID:** `SV-221489r961050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified, and cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised due to weak algorithms. FIPS 140-2 is the current standard for validating cryptographic modules and NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. The web server must provide FIPS-compliant encryption modules when storing encrypted data and configuration settings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. 2. Search for the "SSLCipherSuite" directive at the OHS server, virtual host, and/or directory configuration scopes. 3. If the directive is omitted or set improperly, this is a finding.

## Group: SRG-APP-000179-WSR-000111

**Group ID:** `V-221490`

### Rule: OHS must have the LoadModule ossl_module directive enabled to meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance for such authentication.

**Rule ID:** `SV-221490r961050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified and cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised due to weak algorithms. FIPS 140-2 is the current standard for validating cryptographic modules and NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. The web server must provide FIPS-compliant encryption modules when authenticating users and processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule ossl_module" directive at the OHS server configuration scope. 3. If the directive is omitted, this is a finding. 4. Validate that the file specified exists. If the file does not exist, this is a finding.

## Group: SRG-APP-000179-WSR-000111

**Group ID:** `V-221491`

### Rule: OHS must have the SSLFIPS directive enabled to meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance for such authentication.

**Rule ID:** `SV-221491r961050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified and cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised due to weak algorithms. FIPS 140-2 is the current standard for validating cryptographic modules and NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. The web server must provide FIPS-compliant encryption modules when authenticating users and processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/ssl.conf with an editor. 2. Search for the "SSLFIPS" directive at the OHS server configuration scope. 3. If the directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000179-WSR-000111

**Group ID:** `V-221492`

### Rule: OHS must have the SSLEngine, SSLProtocol, and SSLWallet directives enabled and configured to meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance for such authentication.

**Rule ID:** `SV-221492r961050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified and cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised due to weak algorithms. FIPS 140-2 is the current standard for validating cryptographic modules and NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. The web server must provide FIPS-compliant encryption modules when authenticating users and processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. Note: Does not apply to admin.conf. 2. Search for the following directive at the OHS server, virtual host, and/or directory configuration scopes: "SSLEngine" "SSLProtocol" "SSLWallet" 3. If any of these directives are omitted, this is a finding. 4. If "SSLEngine" is not set to "On", or "SSLProtocol" is not set to "TLSv1.2", this is a finding. 5. Validate that the folder specified in the "SSLWallet" directive exists. If the folder does not exist or contain a valid wallet, this is a finding.

## Group: SRG-APP-000179-WSR-000111

**Group ID:** `V-221493`

### Rule: OHS must have the SSLCipherSuite directive enabled to meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance for such authentication.

**Rule ID:** `SV-221493r961050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified and cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised due to weak algorithms. FIPS 140-2 is the current standard for validating cryptographic modules and NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. The web server must provide FIPS-compliant encryption modules when authenticating users and processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. 2. Search for the "SSLCipherSuite" directive at the OHS server, virtual host, and/or directory configuration scopes. 3. If the directive is omitted or set improperly, this is a finding.

## Group: SRG-APP-000206-WSR-000128

**Group ID:** `V-221494`

### Rule: OHS utilizing mobile code must meet DoD-defined mobile code requirements.

**Rule ID:** `SV-221494r961083_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Mobile code in hosted applications allows the developer to add functionality and displays to hosted applications that are fluid, as opposed to a static web page. The data presentation becomes more appealing to the user, is easier to analyze, and navigation through the hosted application and data is much less complicated. Some mobile code technologies in use in today's applications are: Java, JavaScript, ActiveX, PDF, Postscript, Shockwave movies, Flash animations, and VBScript. The DoD has created policies that define the usage of mobile code on DoD systems. The usage restrictions and implementation guidance apply to both the selection and use of mobile code installed on organizational servers and mobile code downloaded and executed on individual workstations. The web server may host applications that contain mobile code and therefore, must meet the DoD-defined requirements regarding the deployment and/or use of mobile code. This includes digitally signing applets in order to provide a means for the client to establish application authenticity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Check to see whether OHS is hosting any applications that use mobile code. 2. If so, check that the mobile code follows DoD policies regarding the acquisition, development, and/or use of mobile code. 3. If not, this is a finding.

## Group: SRG-APP-000211-WSR-000030

**Group ID:** `V-221495`

### Rule: OHS accounts accessing the directory tree, the shell, or other operating system functions and utilities must only be administrative accounts.

**Rule ID:** `SV-221495r961095_rule`
**Severity:** high

**Description:**
<VulnDiscussion>As a rule, accounts on a web server are to be kept to a minimum. Only administrators, web managers, developers, auditors, and web authors require accounts on the machine hosting the web server. The resources to which these accounts have access must also be closely monitored and controlled. Only the system administrator needs access to all the system's capabilities, while the web administrator and associated staff require access and control of the web content and web server configuration files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Get list of OS accounts, with associated privileges, from System Administrator. 2. Confirm that all accounts and privileges are needed and documented. 3. If not, this is a finding.

## Group: SRG-APP-000233-WSR-000146

**Group ID:** `V-221496`

### Rule: OHS must have the DocumentRoot directive set to a separate partition from the OHS system files.

**Rule ID:** `SV-221496r961131_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server is used to deliver content on the request of a client. The content delivered to a client must be controlled, allowing only hosted application files to be accessed and delivered. To allow a client access to system files of any type is a major security risk that is entirely avoidable. Obtaining such access is the goal of directory traversal and URL manipulation vulnerabilities. To facilitate such access by misconfiguring the web document (home) directory is a serious error. In addition, having the path on the same drive as the system folder compounds potential attacks such as drive space exhaustion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "DocumentRoot" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding. 4. Validate that the directory specified exists. If the directory does not exist, this is a finding.

## Group: SRG-APP-000233-WSR-000146

**Group ID:** `V-221497`

### Rule: OHS must have the Directory directive accompanying the DocumentRoot directive set to a separate partition from the OHS system files.

**Rule ID:** `SV-221497r961131_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server is used to deliver content on the request of a client. The content delivered to a client must be controlled, allowing only hosted application files to be accessed and delivered. To allow a client access to system files of any type is a major security risk that is entirely avoidable. Obtaining such access is the goal of directory traversal and URL manipulation vulnerabilities. To facilitate such access by misconfiguring the web document (home) directory is a serious error. In addition, having the path on the same drive as the system folder compounds potential attacks such as drive space exhaustion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for a "<Directory ${ORACLE_INSTANCE}/config/fmwconfig/components/${COMPONENT_TYPE}/instances/${COMPONENT_NAME}/htdocs">" directive or "<Directory>" directive pointing to the location of the directory specified in the "DocumentRoot" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set improperly, this is a finding. 4. Validate that the directory specified exists. If the directory does not exist, this is a finding.

## Group: SRG-APP-000246-WSR-000149

**Group ID:** `V-221498`

### Rule: OHS must have the Timeout directive properly set to restrict the ability of users to launch Denial of Service (DoS) attacks against other information systems or networks.

**Rule ID:** `SV-221498r961152_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can limit the ability of the web server being used in a DoS attack through several methods. The methods employed will depend upon the hosted applications and their resource needs for proper operation. An example setting that could be used to limit the ability of the web server being used in a DoS attack is bandwidth throttling.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "Timeout" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or set greater than 30, this is a finding. Note: This vulnerability can be documented locally with the ISSM/ISSO if the site has operational reasons for the use of a higher value.

## Group: SRG-APP-000246-WSR-000149

**Group ID:** `V-221499`

### Rule: OHS must have the KeepAlive directive properly set to restrict the ability of users to launch Denial of Service (DoS) attacks against other information systems or networks.

**Rule ID:** `SV-221499r961152_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can limit the ability of the web server being used in a DoS attack through several methods. The methods employed will depend upon the hosted applications and their resource needs for proper operation. An example setting that could be used to limit the ability of the web server being used in a DoS attack is bandwidth throttling.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "KeepAlive" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000246-WSR-000149

**Group ID:** `V-221500`

### Rule: OHS must have the KeepAliveTimeout properly set to restrict the ability of users to launch Denial of Service (DoS) attacks against other information systems or networks.

**Rule ID:** `SV-221500r961152_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can limit the ability of the web server being used in a DoS attack through several methods. The methods employed will depend upon the hosted applications and their resource needs for proper operation. An example setting that could be used to limit the ability of the web server being used in a DoS attack is bandwidth throttling.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "KeepAliveTimeout" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or is set greater than 5, this is a finding.

## Group: SRG-APP-000246-WSR-000149

**Group ID:** `V-221501`

### Rule: OHS must have the MaxKeepAliveRequests directive properly set to restrict the ability of users to launch Denial of Service (DoS) attacks against other information systems or networks.

**Rule ID:** `SV-221501r961152_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can limit the ability of the web server being used in a DoS attack through several methods. The methods employed will depend upon the hosted applications and their resource needs for proper operation. An example setting that could be used to limit the ability of the web server being used in a DoS attack is bandwidth throttling.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "MaxKeepAliveRequests" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or is set greater than 500, this is a finding.

## Group: SRG-APP-000246-WSR-000149

**Group ID:** `V-221502`

### Rule: OHS must have the ListenBacklog properly set to restrict the ability of users to launch Denial of Service (DoS) attacks against other information systems or networks.

**Rule ID:** `SV-221502r961152_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can limit the ability of the web server being used in a DoS attack through several methods. The methods employed will depend upon the hosted applications and their resource needs for proper operation. An example setting that could be used to limit the ability of the web server being used in a DoS attack is bandwidth throttling.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "ListenBacklog" directive at the OHS server configuration scope. 3. If the directive is omitted or set less than the value of the Maximum Syn Connection Backlog network parameter of the OS, this is a finding.

## Group: SRG-APP-000246-WSR-000149

**Group ID:** `V-221503`

### Rule: OHS must have the LimitRequestBody directive set to restrict the ability of users to launch Denial of Service (DoS) attacks against other information systems or networks.

**Rule ID:** `SV-221503r961152_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can limit the ability of the web server being used in a DoS attack through several methods. The methods employed will depend upon the hosted applications and their resource needs for proper operation. An example setting that could be used to limit the ability of the web server being used in a DoS attack is bandwidth throttling.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "LimitRequestBody" directive at the OHS server, virtual host, and directory configuration scopes. 3. If the directive is omitted or is set greater than 10240, this is a finding. Note: This vulnerability can be documented locally with the ISSM/ISSO if the site has operational reasons for the use of a higher value.

## Group: SRG-APP-000246-WSR-000149

**Group ID:** `V-221504`

### Rule: OHS must have the LimitRequestFields directive set to restrict the ability of users to launch Denial of Service (DoS) attacks against other information systems or networks.

**Rule ID:** `SV-221504r961152_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can limit the ability of the web server being used in a DoS attack through several methods. The methods employed will depend upon the hosted applications and their resource needs for proper operation. An example setting that could be used to limit the ability of the web server being used in a DoS attack is bandwidth throttling.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "LimitRequestFields" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or is set greater than 40, this is a finding. Note: This vulnerability can be documented locally with the ISSM/ISSO if the site has operational reasons for the use of a higher value.

## Group: SRG-APP-000246-WSR-000149

**Group ID:** `V-221505`

### Rule: OHS must have the LimitRequestFieldSize directive set to restrict the ability of users to launch Denial of Service (DoS) attacks against other information systems or networks.

**Rule ID:** `SV-221505r961152_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can limit the ability of the web server being used in a DoS attack through several methods. The methods employed will depend upon the hosted applications and their resource needs for proper operation. An example setting that could be used to limit the ability of the web server being used in a DoS attack is bandwidth throttling.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "LimitRequestFieldSize" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or is set greater than 1024, this is a finding. Note: This vulnerability can be documented locally with the ISSM/ISSO if the site has operational reasons for the use of a higher value.

## Group: SRG-APP-000246-WSR-000149

**Group ID:** `V-221506`

### Rule: OHS must have the LimitRequestLine directive set to restrict the ability of users to launch Denial of Service (DoS) attacks against other information systems or networks.

**Rule ID:** `SV-221506r961152_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can limit the ability of the web server being used in a DoS attack through several methods. The methods employed will depend upon the hosted applications and their resource needs for proper operation. An example setting that could be used to limit the ability of the web server being used in a DoS attack is bandwidth throttling.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "LimitRequestLine" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or is set greater than 512, this is a finding. Note: This vulnerability can be documented locally with the ISSM/ISSO if the site has operational reasons for the use of a higher value.

## Group: SRG-APP-000246-WSR-000149

**Group ID:** `V-221507`

### Rule: OHS must have the LimitXMLRequestBody directive set to restrict the ability of users to launch Denial of Service (DoS) attacks against other information systems or networks.

**Rule ID:** `SV-221507r961152_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can limit the ability of the web server being used in a DoS attack through several methods. The methods employed will depend upon the hosted applications and their resource needs for proper operation. An example setting that could be used to limit the ability of the web server being used in a DoS attack is bandwidth throttling.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "LimitXMLRequestBody" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted or is set greater than 10240, this is a finding. Note: This vulnerability can be documented locally with the ISSM/ISSO if the site has operational reasons for the use of a higher value.

## Group: SRG-APP-000246-WSR-000149

**Group ID:** `V-221508`

### Rule: OHS must have the LimitInternalRecursion directive set to restrict the ability of users to launch Denial of Service (DoS) attacks against other information systems or networks.

**Rule ID:** `SV-221508r961152_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can limit the ability of the web server being used in a DoS attack through several methods. The methods employed will depend upon the hosted applications and their resource needs for proper operation. An example setting that could be used to limit the ability of the web server being used in a DoS attack is bandwidth throttling.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "LimitInternalRecursion" directive at the server, virtual host, and directory configuration scopes. 3. If the "LimitInternalRecursion" directive is omitted or is set greater than 55, this is a finding.

## Group: SRG-APP-000427-WSR-000186

**Group ID:** `V-221513`

### Rule: OHS must have the LoadModule ossl_module directive enabled so SSL requests can be processed with client certificates only issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs).

**Rule ID:** `SV-221513r965407_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-DoD approved PKIs have not been evaluated to ensure that they have security controls and identity vetting procedures in place which are sufficient for DoD systems to rely on the identity asserted in the certificate. PKIs lacking sufficient security controls and identity vetting procedures risk being compromised and issuing certificates that enable adversaries to impersonate legitimate users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule ossl_module" directive at the OHS server configuration scope. 3. If the directive is omitted, this is a finding. 4. Validate that the file specified exists. If the file does not exist, this is a finding.

## Group: SRG-APP-000427-WSR-000186

**Group ID:** `V-221514`

### Rule: OHS must have the SSLFIPS directive enabled so SSL requests can be processed with client certificates only issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs).

**Rule ID:** `SV-221514r965407_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-DoD approved PKIs have not been evaluated to ensure that they have security controls and identity vetting procedures in place which are sufficient for DoD systems to rely on the identity asserted in the certificate. PKIs lacking sufficient security controls and identity vetting procedures risk being compromised and issuing certificates that enable adversaries to impersonate legitimate users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/ssl.conf with an editor. 2. Search for the "SSLFIPS" directive at the OHS server configuration scope. 3. If the directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000427-WSR-000186

**Group ID:** `V-221515`

### Rule: OHS must have the SSLEngine, SSLProtocol, and SSLWallet directives enabled so SSL requests can be processed with client certificates only issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs).

**Rule ID:** `SV-221515r965407_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-DoD approved PKIs have not been evaluated to ensure that they have security controls and identity vetting procedures in place which are sufficient for DoD systems to rely on the identity asserted in the certificate. PKIs lacking sufficient security controls and identity vetting procedures risk being compromised and issuing certificates that enable adversaries to impersonate legitimate users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. Note: Does not apply to admin.conf. 2. Search for the following directive at the OHS server, virtual host, and/or directory configuration scopes: "SSLEngine" "SSLProtocol" "SSLWallet" 3. If any of these directives are omitted, this is a finding. 4. If "SSLEngine" is not set to "on", or "SSLProtocol" is not set to TLSv1.2, this is a finding. 5. Validate that the folder specified in the "SSLWallet" directive exists. If the folder does not exist or contain a valid wallet, this is a finding.

## Group: SRG-APP-000427-WSR-000186

**Group ID:** `V-221516`

### Rule: OHS must have the SSLCipherSuite directive enabled so SSL requests can be processed with client certificates only issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs).

**Rule ID:** `SV-221516r965407_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-DoD approved PKIs have not been evaluated to ensure that they have security controls and identity vetting procedures in place which are sufficient for DoD systems to rely on the identity asserted in the certificate. PKIs lacking sufficient security controls and identity vetting procedures risk being compromised and issuing certificates that enable adversaries to impersonate legitimate users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. 2. Search for the "SSLCipherSuite" directive at the OHS server, virtual host, and/or directory configuration scopes. 3. If the directive is omitted or set improperly, this is a finding.

## Group: SRG-APP-000427-WSR-000186

**Group ID:** `V-221517`

### Rule: OHS must have the SSLVerifyClient directive enabled to only accept client certificates issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs).

**Rule ID:** `SV-221517r965407_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-DoD approved PKIs have not been evaluated to ensure that they have security controls and identity vetting procedures in place which are sufficient for DoD systems to rely on the identity asserted in the certificate. PKIs lacking sufficient security controls and identity vetting procedures risk being compromised and issuing certificates that enable adversaries to impersonate legitimate users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. 2. Search for the "SSLVerifyClient" directive at the OHS server, virtual host, and/or directory configuration scopes. 3. If this directive is omitted or is not set to "require", this is a finding.

## Group: SRG-APP-000427-WSR-000186

**Group ID:** `V-221518`

### Rule: OHS must use wallets that have only DoD certificate authorities defined.

**Rule ID:** `SV-221518r965407_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-DoD approved PKIs have not been evaluated to ensure that they have security controls and identity vetting procedures in place which are sufficient for DoD systems to rely on the identity asserted in the certificate. PKIs lacking sufficient security controls and identity vetting procedures risk being compromised and issuing certificates that enable adversaries to impersonate legitimate users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Go to the location of the OHS keystores (e.g., cd $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/keystores). 2. For each wallet directory located there, do the following: a) Issue the command "$ORACLE_HOME/oracle_common/bin/orapki wallet display -wallet <wallet_directory>". b) Confirm that only the appropriate DoD Certificate Authorities are listed as Trusted Certificates. 3. If any of the Trusted Certificates are not appropriate DoD Certificate Authorities, this is a finding.

## Group: SRG-APP-000435-WSR-000148

**Group ID:** `V-221519`

### Rule: OHS must be tuned to handle the operational requirements of the hosted application.

**Rule ID:** `SV-221519r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A Denial of Service (DoS) can occur when the web server is so overwhelmed that it can no longer respond to additional requests. A web server not properly tuned may become overwhelmed and cause a DoS condition even with expected traffic from users. To avoid a DoS, the web server must be tuned to handle the expected traffic for the hosted applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Check to see if the following directives have been set appropriately for the server and application: MaxClients MPM Module -worker (StartServers, MinSpareThreads, MaxSpareThreads, ThreadsPerChild) Timeout KeepAlive KeepAliveTimeout MaxKeepAliveRequests ListenBacklog LimitRequestBody LimitRequestFields LimitRequestFieldSize LimitRequestLine LimitXMLRequestBody LimitInternalRecursion 2. If the above directives have not been set to address the specific needs of the web server and applications, this is a finding.

## Group: SRG-APP-000439-WSR-000151

**Group ID:** `V-221520`

### Rule: OHS must have the LoadModule ossl_module directive enabled to prevent unauthorized disclosure of information during transmission.

**Rule ID:** `SV-221520r961632_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that the web server take measures to employ some form of cryptographic mechanism in order to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS). Transmission of data can take place between the web server and a large number of devices/applications external to the web server. Examples are a web client used by a user, a backend database, an audit server, or other web servers in a web cluster. If data is transmitted unencrypted, the data then becomes vulnerable to disclosure. The disclosure may reveal user identifier/password combinations, website code revealing business logic, or other user personal information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule ossl_module" directive at the OHS server configuration scope. 3. If the directive is omitted, this is a finding. 4. Validate that the file specified exists. If the file does not exist, this is a finding.

## Group: SRG-APP-000439-WSR-000151

**Group ID:** `V-221521`

### Rule: OHS must have the SSLFIPS directive enabled to prevent unauthorized disclosure of information during transmission.

**Rule ID:** `SV-221521r961632_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that the web server take measures to employ some form of cryptographic mechanism in order to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS). Transmission of data can take place between the web server and a large number of devices/applications external to the web server. Examples are a web client used by a user, a backend database, an audit server, or other web servers in a web cluster. If data is transmitted unencrypted, the data then becomes vulnerable to disclosure. The disclosure may reveal user identifier/password combinations, website code revealing business logic, or other user personal information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/ssl.conf with an editor. 2. Search for the "SSLFIPS" directive at the OHS server configuration scope. 3. If the directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000439-WSR-000151

**Group ID:** `V-221522`

### Rule: OHS must have the SSLEngine, SSLProtocol, SSLWallet directives enabled and configured to prevent unauthorized disclosure of information during transmission.

**Rule ID:** `SV-221522r961632_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that the web server take measures to employ some form of cryptographic mechanism in order to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS). Transmission of data can take place between the web server and a large number of devices/applications external to the web server. Examples are a web client used by a user, a backend database, an audit server, or other web servers in a web cluster. If data is transmitted unencrypted, the data then becomes vulnerable to disclosure. The disclosure may reveal user identifier/password combinations, website code revealing business logic, or other user personal information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. Note: Does not apply to admin.conf. 2. Search for the following directive at the OHS server, virtual host, and/or directory configuration scopes: "SSLEngine" "SSLProtocol" "SSLWallet" 3. If any of these directives are omitted, this is a finding. 4. If "SSLEngine" is not set to "On", or "SSLProtocol" is not set to "TLSv1.2", this is a finding. 5. Validate that the folder specified in the "SSLWallet" directive exists. If the folder does not exist or contain a valid wallet, this is a finding.

## Group: SRG-APP-000439-WSR-000151

**Group ID:** `V-221523`

### Rule: OHS must have the SSLCipherSuite directive enabled to prevent unauthorized disclosure of information during transmission.

**Rule ID:** `SV-221523r961632_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that the web server take measures to employ some form of cryptographic mechanism in order to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS). Transmission of data can take place between the web server and a large number of devices/applications external to the web server. Examples are a web client used by a user, a backend database, an audit server, or other web servers in a web cluster. If data is transmitted unencrypted, the data then becomes vulnerable to disclosure. The disclosure may reveal user identifier/password combinations, website code revealing business logic, or other user personal information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. 2. Search for the "SSLCipherSuite" directive at the OHS server, virtual host, and/or directory configuration scopes. 3. If the directive is omitted or set improperly, this is a finding.

## Group: SRG-APP-000439-WSR-000151

**Group ID:** `V-221524`

### Rule: If using the WebLogic Web Server Proxy Plugin and configuring end-to-end SSL, OHS must have the SecureProxy directive enabled to prevent unauthorized disclosure of information during transmission.

**Rule ID:** `SV-221524r961632_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that the web server take measures to employ some form of cryptographic mechanism in order to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS). Transmission of data can take place between the web server and a large number of devices/applications external to the web server. Examples are a web client used by a user, a backend database, an audit server, or other web servers in a web cluster. If data is transmitted unencrypted, the data then becomes vulnerable to disclosure. The disclosure may reveal user identifier/password combinations, website code revealing business logic, or other user personal information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using the WebLogic Web Server Proxy Plugin and configuring end-to-end SSL: 1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that contains an SSL-enabled "<VirtualHost>" directive. 2. Search for the "SecureProxy" directive within an "<IfModule weblogic_module>" at the virtual host configuration scope. 3. If the directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000439-WSR-000151

**Group ID:** `V-221525`

### Rule: OHS must have the WLSSLWallet directive enabled to prevent unauthorized disclosure of information during transmission.

**Rule ID:** `SV-221525r961632_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that the web server take measures to employ some form of cryptographic mechanism in order to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS). Transmission of data can take place between the web server and a large number of devices/applications external to the web server. Examples are a web client used by a user, a backend database, an audit server, or other web servers in a web cluster. If data is transmitted unencrypted, the data then becomes vulnerable to disclosure. The disclosure may reveal user identifier/password combinations, website code revealing business logic, or other user personal information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using the WebLogic Web Server Proxy Plugin and configuring end-to-end SSL: 1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that contains an SSL-enabled "<VirtualHost>" directive. 2. Search for the "WLSSLWallet" directive within an "<IfModule weblogic_module>" at the virtual host configuration scope. 3. If the directive is omitted or is not set to a valid wallet folder, this is a finding.

## Group: SRG-APP-000439-WSR-000151

**Group ID:** `V-221526`

### Rule: If using the WebLogic Web Server Proxy Plugin and configuring end-to-end SSL, OHS must have the WebLogicSSLVersion directive enabled to prevent unauthorized disclosure of information during transmission.

**Rule ID:** `SV-221526r961632_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that the web server take measures to employ some form of cryptographic mechanism in order to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS). Transmission of data can take place between the web server and a large number of devices/applications external to the web server. Examples are a web client used by a user, a backend database, an audit server, or other web servers in a web cluster. If data is transmitted unencrypted, the data then becomes vulnerable to disclosure. The disclosure may reveal user identifier/password combinations, website code revealing business logic, or other user personal information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using the WebLogic Web Server Proxy Plugin and configuring end-to-end SSL: 1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that contains an SSL-enabled "<VirtualHost>" directive. 2. Search for the "WebLogicSSLVersion" directive within an "<IfModule weblogic_module>" at the virtual host configuration scope. 3. If the directive is omitted or is not set to "TLSv1.2", this is a finding.

## Group: SRG-APP-000439-WSR-000151

**Group ID:** `V-221527`

### Rule: If using the WebLogic Web Server Proxy Plugin and configuring SSL termination at OHS, OHS must have the WLProxySSL directive enabled to prevent unauthorized disclosure of information during transmission.

**Rule ID:** `SV-221527r961632_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that the web server take measures to employ some form of cryptographic mechanism in order to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS). Transmission of data can take place between the web server and a large number of devices/applications external to the web server. Examples are a web client used by a user, a backend database, an audit server, or other web servers in a web cluster. If data is transmitted unencrypted, the data then becomes vulnerable to disclosure. The disclosure may reveal user identifier/password combinations, website code revealing business logic, or other user personal information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using the WebLogic Web Server Proxy Plugin and configuring SSL termination at OHS: 1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that contains an SSL-enabled "<VirtualHost>" directive. 2. Search for the "WLProxySSL" directive within an "<IfModule weblogic_module>" at the virtual host configuration scope. 3. If the directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000439-WSR-000156

**Group ID:** `V-221528`

### Rule: OHS must have the LoadModule ossl_module directive enabled to maintain the confidentiality of controlled information during transmission through the use of an approved TLS version.

**Rule ID:** `SV-221528r961632_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Transport Layer Security (TLS) is a required transmission protocol for a web server hosting controlled information. The use of TLS provides confidentiality of data in transit between the web server and client. FIPS 140-2 approved TLS versions must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 defines the approved TLS versions for government applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule ossl_module" directive at the OHS server configuration scope. 3. If the directive is omitted, this is a finding. 4. Validate that the file specified exists. If the file does not exist, this is a finding.

## Group: SRG-APP-000439-WSR-000156

**Group ID:** `V-221529`

### Rule: OHS must have the SSLFIPS directive enabled to maintain the confidentiality of controlled information during transmission through the use of an approved TLS version.

**Rule ID:** `SV-221529r961632_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Transport Layer Security (TLS) is a required transmission protocol for a web server hosting controlled information. The use of TLS provides confidentiality of data in transit between the web server and client. FIPS 140-2 approved TLS versions must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 defines the approved TLS versions for government applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/ssl.conf with an editor. 2. Search for the "SSLFIPS" directive at the OHS server configuration scope. 3. If the directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000439-WSR-000156

**Group ID:** `V-221530`

### Rule: OHS must have the SSLEngine, SSLProtocol, and SSLWallet directives enabled and configured to maintain the confidentiality of controlled information during transmission through the use of an approved TLS version.

**Rule ID:** `SV-221530r961632_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Transport Layer Security (TLS) is a required transmission protocol for a web server hosting controlled information. The use of TLS provides confidentiality of data in transit between the web server and client. FIPS 140-2 approved TLS versions must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 defines the approved TLS versions for government applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. Note: Does not apply to admin.conf. 2. Search for the following directive at the OHS server, virtual host, and/or directory configuration scopes: "SSLEngine" "SSLProtocol" "SSLWallet" 3. If any of these directives are omitted, this is a finding. 4. If "SSLEngine" is not set to "On", or "SSLProtocol" is not set to "TLSv1.2", this is a finding. 5. Validate that the folder specified in the "SSLWallet" directive exists. If the folder does not exist or contain a valid wallet, this is a finding.

## Group: SRG-APP-000439-WSR-000156

**Group ID:** `V-221531`

### Rule: OHS must have the SSLCipherSuite directive enabled to maintain the confidentiality of controlled information during transmission through the use of an approved TLS version.

**Rule ID:** `SV-221531r961632_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Transport Layer Security (TLS) is a required transmission protocol for a web server hosting controlled information. The use of TLS provides confidentiality of data in transit between the web server and client. FIPS 140-2 approved TLS versions must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 defines the approved TLS versions for government applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. 2. Search for the "SSLCipherSuite" directive at the OHS server, virtual host, and/or directory configuration scopes. 3. If the directive is omitted or set improperly, this is a finding.

## Group: SRG-APP-000441-WSR-000181

**Group ID:** `V-221532`

### Rule: OHS must have the LoadModule ossl_module directive enabled to maintain the confidentiality and integrity of information during preparation for transmission.

**Rule ID:** `SV-221532r961638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. An example of this would be an SMTP queue. This queue may be added to a web server through an SMTP module to enhance error reporting or to allow developers to add SMTP functionality to their applications. Any modules used by the web server that queue data before transmission must maintain the confidentiality and integrity of the information before the data is transmitted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule ossl_module" directive at the OHS server configuration scope. 3. If the directive is omitted, this is a finding. 4. Validate that the file specified exists. If the file does not exist, this is a finding.

## Group: SRG-APP-000441-WSR-000181

**Group ID:** `V-221533`

### Rule: OHS must have the SSLFIPS directive enabled to maintain the confidentiality and integrity of information during preparation for transmission.

**Rule ID:** `SV-221533r961638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. An example of this would be an SMTP queue. This queue may be added to a web server through an SMTP module to enhance error reporting or to allow developers to add SMTP functionality to their applications. Any modules used by the web server that queue data before transmission must maintain the confidentiality and integrity of the information before the data is transmitted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/ssl.conf with an editor. 2. Search for the "SSLFIPS" directive at the OHS server configuration scope. 3. If the directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000441-WSR-000181

**Group ID:** `V-221534`

### Rule: OHS must have the SSLEngine, SSLProtocol, and SSLWallet directives enabled and configured to maintain the confidentiality and integrity of information during preparation for transmission.

**Rule ID:** `SV-221534r961638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. An example of this would be an SMTP queue. This queue may be added to a web server through an SMTP module to enhance error reporting or to allow developers to add SMTP functionality to their applications. Any modules used by the web server that queue data before transmission must maintain the confidentiality and integrity of the information before the data is transmitted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. Note: Does not apply to admin.conf. 2. Search for the following directive at the OHS server, virtual host, and/or directory configuration scopes: "SSLEngine" "SSLProtocol" "SSLWallet" 3. If any of these directives are omitted, this is a finding. 4. If "SSLEngine" is not set to "On", or "SSLProtocol" is not set to "TLSv1.2", this is a finding. 5. Validate that the folder specified in the "SSLWallet" directive exists. If the folder does not exist or contain a valid wallet, this is a finding.

## Group: SRG-APP-000441-WSR-000181

**Group ID:** `V-221535`

### Rule: OHS must have the SSLCipherSuite directive enabled to maintain the confidentiality and integrity of information during preparation for transmission.

**Rule ID:** `SV-221535r961638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. An example of this would be an SMTP queue. This queue may be added to a web server through an SMTP module to enhance error reporting or to allow developers to add SMTP functionality to their applications. Any modules used by the web server that queue data before transmission must maintain the confidentiality and integrity of the information before the data is transmitted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. 2. Search for the "SSLCipherSuite" directive at the OHS server, virtual host, and/or directory configuration scopes. 3. If the directive is omitted or set improperly, this is a finding.

## Group: SRG-APP-000441-WSR-000181

**Group ID:** `V-221536`

### Rule: If using the WebLogic Web Server Proxy Plugin and configuring end-to-end SSL, OHS must have the SecureProxy directive enabled to maintain the confidentiality and integrity of information during preparation for transmission.

**Rule ID:** `SV-221536r961638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. An example of this would be an SMTP queue. This queue may be added to a web server through an SMTP module to enhance error reporting or to allow developers to add SMTP functionality to their applications. Any modules used by the web server that queue data before transmission must maintain the confidentiality and integrity of the information before the data is transmitted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using the WebLogic Web Server Proxy Plugin and configuring end-to-end SSL: 1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that contains an SSL-enabled "<VirtualHost>" directive. 2. Search for the "SecureProxy" directive within an "<IfModule weblogic_module>" at the virtual host configuration scope. 3. If the directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000441-WSR-000181

**Group ID:** `V-221537`

### Rule: If using the WebLogic Web Server Proxy Plugin and configuring end-to-end SSL, OHS must have the WLSSLWallet directive enabled to maintain the confidentiality and integrity of information during preparation for transmission.

**Rule ID:** `SV-221537r961638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. An example of this would be an SMTP queue. This queue may be added to a web server through an SMTP module to enhance error reporting or to allow developers to add SMTP functionality to their applications. Any modules used by the web server that queue data before transmission must maintain the confidentiality and integrity of the information before the data is transmitted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using the WebLogic Web Server Proxy Plugin and configuring end-to-end SSL: 1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that contains an SSL-enabled "<VirtualHost>" directive. 2. Search for the "WLSSLWallet" directive within an "<IfModule weblogic_module>" at the virtual host configuration scope. 3. If the directive is omitted or is not set to a valid wallet folder, this is a finding.

## Group: SRG-APP-000441-WSR-000181

**Group ID:** `V-221538`

### Rule: If using the WebLogic Web Server Proxy Plugin and configuring SSL termination at OHS, OHS must have the WLSProxySSL directive enabled to maintain the confidentiality and integrity of information during preparation for transmission.

**Rule ID:** `SV-221538r961638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. An example of this would be an SMTP queue. This queue may be added to a web server through an SMTP module to enhance error reporting or to allow developers to add SMTP functionality to their applications. Any modules used by the web server that queue data before transmission must maintain the confidentiality and integrity of the information before the data is transmitted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using the WebLogic Web Server Proxy Plugin and configuring SSL termination at OHS: 1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that contains an SSL-enabled "<VirtualHost>" directive. 2. Search for the "WLProxySSL" directive within an "<IfModule weblogic_module>" at the virtual host configuration scope. 3. If the directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000442-WSR-000182

**Group ID:** `V-221539`

### Rule: OHS must have the LoadModule ossl_module directive enabled to maintain the confidentiality and integrity of information during reception.

**Rule ID:** `SV-221539r961641_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Protecting the confidentiality and integrity of received information requires that application servers take measures to employ approved cryptography in order to protect the information during transmission over the network. This is usually achieved through the use of Transport Layer Security (TLS), SSL VPN, or IPsec tunnel. The web server must utilize approved encryption when receiving transmitted data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule ossl_module" directive at the OHS server configuration scope. 3. If the directive is omitted, this is a finding. 4. Validate that the file specified exists. If the file does not exist, this is a finding.

## Group: SRG-APP-000442-WSR-000182

**Group ID:** `V-221540`

### Rule: OHS must have the SSLFIPS directive enabled to maintain the confidentiality and integrity of information during reception.

**Rule ID:** `SV-221540r961641_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Protecting the confidentiality and integrity of received information requires that application servers take measures to employ approved cryptography in order to protect the information during transmission over the network. This is usually achieved through the use of Transport Layer Security (TLS), SSL VPN, or IPsec tunnel. The web server must utilize approved encryption when receiving transmitted data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/ssl.conf with an editor. 2. Search for the "SSLFIPS" directive at the OHS server configuration scope. 3. If the directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000442-WSR-000182

**Group ID:** `V-221541`

### Rule: OHS must have the SSLEngine, SSLProtocol, and SSLWallet directives enabled and configured to maintain the confidentiality and integrity of information during reception.

**Rule ID:** `SV-221541r961641_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Protecting the confidentiality and integrity of received information requires that application servers take measures to employ approved cryptography in order to protect the information during transmission over the network. This is usually achieved through the use of Transport Layer Security (TLS), SSL VPN, or IPsec tunnel. The web server must utilize approved encryption when receiving transmitted data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. Note: Does not apply to admin.conf. 2. Search for the following directive at the OHS server, virtual host, and/or directory configuration scopes: "SSLEngine" "SSLProtocol" "SSLWallet" 3. If any of these directives are omitted, this is a finding. 4. If "SSLEngine" is not set to "On", or "SSLProtocol" is not set to "TLSv1.2", this is a finding. 5. Validate that the folder specified in the "SSLWallet" directive exists. If the folder does not exist or contain a valid wallet, this is a finding.

## Group: SRG-APP-000442-WSR-000182

**Group ID:** `V-221542`

### Rule: OHS must have the SSLCipherSuite directive enabled to maintain the confidentiality and integrity of information during reception.

**Rule ID:** `SV-221542r961641_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Protecting the confidentiality and integrity of received information requires that application servers take measures to employ approved cryptography in order to protect the information during transmission over the network. This is usually achieved through the use of Transport Layer Security (TLS), SSL VPN, or IPsec tunnel. The web server must utilize approved encryption when receiving transmitted data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that requires an SSL-enabled "<VirtualHost>" directive. 2. Search for the "SSLCipherSuite" directive at the OHS server, virtual host, and/or directory configuration scopes. 3. If the directive is omitted or set improperly, this is a finding.

## Group: SRG-APP-000442-WSR-000182

**Group ID:** `V-221543`

### Rule: If using the WebLogic Web Server Proxy Plugin and configuring end-to-end SSL, OHS must have the SSLSecureProxy directive enabled to maintain the confidentiality and integrity of information during reception.

**Rule ID:** `SV-221543r961641_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Protecting the confidentiality and integrity of received information requires that application servers take measures to employ approved cryptography in order to protect the information during transmission over the network. This is usually achieved through the use of Transport Layer Security (TLS), SSL VPN, or IPsec tunnel. The web server must utilize approved encryption when receiving transmitted data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using the WebLogic Web Server Proxy Plugin and configuring end-to-end SSL: 1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that contains an SSL-enabled "<VirtualHost>" directive. 2. Search for the "SecureProxy" directive within an "<IfModule weblogic_module>" at the virtual host configuration scope. 3. If the directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000442-WSR-000182

**Group ID:** `V-221544`

### Rule: If using the WebLogic Web Server Proxy Plugin and configuring end-to-end SSL, OHS must have the WLSSLWallet directive enabled to maintain the confidentiality and integrity of information during reception.

**Rule ID:** `SV-221544r961641_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Protecting the confidentiality and integrity of received information requires that application servers take measures to employ approved cryptography in order to protect the information during transmission over the network. This is usually achieved through the use of Transport Layer Security (TLS), SSL VPN, or IPsec tunnel. The web server must utilize approved encryption when receiving transmitted data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using the WebLogic Web Server Proxy Plugin and configuring end-to-end SSL: 1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that contains an SSL-enabled "<VirtualHost>" directive. 2. Search for the "WLSSLWallet" directive within an "<IfModule weblogic_module>" at the virtual host configuration scope. 3. If the directive is omitted or is not set to a valid wallet folder, this is a finding.

## Group: SRG-APP-000442-WSR-000182

**Group ID:** `V-221545`

### Rule: If using the WebLogic Web Server Proxy Plugin and configuring SSL termination at OHS, OHS must have the WLProxySSL directive enabled to maintain the confidentiality and integrity of information during reception.

**Rule ID:** `SV-221545r961641_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Protecting the confidentiality and integrity of received information requires that application servers take measures to employ approved cryptography in order to protect the information during transmission over the network. This is usually achieved through the use of Transport Layer Security (TLS), SSL VPN, or IPsec tunnel. The web server must utilize approved encryption when receiving transmitted data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using the WebLogic Web Server Proxy Plugin and configuring SSL termination at OHS: 1. Open every .conf file (e.g., ssl.conf) included in $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor that contains an SSL-enabled "<VirtualHost>" directive. 2. Search for the "WLProxySSL" directive within an "<IfModule weblogic_module>" at the virtual host configuration scope. 3. If the directive is omitted or is not set to "On", this is a finding.

## Group: SRG-APP-000266-WSR-000142

**Group ID:** `V-221546`

### Rule: OHS must display a default hosted application web page, not a directory listing, when a requested web page cannot be found.

**Rule ID:** `SV-221546r961167_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The goal is to completely control the web user's experience in navigating any portion of the web document root directories. Ensuring all web content directories have at least the equivalent of an index.html file is a significant factor to accomplish this end. Enumeration techniques, such as URL parameter manipulation, rely upon being able to obtain information about the web server's directory structure by locating directories without default pages. In the scenario, the web server will display to the user a listing of the files in the directory being accessed. By having a default hosted application web page, the anonymous web user will not obtain directory browsing information or an error message that reveals the server type and version.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "DocumentRoot" directives at the server and virtual host configuration scopes. 3. Go to the location specified as the value for each "DocumentRoot" directive (e.g., cd $DOMAIN_HOME/config/fmwconfig/components/OHS/instances/ohs1/htdocs). 4. Check for the existence of any index.html file in the directory specified as the "DocumentRoot" and its subdirectories (e.g., find . -type d, find . -type f -name index.html, cat index.html). 5. If an index.html files is not found or there is content in the file that is irrelevant to the website, this is a finding.

## Group: SRG-APP-000266-WSR-000159

**Group ID:** `V-221547`

### Rule: OHS must have the ServerSignature directive disabled.

**Rule ID:** `SV-221547r961167_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information needed by an attacker to begin looking for possible vulnerabilities in a web server includes any information about the web server, backend systems being accessed, and plug-ins or modules being used. Web servers will often display error messages to client users displaying enough information to aid in the debugging of the error. The information given back in error messages may display the web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage. This information could be used by an attacker to blueprint what type of attacks might be successful. The information given to users must be minimized to not aid in the blueprinting of the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "ServerSignature" directive at the OHS server, virtual host, and directory configuration scopes. 3. If the directive is omitted or is not set to "Off", this is a finding.

## Group: SRG-APP-000266-WSR-000159

**Group ID:** `V-221548`

### Rule: OHS must have the ServerTokens directive set to limit the response header.

**Rule ID:** `SV-221548r961167_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information needed by an attacker to begin looking for possible vulnerabilities in a web server includes any information about the web server, backend systems being accessed, and plug-ins or modules being used. Web servers will often display error messages to client users displaying enough information to aid in the debugging of the error. The information given back in error messages may display the web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage. This information could be used by an attacker to blueprint what type of attacks might be successful. The information given to users must be minimized to not aid in the blueprinting of the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "ServerTokens" directive at the OHS server configuration scope. 3. If the directive is omitted or is not set to "Custom DoD-Web-Server", this is a finding.

## Group: SRG-APP-000266-WSR-000159

**Group ID:** `V-221549`

### Rule: OHS must have the Alias /error directive defined to reference the directory accompanying the ErrorDocument directives to minimize the identity of OHS, patches, loaded modules, and directory paths in warning and error messages displayed to clients.

**Rule ID:** `SV-221549r961167_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information needed by an attacker to begin looking for possible vulnerabilities in a web server includes any information about the web server, backend systems being accessed, and plug-ins or modules being used. Web servers will often display error messages to client users displaying enough information to aid in the debugging of the error. The information given back in error messages may display the web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage. This information could be used by an attacker to blueprint what type of attacks might be successful. The information given to users must be minimized to not aid in the blueprinting of the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "Alias /error/ "${ORACLE_INSTANCE}/config/fmwconfig/components/${COMPONENT_TYPE}/instances/${COMPONENT_NAME}/error/"" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted, this is a finding. 4. Validate that the folder where the directive is pointing is valid. If the folder is not valid, this is a finding.

## Group: SRG-APP-000266-WSR-000159

**Group ID:** `V-221550`

### Rule: OHS must have the permissions set properly via the Directory directive accompanying the ErrorDocument directives to minimize improper access to the warning and error messages displayed to clients.

**Rule ID:** `SV-221550r961167_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information needed by an attacker to begin looking for possible vulnerabilities in a web server includes any information about the web server, backend systems being accessed, and plug-ins or modules being used. Web servers will often display error messages to client users displaying enough information to aid in the debugging of the error. The information given back in error messages may display the web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage. This information could be used by an attacker to blueprint what type of attacks might be successful. The information given to users must be minimized to not aid in the blueprinting of the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every.conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "Directory "${ORACLE_INSTANCE}/config/fmwconfig/components/${COMPONENT_TYPE}/instances/${COMPONENT_NAME}/error"" directive at the OHS server and virtual host configuration scopes. 3. If the directive is omitted, this is a finding. 4. Validate that the folder where the directive is pointing is valid. If the folder is not valid, this is a finding.

## Group: SRG-APP-000266-WSR-000159

**Group ID:** `V-221551`

### Rule: OHS must have defined error pages for common error codes that minimize the identity of the web server, patches, loaded modules, and directory paths.

**Rule ID:** `SV-221551r961167_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information needed by an attacker to begin looking for possible vulnerabilities in a web server includes any information about the web server, backend systems being accessed, and plug-ins or modules being used. Web servers will often display error messages to client users displaying enough information to aid in the debugging of the error. The information given back in error messages may display the web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage. This information could be used by an attacker to blueprint what type of attacks might be successful. The information given to users must be minimized to not aid in the blueprinting of the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for "ErrorDocument" directives at the OHS server, virtual host, and directory configuration scopes. 3. If the directives are omitted or set improperly for HTTP errors 400, 401, 403 - 405, 408, 410 - 415, 500 - 503, or 506, this is a finding. 4. Validate that the folder and files where the "ErrorDocument" directive are pointing are valid. If the folder or file is not valid, this is a finding.

## Group: SRG-APP-000266-WSR-000159

**Group ID:** `V-221552`

### Rule: OHS must have production information removed from error documents to minimize the identity of OHS, patches, loaded modules, and directory paths in warning and error messages displayed to clients.

**Rule ID:** `SV-221552r961167_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information needed by an attacker to begin looking for possible vulnerabilities in a web server includes any information about the web server, backend systems being accessed, and plug-ins or modules being used. Web servers will often display error messages to client users displaying enough information to aid in the debugging of the error. The information given back in error messages may display the web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage. This information could be used by an attacker to blueprint what type of attacks might be successful. The information given to users must be minimized to not aid in the blueprinting of the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "Alias /error/ "${ORACLE_INSTANCE}/config/fmwconfig/components/${COMPONENT_TYPE}/instances/${COMPONENT_NAME}/error/"", "Directory "${ORACLE_INSTANCE}/config/fmwconfig/components/${COMPONENT_TYPE}/instances/{COMPONENT_NAME}/error"", and "ErrorDocument" directives at the OHS server, virtual host, and directory configuration scopes. 3. For every file specified by an "ErrorDocument" directive, check the file exists and its contents to determine whether any OHS product information is present. 4. If OHS product information is present in the file(s), this is a finding.

## Group: SRG-APP-000266-WSR-000160

**Group ID:** `V-221553`

### Rule: Debugging and trace information used to diagnose OHS must be disabled.

**Rule ID:** `SV-221553r961167_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information needed by an attacker to begin looking for possible vulnerabilities in a web server includes any information about the web server and plug-ins or modules being used. When debugging or trace information is enabled in a production web server, information about the web server, such as web server type, version, patches installed, plug-ins and modules installed, type of code being used by the hosted application, and any backends being used for data storage may be displayed. Since this information may be placed in logs and general messages during normal operation of the web server, an attacker does not need to cause an error condition to gain this information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor. 2. Search for the "TraceEnable" directive at the OHS server and virtual host configuration scopes. 3. If the directive not set to "Off", this is a finding.

## Group: SRG-APP-000516-WSR-000079

**Group ID:** `V-252204`

### Rule: OHS must capture, record, and log all content related to a user session.

**Rule ID:** `SV-252204r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A user session to a web server is in the context of a user accessing a hosted application that extends to any plug-ins/modules and services that may execute on behalf of the user. The web server must be capable of enabling a setting for troubleshooting, debugging, or forensic gathering purposes which will log all user session information related to the hosted application session. Without the capability to capture, record, and log all content related to a user session, investigations into suspicious user activity would be hampered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf and every .conf file (e.g., ssl.conf) included in it with an editor that contains a "<VirtualHost>" directive. 2. Search for the "LogFormat" directive with nicknames of "dod" and "dod_ssl" at the OHS server and virtual host configuration scopes. 3. If either of these directives is omitted or set improperly, this is a finding unless inherited from a larger scope.

## Group: SRG-APP-000416-WSR-000118

**Group ID:** `V-252205`

### Rule: OHS must have the LoadModule ossl_module directive enabled to implement required cryptographic protections using cryptographic modules complying with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance when encrypting data that must be compartmentalized.

**Rule ID:** `SV-252205r962034_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Cryptography is only as strong as the encryption modules/algorithms employed to encrypt the data. Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. NSA has developed Type 1 algorithms for protecting classified information. The Committee on National Security Systems (CNSS) National Information Assurance Glossary (CNSS Instruction No. 4009) defines Type 1 products as: "Cryptographic equipment, assembly or component classified or certified by NSA for encrypting and decrypting classified and sensitive national security information when appropriately keyed. Developed using established NSA business processes and containing NSA-approved algorithms are used to protect systems requiring the most stringent protection mechanisms." Although persons may have a security clearance, they may not have a "need-to-know" and are required to be separated from the information in question. The web server must employ NSA-approved cryptography to protect classified information from those individuals who have no "need-to-know" or when encryption of compartmentalized data is required by data classification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/httpd.conf with an editor. 2. Search for the "LoadModule ossl_module" directive at the OHS server configuration scope. 3. If the directive is omitted, this is a finding. 4. Validate that the file specified exists. If the file does not exist, this is a finding.

## Group: SRG-APP-000416-WSR-000118

**Group ID:** `V-252546`

### Rule: OHS must have the SSLFIPS directive enabled to implement required cryptographic protections using cryptographic modules complying with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance when encrypting data that must be compartmentalized.

**Rule ID:** `SV-252546r962034_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Cryptography is only as strong as the encryption modules/algorithms employed to encrypt the data. Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. NSA has developed Type 1 algorithms for protecting classified information. The Committee on National Security Systems (CNSS) National Information Assurance Glossary (CNSS Instruction No. 4009) defines Type 1 products as: "Cryptographic equipment, assembly or component classified or certified by NSA for encrypting and decrypting classified and sensitive national security information when appropriately keyed. Developed using established NSA business processes and containing NSA-approved algorithms are used to protect systems requiring the most stringent protection mechanisms." Although persons may have a security clearance, they may not have a "need-to-know" and are required to be separated from the information in question. The web server must employ NSA-approved cryptography to protect classified information from those individuals who have no "need-to-know" or when encryption of compartmentalized data is required by data classification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. As required, open $DOMAIN_HOME/config/fmwconfig/components/OHS/<componentName>/ssl.conf with an editor. 2. Search for the "SSLFIPS" directive at the OHS server configuration scope. 3. If the directive is omitted or is not set to "On", this is a finding.

