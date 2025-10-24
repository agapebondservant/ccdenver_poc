# STIG Benchmark: Google Chrome Current Windows Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000039

**Group ID:** `V-221558`

### Rule: Firewall traversal from remote host must be disabled.

**Rule ID:** `SV-221558r960804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote connections should never be allowed that bypass the firewall, as there is no way to verify if they can be trusted. Enables usage of STUN and relay servers when remote clients are trying to establish a connection to this machine. If this setting is enabled, then remote clients can discover and connect to this machine even if they are separated by a firewall. If this setting is disabled and outgoing UDP connections are filtered by the firewall, then this machine will only allow connections from client machines within the local network. If this policy is left not set the setting will be enabled. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If RemoteAccessHostFirewallTraversal is not displayed under the Policy Name column or it is not set to false under the Policy Value column, then this is a finding. Windows registry: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the RemoteAccessHostFirewallTraversal value name does not exist or its value data is not set to 0, then this is a finding.

## Group: SRG-APP-000206

**Group ID:** `V-221559`

### Rule: Site tracking users location must be disabled.

**Rule ID:** `SV-221559r961083_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Website tracking is the practice of gathering information as to which websites were accesses by a browser. The common method of doing this is to have a website create a tracking cookie on the browser. If the information of what sites are being accessed is made available to unauthorized persons, this violates confidentiality requirements, and over time poses a significant OPSEC issue. This policy setting allows you to set whether websites are allowed to track the user’s physical location. Tracking the user’s physical location can be allowed by default, denied by default or the user can be asked every time a website requests the physical location. 1 = Allow sites to track the user’s physical location 2 = Do not allow any site to track the user’s physical location 3 = Ask whenever a site wants to track the user’s physical location</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If DefaultGeolocationSetting is not displayed under the Policy Name column or it is not set to 2, then this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the DefaultGeolocationSetting value name does not exist or its value data is not set to 2, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-221561`

### Rule: Sites ability to show pop-ups must be disabled.

**Rule ID:** `SV-221561r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Chrome allows you to manage whether unwanted pop-up windows appear. Pop-up windows that are opened when the end user clicks a link are not blocked. If you enable this policy setting, most unwanted pop-up windows are prevented from appearing. If you disable this policy setting, pop-up windows are not prevented from appearing. If you disable this policy setting, scripts can continue to create pop-up windows, and pop-ups that hide other windows. Recommend configuring this setting to ‘2’ to help prevent malicious websites from controlling the pop-up windows or fooling users into clicking on the wrong window. If you do not configure this policy setting, most unwanted pop-up windows are prevented from appearing. If this policy is left not set, 'BlockPopups' will be used and the user will be able to change it. 1 = Allow all sites to show pop-ups 2 = Do not allow any site to show pop-ups</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If DefaultPopupsSetting is not displayed under the Policy Name column or it is not set to 2, then this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the value name DefaultPopupsSetting does not exist or its value data is not set to 2, then this is a finding. Note: If AO Approved exceptions to this rule have been enabled, this is not a finding.

## Group: SRG-APP-000089

**Group ID:** `V-221562`

### Rule: Extensions installation must be blocklisted by default.

**Rule ID:** `SV-221562r960879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Extensions are developed by third party sources and are designed to extend Google Chrome's functionality. An extension can be made by anyone, to do and access almost anything on a system; this means they pose a high risk to any system that would allow all extensions to be installed by default. Allows you to specify which extensions the users can NOT install. Extensions already installed will be removed if blocklisted. A blocklist value of '*' means all extensions are blocklisted unless they are explicitly listed in the allowlist. If this policy is left not set the user can install any extension in Google Chrome.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If ExtensionInstallBlocklist is not displayed under the Policy Name column or it is not set to * under the Policy Value column, then this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ExtensionInstallBlocklist 3. If the a registry value name of 1 does not exist under that key or its value is not set to *, then this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-221563`

### Rule: Extensions that are approved for use must be allowlisted.

**Rule ID:** `SV-221563r1015468_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The allowlist should only contain organizationally approved extensions. This is to prevent a user from accidently allowlisitng a malicious extension. This policy allows you to specify which extensions are not subject to the blacklist. A blacklist value of ‘*’ means all extensions are blacklisted and users can only install extensions listed in the allowlist. By default, no extensions are allowlisted. If all extensions have been blacklisted by policy, then the allowlist policy can be used to allow specific extensions to be installed. Administrators should determine which extensions should be allowed to be installed by their users. If no extensions are allowlisted, then no extensions can be installed when combined with blacklisting all extensions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If ExtensionInstallAllowlist is not displayed under the Policy Name column or it is not set to oiigbmnaadbkfbmpbfijlflahbdbdgdf or a list of administrator approved extension IDs, then this is a finding. Windows method: 1. Start regedit 2. Navigate to the key HKLM\Software\Policies\Google\Chrome\ExtensionInstallAllowlist 3. If the ExtensionInstallAllowlist key is not set to 1 and oiigbmnaadbkfbmpbfijlflahbdbdgdf or a list of administrator-approved extension IDs, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-221564`

