# STIG Benchmark: Microsoft Excel 2016 Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000210

**Group ID:** `V-238155`

### Rule: Disabling of user name and password syntax from being used in URLs must be enforced.


**Rule ID:** `SV-238155r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Uniform Resource Locator (URL) standard allows user authentication to be included in URL strings in the form http://username:password@example.com. A malicious user might use this URL syntax to create a hyperlink that appears to open a legitimate website but actually opens a deceptive (spoofed) website. For example, the URL http://www.wingtiptoys.com@example.com appears to open http://www.wingtiptoys.com but actually opens http://example.com. To protect users from such attacks, Internet Explorer usually blocks any URLs using this syntax. This functionality can be controlled separately for instances of Internet Explorer spawned by Office applications (for example, if a user clicks a link in an Office document or selects a menu option that loads a website). If user names and passwords in URLs are allowed, users could be diverted to dangerous Web pages, which could pose a security risk.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Disable user name and password" is set to "Enabled" and 'excel.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_HTTP_USERNAME_PASSWORD_DISABLE Criteria: If the value excel.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-238156`

### Rule: Open/Save actions for Excel 4 macrosheets and add-in files must be blocked.


**Rule ID:** `SV-238156r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to determine whether users can open, view, edit, or save Excel files with the format specified by the title of this policy setting. If you enable this policy setting, you can specify whether users can open, view, edit, or save files. The options that can be selected are below. Note: Not all options may be available for this policy setting.- Do not block: The file type will not be blocked.- Save blocked: Saving of the file type will be blocked.- Open/Save blocked, use open policy: Both opening and saving of the file type will be blocked. The file will open based on the policy setting configured in the "default file block behavior" key.- Block: Both opening and saving of the file type will be blocked, and the file will not open.- Open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit the file type will not be enabled.- Allow editing and open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit will be enabled. If you disable or do not configure this policy setting, the file type will be blocked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center -> File Block Settings "Excel 4 macrosheets and add-in files" is set to "Enabled: Open/Save blocked, use open policy". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security\fileblock Criteria: If the value XL4Macros is REG_DWORD = 2, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-238157`

### Rule: Open/Save actions for Excel 4 workbooks must be blocked.


**Rule ID:** `SV-238157r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to determine whether users can open, view, edit, or save Excel files with the format specified by the title of this policy setting. If you enable this policy setting, you can specify whether users can open, view, edit, or save files. The options that can be selected are below. Note: Not all options may be available for this policy setting.- Do not block: The file type will not be blocked.- Save blocked: Saving of the file type will be blocked.- Open/Save blocked, use open policy: Both opening and saving of the file type will be blocked. The file will open based on the policy setting configured in the "default file block behavior" key.- Block: Both opening and saving of the file type will be blocked, and the file will not open.- Open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit the file type will not be enabled.- Allow editing and open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit will be enabled. If you disable or do not configure this policy setting, the file type will be blocked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center -> File Block Settings "Excel 4 workbooks" is set to "Enabled: Open/Save blocked, use open policy". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security\fileblock Criteria: If the value XL4Workbooks is REG_DWORD = 2, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-238158`

### Rule: Open/Save actions for Excel 4 worksheets must be blocked.


**Rule ID:** `SV-238158r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to determine whether users can open, view, edit, or save Excel files with the format specified by the title of this policy setting. If you enable this policy setting, you can specify whether users can open, view, edit, or save files. The options that can be selected are below. Note: Not all options may be available for this policy setting.- Do not block: The file type will not be blocked.- Save blocked: Saving of the file type will be blocked.- Open/Save blocked, use open policy: Both opening and saving of the file type will be blocked. The file will open based on the policy setting configured in the "default file block behavior" key.- Block: Both opening and saving of the file type will be blocked, and the file will not open.- Open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit the file type will not be enabled.- Allow editing and open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit will be enabled. If you disable or do not configure this policy setting, the file type will be blocked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center -> File Block Settings "Excel 4 worksheets" is set to "Enabled: Open/Save blocked, use open policy". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security\fileblock Criteria: If the value XL4Worksheets is REG_DWORD = 2, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-238159`

### Rule: Actions for Excel 95 workbooks must be configured to edit in Protected View.


**Rule ID:** `SV-238159r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to determine whether users can open, view, edit, or save Excel files with the format specified by the title of this policy setting. If you enable this policy setting, you can specify whether users can open, view, edit, or save files. The options that can be selected are below. Note: Not all options may be available for this policy setting.- Do not block: The file type will not be blocked.- Save blocked: Saving of the file type will be blocked.- Open/Save blocked, use open policy: Both opening and saving of the file type will be blocked. The file will open based on the policy setting configured in the "default file block behavior" key.- Block: Both opening and saving of the file type will be blocked, and the file will not open.- Open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit the file type will not be enabled.- Allow editing and open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit will be enabled. If you disable or do not configure this policy setting, the file type will not be blocked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center -> File Block Settings "Excel 95 workbooks" is set to "Enabled: Allow editing and open in Protected View". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security\fileblock Criteria: If the value XL95Workbooks is REG_DWORD = 5, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-238160`

