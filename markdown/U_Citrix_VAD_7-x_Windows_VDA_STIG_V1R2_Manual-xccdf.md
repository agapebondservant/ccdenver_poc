# STIG Benchmark: Citrix Virtual Apps and Desktop 7.x Windows Virtual Delivery Agent Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000014

**Group ID:** `V-234253`

### Rule: Citrix Windows Virtual Delivery Agent must implement DoD-approved encryption.

**Rule ID:** `SV-234253r960759_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection thereby providing a degree of confidentiality. The encryption strength of mechanism is selected based on the security categorization of the information. Satisfies: SRG-APP-000014, SRG-APP-000015, SRG-APP-000039, SRG-APP-000219, SRG-APP-000439, SRG-APP-000440, SRG-APP-000441, SRG-APP-000442</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
A DoD approved VPN, or gateway/proxy, must be leveraged to access the Windows VDA from a remote network. This VPN, or gateway, must handle user authentication and tunneling of Citrix traffic. The VPN, or gateway, must meet the DoD encryption requirements, such as FIPS 140-2, for the environment. If no VPN, or gateway/proxy, is used for remote access to the VDA, this is a finding. If the VPN, or gateway/proxy, does not authenticate the remote user before providing access to the VDA, this is a finding. If the VPN, or gateway/proxy, fails to meet the DoD encryption requirements for the environment, this is a finding.

## Group: SRG-APP-000142

**Group ID:** `V-234254`

### Rule: Citrix Windows Virtual Delivery Agent must be configured to prohibit or restrict the use of ports, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-234254r1043177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web service); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Some organizations consider port 80 to be a non-secure port regardless of the protocol. Ensure VDA registration traffic to the Delivery Controller is occurring on an approved port. To verify the Delivery Controller is using an approved port, perform the following: 1. On each the Delivery Controller, open a command prompt. 2. Navigate to the Citrix install directory Program Files\Citrix\Broker\Service. 3. Run the command "BrokerService.exe /Show" to display the currently used "VDA Port". 4. Ensure the port in use on each Delivery Controller matches and is approved by the DoD organization. To verify the Windows VDA is using the approved port for registration, perform the following: 1. In Active Directory, open the Group Policy object used to apply VDA settings to the Windows VDA. 2. Navigate to Computer Configuration >> Policies >> Citrix Policies. 3. Edit the "Unfiltered Policy", or the custom policy used to apply Delivery Controller settings in the GPO. 4. Under the "Settings" tab, find the Virtual Delivery Agent Setting called "Controller registration port". 5. Ensure the port number matches the approved port set on the Delivery Controller. If an unapproved port is used, this is a finding.

## Group: SRG-APP-000456

**Group ID:** `V-275971`

### Rule: The version of Virtual Apps and Desktop Windows VDA running on the system must be a supported version.

**Rule ID:** `SV-275971r1115778_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications that are not part of that patch management solution. For example, many browsers provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may depend on the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Virtual Apps and Desktop Windows VDA 7.x is no longer supported by the vendor. If the system is running Virtual Apps and Desktop Windows VDA 7.x, this is a finding.

