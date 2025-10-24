# STIG Benchmark: IBM WebSphere Liberty Server Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-AS-000001

**Group ID:** `V-250322`

### Rule: Maximum in-memory session count must be set according to application requirements.

**Rule ID:** `SV-250322r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application management includes the ability to control the number of sessions that use an application by all accounts and/or account types. Limiting the number of allowed sessions is helpful in limiting risks related to Denial of Service attacks. Application servers host and expose business logic and application processes. The application server must possess the capability to limit the maximum number of concurrent sessions in a manner that affects the entire application server or on an individual application basis. Although there is some latitude concerning the settings themselves, the settings should follow DoD-recommended values, but the settings should be configurable to allow for future DoD direction. While the DoD will specify recommended values, the values can be adjusted to accommodate the operational requirement of a given system. The System Security Plan should be reviewed and the maximum number of concurrent sessions allowable and defined within that plan should be used in the httpSession element. For example, if the maximum number of concurrent sessions is defined in the System Security Plan as 5000, then the httpSession element in ${server.config.dir}/server.xml should be configured as: <httpSession maxInMemorySessionCount="5000" allowOverflow="false" /> For http session security settings to apply, the security feature (appSecurity-2.0) must be defined in order to configure a user registry for the servlet to authenticate against. The servlet feature (servlet-3.1) must be defined in order to use a web application, and the ldap feature (ldapRegistry-3.0) must be defined in order to configure an enterprise-level user registry for authentication of the servlet users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the System Security plan to determine the maximum number of concurrent sessions allowed. This is a per user setting and must be defined by the application admins. As a privileged user with access to the server.xml file, review file content and identify the "maxInMemorySessionCount" and the allowOverflow settings. EXAMPLE: grep -i maxInMemorySessionCount server.xml <httpSession maxInMemorySessionCount="xxxx" allowOverflow="false" /> If maxInMemorySessionCount is not set in server.xml according to the settings defined in the system security plan or if allowOverflow="true", this is a finding.

## Group: SRG-APP-000014-AS-000009

**Group ID:** `V-250323`

### Rule: The WebSphere Liberty Server Quality of Protection (QoP) must be set to use TLSv1.2 or higher.

**Rule ID:** `SV-250323r960759_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Quality of Protection in WebSphere Liberty specifies the security level, ciphers, and mutual authentication settings for the Secure Socket Layer (SSL/TLS) configuration. For Quality of Protection settings to apply, the security feature (appSecurity-2.0) must be defined in order to configure a user registry for the servlet to authenticate against. The SSL feature (ssl-1.0) must be defined in order to configure ssl settings, and the ldap feature (ldapRegistry-3.0) must be defined in order to configure an enterprise-level user registry for authentication of users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a privileged user with local file access to ${server.config.dir}/server.xml, verify the appSecurity-x.x feature and the sslProtocol settings are configured. grep -i appsecurity- server.xml RESULT: <feature>appSecurity-2.0</feature> Verify the SSL protocol setting is configured for TLSV1.2 for every SSL configuration. There can be multiple SSL configurations and SSL ID settings. grep -i "<ssl id=" server.xml SAMPLE RESULT: <ssl id="TLSSettings" keyStoreRef="TLSKeyStore" trustStoreRef="TLSTrustStore" sslProtocol="TLSv1.2"/> If the SSL protocol setting does not specify TLS v.1.2 or higher, or if the appSecurity feature is not configured, this is a finding.

## Group: SRG-APP-000015-AS-000010

**Group ID:** `V-250324`

### Rule: Security cookies must be set to HTTPOnly.

**Rule ID:** `SV-250324r960762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web applications use cookies to track users across requests. These cookies, while typically not sensitive in themselves, connect to the existing state on the back-end system. If an intruder were to capture one of these cookies, they could potentially use the cookie to act as the user. Important web traffic should be encrypted using SSL. This includes important cookies. In the case of WebSphere Liberty Server, the most important cookies are the LTPA cookie and session cookie; therefore, both should be configured to be only sent over SSL. To set httpOnly on the application server’s cookies, the security feature (appSecurity-2.0) must be defined in order to configure a user registry for the servlet to authenticate against. The servlet (servlet-3.1) feature must be defined in order to deploy web applications, the ssl (ssl-1.0) feature must be defined in order to do SSL communications, and the ldap feature (ldapRegistry-3.0) must be defined in order to configure an enterprise-level user registry for authentication of users. For the LTPA cookie, the httpOnlyCookies element must be set to true: <webAppSecurity ssoCookieName="LtpaToken2" ssoRequiresSSL="true" httpOnlyCookies="true" logoutOnHttpSessionExpire="true"/> For the JSESSIONID cookie, the cookieHttpOnly element must be set to true: <httpSession cookieName="JSESSIONID" cookieSecure="true" cookieHttpOnly="true" cookiePath="/"/></VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a user with local file access to ${server.config.dir}/server.xml, verify appSecurity feature is enabled. <featureManager><feature>appSecurity-2.0</feature></featureManager> Verify both web application LTPA and http session cookies are configured for httpOnly. <webAppSecurity ssoCookieName="LtpaToken2" ssoRequiresSSL="true" httpOnlyCookies="true" logoutOnHttpSessionExpire="true"/> <httpSession cookieName="JSESSIONID" cookieSecure="true" cookieHttpOnly="true" cookiePath="/"/> If the appSecurity feature is not enabled or if the LPTA or Session cookie settings are not set for httpOnly, this is a finding.

## Group: SRG-APP-000016-AS-000013

**Group ID:** `V-250325`

### Rule: The WebSphere Liberty Server must log remote session and security activity.

**Rule ID:** `SV-250325r1015250_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security auditing must be configured in order to log remote session activity. Security auditing will not be performed unless the audit feature (audit-1.0) has been enabled. The security feature (appSecurity-2.0) must be enabled for the security auditing to capture security transactions. Remote session activity will then be logged, regardless of the user attempting that activity. Satisfies: SRG-APP-000016-AS-000013, SRG-APP-000080-AS-000045, SRG-APP-000089-AS-000050, SRG-APP-000091-AS-000052, SRG-APP-000095-AS-000056, SRG-APP-000096-AS-000059, SRG-APP-000097-AS-000060, SRG-APP-000098-AS-000061, SRG-APP-000099-AS-000062, SRG-APP-000100-AS-000063, SRG-APP-000101-AS-000072, SRG-APP-000266-AS-000168, SRG-APP-000343-AS-000030, SRG-APP-000172-AS-000121</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ${server.config.dir}/server.xml file and ensure audit-1.0 and appSecurity-2.0 are defined within the <featureManager> setting in the server.xml file. If audit-1.0 and appSecurity-2.0 are not defined within the <featureManager> setting in the server.xml file, this is a finding. EXAMPLE: <featureManager> <feature>audit-1.0</feature> <feature>appSecurity-3.0</feature> </featureManager>