### Rule: The default search providers name must be set.

**Rule ID:** `SV-221564r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Specifies the name of the default search provider that is to be used, if left empty or not set, the host name specified by the search URL will be used. This policy is only considered if the 'DefaultSearchProviderEnabled' policy is enabled. When doing internet searches it is important to use an encrypted connection via https.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If DefaultSearchProviderName is displayed under the Policy Name column or it is not set to an organization approved encrypted search provider that corresponds to the encrypted search provider set in DTBC-0008(ex. Google Encrypted, Bing Encrypted) under the Policy Value column, then this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the DefaultSearchProviderName value name does not exist or it is not set to an organization approved encrypted search provider that corresponds to the encrypted search provider set in DTBC-0008(ex. Google Encrypted, Bing Encrypted), then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-221565`

### Rule: The default search provider URL must be set to perform encrypted searches.

**Rule ID:** `SV-221565r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Specifies the URL of the search engine used when doing a default search. The URL should contain the string '{searchTerms}', which will be replaced at query time by the terms the user is searching for. This option must be set when the 'DefaultSearchProviderEnabled' policy is enabled and will only be respected if this is the case. When doing internet searches it is important to use an encrypted connection via https.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is on the SIPRNet, this requirement is NA. Universal method: 1. In the omnibox (address bar) type chrome://policy. 2. If DefaultSearchProviderSearchURL is not displayed under the Policy Name column or it is not set to an organization-approved encrypted search string (ex. https://www.google.com/search?q={searchTerms} or https://www.bing.com/search?q={searchTerms} ) under the Policy Value column, this is a finding. Windows method: 1. Start regedit. 2. Navigate to HKLM\Software\Policies\Google\Chrome\. 3. If the DefaultSearchProviderSearchURL value name does not exist or its value data is not set to an organization-approved encrypted search string (ex. https://www.google.com/search?q={searchTerms} or https://www.bing.com/search?q={searchTerms} ), this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-221566`

### Rule: Default search provider must be enabled.

**Rule ID:** `SV-221566r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Policy enables the use of a default search provider. If you enable this setting, a default search is performed when the user types text in the omnibox that is not a URL. You can specify the default search provider to be used by setting the rest of the default search policies. If these are left empty, the user can choose the default provider. If you disable this setting, no search is performed when the user enters non-URL text in the omnibox. If you enable or disable this setting, users cannot change or override this setting in Google Chrome. If this policy is left not set, the default search provider is enabled, and the user will be able to set the search provider list.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If DefaultSearchProviderEnabled is not displayed under the Policy Name column or it is not set to true under the Policy Value column, then this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the DefaultSearchProviderEnabled value name does not exist or its value data is not set to 1, then this is a finding. Note: This policy will only display in the chrome://policy tab on domain joined systems. On standalone systems, the policy will not display.

## Group: SRG-APP-000141

**Group ID:** `V-221567`

### Rule: The Password Manager must be disabled.

**Rule ID:** `SV-221567r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enables saving passwords and using saved passwords in Google Chrome. Malicious sites may take advantage of this feature by using hidden fields gain access to the stored information. If you enable this setting, users can have Google Chrome memorize passwords and provide them automatically the next time they log in to a site. If you disable this setting, users are not able to save passwords or use already saved passwords. If you enable or disable this setting, users cannot change or override this setting in Google Chrome. If this policy is left not set, this will be enabled but the user will be able to change it. ListPassword manager should not be used as it stores passwords locally.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If PasswordManagerEnabled is not displayed under the Policy Name column or it is not set to false under the Policy Value column, then this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the PasswordManagerEnabled value name does not exist or its value data is not set to 0, then this is a finding.

## Group: SRG-APP-000112

**Group ID:** `V-221570`

### Rule: Background processing must be disabled.

