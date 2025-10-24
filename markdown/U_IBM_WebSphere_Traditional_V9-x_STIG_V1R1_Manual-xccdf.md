# STIG Benchmark: IBM WebSphere Traditional V9.x Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-AS-000001

**Group ID:** `V-81193`

### Rule: The WebSphere Application Server maximum in-memory session count must be set according to application requirements.

**Rule ID:** `SV-95907r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application management includes the ability to control the number of sessions that utilize an application by all accounts and/or account types. Limiting the number of allowed sessions is helpful in limiting risks related to Denial of Service attacks. Application servers host and expose business logic and application processes. The application server must possess the capability to limit the maximum number of concurrent sessions in a manner that affects the entire application server or on an individual application basis. Although there is some latitude concerning the settings themselves, the settings should follow DoD-recommended values, but the settings should be configurable to allow for future DoD direction. While the DoD will specify recommended values, the values can be adjusted to accommodate the operational requirement of a given system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation. Identify the application session requirements. In the administrative console page, click Servers >> Server Types >> WebSphere application servers >> [server_name] >> Session management. Ensure the Maximum in-memory session count field is set to the number of sessions allowable. If not set according to application requirements, this is a finding.

## Group: SRG-APP-000295-AS-000263

**Group ID:** `V-81195`

### Rule: The WebSphere Application Server admin console session timeout must be configured.

**Rule ID:** `SV-95909r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An attacker can take advantage of user sessions that are left open, thus bypassing the user authentication process. To thwart the vulnerability of open and unused user sessions, the application server must be configured to close the sessions when a configured condition or trigger event is met. Session termination terminates all processes associated with a user's logical session except those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan and system configuration documentation. Access the Deployment Manager (DMGR) operating system. Locate the deployment.xml file. The default file location where deployment.xml is installed are provided below. UNIX: /opt/IBM/WebSphere/Profiles/DefaultDmgr01/config/cells/<CELL NAME>/applications/isclite.ear/deployments/isclite/ Windows: C:\Program Files\IBM\WebSphere\Profiles\DefaultDmgr01\config\cells\<CELL NAME>\applications\isclite.ear\deployments\isclite\ Search the deployment.xml file for the string, "invalidationtimeout=" UNIX: grep -i invalidationtimeout $PATH/deployment.xml Windows: findstr -I invalidationtimeout= $PATH\deployment.xml The value is expressed in minutes and the default value is set to "30 minutes". If "invalidationtimeout" is not set to "10 minutes", this is a finding.

## Group: SRG-APP-000016-AS-000013

**Group ID:** `V-81197`

### Rule: The WebSphere Application Server automatic repository checkpoints must be enabled to track configuration changes.

**Rule ID:** `SV-95911r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without enabling repository checkpoints, you will not be able to determine the history of changes to WebSphere configuration files, and who made those changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation. Identify the required "Automatic CheckPoint Depth" setting that has been defined. From administrative console, click System administration >> Extended repository service. If "Enable automatic repository checkpoints" is not selected or if the "automatic checkpoint depth" is less than the number of saves defined in the System Security Plan, this is a finding.

## Group: SRG-APP-000315-AS-000094

**Group ID:** `V-81199`

### Rule: The WebSphere Application Server administrative security must be enabled.

**Rule ID:** `SV-95913r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>In previous releases of WebSphere® Application Server, when a user enabled global security, both administrative and application security were enabled. The previous notion of global security is split into administrative security and application security, each of which you can enable separately. As a result of this split, WebSphere Application Server clients must know whether application security is disabled at the target server. Administrative security is enabled, by default. Application security is disabled, by default. Before you can enable application security, you must verify that administrative security is enabled. Application security is in effect only when administrative security is enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the administrative console, click Security >> Global Security. If "Enable administrative security" is not selected, this is a finding.

## Group: SRG-APP-000315-AS-000095

**Group ID:** `V-81201`

### Rule: The WebSphere Application Server bus security must be enabled.

**Rule ID:** `SV-95915r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A service integration bus is a group of one or more application servers or server clusters in a WebSphere® Application Server cell that cooperate to provide asynchronous messaging services. The application servers or server clusters in a bus are known as bus members. When a bus is created with bus security enabled, the following conditions apply: The bus requires client authentication. The bus enforces authorization policy. The bus requires use of SSL transport chains.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation. Interview the system administrator. Identify the service integration buses configured on the WAS. If there are no service integration buses, this requirement is NA. From the administration console, navigate to Security >> Bus Security. For each service integration bus, if security is not enabled, this is a finding.

## Group: SRG-APP-000016-AS-000013

**Group ID:** `V-81203`

### Rule: The WebSphere Application Server security auditing must be enabled.

**Rule ID:** `SV-95917r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security auditing will not be performed unless the audit security subsystem has been enabled. Global security must be enabled for the security audit subsystem to function, as no security auditing occurs if global security is not also enabled. Enable global security before enabling security auditing. Satisfies: SRG-APP-000016-AS-000013, SRG-APP-000343-AS-000030, SRG-APP-000080-AS-000045, SRG-APP-000092-AS-000053, SRG-APP-000266-AS-000168, SRG-APP-000267-AS-000170</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the administrative console, navigate to Security >> Security auditing. If "Enable security auditing" is not enabled, this is a finding.

## Group: SRG-APP-000016-AS-000013

**Group ID:** `V-81205`

### Rule: The WebSphere Application Server groups in the user registry mapped to WebSphere auditor roles must be configured in accordance with the security plan.

**Rule ID:** `SV-95919r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Logging must be utilized in order to track system activity, assist in diagnosing system issues, and provide evidence needed for forensic investigations post security incident. Remote access by administrators requires that the admin activity be logged. Application servers provide a web and command line-based remote management capability for managing the application server. Application servers must ensure that all actions related to administrative functionality such as application server configuration are logged. Satisfies: SRG-APP-000016-AS-000013, SRG-APP-000343-AS-000030</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation. Identify groups and roles. In the administrative console, navigate to Users and Groups >> Administrative Group Roles. Check the roles for each group and compare to System Security Plan. If any group is not authorized by the ISSO/ISSM to be in an auditor role, this is a finding.

## Group: SRG-APP-000016-AS-000013

**Group ID:** `V-81207`

### Rule: The WebSphere Application Server users in the WebSphere auditor role must be configured in accordance with the System Security Plan.

**Rule ID:** `SV-95921r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Logging must be utilized in order to track system activity, assist in diagnosing system issues, and provide evidence needed for forensic investigations post security incident. Remote access by administrators requires that the admin activity be logged. Application servers provide a web and command line-based remote management capability for managing the application server. Application servers must ensure that all actions related to administrative functionality such as application server configuration are logged. Satisfies: SRG-APP-000016-AS-000013, SRG-APP-000343-AS-000030, SRG-APP-000090-AS-000051</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation. Identify users and roles. In the administrative console, navigate to Users and Groups >> Administrative User Roles. Check the roles for each user. If any user is not authorized by the ISSO/ISSM to be in the role of an auditor, this is a finding.

## Group: SRG-APP-000016-AS-000013

**Group ID:** `V-81209`

### Rule: The WebSphere Application Server audit event type filters must be configured.

**Rule ID:** `SV-95923r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Logging must be utilized in order to track system activity, assist in diagnosing system issues, and provide evidence needed for forensic investigations post security incident. Remote access by administrators requires that the admin activity be logged. Application servers provide a web and command line-based remote management capability for managing the application server. Application servers must ensure that all actions related to administrative functionality such as application server configuration are logged. Satisfies: SRG-APP-000016-AS-000013, SRG-APP-000343-AS-000030, SRG-APP-000089-AS-000050, SRG-APP-000495-AS-000220, SRG-APP-000499-AS-000224, SRG-APP-000503-AS-000228, SRG-APP-000504-AS-000229, SRG-APP-000505-AS-000230, SRG-APP-000506-AS-000231, SRG-APP-000093-AS-000054, SRG-APP-000095-AS-000056, SRG-APP-000097-AS-000060, SRG-APP-000098-AS-000061, SRG-APP-000099-AS-000062, SRG-APP-000100-AS-000063, SRG-APP-000101-AS-000072, SRG-APP-000381-AS-000089, SRG-APP-000080-AS-000045</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the administrative console, navigate to Security >> Security auditing >> Event type Filters. Verify the following events and outcomes are enabled in the "Events and Outcomes" box. Also note the name of the filter associated with these events. This name will be referenced in STIG ID WBSP-AS-000110. AUTHN: SUCCESS,INFO,WARNING,ERROR,DENIED,REDIRECT AUTHZ: SUCCESS,INFO,WARNING,ERROR,DENIED,REDIRECT AUTHN_TERMINATE: SUCCESS,INFO,WARNING,ERROR,DENIED,REDIRECT REPOSITORY_SAVE: SUCCESS,INFO,WARNING,ERROR,DENIED,REDIRECT If these audit filters are not configured in "Events and Outcomes", this is a finding.

## Group: SRG-APP-000016-AS-000013

**Group ID:** `V-81211`

### Rule: The WebSphere Application Server audit service provider must be enabled.

**Rule ID:** `SV-95925r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Logging must be utilized in order to track system activity, assist in diagnosing system issues, and provide evidence needed for forensic investigations post security incident. Remote access by administrators requires that the admin activity be logged. Application servers provide a web and command line-based remote management capability for managing the application server. Application servers must ensure that all actions related to administrative functionality such as application server configuration are logged. Satisfies: SRG-APP-000016-AS-000013, SRG-APP-000343-AS-000030</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the administrative console, navigate to Security >> Security auditing >> Audit Service Provider [provider name]. Under "Enabled filters", determine if the filter name from select the name of the filter that was recorded from STIG ID WBSP-AS-000100. If the filter that was identified in STIG ID WBSP-AS-000100 is not enabled, this is a finding.

