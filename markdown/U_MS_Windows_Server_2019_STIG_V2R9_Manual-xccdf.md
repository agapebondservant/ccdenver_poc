# STIG Benchmark: Microsoft Windows Server 2019 Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000002-GPOS-00002

**Group ID:** `V-205624`

### Rule: Windows Server 2019 must automatically remove or disable temporary user accounts after 72 hours.

**Rule ID:** `SV-205624r857301_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If temporary user accounts remain active when no longer needed or for an excessive period, these accounts may be used to gain unauthorized access. To mitigate this risk, automated termination of all temporary accounts must be set upon account creation. Temporary accounts are established as part of normal account activation procedures when there is a need for short-term accounts without the demand for immediacy in account activation. If temporary accounts are used, the operating system must be configured to automatically terminate these types of accounts after a DoD-defined time period of 72 hours. To address access requirements, many operating systems may be integrated with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review temporary user accounts for expiration dates. Determine if temporary user accounts are used and identify any that exist. If none exist, this is NA. Domain Controllers: Open "PowerShell". Enter "Search-ADAccount -AccountExpiring | FT Name, AccountExpirationDate". If "AccountExpirationDate" has not been defined within 72 hours for any temporary user account, this is a finding. Member servers and standalone or nondomain-joined systems: Open "Command Prompt". Run "Net user [username]", where [username] is the name of the temporary user account. If "Account expires" has not been defined within 72 hours for any temporary user account, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-205625`

### Rule: Windows Server 2019 must be configured to audit Account Management - Security Group Management successes.

**Rule ID:** `SV-205625r852412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Security Group Management records events such as creating, deleting, or changing security groups, including changes in group members. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Account Management >> Security Group Management - Success

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-205626`

### Rule: Windows Server 2019 must be configured to audit Account Management - User Account Management successes.

**Rule ID:** `SV-205626r852413_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. User Account Management records events such as creating, changing, deleting, renaming, disabling, or enabling user accounts. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Account Management >> User Account Management - Success

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-205627`

### Rule: Windows Server 2019 must be configured to audit Account Management - User Account Management failures.

**Rule ID:** `SV-205627r852414_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. User Account Management records events such as creating, changing, deleting, renaming, disabling, or enabling user accounts. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Account Management >> User Account Management - Failure

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-205628`

### Rule: Windows Server 2019 must be configured to audit Account Management - Computer Account Management successes.

**Rule ID:** `SV-205628r852415_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Computer Account Management records events such as creating, changing, deleting, renaming, disabling, or enabling computer accounts. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Account Management >> Computer Account Management - Success

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-205629`

### Rule: Windows Server 2019 must have the number of allowed bad logon attempts configured to three or less.

**Rule ID:** `SV-205629r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The account lockout feature, when enabled, prevents brute-force password attacks on the system. The higher this value is, the less effective the account lockout feature will be in protecting the local system. The number of bad logon attempts must be reasonably small to minimize the possibility of a successful password attack while allowing for honest errors made during normal user logon.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Account Policies >> Account Lockout Policy. If the "Account lockout threshold" is "0" or more than "3" attempts, this is a finding. For server core installations, run the following command: Secedit /Export /Areas SecurityPolicy /CFG C:\Path\FileName.Txt If "LockoutBadCount" equals "0" or is greater than "3" in the file, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-205630`

### Rule: Windows Server 2019 must have the period of time before the bad logon counter is reset configured to 15 minutes or greater.

**Rule ID:** `SV-205630r852416_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The account lockout feature, when enabled, prevents brute-force password attacks on the system. This parameter specifies the period of time that must pass after failed logon attempts before the counter is reset to "0". The smaller this value is, the less effective the account lockout feature will be in protecting the local system. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Account Policies >> Account Lockout Policy. If the "Reset account lockout counter after" value is less than "15" minutes, this is a finding. For server core installations, run the following command: Secedit /Export /Areas SecurityPolicy /CFG C:\Path\FileName.Txt If "ResetLockoutCount" is less than "15" in the file, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-205631`

### Rule: Windows Server 2019 required legal notice must be configured to display before console logon.

**Rule ID:** `SV-205631r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to display the logon banner prior to a logon attempt will negate legal proceedings resulting from unauthorized access to system resources. Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000024-GPOS-00007, SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: LegalNoticeText Value Type: REG_SZ Value: See message text below You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-205632`

### Rule: Windows Server 2019 title for legal banner dialog box must be configured with the appropriate text.

**Rule ID:** `SV-205632r890533_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Failure to display the logon banner prior to a logon attempt will negate legal proceedings resulting from unauthorized access to system resources. Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: LegalNoticeCaption Value Type: REG_SZ Value: Refer to message title options below "DoD Notice and Consent Banner", "US Department of Defense Warning Statement", or an organization-defined equivalent. If an organization-defined title is used, it can in no case contravene or modify the language of the banner text required in WN19-SO-000130. Automated tools may only search for the titles defined above. If an organization-defined title is used, a manual review will be required.

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-205633`

### Rule: Windows Server 2019 machine inactivity limit must be set to 15 minutes or less, locking the system with the screen saver.

**Rule ID:** `SV-205633r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unattended systems are susceptible to unauthorized use and should be locked when unattended. The screen saver should be set at a maximum of 15 minutes and be password protected. This protects critical and sensitive data from exposure to unauthorized personnel with physical access to the computer. Satisfies: SRG-OS-000028-GPOS-00009, SRG-OS-000029-GPOS-00010, SRG-OS-000031-GPOS-00012</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: InactivityTimeoutSecs Value Type: REG_DWORD Value: 0x00000384 (900) (or less, excluding "0" which is effectively disabled)

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-205634`

### Rule: Windows Server 2019 must be configured to audit logon successes.

**Rule ID:** `SV-205634r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Logon records user logons. If this is an interactive logon, it is recorded on the local system. If it is to a network share, it is recorded on the system accessed. Satisfies: SRG-OS-000032-GPOS-00013, SRG-OS-000470-GPOS-00214, SRG-OS-000472-GPOS-00217, SRG-OS-000473-GPOS-00218, SRG-OS-000475-GPOS-00220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Logon/Logoff >> Logon - Success

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-205635`

### Rule: Windows Server 2019 must be configured to audit logon failures.

**Rule ID:** `SV-205635r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Logon records user logons. If this is an interactive logon, it is recorded on the local system. If it is to a network share, it is recorded on the system accessed. Satisfies: SRG-OS-000032-GPOS-00013, SRG-OS-000470-GPOS-00214, SRG-OS-000472-GPOS-00217, SRG-OS-000473-GPOS-00218, SRG-OS-000475-GPOS-00220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Logon/Logoff >> Logon - Failure

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-205636`

### Rule: Windows Server 2019 Remote Desktop Services must require secure Remote Procedure Call (RPC) communications.

**Rule ID:** `SV-205636r877398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing unsecure RPC communication exposes the system to man-in-the-middle attacks and data disclosure attacks. A man-in-the-middle attack occurs when an intruder captures packets between a client and server and modifies them before allowing the packets to be exchanged. Usually the attacker will modify the information in the packets in an attempt to cause either the client or server to reveal sensitive information. Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000250-GPOS-00093</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services\ Value Name: fEncryptRPCTraffic Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-205637`

### Rule: Windows Server 2019 Remote Desktop Services must be configured with the client connection encryption set to High Level.

**Rule ID:** `SV-205637r877398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote connections must be encrypted to prevent interception of data or sensitive information. Selecting "High Level" will ensure encryption of Remote Desktop Services sessions in both directions. Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000250-GPOS-00093</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services\ Value Name: MinEncryptionLevel Type: REG_DWORD Value: 0x00000003 (3)

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-205638`

### Rule: Windows Server 2019 command line data must be included in process creation events.

**Rule ID:** `SV-205638r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Enabling "Include command line data for process creation events" will record the command line information with the process creation events in the log. This can provide additional detail when malware has run on a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\Audit\ Value Name: ProcessCreationIncludeCmdLine_Enabled Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-205639`

### Rule: Windows Server 2019 PowerShell script block logging must be enabled.

**Rule ID:** `SV-205639r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Enabling PowerShell script block logging will record detailed information from the processing of PowerShell commands and scripts. This can provide additional detail when malware has run on a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging\ Value Name: EnableScriptBlockLogging Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-205640`

### Rule: Windows Server 2019 permissions for the Application event log must prevent access by non-privileged accounts.

**Rule ID:** `SV-205640r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. The Application event log may be susceptible to tampering if proper permissions are not applied. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to the Application event log file. The default location is the "%SystemRoot%\System32\winevt\Logs" folder. However, the logs may have been moved to another folder. If the permissions for the "Application.evtx" file are not as restrictive as the default permissions listed below, this is a finding: Eventlog - Full Control SYSTEM - Full Control Administrators - Full Control

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-205641`

### Rule: Windows Server 2019 permissions for the Security event log must prevent access by non-privileged accounts.

**Rule ID:** `SV-205641r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. The Security event log may disclose sensitive information or be susceptible to tampering if proper permissions are not applied. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to the Security event log file. The default location is the "%SystemRoot%\System32\winevt\Logs" folder. However, the logs may have been moved to another folder. If the permissions for the "Security.evtx" file are not as restrictive as the default permissions listed below, this is a finding: Eventlog - Full Control SYSTEM - Full Control Administrators - Full Control

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-205642`

### Rule: Windows Server 2019 permissions for the System event log must prevent access by non-privileged accounts.

**Rule ID:** `SV-205642r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. The System event log may be susceptible to tampering if proper permissions are not applied. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to the System event log file. The default location is the "%SystemRoot%\System32\winevt\Logs" folder. However, the logs may have been moved to another folder. If the permissions for the "System.evtx" file are not as restrictive as the default permissions listed below, this is a finding: Eventlog - Full Control SYSTEM - Full Control Administrators - Full Control

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-205643`

### Rule: Windows Server 2019 Manage auditing and security log user right must only be assigned to the Administrators group.

**Rule ID:** `SV-205643r852417_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Manage auditing and security log" user right can manage the security log and change auditing configurations. This could be used to clear evidence of tampering. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029, SRG-OS-000063-GPOS-00032, SRG-OS-000337-GPOS-00129</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Manage auditing and security log" user right, this is a finding. - Administrators For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeSecurityPrivilege" user right, this is a finding: S-1-5-32-544 (Administrators) If the organization has an Auditors group, the assignment of this group to the user right would not be a finding. If an application requires this user right, this would not be a finding. Vendor documentation must support the requirement for having the user right. The requirement must be documented with the ISSO. The application account must meet requirements for application account passwords, such as length (WN19-00-000050) and required frequency of changes (WN19-00-000060).

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-205644`

### Rule: Windows Server 2019 must force audit policy subcategory settings to override audit policy category settings.

**Rule ID:** `SV-205644r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. This setting allows administrators to enable more precise auditing capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\ Value Name: SCENoApplyLegacyAuditPolicy Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-205645`

### Rule: Windows Server 2019 domain controllers must have a PKI server certificate.

**Rule ID:** `SV-205645r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Domain controllers are part of the chain of trust for PKI authentications. Without the appropriate certificate, the authenticity of the domain controller cannot be verified. Domain controllers must have a server certificate to establish authenticity as part of PKI authentications in the domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Run "MMC". Select "Add/Remove Snap-in" from the "File" menu. Select "Certificates" in the left pane and click the "Add >" button. Select "Computer Account" and click "Next". Select the appropriate option for "Select the computer you want this snap-in to manage" and click "Finish". Click "OK". Select and expand the Certificates (Local Computer) entry in the left pane. Select and expand the Personal entry in the left pane. Select the Certificates entry in the left pane. If no certificate for the domain controller exists in the right pane, this is a finding.

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-205646`

### Rule: Windows Server 2019 domain Controller PKI certificates must be issued by the DoD PKI or an approved External Certificate Authority (ECA).

**Rule ID:** `SV-205646r569188_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A PKI implementation depends on the practices established by the Certificate Authority (CA) to ensure the implementation is secure. Without proper practices, the certificates issued by a CA have limited value in authentication functions. The use of multiple CAs from separate PKI implementations results in interoperability issues. If servers and clients do not have a common set of root CA certificates, they are not able to authenticate each other.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Run "MMC". Select "Add/Remove Snap-in" from the "File" menu. Select "Certificates" in the left pane and click the "Add >" button. Select "Computer Account" and click "Next". Select the appropriate option for "Select the computer you want this snap-in to manage" and click "Finish". Click "OK". Select and expand the Certificates (Local Computer) entry in the left pane. Select and expand the Personal entry in the left pane. Select the Certificates entry in the left pane. In the right pane, examine the "Issued By" field for the certificate to determine the issuing CA. If the "Issued By" field of the PKI certificate being used by the domain controller does not indicate the issuing CA is part of the DoD PKI or an approved ECA, this is a finding. If the certificates in use are issued by a CA authorized by the Component's CIO, this is a CAT II finding. There are multiple sources from which lists of valid DoD CAs and approved ECAs can be obtained: The Global Directory Service (GDS) website provides an online source. The address for this site is https://crl.gds.disa.mil. DoD Public Key Enablement (PKE) Engineering Support maintains the InstallRoot utility to manage DoD supported root certificates on Windows computers, which includes a list of authorized CAs. The utility package can be downloaded from the PKI and PKE Tools page on IASE: http://iase.disa.mil/pki-pke/function_pages/tools.html

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-205647`

### Rule: Windows Server 2019 PKI certificates associated with user accounts must be issued by a DoD PKI or an approved External Certificate Authority (ECA).

**Rule ID:** `SV-205647r569188_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A PKI implementation depends on the practices established by the Certificate Authority (CA) to ensure the implementation is secure. Without proper practices, the certificates issued by a CA have limited value in authentication functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Review user account mappings to PKI certificates. Open "Windows PowerShell". Enter "Get-ADUser -Filter * | FT Name, UserPrincipalName, Enabled". Exclude disabled accounts (e.g., DefaultAccount, Guest) and the krbtgt account. If the User Principal Name (UPN) is not in the format of an individual's identifier for the certificate type and for the appropriate domain suffix, this is a finding. For standard NIPRNet certificates, the individual's identifier is in the format of an Electronic Data Interchange - Personnel Identifier (EDI-PI). Alt Tokens and other certificates may use a different UPN format than the EDI-PI which vary by organization. Verified these with the organization. NIPRNet Example: Name - User Principal Name User1 - 1234567890@mil See PKE documentation for other network domain suffixes. If the mappings are to certificates issued by a CA authorized by the Component's CIO, this is a CAT II finding.

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-205648`

### Rule: Windows Server 2019 must have the DoD Root Certificate Authority (CA) certificates installed in the Trusted Root Store.

**Rule ID:** `SV-205648r921948_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure secure DoD websites and DoD-signed code are properly validated, the system must trust the DoD Root CAs. The DoD root certificates will ensure that the trust chain is established for server certificates issued from the DoD CAs. Satisfies: SRG-OS-000066-GPOS-00034, SRG-OS-000403-GPOS-00182</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Certificates and thumbprints referenced below apply to unclassified systems; refer to PKE documentation for other networks. Open "Windows PowerShell" as an administrator. Execute the following command: Get-ChildItem -Path Cert:Localmachine\root | Where Subject -Like "*DoD*" | FL Subject, Thumbprint, NotAfter If the following certificate "Subject" and "Thumbprint" information is not displayed, this is a finding. Subject: CN=DoD Root CA 3, OU=PKI, OU=DoD, O=U.S. Government, C=US Thumbprint: D73CA91102A2204A36459ED32213B467D7CE97FB NotAfter: 12/30/2029 Subject: CN=DoD Root CA 4, OU=PKI, OU=DoD, O=U.S. Government, C=US Thumbprint: B8269F25DBD937ECAFD4C35A9838571723F2D026 NotAfter: 7/25/2032 Subject: CN=DoD Root CA 5, OU=PKI, OU=DoD, O=U.S. Government, C=US Thumbprint: 4ECB5CC3095670454DA1CBD410FC921F46B8564B NotAfter: 6/14/2041 Subject: CN=DoD Root CA 6, OU=PKI, OU=DoD, O=U.S. Government, C=US Thumbprint: D37ECF61C0B4ED88681EF3630C4E2FC787B37AEF NotAfter: 1/24/2053 11:36:17 AM Alternately, use the Certificates MMC snap-in: Run "MMC". Select "File", "Add/Remove Snap-in". Select "Certificates" and click "Add". Select "Computer account" and click "Next". Select "Local computer: (the computer this console is running on)" and click "Finish". Click "OK". Expand "Certificates" and navigate to "Trusted Root Certification Authorities >> Certificates". Expand "Certificates" and navigate to "Trusted Root Certification Authorities >> Certificates". For each of the DoD Root CA certificates noted below: Right-click on the certificate and select "Open". Select the "Details" tab. Scroll to the bottom and select "Thumbprint". If the DoD Root CA certificates below are not listed or the value for the "Thumbprint" field is not as noted, this is a finding. DoD Root CA 3 Thumbprint: D73CA91102A2204A36459ED32213B467D7CE97FB Valid to: Sunday, December 30, 2029 DoD Root CA 4 Thumbprint: B8269F25DBD937ECAFD4C35A9838571723F2D026 Valid to: Sunday, July 25, 2032 DoD Root CA 5 Thumbprint: 4ECB5CC3095670454DA1CBD410FC921F46B8564B Valid to: Friday, June 14, 2041 DoD Root CA 6 Thumbprint: D37ECF61C0B4ED88681EF3630C4E2FC787B37AEFB Valid to: Friday, January 24, 2053

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-205649`

### Rule: Windows Server 2019 must have the DoD Interoperability Root Certificate Authority (CA) cross-certificates installed in the Untrusted Certificates Store on unclassified systems.

**Rule ID:** `SV-205649r894615_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure users do not experience denial of service when performing certificate-based authentication to DoD websites due to the system chaining to a root other than DoD Root CAs, the DoD Interoperability Root CA cross-certificates must be installed in the Untrusted Certificate Store. This requirement only applies to unclassified systems. Satisfies: SRG-OS-000066-GPOS-00034, SRG-OS-000403-GPOS-00182</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is applicable to unclassified systems. It is NA for others. Open "PowerShell" as an administrator. Execute the following command: Get-ChildItem -Path Cert:Localmachine\disallowed | Where {$_.Issuer -Like "*DoD Interoperability*" -and $_.Subject -Like "*DoD*"} | FL Subject, Issuer, Thumbprint, NotAfter If the following certificate "Subject", "Issuer", and "Thumbprint" information is not displayed, this is a finding. Subject: CN=DoD Root CA 3, OU=PKI, OU=DoD, O=U.S. Government, C=US Issuer: CN=DoD Interoperability Root CA 2, OU=PKI, OU=DoD, O=U.S. Government, C=US Thumbprint: 49CBE933151872E17C8EAE7F0ABA97FB610F6477 NotAfter: 11/16/2024 9:57:16 AM Alternately, use the Certificates MMC snap-in: Run "MMC". Select "File", "Add/Remove Snap-in". Select "Certificates" and click "Add". Select "Computer account" and click "Next". Select "Local computer: (the computer this console is running on)" and click "Finish". Click "OK". Expand "Certificates" and navigate to Untrusted Certificates >> Certificates. For each certificate with "DoD Root CA..." under "Issued To" and "DoD Interoperability Root CA..." under "Issued By": Right-click on the certificate and select "Open". Select the "Details" tab. Scroll to the bottom and select "Thumbprint". If the certificate below is not listed or the value for the "Thumbprint" field is not as noted, this is a finding. Issued to: DoD Root CA 3 Issued By: DoD Interoperability Root CA 2 Thumbprint: 49CBE933151872E17C8EAE7F0ABA97FB610F6477 Valid to: 11/16/2024 9:57:16 AM

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-205650`

### Rule: Windows Server 2019 must have the US DoD CCEB Interoperability Root CA cross-certificates in the Untrusted Certificates Store on unclassified systems.

