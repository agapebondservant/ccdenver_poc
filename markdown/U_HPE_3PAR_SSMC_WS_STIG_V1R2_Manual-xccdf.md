# STIG Benchmark: HPE 3PAR SSMC Web Server Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000179-WSR-000111

**Group ID:** `V-255251`

### Rule: The SSMC web server must use cryptographic modules that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance for such authentication.

**Rule ID:** `SV-255251r879616_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified and cannot be relied upon to provide confidentiality or integrity, and DOD data may be compromised due to weak algorithms. FIPS 140-2 is the current standard for validating cryptographic modules and NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. The web server must provide FIPS-compliant encryption modules when authenticating users and processes. Satisfies: SRG-APP-000179-WSR-000111, SRG-APP-000014-WSR-000006, SRG-APP-000015-WSR-000014, SRG-APP-000179-WSR-000110, SRG-APP-000224-WSR-000135, SRG-APP-000224-WSR-000136, SRG-APP-000224-WSR-000139, SRG-APP-000416-WSR-000118, SRG-APP-000439-WSR-000156, SRG-APP-000441-WSR-000181, SRG-APP-000442-WSR-000182</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC utilizes FIPS 140-2 approved mode of encryption for authenticating users by doing the following: 1. Log on to SSMC Administrator Console on web GUI as ssmcadmin. 2. Click the information icon on top right corner and verify "FIPS mode enabled" displays "true". 3. Log on to SSMC appliance as ssmcadmin via SSH, press "X" to escape to general bash shell from the TUI menu, and issue the following command: $ sudo /ssmc/bin/config_security.sh -o fips_mode -a status The output of the command must read "FIPS mode is enabled". If the observations do not indicate FIPS mode as enabled in both steps 1 and 2, this is a finding.

## Group: SRG-APP-000001-WSR-000001

**Group ID:** `V-255252`

### Rule: SSMC web server must limit the number of allowed simultaneous session requests.

**Rule ID:** `SV-255252r916426_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web server management includes the ability to control the number of users and user sessions that utilize a web server. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to several types of Denial of Service attacks. Although there is some latitude concerning the settings themselves, the settings should follow DoD-recommended values, but the settings should be configurable to allow for future DOD direction. While the DOD will specify recommended values, the values can be adjusted to accommodate the operational requirement of a given system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC limits the number of concurrent sessions by doing the following: 1. Log on to SSMC TUI via SSH as ssmcadmin. Press "X" to escape to general bash shell. 2. Execute the following commands: $ grep ^security.max.active.ui.sessions /opt/hpe/ssmc/ssmcbase/resources/ssmc.properties security.max.active.ui.sessions=10 $ grep ^security.max.active.ui.per.user.sessions /opt/hpe/ssmc/ssmcbase/resources/ssmc.properties security.max.active.ui.per.user.sessions=1 If the output of the above commands does not show the values for "security.max.active.ui.sessions" and "security.max.active.ui.per.user.sessions" properties with values set as "10" and "1" respectively, this is a finding.

## Group: SRG-APP-000014-WSR-000006

**Group ID:** `V-255253`

### Rule: SSMC web server must use encryption strength in accordance with the categorization of data hosted by the web server when remote connections are provided.

**Rule ID:** `SV-255253r879519_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The SSMC web server has several remote communications channels. Examples are user requests via http/https, communication to a backend database, or communication to authenticate users. The encryption used to communicate must match the data that is being retrieved or presented. Methods of communication are http for publicly displayed information, https to encrypt when user data is being transmitted, VPN tunneling, or other encryption methods to a database. Satisfies: SRG-APP-000014-WSR-000006, SRG-APP-000172-WSR-000104, SRG-APP-000439-WSR-000151, SRG-APP-000439-WSR-000156, SRG-APP-000441-WSR-000181, SRG-APP-000442-WSR-000182</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC uses encryption strength equal to the categorization of data hosted by doing the following: 1. Log on to SSH as ssmcadmin. Press "X" to escape to general bash shell. 2. Execute the following: $ grep ^ssmc.secure.tls.only /opt/hpe/ssmc/ssmcbase/resources/ssmc.properties ssmc.secure.tls.only = true If the command output does not read "ssmc.secure.tls.only = true", this is a finding.

## Group: SRG-APP-000015-WSR-000014

**Group ID:** `V-255254`

### Rule: SSMC web server must use cryptography to protect the integrity of remote sessions.

**Rule ID:** `SV-255254r879520_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Data exchanged between the user and the web server can range from static display data to credentials used to Log on to the hosted application. Even when data appears to be static, the nondisplayed logic in a web page may expose business logic or trusted system relationships. The integrity of all data being exchanged between the user and web server must always be trusted. To protect the integrity and trust, encryption methods should be used to protect the complete communication session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC encrypts log exports to a remote syslog server with the following command: $ sudo /ssmc/bin/config_security.sh -o remote_syslog_appliance -a status | grep tls ssmc.rsyslog.server.tls-enabled=1 If "ssmc.rsyslog.server.tls-enabled" does not equal "1", this is a finding.