## Group: SRG-APP-000315-AS-000094

**Group ID:** `V-81213`

### Rule: The WebSphere Application Server users in a local user registry group must be authorized for that group.

**Rule ID:** `SV-95927r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application servers provide remote access capability and must be able to enforce remote access policy requirements or work in conjunction with enterprise tools designed to enforce policy requirements. Automated monitoring and control of remote access sessions allows organizations to detect cyber attacks and also ensure ongoing compliance with remote access policies by logging connection activities of remote users. Examples of policy requirements include, but are not limited to, authorizing remote access to the information system, limiting access based on authentication credentials, and monitoring for unauthorized access. Satisfies: SRG-APP-000315-AS-000094, SRG-APP-000380-AS-000088, SRG-APP-000133-AS-000092, SRG-APP-000033-AS-000024, SRG-APP-000153-AS-000104</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the systems user registry is managed by LDAP, this requirement is NA. Review the System Security Plan documentation. Interview the system administrator. Obtain a list of authorized users. In the administrative console, navigate to Users and Groups >> Manage Groups. Select each group. Select the "Members" tab. Validate the members of the group are authorized. If users in the group are not authorized by the ISSO/ISSM, this is a finding.

## Group: SRG-APP-000014-AS-000009

**Group ID:** `V-81215`

### Rule: The WebSphere Application Server Quality of Protection (QoP) must be set to use TLSv1.2 or higher.

**Rule ID:** `SV-95929r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Quality of Protection specifies the security level, ciphers, and mutual authentication settings for the Secure Socket Layer (SSL/TLS) configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the administrative console, navigate to Security >> SSL certificate and key management. Click "SSL configurations". Click on each SSL configuration to review. Under "Additional Properties", click "Quality of protection (QoP)" settings. If the "Protocol" field does not show "TLSv1.2 or greater", this is a finding.

## Group: SRG-APP-000014-AS-000009

**Group ID:** `V-81217`

### Rule: The WebSphere Application Server global application security must be enabled.

**Rule ID:** `SV-95931r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Application security enables security for the applications in your environment. This setting provides application isolation and meets security requirements such as using SSL for authenticating application users. In previous releases of WebSphere® Application Server, when a user enabled global security, both administrative and application security were enabled. The previous notion of global security is split into administrative security and application security, each of which you can enable separately. As a result of this split, WebSphere Application Server clients must know whether application security is disabled at the target server. Administrative security is enabled, by default. Application security is disabled, by default. Before you can enable application security, you must verify that administrative security is enabled. Application security is in effect only when administrative security is enabled. Satisfies: SRG-APP-000014-AS-000009, SRG-APP-000172-AS-000120</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the administrative console, navigate to Security >> Global Security. If "Enable administrative security" and "Enable application security" are not selected, this is a finding.

## Group: SRG-APP-000014-AS-000009

**Group ID:** `V-81219`

### Rule: The WebSphere Application Server Single Sign On (SSO) must have SSL enabled for Web and SIP Security.

**Rule ID:** `SV-95933r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Remote management access is accomplished by leveraging common communication protocols and establishing a remote connection to the application server via a network for the purposes of managing the application server. If cryptography is not used, then the session data traversing the remote connection could be intercepted and compromised. Types of management interfaces utilized by an application server include web-based HTTPS interfaces as well as command line-based management interfaces. Satisfies: SRG-APP-000014-AS-000009, SRG-APP-000172-AS-000120, SRG-APP-000158-AS-000108</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the administrative console, navigate to Security >> Global Security. Expand "Web and SIP security". Click on "Single sign-on (SSO)". If "requires SSL" is not selected, this is a finding.

## Group: SRG-APP-000015-AS-000010

**Group ID:** `V-81221`

### Rule: The WebSphere Application Server security cookies must be set to HTTPOnly.

**Rule ID:** `SV-95935r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web applications use cookies to track users across requests. These cookies, while typically not sensitive in themselves, connect you to your existing state on the back end system. If an intruder were to capture one of your cookies, they could potentially use the cookie to act as you. Important Web traffic should be encrypted using SSL. This includes important cookies. In the case of WebSphere Application Server, the most important cookie is the LTPA cookie, and therefore it should be configured to be sent only over SSL.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the administrative console, navigate to Security >> Global Security. Expand "Web and SIP security". Click on "Single sign-on (SSO)". If "Set security cookies to HTTPOnly" is not selected, this is a finding.

## Group: SRG-APP-000033-AS-000024

**Group ID:** `V-81223`

### Rule: The WebSphere Application Server Java 2 security must be enabled.

**Rule ID:** `SV-95937r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Java 2 security provides a policy-based fine grained access control mechanism that increases overall system integrity by checking for permissions before allowing access to certain protected system resources. Java 2 Security is independent on J2EE role-based authorization. Java 2 Security guards access to system resources such as file input and output, sockets, and properties, whereas J2EE security guards access to Web resources such as servlets and JSP files. Administrators should understand the possible consequences of enabling Java 2 Security if applications are not prepared for Java 2 Security. Java 2 Security places some new requirements on application developers and administrators. Admins need to make sure that all the applications are granted the required permissions; otherwise, applications may fail to run. By default, applications are granted the permissions recommended in the J2EE 1.3 Specification. For details of default permissions granted to applications in WebSphere, please refer to the following policy files: /QIBM/ProdData/Java400/jdk14/lib/security/java.policy /QIBM/UserData/WebASE51/ASE/instance/properties/server.policy /QIBM/UserData/WebASE51/ASE/instance/config/cells/cell/nodes/node/app.policy where instance is the name of your instance, cell is the name of your cell, and node is the name of your node.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the admin console, select Security >> Global Security >> Java 2 Security. If "Use Java 2 security to restrict application access to local resources" is not selected, this is a finding.

## Group: SRG-APP-000033-AS-000024

**Group ID:** `V-81225`

### Rule: The WebSphere Application Server Java 2 security must not be bypassed.

**Rule ID:** `SV-95939r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>WebSphere provides a passive filter mechanism that will allow administrators to set Java 2 security in the admin console as enabled while still allowing applications to access host resources. This setting bypasses the enforcement of Java2 security. Application access is allowed and activity is logged to the system.out file. This feature is to aid in the identification of application access requirements to the underlying host so security policies can be created. This feature is executed via a custom property that is set for each application server instance operating on the WebSphere server. This setting should only be enabled in a development or testing environment in order to identify what applications access requirements are so security policies can then be created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is a development or test system, this requirement is NA. From the admin console, select Servers >> Server Types >> WebSphere application servers. For each application server, select Server Infrastructure >> Administration >> Custom properties. If the "com.ibm.websphere.java2secman.norethrow" resource value exists and is set to "true", this is a finding.

## Group: SRG-APP-000033-AS-000024

**Group ID:** `V-81227`

### Rule: The WebSphere Application Server users in the admin role must be authorized.

**Rule ID:** `SV-95941r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Strong access controls are critical to securing the application server. Access control policies (e.g., identity-based policies, role-based policies, attribute-based policies) and access enforcement mechanisms (e.g., access control lists, access control matrices, cryptography) must be employed by the application server to control access between users (or processes acting on behalf of users) and objects (e.g., applications, files, records, processes, application domains) in the application server. Without stringent logical access and authorization controls, an adversary may have the ability, with very little effort, to compromise the application server and associated supporting infrastructure. Satisfies: SRG-APP-000033-AS-000024, SRG-APP-000380-AS-000088, SRG-APP-000340-AS-000185</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation. In the administrative console, navigate to Users and Groups >> Administrative user roles. If users assigned to the admin role are not authorized by the ISSO/ISSM, this is a finding.

## Group: SRG-APP-000033-AS-000024

**Group ID:** `V-81229`

### Rule: The WebSphere Application Server LDAP groups must be authorized for the WebSphere role.

**Rule ID:** `SV-95943r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Strong access controls are critical to securing the application server. Access control policies (e.g., identity-based policies, role-based policies, attribute-based policies) and access enforcement mechanisms (e.g., access control lists, access control matrices, cryptography) must be employed by the application server to control access between users (or processes acting on behalf of users) and objects (e.g., applications, files, records, processes, application domains) in the application server. Without stringent logical access and authorization controls, an adversary may have the ability, with very little effort, to compromise the application server and associated supporting infrastructure. Satisfies: SRG-APP-000033-AS-000024, SRG-APP-000267-AS-000170</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation. Review details regarding LDAP groups that are mapped to WebSphere roles. In the administrative console, under Users and Groups >> Administrative group roles. If there is a LDAP group or groups assigned to a WebSphere role that has not been authorized by the ISSO/ISSM, this is a finding.

## Group: SRG-APP-000340-AS-000185

**Group ID:** `V-81231`

### Rule: The WebSphere Application Server users in a LDAP user registry group must be authorized for that group.

**Rule ID:** `SV-95945r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Restricting non-privileged users also prevents an attacker, who has gained access to a non-privileged account, from elevating privileges, creating accounts, and performing system checks and maintenance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If a file based or local federated repository is in use, this requirement is NA. Review System Security Plan documentation. Interview the system administrator. In the administrative console select Security >> Global Security. Under "User Account Repository", verify the "Available realm Definition" is set to "Standalone LDAP registry". Select "Configure". The properties of the LDAP repository are displayed for purposes of identifying the LDAP server. Work with the admin of LDAP repository. Identify users and groups. Validate members of groups are authorized. If the group members have not been authorized by the ISSO/ISSM, this is a finding.

