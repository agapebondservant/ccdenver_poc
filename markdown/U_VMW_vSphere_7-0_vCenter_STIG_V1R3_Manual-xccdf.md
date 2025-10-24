# STIG Benchmark: VMware vSphere 7.0 vCenter Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000014

**Group ID:** `V-256318`

### Rule: The vCenter Server must use TLS 1.2, at a minimum, to protect the confidentiality of sensitive data during electronic dissemination using remote access.

**Rule ID:** `SV-256318r919041_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Using older unauthorized versions or incorrectly configuring protocol negotiation makes the gateway vulnerable to known and unknown attacks that exploit vulnerabilities in this protocol. Satisfies: SRG-APP-000014, SRG-APP-000645, SRG-APP-000156, SRG-APP-000157, SRG-APP-000219, SRG-APP-000439, SRG-APP-000440, SRG-APP-000441, SRG-APP-000442, SRG-APP-000560, SRG-APP-000565, SRG-APP-000625</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt on the vCenter Server Appliance, run the following command: # /usr/lib/vmware-TlsReconfigurator/VcTlsReconfigurator/reconfigureVc scan If the output indicates versions of TLS other than 1.2 are enabled, this is a finding.

## Group: SRG-APP-000065

**Group ID:** `V-256319`

### Rule: The vCenter Server must enforce the limit of three consecutive invalid login attempts by a user.

**Rule ID:** `SV-256319r885568_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Administration >> Single Sign On >> Configuration >> Local Accounts >> Lockout Policy. The lockout policy should be set as follows: Maximum number of failed login attempts: 3 If this account lockout policy is not configured as stated, this is a finding.

## Group: SRG-APP-000068

**Group ID:** `V-256320`

### Rule: The vCenter Server must display the Standard Mandatory DOD Notice and Consent Banner before login.

**Rule ID:** `SV-256320r885571_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DOD-approved use notification before granting access to the application ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with DTM-08-060. Use the following verbiage for applications that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read (literal ampersand) consent to terms in IS user agreem't." Satisfies: SRG-APP-000068, SRG-APP-000069, SRG-APP-000070</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Administration >> Single Sign On >> Configuration >> Login Message. If the selection box next to "Show login message" is disabled, "Details of login message" is not configured to the standard DOD User Agreement, or the "Consent checkbox" is disabled, this is a finding. Note: Refer to vulnerability discussion for user agreement language.

## Group: SRG-APP-000095

**Group ID:** `V-256321`

### Rule: The vCenter Server must produce audit records containing information to establish what type of events occurred.

**Rule ID:** `SV-256321r885574_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what types of events occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Host and Clusters. Select a vCenter Server >> Configure >> Settings >> Advanced Settings. Verify the "config.log.level" value is set to "info". or From a PowerCLI command prompt while connected to the vCenter server, run the following command: Get-AdvancedSetting -Entity <vcenter server name> -Name config.log.level and verify it is set to "info". If the "config.log.level" value is not set to "info" or does not exist, this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-256322`

### Rule: vCenter Server plugins must be verified.

**Rule ID:** `SV-256322r885577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The vCenter Server includes a vSphere Client extensibility framework, which provides the ability to extend the vSphere Client with menu selections or toolbar icons that provide access to vCenter Server add-on components or external, web-based functionality. vSphere Client plugins or extensions run at the same privilege level as the user. Malicious extensions might masquerade as useful add-ons while compromising the system by stealing credentials or incorrectly configuring the system. Additionally, vCenter comes with a number of plugins preinstalled that may or may not be necessary for proper operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Administration >> Solutions >> Client Plug-Ins. View the Installed/Available Plug-ins list and verify they are all identified as authorized VMware, third-party (partner), and/or site-specific approved plug-ins. If any installed/available plug-ins in the viewable list cannot be verified as allowed vSphere Client plug-ins from trusted sources or are not in active use, this is a finding.

## Group: SRG-APP-000148

**Group ID:** `V-256323`

### Rule: The vCenter Server must uniquely identify and authenticate users or processes acting on behalf of users.

**Rule ID:** `SV-256323r885580_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses except the following. (i) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and (ii) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. Using Active Directory or an identity provider for authentication provides more robust account management capabilities and accountability. Satisfies: SRG-APP-000148, SRG-APP-000153, SRG-APP-000163, SRG-APP-000180, SRG-APP-000234</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Web Client, go to Administration >> Single Sign On >> Configuration >> Identity Provider. If the identity provider type is "embedded" and there is no identity source of type "Active Directory" (either Windows Integrated Authentication or LDAP), this is a finding. If the identity provider type is "Microsoft ADFS" or another supported identity provider, this is NOT a finding.

## Group: SRG-APP-000149

**Group ID:** `V-256324`

### Rule: The vCenter Server must require multifactor authentication.

**Rule ID:** `SV-256324r885583_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: (i) something a user knows (e.g., password/PIN); (ii) something a user has (e.g., cryptographic identification device, token); or (iii) something a user is (e.g., biometric). Satisfies: SRG-APP-000149, SRG-APP-000080, SRG-APP-000150, SRG-APP-000391, SRG-APP-000402</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Web Client, go to Administration >> Single Sign On >> Configuration >> Identity Provider. If the embedded identity provider is used, click on "Smart Card Authentication". If the embedded identity provider is used and "Smart Card Authentication" is not enabled, this is a finding. If a third-party identity provider is used, such as Microsoft ADFS, and it does not require multifactor authentication to log on to vCenter, this is a finding.

## Group: SRG-APP-000164

**Group ID:** `V-256325`

### Rule: The vCenter Server passwords must be at least 15 characters in length.

**Rule ID:** `SV-256325r885586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Administration >> Single Sign On >> Configuration >> Local Accounts >> Password Policy. The following password requirement should be set with at least the stated value: Minimum Length: 15 If this password policy is not configured as stated, this is a finding.

## Group: SRG-APP-000165

**Group ID:** `V-256326`

### Rule: The vCenter Server must prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-256326r885589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. To meet password policy requirements, passwords must be changed at specific policy-based intervals. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the result is a password that is not changed per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Administration >> Single Sign On >> Configuration >> Local Accounts >> Password Policy. View the value of the "Restrict reuse" setting. If the "Restrict reuse" policy is not set to "5" or more, this is a finding.

## Group: SRG-APP-000166

**Group ID:** `V-256327`

### Rule: The vCenter Server passwords must contain at least one uppercase character.

**Rule ID:** `SV-256327r885592_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Administration >> Single Sign On >> Configuration >> Local Accounts >> Password Policy. Set the following password requirement with at least the stated value: Upper-case Characters: At least 1 If this password complexity policy is not configured as stated, this is a finding.

