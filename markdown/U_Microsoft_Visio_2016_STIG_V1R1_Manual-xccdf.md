# STIG Benchmark: Microsoft Visio 2016 Security Technical Implementation Guide

---

**Version:** 1

**Description:**
The Microsoft Visio 2016 Security Technical Implementation Guide (STIG) is published as a tool to improve the security of Department of Defense (DoD) information systems. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000210

**Group ID:** `V-70803`

### Rule: Disabling of user name and password syntax from being used in URLs must be enforced.


**Rule ID:** `SV-85427r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Uniform Resource Locator (URL) standard allows user authentication to be included in URL strings in the form http://username:password@example.com. A malicious user might use this URL syntax to create a hyperlink that appears to open a legitimate website but actually opens a deceptive (spoofed) website. For example, the URL http://www.wingtiptoys.com@example.com appears to open http://www.wingtiptoys.com but actually opens http://example.com. To protect users from such attacks, Internet Explorer usually blocks any URLs using this syntax. This functionality can be controlled separately for instances of Internet Explorer spawned by Office applications (for example, if a user clicks a link in an Office document or selects a menu option that loads a website). If user names and passwords in URLs are allowed, users could be diverted to dangerous Web pages, which could pose a security risk. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Disable user name and password" is set to "Enabled" and 'visio.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_HTTP_USERNAME_PASSWORD_DISABLE Criteria: If the value visio.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000112

**Group ID:** `V-70805`

### Rule: Enabling IE Bind to Object functionality must be present.


**Rule ID:** `SV-85429r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Explorer performs a number of safety checks before initializing an ActiveX control. It will not initialize a control if the kill bit for the control is set in the registry, or if the security settings for the zone in which the control is located do not allow it to be initialized. This functionality can be controlled separately for instances of Internet Explorer spawned by Office applications (for example, if a user clicks a link in an Office document or selects a menu option that loads a web page). A security risk could occur if potentially dangerous controls are allowed to load.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Bind to Object" is set to "Enabled" and 'visio.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_SAFE_BINDTOOBJECT Criteria: If the value visio.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-70807`

### Rule: Saved from URL mark to assure Internet zone processing must be enforced.


**Rule ID:** `SV-85431r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Typically, when Internet Explorer loads a web page from a Universal Naming Convention (UNC) share that contains a Mark of the Web (MOTW) comment, indicating the page was saved from a site on the Internet, Internet Explorer runs the page in the Internet security zone instead of the less restrictive Local Intranet security zone. This functionality can be controlled separately for instances of Internet Explorer spawned by Office applications (for example, if a user clicks a link in an Office document or selects a menu option that loads a web page). If Internet Explorer does not evaluate the page for a MOTW, potentially dangerous code could be allowed to run. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Saved from URL" is set to "Enabled" and 'visio.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_UNC_SAVEDFILECHECK Criteria: If the value visio.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-70809`

### Rule: Navigation to URLs embedded in Office products must be blocked.


**Rule ID:** `SV-85433r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To protect users from attacks, Internet Explorer usually does not attempt to load malformed URLs. This functionality can be controlled separately for instances of Internet Explorer spawned by Office applications (for example, if a user clicks a link in an Office document or selects a menu option that loads a web page). If Internet Explorer attempts to load a malformed URL, a security risk could occur. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Navigate URL" is set to "Enabled" and 'visio.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_VALIDATE_NAVIGATE_URL Criteria: If the value visio.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000112

**Group ID:** `V-70811`

### Rule: Scripted Window Security must be enforced.


**Rule ID:** `SV-85435r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious websites often try to confuse or trick users into giving a site permission to perform an action allowing the site to take control of the users' computers in some manner. Disabling or not configuring this setting allows unknown websites to: -Create browser windows appearing to be from the local operating system. -Draw active windows displaying outside of the viewable areas of the screen capturing keyboard input. -Overlay parent windows with their own browser windows to hide important system information, choices or prompts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Scripted Window Security Restrictions" is set to "Enabled" and 'visio.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_WINDOW_RESTRICTIONS Criteria: If the value visio.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-70813`

### Rule: Add-on Management functionality must be allowed.


**Rule ID:** `SV-85437r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Explorer add-ons are pieces of code, run in Internet Explorer, to provide additional functionality. Rogue add-ons may contain viruses or other malicious code. Disabling or not configuring this setting could allow malicious code or users to become active on user computers or the network. For example, a malicious user can monitor and then use keystrokes users type into Internet Explorer. Even legitimate add-ons may demand resources, compromising the performance of Internet Explorer, and the operating systems for user computers. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Add-on Management" is set to "Enabled" and 'visio.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_ADDON_MANAGEMENT Criteria: If the value visio.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000131

