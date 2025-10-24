# STIG Benchmark: Citrix Virtual Apps and Desktop 7.x Delivery Controller Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000014

**Group ID:** `V-234565`

### Rule: Citrix Delivery Controller must implement DoD-approved encryption.

**Rule ID:** `SV-234565r960759_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection, thereby providing a degree of confidentiality. The encryption strength of mechanism is selected based on the security categorization of the information. Satisfies: SRG-APP-000014, SRG-APP-000015, SRG-APP-000039, SRG-APP-000142, SRG-APP-000172, SRG-APP-000219, SRG-APP-000224, SRG-APP-000416, SRG-APP-000439, SRG-APP-000440, SRG-APP-000441, SRG-APP-000442, SRG-APP-000514</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Enforcement is via TLS encryption. To verify, open the Registry Editor on each Delivery Controller and find the following key name: HKEY_LOCAL_MACHINE\SOFTWARE\Citrix\DesktopServer 1. Verify that the XmlServicesSslPort registry key exists with the correct value for SSL port. By default, it is set to "443". 2. Verify XmlServicesEnableNonSsl is set to "0". 3. Verify the corresponding registry value to ignore HTTPS traffic, XmlServicesEnableSsl, is not set to "0". If "XmlServicesSslPort" is not set to the desired port, this is a finding. If "XmlServicesEnableNonSsl" is not set to "0", this is a finding. If XmlServicesEnableSsl is not set to "1", this is a finding. To verify the FIPS Cipher Suites used: 1. From the Group Policy Management Console, go to Computer Configuration >> Administrative Templates >> Networks >> SSL Configuration Settings. 2. Double-click "SSL Cipher Suite Order" and verify the "Enabled" option is checked. 3. Verify the correct Cipher Suites are listed in the correct order per current DoD guidelines. If the "Enabled" option is not checked or the correct Cipher Suites are not listed in the correct order per current DoD guidelines, this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-234567`

### Rule: Citrix Delivery Controller must be configured to disable non-essential capabilities.

**Rule ID:** `SV-234567r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for applications to provide or install by default functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include but are not limited to advertising software or browser plug-ins not related to requirements or providing a wide array of functionality not required for every mission but that cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Citrix Customer Experience Improvement Program (CEIP) - PHONE HOME is disabled on Delivery Controller. 1. Launch Studio. 2. Select "Configuration" in the left navigation pane. 3. Select the Support tab. 4. Verify CEIP is disabled. If CEIP is not disabled, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-234569`

### Rule: Citrix Delivery Controller must be configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs.

**Rule ID:** `SV-234569r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the application to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affects the security posture and/or functionality of the system. Security-related parameters are parameters impacting the security state of the application, including the parameters required to satisfy other security control requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that Citrix Delivery Controller and all other infrastructure server components are installable and manageable by authorized administrative accounts, the following policies must be modified: Go to Computer Configuration Policies >> Windows Settings >> Security Settings >> Local Policies/User Rights Assignment. Verify policy settings "Allow log on locally" and "Shut down the system" are both set to the global security group name containing the XenApp or CVAD administrators. If they are not, this is a finding.

## Group: SRG-APP-000456

**Group ID:** `V-275967`

### Rule: The version of Virtual Apps and Desktop Delivery Controller running on the system must be a supported version.

**Rule ID:** `SV-275967r1115781_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications that are not part of that patch management solution. For example, many browsers provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may depend on the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Virtual Apps and Desktop Delivery Controller 7.x is no longer supported by the vendor. If the system is running Virtual Apps and Desktop Delivery Controller 7.x, this is a finding.

