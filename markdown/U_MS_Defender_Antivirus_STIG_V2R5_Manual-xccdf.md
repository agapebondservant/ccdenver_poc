# STIG Benchmark: Microsoft Defender Antivirus Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000279

**Group ID:** `V-213426`

### Rule: Microsoft Defender AV must be configured to block the Potentially Unwanted Application (PUA) feature.

**Rule ID:** `SV-213426r961197_rule`
**Severity:** high

**Description:**
<VulnDiscussion>After enabling this feature, PUA protection blocking takes effect on endpoint clients after the next signature update or computer restart. Signature updates take place daily under typical circumstances. PUA will be blocked and automatically quarantined.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> "Configure detection for potentially unwanted applications" is set to "Enabled" and "Block". Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender If the value "PUAProtection" does not exist, this is a finding. If the value "PUAProtection" is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000279

**Group ID:** `V-213427`

### Rule: Microsoft Defender AV must be configured to automatically take action on all detected tasks.

**Rule ID:** `SV-213427r961197_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows Microsoft Defender configuration to automatically take action on all detected threats. The action to be taken on a particular threat is determined by the combination of the policy-defined action user-defined action and the signature-defined action. If this policy setting is enabled, Microsoft Defender does not automatically take action on the detected threats but prompts users to choose from the actions available for each threat. If this policy setting is disabled or not configured, Microsoft Defender automatically takes action on all detected threats after a nonconfigurable delay of approximately five seconds.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> "Turn off routine remediation" is set to "Disabled" or "Not Configured". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender Criteria: If the value "DisableRoutinelyTakingAction" is REG_DWORD = 0, this is not a finding. If the value does not exist, this is not a finding. If the value is 1, this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-213428`

### Rule: Microsoft Defender AV must be configured to run and scan for malware and other potentially unwanted software.

**Rule ID:** `SV-213428r961194_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This policy setting turns off Microsoft Defender Antivirus. If this policy setting is enabled, Microsoft Defender Antivirus does not run and computers are not scanned for malware or other potentially unwanted software. When the setting is disabled and a third-party antivirus solution is installed, the two applications can both simultaneously try to protect the system. The two AV solutions both attempt to quarantine the same threat and will fight for access to delete the file. Users will see conflicts and the system may lock up until the two solutions finish processing. When the setting is not configured and a third-party antivirus solution is installed, both applications coexist on the system without conflicts. Defender Antivirus will automatically disable itself and will enable if the third-party solution stops functioning. When the setting is not configured and Defender Antivirus is the only AV solution, Defender AV will run (default state) and receive definition updates. An administrator account is needed to turn off the service. A standard user cannot disable the service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> "Turn off Windows Defender Antivirus" is set to “Not Configured”. For Windows 10: Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender Criteria: If the value "DisableAntiSpyware" does not exist, this is not a finding.

## Group: SRG-APP-000278

**Group ID:** `V-213429`

### Rule: Microsoft Defender AV must be configured to not exclude files for scanning.

**Rule ID:** `SV-213429r961194_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows disabling of scheduled and real-time scanning for files under the paths specified or for the fully qualified resources specified. Paths should be added under the Options for this setting. Each entry must be listed as a name value pair where the name should be a string representation of a path or a fully qualified resource name. As an example, a path might be defined as: "c:\Windows" to exclude all files in this directory. A fully qualified resource name might be defined as: "C:\Windows\App.exe". The value is not used and it is recommended that this be set to 0. Exceptions can be made to allow file/folders that are impacting enterprise applications to be excluded from being scanned. All exclusions should be documented and approved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Exclusions >> "Path Exclusions" is set to "Disabled" or "Not Configured. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Exclusions Criteria: If the value "Exclusions_Paths" does not exist, this is not a finding.

## Group: SRG-APP-000278

**Group ID:** `V-213430`

### Rule: Microsoft Defender AV must be configured to not exclude files opened by specified processes.

**Rule ID:** `SV-213430r961194_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows the disabling of scheduled and real-time scanning for any file opened by any of the specified processes. The process itself will not be excluded. To exclude the process, use the Path exclusion. Processes should be added under the options for this setting. Each entry must be listed as a name value pair where the name should be a string representation of the path to the process image. Note that only executables can be excluded. For example, a process might be defined as: "c:\windows\app.exe". The value is not used and it is recommended that this be set to 0.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Exclusions >> "Process Exclusions" is set to "Disabled" or "Not Configured". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Exclusions Criteria: If the value "Exclusions_Processes" does not exist, this is not a finding.

## Group: SRG-APP-000278

**Group ID:** `V-213431`

### Rule: Microsoft Defender AV must be configured to enable the Automatic Exclusions feature.

**Rule ID:** `SV-213431r961194_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting allows an administrator to specify if Automatic Exclusions feature for Server SKUs should be turned off.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Exclusions >> "Turn off Auto Exclusions" is set to "Disabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Exclusions Criteria: If the value "DisableAutoExclusions" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-213432`

### Rule: Microsoft Defender AV must be configured to disable local setting override for reporting to Microsoft MAPS.

**Rule ID:** `SV-213432r961092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting configures a local override for the configuration to join Microsoft MAPS. This setting can only be set by Group Policy. If this setting is enabled, the local preference setting will take priority over Group Policy. If this setting is disabled or not configured, Group Policy will take priority over the local preference setting.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is applicable to unclassified systems. For other systems this is NA. Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> MAPS >> "Configure local setting override for reporting to Microsoft MAPS" is set to "Disabled" or "Not Configured". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Spynet Criteria: If the value "LocalSettingOverrideSpynetReporting" is REG_DWORD = 0, this is not a finding. If the value does not exist, this is not a finding. If the value is 1, this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-213433`

### Rule: Microsoft Defender AV must be configured to check in real time with MAPS before content is run or accessed.

**Rule ID:** `SV-213433r961194_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This feature ensures the device checks in real time with the Microsoft Active Protection Service (MAPS) before allowing certain content to be run or accessed. If this feature is disabled, the check will not occur, which will lower the protection state of the device. Enabled - The Block at First Sight setting is turned on. Disabled - The Block at First Sight setting is turned off. This feature requires these Group Policy settings to be set as follows: MAPS >> The "Join Microsoft MAPS" must be enabled or the "Block at First Sight" feature will not function. MAPS >> The "Send file samples when further analysis is required" should be set to 1 (Send safe samples) or 3 (Send all samples). Setting to 0 (Always Prompt) will lower the protection state of the device. Setting to 2 (Never send) means the "Block at First Sight" feature will not function. Real-time Protection >> The "Scan all downloaded files and attachments" policy must be enabled or the "Block at First Sight" feature will not function. Real-time Protection >> Do not enable the "Turn off real-time protection" policy or the "Block at First Sight" feature will not function.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is applicable to unclassified systems. For other systems this is NA. Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> MAPS >> "Configure the 'Block at First Sight' feature" is set to "Enabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Spynet Criteria: If the value "DisableBlockAtFirstSeen" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-213434`

