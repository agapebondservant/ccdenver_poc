# STIG Benchmark: Microsoft Internet Explorer 11 Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000516

**Group ID:** `V-223015`

### Rule: The Internet Explorer warning about certificate address mismatch must be enforced.

**Rule ID:** `SV-223015r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This parameter warns users if the certificate being presented by the website is invalid. Since server certificates are used to validate the identity of the web server it is critical to warn the user of a potential issue with the certificate being presented by the web server. This setting aids to prevent spoofing attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page 'Turn on certificate address mismatch warning' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings Criteria: If the value "WarnOnBadCertRecving" is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000175

**Group ID:** `V-223016`

### Rule: Check for publishers certificate revocation must be enforced.

**Rule ID:** `SV-223016r879612_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Check for publisher's certificate revocation options should be enforced to ensure all PKI signed objects are validated. Satisfies: SRG-APP-000605</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is on the SIPRNet, this requirement is NA. Open Internet Explorer. From the menu bar, select "Tools". From the "Tools" drop-down menu, select "Internet Options". From the "Internet Options" window, select the "Advanced" tab, from the "Advanced" tab window, scroll down to the "Security" category, and verify the "Check for publisher's certificate revocation" box is selected. Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Microsoft\Windows\CurrentVersion\WinTrust\Trust Providers\Software Publishing Criteria If the value "State" is "REG_DWORD = 23C00", this is not a finding.

## Group: SRG-APP-000209

**Group ID:** `V-223017`

### Rule: The Download signed ActiveX controls property must be disallowed (Internet zone).

**Rule ID:** `SV-223017r879629_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Active X controls can contain potentially malicious code and must only be allowed to be downloaded from trusted sites. Signed code is better than unsigned code in that it may be easier to determine its author, but it is still potentially harmful, especially when coming from an untrusted zone. This policy setting allows you to manage whether users may download signed ActiveX controls from a page in the zone. If you enable this policy, users can download signed controls without user intervention. If you select Prompt in the drop-down box, users are queried whether to download controls signed by untrusted publishers. Code signed by trusted publishers is silently downloaded. If you disable the policy setting, signed controls cannot be downloaded.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Download signed ActiveX controls' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "1001" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000209

**Group ID:** `V-223018`

### Rule: The Download unsigned ActiveX controls property must be disallowed (Internet zone).

**Rule ID:** `SV-223018r879629_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unsigned code is potentially harmful, especially when coming from an untrusted zone. This policy setting allows you to manage whether users may download unsigned ActiveX controls from the zone. If you enable this policy setting, users can run unsigned controls without user intervention. If you select "Prompt" in the drop-down box, users are queried to choose whether to allow the unsigned control to run. If you disable this policy setting, users cannot run unsigned controls. If you do not configure this policy setting, users cannot run unsigned controls.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Download unsigned ActiveX controls' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "1004" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-223019`

### Rule: The Initialize and script ActiveX controls not marked as safe property must be disallowed (Internet zone).

**Rule ID:** `SV-223019r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ActiveX controls that are not marked safe for scripting should not be executed. Although this is not a complete security measure for a control to be marked safe for scripting, if a control is not marked safe, it should not be initialized and executed. This setting causes both unsafe and safe controls to be initialized and scripted, ignoring the Script ActiveX controls marked safe for scripting option. This increases the risk of malicious code being loaded and executed by the browser. If you enable this policy setting, ActiveX controls are run, loaded with parameters and scripted without setting object safety for untrusted data or scripts. If you disable this policy setting, ActiveX controls that cannot be made safe are not loaded with parameters or scripted. This setting is not recommended, except for secure and administered zones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Initialize and script ActiveX controls not marked as safe' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "1201" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223020`

### Rule: The Java permissions must be disallowed (Internet zone).

**Rule ID:** `SV-223020r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Java applications could contain malicious code; sites located in this security zone are more likely to be hosted by malicious individuals. This policy setting allows you to manage permissions for Java applets. If you enable this policy setting, options can be chosen from the drop-down box. Use of the Custom permission will control permissions settings individually. Use of the Low Safety permission enables applets to perform all operations. Use of the Medium Safety permission enables applets to run in their sandbox (an area in memory outside of which the program cannot make calls), plus adds capabilities like scratch space (a safe and secure storage area on the client computer) and a user-controlled file I/O. Use of the High Safety permission enables applets to run in their sandbox. If you disable this policy setting, Java applets cannot run. If you do not configure this policy setting, the permission is set to High Safety.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Java permissions' must be 'Enabled', and 'Disable Java' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "1C00" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000039

**Group ID:** `V-223021`

### Rule: Accessing data sources across domains must be disallowed (Internet zone).

**Rule ID:** `SV-223021r879534_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ability to access data zones across domains could cause the user to unknowingly access content hosted on an unauthorized server. Access to data sources across multiple domains must be controlled based upon the site being browsed. This policy setting allows you to manage whether Internet Explorer can access data from another security zone using the Microsoft XML Parser (MSXML) or ActiveX Data Objects (ADO).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Access data sources across domains' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "1406" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223022`

### Rule: Functionality to drag and drop or copy and paste files must be disallowed (Internet zone).

**Rule ID:** `SV-223022r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Content hosted on sites located in the Internet zone are likely to contain malicious payloads and therefore this feature should be blocked for this zone. Drag and drop or copy and paste files must have a level of protection based upon the site being accessed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Allow drag and drop or copy and paste files' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value for "1802" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223023`

### Rule: Launching programs and files in IFRAME must be disallowed (Internet zone).

**Rule ID:** `SV-223023r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to manage whether applications may be run and files may be downloaded from an IFRAME reference in the HTML of the pages in this zone. Launching of programs in IFRAME must have a level of protection based upon the site being accessed. If you enable this policy setting, applications can run and files can be downloaded from IFRAMEs on the pages in this zone without user intervention. If you disable this setting, users are prevented from running applications and downloading files from IFRAMEs on the pages in this zone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Launching applications and files in an IFRAME' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "1804" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000039

**Group ID:** `V-223024`

### Rule: Navigating windows and frames across different domains must be disallowed (Internet zone).

**Rule ID:** `SV-223024r879534_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Frames that navigate across different domains are a security concern, because the user may think they are accessing pages on one site while they are actually accessing pages on another site. It is possible that a website hosting malicious content could use this feature in a manner similar to cross-site scripting (XSS). This policy setting allows you to manage the opening of sub-frames and access of applications across different domains.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Navigate windows and frames across different domains' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\InternetSettings\Zones\3 Criteria: If the value "1607" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000231

**Group ID:** `V-223025`

### Rule: Userdata persistence must be disallowed (Internet zone).

**Rule ID:** `SV-223025r879642_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Userdata persistence must have a level of protection based upon the site being accessed. It is possible for sites hosting malicious content to exploit this feature as part of an attack against visitors browsing the site. This policy setting allows you to manage the preservation of information in the browser's history, in Favorites, in an XML store, or directly within a web page saved to disk. When a user returns to a persisted page, the state of the page can be restored if this policy setting is not appropriately configured. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Userdata persistence' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "1606" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223026`

### Rule: Clipboard operations via script must be disallowed (Internet zone).

**Rule ID:** `SV-223026r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A malicious script could use the clipboard in an undesirable manner, for example, if the user had recently copied confidential information to the clipboard while editing a document, a malicious script could harvest that information. It might be possible to exploit other vulnerabilities in order to send the harvested data to the attacker. Allow paste operations via script must have a level of protection based upon the site being accessed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Allow cut, copy or paste operations from the clipboard via script' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "1407" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000219

**Group ID:** `V-223027`

### Rule: Logon options must be configured to prompt (Internet zone).

**Rule ID:** `SV-223027r879636_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Users could submit credentials to servers operated by malicious individuals who could then attempt to connect to legitimate servers with those captured credentials. Care must be taken with user credentials, automatic logon performance, and how default Windows credentials are passed to the websites. This policy setting allows management of settings for logon options. If you enable this policy setting, you can choose from varying logon options. “Anonymous logon” disables HTTP authentication and uses the guest account only for the Common Internet File System (CIFS) protocol. “Prompt for user name and password” queries users for user IDs and passwords. After a user is queried, these values can be used silently for the remainder of the session. “Automatic logon only in Intranet zone” queries users for user IDs and passwords in other zones. After a user is queried, these values can be used silently for the remainder of the session. “Automatic logon with current user name and password” attempts logon using Windows NT Challenge Response. If Windows NT Challenge Response is supported by the server, the logon uses the user's network user name and password for login. If Windows NT Challenge Response is not supported by the server, the user is queried to provide the user name and password. If you disable this policy setting, logon is set to “Automatic logon only in Intranet zone”. If you do not configure this policy setting, logon is set to “Automatic logon only in Intranet zone”. The most secure option is to configure this setting to “Enabled”; “Anonymous logon”, but configuring this setting to “Enabled”; “Prompt for user name and password”, provides a reasonable balance between security and usability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Logon options' must be 'Enabled', and 'Prompt for user name and password' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "1A00" is REG_DWORD = 65536 (decimal), this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223028`

### Rule: Java permissions must be configured with High Safety (Intranet zone).

**Rule ID:** `SV-223028r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Java applications could contain malicious code. This policy setting allows you to manage permissions for Java applets. If you enable this policy setting, options can be chosen from the drop-down box. Use of the Custom permission will control permissions settings individually. Use of the Low Safety permission enables applets to perform all operations. Use of the Medium Safety permission enables applets to run in their sandbox (an area in memory outside of which the program cannot make calls), plus adds capabilities like scratch space (a safe and secure storage area on the client computer) and a user-controlled file I/O. Use of the High Safety permission enables applets to run in their sandbox. If you disable this policy setting, Java applets cannot run. If you do not configure this policy setting, the permission is set to High Safety.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Intranet Zone -> 'Java permissions' must be 'Enabled', and 'High Safety' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\1 Criteria: If the value "1C00" is REG_DWORD = 65536, (Decimal), this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-223029`

### Rule: Anti-Malware programs against ActiveX controls must be run for the Intranet zone.

**Rule ID:** `SV-223029r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting determines whether Internet Explorer runs Anti-Malware programs against ActiveX controls, to check if they're safe to load on pages. If you enable this policy setting, Internet Explorer won't check with your Anti-Malware program to see if it's safe to create an instance of the ActiveX control. If you disable this policy setting, Internet Explorer always checks with your Anti-Malware program to see if it's safe to create an instance of the ActiveX control. If you don't configure this policy setting, Internet Explorer won't check with your Anti-Malware program to see if it's safe to create an instance of the ActiveX control. Users can turn this behavior on or off, using Internet Explorer Security settings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer-> Internet Control Panel -> Security Page -> Intranet Zone 'Don't run antimalware programs against ActiveX controls' must be 'Enabled' and 'Disable' selected in the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\1 Criteria: If the value "270C" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223030`

### Rule: Java permissions must be configured with High Safety (Trusted Sites zone).

**Rule ID:** `SV-223030r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Java applications could contain malicious code. This policy setting allows you to manage permissions for Java applets. If you enable this policy setting, options can be chosen from the drop-down box. Use of the Custom permission will control permissions settings individually. Use of the Low Safety permission enables applets to perform all operations. Use of the Medium Safety permission enables applets to run in their sandbox (an area in memory outside of which the program cannot make calls), plus adds capabilities like scratch space (a safe and secure storage area on the client computer) and a user-controlled file I/O. Use of the High Safety permission enables applets to run in their sandbox. If you disable this policy setting, Java applets cannot run. If you do not configure this policy setting, the permission is set to High Safety</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Trusted Sites Zone -> 'Java permissions' must be 'Enabled', and 'High Safety' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2 Criteria: If the value "1C00" is REG_DWORD = 65536, (Decimal), this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-223031`

### Rule: Anti-Malware programs against ActiveX controls must be run for the Trusted Sites zone.

**Rule ID:** `SV-223031r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting determines whether Internet Explorer runs Anti-Malware programs against ActiveX controls, to check if they're safe to load on pages. If you enable this policy setting, Internet Explorer won't check with your Anti-Malware program to see if it's safe to create an instance of the ActiveX control. If you disable this policy setting, Internet Explorer always checks with your Anti-Malware program to see if it's safe to create an instance of the ActiveX control. If you don't configure this policy setting, Internet Explorer won't check with your Anti-Malware program to see if it's safe to create an instance of the ActiveX control. Users can turn this behavior on or off, using Internet Explorer Security settings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer-> Internet Control Panel -> Security Page -> Trusted Sites Zone 'Don't run antimalware programs against ActiveX controls' must be 'Enabled' and 'Disable' selected in the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2 Criteria: If the value "270C" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000039

**Group ID:** `V-223032`

### Rule: Dragging of content from different domains within a window must be disallowed (Internet zone).

