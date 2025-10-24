# STIG Benchmark: Adobe Acrobat Professional DC Continuous Track Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000112

**Group ID:** `V-213117`

### Rule: Adobe Acrobat Pro DC Continuous Enhanced Security for standalone mode must be enabled.

**Rule ID:** `SV-213117r766511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enhanced Security (ES) is a sandbox capability that restricts access to system resources. ES can be configured in two modes: Standalone mode is when Acrobat opens the desktop PDF client. ES Browser mode is when a PDF is opened via the browser plugin. When Enhanced Security is enabled and a PDF file tries to complete a restricted action from an untrusted location, a security warning must appear.Enhanced Security “hardens” the application against risky actions. It prevents cross domain access, prohibits script and data injection, blocks stream access to XObjects, silent printing, and execution of high privilege JavaScript.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown Value Name: bEnhancedSecurityStandalone Type: REG_DWORD Value: 1 If the value for bEnhancedSecurityStandalone is not set to “1” and Type is not configured to REG_DWORD or does not exist, this is a finding. GUI path: Edit > Preferences > Security (Enhanced) > In the 'Enhanced Security' section> Verify 'Enable Enhanced Security' checkbox is checked and greyed out (locked). If the box is not checked nor greyed out (locked), this is a finding. Admin Template path: Computer Configuration > Administrative Templates > Adobe Acrobat Pro DC Continuous > Preferences > Security (Enhanced) > 'Enable Enhanced Security Standalone' must be set to 'Enabled'.

## Group: SRG-APP-000112

**Group ID:** `V-213118`

### Rule: Adobe Acrobat Pro DC Continuous Enhanced Security for browser mode must be enabled.

**Rule ID:** `SV-213118r766514_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enhanced Security (ES) is a sandbox capability that restricts access to system resources and prevents PDF cross domain access. ES can be configured in two modes: Standalone mode is when Acrobat opens the desktop PDF client. ES Browser mode is when a PDF is opened via the browser plugin. When Enhanced Security is enabled and a PDF file tries to complete a restricted action from an untrusted location, a security warning must appear.Enhanced Security “hardens” the application against risky actions. It prevents cross domain access, prohibits script and data injection, blocks stream access to XObjects, silent printing, and execution of high privilege JavaScript.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown Value Name: bEnhancedSecurityInBrowser Type: REG_DWORD Value: 1 If the value for bEnhancedSecurityInBrowser is not set to “1” and Type is not configured to REG_DWORD or does not exist, this is a finding. Admin Template path: Computer Configuration > Administrative Templates > Adobe Acrobat Pro DC Continuous > Preferences > Security (Enhanced) > 'Enable Enhanced Security In Browser' must be set to 'Enabled'.

## Group: SRG-APP-000141

**Group ID:** `V-213119`

### Rule: Adobe Acrobat Pro DC Continuous PDF file attachments must be blocked.

**Rule ID:** `SV-213119r766517_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Acrobat Pro allows for files to be attached to PDF documents. Attachments represent a potential security risk because they can contain malicious content, open other dangerous files, or launch applications.This feature prevents users from opening or launching file types other than PDF or FDF and disables the menu option to re-enable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown Value Name: iFileAttachmentPerms Type: REG_DWORD Value: 1 If the value for iFileAttachmentPerms is not set to “1” and Type is not configured to REG_DWORD or does not exist, this is a finding. GUI path: Edit > Preferences > Trust Manager > In the 'PDF File Attachments' section > Verify 'Allow opening of non-PDF file attachments with external applications' checkbox is unchecked and greyed out (locked). If the box is checked and not greyed out (locked), this is a finding. Admin Template path: Computer Configuration > Administrative Templates > Adobe Acrobat Pro DC Continuous > Preferences > Trust Manager > 'Allow opening of non-PDF file attachments with external applications' must be set to 'Disabled'.

## Group: SRG-APP-000141

**Group ID:** `V-213120`

### Rule: Adobe Acrobat Pro DC Continuous access to unknown websites must be restricted.

**Rule ID:** `SV-213120r766520_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Acrobat provides the ability for the user to store a list of websites with an associated behavior of allow, ask, or block. Websites that are not in this list are unknown. PDF files can contain URLs that will initiate connections to unknown websites in order to share or get information. That access must be restricted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown\cDefaultLaunchURLPerms\ Value Name: iUnknownURLPerms Type: REG_DWORD Value: 3 If the value for iUnknownURLPerms is not set to “3” and Type is not configured to REG_DWORD or does not exist, this is a finding. GUI path: Edit > Preferences > Trust Manager > In the 'Internet Access from PDF Files outside the web browser' section > Select 'Change Settings' option > In the 'PDF Files may connect to web sites to share or get information' section, if 'Block PDF files access to all web sites' is selected and greyed out (locked), then this is not a finding. If 'Custom setting' is checked, then in the 'Default behavior for web sites that are not in the above list' section, verify the radio button 'Block access' is checked and greyed out (locked) . If the box is not checked nor greyed out, this is a finding. Admin Template path: Computer Configuration > Administrative Templates > Adobe Acrobat Pro DC Continuous > Preferences > Trust Manager > 'Access to unknown websites' must be set to 'Enabled' and 'Block access' selected in the drop down box.