## Group: SRG-APP-000167

**Group ID:** `V-256328`

### Rule: The vCenter Server passwords must contain at least one lowercase character.

**Rule ID:** `SV-256328r885595_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Administration >> Single Sign On >> Configuration >> Local Accounts >> Password Policy. Set the following password requirement with at least the stated value: Lower-case Characters: At least 1 If this password complexity policy is not configured as stated, this is a finding.

## Group: SRG-APP-000168

**Group ID:** `V-256329`

### Rule: The vCenter Server passwords must contain at least one numeric character.

**Rule ID:** `SV-256329r885598_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Administration >> Single Sign On >> Configuration >> Local Accounts >> Password Policy. Set the following password requirement with at least the stated value: Numeric Characters: At least 1 If this password complexity policy is not configured as stated, this is a finding.

## Group: SRG-APP-000169

**Group ID:** `V-256330`

### Rule: The vCenter Server passwords must contain at least one special character.

**Rule ID:** `SV-256330r885601_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor in determining how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Special characters are not alphanumeric. Examples include: ~ ! @ # $ % ^ *.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Administration >> Single Sign On >> Configuration >> Local Accounts >> Password Policy. Set the following password requirements with at least the stated value: Special Characters: At least 1 If this password complexity policy is not configured as stated, this is a finding.

## Group: SRG-APP-000172

**Group ID:** `V-256331`

### Rule: The vCenter Server must enable FIPS-validated cryptography.

**Rule ID:** `SV-256331r885604_rule`
**Severity:** high

**Description:**
<VulnDiscussion>FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules use authentication that meets DOD requirements. In vSphere 6.7 and later, ESXi and vCenter Server use FIPS-validated cryptography to protect management interfaces and the VMware Certificate Authority (VMCA). vSphere 7.0 Update 2 and later adds additional FIPS-validated cryptography to vCenter Server Appliance. By default, this FIPS validation option is disabled and must be enabled. Satisfies: SRG-APP-000172, SRG-APP-000179, SRG-APP-000224, SRG-APP-000231, SRG-APP-000412, SRG-APP-000514, SRG-APP-000555, SRG-APP-000600, SRG-APP-000610, SRG-APP-000620, SRG-APP-000630, SRG-APP-000635</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Web Client, go to Developer Center >> API Explorer. From the "Select API" drop-down menu, select appliance. Expand system/security/global_fips >> GET. Click "Execute" and then "Copy Response"  to view the results. Example response: { "enabled": true } If global FIPS mode is not enabled, this is a finding.

## Group: SRG-APP-000174

**Group ID:** `V-256332`

### Rule: The vCenter Server must enforce a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-256332r885607_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords must be changed at specific intervals. One method of minimizing this risk is to use complex passwords and periodically change them. If the application does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the system and/or application passwords could be compromised. This requirement does not include emergency administration accounts, which are meant for access to the application in case of failure. These accounts are not required to have maximum password lifetime restrictions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Administration >> Single Sign On >> Configuration >> Local Accounts >> Password Policy. View the value of the "Maximum lifetime" setting. If the "Maximum lifetime" policy is not set to "60", this is a finding.

## Group: SRG-APP-000175

**Group ID:** `V-256333`

### Rule: The vCenter Server must enable revocation checking for certificate-based authentication.

**Rule ID:** `SV-256333r919043_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The system must establish the validity of the user-supplied identity certificate using Online Certificate Status Protocol (OCSP) and/or Certificate Revocation List (CRL) revocation checking. Satisfies: SRG-APP-000175, SRG-APP-000392, SRG-APP-000401, SRG-APP-000403</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If a federated identity provider is configured and used for an identity source and supports Smartcard authentication, this is not applicable. From the vSphere Client, go to Administration >> Single Sign On >> Configuration >> Identity Provider >> Smart Card Authentication. Under Smart card authentication settings >> Certificate revocation, verify "Revocation check" does not show as disabled. If "Revocation check" shows as disabled, this is a finding.

## Group: SRG-APP-000190

**Group ID:** `V-256334`

### Rule: The vCenter Server must terminate vSphere Client sessions after 10 minutes of inactivity.

**Rule ID:** `SV-256334r885613_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free resources committed by the managed network element. Satisfies: SRG-APP-000190, SRG-APP-000295, SRG-APP-000389</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Administration >> Deployment >> Client Configuration. View the value of the "Session timeout" setting. If "Session timeout" is not set to "10 minute(s)" or below, this is a finding. Note: If vCenter is not 7.0 U2 or newer, this setting is not available through the UI and must be checked with the "session.timeout" setting in the "/etc/vmware/vsphere-ui/webclient.properties file".

## Group: SRG-APP-000211

**Group ID:** `V-256335`

### Rule: The vCenter Server users must have the correct roles assigned.

**Rule ID:** `SV-256335r885616_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Users and service accounts must only be assigned privileges they require. Least privilege requires that these privileges must only be assigned if needed to reduce risk of confidentiality, availability, or integrity loss. Satisfies: SRG-APP-000211, SRG-APP-000233, SRG-APP-000380</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Administration >> Access Control >> Roles. View each role and verify the users and/or groups assigned to it by clicking "Usage". or From a PowerCLI command prompt while connected to the vCenter server, run the following command: Get-VIPermission | Sort Role | Select Role,Principal,Entity,Propagate,IsGroup | FT -Auto Application service account and user required privileges should be documented. If any user or service account has more privileges than required, this is a finding.

## Group: SRG-APP-000247

**Group ID:** `V-256336`

### Rule: The vCenter Server must manage excess capacity, bandwidth, or other redundancy to limit the effects of information flooding types of denial-of-service (DoS) attacks by enabling Network I/O Control (NIOC).