### Rule: Microsoft Defender AV must join Microsoft MAPS.

**Rule ID:** `SV-213434r1134051_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows joining Microsoft MAPS. Microsoft MAPS is the online community that helps in choosing how to respond to potential threats. The community also helps stop the spread of new malicious software infections. You can choose to send basic or additional information about detected software. Additional information helps Microsoft create new definitions and protect your computer. This information can include things like location of detected items on your computer if harmful software was removed. The information will be automatically collected and sent. In some instances personal information might unintentionally be sent to Microsoft. However Microsoft will not use this information to identify you or contact you. Possible options are: (0x0) Disabled (default) (0x1) Basic membership (0x2) Advanced membership Basic membership will send basic information to Microsoft about software that has been detected, including where the software came from, the actions that you apply or that are applied automatically, and whether the actions were successful. Advanced membership will send, in addition to basic information, more information to Microsoft about malicious software spyware and potentially unwanted software, including the location of the software file names, how the software operates, and how it has impacted your computer. If this setting is enabled, you will join Microsoft MAPS with the membership specified. If this setting is disabled or do not configured, you will not join Microsoft MAPS. In Windows 10, Basic membership is no longer available, so setting the value to 1 or 2 enrolls the device into Advanced membership.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is applicable to unclassified systems. For other systems, this is Not Applicable. Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> MAPS >> "Join Microsoft MAPS" is set to "Enabled" and "Advanced MAPS" is selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Spynet Criteria: If the value "SpynetReporting" is REG_DWORD = 1, or REG_DWORD = 2, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-213435`

### Rule: Microsoft Defender AV must be configured to only send safe samples for MAPS telemetry.

**Rule ID:** `SV-213435r961092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting configures behavior of samples submission when opt-in for MAPS telemetry is set. Possible options are: (0x0) Always prompt (0x1) Send safe samples automatically (0x2) Never send (0x3) Send all samples automatically</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is applicable to unclassified systems. For other systems this is NA. Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> MAPS >> "Send file samples when further analysis is required" is set to "Enabled" and "Send safe samples" is selected from the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Spynet Criteria: If the value "SubmitSamplesConsent" is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000278

**Group ID:** `V-213436`

### Rule: Microsoft Defender AV must be configured for protocol recognition for network protection.

**Rule ID:** `SV-213436r961194_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows the configuration of protocol recognition for network protection against exploits of known vulnerabilities. If this setting is enabled or not configured, protocol recognition will be enabled. If this setting is disabled, protocol recognition will be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Network Inspection System >> "Turn on protocol recognition" is set to "Enabled" or "Not Configured". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\NIS Criteria: If the value "DisableProtocolRecognition" is REG_DWORD = 0, this is not a finding. If the value does not exist, this is not a finding. If the value is 1, this is a finding.

## Group: SRG-APP-000112

**Group ID:** `V-213437`

### Rule: Microsoft Defender AV must be configured to not allow local override of monitoring for file and program activity.

**Rule ID:** `SV-213437r960921_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting configures a local override for the configuration of monitoring for file and program activity on your computer. This setting can only be set by Group Policy. If this setting is enabled, the local preference setting will take priority over Group Policy. If this setting is disabled or not configured, Group Policy will take priority over the local preference setting.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Real-time Protection >> "Configure local setting override for monitoring file and program activity on your computer" is set to "Disabled" or "Not Configured". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection Criteria: If the value "LocalSettingOverrideDisableOnAccessProtection" is REG_DWORD = 0, this is not a finding. If the value does not exist, this is not a finding. If the value is 1, this is a finding.

## Group: SRG-APP-000112

**Group ID:** `V-213438`

### Rule: Microsoft Defender AV must be configured to not allow override of monitoring for incoming and outgoing file activity.

**Rule ID:** `SV-213438r960921_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting configures a local override for the configuration of monitoring for incoming and outgoing file activity. This setting can only be set by Group Policy. If this setting is enabled, the local preference setting will take priority over Group Policy. If this setting is disabled or not configured, Group Policy will take priority over the local preference setting.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Real-time Protection >> "Configure local setting override for monitoring for incoming and outgoing file activity" is set to "Disabled" or "Not Configured". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection Criteria: If the value "LocalSettingOverrideRealtimeScanDirection" is REG_DWORD = 0, this is not a finding. If the value does not exist, this is not a finding. If the value is 1, this is a finding.

## Group: SRG-APP-000209

**Group ID:** `V-213439`

### Rule: Microsoft Defender AV must be configured to not allow override of scanning for downloaded files and attachments.

**Rule ID:** `SV-213439r961089_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting configures a local override for the configuration of scanning for all downloaded files and attachments. This setting can only be set by Group Policy. If this setting is enabled, the local preference setting will take priority over Group Policy. If this setting is disabled or not configured, Group Policy will take priority over the local preference setting.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Real-time Protection >> "Configure local setting override for scanning all downloaded files and attachments" is set to "Disabled" or "Not Configured". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection Criteria: If the value "LocalSettingOverrideDisableIOAVProtection" is REG_DWORD = 0, this is not a finding. If the value does not exist, this is not a finding. If the value is 1, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-213440`

### Rule: Microsoft Defender AV must be configured to not allow override of behavior monitoring.

**Rule ID:** `SV-213440r961092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting configures a local override for the configuration of behavior monitoring. This setting can only be set by Group Policy. If this setting is enabled, the local preference setting will take priority over Group Policy. If this setting is disabled or not configured, Group Policy will take priority over the local preference setting.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Real-time Protection >> "Configure local setting override for turn on behavior monitoring" is set to "Disabled" or "Not Configured". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection Criteria: If the value "LocalSettingOverrideDisableBehaviorMonitoring" is REG_DWORD = 0, this is not a finding. If the value does not exist, this is not a finding. If the value is 1, this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-213441`

### Rule: Microsoft Defender AV Group Policy settings must take priority over the local preference settings.

**Rule ID:** `SV-213441r961194_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting configures a local override for the configuration to turn on real-time protection. This setting can only be set by Group Policy. If this setting is enabled, the local preference setting will take priority over Group Policy. If this setting is disabled or not configured, Group Policy will take priority over the local preference setting.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Real-time Protection >> "Configure local setting override to turn on real-time protection" is set to "Disabled" or "Not Configured". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection Criteria: If the value "LocalSettingOverrideDisableRealtimeMonitoring" is REG_DWORD = 0, this is not a finding. If the value does not exist, this is not a finding. If the value is 1, this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-213442`