## Group: SRG-APP-000141

**Group ID:** `V-213121`

### Rule: Adobe Acrobat Pro DC Continuous access to websites must be blocked.

**Rule ID:** `SV-213121r766523_rule`
**Severity:** low

**Description:**
<VulnDiscussion>PDF files can contain URLs that initiate connections to websites in order to share or get information. Any Internet access introduces a security risk as malicious websites can transfer harmful content or silently gather data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Utilizing the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown\cDefaultLaunchURLPerms\ Value Name: iURLPerms Type: REG_DWORD Value: 1 If the value for iURLPerms is not set to “1” and Type is not configured to REG_DWORD or does not exist, this is a finding. Setting the value for iURLPerms to "0" means that a custom settings has been selected. Custom setting allows for specific websites to be used for PDF workflows. These websites must be approved by the ISSO/AO otherwise the setting must be "1" which blocks access to all websites. If the iURLPerms setting is "0" and a documented risk acceptance approving the websites is provided, this is not a finding. GUI path: Edit > Preferences > Trust Manager > In the 'Internet Access from PDF Files outside the web browser' section > Select 'Change Settings' option > In the 'PDF Files may connect to web sites to share or get information' section > Verify the radio button 'Block PDF files access to all web sites' is selected and greyed out (locked). If 'Custom setting' is checked, a documented risk acceptance approved by the ISSO/AO approving the websites must be provided and then this is not a finding. Admin Template path: Computer Configuration > Administrative Templates > Adobe Acrobat Pro DC Continuous > Preferences > Trust Manager > 'Access to websites' must be set to 'Enabled' and 'Block PDF files access to all web sites' selected in the drop down box. If 'Custom setting' is selected, a documented risk acceptance approved by the ISSO/AO approving the websites must be provided and then this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-213122`

### Rule: Adobe Acrobat Pro DC Continuous must be configured to block Flash Content.

**Rule ID:** `SV-213122r766526_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Flash has a long history of vulnerabilities. Although Flash is no longer provided with Acrobat, if the system has Flash installed, a malicious PDF could execute code on the system. Configuring Flash to run from a privileged location limits the execution capability of untrusted Flash content that may be embedded in the PDF.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Using the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown Value Name: bEnableFlash Type: REG_DWORD Value: 0 If the value for bEnableFlash is not set to “0” and Type is not configured to REG_DWORD or does not exist, this is a finding. Admin Template path: Computer Configuration > Administrative Templates > Adobe Acrobat Pro DC Continuous > Preferences > 'Enable Flash' must be set to 'Disabled'.

## Group: SRG-APP-000141

**Group ID:** `V-213123`

### Rule: The Adobe Acrobat Pro DC Continuous Send and Track plugin for Outlook must be disabled.

