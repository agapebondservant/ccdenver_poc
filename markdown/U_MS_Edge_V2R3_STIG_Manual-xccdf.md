# STIG Benchmark: Microsoft Edge Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000039

**Group ID:** `V-235719`

### Rule: User control of proxy settings must be disabled.

**Rule ID:** `SV-235719r1007484_rule`
**Severity:** low

**Description:**
<VulnDiscussion>This action configures the proxy settings for Microsoft Edge. If this policy is enabled, Microsoft Edge ignores all proxy-related options specified from the command line. If this policy is not configured, users can choose their own proxy settings. This policy overrides the following individual policies: - ProxyMode - ProxyPacUrl - ProxyServer - ProxyBypassList Setting the ProxySettings policy accepts the following fields: - ProxyMode, which allows for the proxy server used by Microsoft Edge to be specified and prevents users from changing proxy settings. - ProxyPacUrl, a URL to a proxy .pac file. - ProxyServer, a URL for the proxy server. - ProxyBypassList, a list of proxy hosts that Microsoft Edge bypasses. For ProxyMode, the following values have the noted impact: - direct, a proxy is never used and all other fields are ignored. - system, the system's proxy is used and all other fields are ignored. - auto_detect, all other fields are ignored. - fixed_servers, the ProxyServer and ProxyBypassList fields are used. - pac_script, the ProxyPacUrl and ProxyBypassList fields are used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Proxy server/Proxy Settings" must be “Enabled”, and have a “Proxy Settings” value defined for "ProxyMode". "ProxyMode" must be defined and set to one of the following: "direct", "system", "auto_detect", "fixed_servers", or "pac_script". Consult Microsoft documentaion for proper configuration of the text string required to define the "Proxy Settings" value. Example: {"ProxyMode": "fixed_servers", "ProxyServer": "123.123.123.123:8080"} Values for "ProxyPacUrl", "ProxyServer", or "ProxyBypassList" are optional. Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the REG_SZ value for "ProxySettings" does not have "ProxyMode" configured, this is a finding.

## Group: SRG-APP-000073

**Group ID:** `V-235720`

### Rule: Bypassing Microsoft Defender SmartScreen prompts for sites must be disabled.

**Rule ID:** `SV-235720r960852_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows a decision to be made on whether users can override the Microsoft Defender SmartScreen warnings about potentially malicious websites. If this setting is enabled, users cannot ignore Microsoft Defender SmartScreen warnings, and are blocked from continuing to the site. If this setting is disabled or not configured, users can ignore Microsoft Defender SmartScreen warnings and continue to the site.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/SmartScreen settings/Prevent bypassing Microsoft Defender SmartScreen prompts for sites" must be set to "Enabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "PreventSmartScreenPromptOverride" is not set to "REG_DWORD = 1", this is a finding. If this machine is on SIPRNet, this is Not Applicable.

## Group: SRG-APP-000073

**Group ID:** `V-235721`

### Rule: Bypassing of Microsoft Defender SmartScreen warnings about downloads must be disabled.

**Rule ID:** `SV-235721r960852_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows a decision to be made on whether users can override Microsoft Defender SmartScreen warnings about unverified downloads. If this setting is enabled, users cannot ignore Microsoft Defender SmartScreen warnings, and are prevented from completing the unverified downloads. If this policy is disabled or not configured, users can ignore Microsoft Defender SmartScreen warnings and complete unverified downloads.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/SmartScreen settings/Prevent bypassing of Microsoft Defender SmartScreen warnings about downloads" must be set to "Enabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "PreventSmartScreenPromptOverrideForFiles" is not set to "REG_DWORD = 1", this is a finding. If this machine is on SIPRNet, this is Not Applicable.

## Group: SRG-APP-000073

**Group ID:** `V-235722`

### Rule: The list of domains for which Microsoft Defender SmartScreen will not trigger warnings must be allowlisted if used.

