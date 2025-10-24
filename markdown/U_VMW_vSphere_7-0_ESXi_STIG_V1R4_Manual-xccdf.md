# STIG Benchmark: VMware vSphere 7.0 ESXi Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000027-VMM-000080

**Group ID:** `V-256375`

### Rule: Access to the ESXi host must be limited by enabling lockdown mode.

**Rule ID:** `SV-256375r958398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling lockdown mode disables direct access to an ESXi host, requiring the host to be managed remotely from vCenter Server. This is done to ensure the roles and access controls implemented in vCenter are always enforced and users cannot bypass them by logging on to a host directly. By forcing all interaction to occur through vCenter Server, the risk of someone inadvertently attaining elevated privileges or performing tasks that are not properly audited is greatly reduced. Satisfies: SRG-OS-000027-VMM-000080, SRG-OS-000123-VMM-000620</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For environments that do not use vCenter server to manage ESXi, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Security Profile. Scroll down to "Lockdown Mode" and verify it is set to "Enabled" (Normal or Strict). or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Select Name,@{N="Lockdown";E={$_.Extensiondata.Config.LockdownMode}} If "Lockdown Mode" is disabled, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256376`

### Rule: The ESXi host must verify the DCUI.Access list.

**Rule ID:** `SV-256376r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Lockdown mode disables direct host access, requiring that administrators manage hosts from vCenter Server. However, if a host becomes isolated from vCenter, the administrator is locked out and can no longer manage the host. The "DCUI.Access" advanced setting allows specified users to exit lockdown mode in such a scenario. If the Direct Console User Interface (DCUI) is running in strict lockdown mode, this setting is ineffective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For environments that do not use vCenter server to manage ESXi, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "DCUI.Access" value and verify only the root user is listed. or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name DCUI.Access and verify it is set to root. If the "DCUI.Access" is not restricted to "root", this is a finding. Note: This list is only for local user accounts and should only contain the root user.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256377`

### Rule: The ESXi host must verify the exception users list for lockdown mode.

**Rule ID:** `SV-256377r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>While a host is in lockdown mode (strict or normal), only users on the "Exception Users" list are allowed access. These users do not lose their permissions when the host enters lockdown mode. The organization may want to add service accounts such as a backup agent to the Exception Users list. Verify the list of users exempted from losing permissions is legitimate and as needed per the environment. Adding unnecessary users to the exception list defeats the purpose of lockdown mode.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For environments that do not use vCenter server to manage ESXi, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Security Profile. Under "Lockdown Mode", review the Exception Users list. or From a PowerCLI command prompt while connected to the ESXi host, run the following script: $vmhost = Get-VMHost | Get-View $lockdown = Get-View $vmhost.ConfigManager.HostAccessManager $lockdown.QueryLockdownExceptions() If the Exception Users list contains accounts that do not require special permissions, this is a finding. Note: The Exception Users list is empty by default and should remain that way except under site-specific circumstances.

## Group: SRG-OS-000032-VMM-000130

**Group ID:** `V-256378`

### Rule: Remote logging for ESXi hosts must be configured.

**Rule ID:** `SV-256378r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote logging to a central log host provides a secure, centralized store for ESXi logs. By gathering host log files onto a central host, it can more easily monitor all hosts with a single tool. It can also do aggregate analysis and searching to look for such things as coordinated attacks on multiple hosts. Logging to a secure, centralized log server also helps prevent log tampering and provides a long-term audit record. Satisfies: SRG-OS-000032-VMM-000130, SRG-OS-000342-VMM-001230, SRG-OS-000479-VMM-001990, SRG-OS-000059-VMM-000280, SRG-OS-000058-VMM-000270, SRG-OS-000051-VMM-000230</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Syslog.global.logHost" value and verify it is set to a site-specific syslog server. Follow the conventions shown below: udp://<IP/FQDN>:514 tcp://<IP/FQDN>:514 ssl://<IP/FQDN>:1514 Multiple servers can be specified when separated by commas. or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Syslog.global.logHost If the "Syslog.global.logHost" setting is not set to a valid, site-specific syslog server, this is a finding.

## Group: SRG-OS-000021-VMM-000050

**Group ID:** `V-256379`

### Rule: The ESXi host must enforce the limit of three consecutive invalid logon attempts by a user.

**Rule ID:** `SV-256379r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized access via user password guessing, otherwise known as brute forcing, is reduced. Once the configured number of attempts is reached, the account is locked by the ESXi host.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Security.AccountLockFailures" value and verify it is set to "3". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Security.AccountLockFailures If the "Security.AccountLockFailures" setting is set to a value other than "3", this is a finding.

## Group: SRG-OS-000329-VMM-001180

**Group ID:** `V-256380`

### Rule: The ESXi host must enforce an unlock timeout of 15 minutes after a user account is locked out.

**Rule ID:** `SV-256380r958736_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By enforcing a reasonable unlock timeout after multiple failed logon attempts, the risk of unauthorized access via user password guessing, otherwise known as brute forcing, is reduced. Users must wait for the timeout period to elapse before subsequent logon attempts are allowed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Security.AccountUnlockTime" value and verify it is set to "900". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Security.AccountUnlockTime If the "Security.AccountUnlockTime" setting is set to a value other than "900", this is a finding.

## Group: SRG-OS-000023-VMM-000060

**Group ID:** `V-256381`

### Rule: The ESXi host must display the Standard Mandatory DOD Notice and Consent Banner before granting access to the system via the Direct Console User Interface (DCUI).

**Rule ID:** `SV-256381r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to display the DOD logon banner prior to a logon attempt will negate legal proceedings resulting from unauthorized access to system resources. Satisfies: SRG-OS-000023-VMM-000060, SRG-OS-000024-VMM-000070</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Annotations.WelcomeMessage" value and verify it contains the DOD logon banner below. or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Annotations.WelcomeMessage Banner: {bgcolor:black} {/color}{align:left}{bgcolor:black}{color:yellow}{hostname} , {ip}{/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:black}{color:yellow}{esxproduct} {esxversion}{/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:black}{color:yellow}{memory} RAM{/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:black}{color:white} {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} using this IS (which includes any device attached to this IS), you consent to the following conditions: {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} - The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} enforcement (LE), and counterintelligence (CI) investigations. {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} - At any time, the USG may inspect and seize data stored on this IS. {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} - Communications using, or data stored on, this IS are not private, are subject to routine monitoring, {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} interception, and search, and may be disclosed or used for any USG-authorized purpose. {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} - This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} for your personal benefit or privacy. {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} - Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} or monitoring of the content of privileged communications, or work product, related to personal representation {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} product are private and confidential. See User Agreement for details. {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{align:left}{bgcolor:yellow}{color:black} {/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{bgcolor:dark-grey}{color:black} {/color}{/bgcolor}\n{bgcolor:black} {/color}{bgcolor:dark-grey}{color:black} {/color}{/bgcolor}\n{bgcolor:black} {/color}{bgcolor:dark-grey}{color:black} {/color}{/bgcolor}\n{bgcolor:black} {/color}{bgcolor:dark-grey}{color:black} {/color}{/bgcolor}\n{bgcolor:black} {/color}{bgcolor:dark-grey}{color:black} {/color}{/bgcolor}\n{bgcolor:black} {/color}{bgcolor:dark-grey}{color:black} {/color}{/bgcolor}\n{bgcolor:black} {/color}{bgcolor:dark-grey}{color:black} {/color}{/bgcolor}\n{bgcolor:black} {/color}{bgcolor:dark-grey}{color:black} {/color}{/bgcolor}\n{bgcolor:black} {/color}{bgcolor:dark-grey}{color:black} {/color}{/bgcolor}\n{bgcolor:black} {/color}{bgcolor:dark-grey}{color:black} {/color}{/bgcolor}\n{bgcolor:black} {/color}{bgcolor:dark-grey}{color:black} {/color}{/bgcolor}\n{bgcolor:black} {/color}{bgcolor:dark-grey}{color:black} {/color}{/bgcolor}\n{bgcolor:black} {/color}{bgcolor:dark-grey}{color:black} {/color}{/bgcolor}\n{bgcolor:black} {/color}{bgcolor:dark-grey}{color:black} {/color}{/bgcolor}\n{bgcolor:black} {/color}{bgcolor:dark-grey}{color:black} {/color}{/bgcolor}\n{bgcolor:black} {/color}{bgcolor:dark-grey}{color:black} {/color}{/bgcolor}\n{bgcolor:black} {/color}{bgcolor:dark-grey}{color:black} {/color}{/bgcolor}\n{bgcolor:black} {/color}{align:left}{bgcolor:dark-grey}{color:white} <F2> Accept Conditions and Customize System / View Logs{/align}{align:right}<F12> Accept Conditions and Shut Down/Restart {bgcolor:black} {/color}{/color}{/bgcolor}{/align}\n{bgcolor:black} {/color}{bgcolor:dark-grey}{color:black} {/color}{/bgcolor} If the "Annotations.WelcomeMessage" setting is not set to the specified banner, this is a finding.

## Group: SRG-OS-000023-VMM-000060

**Group ID:** `V-256382`

### Rule: The ESXi host must display the Standard Mandatory DOD Notice and Consent Banner before granting access to the system via Secure Shell (SSH).

**Rule ID:** `SV-256382r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to display the DOD logon banner prior to a logon attempt will negate legal proceedings resulting from unauthorized access to system resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Config.Etc.issue" value and verify it is set to the DOD logon banner below. or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Config.Etc.issue If the "Config.Etc.issue" setting (/etc/issue file) does not contain the logon banner exactly as shown below, this is a finding. "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details."