**Rule ID:** `SV-223032r879534_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to set options for dragging content from one domain to a different domain when the source and destination are in the same window. If you enable this policy setting, users can drag content from one domain to a different domain when the source and destination are in the same window. Users cannot change this setting. If you disable this policy setting, users cannot drag content from one domain to a different domain when the source and destination are in the same window. Users cannot change this setting in the Internet Options dialog box. If you do not configure this policy setting, users cannot drag content from one domain to a different domain when the source and destination are in the same window. Users can change this setting in the Internet Options dialog box.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer-> Internet Control Panel-> Security Page-> Internet Zone 'Enable dragging of content from different domains within a window' must be 'Enabled', and 'Disabled' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "2708" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000039

**Group ID:** `V-223033`

### Rule: Dragging of content from different domains across windows must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223033r879534_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to set options for dragging content from one domain to a different domain when the source and destination are in different windows. If you enable this policy setting, users can drag content from one domain to a different domain when the source and destination are in different windows. Users cannot change this setting. If you enable this policy setting, users cannot drag content from one domain to a different domain when both the source and destination are in different windows. Users cannot change this setting. If you do not configure this policy setting, users cannot drag content from one domain to a different domain when the source and destination are in different windows. Users can change this setting in the Internet Options dialog box.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer-> Internet Control Panel-> Security Page-> Restricted Sites Zone 'Enable dragging of content from different domains across windows' must be 'Enabled', and 'Disabled' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "2709" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000112

**Group ID:** `V-223034`

### Rule: Internet Explorer Processes Restrict ActiveX Install must be enforced (Explorer).

**Rule ID:** `SV-223034r879573_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Users often choose to install software such as ActiveX controls that are not permitted by their organization's security policy. Such software can pose significant security and privacy risks to networks. This policy setting enables blocking of ActiveX control installation prompts for Internet Explorer processes. If you enable this policy setting, prompts for ActiveX control installations will be blocked for Internet Explorer processes. If you disable this policy setting, prompts for ActiveX control installations will not be blocked and these prompts will be displayed to users. If you do not configure this policy setting, the user's preference will be used to determine whether to block ActiveX control installations for Internet Explorer processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> Restrict ActiveX Install -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_RESTRICT_ACTIVEXINSTALL Criteria: If the value "explorer.exe" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000112

**Group ID:** `V-223035`

### Rule: Internet Explorer Processes Restrict ActiveX Install must be enforced (iexplore).

**Rule ID:** `SV-223035r879573_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Users often choose to install software such as ActiveX controls that are not permitted by their organization's security policy. Such software can pose significant security and privacy risks to networks. This policy setting enables blocking of ActiveX control installation prompts for Internet Explorer processes. If you enable this policy setting, prompts for ActiveX control installations will be blocked for Internet Explorer processes. If you disable this policy setting, prompts for ActiveX control installations will not be blocked and these prompts will be displayed to users. If you do not configure this policy setting, the user's preference will be used to determine whether to block ActiveX control installations for Internet Explorer processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> Restrict ActiveX Install -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_RESTRICT_ACTIVEXINSTALL Criteria: If the value "iexplore.exe" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000039

**Group ID:** `V-223036`

### Rule: Dragging of content from different domains within a window must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223036r879534_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to set options for dragging content from one domain to a different domain when the source and destination are in the same window. If you enable this policy setting, users can drag content from one domain to a different domain when the source and destination are in the same window. Users cannot change this setting. If you disable this policy setting, users cannot drag content from one domain to a different domain when the source and destination are in the same window. Users cannot change this setting in the Internet Options dialog box. If you do not configure this policy setting, users cannot drag content from one domain to a different domain when the source and destination are in the same window. Users can change this setting in the Internet Options dialog box.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer-> Internet Control Panel-> Security Page-> Restricted Sites Zone 'Enable dragging of content from different domains within a window' must be 'Enabled', and 'Disabled' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "2708" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-223037`

### Rule: Anti-Malware programs against ActiveX controls must be run for the Internet zone.

**Rule ID:** `SV-223037r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting determines whether Internet Explorer runs Anti-Malware programs against ActiveX controls, to check if they're safe to load on pages. If you enable this policy setting, Internet Explorer won't check with your Anti-Malware program to see if it's safe to create an instance of the ActiveX control. If you disable this policy setting, Internet Explorer always checks with your Anti-Malware program to see if it's safe to create an instance of the ActiveX control. If you don't configure this policy setting, Internet Explorer always checks with your Anti-Malware program to see if it's safe to create an instance of the ActiveX control. Users can turn this behavior on or off, using Internet Explorer Security settings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer-> Internet Control Panel -> Security Page -> Internet Zone 'Don't run antimalware programs against ActiveX controls' must be 'Enabled' and 'Disable' selected in the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "270C" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-223038`

### Rule: Anti-Malware programs against ActiveX controls must be run for the Restricted Sites zone.

**Rule ID:** `SV-223038r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting determines whether Internet Explorer runs Anti-Malware programs against ActiveX controls, to check if they're safe to load on pages. If you enable this policy setting, Internet Explorer won't check with your Anti-Malware program to see if it's safe to create an instance of the ActiveX control. If you disable this policy setting, Internet Explorer always checks with your Anti-Malware program to see if it's safe to create an instance of the ActiveX control. If you don't configure this policy setting, Internet Explorer always checks with your Anti-Malware program to see if it's safe to create an instance of the ActiveX control. Users can turn this behavior on or off, using Internet Explorer Security settings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer-> Internet Control Panel -> Security Page -> Restricted Sites Zone 'Don't run antimalware programs against ActiveX controls' must be 'Enabled' and 'Disable' selected in the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "270C" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000278

**Group ID:** `V-223039`

### Rule: Prevent bypassing SmartScreen Filter warnings must be enabled.

**Rule ID:** `SV-223039r879664_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting determines whether the user can bypass warnings from SmartScreen Filter. SmartScreen Filter prevents the user from browsing to or downloading from sites that are known to host malicious content. SmartScreen Filter also prevents the execution of files that are known to be malicious. If you enable this policy setting, SmartScreen Filter warnings block the user. If you disable or do not configure this policy setting, the user can bypass SmartScreen Filter warnings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is on the SIPRNet, this requirement is NA. The policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Internet Explorer >> ”Prevent bypassing SmartScreen Filter warnings” must be ”Enabled”. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\PhishingFilter. Criteria: If the value "PreventOverride" is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000209

**Group ID:** `V-223040`

### Rule: Prevent bypassing SmartScreen Filter warnings about files that are not commonly downloaded from the internet must be enabled.

**Rule ID:** `SV-223040r879629_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting determines whether the user can bypass warnings from SmartScreen Filter. SmartScreen Filter warns the user about executable files that Internet Explorer users do not commonly download from the internet. If you enable this policy setting, SmartScreen Filter warnings block the user. If you disable or do not configure this policy setting, the user can bypass SmartScreen Filter warnings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is on the SIPRNet, this requirement is NA. The policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Internet Explorer >> ”Prevent bypassing SmartScreen Filter warnings about files that are not commonly downloaded from the internet” must be ”Enabled”. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\PhishingFilter. Criteria: If the value "PreventOverrideAppRepUnknown" is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-223041`

### Rule: Prevent per-user installation of ActiveX controls must be enabled.

**Rule ID:** `SV-223041r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to prevent the installation of ActiveX controls on a per-user basis. If you enable this policy setting, ActiveX controls cannot be installed on a per-user basis. If you disable or do not configure this policy setting, ActiveX controls can be installed on a per-user basis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Internet Explorer >> ”Prevent per-user installation of ActiveX controls” must be ”Enabled”. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Security\ActiveX. Criteria: If the value "BlockNonAdminActiveXInstall" is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000427

**Group ID:** `V-223042`

### Rule: Prevent ignoring certificate errors option must be enabled.

**Rule ID:** `SV-223042r942482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting prevents the user from ignoring Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificate errors that interrupt browsing (such as “expired”, “revoked”, or “name mismatch” errors) in Internet Explorer. If you enable this policy setting, the user cannot continue browsing. If you disable or do not configure this policy setting, the user can choose to ignore certificate errors and continue browsing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Internet Explorer >> Internet Control Panel >> ”Prevent ignoring certificate errors” must be ”Enabled”. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings. Criteria: If the value "PreventIgnoreCertErrors" is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000278

**Group ID:** `V-223043`

### Rule: Turn on SmartScreen Filter scan option for the Internet Zone must be enabled.

**Rule ID:** `SV-223043r879664_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls whether SmartScreen Filter scans pages in this zone for malicious content. If you enable this policy setting, SmartScreen Filter scans pages in this zone for malicious content. If you disable this policy setting, SmartScreen Filter does not scan pages in this zone for malicious content. If you do not configure this policy setting, the user can choose whether SmartScreen Filter scans pages in this zone for malicious content.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Internet Explorer >> Internet Control Panel >> Security Page >> Internet Zone >> ”Turn on SmartScreen Filter scan” must be ”Enabled” and ”Enable” selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3. Criteria: If the value "2301" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000278

**Group ID:** `V-223044`

### Rule: Turn on SmartScreen Filter scan option for the Restricted Sites Zone must be enabled.

**Rule ID:** `SV-223044r879664_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls whether SmartScreen Filter scans pages in this zone for malicious content. If you enable this policy setting, SmartScreen Filter scans pages in this zone for malicious content. If you disable this policy setting, SmartScreen Filter does not scan pages in this zone for malicious content. If you do not configure this policy setting, the user can choose whether SmartScreen Filter scans pages in this zone for malicious content.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Internet Explorer >> Internet Control Panel >> Security Page >> Restricted Sites Zone >> ”Turn on SmartScreen Filter scan” must be ”Enabled” and ”Enable” selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4. Criteria: If the value "2301" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-223045`

### Rule: The Initialize and script ActiveX controls not marked as safe must be disallowed (Intranet Zone).

**Rule ID:** `SV-223045r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ActiveX controls that are not marked safe for scripting should not be executed. Although this is not a complete security measure for a control to be marked safe for scripting, if a control is not marked safe, it should not be initialized and executed. This setting causes both unsafe and safe controls to be initialized and scripted, ignoring the Script ActiveX controls marked safe for scripting option. This increases the risk of malicious code being loaded and executed by the browser. If you enable this policy setting, ActiveX controls are run, loaded with parameters and scripted without setting object safety for untrusted data or scripts. If you disable this policy setting, ActiveX controls that cannot be made safe are not loaded with parameters or scripted. This setting is not recommended, except for secure and administered zones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Internet Explorer >> Internet Control Panel >> Security Page >> Intranet Zone >> ”Initialize and script ActiveX controls not marked as safe” must be ”Enabled” and ”Disable” selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\1. Criteria: If the value "1201" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-223046`

### Rule: The Initialize and script ActiveX controls not marked as safe must be disallowed (Trusted Sites Zone).

**Rule ID:** `SV-223046r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ActiveX controls that are not marked safe for scripting should not be executed. Although this is not a complete security measure for a control to be marked safe for scripting, if a control is not marked safe, it should not be initialized and executed. This setting causes both unsafe and safe controls to be initialized and scripted, ignoring the Script ActiveX controls marked safe for scripting option. This increases the risk of malicious code being loaded and executed by the browser. If you enable this policy setting, ActiveX controls are run, loaded with parameters and scripted without setting object safety for untrusted data or scripts. If you disable this policy setting, ActiveX controls that cannot be made safe are not loaded with parameters or scripted. This setting is not recommended, except for secure and administered zones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Internet Explorer >> Internet Control Panel >> Security Page >> Trusted Sites Zone >> ”Initialize and script ActiveX controls not marked as safe” must be ”Enabled” and ”Disable” selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2. Criteria: If the value "1201" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223048`

### Rule: Run once selection for running outdated ActiveX controls must be disabled.

**Rule ID:** `SV-223048r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This feature keeps ActiveX controls up to date and helps make them safer to use in Internet Explorer. Many ActiveX controls are not automatically updated as new versions are released. It is very important to keep ActiveX controls up to date because malicious or compromised webpages can target security flaws in out-of-date ActiveX controls.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Internet Explorer >> Security Features >> Add-on Management, verify "Remove the Run this time button for outdated ActiveX controls in IE" is set to “Enabled”. Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\Ext If the value "RunThisTimeEnabled" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223049`

### Rule: Enabling outdated ActiveX controls for Internet Explorer must be blocked.

**Rule ID:** `SV-223049r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This feature keeps ActiveX controls up to date and helps make them safer to use in Internet Explorer. Many ActiveX controls are not automatically updated as new versions are released. It is very important to keep ActiveX controls up to date because malicious or compromised webpages can target security flaws in out-of-date ActiveX controls.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Internet Explorer >> Security Features >> Add-on Management, verify "Turn off blocking of outdated ActiveX controls for Internet Explorer" is set to “Disabled”. Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\Ext If the value "VersionCheckEnabled" is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223050`

### Rule: Use of the Tabular Data Control (TDC) ActiveX control must be disabled for the Internet Zone.

**Rule ID:** `SV-223050r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting determines whether users can run the Tabular Data Control (TDC) ActiveX control, based on security zone. By default, the TDC ActiveX Control is disabled in the Internet and Restricted Sites security zones. If you enable this policy setting, users will not be able to run the TDC ActiveX control from all sites in the specified zone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Internet Explorer >> Internet Control Panel >> Security Page >> Internet Zone, verify "Allow only approved domains to use the TDC ActiveX control" is “Enabled”. In the Options window, verify the “Only allow approved domains to use the TDC ActiveX control" drop-down box is set to “Enable”. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "120c" is REG_DWORD = “3”, this is not a finding.