**Rule ID:** `SV-235722r960852_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Configure the list of Microsoft Defender SmartScreen trusted domains. This means Microsoft Defender SmartScreen will not check for potentially malicious resources, such as phishing software and other malware, if the source URLs match these domains. The Microsoft Defender SmartScreen download protection service will not check downloads hosted on these domains. If this policy is enabled, Microsoft Defender SmartScreen trusts these domains. If the policy is disabled or not set, default Microsoft Defender SmartScreen protection is applied to all resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this machine is on SIPRNet, this is Not Applicable. This requirement for "SmartScreenAllowListDomains" is not required; this is optional. The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/SmartScreen settings/Configure the list of domains for which Microsoft Defender SmartScreen won't trigger warnings" may be set to "allow" for allowlisted domains. Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge SmartScreenAllowListDomains may be set as follows: HKLM\SOFTWARE\Policies\Microsoft\Edge\SmartScreenAllowListDomains\1 = mydomain.com HKLM\SOFTWARE\Policies\Microsoft\Edge\SmartScreenAllowListDomains\2 = myagency.mil If configured, the list of domains for which Microsoft Defender SmartScreen will not trigger warnings may be allowlisted.

## Group: SRG-APP-000080

**Group ID:** `V-235723`

### Rule: InPrivate mode must be disabled.

**Rule ID:** `SV-235723r960864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting specifies whether the user can open pages in InPrivate mode in Microsoft Edge. If this policy is not configured or set it to "Enabled", users can open pages in InPrivate mode. Set this policy to "Disabled" to stop users from using InPrivate mode. Set this policy to "Forced" to always use InPrivate mode. Policy options mapping: - Enabled (0) = InPrivate mode available - Disabled (1) = InPrivate mode disabled - Forced (2) = InPrivate mode forced</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Configure InPrivate mode availability" must be set to "enabled" with the option value set to "InPrivate mode disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "InPrivateModeAvailability" is not set to "REG_DWORD = 1", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235724`

### Rule: Background processing must be disabled.

**Rule ID:** `SV-235724r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Background processing allows Microsoft Edge processes to start at OS sign-in and keep running after the last browser window is closed. In this scenario, background apps and the current browsing session remain active, including any session cookies. An open background process displays an icon in the system tray, and can be closed from there. If this policy is enabled, background mode is turned on. If this policy is disabled, background mode is turned off. If this policy is not configured, background mode is initially turned off, and the user can configure its behavior in edge://settings/system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Continue running background apps after Microsoft Edge closes" must be set to "Disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "BackgroundModeEnabled" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235725`

### Rule: The ability of sites to show pop-ups must be disabled.

**Rule ID:** `SV-235725r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Set whether websites can show pop-up windows. Pop-ups can be allowed on all websites ("AllowPopups") or blocked on all sites ("BlockPopups"). If this policy is configured, pop-up windows are blocked by default, and users can change this setting. Policy options mapping: - AllowPopups (1) = Allow all sites to show pop-ups. - BlockPopups (2) = Do not allow any site to show pop-ups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Content settings/Default pop-up window setting" must be set to "Enabled" with the option value set to "Do not allow any site to show pop-ups". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for DefaultPopupsSetting is not set to "REG_DWORD = 2", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235726`

### Rule: The default search provider must be set to use an encrypted connection.

**Rule ID:** `SV-235726r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allows a list of list of up to 10 search engines to be configured, one of which must be marked as the default search engine. The encoding does not need to be specified. Starting in Microsoft Edge 80, the suggest_url and image_search_url parameters are optional. The optional parameter, image_search_post_params (consists of comma-separated name/value pairs), is available starting in Microsoft Edge 80. Starting in Microsoft Edge 83, search engine discovery can be enabled with the allow_search_engine_discovery optional parameter. This parameter must be the first item in the list. If allow_search_engine_discovery is not specified, search engine discovery will be disabled by default. Starting in Microsoft Edge 84, this policy can be set as a recommended policy to allow search provider discovery. The allow_search_engine_discovery optional parameter does not need to be added. If this policy is enabled, users cannot add, remove, or change any search engine in the list. Users can set their default search engine to any search engine in the list. If this policy is disabled or not configured, users can modify the search engines list as desired.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Manage Search Engines" must be configured. Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge Example REG_SZ value text for "ManagedSearchEngines": [{"allow_search_engine_discovery": false},{"is_default": true,"name": "Microsoft Bing","keyword": "bing","search_url": "https://www.bing.com/search?q={searchTerms}"},{"name": "Google","keyword": "google","search_url": "https://www.google.com/search?q={searchTerms}"}] If any of the search URLs in the list do not begin with "https", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235727`

### Rule: Data Synchronization must be disabled.

**Rule ID:** `SV-235727r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Disables data synchronization in Microsoft Edge. This policy also prevents the sync consent prompt from appearing. If this policy is not set or applied as recommended, users will be able to turn sync on or off. If this policy is applied as mandatory, users will not be able to turn on sync.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Disable synchronization of data using Microsoft sync services" must be set to "Enabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "SyncDisabled" is not set to "REG_DWORD = 1", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235728`

### Rule: Network prediction must be disabled.

**Rule ID:** `SV-235728r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enables network prediction and prevents users from changing this setting. This controls DNS prefetching, TCP and SSL pre-connection, and pre-rendering of web pages. If this policy is not configured, network prediction is enabled but the user can change it. Policy options mapping: - NetworkPredictionAlways (0) = Predict network actions on any network connection. - NetworkPredictionWifiOnly (1) = Not supported; if this value is used it will be treated as if "Predict network actions on any network connection" (0) was set. - NetworkPredictionNever (2) = Do not predict network actions on any network connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Enable network prediction" must be set to "Enabled" with the option value set to "Don't predict network actions on any network connection". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for NetworkPredictionOptions is not set to "REG_DWORD = 2", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235729`

### Rule: Search suggestions must be disabled.

**Rule ID:** `SV-235729r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enables web search suggestions in the Microsoft Edge Address Bar and Auto-Suggest List, and prevents users from changing this policy. If this policy is enabled, web search suggestions are used. If this policy is disabled, web search suggestions are never used; however, local history and local favorites suggestions still appear. If this policy is disabled, neither the typed characters nor the URLs visited will be included in telemetry to Microsoft. If this policy is not set, search suggestions are enabled but the user can change that.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Enable search suggestions" must be set to "Disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "SearchSuggestEnabled" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235730`