**Rule ID:** `SV-205650r890530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure users do not experience denial of service when performing certificate-based authentication to DoD websites due to the system chaining to a root other than DoD Root CAs, the US DoD CCEB Interoperability Root CA cross-certificates must be installed in the Untrusted Certificate Store. This requirement only applies to unclassified systems. Satisfies: SRG-OS-000066-GPOS-00034, SRG-OS-000403-GPOS-00182</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is applicable to unclassified systems. It is NA for others. Open "PowerShell" as an administrator. Execute the following command: Get-ChildItem -Path Cert:Localmachine\disallowed | Where Issuer -Like "*CCEB Interoperability*" | FL Subject, Issuer, Thumbprint, NotAfter If the following certificate "Subject", "Issuer", and "Thumbprint" information is not displayed, this is a finding. Subject: CN=DoD Root CA 3, OU=PKI, OU=DoD, O=U.S. Government, C=US Issuer: CN=US DoD CCEB Interoperability Root CA 2, OU=PKI, OU=DoD, O=U.S. Government, C=US Thumbprint: 9B74964506C7ED9138070D08D5F8B969866560C8 NotAfter: 7/18/2025 9:56:22 AM Alternately, use the Certificates MMC snap-in: Run "MMC". Select "File", "Add/Remove Snap-in". Select "Certificates" and click "Add". Select "Computer account" and click "Next". Select "Local computer: (the computer this console is running on)" and click "Finish". Click "OK". Expand "Certificates" and navigate to Untrusted Certificates >> Certificates. For each certificate with "US DoD CCEB Interoperability Root CA ..." under "Issued By": Right-click on the certificate and select "Open". Select the "Details" tab. Scroll to the bottom and select "Thumbprint". If the certificate below is not listed or the value for the "Thumbprint" field is not as noted, this is a finding. Subject: CN=DoD Root CA 3, OU=PKI, OU=DoD, O=U.S. Government, C=US Issuer: CN=US DoD CCEB Interoperability Root CA 2, OU=PKI, OU=DoD, O=U.S. Government, C=US Thumbprint: 9B74964506C7ED9138070D08D5F8B969866560C8 NotAfter: 7/18/2025 9:56:22 AM

## Group: SRG-OS-000067-GPOS-00035

**Group ID:** `V-205651`

### Rule: Windows Server 2019 users must be required to enter a password to access private keys stored on the computer.

**Rule ID:** `SV-205651r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the private key is discovered, an attacker can use the key to authenticate as an authorized user and gain access to the network infrastructure. The cornerstone of the PKI is the private key used to encrypt or digitally sign information. If the private key is stolen, this will lead to the compromise of the authentication and non-repudiation gained through PKI because the attacker can use the private key to digitally sign documents and pretend to be the authorized user. Both the holders of a digital certificate and the issuing authority must protect the computers, storage devices, or whatever they use to keep the private keys.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Cryptography\ Value Name: ForceKeyProtection Type: REG_DWORD Value: 0x00000002 (2)

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-205652`

### Rule: Windows Server 2019 must have the built-in Windows password complexity policy enabled.

**Rule ID:** `SV-205652r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of complex passwords increases their strength against attack. The built-in Windows password complexity policy requires passwords to contain at least three of the four types of characters (numbers, uppercase and lowercase letters, and special characters) and prevents the inclusion of user names or parts of user names. Satisfies: SRG-OS-000069-GPOS-00037, SRG-OS-000070-GPOS-00038, SRG-OS-000071-GPOS-00039, SRG-OS-000266-GPOS-00101</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Account Policies >> Password Policy. If the value for "Password must meet complexity requirements" is not set to "Enabled", this is a finding. For server core installations, run the following command: Secedit /Export /Areas SecurityPolicy /CFG C:\Path\FileName.Txt If "PasswordComplexity" equals "0" in the file, this is a finding. Note: If an external password filter is in use that enforces all four character types and requires this setting to be set to "Disabled", this would not be considered a finding. If this setting does not affect the use of an external password filter, it must be enabled for fallback purposes.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-205653`

### Rule: Windows Server 2019 reversible password encryption must be disabled.

**Rule ID:** `SV-205653r877397_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Storing passwords using reversible encryption is essentially the same as storing clear-text versions of the passwords, which are easily compromised. For this reason, this policy must never be enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Account Policies >> Password Policy. If the value for "Store passwords using reversible encryption" is not set to "Disabled", this is a finding. For server core installations, run the following command: Secedit /Export /Areas SecurityPolicy /CFG C:\Path\FileName.Txt If "ClearTextPassword" equals "1" in the file, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-205654`

### Rule: Windows Server 2019 must be configured to prevent the storage of the LAN Manager hash of passwords.

**Rule ID:** `SV-205654r877397_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The LAN Manager hash uses a weak encryption algorithm and there are several tools available that use this hash to retrieve account passwords. This setting controls whether a LAN Manager hash of the password is stored in the SAM the next time the password is changed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\ Value Name: NoLMHash Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-205655`

### Rule: Windows Server 2019 unencrypted passwords must not be sent to third-party Server Message Block (SMB) servers.

**Rule ID:** `SV-205655r877396_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some non-Microsoft SMB servers only support unencrypted (plain-text) password authentication. Sending plain-text passwords across the network when authenticating to an SMB server reduces the overall security of the environment. Check with the vendor of the SMB server to determine if there is a way to support encrypted password authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters\ Value Name: EnablePlainTextPassword Value Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-205656`

### Rule: Windows Server 2019 minimum password age must be configured to at least one day.

**Rule ID:** `SV-205656r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Permitting passwords to be changed in immediate succession within the same day allows users to cycle passwords through their history database. This enables users to effectively negate the purpose of mandating periodic password changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Account Policies >> Password Policy. If the value for the "Minimum password age" is set to "0" days ("Password can be changed immediately"), this is a finding. For server core installations, run the following command: Secedit /Export /Areas SecurityPolicy /CFG C:\Path\FileName.Txt If "MinimumPasswordAge" equals "0" in the file, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-205657`

### Rule: Windows Server 2019 passwords for the built-in Administrator account must be changed at least every 60 days.

**Rule ID:** `SV-205657r953815_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The longer a password is in use, the greater the opportunity for someone to gain unauthorized knowledge of the password. The built-in Administrator account is not generally used and its password might not be changed as frequently as necessary. Changing the password for the built-in Administrator account on a regular basis will limit its exposure. Windows LAPS must be used to change the built-in Administrator account password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If there are no enabled local Administrator accounts, this is Not Applicable. Review the password last set date for the enabled local Administrator account. On the stand alone or domain-joined workstation: Open "PowerShell". Enter "Get-LocalUser -Name * | Select-Object *". If the "PasswordLastSet" date is greater than "60" days old for the local Administrator account for administering the computer/domain, this is a finding. Verify LAPS is configured and operational. Navigate to Local Computer Policy >> Computer Configuration >> Administrative Templates >> System >> LAPS >> Password Settings >> Set to enabled. Password Complexity, large letters + small letters + numbers + special, Password Length 14, Password Age 60. If not configured as shown, this is a finding. Navigate to Local Computer Policy >> Computer Configuration >> Administrative Templates >> System >> LAPS >> Password Settings >> Name of administrator Account to manage >> Set to enabled >> Administrator account name is populated. If it is not, this is a finding. Verify LAPS Operational logs >> Event Viewer >> Applications and Services Logs >> Microsoft >> Windows >> LAPS >> Operational. Verify LAPS policy process is completing. If it is not, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-205658`

### Rule: Windows Server 2019 passwords must be configured to expire.

**Rule ID:** `SV-205658r857297_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords that do not expire or are reused increase the exposure of a password with greater probability of being discovered or cracked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the password never expires status for enabled user accounts. Open "PowerShell". Domain Controllers: Enter "Search-ADAccount -PasswordNeverExpires -UsersOnly | FT Name, PasswordNeverExpires, Enabled". Exclude application accounts, disabled accounts (e.g., DefaultAccount, Guest) and the krbtgt account. If any enabled user accounts are returned with a "PasswordNeverExpires" status of "True", this is a finding. Member servers and standalone or nondomain-joined systems: Enter 'Get-CimInstance -Class Win32_Useraccount -Filter "PasswordExpires=False and LocalAccount=True" | FT Name, PasswordExpires, Disabled, LocalAccount'. Exclude application accounts and disabled accounts (e.g., DefaultAccount, Guest). If any enabled user accounts are returned with a "PasswordExpires" status of "False", this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-205659`

### Rule: Windows Server 2019 maximum password age must be configured to 60 days or less.

**Rule ID:** `SV-205659r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The longer a password is in use, the greater the opportunity for someone to gain unauthorized knowledge of the passwords. Scheduled changing of passwords hinders the ability of unauthorized system users to crack passwords and gain access to a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Account Policies >> Password Policy. If the value for the "Maximum password age" is greater than "60" days, this is a finding. If the value is set to "0" (never expires), this is a finding. For server core installations, run the following command: Secedit /Export /Areas SecurityPolicy /CFG C:\Path\FileName.Txt If "MaximumPasswordAge" is greater than "60" or equal to "0" in the file, this is a finding.

## Group: SRG-OS-000077-GPOS-00045

**Group ID:** `V-205660`

### Rule: Windows Server 2019 password history must be configured to 24 passwords remembered.

**Rule ID:** `SV-205660r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A system is more vulnerable to unauthorized access when system users recycle the same password several times without being required to change to a unique password on a regularly scheduled basis. This enables users to effectively negate the purpose of mandating periodic password changes. The default value is "24" for Windows domain systems. DoD has decided this is the appropriate value for all Windows systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Account Policies >> Password Policy. If the value for "Enforce password history" is less than "24" passwords remembered, this is a finding. For server core installations, run the following command: Secedit /Export /Areas SecurityPolicy /CFG C:\Path\FileName.Txt If "PasswordHistorySize" is less than "24" in the file, this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-205661`

### Rule: Windows Server 2019 manually managed application account passwords must be at least 14 characters in length.

**Rule ID:** `SV-205661r953816_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application/service account passwords must be of sufficient length to prevent being easily cracked. Application/service accounts that are manually managed must have passwords at least 14 characters in length.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if manually managed application/service accounts exist. If none exist, this is NA. Verify the organization has a policy to ensure passwords for manually managed application/service accounts are at least 14 characters in length. If such a policy does not exist or has not been implemented, this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-205662`

### Rule: Windows Server 2019 minimum password length must be configured to 14 characters.

**Rule ID:** `SV-205662r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems not protected with strong password schemes (including passwords of minimum length) provide the opportunity for anyone to crack the password, thus gaining access to the system and compromising the device, information, or the local network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Account Policies >> Password Policy. If the value for the "Minimum password length," is less than "14" characters, this is a finding. For server core installations, run the following command: Secedit /Export /Areas SecurityPolicy /CFG C:\Path\FileName.Txt If "MinimumPasswordLength" is less than "14" in the file, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-205663`

### Rule: Windows Server 2019 local volumes must use a format that supports NTFS attributes.

**Rule ID:** `SV-205663r569188_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The ability to set access permissions and auditing is critical to maintaining the security and proper access controls of a system. To support this, volumes must be formatted using a file system that supports NTFS attributes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open "Computer Management". Select "Disk Management" under "Storage". For each local volume, if the file system does not indicate "NTFS", this is a finding. "ReFS" (resilient file system) is also acceptable and would not be a finding. This does not apply to system partitions such the Recovery and EFI System Partition.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-205664`

### Rule: Windows Server 2019 non-administrative accounts or groups must only have print permissions on printer shares.

**Rule ID:** `SV-205664r569188_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Windows shares are a means by which files, folders, printers, and other resources can be published for network users to access. Improper configuration can permit access to devices and data beyond a user's need.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open "Printers & scanners" in "Settings". If there are no printers configured, this is NA. (Exclude Microsoft Print to PDF and Microsoft XPS Document Writer, which do not support sharing.) For each printer: Select the printer and "Manage". Select "Printer Properties". Select the "Sharing" tab. If "Share this printer" is checked, select the "Security" tab. If any standard user accounts or groups have permissions other than "Print", this is a finding. The default is for the "Everyone" group to be given "Print" permission. "All APPLICATION PACKAGES" and "CREATOR OWNER" are not standard user accounts.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-205665`

### Rule: Windows Server 2019 Access this computer from the network user right must only be assigned to the Administrators, Authenticated Users, and 
Enterprise Domain Controllers groups on domain controllers.

**Rule ID:** `SV-205665r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Access this computer from the network" right may access resources on the system, and this right must be limited to those requiring it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Access this computer from the network" right, this is a finding. - Administrators - Authenticated Users - Enterprise Domain Controllers For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeNetworkLogonRight" user right, this is a finding. S-1-5-32-544 (Administrators) S-1-5-11 (Authenticated Users) S-1-5-9 (Enterprise Domain Controllers) If an application requires this user right, this would not be a finding. Vendor documentation must support the requirement for having the user right. The requirement must be documented with the ISSO. The application account must meet requirements for application account passwords, such as length (WN19-00-000050) and required frequency of changes (WN19-00-000060).

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-205666`

### Rule: Windows Server 2019 Allow log on through Remote Desktop Services user right must only be assigned to the Administrators group on domain controllers.

**Rule ID:** `SV-205666r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Allow log on through Remote Desktop Services" user right can access a system through Remote Desktop.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers, it is NA for other systems. Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Allow log on through Remote Desktop Services" user right, this is a finding. - Administrators For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeRemoteInteractiveLogonRight" user right, this is a finding. S-1-5-32-544 (Administrators)

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-205667`

### Rule: Windows Server 2019 Deny access to this computer from the network user right on domain controllers must be configured to prevent unauthenticated access.

**Rule ID:** `SV-205667r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Deny access to this computer from the network" user right defines the accounts that are prevented from logging on from the network. The Guests group must be assigned this right to prevent unauthenticated access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. A separate version applies to other systems. Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If the following accounts or groups are not defined for the "Deny access to this computer from the network" user right, this is a finding: - Guests Group For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If the following SIDs are not defined for the "SeDenyNetworkLogonRight" user right, this is a finding. S-1-5-32-546 (Guests)

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-205668`

### Rule: Windows Server 2019 Deny log on as a batch job user right on domain controllers must be configured to prevent unauthenticated access.

**Rule ID:** `SV-205668r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Deny log on as a batch job" user right defines accounts that are prevented from logging on to the system as a batch job, such as Task Scheduler. The Guests group must be assigned to prevent unauthenticated access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. A separate version applies to other systems. Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If the following accounts or groups are not defined for the "Deny log on as a batch job" user right, this is a finding: - Guests Group For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If the following SID(s) are not defined for the "SeDenyBatchLogonRight" user right, this is a finding: S-1-5-32-546 (Guests)

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-205669`

### Rule: Windows Server 2019 Deny log on as a service user right must be configured to include no accounts or groups (blank) on domain controllers.

**Rule ID:** `SV-205669r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Deny log on as a service" user right defines accounts that are denied logon as a service. Incorrect configurations could prevent services from starting and result in a denial of service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. A separate version applies to other systems. Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups are defined for the "Deny log on as a service" user right, this is a finding. For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs are granted the "SeDenyServiceLogonRight" user right, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-205670`

### Rule: Windows Server 2019 Deny log on locally user right on domain controllers must be configured to prevent unauthenticated access.

**Rule ID:** `SV-205670r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Deny log on locally" user right defines accounts that are prevented from logging on interactively. The Guests group must be assigned this right to prevent unauthenticated access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. A separate version applies to other systems. Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If the following accounts or groups are not defined for the "Deny log on locally" user right, this is a finding: - Guests Group For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If the following SID(s) are not defined for the "SeDenyInteractiveLogonRight" user right, this is a finding: S-1-5-32-546 (Guests)

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-205671`

### Rule: Windows Server 2019 "Access this computer from the network" user right must only be assigned to the Administrators and Authenticated Users groups on domain-joined member servers and standalone or nondomain-joined systems.

**Rule ID:** `SV-205671r857331_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Access this computer from the network" user right may access resources on the system, and this right must be limited to those requiring it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to member servers and standalone or nondomain-joined systems. A separate version applies to domain controllers. Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Access this computer from the network" user right, this is a finding: - Administrators - Authenticated Users For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeNetworkLogonRight" user right, this is a finding: S-1-5-32-544 (Administrators) S-1-5-11 (Authenticated Users) If an application requires this user right, this would not be a finding. Vendor documentation must support the requirement for having the user right. The requirement must be documented with the ISSO. The application account must meet requirements for application account passwords, such as length (WN19-00-000050) and required frequency of changes (WN19-00-000060).

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-205672`

### Rule: Windows Server 2019 "Deny access to this computer from the network" user right on domain-joined member servers must be configured to prevent access from highly privileged domain accounts and local accounts and from unauthenticated access on all systems.

**Rule ID:** `SV-205672r857333_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Deny access to this computer from the network" user right defines the accounts that are prevented from logging on from the network. In an Active Directory Domain, denying logons to the Enterprise Admins and Domain Admins groups on lower-trust systems helps mitigate the risk of privilege escalation from credential theft attacks, which could lead to the compromise of an entire domain. Local accounts on domain-joined systems must also be assigned this right to decrease the risk of lateral movement resulting from credential theft attacks. The Guests group must be assigned this right to prevent unauthenticated access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to member servers and standalone or nondomain-joined systems. A separate version applies to domain controllers. Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If the following accounts or groups are not defined for the "Deny access to this computer from the network" user right, this is a finding: Domain Systems Only: - Enterprise Admins group - Domain Admins group - "Local account and member of Administrators group" or "Local account" (see Note below) All Systems: - Guests group For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If the following SIDs are not defined for the "SeDenyNetworkLogonRight" user right, this is a finding. Domain Systems Only: S-1-5-root domain-519 (Enterprise Admins) S-1-5-domain-512 (Domain Admins) S-1-5-114 ("Local account and member of Administrators group") or S-1-5-113 ("Local account") All Systems: S-1-5-32-546 (Guests) Note: These are built-in security groups. "Local account" is more restrictive but may cause issues on servers such as systems that provide failover clustering.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-205673`

### Rule: Windows Server 2019 "Deny log on as a batch job" user right on domain-joined member servers must be configured to prevent access from highly privileged domain accounts and from unauthenticated access on all systems.

**Rule ID:** `SV-205673r857335_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Deny log on as a batch job" user right defines accounts that are prevented from logging on to the system as a batch job, such as Task Scheduler. In an Active Directory Domain, denying logons to the Enterprise Admins and Domain Admins groups on lower-trust systems helps mitigate the risk of privilege escalation from credential theft attacks, which could lead to the compromise of an entire domain. The Guests group must be assigned to prevent unauthenticated access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to member servers and standalone or nondomain-joined systems. A separate version applies to domain controllers. Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If the following accounts or groups are not defined for the "Deny log on as a batch job" user right, this is a finding: Domain Systems Only: - Enterprise Admins Group - Domain Admins Group All Systems: - Guests Group For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If the following SIDs are not defined for the "SeDenyBatchLogonRight" user right, this is a finding. Domain Systems Only: S-1-5-root domain-519 (Enterprise Admins) S-1-5-domain-512 (Domain Admins) All Systems: S-1-5-32-546 (Guests)

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-205674`

### Rule: Windows Server 2019 "Deny log on as a service" user right on domain-joined member servers must be configured to prevent access from highly privileged domain accounts. No other groups or accounts must be assigned this right.

**Rule ID:** `SV-205674r891848_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Deny log on as a service" user right defines accounts that are denied logon as a service. In an Active Directory Domain, denying logons to the Enterprise Admins and Domain Admins groups on lower-trust systems helps mitigate the risk of privilege escalation from credential theft attacks, which could lead to the compromise of an entire domain. Incorrect configurations could prevent services from starting and result in a denial of service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to member servers only. A separate version applies to domain controllers. Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If the following accounts or groups are not defined for the "Deny log on as a service" user right on domain-joined systems, this is a finding: - Enterprise Admins Group - Domain Admins Group If any accounts or groups are defined for the "Deny log on as a service" user right on nondomain-joined systems, this is a finding. For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If the following SIDs are not defined for the "SeDenyServiceLogonRight" user right on domain-joined systems, this is a finding: S-1-5-root domain-519 (Enterprise Admins) S-1-5-domain-512 (Domain Admins) If any SIDs are defined for the user right, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-205675`

### Rule: Windows Server 2019 "Deny log on locally" user right on domain-joined member servers must be configured to prevent access from highly privileged domain accounts and from unauthenticated access on all systems.

**Rule ID:** `SV-205675r857337_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Deny log on locally" user right defines accounts that are prevented from logging on interactively. In an Active Directory Domain, denying logons to the Enterprise Admins and Domain Admins groups on lower-trust systems helps mitigate the risk of privilege escalation from credential theft attacks, which could lead to the compromise of an entire domain. The Guests group must be assigned this right to prevent unauthenticated access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to member servers and standalone or nondomain-joined systems. A separate version applies to domain controllers. Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If the following accounts or groups are not defined for the "Deny log on locally" user right, this is a finding: Domain Systems Only: - Enterprise Admins Group - Domain Admins Group All Systems: - Guests Group For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If the following SIDs are not defined for the "SeDenyInteractiveLogonRight" user right, this is a finding: Domain Systems Only: S-1-5-root domain-519 (Enterprise Admins) S-1-5-domain-512 (Domain Admins) All Systems: S-1-5-32-546 (Guests)

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-205676`

### Rule: Windows Server 2019 Allow log on locally user right must only be assigned to the Administrators group.

**Rule ID:** `SV-205676r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Allow log on locally" user right can log on interactively to a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Allow log on locally" user right, this is a finding: - Administrators For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeInteractiveLogonRight" user right, this is a finding: S-1-5-32-544 (Administrators) If an application requires this user right, this would not be a finding. Vendor documentation must support the requirement for having the user right. The requirement must be documented with the ISSO. The application account must meet requirements for application account passwords, such as length (WN19-00-000050) and required frequency of changes (WN19-00-000060).

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-205677`

### Rule: Windows Server 2019 must have the roles and features required by the system documented.

**Rule ID:** `SV-205677r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unnecessary roles and features increase the attack surface of a system. Limiting roles and features of a system to only those necessary reduces this potential. The standard installation option (previously called Server Core) further reduces this when selected at installation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Required roles and features will vary based on the function of the individual system. Roles and features specifically required to be disabled per the STIG are identified in separate requirements. If the organization has not documented the roles and features required for the system(s), this is a finding. The PowerShell command "Get-WindowsFeature" will list all roles and features with an "Install State".

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-205678`

### Rule: Windows Server 2019 must not have the Fax Server role installed.

**Rule ID:** `SV-205678r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unnecessary services increase the attack surface of a system. Some of these services may not support required levels of authentication or encryption or may provide unauthorized access to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open "PowerShell". Enter "Get-WindowsFeature | Where Name -eq Fax". If "Installed State" is "Installed", this is a finding. An Installed State of "Available" or "Removed" is not a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-205679`

### Rule: Windows Server 2019 must not have the Peer Name Resolution Protocol installed.

**Rule ID:** `SV-205679r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unnecessary services increase the attack surface of a system. Some of these services may not support required levels of authentication or encryption or may provide unauthorized access to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open "PowerShell". Enter "Get-WindowsFeature | Where Name -eq PNRP". If "Installed State" is "Installed", this is a finding. An Installed State of "Available" or "Removed" is not a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-205680`

### Rule: Windows Server 2019 must not have Simple TCP/IP Services installed.

**Rule ID:** `SV-205680r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unnecessary services increase the attack surface of a system. Some of these services may not support required levels of authentication or encryption or may provide unauthorized access to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open "PowerShell". Enter "Get-WindowsFeature | Where Name -eq Simple-TCPIP". If "Installed State" is "Installed", this is a finding. An Installed State of "Available" or "Removed" is not a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-205681`

### Rule: Windows Server 2019 must not have the TFTP Client installed.

**Rule ID:** `SV-205681r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unnecessary services increase the attack surface of a system. Some of these services may not support required levels of authentication or encryption or may provide unauthorized access to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open "PowerShell". Enter "Get-WindowsFeature | Where Name -eq TFTP-Client". If "Installed State" is "Installed", this is a finding. An Installed State of "Available" or "Removed" is not a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-205682`

### Rule: Windows Server 2019 must not have the Server Message Block (SMB) v1 protocol installed.

**Rule ID:** `SV-205682r819711_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SMBv1 is a legacy protocol that uses the MD5 algorithm as part of SMB. MD5 is known to be vulnerable to a number of attacks such as collision and preimage attacks and is not FIPS compliant.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Different methods are available to disable SMBv1 on Windows Server 2019. This is the preferred method; however, if WN19-00-000390 and WN19-00-000400 are configured, this is NA. Open "Windows PowerShell" with elevated privileges (run as administrator). Enter "Get-WindowsFeature -Name FS-SMB1". If "Installed State" is "Installed", this is a finding. An Installed State of "Available" or "Removed" is not a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-205683`

### Rule: Windows Server 2019 must have the Server Message Block (SMB) v1 protocol disabled on the SMB server.

**Rule ID:** `SV-205683r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SMBv1 is a legacy protocol that uses the MD5 algorithm as part of SMB. MD5 is known to be vulnerable to a number of attacks such as collision and preimage attacks as well as not being FIPS compliant.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Different methods are available to disable SMBv1 on Windows Server 2019, if WN19-00-000380 is configured, this is NA. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters\ Value Name: SMB1 Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-205684`

### Rule: Windows Server 2019 must have the Server Message Block (SMB) v1 protocol disabled on the SMB client.

**Rule ID:** `SV-205684r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SMBv1 is a legacy protocol that uses the MD5 algorithm as part of SMB. MD5 is known to be vulnerable to a number of attacks such as collision and preimage attacks as well as not being FIPS compliant.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Different methods are available to disable SMBv1 on Windows Server 2019, if WN19-00-000380 is configured, this is NA. If the following registry value is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\mrxsmb10\ Value Name: Start Type: REG_DWORD Value: 0x00000004 (4)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-205685`

### Rule: Windows Server 2019 must not have Windows PowerShell 2.0 installed.

**Rule ID:** `SV-205685r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Windows PowerShell 5.x added advanced logging features that can provide additional detail when malware has been run on a system. Disabling the Windows PowerShell 2.0 mitigates against a downgrade attack that evades the Windows PowerShell 5.x script block logging feature.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open "PowerShell". Enter "Get-WindowsFeature | Where Name -eq PowerShell-v2". If "Installed State" is "Installed", this is a finding. An Installed State of "Available" or "Removed" is not a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-205686`

### Rule: Windows Server 2019 must prevent the display of slide shows on the lock screen.

**Rule ID:** `SV-205686r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Slide shows that are displayed on the lock screen could display sensitive information to unauthorized personnel. Turning off this feature will limit access to the information to a logged-on user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the registry value below. If it does not exist or is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\Personalization\ Value Name: NoLockScreenSlideshow Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-205687`

### Rule: Windows Server 2019 must have WDigest Authentication disabled.

**Rule ID:** `SV-205687r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When the WDigest Authentication protocol is enabled, plain-text passwords are stored in the Local Security Authority Subsystem Service (LSASS), exposing them to theft. WDigest is disabled by default in Windows Server 2019. This setting ensures this is enforced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\SecurityProviders\Wdigest\ Value Name: UseLogonCredential Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-205688`

### Rule: Windows Server 2019 downloading print driver packages over HTTP must be turned off.

**Rule ID:** `SV-205688r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some features may communicate with the vendor, sending system information or downloading data or components for the feature. Turning off this capability will prevent potentially sensitive information from being sent outside the enterprise and will prevent uncontrolled updates to the system. This setting prevents the computer from downloading print driver packages over HTTP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows NT\Printers\ Value Name: DisableWebPnPDownload Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-205689`

### Rule: Windows Server 2019 printing over HTTP must be turned off.

**Rule ID:** `SV-205689r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some features may communicate with the vendor, sending system information or downloading data or components for the feature. Turning off this capability will prevent potentially sensitive information from being sent outside the enterprise and will prevent uncontrolled updates to the system. This setting prevents the client computer from printing over HTTP, which allows the computer to print to printers on the intranet as well as the Internet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows NT\Printers\ Value Name: DisableHTTPPrinting Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-205690`

### Rule: Windows Server 2019 network selection user interface (UI) must not be displayed on the logon screen.

