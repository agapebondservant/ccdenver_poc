# STIG Benchmark: JBoss Enterprise Application Platform 6.3 Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000014-AS-000009

**Group ID:** `V-213494`

### Rule: HTTP management session traffic must be encrypted.

**Rule ID:** `SV-213494r960759_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Types of management interfaces utilized by the JBoss EAP application server include web-based HTTP interfaces as well as command line-based management interfaces. In the event remote HTTP management is required, the access must be via HTTPS. This requirement is in conjunction with the requirement to isolate all management access to a restricted network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. For a standalone configuration run the following command: "ls /core-service=management/management-interface=http-interface" If "secure-socket-binding"=undefined, this is a finding. For a domain configuration run the following command: "ls /host=master/core-service=management/management-interface=http-interface" If "secure-port" is undefined, this is a finding.

## Group: SRG-APP-000015-AS-000010

**Group ID:** `V-213495`

### Rule: HTTPS must be enabled for JBoss web interfaces.

**Rule ID:** `SV-213495r960762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption is critical for protection of web-based traffic. If encryption is not being used to protect the application server's web connectors, malicious users may gain the ability to read or modify the application traffic while it is in transit over the network. The use of cryptography on web connectors secures web-based traffic and mitigates that risk. HTTPS and Transport Layer Security (TLS) are the means in which cryptographic protections are applied to web connectors. FIPS 140-2 approved TLS versions include TLS V1.2 or greater.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. Review the web subsystem and ensure that HTTPS is enabled. Run the command: For a managed domain: "ls /profile=<PROFILE_NAME>/subsystem=web/connector=" For a standalone system: "ls /subsystem=web/connector=" If "https" is not returned, this is a finding.

## Group: SRG-APP-000033-AS-000024

**Group ID:** `V-213496`

### Rule: Java permissions must be set for hosted applications.

**Rule ID:** `SV-213496r1069472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Java Security Manager is a java class that manages the external boundary of the Java Virtual Machine (JVM) sandbox, controlling how code executing within the JVM can interact with resources outside the JVM. The JVM requires a security policy in order to restrict application access. A properly configured security policy will define what rights the application has to the underlying system. For example, rights to make changes to files on the host system or to initiate network sockets in order to connect to another system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Enabling the Security Manager in JDK 24 is an error and if using JDK 24, this is not a finding. Note: Security Manager was deprecated in Java 17 and will be permanently removed in JDK 24. For additional information: <https://openjdk.org/jeps/486> Obtain documentation from the admin that identifies the applications hosted on the JBoss server as well as the corresponding rights the application requires. For example, if the application requires network socket permissions and file write permissions, document those requirements. 1. Identify the JBoss installation as either domain or standalone and review the relevant configuration file. For domain installs: JBOSS_HOME/bin/domain.conf For standalone installs: JBOSS_HOME/bin/standalone.conf 2. Identify the location and name of the security policy by reading the JAVA_OPTS flag -Djava.security.policy=<file name> where <file name> will indicate name and location of security policy. If the application uses a policy URL, obtain the URL and policy file from system admin. 3. Review security policy and ensure hosted applications have the appropriate restrictions placed on them per documented application functionality requirements. If the security policy does not restrict application access to host resources per documented requirements, this is a finding.

## Group: SRG-APP-000033-AS-000024

**Group ID:** `V-213497`

### Rule: The Java Security Manager must be enabled for the JBoss application server.

**Rule ID:** `SV-213497r1069475_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Java Security Manager is a java class that manages the external boundary of the Java Virtual Machine (JVM) sandbox, controlling how code executing within the JVM can interact with resources outside the JVM. The Java Security Manager uses a security policy to determine whether a given action will be permitted or denied. To protect the host system, the JBoss application server must be run within the Java Security Manager.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Enabling the Security Manager in JDK 24 is an error and if using JDK 24, this is not a finding. Note, Security Manager was deprecated in Java 17 and will be permanently removed in JDK 24. For additional information: <https://openjdk.org/jeps/486> To determine if the Java Security Manager is enabled for JBoss, the startup commands must be examined. JBoss can be configured to run in either "domain" or a "standalone" mode. JBOSS_HOME is the variable home directory for the JBoss installation. Use relevant OS commands to navigate the file system. 1. For a managed domain installation, review the domain.conf and domain.conf.bat files: JBOSS_HOME/bin/domain.conf JBOSS_HOME/bin/domain.conf.bat In domain.conf file, ensure there is a JAVA_OPTS flag that loads the Java Security Manager as well as a relevant Java Security policy. Example: JAVA_OPTS="$JAVA_OPTS -Djava.security.manager -Djava.security.policy==$PWD/server.policy -Djboss.home.dir=/path/to/JBOSS_HOME -Djboss.modules.policy-permissions=true" In domain.conf.bat file, ensure JAVA_OPTS flag is set. Example: set "JAVA_OPTS=%JAVA_OPTS% -Djava.security.manager -Djava.security.policy==/path/to/server.policy -Djboss.home.dir=/path/to/JBOSS_HOME -Djboss.modules.policy-permissions=true" 2. For a standalone installation, review the standalone.conf and standalone.conf.bat files: JBOSS_HOME/bin/standalone.conf JBOSS_HOME/bin/standalone.conf.bat In the standalone.conf file, ensure the JAVA_OPTS flag is set. Example: JAVA_OPTS="$JAVA_OPTS -Djava.security.manager -Djava.security.policy==$PWD/server.policy -Djboss.home.dir=$JBOSS_HOME -Djboss.modules.policy-permissions=true" In the standalone.conf.bat file, ensure the JAVA_OPTS flag is set. Example: set "JAVA_OPTS=%JAVA_OPTS% -Djava.security.manager -Djava.security.policy==/path/to/server.policy -Djboss.home.dir=%JBOSS_HOME% -Djboss.modules.policy-permissions=true" If the security manager is not enabled and a security policy not defined, this is a finding.

## Group: SRG-APP-000033-AS-000024

**Group ID:** `V-213498`

### Rule: The JBoss server must be configured with Role Based Access Controls.

**Rule ID:** `SV-213498r1028281_rule`
**Severity:** high

**Description:**
<VulnDiscussion>By default, the JBoss server is not configured to utilize role based access controls (RBAC). RBAC provides the capability to restrict user access to their designated management role, thereby limiting access to only the JBoss functionality that they are supposed to have. Without RBAC, the JBoss server is not able to enforce authorized access according to role.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. Run the following command: For standalone servers: "ls /core-service=management/access=authorization/" For managed domain installations, target the domain-management resource (the core management service for the entire domain): "ls /core-service=management/access=authorization/" If the "provider" attribute is not set to "rbac", this is a finding. (Default, the access control is "provider=simple")

## Group: SRG-APP-000033-AS-000024

**Group ID:** `V-213499`

### Rule: Users in JBoss Management Security Realms must be in the appropriate role.

**Rule ID:** `SV-213499r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security realms are a series of mappings between users and passwords and users and roles. There are 2 JBoss security realms provided by default; they are "management realm" and "application realm". Management realm stores authentication information for the management API, which provides functionality for the web-based management console and the management command line interface (CLI). mgmt-groups.properties stores user to group mapping for the ManagementRealm but only when role-based access controls (RBAC) is enabled. If management users are not in the appropriate role, unauthorized access to JBoss resources can occur.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the mgmt-users.properties file. Also review the <management /> section in the standalone.xml or domain.xml configuration files. The relevant xml file will depend on if the JBoss server is configured in standalone or domain mode. Ensure all users listed in these files are approved for management access to the JBoss server and are in the appropriate role. For domain configurations: <JBOSS_HOME>/domain/configuration/mgmt-users.properties. <JBOSS_HOME>/domain/configuration/domain.xml For standalone configurations: <JBOSS_HOME>/standalone/configuration/mgmt-users.properties. <JBOSS_HOME>/standalone/configuration/standalone.xml If the users listed are not in the appropriate role, this is a finding.

## Group: SRG-APP-000033-AS-000024

**Group ID:** `V-213500`

### Rule: Silent Authentication must be removed from the Default Application Security Realm.

**Rule ID:** `SV-213500r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Silent Authentication is a configuration setting that allows local OS users access to the JBoss server and a wide range of operations without specifically authenticating on an individual user basis. By default $localuser is a Superuser. This introduces an integrity and availability vulnerability and violates best practice requirements regarding accountability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. Verify that Silent Authentication has been removed from the default Application security realm. Run the following command. For standalone servers, run the following command: "ls /core-service=management/security-realm=ApplicationRealm/authentication" For managed domain installations, run the following command: "ls /host=HOST_NAME/core-service=management/security-realm=ApplicationRealm/authentication" If "local" is returned, this is a finding.

