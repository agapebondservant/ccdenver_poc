# STIG Benchmark: Microsoft Windows 11 Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253254`

### Rule: Domain-joined systems must use Windows 11 Enterprise Edition 64-bit version.

**Rule ID:** `SV-253254r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Features such as Credential Guard use virtualization-based security to protect information that could be used in credential theft attacks if compromised. There are a number of system requirements that must be met in order for Credential Guard to be configured and enabled properly. Virtualization-based security and Credential Guard are only available with Windows 11 Enterprise 64-bit version.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify domain-joined systems are using Windows 11 Enterprise Edition 64-bit version. For standalone systems, this is NA. Open "Settings". Select "System", then "About". If "Edition" is not "Windows 11 Enterprise", this is a finding. If "System type" is not "64-bit operating system...", this is a finding.

## Group: SRG-OS-000424-GPOS-00188

**Group ID:** `V-253255`

### Rule: Windows 11 domain-joined systems must have a Trusted Platform Module (TPM) enabled.

**Rule ID:** `SV-253255r971547_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Credential Guard uses virtualization-based security to protect information that could be used in credential theft attacks if compromised. There are a number of system requirements that must be met in order for Credential Guard to be configured and enabled properly. Without a TPM enabled and ready for use, Credential Guard keys are stored in a less secure method using software.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify domain-joined systems have a TPM enabled and ready for use. For standalone systems, this is NA. Virtualization-based security, including Credential Guard, currently cannot be implemented in virtual desktop implementations (VDI) due to specific supporting requirements including a TPM, UEFI with Secure Boot, and the capability to run the Hyper-V feature within the virtual desktop. For VDIs where the virtual desktop instance is deleted or refreshed upon logoff, this is NA. Verify the system has a TPM and is ready for use. Run "tpm.msc". Review the sections in the center pane. "Status" must indicate it has been configured with a message such as "The TPM is ready for use" or "The TPM is on and ownership has been taken". TPM Manufacturer Information - Specific Version = 2.0 If a TPM is not found or is not ready for use, this is a finding.

## Group: SRG-OS-000424-GPOS-00188

**Group ID:** `V-253256`

### Rule: Windows 11 systems must have Unified Extensible Firmware Interface (UEFI) firmware and be configured to run in UEFI mode, not Legacy BIOS.

**Rule ID:** `SV-253256r971547_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>UEFI provides additional security features in comparison to legacy BIOS firmware, including Secure Boot. UEFI is required to support additional security features in Windows 11, including virtualization-based Security and Credential Guard. Systems with UEFI that are operating in Legacy BIOS mode will not support these security features.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For virtual desktop implementations (VDIs) where the virtual desktop instance is deleted or refreshed upon logoff, this is NA. Verify the system firmware is configured to run in UEFI mode, not Legacy BIOS. Run "System Information". Under "System Summary", if "BIOS Mode" does not display "UEFI", this is a finding.

## Group: SRG-OS-000424-GPOS-00188

**Group ID:** `V-253257`

### Rule: Secure Boot must be enabled on Windows 11 systems.

**Rule ID:** `SV-253257r971547_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Secure Boot is a standard that ensures systems boot only to a trusted operating system. Secure Boot is required to support additional security features in Windows 11, including virtualization-based Security and Credential Guard. If Secure Boot is turned off, these security features will not function.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system firmware is configured for Secure Boot. For virtual desktop implementations (VDIs) where the virtual desktop instance is deleted or refreshed upon logoff, this is NA. Run "System Information". Under "System Summary", if "Secure Boot State" does not display "On", this is a finding.

## Group: SRG-OS-000191-GPOS-00080

**Group ID:** `V-253258`

### Rule: Windows 11 must employ automated mechanisms to determine the state of system components with regard to flaw remediation using the following frequency: Continuously, where ESS is used; 30 days, for any additional internal network scans not covered by ESS; and annually, for external scans by Computer Network Defense Service Provider (CNDSP).

**Rule ID:** `SV-253258r1000099_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An approved tool for continuous network scanning must be installed and configured to run. Without the use of automated mechanisms to scan for security flaws on a continuous and/or periodic basis, the operating system or other system components may remain vulnerable to the exploits presented by undetected software flaws. To support this requirement, the operating system may have an integrated solution incorporating continuous scanning using ESS and periodic scanning using other tools, as specified in the requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify DOD-approved ESS software is installed and properly operating. Ask the site information system security manager (ISSM) for documentation of the ESS software installation and configuration. If the ISSM is not able to provide a documented configuration for an installed ESS or if the ESS software is not properly maintained or used, this is a finding. Note: Example of documentation can be a copy of the site's CCB approved Software Baseline with version of software noted or a memo from the ISSM stating current ESS software and version.

## Group: SRG-OS-000404-GPOS-00183

**Group ID:** `V-253259`

### Rule: Windows 11 information systems must use BitLocker to encrypt all disks to protect the confidentiality and integrity of all information at rest.

**Rule ID:** `SV-253259r958870_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If data at rest is unencrypted, it is vulnerable to disclosure. Even if the operating system enforces permissions on data access, an adversary can remove non-volatile memory and read it directly, thereby circumventing operating system controls. Encrypting the data ensures that confidentiality is protected even when the operating system is not running.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all Windows 11 information systems (including SIPRNet) employ BitLocker for full disk encryption. For virtual desktop implementations (VDIs) in which the virtual desktop instance is deleted or refreshed upon logoff, this is NA. For AVD implementations with no data at rest, this is NA. If full disk encryption using BitLocker is not implemented, this is a finding. Verify BitLocker is turned on for the operating system drive and any fixed data drives. Open "BitLocker Drive Encryption" from the Control Panel. If the operating system drive or any fixed data drives have "Turn on BitLocker", this is a finding. Note: An alternate encryption application may be used in lieu of BitLocker providing it is configured for full disk encryption and satisfies the pre-boot authentication requirements (WN11-00-000031 and WN11-00-000032).

## Group: SRG-OS-000405-GPOS-00184

**Group ID:** `V-253260`

### Rule: Windows 11 systems must use a BitLocker PIN for pre-boot authentication.

**Rule ID:** `SV-253260r958872_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If data at rest is unencrypted, it is vulnerable to disclosure. Even if the operating system enforces permissions on data access, an adversary can remove non-volatile memory and read it directly, thereby circumventing operating system controls. Encrypting the data ensures that confidentiality is protected even when the operating system is not running. Pre-boot authentication prevents unauthorized users from accessing encrypted drives.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: For virtual desktop implementations (VDIs) in which the virtual desktop instance is deleted or refreshed upon logoff, this is NA. For AVD implementations with no data at rest, this is NA. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\FVE\ Value Name: UseAdvancedStartup Type: REG_DWORD Value: 0x00000001 (1) If one of the following registry values does not exist or is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\FVE\ Value Name: UseTPMPIN Type: REG_DWORD Value: 0x00000001 (1) Value Name: UseTPMKeyPIN Type: REG_DWORD Value: 0x00000001 (1) When BitLocker network unlock is used: Value Name: UseTPMPIN Type: REG_DWORD Value: 0x00000002 (2) Value Name: UseTPMKeyPIN Type: REG_DWORD Value: 0x00000002 (2) BitLocker network unlock may be used in conjunction with a BitLocker PIN. See the article below regarding information about network unlock. https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-how-to-enable-network-unlock

## Group: SRG-OS-000121-GPOS-00062

**Group ID:** `V-253261`

### Rule: Windows 11 systems must use a BitLocker PIN with a minimum length of six digits for pre-boot authentication.

**Rule ID:** `SV-253261r958504_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If data at rest is unencrypted, it is vulnerable to disclosure. Even if the operating system enforces permissions on data access, an adversary can remove non-volatile memory and read it directly, thereby circumventing operating system controls. Encrypting the data ensures that confidentiality is protected even when the operating system is not running. Pre-boot authentication prevents unauthorized users from accessing encrypted drives. Increasing the pin length requires a greater number of guesses for an attacker.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: For virtual desktop implementations (VDIs) in which the virtual desktop instance is deleted or refreshed upon logoff, this is NA. For AVD implementations with no data at rest, this is NA. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\FVE\ Value Name: MinimumPIN Type: REG_DWORD Value: 0x00000006 (6) or greater

## Group: SRG-OS-000370-GPOS-00155

**Group ID:** `V-253262`

### Rule: The operating system must employ a deny-all, permit-by-exception policy to allow the execution of authorized software programs.

**Rule ID:** `SV-253262r958808_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Utilizing an allowlist provides a configuration management method for allowing the execution of only authorized software. Using only authorized software decreases risk by limiting the number of potential vulnerabilities. The organization must identify authorized software programs and only permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as allowlisting.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system employs a deny-all, permit-by-exception policy to allow the execution of authorized software programs. This must include packaged apps such as the universal apps installed by default on systems. If an application allowlisting program is not in use on the system, this is a finding. Configuration of allowlisting applications will vary by the program. AppLocker is an allowlisting application built into Windows 11 Enterprise. A deny-by-default implementation is initiated by enabling any AppLocker rules within a category, only allowing what is specified by defined rules. If AppLocker is used, perform the following to view the configuration of AppLocker: Run "PowerShell". Execute the following command, substituting [c:\temp\file.xml] with a location and file name appropriate for the system: Get-AppLockerPolicy -Effective -XML > c:\temp\file.xml This will produce an xml file with the effective settings that can be viewed in a browser or opened in a program such as Excel for review. Implementation guidance for AppLocker is available at the following link: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/applocker-policies-deployment-guide

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253263`

### Rule: Windows 11 systems must be maintained at a supported servicing level.

**Rule ID:** `SV-253263r1016364_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Windows 11 is maintained by Microsoft at servicing levels for specific periods of time to support Windows as a Service. Systems at unsupported servicing levels or releases will not receive security updates for new vulnerabilities which leaves them subject to exploitation. New versions with feature updates are planned to be released on a semi-annual basis with an estimated support timeframe of 18 to 30 months depending on the release. Support for previously released versions has been extended for Enterprise editions. A separate servicing branch intended for special purpose systems is the Long-Term Servicing Channel (LTSC, formerly Branch - LTSB) which will receive security updates for 10 years but excludes feature updates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run "winver.exe". If the "About Windows" dialog box does not display "Microsoft Windows 11 Version 22H2 (OS Build 22621.380)" or greater, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253264`

### Rule: The Windows 11 system must use an antivirus program.

**Rule ID:** `SV-253264r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Malicious software can establish a base on individual desktops and servers. Employing an automated mechanism to detect this type of software will aid in elimination of the software from the operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an antivirus solution is installed on the system and in use. The antivirus solution may be bundled with an approved Endpoint Security Solution. Verify if Microsoft Defender Antivirus is in use or enabled: Open "PowerShell". Enter "get-service | where {$_.DisplayName -Like "*Defender*"} | Select Status,DisplayName" Verify third-party antivirus is in use or enabled: Open "PowerShell". Enter "get-service | where {$_.DisplayName -Like "*mcafee*"} | Select Status,DisplayName" Enter "get-service | where {$_.DisplayName -Like "*symantec*"} | Select Status,DisplayName" If there is no antivirus solution installed on the system, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-253265`

### Rule: Local volumes must be formatted using NTFS.

**Rule ID:** `SV-253265r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The ability to set access permissions and auditing is critical to maintaining the security and proper access controls of a system. To support this, volumes must be formatted using the NTFS file system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run "Computer Management". Navigate to Storage >> Disk Management. If the "File System" column does not indicate "NTFS" for each volume assigned a drive letter, this is a finding. This does not apply to system partitions such the Recovery and EFI System Partition.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253266`

### Rule: Alternate operating systems must not be permitted on the same system.

**Rule ID:** `SV-253266r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing other operating systems to run on a secure system may allow security to be circumvented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system does not include other operating system installations. Run "Advanced System Settings". Select the "Advanced" tab. Click the "Settings" button in the "Startup and Recovery" section. If the drop-down list box "Default operating system:" shows any operating system other than Windows 11, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-253267`

### Rule: Non-system-created file shares on a system must limit access to groups that require it.

**Rule ID:** `SV-253267r958524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Shares which provide network access, must not exist on a workstation except for system-created administrative shares, and could potentially expose sensitive information. If a share is necessary, share permissions, as well as NTFS permissions, must be reconfigured to give the minimum access to those accounts that require it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Non-system-created shares must not exist on workstations. If only system-created shares exist on the system, this is NA. Run "Computer Management". Navigate to System Tools >> Shared Folders >> Shares. If the only shares listed are "ADMIN$", "C$" and "IPC$", this is NA. (Selecting Properties for system-created shares will display a message that it has been shared for administrative purposes.) Right-click any non-system-created shares. Select "Properties". Select the "Share Permissions" tab. Verify the necessity of any shares found. If the file shares have not been reconfigured to restrict permissions to the specific groups or accounts that require access, this is a finding. Select the "Security" tab. If the NTFS permissions have not been reconfigured to restrict permissions to the specific groups or accounts that require access, this is a finding.

## Group: SRG-OS-000468-GPOS-00212

**Group ID:** `V-253268`

### Rule: Unused accounts must be disabled or removed from the system after 35 days of inactivity.

**Rule ID:** `SV-253268r1051039_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Outdated or unused accounts provide penetration points that may go undetected. Inactive accounts must be deleted if no longer necessary or, if still required, disable until needed. Satisfies: SRG-OS-000468-GPOS-00212, SRG-OS-000118-GPOS-00060</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run "PowerShell". Copy the lines below to the PowerShell window and enter. "([ADSI]('WinNT://{0}' -f $env:COMPUTERNAME)).Children | Where { $_.SchemaClassName -eq 'user' } | ForEach { $user = ([ADSI]$_.Path) $lastLogin = $user.Properties.LastLogin.Value $enabled = ($user.Properties.UserFlags.Value -band 0x2) -ne 0x2 if ($lastLogin -eq $null) { $lastLogin = 'Never' } Write-Host $user.Name $lastLogin $enabled }" This will return a list of local accounts with the account name, last logon, and if the account is enabled (True/False). For example: User1 10/31/2015 5:49:56 AM True Review the list to determine the finding validity for each account reported. Exclude the following accounts: Built-in administrator account (Disabled, SID ending in 500) Built-in guest account (Disabled, SID ending in 501) Built-in DefaultAccount (Disabled, SID ending in 503) Local administrator account If any enabled accounts have not been logged on to within the past 35 days, this is a finding. Inactive accounts that have been reviewed and deemed to be required must be documented with the information system security officer (ISSO).

## Group: SRG-OS-000312-GPOS-00123

**Group ID:** `V-253269`

### Rule: Only accounts responsible for the administration of a system must have Administrator rights on the system.

**Rule ID:** `SV-253269r958702_rule`
**Severity:** high

**Description:**
<VulnDiscussion>An account that does not have Administrator duties must not have Administrator rights. Such rights would allow the account to bypass or modify required security restrictions on that machine and make it vulnerable to attack. System administrators must log on to systems only using accounts with the minimum level of authority necessary. For domain-joined workstations, the Domain Admins group must be replaced by a domain workstation administrator group (see V-36434 in the Active Directory Domain STIG). Restricting highly privileged accounts from the local Administrators group helps mitigate the risk of privilege escalation resulting from credential theft attacks. Standard user accounts must not be members of the local administrators group.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run "Computer Management". Navigate to System Tools >> Local Users and Groups >> Groups. Review the members of the Administrators group. Only the appropriate administrator groups or accounts responsible for administration of the system may be members of the group. For domain-joined workstations, the Domain Admins group must be replaced by a domain workstation administrator group. Standard user accounts must not be members of the local administrator group. If prohibited accounts are members of the local administrators group, this is a finding. The built-in Administrator account or other required administrative accounts would not be a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253270`

### Rule: Only accounts responsible for the backup operations must be members of the Backup Operators group.

**Rule ID:** `SV-253270r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Backup Operators are able to read and write to any file in the system, regardless of the rights assigned to it. Backup and restore rights permit users to circumvent the file access restrictions present on NTFS disk drives for backup and restore purposes. Members of the Backup Operators group must have separate logon accounts for performing backup duties.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run "Computer Management". Navigate to System Tools >> Local Users and Groups >> Groups. Review the members of the Backup Operators group. If the group contains no accounts, this is not a finding. If the group contains any accounts, the accounts must be specifically for backup functions. If the group contains any standard user accounts used for performing normal user tasks, this is a finding.

## Group: SRG-OS-000312-GPOS-00124

**Group ID:** `V-253271`

### Rule: Only authorized user accounts must be allowed to create or run virtual machines on Windows 11 systems.

**Rule ID:** `SV-253271r958702_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing other operating systems to run on a secure system may allow users to circumvent security. For Hyper-V, preventing unauthorized users from being assigned to the Hyper-V Administrators group will prevent them from accessing or creating virtual machines on the system. The Hyper-V Hypervisor is used by virtualization-based Security features such as Credential Guard on Windows 11; however, it is not the full Hyper-V installation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If a hosted hypervisor (Hyper-V, VMware Workstation, etc.) is installed on the system, verify only authorized user accounts are allowed to run virtual machines. For Hyper-V, run "Computer Management". Navigate to System Tools >> Local Users and Groups >> Groups. Double click on "Hyper-V Administrators". If any unauthorized groups or user accounts are listed in "Members:", this is a finding. For hosted hypervisors other than Hyper-V, verify only authorized user accounts have access to run the virtual machines. Restrictions may be enforced by access to the physical system, software restriction policies, or access restrictions built into the application. If any unauthorized groups or user accounts have access to create or run virtual machines, this is a finding. All users authorized to create or run virtual machines must be documented with the ISSM/ISSO. Accounts nested within group accounts must be documented as individual accounts and not the group accounts.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253272`

### Rule: Standard local user accounts must not exist on a system in a domain.

**Rule ID:** `SV-253272r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To minimize potential points of attack, local user accounts, other than built-in accounts and local administrator accounts, must not exist on a workstation in a domain. Users must log on to workstations in a domain with their domain accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run "Computer Management". Navigate to System Tools >> Local Users and Groups >> Users. If local users other than the accounts listed below exist on a workstation in a domain, this is a finding. For standalone or nondomain-joined systems, this is Not Applicable. Built-in Administrator account (Disabled) Built-in Guest account (Disabled) Built-in DefaultAccount (Disabled) Built-in defaultuser0 (Disabled) Built-in WDAGUtilityAccount (Disabled) Local administrator account(s) All of the built-in accounts may not exist on a system, depending on the Windows 11 version.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-253273`