## Group: SRG-APP-000033-AS-000024

**Group ID:** `V-250326`

### Rule: Users in the REST API admin role must be authorized.

**Rule ID:** `SV-250326r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Users with console access and OS permissions to the folders where the Liberty Server is installed can make changes to the server. In addition, REST API calls that execute server management tasks are available and can be executed remotely. Adding a user to the admin role will allow that user to make changes to the server via the REST API calls. The admin role must be controlled and users who are in that role must be authorized.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a user with access to ${server.config.dir}/server.xml, review the file and look for the admin role settings. grep -i administrator-role ${server.config.dir}/server.xml grep -i quickstartsecurity ${server.config.dir}/server.xml If the admin role has been created, users in that role must be documented and approved. However, using the basic registry or the quickstartsecurity methods are not acceptable. The preferred user registry method is to use a centralized access control method via LDAP. If no admin users exist at all, this is not a finding. If admin users in an LDAP user registry configuration are not documented and approved, this is a finding. If admin users exist in a basic user registry configuration, or in a quickstartsecurity user configuration, this is a finding. LDAP EXAMPLE: <administrator-role> <user>cn=bob,o=ibm,c=us</user> </administrator-role> BASIC REGISTRY EXAMPLE: <basicRegistry> <user name="bob" password="bobpassword"/> <user name="joe" password="joepassword"/> <group name="group1" ...> </group> </basicRegistry> <administrator-role> <user>bob</user> <group>group1</group> </administrator-role> QUICKSTARTSECURITY EXAMPLE: <featureManager> <feature>restConnector-2.0</feature> </featureManager> <quickStartSecurity userName="bob" userPassword="bobpassword" /> <keyStore id="defaultKeyStore" password="keystorePassword"/>

## Group: SRG-APP-000109-AS-000070

**Group ID:** `V-250327`

### Rule: The WebSphere Liberty Server must be configured to offload logs to a centralized system.

**Rule ID:** `SV-250327r1043188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log processing failures include, but are not limited to, failures in the application server log capturing mechanisms or log storage capacity being reached or exceeded. In some instances, it is preferred to send alarms to individuals rather than to an entire group. Application servers must be able to trigger an alarm and send an alert to, at a minimum, the SA and ISSO in the event there is an application server log processing failure. Satisfies: SRG-APP-000109-AS-000070, SRG-APP-000358-AS-000064</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a privileged user with local file access to ${server.config.dir}/server.xml, verify the logstashCollector-1.0 feature is enabled. grep -i -A5 logstashcollector server.xml EXAMPLE: <featureManager> <feature>logstashCollector-1.0</feature> </featureManager> <logstashCollector source="message,accessLog,audit" hostName="<ip address of logstash server>" port="<port of logstash server>" sslRef="DefaultTLSSettings" </logstashCollector> If "logstashCollector" is not a configured feature and the logstashCollector "source" setting does not contain "message,accessLog,audit", this is a finding.

## Group: SRG-APP-000119-AS-000079

**Group ID:** `V-250328`

### Rule: The WebSphere Liberty Server must protect log information from unauthorized access or changes.