**Rule ID:** `SV-205690r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling interaction with the network selection UI allows users to change connections to available networks without signing in to Windows.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the registry value below. If it does not exist or is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\System\ Value Name: DontDisplayNetworkSelectionUI Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-205691`

### Rule: Windows Server 2019 Application Compatibility Program Inventory must be prevented from collecting data and sending the information to Microsoft.

**Rule ID:** `SV-205691r569188_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Some features may communicate with the vendor, sending system information or downloading data or components for the feature. Turning off this capability will prevent potentially sensitive information from being sent outside the enterprise and will prevent uncontrolled updates to the system. This setting will prevent the Program Inventory from collecting data about a system and sending the information to Microsoft.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\AppCompat\ Value Name: DisableInventory Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-205692`

### Rule: Windows Server 2019 Windows Defender SmartScreen must be enabled.

**Rule ID:** `SV-205692r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Windows Defender SmartScreen helps protect systems from programs downloaded from the internet that may be malicious. Enabling SmartScreen can block potentially malicious programs or warn users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is applicable to unclassified systems; for other systems, this is NA. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\System\ Value Name: EnableSmartScreen Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-205693`

### Rule: Windows Server 2019 must disable Basic authentication for RSS feeds over HTTP.

**Rule ID:** `SV-205693r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Basic authentication uses plain-text passwords that could be used to compromise a system. Disabling Basic authentication will reduce this potential.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default behavior is for the Windows RSS platform to not use Basic authentication over HTTP connections. If the registry value name below does not exist, this is not a finding. If it exists and is configured with a value of "0", this is not a finding. If it exists and is configured with a value of "1", this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Internet Explorer\Feeds\ Value Name: AllowBasicAuthInClear Value Type: REG_DWORD Value: 0x00000000 (0) (or if the Value Name does not exist)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-205694`

### Rule: Windows Server 2019 must prevent Indexing of encrypted files.

**Rule ID:** `SV-205694r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Indexing of encrypted files may expose sensitive data. This setting prevents encrypted files from being indexed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\Windows Search\ Value Name: AllowIndexingEncryptedStoresOrItems Value Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-205695`

### Rule: Windows Server 2019 domain controllers must run on a machine dedicated to that function.

**Rule ID:** `SV-205695r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Executing application servers on the same host machine with a directory server may substantially weaken the security of the directory server. Web or database server applications usually require the addition of many programs and accounts, increasing the attack surface of the computer. Some applications require the addition of privileged accounts, providing potential sources of compromise. Some applications (such as Microsoft Exchange) may require the use of network ports or services conflicting with the directory server. In this case, non-standard ports might be selected, and this could interfere with intrusion detection or prevention services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers, it is NA for other systems. Review the installed roles the domain controller is supporting. Start "Server Manager". Select "AD DS" in the left pane and the server name under "Servers" to the right. Select "Add (or Remove) Roles and Features" from "Tasks" in the "Roles and Features" section. (Cancel before any changes are made.) Determine if any additional server roles are installed. A basic domain controller setup will include the following: - Active Directory Domain Services - DNS Server - File and Storage Services If any roles not requiring installation on a domain controller are installed, this is a finding. A Domain Name System (DNS) server integrated with the directory server (e.g., AD-integrated DNS) is an acceptable application. However, the DNS server must comply with the DNS STIG security requirements. Run "Programs and Features". Review installed applications. If any applications are installed that are not required for the domain controller, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-205696`

### Rule: Windows Server 2019 local users on domain-joined member servers must not be enumerated.

**Rule ID:** `SV-205696r857322_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The username is one part of logon credentials that could be used to gain access to a system. Preventing the enumeration of users limits this information to authorized personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to member servers. For domain controllers and standalone or nondomain-joined systems, this is NA. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\System\ Value Name: EnumerateLocalUsers Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-205697`

### Rule: Windows Server 2019 must not have the Microsoft FTP service installed unless required by the organization.

**Rule ID:** `SV-205697r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unnecessary services increase the attack surface of a system. Some of these services may not support required levels of authentication or encryption.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the server has the role of an FTP server, this is NA. Open "PowerShell". Enter "Get-WindowsFeature | Where Name -eq Web-Ftp-Service". If "Installed State" is "Installed", this is a finding. An Installed State of "Available" or "Removed" is not a finding. If the system has the role of an FTP server, this must be documented with the ISSO.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-205698`

### Rule: Windows Server 2019 must not have the Telnet Client installed.

**Rule ID:** `SV-205698r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unnecessary services increase the attack surface of a system. Some of these services may not support required levels of authentication or encryption or may provide unauthorized access to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open "PowerShell". Enter "Get-WindowsFeature | Where Name -eq Telnet-Client". If "Installed State" is "Installed", this is a finding. An Installed State of "Available" or "Removed" is not a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-205699`

### Rule: Windows Server 2019 shared user accounts must not be permitted.

**Rule ID:** `SV-205699r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Shared accounts (accounts where two or more people log on with the same user identification) do not provide adequate identification and authentication. There is no way to provide for nonrepudiation or individual accountability for system access and resource usage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine whether any shared accounts exist. If no shared accounts exist, this is NA. Shared accounts, such as required by an application, may be approved by the organization. This must be documented with the ISSO. Documentation must include the reason for the account, who has access to the account, and how the risk of using the shared account is mitigated to include monitoring account activity. If unapproved shared accounts exist, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-205700`

### Rule: Windows Server 2019 accounts must require passwords.

**Rule ID:** `SV-205700r857294_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The lack of password protection enables anyone to gain access to the information system, which opens a backdoor opportunity for intruders to compromise the system as well as other resources. Accounts on a system must require passwords.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the password required status for enabled user accounts. Open "PowerShell". Domain Controllers: Enter "Get-Aduser -Filter * -Properties Passwordnotrequired |FT Name, Passwordnotrequired, Enabled". Exclude disabled accounts (e.g., DefaultAccount, Guest) and Trusted Domain Objects (TDOs). If "Passwordnotrequired" is "True" or blank for any enabled user account, this is a finding. Member servers and standalone or nondomain-joined systems: Enter 'Get-CimInstance -Class Win32_Useraccount -Filter "PasswordRequired=False and LocalAccount=True" | FT Name, PasswordRequired, Disabled, LocalAccount'. Exclude disabled accounts (e.g., DefaultAccount, Guest). If any enabled user accounts are returned with a "PasswordRequired" status of "False", this is a finding.

## Group: SRG-OS-000105-GPOS-00052

**Group ID:** `V-205701`

### Rule: Windows Server 2019 Active Directory user accounts, including administrators, must be configured to require the use of a Common Access Card (CAC), Personal Identity Verification (PIV)-compliant hardware token, or Alternate Logon Token (ALT) for user authentication.

**Rule ID:** `SV-205701r860029_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Smart cards such as the CAC support a two-factor authentication technique. This provides a higher level of trust in the asserted identity than use of the username and password for authentication. Satisfies: SRG-OS-000105-GPOS-00052, SRG-OS-000106-GPOS-00053, SRG-OS-000107-GPOS-00054, SRG-OS-000108-GPOS-00055, SRG-OS-000375-GPOS-00160</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Open "PowerShell". Enter the following: "Get-ADUser -Filter {(Enabled -eq $True) -and (SmartcardLogonRequired -eq $False)} | FT Name" ("DistinguishedName" may be substituted for "Name" for more detailed output.) If any user accounts, including administrators, are listed, this is a finding. Alternately: To view sample accounts in "Active Directory Users and Computers" (available from various menus or run "dsa.msc"): Select the Organizational Unit (OU) where the user accounts are located. (By default, this is the Users node; however, accounts may be under other organization-defined OUs.) Right-click the sample user account and select "Properties". Select the "Account" tab. If any user accounts, including administrators, do not have "Smart card is required for interactive logon" checked in the "Account Options" area, this is a finding.

## Group: SRG-OS-000112-GPOS-00057

**Group ID:** `V-205702`

### Rule: Windows Server 2019 Kerberos user logon restrictions must be enforced.

**Rule ID:** `SV-205702r852424_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy setting determines whether the Kerberos Key Distribution Center (KDC) validates every request for a session ticket against the user rights policy of the target computer. The policy is enabled by default, which is the most secure setting for validating that access to target resources is not circumvented. Satisfies: SRG-OS-000112-GPOS-00057, SRG-OS-000113-GPOS-00058</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Verify the following is configured in the Default Domain Policy: Open "Group Policy Management". Navigate to "Group Policy Objects" in the Domain being reviewed (Forest >> Domains >> Domain). Right-click on the "Default Domain Policy". Select "Edit". Navigate to Computer Configuration >> Policies >> Windows Settings >> Security Settings >> Account Policies >> Kerberos Policy. If the "Enforce user logon restrictions" is not set to "Enabled", this is a finding.

## Group: SRG-OS-000112-GPOS-00057

**Group ID:** `V-205703`

### Rule: Windows Server 2019 Kerberos service ticket maximum lifetime must be limited to 600 minutes or less.

**Rule ID:** `SV-205703r852425_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting determines the maximum amount of time (in minutes) that a granted session ticket can be used to access a particular service. Session tickets are used only to authenticate new connections with servers. Ongoing operations are not interrupted if the session ticket used to authenticate the connection expires during the connection. Satisfies: SRG-OS-000112-GPOS-00057, SRG-OS-000113-GPOS-00058</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Verify the following is configured in the Default Domain Policy: Open "Group Policy Management". Navigate to "Group Policy Objects" in the Domain being reviewed (Forest >> Domains >> Domain). Right-click on the "Default Domain Policy". Select "Edit". Navigate to Computer Configuration >> Policies >> Windows Settings >> Security Settings >> Account Policies >> Kerberos Policy. If the value for "Maximum lifetime for service ticket" is "0" or greater than "600" minutes, this is a finding.

## Group: SRG-OS-000112-GPOS-00057

**Group ID:** `V-205704`

### Rule: Windows Server 2019 Kerberos user ticket lifetime must be limited to 10 hours or less.

**Rule ID:** `SV-205704r852426_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In Kerberos, there are two types of tickets: Ticket Granting Tickets (TGTs) and Service Tickets. Kerberos tickets have a limited lifetime so the time an attacker has to implement an attack is limited. This policy controls how long TGTs can be renewed. With Kerberos, the user's initial authentication to the domain controller results in a TGT, which is then used to request Service Tickets to resources. Upon startup, each computer gets a TGT before requesting a service ticket to the domain controller and any other computers it needs to access. For services that start up under a specified user account, users must always get a TGT first and then get Service Tickets to all computers and services accessed. Satisfies: SRG-OS-000112-GPOS-00057, SRG-OS-000113-GPOS-00058</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Verify the following is configured in the Default Domain Policy: Open "Group Policy Management". Navigate to "Group Policy Objects" in the Domain being reviewed (Forest >> Domains >> Domain). Right-click on the "Default Domain Policy". Select "Edit". Navigate to Computer Configuration >> Policies >> Windows Settings >> Security Settings >> Account Policies >> Kerberos Policy. If the value for "Maximum lifetime for user ticket" is "0" or greater than "10" hours, this is a finding.

## Group: SRG-OS-000112-GPOS-00057

**Group ID:** `V-205705`

### Rule: Windows Server 2019 Kerberos policy user ticket renewal maximum lifetime must be limited to seven days or less.

**Rule ID:** `SV-205705r852427_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting determines the period of time (in days) during which a user's Ticket Granting Ticket (TGT) may be renewed. This security configuration limits the amount of time an attacker has to crack the TGT and gain access. Satisfies: SRG-OS-000112-GPOS-00057, SRG-OS-000113-GPOS-00058</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Verify the following is configured in the Default Domain Policy: Open "Group Policy Management". Navigate to "Group Policy Objects" in the Domain being reviewed (Forest >> Domains >> Domain). Right-click on the "Default Domain Policy". Select "Edit". Navigate to Computer Configuration >> Policies >> Windows Settings >> Security Settings >> Account Policies >> Kerberos Policy. If the "Maximum lifetime for user ticket renewal" is greater than "7" days, this is a finding.

## Group: SRG-OS-000112-GPOS-00057

**Group ID:** `V-205706`

### Rule: Windows Server 2019 computer clock synchronization tolerance must be limited to five minutes or less.

**Rule ID:** `SV-205706r852428_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting determines the maximum time difference (in minutes) that Kerberos will tolerate between the time on a client's clock and the time on a server's clock while still considering the two clocks synchronous. In order to prevent replay attacks, Kerberos uses timestamps as part of its protocol definition. For timestamps to work properly, the clocks of the client and the server need to be in sync as much as possible. Satisfies: SRG-OS-000112-GPOS-00057, SRG-OS-000113-GPOS-00058</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Verify the following is configured in the Default Domain Policy: Open "Group Policy Management". Navigate to "Group Policy Objects" in the Domain being reviewed (Forest >> Domains >> Domain). Right-click on the "Default Domain Policy". Select "Edit". Navigate to Computer Configuration >> Policies >> Windows Settings >> Security Settings >> Account Policies >> Kerberos Policy. If the "Maximum tolerance for computer clock synchronization" is greater than "5" minutes, this is a finding.

## Group: SRG-OS-000118-GPOS-00060

**Group ID:** `V-205707`

### Rule: Windows Server 2019 outdated or unused accounts must be removed or disabled.

**Rule ID:** `SV-205707r857292_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Outdated or unused accounts provide penetration points that may go undetected. Inactive accounts must be deleted if no longer necessary or, if still required, disabled until needed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open "Windows PowerShell". Domain Controllers: Enter "Search-ADAccount -AccountInactive -UsersOnly -TimeSpan 35.00:00:00" This will return accounts that have not been logged on to for 35 days, along with various attributes such as the Enabled status and LastLogonDate. Member servers and standalone or nondomain-joined systems: Copy or enter the lines below to the PowerShell window and enter. (Entering twice may be required. Do not include the quotes at the beginning and end of the query.) "([ADSI]('WinNT://{0}' -f $env:COMPUTERNAME)).Children | Where { $_.SchemaClassName -eq 'user' } | ForEach { $user = ([ADSI]$_.Path) $lastLogin = $user.Properties.LastLogin.Value $enabled = ($user.Properties.UserFlags.Value -band 0x2) -ne 0x2 if ($lastLogin -eq $null) { $lastLogin = 'Never' } Write-Host $user.Name $lastLogin $enabled }" This will return a list of local accounts with the account name, last logon, and if the account is enabled (True/False). For example: User1 10/31/2015 5:49:56 AM True Review the list of accounts returned by the above queries to determine the finding validity for each account reported. Exclude the following accounts: - Built-in administrator account (Renamed, SID ending in 500) - Built-in guest account (Renamed, Disabled, SID ending in 501) - Application accounts If any enabled accounts have not been logged on to within the past 35 days, this is a finding. Inactive accounts that have been reviewed and deemed to be required must be documented with the ISSO.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-205708`

### Rule: Windows Server 2019 Kerberos encryption types must be configured to prevent the use of DES and RC4 encryption suites.

**Rule ID:** `SV-205708r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Certain encryption types are no longer considered secure. The DES and RC4 encryption suites must not be used for Kerberos encryption. Note: Organizations with domain controllers running earlier versions of Windows where RC4 encryption is enabled, selecting "The other domain supports Kerberos AES Encryption" on domain trusts, may be required to allow client communication across the trust relationship.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\Kerberos\Parameters\ Value Name: SupportedEncryptionTypes Value Type: REG_DWORD Value: 0x7ffffff8 (2147483640)

## Group: SRG-OS-000121-GPOS-00062

**Group ID:** `V-205709`

### Rule: Windows Server 2019 must have the built-in guest account disabled.

**Rule ID:** `SV-205709r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A system faces an increased vulnerability threat if the built-in guest account is not disabled. This is a known account that exists on all Windows systems and cannot be deleted. This account is initialized during the installation of the operating system with no password assigned.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> Security Options. If the value for "Accounts: Guest account status" is not set to "Disabled", this is a finding. For server core installations, run the following command: Secedit /Export /Areas SecurityPolicy /CFG C:\Path\FileName.Txt If "EnableGuestAccount" equals "1" in the file, this is a finding.

## Group: SRG-OS-000123-GPOS-00064

**Group ID:** `V-205710`

### Rule: Windows Server 2019 must automatically remove or disable emergency accounts after the crisis is resolved or within 72 hours.

**Rule ID:** `SV-205710r857303_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Emergency administrator accounts are privileged accounts established in response to crisis situations where the need for rapid account activation is required. Therefore, emergency account activation may bypass normal account authorization processes. If these accounts are automatically disabled, system maintenance during emergencies may not be possible, thus adversely affecting system availability. Emergency administrator accounts are different from infrequently used accounts (i.e., local logon accounts used by system administrators when network or normal logon/access is not available). Infrequently used accounts are not subject to automatic termination dates. Emergency accounts are accounts created in response to crisis situations, usually for use by maintenance personnel. The automatic expiration or disabling time period may be extended as needed until the crisis is resolved; however, it must not be extended indefinitely. A permanent account should be established for privileged users who need long-term maintenance accounts. To address access requirements, many operating systems can be integrated with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if emergency administrator accounts are used and identify any that exist. If none exist, this is NA. If emergency administrator accounts cannot be configured with an expiration date due to an ongoing crisis, the accounts must be disabled or removed when the crisis is resolved. If emergency administrator accounts have not been configured with an expiration date or have not been disabled or removed following the resolution of a crisis, this is a finding. Domain Controllers: Open "PowerShell". Enter "Search-ADAccount -AccountExpiring | FT Name, AccountExpirationDate". If "AccountExpirationDate" has been defined and is not within 72 hours for an emergency administrator account, this is a finding. Member servers and standalone or nondomain-joined systems: Open "Command Prompt". Run "Net user [username]", where [username] is the name of the emergency account. If "Account expires" has been defined and is not within 72 hours for an emergency administrator account, this is a finding.

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-205711`

### Rule: Windows Server 2019 Windows Remote Management (WinRM) client must not use Basic authentication.

**Rule ID:** `SV-205711r877395_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Basic authentication uses plain-text passwords that could be used to compromise a system. Disabling Basic authentication will reduce this potential.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\WinRM\Client\ Value Name: AllowBasic Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-205712`

### Rule: Windows Server 2019 Windows Remote Management (WinRM) client must not use Digest authentication.

**Rule ID:** `SV-205712r877395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Digest authentication is not as strong as other options and may be subject to man-in-the-middle attacks. Disallowing Digest authentication will reduce this potential.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\WinRM\Client\ Value Name: AllowDigest Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-205713`

### Rule: Windows Server 2019 Windows Remote Management (WinRM) service must not use Basic authentication.

**Rule ID:** `SV-205713r877395_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Basic authentication uses plain-text passwords that could be used to compromise a system. Disabling Basic authentication will reduce this potential.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\WinRM\Service\ Value Name: AllowBasic Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-205714`

### Rule: Windows Server 2019 administrator accounts must not be enumerated during elevation.

**Rule ID:** `SV-205714r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enumeration of administrator accounts when elevating can provide part of the logon information to an unauthorized user. This setting configures the system to always require users to type in a username and password to elevate a running application.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\CredUI\ Value Name: EnumerateAdministrators Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-205715`

### Rule: Windows Server 2019 local administrator accounts must have their privileged token filtered to prevent elevated privileges from being used over the network on domain-joined member servers.

**Rule ID:** `SV-205715r857320_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A compromised local administrator account can provide means for an attacker to move laterally between domain systems. With User Account Control enabled, filtering the privileged token for local administrator accounts will prevent the elevated privileges of these accounts from being used over the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to member servers. For domain controllers and standalone or nondomain-joined systems, this is NA. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System Value Name: LocalAccountTokenFilterPolicy Type: REG_DWORD Value: 0x00000000 (0) This setting may cause issues with some network scanning tools if local administrative accounts are used remotely. Scans should use domain accounts where possible. If a local administrative account must be used, temporarily enabling the privileged token by configuring the registry value to "1" may be required.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-205716`

### Rule: Windows Server 2019 UIAccess applications must not be allowed to prompt for elevation without using the secure desktop.

**Rule ID:** `SV-205716r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User Account Control (UAC) is a security mechanism for limiting the elevation of privileges, including administrative accounts, unless authorized. This setting prevents User Interface Accessibility programs from disabling the secure desktop for elevation prompts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
UAC requirements are NA for Server Core installations (this is the default installation option for Windows Server 2019 versus Server with Desktop Experience). If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: EnableUIADesktopToggle Value Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-205717`

### Rule: Windows Server 2019 User Account Control must, at a minimum, prompt administrators for consent on the secure desktop.

**Rule ID:** `SV-205717r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User Account Control (UAC) is a security mechanism for limiting the elevation of privileges, including administrative accounts, unless authorized. This setting configures the elevation requirements for logged-on administrators to complete a task that requires raised privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
UAC requirements are NA for Server Core installations (this is default installation option for Windows Server 2019 versus Server with Desktop Experience). If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: ConsentPromptBehaviorAdmin Value Type: REG_DWORD Value: 0x00000002 (2) (Prompt for consent on the secure desktop) 0x00000001 (1) (Prompt for credentials on the secure desktop)

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-205718`

### Rule: Windows Server 2019 User Account Control must be configured to detect application installations and prompt for elevation.

**Rule ID:** `SV-205718r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User Account Control (UAC) is a security mechanism for limiting the elevation of privileges, including administrative accounts, unless authorized. This setting requires Windows to respond to application installation requests by prompting for credentials.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
UAC requirements are NA for Server Core installations (this is the default installation option for Windows Server 2019 versus Server with Desktop Experience). If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: EnableInstallerDetection Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-205719`

### Rule: Windows Server 2019 User Account Control (UAC) must only elevate UIAccess applications that are installed in secure locations.

**Rule ID:** `SV-205719r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>UAC is a security mechanism for limiting the elevation of privileges, including administrative accounts, unless authorized. This setting configures Windows to only allow applications installed in a secure location on the file system, such as the Program Files or the Windows\System32 folders, to run with elevated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
UAC requirements are NA for Server Core installations (this is the default installation option for Windows Server 2019 versus Server with Desktop Experience). If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: EnableSecureUIAPaths Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-205720`

### Rule: Windows Server 2019 User Account Control (UAC) must virtualize file and registry write failures to per-user locations.

**Rule ID:** `SV-205720r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>UAC is a security mechanism for limiting the elevation of privileges, including administrative accounts, unless authorized. This setting configures non-UAC-compliant applications to run in virtualized file and registry entries in per-user locations, allowing them to run.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
UAC requirements are NA for Server Core installations (this is the default installation option for Windows Server 2019 versus Server with Desktop Experience). If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: EnableVirtualization Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-205721`

### Rule: Windows Server 2019 non-system-created file shares must limit access to groups that require it.

**Rule ID:** `SV-205721r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Shares on a system provide network access. To prevent exposing sensitive information, where shares are necessary, permissions must be reconfigured to give the minimum access to accounts that require it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If only system-created shares such as "ADMIN$", "C$", and "IPC$" exist on the system, this is NA. (System-created shares will display a message that it has been shared for administrative purposes when "Properties" is selected.) Run "Computer Management". Navigate to System Tools >> Shared Folders >> Shares. Right-click any non-system-created shares. Select "Properties". Select the "Share Permissions" tab. If the file shares have not been configured to restrict permissions to the specific groups or accounts that require access, this is a finding. Select the "Security" tab. If the permissions have not been configured to restrict permissions to the specific groups or accounts that require access, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-205722`

### Rule: Windows Server 2019 Remote Desktop Services must prevent drive redirection.

**Rule ID:** `SV-205722r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing users from sharing the local drives on their client computers with Remote Session Hosts that they access helps reduce possible exposure of sensitive data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services\ Value Name: fDisableCdm Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-205723`

### Rule: Windows Server 2019 data files owned by users must be on a different logical partition from the directory server data files.

**Rule ID:** `SV-205723r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When directory service data files, especially for directories used for identification, authentication, or authorization, reside on the same logical partition as user-owned files, the directory service data may be more vulnerable to unauthorized access or other availability compromises. Directory service and user-owned data files sharing a partition may be configured with less restrictive permissions in order to allow access to the user data. The directory service may be vulnerable to a denial of service attack when user-owned files on a common partition are expanded to an extent preventing the directory service from acquiring more space for directory or audit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Run "Regedit". Navigate to "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NTDS\Parameters". Note the directory locations in the values for "DSA Database file". Open "Command Prompt". Enter "net share". Note the logical drive(s) or file system partition for any organization-created data shares. Ignore system shares (e.g., NETLOGON, SYSVOL, and administrative shares ending in $). User shares that are hidden (ending with $) should not be ignored. If user shares are located on the same logical partition as the directory server data files, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-205724`

### Rule: Windows Server 2019 must not allow anonymous enumeration of shares.

**Rule ID:** `SV-205724r569188_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Allowing anonymous logon users (null session connections) to list all account names and enumerate all shared resources can provide a map of potential points to attack the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\ Value Name: RestrictAnonymous Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-205725`

### Rule: Windows Server 2019 must restrict anonymous access to Named Pipes and Shares.

**Rule ID:** `SV-205725r569188_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Allowing anonymous access to named pipes or shares provides the potential for unauthorized system access. This setting restricts access to those defined in "Network access: Named Pipes that can be accessed anonymously" and "Network access: Shares that can be accessed anonymously", both of which must be blank under other requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\LanManServer\Parameters\ Value Name: RestrictNullSessAccess Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-205726`

### Rule: Windows Server 2019 directory service must be configured to terminate LDAP-based network connections to the directory server after five minutes of inactivity.

**Rule ID:** `SV-205726r569188_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The failure to terminate inactive network connections increases the risk of a successful attack on the directory server. The longer an established session is in progress, the more time an attacker has to hijack the session, implement a means to passively intercept data, or compromise any protections on client access. For example, if an attacker gains control of a client computer, an existing (already authenticated) session with the directory server could allow access to the directory. The lack of confidentiality protection in LDAP-based sessions increases exposure to this vulnerability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Open an elevated "Command Prompt" (run as administrator). Enter "ntdsutil". At the "ntdsutil:" prompt, enter "LDAP policies". At the "ldap policy:" prompt, enter "connections". At the "server connections:" prompt, enter "connect to server [host-name]" (where [host-name] is the computer name of the domain controller). At the "server connections:" prompt, enter "q". At the "ldap policy:" prompt, enter "show values". If the value for MaxConnIdleTime is greater than "300" (5 minutes) or is not specified, this is a finding. Enter "q" at the "ldap policy:" and "ntdsutil:" prompts to exit. Alternately, Dsquery can be used to display MaxConnIdleTime: Open "Command Prompt (Admin)". Enter the following command (on a single line). dsquery * "cn=Default Query Policy,cn=Query-Policies,cn=Directory Service, cn=Windows NT,cn=Services,cn=Configuration,dc=[forest-name]" -attr LDAPAdminLimits The quotes are required and dc=[forest-name] is the fully qualified LDAP name of the domain being reviewed (e.g., dc=disaost,dc=mil). If the results do not specify a "MaxConnIdleTime" or it has a value greater than "300" (5 minutes), this is a finding.