### Rule: Microsoft Defender AV must monitor for incoming and outgoing files.

**Rule ID:** `SV-213442r961194_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows the configuration of monitoring for incoming and outgoing files without having to turn off monitoring entirely. It is recommended for use on servers that have a lot of incoming and outgoing file activity but for performance reasons need to have scanning disabled for a particular scan direction. The appropriate configuration should be evaluated based on the server role. Note that this configuration is only honored for NTFS volumes. For any other file system type, full monitoring of file and program activity will be present on those volumes. The options for this setting are mutually exclusive: 0 = Scan incoming and outgoing files (default) 1 = Scan incoming files only 2 = Scan outgoing files only Any other value, or if the value does not exist, resolves to the default (0). If this setting is enabled, the specified type of monitoring will be enabled. If this setting is disabled or not configured, monitoring for incoming and outgoing files will be enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Real-time Protection >> "Configure monitoring for incoming and outgoing file and program activity" is set to "Disabled" or "Not Configured". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection Criteria: If the value "RealtimeScanDirection" is REG_DWORD = 0, this is not a finding. If the value does not exist, this is not a finding. If the value is 1 or 2, this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-213443`

### Rule: Microsoft Defender AV must be configured to monitor for file and program activity.

**Rule ID:** `SV-213443r961194_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows configuration of monitoring for file and program activity. If this setting is enabled or not configured, monitoring for file and program activity will be enabled. If this setting is disabled, monitoring for file and program activity will be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Real-time Protection >> "Monitor file and program activity on your computer to be scanned" is set to "Enabled" or "Not Configured". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection Criteria: If the value "DisableOnAccessProtection" is REG_DWORD = 0, this is not a finding. If the value does not exist, this is not a finding. If the value is 1, this is a finding.

## Group: SRG-APP-000209

**Group ID:** `V-213444`

### Rule: Microsoft Defender AV must be configured to scan all downloaded files and attachments.

**Rule ID:** `SV-213444r961089_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows configuration of scanning for all downloaded files and attachments. If this setting is enabled or not configured, scanning for all downloaded files and attachments will be enabled. If this setting is disabled, scanning for all downloaded files and attachments will be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Real-time Protection >> "Scan all downloaded files and attachments" is set to "Enabled" or "Not Configured". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection Criteria: If the value "DisableIOAVProtection" is REG_DWORD = 0, this is not a finding. If the value does not exist, this is not a finding. If the value is 1, this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-213445`

### Rule: Microsoft Defender AV must be configured to always enable real-time protection.

**Rule ID:** `SV-213445r961194_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting turns off real-time protection prompts for known malware detection. Microsoft Defender Antivirus alerts when malware or potentially unwanted software attempts to install itself or to run on your computer. If this policy setting is enabled, Microsoft Defender Antivirus will not prompt users to take actions on malware detections. If this policy setting is disabled or not configured, Microsoft Defender Antivirus will prompt users to take actions on malware detections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Real-time Protection >> "Turn off real-time protection" is set to "Disabled" or "Not Configured". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection Criteria: If the value "DisableRealtimeMonitoring" is REG_DWORD = 0, this is not a finding. If the value does not exist, this is not a finding. If the value is 1, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-213446`

### Rule: Microsoft Defender AV must be configured to enable behavior monitoring.

**Rule ID:** `SV-213446r961092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows configuration of behavior monitoring. If this setting is enabled or not configured, behavior monitoring will be enabled. If this setting is disabled, behavior monitoring will be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Real-time Protection >> "Turn on behavior monitoring" is set to "Enabled" or "Not Configured". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection Criteria: If the value "DisableBehaviorMonitoring" is REG_DWORD = 0, this is not a finding. If the value does not exist, this is not a finding. If the value is 1, this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-213447`

### Rule: Microsoft Defender AV must be configured to process scanning when real-time protection is enabled.

**Rule ID:** `SV-213447r961194_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows the configuration of process scanning when real-time protection is turned on. This helps to catch malware, which could start when real-time protection is turned off. If this setting is enabled or not configured, a process scan will be initiated when real-time protection is turned on. If this setting is disabled, a process scan will not be initiated when real-time protection is turned on.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Real-time Protection >> "Turn on process scanning whenever real-time protection is enabled" is set to "Enabled" or "Not Configured". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection Criteria: If the value "DisableScanOnRealtimeEnable" is REG_DWORD = 0, this is not a finding. If the value does not exist, this is not a finding. If the value is 1, this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-213448`

### Rule: Microsoft Defender AV must be configured to scan archive files.

**Rule ID:** `SV-213448r961194_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows the configuration of scans for malicious software and unwanted software in archive files such as .ZIP or .CAB files. If this setting is enabled or not configured, archive files will be scanned. If this setting is disabled, archive files will not be scanned.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Scan >> "Scan archive files" is set to "Enabled" or "Not Configured". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Scan Criteria: If the value "DisableArchiveScanning" is REG_DWORD = 0, this is not a finding. If the value does not exist, this is not a finding. If the value is 1, this is a finding.

## Group: SRG-APP-000073

**Group ID:** `V-213449`

### Rule: Microsoft Defender AV must be configured to scan removable drives.

**Rule ID:** `SV-213449r960852_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows the management of whether or not to scan for malicious software and unwanted software in the contents of removable drives such as USB flash drives when running a full scan. If this setting is enabled, removable drives will be scanned during any type of scan. If this setting is disabled or not configured, removable drives will not be scanned during a full scan. Removable drives may still be scanned during quick scan and custom scan.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Scan >> "Scan removable drives" is set to "Enabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Scan Criteria: If the value "DisableRemovableDriveScanning" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000277

**Group ID:** `V-213450`

### Rule: Microsoft Defender AV must be configured to perform a weekly scheduled scan.

**Rule ID:** `SV-213450r961191_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows specifying the day of the week on which to perform a scheduled scan. The scan can also be configured to run every day or to never run at all. This setting can be configured with the following ordinal number values: (0x0) Every Day (0x1) Sunday (0x2) Monday (0x3) Tuesday (0x4) Wednesday (0x5) Thursday (0x6) Friday (0x7) Saturday (0x8) Never (default) If this setting is enabled, a scheduled scan will run at the frequency specified. If this setting is disabled or not configured, a scheduled scan will run at a default frequency.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Scan >> "Specify the day of the week to run a scheduled scan" is set to "Enabled" and anything other than "Never" is selected in the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Scan Criteria: If the value "ScheduleDay" is REG_DWORD = 0x8, this is a finding. Values of 0x0 through 0x7 are acceptable and not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-213451`

### Rule: Microsoft Defender AV must be configured to turn on e-mail scanning.

**Rule ID:** `SV-213451r961092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows the configuration of e-mail scanning. When e-mail scanning is enabled, the engine will parse the mailbox and mail files according to their specific format in order to analyze the mail bodies and attachments. Several e-mail formats are currently supported, for example: pst (Outlook), dbx mbx mime (Outlook Express), binhex (Mac). If this setting is enabled, e-mail scanning will be enabled. If this setting is disabled or not configured, e-mail scanning will be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Scan >> "Turn on e-mail scanning" is set to "Enabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Scan Criteria: If the value "DisableEmailScanning" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000276

