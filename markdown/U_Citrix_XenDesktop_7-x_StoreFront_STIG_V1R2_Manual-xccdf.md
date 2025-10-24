# STIG Benchmark: Citrix XenDesktop 7.x StoreFront Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000391

**Group ID:** `V-213211`

### Rule: XenDesktop StoreFront must accept Personal Identity Verification (PIV) credentials.

**Rule ID:** `SV-213211r961494_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. DoD has mandated the use of the CAC to support identity management and personal authentication for systems covered under HSPD 12, as well as a primary component of layered protection for national security systems. Satisfies: SRG-APP-000391, SRG-APP-000033, SRG-APP-000392, SRG-APP-000439, SRG-APP-000440, SRG-APP-000442</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Citrix StoreFront management console. Select the "Store" node in the left pane. In the "Actions" pane, click "Manage Authentication Methods". Select only the "Smart Card" method. If the "Smart Card" method is not selected or if other methods are selected, this is a finding. Note: If a NetScaler Gateway is handling authentication, "Pass-through from NetScaler Gateway" may also be selected, this is not a finding.

## Group: SRG-APP-000456

**Group ID:** `V-275976`

### Rule: The version of XenDesktop Storefront running on the system must be a supported version.

**Rule ID:** `SV-275976r1115920_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications that are not part of that patch management solution. For example, many browsers provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may depend on the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
XenDesktop Storefront 7.x is no longer supported by the vendor. If the system is running XenDesktop Storefront 7.x, this is a finding.

