# STIG Benchmark: Arctic Wolf CylanceON-PREM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001

**Group ID:** `V-272627`

### Rule: CylanceON-PREM must be configured to use a third-party identity provider.

**Rule ID:** `SV-272627r1113422_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Configuring CylanceON-PREM to integrate with an Enterprise Identity Provider enhances security, simplifies user management, ensures compliance, provides auditing capabilities, and offers a more seamless and consistent user experience. It aligns CylanceON-PREM with enterprise standards and contributes to a more efficient and secure environment. Satisfies: SRG-APP-000001, SRG-APP-000023, SRG-APP-000025, SRG-APP-000033, SRG-APP-000065, SRG-APP-000118, SRG-APP-000121, SRG-APP-000148, SRG-APP-000149, SRG-APP-000150, SRG-APP-000153, SRG-APP-000154, SRG-APP-000155, SRG-APP-000157, SRG-APP-000163, SRG-APP-000164, SRG-APP-000165, SRG-APP-000166, SRG-APP-000167, SRG-APP-000168, SRG-APP-000169, SRG-APP-000170, SRG-APP-000173, SRG-APP-000176, SRG-APP-000177, SRG-APP-000183, SRG-APP-000185, SRG-APP-000345, SRG-APP-000400, SRG-APP-000401, SRG-APP-000404, SRG-APP-000405, SRG-APP-000461, SRG-APP-000700, SRG-APP-000705, SRG-APP-000710, SRG-APP-000715, SRG-APP-000720, SRG-APP-000730, SRG-APP-000735, SRG-APP-000740, SRG-APP-000815, SRG-APP-000820, SRG-APP-000825, SRG-APP-000830, SRG-APP-000835, SRG-APP-000840, SRG-APP-000845, SRG-APP-000850, SRG-APP-000855, SRG-APP-000860, SRG-APP-000865, SRG-APP-000870, SRG-APP-000875</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Identity Provider (IDP) settings. Administrator privileges are required. Using LDAP: 1. Log in to the admin console. 2. Navigate to Configuration >> Settings. 3. Locate the LDAP section. If LDAP (an authorized IDP) is not configured correctly or is disabled, this is not a finding. Not using LDAP: 1. Log in to the admin console. 2. Navigate to Configuration >> Settings. 3. Locate Identity Provider Settings. Review documentation of allowed IDPs. If IDP settings are not configured correctly or the IDP is disabled or not authorized, this is a finding.

## Group: SRG-APP-000003

**Group ID:** `V-272628`

### Rule: CylanceON-PREM must be configured to initiate a session timeout after 10 minutes of inactivity.

**Rule ID:** `SV-272628r1113425_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensuring inactive sessions are terminated provides protection against misuse of the system. Satisfies: SRG-APP-000003, SRG-APP-000190, SRG-APP-000295</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Session timeout. 1. Log in to the admin console. 2. Navigate to CONFIGURATION >> Settings. 3. Find Session Timeout. If the value is not set to 10 minutes, this is a finding.

## Group: SRG-APP-000014

**Group ID:** `V-272629`

### Rule: CylanceON-PREM must be configured to use TLS 1.2 or higher.

**Rule ID:** `SV-272629r1113430_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Using older unauthorized versions or incorrectly configuring protocol negotiation makes the gateway vulnerable to known and unknown attacks that exploit vulnerabilities in this protocol. Satisfies: SRG-APP-000014, SRG-APP-000156, SRG-APP-000172, SRG-APP-000179, SRG-APP-000219, SRG-APP-000439, SRG-APP-000440, SRG-APP-000441, SRG-APP-000442, SRG-APP-000560, SRG-APP-000565, SRG-APP-000605, SRG-APP-000645</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Cipher configuration. Administrator privileges are required. 1. Log in to the admin console. 2. Navigate to CONFIGURATION >> Settings. 3. Find CylanceON-PREM Info >> Certificate Cipher. If the value is not set to Modern Mode (TLS 1.2+), this is a finding.

## Group: SRG-APP-000068

**Group ID:** `V-272630`

### Rule: CylanceON-PREM must be configured to show the standard mandatory DOD Notice and Consent Banner before granting access to CylanceON-PREM.

**Rule ID:** `SV-272630r1113685_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Presentation of the standard DOD Notice and Consent Banner is required to ensure privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. Use the following verbiage: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." Satisfies: SRG-APP-000068, SRG-APP-000069, SRG-APP-000070</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Login Screen Banner. Administrator privileges are required. 1. Log in to the admin console. 2. Navigate to CONFIGURATION >> Settings. 3. Find the Login Screen Banner and click "Edit". If the Login Screen Banner is not enabled or is not configured to display the standard DOD Notice and Consent Banner, this is a finding.