## Group: SRG-OS-000185-GPOS-00079

**Group ID:** `V-205727`

### Rule: Windows Server 2019 systems requiring data at rest protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest.

**Rule ID:** `SV-205727r953817_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This requirement addresses protection of user-generated data as well as operating system-specific configuration data. Organizations may choose to employ different mechanisms to achieve confidentiality and integrity protections, as appropriate, in accordance with the security category and/or classification of the information. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). Satisfies: SRG-OS-000185-GPOS-00079, SRG-OS-000404-GPOS-00183, SRG-OS-000405-GPOS-00184</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify systems that require additional protections due to factors such as inadequate physical protection or sensitivity of the data employ encryption to protect the confidentiality and integrity of all information at rest. If they do not, this is a finding.

## Group: SRG-OS-000191-GPOS-00080

**Group ID:** `V-205728`

### Rule: Windows Server 2019 must employ automated mechanisms to determine the state of system components with regard to flaw remediation using the following frequency: continuously, where Endpoint Security Solution (ESS) is used; 30 days, for any additional internal network scans not covered by ESS; and annually, for external scans by Computer Network Defense Service Provider (CNDSP).

**Rule ID:** `SV-205728r939261_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of automated mechanisms to scan for security flaws on a continuous and/or periodic basis, the operating system or other system components may remain vulnerable to the exploits presented by undetected software flaws. The operating system may have an integrated solution incorporating continuous scanning using ESS and periodic scanning using other tools.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify DoD-approved ESS software is installed and properly operating. Ask the site ISSM for documentation of the ESS software installation and configuration. If the ISSM is not able to provide a documented configuration for an installed ESS or if the ESS software is not properly maintained or used, this is a finding. Note: Example of documentation can be a copy of the site's CCB approved Software Baseline with version of software noted or a memo from the ISSM stating current ESS software and version.

## Group: SRG-OS-000240-GPOS-00090

**Group ID:** `V-205730`

### Rule: Windows Server 2019 must be configured to audit Logon/Logoff - Account Lockout failures.

**Rule ID:** `SV-205730r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Account Lockout events can be used to identify potentially malicious logon attempts. Satisfies: SRG-OS-000240-GPOS-00090, SRG-OS-000470-GPOS-00214</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Logon/Logoff >> Account Lockout - Failure

## Group: SRG-OS-000257-GPOS-00098

**Group ID:** `V-205731`

### Rule: Windows Server 2019 Event Viewer must be protected from unauthorized modification and deletion.

**Rule ID:** `SV-205731r953818_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the modification or deletion of audit tools. Satisfies: SRG-OS-000257-GPOS-00098, SRG-OS-000258-GPOS-00099</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is not applicable for Windows Core Editions Navigate to "%SystemRoot%\System32". View the permissions on "Eventvwr.exe". If any groups or accounts other than TrustedInstaller have "Full control" or "Modify" permissions, this is a finding. The default permissions below satisfy this requirement: TrustedInstaller - Full Control Administrators, SYSTEM, Users, ALL APPLICATION PACKAGES, ALL RESTRICTED APPLICATION PACKAGES - Read & Execute

## Group: SRG-OS-000297-GPOS-00115

**Group ID:** `V-205732`

### Rule: Windows Server 2019 Deny log on through Remote Desktop Services user right on domain controllers must be configured to prevent unauthenticated access.

**Rule ID:** `SV-205732r852430_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Deny log on through Remote Desktop Services" user right defines the accounts that are prevented from logging on using Remote Desktop Services. The Guests group must be assigned this right to prevent unauthenticated access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. A separate version applies to other systems. Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If the following accounts or groups are not defined for the "Deny log on through Remote Desktop Services" user right, this is a finding: - Guests Group For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If the following SID(s) are not defined for the "SeDenyRemoteInteractiveLogonRight" user right, this is a finding. S-1-5-32-546 (Guests)

## Group: SRG-OS-000297-GPOS-00115

**Group ID:** `V-205733`

### Rule: Windows Server 2019 "Deny log on through Remote Desktop Services" user right on domain-joined member servers must be configured to prevent access from highly privileged domain accounts and all local accounts and from unauthenticated access on all systems.

**Rule ID:** `SV-205733r860033_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Deny log on through Remote Desktop Services" user right defines the accounts that are prevented from logging on using Remote Desktop Services. In an Active Directory Domain, denying logons to the Enterprise Admins and Domain Admins groups on lower-trust systems helps mitigate the risk of privilege escalation from credential theft attacks, which could lead to the compromise of an entire domain. Local accounts on domain-joined systems must also be assigned this right to decrease the risk of lateral movement resulting from credential theft attacks. The Guests group must be assigned this right to prevent unauthenticated access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to member servers and standalone or nondomain-joined systems. A separate version applies to domain controllers. Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If the following accounts or groups are not defined for the "Deny log on through Remote Desktop Services" user right, this is a finding: Domain Systems Only: - Enterprise Admins group - Domain Admins group - Local account (see Note below) All Systems: - Guests group For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If the following SIDs are not defined for the "SeDenyRemoteInteractiveLogonRight" user right, this is a finding. Domain Systems Only: S-1-5-root domain-519 (Enterprise Admins) S-1-5-domain-512 (Domain Admins) S-1-5-113 ("Local account") All Systems: S-1-5-32-546 (Guests) Note: "Local account" is referring to the Windows built-in security group.

## Group: SRG-OS-000312-GPOS-00122

**Group ID:** `V-205734`

### Rule: Windows Server 2019 permissions for the system drive root directory (usually C:\) must conform to minimum requirements.

**Rule ID:** `SV-205734r852432_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changing the system's file and directory permissions allows the possibility of unauthorized and anonymous modification to the operating system and installed applications. The default permissions are adequate when the Security Option "Network access: Let Everyone permissions apply to anonymous users" is set to "Disabled" (WN19-SO-000240). Satisfies: SRG-OS-000312-GPOS-00122, SRG-OS-000312-GPOS-00123, SRG-OS-000312-GPOS-00124</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default permissions are adequate when the Security Option "Network access: Let Everyone permissions apply to anonymous users" is set to "Disabled" (WN19-SO-000240). Review the permissions for the system drive's root directory (usually C:\). Non-privileged groups such as Users or Authenticated Users must not have greater than "Read & execute" permissions except where noted as defaults. Individual accounts must not be used to assign permissions. If permissions are not as restrictive as the default permissions listed below, this is a finding. Viewing in File Explorer: View the Properties of the system drive's root directory. Select the "Security" tab, and the "Advanced" button. Default permissions: C:\ Type - "Allow" for all Inherited from - "None" for all Principal - Access - Applies to SYSTEM - Full control - This folder, subfolders, and files Administrators - Full control - This folder, subfolders, and files Users - Read & execute - This folder, subfolders, and files Users - Create folders/append data - This folder and subfolders Users - Create files/write data - Subfolders only CREATOR OWNER - Full Control - Subfolders and files only Alternately, use icacls: Open "Command Prompt (Admin)". Enter "icacls" followed by the directory: "icacls c:\" The following results should be displayed: c:\ NT AUTHORITY\SYSTEM:(OI)(CI)(F) BUILTIN\Administrators:(OI)(CI)(F) BUILTIN\Users:(OI)(CI)(RX) BUILTIN\Users:(CI)(AD) BUILTIN\Users:(CI)(IO)(WD) CREATOR OWNER:(OI)(CI)(IO)(F) Successfully processed 1 files; Failed processing 0 files

## Group: SRG-OS-000312-GPOS-00122

**Group ID:** `V-205735`

### Rule: Windows Server 2019 permissions for program file directories must conform to minimum requirements.

**Rule ID:** `SV-205735r852433_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changing the system's file and directory permissions allows the possibility of unauthorized and anonymous modification to the operating system and installed applications. The default permissions are adequate when the Security Option "Network access: Let Everyone permissions apply to anonymous users" is set to "Disabled" (WN19-SO-000240). Satisfies: SRG-OS-000312-GPOS-00122, SRG-OS-000312-GPOS-00123, SRG-OS-000312-GPOS-00124</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default permissions are adequate when the Security Option "Network access: Let Everyone permissions apply to anonymous users" is set to "Disabled" (WN19-SO-000240). Review the permissions for the program file directories (Program Files and Program Files [x86]). Non-privileged groups such as Users or Authenticated Users must not have greater than "Read & execute" permissions. Individual accounts must not be used to assign permissions. If permissions are not as restrictive as the default permissions listed below, this is a finding. Viewing in File Explorer: For each folder, view the Properties. Select the "Security" tab, and the "Advanced" button. Default permissions: \Program Files and \Program Files (x86) Type - "Allow" for all Inherited from - "None" for all Principal - Access - Applies to TrustedInstaller - Full control - This folder and subfolders SYSTEM - Modify - This folder only SYSTEM - Full control - Subfolders and files only Administrators - Modify - This folder only Administrators - Full control - Subfolders and files only Users - Read & execute - This folder, subfolders and files CREATOR OWNER - Full control - Subfolders and files only ALL APPLICATION PACKAGES - Read & execute - This folder, subfolders, and files ALL RESTRICTED APPLICATION PACKAGES - Read & execute - This folder, subfolders, and files Alternately, use icacls: Open a Command prompt (admin). Enter "icacls" followed by the directory: 'icacls "c:\program files"' 'icacls "c:\program files (x86)"' The following results should be displayed for each when entered: c:\program files (c:\program files (x86)) NT SERVICE\TrustedInstaller:(F) NT SERVICE\TrustedInstaller:(CI)(IO)(F) NT AUTHORITY\SYSTEM:(M) NT AUTHORITY\SYSTEM:(OI)(CI)(IO)(F) BUILTIN\Administrators:(M) BUILTIN\Administrators:(OI)(CI)(IO)(F) BUILTIN\Users:(RX) BUILTIN\Users:(OI)(CI)(IO)(GR,GE) CREATOR OWNER:(OI)(CI)(IO)(F) APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(RX) APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(OI)(CI)(IO)(GR,GE) APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(RX) APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(OI)(CI)(IO)(GR,GE) Successfully processed 1 files; Failed processing 0 files

## Group: SRG-OS-000312-GPOS-00122

**Group ID:** `V-205736`

### Rule: Windows Server 2019 permissions for the Windows installation directory must conform to minimum requirements.

**Rule ID:** `SV-205736r852434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changing the system's file and directory permissions allows the possibility of unauthorized and anonymous modification to the operating system and installed applications. The default permissions are adequate when the Security Option "Network access: Let Everyone permissions apply to anonymous users" is set to "Disabled" (WN19-SO-000240). Satisfies: SRG-OS-000312-GPOS-00122, SRG-OS-000312-GPOS-00123, SRG-OS-000312-GPOS-00124</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default permissions are adequate when the Security Option "Network access: Let Everyone permissions apply to anonymous users" is set to "Disabled" (WN19-SO-000240). Review the permissions for the Windows installation directory (usually C:\Windows). Non-privileged groups such as Users or Authenticated Users must not have greater than "Read & execute" permissions. Individual accounts must not be used to assign permissions. If permissions are not as restrictive as the default permissions listed below, this is a finding: Viewing in File Explorer: For each folder, view the Properties. Select the "Security" tab and the "Advanced" button. Default permissions: \Windows Type - "Allow" for all Inherited from - "None" for all Principal - Access - Applies to TrustedInstaller - Full control - This folder and subfolders SYSTEM - Modify - This folder only SYSTEM - Full control - Subfolders and files only Administrators - Modify - This folder only Administrators - Full control - Subfolders and files only Users - Read & execute - This folder, subfolders, and files CREATOR OWNER - Full control - Subfolders and files only ALL APPLICATION PACKAGES - Read & execute - This folder, subfolders, and files ALL RESTRICTED APPLICATION PACKAGES - Read & execute - This folder, subfolders, and files Alternately, use icacls: Open a Command prompt (admin). Enter "icacls" followed by the directory: "icacls c:\windows" The following results should be displayed for each when entered: c:\windows NT SERVICE\TrustedInstaller:(F) NT SERVICE\TrustedInstaller:(CI)(IO)(F) NT AUTHORITY\SYSTEM:(M) NT AUTHORITY\SYSTEM:(OI)(CI)(IO)(F) BUILTIN\Administrators:(M) BUILTIN\Administrators:(OI)(CI)(IO)(F) BUILTIN\Users:(RX) BUILTIN\Users:(OI)(CI)(IO)(GR,GE) CREATOR OWNER:(OI)(CI)(IO)(F) APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(RX) APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(OI)(CI)(IO)(GR,GE) APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(RX) APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(OI)(CI)(IO)(GR,GE) Successfully processed 1 files; Failed processing 0 files

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205737`

### Rule: Windows Server 2019 default permissions for the HKEY_LOCAL_MACHINE registry hive must be maintained.

**Rule ID:** `SV-205737r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The registry is integral to the function, security, and stability of the Windows system. Changing the system's registry permissions allows the possibility of unauthorized and anonymous modification to the operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the registry permissions for the keys of the HKEY_LOCAL_MACHINE hive noted below. If any non-privileged groups such as Everyone, Users, or Authenticated Users have greater than Read permission, this is a finding. If permissions are not as restrictive as the default permissions listed below, this is a finding: Run "Regedit". Right-click on the registry areas noted below. Select "Permissions" and the "Advanced" button. HKEY_LOCAL_MACHINE\SECURITY Type - "Allow" for all Inherited from - "None" for all Principal - Access - Applies to SYSTEM - Full Control - This key and subkeys Administrators - Special - This key and subkeys HKEY_LOCAL_MACHINE\SOFTWARE Type - "Allow" for all Inherited from - "None" for all Principal - Access - Applies to Users - Read - This key and subkeys Administrators - Full Control - This key and subkeys SYSTEM - Full Control - This key and subkeys CREATOR OWNER - Full Control - This key and subkeys ALL APPLICATION PACKAGES - Read - This key and subkeys HKEY_LOCAL_MACHINE\SYSTEM Type - "Allow" for all Inherited from - "None" for all Principal - Access - Applies to Users - Read - This key and subkeys Administrators - Full Control - This key and subkeys SYSTEM - Full Control - This key and subkeys CREATOR OWNER - Full Control - Subkeys only ALL APPLICATION PACKAGES - Read - This key and subkeys Server Operators – Read – This Key and subkeys (Domain controllers only) Other examples under the noted keys may also be sampled. There may be some instances where non-privileged groups have greater than Read permission. Microsoft has given Read permission to the SOFTWARE and SYSTEM registry keys in Windows Server 2019 to the following SID, this is currently not a finding. S-1-15-3-1024-1065365936-1281604716-3511738428-1654721687-432734479-3232135806-4053264122-3456934681 If the defaults have not been changed, these are not a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205738`

### Rule: Windows Server 2019 must only allow administrators responsible for the domain controller to have Administrator rights on the system.

**Rule ID:** `SV-205738r877392_rule`
**Severity:** high

**Description:**
<VulnDiscussion>An account that does not have Administrator duties must not have Administrator rights. Such rights would allow the account to bypass or modify required security restrictions on that machine and make it vulnerable to attack. System administrators must log on to systems using only accounts with the minimum level of authority necessary. Standard user accounts must not be members of the built-in Administrators group.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. A separate version applies to other systems. Review the Administrators group. Only the appropriate administrator groups or accounts responsible for administration of the system may be members of the group. Standard user accounts must not be members of the local administrator group. If prohibited accounts are members of the local administrators group, this is a finding. If the built-in Administrator account or other required administrative accounts are found on the system, this is not a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205739`

### Rule: Windows Server 2019 permissions on the Active Directory data files must only allow System and Administrators access.

**Rule ID:** `SV-205739r877392_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Improper access permissions for directory data-related files could allow unauthorized users to read, modify, or delete directory data or audit trails.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Run "Regedit". Navigate to "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NTDS\Parameters". Note the directory locations in the values for: Database log files path DSA Database file By default, they will be \Windows\NTDS. If the locations are different, the following will need to be run for each. Open "Command Prompt (Admin)". Navigate to the NTDS directory (\Windows\NTDS by default). Run "icacls *.*". If the permissions on each file are not as restrictive as the following, this is a finding: NT AUTHORITY\SYSTEM:(I)(F) BUILTIN\Administrators:(I)(F) (I) - permission inherited from parent container (F) - full access

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205740`

### Rule: Windows Server 2019 Active Directory SYSVOL directory must have the proper access control permissions.

**Rule ID:** `SV-205740r877392_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Improper access permissions for directory data files could allow unauthorized users to read, modify, or delete directory data. The SYSVOL directory contains public files (to the domain) such as policies and logon scripts. Data in shared subdirectories are replicated to all domain controllers in a domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Open a command prompt. Run "net share". Make note of the directory location of the SYSVOL share. By default, this will be \Windows\SYSVOL\sysvol. For this requirement, permissions will be verified at the first SYSVOL directory level. If any standard user accounts or groups have greater than "Read & execute" permissions, this is a finding. The default permissions noted below meet this requirement: Open "Command Prompt". Run "icacls c:\Windows\SYSVOL". The following results should be displayed: NT AUTHORITY\Authenticated Users:(RX) NT AUTHORITY\Authenticated Users:(OI)(CI)(IO)(GR,GE) BUILTIN\Server Operators:(RX) BUILTIN\Server Operators:(OI)(CI)(IO)(GR,GE) BUILTIN\Administrators:(M,WDAC,WO) BUILTIN\Administrators:(OI)(CI)(IO)(F) NT AUTHORITY\SYSTEM:(F) NT AUTHORITY\SYSTEM:(OI)(CI)(IO)(F) CREATOR OWNER:(OI)(CI)(IO)(F) (RX) - Read & execute Run "icacls /help" to view definitions of other permission codes.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205741`

### Rule: Windows Server 2019 Active Directory Group Policy objects must have proper access control permissions.

**Rule ID:** `SV-205741r877392_rule`
**Severity:** high

**Description:**
<VulnDiscussion>When directory service database objects do not have appropriate access control permissions, it may be possible for malicious users to create, read, update, or delete the objects and degrade or destroy the integrity of the data. When the directory service is used for identification, authentication, or authorization functions, a compromise of the database objects could lead to a compromise of all systems relying on the directory service. For Active Directory (AD), the Group Policy objects require special attention. In a distributed administration model (i.e., help desk), Group Policy objects are more likely to have access permissions changed from the secure defaults. If inappropriate access permissions are defined for Group Policy objects, this could allow an intruder to change the security policy applied to all domain client computers (workstations and servers).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Review the permissions on Group Policy objects. Open "Group Policy Management" (available from various menus or run "gpmc.msc"). Navigate to "Group Policy Objects" in the domain being reviewed (Forest >> Domains >> Domain). For each Group Policy object: Select the Group Policy object item in the left pane. Select the "Delegation" tab in the right pane. Select the "Advanced" button. Select each Group or user name. View the permissions. If any standard user accounts or groups have "Allow" permissions greater than "Read" and "Apply group policy", this is a finding. Other access permissions that allow the objects to be updated are considered findings unless specifically documented by the ISSO. The default permissions noted below satisfy this requirement. The permissions shown are at the summary level. More detailed permissions can be viewed by selecting the next "Advanced" button, the desired Permission entry, and the "Edit" button. Authenticated Users - Read, Apply group policy, Special permissions The special permissions for Authenticated Users are for Read-type Properties. If detailed permissions include any Create, Delete, Modify, or Write Permissions or Properties, this is a finding. The special permissions for the following default groups are not the focus of this requirement and may include a wide range of permissions and properties: CREATOR OWNER - Special permissions SYSTEM - Read, Write, Create all child objects, Delete all child objects, Special permissions Domain Admins - Read, Write, Create all child objects, Delete all child objects, Special permissions Enterprise Admins - Read, Write, Create all child objects, Delete all child objects, Special permissions ENTERPRISE DOMAIN CONTROLLERS - Read, Special permissions The Domain Admins and Enterprise Admins will not have the "Delete all child objects" permission on the two default Group Policy objects: Default Domain Policy and Default Domain Controllers Policy. They will have this permission on organization created Group Policy objects.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205742`

### Rule: Windows Server 2019 Active Directory Domain Controllers Organizational Unit (OU) object must have the proper access control permissions.

**Rule ID:** `SV-205742r877392_rule`
**Severity:** high

