# STIG Benchmark: Adobe Acrobat Reader DC Continuous Track Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000112

**Group ID:** `V-213168`

### Rule: Adobe Reader DC must enable Enhanced Security in a Standalone Application.

**Rule ID:** `SV-213168r395811_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>PDFs have evolved from static pages to complex documents with features such as interactive forms, multimedia content, scripting, and other capabilities. These features leave PDFs vulnerable to malicious scripts or actions that can damage the computer or steal data. The Enhanced security feature protects the computer against these threats by blocking or selectively permitting actions for trusted locations and files. Enhanced Security determines if a PDF is viewed within a standalone application. A threat to users of Adobe Reader DC is opening a PDF file that contains malicious executable content. Enhanced Security “hardens” the application against risky actions: prevents cross domain access, prohibits script and data injection, blocks stream access to XObjects, silent printing, and execution of high privilege JavaScript. Satisfies: SRG-APP-000112, SRG-APP-000206, SRG-APP-000207, SRG-APP-000209, SRG-APP-000210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown Value Name: bEnhancedSecurityStandalone Type: REG_DWORD Value: 1 If the value for bEnhancedSecurityStandalone is not set to “1” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000112

**Group ID:** `V-213169`

### Rule: Adobe Reader DC must enable Enhanced Security in a Browser.

**Rule ID:** `SV-213169r395811_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>PDFs have evolved from static pages to complex documents with features such as interactive forms, multimedia content, scripting, and other capabilities. These features leave PDFs vulnerable to malicious scripts or actions that can damage the computer or steal data. The Enhanced security feature protects the computer against these threats by blocking or selectively permitting actions for trusted locations and files. Enhanced Security determines if a PDF is viewed within a browser application. A threat to users of Adobe Reader DC is opening a PDF file that contains malicious executable content. Enhanced Security “hardens” the application against risky actions: prevents cross domain access, prohibits script and data injection, blocks stream access to XObjects, silent printing, and execution of high privilege JavaScript. Satisfies: SRG-APP-000112, SRG-APP-000206, SRG-APP-000207, SRG-APP-000209, SRG-APP-000210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown Value Name: bEnhancedSecurityInBrowser Type: REG_DWORD Value: 1 If the value for bEnhancedSecurityInBrowser is not set to “1” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000112

**Group ID:** `V-213170`

### Rule: Adobe Reader DC must enable Protected Mode.

**Rule ID:** `SV-213170r395811_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A threat to users of Adobe Reader DC is opening a PDF file that contains malicious executable content. Protected mode provides a sandbox capability that prevents malicious PDF files from launching arbitrary executable files, writing to system directories or the Windows registry. This isolation of the PDFs reduces the risk of security breaches in areas outside the sandbox. Satisfies: SRG-APP-000112, SRG-APP-000206, SRG-APP-000207, SRG-APP-000209, SRG-APP-000210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown Value Name: bProtectedMode Type: REG_DWORD Value: 1 If the value for bProtectedMode is not set to “1” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000112

**Group ID:** `V-213171`

### Rule: Adobe Reader DC must enable Protected View.

**Rule ID:** `SV-213171r395811_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A threat to users of Adobe Reader DC is opening a PDF file that contains malicious executable content. Protected view restricts Adobe Reader DC functionality, within a sandbox, when a PDF is opened from an untrusted source. This isolation of the PDFs reduces the risk of security breaches in areas outside the sandbox. Satisfies: SRG-APP-000112, SRG-APP-000206, SRG-APP-000207, SRG-APP-000209, SRG-APP-000210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown Value Name: iProtectedView Type: REG_DWORD Value: 2 If the value for iProtectedView is not set to “2” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000112

**Group ID:** `V-213172`

### Rule: Adobe Reader DC must Block Websites.

**Rule ID:** `SV-213172r395811_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Clicking any link to the Internet poses a potential security risk. Malicious websites can transfer harmful content or silently gather data. Acrobat Reader documents can connect to websites which can pose a potential threat to DoD systems and that functionality must be blocked. However, PDF document workflows that are trusted (e.g., DoD-created) can benefit from leveraging legitimate website access with minimal risk. Therefore, the ISSO may approve of website access and accept the risk if the access provides benefit and is a trusted site or the risk associated with accessing the site has been mitigated. Adobe Reader must block access to all websites that are not specifically allowed by ISSO risk acceptance. Satisfies: SRG-APP-000112, SRG-APP-000206, SRG-APP-000207, SRG-APP-000209, SRG-APP-000210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown\cDefaultLaunchURLPerms Value Name: iURLPerms Type: REG_DWORD Value: 1 Value: 0 - only with a documented ISSO risk acceptance If the value for “iURLPerms” is set to “0” and a documented ISSO risk acceptance approving access to websites is provided, this is not a finding. If the value for “iURLPerms” is not set to “1” and “Type” configured to “REG_DWORD” or does not exist, this is a finding.

## Group: SRG-APP-000112

**Group ID:** `V-213173`

### Rule: Adobe Reader DC must block access to Unknown Websites.

**Rule ID:** `SV-213173r395811_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Because Internet access is a potential security risk, clicking any unknown website link to the Internet poses a potential security risk. Malicious websites can transfer harmful content or silently gather data. Satisfies: SRG-APP-000112, SRG-APP-000206, SRG-APP-000207, SRG-APP-000209, SRG-APP-000210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown\cDefaultLaunchURLPerms Value Name: iUnknownURLPerms Type: REG_DWORD Value: 3 If the value for iUnknownURLPerms is not set to “3” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000112