## Group: SRG-APP-000080

**Group ID:** `V-272631`

### Rule: Session-only-based cookies must be enabled.

**Rule ID:** `SV-272631r1112743_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cookies must only be allowed per session and only for approved URLs, as permanently stored cookies can be used for malicious intent. Approved URLs may be allowlisted via the "CookiesAllowedForUrls" or "SaveCookiesOnExit" policy settings, but these are not requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Content settings/Configure cookies" is set to "Enabled" with the option value set to "Keep cookies for the duration of the session, except ones listed in 'SaveCookiesOnExit'". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "DefaultCookiesSetting" is not set to "REG_DWORD = 4", this is a finding.

## Group: SRG-APP-000108

**Group ID:** `V-272632`

### Rule: CylanceON-PREM must be configured to support integration with a third-party Security Information and Event Management (SIEM) to support notifications.

**Rule ID:** `SV-272632r1113445_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Integrating a Central Log Server for managing audit records enhances security monitoring, incident response, and compliance efforts. By providing centralized logging, real-time analysis, and automated alerting, a Central Log Server allows CylanceON-PREM to maintain a robust security posture and effectively respond to potential threats, ultimately contributing to the organization's overall security strategy. Satisfies: SRG-APP-000108, SRG-APP-000115, SRG-APP-000125, SRG-APP-000126, SRG-APP-000181, SRG-APP-000291, SRG-APP-000292, SRG-APP-000293, SRG-APP-000294, SRG-APP-000320, SRG-APP-000358, SRG-APP-000360, SRG-APP-000474, SRG-APP-000515, SRG-APP-000745, SRG-APP-000795</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SIEM, Administrator privileges are required. 1. Log in to the admin console. 2. Navigate to CONFIGURATION >> Settings. 3. Find Syslog/SIEM. If Syslog/SIEM is not enabled or the settings are not configured correctly, this is a finding.

## Group: SRG-APP-000233

**Group ID:** `V-272633`

### Rule: CylanceON-PREM must be configured with only one local Role to be used by the account of last resort in the event the authentication server is unavailable.

**Rule ID:** `SV-272633r1113481_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>CylanceON-PREM uses a third-party identity provider (IDP) for access. The use of a "break glass" account is a critical failsafe measure for emergency situations where normal administrative access is unavailable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify only Administrator (break-glass user) role is local. 1. Log in to the admin console. 2. Navigate to ACCESS MANAGEMENT >> Role Management. 3. Observe the list of Roles. If any Roles other than break-glass/Admin Role exist, this is a finding.

## Group: SRG-APP-000275

**Group ID:** `V-272634`

### Rule: CylanceON-PREM must be configured to send alerts via Simple Mail Transfer Protocol (SMTP).

**Rule ID:** `SV-272634r1113494_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to notify personnel of failed tests introduces a risk to the system. Corrective action and the unsecure condition(s) will remain. Satisfies: SRG-APP-000275, SRG-APP-000279, SRG-APP-000940</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SMTP Settings. Administrator privileges are required. 1. Log in to the admin console. 2. Navigate to CONFIGURATION >> Settings. 3. Find SMTP. If SMTP is not enabled, this is a finding. If SMTP settings are not populated and event type notifications not enabled, this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-272635`

### Rule: CylanceON-PREM must enforce that all files accessed are evaluated against the AI model for potential threats.

**Rule ID:** `SV-272635r1112755_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>CylanceON-PREM enforces file evaluations against its AI model to ensure proactive, predictive, and comprehensive security. Failure to scan files introduces a potential risk to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Background Threat Detection and File Watcher settings are enabled. Administrator rights are required. 1. Log in to the admin console. 2. Navigate to POLICIES. 3. Click on each device policy. If Background Threat Detection or File Watcher settings are disabled, this is a finding. If there are no enabled policies, this is a finding.

## Group: SRG-APP-000340

**Group ID:** `V-272636`

### Rule: CylanceON-PREM must be configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable.