## Group: SRG-APP-000068-AS-000035

**Group ID:** `V-81233`

### Rule: The WebSphere Application Server management interface must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the system.

**Rule ID:** `SV-95947r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application servers are required to display the Standard Mandatory DoD Notice and Consent Banner before granting access to the system management interface, providing privacy and security notices consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance that states that: (i) users are accessing a U.S. Government information system; (ii) system usage may be monitored, recorded, and subject to audit; (iii) unauthorized use of the system is prohibited and subject to criminal and civil penalties; and (iv) the use of the system indicates consent to monitoring and recording. System use notification messages can be implemented in the form of warning banners displayed when individuals log on to the information system. System use notification is intended only for information system access including an interactive logon interface with a human user, and is not required when an interactive interface does not exist. Use this banner for desktops, laptops, and other devices accommodating banners of 1300 characters. The banner shall be implemented as a click-through banner at logon (to the extent permitted by the operating system), meaning it prevents further activity on the information system unless and until the user executes a positive action to manifest agreement by clicking on a box indicating "OK". "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Point browser to the URL of the WebSphere administration console. If the Standard Mandatory DoD Notice and Consent Banner is not displayed, this is a finding.

## Group: SRG-APP-000069-AS-000036

**Group ID:** `V-81235`

### Rule: The WebSphere Application Server management interface must retain the Standard Mandatory DoD Notice and Consent Banner on the screen until users acknowledge the usage conditions and take explicit actions to log on for further access.

**Rule ID:** `SV-95949r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To establish acceptance of system usage policy, a click-through banner at the application server management interface logon is required. The banner shall prevent further activity on the application server unless and until the user executes a positive action to manifest agreement by clicking on a box indicating "OK".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Point browser to the URL of the WebSphere administration console. If the Standard Mandatory DoD Notice and Consent Banner is not retained until the user acknowledges the usage conditions, this is a finding.

## Group: SRG-APP-000091-AS-000052

**Group ID:** `V-81237`

### Rule: The WebSphere Application Server must generate log records when successful/unsuccessful attempts to access subject privileges occur.

**Rule ID:** `SV-95951r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Accessing a subject's privileges can be used to elevate a lower-privileged subject's privileges temporarily in order to cause harm to the application server or to gain privileges to operate temporarily for a designed purpose. When these actions take place, the event needs to be logged. Application servers either provide a local user store, or they integrate with enterprise user stores like LDAP. When the application server provides the user store and enforces authentication, the application server must generate a log record when modification of privileges is successfully or unsuccessfully performed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the administrative console, navigate to Security >> Security auditing >> Audit Service Provider. Click on the providers in the list. Note: names of all the filters, e.g., "DefaultAuditSpecification_1". Go back to Security >> Security auditing >> Event type Filters. Find the filters previously noted. If you do not see the filter for SECURITY_AUTHN, SECURITY_AUTHZ, SECURITY_AUTHN_TERMINATE, and ADMIN_REPOSITORY_SAVE that has INFO, ERROR, SUCCESS, DENIED, REDIRECT, and WARNING defined, this is a finding.

## Group: SRG-APP-000357-AS-000038

**Group ID:** `V-81239`

### Rule: The WebSphere Application Server must allocate JVM log record storage capacity in accordance with organization-defined log record storage requirements.

**Rule ID:** `SV-95953r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>JVM logs are logs used to store application and runtime related events, rather than audit related events. They are mainly used to diagnose application or runtime bugs. But sometimes they may be useful in providing more context when correlated with audit related events. The proper management of log records not only dictates proper archiving processes and procedures be established, it also requires allocating enough storage space to maintain the logs online for a defined period of time. If adequate online log storage capacity is not maintained, intrusion monitoring, security investigations, and forensic analysis can be negatively affected. It is important to keep a defined amount of logs online and readily available for investigative purposes. The logs may be stored on the application server until they can be archived to a log system or, in some instances, a Storage Area Networks (SAN). Regardless of the method used, log record storage capacity must be sufficient to store log data when the data cannot be offloaded to a log system or SAN.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation. Identify the JVM log size and rotation settings based on component log policy. From the administrative console, navigate to Troubleshooting >> Logs and Trace. Choose [server name]. Click on the server name to select it. Click "JVM" Logs. For "System.out" verify "File Size" is selected and "Maximum size" and "Maximum Historical Log Files" are set according to the System Security Plan. For "System.err" verify "File Size" is selected and "Maximum size" and "Maximum Historical Log Files" are set according to the System Security Plan. If log size and log history retention settings for "System.err" and "System.out" are not set as per the System Security Plan, this is a finding.

## Group: SRG-APP-000357-AS-000038

**Group ID:** `V-81241`

### Rule: The WebSphere Application Server must allocate audit log record storage capacity in accordance with organization-defined log record storage requirements.

**Rule ID:** `SV-95955r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The proper management of log records not only dictates proper archiving processes and procedures be established, it also requires allocating enough storage space to maintain the logs online for a defined period of time. If adequate online log storage capacity is not maintained, intrusion monitoring, security investigations, and forensic analysis can be negatively affected. It is important to keep a defined amount of logs online and readily available for investigative purposes. The logs may be stored on the application server until they can be archived to a log system or, in some instances, a Storage Area Networks (SAN). Regardless of the method used, log record storage capacity must be sufficient to store log data when the data cannot be offloaded to a log system or SAN.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation. Identify the Audit Service Provider log size and rotation settings based on component log policy. From administrative console, click Security >> Security auditing >> Audit service provider. Select each [audit_service_provider_name]. If "Audit Log Size" and "Max Number of Audit Log Files" are not configured as per the System Security Plan, this is a finding.

## Group: SRG-APP-000360-AS-000066

**Group ID:** `V-81243`

### Rule: The WebSphere Application Server must provide an immediate real-time alert to authorized users of all log failure events requiring real-time alerts.

**Rule ID:** `SV-95957r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process logs as required. Log processing failures include software/hardware errors, failures in the log capturing mechanisms, and log storage capacity being reached or exceeded. Notification of the failure event will allow administrators to take actions so that logs are not lost.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If notifications of log processing failures are done via an alternative notification process, this is not a finding. In the administrative console, navigate to Security >> Security auditing >> Audit monitor. If "Enabled monitoring" is not checked and "Monitor notification" is not set to a name in the notifications list, this is a finding.

## Group: SRG-APP-000108-AS-000067

**Group ID:** `V-81245`

### Rule: The WebSphere Application Server must alert the SA and ISSO, at a minimum, in the event of a log processing failure.

**Rule ID:** `SV-95959r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Logs are essential to monitor the health of the system, investigate changes that occurred to the system, or investigate a security incident. When log processing fails, the events during the failure can be lost. To minimize the timeframe of the log failure, an alert needs to be sent to the SA and ISSO at a minimum. Log processing failures include, but are not limited to, failures in the application server log capturing mechanisms or log storage capacity being reached or exceeded. In some instances, it is preferred to send alarms to individuals rather than to an entire group. Application servers must be able to trigger an alarm and send an alert to, at a minimum, the SA and ISSO in the event there is an application server log processing failure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the SA and ISSO are notified of log processing failures via an alternative notification process, this is not a finding. In the administrative console, navigate to Security >> Security auditing >> Audit monitor. If "Enabled monitoring" is not checked and "Monitor notification" is not set to a notification in the notifications list, that includes the SA and ISSO, this is a finding.

## Group: SRG-APP-000108-AS-000067

**Group ID:** `V-81247`

### Rule: The WebSphere Application Server audit subsystem failure action must be set to Log warning.

**Rule ID:** `SV-95961r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Logs are essential to monitor the health of the system, investigate changes that occurred to the system, or investigate a security incident. When log processing fails, the events during the failure can be lost. To minimize the timeframe of the log failure, an alert needs to be sent to the SA and ISSO at a minimum. Log processing failures include, but are not limited to, failures in the application server log capturing mechanisms or log storage capacity being reached or exceeded. WebSphere must be set to log warnings that the audit subsystem has failed or is in danger or failing so action can be taken to correct the issue.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the administrative console, navigate to Security >> Security auditing. If "Audit subsystem failure action" is not set to "Log Warning", this is a finding.

## Group: SRG-APP-000109-AS-000068

**Group ID:** `V-81249`

### Rule: The WebSphere Application Server must shut down by default upon log failure (unless availability is an overriding concern).