**Group ID:** `V-213452`

### Rule: Microsoft Defender AV spyware definition age must not exceed 7 days.

**Rule ID:** `SV-213452r961188_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This policy setting allows defining the number of days that must pass before spyware definitions are considered out of date. If definitions are determined to be out of date, this state may trigger several additional actions, including falling back to an alternative update source or displaying a warning icon in the user interface. By default this value is set to 14 days. If this setting is enabled, spyware definitions will be considered out of date after the number of days specified have passed without an update. If this setting is disabled or not configured, spyware definitions will be considered out of date after the default number of days have passed without an update.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Security Intelligence Updates >> "Define the number of days before spyware security intelligence considered out of date" is set to "Enabled" and "7" or less is selected in the drop-down box (excluding "0", which is unacceptable). If third-party antispyware is installed and up to date, the Windows Defender AV spyware age requirement will be NA. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Signature Updates Criteria: If the value "ASSignatureDue" is REG_DWORD = 7, this is not a finding. A value of 1 - 6 is also acceptable and not a finding. A value of 0 is a finding. A value higher than 7 is a finding.

## Group: SRG-APP-000276

**Group ID:** `V-213453`

### Rule: Microsoft Defender AV virus definition age must not exceed 7 days.

**Rule ID:** `SV-213453r961188_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This policy setting allows defining the number of days that must pass before virus definitions are considered out of date. If definitions are determined to be out of date, this state may trigger several additional actions, including falling back to an alternative update source or displaying a warning icon in the user interface. By default, this value is set to 14 days. If this setting is enabled, virus definitions will be considered out of date after the number of days specified have passed without an update. If this setting is disabled or not configured, virus definitions will be considered out of date after the default number of days have passed without an update.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >>Security Intelligence Updates >> "Define the number of days before virus security intelligence considered out of date" is set to "Enabled" and "7" or less is selected in the drop-down box (excluding "0", which is unacceptable). If third-party antivirus protection is installed and up to date, the Windows Defender Antivirus age requirement is NA. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Signature Updates Criteria: If the value "AVSignatureDue" is REG_DWORD = 7, this is not a finding. A value of 1 - 6 is also acceptable and not a finding. A value of 0 is a finding. A value higher than 7 is a finding.

## Group: SRG-APP-000261

**Group ID:** `V-213454`

### Rule: Microsoft Defender AV must be configured to check for definition updates daily.

**Rule ID:** `SV-213454r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows specifying the day of the week on which to check for definition updates. The check can also be configured to run every day or to never run at all. This setting can be configured with the following ordinal number values: (0x0) Every Day (default) (0x1) Sunday (0x2) Monday (0x3) Tuesday (0x4) Wednesday (0x5) Thursday (0x6) Friday (0x7) Saturday (0x8) Never If this setting is enabled, the check for definition updates will occur at the frequency specified. If this setting is disabled or not configured, the check for definition updates will occur at a default frequency.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Security Intelligence Updates >> "Specify the day of the week to check for security intelligence updates" is set to "Enabled" and "Every Day" is selected in the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Signature Updates Criteria: If the value "ScheduleDay" is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-213455`

### Rule: Microsoft Defender AV must be configured for automatic remediation action to be taken for threat alert level Severe.

**Rule ID:** `SV-213455r961086_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows the customization of which automatic remediation action will be taken for each threat alert level. Threat alert levels should be added under the Options for this setting. Each entry must be listed as a name value pair. The name defines a threat alert level. The value contains the action ID for the remediation action that should be taken. Valid threat alert levels are: 1 = Low 2 = Medium 4 = High 5 = Severe Valid remediation action values are: 2 = Quarantine 3 = Remove 6 = Ignore</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Threats >> "Specify threat alert levels at which default action should not be taken when detected" is set to "Enabled". Click the “Show…” box option and verify the "Value name" field contains a value of "5" and the "Value" field contains "2". A value of "3" in the "Value" field is more restrictive and also an acceptable value. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Threats\ThreatSeverityDefaultAction Criteria: If the value "5" is REG_SZ = 2 (or 3), this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-213456`

### Rule: Microsoft Defender AV must be configured to block executable content from email client and webmail.

**Rule ID:** `SV-213456r961092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This rule blocks the following file types from being run or launched from an email seen in either Microsoft Outlook or webmail (such as Gmail.com or Outlook.com): Executable files (such as .exe, .dll, or .scr) Script files (such as a PowerShell .ps, VisualBasic .vbs, or JavaScript .js file) Script archive files</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This setting is applicable starting with v1709 of Windows 10. It is NA for prior versions. Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Microsoft Defender Exploit Guard >> Attack Surface Reduction >> "Configure Attack Surface Reduction rules" is set to "Enabled”. Click "Show...". Verify the rule ID in the Value name column and the desired state in the Value column is set as follows: Value name: BE9BA2D9-53EA-4CDC-84E5-9B1EEEE46550 Value: 1 Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Windows Defender Exploit Guard\ASR\Rules Criteria: If the value "BE9BA2D9-53EA-4CDC-84E5-9B1EEEE46550" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-213457`

### Rule: Microsoft Defender AV must be configured block Office applications from creating child processes.

**Rule ID:** `SV-213457r961092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Office apps, such as Word or Excel, will not be allowed to create child processes. This is a typical malware behavior, especially for macro-based attacks that attempt to use Office apps to launch or download malicious executables.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This setting is applicable starting with v1709 of Windows 10. It is NA for prior versions. Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Microsoft Defender Exploit Guard >> Attack Surface Reduction >> "Configure Attack Surface Reduction rules" is set to "Enabled”. Click "Show...". Verify the rule ID in the Value name column and the desired state in the Value column is set as follows: Value name: D4F940AB-401B-4EFC-AADC-AD5F3C50688A Value: 1 Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Windows Defender Exploit Guard\ASR\Rules Criteria: If the value "D4F940AB-401B-4EFC-AADC-AD5F3C50688A" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-213458`