## Group: SRG-APP-000033-AS-000024

**Group ID:** `V-213501`

### Rule: Silent Authentication must be removed from the Default Management Security Realm.

**Rule ID:** `SV-213501r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Silent Authentication is a configuration setting that allows local OS users access to the JBoss server and a wide range of operations without specifically authenticating on an individual user basis. By default $localuser is a Superuser. This introduces an integrity and availability vulnerability and violates best practice requirements regarding accountability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. Verify that Silent Authentication has been removed from the default Management security realm. Run the following command. For standalone servers run the following command: "ls /core-service=management/security-realm=ManagementRealm/authentication" For managed domain installations run the following command: "ls /host=HOST_NAME/core-service=management/security-realm=ManagementRealm/authentication" If "local" is returned, this is a finding.

## Group: SRG-APP-000033-AS-000024

**Group ID:** `V-213502`

### Rule: JBoss management interfaces must be secured.

**Rule ID:** `SV-213502r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>JBoss utilizes the concept of security realms to secure the management interfaces used for JBoss server administration. If the security realm attribute is omitted or removed from the management interface definition, access to that interface is no longer secure. The JBoss management interfaces must be secured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. Identify the management interfaces. To identity the management interfaces, run the following command: For standalone servers: "ls /core-service=management/management-interface=" For managed domain installations: "ls /host=HOST_NAME/core-service=management/management-interface=" By default, JBoss provides two management interfaces; they are named "NATIVE-INTERFACE" and "HTTP-INTERFACE". The system may or may not have both interfaces enabled. For each management interface listed as a result of the previous command, append the name of the management interface to the end of the following command. For a standalone system: "ls /core-service=management/management-interface=<MANAGEMENT INTERFACE NAME>" For a managed domain: "ls /host=HOST_NAME/core-service=management/management-interface=<MANAGEMENT INTERFACE NAME>" If the "security-realm=" attribute is not associated with a management realm, this is a finding.

## Group: SRG-APP-000089-AS-000050

**Group ID:** `V-213503`

### Rule: The JBoss server must generate log records for access and authentication events to the management interface.

**Rule ID:** `SV-213503r1028283_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log records can be generated from various components within the JBoss application server. The minimum list of logged events should be those pertaining to access and authentication events to the management interface as well as system startup and shutdown events. By default, JBoss does not log management interface access but does provide a default file handler. This handler needs to be enabled. Configuring this setting meets several STIG auditing requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script to start the Command Line Interface (CLI). Connect to the server and authenticate. Run the command: For a Managed Domain configuration: "ls host=master/server=<SERVERNAME>/core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" For a Standalone configuration: "ls /core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" If "enabled" = false, this is a finding.

## Group: SRG-APP-000090-AS-000051

**Group ID:** `V-213504`

### Rule: JBoss must be configured to allow only the ISSM (or individuals or roles appointed by the ISSM) to select which loggable events are to be logged.

**Rule ID:** `SV-213504r960882_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The JBoss server must be configured to select which personnel are assigned the role of selecting which loggable events are to be logged. In JBoss, the role designated for selecting auditable events is the "Auditor" role. The personnel or roles that can select loggable events are only the ISSM (or individuals or roles appointed by the ISSM).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script to start the Command Line Interface (CLI). Connect to the server and authenticate. Run the command: For a Managed Domain configuration: "ls host=master/server=<SERVERNAME>/core-service=management/access=authorization/role-mapping=Auditor/include=" For a Standalone configuration: "ls /core-service=management/access=authorization/role-mapping=Auditor/include=" If the list of users in the Auditors group is not approved by the ISSM, this is a finding.

## Group: SRG-APP-000092-AS-000053

**Group ID:** `V-213505`

### Rule: JBoss must be configured to initiate session logging upon startup.

**Rule ID:** `SV-213505r960888_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Session logging activities are developed, integrated, and used in consultation with legal counsel in accordance with applicable federal laws, Executive Orders, directives, policies, or regulations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script to start the Command Line Interface (CLI). Connect to the server and authenticate. Run the command: For a Managed Domain configuration: "ls host=master/server=<SERVERNAME>/core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" For a Standalone configuration: "ls /core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" If "enabled" = false, this is a finding.

## Group: SRG-APP-000095-AS-000056

**Group ID:** `V-213506`

### Rule: JBoss must be configured to log the IP address of the remote system connecting to the JBoss system/cluster.

**Rule ID:** `SV-213506r960891_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system logging capability is critical for accurate forensic analysis. Without being able to establish what type of event occurred, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible. Log record content that may be necessary to satisfy the requirement of this control includes time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Application servers must log all relevant log data that pertains to the application server. Examples of relevant data include, but are not limited to, Java Virtual Machine (JVM) activity, HTTPD/Web server activity, and application server-related system process activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script to start the Command Line Interface (CLI). Connect to the server and authenticate. Run the command: For a Managed Domain configuration: "ls host=master/server=<SERVERNAME>/core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" For a Standalone configuration: "ls /core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" If "enabled" = false, this is a finding.

## Group: SRG-APP-000095-AS-000056

**Group ID:** `V-213507`

### Rule: JBoss must be configured to produce log records containing information to establish what type of events occurred.

**Rule ID:** `SV-213507r960891_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system logging capability is critical for accurate forensic analysis. Without being able to establish what type of event occurred, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible. Log record content that may be necessary to satisfy the requirement of this control includes time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Application servers must log all relevant log data that pertains to the application server. Examples of relevant data include, but are not limited to, Java Virtual Machine (JVM) activity, HTTPD/Web server activity, and application server-related system process activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script to start the Command Line Interface (CLI). Connect to the server and authenticate. Run the command: For a Managed Domain configuration: "ls host=master/server=<SERVERNAME>/core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" For a Standalone configuration: "ls /core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" If "enabled" = false, this is a finding.

## Group: SRG-APP-000096-AS-000059

**Group ID:** `V-213508`

### Rule: JBoss Log Formatter must be configured to produce log records that establish the date and time the events occurred.

**Rule ID:** `SV-213508r960894_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct order of the events that occurred is important during forensic analysis. Events that appear harmless by themselves might be flagged as a potential threat when properly viewed in sequence. By also establishing the event date and time, an event can be properly viewed with an enterprise tool to fully see a possible threat in its entirety. Without sufficient information establishing when the log event occurred, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, filenames involved, access control, or flow control rules invoked. In addition to logging event information, application servers must also log the corresponding dates and times of these events. Examples of event data include, but are not limited to, Java Virtual Machine (JVM) activity, HTTPD activity, and application server-related system process activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script to start the Command Line Interface (CLI). Connect to the server and authenticate. Run the command: For a Managed Domain configuration: "ls host=master/server=<SERVERNAME>/core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" For a Standalone configuration: "ls /core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" If "enabled" = false, this is a finding.

## Group: SRG-APP-000097-AS-000060

**Group ID:** `V-213509`

### Rule: JBoss must be configured to produce log records that establish which hosted application triggered the events.

