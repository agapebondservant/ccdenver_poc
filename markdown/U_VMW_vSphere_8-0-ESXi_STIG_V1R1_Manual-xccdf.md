# STIG Benchmark: VMware vSphere 8.0 ESXi Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000021-VMM-000050

**Group ID:** `V-258728`

### Rule: The ESXi host must enforce the limit of three consecutive invalid logon attempts by a user.

**Rule ID:** `SV-258728r933245_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized access via user password guessing, otherwise known as brute forcing, is reduced. Once the configured number of attempts is reached, the account is locked by the ESXi host.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Security.AccountLockFailures" value and verify it is set to "3". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Security.AccountLockFailures If the "Security.AccountLockFailures" setting is set to a value other than "3", this is a finding.

## Group: SRG-OS-000023-VMM-000060

**Group ID:** `V-258729`

### Rule: The ESXi host must display the Standard Mandatory DOD Notice and Consent Banner before granting access to the system via the Direct Console User Interface (DCUI).

**Rule ID:** `SV-258729r933248_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the host ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for a host that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) VMM (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for VMMs that have severe limitations on the number of characters that can be displayed in the banner: "I've read (literal ampersand) consent to terms in IS user agreem't." Satisfies: SRG-OS-000023-VMM-000060, SRG-OS-000024-VMM-000070</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Annotations.WelcomeMessage" value and verify it contains the standard mandatory DOD notice and consent banner. or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Annotations.WelcomeMessage If the "Annotations.WelcomeMessage" setting does not contain the standard mandatory DOD notice and consent banner, this is a finding.

## Group: SRG-OS-000027-VMM-000080

**Group ID:** `V-258730`

### Rule: The ESXi host must enable lockdown mode.

**Rule ID:** `SV-258730r933251_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling Lockdown Mode disables direct access to an ESXi host, requiring the host to be managed remotely from vCenter Server. This is done to ensure the roles and access controls implemented in vCenter are always enforced and users cannot bypass them by logging on to a host directly. By forcing all interaction to occur through vCenter Server, the risk of someone inadvertently attaining elevated privileges or performing tasks that are not properly audited is greatly reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For environments that do not use vCenter server to manage ESXi, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Security Profile. Scroll down to "Lockdown Mode" and verify it is set to "Enabled" (Normal or Strict). or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Select Name,@{N="Lockdown";E={$_.Extensiondata.Config.LockdownMode}} If "Lockdown Mode" is disabled, this is a finding.

## Group: SRG-OS-000029-VMM-000100

**Group ID:** `V-258731`

### Rule: The ESXi host client must be configured with an idle session timeout.

**Rule ID:** `SV-258731r933254_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ESXi host client is the UI served up by the host itself, outside of vCenter. It is accessed at https://<ESX FQDN>/ui. ESXi is not usually administered via this interface for long periods, and all users will be highly privileged. Implementing a mandatory session idle limit will ensure that orphaned, forgotten, or ignored sessions will be closed promptly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "UserVars.HostClientSessionTimeout" value and verify it is set to "900" or less. or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name UserVars.HostClientSessionTimeout If the "UserVars.HostClientSessionTimeout" setting is not set to "900" or less, this is a finding.

## Group: SRG-OS-000033-VMM-000140

**Group ID:** `V-258732`

### Rule: The ESXi host Secure Shell (SSH) daemon must use FIPS 140-2 validated cryptographic modules to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-258732r933257_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. OpenSSH on the ESXi host ships with a FIPS 140-2 validated cryptographic module and it is enabled by default. For backward compatibility reasons, this can be disabled so this setting must be audited and corrected if necessary.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # esxcli system security fips140 ssh get or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.security.fips140.ssh.get.invoke() Expected result: Enabled: true If the FIPS mode is not enabled for SSH, this is a finding.

## Group: SRG-OS-000037-VMM-000150

**Group ID:** `V-258733`

### Rule: The ESXi must produce audit records containing information to establish what type of events occurred.

**Rule ID:** `SV-258733r933260_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what types of events occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Satisfies: SRG-OS-000037-VMM-000150, SRG-OS-000063-VMM-000310</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Config.HostAgent.log.level" value and verify it is set to "info". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Config.HostAgent.log.level If the "Config.HostAgent.log.level" setting is not set to "info", this is a finding. Note: Verbose logging level is acceptable for troubleshooting purposes.

## Group: SRG-OS-000069-VMM-000360

**Group ID:** `V-258734`

### Rule: The ESXi host must enforce password complexity by configuring a password quality policy.

**Rule ID:** `SV-258734r933263_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To enforce the use of complex passwords, minimum numbers of characters of different classes are mandated. The use of complex passwords reduces the ability of attackers to successfully obtain valid passwords using guessing or exhaustive search techniques. Complexity requirements increase the password search space by requiring users to construct passwords from a larger character set than they may otherwise use. Satisfies: SRG-OS-000069-VMM-000360, SRG-OS-000070-VMM-000370, SRG-OS-000071-VMM-000380, SRG-OS-000072-VMM-000390, SRG-OS-000072-VMM-000390, SRG-OS-000078-VMM-000450, SRG-OS-000266-VMM-000940</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Security.PasswordQualityControl" value and verify it is set to "similar=deny retry=3 min=disabled,disabled,disabled,disabled,15". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Security.PasswordQualityControl If the "Security.PasswordQualityControl" setting is set to a value other than "similar=deny retry=3 min=disabled,disabled,disabled,disabled,15", this is a finding.

## Group: SRG-OS-000077-VMM-000440

**Group ID:** `V-258735`

### Rule: The ESXi host must prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-258735r933266_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user or root used the same password continuously or was allowed to change it back shortly after being forced to change it to something else, it would provide a potential intruder with the opportunity to keep guessing at one user's password until it was guessed correctly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Security.PasswordHistory" value and verify it is set to "5" or greater. or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Security.PasswordHistory If the "Security.PasswordHistory" setting is set to a value other than 5 or greater, this is a finding.

## Group: SRG-OS-000095-VMM-000480

**Group ID:** `V-258736`

### Rule: The ESXi host must be configured to disable nonessential capabilities by disabling the Managed Object Browser (MOB).

**Rule ID:** `SV-258736r933269_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The MOB provides a way to explore the object model used by the VMkernel to manage the host and enables configurations to be changed. This interface is meant to be used primarily for debugging the vSphere Software Development Kit (SDK), but because there are no access controls it could also be used as a method to obtain information about a host being targeted for unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Config.HostAgent.plugins.solo.enableMob" value and verify it is set to "false". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Config.HostAgent.plugins.solo.enableMob If the "Config.HostAgent.plugins.solo.enableMob" setting is not set to "false", this is a finding.

## Group: SRG-OS-000104-VMM-000500

**Group ID:** `V-258737`

### Rule: The ESXi host must uniquely identify and must authenticate organizational users by using Active Directory.

**Rule ID:** `SV-258737r933272_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Join ESXi hosts to an Active Directory domain to eliminate the need to create and maintain multiple local user accounts. Using Active Directory for user authentication simplifies the ESXi host configuration, ensures password complexity and reuse policies are enforced, and reduces the risk of security breaches and unauthorized access. Note: If the Active Directory group "ESX Admins" (default) exists, all users and groups assigned as members to this group will have full administrative access to all ESXi hosts in the domain. Satisfies: SRG-OS-000104-VMM-000500, SRG-OS-000109-VMM-000550, SRG-OS-000112-VMM-000560, SRG-OS-000113-VMM-000570, SRG-OS-000123-VMM-000620</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For systems that do not use Active Directory and have no local user accounts other than root and/or service accounts, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Authentication Services. Verify the "Directory Services Type" is set to "Active Directory". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-VMHostAuthentication For systems that do not use Active Directory and do have local user accounts, other than root and/or service accounts, this is a finding. If the "Directory Services Type" is not set to "Active Directory", this is a finding.

## Group: SRG-OS-000107-VMM-000530

**Group ID:** `V-258738`

### Rule: The ESXi host Secure Shell (SSH) daemon must ignore .rhosts files.

**Rule ID:** `SV-258738r933275_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH trust relationships mean a compromise on one host can allow an attacker to move trivially to other hosts. SSH can emulate the behavior of the obsolete "rsh" command in allowing users to enable insecure access to their accounts via ".rhosts" files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # esxcli system ssh server config list -k ignorerhosts or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.ssh.server.config.list.invoke() | Where-Object {$_.Key -eq 'ignorerhosts'} Example result: ignorerhosts yes If "ignorerhosts" is not configured to "yes", this is a finding.

## Group: SRG-OS-000163-VMM-000700

**Group ID:** `V-258739`

### Rule: The ESXi host must set a timeout to automatically end idle shell sessions after fifteen minutes.

**Rule ID:** `SV-258739r933278_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user forgets to log out of their local or remote ESXi Shell session, the idle connection will remain open indefinitely and increase the likelihood of inappropriate host access via session hijacking. The "ESXiShellInteractiveTimeOut" allows the automatic termination of idle shell sessions. Satisfies: SRG-OS-000163-VMM-000700, SRG-OS-000279-VMM-001010</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "UserVars.ESXiShellInteractiveTimeOut" value and verify it is set to less than "900" and not "0". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name UserVars.ESXiShellInteractiveTimeOut If the "UserVars.ESXiShellInteractiveTimeOut" setting is set to a value greater than "900" or "0", this is a finding.

## Group: SRG-OS-000257-VMM-000910

**Group ID:** `V-258740`

### Rule: The ESXi host must implement Secure Boot enforcement.

**Rule ID:** `SV-258740r933281_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Secure Boot is part of the UEFI firmware standard. With UEFI Secure Boot enabled, a host refuses to load any UEFI driver or app unless the operating system bootloader has a valid digital signature. Secure Boot for ESXi requires support from the firmware and it requires that all ESXi kernel modules, drivers, and VIBs be signed by VMware or a partner subordinate. Secure Boot is enabled in the BIOS of the ESXi physical server and supported by the hypervisor boot loader. This control flips ESXi from merely supporting Secure Boot to requiring it. Without this setting enabled, and configuration encryption, an ESXi host could be subject to offline attacks. An attacker could simply transfer the ESXi install drive to a non-Secure Boot host and boot it up without ESXi complaining. Satisfies: SRG-OS-000257-VMM-000910, SRG-OS-000258-VMM-000920, SRG-OS-000445-VMM-001780, SRG-OS-000446-VMM-001790</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ESXi host does not have a compatible TPM, this finding is downgraded to a CAT III. From an ESXi shell, run the following command: # esxcli system settings encryption get or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.settings.encryption.get.invoke() | Select RequireSecureBoot Expected result: Require Secure Boot: true If "Require Secure Boot" is not enable, this is a finding.

## Group: SRG-OS-000278-VMM-001000

**Group ID:** `V-258741`

### Rule: The ESXi host must enable Secure Boot.

**Rule ID:** `SV-258741r933284_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Secure Boot is part of the Unified Extensible Firmware Interface (UEFI) firmware standard. With UEFI Secure Boot enabled, a host refuses to load any UEFI driver or app unless the operating system bootloader has a valid digital signature. Secure Boot for ESXi requires support from the firmware and requires that all ESXi kernel modules, drivers, and vSphere Installation Bundles (VIBs) be signed by VMware or a partner subordinate. Secure Boot is enabled in the BIOS of the ESXi physical server and supported by the hypervisor boot loader. There is no ESXi control to "turn on" Secure Boot. Requiring Secure Boot (failing to boot without it present) is accomplished in another control.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # /usr/lib/vmware/secureboot/bin/secureBoot.py -s If Secure Boot is not "Enabled", this is a finding.

## Group: SRG-OS-000329-VMM-001180

**Group ID:** `V-258742`

### Rule: The ESXi host must enforce an unlock timeout of 15 minutes after a user account is locked out.

**Rule ID:** `SV-258742r933287_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By enforcing a reasonable unlock timeout after multiple failed logon attempts, the risk of unauthorized access via user password guessing, otherwise known as brute forcing, is reduced. Users must wait for the timeout period to elapse before subsequent logon attempts are allowed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Security.AccountUnlockTime" value and verify it is set to less than "900" and not "0". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Security.AccountUnlockTime If the "Security.AccountUnlockTime" setting is less than 900 or 0, this is a finding.

## Group: SRG-OS-000341-VMM-001220

**Group ID:** `V-258743`

### Rule: The ESXi host must allocate audit record storage capacity to store at least one week's worth of audit records.

**Rule ID:** `SV-258743r933290_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure ESXi has sufficient storage capacity in which to write the audit logs, audit record storage capacity should be configured. If a central audit record storage facility is available, the local storage capacity should be sufficient to hold audit records that would accumulate during anticipated interruptions in delivery of records to the facility.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Syslog.global.auditRecord.storageCapacity" value and verify it is set to "100". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Syslog.global.auditRecord.storageCapacity If the "Syslog.global.auditRecord.storageCapacity" setting is not set to 100, this is a finding.

## Group: SRG-OS-000342-VMM-001230

**Group ID:** `V-258744`

### Rule: The ESXi host must off-load logs via syslog.

**Rule ID:** `SV-258744r933293_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote logging to a central log host provides a secure, centralized store for ESXi logs. By gathering host log files onto a central host, it can more easily monitor all hosts with a single tool. It can also do aggregate analysis and searching to look for such things as coordinated attacks on multiple hosts. Logging to a secure, centralized log server also helps prevent log tampering and provides a long-term audit record. Satisfies: SRG-OS-000342-VMM-001230, SRG-OS-000274-VMM-000960, SRG-OS-000275-VMM-000970, SRG-OS-000277-VMM-000990, SRG-OS-000479-VMM-001990</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Syslog.global.logHost" value and verify it is set to a site-specific syslog server. Syslog servers are specified in the following formats: udp://<IP or FQDN>:514 tcp://<IP or FQDN>:514 ssl://<IP or FQDN>:1514 Multiple servers can also be specified when separated by commas. or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Syslog.global.logHost If the "Syslog.global.logHost" setting is not set to a valid, site-specific syslog server, this is a finding.

## Group: SRG-OS-000355-VMM-001330

**Group ID:** `V-258745`

### Rule: The ESXi host must synchronize internal information system clocks to an authoritative time source.

**Rule ID:** `SV-258745r933296_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure the accuracy of the system clock, it must be synchronized with an authoritative time source within DOD. Many system functions, including time-based logon and activity restrictions, automated reports, system logs, and audit records, depend on an accurate system clock. If there is no confidence in the correctness of the system clock, time-based functions may not operate as intended and records may be of diminished value. Satisfies: SRG-OS-000355-VMM-001330, SRG-OS-000356-VMM-001340</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Time Configuration. Verify NTP or PTP are configured, and one or more authoritative time sources are listed. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Services. Verify the NTP or PTP service is running and configured to start and stop with the host. or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: Get-VMHost | Get-VMHostNTPServer Get-VMHost | Get-VMHostService | Where {$_.Label -eq "NTP Daemon" -or $_.Label -eq "PTP Daemon"} If the NTP service is not configured with authoritative DOD time sources or the service is not configured to start and stop with the host ("Policy" of "on" in PowerCLI) or is stopped, this is a finding. If PTP is used instead of NTP, this is not a finding.

## Group: SRG-OS-000366-VMM-001430

**Group ID:** `V-258746`

### Rule: The ESXi Image Profile and vSphere Installation Bundle (VIB) acceptance level must be verified.

**Rule ID:** `SV-258746r933299_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Verify the ESXi Image Profile to only allow signed VIBs. An unsigned VIB represents untested code installed on an ESXi host. The ESXi Image profile supports four acceptance levels: 1. VMwareCertified - VIBs created, tested, and signed by VMware. 2. VMwareAccepted - VIBs created by a VMware partner but tested and signed by VMware. 3. PartnerSupported - VIBs created, tested, and signed by a certified VMware partner. 4. CommunitySupported - VIBs that have not been tested by VMware or a VMware partner. Community Supported VIBs are not supported and do not have a digital signature. To protect the security and integrity of ESXi hosts, do not allow unsigned (CommunitySupported) VIBs to be installed on hosts. Satisfies: SRG-OS-000366-VMM-001430, SRG-OS-000370-VMM-001460</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Security Profile. Under "Host Image Profile Acceptance Level" view the acceptance level. or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.software.acceptance.get.Invoke() If the acceptance level is "CommunitySupported", this is a finding.

## Group: SRG-OS-000379-VMM-001550

**Group ID:** `V-258747`

### Rule: The ESXi host must enable bidirectional Challenge-Handshake Authentication Protocol (CHAP) authentication for Internet Small Computer Systems Interface (iSCSI) traffic.

**Rule ID:** `SV-258747r933302_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When enabled, vSphere performs bidirectional authentication of both the iSCSI target and host. When not authenticating both the iSCSI target and host, there is potential for a man-in-the-middle attack, in which an attacker might impersonate either side of the connection to steal data. Bidirectional authentication mitigates this risk.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If iSCSI is not used, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> Storage >> Storage Adapters. Select the iSCSI adapter >> Properties >> Authentication >> Method. View the CHAP configuration and verify CHAP is required for target and host authentication. or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-VMHostHba | Where {$_.Type -eq "iscsi"} | Select AuthenticationProperties -ExpandProperty AuthenticationProperties If iSCSI is used and CHAP is not set to "required" for both the target and host, this is a finding. If iSCSI is used and unique CHAP secrets are not used for each host, this is a finding.

## Group: SRG-OS-000423-VMM-001700

**Group ID:** `V-258748`

### Rule: The ESXi host must protect the confidentiality and integrity of transmitted information by isolating vMotion traffic.

**Rule ID:** `SV-258748r933305_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>While encrypted vMotion is available, vMotion traffic should still be sequestered from other traffic to further protect it from attack. This network must only be accessible to other ESXi hosts, preventing outside access to the network. The vMotion VMkernel port group must be in a dedicated VLAN that can be on a standard or distributed virtual switch as long as the vMotion VLAN is not shared by any other function and is only routed to ESXi hosts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For environments that do not use vCenter server to manage ESXi, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> Networking >> VMkernel adapters. Review the VLAN associated with any vMotion VMkernel(s) and verify they are dedicated for that purpose and are logically separated from other functions. If long distance or cross vCenter vMotion is used, the vMotion network can be routable but must be accessible to only the intended ESXi hosts. If the vMotion port group is not on an isolated VLAN and/or is routable to systems other than ESXi hosts, this is a finding.

## Group: SRG-OS-000425-VMM-001710

**Group ID:** `V-258749`

### Rule: The ESXi host must maintain the confidentiality and integrity of information during transmission by exclusively enabling Transport Layer Security (TLS) 1.2.

**Rule ID:** `SV-258749r933308_rule`
**Severity:** high

**Description:**
<VulnDiscussion>TLS 1.0 and 1.1 are deprecated protocols with well-published shortcomings and vulnerabilities. TLS 1.2 should be enabled on all interfaces and SSLv3, TL 1.1, and 1.0 disabled, where supported. Mandating TLS 1.2 may break third-party integrations and add-ons to vSphere. Test these integrations carefully after implementing TLS 1.2 and roll back where appropriate. On interfaces where required functionality is broken with TLS 1.2, this finding is not applicable until such time as the third-party software supports TLS 1.2. Modify TLS settings in the following order: 1. vCenter. 2. ESXi. Satisfies: SRG-OS-000425-VMM-001710, SRG-OS-000426-VMM-001720</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "UserVars.ESXiVPsDisabledProtocols" value and verify it is set to "sslv3,tlsv1,tlsv1.1". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name UserVars.ESXiVPsDisabledProtocols If the "UserVars.ESXiVPsDisabledProtocols" setting is set to a value other than "sslv3,tlsv1,tlsv1.1", this is a finding.

## Group: SRG-OS-000478-VMM-001980

**Group ID:** `V-258750`

### Rule: The ESXi host Secure Shell (SSH) daemon must be configured to only use FIPS 140-2 validated ciphers.

**Rule ID:** `SV-258750r933311_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. ESXi must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # esxcli system ssh server config list -k ciphers or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.ssh.server.config.list.invoke() | Where-Object {$_.Key -eq 'ciphers'} Expected result: ciphers aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr If the output matches the ciphers in the expected result or a subset thereof, this is not a finding. If the ciphers in the output contain any ciphers not listed in the expected result, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258751`

### Rule: The ESXi host DCUI.Access list must be verified.

**Rule ID:** `SV-258751r933314_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Lockdown mode disables direct host access, requiring that administrators manage hosts from vCenter Server. However, if a host becomes isolated from vCenter, the administrator is locked out and can no longer manage the host. The "DCUI.Access" advanced setting allows specified users to exit lockdown mode in such a scenario. If the Direct Console User Interface (DCUI) is running in strict lockdown mode, this setting is ineffective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For environments that do not use vCenter server to manage ESXi, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "DCUI.Access" value and verify only the root user is listed. or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name DCUI.Access and verify it is set to root. If the "DCUI.Access" is not restricted to "root", this is a finding. Note: This list is only for local user accounts and should only contain the root user.

## Group: SRG-OS-000023-VMM-000060

**Group ID:** `V-258752`

### Rule: The ESXi host must display the Standard Mandatory DOD Notice and Consent Banner before granting access to the system via Secure Shell (SSH).

**Rule ID:** `SV-258752r933317_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the host ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for a host that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) VMM (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for VMMs that have severe limitations on the number of characters that can be displayed in the banner: "I've read (literal ampersand) consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Config.Etc.issue" value and verify it contains the standard mandatory DOD notice and consent banner. or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Config.Etc.issue If the "Config.Etc.issue" setting does not contain the standard mandatory DOD notice and consent banner, this is a finding.

## Group: SRG-OS-000023-VMM-000060

**Group ID:** `V-258753`

### Rule: The ESXi host Secure Shell (SSH) daemon must display the Standard Mandatory DOD Notice and Consent Banner before granting access to the system.

**Rule ID:** `SV-258753r933320_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the host ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for a host that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) VMM (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for VMMs that have severe limitations on the number of characters that can be displayed in the banner: "I've read (literal ampersand) consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # esxcli system ssh server config list -k banner or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.ssh.server.config.list.invoke() | Where-Object {$_.Key -eq 'banner'} Example result: banner /etc/issue If "banner" is not configured to "/etc/issue", this is a finding.

## Group: SRG-OS-000095-VMM-000480

**Group ID:** `V-258754`

### Rule: The ESXi host must be configured to disable nonessential capabilities by disabling Secure Shell (SSH).

**Rule ID:** `SV-258754r933323_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ESXi Shell is an interactive command line interface (CLI) available at the ESXi server console. The ESXi shell provides temporary access to commands essential for server maintenance. Intended primarily for use in break-fix scenarios, the ESXi shell is well suited for checking and modifying configuration details, which are not always generally accessible, using the vSphere Client. The ESXi shell is accessible remotely using SSH by users with the Administrator role. Under normal operating conditions, SSH access to the host must be disabled as is the default. As with the ESXi shell, SSH is also intended only for temporary use during break-fix scenarios. SSH must therefore be disabled under normal operating conditions and must only be enabled for diagnostics or troubleshooting. Remote access to the host must therefore be limited to the vSphere Client or Host Client at all other times. Satisfies: SRG-OS-000095-VMM-000480, SRG-OS-000297-VMM-001040, SRG-OS-000298-VMM-001050</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Services. Under Services, locate the "SSH" service and verify it is "Stopped". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-VMHostService | Where {$_.Label -eq "SSH"} If the SSH service is "Running", this is a finding.

## Group: SRG-OS-000095-VMM-000480

**Group ID:** `V-258755`

### Rule: The ESXi host must be configured to disable nonessential capabilities by disabling the ESXi shell.

**Rule ID:** `SV-258755r933326_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ESXi Shell is an interactive command line environment available locally from the Direct Console User Interface (DCUI) or remotely via SSH. Activities performed from the ESXi Shell bypass vCenter role-based access control (RBAC) and audit controls. The ESXi shell must only be turned on when needed to troubleshoot/resolve problems that cannot be fixed through the vSphere client.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Services. Under Services, locate the "ESXi Shell" service and verify it is "Stopped". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-VMHostService | Where {$_.Label -eq "ESXi Shell"} If the ESXi Shell service is "Running", this is a finding.

## Group: SRG-OS-000163-VMM-000700

**Group ID:** `V-258756`

### Rule: The ESXi host must automatically stop shell services after 10 minutes.

**Rule ID:** `SV-258756r933329_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When the ESXi Shell or Secure Shell (SSH) services are enabled on a host, they will run indefinitely. To avoid having these services left running, set the "ESXiShellTimeOut". The "ESXiShellTimeOut" defines a window of time after which the ESXi Shell and SSH services will be stopped automatically.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "UserVars.ESXiShellTimeOut" value and verify it is set to less than "600" and not "0". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name UserVars.ESXiShellTimeOut If the "UserVars.ESXiShellTimeOut" setting is set to a value greater than "600" or "0", this is a finding.

## Group: SRG-OS-000163-VMM-000700

**Group ID:** `V-258757`

### Rule: The ESXi host must set a timeout to automatically end idle DCUI sessions after 10 minutes.

**Rule ID:** `SV-258757r933332_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When the Direct Console User Interface (DCUI) is enabled and logged in, it should be automatically logged out if left logged on to avoid access by unauthorized persons. The "DcuiTimeOut" setting defines a window of time after which the DCUI will be logged out.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "UserVars.DcuiTimeOut" value and verify it is set to less than "600" and not "0". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name UserVars.DcuiTimeOut If the "UserVars.DcuiTimeOut" setting is set to a value greater than "600" or "0", this is a finding.

## Group: SRG-OS-000423-VMM-001700

**Group ID:** `V-258758`

### Rule: The ESXi host must protect the confidentiality and integrity of transmitted information by isolating ESXi management traffic.

**Rule ID:** `SV-258758r933335_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The vSphere management network provides access to the vSphere management interface on each component. Services running on the management interface provide an opportunity for an attacker to gain privileged access to the systems. Any remote attack most likely would begin with gaining entry to this network. The Management VMkernel port group can be on a standard or distributed virtual switch but must be on a dedicated VLAN. The Management VLAN must not be shared by any other function and must not be accessible to anything other than management-related functions such as vCenter.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> Networking >> VMkernel adapters. Review each VMkernel adapter that is used for management traffic and view the "Enabled services". Review the VLAN associated with each VMkernel that is used for management traffic. Verify with the system administrator that they are dedicated for that purpose and are logically separated from other functions. If any services other than "Management" are enabled on the Management VMkernel adapter, this is a finding. If the network segment is accessible, except to networks where other management-related entities are located such as vCenter, this is a finding. If there are any other systems or devices such as VMs on the ESXi management segment, this is a finding.

## Group: SRG-OS-000423-VMM-001700

**Group ID:** `V-258759`

### Rule: The ESXi host must protect the confidentiality and integrity of transmitted information by isolating IP-based storage traffic.

**Rule ID:** `SV-258759r933338_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Virtual machines (VMs) might share virtual switches and VLANs with the IP-based storage configurations. IP-based storage includes vSAN, iSCSI, and NFS. This configuration might expose IP-based storage traffic to unauthorized VM users. IP-based storage frequently is not encrypted. It can be viewed by anyone with access to this network. To restrict unauthorized users from viewing the IP-based storage traffic, the IP-based storage network must be logically separated from any other traffic. Configuring the IP-based storage adaptors on separate VLANs or network segments from other VMkernels and VMs will limit unauthorized users from viewing the traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If IP-based storage is not used, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> Networking >> VMkernel adapters. Review each VMkernel adapter that is used for IP-based storage traffic and view the "Enabled services". Review the VLAN associated with each VMkernel that is used for IP-based storage traffic. Verify with the system administrator that they are dedicated for that purpose and are logically separated from other functions. If any services are enabled on an NFS or iSCSI IP-based storage VMkernel adapter, this is a finding. If any services are enabled on a vSAN VMkernel adapter other than vSAN, this is a finding. If any IP-based storage networks are not isolated from other traffic types, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258760`

### Rule: The ESXi host lockdown mode exception users list must be verified.

**Rule ID:** `SV-258760r933341_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>While a host is in lockdown mode (strict or normal), only users on the "Exception Users" list are allowed access. These users do not lose their permissions when the host enters lockdown mode. The organization may want to add service accounts such as a backup agent to the Exception Users list. Verify the list of users exempted from losing permissions is legitimate and as needed per the environment. Adding unnecessary users to the exception list defeats the purpose of lockdown mode.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For environments that do not use vCenter server to manage ESXi, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Security Profile. Under "Lockdown Mode", review the Exception Users list. or From a PowerCLI command prompt while connected to the ESXi host, run the following script: $vmhost = Get-VMHost | Get-View $lockdown = Get-View $vmhost.ConfigManager.HostAccessManager $lockdown.QueryLockdownExceptions() If the Exception Users list contains accounts that do not require special permissions, this is a finding. Note: The Exception Users list is empty by default and should remain that way except under site-specific circumstances.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258761`

### Rule: The ESXi host Secure Shell (SSH) daemon must not allow host-based authentication.

**Rule ID:** `SV-258761r933344_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH trust relationships mean a compromise on one host can allow an attacker to move trivially to other hosts. SSH's cryptographic host-based authentication is more secure than ".rhosts" authentication since hosts are cryptographically authenticated. However, it is not recommended that hosts unilaterally trust one another, even within an organization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # esxcli system ssh server config list -k hostbasedauthentication or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.ssh.server.config.list.invoke() | Where-Object {$_.Key -eq 'hostbasedauthentication'} Example result: hostbasedauthentication no If "hostbasedauthentication" is not configured to "no", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258762`

### Rule: The ESXi host Secure Shell (SSH) daemon must not permit user environment settings.

**Rule ID:** `SV-258762r933347_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH environment options potentially allow users to bypass access restriction in some configurations. Users must not be able to present environment options to the SSH daemon.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # esxcli system ssh server config list -k permituserenvironment or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.ssh.server.config.list.invoke() | Where-Object {$_.Key -eq 'permituserenvironment'} Example result: permituserenvironment no If "permituserenvironment" is not configured to "no", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258763`

### Rule: The ESXi host Secure Shell (SSH) daemon must be configured to not allow gateway ports.

**Rule ID:** `SV-258763r933350_rule`
**Severity:** low

**Description:**
<VulnDiscussion>SSH Transmission Control Protocol (TCP) connection forwarding provides a mechanism to establish TCP connections proxied by the SSH server. This function can provide convenience similar to a virtual private network (VPN) with the similar risk of providing a path to circumvent firewalls and network Access Control Lists (ACLs). Gateway ports allow remote forwarded ports to bind to nonloopback addresses on the server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # esxcli system ssh server config list -k gatewayports or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.ssh.server.config.list.invoke() | Where-Object {$_.Key -eq 'gatewayports'} Example result: gatewayports no If "gatewayports" is not configured to "no", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258764`

### Rule: The ESXi host Secure Shell (SSH) daemon must not permit tunnels.

**Rule ID:** `SV-258764r933353_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OpenSSH has the ability to create network tunnels (layer 2 and layer 3) over an SSH connection. This function can provide similar convenience to a virtual private network (VPN) with the similar risk of providing a path to circumvent firewalls and network Access Control Lists (ACLs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # esxcli system ssh server config list -k permittunnel or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.ssh.server.config.list.invoke() | Where-Object {$_.Key -eq 'permittunnel'} Example result: permittunnel no If "permittunnel" is not configured to "no", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258765`

### Rule: The ESXi host Secure Shell (SSH) daemon must set a timeout count on idle sessions.

**Rule ID:** `SV-258765r933356_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Setting a timeout ensures that a user login will be terminated as soon as the "ClientAliveCountMax" is reached.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # esxcli system ssh server config list -k clientalivecountmax or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.ssh.server.config.list.invoke() | Where-Object {$_.Key -eq 'clientalivecountmax'} Example result: clientalivecountmax 3 If "clientalivecountmax" is not configured to "3", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258766`

### Rule: The ESXi host Secure Shell (SSH) daemon must set a timeout interval on idle sessions.

**Rule ID:** `SV-258766r933359_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Automatically logging out idle users guards against compromises via hijacked administrative sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # esxcli system ssh server config list -k clientaliveinterval or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.ssh.server.config.list.invoke() | Where-Object {$_.Key -eq 'clientaliveinterval'} Example result: clientaliveinterval 200 If "clientaliveinterval" is not configured to "200", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258767`

### Rule: The ESXi host must disable Simple Network Management Protocol (SNMP) v1 and v2c.

**Rule ID:** `SV-258767r933362_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SNMP is not being used, it must remain disabled. If it is being used, the proper trap destination must be configured. If SNMP is not properly configured, monitoring information can be sent to a malicious host that can use this information to plan an attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # esxcli system snmp get or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHostSnmp | Select * If SNMP is not in use and is enabled, this is a finding. If SNMP is enabled and is not using v3 targets with authentication, this is a finding. Note: SNMP v3 targets can only be viewed and configured via the "esxcli" command.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258768`

### Rule: The ESXi host must disable Inter-Virtual Machine (VM) Transparent Page Sharing.

**Rule ID:** `SV-258768r933365_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Published academic papers have demonstrated that by forcing a flush and reload of cache memory, it is possible to measure memory timings to try to determine an Advanced Encryption Standard (AES) encryption key in use on another virtual machine running on the same physical processor of the host server if Transparent Page Sharing (TPS) is enabled between the two VMs. This technique works only in a highly controlled system configured in a nonstandard way that VMware believes would not be recreated in a production environment. Although VMware believes information being disclosed in real-world conditions is unrealistic, out of an abundance of caution, upcoming ESXi update releases will no longer enable TPS between VMs by default (TPS will still be used within individual VMs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Mem.ShareForceSalting" value and verify it is set to "2". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Mem.ShareForceSalting If the "Mem.ShareForceSalting" setting is not set to 2, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258769`

### Rule: The ESXi host must configure the firewall to block network traffic by default.

**Rule ID:** `SV-258769r933368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In addition to service-specific firewall rules, ESXi has a default firewall rule policy to allow or deny incoming and outgoing traffic. Reduce the risk of attack by ensuring this is set to deny incoming and outgoing traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # esxcli network firewall get If the "Default Action" does not equal "DROP", this is a finding. If "Enabled" does not equal "true", this is a finding. or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHostFirewallDefaultPolicy If the Incoming or Outgoing policies are "True", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258770`

### Rule: The ESXi host must enable Bridge Protocol Data Units (BPDU) filter on the host to prevent being locked out of physical switch ports with Portfast and BPDU Guard enabled.

**Rule ID:** `SV-258770r933371_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>BPDU Guard and Portfast are commonly enabled on the physical switch to which the ESXi host is directly connected to reduce the Spanning Tree Protocol (STP) convergence delay. If a BPDU packet is sent from a virtual machine (VM) on the ESXi host to the physical switch configured as stated above, a cascading lockout of all the uplink interfaces from the ESXi host can occur. To prevent this type of lockout, BPDU Filter can be enabled on the ESXi host to drop any BPDU packets being sent to the physical switch. The caveat is that certain Secure Socket Layer (SSL) virtual private networks that use Windows bridging capability can legitimately generate BPDU packets. The administrator should verify no legitimate BPDU packets are generated by VMs on the ESXi host prior to enabling BPDU Filter. If BPDU Filter is enabled in this situation, enabling Reject Forged Transmits on the virtual switch port group adds protection against Spanning Tree loops.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Net.BlockGuestBPDU" value and verify it is set to "1". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Net.BlockGuestBPDU If the "Net.BlockGuestBPDU" setting is not set to "1", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258771`

### Rule: The ESXi host must configure virtual switch security policies to reject forged transmits.

**Rule ID:** `SV-258771r933374_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the virtual machine (VM) operating system changes the Media Access Control (MAC) address, the operating system can send frames with an impersonated source MAC address at any time. This allows an operating system to stage malicious attacks on the devices in a network by impersonating a network adaptor authorized by the receiving network. This means the virtual switch does not compare the source and effective MAC addresses. To protect against MAC address impersonation, all virtual switches must have forged transmissions set to reject. Reject Forged Transmit can be set at the vSwitch and/or the Portgroup level. Switch-level settings can be overridden at the Portgroup level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This control addresses ESXi standard switches. Distributed switches are addressed in the vCenter STIG. If there is no standard switch on the ESXi host, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> Networking >> Virtual Switches. On each standard switch, click the '...' button next to each port group and select "Edit Settings". Click the "Security" tab. Verify that "Forged transmits" is set to "Reject" and that "Override" is not checked. or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: Get-VirtualSwitch | Get-SecurityPolicy Get-VirtualPortGroup | Get-SecurityPolicy | Select-Object * If the "Forged Transmits" policy is set to "Accept" (or "true", via PowerCLI) or the security policy inherited from the virtual switch is overridden, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258772`

### Rule: The ESXi host must configure virtual switch security policies to reject Media Access Control (MAC) address changes.

**Rule ID:** `SV-258772r933377_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If the virtual machine (VM) operating system changes the MAC address, it can send frames with an impersonated source MAC address at any time. This allows it to stage malicious attacks on the devices in a network by impersonating a network adaptor authorized by the receiving network. This will prevent VMs from changing their effective MAC address, which will affect applications that require this functionality. This will also affect how a layer 2 bridge will operate and will affect applications that require a specific MAC address for licensing. "Reject MAC Changes" can be set at the vSwitch and/or the Portgroup level. Switch-level settings can be overridden at the Portgroup level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This control addresses ESXi standard switches. Distributed switches are addressed in the vCenter STIG. If there is no standard switch on the ESXi host, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> Networking >> Virtual Switches. On each standard switch, click the '...' button next to each port group and select "Edit Settings". Click the "Security" tab. Verify that "MAC Address Changes" is set to "Reject" and that "Override" is not checked. or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: Get-VirtualSwitch | Get-SecurityPolicy Get-VirtualPortGroup | Get-SecurityPolicy | Select-Object * If the "MAC Address Changes" policy is set to "Accept" (or "true", via PowerCLI) or the security policy inherited from the virtual switch is overridden, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258773`

### Rule: The ESXi host must configure virtual switch security policies to reject promiscuous mode requests.

**Rule ID:** `SV-258773r933380_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When promiscuous mode is enabled for a virtual switch, all virtual machines (VMs) connected to the Portgroup have the potential to read all packets across that network (only the virtual machines connected to that Portgroup). Promiscuous mode is disabled by default on the ESXi Server, and this is the recommended setting. Promiscuous mode can be set at the vSwitch and/or the Portgroup level. Switch-level settings can be overridden at the Portgroup level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This control addresses ESXi standard switches. Distributed switches are addressed in the vCenter STIG. If there is no standard switch on the ESXi host, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> Networking >> Virtual Switches. On each standard switch, click the '...' button next to each port group and select "Edit Settings". Click the "Security" tab. Verify that "Promiscuous Mode" is set to "Reject" and that "Override" is not checked. or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: Get-VirtualSwitch | Get-SecurityPolicy Get-VirtualPortGroup | Get-SecurityPolicy | Select-Object * If the "Promiscuous Mode" policy is set to "Accept" (or "true", via PowerCLI) or the security policy inherited from the virtual switch is overridden, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258774`

### Rule: The ESXi host must restrict use of the dvFilter network application programming interface (API).

**Rule ID:** `SV-258774r933383_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the organization is not using products that use the dvFilter network API, the host should not be configured to send network information to a virtual machine (VM). If the API is enabled, an attacker might attempt to connect a virtual machine to it, potentially providing access to the network of other VMs on the host. If using a product that makes use of this API, verify the host has been configured correctly. If not using such a product, ensure the setting is blank.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Net.DVFilterBindIpAddress" value and verify the value is blank or the correct IP address of a security appliance if in use. or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Net.DVFilterBindIpAddress If the "Net.DVFilterBindIpAddress" setting is not blank and security appliances are not in use on the host, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258775`

### Rule: The ESXi host must restrict the use of Virtual Guest Tagging (VGT) on standard switches.

**Rule ID:** `SV-258775r933386_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a port group is set to VLAN 4095, the vSwitch passes all network frames to the attached virtual machines (VMs) without modifying the VLAN tags. In vSphere, this is referred to as VGT. The VM must process the VLAN information itself via an 802.1Q driver in the operating system. VLAN 4095 must only be implemented if the attached VMs have been specifically authorized and are capable of managing VLAN tags themselves. If VLAN 4095 is enabled inappropriately, it may cause denial of service or allow a VM to interact with traffic on an unauthorized VLAN.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This control addresses ESXi standard switches. Distributed switches are addressed in the vCenter STIG. If there is no standard switch on the ESXi host, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> Networking >> Virtual Switches. For each standard switch, review the "VLAN ID" on each port group and verify it is not set to "4095". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VirtualPortGroup | Select Name, VLanID If any port group is configured with VLAN 4095 and is not documented as a needed exception, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258776`

### Rule: The ESXi host must have all security patches and updates installed.

**Rule ID:** `SV-258776r933389_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Installing software updates is a fundamental mitigation against the exploitation of publicly known vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine the current version and build: From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Summary. Note the version string next to "Hypervisor:". or From a Secure Shell (SSH) session connected to the ESXi host, or from the ESXi shell, run the following command: # vmware -v If the ESXi host does not have the latest patches, this is a finding. If the ESXi host is not on a supported release, this is a finding. The latest ESXi versions and their build numbers can be found here: https://kb.vmware.com/s/article/2143832 VMware also publishes advisories on security patches and offers a way to subscribe to email alerts for them. Go to: https://www.vmware.com/support/policies/security_response

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258777`

### Rule: The ESXi host must not suppress warnings that the local or remote shell sessions are enabled.

**Rule ID:** `SV-258777r933392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Warnings that local or remote shell sessions are enabled alert administrators to activity they may not be aware of and need to investigate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "UserVars.SuppressShellWarning" value and verify it is set to "0". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name UserVars.SuppressShellWarning If the "UserVars.SuppressShellWarning" setting is not set to "0", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258778`

### Rule: The ESXi host must not suppress warnings about unmitigated hyperthreading vulnerabilities.

**Rule ID:** `SV-258778r933395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The L1 Terminal Fault (L1TF) CPU vulnerabilities published in 2018 have patches and mitigations available in vSphere. However, there are performance impacts to these mitigations that require careful thought and planning from the system administrator before implementation. Until a mitigation is implemented, the UI warning about the lack of a mitigation must not be dismissed so the system administrator does not assume the vulnerability has been addressed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "UserVars.SuppressHyperthreadWarning" value and verify it is set to "0". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name UserVars.SuppressHyperthreadWarning If the "UserVars.SuppressHyperthreadWarning" setting is not set to "0", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258779`

### Rule: The ESXi host must verify certificates for SSL syslog endpoints.

**Rule ID:** `SV-258779r933398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When sending syslog data to a remote host, ESXi can be configured to use any combination of TCP, UDP, and SSL transports. When using SSL, the server certificate must be validated to ensure that the host is connecting to a valid syslog server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If SSL is not used for a syslog target, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Syslog.global.logCheckSSLCerts" value and verify it is set to "true". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Syslog.global.logCheckSSLCerts If the "Syslog.global.logCheckSSLCerts" setting is not set to "true", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258780`

### Rule: The ESXi host must enable volatile key destruction.

**Rule ID:** `SV-258780r933401_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, pages allocated for virtual machines (VMs), userspace applications, and kernel threads are zeroed out at allocation time. ESXi will always ensure that no nonzero pages are exposed to VMs or userspace applications. While this prevents exposing cryptographic keys from VMs or userworlds to other clients, these keys can stay present in host memory for a long time if the memory is not reused. The NIAP Virtualization Protection Profile and Server Virtualization Extended Package require that memory that may contain cryptographic keys be zeroed upon process exit. To this end, a new configuration option, MemEagerZero, can be configured to enforce zeroing out userworld and guest memory pages when a userworld process or guest exits. For kernel threads, memory spaces holding keys are zeroed out as soon as the secret is no longer needed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Mem.MemEagerZero" value and verify it is set to "1". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Mem.MemEagerZero If the "Mem.MemEagerZero" setting is not set to "1", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258781`

### Rule: The ESXi host must configure a session timeout for the vSphere API.

**Rule ID:** `SV-258781r933404_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The vSphere API (VIM) allows for remote, programmatic administration of the ESXi host. Authenticated API sessions are no different from a risk perspective than authenticated UI sessions and they need similar protections. One of these protections is a basic inactivity timeout, after which the session will be invalidated and reauthentication will be required by the application accessing the API. This is set to 30 seconds by default but can be disabled, thus leaving API sessions open indefinitely. The 30 second default must be verified and maintained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Config.HostAgent.vmacore.soap.sessionTimeout" value and verify it is set to "30". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Config.HostAgent.vmacore.soap.sessionTimeout If the "Config.HostAgent.vmacore.soap.sessionTimeout" setting is not set to "30", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258782`

### Rule: The ESXi host must be configured with an appropriate maximum password age.

**Rule ID:** `SV-258782r933407_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The older an ESXi local account password is, the larger the opportunity window is for attackers to guess, crack or reuse a previously cracked password. Rotating passwords on a regular basis is a fundamental security practice and one that ESXi supports.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Security.PasswordMaxDays" value and verify it is set to "90". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Security.PasswordMaxDays If the "Security.PasswordMaxDays" setting is not set to "90", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258783`

### Rule: The ESXi Common Information Model (CIM) service must be disabled.

**Rule ID:** `SV-258783r933410_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The CIM system provides an interface that enables hardware-level management from remote applications via a set of standard application programming interfaces (APIs). These APIs are consumed by external applications such as HP SIM or Dell OpenManage for agentless, remote hardware monitoring of the ESXi host. To reduce attack surface area and following the minimum functionality principal, the CIM service must be disabled unless explicitly needed and approved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Services. Under "Services", locate the "CIM Server" service and verify it is "Stopped" and the "Startup Policy" is set to "Start and stop manually". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-VMHostService | Where {$_.Label -eq "CIM Server"} If the "CIM Server" service does not have a "Policy" of "off" or is running, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258784`

### Rule: The ESXi host must use DOD-approved certificates.

**Rule ID:** `SV-258784r933413_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The default self-signed host certificate issued by the VMware Certificate Authority (VMCA) must be replaced with a DOD-approved certificate when the host will be accessed directly, such as during a virtual machine (VM) console connection. The use of a DOD certificate on the host assures clients the service they are connecting to is legitimate and properly secured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Certificate. If the issuer is not a DOD-approved certificate authority, this is a finding. If the host will never be accessed directly (virtual machine console connections bypass vCenter), this is not a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258785`

### Rule: The ESXi host Secure Shell (SSH) daemon must disable port forwarding.

**Rule ID:** `SV-258785r933416_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>While enabling Transmission Control Protocol (TCP) tunnels is a valuable function of sshd, this feature is not appropriate for use on the ESXi hypervisor.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # esxcli system ssh server config list -k allowtcpforwarding or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.ssh.server.config.list.invoke() | Where-Object {$_.Key -eq 'allowtcpforwarding'} Example result: allowtcpforwarding no If "allowtcpforwarding" is not configured to "no", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258786`

### Rule: The ESXi host OpenSLP service must be disabled.

**Rule ID:** `SV-258786r933419_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OpenSLP implements the Service Location Protocol to help CIM clients discover CIM servers over TCP 427. This service is not widely needed and has had vulnerabilities exposed in the past. To reduce attack surface area and following the minimum functionality principal, the OpenSLP service must be disabled unless explicitly needed and approved. Note: Disabling the OpenSLP service may affect monitoring and third-party systems that use the WBEM DTMF protocols.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Services. Under "Services", locate the "slpd" service and verify it is "Stopped" and the "Startup Policy" is set to "Start and stop manually". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-VMHostService | Where {$_.Label -eq "slpd"} If the slpd service does not have a "Policy" of "off" or is running, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258787`

### Rule: The ESXi host must enable audit logging.

**Rule ID:** `SV-258787r933422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ESXi offers both local and remote audit recordkeeping to meet the requirements of the NIAP Virtualization Protection Profile and Server Virtualization Extended Package. Local records are stored on any accessible local or VMFS path. Remote records are sent to the global syslog servers configured elsewhere. To operate in the NIAP validated state, ESXi must enable and properly configure this audit system. This system is disabled by default. Note: Audit records can be viewed locally via the "/bin/viewAudit" utility over SSH or at the ESXi shell.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Syslog.global.auditRecord.storageEnable" value and verify it is set to "true". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Syslog.global.auditRecord.storageEnable If the "Syslog.global.auditRecord.storageEnable" setting is not set to "true", this is a finding.

## Group: SRG-OS-000342-VMM-001230

**Group ID:** `V-258788`

### Rule: The ESXi host must off-load audit records via syslog.

**Rule ID:** `SV-258788r933425_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ESXi offers both local and remote audit recordkeeping to meet the requirements of the NIAP Virtualization Protection Profile and Server Virtualization Extended Package. Local records are stored on any accessible local or VMFS path. Remote records are sent to the global syslog servers configured elsewhere. To operate in the NIAP-validated state, ESXi must enable and properly configure this audit system. This system is disabled by default. Note: Audit records can be viewed locally via the "/bin/viewAudit" utility over SSH or at the ESXi shell.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Syslog.global.auditRecord.remoteEnable" value and verify it is set to "true". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Syslog.global.auditRecord.remoteEnable If the "Syslog.global.auditRecord.remoteEnable" setting is not set to "true", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258789`

### Rule: The ESXi host must enable strict x509 verification for SSL syslog endpoints.

**Rule ID:** `SV-258789r933428_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When sending syslog data to a remote host via SSL, the ESXi host is presented with the endpoint's SSL server certificate. In addition to trust verification, configured elsewhere, this "x509-strict" option performs additional validity checks on CA root certificates during verification. These checks are generally not performed (CA roots are inherently trusted) and might cause incompatibilities with existing, misconfigured CA roots. The NIAP requirements in the Virtualization Protection Profile and Server Virtualization Extended Package, however, require even CA roots to pass validations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If SSL is not used for a syslog target, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Syslog.global.certificate.strictX509Compliance" value and verify it is set to "true". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Syslog.global.certificate.strictX509Compliance If the "Syslog.global.certificate.strictX509Compliance" setting is not set to "true", this is a finding.

## Group: SRG-OS-000037-VMM-000150

**Group ID:** `V-258790`

### Rule: The ESXi host must forward audit records containing information to establish what type of events occurred.

**Rule ID:** `SV-258790r933431_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what types of events occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process/VM identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in the ESXi audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured host.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Syslog.global.logLevel" value and verify it is set to "info". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Syslog.global.logLevel If the "Syslog.global.logLevel" setting is not set to "info", this is a finding. Note: Verbose logging level is acceptable for troubleshooting purposes.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258791`

### Rule: The ESXi host must not be configured to override virtual machine (VM) configurations.

**Rule ID:** `SV-258791r933434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Each VM on an ESXi host runs in its own "vmx" process. Upon creation, a vmx process will look in two locations for configuration items, the ESXi host itself and the per-vm *.vmx file in the VM storage path on the datastore. The settings on the ESXi host are read first and take precedence over settings in the *.vmx file. This can be a convenient way to set a setting in one place and have it apply to all VMs running on that host. The difficulty is in managing those settings and determining the effective state. Since managing per-VM vmx settings can be fully automated and customized while the ESXi setting cannot be easily queried, the ESXi configuration must not be used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # stat -c "%s" /etc/vmware/settings Expected result: 0 If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258792`

### Rule: The ESXi host must not be configured to override virtual machine (VM) logger settings.

**Rule ID:** `SV-258792r933437_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Each VM on an ESXi host runs in its own "vmx" process. Upon creation, a vmx process will look in two locations for configuration items, the ESXi host itself and the per-vm *.vmx file in the VM storage path on the datastore. The settings on the ESXi host are read first and take precedence over settings in the *.vmx file. This can be a convenient way to set a setting in one place and have it apply to all VMs running on that host. The difficulty is in managing those settings and determining the effective state. Since managing per-VM vmx settings can be fully automated and customized while the ESXi setting cannot be easily queried, the ESXi configuration must not be used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # grep "^vmx\.log" /etc/vmware/config If the command produces any output, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258793`

### Rule: The ESXi host must require TPM-based configuration encryption.

**Rule ID:** `SV-258793r933440_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An ESXi host's configuration consists of configuration files for each service that runs on the host. The configuration files typically reside in the /etc/ directory, but they can also reside in other namespaces. The configuration files contain run-time information about the state of the services. Over time, the default values in the configuration files might change, for example, when settings on the ESXi host are changed. A cron job backs up the ESXi configuration files periodically, when ESXi shuts down gracefully or on demand, and creates an archived configuration file in the boot bank. When ESXi reboots, it reads the archived configuration file and recreates the state that ESXi was in when the backup was taken. Before vSphere 7.0 Update 2, the archived ESXi configuration file is not encrypted. In vSphere 7.0 Update 2 and later, the archived configuration file is encrypted. When the ESXi host is configured with a Trusted Platform Module (TPM), the TPM is used to "seal" the configuration to the host, providing a strong security guarantee and additional protection from offline attacks. Configuration encryption uses the physical TPM when it is available and supported at install or upgrade time. If the TPM was added or enabled later, the ESXi host must be told to reconfigure to use the newly available TPM. Once the TPM configuration encryption is enabled, it cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ESXi host does not have a compatible TPM, this finding is downgraded to a CAT III. From an ESXi shell, run the following command: # esxcli system settings encryption get or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.settings.encryption.get.invoke() | Select Mode Expected result: Mode: TPM If the "Mode" is not set to "TPM", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258794`

### Rule: The ESXi host must configure the firewall to restrict access to services running on the host.

**Rule ID:** `SV-258794r933443_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted access to services running on an ESXi host can expose a host to outside attacks and unauthorized access. Reduce the risk by configuring the ESXi firewall to only allow access from authorized networks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Firewall. Under the "Allowed IP addresses" column, review the allowed IPs for each service. Check this for "Incoming" and "Outgoing" sections. or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-VMHostFirewallException | Where {$_.Enabled -eq $true} | Select Name,Enabled,@{N="AllIPEnabled";E={$_.ExtensionData.AllowedHosts.AllIP}} If for an enabled service "Allow connections from any IP address" is selected, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258795`

### Rule: The ESXi host when using Host Profiles and/or Auto Deploy must use the vSphere Authentication Proxy to protect passwords when adding themselves to Active Directory.

**Rule ID:** `SV-258795r933446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a host is configured to join an Active Directory domain using Host Profiles and/or Auto Deploy, the Active Directory credentials are saved in the profile and are transmitted over the network. To avoid having to save Active Directory credentials in the Host Profile and to avoid transmitting Active Directory credentials over the network, use the vSphere Authentication Proxy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For environments that do not use vCenter server to manage ESXi, this is not applicable. If the organization is not using Host Profiles to join Active Directory, this is not applicable. From the vSphere Client, go to Home >> Policies and Profiles >> Host Profiles. Click a Host Profile >> Configure >> Security and Services >> Security Settings >> Authentication Configuration >> Active Directory Configuration >> Join Domain Method. If the method used to join hosts to a domain is not set to "Use vSphere Authentication Proxy to add the host to domain", this is a finding. or From a PowerCLI command prompt while connected to vCenter, run the following command: Get-VMHost | Select Name, ` @{N="HostProfile";E={$_ | Get-VMHostProfile}}, ` @{N="JoinADEnabled";E={($_ | Get-VmHostProfile).ExtensionData.Config.ApplyProfile.Authentication.ActiveDirectory.Enabled}}, ` @{N="JoinDomainMethod";E={(($_ | Get-VMHostProfile).ExtensionData.Config.ApplyProfile.Authentication.ActiveDirectory | Select -ExpandProperty Policy | Where {$_.Id -eq "JoinDomainMethodPolicy"}).Policyoption.Id}} If "JoinADEnabled" is "True" and "JoinDomainMethod" is not "FixedCAMConfigOption", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258796`

### Rule: The ESXi host must not use the default Active Directory ESX Admin group.

**Rule ID:** `SV-258796r933449_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When adding ESXi hosts to Active Directory, all user/group accounts assigned to the Active Directory group "ESX Admins" will have full administrative access to the host. If this group is not controlled or known to the system administrators, it may be used for inappropriate access to the host. Therefore, the default group must be changed to a site-specific Active Directory group and membership must be severely restricted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For systems that do not use Active Directory, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Config.HostAgent.plugins.hostsvc.esxAdminsGroup" value and verify it is not set to "ESX Admins". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Config.HostAgent.plugins.hostsvc.esxAdminsGroup If the "Config.HostAgent.plugins.hostsvc.esxAdminsGroup" setting is set to "ESX Admins", this is a finding.

## Group: SRG-OS-000341-VMM-001220

**Group ID:** `V-258797`

### Rule: The ESXi host must configure a persistent log location for all locally stored logs.

**Rule ID:** `SV-258797r933452_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ESXi can be configured to store log files on an in-memory file system. This occurs when the host's "/scratch" directory is linked to "/tmp/scratch". When this is done, only a single day's worth of logs are stored at any time. In addition, log files will be reinitialized upon each reboot. This presents a security risk as user activity logged on the host is only stored temporarily and will not persist across reboots. This can also complicate auditing and make it harder to monitor events and diagnose issues. ESXi host logging should always be configured to a persistent datastore. Note: Scratch space is configured automatically during installation or first boot of an ESXi host and does not usually need to be configured manually. If ESXi is installed on an SD card or USB device, a persistent log location may not be configured upon install as normal.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Syslog.global.logDir" value and verify it is set to a persistent location. If the value of the setting is "[] /scratch/logs", verify the advanced setting "ScratchConfig.CurrentScratchLocation" is not set to "/tmp/scratch". This is a nonpersistent location. If "Syslog.global.logDir" is not configured to a persistent location, this is a finding. or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.syslog.config.get.Invoke() | Select LocalLogOutput,LocalLogOutputIsPersistent If the "LocalLogOutputIsPersistent" value is not true, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258798`

### Rule: The ESXi host must enforce the exclusive running of executables from approved VIBs.

**Rule ID:** `SV-258798r933455_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "execInstalledOnly" advanced ESXi boot option, when set to TRUE, guarantees that the VMkernel executes only those binaries that have been packaged as part of a signed VIB. While this option is effective on its own, it can be further enhanced by telling the Secure Boot to check with the TPM to make sure that the boot process does not proceed unless this setting is enabled. This further protects against malicious offline changes to ESXi configuration to disable the "execInstalledOnly" option.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ESXi host does not have a compatible TPM, this finding is downgraded to a CAT III. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "VMkernel.Boot.execInstalledOnly" value and verify that it is "true". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name VMkernel.Boot.execInstalledOnly If the "VMkernel.Boot.execInstalledOnly" setting is not "true", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258799`

### Rule: The ESXi host must use sufficient entropy for cryptographic operations.

**Rule ID:** `SV-258799r933458_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Starting in vSphere 8.0, the ESXi Entropy implementation supports the FIPS 140-3 and EAL4 certifications. Kernel boot options control which entropy sources to activate on an ESXi host. In computing, the term "entropy" refers to random characters and data that are collected for use in cryptography, such as generating encryption keys to secure data transmitted over a network. Entropy is required by security for generating keys and communicating securely over the network. Entropy is often collected from a variety of sources on a system. FIPS entropy handling is the default behavior if the following conditions are true: -The hardware supports RDSEED. -The disableHwrng VMkernel boot option is not present or is FALSE. -The entropySources VMkernel boot option is not present or is 0 (zero).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following commands: # esxcli system settings kernel list -o disableHwrng # esxcli system settings kernel list -o entropySources or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.settings.kernel.list.invoke() | Where {$_.Name -eq "disableHwrng" -or $_.Name -eq "entropySources"} If "disableHwrng" is not set to "false", this is a finding. If "entropySources" is not set to "0", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258800`

### Rule: The ESXi host must not enable log filtering.

**Rule ID:** `SV-258800r933461_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The log filtering capability allows users to modify the logging policy of the syslog service that is running on an ESXi host. Users can create log filters to reduce the number of repetitive entries in the ESXi logs and to deny specific log events entirely. Setting a limit to the amount of logging information restricts the ability to detect and respond to potential security issues or system failures properly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # esxcli system syslog config logfilter get or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.syslog.config.logfilter.get.invoke() If "LogFilteringEnabled" is not set to "false", this is a finding.