### Rule: Actions for Excel 95-97 workbooks and templates must be configured to edit in Protected View.


**Rule ID:** `SV-238160r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to determine whether users can open, view, edit, or save Excel files with the format specified by the title of this policy setting. If you enable this policy setting, you can specify whether users can open, view, edit, or save files. The options that can be selected are below. Note: Not all options may be available for this policy setting.- Do not block: The file type will not be blocked.- Save blocked: Saving of the file type will be blocked.- Open/Save blocked, use open policy: Both opening and saving of the file type will be blocked. The file will open based on the policy setting configured in the "default file block behavior" key.- Block: Both opening and saving of the file type will be blocked, and the file will not open.- Open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit the file type will not be enabled.- Allow editing and open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit will be enabled. If you disable or do not configure this policy setting, the file type will not be blocked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center -> File Block Settings "Excel 95-97 workbooks and templates" is set to "Enabled: Allow editing and open in Protected View". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\office\16.0\excel\security\fileblock Criteria: If the value XL9597WorkbooksandTemplates is REG_DWORD = 5, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-238161`

### Rule: Blocking as default file block opening behavior must be enforced.


**Rule ID:** `SV-238161r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to determine if users can open, view, or edit Excel files. If you enable this policy setting, you can set one of these options:- Blocked files are not opened- Blocked files open in Protected View and can not be edited- Blocked files open in Protected View and can be edited. If you disable or do not configure this policy setting, the behavior is the same as the "Blocked files are not opened" setting. Users will not be able to open blocked files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center -> File Block Settings "Set default file block behavior" is set to "Enabled: Blocked files are not opened". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security\fileblock Criteria: If the value OpenInProtectedView is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000112

**Group ID:** `V-238162`

### Rule: Enabling IE Bind to Object functionality must be present.


**Rule ID:** `SV-238162r879573_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Explorer performs a number of safety checks before initializing an ActiveX control. It will not initialize a control if the kill bit for the control is set in the registry, or if the security settings for the zone in which the control is located do not allow it to be initialized. This functionality can be controlled separately for instances of Internet Explorer spawned by Office applications (for example, if a user clicks a link in an Office document or selects a menu option that loads a web page). A security risk could occur if potentially dangerous controls are allowed to load.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Bind to Object" is set to "Enabled" and 'excel.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_SAFE_BINDTOOBJECT Criteria: If the value excel.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-238163`

### Rule: Open/Save actions for Dif and Sylk files must be blocked.


**Rule ID:** `SV-238163r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to determine whether users can open, view, edit, or save Excel files with the format specified by the title of this policy setting. If you enable this policy setting, you can specify whether users can open, view, edit, or save files. The options that can be selected are below. Note: Not all options may be available for this policy setting.- Do not block: The file type will not be blocked.- Save blocked: Saving of the file type will be blocked.- Open/Save blocked, use open policy: Both opening and saving of the file type will be blocked. The file will open based on the policy setting configured in the "default file block behavior" key.- Block: Both opening and saving of the file type will be blocked, and the file will not open.- Open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit the file type will not be enabled.- Allow editing and open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit will be enabled. If you disable or do not configure this policy setting, the file type will not be blocked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center -> File Block Settings "Dif and Sylk files" is set to "Enabled: Open/Save blocked, use open policy". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security\fileblock Criteria: If the value DifandSylkFiles is REG_DWORD = 2, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-238164`

### Rule: Open/Save actions for Excel 2 macrosheets and add-in files must be blocked.


**Rule ID:** `SV-238164r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to determine whether users can open, view, edit, or save Excel files with the format specified by the title of this policy setting. If you enable this policy setting, you can specify whether users can open, view, edit, or save files. The options that can be selected are below. Note: Not all options may be available for this policy setting.- Do not block: The file type will not be blocked.- Save blocked: Saving of the file type will be blocked.- Open/Save blocked, use open policy: Both opening and saving of the file type will be blocked. The file will open based on the policy setting configured in the "default file block behavior" key.- Block: Both opening and saving of the file type will be blocked, and the file will not open.- Open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit the file type will not be enabled.- Allow editing and open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit will be enabled. If you disable or do not configure this policy setting, the file type will be blocked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center -> File Block Settings "Excel 2 macrosheets and add-in files" is set to "Enabled: Open/Save blocked, use open policy". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security\fileblock Criteria: If the value XL2Macros is REG_DWORD = 2, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-238165`

### Rule: Open/Save actions for Excel 2 worksheets must be blocked.