### Rule: Importing of autofill form data must be disabled.

**Rule ID:** `SV-235730r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allows users to import autofill form data from another browser into Microsoft Edge. If this policy is enabled, the option to manually import autofill data is automatically selected. If this policy is disabled, autofill form data is not imported at first run, and users cannot import it manually. If this policy is not configured, autofill data is imported at first run, and users can choose whether to import this data manually during later browsing sessions. This policy cannot be set as a recommendation. This means that Microsoft Edge will import autofill data on first run, but users can select or clear autofill data option during manual import.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Allow importing of autofill form data" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "ImportAutofillFormData" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235731`

### Rule: Importing of browser settings must be disabled.

**Rule ID:** `SV-235731r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Allows users to import browser settings from another browser into Microsoft Edge. If this policy is enabled, the Browser settings check box is automatically selected in the Import browser data dialog box. If this policy is disabled, browser settings are not imported at first run, and users cannot import them manually. If this policy is not configured, browser settings are imported at first run, and users can choose whether to import them manually during later browsing sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Allow importing of browser settings" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "ImportBrowserSettings" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235732`

### Rule: Importing of cookies must be disabled.

**Rule ID:** `SV-235732r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allows users to import cookies from another browser into Microsoft Edge. If this policy is disabled, cookies are not imported on first run. If this policy is not configured, cookies are imported on first run.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Allow importing of cookies" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "ImportCookies" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235733`

### Rule: Importing of extensions must be disabled.

**Rule ID:** `SV-235733r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allows users to import extensions from another browser into Microsoft Edge. If this policy is enabled, the Extensions check box is automatically selected in the Import browser data dialog box. If this policy is disabled, extensions are not imported at first run, and users cannot import them manually.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Allow importing of extensions" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "ImportExtensions" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235734`

### Rule: Importing of browsing history must be disabled.

**Rule ID:** `SV-235734r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allows users to import their browsing history from another browser into Microsoft Edge. If this policy is enabled, the Browsing history check box is automatically selected in the Import browser data dialog box. If this policy is disabled, browsing history data is not imported at first run, and users cannot import this data manually.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Allow importing of browsing history" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "ImportHistory" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235735`

### Rule: Importing of home page settings must be disabled.

**Rule ID:** `SV-235735r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allows users to import their home page setting from another browser into Microsoft Edge. If this policy is enabled, the option to manually import the home page setting is automatically selected. If this policy is disabled, the home page setting is not imported at first run, and users cannot import it manually.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Allow importing of home page settings" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "ImportHomepage" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235736`

### Rule: Importing of open tabs must be disabled.

**Rule ID:** `SV-235736r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allows users to import open and pinned tabs from another browser into Microsoft Edge. If this policy is enabled, the Open tabs check box is automatically selected in the Import browser data dialog box. If this policy is disabled, open tabs are not imported at first run, and users cannot import them manually. If this policy is not configured, open tabs are imported at first run, and users can choose whether to import them manually during later browsing sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Allow importing of open tabs" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "ImportOpenTabs" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235737`

### Rule: Importing of payment info must be disabled.

**Rule ID:** `SV-235737r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allows users to import payment info from another browser into Microsoft Edge. If this policy is enabled, the payment info check box is automatically selected in the Import browser data dialog box. If this policy is disabled, payment info is not imported at first run, and users cannot import it manually.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Allow importing of payment info" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "ImportPaymentInfo" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235738`

### Rule: Importing of saved passwords must be disabled.

**Rule ID:** `SV-235738r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allows users to import saved passwords from another browser into Microsoft Edge. If this policy is enabled, the option to manually import saved passwords is automatically selected. If this policy is disabled, saved passwords are not imported on first run, and users cannot import them manually.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Allow importing of saved passwords" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "ImportSavedPasswords" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235739`

### Rule: Importing of search engine settings must be disabled.

**Rule ID:** `SV-235739r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allows users to import search engine settings from another browser into Microsoft Edge. If this policy is enabled, the option to import search engine settings is automatically selected. If this policy is disabled, search engine settings are not imported at first run, and users cannot import them manually.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Allow importing of search engine settings" must be set to "disabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "ImportSearchEngine" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235740`

### Rule: Importing of shortcuts must be disabled.

**Rule ID:** `SV-235740r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allows users to import Shortcuts from another browser into Microsoft Edge. If this policy is disabled, Shortcuts are not imported on first run. If this policy is not configured, Shortcuts are imported on first run.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Allow importing of shortcuts" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "ImportShortcuts" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235741`

### Rule: AutoplayAllowed must be set to disabled.

**Rule ID:** `SV-235741r1007485_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy sets the media autoplay policy for websites. The default setting "Not configured" respects the current media autoplay settings and lets users configure their autoplay settings. Setting to "Enabled" sets media autoplay to "Allow". All websites are allowed to autoplay media. Users cannot override this policy. Setting to "Disabled" sets media autoplay to "Limit". This limits websites that are allowed to autoplay media to webpages with high media engagement and active WebRTC streams. Prior to Microsoft Edge version 92, this would set media autoplay to "Block". Users cannot override this policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Allow media autoplay for websites" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "AutoplayAllowed" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235742`