**Rule ID:** `SV-256336r885619_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Managing excess capacity ensures sufficient capacity is available to counter flooding attacks. Employing increased capacity and service redundancy may reduce the susceptibility to some DoS attacks. Managing excess capacity may include, for example, establishing selected usage priorities, quotas, or partitioning.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If distributed switches are not used, this is not applicable. From the vSphere Client, go to Networking. Select a distributed switch >> Configure >> Settings >> Properties. View the "Properties" pane and verify "Network I/O Control" is "Enabled". or From a PowerCLI command prompt while connected to the vCenter server, run the following command: Get-VDSwitch | select Name,@{N="NIOC Enabled";E={$_.ExtensionData.config.NetworkResourceManagementEnabled}} If "Network I/O Control" is disabled, this is a finding.

## Group: SRG-APP-000291

**Group ID:** `V-256337`

### Rule: The vCenter Server must provide an immediate real-time alert to the system administrator (SA) and information system security officer (ISSO), at a minimum, on every Single Sign-On (SSO) account action.

**Rule ID:** `SV-256337r885622_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, they often attempt to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create a new account. They may also try to hijack an existing account by changing a password or enabling a previously disabled account. Therefore, all actions performed on accounts in the SSO domain much be alerted on in vCenter at a minimum and ideally on a Security Information and Event Management (SIEM) system as well. To ensure the appropriate personnel are alerted about SSO account actions, create a new vCenter alarm for the "com.vmware.sso.PrincipalManagement" event ID and configure the alert mechanisms appropriately. Satisfies: SRG-APP-000291, SRG-APP-000292, SRG-APP-000293, SRG-APP-000294, SRG-APP-000320</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Host and Clusters. Select a vCenter Server >> Configure >> Security >> Alarm Definitions. Verify an alarm has been created to alert upon all SSO account actions. The alarm name may vary, but it is suggested to name it "SSO account actions - com.vmware.sso.PrincipalManagement". or From a PowerCLI command prompt while connected to the vCenter server, run the following command: Get-AlarmDefinition | Where {$_.ExtensionData.Info.Expression.Expression.EventTypeId -eq "com.vmware.sso.PrincipalManagement"} | Select Name,Enabled,@{N="EventTypeId";E={$_.ExtensionData.Info.Expression.Expression.EventTypeId}} If an alarm is not created to alert on SSO account actions, this is a finding.

## Group: SRG-APP-000345

**Group ID:** `V-256338`

### Rule: The vCenter Server must set the interval for counting failed login attempts to at least 15 minutes.

**Rule ID:** `SV-256338r885625_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Administration >> Single Sign On >> Configuration >> Local Accounts >> Lockout Policy. Verify the following lockout policy is set as follows: Time interval between failures: 900 seconds If this lockout policy is not configured as stated, this is a finding.

## Group: SRG-APP-000358

**Group ID:** `V-256339`

### Rule: The vCenter Server must be configured to send logs to a central log server.

**Rule ID:** `SV-256339r885628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>vCenter must be configured to send near real-time log data to syslog collectors so information will be available to investigators in the case of a security incident or to assist in troubleshooting.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Virtual Appliance Management Interface (VAMI) by navigating to https://<vCenter server>:5480. Log in with local operating system administrative credentials or with a Single Sign-On (SSO) account that is a member of the "SystemConfiguration.BashShellAdministrator" group. Select "Syslog" on the left navigation pane. On the resulting pane on the right, verify at least one site-specific syslog receiver is configured and is listed as "Reachable". If no valid syslog collector is configured or if the collector is not listed as "Reachable", this is a finding.

## Group: SRG-APP-000360

**Group ID:** `V-256340`

### Rule: vCenter must provide an immediate real-time alert to the system administrator (SA) and information system security officer (ISSO), at a minimum, of all audit failure events requiring real-time alerts.

**Rule ID:** `SV-256340r885631_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less). Satisfies: SRG-APP-000360, SRG-APP-000379, SRG-APP-000510</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Central Logging Server being used to verify it is configured to alert the SA and ISSO, at a minimum, on any AO-defined events. Otherwise, this is a finding. If there are no AO-defined events, this is not a finding.

## Group: SRG-APP-000371

**Group ID:** `V-256341`

### Rule: The vCenter Server must compare internal information system clocks at least every 24 hours with an authoritative time server.

**Rule ID:** `SV-256341r892804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside of the configured acceptable allowance (drift) may be inaccurate. Additionally, unnecessary synchronization may have an adverse impact on system performance and may indicate malicious activity. Synchronizing internal information system clocks to an authoritative time server provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Virtual Appliance Management Interface (VAMI) by navigating to https://<vCenter server>:5480. Log in with local operating system administrative credentials or with a Single Sign-On (SSO) account that is a member of the "SystemConfiguration.BashShellAdministrator" group. Select "Time" on the left navigation pane. On the resulting pane on the right, verify at least one authorized time server is configured and is listed as "Reachable". If "NTP" is not enabled and at least one authorized time server configured, this is a finding.

## Group: SRG-APP-000427

**Group ID:** `V-256342`

### Rule: The vCenter Server Machine Secure Sockets Layer (SSL) certificate must be issued by a DOD certificate authority.

**Rule ID:** `SV-256342r885637_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted certificate authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DOD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DOD-approved CA, trust of this CA has not been established. The DOD will only accept public key infrastructure (PKI) certificates obtained from a DOD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of Transport Layer Security (TLS) certificates. The default self-signed, VMware Certificate Authority (VMCA)-issued vCenter reverse proxy certificate must be replaced with a DOD-approved certificate. The use of a DOD certificate on the vCenter reverse proxy and other services assures clients that the service they are connecting to is legitimate and trusted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Administration >> Certificates >> Certificate Management >> Machine SSL Certificate. Click "View Details" and examine the "Issuer Information" block. If the issuer specified is not a DOD-approved certificate authority, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256343`

### Rule: The vCenter Server must disable the Customer Experience Improvement Program (CEIP).

**Rule ID:** `SV-256343r885640_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The VMware CEIP sends VMware anonymized system information that is used to improve the quality, reliability, and functionality of VMware products and services. For confidentiality purposes this feature must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Administration >> Deployment >> Customer Experience Improvement Program. If Customer Experience Improvement "Program Status" is "Joined", this is a finding.

## Group: SRG-APP-000575

**Group ID:** `V-256344`

### Rule: The vCenter server must enforce SNMPv3 security features where SNMP is required.

**Rule ID:** `SV-256344r885643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SNMPv3 supports commercial-grade security, including authentication, authorization, access control, and privacy. Previous versions of the protocol contained well-known security weaknesses that were easily exploited. SNMPv3 can be configured for identification and cryptographically based authentication. SNMPv3 defines a user-based security model (USM) and a view-based access control model (VACM). SNMPv3 USM provides data integrity, data origin authentication, message replay protection, and protection against disclosure of the message payload. SNMPv3 VACM provides access control to determine whether a specific type of access (read or write) to the management information is allowed. Implement both VACM and USM for full protection. SNMPv3 must be disabled by default and enabled only if used. SNMP v3 provides security feature enhancements to SNMP, including encryption and message authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt on the vCenter Server Appliance, run the following commands: # appliancesh # snmp.get Note: The "appliancesh" command is not needed if the default shell has not been changed for root. If "Enable" is set to "False", this is not a finding. If "Enable" is set to "True" and "Authentication" is not set to "SHA1", this is a finding. If "Enable" is set to "True" and "Privacy" is not set to "AES128", this is a finding. If any "Users" are configured with a "Sec_level" that does not equal "priv", this is a finding.