**Rule ID:** `SV-95963r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is critical that, when a system is at risk of failing to process logs, it detects and takes action to mitigate the failure. Log processing failures include software/hardware errors, failures in the log capturing mechanisms, and log storage capacity being reached or exceeded. During a failure, the application server must be configured to shut down unless the application server is part of a high availability system or availability is an overriding concern. When availability is an overriding concern, other approved actions in response to a log failure include: (i) If the failure was caused by the lack of log record storage capacity, the application must continue generating log records if possible (automatically restarting the log service if necessary), overwriting the oldest log records in a first-in-first-out manner. (ii) If log records are sent to a centralized collection server and communication with this server is lost or the server fails, the application must queue log records locally until communication is restored or until the log records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local log data with the collection server. If the server will continue to process without any logging mitigations in place and the availability of the server is not critical to the success of the mission, the server must be configured to shut down on log failure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the System Security Plan documentation specifies system availability is an overriding concern, this requirement is NA. In the admin console click Security >> Security Auditing. If "Audit subsystem failure action" is not set to "Terminate", this is a finding.

## Group: SRG-APP-000109-AS-000070

**Group ID:** `V-81251`

### Rule: The WebSphere Application Server high availability applications must be configured to fail over to another system in the event of log subsystem failure.

**Rule ID:** `SV-95965r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>This requirement is dependent upon system MAC and availability. If the system MAC and availability do not specify redundancy requirements, this requirement is NA. It is critical that, when a system is at risk of failing to process logs as required, it detects and takes action to mitigate the failure. Application servers must be capable of failing over to another system which can handle application and logging functions upon detection of an application log processing failure. This will allow continual operation of the application and logging functions while minimizing the loss of operation for the users and loss of log data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the System Security Plan documentation does not require redundancy, this requirement is NA. Click Servers >> Clusters >> WebSphere application server clusters. Ensure you have a cluster defined for every application requiring redundancy. If there is not a cluster defined for every application requiring redundancy, this is a finding.

## Group: SRG-APP-000118-AS-000078

**Group ID:** `V-81253`

### Rule: The WebSphere Application Server must be configured to protect log information from any type of unauthorized read access.

**Rule ID:** `SV-95967r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>WebSphere uses role-based access controls to restrict access to log data. To take advantage of this capability, WebSphere administrators must identify specific users and place them into their respective roles. The auditor role is used for controlling access to logs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation and System Security Plan. Identify the home folder and user account for the WebSphere installation. Log on to the operating system that is hosting the WebSphere application server. By default, WebSphere will be installed in the "/opt/IBM/Websphere" folder on UNIX like systems and in the "C:\Program Files\IBM\Websphere\" folder on Windows systems. On UNIX systems, verify file permissions for the "WebSphere" folder are set to "770" for the WebSphere user, group, and other. Permissions do not propagate to sub-folders. On Windows systems, verify file permissions for "WebSphere" folder allow SYSTEM, WebSphere User and Admin Group full control. Permissions do not propagate to sub-folders. If file permissions exceed these restrictions, this is a finding.

## Group: SRG-APP-000119-AS-000079

**Group ID:** `V-81255`

### Rule: The WebSphere Application Server must protect log information from unauthorized modification.

**Rule ID:** `SV-95969r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>WebSphere uses role-based access controls to restrict access to log data. To take advantage of this capability, WebSphere administrators must identify specific users and place them into their respective roles. The auditor role is used for controlling access to logs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan and the system documentation. Identify the home folder and user account for the WebSphere installation. Log on to the operating system that is hosting the WebSphere application server. By default, WebSphere will be installed in the "/opt/IBM/Websphere" folder on UNIX like systems and in the "C:\Program Files\IBM\Websphere\" folder on Windows systems. On UNIX systems, verify file permissions for the "WebSphere" folder are set to "770" for the WebSphere user, group and other. Permissions do not propagate to sub-folders. On Windows systems, verify file permissions for "WebSphere" folder allow SYSTEM, WebSphere User, and Admin Group full control. Permissions do not propagate to sub-folders. If file permissions exceed these restrictions, this is a finding.

## Group: SRG-APP-000120-AS-000080

**Group ID:** `V-81257`

### Rule: The WebSphere Application Server must protect log information from unauthorized deletion.

**Rule ID:** `SV-95971r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>WebSphere uses role based access controls to restrict access to log data. To take advantage of this capability, WebSphere administrators must identify specific users and place them into their respective roles. The auditor role is used for controlling access to logs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan and the system documentation. Identify the home folder and user account for the WebSphere installation. Log on to the operating system that is hosting the WebSphere application server. By default, WebSphere will be installed in the "/opt/IBM/Websphere" folder on UNIX like systems and in the "C:\Program Files\IBM\Websphere\" folder on Windows systems. On UNIX systems, verify file permissions for the "WebSphere" folder are set to "770" for the WebSphere user, group, and other. Permissions do not propagate to sub-folders. On Windows systems, verify file permissions for "WebSphere" folder allow SYSTEM, WebSphere User and Admin Group full control. Permissions do not propagate to sub-folders. If file permissions exceed these restrictions, this is a finding.

## Group: SRG-APP-000121-AS-000081

**Group ID:** `V-81259`

### Rule: The WebSphere Application Server wsadmin file must be protected from unauthorized access.

**Rule ID:** `SV-95973r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting log data also includes identifying and protecting the tools used to view and manipulate log data. Depending upon the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. It is, therefore, imperative that access to log tools be controlled and protected from unauthorized access. Application servers provide a web- and/or a command line-based management functionality for managing the application server log capabilities. In addition, subsets of log tool components may be stored on the file system as jar or xml configuration files. The application server must ensure that in addition to protecting any web-based log tools, any file system-based tools are protected as well.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan and the system documentation. Identify the home folder and user account for the WebSphere installation. Log on to the operating system that is hosting the WebSphere application server. By default, WebSphere will be installed in the "/opt/IBM/Websphere" folder on UNIX like systems and in the "C:\Program Files\IBM\Websphere\" folder on Windows systems. On UNIX systems, verify file permissions for the "WebSphere" folder are set to "770" for the WebSphere user, group, and other. Permissions do not propagate to sub-folders. On Windows systems, verify file permissions for "WebSphere" folder allow SYSTEM, WebSphere User, and Admin Group full control. Permissions do not propagate to sub-folders. If file permissions exceed these restrictions, this is a finding.

## Group: SRG-APP-000122-AS-000082

**Group ID:** `V-81261`

### Rule: The WebSphere Application Server wsadmin file must be protected from unauthorized modification.

**Rule ID:** `SV-95975r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting log data also includes identifying and protecting the tools used to view and manipulate log data. Depending upon the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. It is, therefore, imperative that access to log tools be controlled and protected from unauthorized modification. If an attacker were to modify log tools, he could also manipulate logs to hide evidence of malicious activity. Application servers provide a web- and/or a command line-based management functionality for managing the application server log capabilities. In addition, subsets of log tool components may be stored on the file system as jar or xml configuration files. The application server must ensure that in addition to protecting any web-based log tools, any file system-based tools are protected as well.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan and the system documentation. Identify the home folder and user account for the WebSphere installation. Log on to the operating system that is hosting the WebSphere application server. By default, WebSphere will be installed in the "/opt/IBM/Websphere" folder on UNIX like systems and in the "C:\Program Files\IBM\Websphere\" folder on Windows systems. On UNIX systems, verify file permissions for the "WebSphere" folder are set to "770" for the WebSphere user, group, and other. Permissions do not propagate to sub-folders. On Windows systems, verify file permissions for "WebSphere" folder allow SYSTEM, WebSphere User, and Admin Group full control. Permissions do not propagate to sub-folders. If file permissions exceed these restrictions, this is a finding.

## Group: SRG-APP-000123-AS-000083

**Group ID:** `V-81263`

### Rule: The WebSphere Application Server wsadmin file must be protected from unauthorized deletion.

**Rule ID:** `SV-95977r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting log data also includes identifying and protecting the tools used to view and manipulate log data. Depending upon the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. It is, therefore, imperative that access to log tools be controlled and protected from unauthorized modification. If an attacker were to delete log tools, the application server administrator would have no way of managing or viewing the logs. Application servers provide a web- and/or a command line-based management functionality for managing the application server log capabilities. In addition, subsets of log tool components may be stored on the file system as jar, class, or xml configuration files. The application server must ensure that in addition to protecting any web-based log tools, any file system-based tools are protected from unauthorized deletion as well.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation and security plan. Identify the home folder and user account for the WebSphere installation. Log on to the operating system that is hosting the WebSphere application server. By default, WebSphere will be installed in the "/opt/IBM/Websphere" folder on UNIX like systems and in the "C:\Program Files\IBM\Websphere\" folder on Windows systems. On UNIX systems, verify file permissions for the "WebSphere" folder are set to "770" for the WebSphere user, group, and other. Permissions do not propagate to sub-folders. On Windows systems, verify file permissions for WebSphere folder allow SYSTEM, WebSphere User, and Admin Group full control. Permissions do not propagate to sub-folders. If file permissions exceed these restrictions, this is a finding.

## Group: SRG-APP-000126-AS-000085

**Group ID:** `V-81265`

### Rule: The WebSphere Application Server must be configured to encrypt log information.