**Rule ID:** `SV-221570r960921_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Determines whether a Google Chrome process is started on OS login that keeps running when the last browser window is closed, allowing background apps to remain active. The background process displays an icon in the system tray and can always be closed from there. If this policy is set to True, background mode is enabled and cannot be controlled by the user in the browser settings. If this policy is set to False, background mode is disabled and cannot be controlled by the user in the browser settings. If this policy is left unset, background mode is initially disabled and can be controlled by the user in the browser settings.' - Google Chrome Administrators Policy ListThis setting, if enabled, allows Google Chrome to run at all times. There is two reasons that this is not wanted. First, it can tie up system resources that might otherwise be needed. Second, it does not make it obvious to the user that it is running and poorly written extensions could cause instability on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If BackgroundModeEnabled is not displayed under the Policy Name column and it is not set to false under the Policy Value column, then this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the BackgroundModeEnabled value name does not exist or its value data is not set to 0, then this is a finding.

## Group: SRG-APP-000047

**Group ID:** `V-221571`

### Rule: Google Data Synchronization must be disabled.

**Rule ID:** `SV-221571r987620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Disables data synchronization in Google Chrome using Google-hosted synchronization services and prevents users from changing this setting. If you enable this setting, users cannot change or override this setting in Google Chrome. If this policy is left not set the user will be able to enable Google Sync. Google Sync is used to sync information between different user devices, this data is then stored on Google owned servers. The synced data may consist of information such as email, calendars, viewing history, etc. This feature must be disabled because the organization does not have control over the servers the data is stored on.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If SyncDisabled is not displayed under the Policy Name column or it is not set to true under the Policy Value column, then this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the SyncDisabled value name does not exist or its value data is not set to 1, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-221572`

### Rule: The URL protocol schema javascript must be disabled.

**Rule ID:** `SV-221572r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Each access to a URL is handled by the browser according to the URL's "scheme". The "scheme" of a URL is the section before the ":". The term "protocol" is often mistakenly used for a "scheme". The difference is that the scheme is how the browser handles a URL and the protocol is how the browser communicates with a service. If a scheme or its associated protocol used by a browser is insecure or obsolete, vulnerabilities can be exploited resulting in exposed data or unrestricted access to the browser's system. The browser must be configured to disable the use of insecure and obsolete schemas (protocols). This policy disables the listed protocol schemes in Google Chrome, URLs using a scheme from this list will not load and cannot be navigated to. If this policy is left not set or the list is empty all schemes will be accessible in Google Chrome.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy. 2. If URLBlocklist is not displayed under the Policy Name column or it is not set to javascript://* under the Policy Value column, this is a finding. Windows method: 1. Start regedit. 2. Navigate to HKLM\Software\Policies\Google\Chrome\URLBlocklist. 3. If the URLBlocklist key does not exist, or the does not contain entries 1 set to javascript://*, this is a finding.

## Group: SRG-APP-000047

**Group ID:** `V-221573`

### Rule: Cloud print sharing must be disabled.

**Rule ID:** `SV-221573r987620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Policy enables Google Chrome to act as a proxy between Google Cloud Print and legacy printers connected to the machine. If this setting is enabled or not configured, users can enable the cloud print proxy by authentication with their Google account. If this setting is disabled, users cannot enable the proxy, and the machine will not be allowed to share it’s printers with Google Cloud Print. If this policy is not set, this will be enabled but the user will be able to change it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If CloudPrintProxyEnabled is not displayed under the Policy Name column or it is not set to false under the Policy Value column, then this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the CloudPrintProxyEnabled value name does not exist or its value data is not set to 0, then this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-221574`

### Rule: Network prediction must be disabled.

**Rule ID:** `SV-221574r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enables network prediction in Google Chrome and prevents users from changing this setting. If you enable or disable this setting, users cannot change or override this setting in Google Chrome. If this policy is left not set, this will be disabled but the user will be able to change it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If "NetworkPredictionOptions" is not displayed under the “Policy Name” column or it is not set to "2" under the “Policy Value” column, this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the "NetworkPredictionOptions" value name does not exist or its value data is not set to "2," this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-221575`

### Rule: Metrics reporting to Google must be disabled.

**Rule ID:** `SV-221575r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enables anonymous reporting of usage and crash-related data about Google Chrome to Google and prevents users from changing this setting. If you enable this setting, anonymous reporting of usage and crash-related data is sent to Google. A crash report could contain sensitive information from the computer's memory. If you disable this setting, anonymous reporting of usage and crash-related data is never sent to Google. If you enable or disable this setting, users cannot change or override this setting in Google Chrome. If this policy is left not set the setting will be what the user chose upon installation / first run.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If MetricsReportingEnabled is not displayed under the Policy Name column or it is not set to false under the Policy Value column, then this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the MetricsReportingEnabled value name does not exist or its value data is not set to 0, then this is a finding. Note: This policy will only display in the chrome://policy tab on domain joined systems. On standalone systems, the policy will not display.

## Group: SRG-APP-000141

**Group ID:** `V-221576`

### Rule: Search suggestions must be disabled.

**Rule ID:** `SV-221576r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Search suggestion should be disabled as it could lead to searches being conducted that were never intended to be made. Enables search suggestions in Google Chrome's omnibox and prevents users from changing this setting. If you enable this setting, search suggestions are used. If you disable this setting, search suggestions are never used. If you enable or disable this setting, users cannot change or override this setting in Google Chrome. If this policy is left not set, this will be enabled but the user will be able to change it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If SearchSuggestEnabled is not displayed under the Policy Name column or it is not set to false under the Policy Value column, then this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the SearchSuggestEnabled value name does not exist or its value data is not set to 0, then this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-221577`

### Rule: Importing of saved passwords must be disabled.