## Group: SRG-APP-000575

**Group ID:** `V-256345`

### Rule: The vCenter server must disable SNMPv1/2 receivers.

**Rule ID:** `SV-256345r885646_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SNMPv3 supports commercial-grade security, including authentication, authorization, access control, and privacy. Previous versions of the protocol contained well-known security weaknesses that were easily exploited. Therefore, SNMPv1/2 receivers must be disabled, while SNMPv3 is configured in another control. vCenter exposes SNMP v1/2 in the UI and SNMPv3 in the CLI.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Host and Clusters. Select a vCenter Server >> Configure >> Settings >> General. Click "Edit". On the "SNMP receivers" tab, note the presence of any enabled receiver. If there are any enabled receivers, this is a finding.

## Group: SRG-APP-000345

**Group ID:** `V-256346`

### Rule: The vCenter Server must require an administrator to unlock an account locked due to excessive login failures.

**Rule ID:** `SV-256346r885649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By requiring that Single Sign-On (SSO) accounts be unlocked manually, the risk of unauthorized access via user password guessing, otherwise known as brute forcing, is reduced. When the account unlock time is set to zero, once an account is locked it can only be unlocked manually by an administrator.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Administration >> Single Sign On >> Configuration >> Local Accounts >> Lockout Policy. Verify the following lockout policy is set as follows: Unlock time: 0 If this account lockout policy is not configured as stated, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256347`

### Rule: The vCenter Server must disable the distributed virtual switch health check.

**Rule ID:** `SV-256347r885652_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Network health check is disabled by default. Once enabled, the health check packets contain information on host#, vds#, and port#, which an attacker would find useful. It is recommended that network health check be used for troubleshooting and turned off when troubleshooting is finished.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If distributed switches are not used, this is not applicable. From the vSphere Client, go to "Networking". Select a distributed switch >> Configure >> Settings >> Health Check. View the health check pane and verify the "VLAN and MTU" and "Teaming and failover" checks are "Disabled". or From a PowerCLI command prompt while connected to the vCenter server, run the following commands: $vds = Get-VDSwitch $vds.ExtensionData.Config.HealthCheckConfig If the health check feature is enabled on distributed switches and is not on temporarily for troubleshooting purposes, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256348`

### Rule: The vCenter Server must set the distributed port group Forged Transmits policy to "Reject".

**Rule ID:** `SV-256348r942488_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the virtual machine operating system changes the Media Access Control (MAC) address, the operating system can send frames with an impersonated source MAC address at any time. This allows an operating system to stage malicious attacks on the devices in a network by impersonating a network adaptor authorized by the receiving network. When the "Forged Transmits" option is set to "Accept", ESXi does not compare source and effective MAC addresses. To protect against MAC impersonation, set the "Forged Transmits" option to "Reject". The host compares the source MAC address being transmitted by the guest operating system with the effective MAC address for its virtual machine adapter to determine if they match. If the addresses do not match, the ESXi host drops the packet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If distributed switches are not used, this is not applicable. From the vSphere Client, go to "Networking". Select a distributed switch and then select a port group. Select Configure >> Settings >> Policies. Verify "Forged Transmits" is set to "Reject". or From a PowerCLI command prompt while connected to the vCenter server, run the following commands: Get-VDSwitch | Get-VDSecurityPolicy Get-VDPortgroup | ?{$_.IsUplink -eq $false} | Get-VDSecurityPolicy If the "Forged Transmits" policy is set to accept for a nonuplink port, and is not documented as an exception, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256349`

### Rule: The vCenter Server must set the distributed port group Media Access Control (MAC) Address Change policy to "Reject".

**Rule ID:** `SV-256349r885658_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the virtual machine operating system changes the MAC address, it can send frames with an impersonated source MAC address at any time. This allows it to stage malicious attacks on the devices in a network by impersonating a network adaptor authorized by the receiving network. This will prevent virtual machines from changing their effective MAC address and will affect applications that require this functionality. This will also affect how a layer 2 bridge will operate and will affect applications that require a specific MAC address for licensing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If distributed switches are not used, this is not applicable. From the vSphere Client, go to "Networking". Select a distributed switch and then select a port group. Select Configure >> Settings >> Policies. Verify "MAC Address Changes" is set to "Reject". or From a PowerCLI command prompt while connected to the vCenter server, run the following commands: Get-VDSwitch | Get-VDSecurityPolicy Get-VDPortgroup | ?{$_.IsUplink -eq $false} | Get-VDSecurityPolicy If the "MAC Address Changes" policy is set to "Accept", this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256350`

### Rule: The vCenter Server must set the distributed port group Promiscuous Mode policy to "Reject".

**Rule ID:** `SV-256350r942490_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When promiscuous mode is enabled for a virtual switch, all virtual machines connected to the port group have the potential of reading all packets across that network, meaning only the virtual machines connected to that port group. Promiscuous mode is disabled by default on the ESXi Server, and this is the recommended setting.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If distributed switches are not used, this is not applicable. From the vSphere Client, go to "Networking". Select a distributed switch and then select a port group. Select Configure >> Settings >> Policies. Verify "Promiscuous Mode" is set to "Reject". or From a PowerCLI command prompt while connected to the vCenter server, run the following commands: Get-VDSwitch | Get-VDSecurityPolicy Get-VDPortgroup | ?{$_.IsUplink -eq $false} | Get-VDSecurityPolicy If the "Promiscuous Mode" policy is set to "Accept", and is not documented as an exception, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256351`

### Rule: The vCenter Server must only send NetFlow traffic to authorized collectors.