**Rule ID:** `SV-250328r960933_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>WebSphere Liberty provides the capability to encrypt and sign the log data to prevent unauthorized modification. - The security feature (appSecurity-2.0) must be defined in order to configure a user registry for the servlet to authenticate against. - The audit feature (audit-1.0) must be defined in order to generate audit records. - The servlet feature (servlet-3.1) must be defined to be able to deploy a web application. - The ejb feature (ejbLite-3.1) must be defined to be able to deploy an ejb application. - The ssl feature (ssl-1.0) must be defined to be able to generate and use certificates to sign and encrypt logs. - The ldap feature (ldapRegistry-3.0) must be defined in order to configure an enterprise-level user registry to authenticate users against. When the audit-1.0 feature is defined, all supported audit events will be captured and logged to an audit.log located under ${server.config.dir}/logs. The audit log that is currently being logged to is called audit.log. When an audit log fills to a configured maximum capacity, it is archived with a timestamp with the naming convention audit_<timestamp>.log and new records are written to audit.log. The audit logs are found under the ${server.config.dir}/logs directory and are named audit.log for the most recent, and audit_<timestamp>.log for any archived logs. Two keystores need to be created (ikeyman as part of the JDK may be used) and a personal certificate created in each. One keystore will contain the certificate used to encrypt the logs; the other keystore will contain the certificate used to sign the logs. The audit configuration needs to define the location of these two keystores, their passwords, and the alias of each certificate used to encrypt and sign the logs. As an example: <keyStore id="auditEncKeyStore" password="Liberty" location="${server.config.dir}/resources/security/AuditEncryptionKeyStore.jks" type="JKS" /> <keyStore id="auditSignKeyStore" password="{xor}EzY9Oi0rJg==" location="${server.config.dir}/resources/security/AuditSigningKeyStore2.jks" type="JKS" /> <auditFileHandler encrypt="true" encryptAlias="auditencryption" encryptKeyStoreRef="auditEncKeyStore" sign="true" signingAlias="auditsigning2" signingKeyStoreRef="auditSignKeyStore"> </auditFileHandler> Satisfies: SRG-APP-000119-AS-000079, SRG-APP-000120-AS-000080</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a user with local file access to ${server.config.dir}/logs, verify the following audit log files have the correct file permissions of 660. audit.log messages.log console.log trace.log (if it exists) If the file permissions for these files are not set to 660, this is a finding.

## Group: SRG-APP-000121-AS-000081

**Group ID:** `V-250329`

### Rule: The WebSphere Liberty Server must protect log tools from unauthorized access.

**Rule ID:** `SV-250329r960939_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting log data also includes identifying and protecting the tools used to view and manipulate log data. Depending on the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. Therefore, it is imperative that access to log tools be controlled and protected from unauthorized access. Application servers provide a web- and/or a command line-based management functionality for managing the application server log capabilities. In addition, subsets of log tool components may be stored on the file system as jar or xml configuration files. The application server must ensure that in addition to protecting any web-based log tools, any file system-based tools are protected as well.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a user with local file access to the /opt/IBM/WebSphere/Liberty/bin folder, verify the following audit tool files have the correct file permissions of 755. binaryLog auditUtility If the file permissions for these files are not set to 755, this is a finding.

## Group: SRG-APP-000126-AS-000085

**Group ID:** `V-250330`

### Rule: The WebSphere Liberty Server must be configured to encrypt log information.

**Rule ID:** `SV-250330r960951_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of log records is of critical importance. Encrypting log records provides a level of protection that does not rely on host-based protections that can be accidentally misconfigured, such as file system permissions. Cryptographic mechanisms are the industry-established standard used to protect the integrity of log data. An example of a cryptographic mechanism is the computation and application of a cryptographic-signed hash using asymmetric cryptography. - The security feature (appSecurity-2.0) must be defined in order to configure a user registry for the servlet to authenticate against. - The audit feature (audit-1.0) must be defined in order to generate audit records. - The servlet feature (servlet-3.1) must be defined to be able to deploy a web application. - The ejb feature (ejbLite-3.1) must be defined to be able to deploy an ejb application. - The ssl feature (ssl-1.0) must be defined to be able to generate and use certificates to sign and encrypt logs. - The ldap feature (ldapRegistry-3.0) must be defined in order to configure an enterprise-level user registry to authenticate users against. When the audit-1.0 feature is defined, all supported audit events will be captured and logged to an audit.log located under ${server.config.dir}/logs. The audit log that is currently being logged to is called audit.log. When an audit log fills to a configured maximum capacity, it is archived with a timestamp with the naming convention audit_<timestamp>.log and new records are written to audit.log. The audit logs are found under the ${server.config.dir}/logs directory and are named audit.log for the most recent, and audit_<timestamp>.log for any archived logs. One keystore needs to be created (ikeyman as part of the JDK may be used) and a personal certificate created. This certificate is used to encrypt the logs. The audit configuration needs to define the location of this keystore, its password, and the alias of the certificate used to encrypt the logs. As an example: <keyStore id="auditEncKeyStore" password="Liberty" location="${server.config.dir}/resources/security/AuditEncryptionKeyStore.jks" type="JKS" /> <keyStore id="auditSignKeyStore" password="{xor}EzY9Oi0rJg==" location="${server.config.dir}/resources/security/AuditSigningKeyStore2.jks" type="JKS" /> <auditFileHandler encrypt="true" encryptAlias="auditencryption" encryptKeyStoreRef="auditEncKeyStore" </auditFileHandler> Satisfies: SRG-APP-000126-AS-000085, SRG-APP-000118-AS-000078, SRG-APP-000267-AS-000170</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is configured to send logs to a remote ELK stack log server, as per requirement IBMW-LS-000230, (or other remote logging solution) this requirement is Not Applicable. As a user with local file access to ${server.config.dir}/server.xml: 1. Verify the following features are configured. <featureManager> <feature>appSecurity-2.0</feature> <feature>audit-1.0</feature> <feature>ssl-1.0</feature> </featureManager> 2. Verify a keystore is configured. The following is an example: <keyStore id="auditEncKeyStore" password="ENTER THE ENCRYPTION KEYSTORE PASSWORD" location="${server.config.dir}/resources/security/AuditEncryptionKeyStore.jks" type="JKS" /> <keyStore id="auditSignKeyStore" password="ENTER THE SIGNING KEYSTORE PASSWORD" location="${server.config.dir}/resources/security/AuditSigningKeyStore2.jks" type="JKS" /> 3. Verify auditFileHandler encryption is enabled. Signing is optional. <auditFileHandler encrypt="true" encryptAlias="auditencryption" encryptKeyStoreRef="auditEncKeyStore" sign="true" signingAlias="auditsigning2" signingKeyStoreRef="auditSignKeyStore"> </auditFileHandler> If the features and keystore are not configured, and encryption is not enabled, this is a finding.

## Group: SRG-APP-000133-AS-000092

**Group ID:** `V-250331`

### Rule: The WebSphere Liberty Server must protect software libraries from unauthorized access.

**Rule ID:** `SV-250331r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application servers have the ability to specify that the hosted applications use shared libraries. The application server must have a capability to divide roles based upon duties wherein one project user (such as a developer) cannot modify the shared library code of another project user. The application server must also be able to specify that non-privileged users cannot modify any shared library code at all.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a privileged user with local file access to the /opt/IBM/WebSphere/Liberty/lib/ folder, verify all of the jar files in the lib folder have the correct file permissions of 664. If the file permissions for all jar files in the lib folder are not set to 664, this is a finding.

