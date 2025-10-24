# STIG Benchmark: Citrix XenDesktop 7.x Receiver Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000014

**Group ID:** `V-213208`

### Rule: Citrix Receiver must implement DoD-approved encryption.

**Rule ID:** `SV-213208r960759_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection thereby providing a degree of confidentiality. The encryption strength of mechanism is selected based on the security categorization of the information. Satisfies: SRG-APP-000014, SRG-APP-000015, SRG-APP-000142, SRG-APP-000219, SRG-APP-000416, SRG-APP-000427, SRG-APP-000439, SRG-APP-000440, SRG-APP-000441, SRG-APP-000442, SRG-APP-000514</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify encryption has been enabled on devices running Citrix Receiver: Open the Citrix Receiver Group Policy Object administrative template by running gpedit.msc. 1. Launch the Citrix Receiver Group Policy Object administrative template using the Group Policy Management Console. 2. Under the Computer Configuration node, go to Administrative Templates >> Citrix Receiver >> Network routing and select the TLS and Compliance Mode Configuration policy. 3. Verify the policy is enabled. If the policy is not enabled, this is a finding. 4. Verify the following policy options are selected: - Verify "Require TLS for all connections" is selected. - From the Security Compliance Mode drop-down, verify "SP800-52" is selected. - Verify "Full access check and CRL required" is selected. - Verify "Enable FIPS: is selected. - From the Allow TLS Servers drop-down, verify the desired port number is entered. - Verify "TLS 1.2" is selected. - From the TLS cipher suite drop-down, verify "Select Government (GOV)" is selected. - From the Certificate Revocation Check Policy drop-down, select the policy required by your Organizational Security Policy. If any of the policy options noted above are not selected, this is a finding.

## Group: SRG-APP-000391

**Group ID:** `V-213209`

### Rule: Citrix Receiver must accept Personal Identity Verification (PIV) credentials.

**Rule ID:** `SV-213209r961494_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. DoD has mandated the use of the CAC to support identity management and personal authentication for systems covered under HSPD 12, as well as a primary component of layered protection for national security systems. Satisfies: SRG-APP-000391, SRG-APP-000392</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Administrative Templates >> Classic Administrative Templates (ADM) >> Citrix Components >> Citrix Receiver >> User authentication >> "Local user name and password" is set to "Enabled" with the option "Enable pass-through authentication" checked. If the "Local user name and password" policy is not "Enabled" or does not have the "Enable pass-through authentication" option checked, this is a finding.

## Group: SRG-APP-000456

**Group ID:** `V-275974`

### Rule: The version of XenDesktop Receiver running on the system must be a supported version.

**Rule ID:** `SV-275974r1115919_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications that are not part of that patch management solution. For example, many browsers provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may depend on the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
XenDesktop Receiver 7.x is no longer supported by the vendor. If the system is running XenDesktop Receiver 7.x, this is a finding.