### Rule: Accounts must be configured to require password expiration.

**Rule ID:** `SV-253273r1051040_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords that do not expire increase exposure with a greater probability of being discovered or cracked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run "Computer Management". Navigate to System Tools >> Local Users and Groups >> Users. Double-click each active account. If "Password never expires" is selected for any account, this is a finding.

## Group: SRG-OS-000312-GPOS-00122

**Group ID:** `V-253274`

### Rule: Permissions for system files and directories must conform to minimum requirements.

**Rule ID:** `SV-253274r1016661_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changing the system's file and directory permissions allows the possibility of unauthorized and anonymous modification to the operating system and installed applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default file system permissions are adequate when the Security Option "Network access: Let Everyone permissions apply to anonymous users" is set to "Disabled" (WN11-SO-000160). If the default file system permissions are maintained and the referenced option is set to "Disabled", this is not a finding. Verify the default permissions for the sample directories below. Non-privileged groups such as Users or Authenticated Users must not have greater than read & execute permissions except where noted as defaults. (Individual accounts must not be used to assign permissions.) Select the "Security" tab, and the "Advanced" button. C:\ Type - "Allow" for all Inherited from - "None" for all Principal - Access - Applies to Administrators - Full control - This folder, subfolders, and files SYSTEM - Full control - This folder, subfolders, and files Users - Read & execute - This folder, subfolders, and files Authenticated Users - Modify - Subfolders and files only Authenticated Users - Create folders / append data - This folder only \Program Files Type - "Allow" for all Inherited from - "None" for all Principal - Access - Applies to TrustedInstaller - Full control - This folder and subfolders SYSTEM - Modify - This folder only SYSTEM - Full control - Subfolders and files only Administrators - Modify - This folder only Administrators - Full control - Subfolders and files only Users - Read & execute - This folder, subfolders, and files CREATOR OWNER - Full control - Subfolders and files only ALL APPLICATION PACKAGES - Read & execute - This folder, subfolders, and files ALL RESTRICTED APPLICATION PACKAGES - Read & execute - This folder, subfolders, and files \Windows Type - "Allow" for all Inherited from - "None" for all Principal - Access - Applies to TrustedInstaller - Full control - This folder and subfolders SYSTEM - Modify - This folder only SYSTEM - Full control - Subfolders and files only Administrators - Modify - This folder only Administrators - Full control - Subfolders and files only Users - Read & execute - This folder, subfolders, and files CREATOR OWNER - Full control - Subfolders and files only ALL APPLICATION PACKAGES - Read & execute - This folder, subfolders, and files ALL RESTRICTED APPLICATION PACKAGES - Read & execute - This folder, subfolders, and files Alternately use icacls. Run "CMD" as administrator. Enter "icacls" followed by the directory. icacls c:\ icacls "c:\program files" icacls c:\windows The following results will be displayed as each is entered: c:\ S-1-15-3-65536-1888954469-739942743-1668119174-2468466756-4239452838-1296943325-355587736-700089176 (S,RD,X,RA) BUILTIN\Administrators:(OI)(CI)(F) NT AUTHORITY\SYSTEM:(OI)(CI)(F) BUILTIN\Users:(OI)(CI)(RX) NT AUTHORITY\Authenticated Users:(OI)(CI)(IO)(M) NT AUTHORITY\Authenticated Users:(AD) Mandatory Label\High Mandatory Level:(OI)(NP)(IO)(NW) Successfully processed 1 files; Failed processing 0 files c:\program files NT SERVICE\TrustedInstaller:(F) NT SERVICE\TrustedInstaller:(CI)(IO)(F) NT AUTHORITY\SYSTEM:(M) NT AUTHORITY\SYSTEM:(OI)(CI)(IO)(F) BUILTIN\Administrators:(M) BUILTIN\Administrators:(OI)(CI)(IO)(F) BUILTIN\Users:(RX) BUILTIN\Users:(OI)(CI)(IO)(GR,GE) CREATOR OWNER:(OI)(CI)(IO)(F) APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(RX) APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(OI)(CI)(IO)(GR,GE) APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(RX) APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(OI)(CI)(IO)(GR,GE) Successfully processed 1 files; Failed processing 0 files c:\windows NT SERVICE\TrustedInstaller:(F) NT SERVICE\TrustedInstaller:(CI)(IO)(F) NT AUTHORITY\SYSTEM:(M) NT AUTHORITY\SYSTEM:(OI)(CI)(IO)(F) BUILTIN\Administrators:(M) BUILTIN\Administrators:(OI)(CI)(IO)(F) BUILTIN\Users:(RX) BUILTIN\Users:(OI)(CI)(IO)(GR,GE) CREATOR OWNER:(OI)(CI)(IO)(F) APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(RX) APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(OI)(CI)(IO)(GR,GE) APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(RX) APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(OI)(CI)(IO)(GR,GE) Successfully processed 1 files; Failed processing 0 files

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253275`

### Rule: Internet Information System (IIS) or its subcomponents must not be installed on a workstation.

**Rule ID:** `SV-253275r958478_rule`
**Severity:** high

**Description:**
<VulnDiscussion>IIS is not installed by default. Installation of Internet Information System (IIS) may allow unauthorized internet services to be hosted. Websites must only be hosted on servers that have been designed for that purpose and can be adequately secured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify it has not been installed on the system. Run "Programs and Features". Select "Turn Windows features on or off". If the entries for "Internet Information Services" or "Internet Information Services Hostable Web Core" are selected, this is a finding. If an application requires IIS or a subset to be installed to function, this needs be documented with the ISSO. In addition, any applicable requirements from the IIS STIG must be addressed.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-253276`

### Rule: Simple Network Management Protocol (SNMP) must not be installed on the system.

**Rule ID:** `SV-253276r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>"SNMP" is not installed by default. Some protocols and services do not support required security features, such as encrypting passwords or traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SNMP has not been installed. Navigate to the Windows\System32 directory. If the "SNMP" application exists, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253277`

### Rule: Simple TCP/IP Services must not be installed on the system.

**Rule ID:** `SV-253277r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>"Simple TCP/IP Services" is not installed by default. Some protocols and services do not support required security features, such as encrypting passwords or traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Simple TCP/IP Services has not been installed. Run "Services.msc". If "Simple TCP/IP Services" is listed, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-253278`

### Rule: The Telnet Client must not be installed on the system.

**Rule ID:** `SV-253278r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "Telnet Client" is not installed by default. Some protocols and services do not support required security features, such as encrypting passwords or traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Telnet Client has not been installed. Navigate to the Windows\System32 directory. If the "telnet" application exists, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-253279`

### Rule: The TFTP Client must not be installed on the system.

**Rule ID:** `SV-253279r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "TFTP Client" is not installed by default. Some protocols and services do not support required security features, such as encrypting passwords or traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify TFTP Client has not been installed. Navigate to the Windows\System32 directory. If the "TFTP" application exists, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253280`

### Rule: Software certificate installation files must be removed from Windows 11.

**Rule ID:** `SV-253280r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of software certificates and their accompanying installation files for end users to access resources is less secure than the use of hardware-based certificates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Search all drives for *.p12 and *.pfx files. If any files with these extensions exist, this is a finding. This does not apply to server-based applications that have a requirement for .p12 certificate files (e.g., Oracle Wallet Manager) or Adobe PreFlight certificate files. Some applications create files with extensions of .p12 that are not certificate installation files. Removal of non-certificate installation files from systems is not required. These must be documented with the ISSO.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253281`

### Rule: A host-based firewall must be installed and enabled on the system.

**Rule ID:** `SV-253281r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack, allowing or blocking inbound and outbound connections based on a set of rules.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if a host-based firewall is installed and enabled on the system. If a host-based firewall is not installed and enabled on the system, this is a finding. The configuration requirements will be determined by the applicable firewall STIG.

## Group: SRG-OS-000480-GPOS-00232

**Group ID:** `V-253282`

### Rule: Inbound exceptions to the firewall on Windows 11 domain workstations must only allow authorized remote management hosts.

**Rule ID:** `SV-253282r991593_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing inbound access to domain workstations from other systems may allow lateral movement across systems if credentials are compromised. Limiting inbound connections only from authorized remote management systems will help limit this exposure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify firewall exceptions to inbound connections on domain workstations include only authorized remote management hosts. If allowed inbound exceptions are not limited to authorized remote management hosts, this is a finding. Review inbound firewall exceptions. Computer Configuration >> Windows Settings >> Security Settings >> Windows Defender Firewall with Advanced Security >> Windows Defender Firewall with Advanced Security >> Inbound Rules (this link will be in the right pane) For any inbound rules that allow connections view the Scope for Remote IP address. This may be defined as an IP address, subnet, or range. The rule must apply to all firewall profiles. If a third-party firewall is used, ensure comparable settings are in place.

## Group: SRG-OS-000433-GPOS-00193

**Group ID:** `V-253283`

### Rule: Data Execution Prevention (DEP) must be configured to at least OptOut.

**Rule ID:** `SV-253283r958928_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Attackers are constantly looking for vulnerabilities in systems and applications. Data Execution Prevention (DEP) prevents harmful code from running in protected memory locations reserved for Windows and other programs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DEP configuration. Open a command prompt (cmd.exe) or PowerShell with elevated privileges (Run as administrator). Enter "BCDEdit /enum {current}". (If using PowerShell "{current}" must be enclosed in quotes.) If the value for "nx" is not "OptOut", this is a finding. (The more restrictive configuration of "AlwaysOn" would not be a finding.)

## Group: SRG-OS-000433-GPOS-00192

**Group ID:** `V-253284`

### Rule: Structured Exception Handling Overwrite Protection (SEHOP) must be enabled.

**Rule ID:** `SV-253284r958928_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Attackers are constantly looking for vulnerabilities in systems and applications. Structured Exception Handling Overwrite Protection (SEHOP) blocks exploits that use the Structured Exception Handling overwrite technique, a common buffer overflow attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SEHOP is turned on. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Session Manager\kernel\ Value Name: DisableExceptionChainValidation Value Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253285`

### Rule: The Windows PowerShell 2.0 feature must be disabled on the system.

**Rule ID:** `SV-253285r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Windows PowerShell 5.0 added advanced logging features which can provide additional detail when malware has been run on a system. Disabling the Windows PowerShell 2.0 mitigates against a downgrade attack that evades the Windows PowerShell 5.0 script block logging feature.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run "Windows PowerShell" with elevated privileges (run as administrator). Enter the following: Get-WindowsOptionalFeature -Online | Where FeatureName -like *PowerShellv2* If either of the following have a "State" of "Enabled", this is a finding. FeatureName : MicrosoftWindowsPowerShellV2 State : Enabled FeatureName : MicrosoftWindowsPowerShellV2Root State : Enabled Alternately: Search for "Features". Select "Turn Windows features on or off". If "Windows PowerShell 2.0" (whether the subcategory of "Windows PowerShell 2.0 Engine" is selected or not) is selected, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253286`

### Rule: The Server Message Block (SMB) v1 protocol must be disabled on the system.

**Rule ID:** `SV-253286r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SMBv1 is a legacy protocol that uses the MD5 algorithm as part of SMB. MD5 is known to be vulnerable to a number of attacks such as collision and preimage attacks as well as not being FIPS compliant. Disabling SMBv1 support may prevent access to file or print sharing resources with systems or devices that only support SMBv1. File shares and print services hosted on Windows Server 2003 are an example, however Windows Server 2003 is no longer a supported operating system. Some older Network Attached Storage (NAS) devices may only support SMBv1.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Different methods are available to disable SMBv1 on Windows 11. This is the preferred method, however if WN11-00-000165 and WN11-00-000170 are configured, this is NA. Run "Windows PowerShell" with elevated privileges (run as administrator). Enter the following: Get-WindowsOptionalFeature -Online | Where FeatureName -eq SMB1Protocol If "State : Enabled" is returned, this is a finding. Alternately: Search for "Features". Select "Turn Windows features on or off". If "SMB 1.0/CIFS File Sharing Support" is selected, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253287`

### Rule: The Server Message Block (SMB) v1 protocol must be disabled on the SMB server.

**Rule ID:** `SV-253287r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SMBv1 is a legacy protocol that uses the MD5 algorithm as part of SMB. MD5 is known to be vulnerable to a number of attacks such as collision and preimage attacks as well as not being FIPS compliant. Disabling SMBv1 support may prevent access to file or print sharing resources with systems or devices that only support SMBv1. File shares and print services hosted on Windows Server 2003 are an example, however Windows Server 2003 is no longer a supported operating system. Some older network attached devices may only support SMBv1.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Different methods are available to disable SMBv1 on Windows 11, if WN11-00-000160 is configured, this is NA. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters\ Value Name: SMB1 Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253288`

### Rule: The Server Message Block (SMB) v1 protocol must be disabled on the SMB client.

**Rule ID:** `SV-253288r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SMBv1 is a legacy protocol that uses the MD5 algorithm as part of SMB. MD5 is known to be vulnerable to a number of attacks such as collision and preimage attacks as well as not being FIPS compliant. Disabling SMBv1 support may prevent access to file or print sharing resources with systems or devices that only support SMBv1. File shares and print services hosted on Windows Server 2003 are an example, however Windows Server 2003 is no longer a supported operating system. Some older network attached devices may only support SMBv1.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Different methods are available to disable SMBv1 on Windows 11, if WN11-00-000160is configured, this is NA. If the following registry value is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\mrxsmb10\ Value Name: Start Type: REG_DWORD Value: 0x00000004 (4)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253289`

### Rule: The Secondary Logon service must be disabled on Windows 11.

**Rule ID:** `SV-253289r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Secondary Logon service provides a means for entering alternate credentials, typically used to run commands with elevated privileges. Using privileged credentials in a standard user session can expose those credentials to theft.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run "Services.msc". Locate the "Secondary Logon" service. If the "Startup Type" is not "Disabled" or the "Status" is "Running", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253290`

### Rule: Orphaned security identifiers (SIDs) must be removed from user rights on Windows 11.

**Rule ID:** `SV-253290r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accounts or groups given rights on a system may show up as unresolved SIDs for various reasons including deletion of the accounts or groups. If the account or group objects are reanimated, there is a potential they may still have rights no longer intended. Valid domain accounts or groups may also show up as unresolved SIDs if a connection to the domain cannot be established for some reason.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the effective User Rights setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. Review each User Right listed for any unresolved SIDs to determine whether they are valid, such as due to being temporarily disconnected from the domain. (Unresolved SIDs have the format of "*S-1-..".) If any unresolved SIDs exist and are not for currently valid accounts or groups, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253291`

### Rule: Bluetooth must be turned off unless approved by the organization.

**Rule ID:** `SV-253291r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If not configured properly, Bluetooth may allow rogue devices to communicate with a system. If a rogue device is paired with a system, there is potential for sensitive information to be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is NA if the system does not have Bluetooth. Verify the Bluetooth radio is turned off unless approved by the organization. If it is not, this is a finding. Approval must be documented with the ISSO.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253292`

### Rule: Bluetooth must be turned off when not in use.

**Rule ID:** `SV-253292r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If not configured properly, Bluetooth may allow rogue devices to communicate with a system. If a rogue device is paired with a system, there is potential for sensitive information to be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is NA if the system does not have Bluetooth. Verify the organization has a policy to turn off Bluetooth when not in use and personnel are trained. If it does not, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253293`

### Rule: The system must notify the user when a Bluetooth device attempts to connect.

**Rule ID:** `SV-253293r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If not configured properly, Bluetooth may allow rogue devices to communicate with a system. If a rogue device is paired with a system, there is potential for sensitive information to be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is NA if the system does not have Bluetooth, or if Bluetooth is turned off per the organizations policy. Search for "Bluetooth". View Bluetooth Settings. Select "More Bluetooth Options" If "Alert me when a new Bluetooth device wants to connect" is not checked, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253294`

### Rule: Administrative accounts must not be used with applications that access the internet, such as web browsers, or with potential internet sources, such as email.

**Rule ID:** `SV-253294r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Using applications that access the internet or have potential internet sources using administrative privileges exposes a system to compromise. If a flaw in an application is exploited while running as a privileged user, the entire system could be compromised. Web browsers and email are common attack vectors for introducing malicious code and must not be run with an administrative account. Since administrative accounts may generally change or work around technical restrictions for running a web browser or other applications, it is essential that policy requires administrative accounts to not access the internet or use applications, such as email. The policy must define specific exceptions for local service administration. These exceptions may include HTTP(S)-based tools that are used for the administration of the local system, services, or attached devices. Technical means such as application allowlisting can be used to enforce the policy to ensure compliance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine whether administrative accounts are prevented from using applications that access the internet, such as web browsers, or with potential internet sources, such as email, except as necessary for local service administration. The organization must have a policy that prohibits administrative accounts from using applications that access the internet, such as web browsers, or with potential internet sources, such as email, except as necessary for local service administration. The policy must define specific exceptions for local service administration. These exceptions may include HTTP(S)-based tools that are used for the administration of the local system, services, or attached devices. Technical measures such as the removal of applications or application allowlisting must be used where feasible to prevent the use of applications that access the internet. If accounts with administrative privileges are not prevented from using applications that access the internet or with potential internet sources, this is a finding.

## Group: SRG-OS-000185-GPOS-00079

**Group ID:** `V-253295`

### Rule: Windows 11 nonpersistent VM sessions must not exceed 24 hours.

**Rule ID:** `SV-253295r958552_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For virtual desktop implementations (VDIs) where the virtual desktop instance is deleted or refreshed upon logoff, the organization must enforce that sessions be terminated within 24 hours. This would ensure any data stored on the VM that is not encrypted or covered by Credential Guard is deleted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there is a documented policy or procedure in place that nonpersistent VM sessions do not exceed 24 hours. If the system is NOT a nonpersistent VM, this is Not Applicable. For Azure Virtual Desktop (AVD) implementations with no data at rest, this is Not Applicable. If there is no such documented policy or procedure in place, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-253296`

### Rule: The Windows 11 time service must synchronize with an appropriate DOD time source.