**Rule ID:** `SV-213509r960897_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. By default, no web logging is enabled in JBoss. Logging can be configured per web application or by virtual server. If web application logging is not set up, application activity will not be logged. Ascertaining the correct location or process within the application server where the events occurred is important during forensic analysis. To determine where an event occurred, the log data must contain data containing the application identity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Application logs are a configurable variable. Interview the system admin, and have them identify the applications that are running on the application server. Have the system admin identify the log files/location where application activity is stored. Review the log files to ensure each application is uniquely identified within the logs or each application has its own unique log file. Generate application activity by either authenticating to the application or generating an auditable event, and ensure the application activity is recorded in the log file. Recently time stamped application events are suitable evidence of compliance. If the log records do not indicate which application hosted on the application server generated the event, or if no events are recorded related to application activity, this is a finding.

## Group: SRG-APP-000098-AS-000061

**Group ID:** `V-213510`

### Rule: JBoss must be configured to record the IP address and port information used by management interface network traffic.

**Rule ID:** `SV-213510r960900_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application server logging capability is critical for accurate forensic analysis. Without sufficient and accurate information, a correct replay of the events cannot be determined. Ascertaining the correct source, e.g., source IP, of the events is important during forensic analysis. Correctly determining the source will add information to the overall reconstruction of the loggable event. By determining the source of the event correctly, analysis of the enterprise can be undertaken to determine if the event compromised other assets within the enterprise. Without sufficient information establishing the source of the logged event, investigation into the cause of event is severely hindered. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, filenames involved, access control, or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script to start the Command Line Interface (CLI). Connect to the server and authenticate. Run the command: For a Managed Domain configuration: "ls host=master/server=<SERVERNAME>/core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" For a Standalone configuration: "ls /core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" If "enabled" = false, this is a finding.

## Group: SRG-APP-000099-AS-000062

**Group ID:** `V-213511`

### Rule: The application server must produce log records that contain sufficient information to establish the outcome of events.

**Rule ID:** `SV-213511r960903_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system logging capability is critical for accurate forensic analysis. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, filenames involved, access control or flow control rules invoked. Success and failure indicators ascertain the outcome of a particular application server event or function. As such, they also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response. Event outcome may also include event-specific results (e.g., the security state of the information system after the event occurred).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script to start the Command Line Interface (CLI). Connect to the server and authenticate. Run the command: For a Managed Domain configuration: "ls host=master/server=<SERVERNAME>/core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" For a Standalone configuration: "ls /core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" If "enabled" = false, this is a finding.

## Group: SRG-APP-000100-AS-000063

**Group ID:** `V-213512`

### Rule: JBoss ROOT logger must be configured to utilize the appropriate logging level.

**Rule ID:** `SV-213512r960906_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system logging capability is critical for accurate forensic analysis. Log record content that may be necessary to satisfy the requirement of this control includes: time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. See Chapter 14, Section 14.1.9, Table 14.4 of the Red Hat JBoss EAP Administration and Configuration Guide version 6.3 for specific details on log levels and log level values. The JBOSS application server ROOT logger captures all messages not captured by a log category and sends them to a log handler (FILE, CONSOLE, SYSLOG, ETC.). By default, the ROOT logger level is set to INFO, which is a value of 800. This will capture most events adequately. Any level numerically higher than INFO (> 800) records less data and may result in an insufficient amount of information being logged by the ROOT logger. This can result in failed forensic investigations. The ROOT logger level must be INFO level or lower to provide adequate log information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script to start the Command Line Interface (CLI). Connect to the server and authenticate. The PROFILE NAMEs included with a Managed Domain JBoss configuration are: "default", "full", "full-ha" or "ha" For a Managed Domain configuration, you must check each profile name: For each PROFILE NAME, run the command: "ls /profile=<PROFILE NAME>/subsystem=logging/root-logger=ROOT" If ROOT logger "level" is not set to INFO, DEBUG or TRACE This is a finding for each <PROFILE NAME> (default, full, full-ha and ha) For a Standalone configuration: "ls /subsystem=logging/root-logger=ROOT" If "level" not = INFO, DEBUG or TRACE, this is a finding.

## Group: SRG-APP-000118-AS-000078

**Group ID:** `V-213513`

### Rule: File permissions must be configured to protect log information from any type of unauthorized read access.

**Rule ID:** `SV-213513r960930_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. When not configured to use a centralized logging solution like a syslog server, the JBoss EAP application server writes log data to log files that are stored on the OS; appropriate file permissions must be used to restrict access. Log information includes all information (e.g., log records, log settings, transaction logs, and log reports) needed to successfully log information system activity. Application servers must protect log information from unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the log file locations and inspect the file permissions. Interview the system admin to determine log file locations. The default location for the log files is: Standalone configuration: <JBOSS_HOME>/standalone/log/ Managed Domain configuration: <JBOSS_HOME>/domain/servers/<servername>/log/ <JBOSS_HOME>/domain/log/ Review the file permissions for the log file directories. The method used for identifying file permissions will be based upon the OS the EAP server is installed on. Identify all users with file permissions that allow them to read log files. Request documentation from system admin that identifies the users who are authorized to read log files. If unauthorized users are allowed to read log files, or if documentation that identifies the users who are authorized to read log files is missing, this is a finding.

## Group: SRG-APP-000119-AS-000079

**Group ID:** `V-213514`

### Rule: File permissions must be configured to protect log information from unauthorized modification.

**Rule ID:** `SV-213514r960933_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. When not configured to use a centralized logging solution like a syslog server, the JBoss EAP application server writes log data to log files that are stored on the OS; appropriate file permissions must be used to restrict modification. Log information includes all information (e.g., log records, log settings, transaction logs, and log reports) needed to successfully log information system activity. Application servers must protect log information from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the log file locations and inspect the file permissions. Interview the system admin to determine log file locations. The default location for the log files is: Standalone configuration: <JBOSS_HOME>/standalone/log/ Managed Domain configuration: <JBOSS_HOME>/domain/servers/<servername>/log/ <JBOSS_HOME>/domain/log/ Review the file permissions for the log file directories. The method used for identifying file permissions will be based upon the OS the EAP server is installed on. Identify all users with file permissions that allow them to modify log files. Request documentation from system admin that identifies the users who are authorized to modify log files. If unauthorized users are allowed to modify log files, or if documentation that identifies the users who are authorized to modify log files is missing, this is a finding.

## Group: SRG-APP-000120-AS-000080

**Group ID:** `V-213515`

### Rule: File permissions must be configured to protect log information from unauthorized deletion.

**Rule ID:** `SV-213515r960936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. When not configured to use a centralized logging solution like a syslog server, the JBoss EAP application server writes log data to log files that are stored on the OS, appropriate file permissions must be used to restrict deletion. Logon formation includes all information (e.g., log records, log settings, transaction logs, and log reports) needed to successfully log information system activity. Application servers must protect log information from unauthorized deletion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the log file locations and inspect the file permissions. Interview the system admin to determine log file locations. The default location for the log files is: Standalone configuration: <JBOSS_HOME>/standalone/log/ Managed Domain configuration: <JBOSS_HOME>/domain/servers/<servername>/log/ <JBOSS_HOME>/domain/log/ Review the file permissions for the log file directories. The method used for identifying file permissions will be based upon the OS the EAP server is installed on. Identify all users with file permissions that allow them to delete log files. Request documentation from system admin that identifies the users who are authorized to delete log files. If unauthorized users are allowed to delete log files, or if documentation that identifies the users who are authorized to delete log files is missing, this is a finding.

## Group: SRG-APP-000125-AS-000084

**Group ID:** `V-213516`

### Rule: JBoss log records must be off-loaded onto a different system or system component a minimum of every seven days.

**Rule ID:** `SV-213516r960948_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>JBoss logs by default are written to the local file system. A centralized logging solution like syslog should be used whenever possible; however, any log data stored to the file system needs to be off-loaded. JBoss EAP does not provide an automated backup capability. Instead, reliance is placed on OS or third-party tools to back up or off-load the log files. Protection of log data includes assuring log data is not accidentally lost or deleted. Off-loading log records to a different system or onto separate media from the system the application server is actually running on helps to assure that, in the event of a catastrophic system failure, the log records will be retained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the system admin and obtain details on how the log files are being off-loaded to a different system or media. If the log files are not off-loaded a minimum of every 7 days, this is a finding.

## Group: SRG-APP-000133-AS-000092

**Group ID:** `V-213517`

### Rule: mgmt-users.properties file permissions must be set to allow access to authorized users only.

**Rule ID:** `SV-213517r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The mgmt-users.properties file contains the password hashes of all users who are in a management role and must be protected. Application servers have the ability to specify that the hosted applications utilize shared libraries. The application server must have a capability to divide roles based upon duties wherein one project user (such as a developer) cannot modify the shared library code of another project user. The application server must also be able to specify that non-privileged users cannot modify any shared library code at all.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The mgmt-users.properties files are located in the standalone or domain configuration folder. <JBOSS_HOME>/domain/configuration/mgmt-users.properties. <JBOSS_HOME>/standalone/configuration/mgmt-users.properties. Identify users who have access to the files using relevant OS commands. Obtain documentation from system admin identifying authorized users. Owner can be full access. Group can be full access. All others must have execute permissions only. If the file permissions are not configured so as to restrict access to only authorized users, or if documentation that identifies authorized users is missing, this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-213518`