**Rule ID:** `SV-213123r766529_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When enabled, the Adobe Send and Track button appears in Outlook. When an email is composed it enables the ability to send large files as public links through Outlook. The attached files can be uploaded to the Adobe Document Cloud and public links to the files are inserted in the email body.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Note: The Key Name "cCloud" is not created by default in the Acrobat Pro DC install and must be created. Using the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown\cCloud Value Name: bAdobeSendPluginToggle Type: REG_DWORD Value: 1 If the value for bAdobeSendPluginToggle is not set to “1” and Type is not configured to REG_DWORD or does not exist, this is a finding. Admin Template path: Computer Configuration > Administrative Templates > Adobe Acrobat Pro DC Continuous > Preferences > 'Send and Track plugin' must be set to 'Disabled'.

## Group: SRG-APP-000380

**Group ID:** `V-213124`

### Rule: Adobe Acrobat Pro DC Continuous privileged file and folder locations must be disabled.

**Rule ID:** `SV-213124r766532_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Privileged Locations are the primary method Acrobat uses to allow users and admins to specify trusted content that should be exempt from security restrictions, such as when Enhanced Security is enabled. A Privileged Location may be a file, folder, or a host. If the user is allowed to set a Privileged Location, they could bypass security protections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Using the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown Value Name: bDisableTrustedFolders Type: REG_DWORD Value: 1 If the value for bDisableTrustedFolders is not set to “1” and Type is not configured to REG_DWORD or does not exist, this is a finding. GUI path: Edit > Preferences > Security (Enhanced) > In the 'Privileged Locations' section, verify 'Add Folder Path' option is greyed out (locked). If this option is not greyed out, this is a finding. Admin Template path: Computer Configuration > Administrative Templates > Adobe Acrobat Pro DC Continuous > Preferences > Security (Enhanced) > 'Privileged folder locations' must be set to 'Disabled'.

## Group: SRG-APP-000427

**Group ID:** `V-213126`

### Rule: Adobe Acrobat Pro DC Continuous periodic downloading of Adobe European certificates must be disabled.

**Rule ID:** `SV-213126r766535_rule`
**Severity:** low

**Description:**
<VulnDiscussion>By default, the user can update Adobe European certificates from an Adobe server through the GUI. When updating Adobe European certificates is disabled, it prevents the automatic download and installation of certificates and disables and locks the end user's ability to download those certificates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Note: The Key Name "cEUTLDownload" is not created by default in the Acrobat Pro DC install and must be created. Using the Registry Editor, navigate to the following: HKEY_CURRENT_USER\Software\Adobe\Adobe Acrobat\DC\Security\cDigSig\cEUTLDownload Value Name: bLoadSettingsFromURL Type: REG_DWORD Value: 0 If the value for bLoadSettingsFromURL is not set to “0” and Type is not configured to REG_DWORD or does not exist, this is a finding. GUI path: Edit > Preferences > Trust Manager > In the 'Automatic European Union Trusted Lists (EUTL) updates' section > Verify the 'Load trusted certificates from an Adobe EUTL server' is not checked. If the box is checked, this is a finding. Admin Template path: User Configuration > Administrative Templates > Adobe Acrobat Pro DC Continuous > Preferences > Trust Manager > 'Load trusted certificates from an Adobe EUTL server' must be set to 'Disabled'.

## Group: SRG-APP-000431

**Group ID:** `V-213127`

### Rule: Adobe Acrobat Pro DC Continuous Protected Mode must be enabled.

**Rule ID:** `SV-213127r766538_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protected Mode is a “sandbox” that is essentially a read-only mode. When enabled, Acrobat allows the execution environment of untrusted PDF's and the processes the PDF may invoke but also presumes all PDFs are potentially malicious and confines processing to a restricted sandbox.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Using the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown Value Name: bProtectedMode Type: REG_DWORD Value: 1 If the value for bProtectedMode is not set to “1” and Type is not configured to REG_DWORD or does not exist, this is a finding. Admin Template path: Computer Configuration > Administrative Templates > Adobe Acrobat Pro DC Continuous > Preferences > 'Protected Mode' must be set to 'Enabled'.

## Group: SRG-APP-000431

**Group ID:** `V-213128`

### Rule: Adobe Acrobat Pro DC Continuous Protected View must be enabled.

**Rule ID:** `SV-213128r766541_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protected View is a “super-sandbox” that is essentially a read-only mode. When enabled, Acrobat strictly confines the execution environment of untrusted PDF's and the processes the PDF may invoke. Acrobat also assumes all PDFs are potentially malicious and confines processing to a restricted sandbox. When the PDF is opened, the user is presented with the option to trust the document. When the user chooses to trust the document, all features are enabled, this action assigns trust to the document and adds the document to the users’ list of Privileged Locations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Using the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown Value Name: iProtectedView Type: REG_DWORD Value: 2 If the value for iProtectedView is not set to “2” and Type is not configured to REG_DWORD or does not exist, this is a finding. GUI path: Edit > Preferences > Security (Enhanced) > In the 'Protected View' section, verify the radio button for 'All files' is checked and greyed out (locked). If the button is not checked nor greyed out, this is a finding. Admin Template path: Computer Configuration > Administrative Template > Adobe Acrobat Pro DC Continuous > Preferences > Security (Enhanced) > 'Protected View' must be set to 'Enabled' and 'All files' selected in the drop down box.