## Group: SRG-APP-000016-WSR-000005

**Group ID:** `V-255255`

### Rule: SSMC web server must generate information to be used by external applications or entities to monitor and control remote access.

**Rule ID:** `SV-255255r879521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. By providing remote access information to an external monitoring system, the organization can monitor for cyber attacks and monitor compliance with remote access policies. The organization can also look at data organization wide and determine an attack or anomaly is occurring on the organization which might not be noticed if the data were kept local to the web server. Examples of external applications used to monitor or control access would be audit log monitoring systems, dynamic firewalls, or infrastructure monitoring systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC monitors remote access by doing the following: 1. Log on to SSH as ssmcadmin. Press "X" to escape to general bash shell. 2. Execute the following command to enable HTTP access logs: $ sudo /ssmc/bin/config_security.sh -o http_access_log -a status HTTP access logging is enabled. If the command output does not read "HTTP access logging is enabled", this is a finding.

## Group: SRG-APP-000016-WSR-000005

**Group ID:** `V-255256`

### Rule: SSMC web server must generate information to be used by external applications or entities to monitor and control remote access.

**Rule ID:** `SV-255256r879521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. By providing remote access information to an external monitoring system, the organization can monitor for cyber attacks and monitor compliance with remote access policies. The organization can also look at data organization wide and determine an attack or anomaly is occurring on the organization which might not be noticed if the data were kept local to the web server. Examples of external applications used to monitor or control access would be audit log monitoring systems, dynamic firewalls, or infrastructure monitoring systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC monitors remote access by doing the following: 1. Log on to SSH as ssmcadmin. Press "X" to escape to general bash shell. 2. Execute the following command to enable TCP access logs: $ sudo /ssmc/bin/config_security.sh -o tcp_access_log -a status TCP access logging is enabled If the command output does not read "TCP access logging is enabled", this is a finding.

## Group: SRG-APP-000016-WSR-000005

**Group ID:** `V-255257`

### Rule: SSMC web server must generate information to be used by external applications or entities to monitor and control remote access.

**Rule ID:** `SV-255257r879521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. By providing remote access information to an external monitoring system, the organization can monitor for cyber attacks and monitor compliance with remote access policies. The organization can also look at data organization wide and determine an attack or anomaly is occurring on the organization which might not be noticed if the data were kept local to the web server. Examples of external applications used to monitor or control access would be audit log monitoring systems, dynamic firewalls, or infrastructure monitoring systems. Satisfies: SRG-APP-000016-WSR-000005, SRG-APP-000358-WSR-000163, SRG-APP-000358-WSR-000063, SRG-APP-000125-WSR-000071</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC monitors remote access by enabling exports to a remote syslog server with the following command: $ sudo /ssmc/bin/config_security.sh -o remote_syslog_appliance -a status | sed 1q Remote syslog service status is OK If the output does not read "Remote syslog service status is OK", this is a finding.

## Group: SRG-APP-000142-WSR-000089

**Group ID:** `V-255258`

### Rule: The SSMC web server must be configured to use a specified IP address and port.

**Rule ID:** `SV-255258r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The web server must be configured to listen on a specified IP address and port. Without specifying an IP address and port for the web server to utilize, the web server will listen on all IP addresses available to the hosting server. If the web server has multiple IP addresses, i.e., a management IP address, the web server will also accept connections on the management IP address. Accessing the hosted application through an IP address normally used for nonapplication functions opens the possibility of user access to resources, utilities, files, ports, and protocols that are protected on the desired application IP address.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC web server is configured to listen on a specific network IP address, by doing the following: 1. Log on to ssmc appliance as ssmcadmin. Press "X" to escape to general bash shell. 2. Execute the command: $ sudo /ssmc/bin/config_security.sh -o webserver_service_network -a status Webserver service is listening on <ip_address> If the command output does not display a specific IP address assigned to the SSMC host but reads "default IP address", this is a finding.