### Rule: JBoss process owner interactive access must be restricted.

**Rule ID:** `SV-213518r960963_rule`
**Severity:** high

**Description:**
<VulnDiscussion>JBoss does not require admin rights to operate and should be run as a regular user. In addition, if the user account was to be compromised and the account was allowed interactive logon rights, this would increase the risk and attack surface against the JBoss system. The right to interactively log on to the system using the JBoss account should be limited according to the OS capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Identify the user account used to run the JBoss server. Use relevant OS commands to determine logon rights to the system. This account should not have full shell/interactive access to the system. If the user account used to operate JBoss can log on interactively, this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-213519`

### Rule: Google Analytics must be disabled in EAP Console.

**Rule ID:** `SV-213519r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Google Analytics feature aims to help Red Hat EAP team understand how customers are using the console and which parts of the console matter the most to the customers. This information will, in turn, help the team to adapt the console design, features, and content to the immediate needs of the customers. Sending analytical data to the vendor introduces risk of unauthorized data exfiltration. This capability must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the EAP web console by pointing a web browser to HTTPS://<SERVERNAME>:9443 or HTTP://<SERVERNAME>:9990 Log on to the admin console using admin credentials. On the bottom right-hand side of the screen, select "Settings". If the "Enable Data Usage Collection" box is checked, this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-213520`

### Rule: JBoss process owner execution permissions must be limited.

**Rule ID:** `SV-213520r960963_rule`
**Severity:** high

**Description:**
<VulnDiscussion>JBoss EAP application server can be run as the OS admin, which is not advised. Running the application server with admin privileges increases the attack surface by granting the application server more rights than it requires in order to operate. If the server is compromised, the attacker will have the same rights as the application server, which in that case would be admin rights. The JBoss EAP server must not be run as the admin user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The script that is used to start JBoss determines the mode in which JBoss will operate, which will be in either in standalone mode or domain mode. Both scripts are installed by default in the <JBOSS_HOME>/bin/ folder. In addition to running the JBoss server as an interactive script launched from the command line, JBoss can also be started as a service. The scripts used to start JBoss are: Red Hat: standalone.sh domain.sh Windows: standalone.bat domain.bat Use the relevant OS commands to determine JBoss ownership. When running as a process: Red Hat: "ps -ef|grep -i jboss". Windows: "services.msc". Search for the JBoss process, which by default is named "JBOSSEAP6". If the user account used to launch the JBoss script or start the JBoss process has admin rights on the system, this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-213521`

### Rule: JBoss QuickStarts must be removed.

**Rule ID:** `SV-213521r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>JBoss QuickStarts are demo applications that can be deployed quickly. Demo applications are not written with security in mind and often open new attack vectors. QuickStarts must be removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the <JBOSS_HOME> folder. If a jboss-eap-6.3.0-GA-quickstarts folder exits, this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-213522`

### Rule: Remote access to JMX subsystem must be disabled.

**Rule ID:** `SV-213522r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The JMX subsystem allows you to trigger JDK and application management operations remotely. In a managed domain configuration, the JMX subsystem is removed by default. For a standalone configuration, it is enabled by default and must be removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script to start the Command Line Interface (CLI). Connect to the server and authenticate. For a Managed Domain configuration, you must check each profile name: For each PROFILE NAME, run the command: "ls /profile=<PROFILE NAME>/subsystem=jmx/remoting-connector" For a Standalone configuration: "ls /subsystem=jmx/remoting-connector" If "jmx" is returned, this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-213523`

### Rule: Welcome Web Application must be disabled.

**Rule ID:** `SV-213523r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Welcome to JBoss web page provides a redirect to the JBoss admin console, which, by default, runs on TCP 9990 as well as redirects to the Online User Guide and Online User Groups hosted at locations on the Internet. The welcome page is unnecessary and should be disabled or replaced with a valid web page.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use a web browser and browse to HTTP://JBOSS SERVER IP ADDRESS:8080 If the JBoss Welcome page is displayed, this is a finding.

## Group: SRG-APP-000141-AS-000095

**Group ID:** `V-213524`

### Rule: Any unapproved applications must be removed.

**Rule ID:** `SV-213524r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Extraneous services and applications running on an application server expands the attack surface and increases risk to the application server. Securing any server involves identifying and removing any unnecessary services and, in the case of an application server, unnecessary and/or unapproved applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. Run the command: ls /deployment The list of deployed applications is displayed. Have the system admin identify the applications listed and confirm they are approved applications. If the system admin cannot provide documentation proving their authorization for deployed applications, this is a finding.

## Group: SRG-APP-000142-AS-000014

**Group ID:** `V-213525`

### Rule: JBoss application and management ports must be approved by the PPSM CAL.

**Rule ID:** `SV-213525r1043177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some networking protocols may not meet organizational security requirements to protect data and components. Application servers natively host a number of various features, such as management interfaces, httpd servers and message queues. These features all run on TCPIP ports. This creates the potential that the vendor may choose to utilize port numbers or network services that have been deemed unusable by the organization. The application server must have the capability to both reconfigure and disable the assigned ports without adversely impacting application server operation capabilities. For a list of approved ports and protocols, reference the DoD ports and protocols website at https://powhatan.iiie.disa.mil/ports/cal.html.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the EAP web console by pointing a web browser to HTTPS://<Servername>:9443 or HTTP://<Servername>:9990 Log on to the admin console using admin credentials Select the "Configuration" tab Expand the "General Configuration" sub system by clicking on the + Select "Socket Binding" Select the "View" option next to "standard-sockets" Select "Inbound" Review the configured ports and determine if they are all approved by the PPSM CAL. If all the ports are not approved by the PPSM CAL, this is a finding.

## Group: SRG-APP-000148-AS-000101

**Group ID:** `V-213526`

### Rule: The JBoss Server must be configured to utilize a centralized authentication mechanism such as AD or LDAP.

**Rule ID:** `SV-213526r1051118_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthorized access, application server users must be uniquely identified and authenticated. This is typically accomplished via the use of a user store that is either local (OS-based) or centralized (Active Directory/LDAP) in nature. It should be noted that JBoss does not specifically mention Active Directory since AD is LDAP aware. To ensure accountability and prevent unauthorized access, the JBoss Server must be configured to utilize a centralized authentication mechanism.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. To obtain the list of security realms run the command: "ls /core-service=management/security-realm=" Review each security realm using the command: "ls /core-service=management/security-realm=<SECURITY_REALM_NAME>/authentication" If this command does not return a security realm that uses LDAP for authentication, this is a finding.

## Group: SRG-APP-000149-AS-000102

**Group ID:** `V-213527`

### Rule: The JBoss Server must be configured to use certificates to authenticate admins.

**Rule ID:** `SV-213527r960972_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Multifactor authentication creates a layered defense and makes it more difficult for an unauthorized person to access the application server. If one factor is compromised or broken, the attacker still has at least one more barrier to breach before successfully breaking into the target. Unlike a simple username/password scenario where the attacker could gain access by knowing both the username and password without the user knowing his account was compromised, multifactor authentication adds the requirement that the attacker must have something from the user, such as a token, or to biometrically be the user. Multifactor authentication is defined as: using two or more factors to achieve authentication. Factors include: (i) something a user knows (e.g., password/PIN); (ii) something a user has (e.g., cryptographic identification device, token); or (iii) something a user is (e.g., biometric). A CAC or PKI Hardware Token meets this definition. A privileged account is defined as an information system account with authorizations of a privileged user. These accounts would be capable of accessing the web management interface. When accessing the application server via a network connection, administrative access to the application server must be PKI Hardware Token enabled or a DoD-approved soft certificate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. Follow these steps: 1. Identify the security realm assigned to the management interfaces by using the following command: For standalone systems: "ls /core-service=management/management-interface=<INTERFACE-NAME>" For managed domain systems: "ls /host=master/core-service=management/management-interface=<INTERFACE-NAME>" Document the name of the security-realm associated with each management interface. 2. Review the security realm using the command: For standalone systems: "ls /core-service=management/security-realm=<SECURITY_REALM_NAME>/authentication" For managed domains: "ls /host=master/core-service=management/security-realm=<SECURITY_REALM_NAME>/authentication" If the command in step 2 does not return a security realm that uses certificates for authentication, this is a finding.