**Rule ID:** `SV-238165r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to determine whether users can open, view, edit, or save Excel files with the format specified by the title of this policy setting. If you enable this policy setting, you can specify whether users can open, view, edit, or save files. The options that can be selected are below. Note: Not all options may be available for this policy setting.- Do not block: The file type will not be blocked.- Save blocked: Saving of the file type will be blocked.- Open/Save blocked, use open policy: Both opening and saving of the file type will be blocked. The file will open based on the policy setting configured in the "default file block behavior" key.- Block: Both opening and saving of the file type will be blocked, and the file will not open.- Open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit the file type will not be enabled.- Allow editing and open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit will be enabled. If you disable or do not configure this policy setting, the file type will be blocked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center -> File Block Settings "Excel 2 worksheets" is set to "Enabled: Open/Save blocked, use open policy". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security\fileblock Criteria: If the value XL2Worksheets is REG_DWORD = 2, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-238166`

### Rule: Open/Save actions for Excel 3 macrosheets and add-in files must be blocked.


**Rule ID:** `SV-238166r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to determine whether users can open, view, edit, or save Excel files with the format specified by the title of this policy setting. If you enable this policy setting, you can specify whether users can open, view, edit, or save files. The options that can be selected are below. Note: Not all options may be available for this policy setting.- Do not block: The file type will not be blocked.- Save blocked: Saving of the file type will be blocked.- Open/Save blocked, use open policy: Both opening and saving of the file type will be blocked. The file will open based on the policy setting configured in the "default file block behavior" key.- Block: Both opening and saving of the file type will be blocked, and the file will not open.- Open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit the file type will not be enabled.- Allow editing and open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit will be enabled. If you disable or do not configure this policy setting, the file type will be blocked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center -> File Block Settings "Excel 3 macrosheets and add-in files" is set to "Enabled: Open/Save blocked, use open policy". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security\fileblock Criteria: If the value XL3Macros is REG_DWORD = 2, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-238167`

### Rule: Open/Save actions for Excel 3 worksheets must be blocked.


**Rule ID:** `SV-238167r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to determine whether users can open, view, edit, or save Excel files with the format specified by the title of this policy setting. If you enable this policy setting, you can specify whether users can open, view, edit, or save files. The options that can be selected are below. Note: Not all options may be available for this policy setting.- Do not block: The file type will not be blocked.- Save blocked: Saving of the file type will be blocked.- Open/Save blocked, use open policy: Both opening and saving of the file type will be blocked. The file will open based on the policy setting configured in the "default file block behavior" key.- Block: Both opening and saving of the file type will be blocked, and the file will not open.- Open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit the file type will not be enabled.- Allow editing and open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit will be enabled. If you disable or do not configure this policy setting, the file type will be blocked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center -> File Block Settings "Excel 3 worksheets" is set to "Enabled: Open/Save blocked, use open policy". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security\fileblock Criteria: If the value XL3Worksheets is REG_DWORD = 2, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-238168`

### Rule: Saved from URL mark to assure Internet zone processing must be enforced.


**Rule ID:** `SV-238168r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Typically, when Internet Explorer loads a web page from a Universal Naming Convention (UNC) share that contains a Mark of the Web (MOTW) comment, indicating the page was saved from a site on the Internet, Internet Explorer runs the page in the Internet security zone instead of the less restrictive Local Intranet security zone. This functionality can be controlled separately for instances of Internet Explorer spawned by Office applications (for example, if a user clicks a link in an Office document or selects a menu option that loads a web page). If Internet Explorer does not evaluate the page for a MOTW, potentially dangerous code could be allowed to run.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Saved from URL" is set to "Enabled" and 'excel.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_UNC_SAVEDFILECHECK Criteria: If the value excel.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000112

**Group ID:** `V-238169`

### Rule: Configuration for file validation must be enforced.


**Rule ID:** `SV-238169r879573_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to turn off the file validation feature. If you enable this policy setting, file validation will be turned off. If you disable or do not configure this policy setting, file validation will be turned on. Office Binary Documents (97-2003) are checked to see if they conform against the file format schema before they are opened.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration >> Administrative Templates >> Microsoft Excel 2016 >> Excel Options >> Security "Turn off file validation" is set to "Disabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security\filevalidation Criteria: If the value EnableOnLoad is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-238170`

### Rule: Open/Save actions for web pages and Excel 2003 XML spreadsheets must be blocked.


**Rule ID:** `SV-238170r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to determine whether users can open, view, edit, or save Excel files with the format specified by the title of this policy setting. If you enable this policy setting, you can specify whether users can open, view, edit, or save files. The options that can be selected are below. Note: Not all options may be available for this policy setting.- Do not block: The file type will not be blocked.- Save blocked: Saving of the file type will be blocked.- Open/Save blocked, use open policy: Both opening and saving of the file type will be blocked. The file will open based on the policy setting configured in the "default file block behavior" key.- Block: Both opening and saving of the file type will be blocked, and the file will not open.- Open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit the file type will not be enabled.- Allow editing and open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit will be enabled. If you disable or do not configure this policy setting, the file type will not be blocked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center -> File Block Settings "Web pages and Excel 2003 XML spreadsheets" is set to "Enabled: Open/Save blocked, use open policy". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security\fileblock Criteria: If the value HtmlandXmlssFiles is REG_DWORD = 2, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-238171`