**Group ID:** `V-213174`

### Rule: Adobe Reader DC must prevent opening files other than PDF or FDF.

**Rule ID:** `SV-213174r395811_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Attachments represent a potential security risk because they can contain malicious content, open other dangerous files, or launch applications. Certainly file types such as .bin, .exe, .bat, and so on will be recognized as threats. This feature prevents users from opening or launching file types other than PDF or FDF and disables the menu option. Satisfies: SRG-APP-000112, SRG-APP-000206, SRG-APP-000207, SRG-APP-000209, SRG-APP-000210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown Value Name: iFileAttachmentPerms Type: REG_DWORD Value: 1 If the value for iFileAttachmentPerms is not set to “1” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000112

**Group ID:** `V-213175`

### Rule: Adobe Reader DC must block Flash Content.

**Rule ID:** `SV-213175r395811_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Flash content is commonly hosted on a web page, but it can also be embedded in PDF and other documents. Flash could be used to surreptitious install malware on the end-users computer. Flash Content restricts Adobe Reader DC not to play Flash content within a PDF. Satisfies: SRG-APP-000112, SRG-APP-000206, SRG-APP-000207, SRG-APP-000209, SRG-APP-000210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown Value Name: bEnableFlash Type: REG_DWORD Value: 0 If the value for bEnableFlash is not set to “0” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000133

**Group ID:** `V-213176`

### Rule: Adobe Reader DC must disable the ability to change the Default Handler.

**Rule ID:** `SV-213176r395850_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Allowing user to make changes to an application case cause a security risk. When the Default PDF Handler is disabled, the end users will not be able to change the default PDF viewer.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown Value Name: bDisablePDFHandlerSwitching Type: REG_DWORD Value: 1 If the value for bDisablePDFHandlerSwitching is not set to “1” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-213177`

### Rule: Adobe Reader DC must disable the Adobe Send and Track plugin for Outlook.

**Rule ID:** `SV-213177r766574_rule`
**Severity:** low

**Description:**
<VulnDiscussion>When enabled, Adobe Send and Track button appears in Outlook. When an email is composed it enables the ability to send large files as public links through Outlook. The attached files can be uploaded to the Adobe Document Cloud and public links to the files are inserted in the email body.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Note: The Key Name "cCloud" is not created by default in the Adobe Reader DC install and must be created. Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown\cCloud Value Name: bAdobeSendPluginToggle Type: REG_DWORD Value: 1 If the value for bAdobeSendPluginToggle is not set to “1” and Type configured to REG_DWORD or does not exist, then this is a finding. Admin Template path: Computer Configuration > Administrative Templates > Adobe Reader DC Continuous > Preferences > 'Send and Track plugin' must be set to 'Disabled'.

## Group: SRG-APP-000141

**Group ID:** `V-213178`

### Rule: Adobe Reader DC must disable all service access to Document Cloud Services.

**Rule ID:** `SV-213178r395853_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, Adobe online services are tightly integrated in Adobe Reader DC. With the integration of Adobe Document Cloud, disabling this feature prevents the risk of additional attack vectors. Within Adobe Reader DC, the Adobe Cloud resources require a paid subscription for each service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Note: The Key Name "cServices" is not created by default in the Adobe Reader DC install and must be created. Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown\cServices Value Name: bToggleAdobeDocumentServices Type: REG_DWORD Value: 1 If the value for bToggleAdobeDocumentServices is not set to “1” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-213179`

### Rule: Adobe Reader DC must disable Cloud Synchronization.

**Rule ID:** `SV-213179r395853_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, Adobe online services are tightly integrated in Adobe Reader DC. When the Adobe Cloud synchronization is disabled it prevents the synchronization of desktop preferences across devices on which the user is signed in with an Adobe ID (including phones).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Note: The Key Name "cServices" is not created by default in the Adobe Reader DC install and must be created. Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown\cServices Value Name: bTogglePrefsSync Type: REG_DWORD Value: 1 If the value for bTogglePrefsSync is not set to “1” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-213180`