## Group: SRG-APP-000153-AS-000104

**Group ID:** `V-213528`

### Rule: The JBoss server must be configured to use individual accounts and not generic or shared accounts.

**Rule ID:** `SV-213528r981680_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure individual accountability and prevent unauthorized access, application server users (and any processes acting on behalf of application server users) must be individually identified and authenticated. A group authenticator is a generic account used by multiple individuals. Use of a group authenticator alone does not uniquely identify individual users. Application servers must ensure that individual users are authenticated prior to authenticating via role or group authentication. This is to ensure that there is non-repudiation for actions taken.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the application server management interface is configured to use LDAP authentication this requirement is NA. Determine the mode in which the JBoss server is operating by authenticating to the OS, changing to the <JBOSS_HOME>/bin/ folder and executing the jboss-cli script. Connect to the server and authenticate. Run the command: "ls" and examine the "launch-type" setting. User account information is stored in the following files for a JBoss server configured in standalone mode. The command line flags passed to the "standalone" startup script determine the standalone operating mode: <JBOSS_HOME>/standalone/configuration/standalone.xml <JBOSS_HOME>/standalone/configuration/standalone-full.xml <JBOSS_HOME>/standalone/configuration/standalone.-full-ha.xml <JBOSS_HOME>/standalone/configuration/standalone.ha.xml For a Managed Domain: <JBOSS_HOME>/domain/configuration/domain.xml. Review file(s) for generic or shared user accounts. Open each xml file with a text editor and locate the <management-interfaces> section. Review the <user name = "xxxxx"> sub-section where "xxxxx" will be a user name. Have the system administrator identify the user of each user account. If user accounts are not assigned to individual users, this is a finding.

## Group: SRG-APP-000163-AS-000111

**Group ID:** `V-213529`

### Rule: JBoss management Interfaces must be integrated with a centralized authentication mechanism that is configured to manage accounts according to DoD policy.

**Rule ID:** `SV-213529r981681_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>JBoss EAP provides a security realm called ManagementRealm. By default, this realm uses the mgmt-users.properties file for authentication. Using file-based authentication does not allow the JBoss server to be in compliance with a wide range of user management requirements such as automatic disabling of inactive accounts as per DoD policy. To address this issue, the management interfaces used to manage the JBoss server must be associated with a security realm that provides centralized authentication management. Examples are AD or LDAP. Management of user identifiers is not applicable to shared information system accounts (e.g., guest and anonymous accounts). It is commonly the case that a user account is the name of an information system account associated with an individual.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. Obtain the list of management interfaces by running the command: "ls /core-service=management/management-interface" Identify the security realm used by each management interface configuration by running the command: "ls /core-service=management/management-interface=<MANAGEMENT-INTERFACE-NAME>" Determine if the security realm assigned to the management interface uses LDAP for authentication by running the command: "ls /core-service=management/security-realm=<SECURITY_REALM_NAME>/authentication" If the security realm assigned to the management interface does not utilize LDAP for authentication, this is a finding.

## Group: SRG-APP-000171-AS-000119

**Group ID:** `V-213530`

### Rule: The JBoss Password Vault must be used for storing passwords or other sensitive configuration information.

**Rule ID:** `SV-213530r981682_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>JBoss EAP 6 has a Password Vault to encrypt sensitive strings, store them in an encrypted keystore, and decrypt them for applications and verification systems. Plain-text configuration files, such as XML deployment descriptors, need to specify passwords and other sensitive information. Use the JBoss EAP Password Vault to securely store sensitive strings in plain-text files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Based on your installation, use the relevant OS commands and syntax to access the standalone or domain configuration folder. <JBOSS_HOME>/standalone/configuration folder. Review the standalone.xml file. <JBOSS_HOME>/domain/configuration folder. Review the domain.xml file If the <vault> section does not exist or if the <vault-option> settings are not configured, this is a finding. If the <vault> section does not exist or if the <vault-option> settings are not configured, this is a finding.

## Group: SRG-APP-000171-AS-000119

**Group ID:** `V-213531`

### Rule: JBoss KeyStore and Truststore passwords must not be stored in clear text.

**Rule ID:** `SV-213531r981682_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access to the JBoss Password Vault must be secured, and the password used to access must be encrypted. There is a specific process used to generate the encrypted password hash. This process must be followed in order to store the password in an encrypted format. The admin must utilize this process in order to ensure the Keystore password is encrypted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default location for the keystore used by the JBoss vault is the <JBOSS_HOME>/vault/ folder. If a vault keystore has been created, by default it will be in the file: <JBOSS_HOME>/vault/vault.keystore. The file stores a single key, with the default alias vault, which will be used to store encrypted strings, such as passwords, for JBoss EAP. Have the system admin provide the procedure used to encrypt the keystore password that unlocks the keystore. If the system administrator is unable to demonstrate or provide written process documentation on how to encrypt the keystore password, this is a finding.

## Group: SRG-APP-000172-AS-000120

**Group ID:** `V-213532`

### Rule: LDAP enabled security realm value allow-empty-passwords must be set to false.

**Rule ID:** `SV-213532r961029_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords during transmission. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Application servers have the capability to utilize either certificates (tokens) or user IDs and passwords in order to authenticate. When the application server transmits or receives passwords, the passwords must be encrypted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. Run the command: "ls /core-service=management/security-realm=ldap_security_realm/authentication=ldap" If "allow-empty-passwords=true", this is a finding.

## Group: SRG-APP-000172-AS-000121

**Group ID:** `V-213533`

### Rule: JBoss must utilize encryption when using LDAP for authentication.

**Rule ID:** `SV-213533r961029_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords during transmission. Application servers have the capability to utilize LDAP directories for authentication. If LDAP connections are not protected during transmission, sensitive authentication credentials can be stolen. When the application server utilizes LDAP, the LDAP traffic must be encrypted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. Run the following command: For standalone servers: "ls /socket-binding-group=standard-sockets/remote-destination-outbound-socket-binding=ldap_connection" For managed domain installations: "ls /socket-binding-group=<PROFILE>/remote-destination-outbound-socket-binding=" The default port for secure LDAP is 636. If 636 or secure LDAP protocol is not utilized, this is a finding.

## Group: SRG-APP-000176-AS-000125

**Group ID:** `V-213534`

### Rule: The JBoss server must be configured to restrict access to the web servers private key to authenticated system administrators.

**Rule ID:** `SV-213534r961041_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The cornerstone of the PKI is the private key used to encrypt or digitally sign information. If the private key is stolen, this will lead to the compromise of the authentication and non-repudiation gained through PKI because the attacker can use the private key to digitally sign documents and can pretend to be the authorized user. Both the holders of a digital certificate and the issuing authority must protect the computers, storage devices, or whatever they use to keep the private keys. Java-based application servers utilize the Java keystore, which provides storage for cryptographic keys and certificates. The keystore is usually maintained in a file stored on the file system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default location for the keystore used by the JBoss vault is the <JBOSS_HOME>/vault/ folder. If a vault keystore has been created, by default it will be in the file: <JBOSS_HOME>/vault/vault.keystore. The file stores a single key, with the default alias vault, which will be used to store encrypted strings, such as passwords, for JBoss EAP. Browse to the JBoss vault folder using the relevant OS commands. Review the file permissions and ensure only system administrators and JBoss users are allowed access. Owner can be full access Group can be full access All others must be restricted to execute access or no permission. If non-system administrators are allowed to access the <JBOSS_HOME>/vault/ folder, this is a finding.

## Group: SRG-APP-000211-AS-000146

**Group ID:** `V-213535`

### Rule: The JBoss server must separate hosted application functionality from application server management functionality.

**Rule ID:** `SV-213535r961095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The application server consists of the management interface and hosted applications. By separating the management interface from hosted applications, the user must authenticate as a privileged user to the management interface before being presented with management functionality. This prevents non-privileged users from having visibility to functions not available to the user. By limiting visibility, a compromised non-privileged account does not offer information to the attacker or functionality and information needed to further the attack on the application server. JBoss is designed to operate with separate application and management interfaces. The JBoss server is started via a script. To start the JBoss server in domain mode, the admin will execute the <JBOSS_HOME>/bin/domain.sh or domain.bat script. To start the JBoss server in standalone mode, the admin will execute <JBOSS_HOME>/bin/standalone.bat or standalone.sh. Command line flags are used to specify which network address is used for management and which address is used for public/application access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If JBoss is not started with separate management and public interfaces, this is a finding. Review the network design documents to identify the IP address space for the management network. Use relevant OS commands and administrative techniques to determine how the system administrator starts the JBoss server. This includes interviewing the system admin, using the "ps -ef|grep" command for UNIX like systems or checking command line flags and properties on batch scripts for Windows systems. Ensure the startup syntax used to start JBoss specifies a management network address and a public network address. The "-b" flag specifies the public address space. The "-bmanagement" flag specifies the management address space. Example: <JBOSS_HOME>/bin/standalone.sh -bmanagement 10.10.10.35 -b 192.168.10.25 If JBoss is not started with separate management and public interfaces, this is a finding.

