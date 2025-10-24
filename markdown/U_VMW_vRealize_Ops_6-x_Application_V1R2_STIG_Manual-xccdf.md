# STIG Benchmark: VMware vRealize Operations Manager 6.x Application Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000148-AS-000101

**Group ID:** `V-239840`

### Rule: The vRealize Operations server must use an enterprise user management system to uniquely identify and authenticate users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-239840r879589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthorized access, application server users must be uniquely identified and authenticated. This is typically accomplished via the use of a user store that is either local (OS-based) or centralized (LDAP) in nature. To ensure support to the enterprise, the authentication must utilize an enterprise solution.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the site configuration control policy from the ISSO. Review site procedures to determine if an enterprise management system is used to uniquely identify and authenticate users. If an enterprise management solution is not used, this is a finding.

## Group: SRG-APP-000220-AS-000148

**Group ID:** `V-239841`

### Rule: The vRealize Operations server session timeout must be configured.

**Rule ID:** `SV-239841r879637_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If communications sessions remain open for extended periods of time even when unused, there is the potential for an adversary to hijack the session and use it to gain access to the device or networks to which it is attached. Terminating sessions after a logout event or after a certain period of inactivity is a method for mitigating the risk of this vulnerability. When a user management session becomes idle, or when a user logs out of the management interface, the application server must terminate the session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the session timeout is set to "15" minutes with the following steps: 1. Log on to the admin UI as the administrator. 2. Navigate to "Global Settings". 3. Review the session timeout value in mins. If the "Session Timeout:" setting is not "15" minutes, this is a finding.

## Group: SRG-APP-000225-AS-000153

**Group ID:** `V-239842`

### Rule: The vRealize Operations server must be configured to perform complete application deployments.

**Rule ID:** `SV-239842r879640_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. When an application is deployed to the application server, if the deployment process does not complete properly and without errors, there is the potential that some application files may not be deployed or may be corrupted and an application error may occur during runtime. The application server must be able to perform complete application deployments. A partial deployment can leave the server in an inconsistent state. Application servers may provide a transaction rollback function to address this issue.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the site configuration control policy from the ISSO. Review site procedures to determine if a site policy exists to verify vROps installation after release into a production environment. The site policy should ensure that the installation was a complete application deployment before users are allowed to conduct business. If a site policy does not exist or is not being followed, this is a finding.

## Group: SRG-APP-000427-AS-000264

**Group ID:** `V-239843`

### Rule: The vRealize Operations server must only allow the use of DoD PKI-established certificate authorities for verification of the establishment of protected sessions.

**Rule ID:** `SV-239843r879798_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DoD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DoD-approved CA, trust of this CA has not been established. The DoD will only accept PKI certificates obtained from a DoD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of SSL/TLS certificates. The application server must only allow the use of DoD PKI-established certificate authorities for verification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the vROps Single Sign-On (SSO) is configured with the correct authentication source only (DoD PKI CAC enabled vSphere SSO instance) by using the following steps: 1. Log on to the admin UI as the administrator. 2. In the menu, click Administration, and then in the left pane click Access >> Authentication Sources. 3. Review the authentication sources and ensure that only the DoD PKI CAC enabled vSphere SSO instance is available as an authentication source. If there is no authentication source, or multiple non-DoD PKI CAC enabled vSphere SSO instance authentication sources exist, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-239844`

### Rule: The vRealize Operations appliance must be configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs.

**Rule ID:** `SV-239844r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the vRealize Operations appliance to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. The vROps product is continually under refinement, and patches are regularly released to address vulnerabilities. As a result, the vROps STIG is also subject to a release cycle on a quarterly basis. Assessors should ensure that they are reviewing the vRealize Operations appliance with the most current STIG.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the current vRealize Operations STIGs from the ISSO. Verify that this Security Technical Implementation Guide (STIG) is the most current STIG available for vRealize Operations. Assess all of the organization's vROps installations to ensure that they are fully compliant with the most current STIG. If the most current version of the vROps STIG was not used, or if the vROps appliance configuration is not compliant with the most current STIG, this is a finding.

## Group: SRG-APP-000456-AS-000266

**Group ID:** `V-258457`

### Rule: The version of vRealize Operations Manager 6.x Application running on the system must be a supported version.

**Rule ID:** `SV-258457r928893_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions used to install patches across the enclave and to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs). </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
vRealize Operations Manager 6.x Application is no longer supported by the vendor. If the system is running vRealize Operations Manager 6.x Application, this is a finding.