**Rule ID:** `SV-253296r1051041_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Windows Time Service controls time synchronization settings. Time synchronization is essential for authentication and auditing purposes. If the Windows Time Service is used, it must synchronize with a secure, authorized time source. Domain-joined systems are automatically configured to synchronize with domain controllers. If an NTP server is configured, it must synchronize with a secure, authorized time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Windows time service configuration. Open an elevated "Command Prompt" (run as administrator). Enter "W32tm /query /configuration". Domain-joined systems (excluding the domain controller with the PDC emulator role): If the value for "Type" under "NTP Client" is not "NT5DS", this is a finding.

## Group: SRG-OS-000329-GPOS-00128

**Group ID:** `V-253297`

### Rule: Windows 11 account lockout duration must be configured to 15 minutes or greater.

**Rule ID:** `SV-253297r958736_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The account lockout feature, when enabled, prevents brute-force password attacks on the system. This parameter specifies the amount of time that an account will remain locked after the specified number of failed logon attempts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Account Policies >> Account Lockout Policy. If the "Account lockout duration" is less than "15" minutes (excluding "0"), this is a finding. Configuring this to "0", requiring an administrator to unlock the account, is more restrictive and is not a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-253298`

### Rule: The number of allowed bad logon attempts must be configured to three or less.

**Rule ID:** `SV-253298r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The account lockout feature, when enabled, prevents brute-force password attacks on the system. The higher this value is, the less effective the account lockout feature will be in protecting the local system. The number of bad logon attempts must be reasonably small to minimize the possibility of a successful password attack, while allowing for honest errors made during a normal user logon.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Account Policies >> Account Lockout Policy. If the "Account lockout threshold" is "0" or more than "3" attempts, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-253299`

### Rule: The period of time before the bad logon counter is reset must be configured to 15 minutes.

**Rule ID:** `SV-253299r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The account lockout feature, when enabled, prevents brute-force password attacks on the system. This parameter specifies the period of time that must pass after failed logon attempts before the counter is reset to 0. The smaller this value is, the less effective the account lockout feature will be in protecting the local system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Account Policies >> Account Lockout Policy. If the "Reset account lockout counter after" value is less than "15" minutes, this is a finding.

## Group: SRG-OS-000077-GPOS-00045

**Group ID:** `V-253300`

### Rule: The password history must be configured to 24 passwords remembered.

**Rule ID:** `SV-253300r1000103_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A system is more vulnerable to unauthorized access when system users recycle the same password several times without being required to change a password to a unique password on a regularly scheduled basis. This enables users to effectively negate the purpose of mandating periodic password changes. The default value is 24 for Windows domain systems. DOD has decided this is the appropriate value for all Windows systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Account Policies >> Password Policy. If the value for "Enforce password history" is less than "24" passwords remembered, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-253301`

### Rule: The maximum password age must be configured to 60 days or less.

**Rule ID:** `SV-253301r1051042_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The longer a password is in use, the greater the opportunity for someone to gain unauthorized knowledge of the passwords. Scheduled changing of passwords hinders the ability of unauthorized system users to crack passwords and gain access to a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Account Policies >> Password Policy. If the value for the "Maximum password age" is greater than "60" days, this is a finding. If the value is set to "0" (never expires), this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-253302`

### Rule: The minimum password age must be configured to at least 1 day.

**Rule ID:** `SV-253302r1051043_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Permitting passwords to be changed in immediate succession within the same day allows users to cycle passwords through their history database. This enables users to effectively negate the purpose of mandating periodic password changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Account Policies >> Password Policy. If the value for the "Minimum password age" is less than "1" day, this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-253303`

### Rule: Passwords must, at a minimum, be 14 characters.

**Rule ID:** `SV-253303r1051044_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems not protected with strong password schemes (including passwords of minimum length) provide the opportunity for anyone to crack the password, thus gaining access to the system and compromising the device, information, or the local network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Account Policies >> Password Policy. If the value for the "Minimum password length," is less than "14" characters, this is a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-253304`

### Rule: The built-in Microsoft password complexity filter must be enabled.

**Rule ID:** `SV-253304r1051045_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of complex passwords increases their strength against guessing and brute-force attacks. This setting configures the system to verify that newly created passwords conform to the Windows password complexity policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Account Policies >> Password Policy. If the value for "Password must meet complexity requirements" is not set to "Enabled", this is a finding. If the site is using a password filter that requires this setting be set to "Disabled" for the filter to be used, this would not be considered a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-253305`

### Rule: Reversible password encryption must be disabled.

**Rule ID:** `SV-253305r1051046_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Storing passwords using reversible encryption is essentially the same as storing clear-text versions of the passwords. For this reason, this policy must never be enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Account Policies >> Password Policy. If the value for "Store password using reversible encryption" is not set to "Disabled", this is a finding.

## Group: SRG-OS-000458-GPOS-00203

**Group ID:** `V-253306`

### Rule: The system must be configured to audit Account Logon - Credential Validation failures.

**Rule ID:** `SV-253306r991570_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Credential validation records events related to validation tests on credentials for a user account logon.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Account Logon >> Credential Validation - Failure

## Group: SRG-OS-000458-GPOS-00203

**Group ID:** `V-253307`

### Rule: The system must be configured to audit Account Logon - Credential Validation successes.

**Rule ID:** `SV-253307r991570_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Credential validation records events related to validation tests on credentials for a user account logon.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Account Logon >> Credential Validation - Success

## Group: SRG-OS-000337-GPOS-00129

**Group ID:** `V-253308`

### Rule: The system must be configured to audit Account Management - Security Group Management successes.

**Rule ID:** `SV-253308r971541_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Security Group Management records events such as creating, deleting or changing of security groups, including changes in group members.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Account Management >> Security Group Management - Success

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-253309`

### Rule: The system must be configured to audit Account Management - User Account Management failures.

**Rule ID:** `SV-253309r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. User Account Management records events such as creating, changing, deleting, renaming, disabling, or enabling user accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Account Management >> User Account Management - Failure

## Group: SRG-OS-000239-GPOS-00089

**Group ID:** `V-253310`

### Rule: The system must be configured to audit Account Management - User Account Management successes.

**Rule ID:** `SV-253310r991551_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. User Account Management records events such as creating, changing, deleting, renaming, disabling, or enabling user accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Account Management >> User Account Management - Success

## Group: SRG-OS-000365-GPOS-00152

**Group ID:** `V-253311`

### Rule: The system must be configured to audit Detailed Tracking - PNP Activity successes.

**Rule ID:** `SV-253311r1051047_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Plug and Play activity records events related to the successful connection of external devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*" Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Detailed Tracking >> Plug and Play Events - Success

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-253312`

### Rule: The system must be configured to audit Detailed Tracking - Process Creation successes.

**Rule ID:** `SV-253312r1051048_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Process creation records events related to the creation of a process and the source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Detailed Tracking >> Process Creation - Success

## Group: SRG-OS-000470-GPOS-00214

**Group ID:** `V-253313`

### Rule: The system must be configured to audit Logon/Logoff - Account Lockout failures.

**Rule ID:** `SV-253313r991578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Account Lockout events can be used to identify potentially malicious logon attempts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*" Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Logon/Logoff >> Account Lockout - Failure

## Group: SRG-OS-000458-GPOS-00203

**Group ID:** `V-253314`

### Rule: The system must be configured to audit Logon/Logoff - Group Membership successes.

**Rule ID:** `SV-253314r991570_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Audit Group Membership records information related to the group membership of a user's logon token.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*" Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Logon/Logoff >> Group Membership - Success

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-253315`

### Rule: The system must be configured to audit Logon/Logoff - Logoff successes.

**Rule ID:** `SV-253315r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Logoff records user logoffs. If this is an interactive logoff, it is recorded on the local system. If it is to a network share, it is recorded on the system accessed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Logon/Logoff >> Logoff - Success

## Group: SRG-OS-000472-GPOS-00217

**Group ID:** `V-253316`

### Rule: The system must be configured to audit Logon/Logoff - Logon failures.

**Rule ID:** `SV-253316r991581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Logon records user logons. If this is an interactive logon, it is recorded on the local system. If it is to a network share, it is recorded on the system accessed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Logon/Logoff >> Logon - Failure

## Group: SRG-OS-000472-GPOS-00217

**Group ID:** `V-253317`

### Rule: The system must be configured to audit Logon/Logoff - Logon successes.

**Rule ID:** `SV-253317r991581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Logon records user logons. If this is an interactive logon, it is recorded on the local system. If it is to a network share, it is recorded on the system accessed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Logon/Logoff >> Logon - Success

## Group: SRG-OS-000470-GPOS-00214

**Group ID:** `V-253318`

### Rule: The system must be configured to audit Logon/Logoff - Special Logon successes.

**Rule ID:** `SV-253318r991578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Special Logon records special logons which have administrative privileges and can be used to elevate processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Logon/Logoff >> Special Logon - Success

## Group: SRG-OS-000462-GPOS-00206

**Group ID:** `V-253319`

### Rule: Windows 11 must be configured to audit Object Access - File Share failures.

**Rule ID:** `SV-253319r991572_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Auditing file shares records events related to connection to shares on a system including system shares such as C$.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open PowerShell or a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*" Compare the AuditPol settings with the following: Object Access >> File Share - Failure If the system does not audit the above, this is a finding.

## Group: SRG-OS-000462-GPOS-00206

**Group ID:** `V-253320`

### Rule: Windows 11 must be configured to audit Object Access - File Share successes.

**Rule ID:** `SV-253320r991572_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Auditing file shares records events related to connection to shares on a system including system shares such as C$.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open PowerShell or a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*" Compare the AuditPol settings with the following: Object Access >> File Share - Success If the system does not audit the above, this is a finding.

## Group: SRG-OS-000462-GPOS-00206

**Group ID:** `V-253321`

### Rule: Windows 11 must be configured to audit Object Access - Other Object Access Events successes.

**Rule ID:** `SV-253321r991572_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Auditing for other object access records events related to the management of task scheduler jobs and COM+ objects.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open PowerShell or a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*" Compare the AuditPol settings with the following: Object Access >> Other Object Access Events - Success If the system does not audit the above, this is a finding.

## Group: SRG-OS-000462-GPOS-00206

**Group ID:** `V-253322`

### Rule: Windows 11 must be configured to audit Object Access - Other Object Access Events failures.

**Rule ID:** `SV-253322r991572_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Auditing for other object access records events related to the management of task scheduler jobs and COM+ objects.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open PowerShell or a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*" Compare the AuditPol settings with the following: Object Access >> Other Object Access Events - Failure If the system does not audit the above, this is a finding.

## Group: SRG-OS-000474-GPOS-00219

**Group ID:** `V-253323`

### Rule: The system must be configured to audit Object Access - Removable Storage failures.

**Rule ID:** `SV-253323r991583_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Auditing object access for removable media records events related to access attempts on file system objects on removable storage devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*" Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Object Access >> Removable Storage - Failure Some virtual machines may generate excessive audit events for access to the virtual hard disk itself when this setting is enabled. This may be set to Not Configured in such cases and would not be a finding. This must be documented with the ISSO to include mitigations such as monitoring or restricting any actual removable storage connected to the VM.

## Group: SRG-OS-000474-GPOS-00219

**Group ID:** `V-253324`

### Rule: The system must be configured to audit Object Access - Removable Storage successes.

**Rule ID:** `SV-253324r991583_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Auditing object access for removable media records events related to access attempts on file system objects on removable storage devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*" Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Object Access >> Removable Storage - Success Some virtual machines may generate excessive audit events for access to the virtual hard disk itself when this setting is enabled. This may be set to Not Configured in such cases and would not be a finding. This must be documented with the ISSO to include mitigations such as monitoring or restricting any actual removable storage connected to the VM.

## Group: SRG-OS-000462-GPOS-00206

**Group ID:** `V-253325`

### Rule: The system must be configured to audit Policy Change - Audit Policy Change successes.

**Rule ID:** `SV-253325r991572_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Audit Policy Change records events related to changes in audit policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Policy Change >> Audit Policy Change - Success

## Group: SRG-OS-000462-GPOS-00206

**Group ID:** `V-253326`

### Rule: The system must be configured to audit Policy Change - Authentication Policy Change successes.

**Rule ID:** `SV-253326r991572_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Authentication Policy Change records events related to changes in authentication policy including Kerberos policy and Trust changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Policy Change >> Authentication Policy Change - Success

## Group: SRG-OS-000462-GPOS-00206

**Group ID:** `V-253327`

### Rule: The system must be configured to audit Policy Change - Authorization Policy Change successes.

**Rule ID:** `SV-253327r991572_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Authorization Policy Change records events related to changes in user rights, such as create a token object.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: -Open a Command Prompt with elevated privileges ("Run as Administrator"). -Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding. Policy Change >> Authorization Policy Change - Success

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-253328`

### Rule: The system must be configured to audit Privilege Use - Sensitive Privilege Use failures.

**Rule ID:** `SV-253328r958732_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Sensitive Privilege Use records events related to use of sensitive privileges, such as "Act as part of the operating system" or "Debug programs".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Privilege Use >> Sensitive Privilege Use - Failure

## Group: SRG-OS-000466-GPOS-00210

**Group ID:** `V-253329`

### Rule: The system must be configured to audit Privilege Use - Sensitive Privilege Use successes.

**Rule ID:** `SV-253329r991575_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Sensitive Privilege Use records events related to use of sensitive privileges, such as "Act as part of the operating system" or "Debug programs".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Privilege Use >> Sensitive Privilege Use - Success

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-253330`

### Rule: The system must be configured to audit System - IPsec Driver failures.

**Rule ID:** `SV-253330r991586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. IPsec Driver records events related to the IPsec Driver such as dropped packets.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: System >> IPsec Driver - Failure

## Group: SRG-OS-000471-GPOS-00215

**Group ID:** `V-253331`

### Rule: The system must be configured to audit System - Other System Events successes.

**Rule ID:** `SV-253331r991579_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Audit Other System Events records information related to cryptographic key operations and the Windows Firewall service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*" Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: System >> Other System Events - Success

## Group: SRG-OS-000471-GPOS-00215

**Group ID:** `V-253332`

### Rule: The system must be configured to audit System - Other System Events failures.

**Rule ID:** `SV-253332r991579_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Audit Other System Events records information related to cryptographic key operations and the Windows Firewall service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*" Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: System >> Other System Events - Failure

## Group: SRG-OS-000466-GPOS-00210

**Group ID:** `V-253333`

### Rule: The system must be configured to audit System - Security State Change successes.

**Rule ID:** `SV-253333r991575_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Security State Change records events related to changes in the security state, such as startup and shutdown of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: System >> Security State Change - Success

## Group: SRG-OS-000466-GPOS-00210

**Group ID:** `V-253334`

### Rule: The system must be configured to audit System - Security System Extension successes.

**Rule ID:** `SV-253334r991575_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Security System Extension records events related to extension code being loaded by the security subsystem.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: System >> Security System Extension - Success

## Group: SRG-OS-000463-GPOS-00207

**Group ID:** `V-253335`

### Rule: The system must be configured to audit System - System Integrity failures.

**Rule ID:** `SV-253335r991573_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. System Integrity records events related to violations of integrity to the security subsystem.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: System >> System Integrity - Failure

## Group: SRG-OS-000463-GPOS-00207

**Group ID:** `V-253336`

### Rule: The system must be configured to audit System - System Integrity successes.

**Rule ID:** `SV-253336r991573_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. System Integrity records events related to violations of integrity to the security subsystem.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Security Option "Audit: Force audit policy subcategory settings to override audit policy category settings" must be set to "Enabled" (WN11-SO-000030) for the detailed auditing subcategories to be effective. Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: System >> System Integrity - Success

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-253337`

### Rule: The Application event log size must be configured to 32768 KB or greater.

**Rule ID:** `SV-253337r958752_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inadequate log size will cause the log to fill up quickly. This may prevent audit events from being recorded properly and require frequent attention by administrative personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is configured to send audit records directly to an audit server, this is NA. This must be documented with the ISSO. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\EventLog\Application\ Value Name: MaxSize Value Type: REG_DWORD Value: 0x00008000 (32768) (or greater)

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-253338`

### Rule: The Security event log size must be configured to 1024000 KB or greater.

**Rule ID:** `SV-253338r958752_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inadequate log size will cause the log to fill up quickly. This may prevent audit events from being recorded properly and require frequent attention by administrative personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is configured to send audit records directly to an audit server, this is NA. This must be documented with the ISSO. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\EventLog\Security\ Value Name: MaxSize Value Type: REG_DWORD Value: 0x000fa000 (1024000) (or greater)

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-253339`

### Rule: The System event log size must be configured to 32768 KB or greater.

**Rule ID:** `SV-253339r958752_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inadequate log size will cause the log to fill up quickly. This may prevent audit events from being recorded properly and require frequent attention by administrative personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is configured to send audit records directly to an audit server, this is NA. This must be documented with the ISSO. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\EventLog\System\ Value Name: MaxSize Value Type: REG_DWORD Value: 0x00008000 (32768) (or greater)

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-253340`

### Rule: Windows 11 permissions for the Application event log must prevent access by non-privileged accounts.

**Rule ID:** `SV-253340r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. The Application event log may be susceptible to tampering if proper permissions are not applied.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the permissions on the Application event log (Application.evtx). Standard user accounts or groups must not have access. The default permissions listed below satisfy this requirement. Eventlog - Full Control SYSTEM - Full Control Administrators - Full Control The default location is the "%SystemRoot%\SYSTEM32\WINEVT\LOGS" directory. They may have been moved to another folder. If the permissions for these files are not as restrictive as the ACLs listed, this is a finding. Note: If "APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES" has Special Permissions, this would not be a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-253341`

### Rule: Windows 11 permissions for the Security event log must prevent access by non-privileged accounts.

**Rule ID:** `SV-253341r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. The Security event log may disclose sensitive information or be susceptible to tampering if proper permissions are not applied.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the permissions on the Security event log (Security.evtx). Standard user accounts or groups must not have access. The default permissions listed below satisfy this requirement. Eventlog - Full Control SYSTEM - Full Control Administrators - Full Control The default location is the "%SystemRoot%\SYSTEM32\WINEVT\LOGS" directory. They may have been moved to another folder. If the permissions for these files are not as restrictive as the ACLs listed, this is a finding. Note: If "APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES" has Special Permissions, this would not be a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-253342`

### Rule: Windows 11 permissions for the System event log must prevent access by non-privileged accounts.

**Rule ID:** `SV-253342r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. The System event log may be susceptible to tampering if proper permissions are not applied.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the permissions on the System event log (System.evtx). Standard user accounts or groups must not have access. The default permissions listed below satisfy this requirement. Eventlog - Full Control SYSTEM - Full Control Administrators - Full Control The default location is the "%SystemRoot%\SYSTEM32\WINEVT\LOGS" directory. They may have been moved to another folder. If the permissions for these files are not as restrictive as the ACLs listed, this is a finding. Note: If "APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES" has Special Permissions, this would not be a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-253343`