## Group: SRG-APP-000142-AS-000014

**Group ID:** `V-250332`

### Rule: The WebSphere Liberty Server must prohibit or restrict the use of nonsecure ports, protocols, modules, and/or services as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-250332r1043177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some networking protocols may not meet organizational security requirements to protect data and components. Application servers natively host a number of various features, such as management interfaces, httpd servers, and message queues. These features all run on TCPIP ports. This creates the potential that the vendor may choose to use port numbers or network services that have been deemed unusable by the organization. The application server must have the capability to both reconfigure and disable the assigned ports without adversely impacting application server operation capabilities. For a list of approved ports and protocols, reference the DoD ports and protocols website at https://powhatan.iiie.disa.mil/ports/cal.html.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a privileged user with access to the server.xml file, review the file and identify all TCPIP ports used by the server. EXAMPLE: grep -I "port=" server.xml httpsPort="9443"> Review the PPSM site for the list of approved ports. If any of the ports used are not registered with PPSM, this is a finding.

## Group: SRG-APP-000148-AS-000101

**Group ID:** `V-250333`

### Rule: The WebSphere Liberty Server must use an LDAP user registry.

**Rule ID:** `SV-250333r1051118_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthorized access, application server users must be uniquely identified and authenticated. This is typically accomplished via the use of a user store which is either local (OS-based) or centralized (LDAP) in nature. Best practice guideline to is to use a centralized enterprise LDAP server. To ensure support to the enterprise, the authentication must use an enterprise solution.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a user with local file access to ${server.config.dir}/server.xml file, verify the LDAP user registry is used to authenticate users. If the LDAP user registry is not defined within server.xml, this is a finding. <featureManager> <feature>appSecurity-2.0</feature> <feature>ldapRegistry-3.0</feature> </featureManager> <ldapRegistry id="ldap" realm="SampleLdapRealm" host="${ldap.server.name}" port="${ldap.server.port}" ignoreCase="true" baseDN="${ldap.server.base.dn}" ldapType="${ldap.vendor.type}" searchTimeout="8m"> </ldapRegistry>

## Group: SRG-APP-000148-AS-000101

**Group ID:** `V-250334`

### Rule: Basic Authentication must be disabled.

**Rule ID:** `SV-250334r1051118_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Basic authentication does not use a centralized user store like LDAP. Not using a centralized user store complicates user management tasks and increases the risk that user accounts could remain on the system long after users have moved to their next deployment. Basic Auth also stores user credentials and passwords on the system and creates the potential for an attacker to circumvent strong authentication requirements like multi-factor or certificate based authentication. Allowing failover to Basic Auth allows the Liberty Server to fall back to basic authentication in the event certificate based authentication methods fail. Configuring the Liberty Server to fall back to basic authentication creates the potential for an attacker to circumvent strong authentication requirements and must be avoided.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a privileged user with local file access to the ${server.config.dir}/server.xml file, search the server.xml for the basicRegistry setting. grep -i basicregistry server.xml SAMPLE: <basicRegistry id="basic" realm="BasicRealm"> <user name="employee0" password="emp0pwd" /> <user name="employee1" password="emp1pwd" /> <user name="manager0" password="mgr0pwd" /> <group name="employeeGroup"> <member name="employee0" /> <member name="employee1" /> </group> </basicRegistry> If <basicRegistry> settings are defined in server.xml, this is a finding.

## Group: SRG-APP-000149-AS-000102

**Group ID:** `V-250335`

### Rule: Multifactor authentication for network access to privileged accounts must be used.