## Group: SRG-APP-000209

**Group ID:** `V-223051`

### Rule: The Download signed ActiveX controls property must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223051r879629_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ActiveX controls can contain potentially malicious code and must only be allowed to be downloaded from trusted sites. Signed code is better than unsigned code in that it may be easier to determine its author, but it is still potentially harmful, especially when coming from an untrusted zone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Download signed ActiveX controls' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1001" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223052`

### Rule: Use of the Tabular Data Control (TDC) ActiveX control must be disabled for the Restricted Sites Zone.

**Rule ID:** `SV-223052r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting determines whether users can run the Tabular Data Control (TDC) ActiveX control, based on security zone. By default, the TDC ActiveX Control is disabled in the Internet and Restricted Sites security zones. If you enable this policy setting, users won’t be able to run the TDC ActiveX control from all sites in the specified zone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Internet Explorer >> Internet Control Panel >> Security Page >> Restricted Sites Zone, verify "Allow only approved domains to use the TDC ActiveX control" is “Enabled”. In the Options window, verify the “Only allow approved domains to use the TDC ActiveX control" drop-down box is set to “Enable”. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "120c" is REG_DWORD = “3”, this is not a finding.

## Group: SRG-APP-000209

**Group ID:** `V-223053`

### Rule: VBScript must not be allowed to run in Internet Explorer (Internet zone).

**Rule ID:** `SV-223053r879629_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows the management of whether VBScript can be run on pages from the specified zone in Internet Explorer. By selecting "Enable" in the drop-down box, VBScript can run without user intervention. By selecting "Prompt" in the drop-down box, users are asked to choose whether to allow VBScript to run. By selecting "Disable" in the drop-down box, VBScript is prevented from running. If this policy setting is not configured or disabled, VBScript will run without user intervention.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Internet Explorer >> Internet Control Panel >> Security Page >> Internet Zone >> "Allow VBScript to run in Internet Explorer" must be "Enabled", and "Disable" must be selected from the drop-down box. Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 If the value for "140C" is not REG_DWORD = 3, this is a finding.

## Group: SRG-APP-000209

**Group ID:** `V-223054`

### Rule: The Download unsigned ActiveX controls property must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223054r879629_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unsigned code is potentially harmful, especially when coming from an untrusted zone. ActiveX controls can contain potentially malicious code and must only be allowed to be downloaded from trusted sites. They must also be digitally signed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Download unsigned ActiveX controls' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1004" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000209

**Group ID:** `V-223055`

### Rule: VBScript must not be allowed to run in Internet Explorer (Restricted Sites zone).

**Rule ID:** `SV-223055r879629_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows the management of whether VBScript can be run on pages from the specified zone in Internet Explorer. By selecting "Enable" in the drop-down box, VBScript can run without user intervention. By selecting "Prompt" in the drop-down box, users are asked to choose whether to allow VBScript to run. By selecting "Disable" in the drop-down box, VBScript is prevented from running. If this policy setting is not configured or disabled, VBScript will run without user intervention.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Internet Explorer >> Internet Control Panel >> Security Page >> Restricted Sites Zone >> "Allow VBScript to run in Internet Explorer" must be "Enabled", and "Disable" must be selected from the drop-down box. Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 If the value for "140C" is not REG_DWORD = 3, this is a finding.

## Group: SRG-APP-000266

**Group ID:** `V-223056`

### Rule: Internet Explorer Development Tools Must Be Disabled.

**Rule ID:** `SV-223056r879655_rule`
**Severity:** low

**Description:**
<VulnDiscussion>While the risk associated with browser development tools is more related to the proper design of a web application, a risk vector remains within the browser. The developer tools allow end users and application developers to view and edit all types of web application related data via the browser. Page elements, source code, javascript, API calls, application data, etc. may all be viewed and potentially manipulated. Manipulation could be useful for troubleshooting legitimate issues, and this may be performed in a development environment. Manipulation could also be malicious and must be addressed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Internet Explorer >> Toolbars >> “Turn off Developer Tools” must be “Enabled”. Procedure: Use the Windows Registry Editor to navigate to the following key: HKEY_LOCAL_Machine\SOFTWARE\Policies\Microsoft\Internet Explorer\IEDevTools Criteria: If the value "Disabled" is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-223057`

### Rule: The Initialize and script ActiveX controls not marked as safe property must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223057r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ActiveX controls not marked safe for scripting should not be executed. Although this is not a complete security measure for a control to be marked safe for scripting, if a control is not marked safe, it should not be initialized and executed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Initialize and script ActiveX controls not marked as safe' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1201" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000516

**Group ID:** `V-223058`

### Rule: ActiveX controls and plug-ins must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223058r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to manage whether ActiveX controls and plug-ins can be run on pages from the specified zone. ActiveX controls not marked as safe should not be executed. If you enable this policy setting, controls and plug-ins can run without user intervention. If you disable this policy setting, controls and plug-ins are prevented from running.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Run ActiveX controls and plugins' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1200" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-223059`

### Rule: ActiveX controls marked safe for scripting must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223059r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows management of whether ActiveX controls marked safe for scripting can interact with a script. If you enable this policy setting, script interaction can occur automatically without user intervention. ActiveX controls not marked as safe for scripting should not be executed. Although this is not a complete security measure for a control to be marked safe for scripting, if a control is not marked safe, it should not be initialized and executed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Script ActiveX controls marked safe for scripting' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1405" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223060`

### Rule: File downloads must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223060r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Sites located in the Restricted Sites Zone are more likely to contain malicious payloads and therefore downloads from this zone should be blocked. Files should not be able to be downloaded from sites that are considered restricted. This policy setting allows you to manage whether file downloads are permitted from the zone. This option is determined by the zone of the page with the link causing the download, not the zone from which the file is delivered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Allow file downloads' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1803" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223061`

### Rule: Java permissions must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223061r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Java applications could contain malicious code; sites located in this security zone are more likely to be hosted by malicious individuals. This policy setting allows you to manage permissions for Java applets. If you enable this policy setting, options can be chosen from the drop-down box. Use of the Custom permission will control permissions settings individually. Use of the Low Safety permission enables applets to perform all operations. Use of the Medium Safety permission enables applets to run in their sandbox (an area in memory outside of which the program cannot make calls), plus adds capabilities like scratch space (a safe and secure storage area on the client computer) and a user-controlled file I/O. Use of the High Safety permission enables applets to run in their sandbox. If you disable this policy setting, Java applets cannot run. If you do not configure this policy setting, the permission is set to High Safety.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Java permissions' must be 'Enabled', and 'Disable Java' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1C00" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000039

**Group ID:** `V-223062`

### Rule: Accessing data sources across domains must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223062r879534_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ability to access data zones across domains could cause the user to unknowingly access content hosted on an unauthorized server. This policy setting allows you to manage whether Internet Explorer can access data from another security zone using the Microsoft XML Parser (MSXML) or ActiveX Data Objects (ADO).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Access data sources across domains' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1406" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000516

**Group ID:** `V-223063`

### Rule: The Allow META REFRESH property must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223063r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is possible that users will unknowingly be redirected to a site hosting malicious content. 'Allow META REFRESH' must have a level of protection based upon the site being browsed. This policy setting allows you to manage whether a user's browser can be redirected to another web page if the author of the web page uses the Meta Refresh setting to redirect browsers to another web page.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Allow META REFRESH' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1608" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223064`

### Rule: Functionality to drag and drop or copy and paste files must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223064r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Content hosted on sites located in the Restricted Sites zone are more likely to contain malicious payloads and therefore this feature should be blocked for this zone. Drag and drop or copy and paste files must have a level of protection based upon the site being accessed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Allow drag and drop or copy and paste files' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1802" is REG_DWORD=3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223065`

### Rule: Launching programs and files in IFRAME must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223065r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to manage whether applications may be run and files may be downloaded from an IFRAME reference in the HTML of the pages in this zone. Launching of programs in IFRAME must have a level of protection based upon the site being accessed. If you enable this policy setting, applications can run and files can be downloaded from IFRAMEs on the pages in this zone without user intervention. If you disable this setting, users are prevented from running applications and downloading files from IFRAMEs on the pages in this zone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Launching applications and files in an IFRAME' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1804" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000039

**Group ID:** `V-223066`

### Rule: Navigating windows and frames across different domains must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223066r879534_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Frames navigating across different domains are a security concern, because the user may think they are accessing pages on one site while they are actually accessing pages on another site. It is possible that a website hosting malicious content could use this feature in a manner similar to cross-site scripting (XSS). This policy setting allows you to manage the opening of sub-frames and access of applications across different domains.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Navigate windows and frames across different domains' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1607" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000231

**Group ID:** `V-223067`

### Rule: Userdata persistence must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223067r879642_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Userdata persistence must have a level of protection based upon the site being accessed. This policy setting allows you to manage the preservation of information in the browser's history, in Favorites, in an XML store, or directly within a web page saved to disk. When a user returns to a persisted page, the state of the page can be restored if this policy setting is not appropriately configured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Userdata persistence' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1606" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223068`

### Rule: Active scripting must be disallowed (Restricted Sites Zone).

**Rule ID:** `SV-223068r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Active scripts hosted on sites located in this zone are more likely to contain malicious code. Active scripting must have a level of protection based upon the site being accessed. This policy setting allows you to manage whether script code on pages in the zone are run.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Allow active scripting' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1400" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223069`

### Rule: Clipboard operations via script must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223069r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A malicious script could use the clipboard in an undesirable manner, for example, if the user had recently copied confidential information to the clipboard while editing a document, a malicious script could harvest that information. It might be possible to exploit other vulnerabilities in order to send the harvested data to the attacker. Allow paste operations via script must have a level of protection based upon the site being accessed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Allow cut, copy or paste operations from the clipboard via script' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1407" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000219

**Group ID:** `V-223070`

### Rule: Logon options must be configured and enforced (Restricted Sites zone).

**Rule ID:** `SV-223070r879636_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Users could submit credentials to servers operated by malicious individuals who could then attempt to connect to legitimate servers with those captured credentials. Care must be taken with user credentials, automatic logon performance, and how default Windows credentials are passed to the websites. This policy setting allows management of settings for logon options. If you enable this policy setting, you can choose from varying logon options. “Anonymous logon” disables HTTP authentication and uses the guest account only for the Common Internet File System (CIFS) protocol. “Prompt for user name and password” queries users for user IDs and passwords. After a user is queried, these values can be used silently for the remainder of the session. “Automatic logon only in Intranet zone” queries users for user IDs and passwords in other zones. After a user is queried, these values can be used silently for the remainder of the session. “Automatic logon with current user name and password” attempts logon using Windows NT Challenge Response. If Windows NT Challenge Response is supported by the server, the logon uses the user's network user name and password for login. If Windows NT Challenge Response is not supported by the server, the user is queried to provide the user name and password. If you disable this policy setting, logon is set to “Automatic logon only in Intranet zone”. If you do not configure this policy setting, logon is set to “Automatic logon only in Intranet zone”. The most secure option is to configure this setting to “Enabled”; “Anonymous logon”. This will prevent users from submitting credentials to servers in this security zone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Logon options' must be 'Enabled', and 'Anonymous logon' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1A00" is REG_DWORD = 196608 (decimal), this is not a finding.

## Group: SRG-APP-000089

**Group ID:** `V-223071`

### Rule: Configuring History setting must be set to 40 days.

**Rule ID:** `SV-223071r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting specifies the number of days that Internet Explorer keeps track of the pages viewed in the History List. The delete Browsing History option can be accessed using Tools, Internet Options, "General" tab, and then click Settings under Browsing History. If you enable this policy setting, a user cannot set the number of days that Internet Explorer keeps track of the pages viewed in the History List. The number of days that Internet Explorer keeps track of the pages viewed in the History List must be specified. Users will not be able to delete browsing history. If you disable or do not configure this policy setting, a user can set the number of days that Internet Explorer tracks views of pages in the History List. Users can delete browsing history.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Delete Browsing History -> 'Disable Configuring History' must be 'Enabled', and '40' entered in 'Days to keep pages in History'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Control Panel Criteria: If the value "History" is REG_DWORD = 1, this is not a finding. AND Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Url History Criteria: If the value "DaysToKeep" is REG_DWORD = 40 (decimal), this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223072`

### Rule: Internet Explorer must be set to disallow users to add/delete sites.

**Rule ID:** `SV-223072r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting prevents users from adding sites to various security zones. Users should not be able to add sites to different zones, as this could allow them to bypass security controls of the system. If you do not configure this policy setting, users will be able to add or remove sites from the Trusted Sites and Restricted Sites zones at will and change settings in the Local Intranet zone. This configuration could allow sites that host malicious mobile code to be added to these zones, and users could execute the code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer 'Security Zones: Do not allow users to add/delete sites' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings Criteria: If the value "Security_zones_map_edit" is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000516