**Rule ID:** `SV-221577r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Importing of saved passwords should be disabled as it could lead to unencrypted account passwords stored on the system from another browser to be viewed. This policy forces the saved passwords to be imported from the previous default browser if enabled. If enabled, this policy also affects the import dialog. If disabled, the saved passwords are not imported. If it is not set, the user may be asked whether to import, or importing may happen automatically.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If ImportSavedPasswords is not displayed under the Policy Name column or it is not set to false under the Policy Value column, then this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the ImportSavedPasswords value name does not exist or its value data is not set to 0, then this is a finding.

## Group: SRG-APP-000080

**Group ID:** `V-221578`

### Rule: Incognito mode must be disabled.

**Rule ID:** `SV-221578r960864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Incognito mode allows the user to browse the Internet without recording their browsing history/activity. From a forensics perspective, this is unacceptable. Best practice requires that browser history is retained. The "IncognitoModeAvailability" setting controls whether the user may utilize Incognito mode in Google Chrome. If 'Enabled' is selected or the policy is left unset, pages may be opened in Incognito mode. If 'Disabled' is selected, pages may not be opened in Incognito mode. If 'Forced' is selected, pages may be opened ONLY in Incognito mode. 0 = Incognito mode available. 1 = Incognito mode disabled. 2 = Incognito mode forced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If IncognitoModeAvailability is not displayed under the Policy Name column or it is not set to 1 under the Policy Value column, then this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the IncognitoModeAvailability value name does not exist or its value data is not set to 1, then this is a finding.

## Group: SRG-APP-000605

**Group ID:** `V-221579`

### Rule: Online revocation checks must be performed.

**Rule ID:** `SV-221579r961893_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By setting this policy to true, the previous behavior is restored and online OCSP/CRL checks will be performed. If the policy is not set, or is set to false, then Chrome will not perform online revocation checks. Certificates are revoked when they have been compromised or are no longer valid, and this option protects users from submitting confidential data to a site that may be fraudulent or not secure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If EnableOnlineRevocationChecks is not displayed under the Policy Name column or it is not set to true under the Policy Value column, then this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the EnableOnlineRevocationChecks value name does not exist or its value data is not set to 1, then this is a finding.

## Group: SRG-APP-000206

**Group ID:** `V-221580`

### Rule: Safe Browsing must be enabled.

**Rule ID:** `SV-221580r961083_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allows you to control whether Google Chrome's Safe Browsing feature is enabled and the mode it operates in. If this policy is set to 'NoProtection' (value 0), Safe Browsing is never active. If this policy is set to 'StandardProtection' (value 1, which is the default), Safe Browsing is always active in the standard mode. If this policy is set to 'EnhancedProtection' (value 2), Safe Browsing is always active in the enhanced mode, which provides better security, but requires sharing more browsing information with Google.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If SafeBrowsingProtectionLevel is not displayed under the Policy Name column or it is not set to 1 or 2 under the Policy Value column, then this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the SafeBrowsingProtectionLevel value name does not exist or its value data is not set to 1 or 2, then this is a finding.

## Group: SRG-APP-000231

**Group ID:** `V-221581`

### Rule: Browser history must be saved.

**Rule ID:** `SV-221581r961128_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy disables saving browser history in Google Chrome and prevents users from changing this setting. If this setting is enabled, browsing history is not saved. If this setting is disabled or not set, browsing history is saved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If the policy 'SavingBrowserHistoryDisabled' is not shown or is not set to false, then this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the SavingBrowserHistoryDisabled value name does not exist or its value data is not set to 0, then this is a finding.

## Group: SRG-APP-000456

**Group ID:** `V-221584`

### Rule: The version of Google Chrome running on the system must be a supported version.

**Rule ID:** `SV-221584r961683_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Google Chrome is being continually updated by the vendor in order to address identified security vulnerabilities. Running an older version of the browser can introduce security vulnerabilities to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://settings/help 2. Cross-reference the build information displayed with the Google Chrome site to identify, at minimum, the oldest supported build available. As of July 2019, this is 74.x.x. 3. If the installed version of Chrome is not supported by Google, this is a finding.

## Group: SRG-APP-000089

**Group ID:** `V-221586`

### Rule: Deletion of browser history must be disabled.

**Rule ID:** `SV-221586r960879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Disabling this function will prevent users from deleting their browsing history, which could be used to identify malicious websites and files that could later be used for anti-virus and Intrusion Detection System (IDS) signatures. Furthermore, preventing users from deleting browsing history could be used to identify abusive web surfing on government systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If the policy "AllowDeletingBrowserHistory" is not shown or is not set to false, this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the "AllowDeletingBrowserHistory" value name does not exist or its value data is not set to "0", this is a finding.

## Group: SRG-APP-000089

**Group ID:** `V-221587`

### Rule: Prompt for download location must be enabled.

**Rule ID:** `SV-221587r960879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the policy is enabled, the user will be asked where to save each file before downloading. If the policy is disabled, downloads will start immediately, and the user will not be asked where to save the file. If the policy is not configured, the user will be able to change this setting.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome:// policy 2. If "PromptForDownloadLocation" is not displayed under the "Policy Name" column or it is not set to "true" under the "Policy Value" column, then this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the "PromptForDownloadLocation" value name does not exist or its value data is not set to "1", this is a finding.