## Group: SRG-APP-000456

**Group ID:** `V-213129`

### Rule: The Adobe Acrobat Pro DC Continuous latest security-related software updates must be installed.

**Rule ID:** `SV-213129r400525_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open Adobe Acrobat Pro DC. Navigate to and click on Help >> About Adobe Acrobat Pro DC. Verify that the latest security-related software updates by Adobe are being applied. If the latest security-related software updates by Adobe are not being applied, this is a finding.

## Group: SRG-APP-000133

**Group ID:** `V-213130`

### Rule: Adobe Acrobat Pro DC Continuous Default Handler changes must be disabled.

**Rule ID:** `SV-213130r766544_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Acrobat Pro allows users to change the version of Acrobat Pro that is used to read PDF files. This is a risk if multiple versions of Acrobat are installed on the system and the other version has dissimilar security configurations or known vulnerabilities. When the Default PDF Handler is disabled, the end users will not be able to change the default PDF viewer.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Using the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown Value Name: bDisablePDFHandlerSwitching Type: REG_DWORD Value: 1 If the value for bDisablePDFHandlerSwitching is not set to “1” and Type is not configured to REG_DWORD or does not exist, this is a finding. GUI path: Edit > Preferences > General > Verify the 'Select As Default PDF Handler' option is greyed out (locked). If the option is not greyed out, this is a finding. Admin Template path: Computer Configuration > Administrative Template > Adobe Acrobat Pro DC Continuous > Preferences > General > 'Disable PDF handler switching' must be set to 'Enabled'.

## Group: SRG-APP-000141

**Group ID:** `V-213131`

### Rule: Adobe Acrobat Pro DC Continuous must disable the ability to store files on Acrobat.com.

**Rule ID:** `SV-213131r766547_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Adobe Acrobat Pro DC provides the ability to store PDF files on Adobe.com servers. Allowing users to store files on non-DoD systems introduces risk of data compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Note: The Key Name "cCloud" is not created by default in the Acrobat Pro DC install and must be created. Using the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown\cCloud Value Name: bDisableADCFileStore Type: REG_DWORD Value: 1 If the value for bDisableADCFileStore is not set to “1” and Type is not configured to REG_DWORD or does not exist, this is a finding. Admin Template path: Computer Configuration > Administrative Template > Adobe Acrobat Pro DC Continuous > Preferences > 'Store files on Adobe.com' must be set to 'Disabled'.

## Group: SRG-APP-000141

**Group ID:** `V-213132`

### Rule: Adobe Acrobat Pro DC Continuous Cloud Synchronization must be disabled.

**Rule ID:** `SV-213132r766550_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, Adobe online services are tightly integrated in Adobe Acrobat. When the Adobe Cloud synchronization is disabled it prevents the synchronization of desktop preferences across devices on which the user is signed in with an Adobe ID (including phones).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Using the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown\cServices Value Name: bTogglePrefsSync Type: REG_DWORD Value: 1 If the value for bTogglePrefsSync is not set to “1” and Type is not configured to REG_DWORD or does not exist, this is a finding. Admin Template path: Computer Configuration > Administrative Template > Adobe Acrobat Pro DC Continuous > Preferences > 'Cloud Synchronization' must be set to 'Disabled'.