### Rule: Windows 11 must be configured to audit Other Policy Change Events Successes.

**Rule ID:** `SV-253343r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Audit Other Policy Change Events contains events about EFS Data Recovery Agent policy changes, changes in Windows Filtering Platform filter, status on Security policy settings updates for local Group Policy settings, Central Access Policy changes, and detailed troubleshooting events for Cryptographic Next Generation (CNG) operations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Policy Change >> Other Policy Change Events - Success

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-253344`

### Rule: Windows 11 must be configured to audit Other Policy Change Events Failures.

**Rule ID:** `SV-253344r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Audit Other Policy Change Events contains events about EFS Data Recovery Agent policy changes, changes in Windows Filtering Platform filter, status on Security policy settings updates for local Group Policy settings, Central Access Policy changes, and detailed troubleshooting events for Cryptographic Next Generation (CNG) operations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Policy Change >> Other Policy Change Events - Failure

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-253345`

### Rule: Windows 11 must be configured to audit other Logon/Logoff Events Successes.

**Rule ID:** `SV-253345r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Audit Other Logon/Logoff Events determines whether Windows generates audit events for other logon or logoff events. Logon events are essential to understanding user activity and detecting potential attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Logon/Logoff >> Other Logon/Logoff Events - Success

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-253346`

### Rule: Windows 11 must be configured to audit other Logon/Logoff Events Failures.

**Rule ID:** `SV-253346r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Audit Other Logon/Logoff Events determines whether Windows generates audit events for other logon or logoff events. Logon events are essential to understanding user activity and detecting potential attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Logon/Logoff >> Other Logon/Logoff Events - Failure

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-253347`

### Rule: Windows 11 must be configured to audit Detailed File Share Failures.

**Rule ID:** `SV-253347r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Audit Detailed File Share allows the user to audit attempts to access files and folders on a shared folder. The Detailed File Share setting logs an event every time a file or folder is accessed, whereas the File Share setting only records one event for any connection established between a client and file share. Detailed File Share audit events include detailed information about the permissions or other criteria used to grant or deny access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Object Access >> Detailed File Share - Failure

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-253348`

### Rule: Windows 11 must be configured to audit MPSSVC Rule-Level Policy Change Successes.

**Rule ID:** `SV-253348r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Audit MPSSVC Rule-Level Policy Change determines whether the operating system generates audit events when changes are made to policy rules for the Microsoft Protection Service (MPSSVC.exe).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Policy Change >> MPSSVC Rule-Level Policy Change - Success

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-253349`

### Rule: Windows 11 must be configured to audit MPSSVC Rule-Level Policy Change Failures.

**Rule ID:** `SV-253349r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Audit MPSSVC Rule-Level Policy Change determines whether the operating system generates audit events when changes are made to policy rules for the Microsoft Protection Service (MPSSVC.exe).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the AuditPol tool to review the current Audit Policy configuration: Open a Command Prompt with elevated privileges ("Run as Administrator"). Enter "AuditPol /get /category:*". Compare the AuditPol settings with the following. If the system does not audit the following, this is a finding: Policy Change >> MPSSVC Rule-Level Policy Change - Failure

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253350`

### Rule: Camera access from the lock screen must be disabled.

**Rule ID:** `SV-253350r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling camera access from the lock screen could allow for unauthorized use. Requiring logon will ensure the device is only used by authorized personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the device does not have a camera, this is NA. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\Personalization\ Value Name: NoLockScreenCamera Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253351`

### Rule: Windows 11 must cover or disable the built-in or attached camera when not in use.

**Rule ID:** `SV-253351r1106508_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Failing to disconnect from collaborative computing devices (i.e. cameras) can result in subsequent compromises of organizational information. Providing easy methods to physically disconnect from such devices after a collaborative computing session helps to ensure that participants actually carry out the disconnect activity without having to go through complex and tedious procedures. Satisfies: SRG-OS-000095-GPOS-00049, SRG-OS-000370-GPOS-00155</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the device or operating system does not have a camera installed, this requirement is not applicable. This requirement is not applicable to mobile devices (smartphones and tablets), where the use of the camera is a local authorizing official (AO) decision. This requirement is not applicable to dedicated VTC suites located in approved VTC locations that are centrally managed. For an external camera, if there is not a method for the operator to manually disconnect camera at the end of collaborative computing sessions, this is a finding. For a built-in camera, the camera must be protected by a camera cover (e.g. laptop camera cover slide) when not in use. If the built-in camera is not protected with a camera cover, or if the built-in camera is not disabled in the bios, this is a finding. If the camera is not disconnected or covered, the following registry entry is required: Registry Hive: HKEY_LOCAL_MACHINE RegistryPath\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam Value Name: Value Value Data: Deny If "Value Name" is set to a value other than "Deny" and the collaborative computing device has not been authorized for use, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253352`

### Rule: The display of slide shows on the lock screen must be disabled.

**Rule ID:** `SV-253352r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Slide shows that are displayed on the lock screen could display sensitive information to unauthorized personnel. Turning off this feature will limit access to the information to a logged on user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\Personalization\ Value Name: NoLockScreenSlideshow Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253353`

### Rule: IPv6 source routing must be configured to highest protection.

**Rule ID:** `SV-253353r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the system to disable IPv6 source routing protects against spoofing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Tcpip6\Parameters\ Value Name: DisableIpSourceRouting Value Type: REG_DWORD Value: 2

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253354`

### Rule: The system must be configured to prevent IP source routing.

**Rule ID:** `SV-253354r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the system to disable IP source routing protects against spoofing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\ Value Name: DisableIPSourceRouting Value Type: REG_DWORD Value: 2

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253355`

### Rule: The system must be configured to prevent Internet Control Message Protocol (ICMP) redirects from overriding Open Shortest Path First (OSPF) generated routes.

**Rule ID:** `SV-253355r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Allowing ICMP redirect of routes can lead to traffic not being routed properly. When disabled, this forces ICMP to be routed via shortest path first.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\ Value Name: EnableICMPRedirect Value Type: REG_DWORD Value: 0

## Group: SRG-OS-000420-GPOS-00186

**Group ID:** `V-253356`

### Rule: The system must be configured to ignore NetBIOS name release requests except from WINS servers.

**Rule ID:** `SV-253356r958902_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Configuring the system to ignore name release requests, except from WINS servers, prevents a denial of service (DoS) attack. The DoS consists of sending a NetBIOS name release request to the server for each entry in the server's cache, causing a response delay in the normal operation of the servers WINS resolution capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Netbt\Parameters\ Value Name: NoNameReleaseOnDemand Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-253357`

### Rule: Local administrator accounts must have their privileged token filtered to prevent elevated privileges from being used over the network on domain systems.

**Rule ID:** `SV-253357r958518_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A compromised local administrator account can provide means for an attacker to move laterally between domain systems. With User Account Control enabled, filtering the privileged token for built-in administrator accounts will prevent the elevated privileges of these accounts from being used over the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is not a member of a domain, this is NA. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: LocalAccountTokenFilterPolicy Value Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253358`

### Rule: WDigest Authentication must be disabled.

**Rule ID:** `SV-253358r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When the WDigest Authentication protocol is enabled, plain text passwords are stored in the Local Security Authority Subsystem Service (LSASS) exposing them to theft. WDigest is disabled by default in Windows 11. This setting ensures this is enforced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\SecurityProviders\Wdigest\ Value Name: UseLogonCredential Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253359`

### Rule: Run as different user must be removed from context menus.

**Rule ID:** `SV-253359r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "Run as different user" selection from context menus allows the use of credentials other than the currently logged on user. Using privileged credentials in a standard user session can expose those credentials to theft. Removing this option from context menus helps prevent this from occurring.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry values do not exist or are not configured as specified, this is a finding. The policy configures the same Value Name, Type and Value under four different registry paths. Registry Hive: HKEY_LOCAL_MACHINE Registry Paths: \SOFTWARE\Classes\batfile\shell\runasuser\ \SOFTWARE\Classes\cmdfile\shell\runasuser\ \SOFTWARE\Classes\exefile\shell\runasuser\ \SOFTWARE\Classes\mscfile\shell\runasuser\ Value Name: SuppressionPolicy Type: REG_DWORD Value: 0x00001000 (4096)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253360`

### Rule: Insecure logons to an SMB server must be disabled.

**Rule ID:** `SV-253360r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Insecure guest logons allow unauthenticated access to shared folders. Shared resources on a system must require authentication to establish proper access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\LanmanWorkstation\ Value Name: AllowInsecureGuestAuth Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253361`

### Rule: Internet connection sharing must be disabled.

**Rule ID:** `SV-253361r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet connection sharing makes it possible for an existing internet connection, such as through wireless, to be shared and used by other systems essentially creating a mobile hotspot. This exposes the system sharing the connection to others with potentially malicious purpose.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\Network Connections\ Value Name: NC_ShowSharedAccessUI Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253362`

### Rule: Hardened UNC Paths must be defined to require mutual authentication and integrity for at least the \\*\SYSVOL and \\*\NETLOGON shares.

**Rule ID:** `SV-253362r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Additional security requirements are applied to Universal Naming Convention (UNC) paths specified in Hardened UNC paths before allowing access them. This aids in preventing tampering with or spoofing of connections to these paths.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is applicable to domain-joined systems, for standalone systems this is NA. If the following registry values do not exist or are not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\NetworkProvider\HardenedPaths\ Value Name: \\*\NETLOGON Value Type: REG_SZ Value: RequireMutualAuthentication=1, RequireIntegrity=1 Value Name: \\*\SYSVOL Value Type: REG_SZ Value: RequireMutualAuthentication=1, RequireIntegrity=1 Additional entries would not be a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-253363`

### Rule: Windows 11 must be configured to prioritize ECC Curves with longer key lengths first.

**Rule ID:** `SV-253363r971535_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. By default Windows uses ECC curves with shorter key lengths first. Requiring ECC curves with longer key lengths to be prioritized first helps ensure more secure algorithms are used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Cryptography\Configuration\SSL\00010002\ Value Name: EccCurves Value Type: REG_MULTI_SZ Value: NistP384 NistP256

## Group: SRG-OS-000481-GPOS-00481

**Group ID:** `V-253364`

### Rule: Simultaneous connections to the internet or a Windows domain must be limited.

**Rule ID:** `SV-253364r958358_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Multiple network connections can provide additional attack vectors to a system and must be limited. The "Minimize the number of simultaneous connections to the Internet or a Windows Domain" setting prevents systems from automatically establishing multiple connections. When both wired and wireless connections are available, for example, the less preferred connection (typically wireless) will be disconnected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default behavior for "Minimize the number of simultaneous connections to the Internet or a Windows Domain" is "Enabled". If it exists and is configured with a value of "0", this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\WcmSvc\GroupPolicy\ Value Name: fMinimizeConnections Value Type: REG_DWORD Value: 3 (or if the Value Name does not exist)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253365`

### Rule: Connections to non-domain networks when connected to a domain authenticated network must be blocked.

**Rule ID:** `SV-253365r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Multiple network connections can provide additional attack vectors to a system and must be limited. When connected to a domain, communication must go through the domain connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\WcmSvc\GroupPolicy\ Value Name: fBlockNonDomain Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253366`

### Rule: Wi-Fi Sense must be disabled.

**Rule ID:** `SV-253366r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Wi-Fi Sense automatically connects the system to known hotspots and networks that contacts have shared. It also allows the sharing of the system's known networks to contacts. Automatically connecting to hotspots and shared networks can expose a system to unsecured or potentially malicious systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\WcmSvc\wifinetworkmanager\config\ Value Name: AutoConnectAllowedOEM Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-253367`

### Rule: Command line data must be included in process creation events.

**Rule ID:** `SV-253367r958422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Enabling "Include command line data for process creation events" will record the command line information with the process creation events in the log. This can provide additional detail when malware has run on a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\Audit\ Value Name: ProcessCreationIncludeCmdLine_Enabled Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253368`

### Rule: Windows 11 must be configured to enable Remote host allows delegation of non-exportable credentials.

**Rule ID:** `SV-253368r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An exportable version of credentials is provided to remote hosts when using credential delegation which exposes them to theft on the remote host. Restricted Admin mode or Remote Credential Guard allow delegation of non-exportable credentials providing additional protection of the credentials. Enabling this configures the host to support Restricted Admin mode or Remote Credential Guard.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\CredentialsDelegation\ Value Name: AllowProtectedCreds Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253369`

### Rule: Virtualization-based Security must be enabled on Windows 11 with the platform security level configured to Secure Boot or Secure Boot with DMA Protection.

**Rule ID:** `SV-253369r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Virtualization-based Security (VBS) provides the platform for the additional security features, Credential Guard and virtualization-based protection of code integrity. Secure Boot is the minimum security level with DMA protection providing additional memory protection. DMA Protection requires a CPU that supports input/output memory management unit (IOMMU).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm virtualization-based Security is enabled and running with Secure Boot or Secure Boot and DMA Protection. For those devices that support virtualization-based security (VBS) features, including Credential Guard or protection of code integrity, this must be enabled. If the system meets the hardware and firmware dependencies for enabling VBS but it is not enabled, this is a CAT III finding. Virtualization-based security, including Credential Guard, currently cannot be implemented in virtual desktop implementations (VDI) due to specific supporting requirements including a TPM, UEFI with Secure Boot, and the capability to run the Hyper-V feature within the virtual desktop. For VDIs where the virtual desktop instance is deleted or refreshed upon logoff, this is NA. Run "PowerShell" with elevated privileges (run as administrator). Enter the following: "Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard" If "RequiredSecurityProperties" does not include a value of "2" indicating "Secure Boot" (e.g., "{1, 2}"), this is a finding. If "Secure Boot and DMA Protection" is configured, "3" will also be displayed in the results (e.g., "{1, 2, 3}"). If "VirtualizationBasedSecurityStatus" is not a value of "2" indicating "Running", this is a finding. Alternately: Run "System Information". Under "System Summary", verify the following: If "Device Guard virtualization-based security" does not display "Running", this is finding. If "Device Guard Required Security Properties" does not display "Base Virtualization Support, Secure Boot", this is finding. If "Secure Boot and DMA Protection" is configured, "DMA Protection" will also be displayed (e.g., "Base Virtualization Support, Secure Boot, DMA Protection"). The policy settings referenced in the Fix section will configure the following registry values. However due to hardware requirements, the registry values alone do not ensure proper function. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\DeviceGuard\ Value Name: EnableVirtualizationBasedSecurity Value Type: REG_DWORD Value: 1 Value Name: RequirePlatformSecurityFeatures Value Type: REG_DWORD Value: 1 (Secure Boot only) or 3 (Secure Boot and DMA Protection) A Microsoft article on Credential Guard system requirement can be found at the following link: https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard-requirements

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253370`

### Rule: Credential Guard must be running on Windows 11 domain-joined systems.

**Rule ID:** `SV-253370r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Credential Guard uses virtualization-based security to protect information that could be used in credential theft attacks if compromised. This authentication information, which was stored in the Local Security Authority (LSA) in previous versions of Windows, is isolated from the rest of operating system and can only be accessed by privileged system software.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm Credential Guard is running on domain-joined systems. For those devices that support Credential Guard, this feature must be enabled. Organizations need to take the appropriate action to acquire and implement compatible hardware with Credential Guard enabled. Virtualization-based security, including Credential Guard, currently cannot be implemented in virtual desktop implementations (VDI) due to specific supporting requirements including a TPM, UEFI with Secure Boot, and the capability to run the Hyper-V feature within the virtual desktop. For VDIs where the virtual desktop instance is deleted or refreshed upon logoff, this is NA. Run "PowerShell" with elevated privileges (run as administrator). Enter the following: "Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard" If "SecurityServicesRunning" does not include a value of "1" (e.g., "{1, 2}"), this is a finding. Alternately: Run "System Information". Under "System Summary", verify the following: If "virtualization-based Services Running" does not list "Credential Guard", this is finding. The policy settings referenced in the Fix section will configure the following registry value. However, due to hardware requirements, the registry value alone does not ensure proper function. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\DeviceGuard\ Value Name: LsaCfgFlags Value Type: REG_DWORD Value: 0x00000001 (1) (Enabled with UEFI lock)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253371`

### Rule: Virtualization-based protection of code integrity must be enabled.

**Rule ID:** `SV-253371r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Virtualization-based protection of code integrity enforces kernel mode memory protections as well as protecting Code Integrity validation paths. This isolates the processes from the rest of the operating system and can only be accessed by privileged system software.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm virtualization-based protection of code integrity. For those devices that support the virtualization-based security (VBS) feature for protection of code integrity, this must be enabled. If the system meets the hardware, firmware and compatible device driver dependencies for enabling virtualization-based protection of code integrity but it is not enabled, this is a CAT II finding. Virtualization-based security currently cannot be implemented in virtual desktop implementations (VDI) due to specific supporting requirements including a TPM, UEFI with Secure Boot, and the capability to run the Hyper-V feature within the virtual desktop. For VDIs where the virtual desktop instance is deleted or refreshed upon logoff, this is NA. Run "PowerShell" with elevated privileges (run as administrator). Enter the following: "Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard" If "SecurityServicesRunning" does not include a value of "2" (e.g., "{1, 2}"), this is a finding. Alternately: Run "System Information". Under "System Summary", verify the following: If "Virtualization-based Security Services Running" does not list "Hypervisor enforced Code Integrity", this is finding. The policy settings referenced in the Fix section will configure the following registry value. However due to hardware requirements, the registry value alone does not ensure proper function. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\DeviceGuard\ Value Name: HypervisorEnforcedCodeIntegrity Value Type: REG_DWORD Value: 0x00000001 (1) (Enabled with UEFI lock), or 0x00000002 (2) (Enabled without lock)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253372`

### Rule: Early Launch Antimalware, Boot-Start Driver Initialization Policy must prevent boot drivers.

**Rule ID:** `SV-253372r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The default behavior is for Early Launch Antimalware - Boot-Start Driver Initialization policy is to enforce "Good, unknown and bad but critical" (preventing "bad"). By being launched first by the kernel, ELAM ( Early Launch Antimalware) is ensured to be launched before any third-party software, and is therefore able to detect malware in the boot process and prevent it from initializing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default behavior is for Early Launch Antimalware - Boot-Start Driver Initialization policy is to enforce "Good, unknown and bad but critical" (preventing "bad"). If the registry value name below does not exist, this is a finding. If it exists and is configured with a value of "7", this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Policies\EarlyLaunch\ Value Name: DriverLoadPolicy Value Type: REG_DWORD Value: 1, 3, or 8 Possible values for this setting are: 8 - Good only 1 - Good and unknown 3 - Good, unknown and bad but critical 7 - All (which includes "Bad" and would be a finding)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253373`