## Group: SRG-APP-000175-WSR-000095

**Group ID:** `V-255259`

### Rule: The SSMC web server must perform RFC 5280-compliant certification path validation.

**Rule ID:** `SV-255259r916429_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify SSMC always validates PKI certificates of all remote hosts that it connects to, in accordance with RFC 5280, do the following: 1. Log on to ssmc appliance as ssmcadmin and escape to general bash shell. 2. Execute the following command: $ grep ^ssmc.tls.trustManager.enabled /opt/hpe/ssmc/ssmcbase/resources/ssmc.properties ssmc.tls.trustManager.enabled=true If the command output does not show the property ssmc.tls.trustManager.enabled as set to "true", this is a finding.

## Group: SRG-APP-000295-WSR-000012

**Group ID:** `V-255260`

### Rule: SSMC web server must set an absolute timeout for sessions.

**Rule ID:** `SV-255260r879673_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Leaving sessions open indefinitely is a major security risk. An attacker can easily use an already authenticated session to access the hosted application as the previously authenticated user. By closing sessions after an absolute period of time, the user is forced to re-authenticate guaranteeing the session is still in use. Enabling an absolute timeout for sessions closes sessions that are still active. Examples would be a runaway process accessing the web server or an attacker using a hijacked session to slowly probe the web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC is configured to close web sessions after an absolute period of time by doing the following: 1. Log on to SSMC appliance as ssmcadmin. Press "X" to escape to general bash shell. 2. Execute the following command: $ grep ^server.absolute.session.timeout /opt/hpe/ssmc/ssmcbase/resources/ssmc.properties server.absolute.session.timeout=60 If the command output does not read "server.absolute.session.timeout=60", this is a finding.

## Group: SRG-APP-000295-WSR-000134

**Group ID:** `V-255261`

### Rule: SSMC web server must set an inactive timeout for sessions.

**Rule ID:** `SV-255261r879673_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Leaving sessions open indefinitely is a major security risk. An attacker can easily use an already authenticated session to access the hosted application as the previously authenticated user. By closing sessions after a set period of inactivity, the web server can make certain that those sessions that are not closed through the user logging out of an application are eventually closed. Acceptable values are 5 minutes for high-value applications, 10 minutes for medium-value applications, and 20 minutes for low-value applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that idle session timeout is set by doing the following: 1. Log on to SSMC administrator console as ssmcadmin. 2. Navigate to Actions >> Preferences. 3. Locate Session timeout property and check if it is set to 10 minutes. If the value is not set to 10 minutes, this is a finding.

## Group: SRG-APP-000295-WSR-000134

**Group ID:** `V-255262`

### Rule: SSMC web server must set an inactive timeout for shell sessions.

**Rule ID:** `SV-255262r879673_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Leaving sessions open indefinitely is a major security risk. An attacker can easily use an already authenticated session to access the hosted application as the previously authenticated user. By closing sessions after a set period of inactivity, the web server can make certain that those sessions that are not closed through the user logging out of an application are eventually closed. Acceptable values are 5 minutes for high-value applications, 10 minutes for medium-value applications, and 20 minutes for low-value applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC web server is configured to close inactive sessions after 10 minutes by doing the following: 1. Log on to the SSMC appliance as ssmcadmin. Press "X" to escape to general bash shell. 2. Execute the command: $ sudo /ssmc/bin/config_security.sh -o shell_session_idle_timeout -a status Shell session idle timeout is configured to 600 seconds If the shell session idle timeout status does not read as "configured to 600 seconds", this is a finding.

## Group: SRG-APP-000315-WSR-000004

**Group ID:** `V-255263`

### Rule: SSMC web server must restrict connections from nonsecure zones.