**Rule ID:** `SV-250335r1015469_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Multifactor authentication creates a layered defense and makes it more difficult for an unauthorized person to access the application server. If one factor is compromised or broken, the attacker still has at least one more barrier to breach before successfully breaking into the target. Unlike a simple username/password scenario where the attacker could gain access by knowing both the username and password without the user knowing his account was compromised, multifactor authentication adds the requirement that the attacker must have something from the user, such as a token, or to biometrically be the user. When accessing the application server via a network connection, administrative access to the application server must be PKI Hardware Token enabled. The high level steps required for configuring Liberty Server to use certificate based authentication include the following: 1. Configure Web Application with client certificate authentication. 2. Configure Liberty SSL configuration with client authentication. 3. Configure Liberty LDAP Security Configuration with certificate filter. Satisfies: SRG-APP-000149-AS-000102, SRG-APP-000151-AS-000103, SRG-APP-000402-AS-000247, SRG-APP-000403-AS-000248, SRG-APP-000177-AS-000126</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a user with local file access to ${server.config.dir}/server.xml file, verify the TLS connection used for managing the server is configured to use clientAuthentication. <featureManager> <feature>appSecurity-2.0</feature> <feature>ldapRegistry-3.0</feature> <feature>transportSecurity-1.0</feature> </featureManager> Verify the TLS connection used for managing the server is configured to use clientAuthentication. The following is used as an example. If the clientAuthentication setting for the TLS management application is not set to "true", this is a finding. EXAMPLE: <!-- default SSL configuration is defaultSSLSettings --> <sslDefault sslRef="defaultSSLSettings" /> <ssl id="defaultSSLSettings" keyStoreRef="defaultKeyStore" sslProtocol="SSL_TLSv2" trustStoreRef="defaultTrustStore" clientAuthentication="true"/> Access the web management interface via a web browser and verify TLS secured connectivity to the web based management application.

## Group: SRG-APP-000171-AS-000119

**Group ID:** `V-250336`

### Rule: The WebSphere Liberty Server must store only encrypted representations of user passwords.

**Rule ID:** `SV-250336r1015470_rule`
**Severity:** high

**Description:**
<VulnDiscussion>WebSphere Liberty can either provide a local account store or integrate with enterprise account stores such as LDAP directories. If the application server stores application passwords in the server.xml configuration files, the application server must store encrypted representations of passwords rather than unencrypted, clear-text passwords. The Liberty Application Server provides a SecurityUtility tool that can take a plain-text or encoded password and convert it to an encrypted password. This tool does not update the ${server.config.dir/server.xml file directly; a manual update of the server.xml is needed once the utility is run. It is imperative that administrators understand that the SecurityUtility tool must be run for each application password that is stored within the server.xml file. Satisfies: SRG-APP-000171-AS-000119, SRG-APP-000428-AS-000265, SRG-APP-000429-AS-000157</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a privileged user with file access to ${server.config.dir}/server.xml, review and ensure there are no clear-text passwords stored within the server.xml file. If any passwords appear in plain text, or if any passwords start with {xor}, this is a finding.

## Group: SRG-APP-000172-AS-000120

**Group ID:** `V-250337`

### Rule: The WebSphere Liberty Server must use TLS-enabled LDAP.

**Rule ID:** `SV-250337r961029_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords during transmission. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Application servers have the capability to use either certificates (tokens) or user IDs and passwords in order to authenticate. When the application server transmits or receives passwords, the passwords must be encrypted. The certificate used by LDAP to establish trust with incoming client requests must be imported into a trust keystore created on the Liberty Server (JDK ikeyman may be used to do this). The LDAP configuration must indicate it is using SSL, provide the BindDN and BindPassword and point to the trust keystore containing the LDAP certificate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a user with local file access to ${server.config.dir}/server.xml, verify TLS-enabled LDAP is in use. If TLS-Enabled LDAP is not defined within server.xml, this is a finding. <featureManager> <feature>appSecurity-2.0</feature> <feature>ssl-1.0</feature> <feature>ldapRegistry-3.0</feature> </featureManager> <ldapRegistry id="ldap" realm="SampleLdapRealm" host="${ldap.server.name}" port="${ldap.server.port}" ignoreCase="true" baseDN="${ldap.server.base.dn}" bindDN="${ldap.server.bind.dn}’ bindPassword="${ldap.server.bind.password}" sslEnabled="true" sslRef="LDAPTLSSettings" ldapType="${ldap.vendor.type}" searchTimeout="8m"> </ldapRegistry> <sslDefault sslRef="LDAPTLSSettings" /> <ssl id="LDAPTLSSettings" keyStoreRef="LDAPKeyStore" trustStoreRef="LDAPTrustStore" sslProtocol="TLSv1.2"/> <keyStore id="LDAPKeyStore" location="${server.config.dir}/LdapSSLKeyStore.jks" type="JKS" password="{xor}CDo9Hgw=" /> <keyStore id="LDAPTrustStore" location="${server.config.dir}/LdapTLSTrustStore.jks" type="JKS" password="{xor}CDo9Hgw=" />

## Group: SRG-APP-000177-AS-000126

**Group ID:** `V-250338`

### Rule: The WebSphere Liberty Server must use DoD-issued/signed certificates.