**Rule ID:** `SV-95979r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of log records is of critical importance. Encrypting log records provides a level of protection that does not rely on host-based protections that can be accidentally misconfigured, such as file system permissions. Cryptographic mechanisms are the industry-established standard used to protect the integrity of log data. An example of a cryptographic mechanism is the computation and application of a cryptographic-signed hash using asymmetric cryptography. Encryption of log records must be tempered with architecture designs that incorporate log data into SIEM systems that read and act upon log data. Some SIEM systems may not be able to decrypt encrypted log data so encrypting the logs could be detrimental to the incident response process. This must be taken into account and addressed in the security plan.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation. If the System Security Plan does not specify the encryption of audit records, this requirement is NA. From the administrative console, click Security >> Security Auditing >> Audit record encryption configuration. If the "Enable encryption" check box is not selected, this is a finding.

## Group: SRG-APP-000126-AS-000085

**Group ID:** `V-81267`

### Rule: The WebSphere Application Server must be configured to sign log information.

**Rule ID:** `SV-95981r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of log records is of critical importance. Encrypting log records provides a level of protection that does not rely on host-based protections that can be accidentally misconfigured, such as file system permissions. Cryptographic mechanisms are the industry-established standard used to protect the integrity of log data. An example of a cryptographic mechanism is the computation and application of a cryptographic-signed hash using asymmetric cryptography.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the administrative console, click Security >> Security Auditing >> Audit record signing configuration. If the "Enable signing" checkbox is not selected, this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-81269`

### Rule: The WebSphere Application Server process must not be started from the command line with the -password option.

**Rule ID:** `SV-95983r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of the -password option to launch a WebSphere process from the command line can result in a security exposure. Password information may become visible to any user with the ability to view system processes. For example, on a Linux system the "ps" command will display all running processes, which would include all of the command line flags used to start a WebSphere process.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation. Interview the system administrator. Access operating system to list commands currently running. For UNIX: run "ps -ef | grep -i wsadmin.sh" For windows: from a DOS prompt as admin user run "WMIC path win32_process where "caption='wsadmin.exe'" get CommandLine" If the results show "wsadmin.sh(exe) -user <username> -password <password>", this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-81271`

### Rule: The WebSphere Application Server files must be owned by the non-root WebSphere user ID.

**Rule ID:** `SV-95985r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Having files owned by the root or administrator user is an indication that the WebSphere processes are being run with escalated privileges. Running as root/admin user gives attackers elevated privileges that can be used to compromise the system more easily compared to operating the WebSphere processes with regular user privileges. Specifying a regular OS user when installing and managing WebSphere is best practice. By doing so, the WebSphere files will be owned by the user ID specified rather than being owned by the admin user. Use the underlying OS file permissions to ensure that access to the WebSphere files are restricted to only those users who require access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation. Interview the system administrator. Determine the OS user and group information associated with the WebSphere processes. Identify the paths, files, and folders associated with the WebSphere installation. These include: - <WAS_HOME>: where you installed WebSphere. <WAS_HOME> default location: For UNIX: /opt/IBM/WebSphere/AppServer For Windows: C:\Program Files\IBM\WebSphere\AppServer - <PROFILE_HOME>: where the appserver instance resides. The default location is under "<WAS_HOME>/profiles". - <OTHER_HOME>: any additional files that may reside outside of <WAS_HOME>. Examples include: - shared library .jar files - Resource Adapter .rar files - Key and trust store files (.jks and .p12) - Other files such as jdbc drivers For Linux, use the command "find <directory> -user root" to find files owned by root user. On windows use the "dir /Q /S" command from the root directories to show the owners of all files. Examine the output for files owned by the administrator or root account. If any WebSphere file or additional files as described above are owned by root or the administrator, this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-81273`

### Rule: The WebSphere Application Server sample applications must be removed.

**Rule ID:** `SV-95987r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>WebSphere samples are not intended for use in a production environment. Do not run them there, as they create significant security risks. In particular, the snoop servlet can provide an outsider with tremendous amounts of information about your system. This is precisely the type of information you do not want to give a potential intruder. Do not install the samples during the profile creation or uninstall the sample programs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Applications >> All Applications. Review all applications installed on the application server. If the sample applications snoop, ivt, or DefaultApplication are installed on a production system, this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-81275`

### Rule: The WebSphere Application Server must remove JREs left by web server and plug-in installers for web servers and plugins running in the DMZ.

**Rule ID:** `SV-95989r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>When you install IBM HTTP Server, the installer leaves behind a JRE. Remove this JRE, as it provides functions that are not needed by the Web server or plug-in under normal conditions. Keep in mind that this will make it impossible to run some tools such as ikeyman on this Web server. When you install the WebSphere Application Server HTTP Server plug-in using the IBM installer, it also leaves behind a JRE. Also, remove this JRE post install. Having a functioning JRE in the DMZ provides attackers who have breached into the DMZ with additional tools to carry out further attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check needs to be run on the web server operating in the DMZ. Review system documentation. Identify web servers operating in DMZ. If there are no web servers configured for the DMZ, this is not applicable. From the administrative console, select Server Types >> Web Servers. Select each web server operating in the DMZ. Identify the "Web server installation location". Open a secured command shell to the web server in the DMZ. Change directory to the web server installation location. CD to the /plugins folder. If a /java directory exists in the plugins folder, this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-81277`

### Rule: The WebSphere Application Server must be run as a non-admin user.

**Rule ID:** `SV-95991r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Running WebSphere as an admin user gives attackers immediate admin privileges in the event the WebSphere processes are compromised. Best practice is to operate the WebSphere server with an account that has limited OS privileges. To configure system startup: https://www.ibm.com/support/knowledgecenter/en/SSAW57_8.5.5/com.ibm.websphere.nd.multiplatform.doc/ae/trun_processrestart.html</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview systems manager. Identify the OS user ID that the WAS server runs as. Using relevant OS commands review OS processes and search for WAS processes (running as Java). Ensure they are running under the assigned non-administrative user id. For UNIX: "ps -ef|grep -i websphere" For Windows: "wmic path win32_process where "caption = 'java.exe'" get CommandLine If the WebSphere processes are running as the root or administrator user, this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-81279`

### Rule: The WebSphere Application Server must disable JSP class reloading.

**Rule ID:** `SV-95993r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application servers provide a myriad of differing processes, features, and functionalities. Some of these processes may be deemed to be unnecessary or too unsecure to run on a production DoD system. Application servers must provide the capability to disable or deactivate functionality and services that are deemed to be non-essential to the server mission or can adversely impact server performance, for example, disabling dynamic JSP reloading on production application servers as a best practice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From admin console, navigate to: Applications >> All applications >> [application name] >> JSP and JSP options. If "JSP enable class reloading" is checked, this is a finding.

## Group: SRG-APP-000142-AS-000014

**Group ID:** `V-81293`

### Rule: The WebSphere Application Server must prohibit or restrict the use of nonsecure ports, protocols, modules, and/or services as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-96007r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some networking protocols may not meet organizational security requirements to protect data and components. Application servers natively host a number of various features, such as management interfaces, httpd servers, and message queues. These features all run on TCPIP ports. This creates the potential that the vendor may choose to utilize port numbers or network services that have been deemed unusable by the organization. The application server must have the capability to both reconfigure and disable the assigned ports without adversely impacting application server operation capabilities. For a list of approved ports and protocols, reference the DoD ports and protocols website at https://powhatan.iiie.disa.mil/ports/cal.html.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the administrative console, click Servers >> All Servers. Select each [server_name]. Select >> Ports. Confirm server ports are registered with PPSM. Navigate to System Administration >> Deployment Manager >> Ports. Confirm ports are registered with PPSM. Navigate to System Administration >> node agents. For each [node agent], select >> Ports. Confirm ports are registered with PPSM. If any of available ports are not registered with PPSM, or if those ports to be connected through the firewall are not approved by PPSM, this is a finding.

## Group: SRG-APP-000148-AS-000101

**Group ID:** `V-81299`

### Rule: The WebSphere Application Server LDAP user registry must be used.

**Rule ID:** `SV-96013r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthorized access, application server users must be uniquely identified and authenticated. This is typically accomplished via the use of a user store which is either local (OS-based) or centralized (LDAP) in nature. To ensure support to the enterprise, the authentication must utilize an enterprise solution.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the administrative console, click Security >> Global security. If the "Available realm definitions" drop down box under the "User account repository" section is not set to "Standalone LDAP registry", this is a finding.

## Group: SRG-APP-000148-AS-000101

**Group ID:** `V-81305`

### Rule: The WebSphere Application Server local file-based user registry must not be used.