### Rule: Files from the Internet zone must be opened in Protected View.


**Rule ID:** `SV-238171r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to determine if files downloaded from the Internet zone open in Protected View. If you enable this policy setting, files downloaded from the Internet zone do not open in Protected View. If you disable or do not configure this policy setting, files downloaded from the Internet zone open in Protected View.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center -> Protected View "Do not open files from the Internet zone in Protected View" is set to "Not Configured" or "Disabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security\protectedview Criteria: If the value DisableInternetFilesInPV is REG_DWORD = 0, this is not a finding. If the value does not exist, this is not a finding. If the value is REG_DWORD = 1, then this is a finding.

## Group: SRG-APP-000207

**Group ID:** `V-238172`

### Rule: Open/Save actions for dBase III / IV files must be blocked.


**Rule ID:** `SV-238172r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to determine whether users can open, view, edit, or save Excel files with the format specified by the title of this policy setting. If you enable this policy setting, you can specify whether users can open, view, edit, or save files. The options that can be selected are below. Note: Not all options may be available for this policy setting.- Do not block: The file type will not be blocked.- Save blocked: Saving of the file type will be blocked.- Open/Save blocked, use open policy: Both opening and saving of the file type will be blocked. The file will open based on the policy setting configured in the "default file block behavior" key.- Block: Both opening and saving of the file type will be blocked, and the file will not open.- Open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit the file type will not be enabled.- Allow editing and open in Protected View: Both opening and saving of the file type will be blocked, and the option to edit will be enabled. If you disable or do not configure this policy setting, the file type will not be blocked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center -> File Block Settings "dBase III / IV files" is set to "Enabled: Open/Save blocked, use open policy". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security\fileblock Criteria: If the value DBaseFiles is REG_DWORD = 2, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-238173`

### Rule: Navigation to URLs embedded in Office products must be blocked.


**Rule ID:** `SV-238173r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To protect users from attacks, Internet Explorer usually does not attempt to load malformed URLs. This functionality can be controlled separately for instances of Internet Explorer spawned by Office applications (for example, if a user clicks a link in an Office document or selects a menu option that loads a web page). If Internet Explorer attempts to load a malformed URL, a security risk could occur.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Navigate URL" is set to "Enabled" and 'excel.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_VALIDATE_NAVIGATE_URL Criteria: If the value excel.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000112

**Group ID:** `V-238174`

### Rule: Scripted Window Security must be enforced.


**Rule ID:** `SV-238174r879573_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious websites often try to confuse or trick users into giving a site permission to perform an action allowing the site to take control of the users' computers in some manner. Disabling or not configuring this setting allows unknown websites to: -Create browser windows appearing to be from the local operating system. -Draw active windows displaying outside of the viewable areas of the screen capturing keyboard input. -Overlay parent windows with their own browser windows to hide important system information, choices or prompts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Scripted Window Security Restrictions" is set to "Enabled" and 'excel.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_WINDOW_RESTRICTIONS Criteria: If the value excel.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-238175`

### Rule: Add-on Management functionality must be allowed.


**Rule ID:** `SV-238175r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Explorer add-ons are pieces of code, run in Internet Explorer, to provide additional functionality. Rogue add-ons may contain viruses or other malicious code. Disabling or not configuring this setting could allow malicious code or users to become active on user computers or the network. For example, a malicious user can monitor and then use keystrokes users type into Internet Explorer. Even legitimate add-ons may demand resources, compromising the performance of Internet Explorer, and the operating systems for user computers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Add-on Management" is set to "Enabled" and 'excel.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_ADDON_MANAGEMENT Criteria: If the value excel.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000131

**Group ID:** `V-238176`

### Rule: Add-ins to Office applications must be signed by a Trusted Publisher.


**Rule ID:** `SV-238176r879584_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls whether add-ins for the specified Office 2016 applications must be digitally signed by a trusted publisher. If you enable this policy setting, this application checks the digital signature for each add-in before loading it. If an add-in does not have a digital signature, or if the signature did not come from a trusted publisher, this application disables the add-in and notifies the user. Certificates must be added to the Trusted Publishers list if you require that all add-ins be signed by a trusted publisher. For detail on about obtaining and distributing certificates, see http://go.microsoft.com/fwlink/?LinkId=294922. Office 2016 stores certificates for trusted publishers in the Internet Explorer trusted publisher store. Earlier versions of Microsoft Office stored trusted publisher certificate information (specifically, the certificate thumbprint) in a special Office trusted publisher store. Office 2016 still reads trusted publisher certificate information from the Office trusted publisher store, but it does not write information to this store. Therefore, if you created a list of trusted publishers in a previous version of Office and you upgrade to Office 2016, your trusted publisher list will still be recognized. However, any trusted publisher certificates that you add to the list will be stored in the Internet Explorer trusted publisher store. For more information about trusted publishers, see the Office Resource Kit. If you disable or do not configure this policy setting, Office 2016 applications do not check the digital signature on application add-ins before opening them. If a dangerous add-in is loaded, it could harm users' computers or compromise data security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center "Require that application add-ins are signed by Trusted Publisher" is set to "Enabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security Criteria: If the value RequireAddinSig is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-238177`