### Rule: WebUSB must be disabled.

**Rule ID:** `SV-235742r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Set whether websites can access connected USB devices. Access can be blocked completely or the user asked each time a website wants to get access to connected USB devices. Override this policy for specific URL patterns by using the WebUsbAskForUrls and WebUsbBlockedForUrls policies. If this policy is not configured, sites can ask users whether they can access the connected USB devices ('AskWebUsb') by default, and users can change this setting.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Content settings/Control use of the WebUSB API" must be set to "enabled" with the option value set to "Do not allow any site to request access to USB devices via the WebUSB API". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "DefaultWebUsbGuardSetting" is not set to "REG_DWORD = 2", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235743`

### Rule: Google Cast must be disabled.

**Rule ID:** `SV-235743r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enable this policy to enable Google Cast. Users will be able to launch it from the app menu, page context menus, media controls on Cast-enabled websites, and (if shown) the Cast toolbar icon. Disable this policy to disable Google Cast. By default, Google Cast is enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Cast/Enable Google Cast" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "EnableMediaRouter" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235744`

### Rule: Web Bluetooth API must be disabled.

**Rule ID:** `SV-235744r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Control whether websites can access nearby Bluetooth devices. Access can be blocked completely or the site required to ask the user each time it wants to access a Bluetooth device. If this policy is not configured, the default value ('AskWebBluetooth', meaning users are asked each time) is used and users can change it. Policy options mapping: - BlockWebBluetooth (2) = Do not allow any site to request access to Bluetooth devices via the Web Bluetooth API. - AskWebBluetooth (3) = Allow sites to ask the user to grant access to a nearby Bluetooth device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Content settings/Control use of the Web Bluetooth API" must be set to "enabled" with the option value set to "Do not allow any site to request access to Bluetooth devices via the Web Bluetooth API". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "DefaultWebBluetoothGuardSetting" is not set to "REG_DWORD = 2", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235745`

### Rule: Autofill for Credit Cards must be disabled.

**Rule ID:** `SV-235745r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enables the Microsoft Edge AutoFill feature and lets users auto complete credit card information in web forms using previously stored information. If this policy is disabled, AutoFill never suggests or fills credit card information, nor will it save additional credit card information that users might submit while browsing the web. If this policy is enabled or not configured, users can control AutoFill for credit cards.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Enable AutoFill for credit cards" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "AutofillCreditCardEnabled" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235746`

### Rule: Autofill for addresses must be disabled.

**Rule ID:** `SV-235746r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enables the AutoFill feature and allows users to auto-complete address information in web forms using previously stored information. If this policy is disabled, AutoFill never suggests or fills credit card information, nor will it save additional credit card information that users might submit while browsing the web. If this policy is enabled or not configured, users can control AutoFill for addresses in the user interface.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Enable AutoFill for addresses" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "AutofillAddressEnabled" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000175

**Group ID:** `V-235747`

### Rule: Online revocation checks must be performed.

**Rule ID:** `SV-235747r961038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If you enable this policy, Microsoft Edge will perform soft-fail, online OCSP/CRL checks. "Soft fail" means that if the revocation server can't be reached, the certificate will be considered valid. If you disable the policy or don't configure it, Microsoft Edge won't perform online revocation checks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Enable online OCSP/CRL checks" must be set to "Enabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "EnableOnlineRevocationChecks" is not set to "REG_DWORD = 1", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235748`

### Rule: Personalization of ads, search, and news by sending browsing history to Microsoft must be disabled.

**Rule ID:** `SV-235748r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy prevents Microsoft from collecting a user's Microsoft Edge browsing history to be used for personalizing advertising, search, news and other Microsoft services. This setting is only available for users with a Microsoft account. This setting is not available for child accounts or enterprise accounts. If this policy is disabled, users cannot change or override the setting. If this policy is enabled or not configured, Microsoft Edge will default to the user's preference.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Allow personalization of ads, search and news by sending browsing history to Microsoft" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "PersonalizationReportingEnabled" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235749`

### Rule: Site tracking of a user’s location must be disabled.

**Rule ID:** `SV-235749r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Set whether websites can track users' physical locations. Tracking can be allowed by default ("AllowGeolocation") or denied by default ("BlockGeolocation"), or the user can be asked each time a website requests their location ("AskGeolocation"). If this policy is not configured, "AskGeolocation" is used and the user can change it. Policy options mapping: - AllowGeolocation (1) = Allow sites to track users' physical location. - BlockGeolocation (2) = Do not allow any site to track users' physical location. - AskGeolocation (3) = Ask whenever a site wants to track users' physical location.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Content settings/Default geolocation setting" must be set to "enabled" with the option value set to "Don't allow any site to track users' physical location". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "DefaultGeolocationSetting" is not set to "REG_DWORD = 2", this is a finding.

## Group: SRG-APP-000080

**Group ID:** `V-235750`

### Rule: Browser history must be saved.

**Rule ID:** `SV-235750r960864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting disables deleting browser history and download history and prevents users from changing this setting.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Enable deleting browser and download history" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "AllowDeletingBrowserHistory" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235751`