**Rule ID:** `SV-96019r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>WebSphere does not provide direct audit of changes to the built-in file registry. The built-in file registry must not be used to support user logon accounts. Use an LDAP/AD server and manage user accounts centrally.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Security >> Global Security. Under "User Account Repository" if the "Federated Repositories" is chosen, click on "Configure". Under "Repositories in the realm", if "o=defaultWIMFileBasedRealm" appears in the "Base Entry" column, this is a finding.

## Group: SRG-APP-000149-AS-000102

**Group ID:** `V-81311`

### Rule: The WebSphere Application Server multifactor authentication for network access to privileged accounts must be used.

**Rule ID:** `SV-96025r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Multifactor authentication creates a layered defense and makes it more difficult for an unauthorized person to access the application server. If one factor is compromised or broken, the attacker still has at least one more barrier to breach before successfully breaking into the target. Unlike a simple username/password scenario where the attacker could gain access by knowing both the username and password without the user knowing his account was compromised, multifactor authentication adds the requirement that the attacker must have something from the user, such as a token, or to biometrically be the user. Multifactor authentication is defined as: using two or more factors to achieve authentication. Factors include: (i) something a user knows (e.g., password/PIN); (ii) something a user has (e.g., cryptographic identification device, token); or (iii) something a user is (e.g., biometric). A CAC or PKI Hardware Token meets this definition. A privileged account is defined as an information system account with authorizations of a privileged user. These accounts would be capable of accessing the web management interface. When accessing the application server via a network connection, administrative access to the application server must be PKI Hardware Token enabled. Satisfies: SRG-APP-000149-AS-000102, SRG-APP-000391-AS-000239, SRG-APP-000392-AS-000240, SRG-APP-000151-AS-000103, SRG-APP-000177-AS-000126, SRG-APP-000402-AS-000247, SRG-APP-000403-AS-000248, SRG-APP-000404-AS-000249, SRG-APP-000219-AS-000147</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that the admin console is enabled for client certificate logon. In the Deployment Manager, check the file on: <WAS_INSTALL>/profiles/<profileName>/config/cells/<cellName>/applications/isclite.ear/deployments/isclite/isclite.war/WEB-INF/web.xml. If the "XML element <auth-method>FORM</auth-method>" is present, this is a finding.

## Group: SRG-APP-000156-AS-000106

**Group ID:** `V-81325`

### Rule: The WebSphere Application Server must provide security extensions to extend the SOAP protocol and provide secure authentication when accessing sensitive data.

**Rule ID:** `SV-96039r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application servers may provide a web services capability that could be leveraged to allow remote access to sensitive application data. A web service which is a repeatable process used to make data available to remote clients, should not be confused with a web server. Many web services utilize SOAP, which in turn utilizes XML and HTTP as a transport. Natively, SOAP does not provide security protections. As such, the application server must provide security extensions to enhance SOAP capabilities to ensure that secure authentication mechanisms are employed to protect sensitive data. The WS_Security suite is a widely used and acceptable SOAP security extension.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation. Interview the system administrator. Identify any application web service providers and the secure authentication requirements for each service provider. From admin console, navigate to Applications >> All applications. Click on each application that is a web service provider where the security plan specifies security extensions are to be applied. Navigate to "Service provider policy sets and bindings". Verify that any web service providers that are required to have security extensions applied as per the security plan have a policy attached. If "Attached policy set" column displays none, but the System Security Plan specifies security extensions as required, this is a finding.

## Group: SRG-APP-000156-AS-000106

**Group ID:** `V-81329`

### Rule: The WebSphere Application Server must provide security extensions to extend the SOAP protocol and provide secure authentication when accessing sensitive data.

**Rule ID:** `SV-96043r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application servers may provide a web services capability that could be leveraged to allow remote access to sensitive application data. A web service, which is a repeatable process used to make data available to remote clients, should not be confused with a web server. Many web services utilize SOAP, which in turn utilizes XML and HTTP as a transport. Natively, SOAP does not provide security protections. As such, the application server must provide security extensions to enhance SOAP capabilities to ensure that secure authentication mechanisms are employed to protect sensitive data. The WS_Security suite is a widely used and acceptable SOAP security extension.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation. Interview the system administrator. Identify any application web service clients. Identify the secure authentication requirements for each client. From admin console, navigate to Applications >> All applications. Click on each application that is a web service client where the security plan specifies security extensions are to be applied. Navigate to "Service client policy sets and bindings". Verify that any web service clients that are required to have security extensions applied as per the security plan have a policy attached. If "Attached policy set" column displays none, but the System Security Plan specifies security extensions as required, this is a finding.

## Group: SRG-APP-000394-AS-000241

**Group ID:** `V-81333`

### Rule: The WebSphere Application Server must authenticate all network-connected endpoint devices before establishing any connection.

**Rule ID:** `SV-96047r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Device authentication requires unique identification and authentication that may be defined by type, by specific device, or by a combination of type and device. Device authentication is accomplished via the use of certificates and protocols such as SSL mutual authentication. Device authentication is performed when the application server is providing web services capabilities and data protection requirements mandate the need to establish the identity of the connecting device before the connection is established. Note: with LDAP registry, the entire DN in the certificate is used to look up LDAP. Filters may be configured. With other registries, only the first attribute after the first "=", e.g., CN=<user> is used. https://www.ibm.com/support/knowledgecenter/prodconn_1.0.0/com.ibm.scenarios.wmqwassecure.doc/topics/implementing.htm?cp=SSEQTP_8.0.0 Satisfies: SRG-APP-000394-AS-000241, SRG-APP-000177-AS-000126</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation. Identify mutual authentication connection requirements. From the admin console, navigate to Security >> SSL Certificate and Key Management >> SSL Configuration. Select each [NodeDefaultSSLSettings] then go to Quality of Protection (QoP) Settings. If "Client authentication" is not set according to the security plan, this is a finding.

## Group: SRG-APP-000395-AS-000109

**Group ID:** `V-81341`

### Rule: The WebSphere Application Server must authenticate all endpoint devices before establishing a local, remote, and/or network connection using bidirectional authentication that is cryptographically based.

**Rule ID:** `SV-96055r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Device authentication requires unique identification and authentication that may be defined by type, by specific device, or by a combination of type and device. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. Device authentication is performed when the application server is providing web services capabilities and data protection requirements mandate the need to establish the identity of the connecting device before the connection is established. Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability. Note: with LDAP registry, the entire DN in the certificate is used to look up LDAP. Filters may be configured. With other registries, only the first attribute after the first "=", e.g., CN=<user> is used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation. Identify mutual authentication connection requirements. From the admin console, navigate to Security >> SSL Certificate and Key Management >> SSL Configuration. Select each [NodeDefaultSSLSettings] then go to Quality of Protection (QoP) Settings. If "Client authentication" is not set according to the security plan, this is a finding. Note: with LDAP registry, the entire DN in the certificate is used to look up LDAP. Filters may be configured. With other registries, only the first attribute after the first "=", e.g., CN=<user> is used.

## Group: SRG-APP-000172-AS-000120

**Group ID:** `V-81343`

### Rule: The WebSphere Application Server application security must be enabled for each security domain except for publicly available applications specified in the System Security Plan.

**Rule ID:** `SV-96057r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>By default, all administrative and user applications in WebSphere® Application Server use the global security configuration. For example, a user registry defined in global security is used to authenticate users for every application in the cell. WebSphere allows for additional WebSphere security domains where different security attributes for some or all of your user applications can be set. These domains must also be configured to use application security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation. Identify any publicly available applications. These are applications available to the public that do not require authentication to access (e.g., recruiting websites). If such applications exist on the system and are specifically allowed according to the security plan, this requirement is NA for those applications only. Navigate to security >> security domains. Click through each security domain. If "Customize for this domain" is checked for Application Security under the Security Attributes, but "Enable application security" is not checked, this is a finding.

## Group: SRG-APP-000172-AS-000121

**Group ID:** `V-81347`

### Rule: The WebSphere Application Server secure LDAP (LDAPS) must be used for authentication.

**Rule ID:** `SV-96061r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords during transmission. Application servers have the capability to utilize LDAP directories for authentication. If LDAP connections are not protected during transmission, sensitive authentication credentials can be stolen. When the application server utilizes LDAP, the LDAP traffic must be encrypted. To ensure an error-free operation for this step, first extract to a file the Signer certificate of the LDAP and send that file to the WebSphere Application Server machine. Then add the certificate to the truststore being defined for the LDAP. In this way, you are assured that the remaining actions for this step will be successful. Satisfies: SRG-APP-000172-AS-000121, SRG-APP-000172-AS-000120</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the administrative console, click Security >> Global security. Under "User account repository", click "Configure" for the "Standalone LDAP registry", on "Standalone LDAP registry" panel. If the "SSL" flag is not enabled, this is a finding.

## Group: SRG-APP-000400-AS-000246

**Group ID:** `V-81351`

### Rule: The WebSphere Application Server must prohibit the use of cached authenticators after an organization-defined time period.

