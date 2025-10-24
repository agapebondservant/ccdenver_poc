# STIG Benchmark: BlackBerry Enterprise Mobility Server 3.x Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000118-AS-000078

**Group ID:** `V-254706`

### Rule: The BlackBerry Enterprise Mobility Server (BEMS) must protect log information from any type of unauthorized read access.

**Rule ID:** `SV-254706r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to his or her advantage. Application servers contain admin interfaces that allow reading and manipulation of log records. Therefore, these interfaces should not allow unfettered access to those records. Application servers also write log data to log files stored on the OS, so appropriate file permissions must also be used to restrict access. Log information includes all information (e.g., log records, log settings, transaction logs, and log reports) needed to successfully log information system activity. Application servers must protect log information from unauthorized read access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify BEMS has been configured with the following administrator groups/roles, each group/role has required permissions, and at least one user has been assigned to each Administrator group/role: Server primary administrator, auditor. Procedure for Server Primary Administrator: 1. In the BEMS Dashboard, under "BEMS System Settings", click "BEMS Configuration". 2. Click "Dashboard Administrators". 3. Confirm the Administrator role for the primary server administrator has been assigned the dashboard role of Admin. 4. Verify in Active Directory (AD) at least one member has been assigned to the BEMS administrator group. (Note: Actual group name may be different.) Procedure for Auditor: 1. Verify in AD an auditor group has been set up with at least one member. 2. Browse to the log repository. 3. Right-click on the folder. 4. Select "Properties". 5. Select the "Security" tab. 6. Confirm the auditor security group is listed. If required administrator roles have not been set up on BEMS and at least one user has not been assigned to each role, this is a finding.

## Group: SRG-APP-000119-AS-000079

**Group ID:** `V-254707`

### Rule: The BlackBerry Enterprise Mobility Server (BEMS) must protect log information from unauthorized modification.

**Rule ID:** `SV-254707r879577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to log records provides information an attacker could potentially use to his or her advantage. Application servers contain admin interfaces that allow reading and manipulation of log records. Therefore, these interfaces should not allow unfettered access to those records. Application servers also write log data to log files stored on the OS, so appropriate file permissions must also be used to restrict access. Log information includes all information (e.g., log records, log settings, transaction logs and log reports) needed to successfully log information system activity. Application servers must protect log information from unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify BEMS has been configured with the following administrator groups/roles, each group/role has required permissions, and at least one user has been assigned to each Administrator group/role: Server primary administrator, auditor. Procedure for Server Primary Administrator: 1. In the BEMS Dashboard, under "BEMS System Settings", click "BEMS Configuration". 2. Click "Dashboard Administrators". 3. Confirm the Administrator role for the primary server administrator has been assigned the dashboard role of Admin. 4. Verify in Active Directory (AD) at least one member has been assigned to the BEMS administrator group. (Note: Actual group name may be different.) Procedure for Auditor: 1. Verify in AD an auditor group has been set up with at least one member. 2. Browse to the log repository. 3. Right-click on the folder. 4. Select "Properties". 5. Select the "Security" tab. 6. Confirm the auditor security group is listed. If required administrator roles have not been set up on BEMS and at least one user has not been assigned to each role, this is a finding.

## Group: SRG-APP-000120-AS-000080

**Group ID:** `V-254708`

### Rule: The BlackBerry Enterprise Mobility Server (BEMS) must protect log information from unauthorized deletion.