**Rule ID:** `SV-250338r961044_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The cornerstone of PKI is the private key used to encrypt or digitally sign information. The key by itself is a cryptographic value that does not contain specific user information, but the key can be mapped to a user. Without mapping the certificate used to authenticate to the user account, the ability to determine the identity of the individual user or group will not be available for forensic analysis. Satisfies: SRG-APP-000177-AS-000126, SRG-APP-000427-AS-000264, SRG-APP-000514-AS-000137</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a privileged user with access to the ${server.config.dir}/server.xml file; search for SSLDefault in order to identify the default SSL configuration. grep -i ssldefault server.xml Identify the default ssl configuration by examining the sslRef flag. SAMPLE: <sslDefault sslRef="DefaultTLSSettings" /> Review the default ssl configuration to identify the default truststore. SAMPLE: <ssl id="DefaultTLSSettings" keyStoreRef="defaultKeyStore" /> <keyStore id="LDAPTrustStore" location="${server.config.dir}/liberty.ks" type="JKS" password="xxxxxxx" /> Use the java keytool or ikeyman utilities to open and examine the certificates stored in the truststore. If the certificates are self signed or not signed by a DoD approved CA, this is a finding.

## Group: SRG-APP-000179-AS-000129

**Group ID:** `V-250339`

### Rule: The WebSphere Liberty Server must use FIPS 140-2 approved encryption modules when authenticating users and processes.

**Rule ID:** `SV-250339r1067571_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Application servers must use and meet requirements of the DOD Enterprise PKI infrastructure for application authentication. Encryption is only as good as the encryption modules used. Unapproved cryptographic module algorithms cannot be verified and cannot be relied upon to provide confidentiality or integrity, and DOD data may be compromised due to weak algorithms. The use of TLS provides confidentiality of data in transit between the application server and client. TLS must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 specifies the preferred configurations for government systems. Satisfies: SRG-APP-000179-AS-000129, SRG-APP-000224-AS-000152, SRG-APP-000416-AS-000140, SRG-APP-000439-AS-000155, SRG-APP-000442-AS-000259, SRG-APP-000514-AS-000136</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
There are two ways to meet this requirement. Only one method is required. If IBM JDK 8 is installed and configured to run with WebSphere Liberty, proceed with method (I). If IBM Semeru Runtimes version 11 and above is installed and configured with WebSphere Liberty, proceed with method (II). Currently IBM Semeru supports FIPS on RedHat Enterprise Linux. Method (I) IBM JDK 8 is configured to run with WebSphere Liberty: 1. Review the ${server.config.dir}/jvm.options file. Verify FIPS is in use by checking the following lines: Dcom.ibm.jsse2.usefipsprovider=true Dcom.ibm.jsse2.usefipsProviderName=IBMJCEPlusFIPS If the properties are not set as shown in the ${server.config.dir}/jvm.options file, this is a finding. 2. Open ${JAVA_HOME}/jre/lib/security/java.security file. Locate the list of cryptographic providers and confirm the following entries in the provider list: com.ibm.crypto.plus.provider.IBMJSSEProvider2 com.ibm.crypto.plus.provider.IBMJCEPlusFIPS com.ibm.crypto.plus.provider.IBMJCEPlus com.ibm.crypto.plus.provider.IBMJCE If the entries are not set as shown in the ${JAVA_HOME}/jre/lib/security/java.security file, this is a finding. Method (II) Semeru Runtimes version 11 and above is installed and configured with WebSphere Liberty. Requires RedHat Enterprise Linux as the Host Operating System. 1. Run the following command on the RedHat Enterprise Linux. Verify FIPS mode is enabled. # fips-mode-setup --check If FIPS mode is not enabled, this is a finding. 2. Review the ${server.config.dir}/jvm.options file. Verify "semeru.fips" property is set to true. Dsemeru.fips=true If the property is not set as shown in the ${server.config.dir}/jvm.options file, this is a finding. 3. Confirm NSS packages are installed by running "# dnf install nss" in a terminal. # dnf install nss Updating Subscription Management repositories. Last metadata expiration check: 0:56:30 ago on Wed 13 Sep 2023 07:29:35 AM PDT. Package nss-3.79.0-11.el8_7.x86_64 is already installed. Dependencies resolved. Nothing to do. Complete! If the command does not return output stating NSS is installed, this is a finding. 4. Confirm NSS Database has the keystore imported by running "# certutil -L -d /etc/pki/nssdb" in a terminal. # certutil -L -d /etc/pki/nssdb Certificate Nickname Trust Attributes SSL,S/MIME,JAR/XPI default CTu,Cu,Cu If the command does not return the results as shown, this is a finding. 5. Review the ${server.config.dir}/server.xml and confirm the following entries: name = NSS-FIPS library = /usr/lib64/libsoftokn3.so slot = 3 showInfo = true If the entries are not set as shown in the ${server.config.dir}/server.xml file, this is a finding. 6. Review the ${server.config.dir}/server.xml file with the following steps: 6.1 Locate <ssl> configuration that is specifying the default SSL configuration for Liberty. 6.2 Locate the "keyStoreRef" attribute in the <ssl> configuration and find the referenced <keyStore> configuration. 6.3 Verify the "provider" attribute is set to either "SunPKCS11-NSS-FIPS" or "PKCS11-NSS-FIPS" in the <keyStore> configuration. 6.4 Verify the "type" attribute is set to "PKCS11". 6.5 Verify the "fileBased" attribute is set to "false". 6.6 Find the "location" attribute for the configuration file of NSS keystore database (In the example below, it is "/tmp/pkcs11cfg.cfg"). 6.7 Verify the file is in a location that is accessible to Liberty. Snippet of server.xml: <ssl id="defaultSSLConfig" keyStoreRef="defaultKeyStore" sslProtocol="TLSv1.2" /> <keyStore id="defaultKeyStore" password="{xor}Lz4sLCgwLTsINis3" location="/tmp/pkcs11cfg.cfg" type="PKCS11" fileBased="false" provider="SunPKCS11-NSS-FIPS" /> If the entries are not set as shown in the ${server.config.dir}/server.xml file, this is a finding.

