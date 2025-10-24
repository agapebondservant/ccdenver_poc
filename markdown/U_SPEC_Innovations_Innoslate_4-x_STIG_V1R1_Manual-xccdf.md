# STIG Benchmark: SPEC Innovations Innoslate 4.x Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000003

**Group ID:** `V-254086`

### Rule: Innoslate must initiate a session lock after a 15-minute period of inactivity.

**Rule ID:** `SV-254086r845234_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system, but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their application session prior to vacating the vicinity, applications need to be able to identify when a user's application session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. This is typically at the operating system-level and results in a system lock, but may be at the application-level where the application interface window is secured instead. Satisfies: SRG-APP-000003, SRG-APP-000190, SRG-APP-000390</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Enter the web.xml file located at C:\Innoslate4\apache-tomcat\webapps\Innoslate4\WEB-INF. 2. Search (Ctrl+f) for "session-timeout" object (typically found on line 8). 3. Verify time is set to 15 minutes, if not , this is a finding.

## Group: SRG-APP-000014

**Group ID:** `V-254087`

### Rule: Innoslate must use TLS 1.2, at a minimum, to protect the confidentiality of sensitive data during electronic dissemination using remote access.

**Rule ID:** `SV-254087r845265_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Using older unauthorized versions or incorrectly configuring protocol negotiation makes the gateway vulnerable to known and unknown attacks that exploit vulnerabilities in this protocol. This requirement applies to Transport Layer Security (TLS) gateways (also known as Secure Sockets Layer [SSL] gateways), web servers, and web applications and is not applicable to virtual private network (VPN) devices. Application protocols such as HTTPS and DNSSEC use TLS as the underlying security protocol and thus are in scope for this requirement. NIST SP 800-52 provides guidance for client negotiation on either DoD-only or on public-facing servers. Satisfies: SRG-APP-000014, SRG-APP-000156, SRG-APP-000179, SRG-APP-000442, SRG-APP-000555, SRG-APP-000560, SRG-APP-000565, SRG-APP-000605, SRG-APP-000635, SRG-APP-000645, SRG-APP-000219</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Consult the System Administrator if needed to determine the location of the Apache Tomcat server.xml file and the network port that was specified during installation for use with Innoslate. The default is 8443; other AO-approved ports may be used. 2. Open the server.xml file with a text editor, and locate the <Connector/> element. The following is an example: Connector port="8443" protocol="org.apache.coyote.http11.Http11NioProtocol" maxThreads="150" SSLEnabled="true" scheme="https" secure="true" clientAuth="false" SSLProtocol="TLSv1.2" keystoreFile="$keystorepath" keystorePass="123456" keyAlias="tomcatssl" / If "port" is not set to 8443, or other AO-approved port, this is a finding. If "protocol" is not set to "org.apache.coyote.http11.Http11NioProtocol", this is a finding. If "SSLEnabled" is not set to "true", this is a finding. If "scheme" is not set to "https", this is a finding. If "secure" is not set to "true", this is a finding. If "SSLProtocol"or "SSLEnabledProtocols" is not set to "TLSv1.2", this is a finding. The name of this flag varies with Tomcat versions.

## Group: SRG-APP-000023

**Group ID:** `V-254088`

### Rule: Innoslate must provide automated mechanisms for supporting account management functions.