### Rule: Links that invoke instances of Internet Explorer from within an Office product must be blocked.


**Rule ID:** `SV-238177r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Pop-up Blocker feature in Internet Explorer can be used to block most unwanted pop-up and pop-under windows from appearing. This functionality can be controlled separately for instances of Internet Explorer spawned by Office applications (for example, if a user clicks a link in an Office document or selects a menu option that loads a web page). If the Pop-up Blocker is disabled, disruptive and potentially dangerous pop-up windows could load and present a security risk.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Block popups" is set to "Enabled" and 'excel.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_WEBOC_POPUPMANAGEMENT Criteria: If the value excel.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000131

**Group ID:** `V-238178`

### Rule: Trust Bar Notifications for unsigned application add-ins must be blocked.


**Rule ID:** `SV-238178r879584_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls whether the specified Office 2016 applications notify users when unsigned application add-ins are loaded or silently disable such add-ins without notification. This policy setting only applies if you enable the ''Require that application add-ins are signed by Trusted Publisher'' policy setting, which prevents users from changing this policy setting. If you enable this policy setting, applications automatically disable unsigned add-ins without informing users. If you disable this policy setting, if an application is configured to require that all add-ins be signed by a trusted publisher, any unsigned add-ins the application loads will be disabled and the application will display the Trust Bar at the top of the active window. The Trust Bar contains a message that informs users about the unsigned add-in. If you do not configure this policy setting, the disable behavior applies, and in addition, users can configure this requirement themselves in the ''Add-ins'' category of the Trust Center for the application.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center "Disable Trust Bar Notification for unsigned application add-ins and block them" is set to "Enabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security Criteria: If the value NoTBPromptUnsignedAddin is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000209

**Group ID:** `V-238179`

### Rule: File Downloads must be configured for proper restrictions.


**Rule ID:** `SV-238179r879629_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Disabling this setting allows websites to present file download prompts via code without the user specifically initiating the download. User preferences may also allow the download to occur without prompting or interaction with the user. Even if Internet Explorer prompts the user to accept the download, some websites abuse this functionality. Malicious websites may continually prompt users to download a file or present confusing dialog boxes to trick users into downloading or running a file. If the download occurs and it contains malicious code, the code could become active on user computers or the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Restrict File Download" is set to "Enabled" and 'excel.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_RESTRICT_FILEDOWNLOAD Criteria: If the value of excel.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-238180`

### Rule: All automatic loading from trusted locations must be disabled.


**Rule ID:** `SV-238180r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows administrators to disable all trusted locations in the specified applications. Trusted locations specified in the Trust Center are used to define file locations that are assumed to be safe. Content, code, and add-ins are allowed to load from trusted locations with a minimal amount of security, without prompting the users for permission. If a dangerous file is opened from a trusted location, it will not be subject to standard security measures and could harm users' computers or data. If you enable this policy setting, all trusted locations (those specified in the Trust Center) in the specified applications are ignored, including any trusted locations established by Office 2016 during setup, deployed to users using Group Policy, or added by users themselves. Users will be prompted again when opening files from trusted locations. If you disable or do not configure this policy setting, all trusted locations (those specified in the Trust Center) in the specified applications are assumed to be safe.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center -> Trusted Locations "Disable all trusted locations" is set to "Enabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security\trusted locations Criteria: If the value AllLocationsDisabled is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-238181`

### Rule: Disallowance of trusted locations on the network must be enforced.


**Rule ID:** `SV-238181r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls whether trusted locations on the network can be used. If you enable this policy setting, users can specify trusted locations on network shares or in other remote locations that are not under their direct control by clicking the "Add new location" button in the Trusted Locations section of the Trust Center. Content, code, and add-ins are allowed to load from trusted locations with minimal security and without prompting the user for permission. If you disable this policy setting, the selected application ignores any network locations listed in the Trusted Locations section of the Trust Center. If you also deploy Trusted Locations via Group Policy, you should verify whether any of them are remote locations. If any of them are remote locations and you do not allow remote locations via this policy setting, those policy keys that point to remote locations will be ignored on client computers. Disabling this policy setting does not delete any network locations from the Trusted Locations list, but causes disruption for users who add network locations to the Trusted Locations list. Users are also prevented from adding new network locations to the Trusted Locations list in the Trust Center. We recommended that you do not enable this policy setting (as the "Allow Trusted Locations on my network (not recommended)" check box also states). Therefore, in practice, it should be possible to disable this policy setting in most situations without causing significant usability issues for most users. If you do not enable this policy setting, users can select the "Allow Trusted Locations on my network (not recommended)" check box if desired and then specify trusted locations by clicking the "Add new location" button.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center -> Trusted Locations "Allow Trusted Locations on the network" is set to "Disabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security\trusted locations Criteria: If the value AllowNetworkLocations is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-238182`