### Rule: Microsoft Defender AV must be configured block Office applications from creating executable content.

**Rule ID:** `SV-213458r961092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This rule targets typical behaviors used by suspicious and malicious add-ons and scripts (extensions) that create or launch executable files. This is a typical malware technique. Extensions will be blocked from being used by Office apps. Typically these extensions use the Windows Scripting Host (.wsh files) to run scripts that automate certain tasks or provide user-created add-on features.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This setting is applicable starting with v1709 of Windows 10. It is NA for prior versions. Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Microsoft Defender Exploit Guard >> Attack Surface Reduction >> "Configure Attack Surface Reduction rules" is set to "Enabled”. Click "Show...". Verify the rule ID in the Value name column and the desired state in the Value column is set as follows: Value name: 3B576869-A4EC-4529-8536-B80A7769E899 Value: 1 Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Windows Defender Exploit Guard\ASR\Rules Criteria: If the value "3B576869-A4EC-4529-8536-B80A7769E899" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-213459`

### Rule: Microsoft Defender AV must be configured to block Office applications from injecting into other processes.

**Rule ID:** `SV-213459r961092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Office apps, such as Word, Excel, or PowerPoint, will not be able to inject code into other processes. This is typically used by malware to run malicious code in an attempt to hide the activity from antivirus scanning engines.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This setting is applicable starting with v1709 of Windows 10. It is NA for prior versions. Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Microsoft Defender Exploit Guard >> Attack Surface Reduction >> "Configure Attack Surface Reduction rules" is set to "Enabled”. Click "Show...". Verify the rule ID in the Value name column and the desired state in the Value column is set as follows: Value name: 75668C1F-73B5-4CF0-BB93-3ECF5CB7CC84 Value: 1 Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Windows Defender Exploit Guard\ASR\Rules Criteria: If the value "75668C1F-73B5-4CF0-BB93-3ECF5CB7CC84" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-213460`

### Rule: Microsoft Defender AV must be configured to impede JavaScript and VBScript to launch executables.

**Rule ID:** `SV-213460r961092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>JavaScript and VBScript scripts can be used by malware to launch other malicious apps. This rule prevents these scripts from being allowed to launch apps, thus preventing malicious use of the scripts to spread malware and infect machines.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This setting is applicable starting with v1709 of Windows 10. It is NA for prior versions. Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Microsoft Defender Exploit Guard >> Attack Surface Reduction >> "Configure Attack Surface Reduction rules" is set to "Enabled". Click "Show...". Verify the rule ID in the Value name column and the desired state in the Value column is set as follows: Value name: D3E037E1-3EB8-44C8-A917-57927947596D Value: 1 Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Windows Defender Exploit Guard\ASR\Rules Criteria: If the value "D3E037E1-3EB8-44C8-A917-57927947596D" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-213461`

### Rule: Microsoft Defender AV must be configured to block execution of potentially obfuscated scripts.

**Rule ID:** `SV-213461r961092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malware and other threats can attempt to obfuscate or hide their malicious code in some script files. This rule prevents scripts that appear to be obfuscated from running. It uses the AntiMalwareScanInterface (AMSI) to determine if a script is potentially obfuscated and then blocks such a script or blocks scripts when an attempt is made to access them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This setting is applicable starting with v1709 of Windows 10. It is NA for prior versions. Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Windows Defender Exploit Guard >> Attack Surface Reduction >> "Configure Attack Surface Reduction rules" is set to "Enabled”. Click "Show...". Verify the rule ID in the Value name column and the desired state in the Value column is set as follows: Value name: 5BEB7EFE-FD9A-4556-801D-275E5FFC04CC Value: 1 Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Windows Defender Exploit Guard\ASR\Rules Criteria: If the value "5BEB7EFE-FD9A-4556-801D-275E5FFC04CC" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-213462`

### Rule: Microsoft Defender AV must be configured to block Win32 imports from macro code in Office.

**Rule ID:** `SV-213462r961092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This rule blocks potentially malicious behavior by not allowing macro code to execute routines in the Win 32 dynamic link library (DLL).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This setting is applicable starting with v1709 of Windows 10. It is NA for prior versions. Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Microsoft Defender Exploit Guard >> Attack Surface Reduction >> "Configure Attack Surface Reduction rules" is set to "Enabled". Click "Show...". Verify the rule ID in the Value name column and the desired state in the Value column is set as follows: Value name: 92E97FA1-2EDF-4476-BDD6-9DD0B4DDDC7B Value: 1 Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Windows Defender Exploit Guard\ASR\Rules Criteria: If the value "92E97FA1-2EDF-4476-BDD6-9DD0B4DDDC7B" is REG_SZ = 1, this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-213463`

### Rule: Microsoft Defender AV must be configured to prevent user and apps from accessing dangerous websites.

**Rule ID:** `SV-213463r961092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enable Microsoft Defender Exploit Guard network protection to prevent employees from using any application to access dangerous domains that may host phishing scams, exploit-hosting sites, and other malicious content on the internet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This setting is applicable starting with v1709 of Windows 10, it is NA for prior versions. Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Microsoft Defender Exploit Guard >> Network Protection >> "Prevent users and apps from accessing dangerous websites" is set to "Enabled” and "Block" is selected in the drop-down box. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Windows Defender Exploit Guard\Network Protection Criteria: If the value "EnableNetworkProtection" is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-213464`

### Rule: Microsoft Defender AV must be configured for automatic remediation action to be taken for threat alert level High.

**Rule ID:** `SV-213464r961086_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows the customization of which automatic remediation action will be taken for each threat alert level. Threat alert levels should be added under the Options for this setting. Each entry must be listed as a name value pair. The name defines a threat alert level. The value contains the action ID for the remediation action that should be taken. Valid threat alert levels are: 1 = Low 2 = Medium 4 = High 5 = Severe Valid remediation action values are: 2 = Quarantine 3 = Remove 6 = Ignore</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Threats >> "Specify threat alert levels at which default action should not be taken when detected" is set to "Enabled". Click the "Show…" box option and verify the "Value name" field contains a value of "4" and the "Value" field contains a "2". A value of "3" in the "Value" field is more restrictive and also an acceptable value. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Threats\ThreatSeverityDefaultAction Criteria: If the value "4" is REG_SZ = 2 (or 3), this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-213465`

### Rule: Microsoft Defender AV must be configured for automatic remediation action to be taken for threat alert level Medium.