**Rule ID:** `SV-256351r885664_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The distributed virtual switch can export NetFlow information about traffic crossing the switch. NetFlow exports are not encrypted and can contain information about the virtual network, making it easier for a man-in-the-middle attack to be executed successfully. If NetFlow export is required, verify that all NetFlow target Internet Protocols (IPs) are correct.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If distributed switches are not used, this is not applicable. To view NetFlow Collector IPs configured on distributed switches: From the vSphere Client, go to "Networking". Select a distributed switch >> Configure >> Settings >> NetFlow. View the NetFlow pane and verify any collector IP addresses are valid and in use for troubleshooting. or From a PowerCLI command prompt while connected to the vCenter server, run the following command: Get-VDSwitch | select Name,@{N="NetFlowCollectorIPs";E={$_.ExtensionData.config.IpfixConfig.CollectorIpAddress}} To view if NetFlow is enabled on any distributed port groups: From the vSphere Client, go to Networking. Select a distributed port group >> Manage >> Settings >> Policies. Go to "Monitoring" and view the NetFlow status. or From a PowerCLI command prompt while connected to the vCenter server, run the following command: Get-VDPortgroup | Select Name,VirtualSwitch,@{N="NetFlowEnabled";E={$_.Extensiondata.Config.defaultPortConfig.ipfixEnabled.Value}} If NetFlow is configured and the collector IP is not known and documented, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256352`

### Rule: The vCenter Server must configure all port groups to a value other than that of the native virtual local area network (VLAN).

**Rule ID:** `SV-256352r885667_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ESXi does not use the concept of native VLAN. Frames with VLAN specified in the port group will have a tag, but frames with VLAN not specified in the port group are not tagged and therefore will end up belonging to native VLAN of the physical switch. For example, frames on VLAN 1 from a Cisco physical switch will be untagged, because this is considered as the native VLAN. However, frames from ESXi specified as VLAN 1 will be tagged with a "1"; therefore, traffic from ESXi that is destined for the native VLAN will not be correctly routed (because it is tagged with a "1" instead of being untagged), and traffic from the physical switch coming from the native VLAN will not be visible (because it is not tagged). If the ESXi virtual switch port group uses the native VLAN ID, traffic from those virtual machines will not be visible to the native VLAN on the switch, because the switch is expecting untagged traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If distributed switches are not used, this is not applicable. From the vSphere Client, go to "Networking". Select a distributed switch >> distributed port group >> Configure >> Settings >> Policies. Review the port group VLAN tags and verify they are not set to the native VLAN ID of the attached physical switch. or From a PowerCLI command prompt while connected to the vCenter server, run the following command: Get-VDPortgroup | select Name, VlanConfiguration If any port group is configured with the native VLAN of the ESXi host's attached physical switch, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256353`

### Rule: The vCenter Server must not configure VLAN Trunking unless Virtual Guest Tagging (VGT) is required and authorized.

**Rule ID:** `SV-256353r885670_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a port group is set to VLAN Trunking, the vSwitch passes all network frames in the specified range to the attached virtual machines without modifying the virtual local area network (VLAN) tags. In vSphere, this is referred to as VGT. The virtual machine must process the VLAN information itself via an 802.1Q driver in the operating system. VLAN Trunking must only be implemented if the attached virtual machines have been specifically authorized and are capable of managing VLAN tags themselves. If VLAN Trunking is enabled inappropriately, it may cause a denial of service or allow a virtual machine to interact with traffic on an unauthorized VLAN.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If distributed switches are not used, this is not applicable. From the vSphere Client, go to "Networking". Select a distributed switch >> distributed port group >> Configure >> Settings >> Policies. Review the port group "VLAN Type" and "VLAN trunk range", if present. or From a PowerCLI command prompt while connected to the vCenter server, run the following command: Get-VDPortgroup | Where {$_.ExtensionData.Config.Uplink -ne "True"} | Select Name,VlanConfiguration If any port group is configured with "VLAN trunking" and is not documented as a needed exception (such as NSX appliances), this is a finding. If any port group is authorized to be configured with "VLAN trunking" but is not configured with the most limited range necessary, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256354`

### Rule: The vCenter Server must not configure all port groups to virtual local area network (VLAN) values reserved by upstream physical switches.

**Rule ID:** `SV-256354r885673_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Certain physical switches reserve certain VLAN IDs for internal purposes and often disallow traffic configured to these values. For example, Cisco Catalyst switches typically reserve VLANs 1001 to 1024 and 4094, while Nexus switches typically reserve 3968 to 4094. Check with the documentation for the organization's specific switch. Using a reserved VLAN might result in a denial of service on the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If distributed switches are not used, this is not applicable. From the vSphere Client, go to Networking. Select a distributed switch >> distributed port group >> Configure >> Settings >> Policies. Review the port group VLAN tags and verify they are not set to a reserved VLAN ID. or From a PowerCLI command prompt while connected to the vCenter server, run the following command: Get-VDPortgroup | select Name, VlanConfiguration If any port group is configured with a reserved VLAN ID, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256355`

### Rule: The vCenter Server must configure the "vpxuser" auto-password to be changed every 30 days.

**Rule ID:** `SV-256355r885676_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, vCenter will change the "vpxuser" password automatically every 30 days. Ensure this setting meets site policies. If it does not, configure it to meet password aging policies. Note: It is very important the password aging policy is not shorter than the default interval that is set to automatically change the "vpxuser" password to preclude the possibility that vCenter might be locked out of an ESXi host.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Host and Clusters. Select a vCenter Server >> Configure >> Settings >> Advanced Settings. Verify "VirtualCenter.VimPasswordExpirationInDays" is set to "30". or From a PowerCLI command prompt while connected to the vCenter server, run the following command: Get-AdvancedSetting -Entity <vcenter server name> -Name VirtualCenter.VimPasswordExpirationInDays If the "VirtualCenter.VimPasswordExpirationInDays" is set to a value other than "30" or does not exist, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256356`

### Rule: The vCenter Server must configure the "vpxuser" password to meet length policy.

**Rule ID:** `SV-256356r885679_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "vpxuser" password default length is 32 characters. Ensure this setting meets site policies; if not, configure to meet password length policies. Longer passwords make brute-force password attacks more difficult. The "vpxuser" password is added by vCenter, meaning no manual intervention is normally required. The "vpxuser" password length must never be modified to less than the default length of 32 characters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Host and Clusters. Select a vCenter Server >> Configure >> Settings >> Advanced Settings. Verify "config.vpxd.hostPasswordLength" is set to "32". or From a PowerCLI command prompt while connected to the vCenter server, run the following command: Get-AdvancedSetting -Entity <vcenter server name> -Name config.vpxd.hostPasswordLength and verify it is set to 32. If the "config.vpxd.hostPasswordLength" is set to a value other than "32", this is a finding. If the setting does not exist, this is not a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256357`