### Rule: Adobe Reader DC must disable the Adobe Repair Installation.

**Rule ID:** `SV-213180r395853_rule`
**Severity:** low

**Description:**
<VulnDiscussion>When Repair Installation is disabled the user does not have the option (Help Menu) or functional to repair an Adobe Reader DC install.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Utilizing the Registry Editor, navigate to the following: For 32 bit: HKEY_LOCAL_MACHINE\Software\Adobe\Acrobat Reader\DC\Installer For 64 bit: HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Adobe\Acrobat Reader\DC\Installer Value Name: DisableMaintenance Type: REG_DWORD Value: 1 If the value for DisableMaintenance is not set to “1” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-213181`

### Rule: Adobe Reader DC must disable 3rd Party Web Connectors.

**Rule ID:** `SV-213181r395853_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When 3rd Party Web Connectors are disabled it prevents the configuration of Adobe Reader DC access to third party services for file storage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Note: The Key Name "cServices" is not created by default in the Adobe Reader DC install and must be created. Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown\cServices Value Name: bToggleWebConnectors Type: REG_DWORD Value: 1 If the value for bToggleWebConnectors is not set to “1” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-213182`

### Rule: Adobe Reader DC must disable Acrobat Upsell.

**Rule ID:** `SV-213182r395853_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Products that don't provide the full set of features by default provide the user the opportunity to upgrade. Acrobat Upsell displays message which encourage the user to upgrade the product. For example, Reader users can purchase additional tools and features, and Acrobat Reader users can upgrade to Acrobat Professional.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown Value Name: bAcroSuppressUpsell Type: REG_DWORD Value: 1 If the value for bAcroSuppressUpsell is not set to “1” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-213183`

### Rule: Adobe Reader DC must disable Adobe Send for Signature.

**Rule ID:** `SV-213183r395853_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Adobe Document Cloud sign service allows users to send documents online for signature and sign from anywhere or any device. The signed documents are stored in the Adobe Cloud. The Adobe Document Cloud sign service is a paid subscription. When Adobe Send for Signature is disabled users will not be allowed to utilize the Adobe Document Cloud sign function.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Note: The Key Name "cServices" is not created by default in the Adobe Reader DC install and must be created. Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown\cServices Value Name: bToggleAdobeSign Type: REG_DWORD Value: 1 If the value for bToggleAdobeSign is not set to “1” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-213184`

### Rule: Adobe Reader DC must disable access to Webmail.

**Rule ID:** `SV-213184r395853_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When Webmail is disabled the user cannot configure a webmail account to send an open PDF document as an attachment. Users should have the ability to send documents as Microsoft Outlook attachments. The difference is that Outlook must be configured by the administrator on the local machine.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Note: The Key Name "cWebmailProfiles" is not created by default in the Adobe Reader DC install and must be created. Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown\cWebmailProfiles Value Name: bDisableWebmail Type: REG_DWORD Value: 1 If the value for bDisableWebmail is not set to “1” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-213185`

### Rule: Adobe Reader DC must disable Online SharePoint Access.

**Rule ID:** `SV-213185r395853_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Disabling SharePoint disables or removes the user’s ability to add a SharePoint account access controls the application's ability to detect that a file came from a SharePoint server, and disables the check-out prompt.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: If configured to an approved DoD SharePoint Server, this is NA. Note: The Key Name "cSharePoint" is not created by default in the Adobe Reader DC install and must be created. Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown\cSharePoint Value Name: bDisableSharePointFeatures Type: REG_DWORD Value: 1 If the value for bDisableSharePointFeatures is not set to “1” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-213186`

### Rule: Adobe Reader DC must disable the Adobe Welcome Screen.

**Rule ID:** `SV-213186r395853_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Adobe Reader DC Welcome screen can be distracting and also has online links to the Adobe quick tips website, tutorials, blogs and community forums. When the Adobe Reader DC Welcome screen is disabled the Welcome screen will not be populated on application startup.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Note: The Key Name "cWelcomeScreen" is not created by default in the Adobe Reader DC install and must be created. Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown\cWelcomeScreen Value Name: bShowWelcomeScreen Type: REG_DWORD Value: 0 If the value for bShowWelcomeScreen is not set to “0” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-213187`

### Rule: Adobe Reader DC must disable Service Upgrades.

**Rule ID:** `SV-213187r395853_rule`
**Severity:** low

