# STIG Benchmark: Canonical Ubuntu 22.04 LTS Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-260469`

### Rule: Ubuntu 22.04 LTS must disable the x86 Ctrl-Alt-Delete key sequence.

**Rule ID:** `SV-260469r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A locally logged-on user who presses Ctrl-Alt-Delete, when at the console, can reboot the system. If accidentally pressed, as could happen in the case of a mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS is not configured to reboot the system when Ctrl-Alt-Delete is pressed by using the following command: $ systemctl status ctrl-alt-del.target ctrl-alt-del.target Loaded: masked (Reason: Unit ctrl-alt-del.target is masked.) Active: inactive (dead) If the "ctrl-alt-del.target" is not masked, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-260470`

### Rule: Ubuntu 22.04 LTS, when booted, must require authentication upon booting into single-user and maintenance modes.

**Rule ID:** `SV-260470r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS requires a password for authentication upon booting into single-user and maintenance modes by using the following command: $ sudo grep -i password /boot/grub/grub.cfg password_pbkdf2 root grub.pbkdf2.sha512.10000.03255F190F0E2F7B4F0D1C3216012309162F022A7A636771 If the root password entry does not begin with "password_pbkdf2", this is a finding.

## Group: SRG-OS-000254-GPOS-00095

**Group ID:** `V-260471`

### Rule: Ubuntu 22.04 LTS must initiate session audits at system startup.

**Rule ID:** `SV-260471r1069117_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If auditing is enabled late in the startup process, the actions of some startup processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Ubuntu 22.04 LTS enables auditing at system startup in grub by using the following command: $ sudo grep "^\s*linux" /boot/grub/grub.cfg linux /boot/vmlinuz-5.4.0-31-generic root=UUID=74d13bcd-6ebd-4493-b5d2-3ebc37d01702 ro audit=1 linux /boot/vmlinuz-5.4.0-31-generic root=UUID=74d13bcd-6ebd-4493-b5d2-3ebc37d01702 ro recovery nomodeset audit=1 If any linux lines do not contain "audit=1", this is a finding. Note: Output may vary by system.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-260472`

### Rule: Ubuntu 22.04 LTS must restrict access to the kernel message buffer.

**Rule ID:** `SV-260472r958524_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Restricting access to the kernel message buffer limits access only to root. This prevents attackers from gaining additional system information as a nonprivileged user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS is configured to restrict access to the kernel message buffer by using the following command: $ sysctl kernel.dmesg_restrict kernel.dmesg_restrict = 1 If "kernel.dmesg_restrict" is not set to "1" or is missing, this is a finding. Verify that there are no configurations that enable the kernel dmesg function: $ sudo grep -ir kernel.dmesg_restrict /run/sysctl.d/* /etc/sysctl.d/* /usr/local/lib/sysctl.d/* /usr/lib/sysctl.d/* /lib/sysctl.d/* /etc/sysctl.conf 2> /dev/null /etc/sysctl.d/10-kernel-hardening.conf:kernel.dmesg_restrict = 1 If "kernel.dmesg_restrict" is not set to "1", is commented out, is missing, or conflicting results are returned, this is a finding.

## Group: SRG-OS-000184-GPOS-00078

**Group ID:** `V-260473`

### Rule: Ubuntu 22.04 LTS must disable kernel core dumps so that it can fail to a secure state if system initialization fails, shutdown fails or aborts fail.

**Rule ID:** `SV-260473r1044782_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kernel core dumps may contain the full contents of system memory at the time of the crash. Kernel core dumps may consume a considerable amount of disk space and may result in denial of service by exhausting the available space on the target file system partition.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that kernel core dumps are disabled unless needed by using the following command: $ systemctl status kdump-tools.service kdump-tools.service Loaded: masked (Reason: Unit kdump-tools.service is masked.) Active: inactive (dead) If "kdump-tools.service" is not masked and inactive, ask the system administrator (SA) if the use of the service is required and documented with the information system security officer (ISSO). If the service is active and is not documented, this is a finding.

## Group: SRG-OS-000433-GPOS-00193

**Group ID:** `V-260474`

### Rule: Ubuntu 22.04 LTS must implement address space layout randomization to protect its memory from unauthorized code execution.

**Rule ID:** `SV-260474r958928_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in nonexecutable regions of memory or in prohibited memory locations. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can either be hardware-enforced or software-enforced with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS implements address space layout randomization (ASLR) by using the following command: $ sysctl kernel.randomize_va_space kernel.randomize_va_space = 2 If no output is returned, verify the kernel parameter "randomize_va_space" is set to "2" by using the following command: $ cat /proc/sys/kernel/randomize_va_space 2 If "kernel.randomize_va_space" is not set to "2", this is a finding. Verify that a saved value of the "kernel.randomize_va_space" variable is not defined. $ sudo grep -ER "^kernel.randomize_va_space=[^2]" /etc/sysctl.conf /etc/sysctl.d If this returns a result, this is a finding.

## Group: SRG-OS-000433-GPOS-00192

**Group ID:** `V-260475`

### Rule: Ubuntu 22.04 LTS must implement nonexecutable data to protect its memory from unauthorized code execution.

**Rule ID:** `SV-260475r958928_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in nonexecutable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can either be hardware-enforced or software-enforced with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the NX (no-execution) bit flag is set on the system by using the following command: $ sudo dmesg | grep -i "execute disable" [ 0.000000] NX (Execute Disable) protection: active If "dmesg" does not show "NX (Execute Disable) protection: active", check the hardware capabilities of the installed CPU by using the following command: $ grep flags /proc/cpuinfo | grep -o nx | sort -u nx If no output is returned, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-260476`

### Rule: Ubuntu 22.04 LTS must be configured so that the Advance Package Tool (APT) prevents the installation of patches, service packs, device drivers, or operating system components without verification they have been digitally signed using a certificate that is recognized and approved by the organization.

**Rule ID:** `SV-260476r1015003_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. Accordingly, patches, service packs, device drivers, or operating system components must be signed with a certificate recognized and approved by the organization. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. The operating system should not have to verify the software again. This requirement does not mandate DOD certificates for this purpose; however, the certificate used to verify the software must be from an approved certificate authority (CA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that APT is configured to prevent the installation of patches, service packs, device drivers, or Ubuntu operating system components without verification they have been digitally signed using a certificate that is recognized and approved by the organization by using the following command: $ grep -i allowunauthenticated /etc/apt/apt.conf.d/* /etc/apt/apt.conf.d/01-vendor-ubuntu:APT::Get::AllowUnauthenticated "false"; If "APT::Get::AllowUnauthenticated" is not set to "false", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000437-GPOS-00194

**Group ID:** `V-260477`

### Rule: Ubuntu 22.04 LTS must be configured so that the Advance Package Tool (APT) removes all software components after updated versions have been installed.

**Rule ID:** `SV-260477r1044773_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Previous versions of software components that are not removed from the information system after updates have been installed may be exploited by adversaries. Some information technology products may remove older versions of software automatically from the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify APT is configured to remove all software components after updated versions have been installed by using the following command: $ grep -i remove-unused /etc/apt/apt.conf.d/50unattended-upgrades Unattended-Upgrade::Remove-Unused-Kernel-Packages "true"; Unattended-Upgrade::Remove-Unused-Dependencies "true"; If "Unattended-Upgrade::Remove-Unused-Kernel-Packages" and "Unattended-Upgrade::Remove-Unused-Dependencies" are not set to "true", are commented out, or are missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-260478`

### Rule: Ubuntu 22.04 LTS must have the "libpam-pwquality" package installed.

**Rule ID:** `SV-260478r991587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. "pwquality" enforces complex password construction configuration and has the ability to limit brute-force attacks on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS has the "libpam-pwquality" package installed with the following command: $ dpkg -l | grep libpam-pwquality ii libpam-pwquality:amd64 1.4.4-1build2 amd64 PAM module to check password strength If "libpam-pwquality" is not installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-260479`

### Rule: Ubuntu 22.04 LTS must have the "chrony" package installed.

**Rule ID:** `SV-260479r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Organizations must consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "chrony" package is installed using the following command: $ dpkg -l | grep chrony ii chrony 4.2-2ubuntu2 amd64 Versatile implementation of the Network Time Protocol If the "chrony" package is not installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-260480`

### Rule: Ubuntu 22.04 LTS must not have the "systemd-timesyncd" package installed.

**Rule ID:** `SV-260480r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Organizations must consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "systemd-timesyncd" package is not installed by using the following command: $ dpkg -l | grep systemd-timesyncd If the "systemd-timesyncd" package is installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-260481`

### Rule: Ubuntu 22.04 LTS must not have the "ntp" package installed.

**Rule ID:** `SV-260481r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Organizations must consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "ntp" package is not installed by using the following command: $ dpkg -l | grep ntp If the "ntp" package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-260482`

### Rule: Ubuntu 22.04 LTS must not have the "rsh-server" package installed.

**Rule ID:** `SV-260482r958478_rule`
**Severity:** high

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Remote Shell (RSH) is a client/server application protocol that provides an unencrypted remote access service, which does not provide for the confidentiality and integrity of user passwords or the remote session. If users were allowed to login to a system using RSH, the privileged user passwords and communications could be compromised. Removing the "rsh-server" package decreases the risk of accidental or intentional activation of the RSH service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "rsh-server" package is not installed by using the following command: $ dpkg -l | grep rsh-server If the "rsh-server" package is installed, this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-260483`

### Rule: Ubuntu 22.04 LTS must not have the "telnet" package installed.

**Rule ID:** `SV-260483r987796_rule`
**Severity:** high

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities are often overlooked and therefore, may remain unsecure. They increase the risk to the platform by providing additional attack vectors. Telnet is a client/server application protocol that provides an unencrypted remote access service, which does not provide for the confidentiality and integrity of user passwords or the remote session. If users were allowed to login to a system using Telnet, the privileged user passwords and communications could be compromised. Removing the "telnetd" package decreases the risk of accidental or intentional activation of the Telnet service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "telnetd" package is not installed on Ubuntu 22.04 LTS by using the following command: $ dpkg -l | grep telnetd If the "telnetd" package is installed, this is a finding.

## Group: SRG-OS-000185-GPOS-00079

**Group ID:** `V-260484`

### Rule: Ubuntu 22.04 LTS must implement cryptographic mechanisms to prevent unauthorized disclosure and modification of all information that requires protection at rest.

**Rule ID:** `SV-260484r958552_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Operating systems handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). Satisfies: SRG-OS-000185-GPOS-00079, SRG-OS-000404-GPOS-00183, SRG-OS-000405-GPOS-00184</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS prevents unauthorized disclosure or modification of all information requiring at-rest protection by using disk encryption. Note: If there is a documented and approved reason for not having data-at-rest encryption, this requirement is not applicable. Determine the partition layout for the system by using the following command: $ sudo fdisk -l ... Device Start End Sectors Size Type /dev/sda1 2048 2203647 2201600 1G EFI System /dev/sda2 2203648 6397951 4194304 2G Linux filesystem /dev/sda3 6397952 536868863 530470912 252.9G Linux filesystem ... Verify the system partitions are all encrypted by using the following command: # more /etc/crypttab Every persistent disk partition present must have an entry in the file. If any partitions other than the boot partition or pseudo file systems (such as /proc or /sys) are not listed, this is a finding.

## Group: SRG-OS-000258-GPOS-00099

**Group ID:** `V-260485`

### Rule: Ubuntu 22.04 LTS must have directories that contain system commands set to a mode of "755" or less permissive.

**Rule ID:** `SV-260485r991559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user has in order to make access decisions regarding the deletion of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands directories have mode "755" or less permissive by using the following command: $ find /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin -perm /022 -type d -exec stat -c "%n %a" '{}' \; If any directories are found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-260486`

### Rule: Ubuntu 22.04 LTS must have system commands set to a mode of "755" or less permissive.

**Rule ID:** `SV-260486r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Ubuntu 22.04 LTS were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to Ubuntu 22.04 LTS with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands contained in the following directories have mode "755" or less permissive by using the following command: $ sudo find /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin -perm /022 -type f -exec stat -c "%n %a" '{}' \; If any files are found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-260487`

### Rule: Ubuntu 22.04 LTS library files must have mode "755" or less permissive.

**Rule ID:** `SV-260487r1107262_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and "/usr/lib64" have mode 0755 or less permissive. Check that the systemwide shared library files have mode 0755 or less permissive with the following command: $ sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' -perm /022 -exec stat -c "%n %a" {} + If any output is returned, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-260488`

### Rule: Ubuntu 22.04 LTS must configure the "/var/log" directory to have mode "755" or less permissive.

**Rule ID:** `SV-260488r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/var/log" directory has mode of "755" or less permissive by using the following command: Note: If rsyslog is active and enabled on the operating system, this requirement is not applicable. $ stat -c "%n %a" /var/log /var/log 755 If a value of "755" or less permissive is not returned, this is a finding.

## Group: SRG-OS-000205-GPOS-00083

**Group ID:** `V-260489`

### Rule: Ubuntu 22.04 LTS must generate error messages that provide information necessary for corrective actions without revealing information that could be exploited by adversaries.

**Rule ID:** `SV-260489r958564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any operating system providing too much information in error messages risks compromising the data and security of the structure, and content of error messages needs to be carefully considered by the organization. Organizations carefully consider the structure/content of error messages. The extent to which information systems are able to identify and handle error conditions is guided by organizational policy and operational requirements. Information that could be exploited by adversaries includes, for example, erroneous logon attempts with passwords entered by mistake as the username, mission/business information that can be derived from (if not stated explicitly by) information recorded, and personal information, such as account numbers, social security numbers, and credit card numbers. The /var/log/btmp, /var/log/wtmp, and /var/log/lastlog files have group write and global read permissions to allow for the lastlog function to perform. Limiting the permissions beyond this configuration will result in the failure of functions that rely on the lastlog database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS has all system log files under the "/var/log" directory with a permission set to "640" or less permissive by using the following command: Note: The btmp, wtmp, and lastlog files are excluded. Refer to the Discussion for details. $ sudo find /var/log -perm /137 ! -name '*[bw]tmp' ! -name '*lastlog' -type f -exec stat -c "%n %a" {} \; If the command displays any output, this is a finding.

## Group: SRG-OS-000205-GPOS-00083

**Group ID:** `V-260490`

### Rule: Ubuntu 22.04 LTS must generate system journal entries without revealing information that could be exploited by adversaries.

**Rule ID:** `SV-260490r1069105_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any operating system providing too much information in error messages risks compromising the data and security of the structure, and content of error messages needs to be carefully considered by the organization. Organizations carefully consider the structure/content of error messages. The extent to which information systems are able to identify and handle error conditions is guided by organizational policy and operational requirements. Information that could be exploited by adversaries includes, for example, erroneous logon attempts with passwords entered by mistake as the username, mission/business information that can be derived from (if not stated explicitly by) information recorded, and personal information, such as account numbers, social security numbers, and credit card numbers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the /run/log/journal and /var/log/journal directories have permissions set to "2750" or less permissive by using the following command: $ sudo find /run/log/journal /var/log/journal -type d -exec stat -c "%n %a" {} \; /run/log/journal 2750 /var/log/journal 2750 /var/log/journal/3b018e681c904487b11671b9c1987cce 2750 If any output returned has a permission set greater than "2750", this is a finding. Verify all files in the /run/log/journal and /var/log/journal directories have permissions set to "640" or less permissive by using the following command: $ sudo find /run/log/journal /var/log/journal -type f -exec stat -c "%n %a" {} \; /var/log/journal/3b018e681c904487b11671b9c1987cce/system@99dcc72bb1134aaeae4bf157aa7606f4-0000000000003c7a-0006073f8d1c0fec.journal 640 /var/log/journal/3b018e681c904487b11671b9c1987cce/system.journal 640 /var/log/journal/3b018e681c904487b11671b9c1987cce/user-1000.journal 640 /var/log/journal/3b018e681c904487b11671b9c1987cce/user-1000@bdedf14602ff4081a77dc7a6debc8626-00000000000062a6-00060b4b414b617a.journal 640 /var/log/journal/3b018e681c904487b11671b9c1987cce If any output returned has a permission set greater than "640", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-260491`

### Rule: Ubuntu 22.04 LTS must configure "/var/log/syslog" file with mode "640" or less permissive.

**Rule ID:** `SV-260491r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Ubuntu 22.04 LTS configures the "/var/log/syslog" file with mode "640" or less permissive by using the following command: $ stat -c "%n %a" /var/log/syslog /var/log/syslog 640 If a value of "640" or less permissive is not returned, this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-260492`

### Rule: Ubuntu 22.04 LTS must configure audit tools with a mode of "755" or less permissive.

**Rule ID:** `SV-260492r991557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000257-GPOS-00098</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS configures the audit tools to have a file permission of "755" or less to prevent unauthorized access by using the following command: $ stat -c "%n %a" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/audispd* /sbin/augenrules /sbin/auditctl 755 /sbin/aureport 755 /sbin/ausearch 755 /sbin/autrace 755 /sbin/auditd 755 /sbin/audispd-zos-remote 755 /sbin/augenrules 755 If any of the audit tools have a mode more permissive than "0755", this is a finding.

## Group: SRG-OS-000258-GPOS-00099

**Group ID:** `V-260493`

### Rule: Ubuntu 22.04 LTS must have directories that contain system commands owned by "root".

**Rule ID:** `SV-260493r991559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user has in order to make access decisions regarding the deletion of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands directories are owned by "root" by using the following command: $ sudo find /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -user root -type d -exec stat -c "%n %U" '{}' \; If any system commands directories are returned, this is a finding.

## Group: SRG-OS-000258-GPOS-00099

**Group ID:** `V-260494`

### Rule: Ubuntu 22.04 LTS must have directories that contain system commands group-owned by "root".

**Rule ID:** `SV-260494r991559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user has in order to make access decisions regarding the deletion of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands directories are group-owned by "root" by using the following command: $ sudo find /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -group root -type d -exec stat -c "%n %G" '{}' \; If any system commands directories are returned that are not Set Group ID up on execution (SGID) files and owned by a privileged account, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-260495`

### Rule: Ubuntu 22.04 LTS must have system commands owned by "root" or a system account.

**Rule ID:** `SV-260495r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Ubuntu 22.04 LTS were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to Ubuntu 22.04 LTS with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands contained in the following directories are owned by "root", or a required system account, by using the following command: $ sudo find /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -user root -type f -exec stat -c "%n %U" '{}' \; If any system commands are returned and are not owned by a required system account, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-260496`

### Rule: Ubuntu 22.04 LTS must have system commands group-owned by "root" or a system account.

**Rule ID:** `SV-260496r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Ubuntu 22.04 LTS were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to Ubuntu 22.04 LTS with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands contained in the following directories are group-owned by "root" or a required system account by using the following command: $ sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -group root -type f ! -perm /2000 -exec stat -c "%n %G" '{}' \; If any system commands are returned that are not Set Group ID upon execution (SGID) files and group-owned by a required system account, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-260497`

### Rule: Ubuntu 22.04 LTS library directories must be owned by "root".

**Rule ID:** `SV-260497r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library directories "/lib", "/lib64", and "/usr/lib" are owned by "root" by using the following command: $ sudo find /lib /usr/lib /lib64 ! -user root -type d -exec stat -c "%n %U" '{}' \; If any systemwide library directory is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-260498`

### Rule: Ubuntu 22.04 LTS library directories must be group-owned by "root".

**Rule ID:** `SV-260498r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide library directories "/lib", "/lib64", and "/usr/lib" are group-owned by "root" by using the following command: $ sudo find /lib /usr/lib /lib64 ! -group root -type d -exec stat -c "%n %G" '{}' \; If any systemwide shared library directory is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-260499`

### Rule: Ubuntu 22.04 LTS library files must be owned by "root".

**Rule ID:** `SV-260499r1107264_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and "/usr/lib64" are owned by root with the following command: $ sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' ! -user root -exec stat -c "%n %U" {} + If any output is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-260500`

### Rule: Ubuntu 22.04 LTS library files must be group-owned by "root".

**Rule ID:** `SV-260500r1107266_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and "/usr/lib64" are group owned by root with the following command: $ sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' ! -group root -exec stat -c "%n %G" {} + If any output is returned, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-260501`

### Rule: Ubuntu 22.04 LTS must configure the directories used by the system journal to be owned by "root".

**Rule ID:** `SV-260501r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the /run/log/journal and /var/log/journal directories are owned by "root" by using the following command: $ sudo find /run/log/journal /var/log/journal -type d -exec stat -c "%n %U" {} \; /run/log/journal root /var/log/journal root /var/log/journal/3b018e681c904487b11671b9c1987cce root If any output returned is not owned by "root", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-260502`

### Rule: Ubuntu 22.04 LTS must configure the directories used by the system journal to be group-owned by "systemd-journal".

**Rule ID:** `SV-260502r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the /run/log/journal and /var/log/journal directories are group-owned by "systemd-journal" by using the following command: $ sudo find /run/log/journal /var/log/journal -type d -exec stat -c "%n %G" {} \; /run/log/journal systemd-journal /var/log/journal systemd-journal /var/log/journal/3b018e681c904487b11671b9c1987cce systemd-journal If any output returned is not group-owned by "systemd-journal", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-260503`

### Rule: Ubuntu 22.04 LTS must configure the files used by the system journal to be owned by "root".

**Rule ID:** `SV-260503r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the /run/log/journal and /var/log/journal files are owned by "root" by using the following command: $ sudo find /run/log/journal /var/log/journal -type f -exec stat -c "%n %U" {} \; /var/log/journal/3b018e681c904487b11671b9c1987cce/system@99dcc72bb1134aaeae4bf157aa7606f4-0000000000003c7a-0006073f8d1c0fec.journal root /var/log/journal/3b018e681c904487b11671b9c1987cce/system.journal root /var/log/journal/3b018e681c904487b11671b9c1987cce/user-1000.journal root /var/log/journal/3b018e681c904487b11671b9c1987cce/user-1000@bdedf14602ff4081a77dc7a6debc8626-00000000000062a6-00060b4b414b617a.journal root /var/log/journal/3b018e681c904487b11671b9c1987cce/system@99dcc72bb1134aaeae4bf157aa7606f4-0000000000005301-000609a409 593.journal root /var/log/journal/3b018e681c904487b11671b9c1987cce/system@99dcc72bb1134aaeae4bf157aa7606f4-0000000000000001-000604dae53225ee.journal root /var/log/journal/3b018e681c904487b11671b9c1987cce/user-1000@bdedf14602ff4081a77dc7a6debc8626-000000000000083b-000604dae72c7e3b.journal root If any output returned is not owned by "root", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-260504`

### Rule: Ubuntu 22.04 LTS must configure the files used by the system journal to be group-owned by "systemd-journal".

**Rule ID:** `SV-260504r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the /run/log/journal and /var/log/journal files are group-owned by "systemd-journal" by using the following command: $ sudo find /run/log/journal /var/log/journal -type f -exec stat -c "%n %G" {} \; /var/log/journal/3b018e681c904487b11671b9c1987cce/system@99dcc72bb1134aaeae4bf157aa7606f4-0000000000003c7a-0006073f8d1c0fec.journal systemd-journal /var/log/journal/3b018e681c904487b11671b9c1987cce/system.journal systemd-journal /var/log/journal/3b018e681c904487b11671b9c1987cce/user-1000.journal systemd-journal /var/log/journal/3b018e681c904487b11671b9c1987cce/user-1000@bdedf14602ff4081a77dc7a6debc8626-00000000000062a6-00060b4b414b617a.journal systemd-journal /var/log/journal/3b018e681c904487b11671b9c1987cce/system@99dcc72bb1134aaeae4bf157aa7606f4-0000000000005301-000609a409 593.journal systemd-journal /var/log/journal/3b018e681c904487b11671b9c1987cce/system@99dcc72bb1134aaeae4bf157aa7606f4-0000000000000001-000604dae53225ee.journal systemd-journal /var/log/journal/3b018e681c904487b11671b9c1987cce/user-1000@bdedf14602ff4081a77dc7a6debc8626-000000000000083b-000604dae72c7e3b.journal systemd-journal If any output returned is not group-owned by "systemd-journal", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-260505`

### Rule: Ubuntu 22.04 LTS must be configured so that the "journalctl" command is owned by "root".

**Rule ID:** `SV-260505r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, Personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "journalctl" command is owned by "root" by using the following command: $ sudo find /usr/bin/journalctl -exec stat -c "%n %U" {} \; /usr/bin/journalctl root If "journalctl" is not owned by "root", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-260506`

### Rule: Ubuntu 22.04 LTS must be configured so that the "journalctl" command is group-owned by "root".

**Rule ID:** `SV-260506r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "journalctl" command is group-owned by "root" by using the following command: $ sudo find /usr/bin/journalctl -exec stat -c "%n %G" {} \; /usr/bin/journalctl root If "journalctl" is not group-owned by "root", this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-260507`

### Rule: Ubuntu 22.04 LTS must configure audit tools to be owned by "root".

**Rule ID:** `SV-260507r1101725_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000257-GPOS-00098</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS configures the audit tools to be owned by "root" to prevent any unauthorized access with the following command: $ stat -c "%n %U" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/audisp* /sbin/augenrules /sbin/auditctl root /sbin/aureport root /sbin/ausearch root /sbin/autrace root /sbin/auditd root /sbin/audispd-zos-remote root /sbin/augenrules root If any of the audit tools are not owned by "root", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-260508`

### Rule: Ubuntu 22.04 LTS must configure the "/var/log" directory to be owned by "root".

**Rule ID:** `SV-260508r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS configures the "/var/log" directory to be owned by "root" by using the following command: $ stat -c "%n %U" /var/log /var/log root If the "/var/log" directory is not owned by "root", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-260509`

### Rule: Ubuntu 22.04 LTS must configure the "/var/log" directory to be group-owned by "syslog".

**Rule ID:** `SV-260509r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Ubuntu 22.04 LTS configures the "/var/log" directory to be group-owned by "syslog" by using the following command: $ stat -c "%n %G" /var/log /var/log syslog If the "/var/log" directory is not group-owned by "syslog", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-260510`

### Rule: Ubuntu 22.04 LTS must configure "/var/log/syslog" file to be owned by "syslog".

**Rule ID:** `SV-260510r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Ubuntu 22.04 LTS configures the "/var/log/syslog" file to be owned by "syslog" by using the following command: $ stat -c "%n %U" /var/log/syslog /var/log/syslog If the "/var/log/syslog" file is not owned by "syslog", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-260511`

### Rule: Ubuntu 22.04 LTS must configure the "/var/log/syslog" file to be group-owned by "adm".

**Rule ID:** `SV-260511r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Ubuntu 22.04 LTS configures the "/var/log/syslog" file to be group-owned by "adm" by using the following command: $ stat -c "%n %G" /var/log/syslog /var/log/syslog adm If the "/var/log/syslog" file is not group-owned by "adm", this is a finding.

## Group: SRG-OS-000205-GPOS-00083

**Group ID:** `V-260512`

### Rule: Ubuntu 22.04 LTS must be configured so that the "journalctl" command is not accessible by unauthorized users.

**Rule ID:** `SV-260512r958564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any operating system providing too much information in error messages risks compromising the data and security of the structure, and content of error messages needs to be carefully considered by the organization. Organizations carefully consider the structure/content of error messages. The extent to which information systems are able to identify and handle error conditions is guided by organizational policy and operational requirements. Information that could be exploited by adversaries includes, for example, erroneous logon attempts with passwords entered by mistake as the username, mission/business information that can be derived from (if not stated explicitly by) information recorded, and personal information, such as account numbers, social security numbers, and credit card numbers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "journalctl" command has a permission set of "740" by using the following command: $ sudo find /usr/bin/journalctl -exec stat -c "%n %a" {} \; /usr/bin/journalctl 740 If "journalctl" is not set to "740", this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-260513`

### Rule: Ubuntu 22.04 LTS must set a sticky bit on all public directories to prevent unauthorized and unintended information transferred via shared system resources.

**Rule ID:** `SV-260513r958524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DOD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all public directories have the public sticky bit set by using the following command: $ sudo find / -type d -perm -002 ! -perm -1000 If any public directories are found missing the sticky bit, this is a finding.

## Group: SRG-OS-000297-GPOS-00115

**Group ID:** `V-260514`

### Rule: Ubuntu 22.04 LTS must have an application firewall installed in order to control remote access methods.

**Rule ID:** `SV-260514r958672_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Ubuntu 22.04 LTS functionality (e.g., RDP) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Uncomplicated Firewall is installed by using the following command: $ dpkg -l | grep ufw ii ufw 0.36.1-4ubuntu0.1 all program for managing a Netfilter firewall If the "ufw" package is not installed, ask the system administrator if another application firewall is installed. If no application firewall is installed, this is a finding.

## Group: SRG-OS-000297-GPOS-00115

**Group ID:** `V-260515`

### Rule: Ubuntu 22.04 LTS must enable and run the Uncomplicated Firewall (ufw).

**Rule ID:** `SV-260515r958672_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Ubuntu 22.04 LTS functionality (e.g., RDP) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ufw is enabled on the system with the following command: $ sudo ufw status Status: active If the above command returns the status as "inactive" or any type of error, this is a finding.

## Group: SRG-OS-000480-GPOS-00232

**Group ID:** `V-260516`

### Rule: Ubuntu 22.04 LTS must have an application firewall enabled.

**Rule ID:** `SV-260516r991593_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Firewalls protect computers from network attacks by blocking or limiting access to open network ports. Application firewalls limit which applications are allowed to communicate over the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Uncomplicated Firewall (ufw) is enabled on the system with the following command: $ systemctl status ufw.service | grep -i "active:" Active: active (exited) since Thu 2022-12-25 00:00:01 NZTD; 365 days 11h ago If "ufw.service" is "inactive", this is a finding. If the ufw is not installed, ask the system administrator if another application firewall is installed. If no application firewall is installed, this is a finding.

## Group: SRG-OS-000420-GPOS-00186

**Group ID:** `V-260517`

### Rule: Ubuntu 22.04 LTS must configure the Uncomplicated Firewall (ufw) to rate-limit impacted network interfaces.

**Rule ID:** `SV-260517r958902_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Denial of service (DoS) is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of the operating system to mitigate the impact of DoS attacks that have occurred or are ongoing on system availability. For each system, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or establishing memory partitions). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an application firewall is configured to rate limit any connection to the system. Check all the services listening to the ports by using the following command: $ ss -l46ut Netid State Recv-Q Send-Q Local Address:Port Peer Address:Port Process tcp LISTEN 0 511 *:http *:* tcp LISTEN 0 128 [::]:ssh [::]:* tcp LISTEN 0 128 [::]:ipp [::]:* tcp LISTEN 0 128 [::]:smtp [::]:* For each entry, verify that the ufw is configured to rate limit the service ports by using the following command: $ sudo ufw status Status: active To Action From -- ------ ---- 80/tcp LIMIT Anywhere 25/tcp LIMIT Anywhere Anywhere DENY 240.9.19.81 443 LIMIT Anywhere 22/tcp LIMIT Anywhere 80/tcp (v6) LIMIT Anywhere 25/tcp (v6) LIMIT Anywhere 22/tcp (v6) LIMIT Anywhere (v6) 25 DENY OUT Anywhere 25 (v6) DENY OUT Anywhere (v6) If any port with a state of "LISTEN" that does not have an action of "DENY", is not marked with the "LIMIT" action, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-260518`

### Rule: Ubuntu 22.04 LTS must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-260518r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the operating system must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the firewall configuration for any unnecessary or prohibited functions, ports, protocols, and/or services by using the following command: $ sudo ufw show raw Chain INPUT (policy ACCEPT 0 packets, 0 bytes) pkts bytes target prot opt in out source destination Chain FORWARD (policy ACCEPT 0 packets, 0 bytes) pkts bytes target prot opt in out source destination Chain OUTPUT (policy ACCEPT 0 packets, 0 bytes) pkts bytes target prot opt in out source destination Ask the system administrator for the site or program PPSM CLSA. Verify the services allowed by the firewall match the PPSM CLSA. If there are any additional ports, protocols, or services that are not included in the PPSM CLSA, this is a finding. If there are any ports, protocols, or services that are prohibited by the PPSM CAL, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-260519`

### Rule: Ubuntu 22.04 LTS must, for networked systems, compare internal information system clocks at least every 24 hours with a server synchronized to one of the redundant United States Naval Observatory (USNO) time servers, or a time server designated for the appropriate DOD network (NIPRNet/SIPRNet), and/or the Global Positioning System (GPS).

**Rule ID:** `SV-260519r1038944_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). Note that USNO offers authenticated NTP service to DOD and U.S. Government agencies operating on the NIPR and SIPR networks. Visit https://www.usno.navy.mil/USNO/time/ntp/DOD-customers for more information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS is configured to compare the system clock at least every 24 hours to the authoritative time source by using the following command: Note: If the system is not networked, this requirement is not applicable. $ sudo grep maxpoll -ir /etc/chrony* server tick.usno.navy.mil iburst maxpoll 16 If the "maxpoll" option is set to a number greater than 16, the line is commented out, or is missing, this is a finding. Verify that the "chrony.conf" file is configured to an authoritative DOD time source by using the following command: $ sudo grep -ir server /etc/chrony* server tick.usno.navy.mil iburst maxpoll 16 server tock.usno.navy.mil iburst maxpoll 16 server ntp2.usno.navy.mil iburst maxpoll 16 If "server" is not defined, is not set to an authoritative DOD time source, is commented out, or missing, this is a finding.

## Group: SRG-OS-000356-GPOS-00144

**Group ID:** `V-260520`

### Rule: Ubuntu 22.04 LTS must synchronize internal information system clocks to the authoritative time source when the time difference is greater than one second.

**Rule ID:** `SV-260520r1044776_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider setting time periods for different types of systems (e.g., financial, legal, or mission-critical systems). Organizations should also consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). This requirement is related to the comparison done every 24 hours in SRG-OS-000355 because a comparison must be done to determine the time difference.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS synchronizes internal system clocks to the authoritative time source when the time difference is greater than one second. Note: If the system is not networked, this requirement is not applicable. Check the value of "makestep" by using the following command: $ grep -ir makestep /etc/chrony* makestep 1 -1 If "makestep" is not set to "1 -1", is commented out, or is missing, this is a finding. Verify the NTP service is active and the system clock is synchronized with the authoritative time source: $ timedatectl | grep -Ei '(synchronized|service)' System clock synchronized: yes NTP service: active If the NTP service is not active, this is a finding. If the system clock is not synchronized, this is a finding.

## Group: SRG-OS-000359-GPOS-00146

**Group ID:** `V-260521`

### Rule: Ubuntu 22.04 LTS must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC).

**Rule ID:** `SV-260521r958788_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the operating system include date and time. Time is commonly expressed in UTC or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the time zone is configured to use UTC by using the following command: $ timedatectl status | grep -i "time zone" Time zone: Etc/UTC (UTC, +0000) If "Time zone" is not set to UTC, this is a finding.

## Group: SRG-OS-000142-GPOS-00071

**Group ID:** `V-260522`

### Rule: Ubuntu 22.04 LTS must be configured to use TCP syncookies.

**Rule ID:** `SV-260522r1069097_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Managing excess capacity ensures that sufficient capacity is available to counter flooding attacks. Employing increased capacity and service redundancy may reduce the susceptibility to some DoS attacks. Managing excess capacity may include, for example, establishing selected usage priorities, quotas, or partitioning.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS is configured to use TCP syncookies by using the following command: $ sysctl net.ipv4.tcp_syncookies net.ipv4.tcp_syncookies = 1 If the value is not "1", this is a finding. Check the saved value of TCP syncookies by using the following command: $ sudo grep -ir net.ipv4.tcp_syncookies /etc/sysctl.d/*.conf /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf 2> /dev/null If the "net.ipv4.tcp_syncookies" option is not set to "1", is commented out, or is missing, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-260523`

### Rule: Ubuntu 22.04 LTS must have SSH installed.

**Rule ID:** `SV-260523r958908_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH package is installed by using the following command: $ sudo dpkg -l | grep openssh ii openssh-client 1:8.9p1-3ubuntu0.4 amd64 secure shell (SSH) client, for secure access to remote machines ii openssh-server 1:8.9p1-3ubuntu0.4 amd64 secure shell (SSH) server, for secure access from remote machines ii openssh-sftp-server 1:8.9p1-3ubuntu0.4 amd64 secure shell (SSH) sftp server module, for SFTP access from remote machines If the "openssh" server package is not installed, this is a finding.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-260524`

### Rule: Ubuntu 22.04 LTS must use SSH to protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-260524r958908_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "ssh.service" is enabled and active by using the following commands: $ sudo systemctl is-enabled ssh enabled $ sudo systemctl is-active ssh active If "ssh.service" is not enabled and active, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-260525`

### Rule: Ubuntu 22.04 LTS must display the Standard Mandatory DOD Notice and Consent Banner before granting any local or remote connection to the system.

**Rule ID:** `SV-260525r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read (literal ampersand) consent to terms in IS user agreem't." Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS displays the Standard Mandatory DOD Notice and Consent Banner before granting access to Ubuntu 22.04 LTS via an SSH logon by using the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH 'banner' /etc/ssh/sshd_config:Banner /etc/issue.net The command will return the banner option along with the name of the file that contains the SSH banner. If the line is commented out, missing, or conflicting results are returned, this is a finding. Verify the specified banner file matches the Standard Mandatory DOD Notice and Consent Banner exactly: $ cat /etc/issue.net You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. If the banner text does not match the Standard Mandatory DOD Notice and Consent Banner exactly, this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-260526`

### Rule: Ubuntu 22.04 LTS must not allow unattended or automatic login via SSH.

**Rule ID:** `SV-260526r991591_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Failure to restrict system access to authenticated users negatively impacts Ubuntu 22.04 LTS security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that unattended or automatic login via SSH is disabled by using the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iEH '(permit(.*?)(passwords|environment))' /etc/ssh/sshd_config:PermitEmptyPasswords no /etc/ssh/sshd_config:PermitUserEnvironment no If "PermitEmptyPasswords" and "PermitUserEnvironment" are not set to "no", are commented out, are missing, or conflicting results are returned, this is a finding.

## Group: SRG-OS-000126-GPOS-00066

**Group ID:** `V-260527`

### Rule: Ubuntu 22.04 LTS must be configured so that all network connections associated with SSH traffic terminate after becoming unresponsive.

**Rule ID:** `SV-260527r986275_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an unresponsive SSH session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle SSH session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level and deallocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean the operating system terminates all sessions or network access; it only ends the unresponsive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH server automatically terminates a user session after the SSH client has become unresponsive by using the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH 'clientalivecountmax' /etc/ssh/sshd_config:ClientAliveCountMax 1 If "ClientAliveCountMax" is not to "1", if conflicting results are returned, is commented out, or is missing, this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-260528`

### Rule: Ubuntu 22.04 LTS must be configured so that all network connections associated with SSH traffic are terminated after 10 minutes of becoming unresponsive.

**Rule ID:** `SV-260528r970703_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an unresponsive SSH session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle SSH session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level and deallocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that the operating system terminates all sessions or network access; it only ends the unresponsive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH server automatically terminates a user session after the SSH client has been unresponsive for 10 minutes by using the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH 'clientaliveinterval' /etc/ssh/sshd_config:ClientAliveInterval 600 If "ClientAliveInterval" does not exist, is not set to a value of "600" or less, if conflicting results are returned, is commented out, or is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-260529`

### Rule: Ubuntu 22.04 LTS must be configured so that remote X connections are disabled, unless to fulfill documented and validated mission requirements.

**Rule ID:** `SV-260529r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The security risk of using X11 forwarding is that the client's X11 display server may be exposed to attack when the SSH client requests forwarding. A system administrator may have a stance in which they want to protect clients that may expose themselves to attack by unwittingly requesting X11 forwarding, which can warrant a ''no'' setting. X11 forwarding should be enabled with caution. Users with the ability to bypass file permissions on the remote host (for the user's X11 authorization database) can access the local X11 display through the forwarded connection. An attacker may then be able to perform activities such as keystroke monitoring if the ForwardX11Trusted option is also enabled. If X11 services are not required for the system's intended function, they should be disabled or restricted as appropriate to the system's needs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that X11 forwarding is disabled by using the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH 'x11forwarding' /etc/ssh/sshd_config:X11Forwarding no If "X11Forwarding" is set to "yes" and is not documented with the information system security officer (ISSO) as an operational requirement, is commented out, is missing, or conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-260530`

### Rule: Ubuntu 22.04 LTS SSH daemon must prevent remote hosts from connecting to the proxy display.

**Rule ID:** `SV-260530r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When X11 forwarding is enabled, there may be additional exposure to the server and client displays if the sshd proxy display is configured to listen on the wildcard address. By default, sshd binds the forwarding server to the loopback address and sets the hostname part of the DISPLAY environment variable to localhost. This prevents remote hosts from connecting to the proxy display.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH server prevents remote hosts from connecting to the proxy display by using the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH 'x11uselocalhost' /etc/ssh/sshd_config:X11UseLocalhost yes If "X11UseLocalhost" is set to "no", is commented out, is missing, or conflicting results are returned, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-260531`

### Rule: Ubuntu 22.04 LTS must configure the SSH daemon to use FIPS 140-3-approved ciphers to prevent the unauthorized disclosure of information and/or detect changes to information during transmission.

**Rule ID:** `SV-260531r958408_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. Encrypting information for transmission protects information from unauthorized disclosure and modification. Cryptographic mechanisms implemented to protect information integrity include, for example, cryptographic hash functions which have common application in digital signatures, checksums, and message authentication codes. By specifying a cipher list with the order of ciphers being in a "strongest to weakest" orientation, the system will automatically attempt to use the strongest cipher for securing SSH connections. Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000394-GPOS-00174, SRG-OS-000424-GPOS-00188</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH server is configured to only implement FIPS-approved ciphers with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH 'ciphers' /etc/ssh/sshd_config:Ciphers aes256-ctr,aes256-gcm@openssh.com,aes192-ctr,aes128-ctr,aes128-gcm@openssh.com If "Ciphers" does not contain only the ciphers "aes256-ctr,aes256-gcm@openssh.com,aes192-ctr,aes128-ctr,aes128-gcm@openssh.com" in exact order, is commented out, is missing, or conflicting results are returned, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-260532`

### Rule: Ubuntu 22.04 LTS must configure the SSH daemon to use Message Authentication Codes (MACs) employing FIPS 140-3-approved cryptographic hashes to prevent the unauthorized disclosure of information and/or detect changes to information during transmission.

**Rule ID:** `SV-260532r991554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. Encrypting information for transmission protects information from unauthorized disclosure and modification. Cryptographic mechanisms implemented to protect information integrity include, for example, cryptographic hash functions, which have common application in digital signatures, checksums, and message authentication codes. Satisfies: SRG-OS-000250-GPOS-00093, SRG-OS-000393-GPOS-00173, SRG-OS-000424-GPOS-00188</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH server is configured to only use MACs that employ FIPS 140-3 approved ciphers by using the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH 'macs' /etc/ssh/sshd_config:MACs hmac-sha2-512,hmac-sha2-512-etm@openssh.com,hmac-sha2-256,hmac-sha2-256-etm@openssh.com If "MACs" does not contain only the hashes "hmac-sha2-512,hmac-sha2-512-etm@openssh.com,hmac-sha2-256,hmac-sha2-256-etm@openssh.com" in exact order, is commented out, is missing, or conflicting results are returned, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-260533`

### Rule: Ubuntu 22.04 LTS SSH server must be configured to use only FIPS-validated key exchange algorithms.

**Rule ID:** `SV-260533r958408_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections provided by FIPS-validated cryptographic algorithms, information can be viewed and altered by unauthorized users without detection. The system will attempt to use the first algorithm presented by the client that matches the server list. Listing the values "strongest to weakest" is a method to ensure the use of the strongest algorithm available to secure the SSH connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SSH server is configured to use only FIPS-validated key exchange algorithms by using the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH 'kexalgorithms' /etc/ssh/sshd_config:KexAlgorithms ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256 If "KexAlgorithms" does not contain only the algorithms "ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256" in exact order, is commented out, is missing, or conflicting results are returned, this is a finding.

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-260534`

### Rule: Ubuntu 22.04 LTS must use strong authenticators in establishing nonlocal maintenance and diagnostic sessions.

**Rule ID:** `SV-260534r958510_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. Typically, strong authentication requires authenticators that are resistant to replay attacks and employ multifactor authentication. Strong authenticators include, for example, PKI where certificates are stored on a token protected by a password, passphrase, or biometric.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS is configured to use strong authenticators in the establishment of nonlocal maintenance and diagnostic maintenance by using the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH 'usepam' /etc/ssh/sshd_config:UsePAM yes If "UsePAM" is not set to "yes", is commented out, is missing, or conflicting results are returned, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-260535`

### Rule: Ubuntu 22.04 LTS must enable the graphical user logon banner to display the Standard Mandatory DOD Notice and Consent Banner before granting local access to the system via a graphical user logon.

**Rule ID:** `SV-260535r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to Ubuntu 22.04 LTS ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read (literal ampersand) consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS is configured to display the Standard Mandatory DOD Notice and Consent Banner before granting access to the operating system via a graphical user logon by using the following command: Note: If no graphical user interface is installed, this requirement is not applicable. $ grep -i banner-message-enable /etc/gdm3/greeter.dconf-defaults banner-message-enable=true If the value for "banner-message-enable" is set to "false", the line is commented out, or no value is returned, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-260536`

### Rule: Ubuntu 22.04 LTS must display the Standard Mandatory DOD Notice and Consent Banner before granting local access to the system via a graphical user logon.

**Rule ID:** `SV-260536r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to Ubuntu 22.04 LTS ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read (literal ampersand) consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the operating system via a graphical user logon with the command: Note: If no graphical user interface is installed, this requirement is not applicable. $ grep -i banner-message-text /etc/gdm3/greeter.dconf-defaults banner-message-text="You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only.\n\nBy using this IS (which includes any device attached to this IS), you consent to the following conditions:\n\n-The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations.\n\n-At any time, the USG may inspect and seize data stored on this IS.\n\n-Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose.\n\n-This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy.\n\n-Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the banner-message-text is missing, commented out, or does not match the Standard Mandatory DOD Notice and Consent Banner exactly, this is a finding.

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-260537`

### Rule: Ubuntu 22.04 LTS must retain a user's session lock until that user reestablishes access using established identification and authentication procedures.

**Rule ID:** `SV-260537r1069101_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Regardless of where the session lock is determined and implemented, once invoked, a session lock of Ubuntu 22.04 LTS must remain in place until the user reauthenticates. No other activity aside from reauthentication must unlock the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS has a graphical user interface session lock enabled by using the following command: Note: If no graphical user interface is installed, this requirement is not applicable. $ sudo gsettings get org.gnome.desktop.screensaver lock-enabled true If "lock-enabled" is not set to "true", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-260538`

### Rule: Ubuntu 22.04 LTS must initiate a graphical session lock after 15 minutes of inactivity.

**Rule ID:** `SV-260538r1069119_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Regardless of where the session lock is determined and implemented, once invoked, a session lock of Ubuntu 22.04 LTS must remain in place until the user reauthenticates. No other activity aside from reauthentication must unlock the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS has a graphical user interface session lock configured to activate after 15 minutes of inactivity by using the following commands: Note: If no graphical user interface is installed, this requirement is not applicable. Get the following settings to verify the graphical user interface session is configured to lock the graphical user session after 15 minutes of inactivity: $ gsettings get org.gnome.desktop.screensaver lock-enabled true $ gsettings get org.gnome.desktop.screensaver lock-delay uint32 0 $ gsettings get org.gnome.desktop.session idle-delay uint32 900 If "lock-enabled" is not set to "true", is commented out, or is missing, this is a finding. If "lock-delay" is set to a value greater than "0", or if "idle-delay" is set to a value greater than "900", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-260539`

### Rule: Ubuntu 22.04 LTS must disable the x86 Ctrl-Alt-Delete key sequence if a graphical user interface is installed.

**Rule ID:** `SV-260539r1069103_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A locally logged-on user who presses Ctrl-Alt-Delete, when at the console, can reboot the system. If accidentally pressed, as could happen in the case of a mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot. In the graphical environment, risk of unintentional reboot from the Ctrl-Alt-Delete sequence is reduced because the user will be prompted before any action is taken.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS is not configured to reboot the system when Ctrl-Alt-Delete is pressed when using a graphical user interface by using the following command: Note: If no graphical user interface is installed, this requirement is not applicable. $ gsettings get org.gnome.settings-daemon.plugins.media-keys logout @as [] If the "logout" key is bound to an action, is commented out, or is missing, this is a finding.

## Group: SRG-OS-000378-GPOS-00163

**Group ID:** `V-260540`

### Rule: Ubuntu 22.04 LTS must disable automatic mounting of Universal Serial Bus (USB) mass storage driver.

**Rule ID:** `SV-260540r986276_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Peripherals include, but are not limited to, such devices as flash drives, external storage, and printers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS disables ability to load the USB storage kernel module by using the following command: $ grep usb-storage /etc/modprobe.d/* | grep "/bin/false" /etc/modprobe.d/stig.conf:install usb-storage /bin/false If the command does not return any output, or the line is commented out, this is a finding. Verify Ubuntu 22.04 LTS disables the ability to use USB mass storage device. $ grep usb-storage /etc/modprobe.d/* | grep -i "blacklist" /etc/modprobe.d/stig.conf:blacklist usb-storage If the command does not return any output, or the line is commented out, this is a finding.

## Group: SRG-OS-000481-GPOS-00481

**Group ID:** `V-260541`

### Rule: Ubuntu 22.04 LTS must disable all wireless network adapters.

**Rule ID:** `SV-260541r958358_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of communications with wireless peripherals, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read, altered, or used to compromise the operating system. This requirement applies to wireless peripheral technologies (e.g., wireless mice, keyboards, displays, etc.) used with an operating system. Wireless peripherals (e.g., Wi-Fi/Bluetooth/IR Keyboards, Mice, and Pointing Devices and Near Field Communications [NFC]) present a unique challenge by creating an open, unsecured port on a computer. Wireless peripherals must meet DOD requirements for wireless data transmission and be approved for use by the AO. Even though some wireless peripherals, such as mice and pointing devices, do not ordinarily carry information that need to be protected, modification of communications with these wireless peripherals may be used to compromise the operating system. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of communications with wireless peripherals can be accomplished by physical means (e.g., employing physical barriers to wireless radio frequencies) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. If the wireless peripheral is only passing telemetry data, encryption of the data may not be required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that there are no wireless interfaces configured on the system by using the following command: Note: If the system does not have any physical wireless network radios, this requirement is not applicable. $ cat /proc/net/wireless If any wireless interface names are listed under "Interface" and have not been documented and approved by the information system security officer (ISSO), this is a finding.

## Group: SRG-OS-000109-GPOS-00056

**Group ID:** `V-260542`

### Rule: Ubuntu 22.04 LTS must prevent direct login into the root account.

**Rule ID:** `SV-260542r1015006_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure individual accountability and prevent unauthorized access, organizational users must be individually identified and authenticated. A group authenticator is a generic account used by multiple individuals. Use of a group authenticator alone does not uniquely identify individual users. Examples of the group authenticator is the Unix OS "root" user account, the Windows "Administrator" account, the "sa" account, or a "helpdesk" account. For example, the Unix and Windows operating systems offer a "switch user" capability allowing users to authenticate with their individual credentials and, when needed, "switch" to the administrator role. This method provides for unique individual authentication prior to using a group authenticator. Users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization, which outlines specific user actions that can be performed on the operating system without identification or authentication. Requiring individuals to be authenticated with an individual authenticator prior to using a group authenticator allows for traceability of actions, as well as adding an additional level of protection of the actions that can be taken with group account knowledge.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS prevents direct logins to the root account by using the following command: $ sudo passwd -S root root L 08/09/2022 0 99999 7 -1 If the output does not contain "L" in the second field to indicate the account is locked, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-260543`

### Rule: Ubuntu 22.04 LTS must uniquely identify interactive users.

**Rule ID:** `SV-260543r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1. Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2. Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. Satisfies: SRG-OS-000104-GPOS-00051, SRG-OS-000121-GPOS-00062</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS contains no duplicate User IDs (UIDs) for interactive users by using the following command: $ awk -F ":" 'list[$3]++{print $1, $3}' /etc/passwd If output is produced and the accounts listed are interactive user accounts, this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-260545`

### Rule: Ubuntu 22.04 LTS must enforce 24 hours/one day as the minimum password lifetime. Passwords for new users must have a 24 hours/one day minimum password lifetime restriction.

**Rule ID:** `SV-260545r1015007_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS enforces a 24 hours/one day minimum password lifetime for new user accounts by using the following command: $ grep -i pass_min_days /etc/login.defs PASS_MIN_DAYS 1 If "PASS_MIN_DAYS" is less than "1", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-260546`

### Rule: Ubuntu 22.04 LTS must enforce a 60-day maximum password lifetime restriction. Passwords for new users must have a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-260546r1038967_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If the operating system does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the operating system passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS enforces a 60-day maximum password lifetime for new user accounts by using the following command: $ grep -i pass_max_days /etc/login.defs PASS_MAX_DAYS 60 If "PASS_MAX_DAYS" is less than "60", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000118-GPOS-00060

**Group ID:** `V-260547`

### Rule: Ubuntu 22.04 LTS must disable account identifiers (individuals, groups, roles, and devices) after 35 days of inactivity.

**Rule ID:** `SV-260547r1015009_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. Operating systems need to track periods of inactivity and disable application identifiers after 35 days of inactivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the account identifiers (individuals, groups, roles, and devices) are disabled after 35 days of inactivity by using the following command: Check the account inactivity value by performing the following command: $ grep INACTIVE /etc/default/useradd INACTIVE=35 If "INACTIVE" is set to "-1" or is not set to "35", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000002-GPOS-00002

**Group ID:** `V-260548`

### Rule: Ubuntu 22.04 LTS must automatically expire temporary accounts within 72 hours.

**Rule ID:** `SV-260548r958364_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Temporary accounts are privileged or nonprivileged accounts established during pressing circumstances, such as new software or hardware configuration or an incident response, where the need for prompt account activation requires bypassing normal account authorization procedures. If any inactive temporary accounts are left enabled on the system and are not either manually removed or automatically expired within 72 hours, the security posture of the system will be degraded and exposed to exploitation by unauthorized users or insider threat actors. Temporary accounts are different from emergency accounts. Emergency accounts, also known as "last resort" or "break glass" accounts, are local logon accounts enabled on the system for emergency use by authorized system administrators to manage a system when standard logon methods are failing or not available. Emergency accounts are not subject to manual removal or scheduled expiration requirements. The automatic expiration of temporary accounts may be extended as needed by the circumstances, but it must not be extended indefinitely. A documented permanent account should be established for privileged users who need long-term maintenance accounts. Satisfies: SRG-OS-000002-GPOS-00002, SRG-OS-000123-GPOS-00064</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify temporary accounts have been provisioned with an expiration date of 72 hours by using the following command: $ sudo chage -l <temporary_account_name> | grep -E '(Password|Account) expires' Password expires : Apr 1, 2024 Account expires : Apr 1, 2024 Verify each of these accounts has an expiration date set within 72 hours. If any temporary accounts have no expiration date set or do not expire within 72 hours, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-260549`

### Rule: Ubuntu 22.04 LTS must automatically lock an account until the locked account is released by an administrator when three unsuccessful logon attempts have been made.

**Rule ID:** `SV-260549r958388_rule`
**Severity:** low

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Ubuntu 22.04 LTS utilizes the "pam_faillock" module by using the following command: $ grep faillock /etc/pam.d/common-auth auth [default=die] pam_faillock.so authfail auth sufficient pam_faillock.so authsucc If the "pam_faillock.so" module is not present in the "/etc/pam.d/common-auth" file, this is a finding. Verify the "pam_faillock" module is configured to use the following options: $ sudo grep -Ew 'silent|audit|deny|fail_interval|unlock_time' /etc/security/faillock.conf audit silent deny = 3 fail_interval = 900 unlock_time = 0 If "audit" is commented out, or is missing, this is a finding. If "silent" is commented out, or is missing, this is a finding. If "deny" is set to a value greater than "3", is commented out, or is missing, this is a finding. If "fail_interval" is set to a value greater than "900", is commented out, or is missing, this is a finding. If "unlock_time" is not set to "0", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-260550`

### Rule: Ubuntu 22.04 LTS must enforce a delay of at least four seconds between logon prompts following a failed logon attempt.

**Rule ID:** `SV-260550r991588_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Limiting the number of logon attempts over a certain time interval reduces the chances that an unauthorized user may gain access to an account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS enforces a delay of at least four seconds between logon prompts following a failed logon attempt by using the following command: $ grep pam_faildelay /etc/pam.d/common-auth auth required pam_faildelay.so delay=4000000 If "delay" is not set to "4000000" or greater, the line is commented out, or is missing, this is a finding.

## Group: SRG-OS-000027-GPOS-00008

**Group ID:** `V-260552`

### Rule: Ubuntu 22.04 LTS must limit the number of concurrent sessions to ten for all accounts and/or account types.

**Rule ID:** `SV-260552r958398_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Ubuntu 22.04 LTS management includes the ability to control the number of users and user sessions that utilize an operating system. Limiting the number of allowed users and sessions per user is helpful in reducing the risks related to denial-of-service (DoS) attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS limits the number of concurrent sessions to 10 for all accounts and/or account types by using the following command: $ sudo grep -r -s '^[^#].*maxlogins' /etc/security/limits.conf /etc/security/limits.d/*.conf /etc/security/limits.conf:* hard maxlogins 10 If "maxlogins" does not have a value of "10" or less, is commented out, or is missing, this is a finding.

## Group: SRG-OS-000030-GPOS-00011

**Group ID:** `V-260553`

### Rule: Ubuntu 22.04 LTS must allow users to directly initiate a session lock for all connection types.

**Rule ID:** `SV-260553r1015010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Rather than be forced to wait for a period of time to expire before the user session can be locked, Ubuntu 22.04 LTS need to provide users with the ability to manually invoke a session lock so users may secure their session if they need to temporarily vacate the immediate physical vicinity. Satisfies: SRG-OS-000030-GPOS-00011, SRG-OS-000031-GPOS-00012</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS has the "vlock" package installed by using the following command: $ dpkg -l | grep vlock ii vlock 2.2.2-10 amd64 Virtual Console locking program If "vlock" is not installed, this is a finding.

## Group: SRG-OS-000279-GPOS-00109

**Group ID:** `V-260554`

### Rule: Ubuntu 22.04 LTS must automatically exit interactive command shell user sessions after 15 minutes of inactivity.

**Rule ID:** `SV-260554r958636_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle interactive command shell user session within a short time period reduces the window of opportunity for unauthorized personnel to take control of it when left unattended in a virtual terminal or physical console.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS is configured to automatically exit interactive command shell user sessions after 15 minutes of inactivity or less by using the following command: $ sudo grep -E "\bTMOUT=[0-9]+" /etc/bash.bashrc /etc/profile.d/* /etc/profile.d/99-terminal_tmout.sh:TMOUT=900 If "TMOUT" is not set to "900" or less, is set to "0", is commented out, or missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-260555`

### Rule: Ubuntu 22.04 LTS default filesystem permissions must be defined in such a way that all authenticated users can read and modify only their own files.

**Rule ID:** `SV-260555r991590_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the most restrictive default permissions ensures newly created accounts do not have unnecessary access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS defines default permissions for all authenticated users in such a way that the user can read and modify only their own files by using the following command: $ grep -i '^\s*umask' /etc/login.defs UMASK 077 If the "UMASK" variable is set to "000", this is a finding with the severity raised to a CAT I. If "UMASK" is not set to "077", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000312-GPOS-00124

**Group ID:** `V-260556`

### Rule: Ubuntu 22.04 LTS must have the "apparmor" package installed.

**Rule ID:** `SV-260556r958702_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Control of program execution is a mechanism used to prevent execution of unauthorized programs. Some operating systems may provide a capability that runs counter to the mission or provides users with functionality that exceeds mission requirements. This includes functions and services installed at the operating system level. Some of the programs, installed by default, may be harmful or may not be necessary to support essential organizational operations (e.g., key missions, functions). Removal of executable programs is not always possible; therefore, establishing a method of preventing program execution is critical to maintaining a secure system baseline. Methods for complying with this requirement include restricting execution of programs in certain environments, while preventing execution in other environments; or limiting execution of certain program functionality based on organization-defined criteria (e.g., privileges, subnets, sandboxed environments, or roles). Satisfies: SRG-OS-000312-GPOS-00124, SRG-OS-000368-GPOS-00154, SRG-OS-000370-GPOS-00155</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS has the "apparmor" package installed by using the following command: $ dpkg -l | grep apparmor ii apparmor 3.0.4-2ubuntu2.3 amd64 user-space parser utility for AppArmor If the "apparmor" package is not installed, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-260557`

### Rule: Ubuntu 22.04 LTS must be configured to use AppArmor.

**Rule ID:** `SV-260557r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Control of program execution is a mechanism used to prevent execution of unauthorized programs. Some operating systems may provide a capability that runs counter to the mission or provides users with functionality that exceeds mission requirements. This includes functions and services installed at the operating system level. Some of the programs, installed by default, may be harmful or may not be necessary to support essential organizational operations (e.g., key missions, functions). Removal of executable programs is not always possible; therefore, establishing a method of preventing program execution is critical to maintaining a secure system baseline. Methods for complying with this requirement include restricting execution of programs in certain environments, while preventing execution in other environments; or limiting execution of certain program functionality based on organization-defined criteria (e.g., privileges, subnets, sandboxed environments, or roles). Satisfies: SRG-OS-000368-GPOS-00154, SRG-OS-000370-GPOS-00155, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS AppArmor is active by using the following commands: $ systemctl is-enabled apparmor.service enabled $ systemctl is-active apparmor.service active If "apparmor.service" is not enabled and active, this is a finding. Check if AppArmor profiles are loaded and enforced by using the following command: $ sudo apparmor_status | grep -i profile 32 profiles are loaded. 32 profiles are in enforce mode. 0 profiles are in complain mode. 0 profiles are in kill mode. 0 profiles are in unconfined mode. 2 processes have profiles defined. 0 processes are unconfined but have a profile defined. If no profiles are loaded and enforced, this is a finding.

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-260558`

### Rule: Ubuntu 22.04 LTS must require users to reauthenticate for privilege escalation or when changing roles.

**Rule ID:** `SV-260558r1101733_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the user reauthenticate. Satisfies: SRG-OS-000373-GPOS-00156, SRG-OS-000373-GPOS-00157</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/etc/sudoers" file has no occurrences of "NOPASSWD" or "!authenticate" by using the following command: $ sudo egrep -iR '!authenticate' /etc/sudoers /etc/sudoers.d/ If any occurrences of "NOPASSWD" or "!authenticate" return from the command, this is a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-260559`

### Rule: Ubuntu 22.04 LTS must ensure only users who need access to security functions are part of sudo group.

**Rule ID:** `SV-260559r958518_rule`
**Severity:** high

**Description:**
<VulnDiscussion>An isolation boundary provides access control and protects the integrity of the hardware, software, and firmware that perform security functions. Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Operating systems implement code separation (i.e., separation of security functions from nonsecurity functions) in a number of ways, including through the provision of security kernels via processor rings or processor modes. For nonkernel code, security function isolation is often achieved through file system protections that serve to protect the code on disk and address space protections that protect executing code. Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Implementation may include isolation of memory space and libraries. Ubuntu 22.04 LTS restricts access to security functions through the use of access control mechanisms and by implementing least privilege capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the sudo group has only members who require access to security functions by using the following command: $ grep sudo /etc/group sudo:x:27:<username> If the sudo group contains users not needing access to security functions, this is a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-260560`

### Rule: Ubuntu 22.04 LTS must enforce password complexity by requiring at least one uppercase character be used.

**Rule ID:** `SV-260560r1015012_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS enforces password complexity by requiring at least one uppercase character be used by using the following command: $ grep -i ucredit /etc/security/pwquality.conf ucredit = -1 If "ucredit" is greater than "-1", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000070-GPOS-00038

**Group ID:** `V-260561`

### Rule: Ubuntu 22.04 LTS must enforce password complexity by requiring at least one lowercase character be used.

**Rule ID:** `SV-260561r1015013_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS enforces password complexity by requiring that at least one lowercase character be used by using the following command: $ grep -i lcredit /etc/security/pwquality.conf lcredit = -1 If "lcredit" is greater than "-1", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000071-GPOS-00039

**Group ID:** `V-260562`

### Rule: Ubuntu 22.04 LTS must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-260562r1015014_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS enforces password complexity by requiring that at least one numeric character be used by using the following command: $ grep -i dcredit /etc/security/pwquality.conf dcredit = -1 If "dcredit" is greater than "-1", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000266-GPOS-00101

**Group ID:** `V-260563`

### Rule: Ubuntu 22.04 LTS must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-260563r1015015_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity or strength is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor in determining how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Special characters are those characters that are not alphanumeric. Examples include: ~ ! @ # $ % ^ *.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS enforces password complexity by requiring that at least one special character be used by using the following command: $ grep -i ocredit /etc/security/pwquality.conf ocredit = -1 If "ocredit" is greater than "-1", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-260564`

### Rule: Ubuntu 22.04 LTS must prevent the use of dictionary words for passwords.

**Rule ID:** `SV-260564r991587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Ubuntu 22.04 LTS allows the user to select passwords based on dictionary words, then this increases the chances of password compromise by increasing the opportunity for successful guesses and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS prevents the use of dictionary words for passwords by using the following command: $ grep -i dictcheck /etc/security/pwquality.conf dictcheck = 1 If "dictcheck" is not set to "1", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-260565`

### Rule: Ubuntu 22.04 LTS must enforce a minimum 15-character password length.

**Rule ID:** `SV-260565r1015016_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the pwquality configuration file enforces a minimum 15-character password length by using the following command: $ grep -i minlen /etc/security/pwquality.conf minlen = 15 If "minlen" is not "15" or higher, is commented out, or is missing, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-260566`

### Rule: Ubuntu 22.04 LTS must require the change of at least eight characters when passwords are changed.

**Rule ID:** `SV-260566r1015017_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. If the password length is an odd number then number of changed characters must be rounded up. For example, a password length of 15 characters must require the change of at least eight characters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS requires the change of at least eight characters when passwords are changed by using the following command: $ grep -i difok /etc/security/pwquality.conf difok = 8 If "difok" is less than "8", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-260567`

### Rule: Ubuntu 22.04 LTS must be configured so that when passwords are changed or new passwords are established, pwquality must be used.

**Rule ID:** `SV-260567r991587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. "pwquality" enforces complex password construction configuration and has the ability to limit brute-force attacks on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS enforces password complexity rules by using the following command: $ grep -i enforcing /etc/security/pwquality.conf enforcing = 1 If "enforcing" is not "1", is commented out, or is missing, this is a finding. Check for the use of "pwquality" by using the following command: $ cat /etc/pam.d/common-password | grep requisite | grep pam_pwquality password requisite pam_pwquality.so retry=3 If "retry" is set to "0" or is greater than "3", or is missing, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-260569`

### Rule: Ubuntu 22.04 LTS must store only encrypted representations of passwords.

**Rule ID:** `SV-260569r1101736_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating stores only encrypted representations of passwords with the following command: $ grep pam_unix.so /etc/pam.d/common-password password [success=1 default=ignore] pam_unix.so obscure sha512 shadow rounds=100000 If "sha512" is missing from the "pam_unix.so" line, or if the "rounds" is set to less than 100000, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-260570`

### Rule: Ubuntu 22.04 LTS must not allow accounts configured with blank or null passwords.

**Rule ID:** `SV-260570r1082233_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log on and run commands with the privileges of that account. Accounts with empty passwords must never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that null passwords cannot be used. Run the following command: $ grep nullok /etc/pam.d/common-auth /etc/pam.d/common-password If this produces any output, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-260571`

### Rule: Ubuntu 22.04 LTS must not have accounts configured with blank or null passwords.

**Rule ID:** `SV-260571r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log on and run commands with the privileges of that account. Accounts with empty passwords must never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all accounts on the system to have a password by using the following command: $ sudo awk -F: '!$2 {print $1}' /etc/shadow If the command returns any results, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-260572`

### Rule: Ubuntu 22.04 LTS must encrypt all stored passwords with a FIPS 140-3-approved cryptographic hashing algorithm.

**Rule ID:** `SV-260572r971535_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the shadow password suite configuration is set to encrypt passwords with a FIPS 140-3 approved cryptographic hashing algorithm by using the following command: $ grep -i '^\s*encrypt_method' /etc/login.defs ENCRYPT_METHOD SHA512 If "ENCRYPT_METHOD" does not equal SHA512 or greater, is commented out, or is missing, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-260573`

### Rule: Ubuntu 22.04 LTS must implement multifactor authentication for remote access to privileged accounts in such a way that one of the factors is provided by a device separate from the system gaining access.

**Rule ID:** `SV-260573r1015019_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a CAC or token separate from the information system, ensures that even if the information system is compromised, that compromise will not affect credentials stored on the authentication device. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government personal identity verification card and the DOD common access card. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., VPN, proxy capability). This does not apply to authentication for the purpose of configuring the device itself (management). Satisfies: SRG-OS-000375-GPOS-00160, SRG-OS-000105-GPOS-00052, SRG-OS-000106-GPOS-00053, SRG-OS-000107-GPOS-00054, SRG-OS-000108-GPOS-00055</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS has the packages required for multifactor authentication installed by using the following command: $ dpkg -l | grep libpam-pkcs11 ii libpam-pkcs11 0.6.11-4build2 amd64 Fully featured PAM module for using PKCS#11 smart cards If the "libpam-pkcs11" package is not installed, this is a finding.

## Group: SRG-OS-000376-GPOS-00161

**Group ID:** `V-260574`

### Rule: Ubuntu 22.04 LTS must accept personal identity verification (PIV) credentials.

**Rule ID:** `SV-260574r958816_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. DOD has mandated the use of the common access card (CAC) to support identity management and personal authentication for systems covered under Homeland Security Presidential Directive (HSPD) 12, as well as making the CAC a primary component of layered protection for national security systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "opensc-pcks11" package is installed on the system by using the following command: $ dpkg -l | grep opensc-pkcs11 ii opensc-pkcs11:amd64 0.22.0-1Ubuntu2 amd64 Smart card utilities with support for PKCS#15 compatible cards If the "opensc-pcks11" package is not installed, this is a finding.

## Group: SRG-OS-000105-GPOS-00052

**Group ID:** `V-260575`

### Rule: Ubuntu 22.04 LTS must implement smart card logins for multifactor authentication for local and network access to privileged and nonprivileged accounts.

**Rule ID:** `SV-260575r1044770_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: 1) Something a user knows (e.g., password/PIN); 2) Something a user has (e.g., cryptographic identification device, token); and 3) Something a user is (e.g., biometric). A privileged account is defined as an information system account with authorizations of a privileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the internet). The DOD common access card (CAC) with DOD-approved PKI is an example of multifactor authentication. Satisfies: SRG-OS-000105-GPOS-00052, SRG-OS-000106-GPOS-00053, SRG-OS-000107-GPOS-00054, SRG-OS-000108-GPOS-00055</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "pam_pkcs11.so" module is configured by using the following command: $ grep -i pam_pkcs11.so /etc/pam.d/common-auth auth [success=3 default=ignore] pam_pkcs11.so If "pam_pkcs11.so" is commented out or is missing, this is a finding. Verify the sshd daemon allows public key authentication by using the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH 'pubkeyauthentication' /etc/ssh/sshd_config:PubkeyAuthentication yes If "PubkeyAuthentication" is not set to "yes" or is commented out or missing, or if conflicting results are returned, this is a finding.

## Group: SRG-OS-000377-GPOS-00162

**Group ID:** `V-260576`

### Rule: Ubuntu 22.04 LTS must electronically verify personal identity verification (PIV) credentials.

**Rule ID:** `SV-260576r1069114_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. DOD has mandated the use of the common access card (CAC) to support identity management and personal authentication for systems covered under Homeland Security Presidential Directive (HSPD) 12, as well as making the CAC a primary component of layered protection for national security systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS electronically verifies PIV credentials via certificate status checking by using the following command: $ sudo grep use_pkcs11_module /etc/pam_pkcs11/pam_pkcs11.conf | sudo awk '/pkcs11_module opensc {/,/}/' /etc/pam_pkcs11/pam_pkcs11.conf | grep cert_policy | grep ocsp_on cert_policy = ca,signature,ocsp_on; If every returned "cert_policy" line is not set to "ocsp_on", the line is commented out, or is missing, this is a finding.

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-260577`

### Rule: Ubuntu 22.04 LTS, for PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

**Rule ID:** `SV-260577r1069112_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a certification authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS, for PKI-based authentication, has valid certificates by constructing a certification path to an accepted trust anchor. Determine which pkcs11 module is being used via the "use_pkcs11_module" in "/etc/pam_pkcs11/pam_pkcs11.conf" and then ensure "ca" is enabled in "cert_policy" by using the following command: $ sudo grep use_pkcs11_module /etc/pam_pkcs11/pam_pkcs11.conf | sudo awk '/pkcs11_module opensc {/,/}/' /etc/pam_pkcs11/pam_pkcs11.conf | grep cert_policy | grep ca cert_policy = ca,signature,ocsp_on; If "cert_policy" is not set to "ca", the line is commented out, or is missing, this is a finding.

## Group: SRG-OS-000384-GPOS-00167

**Group ID:** `V-260578`

### Rule: Ubuntu 22.04 LTS for PKI-based authentication, must implement a local cache of revocation data in case of the inability to access revocation information via the network.

**Rule ID:** `SV-260578r1015021_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without configuring a local cache of revocation data, there is the potential to allow access to users who are no longer authorized (users with revoked certificates).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS, for PKI-based authentication, uses local revocation data when unable to access it from the network by using the following command: Note: If smart card authentication is not being used on the system, this is not applicable. $ grep cert_policy /etc/pam_pkcs11/pam_pkcs11.conf | grep -E -- 'crl_auto|crl_offline' cert_policy = ca,signature,ocsp_on,crl_auto; If "cert_policy" is not set to include "crl_auto" or "crl_offline", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000068-GPOS-00036

**Group ID:** `V-260579`

### Rule: Ubuntu 22.04 LTS must map the authenticated identity to the user or group account for PKI-based authentication.

**Rule ID:** `SV-260579r958452_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without mapping the certificate used to authenticate to the user account, the ability to determine the identity of the individual user or group will not be available for forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "use_mappers" is set to "pwent" in "/etc/pam_pkcs11/pam_pkcs11.conf" file by using the following command: $ grep -i use_mappers /etc/pam_pkcs11/pam_pkcs11.conf use_mappers = pwent If "use_mappers" does not contain "pwent", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000403-GPOS-00182

**Group ID:** `V-260580`

### Rule: Ubuntu 22.04 LTS must use DOD PKI-established certificate authorities for verification of the establishment of protected sessions.

**Rule ID:** `SV-260580r958868_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted certificate authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DOD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DOD-approved CA, trust of this CA has not been established. The DOD will only accept PKI-certificates obtained from a DOD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of SSL/TLS certificates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the directory containing the root certificates for Ubuntu 22.04 LTS contains certificate files for DOD PKI-established certificate authorities by iterating over all files in the "/etc/ssl/certs" directory and checking if, at least one, has the subject matching "DOD ROOT CA". $ ls /etc/ssl/certs | grep -i DOD DOD_PKE_CA_chain.pem If no DOD root certificate is found, this is a finding. Verify that all root certificates present on the system have been approved by the AO. $ ls /etc/ssl/certs If a certificate is present that is not approved by the AO, this is a finding.

## Group: SRG-OS-000383-GPOS-00166

**Group ID:** `V-260581`

### Rule: Ubuntu 22.04 LTS must be configured such that Pluggable Authentication Module (PAM) prohibits the use of cached authentications after one day.

**Rule ID:** `SV-260581r958828_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If cached authentication information is out-of-date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that PAM prohibits the use of cached authentications after one day by using the following command: Note: If smart card authentication is not being used on the system, this requirement is not applicable. $ sudo grep -i '^\s*offline_credentials_expiration' /etc/sssd/sssd.conf /etc/sssd/conf.d/*.conf /etc/sssd/sssd.conf:offline_credentials_expiration = 1 If "offline_credentials_expiration" is not set to "1", is commented out, is missing, or conflicting results are returned, this is a finding.

## Group: SRG-OS-000445-GPOS-00199

**Group ID:** `V-260582`

### Rule: Ubuntu 22.04 LTS must use a file integrity tool to verify correct operation of all security functions.

**Rule ID:** `SV-260582r958944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. This requirement applies to Ubuntu 22.04 LTS performing security function verification/testing and/or systems and environments that require this functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Advanced Intrusion Detection Environment (AIDE) is installed by using the following command: $ dpkg -l | grep aide ii aide 0.17.4-1 amd64 Advanced Intrusion Detection Environment - dynamic binary If AIDE is not installed, ask the system administrator how file integrity checks are performed on the system. If there is no application installed to perform integrity checks, this is a finding.

## Group: SRG-OS-000445-GPOS-00199

**Group ID:** `V-260583`

### Rule: Ubuntu 22.04 LTS must configure AIDE to perform file integrity checking on the file system.

**Rule ID:** `SV-260583r1101723_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. This requirement applies to Ubuntu 22.04 LTS performing security function verification/testing and/or systems and environments that require this functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Advanced Intrusion Detection Environment (AIDE) is configured and operating correctly by using the following command (this will take a few minutes): $ sudo aide -c /etc/aide/aide.conf --check Example output: Start timestamp: 2024-04-01 04:20:00 +1300 (AIDE 0.17.4) AIDE found differences between database and filesystem!! Ignored e2fs attributes: EIh ... If AIDE is being used to perform file integrity checks but the command fails, this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-260584`

### Rule: Ubuntu 22.04 LTS must notify designated personnel if baseline configurations are changed in an unauthorized manner. The file integrity tool must notify the system administrator when changes to the baseline configuration or anomalies in the operation of any security functions are discovered.

**Rule ID:** `SV-260584r958794_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to the operating system. Changes to operating system configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of the operating system. The operating system's IMO/ISSO and SAs must be notified via email and/or monitoring system trap when there is an unauthorized modification of a configuration item. Satisfies: SRG-OS-000363-GPOS-00150, SRG-OS-000447-GPOS-00201</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Advanced Intrusion Detection Environment (AIDE) notifies the system administrator when anomalies in the operation of any security functions are discovered by using the following command: $ grep -i '^\s*silentreports' /etc/default/aide SILENTREPORTS=no If "SILENTREPORTS" is set to "yes", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000446-GPOS-00200

**Group ID:** `V-260585`

### Rule: Ubuntu 22.04 LTS must be configured so that the script that runs each 30 days or less to check file integrity is the default.

**Rule ID:** `SV-260585r958946_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. Notifications provided by information systems include, for example, electronic alerts to system administrators, messages to local computer consoles, and/or hardware indications, such as lights. This requirement applies to Ubuntu 22.04 LTS performing security function verification/testing and/or systems and environments that require this functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Advanced Intrusion Detection Environment (AIDE) default script used to check file integrity each 30 days or less is unchanged. Download the original aide-common package in the /tmp directory: $ cd /tmp; apt download aide-common Fetch the SHA1 of the original script file: $ dpkg-deb --fsys-tarfile /tmp/aide-common_*.deb | tar -xO ./usr/share/aide/config/cron.daily/aide | sha1sum b71bb2cafaedf15ec3ac2f566f209d3260a37af0 - Compare with the SHA1 of the file in the daily or monthly cron directory: $ sha1sum /etc/cron.{daily,monthly}/aide 2>/dev/null b71bb2cafaedf15ec3ac2f566f209d3260a37af0 /etc/cron.daily/aide If there is no AIDE script file in the cron directories, or the SHA1 value of at least one file in the daily or monthly cron directory does not match the SHA1 of the original, this is a finding.

## Group: SRG-OS-000278-GPOS-00108

**Group ID:** `V-260586`

### Rule: Ubuntu 22.04 LTS must use cryptographic mechanisms to protect the integrity of audit tools.

**Rule ID:** `SV-260586r1069107_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting the integrity of the tools used for auditing purposes is a critical step toward ensuring the integrity of audit information. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. It is not uncommon for attackers to replace the audit tools or inject code into the existing tools with the purpose of providing the capability to hide or erase system activity from the audit logs. To address this risk, audit tools must be cryptographically signed in order to provide the capability to identify when the audit tools have been modified, manipulated, or replaced. An example is a checksum hash of the file or files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Advanced Intrusion Detection Environment (AIDE) is properly configured to use cryptographic mechanisms to protect the integrity of audit tools by using the following command: $ grep -E '(\/sbin\/(audit|au))' /etc/aide/aide.conf /sbin/auditctl p+i+n+u+g+s+b+acl+xattrs+sha512 /sbin/auditd p+i+n+u+g+s+b+acl+xattrs+sha512 /sbin/ausearch p+i+n+u+g+s+b+acl+xattrs+sha512 /sbin/aureport p+i+n+u+g+s+b+acl+xattrs+sha512 /sbin/autrace p+i+n+u+g+s+b+acl+xattrs+sha512 /sbin/augenrules p+i+n+u+g+s+b+acl+xattrs+sha512 If any of the lines do not appear as shown, are commented out, or are missing, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-260587`

### Rule: Ubuntu 22.04 LTS must have a crontab script running weekly to offload audit events of standalone systems.

**Rule ID:** `SV-260587r959008_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there is a script that offloads audit data and that script runs weekly by using the following command: Note: If the system is not connected to a network, this requirement is not applicable. $ ls /etc/cron.weekly <audit_offload_script_name> Check if the script inside the file does offloading of audit logs to external media. If the script file does not exist or does not offload audit logs, this is a finding.

## Group: SRG-OS-000269-GPOS-00103

**Group ID:** `V-260588`

### Rule: Ubuntu 22.04 LTS must be configured to preserve log records from failure events.

**Rule ID:** `SV-260588r991562_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known state can address safety or security in accordance with the mission/business needs of the organization. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. Preserving operating system state information helps to facilitate operating system restart and return to the operational mode of the organization with least disruption to mission/business processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the log service is installed properly by using the following command: $ dpkg -l | grep rsyslog ii rsyslog 8.2112.0-2ubuntu2.2 amd64 reliable system and kernel logging daemon If the "rsyslog" package is not installed, this is a finding. Check that the log service is enabled and active by using the following commands: $ systemctl is-enabled rsyslog.service enabled $ systemctl is-active rsyslog.service active If "rsyslog.service" is not enabled and active, this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-260589`

### Rule: Ubuntu 22.04 LTS must monitor remote access methods.

**Rule ID:** `SV-260589r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyberattacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Ubuntu 22.04 LTS monitors all remote access methods by using the following command: $ grep -Er '^(auth\.\*,authpriv\.\*|daemon\.\*)' /etc/rsyslog.* /etc/rsyslog.d/50-default.conf:auth.*,authpriv.* /var/log/secure /etc/rsyslog.d/50-default.conf:daemon.* /var/log/messages If "auth.*", "authpriv.*", or "daemon.*" are not configured to be logged in at least one of the config files, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-260590`

### Rule: Ubuntu 22.04 LTS must have the "auditd" package installed.

**Rule ID:** `SV-260590r1015022_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing the when, where, type, source, and outcome of events that occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. Successful incident response and auditing relies on timely, accurate system information and analysis in order to allow the organization to identify and respond to potential incidents in a proficient manner. If the operating system does not provide the ability to centrally review the operating system logs, forensic analysis is negatively impacted. Associating event types with detected events in Ubuntu 22.04 LTS audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured operating system. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00020, SRG-OS-000042-GPOS-00021, SRG-OS-000051-GPOS-00024, SRG-OS-000054-GPOS-00025, SRG-OS-000062-GPOS-00031, SRG-OS-000122-GPOS-00063, SRG-OS-000337-GPOS-00129, SRG-OS-000348-GPOS-00136, SRG-OS-000349-GPOS-00137, SRG-OS-000350-GPOS-00138, SRG-OS-000351-GPOS-00139, SRG-OS-000352-GPOS-00140, SRG-OS-000353-GPOS-00141, SRG-OS-000354-GPOS-00142, SRG-OS-000365-GPOS-00152, SRG-OS-000475-GPOS-00220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "auditd" package is installed by using the following command: $ dpkg -l | grep auditd ii libauditd 1:3.0.7-1build1 amd64 User space tools for security auditing If the "auditd" package is not installed, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-260591`

### Rule: Ubuntu 22.04 LTS must produce audit records and reports containing information to establish when, where, what type, the source, and the outcome for all DOD-defined auditable events and actions in near real time.

**Rule ID:** `SV-260591r1015023_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing the when, where, type, source, and outcome of events that occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. Successful incident response and auditing relies on timely, accurate system information and analysis to allow the organization to identify and respond to potential incidents in a proficient manner. If the operating system does not provide the ability to centrally review the operating system logs, forensic analysis is negatively impacted. Associating event types with detected events in Ubuntu 22.04 LTS audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured operating system. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00020, SRG-OS-000042-GPOS-00021, SRG-OS-000051-GPOS-00024, SRG-OS-000054-GPOS-00025, SRG-OS-000062-GPOS-00031, SRG-OS-000122-GPOS-00063, SRG-OS-000337-GPOS-00129, SRG-OS-000348-GPOS-00136, SRG-OS-000349-GPOS-00137, SRG-OS-000350-GPOS-00138, SRG-OS-000351-GPOS-00139, SRG-OS-000352-GPOS-00140, SRG-OS-000353-GPOS-00141, SRG-OS-000354-GPOS-00142, SRG-OS-000365-GPOS-00152, SRG-OS-000475-GPOS-00220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "auditd.service" is enabled and active by using the following commands: $ systemctl is-enabled auditd.service enabled $ systemctl is-active auditd.service active If the "auditd.service" is not enabled and active, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-260592`

### Rule: Ubuntu 22.04 LTS audit event multiplexor must be configured to offload audit logs onto a different system from the system being audited.

**Rule ID:** `SV-260592r1101709_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. The auditd service does not include the ability to send audit records to a centralized server for management directly. However, it can use a plug-in for audit event multiplexor to pass audit records to a remote server. Satisfies: SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit event multiplexor is configured to offload audit records to a different system from the system being audited. Check if the "audispd-plugins" package is installed: $ dpkg -l | grep audispd-plugins ii audispd-plugins 1:3.0.7-1build1 amd64 Plugins for the audit event dispatcher If the "audispd-plugins" package is not installed, this is a finding. Check that the records are being offloaded to a remote server by using the following command: $ sudo grep -i active /etc/audit/plugins.d/au-remote.conf active = yes If "active" is not set to "yes", or the line is commented out, or is missing, this is a finding. Check that audisp-remote plugin is configured to send audit logs to a different system: $ sudo grep -i remote_server /etc/audit/audisp-remote.conf remote_server = 240.9.19.81 If the "remote_server" parameter is not set, is set with a local IP address, or is set with an invalid IP address, this is a finding.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-260593`

### Rule: Ubuntu 22.04 LTS must alert the information system security officer (ISSO) and system administrator (SA) in the event of an audit processing failure.

**Rule ID:** `SV-260593r958424_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SA and ISSO are notified in the event of an audit processing failure by using the following command: Note: An email package must be installed on the system for email notifications to be sent. $ sudo grep -i action_mail_acct /etc/audit/auditd.conf action_mail_acct = <administrator_email_account> If "action_mail_acct" is not set to the email address of the SA and/or ISSO, is commented out, or is missing, this is a finding.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-260594`

### Rule: Ubuntu 22.04 LTS must shut down by default upon audit failure.

**Rule ID:** `SV-260594r1038966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the operating system is at risk of failing to process audit logs as required, it takes action to mitigate the failure. Audit processing failures include: software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When availability is an overriding concern, other approved actions in response to an audit failure are as follows: 1. If the failure was caused by the lack of audit record storage capacity, the operating system must continue generating audit records if possible (automatically restarting the audit service if necessary), overwriting the oldest audit records in a first-in-first-out manner. 2. If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, the operating system must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS takes the appropriate action when the audit storage volume is full by using the following command: $ sudo grep -i disk_full_action /etc/audit/auditd.conf disk_full_action = HALT If "disk_full_action" is not set to "HALT", "SYSLOG", or "SINGLE", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-260595`

### Rule: Ubuntu 22.04 LTS must allocate audit record storage capacity to store at least one weeks' worth of audit records, when audit records are not immediately sent to a central audit record storage facility.

**Rule ID:** `SV-260595r958752_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To ensure operating systems have a sufficient storage capacity in which to write the audit logs, operating systems must be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial installation of the operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS allocates audit record storage capacity to store at least one week's worth of audit records when audit records are not immediately sent to a central audit record storage facility. Determine which partition the audit records are being written to by using the following command: $ sudo grep -i log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Check the size of the partition that audit records are written to (with the example being "/var/log/audit/") by using the following command: $ sudo df -h /var/log/audit/ /dev/sda2 24G 10.4G 13.6G 43% /var/log/audit If the audit records are not written to a partition made specifically for audit records ("/var/log/audit" as a separate partition), determine the amount of space being used by other files in the partition by using the following command: $ sudo du -sh <audit_partition> 1.8G /var/log/audit Note: The partition size needed to capture a week's worth of audit records is based on the activity level of the system and the total storage capacity available. If the audit record partition is not allocated for sufficient storage capacity, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-260596`

### Rule: Ubuntu 22.04 LTS must immediately notify the system administrator (SA) and information system security officer (ISSO) when the audit record storage volume reaches 25 percent remaining of the allocated capacity.

**Rule ID:** `SV-260596r971542_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches 25 percent remaining of the allocated capacity, they are unable to plan for audit record storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS is configured to notify the SA and ISSO when the audit record storage volume reaches 25 percent remaining of the allocated capacity by using the following command: $ sudo grep -i space_left /etc/audit/auditd.conf space_left = 25% space_left_action = email If "space_left" is set to a value less than "25%", is commented out, or is missing, this is a finding. If "space_left_action" is not set to "email", is commented out, or is missing, this is a finding. Note: If the "space_left_action" is set to "exec", the system executes a designated script. If this script informs the SA of the event, this is not a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-260597`

### Rule: Ubuntu 22.04 LTS must be configured so that audit log files are not read- or write-accessible by unauthorized users.

**Rule ID:** `SV-260597r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the audit log files have a mode of "600" or less permissive. Determine where the audit logs are stored by using the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the path of the directory containing the audit logs, determine if the audit log files have a mode of "600" or less by using the following command: $ sudo stat -c "%n %a" /var/log/audit/* /var/log/audit/audit.log 600 If the audit log files have a mode more permissive than "600", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-260598`

### Rule: Ubuntu 22.04 LTS must be configured to permit only authorized users ownership of the audit log files.

**Rule ID:** `SV-260598r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit log files are owned by "root" account. Determine where the audit logs are stored by using the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the path of the directory containing the audit logs, determine if the audit log files are owned by the "root" user by using the following command: $ sudo stat -c "%n %U" /var/log/audit/* /var/log/audit/audit.log root If the audit log files are owned by a user other than "root", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-260599`

### Rule: Ubuntu 22.04 LTS must permit only authorized groups ownership of the audit log files.

**Rule ID:** `SV-260599r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the group owner of newly created audit logs is "root" by using the following command: $ sudo grep -iw log_group /etc/audit/auditd.conf log_group = root If "log_group" is not set to "root", this is a finding.

## Group: SRG-OS-000059-GPOS-00029

**Group ID:** `V-260600`

### Rule: Ubuntu 22.04 LTS must be configured so that the audit log directory is not write-accessible by unauthorized users.

**Rule ID:** `SV-260600r958438_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit information were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit information, the operating system must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit information system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the audit log directory has a mode of "750" or less permissive. Determine where the audit logs are stored by using the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the path of the directory containing the audit logs, determine if the directory has a mode of "750" or less by using the following command: $ sudo stat -c "%n %a" /var/log/audit /var/log/audit 750 If the audit log directory has a mode more permissive than "750", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-260601`

### Rule: Ubuntu 22.04 LTS must be configured so that audit configuration files are not write-accessible by unauthorized users.

**Rule ID:** `SV-260601r958444_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "/etc/audit/audit.rules", "/etc/audit/auditd.conf", and "/etc/audit/rules.d/*" files have a mode of "640" or less permissive by using the following command: $ sudo ls -al /etc/audit/audit.rules /etc/audit/auditd.conf /etc/audit/rules.d/* | awk '{print $1, $9}' -rw-r----- /etc/audit/audit.rules -rw-r----- /etc/audit/auditd.conf -rw-r----- /etc/audit/rules.d/audit.rules If "/etc/audit/audit.rules", "/etc/audit/auditd.conf", or "/etc/audit/rules.d/*" files have a mode more permissive than "640", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-260602`

### Rule: Ubuntu 22.04 LTS must permit only authorized accounts to own the audit configuration files.

**Rule ID:** `SV-260602r958444_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "/etc/audit/audit.rules", "/etc/audit/auditd.conf", and "/etc/audit/rules.d/*" files are owned by root account by using the following command: $ sudo ls -al /etc/audit/audit.rules /etc/audit/auditd.conf /etc/audit/rules.d/* | awk '{print $3, $9}' root /etc/audit/audit.rules root /etc/audit/auditd.conf root /etc/audit/rules.d/audit.rules If "/etc/audit/audit.rules", "/etc/audit/auditd.conf", or "/etc/audit/rules.d/*" files are owned by a user other than "root", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-260603`

### Rule: Ubuntu 22.04 LTS must permit only authorized groups to own the audit configuration files.

**Rule ID:** `SV-260603r958444_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "/etc/audit/audit.rules", "/etc/audit/auditd.conf", and "/etc/audit/rules.d/*" files are owned by root group by using the following command: $ sudo ls -al /etc/audit/audit.rules /etc/audit/auditd.conf /etc/audit/rules.d/* | awk '{print $4, $9}' root /etc/audit/audit.rules root /etc/audit/auditd.conf root /etc/audit/rules.d/audit.rules If "/etc/audit/audit.rules", "/etc/audit/auditd.conf", or "/etc/audit/rules.d/*" files are owned by a group other than "root", this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260604`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the apparmor_parser command.

**Rule ID:** `SV-260604r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates an audit record upon successful/unsuccessful attempts to use the "apparmor_parser" command by using the following command: $ sudo auditctl -l | grep apparmor_parser -a always,exit -S all -F path=/sbin/apparmor_parser -F perm=x -F auid>=1000 -F auid!=-1 -F key=perm_chng If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260605`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the chacl command.

**Rule ID:** `SV-260605r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates an audit record upon successful/unsuccessful attempts to use the "chacl" command by using the following command: $ sudo auditctl -l | grep chacl -a always,exit -S all -F path=/usr/bin/chacl -F perm=x -F auid>=1000 -F auid!=-1 -F key=perm_chng If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260606`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the chage command.

**Rule ID:** `SV-260606r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "chage" command by using the following command: $ sudo auditctl -l | grep -w chage -a always,exit -S all -F path=/usr/bin/chage -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-chage If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260607`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the chcon command.

**Rule ID:** `SV-260607r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates an audit record upon successful/unsuccessful attempts to use the "chcon" command by using the following command: $ sudo auditctl -l | grep chcon -a always,exit -S all -F path=/usr/bin/chcon -F perm=x -F auid>=1000 -F auid!=-1 -F key=perm_chng If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260608`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the chfn command.

**Rule ID:** `SV-260608r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates audit records upon successful/unsuccessful attempts to use the "chfn" command by using the following command: $ sudo auditctl -l | grep /usr/bin/chfn -a always,exit -S all -F path=/usr/bin/chfn -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-chfn If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260609`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the chsh command.

**Rule ID:** `SV-260609r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates an audit record upon successful/unsuccessful attempts to use the "chsh" command by using the following command: $ sudo auditctl -l | grep chsh -a always,exit -S all -F path=/usr/bin/chsh -F perm=x -F auid>=1000 -F auid!=-1 -F key=priv_cmd If the command does not return a line that matches the example or the line is commented out, this is a finding. Notes: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260610`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the crontab command.

**Rule ID:** `SV-260610r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "crontab" command by using the following command: $ sudo auditctl -l | grep -w crontab -a always,exit -S all -F path=/usr/bin/crontab -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-crontab If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-260611`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful attempts to use the fdisk command.

**Rule ID:** `SV-260611r991586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS is configured to audit the execution of the partition management program "fdisk" by using the following command: $ sudo auditctl -l | grep fdisk -w /usr/sbin/fdisk -p x -k fdisk If the command does not return a line, or the line is commented out, this is a finding. Note: The "-k" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260612`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the gpasswd command.

**Rule ID:** `SV-260612r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "gpasswd" command by using the following command: $ sudo auditctl -l | grep -w gpasswd -a always,exit -S all -F path=/usr/bin/gpasswd -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-gpasswd If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-260613`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful attempts to use the kmod command.

**Rule ID:** `SV-260613r991586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS is configured to audit the execution of the module management program "kmod" by using the following command: $ sudo auditctl -l | grep kmod -w /bin/kmod -p x -k module If the command does not return a line, or the line is commented out, this is a finding. Note: The "-k" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-260614`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful attempts to use modprobe command.

**Rule ID:** `SV-260614r991586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if Ubuntu 22.04 LTS is configured to audit the execution of the module management program "modprobe" with the following command: $ sudo auditctl -l | grep /sbin/modprobe -w /sbin/modprobe -p x -k modules If the command does not return a line, or the line is commented out, this is a finding. Note: The "-k" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260615`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the mount command.

**Rule ID:** `SV-260615r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates audit records upon successful/unsuccessful attempts to use the "mount" command by using the following command: $ sudo auditctl -l | grep /usr/bin/mount -a always,exit -S all -F path=/usr/bin/mount -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-mount If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260616`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the newgrp command.

**Rule ID:** `SV-260616r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates an audit record upon successful/unsuccessful attempts to use the "newgrp" command by using the following command: $ sudo auditctl -l | grep newgrp -a always,exit -S all -F path=/usr/bin/newgrp -F perm=x -F auid>=1000 -F auid!=-1 -F key=priv_cmd If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260617`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the pam_timestamp_check command.

**Rule ID:** `SV-260617r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "pam_timestamp_check" command by using the following command: $ sudo auditctl -l | grep -w pam_timestamp_check -a always,exit -S all -F path=/usr/sbin/pam_timestamp_check -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-pam_timestamp_check If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260618`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the passwd command.

**Rule ID:** `SV-260618r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "passwd" command by using the following command: $ sudo auditctl -l | grep -w passwd -a always,exit -S all -F path=/usr/bin/passwd -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-passwd If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260619`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the setfacl command.

**Rule ID:** `SV-260619r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates an audit record upon successful/unsuccessful attempts to use the "setfacl" command by using the following command: $ sudo auditctl -l | grep setfacl -a always,exit -S all -F path=/usr/bin/setfacl -F perm=x -F auid>=1000 -F auid!=-1 -F key=perm_chng If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260620`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the ssh-agent command.

**Rule ID:** `SV-260620r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates an audit record upon successful/unsuccessful attempts to use the "ssh-agent" command by using the following command: $ sudo auditctl -l | grep /usr/bin/ssh-agent -a always,exit -S all -F path=/usr/bin/ssh-agent -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-ssh If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260621`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the ssh-keysign command.

**Rule ID:** `SV-260621r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates an audit record upon successful/unsuccessful attempts to use the "ssh-keysign" command by using the following command: $ sudo auditctl -l | grep ssh-keysign -a always,exit -S all -F path=/usr/lib/openssh/ssh-keysign -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-ssh If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260622`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the su command.

**Rule ID:** `SV-260622r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates audit records upon successful/unsuccessful attempts to use the "su" command by using the following command: $ sudo auditctl -l | grep /bin/su -a always,exit -S all -F path=/bin/su -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-priv_change If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260623`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the sudo command.

**Rule ID:** `SV-260623r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "sudo" command by using the following command: $ sudo auditctl -l | grep /usr/bin/sudo -a always,exit -S all -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -F auid!=-1 -F key=priv_cmd If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260624`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the sudoedit command.

**Rule ID:** `SV-260624r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates an audit record upon successful/unsuccessful attempts to use the "sudoedit" command by using the following command: $ sudo auditctl -l | grep /usr/bin/sudoedit -a always,exit -S all -F path=/usr/bin/sudoedit -F perm=x -F auid>=1000 -F auid!=-1 -F key=priv_cmd If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260625`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the umount command.

**Rule ID:** `SV-260625r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if Ubuntu 22.04 LTS generates audit records upon successful/unsuccessful attempts to use the "umount" command by using the following command: $ sudo auditctl -l | grep /usr/bin/umount -a always,exit -S all -F path=/usr/bin/umount -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-umount If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260626`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the unix_update command.

**Rule ID:** `SV-260626r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "unix_update" command by using the following command: $ sudo auditctl -l | grep -w unix_update -a always,exit -S all -F path=/sbin/unix_update -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-unix-update If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260627`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the usermod command.

**Rule ID:** `SV-260627r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "usermod" command by using the following command: $ sudo auditctl -l | grep -w usermod -a always,exit -S all -F path=/usr/sbin/usermod -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-usermod If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-260628`

### Rule: Ubuntu 22.04 LTS must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/group.

**Rule ID:** `SV-260628r958368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create an account. Auditing account creation actions provides logging that can be used for forensic purposes. To address access requirements, many operating systems may be integrated with enterprise level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/group" by using the following command: $ sudo auditctl -l | grep group -w /etc/group -p wa -k usergroup_modification If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "-k" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-260629`

### Rule: Ubuntu 22.04 LTS must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/gshadow.

**Rule ID:** `SV-260629r958368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create an account. Auditing account creation actions provides logging that can be used for forensic purposes. To address access requirements, many operating systems may be integrated with enterprise level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/gshadow" by using the following command: $ sudo auditctl -l | grep gshadow -w /etc/gshadow -p wa -k usergroup_modification If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "-k" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-260630`

### Rule: Ubuntu 22.04 LTS must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/opasswd.

**Rule ID:** `SV-260630r958368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create an account. Auditing account creation actions provides logging that can be used for forensic purposes. To address access requirements, many operating systems may be integrated with enterprise level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/security/opasswd" by using the following command: $ sudo auditctl -l | grep opasswd -w /etc/security/opasswd -p wa -k usergroup_modification If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "-k" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-260631`

### Rule: Ubuntu 22.04 LTS must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/passwd.

**Rule ID:** `SV-260631r958368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create an account. Auditing account creation actions provides logging that can be used for forensic purposes. To address access requirements, many operating systems may be integrated with enterprise level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/passwd" by using the following command: $ sudo auditctl -l | grep passwd -w /etc/passwd -p wa -k usergroup_modification If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "-k" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-260632`

### Rule: Ubuntu 22.04 LTS must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/shadow.

**Rule ID:** `SV-260632r958368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create an account. Auditing account creation actions provides logging that can be used for forensic purposes. To address access requirements, many operating systems may be integrated with enterprise level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/shadow" by using the following command: $ sudo auditctl -l | grep shadow -w /etc/shadow -p wa -k usergroup_modification If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "-k" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260633`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the chmod, fchmod, and fchmodat system calls.

**Rule ID:** `SV-260633r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall that all programs on the system makes. Therefore, it is very important to only use syscall rules when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, though, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates an audit record upon successful/unsuccessful attempts to use the "chmod", "fchmod", and "fchmodat" system calls by using the following command: $ sudo auditctl -l | grep chmod -a always,exit -F arch=b32 -S chmod,fchmod,fchmodat -F auid>=1000 -F auid!=-1 -F key=perm_chng -a always,exit -F arch=b64 -S chmod,fchmod,fchmodat -F auid>=1000 -F auid!=-1 -F key=perm_chng If the command does not return audit rules for the "chmod", "fchmod" and "fchmodat" syscalls or the lines are commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260634`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the chown, fchown, fchownat, and lchown system calls.

**Rule ID:** `SV-260634r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall that all programs on the system makes. Therefore, it is very important to only use syscall rules when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, though, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates an audit record upon successful/unsuccessful attempts to use the "chown", "fchown", "fchownat", and "lchown" system calls by using the following command: $ sudo auditctl -l | grep chown -a always,exit -F arch=b32 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=-1 -F key=perm_chng -a always,exit -F arch=b64 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=-1 -F key=perm_chng If the command does not return audit rules for the "chown", "fchown", "fchownat", and "lchown" syscalls or the lines are commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260635`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the creat, open, openat, open_by_handle_at, truncate, and ftruncate system calls.

**Rule ID:** `SV-260635r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall that all programs on the system makes. Therefore, it is very important to only use syscall rules when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, though, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000474-GPOS-00219</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates an audit record upon unsuccessful attempts to use the "creat", "open", "openat", "open_by_handle_at", "truncate", and "ftruncate" system calls by using the following command: $ sudo auditctl -l | grep 'open\|truncate\|creat' -a always,exit -F arch=b32 -S creat,open,openat,open_by_handle_at,truncate,ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=-1 -F key=perm_access -a always,exit -F arch=b32 -S creat,open,openat,open_by_handle_at,truncate,ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=-1 -F key=perm_access -a always,exit -F arch=b64 -S creat,open,openat,open_by_handle_at,truncate,ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=-1 -F key=perm_access -a always,exit -F arch=b64 -S creat,open,openat,open_by_handle_at,truncate,ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=-1 -F key=perm_access If the command does not return audit rules for the "creat", "open", "openat", "open_by_handle_at", "truncate", and "ftruncate" syscalls or the lines are commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260636`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the delete_module system call.

**Rule ID:** `SV-260636r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000477-GPOS-00222</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates an audit record for any successful/unsuccessful attempts to use the "delete_module" syscall by using the following command: $ sudo auditctl -l | grep -w delete_module -a always,exit -F arch=b32 -S delete_module -F auid>=1000 -F auid!=-1 -F key=module_chng -a always,exit -F arch=b64 -S delete_module -F auid>=1000 -F auid!=-1 -F key=module_chng If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260637`

### Rule: Ubuntu 22.04 LTS must generate audit records for successful/unsuccessful uses of the init_module and finit_module system calls.

**Rule ID:** `SV-260637r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall that all programs on the system makes. Therefore, it is very important to only use syscall rules when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, though, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000471-GPOS-00216</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates an audit record for any successful/unsuccessful attempts to use the "init_module" and "finit_module" syscalls by using the following command: $ sudo auditctl -l | grep init_module -a always,exit -F arch=b32 -S init_module,finit_module -F auid>=1000 -F auid!=-1 -F key=module_chng -a always,exit -F arch=b64 -S init_module,finit_module -F auid>=1000 -F auid!=-1 -F key=module_chng If the command does not return audit rules for the "init_module" and "finit_module" syscalls or the lines are commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260638`

### Rule: Ubuntu 22.04 LTS must generate audit records for any use of the setxattr, fsetxattr, lsetxattr, removexattr, fremovexattr, and lremovexattr system calls.

**Rule ID:** `SV-260638r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall that all programs on the system makes. Therefore, it is very important to only use syscall rules when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, though, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates an audit record upon successful/unsuccessful attempts to use the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr" system calls by using the following command: $ sudo auditctl -l | grep xattr -a always,exit -F arch=b32 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=-1 -F key=perm_mod -a always,exit -F arch=b32 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid=0 -k perm_mod -a always,exit -F arch=b64 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=-1 -F key=perm_mod -a always,exit -F arch=b64 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid=0 -k perm_mod If the command does not return audit rules for the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr" and "lremovexattr" syscalls or the lines are commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000468-GPOS-00212

**Group ID:** `V-260639`

### Rule: Ubuntu 22.04 LTS must generate audit records for any successful/unsuccessful use of unlink, unlinkat, rename, renameat, and rmdir system calls.

**Rule ID:** `SV-260639r991577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall that all programs on the system makes. Therefore, it is very important to only use syscall rules when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, though, by combining syscalls into one rule whenever possible.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates audit records for any successful/unsuccessful use of "unlink", "unlinkat", "rename", "renameat", and "rmdir" system calls by using the following command: $ sudo auditctl -l | grep 'unlink\|rename\|rmdir' -a always,exit -F arch=b64 -S unlink,unlinkat,rename,renameat,rmdir -F auid>=1000 -F auid!=-1 -F key=delete -a always,exit -F arch=b32 -S unlink,unlinkat,rename,renameat,rmdir -F auid>=1000 -F auid!=-1 -F key=delete If the command does not return audit rules for the "unlink", "unlinkat", "rename", "renameat", and "rmdir" syscalls or the lines are commented out, this is a finding. Note: The "key" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-260640`

### Rule: Ubuntu 22.04 LTS must generate audit records for all events that affect the systemd journal files.

**Rule ID:** `SV-260640r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to modify system level binaries and their operation. Auditing the systemd journal files provides logging that can be used for forensic purposes. To address access requirements, many operating systems may be integrated with enterprise level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates audit records for all events that affect "/var/log/journal" by using the following command: $ sudo auditctl -l | grep journal -w /var/log/journal -p wa -k systemd_journal If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "-k" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000472-GPOS-00217

**Group ID:** `V-260641`

### Rule: Ubuntu 22.04 LTS must generate audit records for the /var/log/btmp file.

**Rule ID:** `SV-260641r991581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates audit records showing start and stop times for user access to the system via the "/var/log/btmp" file by using the following command: $ sudo auditctl -l | grep '/var/log/btmp' -w /var/log/btmp -p wa -k logins If the command does not return a line matching the example or the line is commented out, this is a finding. Note: The "-k" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000472-GPOS-00217

**Group ID:** `V-260642`

### Rule: Ubuntu 22.04 LTS must generate audit records for the /var/log/wtmp file.

**Rule ID:** `SV-260642r991581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates audit records showing start and stop times for user access to the system via the "/var/log/wtmp" file by using the following command: $ sudo auditctl -l | grep '/var/log/wtmp' -w /var/log/wtmp -p wa -k logins If the command does not return a line matching the example or the line is commented out, this is a finding. Note: The "-k" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000472-GPOS-00217

**Group ID:** `V-260643`

### Rule: Ubuntu 22.04 LTS must generate audit records for the /var/run/utmp file.

**Rule ID:** `SV-260643r991581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates audit records showing start and stop times for user access to the system via the "/var/run/utmp" file by using the following command: $ sudo auditctl -l | grep '/var/run/utmp' -w /var/run/utmp -p wa -k logins If the command does not return a line matching the example or the line is commented out, this is a finding. Note: The "-k" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260644`

### Rule: Ubuntu 22.04 LTS must generate audit records for the use and modification of faillog file.

**Rule ID:** `SV-260644r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000470-GPOS-00214, SRG-OS-000473-GPOS-00218</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates an audit record upon successful/unsuccessful modifications to the "faillog" file by using the following command: $ sudo auditctl -l | grep faillog -w /var/log/faillog -p wa -k logins If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "-k" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-260645`

### Rule: Ubuntu 22.04 LTS must generate audit records for the use and modification of the lastlog file.

**Rule ID:** `SV-260645r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000470-GPOS-00214, SRG-OS-000473-GPOS-00218</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates an audit record when successful/unsuccessful modifications to the "lastlog" file occur by using the following command: $ sudo auditctl -l | grep lastlog -w /var/log/lastlog -p wa -k logins If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "-k" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000466-GPOS-00210

**Group ID:** `V-260646`

### Rule: Ubuntu 22.04 LTS must generate audit records when successful/unsuccessful attempts to modify the /etc/sudoers file occur.

**Rule ID:** `SV-260646r991575_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates audit records for all modifications that affect "/etc/sudoers" by using the following command: $ sudo auditctl -l | grep sudoers -w /etc/sudoers -p wa -k privilege_modification If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "-k" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000466-GPOS-00210

**Group ID:** `V-260647`

### Rule: Ubuntu 22.04 LTS must generate audit records when successful/unsuccessful attempts to modify the /etc/sudoers.d directory occur.

**Rule ID:** `SV-260647r991575_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS generates audit records for all modifications that affect "/etc/sudoers.d" directory by using the following command: $ sudo auditctl -l | grep sudoers.d -w /etc/sudoers.d -p wa -k privilege_modification If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "-k" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000326-GPOS-00126

**Group ID:** `V-260648`

### Rule: Ubuntu 22.04 LTS must prevent all software from executing at higher privilege levels than users executing the software and the audit system must be configured to audit the execution of privileged functions.

**Rule ID:** `SV-260648r958730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, software applications/programs need to execute with elevated privileges to perform required functions. However, if the privileges required for execution are at a higher level than the privileges assigned to organizational users invoking such applications/programs, those users are indirectly provided with greater privileges than assigned by the organizations. Some programs and processes are required to operate at a higher privilege level and therefore should be excluded from the organization-defined software list after review. Satisfies: SRG-OS-000326-GPOS-00126, SRG-OS-000327-GPOS-00127</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS audits the execution of privilege functions by auditing the "execve" system call by using the following command: $ sudo auditctl -l | grep execve -a always,exit -F arch=b64 -S execve -C uid!=euid -F euid=0 -F key=execpriv -a always,exit -F arch=b64 -S execve -C gid!=egid -F egid=0 -F key=execpriv -a always,exit -F arch=b32 -S execve -C uid!=euid -F euid=0 -F key=execpriv -a always,exit -F arch=b32 -S execve -C gid!=egid -F egid=0 -F key=execpriv If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000392-GPOS-00172

**Group ID:** `V-260649`

### Rule: Ubuntu 22.04 LTS must generate audit records for privileged activities, nonlocal maintenance, diagnostic sessions and other system-level access.

**Rule ID:** `SV-260649r986298_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If events associated with nonlocal administrative access or diagnostic sessions are not logged, a major tool for assessing and investigating attacks would not be available. This requirement addresses auditing-related issues associated with maintenance tools used specifically for diagnostic and repair actions on organizational information systems. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. This requirement applies to hardware/software diagnostic test equipment or tools. This requirement does not cover hardware/software components that may support information system maintenance, yet are a part of the system, for example, the software implementing "ping," "ls," "ipconfig," or the hardware and software implementing the monitoring port of an Ethernet switch. Satisfies: SRG-OS-000392-GPOS-00172, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS audits activities performed during nonlocal maintenance and diagnostic sessions by using the following command: $ sudo auditctl -l | grep sudo.log -w /var/log/sudo.log -p wa -k maintenance If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The "-k" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000396-GPOS-00176

**Group ID:** `V-260650`

### Rule: Ubuntu 22.04 LTS must implement NIST FIPS-validated cryptography to protect classified information and for the following: To provision digital signatures, to generate cryptographic hashes, and to protect unclassified information requiring confidentiality and cryptographic protection in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.

**Rule ID:** `SV-260650r987791_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The operating system must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. Satisfies: SRG-OS-000396-GPOS-00176, SRG-OS-000478-GPOS-00223</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system is configured to run in FIPS mode by using the following command: $ grep -i 1 /proc/sys/crypto/fips_enabled 1 If a value of "1" is not returned, this is a finding.

## Group: SRG-OS-000396-GPOS-00176

**Group ID:** `V-274860`

### Rule: The operating system must require users to provide a password for privilege escalation.

**Rule ID:** `SV-274860r1107272_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical that the user reauthenticate. Satisfies: SRG-OS-000373-GPOS-00156, SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00158</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "/etc/sudoers" has no occurrences of "NOPASSWD" with the following command: $ sudo egrep -iR 'NOPASSWD' /etc/sudoers /etc/sudoers.d/ If any occurrences of "NOPASSWD" are returned from the command and have not been documented with the information system security officer (ISSO) as an organizationally defined administrative group using multifactor authentication (MFA), this is a finding.

## Group: SRG-OS-000396-GPOS-00176

**Group ID:** `V-274861`

### Rule: The operating system must restrict privilege elevation to authorized personnel.

**Rule ID:** `SV-274861r1101704_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the "sudoers" file is not configured correctly, any user defined on the system can initiate privileged actions on the target system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system restricts privilege elevation to authorized personnel with the following command: $ sudo grep -iwR 'ALL' /etc/sudoers /etc/sudoers.d/ | grep -v '#' If the either of the following entries are returned, this is a finding: ALL ALL=(ALL) ALL ALL ALL=(ALL:ALL) ALL

## Group: SRG-OS-000396-GPOS-00176

**Group ID:** `V-274862`

### Rule: Ubuntu 22.04 LTS must audit any script or executable called by cron as root or by any privileged user.

**Rule ID:** `SV-274862r1107273_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any script or executable called by cron as root or by any privileged user must be owned by that user, must have the permissions 755 or more restrictive, and should have no extended rights that allow any nonprivileged user to modify the script or executable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Ubuntu 22.04 LTS is configured to audit the execution of any system call made by cron as root or as any privileged user. $ sudo auditctl -l | grep /etc/cron.d -w /etc/cron.d -p wa -k cronjobs $ sudo auditctl -l | grep /var/spool/cron -w /var/spool/cron -p wa -k cronjobs If either of these commands do not return the expected output, or the lines are commented out, this is a finding.

## Group: SRG-OS-000396-GPOS-00176

**Group ID:** `V-274863`

### Rule: Ubuntu 22.04 LTS must be configured such that Pluggable Authentication Module (PAM) prohibits the use of cached authentications after one day.

**Rule ID:** `SV-274863r1107271_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If cached authentication information is out of date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If smart card authentication is not being used on the system, this is not applicable. Verify that PAM prohibits the use of cached authentications after one day with the following command: $ sudo grep offline_credentials_expiration /etc/sssd/sssd.conf /etc/sssd/conf.d/*.conf offline_credentials_expiration = 1 If "offline_credentials_expiration" is not set to a value of "1" in "/etc/sssd/sssd.conf" or in a file with a name ending in .conf in the "/etc/sssd/conf.d/" directory, this is a finding.

## Group: SRG-OS-000396-GPOS-00176

**Group ID:** `V-274864`

### Rule: Ubuntu 22.04 LTS must have the "SSSD" package installed.

**Rule ID:** `SV-274864r1107268_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: 1) Something a user knows (e.g., password/PIN); 2) Something a user has (e.g., cryptographic identification device, token); and 3) Something a user is (e.g., biometric). A privileged account is defined as an information system account with authorizations of a privileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the internet). The DOD common access card (CAC) with DOD-approved PKI is an example of multifactor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS has the packages required for multifactor authentication installed with the following command: $ dpkg -l | grep sssd ii sssd 2.9.4-1.1ubuntu6.1 amd64 System Security Services Daemon -- metapackage ii sssd-ad 2.9.4-1.1ubuntu6.1 amd64 System Security Services Daemon -- Active Directory back end ii sssd-ad-common 2.9.4-1.1ubuntu6.1 amd64 System Security Services Daemon -- PAC responder ii sssd-common 2.9.4-1.1ubuntu6.1 amd64 System Security Services Daemon -- common files ii sssd-ipa 2.9.4-1.1ubuntu6.1 amd64 System Security Services Daemon -- IPA back end ii sssd-krb5 2.9.4-1.1ubuntu6.1 amd64 System Security Services Daemon -- Kerberos back end ii sssd-krb5-common 2.9.4-1.1ubuntu6.1 amd64 System Security Services Daemon -- Kerberos helpers ii sssd-ldap 2.9.4-1.1ubuntu6.1 amd64 System Security Services Daemon -- LDAP back end ii sssd-proxy 2.9.4-1.1ubuntu6.1 amd64 System Security Services Daemon -- proxy back end If the "sssd" package is not installed, this is a finding. The additional sssd components listed by the command may differ from configuration to configuration. Verify that "libpam-sss" (the PAM integration module for SSSD) is installed with the following command: $ dpkg -l | grep libpam-sss i libpam-sss:amd64 2.9.4-1.1ubuntu6.1 amd64 Pam module for the System Security Services Daemon Verify that "libnss-sss" (the NSS module for retrieving user and group information) is installed with the following command: $ dpkg -l | grep libnss-sss ii libnss-sss:amd64 2.9.4-1.1ubuntu6.1 amd64 Nss library for the System Security Services Daemon

## Group: SRG-OS-000396-GPOS-00176

**Group ID:** `V-274865`

### Rule: Ubuntu 22.04 LTS must map the authenticated identity to the user or group account for PKI-based authentication.

**Rule ID:** `SV-274865r1101731_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without mapping the certificate used to authenticate to the user account, the ability to determine the identity of the individual user or group will not be available for forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that authenticated certificates are mapped to the appropriate user group in the "/etc/sssd/sssd.conf" file with the following command: $ grep -i ldap_user_certificate /etc/sssd/sssd.conf ldap_user_certificate=userCertificate;binary

## Group: SRG-OS-000396-GPOS-00176

**Group ID:** `V-274866`

### Rule: Ubuntu 22.04 LTS must use the "SSSD" package for multifactor authentication services.

**Rule ID:** `SV-274866r1101739_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: 1) Something a user knows (e.g., password/PIN); 2) Something a user has (e.g., cryptographic identification device, token); and 3) Something a user is (e.g., biometric). A privileged account is defined as an information system account with authorizations of a privileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the internet). The DOD common access card (CAC) with DOD-approved PKI is an example of multifactor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "sssd.service" is enabled and active with the following commands: $ sudo systemctl is-enabled sssd enabled $ sudo systemctl is-active sssd active If "sssd.service" is not active or enabled, this is a finding.

## Group: SRG-OS-000396-GPOS-00176

**Group ID:** `V-274867`

### Rule: Ubuntu 22.04 LTS must ensure SSSD performs certificate path validation, including revocation checking, against a trusted anchor for PKI-based authentication.

**Rule ID:** `SV-274867r1107270_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a certification authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Ubuntu 22.04 LTS, for PKI-based authentication, has valid certificates by constructing a certification path to an accepted trust anchor. Verify the pam service is listed under [sssd] with the following command: $ sudo grep -A 1 '^\[sssd\]' /etc/sssd/sssd.conf [sssd] services = nss,pam,ssh If "pam" is not listed in services, this is a finding. Verify the pam service is set to use pam for smart card authentication in the [pam] section of /etc/sssd/sssd.conf with the following command: $ sudo grep -A 1 '^\[pam]' /etc/sssd/sssd.conf [pam] pam_cert_auth = True If "pam_cert_auth = True" is not returned, this is a finding. Verify "ca" is enabled in "certificate_verification" with the following command: $ sudo grep certificate_verification /etc/sssd/sssd.conf certificate_verification = ca_cert,ocsp If "certificate_verification" is not set to "ca" or the line is commented out, this is a finding.