## Group: SRG-APP-000089

**Group ID:** `V-221588`

### Rule: Download restrictions must be configured.

**Rule ID:** `SV-221588r1106670_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the policy means users cannot bypass download security decisions. There are many types of download warnings within Chrome, which roughly break down into these categories: - Malicious, as flagged by the Safe Browsing server. - Uncommon or unwanted, as flagged by the Safe Browsing server. - A dangerous file type (e.g., all SWF downloads and many EXE downloads). Setting the policy blocks different subsets of these, depending on its value: 0 = No special restrictions. Default. 1 = Block malicious downloads and dangerous file types. 2 = Block malicious downloads, uncommon or unwanted downloads, and dangerous file types. 3 = Block all downloads. 4 = Block malicious downloads. Recommended.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is on the SIPRNet, this requirement is Not Applicable. Universal method: 1. In the omnibox (address bar) type "chrome:// policy". 2. If "DownloadRestrictions" is not displayed under the "Policy Name" column or it is set to "0", this is a finding. Windows method: 1. Start "regedit". 2. Navigate to "HKLM\Software\Policies\Google\Chrome\". 3. If the "DownloadRestrictions" value name does not exist or its value data is set to "0", this is a finding.

## Group: SRG-APP-000206

**Group ID:** `V-221590`

### Rule: Safe Browsing Extended Reporting must be disabled.

**Rule ID:** `SV-221590r961083_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enables Google Chrome's Safe Browsing Extended Reporting and prevents users from changing this setting. Extended Reporting sends some system information and page content to Google servers to help detect dangerous apps and sites. If the setting is set to "True", then reports will be created and sent whenever necessary (such as when a security interstitial is shown). If the setting is set to "False", reports will never be sent. If this policy is set to "True" or "False", the user will not be able to modify the setting. If this policy is left unset, the user will be able to change the setting and decide whether to send reports or not.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If "SafeBrowsingExtendedReportingEnabled" is not displayed under the "Policy Name" column or it is not set to "False", this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the "SafeBrowsingExtendedReportingEnabled" value name does not exist or its value data is not set to "0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-221591`

### Rule: WebUSB must be disabled.

**Rule ID:** `SV-221591r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allows you to set whether websites are allowed to get access to connected USB devices. Access can be completely blocked, or the user can be asked every time a website wants to get access to connected USB devices. If this policy is left not set, ”3” will be used, and the user will be able to change it. 2 = Do not allow any site to request access to USB devices via the WebUSB API 3 = Allow sites to ask the user to grant access to a connected USB device</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If "DefaultWebUsbGuardSetting" is not displayed under the "Policy Name" column or it is not set to "2", this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the "DefaultWebUsbGuardSetting" value name does not exist or its value data is not set to "2", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-221594`

### Rule: Google Cast must be disabled.

**Rule ID:** `SV-221594r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If this policy is set to ”True” or is not set, Google Cast will be enabled, and users will be able to launch it from the app menu, page context menus, media controls on Cast-enabled websites, and (if shown) the “Cast toolbar” icon. If this policy set to ”False”, Google Cast will be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If "EnableMediaRouter" is not displayed under the "Policy Name" column or it is not set to "False", this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the "EnableMediaRouter" value name does not exist or its value data is not set to "0", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-221595`

### Rule: Autoplay must be disabled.

**Rule ID:** `SV-221595r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This allows a user to control if videos can play automatically with audio content (without user consent) in Google Chrome. If the policy is set to "True", Google Chrome is allowed to autoplay media. If the policy is set to "False", Google Chrome is not allowed to autoplay media. The "AutoplayAllowlist" policy can be used to override this for certain URL patterns. By default, Google Chrome is not allowed to autoplay media. The "AutoplayAllowlist" policy can be used to override this for certain URL patterns.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If "AutoplayAllowed" is not displayed under the "Policy Name" column or it is not set to "False", this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the "AutoplayAllowed" value name does not exist or its value data is not set to "0", this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-221596`

### Rule: URLs must be allowlisted for Autoplay use.