**Rule ID:** `SV-254708r879578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If log data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. Application servers contain admin interfaces that allow reading and manipulation of log records. Therefore, these interfaces should not allow for unfettered access to those records. Application servers also write log data to log files stored on the OS, so appropriate file permissions must also be used to restrict access. Log information includes all information (e.g., log records, log settings, transaction logs, and log reports) needed to successfully log information system activity. Application servers must protect log information from unauthorized deletion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify BEMS has been configured with the following administrator groups/roles, each group/role has required permissions, and at least one user has been assigned to each Administrator group/role: Server primary administrator, auditor. Procedure for Server Primary Administrator: 1. In the BEMS Dashboard, under "BEMS System Settings", click "BEMS Configuration". 2. Click "Dashboard Administrators". 3. Confirm the Administrator role for the primary server administrator has been assigned the dashboard role of Admin. 4. Verify in Active Directory (AD) at least one member has been assigned to the BEMS administrator group. (Note: Actual group name may be different.) Procedure for Auditor: 1. Verify in AD an auditor group has been set up with at least one member. 2. Browse to the log repository. 3. Right-click on the folder. 4. Select "Properties". 5. Select the "Security" tab. 6. Confirm the auditor security group is listed. If required administrator roles have not been set up on BEMS and at least one user has not been assigned to each role, this is a finding.

## Group: SRG-APP-000142-AS-000014

**Group ID:** `V-254709`

### Rule: The BlackBerry Enterprise Mobility Server (BEMS) platform must be protected by a DOD-approved firewall.

**Rule ID:** `SV-254709r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Most information systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Unneeded services and processes provide additional threat vectors and avenues of attack to the information system. BEMS is a critical component of the mobility architecture and must be configured to enable only those ports, protocols, and services (PPS) necessary to support functionality. All others must be expressly disabled or removed. A DOD-approved firewall implements the required network restrictions. A host-based firewall is appropriate where BEMS runs on a standalone platform. Network firewalls or other architectures may be preferred where BEMS runs in a cloud or virtualized solution.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BEMS configuration to determine whether a DOD-approved firewall is installed or if the platform operating system provides a firewall service that can restrict both inbound and outbound traffic by TCP/UDP port and IP address. If there is not a host-based firewall present on BEMS, this is a finding.

## Group: SRG-APP-000142-AS-000014

**Group ID:** `V-254710`

### Rule: The firewall protecting the BEMS must be configured to restrict all network traffic to and from all addresses with the exception of ports, protocols, and IP address ranges required to support BEMS functions.

**Rule ID:** `SV-254710r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Most information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations. Since BEMS is a critical component of the mobility architecture and must be configured to enable only those ports, protocols, and services (PPS) necessary to support functionality, all others must be expressly disabled or removed. A firewall installed on BEMS provides a protection mechanism to ensure unwanted service requests do not reach BEMS and outbound traffic is limited to only BEMS functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the BEMS administrator for a list of ports, protocols, and IP address ranges necessary to support BEMS functionality. A list can usually be found in the STIG Supplemental document or MDM product documentation. Compare the list against the configuration of the firewall and identify discrepancies. If the host-based firewall is not configured to support only those ports, protocols, and IP address ranges necessary for operation, this is a finding.

## Group: SRG-APP-000142-AS-000014

**Group ID:** `V-254711`

### Rule: The firewall protecting the BlackBerry Enterprise Mobility Server (BEMS) must be configured so that only DOD-approved ports, protocols, and services are enabled.

**Rule ID:** `SV-254711r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All ports, protocols, and services used on DOD networks must be approved and registered via the DOD PPSM process. This is to ensure that a risk assessment has been completed before a new port, protocol, or service is configured on a DOD network and has been approved by proper DOD authorities. Otherwise, the new port, protocol, or service could cause a vulnerability to the DOD network, which could be exploited by an adversary. See the DOD Ports, Protocols, Services Management (PPSM) Category Assurance Levels (CAL) list for DOD-approved ports, protocols, and services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the BEMS administrator for a list of ports, protocols, and services that have been configured on the host-based firewall of BEMS or generate the list by inspecting the firewall. Verify all allowed ports, protocols, and services are included on the DOD PPSM CAL list. If any allowed ports, protocols, and services on the MDM host-based firewall are not included on the DOD PPSM CAL list, this is a finding.

## Group: SRG-APP-000439-AS-000155

**Group ID:** `V-254712`

### Rule: The BlackBerry Enterprise Mobility Server (BEMS) must protect the confidentiality and integrity of transmitted information through the use of an approved TLS version.