**Description:**
<VulnDiscussion>When Active Directory objects do not have appropriate access control permissions, it may be possible for malicious users to create, read, update, or delete the objects and degrade or destroy the integrity of the data. When the directory service is used for identification, authentication, or authorization functions, a compromise of the database objects could lead to a compromise of all systems that rely on the directory service. The Domain Controllers OU object requires special attention as the Domain Controllers are central to the configuration and management of the domain. Inappropriate access permissions defined for the Domain Controllers OU could allow an intruder or unauthorized personnel to make changes that could lead to the compromise of the domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Review the permissions on the Domain Controllers OU. Open "Active Directory Users and Computers" (available from various menus or run "dsa.msc"). Select "Advanced Features" in the "View" menu if not previously selected. Select the "Domain Controllers" OU (folder in folder icon). Right-click and select "Properties". Select the "Security" tab. If the permissions on the Domain Controllers OU do not restrict changes to System, Domain Admins, Enterprise Admins and Administrators, this is a finding. The default permissions listed below satisfy this requirement. Domains supporting Microsoft Exchange will have additional Exchange related permissions on the Domain Controllers OU. These may include some change related permissions and are not a finding. The permissions shown are at the summary level. More detailed permissions can be viewed by selecting the "Advanced" button, the desired Permission entry, and the "View" or "Edit" button. Except where noted otherwise, the special permissions may include a wide range of permissions and properties and are acceptable for this requirement. CREATOR OWNER - Special permissions SELF - Special permissions Authenticated Users - Read, Special permissions The special permissions for Authenticated Users are Read types. If detailed permissions include any Create, Delete, Modify, or Write Permissions or Properties, this is a finding. SYSTEM - Full Control Domain Admins - Read, Write, Create all child objects, Generate resultant set of policy (logging), Generate resultant set of policy (planning), Special permissions Enterprise Admins - Full Control Key Admins - Special permissions Enterprise Key Admins - Special permissions Administrators - Read, Write, Create all child objects, Generate resultant set of policy (logging), Generate resultant set of policy (planning), Special permissions Pre-Windows 2000 Compatible Access - Special permissions The Special permissions for Pre-Windows 2000 Compatible Access are Read types. If detailed permissions include any Create, Delete, Modify, or Write Permissions or Properties, this is a finding. ENTERPRISE DOMAIN CONTROLLERS - Read, Special permissions

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205743`

### Rule: Windows Server 2019 organization created Active Directory Organizational Unit (OU) objects must have proper access control permissions.

**Rule ID:** `SV-205743r877392_rule`
**Severity:** high

**Description:**
<VulnDiscussion>When directory service database objects do not have appropriate access control permissions, it may be possible for malicious users to create, read, update, or delete the objects and degrade or destroy the integrity of the data. When the directory service is used for identification, authentication, or authorization functions, a compromise of the database objects could lead to a compromise of all systems that rely on the directory service. For Active Directory, the OU objects require special attention. In a distributed administration model (i.e., help desk), OU objects are more likely to have access permissions changed from the secure defaults. If inappropriate access permissions are defined for OU objects, it could allow an intruder to add or delete users in the OU. This could result in unauthorized access to data or a denial of service (DoS) to authorized users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Review the permissions on domain-defined OUs. Open "Active Directory Users and Computers" (available from various menus or run "dsa.msc"). Ensure "Advanced Features" is selected in the "View" menu. For each OU that is defined (folder in folder icon) excluding the Domain Controllers OU: Right-click the OU and select "Properties". Select the "Security" tab. If the Allow type permissions on the OU are not at least as restrictive as those below, this is a finding. The permissions shown are at the summary level. More detailed permissions can be viewed by selecting the "Advanced" button, the desired Permission entry, and the "Edit" or "View" button. Except where noted otherwise, the special permissions may include a wide range of permissions and properties and are acceptable for this requirement. CREATOR OWNER - Special permissions Self - Special permissions Authenticated Users - Read, Special permissions The Special permissions for Authenticated Users are Read type. If detailed permissions include any Create, Delete, Modify, or Write Permissions or Properties, this is a finding. SYSTEM - Full Control Domain Admins - Full Control Enterprise Admins - Full Control Key Admins - Special permissions Enterprise Key Admins - Special permissions Administrators - Read, Write, Create all child objects, Generate resultant set of policy (logging), Generate resultant set of policy (planning), Special permissions Pre-Windows 2000 Compatible Access - Special permissions The Special permissions for Pre-Windows 2000 Compatible Access are for Read types. If detailed permissions include any Create, Delete, Modify, or Write Permissions or Properties, this is a finding. ENTERPRISE DOMAIN CONTROLLERS - Read, Special permissions If an ISSO-approved distributed administration model (help desk or other user support staff) is implemented, permissions above Read may be allowed for groups documented by the ISSO. If any OU with improper permissions includes identification or authentication data (e.g., accounts, passwords, or password hash data) used by systems to determine access control, the severity is CAT I (e.g., OUs that include user accounts, including service/application accounts). If an OU with improper permissions does not include identification and authentication data used by systems to determine access control, the severity is CAT II (e.g., Workstation, Printer OUs).

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205744`

### Rule: Windows Server 2019 Add workstations to domain user right must only be assigned to the Administrators group on domain controllers.

**Rule ID:** `SV-205744r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Add workstations to domain" right may add computers to a domain. This could result in unapproved or incorrectly configured systems being added to a domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Add workstations to domain" right, this is a finding. - Administrators For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeMachineAccountPrivilege" user right, this is a finding. S-1-5-32-544 (Administrators)

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205745`

### Rule: Windows Server 2019 Enable computer and user accounts to be trusted for delegation user right must only be assigned to the Administrators group on domain controllers.

**Rule ID:** `SV-205745r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Enable computer and user accounts to be trusted for delegation" user right allows the "Trusted for Delegation" setting to be changed. This could allow unauthorized users to impersonate other users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. A separate version applies to other systems. Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Enable computer and user accounts to be trusted for delegation" user right, this is a finding. - Administrators For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeEnableDelegationPrivilege" user right, this is a finding. S-1-5-32-544 (Administrators)

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205746`

### Rule: Windows Server 2019 must only allow Administrators responsible for the member server or standalone or nondomain-joined system to have Administrator rights on the system.

**Rule ID:** `SV-205746r877392_rule`
**Severity:** high

**Description:**
<VulnDiscussion>An account that does not have Administrator duties must not have Administrator rights. Such rights would allow the account to bypass or modify required security restrictions on that machine and make it vulnerable to attack. System administrators must log on to systems using only accounts with the minimum level of authority necessary. For domain-joined member servers, the Domain Admins group must be replaced by a domain member server administrator group (refer to AD.0003 in the Active Directory Domain STIG). Restricting highly privileged accounts from the local Administrators group helps mitigate the risk of privilege escalation resulting from credential theft attacks. Standard user accounts must not be members of the built-in Administrators group.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to member servers and standalone or nondomain-joined systems. A separate version applies to domain controllers. Open "Computer Management". Navigate to "Groups" under "Local Users and Groups". Review the local "Administrators" group. Only administrator groups or accounts responsible for administration of the system may be members of the group. For domain-joined member servers, the Domain Admins group must be replaced by a domain member server administrator group. Standard user accounts must not be members of the local Administrator group. If accounts that do not have responsibility for administration of the system are members of the local Administrators group, this is a finding. If the built-in Administrator account or other required administrative accounts are found on the system, this is not a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205747`

### Rule: Windows Server 2019 must restrict remote calls to the Security Account Manager (SAM) to Administrators on domain-joined member servers and standalone or nondomain-joined systems.

**Rule ID:** `SV-205747r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Windows SAM stores users' passwords. Restricting Remote Procedure Call (RPC) connections to the SAM to Administrators helps protect those credentials.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to member servers and standalone or nondomain-joined systems. It is NA for domain controllers. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\ Value Name: RestrictRemoteSAM Value Type: REG_SZ Value: O:BAG:BAD:(A;;RC;;;BA)

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205748`

### Rule: Windows Server 2019 "Enable computer and user accounts to be trusted for delegation" user right must not be assigned to any groups or accounts on domain-joined member servers and standalone or nondomain-joined systems.

**Rule ID:** `SV-205748r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Enable computer and user accounts to be trusted for delegation" user right allows the "Trusted for Delegation" setting to be changed. This could allow unauthorized users to impersonate other users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to member servers and standalone or nondomain-joined systems. A separate version applies to domain controllers. Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups are granted the "Enable computer and user accounts to be trusted for delegation" user right, this is a finding. For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs are granted the "SeEnableDelegationPrivilege" user right, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205749`

### Rule: Windows Server 2019 Access Credential Manager as a trusted caller user right must not be assigned to any groups or accounts.

**Rule ID:** `SV-205749r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Access Credential Manager as a trusted caller" user right may be able to retrieve the credentials of other accounts from Credential Manager.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups are granted the "Access Credential Manager as a trusted caller" user right, this is a finding. For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs are granted the "SeTrustedCredManAccessPrivilege" user right, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205750`

### Rule: Windows Server 2019 Act as part of the operating system user right must not be assigned to any groups or accounts.

**Rule ID:** `SV-205750r877392_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Act as part of the operating system" user right can assume the identity of any user and gain access to resources that the user is authorized to access. Any accounts with this right can take complete control of a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups (to include administrators), are granted the "Act as part of the operating system" user right, this is a finding. For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs are granted the "SeTcbPrivilege" user right, this is a finding. If an application requires this user right, this would not be a finding. Vendor documentation must support the requirement for having the user right. The requirement must be documented with the ISSO. The application account must meet requirements for application account passwords, such as length (WN19-00-000050) and required frequency of changes (WN19-00-000060). Passwords for accounts with this user right must be protected as highly privileged accounts.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205751`

### Rule: Windows Server 2019 Back up files and directories user right must only be assigned to the Administrators group.

**Rule ID:** `SV-205751r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Back up files and directories" user right can circumvent file and directory permissions and could allow access to sensitive data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Back up files and directories" user right, this is a finding: - Administrators For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeBackupPrivilege" user right, this is a finding: S-1-5-32-544 (Administrators) If an application requires this user right, this would not be a finding. Vendor documentation must support the requirement for having the user right. The requirement must be documented with the ISSO. The application account must meet requirements for application account passwords, such as length (WN19-00-000050) and required frequency of changes (WN19-00-000060).

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205752`

### Rule: Windows Server 2019 Create a pagefile user right must only be assigned to the Administrators group.

**Rule ID:** `SV-205752r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Create a pagefile" user right can change the size of a pagefile, which could affect system performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Create a pagefile" user right, this is a finding: - Administrators For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeCreatePagefilePrivilege" user right, this is a finding: S-1-5-32-544 (Administrators)

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205753`

### Rule: Windows Server 2019 Create a token object user right must not be assigned to any groups or accounts.

**Rule ID:** `SV-205753r877392_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Create a token object" user right allows a process to create an access token. This could be used to provide elevated rights and compromise a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups are granted the "Create a token object" user right, this is a finding. For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs are granted the "SeCreateTokenPrivilege" user right, this is a finding. If an application requires this user right, this would not be a finding. Vendor documentation must support the requirement for having the user right. The requirement must be documented with the ISSO. The application account must meet requirements for application account passwords, such as length (WN19-00-000050) and required frequency of changes (WN19-00-000060). Passwords for application accounts with this user right must be protected as highly privileged accounts.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205754`

### Rule: Windows Server 2019 Create global objects user right must only be assigned to Administrators, Service, Local Service, and Network Service.

**Rule ID:** `SV-205754r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Create global objects" user right can create objects that are available to all sessions, which could affect processes in other users' sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Create global objects" user right, this is a finding: - Administrators - Service - Local Service - Network Service For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeCreateGlobalPrivilege" user right, this is a finding: S-1-5-32-544 (Administrators) S-1-5-6 (Service) S-1-5-19 (Local Service) S-1-5-20 (Network Service) If an application requires this user right, this would not be a finding. Vendor documentation must support the requirement for having the user right. The requirement must be documented with the ISSO. The application account must meet requirements for application account passwords, such as length (WN19-00-000050) and required frequency of changes (WN19-00-000060).

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205755`

### Rule: Windows Server 2019 Create permanent shared objects user right must not be assigned to any groups or accounts.

**Rule ID:** `SV-205755r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Create permanent shared objects" user right could expose sensitive data by creating shared objects.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups are granted the "Create permanent shared objects" user right, this is a finding. For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs are granted the "SeCreatePermanentPrivilege" user right, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205756`

### Rule: Windows Server 2019 Create symbolic links user right must only be assigned to the Administrators group.

**Rule ID:** `SV-205756r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Create symbolic links" user right can create pointers to other objects, which could expose the system to attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Create symbolic links" user right, this is a finding: - Administrators For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeCreateSymbolicLinkPrivilege" user right, this is a finding: S-1-5-32-544 (Administrators) Systems that have the Hyper-V role will also have "Virtual Machines" given this user right (this may be displayed as "NT Virtual Machine\Virtual Machines", SID S-1-5-83-0). This is not a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205757`

### Rule: Windows Server 2019 Debug programs: user right must only be assigned to the Administrators group.

**Rule ID:** `SV-205757r877392_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Debug programs" user right can attach a debugger to any process or to the kernel, providing complete access to sensitive and critical operating system components. This right is given to Administrators in the default configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Debug programs" user right, this is a finding: - Administrators For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeDebugPrivilege" user right, this is a finding: S-1-5-32-544 (Administrators) If an application requires this user right, this would not be a finding. Vendor documentation must support the requirement for having the user right. The requirement must be documented with the ISSO. The application account must meet requirements for application account passwords, such as length (WN19-00-000050) and required frequency of changes (WN19-00-000060). Passwords for application accounts with this user right must be protected as highly privileged accounts.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205758`

### Rule: Windows Server 2019 Force shutdown from a remote system user right must only be assigned to the Administrators group.

**Rule ID:** `SV-205758r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Force shutdown from a remote system" user right can remotely shut down a system, which could result in a denial of service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Force shutdown from a remote system" user right, this is a finding: - Administrators For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeRemoteShutdownPrivilege" user right, this is a finding: S-1-5-32-544 (Administrators)

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205759`

### Rule: Windows Server 2019 Generate security audits user right must only be assigned to Local Service and Network Service.

**Rule ID:** `SV-205759r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Generate security audits" user right specifies users and processes that can generate Security Log audit records, which must only be the system service accounts defined.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Generate security audits" user right, this is a finding: - Local Service - Network Service For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeAuditPrivilege" user right, this is a finding: S-1-5-19 (Local Service) S-1-5-20 (Network Service) If an application requires this user right, this would not be a finding. Vendor documentation must support the requirement for having the user right. The requirement must be documented with the ISSO. The application account must meet requirements for application account passwords, such as length (WN19-00-000050) and required frequency of changes (WN19-00-000060).

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205760`

### Rule: Windows Server 2019 Impersonate a client after authentication user right must only be assigned to Administrators, Service, Local Service, and Network Service.

**Rule ID:** `SV-205760r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Impersonate a client after authentication" user right allows a program to impersonate another user or account to run on their behalf. An attacker could use this to elevate privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Impersonate a client after authentication" user right, this is a finding: - Administrators - Service - Local Service - Network Service For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeImpersonatePrivilege" user right, this is a finding: S-1-5-32-544 (Administrators) S-1-5-6 (Service) S-1-5-19 (Local Service) S-1-5-20 (Network Service) If an application requires this user right, this would not be a finding. Vendor documentation must support the requirement for having the user right. The requirement must be documented with the ISSO. The application account must meet requirements for application account passwords, such as length (WN19-00-000050) and required frequency of changes (WN19-00-000060).

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205761`

### Rule: Windows Server 2019 Increase scheduling priority: user right must only be assigned to the Administrators group.

**Rule ID:** `SV-205761r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Increase scheduling priority" user right can change a scheduling priority, causing performance issues or a denial of service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Increase scheduling priority" user right, this is a finding: - Administrators For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeIncreaseBasePriorityPrivilege" user right, this is a finding: S-1-5-32-544 (Administrators) If an application requires this user right, this would not be a finding. Vendor documentation must support the requirement for having the user right. The requirement must be documented with the ISSO. The application account must meet requirements for application account passwords, such as length (WN19-00-000050) and required frequency of changes (WN19-00-000060).

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205762`

### Rule: Windows Server 2019 Load and unload device drivers user right must only be assigned to the Administrators group.

**Rule ID:** `SV-205762r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Load and unload device drivers" user right allows a user to load device drivers dynamically on a system. This could be used by an attacker to install malicious code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Load and unload device drivers" user right, this is a finding: - Administrators For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeLoadDriverPrivilege" user right, this is a finding: S-1-5-32-544 (Administrators)

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205763`

### Rule: Windows Server 2019 Lock pages in memory user right must not be assigned to any groups or accounts.

**Rule ID:** `SV-205763r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Lock pages in memory" user right allows physical memory to be assigned to processes, which could cause performance issues or a denial of service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups are granted the "Lock pages in memory" user right, this is a finding. For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs are granted the "SeLockMemoryPrivilege" user right, this is a finding. If an application requires this user right, this would not be a finding. Vendor documentation must support the requirement for having the user right. The requirement must be documented with the ISSO. The application account must meet requirements for application account passwords, such as length (WN19-00-000050) and required frequency of changes (WN19-00-000060).

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205764`

### Rule: Windows Server 2019 Modify firmware environment values user right must only be assigned to the Administrators group.

**Rule ID:** `SV-205764r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Modify firmware environment values" user right can change hardware configuration environment variables. This could result in hardware failures or a denial of service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Modify firmware environment values" user right, this is a finding: - Administrators For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeSystemEnvironmentPrivilege" user right, this is a finding: S-1-5-32-544 (Administrators)

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205765`

### Rule: Windows Server 2019 Perform volume maintenance tasks user right must only be assigned to the Administrators group.

**Rule ID:** `SV-205765r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Perform volume maintenance tasks" user right can manage volume and disk configurations. This could be used to delete volumes, resulting in data loss or a denial of service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Perform volume maintenance tasks" user right, this is a finding: - Administrators For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeManageVolumePrivilege" user right, this is a finding: S-1-5-32-544 (Administrators)

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205766`

### Rule: Windows Server 2019 Profile single process user right must only be assigned to the Administrators group.

**Rule ID:** `SV-205766r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Profile single process" user right can monitor non-system processes performance. An attacker could use this to identify processes to attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Profile single process" user right, this is a finding: - Administrators For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeProfileSingleProcessPrivilege" user right, this is a finding: S-1-5-32-544 (Administrators)

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205767`

### Rule: Windows Server 2019 Restore files and directories user right must only be assigned to the Administrators group.

**Rule ID:** `SV-205767r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Restore files and directories" user right can circumvent file and directory permissions and could allow access to sensitive data. It could also be used to overwrite more current data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Restore files and directories" user right, this is a finding: - Administrators For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeRestorePrivilege" user right, this is a finding: S-1-5-32-544 (Administrators) If an application requires this user right, this would not be a finding. Vendor documentation must support the requirement for having the user right. The requirement must be documented with the ISSO. The application account must meet requirements for application account passwords, such as length (WN19-00-000050) and required frequency of changes (WN19-00-000060).

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-205768`

### Rule: Windows Server 2019 Take ownership of files or other objects user right must only be assigned to the Administrators group.

**Rule ID:** `SV-205768r877392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Take ownership of files or other objects" user right can take ownership of objects and make changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any accounts or groups other than the following are granted the "Take ownership of files or other objects" user right, this is a finding: - Administrators For server core installations, run the following command: Secedit /Export /Areas User_Rights /cfg c:\path\filename.txt Review the text file. If any SIDs other than the following are granted the "SeTakeOwnershipPrivilege" user right, this is a finding: S-1-5-32-544 (Administrators) If an application requires this user right, this would not be a finding. Vendor documentation must support the requirement for having the user right. The requirement must be documented with the ISSO. The application account must meet requirements for application account passwords, such as length (WN19-00-000050) and required frequency of changes (WN19-00-000060).

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205769`

### Rule: Windows Server 2019 must be configured to audit Account Management - Other Account Management Events successes.

**Rule ID:** `SV-205769r852470_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Other Account Management Events records events such as the access of a password hash or the Password Policy Checking API being called. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206, SRG-OS-000466-GPOS-00210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding: Account Management >> Other Account Management Events - Success

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205770`

### Rule: Windows Server 2019 must be configured to audit Detailed Tracking - Process Creation successes.

**Rule ID:** `SV-205770r852471_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Process Creation records events related to the creation of a process and the source. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Detailed Tracking >> Process Creation - Success

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205771`

### Rule: Windows Server 2019 must be configured to audit Policy Change - Audit Policy Change successes.

**Rule ID:** `SV-205771r852472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Audit Policy Change records events related to changes in audit policy. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Policy Change >> Audit Policy Change - Success

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205772`

### Rule: Windows Server 2019 must be configured to audit Policy Change - Audit Policy Change failures.

**Rule ID:** `SV-205772r852473_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Audit Policy Change records events related to changes in audit policy. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Policy Change >> Audit Policy Change - Failure

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205773`

### Rule: Windows Server 2019 must be configured to audit Policy Change - Authentication Policy Change successes.

**Rule ID:** `SV-205773r852474_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Authentication Policy Change records events related to changes in authentication policy, including Kerberos policy and Trust changes. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206, SRG-OS-000466-GPOS-00210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Policy Change >> Authentication Policy Change - Success

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205774`

### Rule: Windows Server 2019 must be configured to audit Policy Change - Authorization Policy Change successes.

**Rule ID:** `SV-205774r852475_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Authorization Policy Change records events related to changes in user rights, such as "Create a token object". Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206, SRG-OS-000466-GPOS-00210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Policy Change >> Authorization Policy Change - Success

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205775`

### Rule: Windows Server 2019 must be configured to audit Privilege Use - Sensitive Privilege Use successes.

**Rule ID:** `SV-205775r852476_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Sensitive Privilege Use records events related to use of sensitive privileges, such as "Act as part of the operating system" or "Debug programs". Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206, SRG-OS-000466-GPOS-00210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Privilege Use >> Sensitive Privilege Use - Success

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205776`

### Rule: Windows Server 2019 must be configured to audit Privilege Use - Sensitive Privilege Use failures.

**Rule ID:** `SV-205776r852477_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Sensitive Privilege Use records events related to use of sensitive privileges, such as "Act as part of the operating system" or "Debug programs". Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206, SRG-OS-000466-GPOS-00210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Privilege Use >> Sensitive Privilege Use - Failure

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205777`

### Rule: Windows Server 2019 must be configured to audit System - IPsec Driver successes.

**Rule ID:** `SV-205777r852478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. IPsec Driver records events related to the IPsec Driver, such as dropped packets. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. System >> IPsec Driver - Success

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205778`

### Rule: Windows Server 2019 must be configured to audit System - IPsec Driver failures.

**Rule ID:** `SV-205778r852479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. IPsec Driver records events related to the IPsec Driver, such as dropped packets. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. System >> IPsec Driver - Failure

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205779`

### Rule: Windows Server 2019 must be configured to audit System - Other System Events successes.

**Rule ID:** `SV-205779r852480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Audit Other System Events records information related to cryptographic key operations and the Windows Firewall service. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. System >> Other System Events - Success

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205780`

### Rule: Windows Server 2019 must be configured to audit System - Other System Events failures.

**Rule ID:** `SV-205780r852481_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Audit Other System Events records information related to cryptographic key operations and the Windows Firewall service. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. System >> Other System Events - Failure

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205781`

### Rule: Windows Server 2019 must be configured to audit System - Security State Change successes.

**Rule ID:** `SV-205781r852482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Security State Change records events related to changes in the security state, such as startup and shutdown of the system. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. System >> Security State Change - Success

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205782`

### Rule: Windows Server 2019 must be configured to audit System - Security System Extension successes.

**Rule ID:** `SV-205782r852483_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Security System Extension records events related to extension code being loaded by the security subsystem. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. System >> Security System Extension - Success

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205783`

### Rule: Windows Server 2019 must be configured to audit System - System Integrity successes.

**Rule ID:** `SV-205783r852484_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. System Integrity records events related to violations of integrity to the security subsystem. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000471-GPOS-00215, SRG-OS-000471-GPOS-00216, SRG-OS-000477-GPOS-00222</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. System >> System Integrity - Success

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205784`

### Rule: Windows Server 2019 must be configured to audit System - System Integrity failures.

**Rule ID:** `SV-205784r852485_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. System Integrity records events related to violations of integrity to the security subsystem. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000471-GPOS-00215, SRG-OS-000471-GPOS-00216, SRG-OS-000477-GPOS-00222</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. System >> System Integrity - Failure

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205785`

### Rule: Windows Server 2019 Active Directory Group Policy objects must be configured with proper audit settings.