### Rule: Edge development tools must be disabled.

**Rule ID:** `SV-235751r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>While the risk associated with browser development tools is more related to the proper design of a web application, a risk vector remains within the browser. The developer tools allow end users and application developers to view and edit all types of web application-related data via the browser. Page elements, source code, javascript, API calls, application data, etc., may all be viewed and potentially manipulated. Manipulation could be useful for troubleshooting legitimate issues, and this may be performed in a development environment. Manipulation could also be malicious and must be addressed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Control where developer tools can be used" with the option value set to "Don't allow using the developer tools". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "DeveloperToolsAvailability" is not set to "REG_DWORD = 2", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235752`

### Rule: Download restrictions must be configured.

**Rule ID:** `SV-235752r1106675_rule`
**Severity:** low

**Description:**
<VulnDiscussion>This configures the type of downloads that Microsoft Edge completely blocks without allowing users to override the security decision. Set "BlockDangerousDownloads" to allow all downloads except those that carry Microsoft Defender SmartScreen warnings of known dangerous downloads or that have dangerous file type extensions. Set "BlockPotentiallyDangerousDownloads" to allow all downloads except those that carry Microsoft Defender SmartScreen warnings of potentially dangerous or unwanted downloads or that have dangerous file type extensions. Set "BlockAllDownloads" to block all downloads. Set "BlockMaliciousDownloads" to allow all downloads except those that carry Microsoft Defender SmartScreen warnings of known malicious downloads. If this policy is not configured or the "DefaultDownloadSecurity" option is not set, the downloads go through the usual security restrictions based on Microsoft Defender SmartScreen analysis results. Policy options mapping: DefaultDownloadSecurity (0) = No special restrictions BlockDangerousDownloads (1) = Block malicious downloads and dangerous file types BlockPotentiallyDangerousDownloads (2) = Block potentially dangerous or unwanted downloads and dangerous file types BlockAllDownloads (3) = Block all downloads BlockMaliciousDownloads (4) = Block malicious downloads</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this machine is on SIPRNet, this is Not Applicable. The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Allow download restrictions" must be set to "Enabled" with the option value set to "BlockDangerousDownloads" or "Block potentially dangerous or unwanted downloads". The more restrictive option, "Block all downloads", is also acceptable. Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "DownloadRestrictions" is set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000378

**Group ID:** `V-235753`

### Rule: URLs must be allowlisted for plugin use if used.

**Rule ID:** `SV-235753r1015297_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Define a list of sites, based on URL patterns that can open pop-up windows.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement for "Allow pop-up windows on specific sites" is not required; this is optional. The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Content settings/Allow pop-up windows on specific sites" must be set to "Enabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge "PopupsAllowedForUrls" must be set as follows: HKLM\SOFTWARE\Policies\Microsoft\Edge\PopupsAllowedForUrls\1 = mydomain.com HKLM\SOFTWARE\Policies\Microsoft\Edge\PopupsAllowedForUrls\2 = myagency.mil If configured, the list of domains for which Microsoft Edge allows pop-ups may be allowlisted.

## Group: SRG-APP-000141

**Group ID:** `V-235754`

### Rule: Extensions installation must be blocklisted by default.

**Rule ID:** `SV-235754r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>List specific extensions that users cannot install in Microsoft Edge. When this policy is deployed, any extensions on this list that were previously installed will be disabled, and the user will not be able to enable them. If an item is removed from the list of blocked extensions, the extension is automatically reenabled anywhere it was previously installed. Use "*" to block all extensions that are not explicitly listed in the allow list. If this policy is not configured, users can install any extension in Microsoft Edge.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Extensions/Control which extensions cannot be installed" must be set to "Enabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge\ExtensionInstallBlocklist\1 If the value for "1" is not set to "REG_SZ = *", this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-235755`

### Rule: Extensions that are approved for use must be allowlisted if used.

**Rule ID:** `SV-235755r961479_rule`
**Severity:** low

**Description:**
<VulnDiscussion>By default, all extensions are allowed. However, if all extensions are blocked by setting the "ExtensionInstallBlockList" policy to "*," users can only install extensions defined in this policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement for "Allow specific extensions to be installed" is not required; this is optional. The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Extensions/Allow specific extensions to be installed" must be set to "Enabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge "ExtensionInstallAllowlist" must be set as follows: HKLM\SOFTWARE\Policies\Microsoft\Edge\ExtensionInstallAllowlist\1 = "extension_id1" HKLM\SOFTWARE\Policies\Microsoft\Edge\ExtensionInstallAllowlist\2 = "extension_id2" If configured, the list of extensions for which Microsoft Edge allows to be installed may be allowlisted.

## Group: SRG-APP-000400

**Group ID:** `V-235756`

### Rule: The Password Manager must be disabled.

**Rule ID:** `SV-235756r961521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enable Microsoft Edge to save user passwords. If this policy is enabled, users can save their passwords in Microsoft Edge. The next time the user visits the site, Microsoft Edge will enter the password automatically.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Password manager and protection/Enable saving passwords to the password manager" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "PasswordManagerEnabled" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000456