### Rule: Group Policy objects must be reprocessed even if they have not changed.

**Rule ID:** `SV-253373r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling this setting and then selecting the "Process even if the Group Policy objects have not changed" option ensures that the policies will be reprocessed even if none have been changed. This way, any unauthorized changes are forced to match the domain-based group policy settings again.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\Group Policy\{35378EAC-683F-11D2-A89A-00C04FBBCFA2} Value Name: NoGPOListChanges Value Type: REG_DWORD Value: 0

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253374`

### Rule: Downloading print driver packages over HTTP must be prevented.

**Rule ID:** `SV-253374r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some features may communicate with the vendor, sending system information or downloading data or components for the feature. Turning off this capability will prevent potentially sensitive information from being sent outside the enterprise and uncontrolled updates to the system. This setting prevents the computer from downloading print driver packages over HTTP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows NT\Printers\ Value Name: DisableWebPnPDownload Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253375`

### Rule: Web publishing and online ordering wizards must be prevented from downloading a list of providers.

**Rule ID:** `SV-253375r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some features may communicate with the vendor, sending system information or downloading data or components for the feature. Turning off this capability will prevent potentially sensitive information from being sent outside the enterprise and uncontrolled updates to the system. This setting prevents Windows from downloading a list of providers for the Web publishing and online ordering wizards.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\ Value Name: NoWebServices Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253376`

### Rule: Printing over HTTP must be prevented.

**Rule ID:** `SV-253376r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some features may communicate with the vendor, sending system information or downloading data or components for the feature. Turning off this capability will prevent potentially sensitive information from being sent outside the enterprise and uncontrolled updates to the system. This setting prevents the client computer from printing over HTTP, which allows the computer to print to printers on the intranet as well as the internet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows NT\Printers\ Value Name: DisableHTTPPrinting Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253377`

### Rule: Systems must at least attempt device authentication using certificates.

**Rule ID:** `SV-253377r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using certificates to authenticate devices to the domain provides increased security over passwords. By default systems will attempt to authenticate using certificates and fall back to passwords if the domain controller does not support certificates for devices. This may also be configured to always use certificates for device authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is applicable to domain-joined systems, for standalone systems this is NA. The default behavior for "Support device authentication using certificate" is "Automatic". If it exists and is configured with a value of "0", this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\Kerberos\Parameters\ Value Name: DevicePKInitEnabled Value Type: REG_DWORD Value: 1 (or if the Value Name does not exist)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253378`

### Rule: The network selection user interface (UI) must not be displayed on the logon screen.

**Rule ID:** `SV-253378r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling interaction with the network selection UI allows users to change connections to available networks without signing into Windows.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\System\ Value Name: DontDisplayNetworkSelectionUI Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253379`

### Rule: Local users on domain-joined computers must not be enumerated.

**Rule ID:** `SV-253379r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The username is one part of logon credentials that could be used to gain access to a system. Preventing the enumeration of users limits this information to authorized personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is applicable to domain-joined systems, for standalone systems this is NA. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\System\ Value Name: EnumerateLocalUsers Value Type: REG_DWORD Value: 0

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-253380`

### Rule: Users must be prompted for a password on resume from sleep (on battery).

**Rule ID:** `SV-253380r1051049_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication must always be required when accessing a system. This setting ensures the user is prompted for a password on resume from sleep (on battery).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Power\PowerSettings\0e796bdb-100d-47d6-a2d5-f7d2daa51f51\ Value Name: DCSettingIndex Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-253381`

### Rule: The user must be prompted for a password on resume from sleep (plugged in).

**Rule ID:** `SV-253381r1051050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication must always be required when accessing a system. This setting ensures the user is prompted for a password on resume from sleep (plugged in).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Power\PowerSettings\0e796bdb-100d-47d6-a2d5-f7d2daa51f51\ Value Name: ACSettingIndex Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-253382`

### Rule: Solicited Remote Assistance must not be allowed.

**Rule ID:** `SV-253382r958524_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Remote assistance allows another user to view or take control of the local session of a user. Solicited assistance is help that is specifically requested by the local user. This may allow unauthorized parties access to the resources on the computer.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services\ Value Name: fAllowToGetHelp Value Type: REG_DWORD Value: 0

## Group: SRG-OS-000379-GPOS-00164

**Group ID:** `V-253383`

### Rule: Unauthenticated RPC clients must be restricted from connecting to the RPC server.

**Rule ID:** `SV-253383r971545_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring RPC to restrict unauthenticated RPC clients from connecting to the RPC server will prevent anonymous connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows NT\Rpc\ Value Name: RestrictRemoteClients Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253384`

### Rule: The setting to allow Microsoft accounts to be optional for modern style apps must be enabled.

**Rule ID:** `SV-253384r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Control of credentials and the system must be maintained within the enterprise. Enabling this setting allows enterprise credentials to be used with modern style apps that support this, instead of Microsoft accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: MSAOptional Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253385`

### Rule: The Application Compatibility Program Inventory must be prevented from collecting data and sending the information to Microsoft.

**Rule ID:** `SV-253385r958478_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Some features may communicate with the vendor, sending system information or downloading data or components for the feature. Turning off this capability will prevent potentially sensitive information from being sent outside the enterprise and uncontrolled updates to the system. This setting will prevent the Program Inventory from collecting data about a system and sending the information to Microsoft.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\AppCompat\ Value Name: DisableInventory Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-253386`

### Rule: Autoplay must be turned off for non-volume devices.

**Rule ID:** `SV-253386r958804_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Allowing autoplay to execute may introduce malicious code to a system. Autoplay begins reading from a drive as soon as media is inserted in the drive. As a result, the setup file of programs or music on audio media may start. This setting will disable autoplay for non-volume devices (such as Media Transfer Protocol (MTP) devices).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\Explorer\ Value Name: NoAutoplayfornonVolume Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-253387`

### Rule: The default autorun behavior must be configured to prevent autorun commands.

**Rule ID:** `SV-253387r958804_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Allowing autorun commands to execute may introduce malicious code to a system. Configuring this setting prevents autorun commands from executing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\ Value Name: NoAutorun Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-253388`

### Rule: Autoplay must be disabled for all drives.

**Rule ID:** `SV-253388r958804_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Allowing autoplay to execute may introduce malicious code to a system. Autoplay begins reading from a drive as soon as media is inserted in the drive. As a result, the setup file of programs or music on audio media may start. By default, autoplay is disabled on removable drives, such as the floppy disk drive (but not the CD-ROM drive) and on network drives. If this policy is enabled, autoplay can be disabled on all drives.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\policies\Explorer\ Value Name: NoDriveTypeAutoRun Value Type: REG_DWORD Value: 0x000000ff (255) Note: If the value for NoDriveTypeAutorun is entered manually, it must be entered as "ff" when Hexadecimal is selected, or "255" with Decimal selected. Using the policy value specified in the Fix section will enter it correctly.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253389`

### Rule: Enhanced anti-spoofing for facial recognition must be enabled on Windows 11.

**Rule ID:** `SV-253389r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enhanced anti-spoofing provides additional protections when using facial recognition with devices that support it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Biometrics\FacialFeatures\ Value Name: EnhancedAntiSpoofing Value Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253390`

### Rule: Microsoft consumer experiences must be turned off.

**Rule ID:** `SV-253390r958478_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Microsoft consumer experiences provides suggestions and notifications to users, which may include the installation of Windows Store apps. Organizations may control the execution of applications through other means such as allowlisting. Turning off Microsoft consumer experiences will help prevent the unwanted installation of suggested applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\CloudContent\ Value Name: DisableWindowsConsumerFeatures Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-253391`

### Rule: Administrator accounts must not be enumerated during elevation.

**Rule ID:** `SV-253391r958518_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enumeration of administrator accounts when elevating can provide part of the logon information to an unauthorized user. This setting configures the system to always require users to type in a username and password to elevate a running application.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\CredUI\ Value Name: EnumerateAdministrators Value Type: REG_DWORD Value: 0

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253392`

### Rule: Enhanced diagnostic data must be limited to the minimum required to support Windows Analytics.

**Rule ID:** `SV-253392r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some features may communicate with the vendor, sending system information or downloading data or components for the feature. Limiting this capability will prevent potentially sensitive information from being sent outside the enterprise. The "Enhanced" level for telemetry includes additional information beyond "Security" and "Basic" on how Windows and apps are used and advanced reliability data. Windows Analytics can use a "limited enhanced" level to provide information such as health data for devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If "Enhanced" level is enabled for telemetry, this must be configured. If "Security" or "Basic" are configured, this is NA. (See WN11-CC-000205). If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\DataCollection\ Value Name: LimitEnhancedDiagnosticDataWindowsAnalytics Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000205-GPOS-00083

**Group ID:** `V-253393`

### Rule: Windows Telemetry must not be configured to Full.

**Rule ID:** `SV-253393r958564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some features may communicate with the vendor, sending system information or downloading data or components for the feature. Limiting this capability will prevent potentially sensitive information from being sent outside the enterprise. The "Security" option for Telemetry configures the lowest amount of data, effectively none outside of the Malicious Software Removal Tool (MSRT), Defender and telemetry client settings. "Basic" sends basic diagnostic and usage data and may be required to support some Microsoft services. "Enhanced" includes additional information on how Windows and apps are used and advanced reliability data. Windows Analytics can use a "limited enhanced" level to provide information such as health data for devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\DataCollection\ Value Name: AllowTelemetry Type: REG_DWORD Value: 0x00000000 (0) (Security) 0x00000001 (1) (Basic)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253394`

### Rule: Windows Update must not obtain updates from other PCs on the internet.

**Rule ID:** `SV-253394r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Windows 11 allows Windows Update to obtain updates from additional sources instead of Microsoft. In addition to Microsoft, updates can be obtained from and sent to PCs on the local network as well as on the Internet. This is part of the Windows Update trusted process, however to minimize outside exposure, obtaining updates from or sending to systems on the internet must be prevented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\DeliveryOptimization\ Value Name: DODownloadMode Value Type: REG_DWORD Value: 0x00000000 (0) - No peering (HTTP Only) 0x00000001 (1) - Peers on same NAT only (LAN) 0x00000002 (2) - Local Network / Private group peering (Group) 0x00000063 (99) - Simple download mode, no peering (Simple) 0x00000064 (100) - Bypass mode, Delivery Optimization not used (Bypass) A value of 0x00000003 (3), Internet, is a finding. Standalone systems (configured in Settings): If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\DeliveryOptimization\Config\ Value Name: DODownloadMode Value Type: REG_DWORD Value: 0x00000000 (0) - Off 0x00000001 (1) - LAN

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253395`

### Rule: The Microsoft Defender SmartScreen for Explorer must be enabled.

**Rule ID:** `SV-253395r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Microsoft Defender SmartScreen helps protect systems from programs downloaded from the internet that may be malicious. Enabling Microsoft Defender SmartScreen will warn or prevent users from running potentially malicious programs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is applicable to unclassified systems, for other systems this is NA. If the following registry values do not exist or are not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\System\ Value Name: EnableSmartScreen Value Type: REG_DWORD Value: 0x00000001 (1) And Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\System\ Value Name: ShellSmartScreenLevel Value Type: REG_SZ Value: Block

## Group: SRG-OS-000433-GPOS-00192

**Group ID:** `V-253396`

### Rule: Explorer Data Execution Prevention must be enabled.

**Rule ID:** `SV-253396r958928_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data Execution Prevention (DEP) provides additional protection by performing checks on memory to help prevent malicious code from running. This setting will prevent Data Execution Prevention from being turned off for File Explorer.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default behavior is for data execution prevention to be turned on for file explorer. If it exists and is configured with a value of "1", this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\Explorer\ Value Name: NoDataExecutionPrevention Value Type: REG_DWORD Value: 0 (or if the Value Name does not exist)

## Group: SRG-OS-000420-GPOS-00186

**Group ID:** `V-253397`

### Rule: File Explorer heap termination on corruption must be disabled.

**Rule ID:** `SV-253397r958902_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Legacy plug-in applications may continue to function when a File Explorer session has become corrupt. Disabling this feature will prevent this.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default behavior is for File Explorer heap termination on corruption to be enabled. If it exists and is configured with a value of "1", this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\Explorer\ Value Name: NoHeapTerminationOnCorruption Value Type: REG_DWORD Value: 0x00000000 (0) (or if the Value Name does not exist)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253398`

### Rule: File Explorer shell protocol must run in protected mode.

**Rule ID:** `SV-253398r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shell protocol will limit the set of folders applications can open when run in protected mode. Restricting files an application can open, to a limited set of folders, increases the security of Windows.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default behavior is for shell protected mode to be turned on for file explorer. If it exists and is configured with a value of "1", this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\ Value Name: PreXPSP2ShellProtocolBehavior Value Type: REG_DWORD Value: 0 (or if the Value Name does not exist)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253399`

### Rule: Windows 11 must be configured to disable Windows Game Recording and Broadcasting.

**Rule ID:** `SV-253399r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Windows Game Recording and Broadcasting is intended for use with games; however, it could potentially record screen shots of other applications and expose sensitive data. Disabling the feature will prevent this from occurring.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is NA for Windows 11 LTSC. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\GameDVR\ Value Name: AllowGameDVR Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253400`

### Rule: The use of a hardware security device with Windows Hello for Business must be enabled.

**Rule ID:** `SV-253400r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of a Trusted Platform Module (TPM) to store keys for Windows Hello for Business provides additional security. Keys stored in the TPM may only be used on that system while keys stored using software are more susceptible to compromise and could be used on other systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Virtual desktop implementations currently may not support the use of TPMs. For virtual desktop implementations where the virtual desktop instance is deleted or refreshed upon logoff, this is NA. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\PassportForWork\ Value Name: RequireSecurityDevice Type: REG_DWORD Value: 1

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253401`

### Rule: Windows 11 must be configured to require a minimum pin length of six characters or greater.

**Rule ID:** `SV-253401r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Windows allows the use of PINs as well as biometrics for authentication without sending a password to a network or website where it could be compromised. Longer minimum PIN lengths increase the available combinations an attacker would have to attempt. Shorter minimum length significantly reduces the strength.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\PassportForWork\PINComplexity\ Value Name: MinimumPINLength Type: REG_DWORD Value: 6 (or greater)

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-253402`

### Rule: Passwords must not be saved in the Remote Desktop Client.

**Rule ID:** `SV-253402r1051051_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Saving passwords in the Remote Desktop Client could allow an unauthorized user to establish a remote desktop session to another system. The system must be configured to prevent users from saving passwords in the Remote Desktop Client.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services\ Value Name: DisablePasswordSaving Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-253403`

### Rule: Local drives must be prevented from sharing with Remote Desktop Session Hosts.

**Rule ID:** `SV-253403r958524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing users from sharing the local drives on their client computers to Remote Session Hosts that they access helps reduce possible exposure of sensitive data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services\ Value Name: fDisableCdm Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-253404`

### Rule: Remote Desktop Services must always prompt a client for passwords upon connection.

**Rule ID:** `SV-253404r1051052_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting controls the ability of users to supply passwords automatically as part of their remote desktop connection. Disabling this setting would allow anyone to use the stored credentials in a connection item to connect to the terminal server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services\ Value Name: fPromptForPassword Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-253405`

### Rule: The Remote Desktop Session Host must require secure RPC communications.

**Rule ID:** `SV-253405r991554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing unsecure RPC communication exposes the system to man in the middle attacks and data disclosure attacks. A man in the middle attack occurs when an intruder captures packets between a client and server and modifies them before allowing the packets to be exchanged. Usually the attacker will modify the information in the packets in an attempt to cause either the client or server to reveal sensitive information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services\ Value Name: fEncryptRPCTraffic Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-253406`

### Rule: Remote Desktop Services must be configured with the client connection encryption set to the required level.

**Rule ID:** `SV-253406r958408_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote connections must be encrypted to prevent interception of data or sensitive information. Selecting "High Level" will ensure encryption of Remote Desktop Services sessions in both directions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services\ Value Name: MinEncryptionLevel Value Type: REG_DWORD Value: 3

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253407`

### Rule: Attachments must be prevented from being downloaded from RSS feeds.

**Rule ID:** `SV-253407r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Attachments from RSS feeds may not be secure. This setting will prevent attachments from being downloaded from RSS feeds.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Internet Explorer\Feeds\ Value Name: DisableEnclosureDownload Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253408`

### Rule: Basic authentication for RSS feeds over HTTP must not be used.

**Rule ID:** `SV-253408r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Basic authentication uses plain text passwords that could be used to compromise a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default behavior is for the Windows RSS platform to not use Basic authentication over HTTP connections. If it exists and is configured with a value of "1", this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Internet Explorer\Feeds\ Value Name: AllowBasicAuthInClear Value Type: REG_DWORD Value: 0 (or if the Value Name does not exist)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253409`

### Rule: Indexing of encrypted files must be turned off.

**Rule ID:** `SV-253409r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Indexing of encrypted files may expose sensitive data. This setting prevents encrypted files from being indexed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\Windows Search\ Value Name: AllowIndexingEncryptedStoresOrItems Value Type: REG_DWORD Value: 0

## Group: SRG-OS-000362-GPOS-00149

**Group ID:** `V-253410`

### Rule: Users must be prevented from changing installation options.

**Rule ID:** `SV-253410r1051053_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Installation options for applications are typically controlled by administrators. This setting prevents users from changing installation options that may bypass security features.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\Installer\ Value Name: EnableUserControl Value Type: REG_DWORD Value: 0

## Group: SRG-OS-000362-GPOS-00149

**Group ID:** `V-253411`

### Rule: The Windows Installer feature "Always install with elevated privileges" must be disabled.

**Rule ID:** `SV-253411r1051054_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Standard user accounts must not be granted elevated privileges. Enabling Windows Installer to elevate privileges when installing applications can allow malicious persons and applications to gain full control of a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\Installer\ Value Name: AlwaysInstallElevated Value Type: REG_DWORD Value: 0

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253412`

### Rule: Users must be notified if a web-based program attempts to install software.