**Rule ID:** `SV-221596r961092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Controls the allowlist of URL patterns that autoplay will always be enabled on. If the "AutoplayAllowed" policy is set to "True" then this policy will have no effect. If the "AutoplayAllowed" policy is set to "False", then any URL patterns set in this policy will still be allowed to play.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar), type chrome://policy. 2. If “AutoplayAllowlist” under the “Policy Name” column may be set to a list of administrator-approved URLs under the “Policy Value” column. This requirement is optional. Windows method: 1. Start regedit. 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the “AutoplayAllowlist” key may contain a list of administrator-approved URLs. This requirement is optional.

## Group: SRG-APP-000206

**Group ID:** `V-221597`

### Rule: Anonymized data collection must be disabled.

**Rule ID:** `SV-221597r961083_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enable URL-keyed anonymized data collection in Google Chrome and prevent users from changing this setting. URL-keyed anonymized data collection sends URLs of pages the user visits to Google to make searches and browsing better. If you enable this policy, URL-keyed anonymized data collection is always active. If you disable this policy, URL-keyed anonymized data collection is never active. If this policy is left not set, URL-keyed anonymized data collection will be enabled but the user will be able to change it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If "UrlKeyedAnonymizedDataCollectionEnabled" is not displayed under the “Policy Name” column or it is not set to "0" under the “Policy Value” column, this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the “UrlKeyedAnonymizedDataCollectionEnabled" value name does not exist or its value data is not set to "0," this is a finding.

## Group: SRG-APP-000206

**Group ID:** `V-221598`

### Rule: Collection of WebRTC event logs must be disabled.

**Rule ID:** `SV-221598r961083_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the policy is set to “true”, Google Chrome is allowed to collect WebRTC event logs from Google services (e.g., Google Meet), and upload those logs to Google. If the policy is set to “false”, or is unset, Google Chrome may not collect nor upload such logs. These logs contain diagnostic information helpful when debugging issues with audio or video calls in Chrome, such as the time and size of sent and received RTP packets, feedback about congestion on the network, and metadata about time and quality of audio and video frames. These logs do not contain audio or video contents from the call. This data collection by Chrome can only be triggered by Google's web services, such as Google Hangouts or Google Meet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If "WebRtcEventLogCollectionAllowed" is not displayed under the “Policy Name” column or it is not set to "0" under the “Policy Value” column, this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the "WebRtcEventLogCollectionAllowed" value name does not exist or its value data is not set to "0," this is a finding.

## Group: SRG-APP-000266

**Group ID:** `V-221599`

### Rule: Chrome development tools must be disabled.

**Rule ID:** `SV-221599r961167_rule`
**Severity:** low

**Description:**
<VulnDiscussion>While the risk associated with browser development tools is more related to the proper design of a web application, a risk vector remains within the browser. The developer tools allow end users and application developers to view and edit all types of web application related data via the browser. Page elements, source code, javascript, API calls, application data, etc. may all be viewed and potentially manipulated. Manipulation could be useful for troubleshooting legitimate issues, and this may be performed in a development environment. Manipulation could also be malicious and must be addressed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If the policy "DeveloperToolsAvailability" is not shown or is not set to "2", this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the key "DeveloperToolsAvailability" does not exist or is not set to "2", this is a finding.

## Group: SRG-APP-000206

**Group ID:** `V-226401`

### Rule: Guest Mode must be disabled.

**Rule ID:** `SV-226401r961083_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If this policy is set to true or not configured, Google Chrome will enable guest logins. Guest logins are Google Chrome profiles where all windows are in incognito mode. If this policy is set to false, Google Chrome will not allow guest profiles to be started.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If BrowserGuestModeEnabled is not displayed under the Policy Name column or it is not set to 0 under the Policy Value column, this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the BrowserGuestModeEnabled value name does not exist or its value data is not set to 0, this is a finding.

## Group: SRG-APP-000206

**Group ID:** `V-226402`

### Rule: AutoFill for credit cards must be disabled.

**Rule ID:** `SV-226402r961083_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling Google Chrome's AutoFill feature allows users to auto complete credit card information in web forms using previously stored information. If this setting is disabled, Autofill will never suggest or fill credit card information, nor will it save additional credit card information that the user might submit while browsing the web. If this setting is enabled or has no value, the user will be able to control Autofill for credit cards in the UI.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If AutofillCreditCardEnabled is not displayed under the Policy Name column or it is not set to 0 under the Policy Value column, this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the AutofillCreditCardEnabled value name does not exist or its value data is not set to 0, this is a finding.

## Group: SRG-APP-000206

**Group ID:** `V-226403`

### Rule: AutoFill for addresses must be disabled.

**Rule ID:** `SV-226403r961083_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling Google Chrome's AutoFill feature allows users to auto complete address information in web forms using previously stored information. If this setting is disabled, Autofill will never suggest or fill address information, nor will it save additional address information that the user might submit while browsing the web. If this setting is enabled or has no value, the user will be able to control Autofill for addresses in the UI.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If AutofillAddressEnabled is not displayed under the Policy Name column or it is not set to 0 under the Policy Value column, this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the AutofillAddressEnabled value name does not exist or its value data is not set to 0, this is a finding.

## Group: SRG-APP-000206

**Group ID:** `V-226404`

### Rule: Import AutoFill form data must be disabled.