**Group ID:** `V-235758`

### Rule: The version of Microsoft Edge running on the system must be a supported version.

**Rule ID:** `SV-235758r961683_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Cross-reference the build information displayed with the Microsoft Edge site to identify, at minimum, the oldest supported build available. If the installed version of Edge is not supported by Microsoft, this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235760`

### Rule: Site isolation for every site must be enabled.

**Rule ID:** `SV-235760r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "SitePerProcess" policy can be used to prevent users from opting out of the default behavior of isolating all sites. The "IsolateOrigins" policy can be used to isolate additional, finer-grained origins. Enabling this policy prevents users from opting out of the default behavior where each site runs in its own process. If this policy is not disabled or configured, a user can opt out of site isolation (e.g., by using "Disable site isolation" entry in edge://flags.) Disabling the policy or not configuring the policy does not turn off Site Isolation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Enable site isolation for every site" must be set to "enabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "SitePerProcess" is not set to "REG_DWORD = 1", this is a finding.

## Group: SRG-APP-000142

**Group ID:** `V-235761`

### Rule: Supported authentication schemes must be configured.

**Rule ID:** `SV-235761r1043177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting specifies which HTTP authentication schemes are supported. The policy can be configured by using these values: "basic", "digest", "ntlm", and "negotiate". Separate multiple values with commas. If this policy is not configured, all four schemes are used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/HTTP authentication/Supported authentication schemes" must be set to "ntlm,negotiate". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "AuthSchemes" is not set to "REG_SZ = ntlm,negotiate", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235763`

### Rule: Microsoft Defender SmartScreen must be enabled.

**Rule ID:** `SV-235763r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting configures Microsoft Defender SmartScreen, which provides warning messages to help protect users from potential phishing scams and malicious software. By default, Microsoft Defender SmartScreen is turned on. If this setting is enabled, Microsoft Defender SmartScreen is turned on. If this setting is disabled, Microsoft Defender SmartScreen is turned off. If this setting is not configured, users can choose whether to use Microsoft Defender SmartScreen. This policy is available only on Windows instances that are joined to a Microsoft Active Directory domain, Windows 10 Pro or Enterprise instances that enrolled for device management, or macOS instances that are that are managed via MDM or joined to a domain via MCX.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/SmartScreen settings/Configure Microsoft Defender SmartScreen" must be set to "Enabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "SmartScreenEnabled" is not set to "REG_DWORD = 1", this is a finding. If this machine is on SIPRNet, this is Not Applicable.

## Group: SRG-APP-000141

**Group ID:** `V-235764`

### Rule: Microsoft Defender SmartScreen must be configured to block potentially unwanted apps.

**Rule ID:** `SV-235764r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting configures blocking for potentially unwanted apps with Microsoft Defender SmartScreen. Potentially unwanted app blocking with Microsoft Defender SmartScreen provides warning messages to help protect users from adware, coin miners, bundleware, and other low-reputation apps that are hosted by websites. Potentially unwanted app blocking with Microsoft Defender SmartScreen is turned off by default. If this setting is enabled, potentially unwanted app blocking with Microsoft Defender SmartScreen is turned on. If this setting is disabled, potentially unwanted app blocking with Microsoft Defender SmartScreen is turned off. If this setting is not configured, users can choose whether to use potentially unwanted app blocking with Microsoft Defender SmartScreen. This policy is available only on Windows instances that are joined to a Microsoft Active Directory domain, Windows 10 Pro or Enterprise instances that enrolled for device management, or macOS instances that are managed via MDM or joined to a domain via MCX.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/SmartScreen settings/Configure Microsoft Defender SmartScreen to block potentially unwanted apps" must be set to "Enabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for SmartScreenPuaEnabled is not set to "REG_DWORD = 1", this is a finding. If this machine is on SIPRNet, this is Not Applicable.

## Group: SRG-APP-000141

**Group ID:** `V-235765`

### Rule: The download location prompt must be configured.

**Rule ID:** `SV-235765r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>This setting provides positive feedback before a download starts, limiting the possibility of inadvertent downloads without notifying the user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Ask where to save downloaded files" must be set to "enabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "PromptForDownloadLocation" is not set to "REG_DWORD = 1", this is a finding.

## Group: SRG-APP-000148

**Group ID:** `V-235766`

### Rule: Tracking of browsing activity must be disabled.

**Rule ID:** `SV-235766r1051115_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The setting allows websites to be blocked from tracking users' web-browsing activity. If this policy is disabled or is not configured, users can set their own level of tracking prevention. Policy options mapping: - TrackingPreventionOff (0) = Off (no tracking prevention) - TrackingPreventionBasic (1) = Basic (blocks harmful trackers; content and ads will be personalized) - TrackingPreventionBalanced (2) = Balanced (blocks harmful trackers and trackers from sites user has not visited; content and ads will be less personalized) - TrackingPreventionStrict (3) = Strict (blocks harmful trackers and majority of trackers from all sites; content and ads will have minimal personalization; some parts of sites might not work)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Block tracking of users' web-browsing activity" must be set to "Enabled" with the option value set to "Balanced" or "Strict". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "TrackingPrevention" is not set to "REG_DWORD = 2" or "REG_DWORD = 3", this is a finding.

