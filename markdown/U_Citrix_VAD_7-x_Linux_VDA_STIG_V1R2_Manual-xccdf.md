# STIG Benchmark: Citrix Virtual Apps and Desktop 7.x Linux Virtual Delivery Agent Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001

**Group ID:** `V-234255`

### Rule: The application must limit the number of concurrent sessions to three.

**Rule ID:** `SV-234255r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application management includes the ability to control the number of users and user sessions that utilize an application. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to DoS attacks. This requirement may be met via the application or by utilizing information system session control provided by a web server with specialized session management capabilities. If it has been specified that this requirement will be handled by the application, the capability to limit the maximum number of concurrent single user sessions must be designed and built into the application. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open Citrix Studio, select "Policy Panel", check for Computer Policies. Maximum number of sessions (MaximumNumberOfSessions) policy is "ENABLED" and explicitly applied to Linux Desktop/Application Delivery Groups. If Maximum Number of Sessions policy is "DISABLED" or limit not set to "3", this is a finding.

## Group: SRG-APP-000003

**Group ID:** `V-234256`

### Rule: The application must initiate a session lock after a 15-minute period of inactivity.

**Rule ID:** `SV-234256r960741_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their application session prior to vacating the vicinity, applications need to be able to identify when a user's application session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. This is typically at the operating system-level and results in a system lock, but may be at the application-level where the application interface window is secured instead. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
All timer values are defined in the registration table. Retrieve current value using the following command: /opt/Citrix/VDA/bin/ctxreg, /opt/Citrix/VDA/bin/ctxreg dump |grep MaxIdleTime If MaxIdleTime is not set to "15 minutes" or less, this is a finding.

## Group: SRG-APP-000014

**Group ID:** `V-234257`

### Rule: Citrix Linux Virtual Delivery Agent must implement DoD-approved encryption.

**Rule ID:** `SV-234257r960759_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection thereby providing a degree of confidentiality. The encryption strength of mechanism is selected based on the security categorization of the information. Satisfies: SRG-APP-000014, SRG-APP-000015, SRG-APP-000039, SRG-APP-000219, SRG-APP-000439, SRG-APP-000440, SRG-APP-000441, SRG-APP-000442</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Delivery Controller, ensure the SSL encryption has been enabled for the delivery group (HdxSslEnabled:True) and the Delivery Controller uses FQDN of Linux VDA to contact target Linux VDA (DnsResolutionEnabled:True). Execute the following commands in a PowerShell window on the Delivery Controller: # Asnp citrix.* # Get-BrokerAccessPolicyRule –DesktopGroupName ‘<GROUPNAME>’ | format-list HdxSslEnabled Where <GROUPNAME> is the target Delivery Group name. On Linux VDA, check the following: Check if SSL listener is up and running; run following command: # netstat -lptn|grep ctxhdx to see that the ctxhdx process is listening on an SSL port (443, by default). If, on the Delivery Controller, HdxSslEnabled is not set to "true", this is a finding. If, on the Delivery Controller, DnsResolutionEnabled is not set to "true", this is a finding. If, on the Linux VDS, the ctxhdx process is not listening on an SSL port (443 by default, or other approved port), this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-234258`

### Rule: The application must be configured to disable non-essential capabilities.

**Rule ID:** `SV-234258r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Applications are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include, but are not limited to, advertising software or browser plug-ins not related to requirements or providing a wide array of functionality not required for every mission but cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command on a client to disable the CEIP: /opt/Citrix/VDA/bin/ctxreg update -k "HKEY_LOCAL_MACHINE\ SOFTWARE\Citrix\CEIP" -v "CEIPSwitch" -d "1" If CEIPSwitch is not set to "1", this is a finding. Run the following command on a client to disable Google Analytics: /opt/Citrix/VDA/bin/ctxreg update -k "HKEY_LOCAL_MACHINE\ SOFTWARE\Citrix\CEIP" -v "GASwitch" -d "1" If GASwitch is not set to "1", this is a finding.

## Group: SRG-APP-000142

**Group ID:** `V-234259`

### Rule: Citrix Linux Virtual Delivery Agent (LVDA) must be configured to prohibit or restrict the use of ports, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-234259r1043177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services; however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On Delivery Controllers, verify that only approved ports are used. 1. Open a command prompt. 2. Navigate to the Citrix install directory Program Files\Citrix\Broker\Service 3. Enter "BrokerService.exe /Show" to display the currently used ports. If an unapproved port is used, this is a finding.

## Group: SRG-APP-000427

**Group ID:** `V-234260`

### Rule: Citrix Linux Virtual Delivery Agent must only allow the use of DoD PKI established certificate authorities for verification of the establishment of protected sessions.

**Rule ID:** `SV-234260r961596_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DoD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DoD-approved CA, trust of this CA has not been established. The DoD will only accept PKI certificates obtained from a DoD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of SSL/TLS certificates. This requirement focuses on communications protection for the application session rather than for the network packet. This requirement applies to applications that utilize communications sessions. This includes, but is not limited to, web-based applications and Service-Oriented Architectures (SOA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the correct server certificate issued by authorized certificate authority is installed on Linux VDA. Navigate to folder /root/myCert/myCA/certs/ and examine certificates. If the certificates are not issued by the DoD or approved CA, this is a finding.

## Group: SRG-APP-000456

**Group ID:** `V-275969`

### Rule: The version of Virtual Apps and Desktop Linux VDA running on the system must be a supported version.

**Rule ID:** `SV-275969r1115779_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications that are not part of that patch management solution. For example, many browsers provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may depend on the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Virtual Apps and Desktop Linux VDA 7.x is no longer supported by the vendor. If the system is running Virtual Apps and Desktop Linux VDA 7.x, this is a finding.