## Group: SRG-OS-000023-VMM-000060

**Group ID:** `V-256383`

### Rule: The ESXi host SSH daemon must be configured with the DOD logon banner.

**Rule ID:** `SV-256383r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The warning message reinforces policy awareness during the logon process and facilitates possible legal action against attackers. Alternatively, systems whose ownership should not be obvious should ensure use of a banner that does not provide easy attribution.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # /usr/lib/vmware/openssh/bin/sshd -T|grep banner Expected result: banner /etc/issue If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000033-VMM-000140

**Group ID:** `V-256384`

### Rule: The ESXi host Secure Shell (SSH) daemon must use FIPS 140-2 validated cryptographic modules to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-256384r958408_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OpenSSH on the ESXi host ships with a FIPS 140-2 validated cryptographic module that is enabled by default. For backward compatibility reasons, this can be disabled so this setting can be audited and corrected if necessary.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # esxcli system security fips140 ssh get or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.security.fips140.ssh.get.invoke() Expected result: Enabled: true If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000107-VMM-000530

**Group ID:** `V-256385`

### Rule: The ESXi host Secure Shell (SSH) daemon must ignore ".rhosts" files.

**Rule ID:** `SV-256385r984206_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH trust relationships mean a compromise on one host can allow an attacker to move trivially to other hosts. SSH can emulate the behavior of the obsolete "rsh" command in allowing users to enable insecure access to their accounts via ".rhosts" files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # /usr/lib/vmware/openssh/bin/sshd -T|grep ignorerhosts Expected result: ignorerhosts yes If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256386`

### Rule: The ESXi host Secure Shell (SSH) daemon must not allow host-based authentication.

**Rule ID:** `SV-256386r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH trust relationships mean a compromise on one host can allow an attacker to move trivially to other hosts. SSH's cryptographic host-based authentication is more secure than ".rhosts" authentication because hosts are cryptographically authenticated. However, it is not recommended that hosts unilaterally trust one another, even within an organization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # /usr/lib/vmware/openssh/bin/sshd -T|grep hostbasedauthentication Expected result: hostbasedauthentication no If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256387`

### Rule: The ESXi host Secure Shell (SSH) daemon must not allow authentication using an empty password.

**Rule ID:** `SV-256387r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Configuring this setting for the SSH daemon provides additional assurance that remote logon via SSH will require a password, even in the event of misconfiguration elsewhere.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # /usr/lib/vmware/openssh/bin/sshd -T|grep permitemptypasswords Expected result: permitemptypasswords no If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256388`

### Rule: The ESXi host Secure Shell (SSH) daemon must not permit user environment settings.

**Rule ID:** `SV-256388r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH environment options potentially allow users to bypass access restriction in some configurations. Users must not be able to present environment options to the SSH daemon.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # /usr/lib/vmware/openssh/bin/sshd -T|grep permituserenvironment Expected result: permituserenvironment no If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256389`

### Rule: The ESXi host Secure Shell (SSH) daemon must perform strict mode checking of home directory configuration files.

**Rule ID:** `SV-256389r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If other users have access to modify user-specific SSH configuration files, they may be able to log on the system as another user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # /usr/lib/vmware/openssh/bin/sshd -T|grep strictmodes Expected result: strictmodes yes If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256390`

### Rule: The ESXi host Secure Shell (SSH) daemon must not allow compression or must only allow compression after successful authentication.

**Rule ID:** `SV-256390r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If compression is allowed in an SSH connection prior to authentication, vulnerabilities in the compression software could result in compromise of the system from an unauthenticated connection, potentially with root privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # /usr/lib/vmware/openssh/bin/sshd -T|grep compression Expected result: compression no If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256391`

### Rule: The ESXi host Secure Shell (SSH) daemon must be configured to not allow gateway ports.

**Rule ID:** `SV-256391r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>SSH Transmission Control Protocol (TCP) connection forwarding provides a mechanism to establish TCP connections proxied by the SSH server. This function can provide convenience similar to a virtual private network (VPN) with the similar risk of providing a path to circumvent firewalls and network Access Control Lists (ACLs). Gateway ports allow remote forwarded ports to bind to nonloopback addresses on the server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # /usr/lib/vmware/openssh/bin/sshd -T|grep gatewayports Expected result: gatewayports no If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256392`

### Rule: The ESXi host Secure Shell (SSH) daemon must be configured to not allow X11 forwarding.

**Rule ID:** `SV-256392r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>X11 forwarding over SSH allows for the secure remote execution of X11-based applications. This feature can increase the attack surface of an SSH connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # /usr/lib/vmware/openssh/bin/sshd -T|grep x11forwarding Expected result: x11forwarding no If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256393`

### Rule: The ESXi host Secure Shell (SSH) daemon must not permit tunnels.

**Rule ID:** `SV-256393r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OpenSSH has the ability to create network tunnels (layer 2 and layer 3) over an SSH connection. This function can provide similar convenience to a virtual private network (VPN) with the similar risk of providing a path to circumvent firewalls and network Access Control Lists (ACLs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # /usr/lib/vmware/openssh/bin/sshd -T|grep permittunnel Expected result: permittunnel no If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256394`

### Rule: The ESXi host Secure Shell (SSH) daemon must set a timeout count on idle sessions.

**Rule ID:** `SV-256394r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Setting a timeout ensures that a user login will be terminated as soon as the "ClientAliveCountMax" is reached.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # /usr/lib/vmware/openssh/bin/sshd -T|grep clientalivecountmax Expected result: clientalivecountmax 3 If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256395`

### Rule: The ESXi host Secure Shell (SSH) daemon must set a timeout interval on idle sessions.

**Rule ID:** `SV-256395r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Automatically logging out idle users guards against compromises via hijacked administrative sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # /usr/lib/vmware/openssh/bin/sshd -T|grep clientaliveinterval Expected result: clientaliveinterval 200 If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000037-VMM-000150

**Group ID:** `V-256396`

### Rule: The ESXi host must produce audit records containing information to establish what type of events occurred.

**Rule ID:** `SV-256396r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what types of events occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Satisfies: SRG-OS-000037-VMM-000150, SRG-OS-000063-VMM-000310</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Config.HostAgent.log.level" value and verify it is set to "info". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Config.HostAgent.log.level If the "Config.HostAgent.log.level" setting is not set to "info", this is a finding. Note: Verbose logging level is acceptable for troubleshooting purposes.

## Group: SRG-OS-000069-VMM-000360