**Rule ID:** `SV-253412r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Web-based programs may attempt to install malicious software on a system. Ensuring users are notified if a web-based program attempts to install software allows them to refuse the installation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default behavior is for Internet Explorer to warn users and select whether to allow or refuse installation when a web-based program attempts to install software on the system. If it exists and is configured with a value of "1", this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\Installer\ Value Name: SafeForScripting Value Type: REG_DWORD Value: 0 (or if the Value Name does not exist)

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-253413`

### Rule: Automatically signing in the last interactive user after a system-initiated restart must be disabled.

**Rule ID:** `SV-253413r991591_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Windows can be configured to automatically sign the user back in after a Windows Update restart. Some protections are in place to help ensure this is done in a secure fashion; however, disabling this will prevent the caching of credentials for this purpose and also ensure the user is aware of the restart.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: DisableAutomaticRestartSignOn Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-253414`

### Rule: PowerShell script block logging must be enabled on Windows 11.

**Rule ID:** `SV-253414r958422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Enabling PowerShell script block logging will record detailed information from the processing of PowerShell commands and scripts. This can provide additional detail when malware has run on a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging\ Value Name: EnableScriptBlockLogging Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000041-GPOS-00019

**Group ID:** `V-253415`

### Rule: PowerShell Transcription must be enabled on Windows 11.

**Rule ID:** `SV-253415r958420_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. Enabling PowerShell Transcription will record detailed information from the processing of PowerShell commands and scripts. This can provide additional detail when malware has run on a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\PowerShell\Transcription\ Value Name: EnableTranscripting Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-253416`

### Rule: The Windows Remote Management (WinRM) client must not use Basic authentication.

**Rule ID:** `SV-253416r958510_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Basic authentication uses plain text passwords that could be used to compromise a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\WinRM\Client\ Value Name: AllowBasic Value Type: REG_DWORD Value: 0

## Group: SRG-OS-000393-GPOS-00173

**Group ID:** `V-253417`

### Rule: The Windows Remote Management (WinRM) client must not allow unencrypted traffic.

**Rule ID:** `SV-253417r958848_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unencrypted remote access to a system can allow sensitive information to be compromised. Windows remote management connections must be encrypted to prevent this.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\WinRM\Client\ Value Name: AllowUnencryptedTraffic Value Type: REG_DWORD Value: 0

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-253418`

### Rule: The Windows Remote Management (WinRM) service must not use Basic authentication.

**Rule ID:** `SV-253418r958510_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Basic authentication uses plain text passwords that could be used to compromise a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\WinRM\Service\ Value Name: AllowBasic Value Type: REG_DWORD Value: 0

## Group: SRG-OS-000394-GPOS-00174

**Group ID:** `V-253419`

### Rule: The Windows Remote Management (WinRM) service must not allow unencrypted traffic.

**Rule ID:** `SV-253419r958850_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unencrypted remote access to a system can allow sensitive information to be compromised. Windows remote management connections must be encrypted to prevent this.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\WinRM\Service\ Value Name: AllowUnencryptedTraffic Value Type: REG_DWORD Value: 0

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-253420`

### Rule: The Windows Remote Management (WinRM) service must not store RunAs credentials.

**Rule ID:** `SV-253420r1051055_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Storage of administrative credentials could allow unauthorized access. Disallowing the storage of RunAs credentials for Windows Remote Management will prevent them from being used with plug-ins.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\WinRM\Service\ Value Name: DisableRunAs Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-253421`

### Rule: The Windows Remote Management (WinRM) client must not use Digest authentication.

**Rule ID:** `SV-253421r958510_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Digest authentication is not as strong as other options and may be subject to man-in-the-middle attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\WinRM\Client\ Value Name: AllowDigest Value Type: REG_DWORD Value: 0

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-253422`

### Rule: Windows 11 must be configured to prevent Windows apps from being activated by voice while the system is locked.

**Rule ID:** `SV-253422r958400_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing Windows apps to be activated by voice from the lock screen could allow for unauthorized use. Requiring logon will ensure the apps are only used by authorized personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The setting is NA when the "Allow voice activation" policy is configured to disallow applications to be activated with voice for all users. If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\AppPrivacy\ Value Name: LetAppsActivateWithVoiceAboveLock Type: REG_DWORD Value: 0x00000002 (2) If the following registry value exists and is configured as specified, requirement is NA: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\Windows\AppPrivacy\ Value Name: LetAppsActivateWithVoice Type: REG_DWORD Value: 0x00000002 (2)

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253423`

### Rule: The convenience PIN for Windows 11 must be disabled.

**Rule ID:** `SV-253423r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This policy controls whether a domain user can sign in using a convenience PIN to prevent enabling (Password Stuffer).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \Software\Policies\Microsoft\Windows\System Value Name: AllowDomainPINLogon Value Type: REG_DWORD Value data: 0

## Group: SRG-OS-000031-GPOS-00012

**Group ID:** `V-253424`

### Rule: Windows Ink Workspace must be configured to disallow access above the lock.

**Rule ID:** `SV-253424r958404_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This action secures Windows Ink, which contains applications and features oriented toward pen computing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \Software\Policies\Microsoft\WindowsInkWorkspace Value Name: AllowWindowsInkWorkspace Value Type: REG_DWORD Value data: 1

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253425`

### Rule: Windows 11 must be configured to prevent users from receiving suggestions for third-party or additional applications.

**Rule ID:** `SV-253425r958478_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Windows spotlight features may suggest apps and content from third-party software publishers in addition to Microsoft apps and content.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_CURRENT_USER Registry Path: \SOFTWARE\Policies\Microsoft\Windows\CloudContent\ Value Name: DisableThirdPartySuggestions Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000471-GPOS-00216

**Group ID:** `V-253426`

### Rule: Windows 11 Kernel (Direct Memory Access) DMA Protection must be enabled.

**Rule ID:** `SV-253426r991580_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kernel DMA Protection to protect PCs against drive-by Direct Memory Access (DMA) attacks using PCI hot plug devices connected to Thunderbolt 3 ports. Drive-by DMA attacks can lead to disclosure of sensitive information residing on a PC, or even injection of malware that allows attackers to bypass the lock screen or control PCs remotely.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \Software\Policies\Microsoft\Windows\Kernel DMA Protection Value Name: DeviceEnumerationPolicy Value Type: REG_DWORD Value: 0

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-253427`

### Rule: The DoD Root CA certificates must be installed in the Trusted Root Store.

**Rule ID:** `SV-253427r958448_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure secure DoD websites and DoD-signed code are properly validated, the system must trust the DoD Root Certificate Authorities (CAs). The DoD root certificates will ensure that the trust chain is established for server certificates issued from the DoD CAs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DoD Root CA certificates are installed as Trusted Root Certification Authorities. The certificates and thumbprints referenced below apply to unclassified systems; refer to PKE documentation for other networks. Run "PowerShell" as an administrator. Execute the following command: Get-ChildItem -Path Cert:Localmachine\root | Where Subject -Like "*DoD*" | FL Subject, Thumbprint, NotAfter If the following certificate "Subject" and "Thumbprint" information is not displayed, this is a finding. Subject: CN=DoD Root CA 3, OU=PKI, OU=DoD, O=U.S. Government, C=US Thumbprint: D73CA91102A2204A36459ED32213B467D7CE97FB NotAfter: 12/30/2029 Subject: CN=DoD Root CA 4, OU=PKI, OU=DoD, O=U.S. Government, C=US Thumbprint: B8269F25DBD937ECAFD4C35A9838571723F2D026 NotAfter: 7/25/2032 Subject: CN=DoD Root CA 5, OU=PKI, OU=DoD, O=U.S. Government, C=US Thumbprint: 4ECB5CC3095670454DA1CBD410FC921F46B8564B NotAfter: 6/14/2041 Subject: CN=DoD Root CA 6 OU=PKI, OU=DoD, O=U.S. Government, C=US Thumbprint: D37ECF61C0B4ED88681EF3630C4E2FC787B37AEF NotAfter: 1/24/2053 Alternately, use the Certificates MMC snap-in: Run "MMC". Select "File", "Add/Remove Snap-in". Select "Certificates", click "Add". Select "Computer account", click "Next". Select "Local computer: (the computer this console is running on)", click "Finish". Click "OK". Expand "Certificates" and navigate to Trusted Root Certification Authorities >> Certificates. For each of the DoD Root CA certificates noted below: Right-click on the certificate and select "Open". Select the "Details" tab. Scroll to the bottom and select "Thumbprint". If the DoD Root CA certificates below are not listed or the value for the "Thumbprint" field is not as noted, this is a finding. DoD Root CA 3 Thumbprint: D73CA91102A2204A36459ED32213B467D7CE97FB Valid to: Sunday, December 30, 2029 DoD Root CA 4 Thumbprint: B8269F25DBD937ECAFD4C35A9838571723F2D026 Valid to: Sunday, July 25, 2032 DoD Root CA 5 Thumbprint: 4ECB5CC3095670454DA1CBD410FC921F46B8564B Valid to: Friday, June 14, 2041 DoD Root CA 6 Thumbprint : D37ECF61C0B4ED88681EF3630C4E2FC787B37AEF Valid to: Friday, January 24, 2053

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-253428`

### Rule: The External Root CA certificates must be installed in the Trusted Root Store on unclassified systems.

**Rule ID:** `SV-253428r958448_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure secure websites protected with External Certificate Authority (ECA) server certificates are properly validated, the system must trust the ECA Root CAs. The ECA root certificates will ensure the trust chain is established for server certificates issued from the External CAs. This requirement only applies to unclassified systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ECA Root CA certificates are installed on unclassified systems as Trusted Root Certification Authorities. Run "PowerShell" as an administrator. Execute the following command: Get-ChildItem -Path Cert:Localmachine\root | Where Subject -Like "*ECA*" | FL Subject, Thumbprint, NotAfter If the following certificate "Subject" and "Thumbprint" information is not displayed, this is a finding. Subject: CN=ECA Root CA 4, OU=ECA, O=U.S. Government, C=US Thumbprint: 73E8BB08E337D6A5A6AEF90CFFDD97D9176CB582 NotAfter: 12/30/2029 Alternately use the Certificates MMC snap-in: Run "MMC". Select "File", "Add/Remove Snap-in". Select "Certificates", click "Add". Select "Computer account", click "Next". Select "Local computer: (the computer this console is running on)", click "Finish". Click "OK". Expand "Certificates" and navigate to Trusted Root Certification Authorities >> Certificates. For each of the ECA Root CA certificates noted below: Right-click on the certificate and select "Open". Select the "Details" tab. Scroll to the bottom and select "Thumbprint". If the ECA Root CA certificates below are not listed or the value for the "Thumbprint" field is not as noted, this is a finding. ECA Root CA 4 Thumbprint: 73E8BB08E337D6A5A6AEF90CFFDD97D9176CB582 Valid to: Sunday, December 30, 2029

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-253429`

### Rule: The DoD Interoperability Root CA cross-certificates must be installed in the Untrusted Certificates Store on unclassified systems.

**Rule ID:** `SV-253429r958448_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure users do not experience denial of service when performing certificate-based authentication to DoD websites due to the system chaining to a root other than DoD Root CAs, the DoD Interoperability Root CA cross-certificates must be installed in the Untrusted Certificate Store. This requirement only applies to unclassified systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DoD Interoperability cross-certificates are installed on unclassified systems as Untrusted Certificates. Run "PowerShell" as an administrator. Execute the following command: Get-ChildItem -Path Cert:Localmachine\disallowed | Where {$_.Issuer -Like "*DoD Interoperability*" -and $_.Subject -Like "*DoD*"} | FL Subject, Issuer, Thumbprint, NotAfter If the following certificate "Subject", "Issuer", and "Thumbprint" information is not displayed, this is a finding. Subject: CN=DoD Root CA 3, OU=PKI, OU=DoD, O=U.S. Government, C=US Issuer: CN=DoD Interoperability Root CA 2, OU=PKI, OU=DoD, O=U.S. Government, C=US Thumbprint: 49CBE933151872E17C8EAE7F0ABA97FB610F6477 NotAfter: 11/16/2024 Subject: CN=DoD Root CA 3, OU=PKI, OU=DoD, O=U.S. Government, C=US Issuer: CN=DoD Interoperability Root CA 2, OU=PKI, OU=DoD, O=U.S. Government, C=US Thumbprint: AC06108CA348CC03B53795C64BF84403C1DBD341 NotAfter: 1/22/2022 Alternately, use the Certificates MMC snap-in: Run "MMC". Select "File", "Add/Remove Snap-in". Select "Certificates", click "Add". Select "Computer account", click "Next". Select "Local computer: (the computer this console is running on)", click "Finish". Click "OK". Expand "Certificates" and navigate to Untrusted Certificates >> Certificates. For each certificate with "DoD Root CA...." under "Issued To" and "DoD Interoperability Root CA...." under "Issued By": Right-click on the certificate and select "Open". Select the "Details" tab. Scroll to the bottom and select "Thumbprint". If the certificates below are not listed or the value for the "Thumbprint" field is not as noted, this is a finding. Issued To: DoD Root CA 3 Issued By: Interoperability Root CA 2 Thumbprint : 49CBE933151872E17C8EAE7F0ABA97FB610F6477 Valid to: Saturday, November 16, 2024

## Group: SRG-OS-000403-GPOS-00182

**Group ID:** `V-253430`

### Rule: The US DOD CCEB Interoperability Root CA cross-certificates must be installed in the Untrusted Certificates Store on unclassified systems.

**Rule ID:** `SV-253430r1081058_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure users do not experience denial of service when performing certificate-based authentication to DOD websites due to the system chaining to a root other than DOD Root CAs, the US DOD CCEB Interoperability Root CA cross-certificates must be installed in the Untrusted Certificate Store. This requirement only applies to unclassified systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the US DOD CCEB Interoperability Root CA cross-certificate is installed on unclassified systems as an Untrusted Certificate. Run "PowerShell" as an administrator. Execute the following command: Get-ChildItem -Path Cert:Localmachine\disallowed | Where Issuer -Like "*CCEB Interoperability*" | FL Subject, Issuer, Thumbprint, NotAfter If the following certificate "Subject", "Issuer", and "Thumbprint" information is not displayed, this is a finding. Subject: CN=DOD Root CA 3, OU=PKI, OU=DOD, O=U.S. Government, C=US Issuer: CN=US DOD CCEB Interoperability Root CA 2, OU=PKI, OU=DOD, O=U.S. Government, C=US Thumbprint: 9B74964506C7ED9138070D08D5F8B969866560C8 NotAfter: 7/18/2025 9:56:22 A Alternately, use the Certificates MMC snap-in: Run "MMC". Select "File", then click "Add/Remove Snap-in". Select "Certificates", then click "Add". Select "Computer account", then click "Next". Select "Local computer: (the computer this console is running on)", then click "Finish". Click "OK". Expand "Certificates" and navigate to Untrusted Certificates >> Certificates. For each certificate with "US DOD CCEB Interoperability Root CA..." under "Issued By": Right-click on the certificate and select "Open". Select the "Details" tab. Scroll to the bottom and select "Thumbprint". If the certificate below is not listed or the value for the "Thumbprint" field is not as noted, this is a finding. Subject: CN=DOD Root CA 3, OU=PKI, OU=DOD, O=U.S. Government, C=US Issuer: CN=US DOD CCEB Interoperability Root CA 2, OU=PKI, OU=DOD, O=U.S. Government, C=US Thumbprint: Thumbprint: 9B74964506C7ED9138070D08D5F8B969866560C8 NotAfter: 7/18/2025 9:56:22 AM Subject: CN=DOD Root CA 6, OU=PKI, OU=DOD, O=U.S. Government, C=US Issuer: CN=US DOD CCEB Interoperability Root CA 2, OU=PKI, OU=DOD, O=U.S. Government, C=US Thumbprint: D471CA32F7A692CE6CBB6196BD3377FE4DBCD106 NotAfter: 7/18/2026 9:56:22 AM

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253431`

### Rule: Default permissions for the HKEY_LOCAL_MACHINE registry hive must be maintained.

**Rule ID:** `SV-253431r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The registry is integral to the function, security, and stability of the Windows system. Changing the system's registry permissions allows the possibility of unauthorized and anonymous modification to the operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the default registry permissions for the keys note below of the HKEY_LOCAL_MACHINE hive. If any non-privileged groups such as Everyone, Users or Authenticated Users have greater than Read permission, this is a finding. Run "Regedit". Right click on the registry areas noted below. Select "Permissions..." and the "Advanced" button. HKEY_LOCAL_MACHINE\SECURITY Type - "Allow" for all Inherited from - "None" for all Principal - Access - Applies to SYSTEM - Full Control - This key and subkeys Administrators - Special - This key and subkeys HKEY_LOCAL_MACHINE\SOFTWARE Type - "Allow" for all Inherited from - "None" for all Principal - Access - Applies to Users - Read - This key and subkeys Administrators - Full Control - This key and subkeys SYSTEM - Full Control - This key and subkeys CREATOR OWNER - Full Control - This key and subkeys ALL APPLICATION PACKAGES - Read - This key and subkeys HKEY_LOCAL_MACHINE\SYSTEM Type - "Allow" for all Inherited from - "None" for all Principal - Access - Applies to Users - Read - This key and subkeys Administrators - Full Control - This key and subkeys SYSTEM - Full Control - This key and subkeys CREATOR OWNER - Full Control - This key and subkeys ALL APPLICATION PACKAGES - Read - This key and subkeys Other subkeys under the noted keys may also be sampled. There may be some instances where non-privileged groups have greater than read permission. Microsoft has given Read permission to the SOFTWARE and SYSTEM registry keys in later versions of Windows 11 to the following SID, this is currently not a finding. S-1-15-3-1024-1065365936-1281604716-3511738428-1654721687-432734479-3232135806-4053264122-3456934681 If the defaults have not been changed, these are not a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-253432`

### Rule: The built-in administrator account must be disabled.