### Rule: The Save commands default file format must be configured.


**Rule ID:** `SV-238182r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls the default file format for saving workbooks in Excel. If you enable this policy setting, you can set the default file format for Excel from among the following options:- Excel Workbook (.xlsx). This option is the default configuration in Excel 2016.- Excel Macro-Enabled Workbook (.xlsm)- Excel Binary Workbook (.xlsb)- Web Page (.htm; .html)- Excel 97-2003 Workbook (.xls)- Excel 5.0/95 Workbook (.xls)- OpenDocument Spreadsheet (*.ods). Users can choose to save workbooks in a different file format than the default. If you disable or you do not configure this policy setting, Excel saves new workbooks in the Office Open XML format with an .xlsx extension.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Save "default file format" is set to "Enabled: (Excel Workbook *.xlsx)". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\options Criteria: If the value DefaultFormat is REG_DWORD = 0x00000033(hex) or 51 (Decimal), this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-238183`

### Rule: The scanning of encrypted macros in open XML documents must be enforced.


**Rule ID:** `SV-238183r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls whether encrypted macros in Open XML workbooks be are required to be scanned with anti-virus software before being opened. If you enable this policy setting, you may choose one of these options:- Scan encrypted macros: encrypted macros are disabled unless anti-virus software is installed. Encrypted macros are scanned by your anti-virus software when you attempt to open an encrypted workbook that contains macros.- Scan if anti-virus software available: if anti-virus software is installed, scan the encrypted macros first before allowing them to load. If anti-virus software is not available, allow encrypted macros to load.- Load macros without scanning: do not check for anti-virus software and allow macros to be loaded in an encrypted file. If you disable or do not configure this policy setting, the behavior will be similar to the "Scan encrypted macros" option.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security "Scan encrypted macros in Excel Open XML workbooks" is set to "Disabled". The option 'Enabled: Scan encrypted macros (default)' is also an acceptable value. Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security Criteria: If the value ExcelBypassEncryptedMacroScan does not exist, this is not a finding. If the value is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-238184`

### Rule: Macro storage must be in personal macro workbooks.


**Rule ID:** `SV-238184r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls the default location for storing macros in Excel. If this policy setting is enabled, Excel stores macros in users' personal macro workbook. If you disable or do not configure this policy setting, Excel stores macros in the active workbook from which they are created. Note: In the user interface (UI), the "Store macro in" drop down list box in the Record Macro dialog box (Macros | Record Macro) allows users to choose whether to store the new macro in the current workbook, a new workbook, or their personal macro workbook (Personal.xlsb), a hidden workbook that opens every time Excel starts. By default, Excel displays the "Store macro in" box with "This Workbook" already selected in the drop-down list. If a user saves a macro in the active workbook and then distributes the workbook to others, the macro is distributed along with the workbook. If you enable this policy setting, Excel displays the "Store macro in" box with "Personal Macro Workbook" already selected. Users can still select one of the other two options in the drop-down menu.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center "Store macro in Personal Macro Workbook by default" is set to "Enabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\options\binaryoptions Criteria: If the value fGlobalSheet_37_1 is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-238185`

### Rule: Trust access for VBA must be disallowed.


**Rule ID:** `SV-238185r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls whether automation clients such as Microsoft Visual Studio 2005 Tools for Microsoft Office (VSTO) can access the Visual Basic for Applications project system in the specified applications. VSTO projects require access to the Visual Basic for Applications project system in Excel, PowerPoint, and Word, even though the projects do not use Visual Basic for Applications. Design-time support of controls in both Visual Basic and C# projects depends on the Visual Basic for Applications project system in Word and Excel. If you enable this policy setting, VSTO and other automation clients can access the Visual Basic for Applications project system in the specified applications. Users will not be able to change this behavior through the "Trust access to the VBA project object model" user interface option under the Macro Settings section of the Trust Center. If you disable this policy setting, VSTO does not have programmatic access to VBA projects. In addition, the "Trust access to the VBA project object model" check box is cleared and users cannot change it. Note: Disabling this policy setting prevents VSTO projects from interacting properly with the VBA project system in the selected application. If you do not configure this policy setting, automation clients do not have programmatic access to VBA projects. Users can enable this by selecting the "Trust access to the VBA project object model" in the "Macro Settings" section of the Trust Center. However, doing so allows macros in any documents the user opens to access the core Visual Basic objects, methods, and properties, which represents a potential security hazard.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center "Trust access to Visual Basic Project" is set to "Disabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security Criteria: If the value AccessVBOM is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000112

**Group ID:** `V-238186`

### Rule: Protection from zone elevation must be enforced.


**Rule ID:** `SV-238186r879573_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Explorer places restrictions on each web page users can use the browser to open. Web pages on a user's local computer have the fewest security restrictions and reside in the Local Machine zone, making this security zone a prime target for malicious users and code. Disabling or not configuring this setting could allow pages in the Internet zone to navigate to pages in the Local Machine zone to then run code to elevate privileges. This could allow malicious code or users to become active on user computers or the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Protection From Zone Elevation" is set to "Enabled" and 'excel.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_ZONE_ELEVATION Criteria: If the value excel.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000488