**Group ID:** `V-256397`

### Rule: The ESXi host must be configured with a sufficiently complex password policy.

**Rule ID:** `SV-256397r984191_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To enforce the use of complex passwords, minimum numbers of characters of different classes are mandated. The use of complex passwords reduces the ability of attackers to successfully obtain valid passwords using guessing or exhaustive search techniques. Complexity requirements increase the password search space by requiring users to construct passwords from a larger character set than they may otherwise use. Satisfies: SRG-OS-000069-VMM-000360, SRG-OS-000070-VMM-000370, SRG-OS-000071-VMM-000380, SRG-OS-000072-VMM-000390, SRG-OS-000078-VMM-000450, SRG-OS-000266-VMM-000940</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Security.PasswordQualityControl" value and verify it is set to "similar=deny retry=3 min=disabled,disabled,disabled,disabled,15". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Security.PasswordQualityControl If the "Security.PasswordQualityControl" setting is not set to "similar=deny retry=3 min=disabled,disabled,disabled,disabled,15", this is a finding.

## Group: SRG-OS-000077-VMM-000440

**Group ID:** `V-256398`

### Rule: The ESXi host must prohibit the reuse of passwords within five iterations.

**Rule ID:** `SV-256398r984204_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user or root used the same password continuously or was allowed to change it back shortly after being forced to change it to something else, it would provide a potential intruder with the opportunity to keep guessing at one user's password until it was guessed correctly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Security.PasswordHistory" value and verify it is set to "5". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Security.PasswordHistory If the "Security.PasswordHistory" setting is not set to "5" this is a finding.

## Group: SRG-OS-000095-VMM-000480

**Group ID:** `V-256399`

### Rule: The ESXi host must disable the Managed Object Browser (MOB).

**Rule ID:** `SV-256399r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The MOB provides a way to explore the object model used by the VMkernel to manage the host and enables configurations to be changed. This interface is meant to be used primarily for debugging the vSphere Software Development Kit (SDK), but because there are no access controls it could also be used as a method to obtain information about a host being targeted for unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Config.HostAgent.plugins.solo.enableMob" value and verify it is set to "false". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Config.HostAgent.plugins.solo.enableMob If the "Config.HostAgent.plugins.solo.enableMob" setting is not set to "false", this is a finding.

## Group: SRG-OS-000095-VMM-000480

**Group ID:** `V-256400`

### Rule: The ESXi host must be configured to disable nonessential capabilities by disabling Secure Shell (SSH).

**Rule ID:** `SV-256400r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ESXi Shell is an interactive command line interface (CLI) available at the ESXi server console. The ESXi shell provides temporary access to commands essential for server maintenance. Intended primarily for use in break-fix scenarios, the ESXi shell is well suited for checking and modifying configuration details, which are not always generally accessible, using the vSphere Client. The ESXi shell is accessible remotely using SSH by users with the Administrator role. Under normal operating conditions, SSH access to the host must be disabled as is the default. As with the ESXi shell, SSH is also intended only for temporary use during break-fix scenarios. SSH must therefore be disabled under normal operating conditions and must only be enabled for diagnostics or troubleshooting. Remote access to the host must therefore be limited to the vSphere Client or Host Client at all other times. Satisfies: SRG-OS-000095-VMM-000480, SRG-OS-000297-VMM-001040, SRG-OS-000298-VMM-001050</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Services. Under "Services", locate the "SSH" service and verify it is "Stopped". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-VMHostService | Where {$_.Label -eq "SSH"} If the SSH service is "Running", this is a finding.

## Group: SRG-OS-000095-VMM-000480

**Group ID:** `V-256401`

### Rule: The ESXi host must disable ESXi Shell unless needed for diagnostics or troubleshooting.

**Rule ID:** `SV-256401r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ESXi Shell is an interactive command line environment available locally from the Direct Console User Interface (DCUI) or remotely via SSH. Activities performed from the ESXi Shell bypass vCenter role-based access control (RBAC) and audit controls. The ESXi shell must only be turned on when needed to troubleshoot/resolve problems that cannot be fixed through the vSphere client.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Services. Under "Services", locate the "ESXi Shell" service and verify it is "Stopped". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-VMHostService | Where {$_.Label -eq "ESXi Shell"} If the ESXi Shell service is "Running", this is a finding.

## Group: SRG-OS-000104-VMM-000500

**Group ID:** `V-256402`

### Rule: The ESXi host must use Active Directory for local user authentication.

**Rule ID:** `SV-256402r958482_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Join ESXi hosts to an Active Directory domain to eliminate the need to create and maintain multiple local user accounts. Using Active Directory for user authentication simplifies the ESXi host configuration, ensures password complexity and reuse policies are enforced, and reduces the risk of security breaches and unauthorized access. Note: If the Active Directory group "ESX Admins" (default) exists, all users and groups assigned as members to this group will have full administrative access to all ESXi hosts in the domain. Satisfies: SRG-OS-000104-VMM-000500, SRG-OS-000109-VMM-000550, SRG-OS-000112-VMM-000560, SRG-OS-000113-VMM-000570</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For systems that do not use Active Directory and have no local user accounts other than root and/or service accounts, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Authentication Services. Verify the "Directory Services Type" is set to "Active Directory". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-VMHostAuthentication For systems that do not use Active Directory and do have local user accounts, other than root and/or service accounts, this is a finding. If the Directory Services Type is not set to "Active Directory", this is a finding.

## Group: SRG-OS-000104-VMM-000500

**Group ID:** `V-256403`

### Rule: ESXi hosts using Host Profiles and/or Auto Deploy must use the vSphere Authentication Proxy to protect passwords when adding themselves to Active Directory.

**Rule ID:** `SV-256403r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a host is configured to join an Active Directory domain using Host Profiles and/or Auto Deploy, the Active Directory credentials are saved in the profile and are transmitted over the network. To avoid having to save Active Directory credentials in the Host Profile and to avoid transmitting Active Directory credentials over the network, use the vSphere Authentication Proxy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the organization is not using Host Profiles to join Active Directory, this is not applicable. From the vSphere Client, go to Home >> Policies and Profiles >> Host Profiles. Click a Host Profile >> Configure >> Security and Services >> Security Settings >> Authentication Configuration >> Active Directory Configuration >> Join Domain Method. If the method used to join hosts to a domain is not set to "Use vSphere Authentication Proxy to add the host to domain", this is a finding. or From a PowerCLI command prompt while connected to vCenter, run the following command: Get-VMHost | Select Name, ` @{N="HostProfile";E={$_ | Get-VMHostProfile}}, ` @{N="JoinADEnabled";E={($_ | Get-VmHostProfile).ExtensionData.Config.ApplyProfile.Authentication.ActiveDirectory.Enabled}}, ` @{N="JoinDomainMethod";E={(($_ | Get-VMHostProfile).ExtensionData.Config.ApplyProfile.Authentication.ActiveDirectory | Select -ExpandProperty Policy | Where {$_.Id -eq "JoinDomainMethodPolicy"}).Policyoption.Id}} If "JoinADEnabled" is "True" and "JoinDomainMethod" is not "FixedCAMConfigOption", this is a finding.

## Group: SRG-OS-000104-VMM-000500

**Group ID:** `V-256404`

### Rule: Active Directory ESX Admin group membership must not be used when adding ESXi hosts to Active Directory.