**Rule ID:** `SV-254712r879810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that the application server take measures to employ some form of cryptographic mechanism to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS). Transmission of data can take place between the application server and a large number of devices/applications external to the application server. Examples are a web client used by a user, a backend database, a log server, or other application servers in an application server cluster. If data is transmitted unencrypted, the data then becomes vulnerable to disclosure. The disclosure may reveal user identifier/password combinations, website code revealing business logic, or other user personal information. FIPS 140-2 approved TLS versions include TLS V1.0 or greater. TLS must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 specifies the preferred configurations for government systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify BEMS has been configured to use only approved versions of TLS as follows: 1. Find the xml file "jetty.xml" located in the BEMS install directory on the BEMS host Windows server. 2. Find the "ExcludeProtocols" field. 3. Verify if unauthorized versions of SSL and TLS are listed in the "jetty.xml" file. <Set name="ExcludeProtocols"> <Array type="java.lang.String"> <Item>TLSv1</Item> <Item>TLSv1.1</Item> <Item>SSL</Item> <Item>SSLv2</Item> <Item>SSLv2Hello</Item> <Item>SSLv3</Item> If BEMS has not been configured to use only approved versions of TLS and the Exclude file does not include all of the above TLS and SSL protocols, this is a finding.

## Group: SRG-APP-000439-AS-000274

**Group ID:** `V-254713`

### Rule: The BlackBerry Enterprise Mobility Server (BEMS) must remove all export ciphers to protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-254713r879810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>During the initial setup of a Transport Layer Security (TLS) connection to the application server, the client sends a list of supported cipher suites in order of preference. The application server will reply with the cipher suite it will use for communication from the client list. If an attacker can intercept the submission of cipher suites to the application server and place, as the preferred cipher suite, a weak export suite, the encryption used for the session becomes easy for the attacker to break, often within minutes to hours.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify BEMS has been configured to remove all export ciphers (automatically implemented when BEMS is in FIPS mode). Verify BEMS-03-014800 has been implemented. If BEMS has been configured to use export ciphers, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-254714`

### Rule: The BlackBerry Enterprise Mobility Server (BEMS) must be configured to have at least one user in the following Administrator roles: Server primary administrator, auditor.

**Rule ID:** `SV-254714r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Having several administrative roles for the BEMS supports separation of duties. This allows administrator-level privileges to be granted granularly, such as giving application management privileges to one group and security policy privileges to another group. This helps prevent administrators from intentionally or inadvertently altering other settings and configurations they may not understand or approve of, which can weaken overall security and increase the risk of compromise. - Server primary administrator: Responsible for server installation, initial configuration, and maintenance functions. Responsible for the setup and maintenance of security configuration administrator and auditor accounts. - Auditor: Responsible for reviewing and maintaining server and mobile device audit logs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify BEMS has been configured with the following administrator groups/roles, each group/role has required permissions, and at least one user has been assigned to each Administrator group/role: Server primary administrator, auditor. Procedure for Server Primary Administrator: 1. In the BEMS Dashboard, under "BEMS System Settings", click "BEMS Configuration". 2. Click "Dashboard Administrators". 3. Confirm the Administrator role for the primary server administrator has been assigned the dashboard role of Admin. 4. Verify in Active Directory (AD) at least one member has been assigned to the BEMS administrator group. (Note: Actual group name may be different.) Procedure for Auditor: 1. Verify in AD an auditor group has been set up with at least one member. 2. Browse to the log repository. 3. Right-click on the folder. 4. Select "Properties". 5. Select the "Security" tab. 6. Confirm the auditor security group is listed. If required administrator roles have not been set up on BEMS and at least one user has not been assigned to each role, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-254715`

### Rule: The BlackBerry Enterprise Mobility Server (BEMS) must be configured to use Windows Authentication for the database connection.

**Rule ID:** `SV-254715r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthorized access, organizational users must be identified and authenticated. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors, guest researchers, individuals from allied nations). Users (and any processes acting on behalf of users) are uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization, which outlines specific user actions that can be performed on the information system without identification or authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify BEMS is configured for Windows Authentication for the database connection as follows: In the Database Information dialog box, verify "Windows Authentication" is selected. If "Windows Authentication" is not selected for the BEMS database connection, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-254716`

### Rule: The BlackBerry Enterprise Mobility Server (BEMS) must be configured to use HTTPS.

**Rule ID:** `SV-254716r879887_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that applications take measures to employ some form of cryptographic mechanism to protect the information during transmission to web applications. This is usually achieved through the use of HTTPS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify BEMS has been configured to use HTTPS as follows: 1. In the BEMS Dashboard, under "BEMS System Settings", click "BEMS Configuration". 2. Click "BlackBerry Dynamics". 3. In the Protocol drop-down list, verify "HTTPS" is selected. If HTTPS is not configured on BEMS, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-254717`

### Rule: The BlackBerry Enterprise Mobility Server (BEMS) must be configured to use DOD certificates for SSL.