## Group: SRG-APP-000231-AS-000133

**Group ID:** `V-213536`

### Rule: JBoss file permissions must be configured to protect the confidentiality and integrity of application files.

**Rule ID:** `SV-213536r961128_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The JBoss EAP Application Server is a Java-based AS. It is installed on the OS file system and depends upon file system access controls to protect application data at rest. The file permissions set on the JBoss EAP home folder must be configured so as to limit access to only authorized people and processes. The account used for operating the JBoss server and any designated administrative or operational accounts are the only accounts that should have access. When data is written to digital media such as hard drives, mobile computers, external/removable hard drives, personal digital assistants, flash/thumb drives, etc., there is risk of data loss and data compromise. Steps must be taken to ensure data stored on the device is protected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
By default, JBoss installs its files into a folder called "jboss-eap-6.3". This folder by default is stored within the home folder of the JBoss user account. The installation process, however, allows for the override of default values to obtain folder and user account information from the system admin. Log on with a user account with JBoss access and permissions. Navigate to the "Jboss-eap-6.3" folder using the relevant OS commands for either a UNIX-like OS or a Windows OS. Examine the permissions of the JBoss folder. Owner can be full access. Group can be full access. All others must be restricted to execute access or no permission. If the JBoss folder is world readable or world writeable, this is a finding.

## Group: SRG-APP-000267-AS-000170

**Group ID:** `V-213537`

### Rule: Access to JBoss log files must be restricted to authorized users.

**Rule ID:** `SV-213537r961170_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the application provides too much information in error logs and administrative messages to the screen, this could lead to compromise. The structure and content of error messages need to be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements. Application servers must protect the error messages that are created by the application server. All application server users' accounts are used for the management of the server and the applications residing on the application server. All accounts are assigned to a certain role with corresponding access rights. The application server must restrict access to error messages so only authorized users may view them. Error messages are usually written to logs contained on the file system. The application server will usually create new log files as needed and must take steps to ensure that the proper file permissions are utilized when the log files are created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the JBoss log folder is installed in the default location and 213514 (JBOS-AS-000170) is not a finding, the log folders are protected and this requirement is not a finding. By default, JBoss installs its log files into a sub-folder of the "jboss-eap-6.3" home folder. Using a UNIX like OS example, the default location for log files is: JBOSS_HOME/standalone/log JBOSS_HOME/domain/log For a standalone configuration: JBOSS_HOME/standalone/log/server.log" Contains all server log messages, including server startup messages. For a domain configuration: JBOSS_HOME/domain/log/hostcontroller.log Host Controller boot log. Contains log messages related to the startup of the host controller. JBOSS_HOME/domain/log/processcontroller.log Process controller boot log. Contains log messages related to the startup of the process controller. JBOSS_HOME/domain/servers/SERVERNAME/log/server.log The server log for the named server. Contains all log messages for that server, including server startup messages. Log on with an OS user account with JBoss access and permissions. Navigate to the "Jboss-eap-6.3" folder using the relevant OS commands for either a UNIX like OS or a Windows OS. Examine the permissions of the JBoss logs folders. Owner can be full access. Group can be full access. All others must be restricted. If the JBoss log folder is world readable or world writeable, this is a finding.

## Group: SRG-APP-000316-AS-000199

**Group ID:** `V-213538`

### Rule: Network access to HTTP management must be disabled on domain-enabled application servers not designated as the domain controller.

**Rule ID:** `SV-213538r961281_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When configuring JBoss application servers into a domain configuration, HTTP management capabilities are not required on domain member servers as management is done via the server that has been designated as the domain controller. Leaving HTTP management capabilities enabled on domain member servers increases the attack surfaces; therefore, management services on domain member servers must be disabled and management services performed via the domain controller.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to each of the JBoss domain member servers. Note: Sites that manage systems using the JBoss Operations Network client require HTTP interface access. It is acceptable that the management console alone be disabled rather than disabling the entire interface itself. Run the <JBOSS_HOME>/bin/jboss-cli command line interface utility and connect to the JBoss server. Run the following command: ls /core-service=management/management-interface=httpinterface/ If "console-enabled=true", this is a finding.

## Group: SRG-APP-000340-AS-000185

**Group ID:** `V-213539`

### Rule: The application server must prevent non-privileged users from executing privileged functions to include disabling, circumventing, or altering implemented security safeguards/countermeasures.

**Rule ID:** `SV-213539r961353_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Restricting non-privileged users also prevents an attacker who has gained access to a non-privileged account, from elevating privileges, creating accounts, and performing system checks and maintenance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. Run the following command: For standalone servers: "ls /core-service=management/access=authorization/" For managed domain installations: "ls /host=master/core-service=management/access=authorization/" If the "provider" attribute is not set to "rbac", this is a finding.

## Group: SRG-APP-000343-AS-000030

**Group ID:** `V-213540`

### Rule: The JBoss server must be configured to log all admin activity.

**Rule ID:** `SV-213540r961362_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to be able to provide a forensic history of activity, the application server must ensure users who are granted a privileged role or those who utilize a separate distinct account when accessing privileged functions or data have their actions logged. If privileged activity is not logged, no forensic logs can be used to establish accountability for privileged actions that occur on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. Run the command: /core-service=management/access=audit:read-resource(recursive=true) Under the "logger" => {audit-log} section of the returned response: If "enabled" => false, this is a finding

## Group: SRG-APP-000358-AS-000064

**Group ID:** `V-213541`

### Rule: The JBoss server must be configured to utilize syslog logging.

**Rule ID:** `SV-213541r961395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system logging capability is critical for accurate forensic analysis. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, filenames involved, access control or flow control rules invoked. Off-loading is a common process in information systems with limited log storage capacity. Centralized management of log records provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. Application servers and their related components are required to off-load log records onto a different system or media than the system being logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. Run the command: Standalone configuration: "ls /subsystem=logging/syslog-handler=" Domain configuration: "ls /profile=<specify>/subsystem=logging/syslog-handler=" Where <specify> = the selected application server profile of; default,full, full-ha or ha. If no values are returned, this is a finding.

## Group: SRG-APP-000380-AS-000088

**Group ID:** `V-213542`

### Rule: Production JBoss servers must not allow automatic application deployment.

**Rule ID:** `SV-213542r961461_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with access restrictions pertaining to change control, it should be noted that any changes to the software and/or application server configuration can potentially have significant effects on the overall security of the system. Access restrictions for changes also include application software libraries. If the application server provides automatic code deployment capability, (where updates to applications hosted on the application server are automatically performed, usually by the developers' IDE tool), it must also provide a capability to restrict the use of automatic application deployment. Automatic code deployments are allowable in a development environment, but not in production.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. Run the command: ls /subsystem=deployment-scanner/scanner=default If "scan-enabled"=true, this is a finding.

## Group: SRG-APP-000381-AS-000089

**Group ID:** `V-213543`

### Rule: Production JBoss servers must log when failed application deployments occur.

**Rule ID:** `SV-213543r981687_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without logging the enforcement of access restrictions against changes to the application server configuration, it will be difficult to identify attempted attacks, and a log trail will not be available for forensic investigation for after-the-fact actions. Configuration changes may occur to any of the modules within the application server through the management interface, but logging of actions to the configuration of a module outside the application server is not logged. Enforcement actions are the methods or mechanisms used to prevent unauthorized changes to configuration settings. Enforcement action methods may be as simple as denying access to a file based on the application of file permissions (access restriction). Log items may consist of lists of actions blocked by access restrictions or changes identified after the fact.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. Run the command: ls /core-service=management/access=audit/logger=audit-log If "enabled" = false, this is a finding.

