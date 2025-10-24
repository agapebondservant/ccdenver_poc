# STIG Benchmark: Microsoft OneDrive Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000210

**Group ID:** `V-215529`

### Rule: Disabling of user name and password syntax from being used in URLs must be enforced.


**Rule ID:** `SV-215529r961092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Uniform Resource Locator (URL) standard allows user authentication to be included in URL strings in the form http://username:password@example.com. A malicious user might use this URL syntax to create a hyperlink that appears to open a legitimate website but actually opens a deceptive (spoofed) website. For example, the URL http://www.wingtiptoys.com@example.com appears to open http://www.wingtiptoys.com but actually opens http://example.com. To protect users from such attacks, Internet Explorer usually blocks any URLs using this syntax. This functionality can be controlled separately for instances of Internet Explorer spawned by Office applications (for example, if a user clicks a link in an Office document or selects a menu option that loads a website). If user names and passwords in URLs are allowed, users could be diverted to dangerous Web pages, which could pose a security risk.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Disable user name and password" is set to "Enabled" and 'groove.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_HTTP_USERNAME_PASSWORD_DISABLE Criteria: If the value groove.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-215531`

### Rule: Saved from URL mark to assure Internet zone processing must be enforced.


**Rule ID:** `SV-215531r961092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Typically, when Internet Explorer loads a web page from a Universal Naming Convention (UNC) share that contains a Mark of the Web (MOTW) comment, indicating the page was saved from a site on the Internet, Internet Explorer runs the page in the Internet security zone instead of the less restrictive Local Intranet security zone. This functionality can be controlled separately for instances of Internet Explorer spawned by Office applications (for example, if a user clicks a link in an Office document or selects a menu option that loads a web page). If Internet Explorer does not evaluate the page for a MOTW, potentially dangerous code could be allowed to run.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Saved from URL" is set to "Enabled" and 'groove.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_UNC_SAVEDFILECHECK Criteria: If the value groove.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-215532`

### Rule: Navigation to URLs embedded in Office products must be blocked.


**Rule ID:** `SV-215532r961092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To protect users from attacks, Internet Explorer usually does not attempt to load malformed URLs. This functionality can be controlled separately for instances of Internet Explorer spawned by Office applications (for example, if a user clicks a link in an Office document or selects a menu option that loads a web page). If Internet Explorer attempts to load a malformed URL, a security risk could occur.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Navigate URL" is set to "Enabled" and 'groove.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_VALIDATE_NAVIGATE_URL Criteria: If the value groove.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000112

**Group ID:** `V-215533`

### Rule: Scripted Window Security must be enforced.


**Rule ID:** `SV-215533r960921_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious websites often try to confuse or trick users into giving a site permission to perform an action allowing the site to take control of the users' computers in some manner. Disabling or not configuring this setting allows unknown websites to: -Create browser windows appearing to be from the local operating system. -Draw active windows displaying outside of the viewable areas of the screen capturing keyboard input. -Overlay parent windows with their own browser windows to hide important system information, choices or prompts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Scripted Window Security Restrictions" is set to "Enabled" and 'groove.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_WINDOW_RESTRICTIONS Criteria: If the value groove.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-215534`

### Rule: Add-on Management functionality must be allowed.


**Rule ID:** `SV-215534r961086_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Explorer add-ons are pieces of code, run in Internet Explorer, to provide additional functionality. Rogue add-ons may contain viruses or other malicious code. Disabling or not configuring this setting could allow malicious code or users to become active on user computers or the network. For example, a malicious user can monitor and then use keystrokes users type into Internet Explorer. Even legitimate add-ons may demand resources, compromising the performance of Internet Explorer, and the operating systems for user computers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Add-on Management" is set to "Enabled" and 'groove.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_ADDON_MANAGEMENT Criteria: If the value groove.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-215535`

### Rule: Links that invoke instances of Internet Explorer from within an Office product must be blocked.


