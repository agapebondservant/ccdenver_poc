# STIG Benchmark: Citrix XenDesktop 7.x Delivery Controller Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001

**Group ID:** `V-213195`

### Rule: Delivery Controller must limit the number of concurrent sessions to an organization-defined number for all accounts and/or account types.

**Rule ID:** `SV-213195r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application management includes the ability to control the number of users and user sessions that utilize an application. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to Denial-of-Service (DoS) attacks. This requirement may be met via the application or by using information system session control provided by a web server with specialized session management capabilities. If it has been specified that this requirement will be handled by the application, the capability to limit the maximum number of concurrent single user sessions must be designed and built into the application. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based on mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open Citrix Studio, right-click a Delivery Group, and choose "Edit Delivery Group". Verify the following check box is not checked: "Give access to unauthenticated (anonymous) users; no credentials are required to access StoreFront". If the check box is checked, this is a finding. A Citrix Studio administrator account is needed to perform this check. Performing this check does not impact system reliability or availability.

## Group: SRG-APP-000141

**Group ID:** `V-213196`

### Rule: Delivery Controller must be configured to disable non-essential capabilities.

**Rule ID:** `SV-213196r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for applications to provide or install by default functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include but are not limited to advertising software or browser plug-ins not related to requirements or providing a wide array of functionality not required for every mission but that cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Citrix Customer Experience Improvement Program (CEIP) - PHONE HOME is disabled on XenDesktop Delivery Controller. 1. Launch Studio. 2. Select "Configuration" in the left navigation pane. 3. Select the Support tab. 4. Verify CEIP is disabled. If CEIP is not disabled, this is a finding.

## Group: SRG-APP-000514

**Group ID:** `V-213197`

### Rule: Delivery Controller must implement NIST FIPS-validated cryptography for the following: to provision digital signatures; to generate cryptographic hashes; and to protect unclassified information requiring confidentiality and cryptographic protection in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.

**Rule ID:** `SV-213197r1115916_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the Federal Government since this provides assurance they have been tested and validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Enforcement is via FIPS encryption. To verify, open the Registry Editor on the XenDesktop Delivery Controller and find the following key name: HKEY_LOCAL_MACHINE\SOFTWARE\Citrix\DesktopServer 1. Verify that the XmlServicesSslPort registry key exists with the correct value for SSL port. By default, it is set to "443". 2. Verify XmlServicesEnableNonSsl is set to "0". 3. Verify the corresponding registry value to ignore HTTPS traffic, XmlServicesEnableSsl, is not set to "0". If "XmlServicesSslPort" is not set to the desired port, this is a finding. If "XmlServicesEnableNonSsl" is not set to "0", this is a finding. If XmlServicesEnableSsl is not set to "1", this is a finding. To verify the FIPS Cipher Suites used: 1. From the Group Policy Management Console, go to Computer Configuration >> Administrative Templates >> Networks >> SSL Configuration Settings. 2. Double-click "SSL Cipher Suite Order" and verify the "Enabled" option is checked. 3. Verify the correct Cipher Suites are listed in the correct order per current DOD guidelines. If the "Enabled" option is not checked or the correct Cipher Suites are not listed in the correct order per current DOD guidelines, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-213198`

### Rule: Delivery Controller must be configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs.

**Rule ID:** `SV-213198r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the application to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affects the security posture and/or functionality of the system. Security-related parameters are parameters impacting the security state of the application, including the parameters required to satisfy other security control requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that XenDesktop Controller and all other infrastructure server components are installable and manageable by authorized administrative accounts, the following policies must be modified: Go to Computer Configuration Policies >> Windows Settings >> Security Settings >> Local Policies/User Rights Assignment. Verify policy settings "Allow log on locally" and "Shut down the system" are both set to the global security group name containing the XenApp or XenDesktop administrators. "Local Administrators" may remain. If they are not set to the global security group name containing the XenApp or XenDesktop administrators, this is a finding.

## Group: SRG-APP-000456

**Group ID:** `V-275973`

### Rule: The version of XenDesktop Delivery Controller running on the system must be a supported version.

**Rule ID:** `SV-275973r1115917_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications that are not part of that patch management solution. For example, many browsers provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may depend on the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
XenDesktop Delivery Controller 7.x is no longer supported by the vendor. If the system is running XenDesktop Delivery Controller 7.x, this is a finding.