**Rule ID:** `SV-254088r845240_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enterprise environments make application account management challenging and complex. A manual process for account management functions adds the risk of a potential oversight or other error. A comprehensive application account management process that includes automation helps to ensure accounts designated as requiring attention are consistently and promptly addressed. Examples include, but are not limited to, using automation to take action on multiple accounts designated as inactive, suspended or terminated or by disabling accounts located in non-centralized account stores such as multiple servers. This requirement applies to all account types, including individual/user, shared, group, system, guest/anonymous, emergency, developer/manufacturer/vendor, temporary, and service. The application must be configured to automatically provide account management functions and these functions must immediately enforce the organization's current account policy. The automated mechanisms may reside within the application itself or may be offered by the operating system or other infrastructure providing automated account management capabilities. Automated mechanisms may be comprised of differing technologies that when placed together contain an overall automated mechanism supporting an organization's automated account management requirements. Account management functions include assignment of group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. The use of automated mechanisms can include, for example using email or text messaging to automatically notify account managers when users are terminated or transferred; using the information system to monitor account usage; and using automated telephonic notification to report atypical system account usage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Enter the settings.properties file located at C:\Innoslate4\apache-tomcat\webapps\Innoslate4\WEB-INF. 2. Find the "default organization" field. 3. Enter the default organization name to automatically add users to once they sign in. 4. Find the "Email notifications" fields. 5. Verify the email information is correct. If not, this is a finding.

## Group: SRG-APP-000033

**Group ID:** `V-254089`

### Rule: Innoslate must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.

**Rule ID:** `SV-254089r845243_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., networks, web servers, and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. This requirement is applicable to access control enforcement applications (e.g., authentication servers) and other applications that perform information and system access control functions. Steps to prove capability: 1. Sign in as admin. 2. Enter the admin dashboard. 3. Select the respective org name on the left. 4. View the users and validate the correct permissions are applied. 5. View the roles and validate they are correct. 6. Enter a project. 7. Click "Share". 8. Verify the correct users are shared with the correct roles to the project. Satisfies: SRG-APP-000033, SRG-APP-000039, SRG-APP-000090, SRG-APP-000343</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Sign in With Admin Account. 2. Enter Admin Dashboard. 3. Click on the "Organization" tab. 4. Find the "Roles" section. 5. Select the role to verify. 6. Ensure Administrative roles are separated from End User roles. Otherwise, this is a finding.

## Group: SRG-APP-000038

**Group ID:** `V-254090`

### Rule: Innoslate must enforce approved authorizations for controlling the flow of information within the system based on organization-defined information flow control policies.

**Rule ID:** `SV-254090r845246_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A mechanism to detect and prevent unauthorized communication flow must be configured or provided as part of the system design. If information flow is not enforced based on approved authorizations, the system may become compromised. Information flow control regulates where information is allowed to travel within a system and between interconnected systems. The flow of all system information must be monitored and controlled so it does not introduce any unacceptable risk to the systems or data. Application specific examples of enforcement occurs in systems that employ rule sets or establish configuration settings that restrict information system services, or message-filtering capability based on message content (e.g., implementing key word searches or using document characteristics). Applications providing information flow control must be able to enforce approved authorizations for controlling the flow of information within the system in accordance with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Sign in as owner of project. 2. Enter Schema Editor. 3. Click "Workflow". 4. Verify permissions are applied to the workflow classes specified. If not, this is a finding.

## Group: SRG-APP-000070

**Group ID:** `V-254091`

### Rule: The publicly accessible application must display the Standard Mandatory DoD Notice and Consent Banner before granting access to Innoslate.

**Rule ID:** `SV-254091r845249_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible application ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with DTM-08-060. Use the following verbiage for desktops, laptops, and other devices accommodating banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." Satisfies: SRG-APP-000070, SRG-APP-000068, SRG-APP-000069</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Sign in to Innoslate. 2. Enter a project. 3. If the DoD Banner does not appear correctly, this is a finding.

## Group: SRG-APP-000091

**Group ID:** `V-254092`

### Rule: Innoslate must generate comprehensive audit records.