**Rule ID:** `SV-215535r961086_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Pop-up Blocker feature in Internet Explorer can be used to block most unwanted pop-up and pop-under windows from appearing. This functionality can be controlled separately for instances of Internet Explorer spawned by Office applications (for example, if a user clicks a link in an Office document or selects a menu option that loads a web page). If the Pop-up Blocker is disabled, disruptive and potentially dangerous pop-up windows could load and present a security risk.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Block popups" is set to "Enabled" and 'groove.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_WEBOC_POPUPMANAGEMENT Criteria: If the value groove.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000209

**Group ID:** `V-215536`

### Rule: File Downloads must be configured for proper restrictions.


**Rule ID:** `SV-215536r961089_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Disabling this setting allows websites to present file download prompts via code without the user specifically initiating the download. User preferences may also allow the download to occur without prompting or interaction with the user. Even if Internet Explorer prompts the user to accept the download, some websites abuse this functionality. Malicious websites may continually prompt users to download a file or present confusing dialog boxes to trick users into downloading or running a file. If the download occurs and it contains malicious code, the code could become active on user computers or the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Restrict File Download" is set to "Enabled" and 'groove.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_RESTRICT_FILEDOWNLOAD Criteria: If the value of groove.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000112

**Group ID:** `V-215537`

### Rule: Protection from zone elevation must be enforced.


**Rule ID:** `SV-215537r960921_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Explorer places restrictions on each web page users can use the browser to open. Web pages on a user's local computer have the fewest security restrictions and reside in the Local Machine zone, making this security zone a prime target for malicious users and code. Disabling or not configuring this setting could allow pages in the Internet zone to navigate to pages in the Local Machine zone to then run code to elevate privileges. This could allow malicious code or users to become active on user computers or the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Protection From Zone Elevation" is set to "Enabled" and 'groove.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_ZONE_ELEVATION Criteria: If the value groove.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000488

**Group ID:** `V-215538`

### Rule: ActiveX Installs must be configured for proper restriction.


**Rule ID:** `SV-215538r961779_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Microsoft ActiveX controls allow unmanaged, unprotected code to run on the user computers. ActiveX controls do not run within a protected container in the browser like the other types of HTML or Microsoft Silverlight-based controls. Disabling or not configuring this setting does not block prompts for ActiveX control installations, and these prompts display to users. This could allow malicious code to become active on user computers or the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Restrict ActiveX Install" is set to "Enabled" and 'groove.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_RESTRICT_ACTIVEXINSTALL Criteria: If the value groove.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000516

**Group ID:** `V-230562`

### Rule: OneDrive must only allow synchronizing of accounts for DoD organization instances.

**Rule ID:** `SV-230562r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OneDrive provides access to external services for data storage, which must be restricted to authorized instances if enabled. Configuring this setting will restrict synchronizing of OneDrive accounts to DoD organization instances.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the organization is using a DoD instance of OneDrive, verify synchronizing is only allowed to the organization's DoD instance. If the organization does not have an instance of OneDrive, verify this is configured with the noted dummy entry to prevent synchronizing with other instances. If the following registry value does not exist or is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\OneDrive\AllowTenantList\ Value Name: Organization's Tenant GUID Value Type: REG_SZ Value: Organization's Tenant GUID If the organization does not have an instance of OneDrive, the Value Name and Value must be 1111-2222-3333-4444. If it is not, this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-230564`

### Rule: The use of personal accounts for OneDrive synchronization must be disabled.

**Rule ID:** `SV-230564r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OneDrive provides access to external services for data storage, which must be restricted to authorized instances. Enabling this setting will prevent the use of personal OneDrive accounts for synchronization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding. Registry Hive: HKEY_CURRENT_USER Registry Path: \Software\Policies\Microsoft\OneDrive\ Value Name: DisablePersonalSync Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-APP-000456

**Group ID:** `V-275978`

### Rule: The version of OneDrive running on the system must be a supported version.

**Rule ID:** `SV-275978r1111822_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
OneDrive version 24.x.x.x (and older) are no longer supported by the vendor. If the system is running OneDrive version 24.x.x.x (or older), this is a finding.