**Rule ID:** `SV-213465r961086_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows the customization of which automatic remediation action will be taken for each threat alert level. Threat alert levels should be added under the Options for this setting. Each entry must be listed as a name value pair. The name defines a threat alert level. The value contains the action ID for the remediation action that should be taken. Valid threat alert levels are: 1 = Low 2 = Medium 4 = High 5 = Severe Valid remediation action values are: 2 = Quarantine 3 = Remove 6 = Ignore</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Threats >> "Specify threat alert levels at which default action should not be taken when detected" is set to "Enabled". Click the "Show…" box option and verify the "Value name" field contains a value of "2" and the "Value" field contains a "2". A value of "3" in the "Value" field is more restrictive and also an acceptable value. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Threats\ThreatSeverityDefaultAction Criteria: If the value "2" is REG_SZ = 2 (or 3), this is not a finding.

## Group: SRG-APP-000207

**Group ID:** `V-213466`

### Rule: Microsoft Defender AV must be configured for automatic remediation action to be taken for threat alert level Low.

**Rule ID:** `SV-213466r961086_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting allows the customization of which automatic remediation action will be taken for each threat alert level. Threat alert levels should be added under the Options for this setting. Each entry must be listed as a name value pair. The name defines a threat alert level. The value contains the action ID for the remediation action that should be taken. Valid threat alert levels are: 1 = Low 2 = Medium 4 = High 5 = Severe Valid remediation action values are: 2 = Quarantine 3 = Remove 6 = Ignore</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Threats >> "Specify threat alert levels at which default action should not be taken when detected" is set to "Enabled". Click the "Show…" box option and verify the "Value name" field contains a value of "1" and the "Value" field contains a "2". A value of "3" in the "Value" field is more restrictive and also an acceptable value. Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\Windows Defender\Threats\ThreatSeverityDefaultAction Criteria: If the value "1" is REG_SZ = 2 (or 3), this is not a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278647`

### Rule: Microsoft Defender AV must block Adobe Reader from creating child processes.

**Rule ID:** `SV-278647r1134293_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting prevents Adobe Reader from launching other processes, which can help mitigate security risks associated with malicious PDF files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Microsoft Defender Exploit Guard >> Attack Surface Reduction >> Configure Attack Surface Reduction rules is set to "Enabled". Under the policy option "Set the state for each ASR rule:", then click "Show". Verify GUID "7674ba52-37eb-4a4f-a9a1-f0f9a1619a2c" is in the "Value name" column with a value of "1"; otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278648`

### Rule: Microsoft Defender AV must block credential stealing from the Windows local security authority subsystem.

**Rule ID:** `SV-278648r1134295_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting helps prevent credential stealing by locking down Local Security Authority Subsystem Service (LSASS). </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Microsoft Defender Exploit Guard >> Attack Surface Reduction >> Configure Attack Surface Reduction rules is set to "Enabled". Under the policy option "Set the state for each ASR rule:", then click "Show". Verify GUID "9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2" is in the "Value name" column with a value of "1"; otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278649`

### Rule: Microsoft Defender AV must block untrusted and unsigned processes that run from USB.

**Rule ID:** `SV-278649r1134297_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting helps prevents unsigned or untrusted executable files from running from USB removable drives, including SD cards. Blocked file types include executable files (such as .exe, .dll, or .scr). </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Microsoft Defender Exploit Guard >> Attack Surface Reduction >> Configure Attack Surface Reduction rules is set to "Enabled". Under the policy option "Set the state for each ASR rule:", then click "Show". Verify GUID "b2b3f03d-6a65-4f7b-a9c7-1c7ef74a9ba4" is in the "Value name" column with a value of "1"; otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278650`

### Rule: Microsoft Defender AV must use advanced protection against ransomware.

**Rule ID:** `SV-278650r1134276_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting provides an extra layer of protection against ransomware. It uses both client and cloud heuristics to determine whether a file resembles ransomware. This rule doesn't block files that have one or more of the following characteristics: - The file is found to be unharmful in the Microsoft cloud. - The file is a valid signed file. - The file is prevalent enough to not be considered as ransomware. - The rule tends to err on the side of caution to prevent ransomware. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Microsoft Defender Exploit Guard >> Attack Surface Reduction >> Configure Attack Surface Reduction rules is set to "Enabled". Under the policy option "Set the state for each ASR rule:", then click "Show". Verify GUID "c1db55ab-c21a-4637-bb3f-a12568109d35" is in the "Value name" column with a value of "1", otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278651`

### Rule: Microsoft Defender AV must block process creations originating from PSExec and WMI commands.

**Rule ID:** `SV-278651r1134279_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting blocks processes created through PsExec and WMI from running. Both PsExec and WMI can remotely execute code. There is a risk of malware abusing functionality of PsExec and WMI for command and control purposes, or to spread an infection throughout an organization's network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Microsoft Defender Exploit Guard >> Attack Surface Reduction >> Configure Attack Surface Reduction rules is set to "Enabled". Under the policy option "Set the state for each ASR rule:", then click "Show". Verify GUID "d1e49aac-8f56-4280-b9ba-993a6d77406c" is in the "Value name" column with a value of "1", otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278652`

### Rule: Microsoft Defender AV must block persistence through WMI event subscription.

**Rule ID:** `SV-278652r1134282_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting prevents malware from abusing WMI to attain persistence on a device. Fileless threats employ various tactics to stay hidden, to avoid being seen in the file system, and to gain periodic execution control. Some threats can abuse the WMI repository and event model to stay hidden.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Microsoft Defender Exploit Guard >> Attack Surface Reduction >> Configure Attack Surface Reduction rules is set to "Enabled". Under the policy option "Set the state for each ASR rule:", then click "Show". Verify GUID "e6db77e5-3df2-4cf1-b95a-636979351e5b" is in the "Value name" column with a value of "1", otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278653`

### Rule: Microsoft Defender AV must block executable files from running unless they meet a prevalence, age, or trusted list criterion.

**Rule ID:** `SV-278653r1134285_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting blocks executable files, such as .exe, .dll, or .scr, from launching. Thus, launching untrusted or unknown executable files can be risky, as it might not be initially clear if the files are malicious.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Microsoft Defender Exploit Guard >> Attack Surface Reduction >> Configure Attack Surface Reduction rules is set to "Enabled". Under the policy option "Set the state for each ASR rule:", then click "Show". Verify GUID "01443614-cd74-433a-b99e-2ecdc07bfc25" is in the "Value name" column with a value of "1", otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278654`

### Rule: Microsoft Defender AV must block Office communication application from creating child processes.

**Rule ID:** `SV-278654r1134288_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting prevents Outlook from creating child processes while still allowing legitimate Outlook functions. This rule protects against social engineering attacks and prevents exploiting code from abusing vulnerabilities in Outlook. It also protects against Outlook rules and forms exploits that attackers can use when a user's credentials are compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Microsoft Defender Exploit Guard >> Attack Surface Reduction >> Configure Attack Surface Reduction rules is set to "Enabled". Under the policy option "Set the state for each ASR rule:", then click "Show". Verify GUID "26190899-1602-49e8-8b27-eb1d0a1ce869" is in the "Value name" column with a value of "1", otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278655`

