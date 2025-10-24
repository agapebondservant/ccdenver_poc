# STIG Benchmark: VMware vRealize Automation 7.x vIDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000016-AS-000013

**Group ID:** `V-240969`

### Rule: vIDM must be configured to log activity to the horizon.log file.

**Rule ID:** `SV-240969r879521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Logging must be utilized in order to track system activity, assist in diagnosing system issues, and provide evidence needed for forensic investigations post security incident. Remote access by administrators requires that the admin activity be logged. Application servers provide a web and command line-based remote management capability for managing the application server. Application servers must ensure that all actions related to administrative functionality such as application server configuration are logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep log4j.appender.rollingFile.file /usr/local/horizon/conf/saas-log4j.properties If the "log4j.appender.rollingFile.file" is not set to "/opt/vmware/horizon/workspace/logs/horizon.log" or is commented out or is missing, this is a finding.

## Group: SRG-APP-000148-AS-000101

**Group ID:** `V-240970`

### Rule: vIDM must be configured correctly for the site enterprise user management system.

**Rule ID:** `SV-240970r879589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthorized access, application server users must be uniquely identified and authenticated. This is typically accomplished via the use of a user store which is either local (OS-based) or centralized (LDAP) in nature. To ensure support to the enterprise, the authentication must utilize an enterprise solution.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSO. Obtain the correct configuration for the site's Directory services. In a browser, log in with Tenant admin privileges and navigate to the Administration page. Select Directories Management >> Directories. Click on the configured Directory to review the configuration. If the Directory service is not configured correctly, this is a finding.

## Group: SRG-APP-000172-AS-000121

**Group ID:** `V-240971`

### Rule: vIDM must utilize encryption when using LDAP for authentication.

**Rule ID:** `SV-240971r879609_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords during transmission. Application servers have the capability to utilize LDAP directories for authentication. If LDAP connections are not protected during transmission, sensitive authentication credentials can be stolen. When the application server utilizes LDAP, the LDAP traffic must be encrypted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In a browser, log in with Tenant admin privileges, and navigate to the Administration page. Select Directories Management >> Directories. Click on the configured Directory to review the configuration. If the SSL checkbox is not selected, this is a finding. Note: The checkbox is labeled, "This Directory requires all connections to use SSL".

## Group: SRG-APP-000225-AS-000154

**Group ID:** `V-240972`

### Rule: vIDM must be configured to provide clustering.

**Rule ID:** `SV-240972r879640_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement is dependent upon system MAC and confidentiality. If the system MAC and confidentiality levels do not specify redundancy requirements, this requirement is NA. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. When application failure is encountered, preserving application state facilitates application restart and return to the operational mode of the organization with less disruption of mission/business processes. Clustering of multiple application servers is a common approach to providing fail-safe application availability when system MAC and confidentiality levels require redundancy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSO. Obtain the correct configuration for clustering used by the site. Review the vRealize Automation appliance's installation, environment, and configuration. Determine if vRA clustering has been correctly implemented. If vRA is not correctly implementing clustering, this is a finding.

## Group: SRG-APP-000266-AS-000168

**Group ID:** `V-240973`

### Rule: vIDM must be configured to log activity to the horizon.log file.

**Rule ID:** `SV-240973r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The structure and content of error messages need to be carefully considered by the organization and development team. Any application providing too much information in error logs and in administrative messages to the screen risks compromising the data and security of the application and system. The extent to which the application server is able to identify and handle error conditions is guided by organizational policy and operational requirements. Adequate logging levels and system performance capabilities need to be balanced with data protection requirements. The structure and content of error messages needs to be carefully considered by the organization and development team. Application servers must have the capability to log at various levels, which can provide log entries for potential security-related error events. An example is the capability for the application server to assign a criticality level to a failed logon attempt error message, a security-related error message being of a higher criticality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: grep log4j.appender.rollingFile.file /usr/local/horizon/conf/saas-log4j.properties If the "log4j.appender.rollingFile.file" is not set to "/opt/vmware/horizon/workspace/logs/horizon.log" or is commented out or is missing, this is a finding.

## Group: SRG-APP-000435-AS-000069

**Group ID:** `V-240974`

### Rule: vIDM, when installed in a MAC I system, must be in a high-availability (HA) cluster.

**Rule ID:** `SV-240974r879806_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A MAC I system is a system that handles data vital to the organization's operational readiness or effectiveness of deployed or contingency forces. A MAC I system must maintain the highest level of integrity and availability. By HA clustering the application server, the hosted application and data are given a platform that is load-balanced and provided high-availability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If vRA is not installed in a MAC I system, this is Not Applicable. Interview the ISSO. Obtain the correct configuration for clustering used by the site. Review the vRealize Automation appliance's installation, environment, and configuration. Determine if vRA clustering has been correctly implemented. If vRA is not correctly implementing clustering, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-240975`

### Rule: The vRealize Automation appliance must be configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs.

**Rule ID:** `SV-240975r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the vRealize Automation application to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. The vRA product is continually under refinement, and patches are regularly released to address vulnerabilities. As a result, the vRA STIG is also subject to a release cycle on a quarterly basis. Assessors should ensure that they are reviewing the vRealize Automation appliance with the most current STIG.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the current vRealize Automation STIGs from the ISSO. Verify that this STIG is the most current STIG available for vRealize Automation. Assess all of the organization's vRA installations to ensure that they are fully compliant with the most current STIG. If the most current version of the vRA STIG was not used, or if the vRA appliance configuration is not compliant with the most current STIG, this is a finding.

## Group: SRG-APP-000456-AS-000266

**Group ID:** `V-258456`

### Rule: The version of vRealize Automation 7.x vIDM running on the system must be a supported version.

**Rule ID:** `SV-258456r928891_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions used to install patches across the enclave and to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs). </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
vRealize Automation 7.x vIDM is no longer supported by the vendor. If the system is running vRealize Automation 7.x vIDM, this is a finding.