## Group: SRG-APP-000381-AS-000089

**Group ID:** `V-213544`

### Rule: Production JBoss servers must log when successful application deployments occur.

**Rule ID:** `SV-213544r981687_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without logging the enforcement of access restrictions against changes to the application server configuration, it will be difficult to identify attempted attacks, and a log trail will not be available for forensic investigation for after-the-fact actions. Configuration changes may occur to any of the modules within the application server through the management interface, but logging of actions to the configuration of a module outside the application server is not logged. Enforcement actions are the methods or mechanisms used to prevent unauthorized changes to configuration settings. Enforcement action methods may be as simple as denying access to a file based on the application of file permissions (access restriction). Log items may consist of lists of actions blocked by access restrictions or changes identified after the fact.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. Run the command: ls /core-service=management/access=audit/logger=audit-log If "enabled" = false, this is a finding.

## Group: SRG-APP-000427-AS-000264

**Group ID:** `V-213545`

### Rule: JBoss must be configured to use DoD PKI-established certificate authorities for verification of the establishment of protected sessions.

**Rule ID:** `SV-213545r961596_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DoD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DoD-approved CA, trust of this CA has not been established. The DoD will only accept PKI certificates obtained from a DoD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of SSL/TLS certificates. The application server must only allow the use of DoD PKI-established certificate authorities for verification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Locate the cacerts file for the JVM. This can be done using the appropriate find command for the OS and change to the directory where the cacerts file is located. To view the certificates stored within this file, execute the java command "keytool -list -v -keystore ./cacerts". Verify that the Certificate Authority (CA) for each certificate is DoD-approved. If any certificates have a CA that are not DoD-approved, this is a finding.

## Group: SRG-APP-000435-AS-000069

**Group ID:** `V-213546`

### Rule: The JBoss server, when hosting mission critical applications, must be in a high-availability (HA) cluster.

**Rule ID:** `SV-213546r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A MAC I system is a system that handles data vital to the organization's operational readiness or effectiveness of deployed or contingency forces. A MAC I system must maintain the highest level of integrity and availability. By HA clustering the application server, the hosted application and data are given a platform that is load-balanced and provides high availability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the system admin and determine if the applications hosted on the application server are mission critical and require load balancing (LB) or high availability (HA). If the applications do not require LB or HA, this requirement is NA. If the documentation shows the LB or HA services are being provided by another system other than the application server, this requirement is NA. If applications require LB or HA, request documentation from the system admin that identifies what type of LB or HA configuration has been implemented on the application server. Ask the system admin to identify the components that require protection. Some options are included here as an example. Bear in mind the examples provided are not complete and absolute and are only provided as examples. The components being made redundant or HA by the application server will vary based upon application availability requirements. Examples are: Instances of the Application Server Web Applications Stateful, stateless and entity Enterprise Java Beans (EJBs) Single Sign On (SSO) mechanisms Distributed Cache HTTP sessions JMS and Message Services. If the hosted application requirements specify LB or HA and the JBoss server has not been configured to offer HA or LB, this is a finding.

## Group: SRG-APP-000439-AS-000155

**Group ID:** `V-213547`

### Rule: JBoss must be configured to use an approved TLS version.

**Rule ID:** `SV-213547r961632_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that the application server take measures to employ some form of cryptographic mechanism in order to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS). JBoss relies on the underlying SSL implementation running on the OS. This can be either Java based or OpenSSL. The SSL protocol setting determines which SSL protocol is used. SSL has known security vulnerabilities, so TLS should be used instead. If data is transmitted unencrypted, the data then becomes vulnerable to disclosure. The disclosure may reveal user identifier/password combinations, website code revealing business logic, or other user personal information. FIPS 140-2 approved TLS versions include TLS V1.2 or greater. TLS must be enabled, and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 specifies the preferred configurations for government systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. Validate that the TLS protocol is used for HTTPS connections. Run the command: "ls /subsystem=web/connector=https/ssl=configuration" If a TLS V1.2 or higher protocol is not returned, this is a finding.

## Group: SRG-APP-000440-AS-000167

**Group ID:** `V-213548`

### Rule: JBoss must be configured to use an approved cryptographic algorithm in conjunction with TLS.

**Rule ID:** `SV-213548r961635_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing the disclosure or modification of transmitted information requires that application servers take measures to employ approved cryptography in order to protect the information during transmission over the network. This is usually achieved through the use of Transport Layer Security (TLS), SSL VPN, or IPSec tunnel. If data in transit is unencrypted, it is vulnerable to disclosure and modification. If approved cryptographic algorithms are not used, encryption strength cannot be assured. FIPS 140-2 approved TLS versions include TLS V1.2 or greater. TLS must be enabled, and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 specifies the preferred configurations for government systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. Validate that the TLS protocol is used for HTTPS connections. Run the command: "ls /subsystem=web/connector=https/ssl=configuration" Review the cipher suites. The following suites are acceptable as per NIST 800-52r1 section 3.3.1 - Cipher Suites. Refer to the NIST document for a complete list of acceptable cipher suites. The source NIST document and approved encryption algorithms/cipher suites are subject to change and should be referenced. AES_128_CBC AES_256_CBC AES_128_GCM AES_128_CCM AES_256_CCM If the cipher suites utilized by the TLS server are not approved by NIST as per 800-52r1, this is a finding.

## Group: SRG-APP-000456-AS-000266

**Group ID:** `V-213549`

### Rule: Production JBoss servers must be supported by the vendor.

**Rule ID:** `SV-213549r961683_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The JBoss product is available as Open Source; however, the Red Hat vendor provides updates, patches and support for the JBoss product. It is imperative that patches and updates be applied to JBoss in a timely manner as many attacks against JBoss focus on unpatched systems. It is critical that support be obtained and made available.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the system admin and have them either show documented proof of current support, or have them demonstrate their ability to access the Red Hat Enterprise Support portal. Verify Red Hat support includes coverage for the JBoss product. If there is no current and active support from the vendor, this is a finding.

## Group: SRG-APP-000456-AS-000266

**Group ID:** `V-213550`

### Rule: The JRE installed on the JBoss server must be kept up to date.

**Rule ID:** `SV-213550r961683_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The JBoss product is available as Open Source; however, the Red Hat vendor provides updates, patches and support for the JBoss product. It is imperative that patches and updates be applied to JBoss in a timely manner as many attacks against JBoss focus on unpatched systems. It is critical that support be obtained and made available.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the system admin and obtain details on their patch management processes as it relates to the OS and the Application Server. If there is no active, documented patch management process in use for these components, this is a finding.

## Group: SRG-APP-000495-AS-000220

**Group ID:** `V-213551`

### Rule: JBoss must be configured to generate log records when successful/unsuccessful attempts to modify privileges occur.

**Rule ID:** `SV-213551r961800_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changing privileges of a subject/object may cause a subject/object to gain or lose capabilities. When successful/unsuccessful changes are made, the event needs to be logged. By logging the event, the modification or attempted modification can be investigated to determine if it was performed inadvertently or maliciously.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script to start the Command Line Interface (CLI). Connect to the server and authenticate. Run the command: For a Managed Domain configuration: "ls host=master/server=<SERVERNAME>/core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" For a Standalone configuration: "ls /core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" If "enabled" = false, this is a finding.

## Group: SRG-APP-000499-AS-000224

**Group ID:** `V-213552`

### Rule: JBoss must be configured to generate log records when successful/unsuccessful attempts to delete privileges occur.