**Rule ID:** `SV-254717r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DOD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DOD-approved CA, trust of this CA has not been established.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify a DOD SSL certificate has been installed on BEMS as follows: 1. Open the browser. 2. Browse to the BEMS dashboard. 3. Select SSL certificate and view the certificate. 4. Verify the certificate is a DOD certificate (has the DOD CA listed in the certificate). If the SSL certificate installed on BEMS is not a DOD certificate, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-254718`

### Rule: The BlackBerry Enterprise Mobility Server (BEMS) must be configured with an inactivity timeout of 15 minutes or less.

**Rule ID:** `SV-254718r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their application session prior to vacating the vicinity, applications need to be able to identify when a user's application session has idled and take action to initiate the session lock.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BEMS inactivity timeout is set to 15 minutes or less: 1. Find the xml file "jetty.xml" located in the BEMS install directory on the BEMS host Windows server. 2. Find the "maxIdleTime" field. (Note: "idleTimeout" may be the field, depending on the version of BEMS.) 3. Verify it is set to 900 or less (seconds). (Note: time may be in milliseconds, depending on the version of BEMS. In this case, the value would be 900000.) If the BEMS inactivity timeout is not set to 15 minutes (900 seconds) or less, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-254719`

### Rule: If the Mail service (Push Notifications support for BlackBerry Work) is installed on the BlackBerry Enterprise Mobility Server (BEMS), it must be configured to use Windows Authentication for the database connection.

**Rule ID:** `SV-254719r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthorized access, organizational users must be identified and authenticated. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors, guest researchers, individuals from allied nations). Users (and any processes acting on behalf of users) are uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization, which outlines specific user actions that can be performed on the information system without identification or authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable if the Mail service (Push Notifications support for BlackBerry Work) is not enabled on BEMS. Verify the mail service in BEMS is configured for Windows Authentication for the database connection as follows: 1. In the BEMS Dashboard, under "BlackBerry Services Configuration", click "Mail". 2. Click "Database". 3. In the "Server" field, type the Microsoft SQL Server host name and instance. 4. In the "Database" field, type the database name. 5. In the Windows Authentication drop-down list, verify "Windows Authentication" is selected. If "Windows Authentication" is not selected for the mail service database connection, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-254720`

### Rule: If the Mail service (Push Notifications support for BlackBerry Work) is installed on the BlackBerry Enterprise Mobility Server (BEMS), it must be configured to use Windows Integrated Authentication for the Exchange connection.

**Rule ID:** `SV-254720r916412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthorized access, organizational users must be identified and authenticated. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors, guest researchers, individuals from allied nations). Users (and any processes acting on behalf of users) are uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization, which outlines specific user actions that can be performed on the information system without identification or authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable if the Mail service (Push Notifications support for BlackBerry Work) is not enabled on BEMS. Verify Windows Integrated Authentication for the Exchange connection for the Mail service has been set up in BEMS as follows: *On-Prem email server used at site: 1. In the BEMS Dashboard, under "BlackBerry Services Configuration", click "Mail". 2. Click "Microsoft Exchange". 3. Under "Enter Service Account Details", verify "Use Windows Integrated Authentication" has been selected. *O-365 email server used at site: 1. If credential authentication is used by the site: a. In the BEMS Dashboard, under "BlackBerry Services Configuration", click "Mail". b. Click "Microsoft Exchange". c. In the "Select Authentication type" section, verify "Credential" authentication type is listed. 2. If client certificate is used at site: a. In the BEMS Dashboard, under "BlackBerry Services Configuration", click "Mail". b. Click "Microsoft Exchange". c. In the "Select Authentication type" section, verify "Client Certificate" authentication type is listed. If Windows Integrated Authentication for the Exchange connection for the Mail service has not been set up in BEMS, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-254721`

### Rule: If the Mail service (Push Notifications support for BlackBerry Work) is installed on the BlackBerry Enterprise Mobility Server (BEMS), it must be configured to Enable SSL LDAP when using LDAP Lookup for users.

**Rule ID:** `SV-254721r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that applications take measures to employ some form of cryptographic mechanism to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS) or SSL.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable if the Mail service (Push Notifications support for BlackBerry Work) is not enabled on BEMS. Verify Enable SSL LDAP for LDAP Lookup for users for the Mail service is configured in BEMS as follows: 1. In the BEMS Dashboard, under "BlackBerry Services Configuration", click "Mail". 2. Click "User Directory Lookup". 3. If the "Enable LDAP Lookup" has been selected, verify the "Enable SSL LDAP" check box is also selected. When LDAP Lookup for user has been configured on BEMS, if Enable SSL LDAP is not configured, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-254722`