**Group ID:** `V-70815`

### Rule: Add-ins to Office applications must be signed by a Trusted Publisher.


**Rule ID:** `SV-85439r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls whether add-ins for this applications must be digitally signed by a trusted publisher. If you enable this policy setting, this application checks the digital signature for each add-in before loading it. If an add-in does not have a digital signature, or if the signature did not come from a trusted publisher, this application disables the add-in and notifies the user. Certificates must be added to the Trusted Publishers list if you require that all add-ins be signed by a trusted publisher. For detail on about obtaining and distributing certificates, see http://go.microsoft.com/fwlink/?LinkId=294922. Office 2016 stores certificates for trusted publishers in the Internet Explorer trusted publisher store. Earlier versions of Microsoft Office stored trusted publisher certificate information (specifically, the certificate thumbprint) in a special Office trusted publisher store. Office 2016 still reads trusted publisher certificate information from the Office trusted publisher store, but it does not write information to this store. Therefore, if you created a list of trusted publishers in a previous version of Office and you upgrade to Office 2016, your trusted publisher list will still be recognized. However, any trusted publisher certificates that you add to the list will be stored in the Internet Explorer trusted publisher store. For more information about trusted publishers, see the Office Resource Kit. If you disable or do not configure this policy setting, this application does not check the digital signature on application add-ins before opening them. If a dangerous add-in is loaded, it could harm users' computers or compromise data security. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Visio 2016 -> Visio Options -> Security -> Trust Center -> "Require that application add-ins are signed by Trusted Publisher" is set to "Enabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\software\policies\Microsoft\office\16.0\Visio\security Criteria: If the value requireaddinsig is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-70817`

### Rule: Links that invoke instances of Internet Explorer from within an Office product must be blocked.


**Rule ID:** `SV-85441r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Pop-up Blocker feature in Internet Explorer can be used to block most unwanted pop-up and pop-under windows from appearing. This functionality can be controlled separately for instances of Internet Explorer spawned by Office applications (for example, if a user clicks a link in an Office document or selects a menu option that loads a web page). If the Pop-up Blocker is disabled, disruptive and potentially dangerous pop-up windows could load and present a security risk. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Block popups" is set to "Enabled" and 'visio.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_WEBOC_POPUPMANAGEMENT Criteria: If the value visio.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000131

**Group ID:** `V-70819`

### Rule: Trust Bar Notifications for unsigned application add-ins must be blocked.


**Rule ID:** `SV-85443r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls whether the specified Office application notifies users when unsigned application add-ins are loaded or silently disable such add-ins without notification. This policy setting only applies if you enable the "Require that application add-ins are signed by Trusted Publisher" policy setting, which prevents users from changing this policy setting. If you enable this policy setting, applications automatically disable unsigned add-ins without informing users. If you disable this policy setting, if this application is configured to require that all add-ins be signed by a trusted publisher, any unsigned add-ins the application loads will be disabled and the application will display the Trust Bar at the top of the active window. The Trust Bar contains a message that informs users about the unsigned add-in. If you do not configure this policy setting, the disable behavior applies, and in addition, users can configure this requirement themselves in the "Add-ins" category of the Trust Center for the application. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Visio 2016 -> Visio Options -> Security -> Trust Center -> "Disable Trust Bar Notification for unsigned application add-ins and block them" is set to "Enabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\software\policies\Microsoft\office\16.0\Visio\security Criteria: If the value notbpromptunsignedaddin is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000209

**Group ID:** `V-70821`

### Rule: File Downloads must be configured for proper restrictions.


