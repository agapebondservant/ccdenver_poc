# STIG Benchmark: Citrix Virtual Apps and Desktop 7.x StoreFront Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000014

**Group ID:** `V-234251`

### Rule: The Citrix Storefront server must implement DoD-approved encryption to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-234251r960759_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection thereby providing a degree of confidentiality. The encryption strength of mechanism is selected based on the security categorization of the information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
A DoD approved VPN, or gateway/proxy, must be leveraged to access StoreFront from a remote network. This VPN, or gateway, must handle user authentication and tunneling of StoreFront traffic. The VPN, or gateway, must meet the DoD encryption requirements, such as FIPS 140-2, for the environment. If no VPN, or gateway/proxy, is used for remote access to StoreFront, this is a finding. If the VPN, or gateway/proxy, does not authenticate the remote user before providing access to StoreFront, this is a finding. If the VPN, or gateway/proxy, fails to meet the DoD encryption requirements for the environment, this is a finding.

## Group: SRG-APP-000391

**Group ID:** `V-234252`

### Rule: Citrix StoreFront server must accept Personal Identity Verification (PIV) credentials.

**Rule ID:** `SV-234252r961494_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. DoD has mandated the use of the Common Access Card (CAC) to support identity management and personal authentication for systems covered under HSPD 12, as well as a primary component of layered protection for national security systems. Satisfies: SRG-APP-000391, SRG-APP-000033, SRG-APP-000392, SRG-APP-000439, SRG-APP-000440, SRG-APP-000442</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Citrix StoreFront management console and select the "Store" node in the left pane. For each Store listed, select the store and perform the following: 1) From the Actions menu item, click "Manage Authentication Methods". 2) Ensure only "Smart card" is selected. If using remote access "Pass-through from NetScaler Gateway" may also be selected. If the "Smart Card" method is not selected, or if other methods are selected, this is a finding. If "Pass-through from NetScaler Gateway" is selected, this is not a finding.

## Group: SRG-APP-000456

**Group ID:** `V-275970`

### Rule: The version of Virtual Apps and Desktop Storefront running on the system must be a supported version.

**Rule ID:** `SV-275970r1115777_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications that are not part of that patch management solution. For example, many browsers provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may depend on the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Virtual Apps and Desktop Storefront 7.x is no longer supported by the vendor. If the system is running Virtual Apps and Desktop Storefront 7.x, this is a finding.