**Rule ID:** `SV-253432r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The built-in administrator account is a well-known account subject to attack. It also provides no accountability to individual administrators on a system. It must be disabled to prevent its use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> Security Options. If the value for "Accounts: Administrator account status" is not set to "Disabled", this is a finding.

## Group: SRG-OS-000121-GPOS-00062

**Group ID:** `V-253433`

### Rule: The built-in guest account must be disabled.

**Rule ID:** `SV-253433r958504_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A system faces an increased vulnerability threat if the built-in guest account is not disabled. This account is a known account that exists on all Windows systems and cannot be deleted. This account is initialized during the installation of the operating system with no password assigned.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> Security Options. If the value for "Accounts: Guest account status" is not set to "Disabled", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253434`

### Rule: Local accounts with blank passwords must be restricted to prevent access from the network.

**Rule ID:** `SV-253434r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An account without a password can allow unauthorized access to a system as only the username would be required. Password policies must prevent accounts with blank passwords from existing on a system. However, if a local account with a blank password did exist, enabling this setting will prevent network access, limiting the account to local console logon only.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\ Value Name: LimitBlankPasswordUse Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253435`

### Rule: The built-in administrator account must be renamed.

**Rule ID:** `SV-253435r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The built-in administrator account is a well-known account subject to attack. Renaming this account to an unidentified name improves the protection of this account and the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> Security Options. If the value for "Accounts: Rename administrator account" is set to "Administrator", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253436`

### Rule: The built-in guest account must be renamed.

**Rule ID:** `SV-253436r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The built-in guest account is a well-known user account on all Windows systems and, as initially installed, does not require a password. This can allow access to system resources by unauthorized users. Renaming this account to an unidentified name improves the protection of this account and the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> Security Options. If the value for "Accounts: Rename guest account" is set to "Guest", this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-253437`

### Rule: Audit policy using subcategories must be enabled.

**Rule ID:** `SV-253437r958442_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Maintaining an audit trail of system activity logs can help identify configuration errors, troubleshoot service disruptions, and analyze compromises that have occurred, as well as detect attacks. Audit logs are necessary to provide a trail of evidence in case the system or network is compromised. Collecting this data is essential for analyzing the security of information assets and detecting signs of suspicious and unexpected behavior. This setting allows administrators to enable more precise auditing capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\ Value Name: SCENoApplyLegacyAuditPolicy Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-253438`

### Rule: Outgoing secure channel traffic must be encrypted or signed.

**Rule ID:** `SV-253438r958908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Requests sent on the secure channel are authenticated, and sensitive information (such as passwords) is encrypted, but not all information is encrypted. If this policy is enabled, outgoing secure channel traffic will be encrypted and signed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Netlogon\Parameters\ Value Name: RequireSignOrSeal Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-253439`

### Rule: Outgoing secure channel traffic must be encrypted.

**Rule ID:** `SV-253439r958908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Requests sent on the secure channel are authenticated, and sensitive information (such as passwords) is encrypted, but not all information is encrypted. If this policy is enabled, outgoing secure channel traffic will be encrypted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Netlogon\Parameters\ Value Name: SealSecureChannel Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-253440`

### Rule: Outgoing secure channel traffic must be signed.

**Rule ID:** `SV-253440r958908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Requests sent on the secure channel are authenticated, and sensitive information (such as passwords) is encrypted, but the channel is not integrity checked. If this policy is enabled, outgoing secure channel traffic will be signed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Netlogon\Parameters\ Value Name: SignSecureChannel Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253441`

### Rule: The computer account password must not be prevented from being reset.

**Rule ID:** `SV-253441r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Computer account passwords are changed automatically on a regular basis. Disabling automatic password changes can make the system more vulnerable to malicious access. Frequent password changes can be a significant safeguard for the system. A new password for the computer account will be generated every 30 days.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Netlogon\Parameters\ Value Name: DisablePasswordChange Value Type: REG_DWORD Value: 0

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253442`

### Rule: The maximum age for machine account passwords must be configured to 30 days or less.

**Rule ID:** `SV-253442r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Computer account passwords are changed automatically on a regular basis. This setting controls the maximum password age that a machine account may have. This setting must be set to no more than 30 days, ensuring the machine changes its password monthly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
(remove)This is the default configuration for this setting (30 days). If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Netlogon\Parameters\ Value Name: MaximumPasswordAge Value Type: REG_DWORD Value: 0x0000001e (30) (or less, excluding 0)

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-253443`

### Rule: The system must be configured to require a strong session key.

**Rule ID:** `SV-253443r958908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A computer connecting to a domain controller will establish a secure channel. Requiring strong session keys enforces 128-bit encryption between systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\Netlogon\Parameters\ Value Name: RequireStrongKey Value Type: REG_DWORD Value: 1 Warning: This setting may prevent a system from being joined to a domain if not configured consistently between systems.

## Group: SRG-OS-000279-GPOS-00109

**Group ID:** `V-253444`

### Rule: The machine inactivity limit must be set to 15 minutes, locking the system with the screensaver.

**Rule ID:** `SV-253444r958636_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unattended systems are susceptible to unauthorized use and must be locked when unattended. The screen saver must be set at a maximum of 15 minutes and be password protected. This protects critical and sensitive data from exposure to unauthorized personnel with physical access to the computer. Satisfies: SRG-OS-000279-GPOS-00109, SRG-OS-000163-GPOS-00072</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: InactivityTimeoutSecs Value Type: REG_DWORD Value: 0x00000384 (900) (or less, excluding "0" which is effectively disabled)

## Group: SRG-OS-000024-GPOS-00007

**Group ID:** `V-253445`

### Rule: The required legal notice must be configured to display before console logon.

**Rule ID:** `SV-253445r958392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to display the logon banner prior to a logon attempt will negate legal proceedings resulting from unauthorized access to system resources. Satisfies: SRG-OS-000024-GPOS-00007, SRG-OS-000228-GPOS-00088, SRG-OS-000024-GPOS-00007</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: LegalNoticeText Value Type: REG_SZ Value: You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details.

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-253446`

### Rule: The Windows message title for the legal notice must be configured.

**Rule ID:** `SV-253446r958586_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Failure to display the logon banner prior to a logon attempt will negate legal proceedings resulting from unauthorized access to system resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: LegalNoticeCaption Value Type: REG_SZ Value: See message title above "DoD Notice and Consent Banner", "US Department of Defense Warning Statement" or a site-defined equivalent, this is a finding. If a site-defined title is used, it can in no case contravene or modify the language of the banner text required in WN11-SO-000075.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253447`

### Rule: Caching of logon credentials must be limited.

**Rule ID:** `SV-253447r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The default Windows configuration caches the last logon credentials for users who log on interactively to a system. This feature is provided for system availability reasons, such as the user's machine being disconnected from the network or domain controllers being unavailable. Even though the credential cache is well-protected, if a system is attacked, an unauthorized individual may isolate the password to a domain user account using a password-cracking program and gain access to the domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is the default configuration for this setting (10 logons to cache). If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\ Value Name: CachedLogonsCount Value Type: REG_SZ Value: 10 (or less) This setting only applies to domain-joined systems, however, it is configured by default on all systems.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253448`

### Rule: The Smart Card removal option must be configured to Force Logoff or Lock Workstation.

**Rule ID:** `SV-253448r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unattended systems are susceptible to unauthorized use and must be locked. Configuring a system to lock when a smart card is removed will ensure the system is inaccessible when unattended.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\ Value Name: SCRemoveOption Value Type: REG_SZ Value: 1 (Lock Workstation) or 2 (Force Logoff) This can be left not configured or set to "No action" on workstations with the following conditions. This must be documented with the ISSO. -The setting cannot be configured due to mission needs, or because it interferes with applications. -Policy must be in place that users manually lock workstations when leaving them unattended. -The screen saver is properly configured to lock as required.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-253449`

### Rule: The Windows SMB client must be configured to always perform SMB packet signing.

**Rule ID:** `SV-253449r958908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The server message block (SMB) protocol provides the basis for many network operations. Digitally signed SMB packets aid in preventing man-in-the-middle attacks. If this policy is enabled, the SMB client will only communicate with an SMB server that performs SMB packet signing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters\ Value Name: RequireSecuritySignature Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-253450`

### Rule: Unencrypted passwords must not be sent to third-party SMB Servers.

**Rule ID:** `SV-253450r987796_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some non-Microsoft SMB servers only support unencrypted (plain text) password authentication. Sending plain text passwords across the network, when authenticating to an SMB server, reduces the overall security of the environment. Check with the vendor of the SMB server to see if there is a way to support encrypted password authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters\ Value Name: EnablePlainTextPassword Value Type: REG_DWORD Value: 0

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-253451`

### Rule: The Windows SMB server must be configured to always perform SMB packet signing.

**Rule ID:** `SV-253451r958908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The server message block (SMB) protocol provides the basis for many network operations. Digitally signed SMB packets aid in preventing man-in-the-middle attacks. If this policy is enabled, the SMB server will only communicate with an SMB client that performs SMB packet signing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\LanManServer\Parameters\ Value Name: RequireSecuritySignature Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253452`

### Rule: Anonymous SID/Name translation must not be allowed.

**Rule ID:** `SV-253452r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Allowing anonymous SID/Name translation can provide sensitive information for accessing a system. Only authorized users must be able to perform such translations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> Security Options. If the value for "Network access: Allow anonymous SID/Name translation" is not set to "Disabled", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253453`

### Rule: Anonymous enumeration of SAM accounts must not be allowed.

**Rule ID:** `SV-253453r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Anonymous enumeration of SAM accounts allows anonymous log on users (null session connections) to list all accounts names, thus providing a list of potential points to attack the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\ Value Name: RestrictAnonymousSAM Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-253454`

### Rule: Anonymous enumeration of shares must be restricted.

**Rule ID:** `SV-253454r958524_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Allowing anonymous logon users (null session connections) to list all account names and enumerate all shared resources can provide a map of potential points to attack the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\ Value Name: RestrictAnonymous Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253455`

### Rule: The system must be configured to prevent anonymous users from having the same rights as the Everyone group.

**Rule ID:** `SV-253455r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access by anonymous users must be restricted. If this setting is enabled, then anonymous users have the same rights and permissions as the built-in Everyone group. Anonymous users must not have these permissions or rights.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\ Value Name: EveryoneIncludesAnonymous Value Type: REG_DWORD Value: 0

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-253456`

### Rule: Anonymous access to Named Pipes and Shares must be restricted.

**Rule ID:** `SV-253456r958524_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Allowing anonymous access to named pipes or shares provides the potential for unauthorized system access. This setting restricts access to those defined in "Network access: Named Pipes that can be accessed anonymously" and "Network access: Shares that can be accessed anonymously", both of which must be blank under other requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\LanManServer\Parameters\ Value Name: RestrictNullSessAccess Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253457`

### Rule: Remote calls to the Security Account Manager (SAM) must be restricted to Administrators.

**Rule ID:** `SV-253457r1081060_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Windows SAM stores users' passwords. Restricting remote rpc connections to the SAM to Administrators helps protect those credentials.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\ Value Name: RestrictRemoteSAM Value Type: REG_SZ Value: O:BAG:BAD:(A;;RC;;;BA) If a domain application account such as for a management tool requires this user right, this would not be a finding. Vendor documentation must support the requirement for having the user right. The requirement must be documented with the ISSO.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253458`

### Rule: NTLM must be prevented from falling back to a Null session.

**Rule ID:** `SV-253458r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>NTLM sessions that are allowed to fall back to Null (unauthenticated) sessions may gain unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\LSA\MSV1_0\ Value Name: allownullsessionfallback Value Type: REG_DWORD Value: 0

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253459`

### Rule: PKU2U authentication using online identities must be prevented.

**Rule ID:** `SV-253459r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>PKU2U is a peer-to-peer authentication protocol. This setting prevents online identities from authenticating to domain-joined systems. Authentication will be centrally managed with Windows user accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\LSA\pku2u\ Value Name: AllowOnlineID Value Type: REG_DWORD Value: 0

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-253460`

### Rule: Kerberos encryption types must be configured to prevent the use of DES and RC4 encryption suites.

**Rule ID:** `SV-253460r971535_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Certain encryption types are no longer considered secure. This setting configures a minimum encryption type for Kerberos, preventing the use of the DES and RC4 encryption suites.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\Kerberos\Parameters\ Value Name: SupportedEncryptionTypes Value Type: REG_DWORD Value: 0x7ffffff8 (2147483640)

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-253461`

### Rule: The system must be configured to prevent the storage of the LAN Manager hash of passwords.

**Rule ID:** `SV-253461r1051056_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The LAN Manager hash uses a weak encryption algorithm and there are several tools available that use this hash to retrieve account passwords. This setting controls whether or not a LAN Manager hash of the password is stored in the SAM the next time the password is changed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\ Value Name: NoLMHash Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253462`

### Rule: The LanMan authentication level must be set to send NTLMv2 response only, and to refuse LM and NTLM.

**Rule ID:** `SV-253462r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Kerberos v5 authentication protocol is the default for authentication of users who are logging on to domain accounts. NTLM, which is less secure, is retained in later Windows versions for compatibility with clients and servers that are running earlier versions of Windows or applications that still use it. It is also used to authenticate logons to stand-alone computers that are running later versions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\ Value Name: LmCompatibilityLevel Value Type: REG_DWORD Value: 5

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253463`

### Rule: The system must be configured to the required LDAP client signing level.

**Rule ID:** `SV-253463r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting controls the signing requirements for LDAP clients. This setting must be set to Negotiate signing or Require signing, depending on the environment and type of LDAP server in use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\LDAP\ Value Name: LDAPClientIntegrity Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253464`

### Rule: The system must be configured to meet the minimum session security requirement for NTLM SSP based clients.

**Rule ID:** `SV-253464r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Microsoft has implemented a variety of security support providers for use with RPC sessions. All of the options must be enabled to ensure the maximum security level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\MSV1_0\ Value Name: NTLMMinClientSec Value Type: REG_DWORD Value: 0x20080000 (537395200)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253465`

### Rule: The system must be configured to meet the minimum session security requirement for NTLM SSP based servers.

**Rule ID:** `SV-253465r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Microsoft has implemented a variety of security support providers for use with RPC sessions. All of the options must be enabled to ensure the maximum security level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\MSV1_0\ Value Name: NTLMMinServerSec Value Type: REG_DWORD Value: 0x20080000 (537395200)

## Group: SRG-OS-000478-GPOS-00223

**Group ID:** `V-253466`

### Rule: The system must be configured to use FIPS-compliant algorithms for encryption, hashing, and signing.

**Rule ID:** `SV-253466r959006_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting ensures that the system uses algorithms that are FIPS-compliant for encryption, hashing, and signing. FIPS-compliant algorithms meet specific standards established by the U.S. Government and must be the algorithms used for all OS encryption functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\FIPSAlgorithmPolicy\ Value Name: Enabled Value Type: REG_DWORD Value: 1 Warning: Clients with this setting enabled will not be able to communicate via digitally encrypted or signed protocols with servers that do not support these algorithms.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253467`

### Rule: The default permissions of global system objects must be increased.

**Rule ID:** `SV-253467r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Windows systems maintain a global list of shared system resources such as DOS device names, mutexes, and semaphores. Each type of object is created with a default DACL that specifies who can access the objects with what permissions. If this policy is enabled, the default DACL is stronger, allowing non-admin users to read shared objects, but not modify shared objects that they did not create.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Control\Session Manager\ Value Name: ProtectionMode Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000373-GPOS-00157

**Group ID:** `V-253468`

### Rule: User Account Control approval mode for the built-in Administrator must be enabled.

**Rule ID:** `SV-253468r1051057_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User Account Control (UAC) is a security mechanism for limiting the elevation of privileges, including administrative accounts, unless authorized. This setting configures the built-in Administrator account so that it runs in Admin Approval Mode.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: FilterAdministratorToken Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-253469`

### Rule: User Account Control must prompt administrators for consent on the secure desktop.

**Rule ID:** `SV-253469r958518_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User Account Control (UAC) is a security mechanism for limiting the elevation of privileges, including administrative accounts, unless authorized. This setting configures the elevation requirements for logged on administrators to complete a task that requires raised privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: ConsentPromptBehaviorAdmin Value Type: REG_DWORD Value: 2 (Prompt for consent on the secure desktop)

## Group: SRG-OS-000105-GPOS-00052

**Group ID:** `V-253470`

### Rule: Windows 11 must use multifactor authentication for local and network access to privileged and nonprivileged accounts.

**Rule ID:** `SV-253470r1106510_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged and nonprivileged functions is greatly increased. All domain accounts must be enabled for multifactor authentication with the exception of local emergency accounts. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: 1) Something a user knows (e.g., password/PIN); 2) Something a user has (e.g., cryptographic identification device, token); and 3) Something a user is (e.g., biometric). A privileged account is defined as an information system account with authorizations of a privileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the internet). Local access is defined as access to an organizational information system by a user (or process acting on behalf of a user) communicating through a direct connection without the use of a network. The DoD CAC with DoD-approved PKI is an example of multifactor authentication. Satisfies: SRG-OS-000106-GPOS-00053, SRG-OS-000107-GPOS-00054, SRG-OS-000108-GPOS-00055</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is not a member of a domain, this is Not Applicable. If all of the following settings exist and are populated, this is not a finding. \HKLM\SOFTWARE\Microsoft\Cryptography\Calais\Readers \HKLM\SOFTWARE\Microsoft\Cryptography\Calais\SmartCards

## Group: SRG-OS-000373-GPOS-00157

**Group ID:** `V-253471`

### Rule: User Account Control must automatically deny elevation requests for standard users.

**Rule ID:** `SV-253471r1051058_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User Account Control (UAC) is a security mechanism for limiting the elevation of privileges, including administrative accounts, unless authorized. Denying elevation requests from standard user accounts requires tasks that need elevation to be initiated by accounts with administrative privileges. This ensures correct accounts are used on the system for privileged tasks to help mitigate credential theft.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: ConsentPromptBehaviorUser Value Type: REG_DWORD Value: 0

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-253472`

### Rule: User Account Control must be configured to detect application installations and prompt for elevation.

**Rule ID:** `SV-253472r958518_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User Account Control (UAC) is a security mechanism for limiting the elevation of privileges, including administrative accounts, unless authorized. This setting requires Windows to respond to application installation requests by prompting for credentials.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: EnableInstallerDetection Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-253473`

### Rule: User Account Control must only elevate UIAccess applications that are installed in secure locations.