**Rule ID:** `SV-256404r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When adding ESXi hosts to Active Directory, all user/group accounts assigned to the Active Directory group \"ESX Admins\" will have full administrative access to the host. If this group is not controlled or known to the system administrators, it may be used for inappropriate access to the host. Therefore, the default group must be changed to a site-specific Active Directory group and membership must be severely restricted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For systems that do not use Active Directory, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Config.HostAgent.plugins.hostsvc.esxAdminsGroup" value and verify it is not set to "ESX Admins". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Config.HostAgent.plugins.hostsvc.esxAdminsGroup If the "Config.HostAgent.plugins.hostsvc.esxAdminsGroup" key is set to "ESX Admins", this is a finding.

## Group: SRG-OS-000163-VMM-000700

**Group ID:** `V-256405`

### Rule: The ESXi host must set a timeout to automatically disable idle shell sessions after two minutes.

**Rule ID:** `SV-256405r970703_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user forgets to log out of their local or remote ESXi Shell session, the idle connection will remain open indefinitely and increase the likelihood of inappropriate host access via session hijacking. The "ESXiShellInteractiveTimeOut" allows the automatic termination of idle shell sessions. Satisfies: SRG-OS-000163-VMM-000700, SRG-OS-000279-VMM-001010</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "UserVars.ESXiShellInteractiveTimeOut" value and verify it is set to "120" (two minutes). or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name UserVars.ESXiShellInteractiveTimeOut If the "UserVars.ESXiShellInteractiveTimeOut" setting is not set to "120", this is a finding.

## Group: SRG-OS-000163-VMM-000700

**Group ID:** `V-256406`

### Rule: The ESXi host must terminate shell services after 10 minutes.

**Rule ID:** `SV-256406r970703_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When the ESXi Shell or Secure Shell (SSH) services are enabled on a host, they will run indefinitely. To avoid having these services left running, set the "ESXiShellTimeOut". The "ESXiShellTimeOut" defines a window of time after which the ESXi Shell and SSH services will be stopped automatically.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "UserVars.ESXiShellTimeOut" value and verify it is set to "600" (10 minutes). or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name UserVars.ESXiShellTimeOut If the "UserVars.ESXiShellTimeOut" setting is not set to "600", this is a finding.

## Group: SRG-OS-000163-VMM-000700

**Group ID:** `V-256407`

### Rule: The ESXi host must log out of the console UI after two minutes.

**Rule ID:** `SV-256407r970703_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When the Direct Console User Interface (DCUI) is enabled and logged in, it should be automatically logged out if left logged on to avoid access by unauthorized persons. The "DcuiTimeOut" setting defines a window of time after which the DCUI will be logged out.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "UserVars.DcuiTimeOut" value and verify it is set to "120" (two minutes). or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name UserVars.DcuiTimeOut If the "UserVars.DcuiTimeOut" setting is not set to "120", this is a finding.

## Group: SRG-OS-000341-VMM-001220

**Group ID:** `V-256408`

### Rule: The ESXi host must enable a persistent log location for all locally stored logs.

**Rule ID:** `SV-256408r958752_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ESXi can be configured to store log files on an in-memory file system. This occurs when the host's "/scratch" directory is linked to "/tmp/scratch". When this is done, only a single day's worth of logs are stored at any time. In addition, log files will be reinitialized upon each reboot. This presents a security risk as user activity logged on the host is only stored temporarily and will not persist across reboots. This can also complicate auditing and make it harder to monitor events and diagnose issues. ESXi host logging should always be configured to a persistent datastore. Note: Scratch space is configured automatically during installation or first boot of an ESXi host and does not usually need to be configured manually. If ESXi is installed on an SD card or USB device, a persistent log location may not be configured upon install as normal.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Syslog.global.logDir" value and verify it is set to a persistent location. If the value of the setting is "[] /scratch/logs", verify the advanced setting "ScratchConfig.CurrentScratchLocation" is not set to "/tmp/scratch". This is a nonpersistent location. If "Syslog.global.logDir" is not configured to a persistent location, this is a finding. or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.syslog.config.get.Invoke() | Select LocalLogOutput,LocalLogOutputIsPersistent If the "LocalLogOutputIsPersistent" value is not true, this is a finding.

## Group: SRG-OS-000355-VMM-001330

**Group ID:** `V-256409`

### Rule: The ESXi host must configure NTP time synchronization.

**Rule ID:** `SV-256409r1038976_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure the accuracy of the system clock, it must be synchronized with an authoritative time source within DOD. Many system functions, including time-based logon and activity restrictions, automated reports, system logs, and audit records, depend on an accurate system clock. If there is no confidence in the correctness of the system clock, time-based functions may not operate as intended and records may be of diminished value. Satisfies: SRG-OS-000355-VMM-001330, SRG-OS-000356-VMM-001340</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Time Configuration. Under "Current Time Configuration", verify "Time Synchronization" is set to "Network Time Protocol". Under "Network Time Protocol", verify the "NTP Servers" are authorized DOD time sources. If the ESXi host is not configured to pull time from authoritative DOD time sources, this is a finding. or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: Get-VMHost | Get-VMHostNTPServer Get-VMHost | Get-VMHostService | Where {$_.Label -eq "NTP Daemon"} If the NTP service is not configured with authoritative DOD time sources or the service does not have a "Policy" of "on" or is stopped, this is a finding.

## Group: SRG-OS-000366-VMM-001430

**Group ID:** `V-256410`

### Rule: The ESXi Image Profile and vSphere Installation Bundle (VIB) acceptance levels must be verified.

**Rule ID:** `SV-256410r984242_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Verify the ESXi Image Profile to only allow signed VIBs. An unsigned VIB represents untested code installed on an ESXi host. The ESXi Image profile supports four acceptance levels: 1. VMwareCertified - VIBs created, tested, and signed by VMware. 2. VMwareAccepted - VIBs created by a VMware partner but tested and signed by VMware. 3. PartnerSupported - VIBs created, tested, and signed by a certified VMware partner. 4. CommunitySupported - VIBs that have not been tested by VMware or a VMware partner. Community Supported VIBs are not supported and do not have a digital signature. To protect the security and integrity of ESXi hosts, do not allow unsigned (CommunitySupported) VIBs to be installed on hosts. Satisfies: SRG-OS-000366-VMM-001430, SRG-OS-000370-VMM-001460, SRG-OS-000404-VMM-001650</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Security Profile. Under "Host Image Profile Acceptance Level", view the acceptance level. or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.software.acceptance.get.Invoke() If the acceptance level is "CommunitySupported", this is a finding.

## Group: SRG-OS-000423-VMM-001700

**Group ID:** `V-256411`

### Rule: The ESXi host must protect the confidentiality and integrity of transmitted information by isolating vMotion traffic.

**Rule ID:** `SV-256411r958908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>While encrypted vMotion is available, vMotion traffic should still be sequestered from other traffic to further protect it from attack. This network must only be accessible to other ESXi hosts, preventing outside access to the network. The vMotion VMkernel port group must be in a dedicated VLAN that can be on a standard or distributed virtual switch as long as the vMotion VLAN is not shared by any other function and is not routed to anything but ESXi hosts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For environments that do not use vCenter server to manage ESXi, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> Networking. Review the VLAN associated with the vMotion VMkernel(s) and verify they are dedicated for that purpose and are logically separated from other functions. If long distance or cross vCenter vMotion is used, the vMotion network can be routable but must be accessible to only the intended ESXi hosts. If the vMotion port group is not on an isolated VLAN and/or is routable to systems other than ESXi hosts, this is a finding.

## Group: SRG-OS-000423-VMM-001700

**Group ID:** `V-256412`

### Rule: The ESXi host must protect the confidentiality and integrity of transmitted information by protecting ESXi management traffic.