**Group ID:** `V-223073`

### Rule: Internet Explorer must be configured to disallow users to change policies.

**Rule ID:** `SV-223073r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Users who change their Internet Explorer security settings could enable the execution of dangerous types of code from the Internet and websites listed in the Restricted Sites zone in the browser. This setting prevents users from changing the Internet Explorer policies on the machine. Policy changes should be made by administrators only, so this setting should be enabled. If you enable this policy setting, you disable the "Custom level" button and "Security" level for this zone slider on the Security tab in the Internet Options dialog box. If this policy setting is disabled or not configured, users will be able to change the settings for security zones. It prevents users from changing security zone policy settings that are established by the administrator.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer 'Security Zones: Do not allow users to change policies' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings Criteria: If the value "Security_options_edit" is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000516

**Group ID:** `V-223074`

### Rule: Internet Explorer must be configured to use machine settings.

**Rule ID:** `SV-223074r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Users who change their Internet Explorer security settings could enable the execution of dangerous types of code from the Internet and websites listed in the Restricted Sites zone in the browser. This setting enforces consistent security zone settings to all users of the computer. Security zones control browser behavior at various websites and it is desirable to maintain a consistent policy for all users of a machine. This policy setting affects how security zone changes apply to different users. If you enable this policy setting, changes that one user makes to a security zone will apply to all users of that computer. If this policy setting is disabled or not configured, users of the same computer are allowed to establish their own security zone settings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer 'Security Zones: Use only machine settings' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings Criteria: If the value "Security_HKLM_only" is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000516

**Group ID:** `V-223075`

### Rule: Security checking features must be enforced.

**Rule ID:** `SV-223075r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting turns off the Security Settings Check feature, which checks Internet Explorer security settings to determine when the settings put Internet Explorer at risk. If you enable this policy setting, the security settings check will not be performed. If you disable or do not configure this policy setting, the security settings check will be performed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> 'Turn off the Security Settings Check feature' must be 'Disabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Security Criteria: If the value "DisableSecuritySettingsCheck" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-223076`

### Rule: Software must be disallowed to run or install with invalid signatures.

**Rule ID:** `SV-223076r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Microsoft ActiveX controls and file downloads often have digital signatures attached that certify the file's integrity and the identity of the signer (creator) of the software. Such signatures help ensure unmodified software is downloaded and the user can positively identify the signer to determine whether you trust them enough to run their software.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: Some legitimate software and controls may have an invalid signature. You should carefully test such software in isolation before it is allowed to be used on an organization's network. The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Advanced Page -> 'Allow software to run or install even if the signature is invalid' must be 'Disabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Download Criteria: If the value "RunInvalidSignatures" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000233

**Group ID:** `V-223077`

### Rule: The 64-bit tab processes, when running in Enhanced Protected Mode on 64-bit versions of Windows, must be turned on.

**Rule ID:** `SV-223077r879643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting determines whether Internet Explorer 11 uses 64-bit processes (for greater security) or 32-bit processes (for greater compatibility) when running in Enhanced Protected Mode on 64-bit versions of Windows.Important: Some ActiveX controls and toolbars may not be available when 64-bit processes are used. If you enable this policy setting, Internet Explorer 11 will use 64-bit tab processes when running in Enhanced Protected Mode on 64-bit versions of Windows. If you disable this policy setting, Internet Explorer 11 will use 32-bit tab processes when running in Enhanced Protected Mode on 64-bit versions of Windows. If you don't configure this policy setting, users can turn this feature on or off using Internet Explorer settings. This feature is turned off by default.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If McAfee ENS Web Control is being used, this is Not Applicable. The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer-> Internet Control Panel -> Advanced Page 'Turn on 64-bit tab processes when running in Enhanced Protected Mode on 64-bit versions of Windows' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main Criteria: If the value "Isolation64Bit" is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000175

**Group ID:** `V-223078`

### Rule: Checking for server certificate revocation must be enforced.

**Rule ID:** `SV-223078r879612_rule`
**Severity:** low

**Description:**
<VulnDiscussion>This policy setting allows you to manage whether Internet Explorer will check revocation status of servers' certificates. Certificates are revoked when they have been compromised or are no longer valid, and this option protects users from submitting confidential data to a site that may be fraudulent or not secure. If you enable this policy setting, Internet Explorer will check to see if server certificates have been revoked. If you disable this policy setting, Internet Explorer will not check server certificates to see if they have been revoked. If you do not configure this policy setting, Internet Explorer will not check server certificates to see if they have been revoked. Satisfies: SRG-APP-000605</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Advanced Page -> 'Check for server certificate revocation' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings Criteria: If the value "CertificateRevocation" is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000131

**Group ID:** `V-223079`

### Rule: Checking for signatures on downloaded programs must be enforced.

**Rule ID:** `SV-223079r942483_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to manage whether Internet Explorer checks for digital signatures (which identifies the publisher of signed software and verifies it has not been modified or tampered with) on user computers before downloading executable programs. If you enable this policy setting, Internet Explorer will check the digital signatures of executable programs and display their identities before downloading them to the user computers. If you disable this policy setting, Internet Explorer will not check the digital signatures of executable programs or display their identities before downloading them to the user computers. If you do not configure this policy, Internet Explorer will not check the digital signatures of executable programs or display their identities before downloading them to the user computers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Advanced Page -> 'Check for signatures on downloaded programs' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Download Criteria: If the value "CheckExeSignatures" is REG_SZ = yes, this is not a finding.

## Group: SRG-APP-000516

**Group ID:** `V-223080`

### Rule: All network paths (UNCs) for Intranet sites must be disallowed.

**Rule ID:** `SV-223080r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some UNC paths could refer to servers not managed by the organization, which means they could host malicious content; and therefore, it is safest to not include all UNC paths in the Intranet Sites zone. This policy setting controls whether URLs representing UNCs are mapped into the local Intranet security zone. If you enable this policy setting, all network paths are mapped into the Intranet Zone. If you disable this policy setting, network paths are not necessarily mapped into the Intranet Zone (other rules might map one there). If you do not configure this policy setting, users choose whether network paths are mapped into the Intranet Zone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> 'Intranet Sites: Include all network paths (UNCs)' must be 'Disabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap Criteria: If the value "UNCAsIntranet" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223081`

### Rule: Script-initiated windows without size or position constraints must be disallowed (Internet zone).

**Rule ID:** `SV-223081r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to manage restrictions on script-initiated pop-up windows and windows including the title and status bars. If you enable this policy setting, Windows Restrictions security will not apply in this zone. The security zone runs without the added layer of security provided by this feature. If you disable this policy setting, the possible harmful actions contained in script-initiated pop-up windows and windows including the title and status bars cannot be run. This Internet Explorer security feature will be on in this zone as dictated by the Scripted Windows Security Restrictions feature control setting for the process. If you do not configure this policy setting, the possible harmful actions contained in script-initiated pop-up windows and windows including the title and status bars cannot be run. This Internet Explorer security feature will be on in this zone as dictated by the Scripted Windows Security Restrictions feature control setting for the process.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Allow script-initiated windows without size or position constraints' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "2102" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223082`

### Rule: Script-initiated windows without size or position constraints must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223082r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to manage restrictions on script-initiated pop-up windows and windows including the title and status bars. If you enable this policy setting, Windows Restrictions security will not apply in this zone. The security zone runs without the added layer of security provided by this feature. If you disable this policy setting, the possible harmful actions contained in script-initiated pop-up windows and windows including the title and status bars cannot be run. This Internet Explorer security feature will be on in this zone as dictated by the Scripted Windows Security Restrictions feature control setting for the process. If you do not configure this policy setting, the possible harmful actions contained in script-initiated pop-up windows and windows including the title and status bars cannot be run. This Internet Explorer security feature will be on in this zone as dictated by the Scripted Windows Security Restrictions feature control setting for the process.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Allow script-initiated windows without size or position constraints' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "2102" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223083`

### Rule: Scriptlets must be disallowed (Internet zone).

**Rule ID:** `SV-223083r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to manage whether scriptlets can be allowed. Scriptlets hosted on sites located in this zone are more likely to contain malicious code. If you enable this policy setting, users will be able to run scriptlets. If you disable this policy setting, users will not be able to run scriptlets. If you do not configure this policy setting, a scriptlet can be enabled or disabled by the user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Allow Scriptlets' must be 'Enabled', and 'Disable' from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "1209" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223084`

### Rule: Automatic prompting for file downloads must be disallowed (Internet zone).

**Rule ID:** `SV-223084r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting determines whether users will be prompted for non user-initiated file downloads. Regardless of this setting, users will receive file download dialogs for user-initiated downloads. Users may accept downloads that they did not request, and those downloaded files may include malicious code. If you enable this setting, users will receive a file download dialog for automatic download attempts. If you disable or do not configure this setting, file downloads that are not user-initiated will be blocked, and users will see the information bar instead of the file download dialog. Users can then click the information bar to allow the file download prompt.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Automatic prompting for file downloads' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "2200" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223085`

### Rule: Java permissions must be disallowed (Local Machine zone).

**Rule ID:** `SV-223085r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Java applications could contain malicious code. This policy setting allows you to manage permissions for Java applets. If you enable this policy setting, options can be chosen from the drop-down box. Use of the Custom permission will control permissions settings individually. Use of the Low Safety permission enables applets to perform all operations. Use of the Medium Safety permission enables applets to run in their sandbox (an area in memory outside of which the program cannot make calls), plus adds capabilities like scratch space (a safe and secure storage area on the client computer) and a user-controlled file I/O. Use of the High Safety permission enables applets to run in their sandbox. If you disable this policy setting, Java applets cannot run. If you do not configure this policy setting, the permission is set to High Safety. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Local Machine Zone -> 'Java permissions' must be 'Enabled', and 'Disable Java' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following keys: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\0 Criteria: If the value "1C00" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-223086`

### Rule: Anti-Malware programs against ActiveX controls must be run for the Local Machine zone.

**Rule ID:** `SV-223086r879628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting determines whether Internet Explorer runs Anti-Malware programs against ActiveX controls, to check if they're safe to load on pages. If you enable this policy setting, Internet Explorer won't check with your Anti-Malware program to see if it's safe to create an instance of the ActiveX control. If you disable this policy setting, Internet Explorer always checks with your Anti-Malware program to see if it's safe to create an instance of the ActiveX control. If you don't configure this policy setting, Internet Explorer won't check with your Anti-Malware program to see if it's safe to create an instance of the ActiveX control. Users can turn this behavior on or off, using Internet Explorer Security settings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer-> Internet Control Panel -> Security Page ->Local Machine Zone 'Don't run antimalware programs against ActiveX controls' must be 'Enabled' and 'Disable' selected in the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\0 Criteria: If the value "270C" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223087`

### Rule: Java permissions must be disallowed (Locked Down Local Machine zone).

**Rule ID:** `SV-223087r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Java applications could contain malicious code. This policy setting allows you to manage permissions for Java applets. If you enable this policy setting, options can be chosen from the drop-down box. Use of the Custom permission will control permissions settings individually. Use of the Low Safety permission enables applets to perform all operations. Use of the Medium Safety permission enables applets to run in their sandbox (an area in memory outside of which the program cannot make calls), plus adds capabilities like scratch space (a safe and secure storage area on the client computer) and a user-controlled file I/O. Use of the High Safety permission enables applets to run in their sandbox. If you disable this policy setting, Java applets cannot run. If you do not configure this policy setting, the permission is set to High Safety.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Locked-Down Local Machine Zone -> 'Java permissions' must be 'Enabled', and 'Disable Java' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following keys: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Lockdown_Zones\0 Criteria: If the value "1C00" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223088`

### Rule: Java permissions must be disallowed (Locked Down Intranet zone).