**Rule ID:** `SV-255263r879692_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access to the web server is any access that communicates through an external, non-organization-controlled network. Remote access can be used to access hosted applications or to perform management functions. A web server can be accessed remotely and must be capable of restricting access from what the DOD defines as nonsecure zones. Nonsecure zones are defined as any IP, subnet, or region that is defined as a threat to the organization. The nonsecure zones must be defined for public web servers logically located in a DMZ, as well as private web servers with perimeter protection devices. By restricting access from nonsecure zones, through internal web server access list, the web server can stop or slow denial of service (DoS) attacks on the web server. Satisfies: SRG-APP-000315-WSR-000004, SRG-APP-000315-WSR-000003</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC is configured to block DOD-defined nonsecure zones using remote host access controls by doing the following: 1. Log on to SSMC appliance as ssmcadmin. Press "X" to escape to general bash shell. 2. Execute the following command: $ sudo /ssmc/bin/config_security.sh -o host_access -a status Host access is configured If the command output does not read "Host access is configured", this is a finding. 3. Review the inbound and outbound allow lists by executing the following command: $ grep ^ssmc.*.hosts.allow /ssmc/conf/security_config.properties ssmc.inbound.hosts.allow=<comma separated list or range of hosts> ssmc.outbound.hosts.allow=<comma separated list or range of hosts> If the inbound and outbound allow lists do not restrict connections from nonsecure zones, this is a finding.

## Group: SRG-APP-000176-WSR-000096

**Group ID:** `V-255264`

### Rule: SSMC web server application, libraries, and configuration files must only be accessible to privileged users.

**Rule ID:** `SV-255264r879613_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A web server can be modified through parameter modification, patch installation, upgrades to the web server or modules, and security parameter changes. With each of these changes, there is the potential for an adverse effect such as a DoS, web server instability, or hosted application instability. To limit changes to the web server and limit exposure to any adverse effects from the changes, files such as the web server application files, libraries, and configuration files must have permissions and ownership set properly to only allow privileged users access. Satisfies: SRG-APP-000176-WSR-000096, SRG-APP-000380-WSR-000072, SRG-APP-000211-WSR-000030</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC is configured to protect web server configuration files and logs from unauthorized access by executing command that enables stricter file permission: $ sudo /ssmc/bin/config_security.sh -o strict_file_permission -a status Strict file permission is set If the output does not read "Strict file permission is set", this is a finding.

## Group: SRG-APP-000516-WSR-000174

**Group ID:** `V-255265`

### Rule: SSMC web server must enable strict two-factor authentication for access to the webUI.

**Rule ID:** `SV-255265r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accounts secured with only a password are subject to multiple forms of attack, from brute force, to social engineering. By enforcing strict two-factor authentication, this reduces the risk of account compromise by requiring an additional factor that is not a password. Strict two-factor authentication is enabled by default. However, this is enforced only when two-factor authentication is configured and active. This blocks access to web administrator console for ssmcadmin as this is a local account authenticated using password credentials. To allow access to administrator console, disable this strict two-factor authentication setting.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC is configured to enforce strict two-factor authentication by doing the following: 1. Log on to SSMC appliance as ssmcadmin. 2. Navigate to the Advanced Features section of the TUI by pressing "9" then "2". If the Advanced Features sections displays "Enable strict two-factor authentication", this is a finding. 3. Escape to the bash shell by pressing "X". 4. Check the two-factor authentication property values in the /opt/hpe/ssmc/ssmcbase/resources/ssmc.properties file with the following command: $ grep ^security.twofactor /opt/hpe/ssmc/ssmcbase/resources/ssmc.properties security.twofactor.strict = true security.twofactor.enabled = true If the properties for "security.twofactor.strict" and "security.twofactor.enabled" are not set to "true" or are missing, this is a finding.

## Group: SRG-APP-000358-WSR-000063

**Group ID:** `V-255266`

### Rule: SSMC web server must not impede the ability to write specified log record content to an audit log server.

**Rule ID:** `SV-255266r879731_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Writing events to a centralized management audit system offers many benefits to the enterprise over having dispersed logs. Centralized management of audit records and logs provides for efficiency in maintenance and management of records, enterprise analysis of events, and backup and archiving of event records enterprise-wide. The web server and related components are required to be capable of writing logs to centralized audit log servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SSMC web process writes the web app and audit log files at the right location on the filesystem for log exports to work correctly: 1. Log on to SSMC appliance via SSH as ssmcadmin. Press "X" to escape to general bash shell. 2. Check the following property values in /opt/hpe/ssmc/ssmcbase/resources/log4j2.json file: a. File name for SSMCRollingFile Appender: $ grep "\"name\" : \"SSMCRollingFile\"" -A13 /opt/hpe/ssmc/ssmcbase/resources/log4j2.json | grep "fileName" "fileName" : "${logpath}/ssmc.log", If the output does not read ' "fileName" : "${logpath}/ssmc.log", ' , this is a finding. b. File name for LocalAuditRollingFile Appender: $ grep "\"name\" : \"LocalAuditRollingFile\"" -A13 /opt/hpe/ssmc/ssmcbase/resources/log4j2.json | grep "fileName" "fileName" : "${logpath}/audit.log", If the output does not read ' "fileName" : "${logpath}/audit.log", ' , this is a finding.