**Rule ID:** `SV-256412r958908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The vSphere management network provides access to the vSphere management interface on each component. Services running on the management interface provide an opportunity for an attacker to gain privileged access to the systems. Any remote attack most likely would begin with gaining entry to this network. The Management VMkernel port group can be on a standard or distributed virtual switch but must be on a dedicated VLAN. The Management VLAN must not be shared by any other function and must not be accessible to anything other than management-related functions such as vCenter.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, select the ESXi host and go to Configure >> Networking >> VMkernel adapters. Select each VMkernel adapter that is "Enabled" for management traffic and, in the bottom pane, view the "Enabled services". If any services other than "Management" are enabled on the Management VMkernel adapter, this is a finding. From the vSphere Client, select the ESXi host and go to Configure >> Networking >> VMkernel adapters. Review the VLAN associated with each VMkernel that is "Enabled" for management traffic. Verify with the system administrator that they are dedicated for that purpose and are logically separated from other functions. If the network segment is accessible, except to networks where other management-related entities are located such as vCenter, this is a finding. If there are any other systems or devices such as VMs on the ESXi management segment, this is a finding.

## Group: SRG-OS-000423-VMM-001700

**Group ID:** `V-256413`

### Rule: The ESXi host must protect the confidentiality and integrity of transmitted information by isolating IP-based storage traffic.

**Rule ID:** `SV-256413r958908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Virtual machines (VMs) might share virtual switches and VLANs with the IP-based storage configurations. IP-based storage includes vSAN, iSCSI, and NFS. This configuration might expose IP-based storage traffic to unauthorized VM users. IP-based storage frequently is not encrypted. It can be viewed by anyone with access to this network. To restrict unauthorized users from viewing the IP-based storage traffic, the IP-based storage network must be logically separated from any other traffic. Configuring the IP-based storage adaptors on separate VLANs or network segments from other VMkernels and VMs will limit unauthorized users from viewing the traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If IP-based storage is not used, this is not applicable. From the vSphere Client, select the ESXi host and go to Configure >> Networking >> VMkernel adapters. Select each IP-based storage VMkernel adapter and view the enabled services. If any services are enabled on an NFS or iSCSI IP-based storage VMkernel adapter, this is a finding. If any services are enabled on a vSAN VMkernel adapter other than vSAN, this is a finding. From the vSphere Client, select the ESXi host and go to Configure >> Networking >> VMkernel adapters. Review the VLANs associated with any IP-based storage VMkernels and verify they are dedicated for that purpose and are logically separated from other functions. If any IP-based storage networks are not isolated from other traffic types, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256414`

### Rule: Simple Network Management Protocol (SNMP) must be configured properly on the ESXi host.

**Rule ID:** `SV-256414r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SNMP is not being used, it must remain disabled. If it is being used, the proper trap destination must be configured. If SNMP is not properly configured, monitoring information can be sent to a malicious host that can use this information to plan an attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # esxcli system snmp get or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHostSnmp | Select * If SNMP is not in use and is enabled, this is a finding. If SNMP is enabled and read-only communities are set to "public", this is a finding. If SNMP is enabled and is not using v3 targets, this is a finding. Note: SNMP v3 targets can only be viewed and configured via the "esxcli" command.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256415`

### Rule: The ESXi host must enable bidirectional Challenge-Handshake Authentication Protocol (CHAP) authentication for Internet Small Computer Systems Interface (iSCSI) traffic.

**Rule ID:** `SV-256415r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When enabled, vSphere performs bidirectional authentication of both the iSCSI target and host. When not authenticating both the iSCSI target and host, there is potential for a man-in-the-middle attack, in which an attacker might impersonate either side of the connection to steal data. Bidirectional authentication mitigates this risk.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If iSCSI is not used, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> Storage >> Storage Adapters. Select the iSCSI adapter >> Properties >> Authentication >> Method. View the CHAP configuration and verify CHAP is required for target and host authentication. or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-VMHostHba | Where {$_.Type -eq "iscsi"} | Select AuthenticationProperties -ExpandProperty AuthenticationProperties If iSCSI is used and CHAP is not set to "required" for both the target and host, this is a finding. If iSCSI is used and unique CHAP secrets are not used for each host, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256416`

### Rule: The ESXi host must disable Inter-Virtual Machine (VM) Transparent Page Sharing.

**Rule ID:** `SV-256416r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Published academic papers have demonstrated that by forcing a flush and reload of cache memory, it is possible to measure memory timings to try to determine an Advanced Encryption Standard (AES) encryption key in use on another virtual machine running on the same physical processor of the host server if Transparent Page Sharing (TPS) is enabled between the two VMs. This technique works only in a highly controlled system configured in a nonstandard way that VMware believes would not be recreated in a production environment. Although VMware believes information being disclosed in real-world conditions is unrealistic, out of an abundance of caution, upcoming ESXi Update releases will no longer enable TPS between VMs by default (TPS will still be used within individual VMs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Mem.ShareForceSalting" value and verify it is set to "2". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Mem.ShareForceSalting If the "Mem.ShareForceSalting" setting is not set to "2", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256417`

### Rule: The ESXi host must configure the firewall to restrict access to services running on the host.

**Rule ID:** `SV-256417r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted access to services running on an ESXi host can expose a host to outside attacks and unauthorized access. Reduce the risk by configuring the ESXi firewall to only allow access from authorized networks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Firewall. Under the "Allowed IP addresses" column, review the allowed IPs for each service. Check this for "Incoming" and "Outgoing" sections. or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-VMHostFirewallException | Where {$_.Enabled -eq $true} | Select Name,Enabled,@{N="AllIPEnabled";E={$_.ExtensionData.AllowedHosts.AllIP}} If for an enabled service "Allow connections from any IP address" is selected, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256418`

### Rule: The ESXi host must configure the firewall to block network traffic by default.

**Rule ID:** `SV-256418r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In addition to service-specific firewall rules, ESXi has a default firewall rule policy to allow or deny incoming and outgoing traffic. Reduce the risk of attack by ensuring this is set to deny incoming and outgoing traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # esxcli network firewall get If the "Default Action" does not equal "DROP", this is a finding. or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHostFirewallDefaultPolicy If the Incoming or Outgoing policies are "True", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256419`

### Rule: The ESXi host must enable Bridge Protocol Data Units (BPDU) filter on the host to prevent being locked out of physical switch ports with Portfast and BPDU Guard enabled.

**Rule ID:** `SV-256419r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>BPDU Guard and Portfast are commonly enabled on the physical switch to which the ESXi host is directly connected to reduce the Spanning Tree Protocol (STP) convergence delay. If a BPDU packet is sent from a virtual machine (VM) on the ESXi host to the physical switch configured as stated above, a cascading lockout of all the uplink interfaces from the ESXi host can occur. To prevent this type of lockout, BPDU Filter can be enabled on the ESXi host to drop any BPDU packets being sent to the physical switch. The caveat is that certain Secure Socket Layer (SSL) virtual private networks that use Windows bridging capability can legitimately generate BPDU packets. The administrator should verify no legitimate BPDU packets are generated by VMs on the ESXi host prior to enabling BPDU Filter. If BPDU Filter is enabled in this situation, enabling Reject Forged Transmits on the virtual switch port group adds protection against Spanning Tree loops.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Net.BlockGuestBPDU" value and verify it is set to "1". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Net.BlockGuestBPDU If the "Net.BlockGuestBPDU" setting is not set to "1", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256420`

### Rule: All port groups on standard switches must be configured to reject forged transmits.

**Rule ID:** `SV-256420r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the virtual machine (VM) operating system changes the Media Access Control (MAC) address, the operating system can send frames with an impersonated source MAC address at any time. This allows an operating system to stage malicious attacks on the devices in a network by impersonating a network adaptor authorized by the receiving network. This means the virtual switch does not compare the source and effective MAC addresses. To protect against MAC address impersonation, all virtual switches must have forged transmissions set to reject. Reject Forged Transmit can be set at the vSwitch and/or the Portgroup level. Switch-level settings can be overridden at the Portgroup level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This control addresses ESXi standard switches. Distributed switches are addressed in the vCenter STIG. If there is no standard switch on the ESXi host, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> Networking >> Virtual Switches. On each standard switch, click the "..." button next to each port group. Click View Settings >> Policies tab. Verify that "Forged transmits" is set to "Reject". or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: Get-VirtualSwitch -Standard | Get-SecurityPolicy Get-VirtualPortGroup -Standard | Get-SecurityPolicy If the "Forged Transmits" policy is set to "Accept" (or "true", via PowerCLI), this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256421`

### Rule: All port groups on standard switches must be configured to reject guest Media Access Control (MAC) address changes.