**Rule ID:** `SV-223088r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Java applications could contain malicious code. This policy setting allows you to manage permissions for Java applets. If you enable this policy setting, options can be chosen from the drop-down box. Use of the Custom permission will control permissions settings individually. Use of the Low Safety permission enables applets to perform all operations. Use of the Medium Safety permission enables applets to run in their sandbox (an area in memory outside of which the program cannot make calls), plus adds capabilities like scratch space (a safe and secure storage area on the client computer) and a user-controlled file I/O. Use of the High Safety permission enables applets to run in their sandbox. If you disable this policy setting, Java applets cannot run. If you do not configure this policy setting, the permission is set to High Safety.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Locked-Down Intranet Zone -> 'Java permissions' must be 'Enabled', and 'Disable Java' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following keys: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Lockdown_Zones\1 Criteria: If the value" 1C00" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223089`

### Rule: Java permissions must be disallowed (Locked Down Trusted Sites zone).

**Rule ID:** `SV-223089r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Java applications could contain malicious code; sites located in this security zone are more likely to be hosted by malicious individuals. This policy setting allows you to manage permissions for Java applets. If you enable this policy setting, options can be chosen from the drop-down box. Use of the Custom permission will control permissions settings individually. Use of the Low Safety permission enables applets to perform all operations. Use of the Medium Safety permission enables applets to run in their sandbox (an area in memory outside of which the program cannot make calls), plus adds capabilities like scratch space (a safe and secure storage area on the client computer) and a user-controlled file I/O. Use of the High Safety permission enables applets to run in their sandbox. If you disable this policy setting, Java applets cannot run. If you do not configure this policy setting, the permission is set to High Safety. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Locked-Down Trusted Sites Zone -> 'Java permissions' must be 'Enabled', and 'Disable Java' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following keys: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Lockdown_Zones\2 Criteria: If the value "1C00" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223090`

### Rule: Java permissions must be disallowed (Locked Down Restricted Sites zone).

**Rule ID:** `SV-223090r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Java applications could contain malicious code. This policy setting allows you to manage permissions for Java applets. If you enable this policy setting, options can be chosen from the drop-down box. Use of the Custom permission will control permissions settings individually. Use of the Low Safety permission enables applets to perform all operations. Use of the Medium Safety permission enables applets to run in their sandbox (an area in memory outside of which the program cannot make calls), plus adds capabilities like scratch space (a safe and secure storage area on the client computer) and a user-controlled file I/O. Use of the High Safety permission enables applets to run in their sandbox. If you disable this policy setting, Java applets cannot run. If you do not configure this policy setting, the permission is set to High Safety. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Locked-Down Restricted Sites Zone -> 'Java permissions' must be 'Enabled', and 'Disable Java' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following keys: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Lockdown_Zones\4 Criteria: If the value "1C00" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000516

**Group ID:** `V-223091`

### Rule: XAML files must be disallowed (Internet zone).

**Rule ID:** `SV-223091r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>These are eXtensible Application Markup Language (XAML) files. XAML is an XML-based declarative markup language commonly used for creating rich user interfaces and graphics that leverage the Windows Presentation Foundation. If you enable this policy setting and the drop-down box is set to Enable, XAML files will be automatically loaded inside Internet Explorer. Users will not be able to change this behavior. If the drop-down box is set to Prompt, users will receive a prompt for loading XAML files. If you disable this policy setting, XAML files will not be loaded inside Internet Explorer. Users will not be able to change this behavior. If you do not configure this policy setting, users will have the freedom to decide whether to load XAML files inside Internet Explorer.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Allow loading of XAML files' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "2402" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000516

**Group ID:** `V-223092`

### Rule: XAML files must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223092r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>These are eXtensible Application Markup Language (XAML) files. XAML is an XML-based declarative markup language commonly used for creating rich user interfaces and graphics that leverage the Windows Presentation Foundation. If you enable this policy setting and the drop-down box is set to Enable, XAML files will be automatically loaded inside Internet Explorer. Users will not be able to change this behavior. If the drop-down box is set to Prompt, users will receive a prompt for loading XAML files. If you disable this policy setting, XAML files will not be loaded inside Internet Explorer. Users will not be able to change this behavior. If you do not configure this policy setting, users will have the freedom to decide whether to load XAML files inside Internet Explorer.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Allow loading of XAML files' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "2402" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000233

**Group ID:** `V-223093`

### Rule: Protected Mode must be enforced (Internet zone).

**Rule ID:** `SV-223093r879643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protected Mode protects Internet Explorer from exploited vulnerabilities by reducing the locations Internet Explorer can write to in the registry and the file system. If you enable this policy setting, Protected Mode will be turned on. Users will not be able to turn off Protected Mode. If you disable this policy setting, Protected Mode will be turned off. It will revert to Internet Explorer 6 behavior that allows for Internet Explorer to write to the registry and the file system. Users will not be able to turn on Protected Mode. If you do not configure this policy, users will be able to turn on or off Protected Mode.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Turn on Protected Mode' must be 'Enabled', and 'Enable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "2500" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000233

**Group ID:** `V-223094`

### Rule: Protected Mode must be enforced (Restricted Sites zone).

**Rule ID:** `SV-223094r879643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protected Mode protects Internet Explorer from exploited vulnerabilities by reducing the locations Internet Explorer can write to in the registry and the file system. If you enable this policy setting, Protected Mode will be turned on. Users will not be able to turn off Protected Mode. If you disable this policy setting, Protected Mode will be turned off. It will revert to Internet Explorer 6 behavior that allows for Internet Explorer to write to the registry and the file system. Users will not be able to turn on Protected Mode. If you do not configure this policy, users will be able to turn on or off Protected Mode.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Turn on Protected Mode' must be 'Enabled', and 'Enable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "2500" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223095`

### Rule: Pop-up Blocker must be enforced (Internet zone).

**Rule ID:** `SV-223095r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to manage whether unwanted pop-up windows appear. Pop-up windows that are opened when the end user clicks a link are not blocked. If you enable this policy setting, most unwanted pop-up windows are prevented from appearing. If you disable this policy setting, pop-up windows are not prevented from appearing. If you do not configure this policy setting, most unwanted pop-up windows are prevented from appearing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Use Pop-up Blocker' must be 'Enabled', and 'Enable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "1809" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223096`

### Rule: Pop-up Blocker must be enforced (Restricted Sites zone).

**Rule ID:** `SV-223096r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to manage whether unwanted pop-up windows appear. Pop-up windows that are opened when the end user clicks a link are not blocked. If you enable this policy setting, most unwanted pop-up windows are prevented from appearing. If you disable this policy setting, pop-up windows are not prevented from appearing. If you do not configure this policy setting, most unwanted pop-up windows are prevented from appearing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Use Pop-up Blocker' must be 'Enabled', and 'Enable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1809" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000039

**Group ID:** `V-223097`

### Rule: Websites in less privileged web content zones must be prevented from navigating into the Internet zone.

**Rule ID:** `SV-223097r879534_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows a user to manage whether websites from less privileged zones, such as Restricted Sites, can navigate into the Internet zone. If this policy setting is enabled, websites from less privileged zones can open new windows in, or navigate into, this zone. The security zone will run without the added layer of security that is provided by the Protection from Zone Elevation security feature. If "Prompt" is selected in the drop-down box, a warning is issued to the user that potentially risky navigation is about to occur. If this policy setting is disabled, the potentially risky navigation is prevented. The Internet Explorer security feature will be on in this zone as set by the Protection from Zone Elevation feature control. If this policy setting is not configured, websites from less privileged zones can open new windows in, or navigate into, this zone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Web sites in less privileged Web content zones can navigate into this zone' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "2101" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000039

**Group ID:** `V-223098`

### Rule: Websites in less privileged web content zones must be prevented from navigating into the Restricted Sites zone.

**Rule ID:** `SV-223098r879534_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to manage whether websites from less privileged zones, such as Restricted Sites, can navigate into the Restricted zone. If this policy setting is enabled, websites from less privileged zones can open new windows in, or navigate into, this zone. The security zone will run without the added layer of security that is provided by the Protection from Zone Elevation security feature. If Prompt is selected in the drop-down box, a warning is issued to the user that potentially risky navigation is about to occur. If this policy setting is disabled, the potentially risky navigation is prevented. The Internet Explorer security feature will be on in this zone as set by the Protection from Zone Elevation feature control. If this policy setting is not configured, websites from less privileged zones can open new windows in, or navigate into, this zone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Web sites in less privileged Web content zones can navigate into this zone' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "2101" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223099`

### Rule: Allow binary and script behaviors must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223099r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to manage dynamic binary and script behaviors of components that encapsulate specific functionality for HTML elements, to which they were attached. If you enable this policy setting, binary and script behaviors are available. If you select "Administrator approved" in the drop-down box, only the behaviors listed in the Admin-approved Behaviors under Binary Behaviors Security Restriction policy are available. If you disable this policy setting, binary and script behaviors are not available unless applications have implemented a custom security manager. If you do not configure this policy setting, binary and script behaviors are available.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Allow binary and script behaviors' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "2000" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223100`

### Rule: Automatic prompting for file downloads must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223100r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting determines whether users will be prompted for non user-initiated file downloads. Regardless of this setting, users will receive file download dialogs for user-initiated downloads. Users may accept downloads that they did not request, and those downloaded files may include malicious code. If you enable this setting, users will receive a file download dialog for automatic download attempts. If you disable or do not configure this setting, file downloads that are not user-initiated will be blocked, and users will see the information bar instead of the file download dialog. Users can then click the information bar to allow the file download prompt.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Automatic prompting for file downloads' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "2200" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000206

**Group ID:** `V-223101`

### Rule: Internet Explorer Processes for MIME handling must be enforced. (Reserved)

**Rule ID:** `SV-223101r879627_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Explorer uses Multipurpose Internet Mail Extensions (MIME) data to determine file handling procedures for files received through a web server. The Consistent MIME Handling\Internet Explorer Processes policy setting determines whether Internet Explorer requires all file-type information provided by web servers to be consistent. For example, if the MIME type of a file is text/plain but the MIME data indicates the file is really an executable file, Internet Explorer changes its extension to reflect this executable status. This capability helps ensure executable code cannot masquerade as other types of data that may be trusted. If you enable this policy setting, Internet Explorer examines all received files and enforces consistent MIME data for them. If you disable or do not configure this policy setting, Internet Explorer does not require consistent MIME data for all received files and will use the MIME data provided by the file. MIME file-type spoofing is a potential threat to an organization. Ensuring these files are consistent and properly labeled helps prevent malicious file downloads from infecting your network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> Consistent Mime Handling -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_MIME_HANDLING Criteria: If the value "(Reserved)" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000206

**Group ID:** `V-223102`

### Rule: Internet Explorer Processes for MIME handling must be enforced (Explorer).

**Rule ID:** `SV-223102r879627_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Explorer uses Multipurpose Internet Mail Extensions (MIME) data to determine file handling procedures for files received through a web server. The Consistent MIME Handling\Internet Explorer Processes policy setting determines whether Internet Explorer requires all file-type information provided by web servers to be consistent. For example, if the MIME type of a file is text/plain but the MIME data indicates the file is really an executable file, Internet Explorer changes its extension to reflect this executable status. This capability helps ensure executable code cannot masquerade as other types of data that may be trusted. If you enable this policy setting, Internet Explorer examines all received files and enforces consistent MIME data for them. If you disable or do not configure this policy setting, Internet Explorer does not require consistent MIME data for all received files and will use the MIME data provided by the file. MIME file-type spoofing is a potential threat to the organization. Ensuring these files are consistent and properly labeled helps prevent malicious file downloads from infecting the network. This guide recommends configuring this policy as "Enabled" for all environments specified in this guide.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> Consistent Mime Handling -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_MIME_HANDLING Criteria: If the value "explorer.exe" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000206

**Group ID:** `V-223103`

### Rule: Internet Explorer Processes for MIME handling must be enforced (iexplore).

**Rule ID:** `SV-223103r879627_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Explorer uses Multipurpose Internet Mail Extensions (MIME) data to determine file handling procedures for files received through a web server. The Consistent MIME Handling\Internet Explorer Processes policy setting determines whether Internet Explorer requires all file-type information provided by web servers to be consistent. For example, if the MIME type of a file is text/plain but the MIME data indicates that the file is really an executable file, Internet Explorer changes its extension to reflect this executable status. This capability helps ensure that executable code cannot masquerade as other types of data that may be trusted. If you enable this policy setting, Internet Explorer examines all received files and enforces consistent MIME data for them. If you disable or do not configure this policy setting, Internet Explorer does not require consistent MIME data for all received files and will use the MIME data provided by the file. MIME file-type spoofing is a potential threat to an organization. Ensuring these files are consistent and properly labeled helps prevent malicious file downloads from infecting the network. This guide recommends configuring this policy as "Enabled" for all environments specified in this guide.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> Consistent Mime Handling -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_MIME_HANDLING Criteria: If the value "iexplore.exe" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000206

**Group ID:** `V-223104`

### Rule: Internet Explorer Processes for MIME sniffing must be enforced (Reserved).

**Rule ID:** `SV-223104r879627_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MIME sniffing is the process of examining the content of a MIME file to determine its context - whether it is a data file, an executable file, or some other type of file. This policy setting determines whether Internet Explorer MIME sniffing will prevent promotion of a file of one type to a more dangerous file type. When set to "Enabled", MIME sniffing will never promote a file of one type to a more dangerous file type. Disabling MIME sniffing configures Internet Explorer processes to allow a MIME sniff that promotes a file of one type to a more dangerous file type. For example, promoting a text file to an executable file is a dangerous promotion because any code in the supposed text file would be executed. MIME file-type spoofing is a potential threat to an organization. Ensuring these files are consistently handled helps prevent malicious file downloads from infecting the network. This guide recommends you configure this policy as "Enabled" for all environments specified in this guide. Note: This setting works in conjunction with, but does not replace, the Consistent MIME Handling settings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> Mime Sniffing Safety Feature -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_MIME_SNIFFING Criteria: If the value "(Reserved)" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000206