**Description:**
<VulnDiscussion>By default, Adobe online services are tightly integrated into Adobe Reader DC. Disabling Service Upgrades disables both updates to the product's web-plugin components as well as all services without exception, including any online sign-in screen.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Note: The Key Name "cServices" is not created by default in the Adobe Reader DC install and must be created. Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown\cServices Value Name: bUpdater Type: REG_DWORD Value: 0 If the value for bUpdater is not set to “0” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000380

**Group ID:** `V-213188`

### Rule: Adobe Reader DC must disable the ability to add Trusted Files and Folders.

**Rule ID:** `SV-213188r400006_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Privileged Locations allow the user to selectively trust files, folders, and hosts to bypass some security restrictions, such as enhanced security and protected view. By default, the user can create privileged locations through the GUI. Disabling Trusted Files and Folders disables and locks the end user's ability to add folders and files as a privileged location prevents them from assigning trust and thereby exempting that location from enhanced security restrictions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown Value Name: bDisableTrustedFolders Type: REG_DWORD Value: 1 If the value for bDisableTrustedFolders is not set to “1” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000380

**Group ID:** `V-213189`

### Rule: Adobe Reader DC must disable the ability to elevate IE Trusts to Privileged Locations.

**Rule ID:** `SV-213189r400006_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Privileged Locations allow the user to selectively trust files, folders, and hosts to bypass some security restrictions, such as enhanced security and protected view. By default, the user can create privileged locations through the GUI. Disabling IE Trusts to Privileged Locations disables and locks the end user's ability to treat IE trusted sites as a privileged location prevents them from assigning trust and thereby exempting that location from enhanced security restrictions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Acrobat Reader\DC\FeatureLockDown Value Name: bDisableTrustedSites Type: REG_DWORD Value: 1 If the value for bDisableTrustedSites is not set to “1” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000427

**Group ID:** `V-213190`

### Rule: Adobe Reader DC must disable periodical uploading of European certificates.

**Rule ID:** `SV-213190r400378_rule`
**Severity:** low

**Description:**
<VulnDiscussion>By default, the user can update European certificates from an Adobe server through the GUI. When uploading European certificates is disabled, it prevents the automatic download and installation of certificates and disables and locks the end user's ability to upload those certificates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Note: The Key Names "cDigSig" and "cEUTLDownload" are not created by default in the Adobe Reader DC install and must be created. Utilizing the Registry Editor, navigate to the following: HKEY_CURRENT_USER\Software\Adobe\Acrobat Reader\DC\Security\cDigSig\cEUTLDownload Value Name: bLoadSettingsFromURL Type: REG_DWORD Value: 0 If the value for bLoadSettingsFromURL is not set to “0” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000427

**Group ID:** `V-213191`

### Rule: Adobe Reader DC must disable periodical uploading of Adobe certificates.

**Rule ID:** `SV-213191r400378_rule`
**Severity:** low

**Description:**
<VulnDiscussion>By default, the user can update Adobe certificates from an Adobe server through the GUI. When uploading Adobe certificates is disabled, it prevents the automatic download and installation of certificates and disables and locks the end user's ability to upload those certificates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Note: The Key Names "cDigSig" and "cAdobeDownload" are not created by default in the Adobe Reader DC install and must be created. Utilizing the Registry Editor, navigate to the following: HKEY_CURRENT_USER\Software\Adobe\Acrobat Reader\DC\Security\cDigSig\cAdobeDownload Value Name: bLoadSettingsFromURL Type: REG_DWORD Value: 0 If the value for bLoadSettingsFromURL is not set to “0” and Type configured to REG_DWORD or does not exist, then this is a finding.

## Group: SRG-APP-000456

**Group ID:** `V-213192`

### Rule: Adobe Reader DC must have the latest Security-related Software Updates installed.

**Rule ID:** `SV-213192r400525_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period utilized must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine the method for doing this (e.g., connection to a WSUS server, local procedure, auto update, etc.). Open Adobe Acrobat Reader DC. Navigate to and click on Help >> About Adobe Acrobat Reader DC. Verify that the latest security-related software updates by Adobe are being applied. If the latest security-related software updates by Adobe are not being applied, this is a finding.

## Group: SRG-APP-000514

**Group ID:** `V-213193`

### Rule: Adobe Reader DC must enable FIPS mode.

**Rule ID:** `SV-213193r400876_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Note: The Key Names "bFIPSMode" is not created by default in the Adobe Reader DC install and must be created. Utilizing the Registry Editor, navigate to the following: HKEY_CURRENT_USER\Software\Adobe\Acrobat Reader\DC\AVGeneral Value Name: bFIPSMode Type: REG_DWORD Value: 1 If the value for bFIPSMode is not set to “1” and Type configured to REG_DWORD does not exist, then this is a finding.