### Rule: If the Mail service (Push Notifications support for BlackBerry Work) is installed on the BlackBerry Enterprise Mobility Server (BEMS), it must be configured to Enable SSL LDAP for certificate directory lookup.

**Rule ID:** `SV-254722r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that applications take measures to employ some form of cryptographic mechanism to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS) or SSL.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable if the Mail service (Push Notifications support for BlackBerry Work) is not enabled on BEMS. Verify Enable SSL LDAP for LDAP Lookup for certificates for the Mail service is configured in BEMS as follows: 1. In the BEMS Dashboard, under "BlackBerry Services Configuration", click "Mail", and then click "Certificate Directory Lookup". 2. If the "Enable LDAP Lookup" has been selected, verify the "Enable SSL LDAP" check box is also selected. When LDAP Lookup for certificates has been configured on BEMS, if Enable SSL LDAP is not configured, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-254723`

### Rule: If the BlackBerry Connect service is installed on the BlackBerry Enterprise Mobility Server (BEMS), it must be configured to use Windows Authentication for the database connection.

**Rule ID:** `SV-254723r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthorized access, organizational users must be identified and authenticated. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors, guest researchers, individuals from allied nations). Users (and any processes acting on behalf of users) are uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization, which outlines specific user actions that can be performed on the information system without identification or authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable if the BlackBerry Connect service is not enabled on BEMS. Verify the BlackBerry Connect service in BEMS is configured for Windows Authentication for the database connection as follows: 1. In the BEMS Dashboard, under "BlackBerry Services Configuration", click "Connect". 2. Click "Database". 3. In the "Database" field, type the database name. 4. In the "Windows Authentication" drop-down list, verify "Windows Authentication" is selected. If "Windows Authentication" is not selected for the BlackBerry Connect database connection, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-254724`

### Rule: If the BlackBerry Connect service is installed on the BlackBerry Enterprise Mobility Server (BEMS), it must be configured to enable SSL support for BlackBerry Proxy and use only DOD approved certificates.

**Rule ID:** `SV-254724r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that applications take measures to employ some form of cryptographic mechanism to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS) or SSL. Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DOD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DOD-approved CA, trust of this CA has not been established.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable if the BlackBerry Connect service is not enabled on BEMS. Verify SSL is enabled for the BlackBerry Connect service and a DOD certificate is used as follows: 1. Browse to FQDN of the BEMS Connect server(s) on port 8082. 2. Click on the SSL certificate to verify it has been issued by the DOD CA. 3. Repeat steps 1 and 2 for each BEMS server that has the Connect service added to it. If SSL is not enabled for BlackBerry Connect and if the SSL certificate is not a DOD CA issued certificate, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-254725`

### Rule: If the BlackBerry Docs service is installed on the BlackBerry Enterprise Mobility Server (BEMS), it must be configured to use Windows Authentication for the database connection.

**Rule ID:** `SV-254725r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthorized access, organizational users must be identified and authenticated. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors, guest researchers, individuals from allied nations). Users (and any processes acting on behalf of users) are uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization, which outlines specific user actions that can be performed on the information system without identification or authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable if the BlackBerry Docs service is not enabled on BEMS. Verify the BlackBerry Docs service in BEMS is configured for Windows Authentication for the database connection as follows: 1. In the BEMS Dashboard, under "BlackBerry Services Configuration", click "Docs". 2. Click "Database". 3. In the "Database" field, type the database name. 4. In the Windows Authentication drop-down list, verify "Windows Authentication" is selected. If "Windows Authentication" is not selected for the BlackBerry Docs database connection, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-254726`

### Rule: If the BlackBerry Docs service is installed on the BlackBerry Enterprise Mobility Server (BEMS), it must be configured to use NTLM authentication.

**Rule ID:** `SV-254726r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthorized access, organizational users must be identified and authenticated. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors, guest researchers, individuals from allied nations). Users (and any processes acting on behalf of users) are uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization, which outlines specific user actions that can be performed on the information system without identification or authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable if the BlackBerry Docs service is not enabled on BEMS. Verify NTLM authentication is enabled for the BlackBerry Docs service as follows: 1. In the BEMS Dashboard, under "Good Services Configuration", click "Docs". 2. Click "Web Proxy". 3. Select "Use Web Proxy". 4. In the Proxy Server Authentication Type drop-down list, verify "NTLM authentication" is selected. If NTLM authentication is not enabled for the BlackBerry Docs service, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-254727`