## Group: SRG-APP-000141

**Group ID:** `V-213133`

### Rule: Adobe Acrobat Pro DC Continuous Repair Installation must be disabled.

**Rule ID:** `SV-213133r766553_rule`
**Severity:** low

**Description:**
<VulnDiscussion>When Repair Installation is disabled the user does not have the option (Help Menu) or ability to repair an Adobe Acrobat Pro DC install. Ability to repair includes the risk that established security settings could be overwritten.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Using the Registry Editor, navigate to the following: For 32 bit: HKEY_LOCAL_MACHINE\Software\Adobe\Adobe Acrobat\DC\Installer For 64 bit: HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Adobe\Adobe Acrobat\DC\Installer Value Name: DisableMaintenance Type: REG_DWORD Value: 1 If the value for DisableMaintenance is not set to “1” and Type is not configured to REG_DWORD or does not exist, this is a finding. GUI path: Help > Verify the option 'Repair Installation' is greyed out (locked). If the option is not greyed out, this is a finding. Admin Template path: Computer Configuration > Administrative Template > Adobe Acrobat Pro DC Continuous > Preferences > Help > 'Repair Installation on 32/64 bit' must be set to 'Disabled'.

## Group: SRG-APP-000141

**Group ID:** `V-213134`

### Rule: Adobe Acrobat Pro DC Continuous third-party web connectors must be disabled.

**Rule ID:** `SV-213134r766556_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Third-party connectors include services such as Dropbox and Google Drive. When third-party web connectors are disabled, it prevents access to third-party services for file storage. Allowing access to online storage services introduces the risk of data loss or data exfiltration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Using the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown\cServices Value Name: bToggleWebConnectors Type: REG_DWORD Value: 1 If the value for bToggleWebConnectors is not set to “1” and Type is not configured to REG_DWORD or does not exist, this is a finding. Admin Template path: Computer Configuration > Administrative Template > Adobe Acrobat Pro DC Continuous > Preferences > 'Third-party web connectors' must be set to 'Disabled'.

## Group: SRG-APP-000141

**Group ID:** `V-213135`

### Rule: Adobe Acrobat Pro DC Continuous Webmail must be disabled.

**Rule ID:** `SV-213135r766559_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Acrobat Pro DC provides a Webmail capability. This allows users to send PDFs as email attachments using any mail account that supports SMTP/IMAP protocols. In addition to existing desktop email clients, users can now configure these mail accounts by providing User Name, Password, IMAP and SMTP details. The capability allows users to utilize Gmail and Yahoo mail accounts to send PDF files directly from within the Acrobat application. This capability allows the user to by-pass existing email protections provided by DoD email services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Using the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown\cWebmailProfiles Value Name: bDisableWebmail Type: REG_DWORD Value: 1 If the value for bDisableWebmail is not set to “1” and Type is not configured to REG_DWORD or does not exist, this is a finding. Admin Template path: Computer Configuration > Administrative Template > Adobe Acrobat Pro DC Continuous > Preferences > 'WebMail' must be set to 'Disabled'.

## Group: SRG-APP-000141

**Group ID:** `V-213136`

### Rule: The Adobe Acrobat Pro DC Continuous Welcome Screen must be disabled.