**Group ID:** `V-223105`

### Rule: Internet Explorer Processes for MIME sniffing must be enforced (Explorer).

**Rule ID:** `SV-223105r879627_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MIME sniffing is the process of examining the content of a MIME file to determine its context - whether it is a data file, an executable file, or some other type of file. This policy setting determines whether Internet Explorer MIME sniffing will prevent promotion of a file of one type to a more dangerous file type. When set to "Enabled", MIME sniffing will never promote a file of one type to a more dangerous file type. Disabling MIME sniffing configures Internet Explorer processes to allow a MIME sniff that promotes a file of one type to a more dangerous file type. For example, promoting a text file to an executable file is a dangerous promotion because any code in the supposed text file would be executed. MIME file-type spoofing is a potential threat to an organization. Ensuring these files are consistently handled helps prevent malicious file downloads from infecting the network. This guide recommends configuring this policy as "Enabled" for all environments specified in this guide. Note: This setting works in conjunction with, but does not replace, the Consistent MIME Handling settings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> Mime Sniffing Safety Feature -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_MIME_SNIFFING Criteria: If the value "explorer.exe" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000206

**Group ID:** `V-223106`

### Rule: Internet Explorer Processes for MIME sniffing must be enforced (iexplore).

**Rule ID:** `SV-223106r879627_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MIME sniffing is the process of examining the content of a MIME file to determine its context - whether it is a data file, an executable file, or some other type of file. This policy setting determines whether Internet Explorer MIME sniffing will prevent promotion of a file of one type to a more dangerous file type. When set to "Enabled", MIME sniffing will never promote a file of one type to a more dangerous file type. Disabling MIME sniffing configures Internet Explorer processes to allow a MIME sniff that promotes a file of one type to a more dangerous file type. For example, promoting a text file to an executable file is a dangerous promotion because any code in the supposed text file would be executed. MIME file-type spoofing is a potential threat to an organization. Ensuring these files are consistently handled helps prevent malicious file downloads from infecting the network. This guide recommends configuring this policy as "Enabled" for all environments specified in this guide. Note: This setting works in conjunction with, but does not replace, the Consistent MIME Handling settings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> Mime Sniffing Safety Feature -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_MIME_SNIFFING Criteria: If the value "iexplore.exe" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223107`

### Rule: Internet Explorer Processes for MK protocol must be enforced (Reserved).

**Rule ID:** `SV-223107r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The MK Protocol Security Restriction policy setting reduces attack surface area by blocking the seldom used MK protocol. Some older web applications use the MK protocol to retrieve information from compressed files. Because the MK protocol is not widely used, it should be blocked wherever it is not needed. Setting this policy to "Enabled"; blocks the MK protocol for Windows Explorer and Internet Explorer, which causes resources that use the MK protocol to fail. Disabling this setting allows applications to use the MK protocol API. This guide recommends configuring this setting to "Enabled" to block the MK protocol unless it is specifically needed in the environment. Note: Because resources that use the MK protocol will fail when deploying this setting, ensure none of the applications use the MK protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> MK Protocol Security Restriction -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_DISABLE_MK_PROTOCOL Criteria: If the value "(Reserved)" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223108`

### Rule: Internet Explorer Processes for MK protocol must be enforced (Explorer).

**Rule ID:** `SV-223108r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The MK Protocol Security Restriction policy setting reduces attack surface area by blocking the seldom used MK protocol. Some older web applications use the MK protocol to retrieve information from compressed files. Because the MK protocol is not widely used, it should be blocked wherever it is not needed. Setting this policy to "Enabled"; blocks the MK protocol for Windows Explorer and Internet Explorer, which causes resources that use the MK protocol to fail. Disabling this setting allows applications to use the MK protocol API. This guide recommends you configure this setting to "Enabled" to block the MK protocol unless it is specifically needed in the environment. Note: Because resources that use the MK protocol will fail when deploying this setting, ensure none of the applications use the MK protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> MK Protocol Security Restriction -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_DISABLE_MK_PROTOCOL Criteria: If the value "explorer.exe" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223109`

### Rule: Internet Explorer Processes for MK protocol must be enforced (iexplore).

**Rule ID:** `SV-223109r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The MK Protocol Security Restriction policy setting reduces attack surface area by blocking the seldom used MK protocol. Some older web applications use the MK protocol to retrieve information from compressed files. Because the MK protocol is not widely used, it should be blocked wherever it is not needed. Setting this policy to "Enabled"; blocks the MK protocol for Windows Explorer and Internet Explorer, which causes resources that use the MK protocol to fail. Disabling this setting allows applications to use the MK protocol API. This guide recommends you configure this setting to "Enabled" to block the MK protocol unless specifically needed in the environment. Note: Because resources that use the MK protocol will fail when deploying this setting, ensure none of the applications use the MK protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> MK Protocol Security Restriction -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_DISABLE_MK_PROTOCOL Criteria: If the value "iexplore.exe" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000233

**Group ID:** `V-223110`

### Rule: Internet Explorer Processes for Zone Elevation must be enforced (Reserved).

**Rule ID:** `SV-223110r879643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Explorer places restrictions on each web page it opens that are dependent upon the location of the web page (such as Internet Zone, Intranet Zone, or Local Machine Zone). Web pages on a local computer have the fewest security restrictions and reside in the Local Machine Zone, which makes the Local Machine Security Zone a prime target for malicious attackers. If you enable this policy setting, any zone can be protected from zone elevation by Internet Explorer processes. This approach stops content running in one zone from gaining the elevated privileges of another zone. If you disable this policy setting, no zone receives such protection from Internet Explorer processes. Because of the severity and relative frequency of zone elevation attacks, this guide recommends that you configure this setting as "Enabled" in all environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> Protection From Zone Elevation -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_ZONE_ELEVATION Criteria: If the value "(Reserved)" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000233

**Group ID:** `V-223111`

### Rule: Internet Explorer Processes for Zone Elevation must be enforced (Explorer).

**Rule ID:** `SV-223111r879643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Explorer places restrictions on each web page it opens that are dependent upon the location of the web page (such as Internet Zone, Intranet Zone, or Local Machine Zone). Web pages on a local computer have the fewest security restrictions and reside in the Local Machine Zone, which makes the Local Machine Security Zone a prime target for malicious attackers. If you enable this policy setting, any zone can be protected from zone elevation by Internet Explorer processes. This approach stops content running in one zone from gaining the elevated privileges of another zone. If you disable this policy setting, no zone receives such protection from Internet Explorer processes. Because of the severity and relative frequency of zone elevation attacks, this guide recommends configuring this setting as "Enabled" in all environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> Protection From Zone Elevation -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_ZONE_ELEVATION Criteria: If the value "explorer.exe" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000233

**Group ID:** `V-223112`

### Rule: Internet Explorer Processes for Zone Elevation must be enforced (iexplore).

**Rule ID:** `SV-223112r879643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Explorer places restrictions on each web page it opens that are dependent upon the location of the web page (such as Internet Zone, Intranet Zone, or Local Machine Zone). Web pages on a local computer have the fewest security restrictions and reside in the Local Machine Zone, which makes the Local Machine Security Zone a prime target for malicious attackers. If you enable this policy setting, any zone can be protected from zone elevation by Internet Explorer processes. This approach stops content running in one zone from gaining the elevated privileges of another zone. If you disable this policy setting, no zone receives such protection from Internet Explorer processes. Because of the severity and relative frequency of zone elevation attacks, this guide recommends that you configure this setting as "Enabled" in all environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> Protection From Zone Elevation -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_ZONE_ELEVATION Criteria: If the value "iexplore.exe" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223113`

### Rule: Internet Explorer Processes for Restrict File Download must be enforced (Reserved).

**Rule ID:** `SV-223113r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain circumstances, websites can initiate file download prompts without interaction from users. This technique can allow websites to put unauthorized files on users' hard drives if they click the wrong button and accept the download. If you configure the Restrict File Download\Internet Explorer Processes policy setting to "Enabled", file download prompts that are not user-initiated are blocked for Internet Explorer processes. If you configure this policy setting as "Disabled", prompting will occur for file downloads that are not user-initiated for Internet Explorer processes. Note: This setting is configured as "Enabled" in all environments specified in this guide to help prevent attackers from placing arbitrary code on users' computers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> Restrict File Download -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_RESTRICT_FILEDOWNLOAD Criteria: If the value "(Reserved)" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223114`

### Rule: Internet Explorer Processes for Restrict File Download must be enforced (Explorer).

**Rule ID:** `SV-223114r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain circumstances, websites can initiate file download prompts without interaction from users. This technique can allow websites to put unauthorized files on users' hard drives if they click the wrong button and accept the download. If you configure the Restrict File Download\Internet Explorer Processes policy setting to "Enabled", file download prompts that are not user-initiated are blocked for Internet Explorer processes. If you configure this policy setting as "Disabled", prompting will occur for file downloads that are not user-initiated for Internet Explorer processes. Note: This setting is configured as "Enabled" in all environments specified in this guide to help prevent attackers from placing arbitrary code on users' computers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> Restrict File Download -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_RESTRICT_FILEDOWNLOAD Criteria: If the value "explorer.exe" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223115`

### Rule: Internet Explorer Processes for Restrict File Download must be enforced (iexplore).

**Rule ID:** `SV-223115r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain circumstances, websites can initiate file download prompts without interaction from users. This technique can allow websites to put unauthorized files on users' hard drives if they click the wrong button and accept the download. If you configure the Restrict File Download\Internet Explorer Processes policy setting to "Enabled", file download prompts that are not user-initiated are blocked for Internet Explorer processes. If you configure this policy setting as "Disabled", prompting will occur for file downloads that are not user-initiated for Internet Explorer processes. Note: This setting is configured as "Enabled" in all environments specified in this guide to help prevent attackers from placing arbitrary code on users' computers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> Restrict File Download -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_RESTRICT_FILEDOWNLOAD Criteria: If the value "iexplore.exe" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223116`

### Rule: Internet Explorer Processes for restricting pop-up windows must be enforced (Reserved).

**Rule ID:** `SV-223116r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Explorer allows scripts to programmatically open, resize, and reposition various types of windows. Often, disreputable websites will resize windows to either hide other windows or force the user to interact with a window containing malicious code. The Scripted Window Security Restrictions security feature restricts pop-up windows and prohibits scripts from displaying windows in which the title and status bars are not visible to the user, or which hide other windows' title and status bars. If you enable the Scripted Window Security Restrictions\Internet Explorer Processes policy setting, pop-up windows and other restrictions apply for Windows Explorer and Internet Explorer processes. If you disable or do not configure this policy setting, scripts can continue to create pop-up windows, and create windows that hide other windows. Recommend configuring this setting to "Enabled" to help prevent malicious websites from controlling the Internet Explorer windows or fooling users into clicking on the wrong window.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> Scripted Window Security Restrictions -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_WINDOW_RESTRICTIONS Criteria: If the value "(Reserved)" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223117`

### Rule: Internet Explorer Processes for restricting pop-up windows must be enforced (Explorer).

**Rule ID:** `SV-223117r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Explorer allows scripts to programmatically open, resize, and reposition various types of windows. Often, disreputable websites will resize windows to either hide other windows or force a user to interact with a window that contains malicious code. The Scripted Window Security Restrictions security feature restricts pop-up windows and prohibits scripts from displaying windows in which the title and status bars are not visible to the user, or which hide other windows' title and status bars. If you enable the Scripted Window Security Restrictions\Internet Explorer Processes policy setting, pop-up windows and other restrictions apply for Windows Explorer and Internet Explorer processes. If you disable or do not configure this policy setting, scripts can continue to create pop-up windows and create windows that hide other windows. This guide recommends configuring this setting to "Enabled" to help prevent malicious websites from controlling the Internet Explorer windows or fooling users into clicking on the wrong window.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> Scripted Window Security Restrictions -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_WINDOW_RESTRICTIONS Criteria: If the value "explorer.exe is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223118`