**Rule ID:** `SV-96065r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When the application server is using PKI authentication, a local revocation cache must be stored for instances when the revocation cannot be authenticated through the network, but if cached authentication information is out of date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation. Identify the cache timeout parameters for authentication. Standard value for admin timeout is 10 minutes; however, the ISSO may allow a case by case exception based on operational requirements. From the admin console, navigate to Security >> Global Security >> Authentication cache settings. If "Enable authentication cache" check box is set and "Cache timeout" is larger than the parameters specified in the security plan, this is a finding.

## Group: SRG-APP-000176-AS-000125

**Group ID:** `V-81357`

### Rule: The WebSphere Application Server default keystore passwords must be changed.

**Rule ID:** `SV-96071r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The cornerstone of the PKI is the private key used to encrypt or digitally sign information. If the private key is stolen, this will lead to the compromise of the authentication and non-repudiation gained through PKI because the attacker can use the private key to digitally sign documents and can pretend to be the authorized user. Both the holders of a digital certificate and the issuing authority must protect the computers, storage devices, or whatever they use to keep the private keys. Java-based application servers utilize the Java keystore, which provides storage for cryptographic keys and certificates. The keystore is usually maintained in a file stored on the file system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation. Interview the system administrator. Identify installation folders and DMGR info. Access the DMGR system via the OS. Stop the DMGR processes. This will shut down the application server so plan outages accordingly. The default file paths and DefaultMgr installation names are provided below, adjust paths, and dmgr name if your installation differs from the default. For UNIX systems: cd /opt/IBM/Websphere/Profiles/<DefaultDmgr01>/logs/dmgr/ -stopManager.sh -user [admin user name] - password [admin user password] -archive the SystemOut*.log files. (Copy to another location) -startManager.sh -grep -i cwpki0041w SystemOut.log For Windows: cd C:\program files\IBM\Websphere\Profiles\<DefaultDmgr01>\logs\dmgr\ -stopManager.exe -user [admin user name] - password [admin user password] -archive the SystemOut*.log files. (Copy to another location) -startManager.exe -findstr -I cwpki0041w systemout.log If the results include: "CWPKI0041W: One or more keystores are using the default password", this is a finding.

## Group: SRG-APP-000177-AS-000126

**Group ID:** `V-81361`

### Rule: The WebSphere Application Server must use signer for DoD-issued certificates.

**Rule ID:** `SV-96075r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The cornerstone of PKI is the private key used to encrypt or digitally sign information. The key by itself is a cryptographic value that does not contain specific user information, but the key can be mapped to a user. Without mapping the certificate used to authenticate to the user account, the ability to determine the identity of the individual user or group will not be available for forensic analysis. Application servers must provide the capability to utilize and meet requirements of the DoD Enterprise PKI infrastructure for application authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Security >> SSl certificate and key management >> SSL Configurations >> CellDefaultSSLSettings >> KeyStores and certificates. Click on cell default trust store. Click on "Signer Certificates". If no DoD root or intermediate certificates are present, this is a finding.

## Group: SRG-APP-000179-AS-000129

**Group ID:** `V-81365`

### Rule: The WebSphere Application Server must utilize FIPS 140-2-approved encryption modules when authenticating users and processes.

**Rule ID:** `SV-96079r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified and cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised due to weak algorithms. The use of TLS provides confidentiality of data in transit between the application server and client. FIPS 140-2 approved TLS versions include TLS V1.0 or greater. TLS must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 specifies the preferred configurations for government systems. Satisfies: SRG-APP-000179-AS-000129, SRG-APP-000440-AS-000167, SRG-APP-000442-AS-000259, SRG-APP-000439-AS-000155, SRG-APP-000224-AS-000152, SRG-APP-000514-AS-000136, SRG-APP-000416-AS-000140</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From administrative console, click Security >> SSL certificate and key management >> Manage FIPS. If "Enable FIPS 140-2" is not selected, this is a finding.

## Group: SRG-APP-000402-AS-000247

**Group ID:** `V-81367`

### Rule: The WebSphere Application Server must accept Personal Identity Verification (PIV) credentials from other federal agencies to access the management interface.

**Rule ID:** `SV-96081r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Personal Identity Verification (PIV) credentials are those credentials issued by federal agencies that conform to FIPS Publication 201 and supporting guidance documents. OMB Memorandum 11-11 requires federal agencies to continue implementing the requirements specified in HSPD-12 to enable agency-wide use of PIV credentials. PIV credentials are only used in an unclassified environment. Access may be denied to authorized users if federal agency PIV credentials are not accepted to access the management interface.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that the admin console is enabled for client certificate logon. In the Deployment Manager, check the file on: <WAS_INSTALL>/profiles/<profileName>/config/cells/<cellName>/applications/isclite.ear/deployments/isclite/isclite.war/WEB-INF/web.xml. If the XML element "<auth-method>FORM</auth-method>" is present, this is a finding.

## Group: SRG-APP-000514-AS-000137

**Group ID:** `V-81369`

### Rule: The WebSphere Application Server must use DoD-approved Signer Certificates.

**Rule ID:** `SV-96083r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Class 3 PKI certificates are used for servers and software signing rather than for identifying individuals. Class 4 certificates are used for business-to-business transactions. Utilizing unapproved certificates not issued or approved by DoD or CNS creates an integrity risk. The application server must utilize approved DoD or CNS Class 3 or Class 4 certificates for software signing and business-to-business transactions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From administrative console, navigate to Security >> SSL Certificates and Key Management >> KeyStores and Certificates. For each keystore, click on "Signer Certificates". If any of the certificates are not issued by an approved DoD CA, this is a finding.

## Group: SRG-APP-000211-AS-000146

**Group ID:** `V-81371`

### Rule: The WebSphere Application Servers must not be in the DMZ.

**Rule ID:** `SV-96085r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The application server consists of the management interface and hosted applications. By separating the management interface from hosted applications, the user must authenticate as a privileged user to the management interface before being presented with management functionality. This prevents non-privileged users from having visibility to functions not available to the user. By limiting visibility, a compromised non-privileged account does not offer information to the attacker to functionality and information needed to further the attack on the application server. Application server management functionality includes functions necessary to administer the application server and requires privileged access via one of the accounts assigned to a management role. The hosted application and hosted application functionality consists of the assets needed for the application to function, such as the business logic, databases, user authentication, etc. The separation of application server administration functionality from hosted application functionality is either physical or logical and is accomplished by using different computers, different central processing units, different instances of the operating system, network addresses, network ports, or combinations of these methods, as appropriate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan and system architecture documentation. Interview the system administrator. Identify any DMZ networks. If there are no DMZ networks in the application server's architecture, this requirement is NA. In the administrative console, click Servers >> Server Types >> WebSphere application servers. For each application server, review the "hostname" field and determine if the application server has a DMZ network IP address. If any application server is hosted in the DMZ network, this is a finding.

## Group: SRG-APP-000219-AS-000147

**Group ID:** `V-81373`

### Rule: The WebSphere Application Server DoD root CAs must be in the trust store.

**Rule ID:** `SV-96087r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This control focuses on communications protection at the session, versus packet level. At the application layer, session IDs are tokens generated by web applications to uniquely identify an application user's session. Web applications utilize session tokens or session IDs in order to establish application user identity. Proper use of session IDs addresses man-in-the-middle attacks, including session hijacking or insertion of false information into a session. Application servers must provide the capability to perform mutual authentication. Mutual authentication is when both the client and the server authenticate each other.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation for location of the trust store used to store the signers of the administrators certificates. By default this is "cellDefaultTrustStore". Navigate to Security >> SSL certificate and key management >> Keystore and certificates. Click on the trust store used to store the signers of the administrators' certificates (root CA). (The default is cellDefaultTrustStore). Click on "Signer Certificates". If there are no DoD signer certificates, this is a finding.

## Group: SRG-APP-000427-AS-000264

**Group ID:** `V-81375`

### Rule: The WebSphere Application Server personal certificates in all keystores must be issued by an approved DoD CA.

**Rule ID:** `SV-96089r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DoD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DoD-approved CA, trust of this CA has not been established. The DoD will only accept PKI certificates obtained from a DoD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of SSL/TLS certificates. The application server must only allow the use of DoD PKI-established certificate authorities for verification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation for a list of DoD-approved CAs. From administrative console, navigate to Security >> SSL Certificates and Key Management >> KeyStores and Certificates. For each keystore, click on "Personal Certificates". If any of the certificates are not issued by an approved DoD CA, this is a finding.

## Group: SRG-APP-000225-AS-000153

**Group ID:** `V-81377`

### Rule: The WebSphere Application Server must be configured to perform complete application deployments when using A/B clusters.

**Rule ID:** `SV-96091r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. When an application is deployed to the application server, if the deployment process does not complete properly and without errors, there is the potential that some application files may not be deployed or may be corrupted and an application error may occur during runtime. The application server must be able to perform complete application deployments. A partial deployment can leave the server in an inconsistent state. Application servers may provide a transaction rollback function to address this issue.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation to determine if the server is configured to use A/B clusters. If the System Security Plan does not specify utilizing A/B clusters, the requirement is NA. From the administration console, select WebSphere application server clusters. Select each cluster name. Select cluster members. If the weight of any cluster member is "0", this is a finding.

## Group: SRG-APP-000225-AS-000154

**Group ID:** `V-81379`

### Rule: The WebSphere Application servers with an RMF categorization of high must be in a high-availability (HA) cluster.

**Rule ID:** `SV-96093r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>This requirement is dependent upon system MAC and confidentiality. If the system MAC and confidentiality levels do not specify redundancy requirements, this requirement is NA. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. When application failure is encountered, preserving application state facilitates application restart and return to the operational mode of the organization with less disruption of mission/business processes. Clustering of multiple application servers is a common approach to providing fail-safe application availability when system MAC and confidentiality levels require redundancy. Satisfies: SRG-APP-000225-AS-000154, SRG-APP-000435-AS-000069</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Systems Security Plan and identify system categorization. If the system is not categorized as HIGH, this requirement is NA. In the administrative console, click Servers >> Clusters >> WebSphere application server clusters. Ensure you have a cluster defined, if not this is a finding.

## Group: SRG-APP-000428-AS-000265

**Group ID:** `V-81381`

### Rule: The WebSphere Application Server must not generate LTPA keys automatically.

**Rule ID:** `SV-96095r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Automated LTPA key generation can create unplanned outages. Plan to change your LTPA keys during a scheduled outage. Distribute the new keys to all nodes in the cell and to all external systems/cells during this outage window.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If LTPA is not utilized, this is not applicable. Request the documented process to manually regenerate the LTPA keys. The time period for regeneration must be defined, documented, and accepted by the ISSO but must be performed at least annually. Navigate to Security >> SSL Certificate and Key Management >> Key set groups >> Cell LTPAKeySetGroup. If automatically generate keys is checked, this is a finding.