## Group: SRG-APP-000295-AS-000263

**Group ID:** `V-250340`

### Rule: HTTP session timeout must be configured.

**Rule ID:** `SV-250340r1043182_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An attacker can take advantage of user sessions that are left open, thus bypassing the user authentication process. To thwart the vulnerability of open and unused user sessions, the application server must be configured to close the sessions when a configured condition or trigger event is met. Session termination terminates all processes associated with a user’s logical session except those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. Satisfies: SRG-APP-000295-AS-000263, SRG-APP-000389-AS-000253</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a user with access to the server xml file, review the contents and verify the httpSession time out setting is configured for 10 minutes. If the ${server.config.dir}/server.xml does not define the timeout setting as 10 minutes, this is a finding. <httpSession invalidationTimeout="10m"/>

## Group: SRG-APP-000315-AS-000094

**Group ID:** `V-250341`

### Rule: Application security must be enabled on the WebSphere Liberty Server.

**Rule ID:** `SV-250341r1015252_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Application security enables security for the applications in the environment. This type of security provides application isolation and requirements for authenticating application users. When a user enables security, both administrative and application security is enabled. Application security is in effect only when administrative security is enabled via the security feature. If the application server is to be used for only web applications, only the servlet-3.1 feature needs to be defined. If the application server is to be used for only ejb applications, only the ejbLite-3.1 feature needs to be defined. If both web and ejb applications are to be deployed on the application server, then both the servlet-3.1 and ejbLite-3.1 features need to be defined. The check and fix assumes that the application server will have both web and ejb applications deployed. Satisfies: SRG-APP-000315-AS-000094, SRG-APP-000014-AS-000009</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a user with local file access to ${server.config.dir}/server.xml file, verify application security is enabled. If the appSecurity-2.0 feature is not defined within server.xml, this is a finding. <featureManager> <feature>appSecurity-2.0</feature> </featureManager>

## Group: SRG-APP-000340-AS-000185

**Group ID:** `V-250342`

### Rule: Users in a reader-role must be authorized.

**Rule ID:** `SV-250342r961353_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The reader role is a management role that allows read-only access to select administrative REST APIs as well as the Admin Center UI (adminCenter-1.0). Preventing non-privileged users from viewing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Users granted reader role access must be authorized.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a user with access to the ${server.config.dir}/server.xml file. Review the contents and identify if users have been granted the reader-role. grep -i reader-role ${server.config.dir}/server.xml If the reader-role has been created, users in that role must be documented and approved. If users in the reader-role are not approved, this is a finding. EXAMPLE: <featureManager><feature>appSecurity-2.0</feature></featureManager> <reader-role> <group>group</group> <group-access-id>group:realmName/groupUniqueId</group-access-id> <user>user</user> <user-access-id>user:realmName/userUniqueId</user-access-id> </reader-role>

## Group: SRG-APP-000357-AS-000038

**Group ID:** `V-250343`

### Rule: The WebSphere Liberty Server must allocate JVM log record storage capacity in accordance with organization-defined log record storage requirements.

**Rule ID:** `SV-250343r961392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>JVM logs are logs used to store application and runtime related events, rather than audit related events. They are mainly used to diagnose application or runtime bugs. However, they are useful for providing more context when correlated with audit related events. By default, Liberty automatically logs the console.log, messages.log, and trace.log but these default settings must be validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ${server.config.dir}/bootstrap.properties file, verify console logging is not turned off. If the property com.ibm.ws.logging.console.log.level=OFF, this is a finding. Review the ${server.config.dir}/server.xml file and verify the logging traceSpecification setting is configured according to system capacity requirements. If the logging traceSpecification settings are not configured, this is a finding. EXAMPLE: <logging traceSpecification="*=info=enabled:my.package.*=all" maxFileSize="40" maxFiles="20"/>

## Group: SRG-APP-000380-AS-000088

**Group ID:** `V-250344`

### Rule: The server.xml file must be protected from unauthorized modification.

**Rule ID:** `SV-250344r961461_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with access restrictions pertaining to change control, it should be noted that any changes to the software, and/or application server configuration could potentially have significant adverse effects on the overall security of the system. Protect the server.xml file from unauthorized modification by applying file permission restrictions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a privileged user with local file access to ${server.config.dir}/server.xml, verify the server.xml file permissions are set to 660. If the server.xml file permissions are not set to 660, this is a finding.

## Group: SRG-APP-000400-AS-000246

**Group ID:** `V-250345`

### Rule: The WebSphere Liberty Server must prohibit the use of cached authenticators after an organization-defined time period.

**Rule ID:** `SV-250345r961521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Larger authentication cache timeout values can increase security risks. For example, a user who is revoked can still log in by using a credential that is cached in the authentication cache until the cache is refreshed. Smaller authentication cache timeout values can affect performance. When this value is smaller, the Liberty Server accesses the user registry or repository more frequently. Larger numbers of entries in the authentication cache, which is caused by an increased number of users, increases the memory usage of the authentication cache. Thus, the application server might slow down and affect performance. If cached authentication information is out of date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system security plan and identify the cache timeout parameters for authentication. The value for admin timeout is 10 minutes. However, a case-by-case exception based on operational requirements can be configured with AO acceptance. As a privileged user with access to server.xml, review the file and verify the authCache timeout parameter is configured for 10 minutes. grep -i authcache server.xml EXAMPLE: <authCache initialSize="100" maxSize="50000" timeout="10m"/> If the authCache timeout parameter is not configured for 10 minutes, or the AO has not accepted the risk for extending the timeout period specified, this is a finding.