### Rule: The vCenter Server must be isolated from the public internet but must still allow for patch notification and delivery.

**Rule ID:** `SV-256357r885682_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>vCenter and the embedded Lifecycle Manager system must never have a direct route to the internet. Despite this, updates and patches sourced from VMware on the internet must be delivered in a timely manner. There are two methods to accomplish this: a proxy server and the Update Manager Download Service (UMDS). UMDS is an optional module for Lifecycle Manager that fetches upgrades for virtual appliances, patch metadata, patch binaries, and notifications that would not otherwise be available to an isolated Lifecycle Manager directly. Alternatively, a proxy for Lifecycle Manager can be configured to allow controlled, limited access to the public internet for the sole purpose of patch gathering. Either solution mitigates the risk of internet connectivity by limiting its scope and use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the following conditions: 1. Lifecycle Manager must be configured to use the UMDS. OR 2. Lifecycle Manager must be configured to use a proxy server for access to VMware patch repositories. OR 3. Lifecycle Manager must disable internet patch repositories and any patches must be manually validated and imported as needed. Option 1: From the vSphere Client, go to Lifecycle Manager >> Settings >> Patch Setup. Click the "Change Download Source" button. Verify the "Download patches from a UMDS shared repository" radio button is selected and a valid UMDS repository is supplied. Click "Cancel". If this is not set, this is a finding. Option 2: From the vSphere Client, go to Lifecycle Manager >> Settings >> Patch Setup. Click the "Change Download Source" button. Verify the "Download patches directly from the internet" radio button is selected. Click "Cancel". Navigate to the vCenter Server Management interface at https://<vcenter dns>:5480 >> Networking >> Proxy Settings. Verify "HTTPS" is "Enabled". Click the "HTTPS" row. Verify the proxy server configuration is accurate. If this is not set, this is a finding. Option 3: From the vSphere Client, go to Lifecycle Manager >> Settings >> Patch Downloads. Verify the "Automatic downloads" option is disabled. From the vSphere Client, go to Lifecycle Manager >> Settings >> Patch Setup. Verify any download sources are disabled. If this is not set, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256358`

### Rule: The vCenter Server must use unique service accounts when applications connect to vCenter.

**Rule ID:** `SV-256358r885685_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To not violate nonrepudiation (i.e., deny the authenticity of who is connecting to vCenter), when applications need to connect to vCenter they must use unique service accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify each external application that connects to vCenter has a unique service account dedicated to that application. For example, there should be separate accounts for Log Insight, Operations Manager, or anything else that requires an account to access vCenter. If any application shares a service account that is used to connect to vCenter, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256359`

### Rule: The vCenter Server must protect the confidentiality and integrity of transmitted information by isolating Internet Protocol (IP)-based storage traffic.

**Rule ID:** `SV-256359r885688_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Virtual machines might share virtual switches and virtual local area networks (VLAN) with the IP-based storage configurations. IP-based storage includes vSAN, Internet Small Computer System Interface (iSCSI), and Network File System (NFS). This configuration might expose IP-based storage traffic to unauthorized virtual machine users. IP-based storage frequently is not encrypted. It can be viewed by anyone with access to this network. To restrict unauthorized users from viewing the IP-based storage traffic, the IP-based storage network must be logically separated from the production traffic. Configuring the IP-based storage adaptors on separate VLANs or network segments from other VMkernels and virtual machines will limit unauthorized users from viewing the traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If IP-based storage is not used, this is not applicable. IP-based storage (iSCSI, NFS, vSAN) VMkernel port groups must be in a dedicated VLAN that can be on a standard or distributed virtual switch that is logically separated from other traffic types. The check for this will be unique per environment. To check a standard switch, from the vSphere Client, select the ESXi host and go to Configure >> Networking >> Virtual switches. Select a standard switch. For each storage port group (iSCSI, NFS, vSAN), select the port group and note the VLAN ID associated with each port group. Verify it is dedicated to that purpose and is logically separated from other traffic types. To check a distributed switch, from the vSphere Client, go to "Networking" and select and expand a distributed switch. For each storage port group (iSCSI, NFS, vSAN), select the port group and navigate to the "Summary" tab. Note the VLAN ID associated with each port group and verify it is dedicated to that purpose and is logically separated from other traffic types. If any IP-based storage networks are not isolated from other traffic types, this is a finding.

## Group: SRG-APP-000358

**Group ID:** `V-256360`

### Rule: The vCenter server must be configured to send events to a central log server.

**Rule ID:** `SV-256360r885691_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>vCenter server generates volumes of security-relevant application-level events. Examples include logins, system reconfigurations, system degradation warnings, and more. To ensure these events are available for forensic analysis and correlation, they must be sent to the syslog and forwarded on to the configured Security Information and Event Management (SIEM) system and/or central log server. The vCenter server sends events to syslog by default, but this configuration must be verified and maintained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Host and Clusters. Select a vCenter Server >> Configure >> Settings >> Advanced Settings. Verify the "vpxd.event.syslog.enabled" value is set to "true". or From a PowerCLI command prompt while connected to the vCenter server, run the following command: Get-AdvancedSetting -Entity <vcenter server name> -Name vpxd.event.syslog.enabled If the "vpxd.event.syslog.enabled" value is not set to "true", this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256361`

### Rule: The vCenter Server must disable or restrict the connectivity between vSAN Health Check and public Hardware Compatibility List (HCL) by use of an external proxy server.

**Rule ID:** `SV-256361r885694_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The vSAN Health Check is able to download the HCL from VMware to check compliance against the underlying vSAN Cluster hosts. To ensure the vCenter server is not directly downloading content from the internet, this functionality must be disabled. If this feature is necessary, an external proxy server must be configured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If no clusters are enabled for vSAN, this is not applicable. From the vSphere Client, go to Host and Clusters. Select the vCenter Server >> Configure >> vSAN >> Internet Connectivity. If the HCL internet download is not required, verify "Status" is "Disabled". If the "Status" is "Enabled", this is a finding. If the HCL internet download is required, verify "Status" is "Enabled" and a proxy host is configured. If "Status" is "Enabled" and a proxy is not configured, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256362`

### Rule: The vCenter Server must configure the vSAN Datastore name to a unique name.

**Rule ID:** `SV-256362r885697_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A vSAN Datastore name by default is "vsanDatastore". If more than one vSAN cluster is present in vCenter, both datastores will have the same name by default, potentially leading to confusion and manually misplaced workloads.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If no clusters are enabled for vSAN, this is not applicable. From the vSphere Client, go to Host and Clusters. Select a vSAN Enabled Cluster >> Datastores. Review the datastores and identify any datastores with "vSAN" as the datastore type. or From a PowerCLI command prompt while connected to the vCenter server, run the following commands: If($(Get-Cluster | where {$_.VsanEnabled} | Measure).Count -gt 0){ Write-Host "vSAN Enabled Cluster found" Get-Cluster | where {$_.VsanEnabled} | Get-Datastore | where {$_.type -match "vsan"} } else{ Write-Host "vSAN is not enabled, this finding is not applicable" } If vSAN is enabled and a datastore is named "vsanDatastore", this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256363`

### Rule: The vCenter Server must disable Username/Password and Windows Integrated Authentication.

**Rule ID:** `SV-256363r885700_rule`
**Severity:** low

**Description:**
<VulnDiscussion>All forms of authentication other than Common Access Card (CAC) must be disabled. Password authentication can be temporarily reenabled for emergency access to the local Single Sign-On (SSO) accounts or Active Directory user/pass accounts, but it must be disabled as soon as CAC authentication is functional.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If a federated identity provider is configured and used for an identity source, this is not applicable. From the vSphere Client, go to Administration >> Single Sign On >> Configuration >> Identity Provider >> Smart Card Authentication. Under "Authentication method", examine the allowed methods. If "Smart card authentication" is not enabled and "Password and windows session authentication" is not disabled , this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256364`