**Rule ID:** `SV-256421r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If the virtual machine (VM) operating system changes the MAC address, it can send frames with an impersonated source MAC address at any time. This allows it to stage malicious attacks on the devices in a network by impersonating a network adaptor authorized by the receiving network. This will prevent VMs from changing their effective MAC address, which will affect applications that require this functionality. This will also affect how a layer 2 bridge will operate and will affect applications that require a specific MAC address for licensing. "Reject MAC Changes" can be set at the vSwitch and/or the Portgroup level. Switch-level settings can be overridden at the Portgroup level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This control addresses ESXi standard switches. Distributed switches are addressed in the vCenter STIG. If there is no standard switch on the ESXi host, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> Networking >> Virtual Switches. On each standard switch, click the "..." button next to each port group. Click View Settings >> Policies tab. Verify "MAC Address Changes" is set to "Reject". or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: Get-VirtualSwitch -Standard | Get-SecurityPolicy Get-VirtualPortGroup -Standard | Get-SecurityPolicy If the "MAC Address Changes" policy is set to "Accept" (or "true", via PowerCLI), this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256422`

### Rule: All port groups on standard switches must be configured to reject guest promiscuous mode requests.

**Rule ID:** `SV-256422r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When promiscuous mode is enabled for a virtual switch, all virtual machines (VMs) connected to the Portgroup have the potential to read all packets across that network (only the virtual machines connected to that Portgroup). Promiscuous mode is disabled by default on the ESXi Server, and this is the recommended setting. Promiscuous mode can be set at the vSwitch and/or the Portgroup level. Switch-level settings can be overridden at the Portgroup level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This control addresses ESXi standard switches. Distributed switches are addressed in the vCenter STIG. If there is no standard switch on the ESXi host, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> Networking >> Virtual Switches. On each standard switch, click the "..." button next to each port group. Click View Settings >> Policies tab. Verify "Promiscuous Mode" is set to "Reject". or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: Get-VirtualSwitch -Standard | Get-SecurityPolicy Get-VirtualPortGroup -Standard | Get-SecurityPolicy If the "Promiscuous Mode" policy is set to "Accept" (or "true", via PowerCLI), this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256423`

### Rule: Use of the dvFilter network application programming interfaces (APIs) must be restricted.

**Rule ID:** `SV-256423r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the organization is not using products that use the dvfilter network API, the host should not be configured to send network information to a virtual machine (VM). If the API is enabled, an attacker might attempt to connect a virtual machine to it, potentially providing access to the network of other VMs on the host. If using a product that makes use of this API, verify the host has been configured correctly. If not using such a product, ensure the setting is blank.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Net.DVFilterBindIpAddress" value and verify the value is blank or the correct IP address of a security appliance if in use. or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Net.DVFilterBindIpAddress If the "Net.DVFilterBindIpAddress" is not blank and security appliances are not in use on the host, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256424`

### Rule: All port groups on standard switches must be configured to a value other than that of the native virtual local area network (VLAN).

**Rule ID:** `SV-256424r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ESXi does not use the concept of native VLAN. Frames with a VLAN specified in the port group will have a tag, but frames with VLAN not specified in the port group are not tagged and therefore will belong to the native VLAN of the physical switch. For example, frames on VLAN 1 from a Cisco physical switch will be untagged, because this is considered as the native VLAN. However, frames from ESXi specified as VLAN 1 will be tagged with a "1"; therefore, traffic from ESXi that is destined for the native VLAN will not be routed correctly (because it is tagged with a "1" instead of being untagged), and traffic from the physical switch coming from the native VLAN will not be visible (because it is not tagged). If the ESXi virtual switch port group uses the native VLAN ID, traffic from those virtual machines (VMs) will not be visible to the native VLAN on the switch because the switch is expecting untagged traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This control addresses ESXi standard switches. Distributed switches are addressed in the vCenter STIG. If there is no standard switch on the ESXi host, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> Networking >> Virtual switches. For each standard switch, review the "VLAN ID" on each port group. Verify they are not set to the native VLAN ID of the attached physical switch. or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VirtualPortGroup -Standard | Select Name, VLanId If any port group is configured with the native VLAN of the attached physical switch, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256425`

### Rule: All port groups on standard switches must not be configured to virtual local area network (VLAN) 4095 unless Virtual Guest Tagging (VGT) is required.

**Rule ID:** `SV-256425r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a port group is set to VLAN 4095, the vSwitch passes all network frames to the attached virtual machines (VMs) without modifying the VLAN tags. In vSphere, this is referred to as VGT. The VM must process the VLAN information itself via an 802.1Q driver in the operating system. VLAN 4095 must only be implemented if the attached VMs have been specifically authorized and are capable of managing VLAN tags themselves. If VLAN 4095 is enabled inappropriately, it may cause denial of service or allow a VM to interact with traffic on an unauthorized VLAN.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This control addresses ESXi standard switches. Distributed switches are addressed in the vCenter STIG. If there is no standard switch on the ESXi host, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> Networking >> Virtual switches. For each standard switch, review the "VLAN ID" on each port group and verify it is not set to "4095". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VirtualPortGroup -Standard | Select Name, VLanId If any port group is configured with VLAN 4095 and is not documented as a needed exception, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256426`

### Rule: All port groups on standard switches must not be configured to virtual local area network (VLAN) values reserved by upstream physical switches.

**Rule ID:** `SV-256426r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Certain physical switches reserve certain VLAN IDs for internal purposes and often disallow traffic configured to these values. For example, Cisco Catalyst switches typically reserve VLANs 1001 to 1024 and 4094, while Nexus switches typically reserve 3968 to 4094. Check the documentation for the specific switch in use. Using a reserved VLAN might result in a denial of service on the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This control addresses ESXi standard switches. Distributed switches are addressed in the vCenter STIG. If there is no standard switch on the ESXi host, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> Networking >> Virtual switches. For each standard switch, review the "VLAN ID" on each port group and verify it is not set to a reserved VLAN ID. or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VirtualPortGroup -Standard | Select Name, VLanId If any port group is configured with a reserved VLAN ID, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256427`

### Rule: The ESXi host must not provide root/administrator-level access to Common Information Model (CIM)-based hardware monitoring tools or other third-party applications.

**Rule ID:** `SV-256427r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The CIM system provides an interface that enables hardware-level management from remote applications via a set of standard application programming interfaces (APIs). In environments that implement CIM hardware monitoring, create a limited-privilege, read-only service account for CIM and place this user in the Exception Users list. When CIM write access is required, create a new role with only the "Host.CIM.Interaction" permission and apply that role to the CIM service account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If CIM monitoring is not implemented, this is not applicable. From the Host Client, select the ESXi host, right-click, and go to "Permissions". Verify the CIM service account is assigned the "Read-only" role or a custom role as described in the discussion. If there is no dedicated CIM service account, this is a finding. If the CIM service account has more permissions than necessary as noted in the discussion, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256428`

### Rule: The ESXi host must have all security patches and updates installed.

**Rule ID:** `SV-256428r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Installing software updates is a fundamental mitigation against the exploitation of publicly known vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine the current version and build: From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Summary. Note the version string next to "Hypervisor:". or From a Secure Shell (SSH) session connected to the ESXi host, or from the ESXi shell, run the following command: # vmware -v Because ESXi hosts should never be able to touch the internet, manually compare the current ESXi version and patch level to the latest available on vmware.com: https://kb.vmware.com/s/article/2143832 If the ESXi host does not have the latest patches, this is a finding. If the ESXi host is not on a supported release, this is a finding. VMware also publishes Advisories on security patches and offers a way to subscribe to email alerts for them. Go to: https://www.vmware.com/support/policies/security_response

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256429`

### Rule: The ESXi host must exclusively enable Transport Layer Security (TLS) 1.2 for all endpoints.

**Rule ID:** `SV-256429r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>TLS 1.0 and 1.1 are deprecated protocols with well-published shortcomings and vulnerabilities. TLS 1.2 should be enabled on all interfaces and SSLv3, TL 1.1, and 1.0 disabled, where supported. Mandating TLS 1.2 may break third-party integrations and add-ons to vSphere. Test these integrations carefully after implementing TLS 1.2 and roll back where appropriate. On interfaces where required functionality is broken with TLS 1.2, this finding is not applicable until such time as the third-party software supports TLS 1.2. Modify TLS settings in the following order: 1. vCenter. 2. ESXi. Satisfies: SRG-OS-000480-VMM-002000, SRG-OS-000425-VMM-001710</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "UserVars.ESXiVPsDisabledProtocols" value and verify it is set to the following: tlsv1,tlsv1.1,sslv3 or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name UserVars.ESXiVPsDisabledProtocols If the "UserVars.ESXiVPsDisabledProtocols" setting is not set to "tlsv1,tlsv1.1,sslv3" or the setting does not exist, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256430`