**Group ID:** `V-238187`

### Rule: ActiveX Installs must be configured for proper restriction.


**Rule ID:** `SV-238187r879859_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Microsoft ActiveX controls allow unmanaged, unprotected code to run on the user computers. ActiveX controls do not run within a protected container in the browser like the other types of HTML or Microsoft Silverlight-based controls. Disabling or not configuring this setting does not block prompts for ActiveX control installations, and these prompts display to users. This could allow malicious code to become active on user computers or the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Microsoft Office 2016 (Machine) -> Security Settings -> IE Security "Restrict ActiveX Install" is set to "Enabled" and 'excel.exe' is checked. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_RESTRICT_ACTIVEXINSTALL Criteria: If the value excel.exe is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-238188`

### Rule: Files in unsafe locations must be opened in Protected View.


**Rule ID:** `SV-238188r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting lets you determine if files located in unsafe locations will open in Protected View. If you have not specified unsafe locations, only the "Downloaded Program Files" and "Temporary Internet Files" folders are considered unsafe locations. If you enable this policy setting, files located in unsafe locations do not open in Protected View. If you disable or do not configure this policy setting, files located in unsafe locations open in Protected View.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center -> Protected View "Do not open files in unsafe locations in Protected View" is set to "Not Configured" or "Disabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security\protectedview Criteria: If the value DisableUnsafeLocationsInPV is REG_DWORD = 0, this is not a finding. If the value does not exist, this is not a finding. If the value is REG_DWORD = 1, then this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-238189`

### Rule: Document behavior if file validation fails must be set.


**Rule ID:** `SV-238189r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls how Office handles documents when they fail file validation. If you enable this policy setting, you can configure the following options for files that fail file validation:- Block files completely. Users cannot open the files.- Open files in Protected View and disallow edit. Users cannot edit the files. This is also how Office handles the files if you disable this policy setting.- Open files in Protected View and allow edit. Users can edit the files. This is also how Office handles the files if you do not configure this policy setting.If you disable this policy setting, Office follows the "Open files in Protected View and disallow edit" behavior. If you do not configure this policy setting, Office follows the "Open files in Protected View and allow edit" behavior.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center -> Protected View "Set document behavior if file validation fails" is set to "Disabled". The option 'Enabled: Open in Protected View' and Unchecked for 'Do not allow edit' is also an acceptable value. Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security\filevalidation Criteria: If the value openinprotectedview does not exist, this is not a finding. If the value is REG_DWORD = 1, this is not a finding. If the value DisableEditFromPV is set to REG_DWORD = 1, this is not a finding. If the value is set to REG_DWORD = 0, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-238190`

### Rule: Excel attachments opened from Outlook must be in Protected View.


**Rule ID:** `SV-238190r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to determine if Excel files in Outlook attachments open in Protected View. If you enable this policy setting, Outlook attachments do not open in Protected View. If you disable or do not configure this policy setting, Outlook attachments open in Protected View.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center -> Protected View "Turn off Protected View for attachments opened from Outlook" is set to "Disabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\Excel\security\protectedview Criteria: If the value DisableAttachmentsInPV is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-238191`

### Rule: Warning Bar settings for VBA macros must be configured.