**Rule ID:** `SV-226404r961083_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy forces the autofill form data to be imported from the previous default browser if enabled. If enabled, this policy also affects the import dialog. If disabled, the autofill form data is not imported. If it is not set, the user may be asked whether to import, or importing may happen automatically.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If ImportAutofillFormData is not displayed under the Policy Name column or it is not set to 0 under the Policy Value column, this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the ImportAutofillFormData value name does not exist or its value data is not set to 0, this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-241787`

### Rule: Web Bluetooth API must be disabled.

**Rule ID:** `SV-241787r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the policy to 3 lets websites ask for access to nearby Bluetooth devices. Setting the policy to 2 denies access to nearby Bluetooth devices. Leaving the policy unset lets sites ask for access, but users can change this setting. 2 = Do not allow any site to request access to Bluetooth devices via the Web Bluetooth API 3 = Allow sites to ask the user to grant access to a nearby Bluetooth device</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type chrome://policy 2. If DefaultWebBluetoothGuardSetting is not displayed under the Policy Name column or it is not set to 2 under the Policy Value column, then this is a finding. Windows method: 1. Start regedit 2. Navigate to HKLM\Software\Policies\Google\Chrome\ 3. If the DefaultWebBluetoothGuardSetting value name does not exist or its value data is not set to 2, then this is a finding.

## Group: SRG-APP-000383

**Group ID:** `V-245538`

### Rule: Use of the QUIC protocol must be disabled.

**Rule ID:** `SV-245538r961470_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>QUIC is used by more than half of all connections from the Chrome web browser to Google's servers, and this activity is undesirable in the DoD. Setting the policy to Enabled or leaving it unset allows the use of QUIC protocol in Google Chrome. Setting the policy to Disabled disallows the use of QUIC protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar), type chrome://policy. 2. If QuicAllowed is not displayed under the Policy Name column or it is not set to False under the Policy Value column, this is a finding. Windows method: 1. Start regedit. 2. Navigate to HKLM\Software\Policies\Google\Chrome\. 3. If the QuicAllowed value name does not exist or its value data is not set to 0, this is a finding.

## Group: SRG-APP-000080

**Group ID:** `V-245539`

### Rule: Session only based cookies must be enabled.

**Rule ID:** `SV-245539r960864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cookies must only be allowed per session and only for approved URLs as permanently stored cookies can be used for malicious intent. Approved URLs may be allowlisted via the CookiesAllowedForUrls policy setting, but is not a requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar), type chrome://policy 2. If the policy "DefaultCookiesSetting" is not shown or is not set to "4", this is a finding. Windows method: 1. Start regedit. 2. Navigate to HKLM\Software\Policies\Google\Chrome\DefaultCookiesSetting. 3. If this key does not exist, or is not set to "4", this is a finding.

## Group: SRG-APP-000089

**Group ID:** `V-275780`

### Rule: Create Themes with AI must be disabled.

**Rule ID:** `SV-275780r1106603_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Create Themes with AI lets users create custom themes/wallpapers by preselecting from a list of options. 0 = Allow the feature to be used, while allowing Google to use relevant data to improve its AI models. Relevant data may include prompts, inputs, outputs, source materials, and written feedback, depending on the feature. It may also be reviewed by humans to improve AI models. 0 is the default value, except when noted below. 1 = Allow the feature to be used, but does not allow Google to improve models using users' content (including prompts, inputs, outputs, source materials, and written feedback). 1 is the default value for Enterprise users managed by Google Admin console and for Education accounts managed by Google Workspace. 2 = Do not allow the feature.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type "chrome:// policy". 2. If "CreateThemesSettings" is not displayed under the "Policy Name" column or it is not set to "2" under the "Policy Value" column, this is a finding. Windows method: 1. Start "regedit". 2. Navigate to "HKLM\Software\Policies\Google\Chrome\". 3. If the "CreateThemesSettings" value name does not exist or its value data is not set to "2", this is a finding.

## Group: SRG-APP-000089

**Group ID:** `V-275781`

### Rule: DevTools Generative AI features must be disabled.