## Group: SRG-APP-000428-AS-000265

**Group ID:** `V-81383`

### Rule: The WebSphere Application Server must periodically regenerate LTPA keys.

**Rule ID:** `SV-96097r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The encryption of authentication information that is exchanged between servers involves the Lightweight Third-Party Authentication (LTPA) mechanism. LTPA utilizes encryption keys, if LTPA is utilized, the LTPA keys must be regenerated on a regular basis. The time period must be defined, documented and accepted by the ISSO but must be performed at least annually. Note: If LTPA keys are shared across cells, you must export the keys from the cell where the keys have been regenerated, and import into the cells whose keys have not changed. Instructions for managing the LTPA keys is provided here: https://www.ibm.com/support/knowledgecenter/en/SSAW57_9.0.0/com.ibm.websphere.nd.multiplatform.doc/ae/tsec_sslmanagelptakeys.html</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If LTPA is not utilized, this is not applicable. Request the documented process to manually regenerate the LTPA keys. The time period for regeneration must be defined, documented and accepted by the ISSO but must be performed at least annually. Review documented process for LTPA key regeneration. If there is no process to regenerate LTPA keys periodically, this is a finding.

## Group: SRG-APP-000435-AS-000163

**Group ID:** `V-81385`

### Rule: The WebSphere Application Server high availability applications must be installed on a cluster.

**Rule ID:** `SV-96099r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. To reduce the possibility or effect of a DoS, the application server must employ defined security safeguards. These safeguards will be determined by the placement of the application server and the type of applications being hosted within the application server framework. There are many examples of technologies that exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the application opens at one time). Employing increased capacity and bandwidth, combined with service redundancy or clustering, may reduce the susceptibility to some DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Systems Security Plan and identify system categorization. If the system is not categorized as HIGH, this requirement is NA. Identify HA applications installed on the server. Verify applications defined as requiring HA protections are running on a cluster. From the admin console, navigate to Application >> All Applications >> [application name] >> Target specific application status. If the target application has been designated as an HA application but is not running on a cluster, this is a finding.

## Group: SRG-APP-000435-AS-000163

**Group ID:** `V-81387`

### Rule: The WebSphere Application Server memory session settings must be defined according to application load requirements.

**Rule ID:** `SV-96101r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. To reduce the possibility or effect of a DoS, the application server must employ defined security safeguards. These safeguards will be determined by the placement of the application server and the type of applications being hosted within the application server framework. There are many examples of technologies that exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the application opens at one time). Employing increased capacity and bandwidth, combined with service redundancy or clustering, may reduce the susceptibility to some DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation. Identify the application load requirements defined by system owner. Regular application user session timeout values are defined at the DoD level at 20 minutes. An ISSO risk acceptance is required to deviate from that value. If session timeout values are not set to "20" and an ISSO risk acceptance is provided, this is not a finding. From the admin console, navigate to Servers >> all servers >> [web application server] >> Session management. For every [web application server], verify maximum in-memory session count. Verify "allow overflow" and "session timeout" are set according to application load requirements. If they are not set according to application load requirements, this is a finding.

## Group: SRG-APP-000435-AS-000163

**Group ID:** `V-81389`

### Rule: The WebSphere Application Server thread pool size must be defined according to application load requirements.

**Rule ID:** `SV-96103r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A thread pool enables components of the application server to reuse threads, which eliminates the need to create new threads at run time. Creating new threads expends system resources and can possibly lead to a DoS. Perform loading for your application to determine the required thread pool sizes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan documentation. Identify the application thread pool size requirements defined by system owner. From the admin console navigate to Servers >> all servers >> [server name] >> ThreadPools. Verify thread pool size according to specifications in documentation. If the maximum size for each threadpool is set too large, and not set according to application requirements, this is a finding.

## Group: SRG-APP-000439-AS-000274

**Group ID:** `V-81391`

### Rule: The WebSphere Application Server must remove all export ciphers to protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-96105r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Export grade encryption suites are not strong and do not meet DoD requirements. The encryption for the session becomes easy for the attacker to break. Do not use export grade encryption. Information on disabling export ciphers can be found in Knowledge Center at this link: http://www.ibm.com/support/knowledgecenter/SS7K4U_8.5.5/com.ibm.websphere.ihs.doc/ihs/rihs_ciphspec.html</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the administrative console, navigate to Security >> SSL certificate and key management >> SSL configurations >> [Name] >> for each SSL Configuration Select "Quality of protection (QoP) settings". Under "Cipher suite" settings, if any of the ciphers contained in the "Selected ciphers" box" contain "EXPORT" in their name, this is a finding.

## Group: SRG-APP-000440-AS-000166

**Group ID:** `V-81393`

### Rule: The WebSphere Application Server distribution and consistency services (DCS) transport links must be encrypted.

**Rule ID:** `SV-96107r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A Core Group (HA Domain) is a component of the high availability manager function. It can contain stand-alone servers, cluster members, node agents, administrative agents, and the deployment manager. Core groups rely on DCS, which uses a reliable multicast message (RMM) system for transport. RMM can use one of several wire transport technologies. Depending on your environment, sensitive information might be transmitted over DCS. For example, data in DynaCache and the security subject cache are transmitted using DCS. To ensure this, select a transport type of channel framework and DCS-Secure as channel chain for each core group. Be aware that DCS always authenticates messages when global security is enabled. Once the transport is encrypted, you then have a highly secure channel. Once you have done this, all services that rely on DCS are now using an encrypted and authenticated transport. Those services are DynaCache, memory-to-memory session replication, core groups, Web services caching, and stateful session bean persistence.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the admin console navigate to Servers >> Core groups. For every Core Group listed, select the Core Group [CoreGroup Name]. Under "Transport Type", select the "Channel Framework" button. If the "transport chain" drop down box is not set to "DCS-Secure", this is a finding.

## Group: SRG-APP-000440-AS-000167

**Group ID:** `V-81395`

### Rule: The WebSphere Application Server plugin must be configured to use HTTPS only.

**Rule ID:** `SV-96109r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Web server plug-in transmits information from the Web server to the Web container over HTTP by default. Extra steps must be taken to protect the traffic from the Web server to the Web container. To force the use of HTTPS for all traffic from the plug-in, disable the HTTP transport from the Web container on every application server and then regenerate and deploy the plug-in. WCInboundDefault and the HttpQueueInboundDefault transport chains must be disabled. At which time the plug-in can only use HTTPS and so it will use it for all traffic regardless of how the traffic arrived at the Web container.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the admin console, navigate to Servers >> Server Types >> WebSphere Application Servers >> select each server (server name) >> Web Container Settings >> Web container transport chains. Verify both "WCInboundDefault" and the "HttpQueueInboundDefault" transport chains are disabled. If they are not disabled, this is a finding.

## Group: SRG-APP-000454-AS-000268

**Group ID:** `V-81397`

### Rule: The WebSphere Application Server must remove organization-defined software components after updated versions have been installed.

**Rule ID:** `SV-96111r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, when updating WebSphere application server, the older version of binaries are saved in case a "roll back" is necessary. Not keeping the older version makes it more difficult for attackers to "revert" back to the older version.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review System Security Plan and system documentation to locate the "IBM InstallationManager" folder. Default locations are: UNIX: /opt/InstallationManager Windows: C:\Program Files\InstallationManager UNIX: <IMHOME>/eclipse/tools/imcl -c Select "P" preferences. Select "3" Files for rollback. Windows: <IMHOME>\eclipse\tools\imcl.exe -c Select "P" preferences. Select "3" Files for rollback. If "Save files for rollback" is checked, this is a finding.

## Group: SRG-APP-000456-AS-000266

**Group ID:** `V-81399`

### Rule: The WebSphere Application Server must apply the latest security fixes.

**Rule ID:** `SV-96113r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security vulnerabilities are often addressed by testing and applying the latest security patches and fix packs. Latest fixpacks can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg27009661</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the admin console to determine the WebSphere version. Review patch level and fix pack. If the most recent patches/fix packs have not been applied, this is a finding.

## Group: SRG-APP-000456-AS-000266

**Group ID:** `V-81401`

### Rule: The WebSphere Application Server must install security-relevant software updates within the time period directed by an authoritative source (e.g., IAVMs, CTOs, DTMs, and STIGs).

**Rule ID:** `SV-96115r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes) to production systems after thorough testing of the patches within a lab environment. Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the admin console, click on "welcome". Under Suite Name, locate "WebSphere Application Server". View the "version". Access IBM support website: https://www.ibm.com/support Identify the most recent patch/fix version available for the WebSphere Traditional Application Server (not the Liberty version). If the most recent patches/fix packs have not been applied, this is a finding.