## Group: SRG-APP-000149

**Group ID:** `V-235767`

### Rule: A website's ability to query for payment methods must be disabled.

**Rule ID:** `SV-235767r960972_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting determines whether websites can check if the user has payment methods saved. If this policy is disabled, websites that use "PaymentRequest.canMakePayment" or "PaymentRequest.hasEnrolledInstrument" API will be informed that no payment methods are available. If this policy is enabled or is not set, websites can check to determine if the user has payment methods saved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Allow websites to query for available payment methods" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for PaymentMethodQueryEnabled is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000151

**Group ID:** `V-235768`

### Rule: Suggestions of similar web pages in the event of a navigation error must be disabled.

**Rule ID:** `SV-235768r1015298_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting allows Microsoft Edge to issue a connection to a web service to generate URL and search suggestions for connectivity issues such as DNS errors. If this policy is enabled, a web service is used to generate URL and search suggestions for network errors. If this policy is disabled, no calls to the web service are made and a standard error page is shown. If this policy is not configured, Microsoft Edge respects the user preference that is set under Services at edge://settings/privacy. Specifically, there is a "Suggest similar pages when a webpage can't be found" toggle, which the user can switch on or off. Note that if this policy has been enabled (AlternateErrorPagesEnabled), the "Suggest similar pages when a webpage can't be found setting" is turned on, but the user cannot change the setting by using the toggle. If this policy is disabled, the "Suggest similar pages when a webpage can't be found" setting is turned off, and the user cannot change the setting by using the toggle.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Suggest similar pages when a webpage can't be found" must be set to "Disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for AlternateErrorPagesEnabled is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000152

**Group ID:** `V-235769`

### Rule: User feedback must be disabled.

**Rule ID:** `SV-235769r960981_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Microsoft Edge uses the Edge Feedback feature (enabled by default) to allow users to send feedback, suggestions, or customer surveys and to report any issues with the browser. By default, users cannot disable (turn off) the Edge Feedback feature. If this policy is enabled or not configured, users can invoke Edge Feedback. If this policy is disabled, users cannot invoke Edge Feedback.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Allow user feedback" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for UserFeedbackAllowed is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000153

**Group ID:** `V-235770`

### Rule: The collections feature must be disabled.

**Rule ID:** `SV-235770r960984_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting allows users to access the Collections feature, where they can collect, organize, share, and export content more efficiently and with Office integration. If this policy is enabled or not configured, users can access and use the Collections feature in Microsoft Edge. If this policy is disabled, users cannot access and use Collections in Microsoft Edge.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Enable the Collections feature" must be set to "Disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "EdgeCollectionsEnabled" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235771`

### Rule: The Share Experience feature must be disabled.

**Rule ID:** `SV-235771r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If this policy is set to "ShareAllowed" (the default), users will be able to access the Windows 10 Share experience from the Settings and More menu in Microsoft Edge to share with other apps on the system. If this policy is set to "ShareDisallowed", users will not be able to access the Windows 10 Share experience. If the Share button is on the toolbar, it will also be hidden. Policy options mapping: - ShareAllowed (0) = Allow using the Share experience. - ShareDisallowed (1) = Do not allow using the Share experience.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Configure the Share experience" must be set to "enabled" with the option value set to "Don't allow using the Share experience". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "ConfigureShare" is not set to "REG_DWORD = 1", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-235772`

### Rule: Guest mode must be disabled.

**Rule ID:** `SV-235772r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling Guest mode allows the use of guest profiles in Microsoft Edge. In a guest profile, the browser does not import browsing data from existing profiles, and it deletes browsing data when all guest profiles are closed. If this policy is enabled or not configured, Microsoft Edge lets users browse in guest profiles. If this policy is disabled, Microsoft Edge does not let users browse in guest profiles.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Enable guest mode" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "BrowserGuestModeEnabled" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000156

**Group ID:** `V-235773`

### Rule: Relaunch notification must be required.

**Rule ID:** `SV-235773r960993_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Users must be required to restart the browser to finish installation of pending updates and prevent users from continually using an old/vulnerable browser version.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Notify a user that a browser restart is recommended or required for pending updates" must be set to "Enabled" with the option value set to "Required". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "RelaunchNotification" is not set to "REG_DWORD = 2", this is a finding.

## Group: SRG-APP-000157

**Group ID:** `V-235774`

### Rule: The built-in DNS client must be disabled.

**Rule ID:** `SV-235774r1015299_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting controls whether to use the built-in DNS client. This does not affect which DNS servers are used; it only controls the software stack that is used to communicate with them. For example, if the operating system is configured to use an enterprise DNS server, that same server would be used by the built-in DNS client. However, it is however possible that the built-in DNS client will address servers in different ways by using more modern DNS-related protocols such as DNS-over-TLS. If this policy is enabled, the built-in DNS client is used if it is available. If this policy is disabled, the client is never used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Use built-in DNS client" must be set to "disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "BuiltInDnsClientEnabled" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-246736`