### Rule: The ESXi host must enable Secure Boot.

**Rule ID:** `SV-256430r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Secure Boot is part of the Unified Extensible Firmware Interface (UEFI) firmware standard. With UEFI Secure Boot enabled, a host refuses to load any UEFI driver or app unless the operating system bootloader has a valid digital signature. Secure Boot for ESXi requires support from the firmware and requires that all ESXi kernel modules, drivers, and vSphere Installation Bundles (VIBs) be signed by VMware or a partner subordinate. Secure Boot is enabled in the BIOS of the ESXi physical server and supported by the hypervisor boot loader. There is no ESXi control to "turn on" Secure Boot. Requiring Secure Boot (failing to boot without it present) is accomplished in another control.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # /usr/lib/vmware/secureboot/bin/secureBoot.py -s If the output is not "Enabled", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256431`

### Rule: The ESXi host must use DOD-approved certificates.

**Rule ID:** `SV-256431r1067573_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The default self-signed host certificate issued by the VMware Certificate Authority (VMCA) must be replaced with a DOD-approved certificate when the host will be accessed directly, such as during a virtual machine (VM) console connection. The use of a DOD certificate on the host assures clients the service they are connecting to is legitimate and properly secured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Certificate. If the issuer is not a DOD-approved certificate authority, or other AO-approved certificate authority, this is a finding. If the host will never be accessed directly (virtual machine console connections bypass vCenter), this is not a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256432`

### Rule: The ESXi host must not suppress warnings that the local or remote shell sessions are enabled.

**Rule ID:** `SV-256432r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Warnings that local or remote shell sessions are enabled alert administrators to activity they may not be aware of and need to investigate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "UserVars.SuppressShellWarning" value and verify it is set to "0". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name UserVars.SuppressShellWarning If the "UserVars.SuppressShellWarning" setting is not set to "0" or the setting does not exist, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256433`

### Rule: The ESXi host must not suppress warnings about unmitigated hyperthreading vulnerabilities.

**Rule ID:** `SV-256433r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The L1 Terminal Fault (L1TF) CPU vulnerabilities published in 2018 have patches and mitigations available in vSphere. However, there are performance impacts to these mitigations that require careful thought and planning from the system administrator before implementation. Until a mitigation is implemented, the UI warning about the lack of a mitigation must not be dismissed so the SA does not assume the vulnerability has been addressed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "UserVars.SuppressHyperthreadWarning" value and verify it is set to "0". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name UserVars.SuppressHyperthreadWarning If "UserVars.SuppressHyperthreadWarning" is not set to "0" or the setting does not exist, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256434`

### Rule: The ESXi host Secure Shell (SSH) daemon must disable port forwarding.

**Rule ID:** `SV-256434r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>While enabling Transmission Control Protocol (TCP) tunnels is a valuable function of sshd, this feature is not appropriate for use on the ESXi hypervisor.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # /usr/lib/vmware/openssh/bin/sshd -T|grep allowtcpforwarding Expected result: allowtcpforwarding no If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256435`

### Rule: The ESXi host OpenSLP service must be disabled.

**Rule ID:** `SV-256435r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OpenSLP implements the Service Location Protocol to help CIM clients discover CIM servers over TCP 427. This service is not widely needed and has had vulnerabilities exposed in the past. To reduce attack surface area and following the minimum functionality principal, the OpenSLP service must be disabled unless explicitly needed and approved. Note: Disabling the OpenSLP service may affect monitoring and third-party systems that use the WBEM DTMF protocols.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Services. Locate the "slpd" service and verify that the "Daemon" is "Stopped" and the "Startup Policy" is set to "Start and stop manually". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-VMHostService | Where {$_.Label -eq "slpd"} If the slpd service does not have a "Policy" of "off" or is running, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256436`

### Rule: The ESXi host must enable audit logging.

**Rule ID:** `SV-256436r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ESXi offers both local and remote audit recordkeeping to meet the requirements of the NIAP Virtualization Protection Profile and Server Virtualization Extended Package. Local records are stored on any accessible local or VMFS path. Remote records are sent to the global syslog servers configured elsewhere. To operate in the NIAP validated state, ESXi must enable and properly configure this audit system. This system is disabled by default. Note: Audit records can be viewed locally via the "/bin/auditLogReader" utility over SSH or at the ESXi shell.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # esxcli system auditrecords get or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.auditrecords.get.invoke()|Format-List Example result: AuditRecordRemoteTransmissionActive : true AuditRecordStorageActive : true AuditRecordStorageCapacity : 100 AuditRecordStorageDirectory : /scratch/auditLog Note: The "Audit Record Storage Directory" may differ from the default above, but it must still be located on persistent storage. If audit record storage is not active and configured, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256437`

### Rule: The ESXi host must enable strict x509 verification for SSL syslog endpoints.

**Rule ID:** `SV-256437r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When sending syslog data to a remote host via SSL, the ESXi host is presented with the endpoint's SSL server certificate. In addition to trust verification, configured elsewhere, this "x509-strict" option performs additional validity checks on CA root certificates during verification. These checks are generally not performed (CA roots are inherently trusted) and might cause incompatibilities with existing, misconfigured CA roots. The NIAP requirements in the Virtualization Protection Profile and Server Virtualization Extended Package, however, require even CA roots to pass validations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If SSL is not used for the syslog target, this is not applicable. From an ESXi shell, run the following command: # esxcli system syslog config get|grep 509 or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.syslog.config.get.invoke()|Select StrictX509Compliance Expected result: Strict X509Compliance: true If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256438`

### Rule: The ESXi host must verify certificates for SSL syslog endpoints.

**Rule ID:** `SV-256438r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When sending syslog data to a remote host, ESXi can be configured to use any combination of TCP, UDP and SSL transports. When using SSL, the server certificate must be validated to ensure that the host is connecting to a valid syslog server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If SSL is not used for a syslog target, this is not applicable. From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Syslog.global.logCheckSSLCerts" value and verify it is set to "true". or From a PowerCLI command prompt while connected to the ESXi host run the following command: Get-VMHost | Get-AdvancedSetting -Name Syslog.global.logCheckSSLCerts If the "Syslog.global.logCheckSSLCerts" setting is not set to "true", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256439`

### Rule: The ESXi host must enable volatile key destruction.

**Rule ID:** `SV-256439r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, pages allocated for virtual machines (VMs), userspace applications, and kernel threads are zeroed out at allocation time. ESXi will always ensure that no nonzero pages are exposed to VMs or userspace applications. While this prevents exposing cryptographic keys from VMs or userworlds to other clients, these keys can stay present in host memory for a long time if the memory is not reused. The NIAP Virtualization Protection Profile and Server Virtualization Extended Package require that memory that may contain cryptographic keys be zeroed upon process exit. To this end, a new configuration option, MemEagerZero, can be configured to enforce zeroing out userworld and guest memory pages when a userworld process or guest exits. For kernel threads, memory spaces holding keys are zeroed out as soon as the secret is no longer needed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Mem.MemEagerZero" value and verify it is set to "1". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Mem.MemEagerZero If the "Mem.MemEagerZero" setting is not set to "1", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256440`

### Rule: The ESXi host must configure a session timeout for the vSphere API.

**Rule ID:** `SV-256440r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The vSphere API (VIM) allows for remote, programmatic administration of the ESXi host. Authenticated API sessions are no different from a risk perspective than authenticated UI sessions and they need similar protections. One of these protections is a basic inactivity timeout, after which the session will be invalidated and reauthentication will be required by the application accessing the API. This is set to 30 seconds by default but can be disabled, thus leaving API sessions open indefinitely. The 30 second default must be verified and maintained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Config.HostAgent.vmacore.soap.sessionTimeout" value and verify it is set to "30". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Config.HostAgent.vmacore.soap.sessionTimeout If the "Config.HostAgent.vmacore.soap.sessionTimeout" setting is not set to "30", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256441`