**Rule ID:** `SV-205785r852486_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When inappropriate audit settings are configured for directory service database objects, it may be possible for a user or process to update the data without generating any tracking data. The impact of missing audit data is related to the type of object. A failure to capture audit data for objects used by identification, authentication, or authorization functions could degrade or eliminate the ability to track changes to access policy for systems or data. For Active Directory (AD), there are a number of critical object types in the domain naming context of the AD database for which auditing is essential. This includes Group Policy objects. Because changes to these objects can significantly impact access controls or the availability of systems, the absence of auditing data makes it impossible to identify the source of changes that impact the confidentiality, integrity, and availability of data and systems throughout an AD domain. The lack of proper auditing can result in insufficient forensic evidence needed to investigate an incident and prosecute the intruder. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Review the auditing configuration for all Group Policy objects. Open "Group Policy Management" (available from various menus or run "gpmc.msc"). Navigate to "Group Policy Objects" in the domain being reviewed (Forest >> Domains >> Domain). For each Group Policy object: Select the Group Policy object item in the left pane. Select the "Delegation" tab in the right pane. Select the "Advanced" button. Select the "Advanced" button again and then the "Auditing" tab. If the audit settings for any Group Policy object are not at least as inclusive as those below, this is a finding: Type - Fail Principal - Everyone Access - Full Control Applies to - This object and all descendant objects or Descendant groupPolicyContainer objects The three Success types listed below are defaults inherited from the Parent Object. Where Special is listed in the summary screens for Access, detailed Permissions are provided for reference. Type - Success Principal - Everyone Access - Special (Permissions: Write all properties, Modify permissions; Properties: all "Write" type selected) Inherited from - Parent Object Applies to - Descendant groupPolicyContainer objects Two instances with the following summary information will be listed: Type - Success Principal - Everyone Access - blank (Permissions: none selected; Properties: one instance - Write gPLink, one instance - Write gPOptions) Inherited from - Parent Object Applies to - Descendant Organization Unit Objects

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205786`

### Rule: Windows Server 2019 Active Directory Domain object must be configured with proper audit settings.

**Rule ID:** `SV-205786r852487_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When inappropriate audit settings are configured for directory service database objects, it may be possible for a user or process to update the data without generating any tracking data. The impact of missing audit data is related to the type of object. A failure to capture audit data for objects used by identification, authentication, or authorization functions could degrade or eliminate the ability to track changes to access policy for systems or data. For Active Directory (AD), there are a number of critical object types in the domain naming context of the AD database for which auditing is essential. This includes the Domain object. Because changes to these objects can significantly impact access controls or the availability of systems, the absence of auditing data makes it impossible to identify the source of changes that impact the confidentiality, integrity, and availability of data and systems throughout an AD domain. The lack of proper auditing can result in insufficient forensic evidence needed to investigate an incident and prosecute the intruder. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Review the auditing configuration for the Domain object. Open "Active Directory Users and Computers" (available from various menus or run "dsa.msc"). Ensure "Advanced Features" is selected in the "View" menu. Select the domain being reviewed in the left pane. Right-click the domain name and select "Properties". Select the "Security" tab. Select the "Advanced" button and then the "Auditing" tab. If the audit settings on the Domain object are not at least as inclusive as those below, this is a finding: Type - Fail Principal - Everyone Access - Full Control Inherited from - None Applies to - This object only The success types listed below are defaults. Where Special is listed in the summary screens for Access, detailed Permissions are provided for reference. Various Properties selections may also exist by default. Two instances with the following summary information will be listed: Type - Success Principal - Everyone Access - (blank) Inherited from - None Applies to - Special Type - Success Principal - Domain Users Access - All extended rights Inherited from - None Applies to - This object only Type - Success Principal - Administrators Access - All extended rights Inherited from - None Applies to - This object only Type - Success Principal - Everyone Access - Special Inherited from - None Applies to - This object only (Access - Special = Permissions: Write all properties, Modify permissions, Modify owner)

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205787`

### Rule: Windows Server 2019 Active Directory Infrastructure object must be configured with proper audit settings.

**Rule ID:** `SV-205787r852488_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When inappropriate audit settings are configured for directory service database objects, it may be possible for a user or process to update the data without generating any tracking data. The impact of missing audit data is related to the type of object. A failure to capture audit data for objects used by identification, authentication, or authorization functions could degrade or eliminate the ability to track changes to access policy for systems or data. For Active Directory (AD), there are a number of critical object types in the domain naming context of the AD database for which auditing is essential. This includes the Infrastructure object. Because changes to these objects can significantly impact access controls or the availability of systems, the absence of auditing data makes it impossible to identify the source of changes that impact the confidentiality, integrity, and availability of data and systems throughout an AD domain. The lack of proper auditing can result in insufficient forensic evidence needed to investigate an incident and prosecute the intruder. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Review the auditing configuration for Infrastructure object. Open "Active Directory Users and Computers" (available from various menus or run "dsa.msc"). Ensure "Advanced Features" is selected in the "View" menu. Select the domain being reviewed in the left pane. Right-click the "Infrastructure" object in the right pane and select "Properties". Select the "Security" tab. Select the "Advanced" button and then the "Auditing" tab. If the audit settings on the Infrastructure object are not at least as inclusive as those below, this is a finding: Type - Fail Principal - Everyone Access - Full Control Inherited from - None The success types listed below are defaults. Where Special is listed in the summary screens for Access, detailed Permissions are provided for reference. Various Properties selections may also exist by default. Type - Success Principal - Everyone Access - Special Inherited from - None (Access - Special = Permissions: Write all properties, All extended rights, Change infrastructure master) Two instances with the following summary information will be listed: Type - Success Principal - Everyone Access - (blank) Inherited from - (CN of domain)

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205788`

### Rule: Windows Server 2019 Active Directory Domain Controllers Organizational Unit (OU) object must be configured with proper audit settings.

**Rule ID:** `SV-205788r852489_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When inappropriate audit settings are configured for directory service database objects, it may be possible for a user or process to update the data without generating any tracking data. The impact of missing audit data is related to the type of object. A failure to capture audit data for objects used by identification, authentication, or authorization functions could degrade or eliminate the ability to track changes to access policy for systems or data. For Active Directory (AD), there are a number of critical object types in the domain naming context of the AD database for which auditing is essential. This includes the Domain Controller OU object. Because changes to these objects can significantly impact access controls or the availability of systems, the absence of auditing data makes it impossible to identify the source of changes that impact the confidentiality, integrity, and availability of data and systems throughout an AD domain. The lack of proper auditing can result in insufficient forensic evidence needed to investigate an incident and prosecute the intruder. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Review the auditing configuration for the Domain Controller OU object. Open "Active Directory Users and Computers" (available from various menus or run "dsa.msc"). Ensure "Advanced Features" is selected in the "View" menu. Select the "Domain Controllers OU" under the domain being reviewed in the left pane. Right-click the "Domain Controllers OU" object and select "Properties". Select the "Security" tab. Select the "Advanced" button and then the "Auditing" tab. If the audit settings on the Domain Controllers OU object are not at least as inclusive as those below, this is a finding: Type - Fail Principal - Everyone Access - Full Control Inherited from - None Applies to - This object and all descendant objects The success types listed below are defaults. Where Special is listed in the summary screens for Access, detailed Permissions are provided for reference. Various Properties selections may also exist by default. Type - Success Principal - Everyone Access - Special Inherited from - None Applies to - This object only (Access - Special = Permissions: all create, delete and modify permissions) Type - Success Principal - Everyone Access - Write all properties Inherited from - None Applies to - This object and all descendant objects Two instances with the following summary information will be listed: Type - Success Principal - Everyone Access - (blank) Inherited from - (CN of domain) Applies to - Descendant Organizational Unit objects

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205789`

### Rule: Windows Server 2019 Active Directory AdminSDHolder object must be configured with proper audit settings.

**Rule ID:** `SV-205789r852490_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When inappropriate audit settings are configured for directory service database objects, it may be possible for a user or process to update the data without generating any tracking data. The impact of missing audit data is related to the type of object. A failure to capture audit data for objects used by identification, authentication, or authorization functions could degrade or eliminate the ability to track changes to access policy for systems or data. For Active Directory (AD), there are a number of critical object types in the domain naming context of the AD database for which auditing is essential. This includes the AdminSDHolder object. Because changes to these objects can significantly impact access controls or the availability of systems, the absence of auditing data makes it impossible to identify the source of changes that impact the confidentiality, integrity, and availability of data and systems throughout an AD domain. The lack of proper auditing can result in insufficient forensic evidence needed to investigate an incident and prosecute the intruder. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Review the auditing configuration for the "AdminSDHolder" object. Open "Active Directory Users and Computers" (available from various menus or run "dsa.msc"). Ensure "Advanced Features" is selected in the "View" menu. Select "System" under the domain being reviewed in the left pane. Right-click the "AdminSDHolder" object in the right pane and select "Properties". Select the "Security" tab. Select the "Advanced" button and then the "Auditing" tab. If the audit settings on the "AdminSDHolder" object are not at least as inclusive as those below, this is a finding: Type - Fail Principal - Everyone Access - Full Control Inherited from - None Applies to - This object only The success types listed below are defaults. Where Special is listed in the summary screens for Access, detailed Permissions are provided for reference. Various Properties selections may also exist by default. Type - Success Principal - Everyone Access - Special Inherited from - None Applies to - This object only (Access - Special = Write all properties, Modify permissions, Modify owner) Two instances with the following summary information will be listed: Type - Success Principal - Everyone Access - (blank) Inherited from - (CN of domain) Applies to - Descendant Organizational Unit objects

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205790`

### Rule: Windows Server 2019 Active Directory RID Manager$ object must be configured with proper audit settings.

**Rule ID:** `SV-205790r852491_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When inappropriate audit settings are configured for directory service database objects, it may be possible for a user or process to update the data without generating any tracking data. The impact of missing audit data is related to the type of object. A failure to capture audit data for objects used by identification, authentication, or authorization functions could degrade or eliminate the ability to track changes to access policy for systems or data. For Active Directory (AD), there are a number of critical object types in the domain naming context of the AD database for which auditing is essential. This includes the RID Manager$ object. Because changes to these objects can significantly impact access controls or the availability of systems, the absence of auditing data makes it impossible to identify the source of changes that impact the confidentiality, integrity, and availability of data and systems throughout an AD domain. The lack of proper auditing can result in insufficient forensic evidence needed to investigate an incident and prosecute the intruder. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Review the auditing configuration for the "RID Manager$" object. Open "Active Directory Users and Computers" (available from various menus or run "dsa.msc"). Ensure "Advanced Features" is selected in the "View" menu. Select "System" under the domain being reviewed in the left pane. Right-click the "RID Manager$" object in the right pane and select "Properties". Select the "Security" tab. Select the "Advanced" button and then the "Auditing" tab. If the audit settings on the "RID Manager$" object are not at least as inclusive as those below, this is a finding: Type - Fail Principal - Everyone Access - Full Control Inherited from - None The success types listed below are defaults. Where Special is listed in the summary screens for Access, detailed Permissions are provided for reference. Various Properties selections may also exist by default. Type - Success Principal - Everyone Access - Special Inherited from - None (Access - Special = Write all properties, All extended rights, Change RID master) Two instances with the following summary information will be listed: Type - Success Principal - Everyone Access - (blank) Inherited from - (CN of domain)

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205791`

### Rule: Windows Server 2019 must be configured to audit DS Access - Directory Service Access successes.

**Rule ID:** `SV-205791r852492_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Audit Directory Service Access records events related to users accessing an Active Directory object. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. DS Access >> Directory Service Access - Success

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205792`

### Rule: Windows Server 2019 must be configured to audit DS Access - Directory Service Access failures.

**Rule ID:** `SV-205792r852493_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Audit Directory Service Access records events related to users accessing an Active Directory object. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. DS Access >> Directory Service Access - Failure

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-205793`

### Rule: Windows Server 2019 must be configured to audit DS Access - Directory Service Changes successes.

**Rule ID:** `SV-205793r852494_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Audit Directory Service Changes records events related to changes made to objects in Active Directory Domain Services. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. DS Access >> Directory Service Changes - Success

## Group: SRG-OS-000329-GPOS-00128

**Group ID:** `V-205795`

### Rule: Windows Server 2019 account lockout duration must be configured to 15 minutes or greater.

**Rule ID:** `SV-205795r852496_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The account lockout feature, when enabled, prevents brute-force password attacks on the system. This parameter specifies the period of time that an account will remain locked after the specified number of failed logon attempts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Account Policies >> Account Lockout Policy. If the "Account lockout duration" is less than "15" minutes (excluding "0"), this is a finding. For server core installations, run the following command: Secedit /Export /Areas SecurityPolicy /CFG C:\Path\FileName.Txt If "LockoutDuration" is less than "15" (excluding "0") in the file, this is a finding. Configuring this to "0", requiring an administrator to unlock the account, is more restrictive and is not a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-205796`

### Rule: Windows Server 2019 Application event log size must be configured to 32768 KB or greater.

**Rule ID:** `SV-205796r877391_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inadequate log size will cause the log to fill up quickly. This may prevent audit events from being recorded properly and require frequent attention by administrative personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is configured to write events directly to an audit server, this is NA. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\EventLog\Application\ Value Name: MaxSize Type: REG_DWORD Value: 0x00008000 (32768) (or greater)

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-205797`

### Rule: Windows Server 2019 Security event log size must be configured to 196608 KB or greater.

**Rule ID:** `SV-205797r877391_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inadequate log size will cause the log to fill up quickly. This may prevent audit events from being recorded properly and require frequent attention by administrative personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is configured to write events directly to an audit server, this is NA. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\EventLog\Security\ Value Name: MaxSize Type: REG_DWORD Value: 0x00030000 (196608) (or greater)

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-205798`

### Rule: Windows Server 2019 System event log size must be configured to 32768 KB or greater.

**Rule ID:** `SV-205798r877391_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inadequate log size will cause the log to fill up quickly. This may prevent audit events from being recorded properly and require frequent attention by administrative personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is configured to write events directly to an audit server, this is NA. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\EventLog\System\ Value Name: MaxSize Type: REG_DWORD Value: 0x00008000 (32768) (or greater)

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-205799`

### Rule: Windows Server 2019 audit records must be backed up to a different system or media than the system being audited.

**Rule ID:** `SV-205799r877390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of log data includes assuring the log data is not accidentally lost or deleted. Audit information stored in one location is vulnerable to accidental or incidental deletion or alteration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if a process to back up log data to a different system or media than the system being audited has been implemented. If it has not, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-205800`

### Rule: The Windows Server 2019 time service must synchronize with an appropriate DOD time source.

**Rule ID:** `SV-205800r921953_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Windows Time Service controls time synchronization settings. Time synchronization is essential for authentication and auditing purposes. If the Windows Time Service is used, it must synchronize with a secure, authorized time source. Domain-joined systems are automatically configured to synchronize with domain controllers. If an NTP server is configured, it must synchronize with a secure, authorized time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Windows time service configuration. Open an elevated "Command Prompt" (run as administrator). Enter "W32tm /query /configuration". Domain-joined systems (excluding the domain controller with the PDC emulator role): If the value for "Type" under "NTP Client" is not "NT5DS", this is a finding. Other systems: If systems are configured with a "Type" of "NTP", including standalone or nondomain-joined systems and the domain controller with the PDC Emulator role, and do not have a DOD time server defined for "NTPServer", this is a finding. To determine the domain controller with the PDC Emulator role: Open "PowerShell". Enter "Get-ADDomain | FT PDCEmulator".

## Group: SRG-OS-000362-GPOS-00149

**Group ID:** `V-205801`

### Rule: Windows Server 2019 must prevent users from changing installation options.

**Rule ID:** `SV-205801r852502_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Installation options for applications are typically controlled by administrators. This setting prevents users from changing installation options that may bypass security features.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\Installer\ Value Name: EnableUserControl Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000362-GPOS-00149

**Group ID:** `V-205802`

### Rule: Windows Server 2019 must disable the Windows Installer Always install with elevated privileges option.

**Rule ID:** `SV-205802r852503_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Standard user accounts must not be granted elevated privileges. Enabling Windows Installer to elevate privileges when installing applications can allow malicious persons and applications to gain full control of a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\Installer\ Value Name: AlwaysInstallElevated Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-205803`

### Rule: Windows Server 2019 system files must be monitored for unauthorized changes.

**Rule ID:** `SV-205803r890522_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Monitoring system files for changes against a baseline on a regular basis may help detect the possible introduction of malicious code on a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine whether the system is monitored for unauthorized changes to system files (e.g., *.exe, *.bat, *.com, *.cmd, and *.dll) against a baseline on a weekly basis. If system files are not monitored for unauthorized changes, this is a finding. An approved and properly configured solution will contain both a list of baselines that includes all system file locations and a file comparison task that is scheduled to run at least weekly.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-205804`

### Rule: Windows Server 2019 Autoplay must be turned off for non-volume devices.

**Rule ID:** `SV-205804r852506_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Allowing AutoPlay to execute may introduce malicious code to a system. AutoPlay begins reading from a drive as soon as media is inserted into the drive. As a result, the setup file of programs or music on audio media may start. This setting will disable AutoPlay for non-volume devices, such as Media Transfer Protocol (MTP) devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\Explorer\ Value Name: NoAutoplayfornonVolume Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-205805`

### Rule: Windows Server 2019 default AutoRun behavior must be configured to prevent AutoRun commands.

**Rule ID:** `SV-205805r852507_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Allowing AutoRun commands to execute may introduce malicious code to a system. Configuring this setting prevents AutoRun commands from executing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\ Value Name: NoAutorun Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-205806`

### Rule: Windows Server 2019 AutoPlay must be disabled for all drives.

**Rule ID:** `SV-205806r852508_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Allowing AutoPlay to execute may introduce malicious code to a system. AutoPlay begins reading from a drive as soon media is inserted into the drive. As a result, the setup file of programs or music on audio media may start. By default, AutoPlay is disabled on removable drives, such as the floppy disk drive (but not the CD-ROM drive) and on network drives. Enabling this policy disables AutoPlay on all drives.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\policies\Explorer\ Value Name: NoDriveTypeAutoRun Type: REG_DWORD Value: 0x000000ff (255)

## Group: SRG-OS-000370-GPOS-00155

**Group ID:** `V-205807`

### Rule: Windows Server 2019 must employ a deny-all, permit-by-exception policy to allow the execution of authorized software programs.

**Rule ID:** `SV-205807r890520_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an allowlist provides a configuration management method to allow the execution of only authorized software. Using only authorized software decreases risk by limiting the number of potential vulnerabilities. The organization must identify authorized software programs and only permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as allowlisting.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system employs a deny-all, permit-by-exception policy to allow the execution of authorized software programs. If an application allowlisting program is not in use on the system, this is a finding. Configuration of allowlisting applications will vary by the program. AppLocker is an allowlisting application built into Windows Server. A deny-by-default implementation is initiated by enabling any AppLocker rules within a category, only allowing what is specified by defined rules. If AppLocker is used, perform the following to view the configuration of AppLocker: Open "PowerShell". If the AppLocker PowerShell module has not been imported previously, execute the following first: Import-Module AppLocker Execute the following command, substituting [c:\temp\file.xml] with a location and file name appropriate for the system: Get-AppLockerPolicy -Effective -XML > c:\temp\file.xml This will produce an xml file with the effective settings that can be viewed in a browser or opened in a program such as Excel for review. Implementation guidance for AppLocker is available at the following link: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/applocker-policies-deployment-guide

## Group: SRG-OS-000373-GPOS-00157

**Group ID:** `V-205808`

### Rule: Windows Server 2019 must not save passwords in the Remote Desktop Client.

**Rule ID:** `SV-205808r852510_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Saving passwords in the Remote Desktop Client could allow an unauthorized user to establish a remote desktop session to another system. The system must be configured to prevent users from saving passwords in the Remote Desktop Client. Satisfies: SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00156</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services\ Value Name: DisablePasswordSaving Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000373-GPOS-00157

**Group ID:** `V-205809`

### Rule: Windows Server 2019 Remote Desktop Services must always prompt a client for passwords upon connection.

**Rule ID:** `SV-205809r852511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting controls the ability of users to supply passwords automatically as part of their remote desktop connection. Disabling this setting would allow anyone to use the stored credentials in a connection item to connect to the terminal server. Satisfies: SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00156</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services\ Value Name: fPromptForPassword Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000373-GPOS-00157

**Group ID:** `V-205810`

### Rule: Windows Server 2019 Windows Remote Management (WinRM) service must not store RunAs credentials.

**Rule ID:** `SV-205810r852512_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Storage of administrative credentials could allow unauthorized access. Disallowing the storage of RunAs credentials for Windows Remote Management will prevent them from being used with plug-ins. Satisfies: SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00156</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\WinRM\Service\ Value Name: DisableRunAs Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000373-GPOS-00157

**Group ID:** `V-205811`

### Rule: Windows Server 2019 User Account Control approval mode for the built-in Administrator must be enabled.

**Rule ID:** `SV-205811r852513_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User Account Control (UAC) is a security mechanism for limiting the elevation of privileges, including administrative accounts, unless authorized. This setting configures the built-in Administrator account so that it runs in Admin Approval Mode. Satisfies: SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00156</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
UAC requirements are NA for Server Core installations (this is the default installation option for Windows Server 2019 versus Server with Desktop Experience). If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: FilterAdministratorToken Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000373-GPOS-00157

**Group ID:** `V-205812`

### Rule: Windows Server 2019 User Account Control must automatically deny standard user requests for elevation.

**Rule ID:** `SV-205812r852514_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User Account Control (UAC) is a security mechanism for limiting the elevation of privileges, including administrative accounts, unless authorized. This setting controls the behavior of elevation when requested by a standard user account. Satisfies: SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00156</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
UAC requirements are NA for Server Core installations (this is the default installation option for Windows Server 2019 versus Server with Desktop Experience). If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: ConsentPromptBehaviorUser Value Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000373-GPOS-00157

**Group ID:** `V-205813`

### Rule: Windows Server 2019 User Account Control must run all administrators in Admin Approval Mode, enabling UAC.

**Rule ID:** `SV-205813r852515_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User Account Control (UAC) is a security mechanism for limiting the elevation of privileges, including administrative accounts, unless authorized. This setting enables UAC. Satisfies: SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00156</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
UAC requirements are NA for Server Core installations (this is the default installation option for Windows Server 2019 versus Server with Desktop Experience). If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: EnableLUA Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000379-GPOS-00164

**Group ID:** `V-205814`

### Rule: Windows Server 2019 must restrict unauthenticated Remote Procedure Call (RPC) clients from connecting to the RPC server on domain-joined member servers and standalone or nondomain-joined systems.

**Rule ID:** `SV-205814r877039_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthenticated RPC clients may allow anonymous access to sensitive information. Configuring RPC to restrict unauthenticated RPC clients from connecting to the RPC server will prevent anonymous connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to member servers and standalone or nondomain-joined systems. It is NA for domain controllers. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows NT\Rpc\ Value Name: RestrictRemoteClients Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000379-GPOS-00164

**Group ID:** `V-205815`

### Rule: Windows Server 2019 computer account password must not be prevented from being reset.

**Rule ID:** `SV-205815r877039_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Computer account passwords are changed automatically on a regular basis. Disabling automatic password changes can make the system more vulnerable to malicious access. Frequent password changes can be a significant safeguard for the system. A new password for the computer account will be generated every 30 days.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Netlogon\Parameters\ Value Name: DisablePasswordChange Value Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000393-GPOS-00173

**Group ID:** `V-205816`

### Rule: Windows Server 2019 Windows Remote Management (WinRM) client must not allow unencrypted traffic.

**Rule ID:** `SV-205816r877382_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unencrypted remote access to a system can allow sensitive information to be compromised. Windows remote management connections must be encrypted to prevent this. Satisfies: SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\WinRM\Client\ Value Name: AllowUnencryptedTraffic Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000393-GPOS-00173

**Group ID:** `V-205817`

### Rule: Windows Server 2019 Windows Remote Management (WinRM) service must not allow unencrypted traffic.

**Rule ID:** `SV-205817r877382_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unencrypted remote access to a system can allow sensitive information to be compromised. Windows remote management connections must be encrypted to prevent this. Satisfies: SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\WinRM\Service\ Value Name: AllowUnencryptedTraffic Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000396-GPOS-00176

**Group ID:** `V-205818`

### Rule: Windows Server 2019 must use separate, NSA-approved (Type 1) cryptography to protect the directory data in transit for directory service implementations at a classified confidentiality level when replication data traverses a network cleared to a lower level than the data.

**Rule ID:** `SV-205818r877380_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Directory data that is not appropriately encrypted is subject to compromise. Commercial-grade encryption does not provide adequate protection when the classification level of directory data in transit is higher than the level of the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Review the organization network diagram(s) or documentation to determine the level of classification for the network(s) over which replication data is transmitted. Determine the classification level of the Windows domain controller. If the classification level of the Windows domain controller is higher than the level of the networks, review the organization network diagram(s) and directory implementation documentation to determine if NSA-approved encryption is used to protect the replication network traffic. If the classification level of the Windows domain controller is higher than the level of the network traversed and NSA-approved encryption is not used, this is a finding.