**Rule ID:** `SV-238191r953843_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls how the specified applications warn users when Visual Basic for Applications (VBA) macros are present. If this policy setting is enabled, four options are available for determining how the specified applications will warn the user about macros: - Disable all with notification: The application displays the Trust Bar for all macros, whether signed or unsigned. This option enforces the default configuration in Office. - Disable all except digitally signed macros: The application displays the Trust Bar for digitally signed macros, allowing users to enable them or leave them disabled. Any unsigned macros are disabled, and users are not notified. - Disable all without notification: The application disables all macros, whether signed or unsigned, and does not notify users. - Enable all macros (not recommended): All macros are enabled, whether signed or unsigned. This option can significantly reduce security by allowing dangerous code to run undetected. If this policy setting is disabled, "Disable all with notification" will be the default setting. If this policy setting is not configured, when users open files in the specified applications that contain VBA macros, the applications open the files with the macros disabled and display the Trust Bar with a warning that macros are present and have been disabled. Users can inspect and edit the files if appropriate but cannot use any disabled functionality until they enable it by clicking "Enable Content" on the Trust Bar. If the user clicks "Enable Content", the document is added as a trusted document. Important: If "Disable all except digitally signed macros" is selected, users will not be able to open unsigned Access databases. Note that Microsoft Office stores certificates for trusted publishers in the Internet Explorer trusted publisher store. Earlier versions of Microsoft Office stored trusted publisher certificate information (specifically, the certificate thumbprint) in a special Office trusted publisher store. Microsoft Office still reads trusted publisher certificate information from the Office trusted publisher store, but it does not write information to this store. Therefore, if the organization created a list of trusted publishers in a previous version of Microsoft Office and upgraded to Office, the trusted publisher list will still be recognized. However, any trusted publisher certificates that are added to the list will be stored in the Internet Explorer trusted publisher store.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration >> Administrative Templates >> Microsoft Excel 2016 >> Excel Options >> Security >> Trust Center >> Macro Notification Settings is set to "Enabled: Disable VBA macros with notification". The options "Enabled: Disable VBA macros except digitally signed macros" and "Enabled: Disable VBA macros without notification" are more restrictive and also acceptable values. Use the Windows Registry Editor to navigate to the following key: HKCU\software\policies\Microsoft\office\16.0\excel\security If the value "vbawarnings" is "REG_DWORD = 2", this is not a finding. Values of "REG_DWORD = 3" or "REG_DWORD = 4" are also acceptable. If the registry key does not exist or the value is "REG_DWORD = 1", this is a finding.

## Group: SRG-APP-000207

**Group ID:** `V-238192`

### Rule: WEBSERVICE functions must be disabled.


**Rule ID:** `SV-238192r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls how Excel will warn users when WEBSERVICE functions are present. If you enable this policy setting, you can choose from three options for determining how the specified applications will warn the user about WEBSERVICE functions:- Disable all with notification: The application displays the Trust Bar for all WEBSERVICE functions. This option enforces the default configuration in Office.- Disable all without notification: The application disables all WEBSERVICE functions and does not notify users.- Enable all WEBSERVICE functions (not recommended): The application enables all WEBSERVICE functions and does not notify users. This option can significantly reduce security by allowing information disclosure to third party web services. If you disable this policy setting, the 'Disable all with notification' will be the default setting. If you do not configure this policy setting, when users open workbooks that contain WEBSERVICE functions, Excel will open the files with the WEBSERVICE functions disabled and display the Trust Bar with a warning that WEBSERVICE functions are present and have been disabled. Users can inspect and edit the files if appropriate, but cannot use any disabled functionality until they enable it by clicking "Enable Content" on the Trust Bar. If the user clicks "Enable Content," then the document is added as a trusted document.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> "WEBSERVICE Function Notification Settings" is set to "Disabled". The option 'Enabled: Disable all with notification' is also an acceptable value. Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\software\policies\Microsoft\office\16.0\excel\security Criteria: If the value webservicefunctionwarnings does not exist, this is not a finding. If the registry key exists and is set to REG_DWORD = 1, this is also an acceptable value. If the value is REG_DWORD = 0 or 2, then this is a finding.

## Group: SRG-APP-000207

**Group ID:** `V-238193`

### Rule: Corrupt workbook options must be disallowed.


**Rule ID:** `SV-238193r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls whether Excel presents users with a list of data extraction options before beginning an Open and Repair operation when users choose to open a corrupt workbook in repair or extract mode. If you enable this policy setting, Excel opens the file using the Safe Load process and does not prompt users to choose between repairing or extracting data. If you disable or do not configure this policy setting, Excel prompts the user to select either to repair or to extract data, and to select either to convert to values or to recover formulas.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Data Recovery -> "Do not show data extraction options when opening corrupt workbooks" is set to "Enabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\software\policies\Microsoft\office\16.0\excel\options Criteria: If the value extractdatadisableui is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-238194`

### Rule: Macros must be blocked from running in Office files from the Internet.


**Rule ID:** `SV-238194r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to block macros from running in Office files that come from the Internet. If you enable this policy setting, macros are blocked from running, even if 'Enable all macro's is selected in the Macro Settings section of the Trust Center. Also, instead of having the choice to 'Enable Content', users will receive a notification that macros are blocked from running. If the Office file is saved to a trusted location or was previously trusted by the user, macros will be allowed to run. If you disable or don't configure this policy setting, the settings configured in the Macro Settings section of the Trust Center determine whether macros run in Office files that come from the Internet. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center "Block macros from running in Office files from the Internet" is set to "Enabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security Criteria: If the value blockcontentexecutionfrominternet is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-238195`

### Rule: Files on local Intranet UNC must be opened in Protected View.

**Rule ID:** `SV-238195r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting lets you determine if files on local Intranet UNC file shares open in Protected View. If you enable this policy setting, files on local Intranet UNC file shares open in Protected View if their UNC paths appear to be within the Internet zone. If you disable or do not configure this policy setting, files on Intranet UNC file shares do not open in Protected View if their UNC paths appear to be within the Internet zone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for User Configuration -> Administrative Templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center -> Protected View "Open files on local Intranet UNC in Protected View" is set to "Enabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Office\16.0\excel\security\protectedview Criteria: If the value DisableIntranetCheck is REG_DWORD = 0, this is not a finding.