### Rule: Internet Explorer Processes for restricting pop-up windows must be enforced (iexplore).

**Rule ID:** `SV-223118r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Explorer allows scripts to programmatically open, resize, and reposition various types of windows. Often, disreputable websites will resize windows to either hide other windows or force a user to interact with a window that contains malicious code. The Scripted Window Security Restrictions security feature restricts pop-up windows and prohibits scripts from displaying windows in which the title and status bars are not visible to the user, or which hide other windows' title and status bars. If you enable the Scripted Window Security Restrictions\Internet Explorer Processes policy setting, pop-up windows and other restrictions apply for Windows Explorer and Internet Explorer processes. If you disable or do not configure this policy setting, scripts can continue to create pop-up windows and create windows that hide other windows. This guide recommends configuring this setting to "Enabled" to help prevent malicious websites from controlling the Internet Explorer windows or fooling users into clicking on the wrong window.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> Scripted Window Security Restrictions -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_WINDOW_RESTRICTIONS Criteria: If the value "iexplore.exe" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000516

**Group ID:** `V-223119`

### Rule: .NET Framework-reliant components not signed with Authenticode must be disallowed to run (Restricted Sites Zone).

**Rule ID:** `SV-223119r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to manage whether .NET Framework-reliant components that are not signed with Authenticode can be executed from Internet Explorer. These components include managed controls referenced from an object tag and managed executables referenced from a link. If you enable this policy setting, Internet Explorer will execute unsigned managed components. If you select "Prompt" in the drop-down box, Internet Explorer will prompt the user to determine whether to execute unsigned managed components. If you disable this policy setting, Internet Explorer will not execute unsigned managed components. If you do not configure this policy setting, Internet Explorer will execute unsigned managed components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Run .NET Framework-reliant components not signed with Authenticode' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "2004" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000516

**Group ID:** `V-223120`

### Rule: .NET Framework-reliant components signed with Authenticode must be disallowed to run (Restricted Sites Zone).

**Rule ID:** `SV-223120r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to manage whether .NET Framework-reliant components that are signed with Authenticode can be executed from Internet Explorer. It may be possible for malicious content hosted on a website to take advantage of these components. These components include managed controls referenced from an object tag and managed executables referenced from a link. If you enable this policy setting, Internet Explorer will execute signed managed components. If you select "Prompt" in the drop-down box, Internet Explorer will prompt the user to determine whether to execute signed managed components. If you disable this policy setting, Internet Explorer will not execute signed managed components. If you do not configure this policy setting, Internet Explorer will execute signed managed components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Run .NET Framework-reliant components signed with Authenticode' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "2001" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223121`

### Rule: Scripting of Java applets must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223121r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to manage whether applets are exposed to scripts within the zone. If you enable this policy setting, scripts can access applets automatically without user intervention. If you select "Prompt" in the drop-down box, users are queried to choose whether to allow scripts to access applets. If you disable this policy setting, scripts are prevented from accessing applets. If you do not configure this policy setting, scripts can access applets automatically without user intervention. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Scripting of Java applets' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1402" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223122`

### Rule: AutoComplete feature for forms must be disallowed.

**Rule ID:** `SV-223122r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This AutoComplete feature suggests possible matches when users are filling in forms. It is possible that this feature will cache sensitive data and store it in the user's profile, where it might not be protected as rigorously as required by organizational policy. If you enable this setting, the user is not presented with suggested matches when filling in forms. If you disable this setting, the user is presented with suggested possible matches when filling forms. If you do not configure this setting, the user has the freedom to turn on the auto-complete feature for forms. To display this option, the user opens the Internet Options dialog box, clicks the "Contents" tab, and clicks the "Settings" button.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for User Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> 'Disable AutoComplete for forms' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Internet Explorer\Main Criteria: If the value "Use FormSuggest" is REG_SZ = no, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223123`

### Rule: Crash Detection management must be enforced.

**Rule ID:** `SV-223123r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The 'Turn off Crash Detection' policy setting allows you to manage the crash detection feature of add-on management in Internet Explorer. A crash report could contain sensitive information from the computer's memory. If you enable this policy setting, a crash in Internet Explorer will be similar to one on a computer running Windows XP Professional Service Pack 1 and earlier, where Windows Error Reporting will be invoked. If you disable this policy setting, the crash detection feature in add-on management will be functional. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> 'Turn off Crash Detection' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key:HKLM\Software\Policies\Microsoft\Internet Explorer\Restrictions Criteria: If the value "NoCrashDetection" is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223124`

### Rule: Turn on the auto-complete feature for user names and passwords on forms must be disabled.

**Rule ID:** `SV-223124r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls automatic completion of fields in forms on web pages. It is possible that malware could be developed which would be able to extract the cached user names and passwords from the currently logged on user, which an attacker could then use to compromise that user's online accounts. If you enable this setting, the user cannot change the 'User name and passwords on forms' or 'prompt me to save passwords'. The Auto Complete feature for" User names and passwords on forms" will be turned on. If you disable this setting, the user cannot change the 'User name and passwords on forms' or 'prompt me to save passwords'. The Auto Complete feature for "User names and passwords on forms" is turned off. The user also cannot opt to be prompted to save passwords. If you do not configure this setting, the user has the freedom of turning on Auto Complete for "User name and passwords on forms", and the option of prompting to save passwords.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for User Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> 'Turn on the auto-complete feature for user names and passwords on forms' must be 'Disabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Internet Explorer\Main Criteria: If the value "FormSuggest Passwords" is REG_SZ = 'no', this is not a finding. AND Procedure: Use the Windows Registry Editor to navigate to the following key: HKCU\Software\Policies\Microsoft\Internet Explorer\Main Criteria: If the value "FormSuggest PW Ask" is REG_SZ = 'no', this is not a finding.

## Group: SRG-APP-000206

**Group ID:** `V-223125`

### Rule: Managing SmartScreen Filter use must be enforced.

**Rule ID:** `SV-223125r879627_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting is important from a security perspective because Microsoft has extensive data illustrating the positive impact the SmartScreen filter has had on reducing the risk of malware infection via visiting malicious websites. This policy setting allows users to enable the SmartScreen Filter, which will warn if the website being visited is known for fraudulent attempts to gather personal information through 'phishing' or is known to host malware. If you enable this setting the user will not be prompted to enable the SmartScreen Filter. It must be specified which mode the SmartScreen Filter uses: On or Off. If the feature is On, all website addresses not contained on the filters allow list, will be sent automatically to Microsoft without prompting the user. If this feature is set to Off, the feature will not run. If you disable or do not configure this policy setting, the user is prompted to decide whether to turn on SmartScreen Filter during the first-run experience.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is on the SIPRNet, this requirement is NA. The policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Internet Explorer >> "Prevent Managing SmartScreen Filter" must be "Enabled", and "On" selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\PhishingFilter Criteria: If the value "EnabledV9" is "REG_DWORD = 1", this is not a finding.

## Group: SRG-APP-000089

**Group ID:** `V-223126`

### Rule: Browser must retain history on exit.

**Rule ID:** `SV-223126r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Delete Browsing History on exit automatically deletes specified items when the last browser window closes. Disabling this function will prevent users from deleting their browsing history, which could be used to identify malicious websites and files that could later be used for anti-virus and Intrusion Detection System (IDS) signatures. Furthermore, preventing users from deleting browsing history could be used to identify abusive web surfing on government systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Delete Browsing History -> 'Allow deleting browsing history on exit' must be 'Disabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Privacy Criteria: If the value "ClearBrowsingHistoryOnExit" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000089

**Group ID:** `V-223127`

### Rule: Deleting websites that the user has visited must be disallowed.

**Rule ID:** `SV-223127r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy prevents users from deleting the history of websites the user has visited. If you enable this policy setting, websites the user has visited will be preserved when the user clicks "Delete". If you disable this policy setting, websites that the user has visited will be deleted when the user clicks "Delete". If you do not configure this policy setting, the user will be able to select whether to delete or preserve websites the user visited when the user clicks "Delete".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Delete Browsing History -> 'Prevent Deleting Web sites that the User has Visited' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Privacy Criteria: If the value "CleanHistory" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000080

**Group ID:** `V-223128`

### Rule: InPrivate Browsing must be disallowed.

**Rule ID:** `SV-223128r879554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>InPrivate Browsing lets the user control whether or not Internet Explorer saves the browsing history, cookies, and other data. User control of settings is not the preferred control method. The InPrivate Browsing feature in Internet Explorer makes browser privacy easy by not storing history, cookies, temporary Internet files, or other data. If you enable this policy setting, InPrivate Browsing will be disabled. If you disable this policy setting, InPrivate Browsing will be available for use. If you do not configure this setting, InPrivate Browsing can be turned on or off through the registry.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Privacy -> 'Turn off InPrivate Browsing' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Privacy Criteria: If the value "EnableInPrivateBrowsing" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223129`

### Rule: Scripting of Internet Explorer WebBrowser control property must be disallowed (Internet zone).

**Rule ID:** `SV-223129r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls whether a page may control embedded WebBrowser control via script. Scripted code hosted on sites located in this zone is more likely to contain malicious code. If you enable this policy setting, script access to the WebBrowser control is allowed. If you disable this policy setting, script access to the WebBrowser control is not allowed. If you do not configure this policy setting, script access to the WebBrowser control can be enabled or disabled by the user. By default, script access to the WebBrowser control is only allowed in the Local Machine and Intranet Zones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Allow scripting of Internet Explorer WebBrowser controls' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "1206" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223130`

### Rule: When uploading files to a server, the local directory path must be excluded (Internet zone).

**Rule ID:** `SV-223130r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls whether or not the local path information will be sent when uploading a file via a HTML form. If the local path information is sent, some information may be unintentionally revealed to the server. If you do not configure this policy setting, the user can choose whether path information will be sent when uploading a file via a form. By default, path information will be sent.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Include local path when user is uploading files to a server' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "160A" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223131`

### Rule: Internet Explorer Processes for Notification Bars must be enforced (Reserved).

**Rule ID:** `SV-223131r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to manage whether the Notification Bar is displayed for Internet Explorer processes when file or code installs are restricted. By default, the Notification Bar is displayed for Internet Explorer processes. If you enable this policy setting, the Notification Bar will be displayed for Internet Explorer processes. If you disable this policy setting, the Notification Bar will not be displayed for Internet Explorer processes. If you do not configure this policy setting, the Notification Bar will be displayed for Internet Explorer processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features-> Notification Bar-> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_SECURITYBAND Criteria: If the value "(Reserved)" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000516

**Group ID:** `V-223132`

### Rule: Security Warning for unsafe files must be set to prompt (Internet zone).

**Rule ID:** `SV-223132r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls whether or not the 'Open File - Security Warning' message appears when the user tries to open executable files or other potentially unsafe files (from an intranet file shared by using Windows Explorer, for example). If you enable this policy setting and set the drop-down box to "Enable", these files open without a security warning. If you set the drop-down box to " Prompt", a security warning appears before the files open. If you disable this policy these files do not open. If you do not configure this policy setting, the user can configure how the computer handles these files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Show security warning for potentially unsafe files' must be 'Enabled', and 'Prompt' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "1806" is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223133`

### Rule: Internet Explorer Processes for Notification Bars must be enforced (Explorer).

**Rule ID:** `SV-223133r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to manage whether the Notification Bar is displayed for Internet Explorer processes when file or code installs are restricted. By default, the Notification Bar is displayed for Internet Explorer processes. If you enable this policy setting, the Notification Bar will be displayed for Internet Explorer processes. If you disable this policy setting, the Notification Bar will not be displayed for Internet Explorer processes. If you do not configure this policy setting, the Notification Bar will be displayed for Internet Explorer processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features-> Notification Bar-> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_SECURITYBAND Criteria: If the value "explorer.exe" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-223134`

### Rule: ActiveX controls without prompt property must be used in approved domains only (Internet zone).

**Rule ID:** `SV-223134r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls whether or not the user is prompted to allow ActiveX controls to run on websites other than the website that installed the ActiveX control. If the user were to disable the setting for the zone, malicious ActiveX controls could be executed without the user's knowledge. Disabling this setting would allow the possibility for malicious ActiveX controls to be executed from non-approved domains within this zone without the user's knowledge. Enabling this setting enforces the default value and prohibits the user from changing the value. Websites should be moved into another zone if permissions need to be changed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> ' Allow only approved domains to use ActiveX controls without prompt' must be 'Enabled', and 'Enable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "120b" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223135`

### Rule: Internet Explorer Processes for Notification Bars must be enforced (iexplore).