## Group: SRG-OS-000420-GPOS-00186

**Group ID:** `V-205819`

### Rule: Windows Server 2019 must be configured to ignore NetBIOS name release requests except from WINS servers.

**Rule ID:** `SV-205819r852521_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Configuring the system to ignore name release requests, except from WINS servers, prevents a denial of service (DoS) attack. The DoS consists of sending a NetBIOS name release request to the server for each entry in the server's cache, causing a response delay in the normal operation of the server's WINS resolution capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Netbt\Parameters\ Value Name: NoNameReleaseOnDemand Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-205820`

### Rule: Windows Server 2019 domain controllers must require LDAP access signing.

**Rule ID:** `SV-205820r916422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unsigned network traffic is susceptible to man-in-the-middle attacks, where an intruder captures packets between the server and the client and modifies them before forwarding them to the client. In the case of an LDAP server, this means that an attacker could cause a client to make decisions based on false records from the LDAP directory. The risk of an attacker pulling this off can be decreased by implementing strong physical security measures to protect the network infrastructure. Furthermore, implementing Internet Protocol security (IPsec) authentication header mode (AH), which performs mutual authentication and packet integrity for Internet Protocol (IP) traffic, can make all types of man-in-the-middle attacks extremely difficult. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\NTDS\Parameters\ Value Name: LDAPServerIntegrity Value Type: REG_DWORD Value: 0x00000002 (2)

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-205821`

### Rule: Windows Server 2019 setting Domain member: Digitally encrypt or sign secure channel data (always) must be configured to Enabled.

**Rule ID:** `SV-205821r916422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Requests sent on the secure channel are authenticated, and sensitive information (such as passwords) is encrypted, but not all information is encrypted. If this policy is enabled, outgoing secure channel traffic will be encrypted and signed. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Netlogon\Parameters\ Value Name: RequireSignOrSeal Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-205822`

### Rule: Windows Server 2019 setting Domain member: Digitally encrypt secure channel data (when possible) must be configured to enabled.

**Rule ID:** `SV-205822r916422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Requests sent on the secure channel are authenticated, and sensitive information (such as passwords) is encrypted, but not all information is encrypted. If this policy is enabled, outgoing secure channel traffic will be encrypted. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Netlogon\Parameters\ Value Name: SealSecureChannel Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-205823`

### Rule: Windows Server 2019 setting Domain member: Digitally sign secure channel data (when possible) must be configured to Enabled.

**Rule ID:** `SV-205823r916422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Requests sent on the secure channel are authenticated, and sensitive information (such as passwords) is encrypted, but the channel is not integrity checked. If this policy is enabled, outgoing secure channel traffic will be signed. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Netlogon\Parameters\ Value Name: SignSecureChannel Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-205824`

### Rule: Windows Server 2019 must be configured to require a strong session key.

**Rule ID:** `SV-205824r916422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A computer connecting to a domain controller will establish a secure channel. The secure channel connection may be subject to compromise, such as hijacking or eavesdropping, if strong session keys are not used to establish the connection. Requiring strong session keys enforces 128-bit encryption between systems. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Netlogon\Parameters\ Value Name: RequireStrongKey Value Type: REG_DWORD Value: 0x00000001 (1) This setting may prevent a system from being joined to a domain if not configured consistently between systems.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-205825`

### Rule: Windows Server 2019 setting Microsoft network client: Digitally sign communications (always) must be configured to Enabled.

**Rule ID:** `SV-205825r916422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The server message block (SMB) protocol provides the basis for many network operations. Digitally signed SMB packets aid in preventing man-in-the-middle attacks. If this policy is enabled, the SMB client will only communicate with an SMB server that performs SMB packet signing. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters\ Value Name: RequireSecuritySignature Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-205826`

### Rule: Windows Server 2019 setting Microsoft network client: Digitally sign communications (if server agrees) must be configured to Enabled.

**Rule ID:** `SV-205826r916422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The server message block (SMB) protocol provides the basis for many network operations. If this policy is enabled, the SMB client will request packet signing when communicating with an SMB server that is enabled or required to perform SMB packet signing. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters\ Value Name: EnableSecuritySignature Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-205827`

### Rule: Windows Server 2019 setting Microsoft network server: Digitally sign communications (always) must be configured to Enabled.

**Rule ID:** `SV-205827r916422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The server message block (SMB) protocol provides the basis for many network operations. Digitally signed SMB packets aid in preventing man-in-the-middle attacks. If this policy is enabled, the SMB server will only communicate with an SMB client that performs SMB packet signing. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\LanManServer\Parameters\ Value Name: RequireSecuritySignature Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-205828`

### Rule: Windows Server 2019 setting Microsoft network server: Digitally sign communications (if client agrees) must be configured to Enabled.

**Rule ID:** `SV-205828r916422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The server message block (SMB) protocol provides the basis for many network operations. Digitally signed SMB packets aid in preventing man-in-the-middle attacks. If this policy is enabled, the SMB server will negotiate SMB packet signing as requested by the client. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\LanManServer\Parameters\ Value Name: EnableSecuritySignature Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000425-GPOS-00189

**Group ID:** `V-205829`

### Rule: Windows Server 2019 must implement protection methods such as TLS, encrypted VPNs, or IPsec if the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process.

**Rule ID:** `SV-205829r852531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Ensuring the confidentiality of transmitted information requires the operating system to take measures in preparing information for transmission. This can be accomplished via access control and encryption. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, operating systems need to support transmission protection mechanisms such as TLS, encrypted VPNs, or IPsec. Satisfies: SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process, verify protection methods such as TLS, encrypted VPNs, or IPsec have been implemented. If protection methods have not been implemented, this is a finding.

## Group: SRG-OS-000433-GPOS-00192

**Group ID:** `V-205830`

### Rule: Windows Server 2019 Explorer Data Execution Prevention must be enabled.

**Rule ID:** `SV-205830r852532_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data Execution Prevention provides additional protection by performing checks on memory to help prevent malicious code from running. This setting will prevent Data Execution Prevention from being turned off for File Explorer.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default behavior is for Data Execution Prevention to be turned on for File Explorer. If the registry value name below does not exist, this is not a finding. If it exists and is configured with a value of "0", this is not a finding. If it exists and is configured with a value of "1", this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\Explorer\ Value Name: NoDataExecutionPrevention Value Type: REG_DWORD Value: 0x00000000 (0) (or if the Value Name does not exist)

## Group: SRG-OS-000470-GPOS-00214

**Group ID:** `V-205832`

### Rule: Windows Server 2019 must be configured to audit Account Logon - Credential Validation successes.

**Rule ID:** `SV-205832r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Credential Validation records events related to validation tests on credentials for a user account logon.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Account Logon >> Credential Validation - Success

## Group: SRG-OS-000470-GPOS-00214

**Group ID:** `V-205833`

### Rule: Windows Server 2019 must be configured to audit Account Logon - Credential Validation failures.

**Rule ID:** `SV-205833r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Credential Validation records events related to validation tests on credentials for a user account logon.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Account Logon >> Credential Validation - Failure

## Group: SRG-OS-000470-GPOS-00214

**Group ID:** `V-205834`

### Rule: Windows Server 2019 must be configured to audit Logon/Logoff - Group Membership successes.

**Rule ID:** `SV-205834r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Audit Group Membership records information related to the group membership of a user's logon token.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Logon/Logoff >> Group Membership - Success

## Group: SRG-OS-000470-GPOS-00214

**Group ID:** `V-205835`

### Rule: Windows Server 2019 must be configured to audit Logon/Logoff - Special Logon successes.

**Rule ID:** `SV-205835r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Special Logon records special logons that have administrative privileges and can be used to elevate processes. Satisfies: SRG-OS-000470-GPOS-00214, SRG-OS-000472-GPOS-00217, SRG-OS-000473-GPOS-00218, SRG-OS-000475-GPOS-00220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Logon/Logoff >> Special Logon - Success

## Group: SRG-OS-000470-GPOS-00214

**Group ID:** `V-205836`

### Rule: Windows Server 2019 must be configured to audit Object Access - Other Object Access Events successes.

**Rule ID:** `SV-205836r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Auditing for other object access records events related to the management of task scheduler jobs and COM+ objects.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Object Access >> Other Object Access Events - Success

## Group: SRG-OS-000470-GPOS-00214

**Group ID:** `V-205837`

### Rule: Windows Server 2019 must be configured to audit Object Access - Other Object Access Events failures.

**Rule ID:** `SV-205837r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Auditing for other object access records events related to the management of task scheduler jobs and COM+ objects.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Object Access >> Other Object Access Events - Failure

## Group: SRG-OS-000472-GPOS-00217

**Group ID:** `V-205838`

### Rule: Windows Server 2019 must be configured to audit logoff successes.

**Rule ID:** `SV-205838r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Logoff records user logoffs. If this is an interactive logoff, it is recorded on the local system. If it is to a network share, it is recorded on the system accessed. Satisfies: SRG-OS-000472-GPOS-00217, SRG-OS-000480-GPOS-00227</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Logon/Logoff >> Logoff - Success

## Group: SRG-OS-000474-GPOS-00219

**Group ID:** `V-205839`

### Rule: Windows Server 2019 must be configured to audit Detailed Tracking - Plug and Play Events successes.

**Rule ID:** `SV-205839r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Plug and Play activity records events related to the successful connection of external devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Detailed Tracking >> Plug and Play Events - Success

## Group: SRG-OS-000474-GPOS-00219

**Group ID:** `V-205840`

### Rule: Windows Server 2019 must be configured to audit Object Access - Removable Storage successes.

**Rule ID:** `SV-205840r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Removable Storage auditing under Object Access records events related to access attempts on file system objects on removable storage devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Object Access >> Removable Storage - Success Virtual machines or systems that use network attached storage may generate excessive audit events for secondary virtual drives or the network attached storage when this setting is enabled. This may be set to Not Configured in such cases and would not be a finding.

## Group: SRG-OS-000474-GPOS-00219

**Group ID:** `V-205841`

### Rule: Windows Server 2019 must be configured to audit Object Access - Removable Storage failures.

**Rule ID:** `SV-205841r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Removable Storage auditing under Object Access records events related to access attempts on file system objects on removable storage devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN19-SO-000050) for the detailed auditing subcategories to be effective. Use the "AuditPol" tool to review the current Audit Policy configuration: Open "PowerShell" or a "Command Prompt" with elevated privileges ("Run as administrator"). Enter "AuditPol /get /category:*" Compare the "AuditPol" settings with the following: If the system does not audit the following, this is a finding. Object Access >> Removable Storage - Failure Virtual machines or systems that use network attached storage may generate excessive audit events for secondary virtual drives or the network attached storage when this setting is enabled. This may be set to Not Configured in such cases and would not be a finding.

## Group: SRG-OS-000478-GPOS-00223

**Group ID:** `V-205842`

### Rule: Windows Server 2019 must be configured to use FIPS-compliant algorithms for encryption, hashing, and signing.

**Rule ID:** `SV-205842r877466_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting ensures the system uses algorithms that are FIPS-compliant for encryption, hashing, and signing. FIPS-compliant algorithms meet specific standards established by the U.S. Government and must be the algorithms used for all OS encryption functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\FIPSAlgorithmPolicy\ Value Name: Enabled Value Type: REG_DWORD Value: 0x00000001 (1) Clients with this setting enabled will not be able to communicate via digitally encrypted or signed protocols with servers that do not support these algorithms. Both the browser and web server must be configured to use TLS; otherwise. the browser will not be able to connect to a secure site.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-205843`

### Rule: Windows Server 2019 must, at a minimum, offload audit records of interconnected systems in real time and offload standalone or nondomain-joined systems weekly.

**Rule ID:** `SV-205843r916198_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of log data includes ensuring the log data is not accidentally lost or deleted. Audit information stored in one location is vulnerable to accidental or incidental deletion or alteration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit records, at a minimum, are offloaded for interconnected systems in real time and offloaded for standalone or nondomain-joined systems weekly. If they are not, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205844`

### Rule: Windows Server 2019 users with Administrative privileges must have separate accounts for administrative duties and normal operational tasks.

**Rule ID:** `SV-205844r569188_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Using a privileged account to perform routine functions makes the computer vulnerable to malicious software inadvertently introduced during a session that has been granted full privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify each user with administrative privileges has been assigned a unique administrative account separate from their standard user account. If users with administrative privileges do not have separate accounts for administrative functions and standard user functions, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205845`

### Rule: Windows Server 2019 administrative accounts must not be used with applications that access the Internet, such as web browsers, or with potential Internet sources, such as email.

**Rule ID:** `SV-205845r569188_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Using applications that access the Internet or have potential Internet sources using administrative privileges exposes a system to compromise. If a flaw in an application is exploited while running as a privileged user, the entire system could be compromised. Web browsers and email are common attack vectors for introducing malicious code and must not be run with an administrative account. Since administrative accounts may generally change or work around technical restrictions for running a web browser or other applications, it is essential that policy require administrative accounts to not access the Internet or use applications such as email. The policy should define specific exceptions for local service administration. These exceptions may include HTTP(S)-based tools that are used for the administration of the local system, services, or attached devices. Whitelisting can be used to enforce the policy to ensure compliance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine whether organization policy, at a minimum, prohibits administrative accounts from using applications that access the Internet, such as web browsers, or with potential Internet sources, such as email, except as necessary for local service administration. If it does not, this is a finding. The organization may use technical means such as whitelisting to prevent the use of browsers and mail applications to enforce this requirement.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205846`

### Rule: Windows Server 2019 members of the Backup Operators group must have separate accounts for backup duties and normal operational tasks.

**Rule ID:** `SV-205846r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Backup Operators are able to read and write to any file in the system, regardless of the rights assigned to it. Backup and restore rights permit users to circumvent the file access restrictions present on NTFS disk drives for backup and restore purposes. Members of the Backup Operators group must have separate logon accounts for performing backup duties.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If no accounts are members of the Backup Operators group, this is NA. Verify users with accounts in the Backup Operators group have a separate user account for backup functions and for performing normal user tasks. If users with accounts in the Backup Operators group do not have separate accounts for backup functions and standard user functions, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205847`

### Rule: Windows Server 2019 manually managed application account passwords must be changed at least annually or when a system administrator with knowledge of the password leaves the organization.

**Rule ID:** `SV-205847r857288_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting application account passwords to expire may cause applications to stop functioning. However, not changing them on a regular basis exposes them to attack. If managed service accounts are used, this alleviates the need to manually change application account passwords.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if manually managed application/service accounts exist. If none exist, this is NA. If passwords for manually managed application/service accounts are not changed at least annually or when an administrator with knowledge of the password leaves the organization, this is a finding. Identify manually managed application/service accounts. To determine the date a password was last changed: Domain controllers: Open "PowerShell". Enter "Get-AdUser -Identity [application account name] -Properties PasswordLastSet | FT Name, PasswordLastSet", where [application account name] is the name of the manually managed application/service account. If the "PasswordLastSet" date is more than one year old, this is a finding. Member servers and standalone or nondomain-joined systems: Open "Command Prompt". Enter 'Net User [application account name] | Find /i "Password Last Set"', where [application account name] is the name of the manually managed application/service account. If the "Password Last Set" date is more than one year old, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205848`

### Rule: Windows Server 2019 domain-joined systems must have a Trusted Platform Module (TPM) enabled and ready for use.

**Rule ID:** `SV-205848r902429_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Credential Guard uses virtualization-based security to protect data that could be used in credential theft attacks if compromised. A number of system requirements must be met in order for Credential Guard to be configured and enabled properly. Without a TPM enabled and ready for use, Credential Guard keys are stored in a less secure method using software.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For standalone or nondomain-joined systems, this is NA. Verify the system has a TPM and it is ready for use. Run "tpm.msc". Review the sections in the center pane. "Status" must indicate it has been configured with a message such as "The TPM is ready for use" or "The TPM is on and ownership has been taken". TPM Manufacturer Information - Specific Version = 2.0 or 1.2 If a TPM is not found or is not ready for use, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205849`

### Rule: Windows Server 2019 must be maintained at a supported servicing level.

**Rule ID:** `SV-205849r569188_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Systems at unsupported servicing levels will not receive security updates for new vulnerabilities, which leave them subject to exploitation. Systems must be maintained at a servicing level supported by the vendor with new security updates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open "Command Prompt". Enter "winver.exe". If the "About Windows" dialog box does not display "Microsoft Windows Server Version 1809 (Build 17763.xxx)" or greater, this is a finding. Preview versions must not be used in a production environment.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205850`

### Rule: Windows Server 2019 must use an anti-virus program.

**Rule ID:** `SV-205850r569245_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Malicious software can establish a base on individual desktops and servers. Employing an automated mechanism to detect this type of software will aid in elimination of the software from the operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an anti-virus solution is installed on the system. The anti-virus solution may be bundled with an approved host-based security solution. If there is no anti-virus solution installed on the system, this is a finding. Verify if Windows Defender is in use or enabled: Open "PowerShell". Enter “get-service | where {$_.DisplayName -Like "*Defender*"} | Select Status,DisplayName” Verify if third-party anti-virus is in use or enabled: Open "PowerShell". Enter "get-service | where {$_.DisplayName -Like "*mcafee*"} | Select Status,DisplayName” Enter "get-service | where {$_.DisplayName -Like "*symantec*"} | Select Status,DisplayName”

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205851`

### Rule: Windows Server 2019 must have a host-based intrusion detection or prevention system.

**Rule ID:** `SV-205851r793214_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A properly configured Host-based Intrusion Detection System (HIDS) or Host-based Intrusion Prevention System (HIPS) provides another level of defense against unauthorized access to critical servers. With proper configuration and logging enabled, such a system can stop and/or alert for many attempts to gain unauthorized access to resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine whether there is a HIDS or HIPS on each server. If the HIPS component of ESS is installed and active on the host and the alerts of blocked activity are being logged and monitored, this meets the requirement. A HIDS device is not required on a system that has the role as the Network Intrusion Device (NID). However, this exception needs to be documented with the ISSO. If a HIDS is not installed on the system, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205852`

### Rule: Windows Server 2019 must have software certificate installation files removed.

**Rule ID:** `SV-205852r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of software certificates and their accompanying installation files for end users to access resources is less secure than the use of hardware-based certificates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Search all drives for *.p12 and *.pfx files. If any files with these extensions exist, this is a finding. This does not apply to server-based applications that have a requirement for .p12 certificate files or Adobe PreFlight certificate files. Some applications create files with extensions of .p12 that are not certificate installation files. Removal of non-certificate installation files from systems is not required. These must be documented with the ISSO.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205853`

### Rule: Windows Server 2019 FTP servers must be configured to prevent anonymous logons.

**Rule ID:** `SV-205853r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The FTP service allows remote users to access shared files and directories. Allowing anonymous FTP connections makes user auditing difficult. Using accounts that have administrator privileges to log on to FTP risks that the userid and password will be captured on the network and give administrator access to an unauthorized user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If FTP is not installed on the system, this is NA. Open "Internet Information Services (IIS) Manager". Select the server. Double-click "FTP Authentication". If the "Anonymous Authentication" status is "Enabled", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205854`

### Rule: Windows Server 2019 FTP servers must be configured to prevent access to the system drive.

**Rule ID:** `SV-205854r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The FTP service allows remote users to access shared files and directories that could provide access to system resources and compromise the system, especially if the user can gain access to the root directory of the boot drive.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If FTP is not installed on the system, this is NA. Open "Internet Information Services (IIS) Manager". Select "Sites" under the server name. For any sites with a Binding that lists FTP, right-click the site and select "Explore". If the site is not defined to a specific folder for shared FTP resources, this is a finding. If the site includes any system areas such as root of the drive, Program Files, or Windows directories, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205855`

### Rule: Windows Server 2019 must have orphaned security identifiers (SIDs) removed from user rights.

**Rule ID:** `SV-205855r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accounts or groups given rights on a system may show up as unresolved SIDs for various reasons including deletion of the accounts or groups. If the account or group objects are reanimated, there is a potential they may still have rights no longer intended. Valid domain accounts or groups may also show up as unresolved SIDs if a connection to the domain cannot be established for some reason.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the effective User Rights setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. Review each User Right listed for any unresolved SIDs to determine whether they are valid, such as due to being temporarily disconnected from the domain. (Unresolved SIDs have the format that begins with "*S-1-".) If any unresolved SIDs exist and are not for currently valid accounts or groups, this is a finding. For server core installations, run the following command: Secedit /export /areas USER_RIGHTS /cfg c:\path\UserRights.txt The results in the file identify user right assignments by SID instead of group name. Review the SIDs for unidentified ones. A list of typical SIDs \ Groups is below, search Microsoft for articles on well-known SIDs for others. If any unresolved SIDs exist and are not for currently valid accounts or groups, this is a finding. SID - Group S-1-5-11 - Authenticated Users S-1-5-113 - Local account S-1-5-114 - Local account and member of Administrators group S-1-5-19 - Local Service S-1-5-20 - Network Service S-1-5-32-544 - Administrators S-1-5-32-546 - Guests S-1-5-6 - Service S-1-5-9 - Enterprise Domain Controllers S-1-5-domain-512 - Domain Admins S-1-5-root domain-519 - Enterprise Admins S-1-5-80-3139157870-2983391045-3678747466-658725712-1809340420 - NT Service\WdiServiceHost

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205856`

### Rule: Windows Server 2019 systems must have Unified Extensible Firmware Interface (UEFI) firmware and be configured to run in UEFI mode, not Legacy BIOS.

**Rule ID:** `SV-205856r569188_rule`
**Severity:** low

**Description:**
<VulnDiscussion>UEFI provides additional security features in comparison to legacy BIOS firmware, including Secure Boot. UEFI is required to support additional security features in Windows, including Virtualization Based Security and Credential Guard. Systems with UEFI that are operating in "Legacy BIOS" mode will not support these security features.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Some older systems may not have UEFI firmware. This is currently a CAT III; it will be raised in severity at a future date when broad support of Windows hardware and firmware requirements are expected to be met. Devices that have UEFI firmware must run in "UEFI" mode. Verify the system firmware is configured to run in "UEFI" mode, not "Legacy BIOS". Run "System Information". Under "System Summary", if "BIOS Mode" does not display "UEFI", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205857`

### Rule: Windows Server 2019 must have Secure Boot enabled.

**Rule ID:** `SV-205857r569188_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Secure Boot is a standard that ensures systems boot only to a trusted operating system. Secure Boot is required to support additional security features in Windows, including Virtualization Based Security and Credential Guard. If Secure Boot is turned off, these security features will not function.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Some older systems may not have UEFI firmware. This is currently a CAT III; it will be raised in severity at a future date when broad support of Windows hardware and firmware requirements are expected to be met. Devices that have UEFI firmware must have Secure Boot enabled. Run "System Information". Under "System Summary", if "Secure Boot State" does not display "On", this is a finding. On server core installations, run the following PowerShell command: Confirm-SecureBootUEFI If a value of "True" is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205858`

### Rule: Windows Server 2019 Internet Protocol version 6 (IPv6) source routing must be configured to the highest protection level to prevent IP source routing.

**Rule ID:** `SV-205858r569188_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Configuring the system to disable IPv6 source routing protects against spoofing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Tcpip6\Parameters\ Value Name: DisableIPSourceRouting Type: REG_DWORD Value: 0x00000002 (2)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205859`

### Rule: Windows Server 2019 source routing must be configured to the highest protection level to prevent Internet Protocol (IP) source routing.

**Rule ID:** `SV-205859r569188_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Configuring the system to disable IP source routing protects against spoofing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\ Value Name: DisableIPSourceRouting Value Type: REG_DWORD Value: 0x00000002 (2)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205860`