**Rule ID:** `SV-254092r845252_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). 1. Access Innoslate folder. 2. Navigate to Innoslate4\apache-tomcat\logs. 3. View the access logs. Satisfies: SRG-APP-000091, SRG-APP-000092, SRG-APP-000095, SRG-APP-000096, SRG-APP-000097, SRG-APP-000492, SRG-APP-000493, SRG-APP-000494, SRG-APP-000504, SRG-APP-000505, SRG-APP-000506, SRG-APP-000507, SRG-APP-000508, SRG-APP-000509, SRG-APP-000510</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Locate the logging.properties file in the following directory: Innoslate\apache-tomcat\conf. 2. Search "level", and check corresponding lines for the correct verbosity settings. If they are incorrect after a change, save, and service restart, this is a finding. Below is an example of the contents of the default logging.properties file. "# Licensed to the Apache Software Foundation (ASF) under one or more # contributor license agreements. See the NOTICE file distributed with # this work for additional information regarding copyright ownership. # The ASF licenses this file to You under the Apache License, Version 2.0 # (the "License"); you may not use this file except in compliance with # the License. You may obtain a copy of the License at # # http://www.apache.org/licenses/LICENSE-2.0 # # Unless required by applicable law or agreed to in writing, software # distributed under the License is distributed on an "AS IS" BASIS, # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. # See the License for the specific language governing permissions and # limitations under the License. handlers = 1catalina.org.apache.juli.AsyncFileHandler, 2localhost.org.apache.juli.AsyncFileHandler, 3manager.org.apache.juli.AsyncFileHandler, 4host-manager.org.apache.juli.AsyncFileHandler, java.util.logging.ConsoleHandler .handlers = 1catalina.org.apache.juli.AsyncFileHandler, java.util.logging.ConsoleHandler ############################################################ # Handler specific properties. # Describes specific configuration info for Handlers. ############################################################ 1catalina.org.apache.juli.AsyncFileHandler.level = FINE 1catalina.org.apache.juli.AsyncFileHandler.directory = ${catalina.base}/logs 1catalina.org.apache.juli.AsyncFileHandler.prefix = catalina. 2localhost.org.apache.juli.AsyncFileHandler.level = FINE 2localhost.org.apache.juli.AsyncFileHandler.directory = ${catalina.base}/logs 2localhost.org.apache.juli.AsyncFileHandler.prefix = localhost. 3manager.org.apache.juli.AsyncFileHandler.level = FINE 3manager.org.apache.juli.AsyncFileHandler.directory = ${catalina.base}/logs 3manager.org.apache.juli.AsyncFileHandler.prefix = manager. 4host-manager.org.apache.juli.AsyncFileHandler.level = FINE 4host-manager.org.apache.juli.AsyncFileHandler.directory = ${catalina.base}/logs 4host-manager.org.apache.juli.AsyncFileHandler.prefix = host-manager. java.util.logging.ConsoleHandler.level = FINE java.util.logging.ConsoleHandler.formatter = org.apache.juli.OneLineFormatter ############################################################ # Facility specific properties. # Provides extra control for each logger. ############################################################ org.apache.catalina.core.ContainerBase.[Catalina].[localhost].level = INFO org.apache.catalina.core.ContainerBase.[Catalina].[localhost].handlers = 2localhost.org.apache.juli.AsyncFileHandler org.apache.catalina.core.ContainerBase.[Catalina].[localhost].[/manager].level = INFO org.apache.catalina.core.ContainerBase.[Catalina].[localhost].[/manager].handlers = 3manager.org.apache.juli.AsyncFileHandler org.apache.catalina.core.ContainerBase.[Catalina].[localhost].[/host-manager].level = INFO org.apache.catalina.core.ContainerBase.[Catalina].[localhost].[/host-manager].handlers = 4host-manager.org.apache.juli.AsyncFileHandler # For example, set the org.apache.catalina.util.LifecycleBase logger to log # each component that extends LifecycleBase changing state: #org.apache.catalina.util.LifecycleBase.level = FINE # To see FINE messages in TldLocationsCache, uncomment the following line: #org.apache.jasper.compiler.TldLocationsCache.level = FINE # To see FINE messages for HTTP/2 handling, uncomment the following line: #org.apache.coyote.http2.level = FINE # To see FINE messages for WebSocket handling, uncomment the following line: #org.apache.tomcat.websocket.level = FINE"

## Group: SRG-APP-000149

**Group ID:** `V-254093`

### Rule: Innoslate must use multifactor authentication for network access to privileged and non-privileged accounts.

**Rule ID:** `SV-254093r845255_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: (i) Something a user knows (e.g., password/PIN); (ii) Something a user has (e.g., cryptographic identification device, token); or (iii) Something a user is (e.g., biometric). A privileged account is defined as an information system account with authorizations of a privileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the internet). Satisfies: SRG-APP-000149, SRG-APP-000024, SRG-APP-000025, SRG-APP-000026, SRG-APP-000027, SRG-APP-000028, SRG-APP-000029, SRG-APP-000065, SRG-APP-000148, SRG-APP-000150, SRG-APP-000151, SRG-APP-000152, SRG-APP-000153, SRG-APP-000157, SRG-APP-000163, SRG-APP-000164, SRG-APP-000165, SRG-APP-000166, SRG-APP-000167, SRG-APP-000168, SRG-APP-000169, SRG-APP-000170, SRG-APP-000173, SRG-APP-000174, SRG-APP-000175, SRG-APP-000176, SRG-APP-000291, SRG-APP-000292, SRG-APP-000293, SRG-APP-000294, SRG-APP-000295, SRG-APP-000318, SRG-APP-000319, SRG-APP-000320, SRG-APP-000356, SRG-APP-000391, SRG-APP-000392, SRG-APP-000397, SRG-APP-000401, SRG-APP-000402, SRG-APP-000403, SRG-APP-000404, SRG-APP-000405, SRG-APP-000427</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Enter the settings.properties file located at C:\Innoslate4\apache-tomcat\webapps\Innoslate4\WEB-INF. 2. Find the LDAP fields. 3. Verify LDAP information is correct. If not, this is a finding. The LDAP Fields should look (not exactly) like this: " LDAP_INITIAL_CONTEXT_FACTORY = com.sun.jndi.ldap.LdapCtxFactory LDAP_PROVIDER_URLS = ldap://providerUrl.com LDAP_SECURITY_AUTHENTICATION = none LDAP_SECURITY_PRINCIPAL = CN=Admin Innoslate,CN=Users,DC=Innoslateactive,DC=com LDAP_SECURITY_CREDENTIALS = password LDAP_USER_CONTEXT = CN=Users,DC=Innoslateactive,DC=com LDAP_USER_OBJECT_CLASS = user LDAP_USER_UID_ATTRIBUTE = sAMAccountName LDAP_CONNECT_TIMEOUT = 1000 LDAP_READ_TIMEOUT = 5000 LDAP_USER_EMAIL_ATTRIBUTE = mail LDAP_USER_FIRST_NAME_ATTRIBUTE = givenName LDAP_USER_LAST_NAME_ATTRIBUTE = sn LDAP_USER_PHONE_NUMBER_ATTRIBUTE = telephoneNumber LDAP_USER_COMPANY_ATTRIBUTE = company LDAP_USER_SEARCH_FILTER = (&(objectClass=user)(sAMAccountName={0})(!(userAccountControl:1.2.840.113556.1.4.803:=2))) "