### Rule: Microsoft Defender AV must block abuse of exploited vulnerable signed drivers.

**Rule ID:** `SV-278655r1134291_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting prevents an application from writing a vulnerable signed driver to disk. Vulnerable signed drivers can be exploited by local applications that have sufficient privileges to gain access to the kernel. Vulnerable signed drivers enable attackers to disable or circumvent security solutions, eventually leading to system compromise. The Block abuse of exploited vulnerable signed drivers rule does not block a driver already existing on the system from being loaded.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Microsoft Defender Exploit Guard >> Attack Surface Reduction >> Configure Attack Surface Reduction rules is set to "Enabled". Under the policy option "Set the state for each ASR rule:", then click "Show". Verify GUID "56a863a9-875e-4185-98a7-b882c64b5ce5" is in the "Value name" column with a value of "1", otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278656`

### Rule: Microsoft Defender AV must configure local administrator merge behavior for lists.

**Rule ID:** `SV-278656r1134248_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting configures how locally defined lists are combined or merged with globally defined lists. This setting applies to exclusion lists, specified remediation lists, and attack surface reduction.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Configure local administrator merge behavior for lists is set to "Enabled"; otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278657`

### Rule: Microsoft Defender AV must enable routine remediation.

**Rule ID:** `SV-278657r1134249_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When Microsoft Defender Antivirus runs a scan, it attempts to remediate or remove threats that are detected. Remediation actions can include removing a file, sending it to quarantine, or allowing it to remain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Turn off routine remediation is set to "Disabled"; otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278658`

### Rule: Microsoft Defender AV must control whether exclusions are visible to Local Admins.

**Rule ID:** `SV-278658r1134250_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Disabled (Default): If this setting is not configured or disabled, local admins can see exclusions in the Windows Security App or via PowerShell. Enabled: If this setting is enabled, local admins no longer see the exclusion list in Windows Security App or via PowerShell.O13. Note: Applying this setting will not remove exclusions, it only prevents them from being visible to local admins. This is reflected in?Get-MpPreference.I13.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Control whether or not exclusions are visible to Local Admins is set to "Enabled"; otherwise, this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-278659`

### Rule: Microsoft Defender AV must randomize scheduled task times.

**Rule ID:** `SV-278659r1134251_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In Microsoft Defender Antivirus, randomize the start time of the scan to any interval from 0 to 23 hours. By default, scheduled tasks begin at a random time within four hours of the time specified in Task Scheduler.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Randomize scheduled task times is set to "Enabled"; otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278660`

### Rule: Microsoft Defender AV must hide the Family options area.

**Rule ID:** `SV-278660r1134252_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Family options section contains links to settings and further information for parents of a Windows PC. It is not intended for enterprise or business environments. This section can be hidden from users of the machine. This option can be useful if you do not want users in the organization to see or have access to this section.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Windows Security >> Family Options >> Hide the Family options area is set to "Enabled"; otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278661`

### Rule: Microsoft Defender AV must enable the file hash computation feature.

**Rule ID:** `SV-278661r1134253_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy drives the ability to enforce Indicators of Compromise (IoC) by using file hash allow/block indicators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> MpEngine >> Enable file hash computation feature is set to "Enabled"; otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278662`

### Rule: Microsoft Defender AV must enable extended cloud check.

**Rule ID:** `SV-278662r1134254_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When Microsoft Defender Antivirus finds a suspicious file, it can prevent the file from running while it queries the Microsoft Defender Antivirus cloud service. The default period that the file is blocked is 10 seconds. Extending the cloud block timeout period can help ensure there is enough time to receive a proper determination from the Microsoft Defender Antivirus cloud service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> MpEngine >> Configure extended cloud check is set to "Enabled" with a Policy Option value of "50"; otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278663`

### Rule: Microsoft Defender AV must enable behavior monitoring.

**Rule ID:** `SV-278663r1134255_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Behavior monitoring is a critical detection and protection functionality of Microsoft Defender Antivirus. Monitors process behavior to detect and analyze potential threats based on the behavior of applications, services, and files. Rather than relying solely on signature-based detection (which identifies known malware patterns), behavior monitoring focuses on observing how software behaves in real time.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Turn on behavior monitoring is set to "Enabled"; otherwise, this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-278664`

### Rule: Microsoft Defender AV must scan all downloaded files and attachments.

**Rule ID:** `SV-278664r1134256_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Always-on protection consists of real-time protection, behavior monitoring, and heuristics to identify malware based on known suspicious and malicious activities. These activities include events, such as processes making unusual changes to existing files, modifying or creating automatic startup registry keys and startup locations (also known as autostart extensibility points, or ASEPs), and other changes to the file system or file structure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Real-time Protection >> Scan all downloaded files and attachments is set to "Enabled"; otherwise, this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-278665`

### Rule: Microsoft Defender AV must monitor file and program activity.

**Rule ID:** `SV-278665r1134257_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Always-on protection consists of real-time protection, behavior monitoring, and heuristics to identify malware based on known suspicious and malicious activities. These activities include events, such as processes making unusual changes to existing files, modifying or creating automatic startup registry keys and startup locations (also known as autostart extensibility points, or ASEPs), and other changes to the file system or file structure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Real-time Protection >> Monitor file and program activity on your computer is set to "Enabled"; otherwise, this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-278666`

### Rule: Microsoft Defender AV must enable real-time protection.

**Rule ID:** `SV-278666r1134258_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Always-on protection consists of real-time protection, behavior monitoring, and heuristics to identify malware based on known suspicious and malicious activities. These activities include events, such as processes making unusual changes to existing files, modifying or creating automatic startup registry keys and startup locations (also known as autostart extensibility points, or ASEPs), and other changes to the file system or file structure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Real-time Protection >> Turn off real-time protection is set to "Disabled"; otherwise, this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-278667`

### Rule: Microsoft Defender AV must enable process scanning whenever real-time protection is enabled.

**Rule ID:** `SV-278667r1134259_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Always-on protection consists of real-time protection, behavior monitoring, and heuristics to identify malware based on known suspicious and malicious activities. These activities include events, such as processes making unusual changes to existing files, modifying or creating automatic startup registry keys and startup locations (also known as autostart extensibility points, or ASEPs), and other changes to the file system or file structure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Real-time Protection >> Turn on process scanning whenever real-time protection is enabled is set to "Enabled"; otherwise, this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-278668`