### Rule: Windows Server 2019 must be configured to prevent Internet Control Message Protocol (ICMP) redirects from overriding Open Shortest Path First (OSPF)-generated routes.

**Rule ID:** `SV-205860r569188_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Allowing ICMP redirect of routes can lead to traffic not being routed properly. When disabled, this forces ICMP to be routed via the shortest path first.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\ Value Name: EnableICMPRedirect Value Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205861`

### Rule: Windows Server 2019 insecure logons to an SMB server must be disabled.

**Rule ID:** `SV-205861r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Insecure guest logons allow unauthenticated access to shared folders. Shared resources on a system must require authentication to establish proper access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\LanmanWorkstation\ Value Name: AllowInsecureGuestAuth Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205862`

### Rule: Windows Server 2019 hardened Universal Naming Convention (UNC) paths must be defined to require mutual authentication and integrity for at least the \\*\SYSVOL and \\*\NETLOGON shares.

**Rule ID:** `SV-205862r857311_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Additional security requirements are applied to UNC paths specified in hardened UNC paths before allowing access to them. This aids in preventing tampering with or spoofing of connections to these paths.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is applicable to domain-joined systems. For standalone or nondomain-joined systems, this is NA. If the following registry values do not exist or are not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\NetworkProvider\HardenedPaths\ Value Name: \\*\NETLOGON Value Type: REG_SZ Value: RequireMutualAuthentication=1, RequireIntegrity=1 Value Name: \\*\SYSVOL Value Type: REG_SZ Value: RequireMutualAuthentication=1, RequireIntegrity=1 Additional entries would not be a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205863`

### Rule: Windows Server 2019 must be configured to enable Remote host allows delegation of non-exportable credentials.

**Rule ID:** `SV-205863r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An exportable version of credentials is provided to remote hosts when using credential delegation which exposes them to theft on the remote host. Restricted Admin mode or Remote Credential Guard allow delegation of non-exportable credentials providing additional protection of the credentials. Enabling this configures the host to support Restricted Admin mode or Remote Credential Guard.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\CredentialsDelegation\ Value Name: AllowProtectedCreds Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205864`

### Rule: Windows Server 2019 virtualization-based security must be enabled with the platform security level configured to Secure Boot or Secure Boot with DMA Protection.

**Rule ID:** `SV-205864r902431_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Virtualization-based security (VBS) provides the platform for the additional security features Credential Guard and virtualization-based protection of code integrity. Secure Boot is the minimum security level, with DMA protection providing additional memory protection. DMA Protection requires a CPU that supports input/output memory management unit (IOMMU).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For standalone or nondomain-joined systems, this is NA. Open "PowerShell" with elevated privileges (run as administrator). Enter the following: "Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard" If "RequiredSecurityProperties" does not include a value of "2" indicating "Secure Boot" (e.g., "{1, 2}"), this is a finding. If "Secure Boot and DMA Protection" is configured, "3" will also be displayed in the results (e.g., "{1, 2, 3}"). If "VirtualizationBasedSecurityStatus" is not a value of "2" indicating "Running", this is a finding. Alternately: Run "System Information". Under "System Summary", verify the following: If "Virtualization based security" does not display "Running", this is a finding. If "Virtualization based Required security Properties" does not display "Base Virtualization Support, Secure Boot", this is a finding. If "Secure Boot and DMA Protection" is configured, "DMA Protection" will also be displayed (e.g., "Base Virtualization Support, Secure Boot, DMA Protection"). The policy settings referenced in the Fix section will configure the following registry values. However, due to hardware requirements, the registry values alone do not ensure proper function. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\DeviceGuard\ Value Name: EnableVirtualizationBasedSecurity Value Type: REG_DWORD Value: 0x00000001 (1) Value Name: RequirePlatformSecurityFeatures Value Type: REG_DWORD Value: 0x00000001 (1) (Secure Boot only) or 0x00000003 (3) (Secure Boot and DMA Protection) A Microsoft TechNet article on Credential Guard, including system requirement details, can be found at the following link: https://technet.microsoft.com/itpro/windows/keep-secure/credential-guard

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205865`

### Rule: Windows Server 2019 Early Launch Antimalware, Boot-Start Driver Initialization Policy must prevent boot drivers identified as bad.

**Rule ID:** `SV-205865r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Compromised boot drivers can introduce malware prior to protection mechanisms that load after initialization. The Early Launch Antimalware driver can limit allowed drivers based on classifications determined by the malware protection application. At a minimum, drivers determined to be bad must not be allowed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default behavior is for Early Launch Antimalware - Boot-Start Driver Initialization policy to enforce "Good, unknown and bad but critical" (preventing "bad"). If the registry value name below does not exist, this is not a finding. If it exists and is configured with a value of "0x00000007 (7)", this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Policies\EarlyLaunch\ Value Name: DriverLoadPolicy Value Type: REG_DWORD Value: 0x00000001 (1), 0x00000003 (3), or 0x00000008 (8) (or if the Value Name does not exist) Possible values for this setting are: 8 - Good only 1 - Good and unknown 3 - Good, unknown and bad but critical 7 - All (which includes "bad" and would be a finding)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205866`

### Rule: Windows Server 2019 group policy objects must be reprocessed even if they have not changed.

**Rule ID:** `SV-205866r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Registry entries for group policy settings can potentially be changed from the required configuration. This could occur as part of troubleshooting or by a malicious process on a compromised system. Enabling this setting and then selecting the "Process even if the Group Policy objects have not changed" option ensures the policies will be reprocessed even if none have been changed. This way, any unauthorized changes are forced to match the domain-based group policy settings again.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\Group Policy\{35378EAC-683F-11D2-A89A-00C04FBBCFA2}\ Value Name: NoGPOListChanges Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205867`

### Rule: Windows Server 2019 users must be prompted to authenticate when the system wakes from sleep (on battery).

**Rule ID:** `SV-205867r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A system that does not require authentication when resuming from sleep may provide access to unauthorized users. Authentication must always be required when accessing a system. This setting ensures users are prompted for a password when the system wakes from sleep (on battery).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Power\PowerSettings\0e796bdb-100d-47d6-a2d5-f7d2daa51f51\ Value Name: DCSettingIndex Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205868`

### Rule: Windows Server 2019 users must be prompted to authenticate when the system wakes from sleep (plugged in).

**Rule ID:** `SV-205868r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A system that does not require authentication when resuming from sleep may provide access to unauthorized users. Authentication must always be required when accessing a system. This setting ensures users are prompted for a password when the system wakes from sleep (plugged in).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Power\PowerSettings\0e796bdb-100d-47d6-a2d5-f7d2daa51f51\ Value Name: ACSettingIndex Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205869`

### Rule: Windows Server 2019 Telemetry must be configured to Security or Basic.

**Rule ID:** `SV-205869r921945_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some features may communicate with the vendor, sending system information or downloading data or components for the feature. Limiting this capability will prevent potentially sensitive information from being sent outside the enterprise. The "Security" option for Telemetry configures the lowest amount of data, effectively none outside of the Malicious Software Removal Tool (MSRT), Defender, and telemetry client settings. "Basic" sends basic diagnostic and usage data and may be required to support some Microsoft services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\DataCollection\ Value Name: AllowTelemetry Type: REG_DWORD Value: 0x00000000 (0) (Security), 0x00000001 (1) (Basic)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205870`

### Rule: Windows Server 2019 Windows Update must not obtain updates from other PCs on the Internet.

**Rule ID:** `SV-205870r569188_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Windows Update can obtain updates from additional sources instead of Microsoft. In addition to Microsoft, updates can be obtained from and sent to PCs on the local network as well as on the Internet. This is part of the Windows Update trusted process, however to minimize outside exposure, obtaining updates from or sending to systems on the Internet must be prevented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\DeliveryOptimization\ Value Name: DODownloadMode Value Type: REG_DWORD Value: 0x00000000 (0) - No peering (HTTP Only) 0x00000001 (1) - Peers on same NAT only (LAN) 0x00000002 (2) - Local Network / Private group peering (Group) 0x00000063 (99) - Simple download mode, no peering (Simple) 0x00000064 (100) - Bypass mode, Delivery Optimization not used (Bypass) A value of 0x00000003 (3), Internet, is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205871`

### Rule: Windows Server 2019 Turning off File Explorer heap termination on corruption must be disabled.

**Rule ID:** `SV-205871r569188_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Legacy plug-in applications may continue to function when a File Explorer session has become corrupt. Disabling this feature will prevent this.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default behavior is for File Explorer heap termination on corruption to be enabled. If the registry Value Name below does not exist, this is not a finding. If it exists and is configured with a value of "0", this is not a finding. If it exists and is configured with a value of "1", this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\Explorer\ Value Name: NoHeapTerminationOnCorruption Value Type: REG_DWORD Value: 0x00000000 (0) (or if the Value Name does not exist)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205872`

### Rule: Windows Server 2019 File Explorer shell protocol must run in protected mode.

**Rule ID:** `SV-205872r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shell protocol will limit the set of folders that applications can open when run in protected mode. Restricting files an application can open to a limited set of folders increases the security of Windows.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default behavior is for shell protected mode to be turned on for File Explorer. If the registry value name below does not exist, this is not a finding. If it exists and is configured with a value of "0", this is not a finding. If it exists and is configured with a value of "1", this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\ Value Name: PreXPSP2ShellProtocolBehavior Value Type: REG_DWORD Value: 0x00000000 (0) (or if the Value Name does not exist)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205873`

### Rule: Windows Server 2019 must prevent attachments from being downloaded from RSS feeds.

**Rule ID:** `SV-205873r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Attachments from RSS feeds may not be secure. This setting will prevent attachments from being downloaded from RSS feeds.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Internet Explorer\Feeds\ Value Name: DisableEnclosureDownload Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205874`

### Rule: Windows Server 2019 users must be notified if a web-based program attempts to install software.

**Rule ID:** `SV-205874r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web-based programs may attempt to install malicious software on a system. Ensuring users are notified if a web-based program attempts to install software allows them to refuse the installation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default behavior is for Internet Explorer to warn users and select whether to allow or refuse installation when a web-based program attempts to install software on the system. If the registry value name below does not exist, this is not a finding. If it exists and is configured with a value of "0", this is not a finding. If it exists and is configured with a value of "1", this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\Installer\ Value Name: SafeForScripting Value Type: REG_DWORD Value: 0x00000000 (0) (or if the Value Name does not exist)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205875`

### Rule: Windows Server 2019 directory data (outside the root DSE) of a non-public directory must be configured to prevent anonymous access.

**Rule ID:** `SV-205875r569188_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To the extent that anonymous access to directory data (outside the root DSE) is permitted, read access control of the data is effectively disabled. If other means of controlling access (such as network restrictions) are compromised, there may be nothing else to protect the confidentiality of sensitive directory data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. Open "Command Prompt" (not elevated). Run "ldp.exe". From the "Connection menu", select "Bind". Clear the User, Password, and Domain fields. Select "Simple bind" for the Bind type and click "OK". Confirmation of anonymous access will be displayed at the end: res = ldap_simple_bind_s Authenticated as: 'NT AUTHORITY\ANONYMOUS LOGON' From the "Browse" menu, select "Search". In the Search dialog, enter the DN of the domain naming context (generally something like "dc=disaost,dc=mil") in the Base DN field. Clear the Attributes field and select "Run". Error messages should display related to Bind and user not authenticated. If attribute data is displayed, anonymous access is enabled to the domain naming context and this is a finding. The following network controls allow the finding severity to be downgraded to a CAT II since these measures lower the risk associated with anonymous access. Network hardware ports at the site are subject to 802.1x authentication or MAC address restrictions. Premise firewall or host restrictions prevent access to ports 389, 636, 3268, and 3269 from client hosts not explicitly identified by domain (.mil) or IP address.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205876`

### Rule: Windows Server 2019 domain controllers must be configured to allow reset of machine account passwords.

**Rule ID:** `SV-205876r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling this setting on all domain controllers in a domain prevents domain members from changing their computer account passwords. If these passwords are weak or compromised, the inability to change them may leave these computers vulnerable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to domain controllers. It is NA for other systems. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Netlogon\Parameters\ Value Name: RefusePasswordChange Value Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205877`

### Rule: The password for the krbtgt account on a domain must be reset at least every 180 days.

**Rule ID:** `SV-205877r857315_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The krbtgt account acts as a service account for the Kerberos Key Distribution Center (KDC) service. The account and password are created when a domain is created and the password is typically not changed. If the krbtgt account is compromised, attackers can create valid Kerberos Ticket Granting Tickets (TGT). The password must be changed twice to effectively remove the password history. Changing once, waiting for replication to complete and the amount of time equal to or greater than the maximum Kerberos ticket lifetime, and changing again reduces the risk of issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is applicable to domain controllers; it is NA for other systems. Open "Windows PowerShell". Enter "Get-ADUser krbtgt -Property PasswordLastSet". If the "PasswordLastSet" date is more than 180 days old, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205906`

### Rule: Windows Server 2019 must limit the caching of logon credentials to four or less on domain-joined member servers.

**Rule ID:** `SV-205906r857326_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The default Windows configuration caches the last logon credentials for users who log on interactively to a system. This feature is provided for system availability reasons, such as the user's machine being disconnected from the network or domain controllers being unavailable. Even though the credential cache is well protected, if a system is attacked, an unauthorized individual may isolate the password to a domain user account using a password-cracking program and gain access to the domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This applies to member servers. For domain controllers and standalone or nondomain-joined systems, this is NA. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\ Value Name: CachedLogonsCount Value Type: REG_SZ Value: 4 (or less)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205907`

### Rule: Windows Server 2019 must be running Credential Guard on domain-joined member servers.

**Rule ID:** `SV-205907r857344_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Credential Guard uses virtualization-based security to protect data that could be used in credential theft attacks if compromised. This authentication information, which was stored in the Local Security Authority (LSA) in previous versions of Windows, is isolated from the rest of operating system and can only be accessed by privileged system software.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For domain controllers and standalone or nondomain-joined systems, this is NA. Open "PowerShell" with elevated privileges (run as administrator). Enter the following: "Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard" If "SecurityServicesRunning" does not include a value of "1" (e.g., "{1, 2}"), this is a finding. Alternately: Run "System Information". Under "System Summary", verify the following: If "Device Guard Security Services Running" does not list "Credential Guard", this is a finding. The policy settings referenced in the Fix section will configure the following registry value. However, due to hardware requirements, the registry value alone does not ensure proper function. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\DeviceGuard\ Value Name: LsaCfgFlags Value Type: REG_DWORD Value: 0x00000001 (1) (Enabled with UEFI lock) A Microsoft article on Credential Guard system requirement can be found at the following link: https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205908`

### Rule: Windows Server 2019 must prevent local accounts with blank passwords from being used from the network.

**Rule ID:** `SV-205908r569188_rule`
**Severity:** high

**Description:**
<VulnDiscussion>An account without a password can allow unauthorized access to a system as only the username would be required. Password policies should prevent accounts with blank passwords from existing on a system. However, if a local account with a blank password does exist, enabling this setting will prevent network access, limiting the account to local console logon only.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\ Value Name: LimitBlankPasswordUse Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205909`

### Rule: Windows Server 2019 built-in administrator account must be renamed.

**Rule ID:** `SV-205909r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The built-in administrator account is a well-known account subject to attack. Renaming this account to an unidentified name improves the protection of this account and the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> Security Options. If the value for "Accounts: Rename administrator account" is not set to a value other than "Administrator", this is a finding. For server core installations, run the following command: Secedit /Export /Areas SecurityPolicy /CFG C:\Path\FileName.Txt If "NewAdministratorName" is not something other than "Administrator" in the file, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205910`

### Rule: Windows Server 2019 built-in guest account must be renamed.

**Rule ID:** `SV-205910r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The built-in guest account is a well-known user account on all Windows systems and, as initially installed, does not require a password. This can allow access to system resources by unauthorized users. Renaming this account to an unidentified name improves the protection of this account and the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> Security Options. If the value for "Accounts: Rename guest account" is not set to a value other than "Guest", this is a finding. For server core installations, run the following command: Secedit /Export /Areas SecurityPolicy /CFG C:\Path\FileName.Txt If "NewGuestName" is not something other than "Guest" in the file, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205911`

### Rule: Windows Server 2019 maximum age for machine account passwords must be configured to 30 days or less.

**Rule ID:** `SV-205911r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Computer account passwords are changed automatically on a regular basis. This setting controls the maximum password age that a machine account may have. This must be set to no more than 30 days, ensuring the machine changes its password monthly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is the default configuration for this setting (30 days). If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Netlogon\Parameters\ Value Name: MaximumPasswordAge Value Type: REG_DWORD Value: 0x0000001e (30) (or less, but not 0)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205912`

### Rule: Windows Server 2019 Smart Card removal option must be configured to Force Logoff or Lock Workstation.

**Rule ID:** `SV-205912r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unattended systems are susceptible to unauthorized use and must be locked. Configuring a system to lock when a smart card is removed will ensure the system is inaccessible when unattended.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\ Value Name: scremoveoption Value Type: REG_SZ Value: 1 (Lock Workstation) or 2 (Force Logoff) If configuring this on servers causes issues, such as terminating users' remote sessions, and the organization has a policy in place that any other sessions on the servers, such as administrative console logons, are manually locked or logged off when unattended or not in use, this would be acceptable. This must be documented with the ISSO.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205913`

### Rule: Windows Server 2019 must not allow anonymous SID/Name translation.

**Rule ID:** `SV-205913r569188_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Allowing anonymous SID/Name translation can provide sensitive information for accessing a system. Only authorized users must be able to perform such translations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> Security Options. If the value for "Network access: Allow anonymous SID/Name translation" is not set to "Disabled", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205914`

### Rule: Windows Server 2019 must not allow anonymous enumeration of Security Account Manager (SAM) accounts.

**Rule ID:** `SV-205914r569188_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Anonymous enumeration of SAM accounts allows anonymous logon users (null session connections) to list all accounts names, thus providing a list of potential points to attack the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\ Value Name: RestrictAnonymousSAM Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205915`

### Rule: Windows Server 2019 must be configured to prevent anonymous users from having the same permissions as the Everyone group.

**Rule ID:** `SV-205915r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access by anonymous users must be restricted. If this setting is enabled, anonymous users have the same rights and permissions as the built-in Everyone group. Anonymous users must not have these permissions or rights.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\ Value Name: EveryoneIncludesAnonymous Value Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205916`

### Rule: Windows Server 2019 services using Local System that use Negotiate when reverting to NTLM authentication must use the computer identity instead of authenticating anonymously.

**Rule ID:** `SV-205916r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Services using Local System that use Negotiate when reverting to NTLM authentication may gain unauthorized access if allowed to authenticate anonymously versus using the computer identity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\LSA\ Value Name: UseMachineId Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205917`

### Rule: Windows Server 2019 must prevent NTLM from falling back to a Null session.

**Rule ID:** `SV-205917r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>NTLM sessions that are allowed to fall back to Null (unauthenticated) sessions may gain unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\LSA\MSV1_0\ Value Name: allownullsessionfallback Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205918`

### Rule: Windows Server 2019 must prevent PKU2U authentication using online identities.

**Rule ID:** `SV-205918r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>PKU2U is a peer-to-peer authentication protocol. This setting prevents online identities from authenticating to domain-joined systems. Authentication will be centrally managed with Windows user accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\LSA\pku2u\ Value Name: AllowOnlineID Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205919`

### Rule: Windows Server 2019 LAN Manager authentication level must be configured to send NTLMv2 response only and to refuse LM and NTLM.

**Rule ID:** `SV-205919r857347_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Kerberos v5 authentication protocol is the default for authentication of users who are logging on to domain accounts. NTLM, which is less secure, is retained in later Windows versions for compatibility with clients and servers that are running earlier versions of Windows or applications that still use it. It is also used to authenticate logons to standalone or nondomain-joined computers that are running later versions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\ Value Name: LmCompatibilityLevel Value Type: REG_DWORD Value: 0x00000005 (5)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205920`

### Rule: Windows Server 2019 must be configured to at least negotiate signing for LDAP client signing.

**Rule ID:** `SV-205920r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting controls the signing requirements for LDAP clients. This must be set to "Negotiate signing" or "Require signing", depending on the environment and type of LDAP server in use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\LDAP\ Value Name: LDAPClientIntegrity Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205921`

### Rule: Windows Server 2019 session security for NTLM SSP-based clients must be configured to require NTLMv2 session security and 128-bit encryption.

**Rule ID:** `SV-205921r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Microsoft has implemented a variety of security support providers for use with Remote Procedure Call (RPC) sessions. All of the options must be enabled to ensure the maximum security level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\MSV1_0\ Value Name: NTLMMinClientSec Value Type: REG_DWORD Value: 0x20080000 (537395200)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205922`

### Rule: Windows Server 2019 session security for NTLM SSP-based servers must be configured to require NTLMv2 session security and 128-bit encryption.

**Rule ID:** `SV-205922r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Microsoft has implemented a variety of security support providers for use with Remote Procedure Call (RPC) sessions. All of the options must be enabled to ensure the maximum security level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\MSV1_0\ Value Name: NTLMMinServerSec Value Type: REG_DWORD Value: 0x20080000 (537395200)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205923`

### Rule: Windows Server 2019 default permissions of global system objects must be strengthened.

**Rule ID:** `SV-205923r569188_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Windows systems maintain a global list of shared system resources such as DOS device names, mutexes, and semaphores. Each type of object is created with a default Discretionary Access Control List (DACL) that specifies who can access the objects with what permissions. When this policy is enabled, the default DACL is stronger, allowing non-administrative users to read shared objects but not to modify shared objects they did not create.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Session Manager\ Value Name: ProtectionMode Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-205924`

### Rule: Windows Server 2019 must preserve zone information when saving attachments.

**Rule ID:** `SV-205924r569188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Attachments from outside sources may contain malicious code. Preserving zone of origin (Internet, intranet, local, restricted) information on file attachments allows Windows to determine risk.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default behavior is for Windows to mark file attachments with their zone information. If the registry Value Name below does not exist, this is not a finding. If it exists and is configured with a value of "2", this is not a finding. If it exists and is configured with a value of "1", this is a finding. Registry Hive: HKEY_CURRENT_USER Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Attachments\ Value Name: SaveZoneInformation Value Type: REG_DWORD Value: 0x00000002 (2) (or if the Value Name does not exist)

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-205925`

### Rule: Windows Server 2019 must disable automatically signing in the last interactive user after a system-initiated restart.

**Rule ID:** `SV-205925r877377_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Windows can be configured to automatically sign the user back in after a Windows Update restart. Some protections are in place to help ensure this is done in a secure fashion; however, disabling this will prevent the caching of credentials for this purpose and also ensure the user is aware of the restart.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the registry value below. If it does not exist or is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: DisableAutomaticRestartSignOn Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-214936`

### Rule: Windows Server 2019 must have a host-based firewall installed and enabled.

**Rule ID:** `SV-214936r852535_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack, allowing or blocking inbound and outbound connections based on a set of rules.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if a host-based firewall is installed and enabled on the system. If a host-based firewall is not installed and enabled on the system, this is a finding. The configuration requirements will be determined by the applicable firewall STIG.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-236001`

### Rule: The Windows Explorer Preview pane must be disabled for Windows Server 2019.

**Rule ID:** `SV-236001r641821_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A known vulnerability in Windows could allow the execution of malicious code by either opening a compromised document or viewing it in the Windows Preview pane. Organizations must disable the Windows Preview pane and Windows Detail pane.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry values do not exist or are not configured as specified, this is a finding: Registry Hive: HKEY_CURRENT_USER Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer Value Name: NoPreviewPane Value Type: REG_DWORD Value: 1 Registry Hive: HKEY_CURRENT_USER Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer Value Name: NoReadingPane Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000041-GPOS-00019

**Group ID:** `V-257503`

### Rule: Windows Server 2019 must have PowerShell Transcription enabled.

**Rule ID:** `SV-257503r921895_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Enabling PowerShell Transcription will record detailed information from the processing of PowerShell commands and scripts. This can provide additional detail when malware has run on a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\PowerShell\Transcription\ Value Name: EnableTranscripting Value Type: REG_DWORD Value: 1