**Rule ID:** `SV-85445r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Disabling this setting allows websites to present file download prompts via code without the user specifically initiating the download. User preferences may also allow the download to occur without prompting or interaction with the user. Even if Internet Explorer prompts the user to accept the download, some websites abuse this functionality. Malicious websites may continually prompt users to download a file or present confusing dialog boxes to trick users into downloading or running a file. If the download occurs and it contains malicious code, the code could become active on user computers or the network. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Restrict File Download" is set to "Enabled" and 'visio.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_RESTRICT_FILEDOWNLOAD Criteria: If the value of visio.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000112

**Group ID:** `V-70823`

### Rule: Protection from zone elevation must be enforced.


**Rule ID:** `SV-85447r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Explorer places restrictions on each web page users can use the browser to open. Web pages on a user's local computer have the fewest security restrictions and reside in the Local Machine zone, making this security zone a prime target for malicious users and code. Disabling or not configuring this setting could allow pages in the Internet zone to navigate to pages in the Local Machine zone to then run code to elevate privileges. This could allow malicious code or users to become active on user computers or the network. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Protection From Zone Elevation" is set to "Enabled" and 'visio.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_ZONE_ELEVATION Criteria: If the value visio.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000488

**Group ID:** `V-70825`

### Rule: ActiveX Installs must be configured for proper restriction.


**Rule ID:** `SV-85449r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Microsoft ActiveX controls allow unmanaged, unprotected code to run on the user computers. ActiveX controls do not run within a protected container in the browser like the other types of HTML or Microsoft Silverlight-based controls. Disabling or not configuring this setting does not block prompts for ActiveX control installations, and these prompts display to users. This could allow malicious code to become active on user computers or the network. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Restrict ActiveX Install" is set to "Enabled" and 'visio.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_RESTRICT_ACTIVEXINSTALL Criteria: If the value visio.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-70827`

### Rule: Warning Bar settings for VBA macros must be configured.


**Rule ID:** `SV-85451r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls how the specified applications warn users when Visual Basic for Applications (VBA) macros are present. If you enable this policy setting, you can choose from four options for determining how the specified applications will warn the user about macros: - Disable all with notification: The application displays the Trust Bar for all macros, whether signed or unsigned. This option enforces the default configuration in Office. - Disable all except digitally signed macros: The application displays the Trust Bar for digitally signed macros, allowing users to enable them or leave them disabled. Any unsigned macros are disabled, and users are not notified. - Disable all without notification: The application disables all macros, whether signed or unsigned, and does not notify users. - Enable all macros (not recommended): All macros are enabled, whether signed or unsigned. This option can significantly reduce security by allowing dangerous code to run undetected. If you disable this policy setting, "Disable all with notification" will be the default setting. If you do not configure this policy setting, when users open files in the specified applications that contain VBA macros, the applications open the files with the macros disabled and display the Trust Bar with a warning that macros are present and have been disabled. Users can inspect and edit the files if appropriate, but cannot use any disabled functionality until they enable it by clicking "Enable Content" on the Trust Bar. If the user clicks "Enable Content", then the document is added as a trusted document. Important: If "Disable all except digitally signed macros" is selected, users will not be able to open unsigned Access databases. Also, note that Microsoft Office stores certificates for trusted publishers in the Internet Explorer trusted publisher store. Earlier versions of Microsoft Office stored trusted publisher certificate information (specifically, the certificate thumbprint) in a special Office trusted publisher store. Microsoft Office still reads trusted publisher certificate information from the Office trusted publisher store, but it does not write information to this store. Therefore, if you created a list of trusted publishers in a previous version of Microsoft Office and you upgrade to Office, your trusted publisher list will still be recognized. However, any trusted publisher certificates that you add to the list will be stored in the Internet Explorer trusted publisher store. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Visio 2016 -> Visio Options -> Security -> Trust Center "VBA Macro Notification Settings" is set to "Enabled: Disable all with notification". The options 'Enabled: Disable all except digitally signed macros' and 'Enabled: Disable all without notification' are more restrictive and also acceptable values. Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\visio\security Criteria: If the value VBAWarnings is REG_DWORD = 2, this is not a finding. Values of REG_DWORD = 3 or 4 are also acceptable values. If the registry key does not exist or the value is REG_DWORD = 1, then this is a finding.