### Rule: The ESXi Host Client must be configured with a session timeout.

**Rule ID:** `SV-256441r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ESXi Host Client is the UI served up by the host itself, outside of vCenter. It is accessed by browsing to "https://<ESX FQDN>/ui". ESXi is not usually administered via this interface for long periods, and all users will be highly privileged. Implementing a mandatory session idle limit will ensure that orphaned, forgotten, or ignored sessions will be closed promptly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "UserVars.HostClientSessionTimeout" value and verify it is set to "600". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name UserVars.HostClientSessionTimeout If the "UserVars.HostClientSessionTimeout" setting is not set to "600", this is a finding.

## Group: SRG-OS-000033-VMM-000140

**Group ID:** `V-256442`

### Rule: The ESXi host rhttpproxy daemon must use FIPS 140-2 validated cryptographic modules to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-256442r958408_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ESXi runs a reverse proxy service called rhttpproxy that front ends internal services and application programming interfaces (APIs) over one HTTPS port by redirecting virtual paths to localhost ports. This proxy implements a FIPS 140-2 validated OpenSSL cryptographic module that is in FIPS mode by default. This configuration must be validated and maintained to protect the traffic that rhttpproxy manages.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # esxcli system security fips140 rhttpproxy get or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.security.fips140.rhttpproxy.get.invoke() Expected result: Enabled: true If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256443`

### Rule: The ESXi host must be configured with an appropriate maximum password age.

**Rule ID:** `SV-256443r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The older an ESXi local account password is, the larger the opportunity window is for attackers to guess, crack or reuse a previously cracked password. Rotating passwords on a regular basis is a fundamental security practice and one that ESXi supports.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Advanced System Settings. Select the "Security.PasswordMaxDays" value and verify it is set to "90". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-AdvancedSetting -Name Security.PasswordMaxDays If the "Security.PasswordMaxDays" setting is not set to "90", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256444`

### Rule: The ESXi host must not be configured to override virtual machine (VM) configurations.

**Rule ID:** `SV-256444r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Each VM on an ESXi host runs in its own "vmx" process. Upon creation, a vmx process will look in two locations for configuration items, the ESXi host itself and the per-vm *.vmx file in the VM storage path on the datastore. The settings on the ESXi host are read first and take precedence over settings in the *.vmx file. This can be a convenient way to set a setting in one place and have it apply to all VMs running on that host. The difficulty is in managing those settings and determining the effective state. Since managing per-VM vmx settings can be fully automated and customized while the ESXi setting cannot be easily queried, the ESXi configuration must not be used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # stat -c "%s" /etc/vmware/settings Expected result: 0 If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256445`

### Rule: The ESXi host must not be configured to override virtual machine (VM) logger settings.

**Rule ID:** `SV-256445r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Each VM on an ESXi host runs in its own "vmx" process. Upon creation, a vmx process will look in two locations for configuration items, the ESXi host itself and the per-vm *.vmx file in the VM storage path on the datastore. The settings on the ESXi host are read first and take precedence over settings in the *.vmx file. This can be a convenient way to set a setting in one place and have it apply to all VMs running on that host. The difficulty is in managing those settings and determining the effective state. Since managing per-VM vmx settings can be fully automated and customized while the ESXi setting cannot be easily queried, the ESXi configuration must not be used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # grep "^vmx\.log" /etc/vmware/config If the command produces any output, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256446`

### Rule: The ESXi host must require TPM-based configuration encryption.

**Rule ID:** `SV-256446r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An ESXi host's configuration consists of configuration files for each service that runs on the host. The configuration files typically reside in the /etc/ directory, but they can also reside in other namespaces. The configuration files contain run-time information about the state of the services. Over time, the default values in the configuration files might change, for example, when settings on the ESXi host are changed. A cron job backs up the ESXi configuration files periodically, when ESXi shuts down gracefully or on demand, and creates an archived configuration file in the boot bank. When ESXi reboots, it reads the archived configuration file and recreates the state that ESXi was in when the backup was taken. Before vSphere 7.0 Update 2, the archived ESXi configuration file is not encrypted. In vSphere 7.0 Update 2 and later, the archived configuration file is encrypted. When the ESXi host is configured with a Trusted Platform Module (TPM), the TPM is used to "seal" the configuration to the host, providing a strong security guarantee and additional protection from offline attacks. Configuration encryption uses the physical TPM when it is available and supported at install or upgrade time. If the TPM was added or enabled later, the ESXi host must be told to reconfigure to use the newly available TPM. Once the TPM configuration encryption is enabled, it cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ESXi host does not have a compatible TPM, this finding is downgraded to a CAT III. From an ESXi shell, run the following command: # esxcli system settings encryption get|grep Mode or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.settings.encryption.get.invoke() | Select Mode Expected result: Mode: TPM If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256447`

### Rule: The ESXi host must implement Secure Boot enforcement.

**Rule ID:** `SV-256447r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Secure Boot is part of the UEFI firmware standard. With UEFI Secure Boot enabled, a host refuses to load any UEFI driver or app unless the operating system bootloader has a valid digital signature. Secure Boot for ESXi requires support from the firmware and it requires that all ESXi kernel modules, drivers and VIBs be signed by VMware or a partner subordinate. Secure Boot is enabled in the BIOS of the ESXi physical server and supported by the hypervisor boot loader. This control flips ESXi from merely supporting Secure Boot to requiring it. Without this setting enabled, and configuration encryption, an ESXi host could be subject to offline attacks. An attacker could simply transfer the ESXi install drive to a non-Secure Boot host and boot it up without ESXi complaining. Note: This setting is only available in 7.0 Update 2 and later. Satisfies: SRG-OS-000480-VMM-002000, SRG-OS-000257-VMM-000910, SRG-OS-000278-VMM-001000, SRG-OS-000446-VMM-001790</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ESXi host does not have a compatible TPM, this finding is downgraded to a CAT III. From an ESXi shell, run the following command: # esxcli system settings encryption get|grep "Secure Boot" or From a PowerCLI command prompt while connected to the ESXi host, run the following commands: $esxcli = Get-EsxCli -v2 $esxcli.system.settings.encryption.get.invoke() | Select RequireSecureBoot Expected result: Require Secure Boot: true If the output does not match the expected result, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-256448`

### Rule: The ESXi Common Information Model (CIM) service must be disabled.

**Rule ID:** `SV-256448r1051419_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The CIM system provides an interface that enables hardware-level management from remote applications via a set of standard application programming interfaces (APIs). These APIs are consumed by external applications such as HP SIM or Dell OpenManage for agentless, remote hardware monitoring of the ESXi host. To reduce attack surface area and following the minimum functionality principal, the CIM service must be disabled unless explicitly needed and approved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the vSphere Client, go to Hosts and Clusters. Select the ESXi Host >> Configure >> System >> Services. Locate the "CIM Server" service and verify the "Daemon" is "Stopped" and the "Startup Policy" is set to "Start and stop manually". or From a PowerCLI command prompt while connected to the ESXi host, run the following command: Get-VMHost | Get-VMHostService | Where {$_.Label -eq "CIM Server"} If the "CIM Server" service does not have a "Policy" of "off" or is running, this is a finding.

## Group: SRG-OS-000478-VMM-001980

**Group ID:** `V-256449`

### Rule: The ESXi host SSH daemon must be configured to only use FIPS 140-2 validated ciphers.

**Rule ID:** `SV-256449r959006_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. ESXi must implement cryptographic modules adhering to the higher standards approved by the federal government because this provides assurance they have been tested and validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an ESXi shell, run the following command: # /usr/lib/vmware/openssh/bin/sshd -T|grep ciphers Expected result: ciphers aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr If the output does not match the expected result, this is a finding.