### Rule: Use of the QUIC protocol must be disabled.

**Rule ID:** `SV-246736r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>QUIC is used by more than half of all connections from the Edge web browser to Google's servers, and this activity is undesirable in the DoD. If you enable this policy or don't configure it, the QUIC protocol is allowed. If you disable this policy, the QUIC protocol is blocked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Allow QUIC protocol" must be set to "Disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "QuicAllowed" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-251694`

### Rule: The list of domains media autoplay allows must be allowlisted if used.

**Rule ID:** `SV-251694r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Define a list of sites, based on URL patterns, that are allowed to autoplay media. If this policy is not configured, the global default value from the AutoplayAllowed policy (if set) or the user's personal configuration is used for all sites. EDGE-00-000024 disables the AutoplayAllowed policy. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this machine is on SIPRNet, this is Not Applicable. This requirement for "AutoplayAllowlist" is not required; this is optional. The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Allow media autoplay on specific sites" may be set to "allow" for allowlisted domains. Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge AutoplayAllowlist may be set as follows: HKLM\SOFTWARE\Policies\Microsoft\Edge\AutoplayAllowlist\1 = mydomain.com HKLM\SOFTWARE\Policies\Microsoft\Edge\AutoplayAllowlist\2 = myagency.mil If configured, the list of domains for which autoplay is allowed may be allowlisted.

## Group: SRG-APP-000141

**Group ID:** `V-260465`

### Rule: Visual Search must be disabled.

**Rule ID:** `SV-260465r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Visual Search allows for quick exploration of more related content about entities in an image. If this policy is enabled or not configured, Visual Search will be enabled via image hover, context menu, and search in Sidebar. If this policy is disabled, Visual Search will be disabled and more information about images will not be available via hover, context menu, and search in Sidebar.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Visual search enabled" is set to "Disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "VisualSearchEnabled" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-260466`

### Rule: Copilot must be disabled.

**Rule ID:** `SV-260466r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Sidebar is a launcher bar on the right side of Microsoft Edge's screen. If this policy is enabled or not configured, the Sidebar will be shown. If this policy is disabled, the Sidebar will never be shown. Disabling Sidebar will disable Copilot.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Show Hubs Sidebar" is set to "Disabled". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "HubsSidebarEnabled" is not set to "REG_DWORD = 0", this is a finding.

## Group: SRG-APP-000080

**Group ID:** `V-260467`

### Rule: Session only-based cookies must be enabled.

**Rule ID:** `SV-260467r960864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cookies must only be allowed per session and only for approved URLs as permanently stored cookies can be used for malicious intent. Approved URLs may be allowlisted via the "CookiesAllowedForUrls" or "SaveCookiesOnExit" policy settings, but these are not requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Content settings/Configure cookies" is set to "Enabled" with the option value set to "Keep cookies for the duration of the session, except ones listed in 'SaveCookiesOnExit'". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for “DefaultCookiesSetting” is not set to "REG_DWORD = 4", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-266981`

### Rule: FriendlyURLs must be disabled.

**Rule ID:** `SV-266981r1007489_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If FriendlyURLs are enabled, Microsoft Edge will compute additional representations of the URL and place them on the clipboard. This policy configures what format will be pasted when the user pastes in external applications, or inside Microsoft Edge without the "Paste As" context menu item. If configured, this policy makes a choice on behalf of the user. The options in edge://settings/shareCopyPaste will be grayed out, and the options in the "Paste As" context menu will not be available. Not configured = The user will be able to choose their preferred paste format. By default, this is set to the friendly URL format. The "Paste As" menu will be available in Microsoft Edge. 1 = No additional formats will be stored on the clipboard. There will be no "Paste as" context menu item in Microsoft Edge and the only format available to paste will be the plain text URL format. Effectively, the friendly URL feature will be disabled. 3 = The user will get a friendly URL whenever they paste into surfaces that accept rich text. The plain URL will still be available for non-rich surfaces. There will be no "Paste As" menu in Microsoft Edge. 4 = (Not currently used) The richer formats may not be well-supported in some paste destinations and/or websites. In these scenarios, the plain URL option is recommended when configuring this policy. The recommended policy is available in Microsoft Edge 105 or later. Policy options mapping: PlainText (1) = The plain URL without any extra information, such as the page's title. This is the recommended option when this policy is configured. For more information, see the description. TitledHyperlink (3) = Titled Hyperlink: A hyperlink that points to the copied URL, but whose visible text is the title of the destination page. This is the Friendly URL format.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The policy value for "Computer Configuration/Administrative Templates/Microsoft Edge/Configure the default paste format of URLs copied from Microsoft Edge and determine if additional formats will be available to users" must be set to "enabled" with the option value set to "0". Use the Windows Registry Editor to navigate to the following key: HKLM\SOFTWARE\Policies\Microsoft\Edge If the value for "ConfigureFriendlyURLFormat" is not set to "REG_DWORD = 1", this is a finding.

