# STIG Benchmark: VMware Automation 7.x Application Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000179-AS-000129

**Group ID:** `V-239845`

### Rule: vRA must enable FIPS Mode.

**Rule ID:** `SV-239845r879616_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified and cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised due to weak algorithms. The use of TLS provides confidentiality of data in transit between the application server and client. FIPS 140-2 approved TLS versions include TLS V1.0 or greater. TLS must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 specifies the preferred configurations for government systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that FIPS mode is enabled in the vRealize Automation virtual appliance management interface with the following steps: 1. Log on to the vRealize Automation virtual appliance management interface (vAMI): https://vrealize-automation-appliance-FQDN:5480 2. Select vRA Settings >> Host Settings. 3. Review the button under the Actions heading on the upper right to confirm that "enable FIPS" is selected. If "enable FIPS" is not selected, this is a finding. Alternately, check that FIPS mode is enabled in the command line using the following steps: 1. Log on to the console as root. 2. Run the command: vcac-vami fips status If FIPS is not enabled, this is a finding.

## Group: SRG-APP-000220-AS-000148

**Group ID:** `V-239846`

### Rule: The vRealize Automation application must be configured to a 15 minute of less session timeout.

**Rule ID:** `SV-239846r879637_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If communications sessions remain open for extended periods of time even when unused, there is the potential for an adversary to hijack the session and use it to gain access to the device or networks to which it is attached. Terminating sessions after a logout event or after a certain period of inactivity is a method for mitigating the risk of this vulnerability. When a user management session becomes idle, or when a user logs out of the management interface, the application server must terminate the session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the session timeout is set to an organization-defined time with the following steps: 1. Log on to the admin UI as the administrator. 2. Navigate to "Global Settings". 3. Review the session timeout value in minutes. If the session timeout setting is not set to 15 minutes or less, this is a finding.

## Group: SRG-APP-000225-AS-000153

**Group ID:** `V-239847`

### Rule: The vRealize Automation server must be configured to perform complete application deployments.

**Rule ID:** `SV-239847r879640_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. When an application is deployed to the application server, if the deployment process does not complete properly and without errors, there is the potential that some application files may not be deployed or may be corrupted and an application error may occur during runtime. The application server must be able to perform complete application deployments. A partial deployment can leave the server in an inconsistent state. Application servers may provide a transaction rollback function to address this issue.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the site configuration control policy from the ISSO. Review site procedures to determine if a site policy exists to verify vRA installation after release into a production environment. The site policy should ensure that the installation was a complete application deployment before users are allowed to conduct business. If a site policy does not exist or is not being followed, this is a finding.

## Group: SRG-APP-000340-AS-000185

**Group ID:** `V-239848`

### Rule: The vRealize Automation security file must be restricted to the vcac user.

**Rule ID:** `SV-239848r879717_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. The vRealize Automation product stores important system information in the security.properties file. Preventing access to this file from non-privileged is essential to ensure the integrity and confidentiality of vRA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, execute the following command: ls -l /etc/vcac/security.properties If the file owner and group-owner are not "vcac", this is a finding.

## Group: SRG-APP-000427-AS-000264

**Group ID:** `V-239849`

### Rule: The application server must only allow the use of DoD PKI-established certificate authorities for verification of the establishment of protected sessions.

**Rule ID:** `SV-239849r879798_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DoD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DoD-approved CA, trust of this CA has not been established. The DoD will only accept PKI certificates obtained from a DoD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of SSL/TLS certificates. The application server must only allow the use of DoD PKI-established certificate authorities for verification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Smart Card Authentication is in use with the following steps: 1. In vRA, go to Administration >> Directories Management >> Identity Providers. 2. Verify that the identity provider listed is the identity provider used for smart card authentication. 3. In vRA, go to Administration >> Directories Management >> Policies. 4. Verify that the default policy authentication method is set to "certificate". If the identity provider listed is not that used for smart card authentication, this is a finding. If the default policy authentication method is not set to "certificate", this is a finding.

## Group: SRG-APP-000514-AS-000137

**Group ID:** `V-239850`

### Rule: The application server must use DoD- or CNSS-approved PKI Class 3 or Class 4 certificates.

**Rule ID:** `SV-239850r879885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Class 3 PKI certificates are used for servers and software signing rather than for identifying individuals. Class 4 certificates are used for business-to-business transactions. Utilizing unapproved certificates not issued or approved by DoD or CNS creates an integrity risk. The application server must utilize approved DoD or CNS Class 3 or Class 4 certificates for software signing and business-to-business transactions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Smart Card Authentication is in use with the following steps: 1. In vRA, go to Administration >> Directories Management >> Identity Providers. 2. Verify that the identity provider listed is the identity provider used for smart card authentication. 3. In vRA, go to Administration >> Directories Management >> Policies. 4. Verify that the default policy authentication method is set to "certificate". If the identity provider listed is not that used for smart card authentication, this is a finding. If the default policy authentication method is not set to "certificate", this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-239851`

### Rule: The vRealize Automation appliance must be configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs.

**Rule ID:** `SV-239851r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the vRealize Automation application to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. The vRA product is continually under refinement, and patches are regularly released to address vulnerabilities. As a result, the vRA STIG is also subject to a release cycle on a quarterly basis. Assessors should ensure that they are reviewing the vRealize Automation appliance with the most current STIG.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the current vRealize Automation STIGs from the ISSO. Verify that this STIG is the most current STIG available for vRealize Automation. Assess all of the organization's vRA installations to ensure they are fully compliant with the most current STIG. If the most current version of the vRA STIG was not used, or if the vRA appliance configuration is not compliant with the most current STIG, this is a finding.

## Group: SRG-APP-000456-AS-000266

**Group ID:** `V-258450`

### Rule: The version of vRealize Automation application running on the system must be a supported version.

**Rule ID:** `SV-258450r928879_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions used to install patches across the enclave and to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs). </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
vRealize Automation 7.x Application is no longer supported by the vendor. If the system is running vRealize Automation 7.x Application, this is a finding.