### Rule: Microsoft Defender AV must enable script scanning.

**Rule ID:** `SV-278668r1134260_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Always-on protection consists of real-time protection, behavior monitoring, and heuristics to identify malware based on known suspicious and malicious activities. These activities include events, such as processes making unusual changes to existing files, modifying or creating automatic startup registry keys and startup locations (also known as autostart extensibility points, or ASEPs), and other changes to the file system or file structure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Real-time Protection >> Turn on script scanning is set to "Enabled"; otherwise, this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-278669`

### Rule: Microsoft Defender AV must enable real-time protection and Security Intelligence Updates during OOBE.

**Rule ID:** `SV-278669r1134261_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Always-on protection consists of real-time protection, behavior monitoring, and heuristics to identify malware based on known suspicious and malicious activities. These activities include events, such as processes making unusual changes to existing files, modifying or creating automatic startup registry keys and startup locations (also known as autostart extensibility points, or ASEPs), and other changes to the file system or file structure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Real-time Protection >> Configure real-time protection and Security Intelligence Updates during OOBE is set to "Enabled"; otherwise, this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-278670`

### Rule: Microsoft Defender AV must enable monitoring for incoming and outgoing file and program activity.

**Rule ID:** `SV-278670r1134262_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Always-on protection consists of real-time protection, behavior monitoring, and heuristics to identify malware based on known suspicious and malicious activities. These activities include events, such as processes making unusual changes to existing files, modifying or creating automatic startup registry keys and startup locations (also known as autostart extensibility points, or ASEPs), and other changes to the file system or file structure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Real-time Protection >> Configure monitoring for incoming and outgoing file and program activity is set to "Enabled" with a policy option of "bi-directional (full on-access)"; otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278671`

### Rule: Microsoft Defender AV must control folder access.

**Rule ID:** `SV-278671r1134263_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Controlled folder access helps protect valuable data from malicious apps and threats, such as ransomware.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Microsoft Defender Exploit Guard >> Controlled Folder Access >> Configure Controlled folder access is set to "Enabled" with a policy option of "Audit Mode". All other policy options aside from "Disable" are allowed. If the policy option for "Configure Controlled folder access" is set to "Disable", this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278672`

### Rule: Microsoft Defender AV must enable network protection to be configured into block or audit mode on Windows Server.

**Rule ID:** `SV-278672r1134264_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Microsoft's Exploit Guard comprises several techniques to defend against phishing attacks and malware. These include controlled folder access, attack surface reduction, and network protection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Microsoft Defender Exploit Guard >> Network Protection >> This settings controls whether Network Protection is allowed to be configured into block or audit mode on Windows Server is set to "Enabled" with a policy option of "Audit Mode"; otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278673`

### Rule: Microsoft Defender AV must disable auto exclusions.

**Rule ID:** `SV-278673r1134265_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Custom exclusions apply to scheduled scans, on-demand scans, and always-on real-time protection and monitoring. Exclusions for process-opened files only apply to real-time protection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Exclusions >> Turn off Auto Exclusions is set to "Disabled"; otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278674`

### Rule: Microsoft Defender AV must enable EDR in block mode.

**Rule ID:** `SV-278674r1134266_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>EDR in block mode allows Microsoft Defender Antivirus to take actions on post-breach, behavioral EDR detections. EDR in block mode is integrated with threat and vulnerability management capabilities. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Features >> Enable EDR in block mode is set to "Enabled"; otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278675`

### Rule: Microsoft Defender AV must report Dynamic Signature dropped events.

**Rule ID:** `SV-278675r1134267_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Microsoft Defender Antivirus logs "Dynamic Signature dropped" events when it blocks or removes a file based on a dynamically updated signature, but the signature itself is dropped, meaning it was not fully processed or applied. This can indicate a potential issue with signature updates or the system's ability to handle them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Reporting >> Configure whether to report Dynamic Signature dropped events is set to "Enabled"; otherwise, this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-278676`

### Rule: Microsoft Defender AV must scan excluded files and directories during quick scans.

**Rule ID:** `SV-278676r1134268_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In Microsoft Defender Antivirus, when an exclusion for a file or folder is created, it will generally be skipped during both real-time protection and on-demand scans (including quick scans and full scans). However, with newer releases, the option exists to configure quick scans to include files and directories that are otherwise excluded from real-time protection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Scan >> Scan excluded files and directories during quick scans is set to "Enabled"; otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278677`

### Rule: Microsoft Defender AV must convert warn verdict to block.

**Rule ID:** `SV-278677r1134269_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a site URL has an unknown or uncertain reputation, a toast notification presents the user with the following options: - Ok: The toast notification is released (removed), and the attempt to access the site is ended. - Unblock: The user has access to the site for 24 hours, at which point the block is reenabled. The user can continue to use Unblock to access the site until such time that the administrator prohibits (blocks) the site, thus removing the option to Unblock. - Feedback: The toast notification presents the user with a link to submit a ticket, which the user can use to submit feedback to the administrator in an attempt to justify access to the site.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Network Inspection System >> Convert warn verdict to block is set to "Enabled"; otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278678`

### Rule: Microsoft Defender AV must enable asynchronous inspection.

**Rule ID:** `SV-278678r1134270_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network protection includes performance optimization that allows block mode to asynchronously inspect long-lived connections, which might provide a performance improvement. This optimization can also help with app compatibility problems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Network Inspection System >> Turn on asynchronous inspection is set to "Enabled"; otherwise, this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-278679`

### Rule: Microsoft Defender AV must scan packed executables.

**Rule ID:** `SV-278679r1134271_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting manages whether Microsoft Defender Antivirus scans packed executables. Packed executables are executable files that contain compressed code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Scan >> Scan packed executables is set to "Enabled"; otherwise, this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-278680`

### Rule: Microsoft Defender AV must enable heuristics.

**Rule ID:** `SV-278680r1134272_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Always-on protection consists of real-time protection, behavior monitoring, and heuristics to identify malware based on known suspicious and malicious activities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> Scan >> Turn on heuristics is set to "Enabled"; otherwise, this is a finding.

## Group: SRG-APP-000210

**Group ID:** `V-278863`

### Rule: Microsoft Defender AV must set cloud protection level to High.

**Rule ID:** `SV-278863r1134300_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cloud protection in Microsoft Defender Antivirus delivers accurate, real-time, and intelligent protection. Cloud protection should be enabled by default.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration >> Administrative Templates >> Windows Components >> Microsoft Defender Antivirus >> MpEngine >> Select cloud protection level is set to "Enabled". Verify the policy value for "Select cloud blocking level" is set to "High"; otherwise, this is a finding.