## Group: SRG-APP-000089-WSR-000047

**Group ID:** `V-255267`

### Rule: SSMC web server must generate, at a minimum, log records for system startup and shutdown, system access, and system authentication events.

**Rule ID:** `SV-255267r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log records can be generated from various components within the web server (e.g., httpd, plug-ins to external backends, etc.). From a web server perspective, certain specific web server functionalities may be logged as well. The web server must allow the definition of what events are to be logged. As conditions change, the number and types of events to be logged may change, and the web server must be able to facilitate these changes. The minimum list of logged events should be those pertaining to system startup and shutdown, system access, and system authentication events. If these events are not logged at a minimum, any type of forensic investigation would be missing pertinent information needed to replay what occurred. Satisfies: SRG-APP-000089-WSR-000047, SRG-APP-000093-WSR-000053, SRG-APP-000095-WSR-000056, SRG-APP-000096-WSR-000057, SRG-APP-000097-WSR-000058, SRG-APP-000098-WSR-000059, SRG-APP-000099-WSR-000061, SRG-APP-000092-WSR-000055</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC generates log records for system access by doing the following: 1. Log on to SSH as ssmcadmin. Press "X" to escape to general bash shell. 2. Execute the following commands: a. $ sudo /ssmc/bin/config_security.sh -o tcp_access_log -a status TCP access logging is enabled If the command output does not read "TCP access logging is enabled", this is a finding. b. $ sudo /ssmc/bin/config_security.sh -o http_access_log -f -a status HTTP access logging is enabled If the command output does not read "HTTP access logging is enabled", this is a finding.

## Group: SRG-APP-000092-WSR-000055

**Group ID:** `V-255268`

### Rule: SSMC web server must initiate session logging upon start up.

**Rule ID:** `SV-255268r879562_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An attacker can compromise a web server during the startup process. If logging is not initiated until all the web server processes are started, key information may be missed and not available during a forensic investigation. To assure all loggable events are captured, the web server must begin logging once the first web server process is initiated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC is configured to generate log records for system startup and shutdown, system access, and system authentication events. To do so, check if auditd facility (session_log) is enabled: 1. Log on as ssmcadmin to ssmc appliance via SSH. Press "X" to escape to general bash shell. 2. Execute the following command: $ sudo /ssmc/bin/config_security.sh -o session_log -a status Session log is enabled If the console output does not show the session log function as enabled, this is a finding.

## Group: SRG-APP-000108-WSR-000166

**Group ID:** `V-255269`

### Rule: SSMC web server must use a logging mechanism that is configured to alert the ISSO and SA in the event of a processing failure.

**Rule ID:** `SV-255269r879570_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reviewing log data allows an investigator to recreate the path of an attacker and to capture forensic data for later use. Log data is also essential to system administrators in their daily administrative duties on the hosted system or within the hosted applications. If the logging system begins to fail, events will not be recorded. Organizations must define logging failure events, at which time the application or the logging mechanism the application utilizes will provide a warning to the ISSO and SA at a minimum.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SSMC is configured to provide an alert to the ISSO and SA when log processing failures occur by doing the following: Execute status check on remote_syslog_appliance security control: $ sudo /ssmc/bin/config_security.sh -o remote_syslog_appliance -a status | grep smtp ssmc.rsyslog.smtp.alert=true ssmc.rsyslog.smtp.mailFrom=id@domain ssmc.rsyslog.smtp.recipient=["id1@domain","id2@domain"] ssmc.rsyslog.smtp.notify-interval=<failure_notify_interval> ssmc.rsyslog.smtp.server=<smtp_server_ip> ssmc.rsyslog.smtp.port=<smtp_port> If the "smtp.alert" is not equal to "true" and the remaining smtp configuration is not established per the site requirements, this is a finding.