### Rule: The vCenter Server must restrict access to the default roles with cryptographic permissions.

**Rule ID:** `SV-256364r919045_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In vSphere, a number of default roles contain permission to perform cryptographic operations such as Key Management Server (KMS) functions and encrypting and decrypting virtual machine disks. These roles must be reserved for cryptographic administrators where virtual machine encryption and/or vSAN encryption is in use. A new built-in role called "No Cryptography Administrator" exists to provide all administrative permissions except cryptographic operations. Permissions must be restricted such that normal vSphere administrators are assigned the "No Cryptography Administrator" role or more restrictive. These default roles must be tightly controlled and must not be applied to administrators who will not be doing cryptographic work. Catastrophic data loss can result from poorly administered cryptography.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
By default, there are four roles that contain cryptographic-related permissions: Administrator, No Trusted Infrastructure Administrator, vCLSAdmin, and vSphere Kubernetes Manager. From the vSphere Client, go to Administration >> Access Control >> Roles. or From a PowerCLI command prompt while connected to the vCenter server, run the following command: Get-VIPermission | Where {$_.Role -eq "Admin" -or $_.Role -eq "NoTrustedAdmin" -or $_.Role -eq "vCLSAdmin" -or $_.Role -eq "vSphereKubernetesManager"} | Select Role,Principal,Entity,Propagate,IsGroup | FT -Auto If there are any users or groups assigned to the default roles with cryptographic permissions and are not explicitly designated to perform cryptographic operations, this is a finding. The built-in solution users assigned to the administrator role are NOT a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256365`

### Rule: The vCenter Server must restrict access to cryptographic permissions.

**Rule ID:** `SV-256365r919040_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>These permissions must be reserved for cryptographic administrators where virtual machine encryption and/or vSAN encryption is in use. Catastrophic data loss can result from poorly administered cryptography.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
By default, there are four roles that contain cryptographic-related permissions: Administrator, No Trusted Infrastructure Administrator, vCLSAdmin, and vSphere Kubernetes Manager. From the vSphere Client, go to Administration >> Access Control >> Roles. Highlight each role and click the 'Privileges" button in the right pane. Verify that only the Administrator, No Trusted Infrastructure Administrator, vCLSAdmin, and vSphere Kubernetes Manager and any site-specific cryptographic roles have the following permissions: Cryptographic Operations privileges Global.Diagnostics Host.Inventory.Add host to cluster Host.Inventory.Add standalone host Host.Local operations.Manage user groups or From a PowerCLI command prompt while connected to the vCenter server, run the following commands: $roles = Get-VIRole ForEach($role in $roles){ $privileges = $role.PrivilegeList If($privileges -match "Crypto*" -or $privileges -match "Global.Diagnostics" -or $privileges -match "Host.Inventory.Add*" -or $privileges -match "Host.Local operations.Manage user groups"){ Write-Host "$role has Cryptographic privileges" } } If any role other than the four default roles contain the permissions listed above and is not authorized to perform cryptographic-related operations, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256366`

### Rule: The vCenter Server must have Mutual Challenge Handshake Authentication Protocol (CHAP) configured for vSAN Internet Small Computer System Interface (iSCSI) targets.

**Rule ID:** `SV-256366r885709_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When enabled, vSphere performs bidirectional authentication of both the iSCSI target and host. When not authenticating both the iSCSI target and host, the potential exists for a man-in-the-middle attack in which an attacker might impersonate either side of the connection to steal data. Bidirectional authentication mitigates this risk.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If no clusters are enabled for vSAN or if vSAN is enabled but iSCSI is not enabled, this is not applicable. From the vSphere Client, go to Host and Clusters. Select a vSAN Enabled Cluster >> Configure >> vSAN >> iSCSI Target Service. For each iSCSI target, review the value in the "Authentication" column. If the Authentication method is not set to "CHAP_Mutual" for any iSCSI target, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256367`

### Rule: The vCenter Server must have new Key Encryption Keys (KEKs) reissued at regular intervals for vSAN encrypted datastore(s).

**Rule ID:** `SV-256367r885712_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The KEK for a vSAN encrypted datastore is generated by the Key Management Server (KMS) and serves as a wrapper and lock around the Disk Encryption Key (DEK). The DEK is generated by the host and is used to encrypt and decrypt the datastore. A shallow rekey is a procedure in which the KMS issues a new KEK to the ESXi host, which rewraps the DEK but does not change the DEK or any data on disk. This operation must be done on a regular, site-defined interval and can be viewed as similar in criticality to changing an administrative password. If the KMS is compromised, a standing operational procedure to rekey will put a time limit on the usefulness of any stolen KMS data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If vSAN is not in use, this is not applicable. Interview the system administrator (SA) to determine that a procedure has been put in place to perform a shallow rekey of all vSAN encrypted datastores at regular, site-defined intervals. VMware recommends a 60-day rekey task, but this interval must be defined by the SA and the information system security officer (ISSO). If vSAN encryption is not in use, this is not a finding. If vSAN encryption is in use and a regular rekey procedure is not in place, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256368`