### Rule: If the BlackBerry Docs service is installed on the BlackBerry Enterprise Mobility Server (BEMS), it must be configured to use SSL for LDAP lookup to connect to the Office Web App Server (e.g., SharePoint).

**Rule ID:** `SV-254727r879887_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that applications take measures to employ some form of cryptographic mechanism to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS) or SSL.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable if the BlackBerry Docs service is not enabled on BEMS. Verify the BlackBerry Docs service is configured to use SSL for LDAP Lookup to connect to the Office Web App Server (e.g., SharePoint) as follows: 1. In the BEMS Dashboard, under "BlackBerry Services Configuration", click "Docs". 2. Click "Settings". 3. Verify "Use SSL for LDAP" is selected. If SSL for LDAP is not enabled for the BlackBerry Docs service, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-254728`

### Rule: If the BlackBerry Docs service is installed on the BlackBerry Enterprise Mobility Server (BEMS), it must be configured to enable audit logs.

**Rule ID:** `SV-254728r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Logging must be used to track system activity, assist in diagnosing system issues, and provide evidence needed for forensic investigations post security incident.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable if the BlackBerry Docs service is not enabled on BEMS. Verify audit logging is enabled for the BlackBerry Docs service as follows: 1. In the BEMS Dashboard, under "BlackBerry Services Configuration", click "Docs". 2. Click "Audit". 3. On the "Audit Settings" tab, verify "Enable Audit Logs" is selected. If audit logging is not enabled for the BlackBerry Docs service, this is a finding.

## Group: SRG-APP-000179-AS-000129

**Group ID:** `V-254729`

### Rule: The BlackBerry Enterprise Mobility Server (BEMS) server must be configured to enable FIPS mode.

**Rule ID:** `SV-254729r879616_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified and cannot be relied upon to provide confidentiality or integrity, and DOD data may be compromised due to weak algorithms. In addition, the application must be configured to use the FIPS version of all cryptographic algorithms and modules.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify FIPS Mode is enabled for BEMS. 1. Under BEMS Systems Settings select "BEMS Configuration". 2. Select "FIPS Mode". 3. Confirm "Enable FIPS Mode for Cluster" has been selected. If "Enable FIPS Mode for Cluster" is not selected, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-254730`

### Rule: If the BlackBerry Connect service is installed on the BlackBerry Enterprise Mobility Server (BEMS), it must be configured to enable the Web Proxy.

**Rule ID:** `SV-254730r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The web proxy provides a secure gateway for the BlackBerry Connect service so that BEMS can securely connect to the internet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable if the Connect service is not enabled on BEMS. Verify that Web Proxy Configuration has been configured. 1. Under "BlackBerry Services Configuration" select "Connect". 2. Select "Web Proxy". 3. Confirm "Use Web Proxy" has been checked. If "Use Web Proxy" has not been selected, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-254731`

### Rule: If the BlackBerry Presence service is installed on the BlackBerry Enterprise Mobility Server (BEMS), it must be configured with the whitelisting control to limit presence subscriptions to only single domain/tenant.

**Rule ID:** `SV-254731r879887_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Whitelisting in Presence subscriptions is used to control which internal and federated environments can be subscribed to. Presence subscriptions should be limited to only DOD environments to control who has access to presence information on DOD users. This is an operational security (OPSEC) issue.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable if the Presence service is not enabled on BEMS. Verify that Domain whitelisting has been configured. 1. Under the BlackBerry Service Configuration select "Presence". 2. Select "Settings". 3. Confirm "Enable domain whitelisting" has been checked. If "Enable domain whitelisting" is not selected, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-254732`

### Rule: If the BlackBerry Docs service is installed on the BlackBerry Enterprise Mobility Server (BEMS), it must be configured to enable the proxy server authentication type (if a proxy is used).

**Rule ID:** `SV-254732r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The web proxy provides a secure gateway for the BlackBerry Docs service so that BEMS can securely connect to enterprise servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable if the Docs service for BEMS is not enabled. Verify that the authentication type is set to NTLM if a web proxy is used. 1. Under the "BlackBerry Services Configuration", select "Docs". 2. Under the "Proxy Server Authentication Type", ensure "NTLM" is Selected. If "NTLM" is not selected, this is a finding.