**Rule ID:** `SV-213552r961812_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Deleting privileges of a subject/object may cause a subject/object to gain or lose capabilities. When successful and unsuccessful privilege deletions are made, the events need to be logged. By logging the event, the modification or attempted modification can be investigated to determine if it was performed inadvertently or maliciously.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script to start the Command Line Interface (CLI). Connect to the server and authenticate. Run the command: For a Managed Domain configuration: "ls host=master/server=<SERVERNAME>/core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" For a Standalone configuration: "ls /core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" If "enabled" = false, this is a finding.

## Group: SRG-APP-000503-AS-000228

**Group ID:** `V-213553`

### Rule: JBoss must be configured to generate log records when successful/unsuccessful logon attempts occur.

**Rule ID:** `SV-213553r961824_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Logging the access to the application server allows the system administrators to monitor user accounts. By logging successful/unsuccessful logons, the system administrator can determine if an account is compromised (e.g., frequent logons) or is in the process of being compromised (e.g., frequent failed logons) and can take actions to thwart the attack. Logging successful logons can also be used to determine accounts that are no longer in use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script to start the Command Line Interface (CLI). Connect to the server and authenticate. Run the command: For a Managed Domain configuration: "ls host=master/server=<SERVERNAME>/core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" For a Standalone configuration: "ls /core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" If "enabled" = false, this is a finding.

## Group: SRG-APP-000504-AS-000229

**Group ID:** `V-213554`

### Rule: JBoss must be configured to generate log records for privileged activities.

**Rule ID:** `SV-213554r961827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating log records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Privileged activities would occur through the management interface. This interface can be web-based or can be command line utilities. Whichever method is utilized by the application server, these activities must be logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script to start the Command Line Interface (CLI). Connect to the server and authenticate. Run the command: For a Managed Domain configuration: "ls host=master/server=<SERVERNAME>/core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" For a Standalone configuration: "ls /core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" If "enabled" = false, this is a finding.

## Group: SRG-APP-000505-AS-000230

**Group ID:** `V-213555`

### Rule: JBoss must be configured to generate log records that show starting and ending times for access to the application server management interface.

**Rule ID:** `SV-213555r961830_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Determining when a user has accessed the management interface is important to determine the timeline of events when a security incident occurs. Generating these events, especially if the management interface is accessed via a stateless protocol like HTTP, the log events will be generated when the user performs a logon (start) and when the user performs a logoff (end). Without these events, the user and later investigators cannot determine the sequence of events and therefore cannot determine what may have happened and by whom it may have been done. The generation of start and end times within log events allows the user to perform their due diligence in the event of a security breach.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script to start the Command Line Interface (CLI). Connect to the server and authenticate. Run the command: For a Managed Domain configuration: "ls host=master/server=<SERVERNAME>/core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" For a Standalone configuration: "ls /core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" If "enabled" = false, this is a finding.

## Group: SRG-APP-000506-AS-000231

**Group ID:** `V-213556`

### Rule: JBoss must be configured to generate log records when concurrent logons from different workstations occur to the application server management interface.

**Rule ID:** `SV-213556r961833_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Concurrent logons from different systems could possibly indicate a compromised account. When concurrent logons are made from different workstations to the management interface, a log record needs to be generated. This configuration setting provides forensic evidence that allows the system administrator to investigate access to the system and determine if the duplicate access was authorized or not. JBoss provides a multitude of different log formats, and API calls that log access to the system. If the default format and location is not used, the system admin must provide the configuration documentation and settings that show that this requirement is being met.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script to start the Command Line Interface (CLI). Connect to the server and authenticate. Run the command: For a Managed Domain configuration: "ls host=master/server=<SERVERNAME>/core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" For a Standalone configuration: "ls /core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" If "enabled" = false, this is a finding.

## Group: SRG-APP-000509-AS-000234

**Group ID:** `V-213557`

### Rule: JBoss must be configured to generate log records for all account creations, modifications, disabling, and termination events.

**Rule ID:** `SV-213557r961842_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The maintenance of user accounts is a key activity within the system to determine access and privileges. Through changes to accounts, an attacker can create an account for persistent access, modify an account to elevate privileges, or terminate/disable an account(s) to cause a DoS for user(s). To be able to track and investigate these actions, log records must be generated for any account modification functions. Application servers either provide a local user store, or they can integrate with enterprise user stores like LDAP. As such, the application server must be able to generate log records on account creation, modification, disabling, and termination.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script to start the Command Line Interface (CLI). Connect to the server and authenticate. Run the command: For a Managed Domain configuration: "ls host=master/server=<SERVERNAME>/core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" For a Standalone configuration: "ls /core-service=management/access=audit/logger=audit-log:write-attribute(name=enabled,value=true)" If "enabled" = false, this is a finding.

## Group: SRG-APP-000514-AS-000137

**Group ID:** `V-213558`

### Rule: The JBoss server must be configured to use DoD- or CNSS-approved PKI Class 3 or Class 4 certificates.

**Rule ID:** `SV-213558r961857_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Class 3 PKI certificates are used for servers and software signing rather than for identifying individuals. Class 4 certificates are used for business-to-business transactions. Utilizing unapproved certificates not issued or approved by DoD or CNS creates an integrity risk. The application server must utilize approved DoD or CNS Class 3 or Class 4 certificates for software signing and business-to-business transactions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the administrator to determine if JBoss is using certificates for PKI. If JBoss is not performing any PKI functions, this finding is NA. The CA certs are usually stored in a file called cacerts located in the directory $JAVA_HOME/lib/security. If the file is not in this location, use a search command to locate the file, or ask the administrator where the certificate store is located. Open a dos shell or terminal window and change to the location of the certificate store. To view the certificates within the certificate store, run the command (in this example, the keystore file is cacerts.): keytool -list -v -keystore ./cacerts Locate the "OU" field for each certificate within the keystore. The field should contain either "DoD" or "CNSS" as the Organizational Unit (OU). If the OU does not show that the certificates are DoD or CNSS supplied, this is a finding.

## Group: SRG-APP-000515-AS-000203

**Group ID:** `V-213559`

### Rule: JBoss servers must be configured to roll over and transfer logs on a minimum weekly basis.

**Rule ID:** `SV-213559r961860_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Protecting log data is important during a forensic investigation to ensure investigators can track and understand what may have occurred. Off-loading should be set up as a scheduled task but can be configured to be run manually, if other processes during the off-loading are manual. Off-loading is a common process in information systems with limited log storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the JBoss server is configured to use a Syslog Handler, this is not a finding. Log on to the OS of the JBoss server with OS permissions that allow access to JBoss. Using the relevant OS commands and syntax, cd to the <JBOSS_HOME>/bin/ folder. Run the jboss-cli script. Connect to the server and authenticate. Determine if there is a periodic rotating file handler. For a domain configuration run the following command; where <SERVERNAME> is a variable for all of the servers in the domain. Usually "server-one", "server-two", etc.: "ls /host=master/server=<SERVERNAME>/subsystem=logging/periodic-rotating-file-handler=" For a standalone configuration run the command: "ls /subsystem=logging/periodic-rotating-file-handler=" If the command does not return "FILE", this is a finding. Review the <JBOSS_HOME>/standalone/log folder for the existence of rotated logs, and ask the admin to demonstrate how rotated logs are packaged and transferred to another system on at least a weekly basis.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-217099`

### Rule: The JBoss server must be configured to bind the management interfaces to only management networks.

**Rule ID:** `SV-217099r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>JBoss provides multiple interfaces for accessing the system. By default, these are called "public" and "management". Allowing non-management traffic to access the JBoss management interface increases the chances of a security compromise. The JBoss server must be configured to bind the management interface to a network that controls access. This is usually a network that has been designated as a management network and has restricted access. Similarly, the public interface must be bound to a network that is not on the same segment as the management interface.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain documentation and network drawings from system admin that shows the network interfaces on the JBoss server and the networks they are configured for. If a management network is not used, you may substitute localhost/127.0.0.1 for management address. If localhost/127.0.0.1 is used for management interface, this is not a finding. From the JBoss server open the web-based admin console by pointing a browser to HTTP://127.0.0.1:9990. Log on to the management console with admin credentials. Select "RUNTIME". Expand STATUS by clicking on +. Expand PLATFORM by clicking on +. In the "Environment" tab, click the > arrow until you see the "jboss.bind.properties" and the "jboss.bind.properties.management" values. If the jboss.bind.properties and the jboss.bind.properties.management do not have different IP network addresses assigned, this is a finding. Review the network documentation. If access to the management IP address is not restricted, this is a finding.