### Rule: The vCenter Server must use secure Lightweight Directory Access Protocol (LDAPS) when adding an LDAP identity source.

**Rule ID:** `SV-256368r885715_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LDAP is an industry standard protocol for querying directory services such as Active Directory. This protocol can operate in clear text or over a Secure Sockets Layer (SSL)/Transport Layer Security (TLS) encrypted tunnel. To protect confidentiality of LDAP communications, secure LDAP (LDAPS) must be explicitly configured when adding an LDAP identity source in vSphere Single Sign-On (SSO). When configuring an identity source and supplying an SSL certificate, vCenter will enforce LDAPS. The server URLs do not need to be explicitly provided if an SSL certificate is uploaded.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If LDAP is not used as an identity provider, this is not applicable. From the vSphere Client, go to Administration >> Single Sign On >> Configuration >> Identity Provider. Click the "Identity Sources" tab. For each identity source of type "Active Directory over LDAP", if the "Server URL" does not indicate "ldaps://", this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256369`

### Rule: The vCenter Server must use a limited privilege account when adding a Lightweight Directory Access Protocol (LDAP) identity source.

**Rule ID:** `SV-256369r885718_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When adding an LDAP identity source to vSphere Single Sign-On (SSO), the account used to bind to Active Directory must be minimally privileged. This account only requires read rights to the base domain name specified. Any other permissions inside or outside of that organizational unit are unnecessary and violate least privilege.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Administration >> Single Sign On >> Configuration >> Identity Provider. Click the "Identity Sources" tab. For each identity source with a type of "Active Directory over LDAP", highlight the item and click "Edit". If the account that is configured to bind to the LDAP server is not one with minimal privileges, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256370`

### Rule: The vCenter Server must limit membership to the "SystemConfiguration.BashShellAdministrators" Single Sign-On (SSO) group.

**Rule ID:** `SV-256370r885721_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>vCenter SSO integrates with PAM in the underlying Photon operating system so members of the "SystemConfiguration.BashShellAdministrators" SSO group can log on to the operating system without needing a separate account. However, even though unique SSO users log on, they are transparently using a group account named "sso-user" as far as Photon auditing is concerned. While the audit trail can still be traced back to the individual SSO user, it is a more involved process. To force accountability and nonrepudiation, the SSO group "SystemConfiguration.BashShellAdministrators" must be severely restricted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Administration >> Single Sign On >> Users and Groups >> Groups. Click the next page arrow until the "SystemConfiguration.BashShellAdministrators" group appears. Click "SystemConfiguration.BashShellAdministrators". Review the members of the group and ensure that only authorized accounts are present. Note: These accounts act as root on the Photon operating system and have the ability to severely damage vCenter, inadvertently or otherwise. If there are any accounts present as members of SystemConfiguration.BashShellAdministrators that are not authorized, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256371`

### Rule: The vCenter Server must limit membership to the "TrustedAdmins" Single Sign-On (SSO) group.

**Rule ID:** `SV-256371r885724_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The vSphere "TrustedAdmins" group grants additional rights to administer the vSphere Trust Authority feature. To force accountability and nonrepudiation, the SSO group "TrustedAdmins" must be severely restricted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Administration >> Single Sign On >> Users and Groups >> Groups. Click the next page arrow until the "TrustedAdmins" group appears. Click "TrustedAdmins". Review the members of the group and verify only authorized accounts are present. Note: These accounts act as root on the Photon operating system and have the ability to severely damage vCenter, inadvertently or otherwise. If any accounts are present as members of "TrustedAdmins" that are not authorized, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256372`

### Rule: The vCenter server configuration must be backed up on a regular basis.

**Rule ID:** `SV-256372r885727_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>vCenter server is the control plane for the vSphere infrastructure and all the workloads it hosts. As such, vCenter is usually a highly critical system in its own right. Backups of vCenter can now be made at a data and configuration level versus traditional storage/image-based backups. This reduces recovery time by letting the system administrator (SA) spin up a new vCenter while simultaneously importing the backed-up data. For sites that implement the Native Key Provider (NKP), introduced in 7.0 Update 2, regular vCenter backups are critical. In a recovery scenario where the virtual machine files are intact but vCenter was lost, the encrypted virtual machines will not be able to boot as their private keys were stored in vCenter after it was last backed up. When using the NKP, vCenter becomes critical to the virtual machine workloads and ceases to be just the control plane.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Option 1: If vCenter is backed up in a traditional manner, at the storage array level, interview the SA to determine configuration and schedule. Option 2: For vCenter native backup functionality, open the Virtual Appliance Management Interface (VAMI) by navigating to https://<vCenter server>:5480. Log in with local operating system administrative credentials or with a Single Sign-On (SSO) account that is a member of the "SystemConfiguration.BashShellAdministrator" group. Select "Backup" on the left navigation pane. On the resulting pane on the right, verify the "Status" is "Enabled". Click "Status" to expand the backup details. If vCenter server backups are not configured and there is no other vCenter backup system, this is a finding. If the backup configuration is not set to a proper, reachable location or if the schedule is anything less frequent than "Daily", this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256373`

### Rule: vCenter task and event retention must be set to at least 30 days.

**Rule ID:** `SV-256373r885730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>vCenter tasks and events contain valuable historical actions, useful in troubleshooting availability issues and for incident forensics. While vCenter events are sent to central log servers in real time, it is important that administrators have quick access to this information when needed. vCenter retains 30 days of tasks and events by default, and this is sufficient for most purposes. The vCenter disk partitions are also sized with this in mind. Decreasing is not recommended for operational reasons, while increasing is not recommended unless guided by VMware support due to the partition sizing concerns.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Host and Clusters. Select a vCenter Server >> Configure >> Settings >> General. Click to expand the "Database" section. Note the "Task retention" and "Event retention" values. If either value is configured to less than "30" days, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-256374`

### Rule: vCenter Native Key Providers must be backed up with a strong password.

**Rule ID:** `SV-256374r919046_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The vCenter Native Key Provider feature was introduced in U2 and acts as a key provider for encryption-based capabilities, such as encrypted virtual machines without requiring an external KMS solution. When enabling this feature, a backup must be taken that is a PKCS#12 formatted file. If no password is provided during the backup process, this presents the opportunity for this to be used maliciously and compromise the environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the vCenter Native Key Provider feature is not in use, this is not applicable. Interview the system administrator and determine if a password was provided for any backups taken of the Native Key Provider. If backups exist for the Native Key Provider that are not password protected, this is a finding.