## Group: SRG-APP-000428-AS-000265

**Group ID:** `V-250346`

### Rule: The WebSphere Liberty Server LTPA keys password must be changed.

**Rule ID:** `SV-250346r1067567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The default location of the automatically generated Lightweight Third Party Authentication (LTPA) keys file is ${server.output.dir}/resources/security/ltpa.keys. The LTPA keys are encrypted with a randomly generated key and a default password of WebAS is initially used to protect the keys. The password is required when importing the LTPA keys into another server. To protect the security of the LTPA keys, change the password. When the LTPA keys are exchanged between servers, this password must match across the servers for Single Sign On (SSO) to work. Automated LTPA key generation can create unplanned outages. Plan to change the LTPA keys during a scheduled outage and do not use automated key changes. Distribute the new keys to all nodes in the cell and to all external systems/cells during this outage window.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If LTPA is not used, this requirement is not a finding. As a privileged user with access to ${server.config.dir}/server.xml file, review the server.xml file and locate LTPA settings. If the LTPA settings do not exist, this is not a finding. EXAMPLE: grep -i "<ltpa" server.xml <ltpa keysFileName="LTPA.keys" keysPassword="myLTPAkeysPassword" expiration="120" monitorInterval="5s" /> If the LTPA setting exists and the password is set to "WebAS", this is a finding.

## Group: SRG-APP-000439-AS-000274

**Group ID:** `V-250347`

### Rule: The WebSphere Liberty Server must remove all export ciphers to protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-250347r961632_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Export grade encryption suites are not strong and do not meet DoD requirements. The encryption for the session becomes easy for the attacker to break. Do not use export grade encryption.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ${server.config.dir}/server.xml file and check the "enabledCiphers" setting. If any of the ciphers specified in the enabledCiphers setting contains the word "EXPORT", this is a finding. <ssl id="myDefaultSSLConfig" keyStoreRef="defaultKeyStore" trustStoreRef="defaultTrustStore" clientAuthentication="true" sslProtocol="TLS" enabledCiphers="SSL_xxx_yyy_zzz"/>

## Group: SRG-APP-000440-AS-000167

**Group ID:** `V-250348`

### Rule: The WebSphere Liberty Server must be configured to use HTTPS only.

**Rule ID:** `SV-250348r961635_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Transmission of data can take place between the application server and a large number of devices/applications external to the application server. Examples are a web client used by a user, a backend database, a log server, or other application servers in an application server cluster.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ${server.config.dir}/server.xml file and check the ssl-1.0 feature and httpEndpoint settings. If the ssl-1.0 feature is not defined, this is a finding. If the httpEndpoint settings do not include ssloptions, this is a finding. <featureManager> <feature>servlet-3.0</feature> <feature>ssl-1.0</feature> <feature>appSecurity-2.0</feature> </featureManager> <httpEndpoint id="defaultHttpEndpoint" host="localhost" httpPort="${bvt.prop.HTTP_default}" httpsPort="${bvt.prop.HTTP_default.secure}" > <tcpOptions soReuseAddr="true" /> <sslOptions sslRef="testSSLConfig" /> </httpEndpoint>

## Group: SRG-APP-000456-AS-000266

**Group ID:** `V-250349`

### Rule: The WebSphere Liberty Server must install security-relevant software updates within the time period directed by an authoritative source.

**Rule ID:** `SV-250349r961683_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security vulnerabilities are often addressed by testing and applying the latest security patches and fix packs. The latest fixpacks can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg27009661</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the "productInfo(.bat/.sh) version" command to determine the WebSphere version. Review the patch level and fix pack. Review the latest fixpacks at: http://www-01.ibm.com/support/docview.wss?uid=swg27009661 and determine if the system is operating at the latest patch level. If the most recent patches/fix packs have not been applied, this is a finding.

## Group: SRG-APP-000499-AS-000224

**Group ID:** `V-250350`

### Rule: The WebSphere Liberty Server must generate log records for authentication and authorization events.

**Rule ID:** `SV-250350r961812_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling authentication (SECURITY_AUTHN) and authorization (SECURITY_AUTHZ) event handlers configures the server to record security authorization and authentication events. By logging these events, the logs can be analyzed to identify activity that could be related to security events and to aid post mortem forensic analysis. Satisfies: SRG-APP-000499-AS-000224, SRG-APP-000495-AS-000220, SRG-APP-000503-AS-000228, SRG-APP-000504-AS-000229, SRG-APP-000505-AS-000230, SRG-APP-000506-AS-000231, SRG-APP-000509-AS-000234, SRG-APP-000092-AS-000053</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ${server.config.dir}/server.xml file, verify the audit-1.0 feature is enabled. Also verify the auditFile Handler is configured to log AUTHN and AUTHZ events. If the audit1.0 feature is not enabled, this is a finding. If the SECURITY_AUTHN and SECURITY_AUTHZ event handlers are not configured, this is a finding. <featureManager> <feature>audit-1.0</feature> </featureManager> <auditFileHandler> <events name="AllAuthn" eventName="SECURITY_AUTHN" /> <events name="AllAuthz" eventName="SECURITY_AUTHZ" /> </auditFileHandler>