**Rule ID:** `SV-272636r1113520_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>there must not be local users/roles within CylanceON-PREM. Manually verifying local users and roles ensures that unauthorized users do not gain access to sensitive resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that only admin break-glass user is local. 1. Log in to the admin console. 2. Navigate to ACCESS MANAGEMENT >> User Management. 3. Observe the list of users. If any users other than break-glass/Admin user exist, this is a finding. If the break-glass/Admin user is using the default name or password, this is a finding.

## Group: SRG-APP-000357

**Group ID:** `V-272637`

### Rule: CylanceON-PREM must be configured to use an external database if users exceed 30,000.

**Rule ID:** `SV-272637r1113525_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Exhausting audit log storage will introduce failures in audit logging, which will result in loss of security monitoring information. Satisfies: SRG-APP-000357, SRG-APP-000359</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If there are less than 30,000 users, this requirement is Not Applicable. Verify external database. Administrator privileges are required. 1. Log in to the admin console. 2. Navigate to CONFIGURATION >> Settings. 3. View Database Connection Settings. If no database settings are found, the system was installed with the local database, and default size settings are used, this is a finding.

## Group: SRG-APP-000383

**Group ID:** `V-272638`

### Rule: CylanceON-PREM must disable all functions, ports, protocols and services not required.

**Rule ID:** `SV-272638r1113550_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unnecessary or unsecured ports, protocols, and services present many risks for attackers and may go undetected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify port configuration to external subordinate services such as syslog/SEIM, SMTP, etc. Administrator privileges are required. 1. Log in to the admin console. 2. Navigate to CONFIGURATION >> Settings. 3. Review settings. 4. Verify the ports used are accurate. If any ports are being used that are not required, this is a finding.

## Group: SRG-APP-000391

**Group ID:** `V-272639`

### Rule: CylanceON-PREM must be configured with a DOD issued certificate (or another authorizing official [AO]-approved certificate).

**Rule ID:** `SV-272639r1113556_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DOD will only accept PKI certificates obtained from a DOD-approved internal or external certificate authority. Reliance on certificate authorities (CAs) for the establishment of secure sessions includes, for example, the use of TLS certificates. This requirement focuses on communications protection for the CylanceON-PREM session rather than for the network packet. This requirement applies to applications that use communications sessions. This includes, but is not limited to, web-based applications and Service-Oriented Architectures (SOAs). Using a trusted access credential reduces risk of unauthorized access. Satisfies: SRG-APP-000391, SRG-APP-000175, SRG-APP-000392, SRG-APP-000402, SRG-APP-000403, SRG-APP-000427</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Certificate-Based Authentication Settings. Administrator privileges are required. 1. Log in to the admin console. 2. Navigate to CONFIGURATION >> Settings. 3. Find Certificate-Based Authentication. 4. Click "Edit" to open configuration. If Certificate-Based Authentication is not enabled, this is a finding. If the certificate is not a DOD-issued certificate (or other AO-approved certificate), this is a finding.

## Group: SRG-APP-000456

**Group ID:** `V-272640`

### Rule: CylanceON-PREM must be running the latest release. 

**Rule ID:** `SV-272640r1113602_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. CylanceON-PREM will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system is the latest release. Administrator access is required. Verify the version: 1. Navigate to CONFIGURATION >> Settings. 2. Verify the version. If the system is not at the latest released version, this is a finding.

## Group: SRG-APP-000473

**Group ID:** `V-272641`

### Rule: CylanceON-PREM must be restarted every 30 days to invoke health checks.

**Rule ID:** `SV-272641r1112773_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restarting CylanceON-PREM every 30 days ensures system stability and performance. Regular health checks of the system reduce the risk of security function failures in the system. Satisfies: SRG-APP-000473, SRG-APP-000475</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the reboot date. Administrator privileges are required. 1. Click AUDIT LOGS. 2. Search for "Reboot" and note the date. If date is more than 30 days in the past, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-272642`

### Rule: All associated custom applications, including API endpoints, must be inventoried and managed.

**Rule ID:** `SV-272642r1113686_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Console Applications page provides integration with the CylanceON-PREM API. An application has a unique application ID and application secret for generating an access token, which is used to access the API. Administrators create the applications, then give API users the application ID and application secret. Inventorying and managing CylanceON-PREM's associated custom applications and API endpoints is critical for securing the environment, ensuring compliance, minimizing risks, maintaining operational efficiency, and improving incident response. By knowing what applications and APIs exist and how they function, organizations can enhance the ability to protect, monitor, and manage systems effectively, thus safeguarding sensitive data and improving overall security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Console Applications. Administrator privileges are required. 1. Log in to the admin console. 2. Navigate to Configuration >> Applications. 3. Review the documentation of allowed applications. 4. Review the internal documentation for the location and protection of application ID and application secret. 5. All APIs must be documented. 6. Verify that controls are in place for who has access to APIs and where YAML files are stored. If any applications exist that are not documented, this is a finding. If application ID and application secrets are not documented and stored in the authorized location, this is a finding. If any APIs are in use and not documented, this is a finding. If the location and access of YAML files are not documented, this is a finding. If any of the above is documented but not adhered to, this is a finding.