## Group: SRG-APP-000177

**Group ID:** `V-254094`

### Rule: Innoslate must map the authenticated identity to the individual user or group account for PKI-based authentication.

**Rule ID:** `SV-254094r845258_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without mapping the certificate used to authenticate to the user account, the ability to determine the identity of the individual user or group will not be available for forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the settings.properties file [Path] and verify the AUTHENTICATION_TYPE is set to "CAC". If AUTHENTICATION_TYPE is not set to "CAC", this is a finding.

## Group: SRG-APP-000358

**Group ID:** `V-254095`

### Rule: Innoslate must off-load audit records onto a different system or media than the system being audited.

**Rule ID:** `SV-254095r845261_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Access the logging.properties file in the logs directory of the Innoslate files. 2. Verify the ____.apache.juli.AsyncFileHandler.directory field is set to a directory on a different system. Otherwise, this is a finding.

## Group: SRG-APP-000495

**Group ID:** `V-254096`

### Rule: Innoslate must generate audit records when DoD required events occur.

**Rule ID:** `SV-254096r845264_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). 1. Access Innoslate folder. 2. Navigate to Innoslate4\apache-tomcat\logs. 3. View the logs. Satisfies: SRG-APP-000495, SRG-APP-000496, SRG-APP-000497, SRG-APP-000498, SRG-APP-000499, SRG-APP-000500, SRG-APP-000501, SRG-APP-000502, SRG-APP-000503</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Locate the logging.properties file in the following directory: Innoslate\apache-tomcat\conf. 2. Modify lines 25, 29, 33, and 41 to be set to DEBUG or VERBOSE as needed. 3. If after a service restart the logs do not change, this is a finding.