**Rule ID:** `SV-223135r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to manage whether the Notification Bar is displayed for Internet Explorer processes when file or code installs are restricted. By default, the Notification Bar is displayed for Internet Explorer processes. If you enable this policy setting, the Notification Bar will be displayed for Internet Explorer processes. If you disable this policy setting, the Notification Bar will not be displayed for Internet Explorer processes. If you do not configure this policy setting, the Notification Bar will be displayed for Internet Explorer processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features-> Notification Bar-> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_SECURITYBAND Criteria: If the value "iexplore.exe" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223136`

### Rule: Cross-Site Scripting Filter must be enforced (Internet zone).

**Rule ID:** `SV-223136r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Cross-Site Scripting Filter is designed to prevent users from becoming victims of unintentional information disclosure. This setting controls if the Cross-Site Scripting (XSS) Filter detects and prevents cross-site script injection into websites in this zone. If you enable this policy setting, the XSS Filter will be enabled for sites in this zone, and the XSS Filter will attempt to block cross-site script injections. If you disable this policy setting, the XSS Filter will be disabled for sites in this zone, and Internet Explorer will permit cross-site script injections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone -> 'Turn on Cross-Site Scripting Filter' must be 'Enabled', and 'Enable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "1409" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223137`

### Rule: Scripting of Internet Explorer WebBrowser Control must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223137r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls whether a page may control embedded WebBrowser Control via script. Scripted code hosted on sites located in this zone is more likely to contain malicious code. If you enable this policy setting, script access to the WebBrowser Control is allowed. If you disable this policy setting, script access to the WebBrowser Control is not allowed. If you do not configure this policy setting, script access to the WebBrowser Control can be enabled or disabled by the user. By default, script access to the WebBrowser Control is only allowed in the Local Machine and Intranet Zones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Allow scripting of Internet Explorer WebBrowser controls' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1206" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223138`

### Rule: When uploading files to a server, the local directory path must be excluded (Restricted Sites zone).

**Rule ID:** `SV-223138r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls whether or not the local path information will be sent when uploading a file via a HTML form. If the local path information is sent, some information may be unintentionally revealed to the server. If you do not configure this policy setting, the user can choose whether path information will be sent when uploading a file via a form. By default, path information will be sent.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Include local path when user is uploading files to a server' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "160A" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000516

**Group ID:** `V-223139`

### Rule: Security Warning for unsafe files must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223139r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls whether or not the 'Open File - Security Warning' message appears when the user tries to open executable files or other potentially unsafe files (from an intranet file shared by using Windows Explorer, for example). If you enable this policy setting and set the drop-down box to "Enable", these files open without a security warning. If you set the drop-down box to "Prompt", a security warning appears before the files open. If you disable this policy these files do not open. If you do not configure this policy setting, the user can configure how the computer handles these files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Show security warning for potentially unsafe files' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1806" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-223140`

### Rule: ActiveX controls without prompt property must be used in approved domains only (Restricted Sites zone).

**Rule ID:** `SV-223140r879630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting controls whether or not the user is prompted to allow ActiveX controls to run on websites other than the website that installed the ActiveX control. If the user were to disable the setting for the zone, malicious ActiveX controls could be executed without the user's knowledge. Disabling this setting would allow the possibility for malicious ActiveX controls to be executed from non-approved domains within this zone without the user's knowledge. Enabling this setting enforces the default value and prohibits the user from changing the value. Websites should be moved into another zone if permissions need to be changed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Allow only approved domains to use ActiveX controls without prompt' must be 'Enabled', and 'Enable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "120b" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223141`

### Rule: Cross-Site Scripting Filter property must be enforced (Restricted Sites zone).

**Rule ID:** `SV-223141r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Cross-Site Scripting Filter is designed to prevent users from becoming victims of unintentional information disclosure. This setting controls if the Cross-Site Scripting (XSS) Filter detects and prevents cross-site script injection into websites in this zone. If you enable this policy setting, the XSS Filter will be enabled for sites in this zone, and the XSS Filter will attempt to block cross-site script injections. If you disable this policy setting, the XSS Filter will be disabled for sites in this zone, and Internet Explorer will permit cross-site script injections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone -> 'Turn on Cross-Site Scripting Filter' must be 'Enabled', and 'Enable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1409" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000112

**Group ID:** `V-223142`

### Rule: Internet Explorer Processes Restrict ActiveX Install must be enforced (Reserved).

**Rule ID:** `SV-223142r879573_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Users often choose to install software such as ActiveX controls that are not permitted by their organization's security policy. Such software can pose significant security and privacy risks to networks. This policy setting enables blocking of ActiveX control installation prompts for Internet Explorer processes. If you enable this policy setting, prompts for ActiveX control installations will be blocked for Internet Explorer processes. If you disable this policy setting, prompts for ActiveX control installations will not be blocked and these prompts will be displayed to users. If you do not configure this policy setting, the user's preference will be used to determine whether to block ActiveX control installations for Internet Explorer processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Security Features -> Restrict ActiveX Install -> 'Internet Explorer Processes' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_RESTRICT_ACTIVEXINSTALL Criteria: If the value "(Reserved)" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223143`

### Rule: Status bar updates via script must be disallowed (Internet zone).

**Rule ID:** `SV-223143r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to manage whether script is allowed to update the status bar within the zone. A script running in the zone could cause false information to be displayed on the status bar, which could confuse the user and cause them to perform an undesirable action. If you enable this policy setting, script is allowed to update the status bar. If you disable this policy setting, script is not allowed to update the status bar. If you do not configure this policy setting, status bar updates via scripts will be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone 'Allow updates to status bar via script' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "2103" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000516

**Group ID:** `V-223144`

### Rule: .NET Framework-reliant components not signed with Authenticode must be disallowed to run (Internet zone).

**Rule ID:** `SV-223144r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unsigned components are more likely to contain malicious code and it is more difficult to determine the author of the application - therefore they should be avoided if possible. This policy setting allows you to manage whether .NET Framework components that are not signed with Authenticode can be executed from Internet Explorer. These components include managed controls referenced from an object tag and managed executables referenced from a link. If you enable this policy setting, Internet Explorer will execute unsigned managed components. If you select "Prompt" in the drop-down box, Internet Explorer will prompt the user to determine whether to execute unsigned managed components. If you disable this policy setting, Internet Explorer will not execute unsigned managed components. If you do not configure this policy setting, Internet Explorer will not execute unsigned managed components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone 'Run .NET Framework-reliant components not signed with Authenticode' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "2004" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000516

**Group ID:** `V-223145`

### Rule: .NET Framework-reliant components signed with Authenticode must be disallowed to run (Internet zone).

**Rule ID:** `SV-223145r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It may be possible for someone to host malicious content on a website that takes advantage of these components. This policy setting allows you to manage whether .NET Framework components that are signed with Authenticode can be executed from Internet Explorer. These components include managed controls referenced from an object tag and managed executables referenced from a link. If you enable this policy setting, Internet Explorer will execute signed managed components. If you select "Prompt" in the drop-down box, Internet Explorer will prompt the user to determine whether to execute signed managed components. If you disable this policy setting, Internet Explorer will not execute signed managed components. If you do not configure this policy setting, Internet Explorer will not execute signed managed components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Internet Zone 'Run .NET Framework-reliant components signed with Authenticode' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "2001" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223146`

### Rule: Scriptlets must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223146r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to manage whether scriptlets can be allowed. Scriptlets hosted on sites located in this zone are more likely to contain malicious code. If you enable this policy setting, users will be able to run scriptlets. If you disable this policy setting, users will not be able to run scriptlets. If you do not configure this policy setting, a scriptlet can be enabled or disabled by the user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone 'Allow Scriptlets' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "1209" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-223147`

### Rule: Status bar updates via script must be disallowed (Restricted Sites zone).

**Rule ID:** `SV-223147r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A script running in the zone could cause false information to be displayed on the status bar, which could confuse the user and cause an undesirable action. This policy setting allows you to manage whether script is allowed to update the status bar within the zone. If you enable this policy setting, script is allowed to update the status bar. If you disable this policy setting, script is not allowed to update the status bar. If you do not configure this policy setting, status bar updates via scripts will be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer -> Internet Control Panel -> Security Page -> Restricted Sites Zone 'Allow updates to status bar via script' must be 'Enabled', and 'Disable' selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\4 Criteria: If the value "2103" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000516

**Group ID:** `V-223148`

### Rule: When Enhanced Protected Mode is enabled, ActiveX controls must be disallowed to run in Protected Mode.

**Rule ID:** `SV-223148r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting prevents ActiveX controls from running in Protected Mode when Enhanced Protected Mode is enabled. When a user has an ActiveX control installed that is not compatible with Enhanced Protected Mode and a website attempts to load the control, Internet Explorer notifies the user and gives the option to run the website in regular Protected Mode. This policy setting disables this notification and forces all websites to run in Enhanced Protected Mode. Enhanced Protected Mode provides additional protection against malicious websites by using 64-bit processes on 64-bit versions of Windows. For computers running at least Windows 8, Enhanced Protected Mode also limits the locations Internet Explorer can read from in the registry and the file system. If you enable this policy setting, Internet Explorer will not give the user the option to disable Enhanced Protected Mode. All Protected Mode websites will run in Enhanced Protected Mode. If you disable or do not configure this policy setting, Internet Explorer notifies users and provides an option to run websites with incompatible ActiveX controls in regular Protected Mode.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If McAfee ENS Web Control is being used, this is Not Applicable. The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer-> Internet Control Panel-> Advanced Page 'Do not allow ActiveX controls to run in Protected Mode when Enhanced Protected Mode is enabled' must be 'Enabled'. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Internet Explorer\Main Criteria: If the value "DisableEPMCompat" is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000039

**Group ID:** `V-223149`

### Rule: Dragging of content from different domains across windows must be disallowed (Internet zone).

**Rule ID:** `SV-223149r879534_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows you to set options for dragging content from one domain to a different domain when the source and destination are in different windows. If you enable this policy setting, users can drag content from one domain to a different domain when the source and destination are in different windows. Users cannot change this setting. If you disable this policy setting, users cannot drag content from one domain to a different domain when both the source and destination are in different windows. Users cannot change this setting. If you do not configure this policy setting, users cannot drag content from one domain to a different domain when the source and destination are in different windows. Users can change this setting in the Internet Options dialog box.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration -> Administrative Templates -> Windows Components -> Internet Explorer-> Internet Control Panel-> Security Page-> Internet Zone 'Enable dragging of content from different domains across windows' must be 'Enabled', and 'Disabled' selected from the drop-down box. Procedure: Use the windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3 Criteria: If the value "2709" is REG_DWORD = 3, this is not a finding.

## Group: SRG-APP-000416

**Group ID:** `V-250540`

### Rule: Turn off Encryption Support must be enabled.

**Rule ID:** `SV-250540r942484_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This parameter ensures only DoD-approved ciphers and algorithms are enabled for use by the web browser by allowing you to turn on/off support for TLS and SSL. TLS is a protocol for protecting communications between the browser and the target server. When the browser attempts to set up a protected communication with the target server, the browser and server negotiate which protocol and version to use. The browser and server attempt to match each other's list of supported protocols and versions and pick the most preferred match. Satisfies: SRG-APP-000514, SRG-APP-000555, SRG-APP-000625, SRG-APP-000630, SRG-APP-000635</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Internet Explorer >> Internet Control Panel >> Advanced Page >> "Turn off Encryption Support" must be "Enabled". Verify the only option selected is "Only use TLS 1.2" from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings!SecureProtocols. Criteria: If the value for "SecureProtocols" is not REG_DWORD = "2048", this is a finding.

## Group: SRG-APP-000416

**Group ID:** `V-250541`

### Rule: Allow Fallback to SSL 3.0 (Internet Explorer) must be disabled.

**Rule ID:** `SV-250541r942485_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This parameter ensures only DoD-approved ciphers and algorithms are enabled for use by the web browser by blocking an insecure fallback to SSL when TLS 1.0 or greater fails. Satisfies: SRG-APP-000514, SRG-APP-000555, SRG-APP-000625, SRG-APP-000630, SRG-APP-000635</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Internet Explorer >> Security Features >> "Allow fallback to SSL 3.0 (Internet Explorer)" must be "Enabled", and "No Sites" selected from the drop-down box. If "Allow fallback to SSL 3.0 (Internet Explorer)" is not "Enabled" or any other drop-down option is selected, this is a finding. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings. Criteria: If the value "EnableSSL3Fallback" is REG_DWORD=0, this is not a finding.

## Group: SRG-APP-000456

**Group ID:** `V-252910`

### Rule: The version of Internet Explorer running on the system must be a supported version.

**Rule ID:** `SV-252910r942486_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may depend on the Information Assurance Vulnerability Management (IAVM) process.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Internet Explorer 11 is no longer supported on Windows 10 General Availability Channel. If Internet Explorer 11 is installed and enabled on Windows 10 General Availability Channel, this is a finding. If Internet Explorer 11 is installed and enabled on an unsupported OS, this is a finding.