**Rule ID:** `SV-275781r1106671_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>These features in Google Chrome's DevTools employ generative AI models to provide additional debugging information. To use these features, Google Chrome collects data such as error messages, stack traces, code snippets, and network requests and sends them to a server owned by Google, which runs a generative AI model. Response body or authentication and cookie headers in network requests are not included in the data sent to the server. 0 = Allow the feature to be used, while allowing Google to use relevant data to improve its AI models. Relevant data may include prompts, inputs, outputs, source materials, and written feedback, depending on the feature. It may also be reviewed by humans to improve AI models. 0 is the default value, except when noted below. 1 = Allow the feature to be used, but does not allow Google to improve models using users' content (including prompts, inputs, outputs, source materials, and written feedback). 1 is the default value for Enterprise users managed by Google Admin console and for Education accounts managed by Google Workspace. 2 = Do not allow the feature.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type "chrome:// policy". 2. If "DevToolsGenAiSettings" is not displayed under the "Policy Name" column or it is not set to "2" under the "Policy Value" column, this is a finding. Windows method: 1. Start "regedit". 2. Navigate to "HKLM\Software\Policies\Google\Chrome\". 3. If the "DevToolsGenAiSettings" value name does not exist or its value data is not set to "2", this is a finding.

## Group: SRG-APP-000089

**Group ID:** `V-275782`

### Rule: GenAI local foundational model must be disabled.

**Rule ID:** `SV-275782r1106672_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configure how Google Chrome downloads the foundational GenAI model and uses it for inference locally. When the policy is set to Allowed (0) or not set, the model is downloaded automatically, and used for inference. When the policy is set to Disabled (1), the model will not be downloaded. Model downloading can also be disabled by ComponentUpdatesEnabled. 0 = Downloads model automatically 1 = Do not download model</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type "chrome:// policy". 2. If "GenAILocalFoundationalModelSettings" is not displayed under the "Policy Name" column or it is not set to "1" under the "Policy Value" column, this is a finding. Windows method: 1. Start "regedit". 2. Navigate to "HKLM\Software\Policies\Google\Chrome\". 3. If the "GenAILocalFoundationalModelSettings" value name does not exist or its value data is not set to "1", this is a finding.

## Group: SRG-APP-000089

**Group ID:** `V-275783`

### Rule: Help Me Write must be disabled.

**Rule ID:** `SV-275783r1106612_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Help Me Write is an AI-based writing assistant for short-form content on the web. Suggested content is based on prompts entered by the user and the content of the web page. 0 = Allow the feature to be used, while allowing Google to use relevant data to improve its AI models. Relevant data may include prompts, inputs, outputs, source materials, and written feedback, depending on the feature. It may also be reviewed by humans to improve AI models. 0 is the default value, except when noted below. 1 = Allow the feature to be used, but does not allow Google to improve models using users' content (including prompts, inputs, outputs, source materials, and written feedback). 1 is the default value for Enterprise users managed by Google Admin console and for Education accounts managed by Google Workspace. 2 = Do not allow the feature.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type "chrome:// policy". 2. If "HelpMeWriteSettings" is not displayed under the "Policy Name" column or it is not set to "2" under the "Policy Value" column, this is a finding. Windows method: 1. Start "regedit". 2. Navigate to "HKLM\Software\Policies\Google\Chrome\". 3. If the "HelpMeWriteSettings" value name does not exist or its value data is not set to "2", this is a finding.

## Group: SRG-APP-000089

**Group ID:** `V-275784`

### Rule: AI-powered History Search must be disabled.

**Rule ID:** `SV-275784r1106615_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>AI History Search is a feature that allows users to search their browsing history and receive generated answers based on page contents and not just the page title and URL. 0 = Allow the feature to be used, while allowing Google to use relevant data to improve its AI models. Relevant data may include prompts, inputs, outputs, source materials, and written feedback, depending on the feature. It may also be reviewed by humans to improve AI models. 0 is the default value, except when noted below. 1 = Allow the feature to be used, but does not allow Google to improve models using users' content (including prompts, inputs, outputs, source materials, and written feedback). 1 is the default value for Enterprise users managed by Google Admin console and for Education accounts managed by Google Workspace. 2 = Do not allow the feature.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type "chrome:// policy". 2. If "HistorySearchSettings" is not displayed under the "Policy Name" column or it is not set to "2" under the "Policy Value" column, this is a finding. Windows method: 1. Start "regedit". 2. Navigate to "HKLM\Software\Policies\Google\Chrome\". 3. If the "HistorySearchSettings" value name does not exist or its value data is not set to "2", this is a finding.

## Group: SRG-APP-000089

**Group ID:** `V-275785`

### Rule: Tab Compare Settings must be disabled.

**Rule ID:** `SV-275785r1106673_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Tab Compare is an AI-powered tool for comparing information across a user's tabs. For example, the feature can be offered to the user when multiple tabs with products in a similar category are open. 0 = Allow the feature to be used, while allowing Google to use relevant data to improve its AI models. Relevant data may include prompts, inputs, outputs, source materials, and written feedback, depending on the feature. It may also be reviewed by humans to improve AI models. 0 is the default value, except when noted below. 1 = Allow the feature to be used, but does not allow Google to improve models using users' content (including prompts, inputs, outputs, source materials, and written feedback). 1 is the default value for Enterprise users managed by Google Admin console and for Education accounts managed by Google Workspace. 2 = Do not allow the feature.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Universal method: 1. In the omnibox (address bar) type "chrome:// policy". 2. If "TabCompareSettings" is not displayed under the "Policy Name" column or it is not set to "2" under the "Policy Value" column, this is a finding. Windows method: 1. Start "regedit". 2. Navigate to "HKLM\Software\Policies\Google\Chrome\". 3. If the "TabCompareSettings" value name does not exist or its value data is not set to "2", this is a finding.