**Rule ID:** `SV-253473r958518_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User Account Control (UAC) is a security mechanism for limiting the elevation of privileges, including administrative accounts, unless authorized. This setting configures Windows to only allow applications installed in a secure location on the file system, such as the Program Files or the Windows\System32 folders, to run with elevated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: EnableSecureUIAPaths Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000373-GPOS-00157

**Group ID:** `V-253474`

### Rule: User Account Control must run all administrators in Admin Approval Mode, enabling UAC.

**Rule ID:** `SV-253474r1051059_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User Account Control (UAC) is a security mechanism for limiting the elevation of privileges, including administrative accounts, unless authorized. This setting enables UAC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: EnableLUA Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-253475`

### Rule: User Account Control must virtualize file and registry write failures to per-user locations.

**Rule ID:** `SV-253475r958518_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User Account Control (UAC) is a security mechanism for limiting the elevation of privileges, including administrative accounts, unless authorized. This setting configures non-UAC compliant applications to run in virtualized file and registry entries in per-user locations, allowing them to run.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ Value Name: EnableVirtualization Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-253476`

### Rule: Passwords for enabled local Administrator accounts must be changed at least every 60 days.

**Rule ID:** `SV-253476r1051060_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The longer a password is in use, the greater the opportunity for someone to gain unauthorized knowledge of the password. A local Administrator account is not generally used and its password may not be changed as frequently as necessary. Changing the password for enabled Administrator accounts on a regular basis will limit its exposure. Windows LAPS must be used to change the built-in Administrator account password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If there are no enabled local Administrator accounts, this is Not Applicable. Review the password last set date for the enabled local Administrator account. On the standalone or domain-joined workstation: Open "PowerShell". Enter "Get-LocalUser -Name * | Select-Object *". If the "PasswordLastSet" date is greater than "60" days old for the local Administrator account for administering the computer/domain, this is a finding. Verify LAPS is configured and operational. Navigate to Local Computer Policy >> Computer Configuration >> Administrative Templates >> System >> LAPS >> Password Settings >> Set to enabled. Password Complexity, large letters + small letters + numbers + special, Password Length 14, Password Age 60. If not configured as shown, this is a finding. Verify LAPS Operational logs >> Event Viewer >> Applications and Services Logs >> Microsoft >> Windows >> LAPS >> Operational. Verify LAPS policy process is completing. If it is not, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-253477`

### Rule: Toast notifications to the lock screen must be turned off.

**Rule ID:** `SV-253477r958478_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Toast notifications that are displayed on the lock screen could display sensitive information to unauthorized personnel. Turning off this feature will limit access to the information to a logged on user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following registry value does not exist or is not configured as specified, this is a finding: Registry Hive: HKEY_CURRENT_USER Registry Path: \SOFTWARE\Policies\Microsoft\Windows\CurrentVersion\PushNotifications\ Value Name: NoToastApplicationNotificationOnLockScreen Value Type: REG_DWORD Value: 1

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-253478`

### Rule: Zone information must be preserved when saving attachments.

**Rule ID:** `SV-253478r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preserving zone of origin (internet, intranet, local, restricted) information on file attachments allows Windows to determine risk.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default behavior is for Windows to mark file attachments with their zone information. If it exists and is configured with a value of "1", this is a finding. Registry Hive: HKEY_CURRENT_USER Registry Path: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Attachments\ Value Name: SaveZoneInformation Value Type: REG_DWORD Value: 0x00000002 (2) (or if the Value Name does not exist)

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253479`

### Rule: The "Access Credential Manager as a trusted caller" user right must not be assigned to any groups or accounts.

**Rule ID:** `SV-253479r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Access Credential Manager as a trusted caller" user right may be able to retrieve the credentials of other accounts from Credential Manager.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts are granted the "Access Credential Manager as a trusted caller" user right, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-253480`

### Rule: The "Access this computer from the network" user right must only be assigned to the Administrators and Remote Desktop Users groups.

**Rule ID:** `SV-253480r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Access this computer from the network" user right may access resources on the system, and must be limited to those that require it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts other than the following are granted the "Access this computer from the network" user right, this is a finding: Administrators Remote Desktop Users If a domain application account such as for a management tool requires this user right, this would not be a finding. Vendor documentation must support the requirement for having the user right. The requirement must be documented with the ISSO. The application account, managed at the domain level, must meet requirements for application account passwords, such as length and frequency of changes as defined in the Windows Server STIGs.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253481`

### Rule: The "Act as part of the operating system" user right must not be assigned to any groups or accounts.

**Rule ID:** `SV-253481r958726_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Act as part of the operating system" user right can assume the identity of any user and gain access to resources that user is authorized to access. Any accounts with this right can take complete control of a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts (to include administrators), are granted the "Act as part of the operating system" user right, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-253482`

### Rule: The "Allow log on locally" user right must only be assigned to the Administrators and Users groups.

**Rule ID:** `SV-253482r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Allow log on locally" user right can log on interactively to a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts other than the following are granted the "Allow log on locally" user right, this is a finding: Administrators Users

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253483`

### Rule: The "Back up files and directories" user right must only be assigned to the Administrators group.

**Rule ID:** `SV-253483r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Back up files and directories" user right can circumvent file and directory permissions and could allow access to sensitive data."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts other than the following are granted the "Back up files and directories" user right, this is a finding: Administrators

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253484`

### Rule: The "Change the system time" user right must only be assigned to Administrators and Local Service.

**Rule ID:** `SV-253484r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Change the system time" user right can change the system time, which can impact authentication, as well as affect time stamps on event log entries.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts other than the following are granted the "Change the system time" user right, this is a finding: Administrators LOCAL SERVICE

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253485`

### Rule: The "Create a pagefile" user right must only be assigned to the Administrators group.

**Rule ID:** `SV-253485r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Create a pagefile" user right can change the size of a pagefile, which could affect system performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts other than the following are granted the "Create a pagefile" user right, this is a finding: Administrators

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253486`

### Rule: The "Create a token object" user right must not be assigned to any groups or accounts.

**Rule ID:** `SV-253486r958726_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Create a token object" user right allows a process to create an access token. This could be used to provide elevated rights and compromise a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts are granted the "Create a token object" user right, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253487`

### Rule: The "Create global objects" user right must only be assigned to Administrators, Service, Local Service, and Network Service.

**Rule ID:** `SV-253487r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Create global objects" user right can create objects that are available to all sessions, which could affect processes in other users' sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts other than the following are granted the "Create global objects" user right, this is a finding: Administrators LOCAL SERVICE NETWORK SERVICE SERVICE

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253488`

### Rule: The "Create permanent shared objects" user right must not be assigned to any groups or accounts.

**Rule ID:** `SV-253488r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Create permanent shared objects" user right could expose sensitive data by creating shared objects.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts are granted the "Create permanent shared objects" user right, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253489`

### Rule: The "Create symbolic links" user right must only be assigned to the Administrators group.

**Rule ID:** `SV-253489r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Create symbolic links" user right can create pointers to other objects, which could potentially expose the system to attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts other than the following are granted the "Create symbolic links" user right, this is a finding: Administrators If the workstation has an approved use of Hyper-V, such as being used as a dedicated admin workstation using Hyper-V to separate administration and standard user functions, "NT VIRTUAL MACHINES\VIRTUAL MACHINE" may be assigned this user right and is not a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253490`

### Rule: The "Debug programs" user right must only be assigned to the Administrators group.

**Rule ID:** `SV-253490r958726_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Debug Programs" user right can attach a debugger to any process or to the kernel, providing complete access to sensitive and critical operating system components. This right is given to Administrators in the default configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts other than the following are granted the "Debug Programs" user right, this is a finding: Administrators

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-253491`

### Rule: The "Deny access to this computer from the network" user right on workstations must be configured to prevent access from highly privileged domain accounts and local accounts on domain systems and unauthenticated access on all systems.

**Rule ID:** `SV-253491r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Deny access to this computer from the network" right defines the accounts that are prevented from logging on from the network. In an Active Directory Domain, denying logons to the Enterprise Admins and Domain Admins groups on lower trust systems helps mitigate the risk of privilege escalation from credential theft attacks, which could lead to the compromise of an entire domain. Local accounts on domain-joined systems must also be assigned this right to decrease the risk of lateral movement resulting from credential theft attacks. The Guests group must be assigned this right to prevent unauthenticated access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If the following groups or accounts are not defined for the "Deny access to this computer from the network" right, this is a finding: Domain Systems Only: Enterprise Admins group Domain Admins group Local account (see Note below) All Systems: Guests group Privileged Access Workstations (PAWs) dedicated to the management of Active Directory are exempt from denying the Enterprise Admins and Domain Admins groups. (See the Windows Privileged Access Workstation STIG for PAW requirements.) Note: "Local account" is a built-in security group used to assign user rights and permissions to all local accounts.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-253492`

### Rule: The "Deny log on as a batch job" user right on domain-joined workstations must be configured to prevent access from highly privileged domain accounts.

**Rule ID:** `SV-253492r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Deny log on as a batch job" right defines accounts that are prevented from logging on to the system as a batch job, such as Task Scheduler. In an Active Directory Domain, denying logons to the Enterprise Admins and Domain Admins groups on lower trust systems helps mitigate the risk of privilege escalation from credential theft attacks which could lead to the compromise of an entire domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is applicable to domain-joined systems, for standalone systems this is NA. Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If the following groups or accounts are not defined for the "Deny log on as a batch job" right, this is a finding: Domain Systems Only: Enterprise Admin Group Domain Admin Group

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-253493`

### Rule: The "Deny log on as a service" user right on Windows 11 domain-joined workstations must be configured to prevent access from highly privileged domain accounts.

**Rule ID:** `SV-253493r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Deny log on as a service" right defines accounts that are denied log on as a service. In an Active Directory Domain, denying logons to the Enterprise Admins and Domain Admins groups on lower trust systems helps mitigate the risk of privilege escalation from credential theft attacks which could lead to the compromise of an entire domain. Incorrect configurations could prevent services from starting and result in a DoS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is applicable to domain-joined systems, for standalone systems this is NA. Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If the following groups or accounts are not defined for the "Deny log on as a service" right , this is a finding: Domain Systems Only: Enterprise Admins Group Domain Admins Group

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-253494`

### Rule: The "Deny log on locally" user right on workstations must be configured to prevent access from highly privileged domain accounts on domain systems and unauthenticated access on all systems.

**Rule ID:** `SV-253494r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Deny log on locally" right defines accounts that are prevented from logging on interactively. In an Active Directory Domain, denying logons to the Enterprise Admins and Domain Admins groups on lower trust systems helps mitigate the risk of privilege escalation from credential theft attacks, which could lead to the compromise of an entire domain. The Guests group must be assigned this right to prevent unauthenticated access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If the following groups or accounts are not defined for the "Deny log on locally" right, this is a finding. Domain Systems Only: Enterprise Admins Group Domain Admins Group Privileged Access Workstations (PAWs) dedicated to the management of Active Directory are exempt from denying the Enterprise Admins and Domain Admins groups. (See the Windows Privileged Access Workstation STIG for PAW requirements.) All Systems: Guests Group

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-253495`

### Rule: The "Deny log on through Remote Desktop Services" user right on Windows 11 workstations must be configured to prevent access from highly privileged domain accounts and local accounts on domain systems and unauthenticated access on all systems.

**Rule ID:** `SV-253495r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Deny log on through Remote Desktop Services" right defines the accounts that are prevented from logging on using Remote Desktop Services. If Remote Desktop Services is not used by the organization, the Everyone group must be assigned this right to prevent all access. In an Active Directory Domain, denying logons to the Enterprise Admins and Domain Admins groups on lower trust systems helps mitigate the risk of privilege escalation from credential theft attacks, which could lead to the compromise of an entire domain. Local accounts on domain-joined systems must also be assigned this right to decrease the risk of lateral movement resulting from credential theft attacks. The Guests group must be assigned this right to prevent unauthenticated access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If the following groups or accounts are not defined for the "Deny log on through Remote Desktop Services" right, this is a finding: If Remote Desktop Services is not used by the organization, the "Everyone" group can replace all of the groups listed below. Domain Systems Only: Enterprise Admins group Domain Admins group Local account (see Note below) All Systems: Guests group Privileged Access Workstations (PAWs) dedicated to the management of Active Directory are exempt from denying the Enterprise Admins and Domain Admins groups. (See the Windows Privileged Access Workstation STIG for PAW requirements.) Note: "Local account" is a built-in security group used to assign user rights and permissions to all local accounts.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253496`

### Rule: The "Enable computer and user accounts to be trusted for delegation" user right must not be assigned to any groups or accounts.

**Rule ID:** `SV-253496r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Enable computer and user accounts to be trusted for delegation" user right allows the "Trusted for Delegation" setting to be changed. This could potentially allow unauthorized users to impersonate other users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts are granted the "Enable computer and user accounts to be trusted for delegation" user right, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253497`

### Rule: The "Force shutdown from a remote system" user right must only be assigned to the Administrators group.

**Rule ID:** `SV-253497r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Force shutdown from a remote system" user right can remotely shut down a system which could result in a DoS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts other than the following are granted the "Force shutdown from a remote system" user right, this is a finding: Administrators

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253498`

### Rule: The "Impersonate a client after authentication" user right must only be assigned to Administrators, Service, Local Service, and Network Service.

**Rule ID:** `SV-253498r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Impersonate a client after authentication" user right allows a program to impersonate another user or account to run on their behalf. An attacker could potentially use this to elevate privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts other than the following are granted the "Impersonate a client after authentication" user right, this is a finding: Administrators LOCAL SERVICE NETWORK SERVICE SERVICE

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253499`

### Rule: The "Load and unload device drivers" user right must only be assigned to the Administrators group.

**Rule ID:** `SV-253499r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Load and unload device drivers" user right allows device drivers to dynamically be loaded on a system by a user. This could potentially be used to install malicious code by an attacker.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts other than the following are granted the "Load and unload device drivers" user right, this is a finding: Administrators

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253500`

### Rule: The "Lock pages in memory" user right must not be assigned to any groups or accounts.

**Rule ID:** `SV-253500r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. The "Lock pages in memory" user right allows physical memory to be assigned to processes, which could cause performance issues or a DoS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts are granted the "Lock pages in memory" user right, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-253501`

### Rule: The "Manage auditing and security log" user right must only be assigned to the Administrators group.

**Rule ID:** `SV-253501r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Manage auditing and security log" user right can manage the security log and change auditing configurations. This could be used to clear evidence of tampering. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000063-GPOS-00032</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts other than the following are granted the "Manage auditing and security log" user right, this is a finding: Administrators If the organization has an "Auditors" group the assignment of this group to the user right would not be a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253502`

### Rule: The "Modify firmware environment values" user right must only be assigned to the Administrators group.

**Rule ID:** `SV-253502r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Modify firmware environment values" user right can change hardware configuration environment variables. This could result in hardware failures or a DoS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts other than the following are granted the "Modify firmware environment values" user right, this is a finding: Administrators

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253503`

### Rule: The "Perform volume maintenance tasks" user right must only be assigned to the Administrators group.

**Rule ID:** `SV-253503r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Perform volume maintenance tasks" user right can manage volume and disk configurations. They could potentially delete volumes, resulting in data loss or a DoS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts other than the following are granted the "Perform volume maintenance tasks" user right, this is a finding: Administrators

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253504`

### Rule: The "Profile single process" user right must only be assigned to the Administrators group.

**Rule ID:** `SV-253504r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Profile single process" user right can monitor non-system processes performance. An attacker could potentially use this to identify processes to attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts other than the following are granted the "Profile single process" user right, this is a finding: Administrators

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253505`

### Rule: The "Restore files and directories" user right must only be assigned to the Administrators group.

**Rule ID:** `SV-253505r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Restore files and directories" user right can circumvent file and directory permissions and could allow access to sensitive data. It could also be used to over-write more current data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts other than the following are granted the "Restore files and directories" user right, this is a finding: Administrators

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-253506`

### Rule: The "Take ownership of files or other objects" user right must only be assigned to the Administrators group.

**Rule ID:** `SV-253506r958726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inappropriate granting of user rights can provide system, administrative, and other high-level capabilities. Accounts with the "Take ownership of files or other objects" user right can take ownership of objects and make changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the effective setting in Local Group Policy Editor. Run "gpedit.msc". Navigate to Local Computer Policy >> Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> User Rights Assignment. If any groups or accounts other than the following are granted the "Take ownership of files or other objects" user right, this is a finding: Administrators

## Group: SRG-OS-000185-GPOS-00079

**Group ID:** `V-256893`

### Rule: Internet Explorer must be disabled for Windows 11.

**Rule ID:** `SV-256893r958552_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Explorer 11 (IE11) is not supported on Windows 11 semi-annual channel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if IE11 is installed or enabled on Windows 11 semi-annual channel. If IE11 is installed or not disabled on Windows 11 semi-annual channel, this is a finding. If IE11 is installed on an unsupported operating system and is enabled or installed, this is a finding. For more information, visit: https://learn.microsoft.com/en-us/lifecycle/faq/internet-explorer-microsoft-edge#what-is-the-lifecycle-policy-for-internet-explorer-

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-257592`

### Rule: Windows 11 must not have portproxy enabled or in use.

**Rule ID:** `SV-257592r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Having portproxy enabled or configured in Windows 10 could allow a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the registry key for existence of proxied ports: HKLM\SYSTEM\CurrentControlSet\Services\PortProxy\. If the key contains v4tov4\tcp\ or is populated v4tov4\tcp\, this is a finding. Run "netsh interface portproxy show all". If the command displays any results, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-257770`

### Rule: Windows 11 must have command line process auditing events enabled for failures.

**Rule ID:** `SV-257770r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When this policy setting is enabled, the operating system generates audit events when a process fails to start and the name of the program or user that created it. These audit events can assist in understanding how a computer is being used and tracking user activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure Audit Process Creation auditing has been enabled: Computer Configuration >> Windows Settings >> Security Settings >> Advanced Audit Policy Configuration >> System Audit Policy >> Detailed Tracking >> Audit Process Creation. If "Audit Process Creation" is not set to "Failure", this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-268317`

### Rule: Copilot in Windows must be disabled for Windows 11

**Rule ID:** `SV-268317r1016371_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some features may communicate with the vendor, sending system information or downloading data or components for the feature. Turning off this capability will prevent potentially sensitive information from being sent outside the enterprise and uncontrolled updates to the system. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following local computer policy is not configured as specified, this is a finding: User Configuration >> Administrative Templates >> Windows Components >> Windows Copilot >> "Turn off Windows Copilot" to "Enabled”.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-268318`

### Rule: Windows 11 systems must use either Group Policy or an approved Mobile Device Management (MDM) product to enforce STIG compliance.

**Rule ID:** `SV-268318r1081062_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without Windows 11 systems being managed, devices could be rogue and become targets of an attacker.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Windows 11 system is receiving policy from either group Policy or an MDM with the following steps: From a command line or PowerShell: gpresult /R OS Configuration: Member Workstation If the system is not being managed by GPO, ask the administrator to indicate which MDM is managing the device. If the Window 11 system is not receiving policy from either group Policy or an MDM, this is a finding. This is NA for standalone, nondomain joined systems.