**Rule ID:** `SV-213136r766562_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Adobe Welcome screen can be distracting. It provides marketing material and also has online links to the Adobe quick tips website, tutorials, blogs, and community forums. When the Adobe Welcome screen is disabled, the Welcome screen will not be populated on application startup.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Note: The Key Name "cWelcomeScreen" is not created by default in the Acrobat Pro DC install and must be created. Using the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown\cWelcomeScreen Value Name: bShowWelcomeScreen Type: REG_DWORD Value: 0 If the value for bShowWelcomeScreen is not set to “0” and Type is not configured to REG_DWORD or does not exist, this is a finding. Admin Template path: Computer Configuration > Administrative Template > Adobe Acrobat Pro DC Continuous > Preferences > 'Welcome Screen' must be set to 'Disabled'.

## Group: SRG-APP-000141

**Group ID:** `V-213137`

### Rule: Adobe Acrobat Pro DC Continuous SharePoint and Office365 access must be disabled.

**Rule ID:** `SV-213137r766565_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Both SharePoint and Office365 configurations are shared in one setting. Disabling this setting removes the user’s ability to use both SharePoint and Office365 cloud features and functions. If the user is allowed to store files on public cloud services, there is a risk of data compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
NOTE: If configured to an approved DoD SharePoint Server, this is NA. Verify the following registry configuration: Note: The Key Name "cSharePoint" is not created by default in the Acrobat Pro DC install and must be created. Using the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown\cSharePoint Value Name: bDisableSharePointFeatures Type: REG_DWORD Value: 1 If the value for bDisableSharePointFeatures is not set to “1” and Type is not configured to REG_DWORD or does not exist, this is a finding. Admin Template path: Computer Configuration > Administrative Template > Adobe Acrobat Pro DC Continuous > Preferences > 'SharePoint and Office 365 access' must be set to 'Disabled'.

## Group: SRG-APP-000427

**Group ID:** `V-213138`

### Rule: Adobe Acrobat Pro DC Continuous Periodic downloading of Adobe certificates must be disabled.

**Rule ID:** `SV-213138r766568_rule`
**Severity:** low

**Description:**
<VulnDiscussion>By default, the user can update Adobe certificates from an Adobe server through the GUI. When updating Adobe certificates is disabled, it prevents the automatic download and installation of certificates and disables and locks the end user's ability to download those certificates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Using the Registry Editor, navigate to the following: HKEY_CURRENT_USER\Software\Adobe\Adobe Acrobat\DC\Security\cDigSig\cAdobeDownload Value Name: bLoadSettingsFromURL Type: REG_DWORD Value: 0 If the value for bLoadSettingsFromURL is not set to “0” and Type is not configured to REG_DWORD or does not exist, this is a finding. GUI path: Edit > Preferences > Trust Manager > In the 'Automatic Adobe Approved Trust List (AATL) Updates' section > verify the 'Load trusted certificates from an Adobe AATL server' is not checked. If the box is checked, this is a finding. Admin Template path: User Configuration > Administrative Templates > Adobe Acrobat Pro DC Continuous > Preferences > Trust Manager > 'Load trusted certificates from an Adobe AATL server' must be set to 'Disabled'.

## Group: SRG-APP-000380

**Group ID:** `V-213139`

### Rule: Adobe Acrobat Pro DC Continuous privileged host locations must be disabled.

**Rule ID:** `SV-213139r766571_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Privileged Locations are the primary method Acrobat uses to allow users and admins to specify trusted content that should be exempt from security restrictions, such as when Enhanced Security is enabled. A Privileged Location may be a file, folder, or a host. If the user is allowed to set a Privileged Location, they could bypass security protections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Using the Registry Editor, navigate to the following: HKEY_LOCAL_MACHINE\Software\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown Value Name: bDisableTrustedSites Type: REG_DWORD Value: 1 If the value for bDisableTrustedSites is not set to “1” and Type is not configured to REG_DWORD or does not exist, this is a finding. GUI path: Edit > Preferences > Security (Enhanced) > In the 'Privileged Locations' section, verify 'Add Host' option is greyed out (locked). If the option is not greyed out, this is a finding. Admin Template path: Computer Configuration > Administrative Templates > Adobe Acrobat Pro DC Continuous > Preferences > Security (Enhanced) > 'Privileged host locations' must be set to 'Disabled'.

## Group: SRG-APP-000416

**Group ID:** `V-245874`

### Rule: Adobe Acrobat Pro DC Continuous FIPS mode must be enabled.

**Rule ID:** `SV-245874r766580_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following registry configuration: Using the Registry Editor, navigate to the following: HKEY_CURRENT_USER\Software\Adobe\Adobe Acrobat\DC\AVGeneral Value Name: bFIPSMode Type: REG_DWORD Value: 1 If the value for bFIPSMode is not set to “1” and Type is not configured to REG_DWORD or does not exist, this is a finding. Admin Template path: User Configuration > Administrative Templates > Adobe Acrobat Pro DC Continuous > Preferences > 'Enable FIPS' must be set to 'Enabled'.

