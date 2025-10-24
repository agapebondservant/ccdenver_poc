# STIG Benchmark: SUSE Linux Enterprise Micro (SLEM) 5 Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261263`

### Rule: SLEM 5 must be a vendor-supported release.

**Rule ID:** `SV-261263r996826_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A SLEM 5 release is considered supported if the vendor continues to provide security patches for the product. With an unsupported release, it will not be possible to resolve security issues discovered in the system software.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the version of SLEM 5 is vendor supported with the following command: > cat /etc/os-release NAME="SLE Micro" VERSION="5.2" ... If the installed version of SLEM 5 is not supported, this is a finding.

## Group: SRG-OS-000191-GPOS-00080

**Group ID:** `V-261264`

### Rule: SLEM 5 must implement an endpoint security tool.

**Rule ID:** `SV-261264r995659_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Adding endpoint security tools can provide the capability to automatically take actions in response to malicious behavior, which can provide additional agility in reacting to network threats. These tools also often include a reporting capability to provide network awareness of the system, which may not otherwise exist in an organization's systems management regime.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLEM 5 has implemented an endpoint security tool. If no endpoint security tool is present and enabled on the system, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-261265`

### Rule: SLEM 5 must display the Standard Mandatory DOD Notice and Consent Banner before granting any local or remote connection to the system.

**Rule ID:** `SV-261265r996289_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to SLEM 5 ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for SLEM 5 that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the system via SSH. Check the issue file to verify it contains one of the DOD required banners. If it does not, this is a finding. > more /etc/issue The output must display the following DOD-required banner text: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the output does not display the correct banner text, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261266`

### Rule: SLEM 5 must disable the x86 Ctrl-Alt-Delete key sequence.

**Rule ID:** `SV-261266r996292_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A locally logged-on user who presses Ctrl-Alt-Delete when at the console can reboot the system. If accidentally pressed, as could happen in the case of a mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot. In the graphical user interface environment, risk of unintentional reboot from the Ctrl-Alt-Delete sequence is reduced because the user will be prompted before any action is taken.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 is not configured to reboot the system when Ctrl-Alt-Delete is pressed with the following command: > systemctl status ctrl-alt-del.target ctrl-alt-del.target Loaded: masked (Reason: Unit ctrl-alt-del.target is masked.) Active: inactive (dead) If ctrl-alt-del.target is not masked, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-261267`

### Rule: SLEM 5 with a basic input/output system (BIOS) must require authentication upon booting into single-user and maintenance modes.

**Rule ID:** `SV-261267r996295_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system does not use a BIOS, this requirement is not applicable. Verify that SLEM 5 has set an encrypted root password with the following command: > sudo cat /boot/grub2/grub.cfg | grep -i password password_pbkdf2 root grub.pbkdf2.sha512.10000.03255F190F0E2F7B4F0D1C3216012309162F022A7A636771 If the root password entry does not begin with "password_pbkdf2", this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-261268`

### Rule: SLEM 5 with Unified Extensible Firmware Interface (UEFI) implemented must require authentication upon booting into single-user mode and maintenance.

**Rule ID:** `SV-261268r996298_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If the system allows a user to boot into single-user or maintenance mode without authentication, any user that invokes single-user or maintenance mode is granted privileged access to all system information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system does not use UEFI, this requirement is not applicable. Verify that SLEM 5 has set an encrypted root password with the following command: > sudo cat /boot/efi/EFI/BOOT/grub.cfg | grep -i password password_pbkdf2 root grub.pbkdf2.sha512.10000.03255F190F0E2F7B4F0D1C3216012309162F022A7A636771 If the root password entry does not begin with "password_pbkdf2", this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-261269`

### Rule: SLEM 5 must restrict access to the kernel message buffer.

**Rule ID:** `SV-261269r996301_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting access to the kernel message buffer limits access only to root. This prevents attackers from gaining additional system information as a nonprivileged user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 is configured to restrict access to the kernel message buffer with the following commands: > sudo sysctl kernel.dmesg_restrict kernel.dmesg_restrict = 1 If "kernel.dmesg_restrict" is not set to "1" or is missing, this is a finding. Check that the configuration files are present to enable this kernel parameter: > sudo grep -r kernel.dmesg_restrict /run/sysctl.d/* /etc/sysctl.d/* /usr/local/lib/sysctl.d/* /usr/lib/sysctl.d/* /lib/sysctl.d/* /etc/sysctl.conf 2> /dev/null /etc/sysctl.conf:kernel.dmesg_restrict = 1 /etc/sysctl.d/99-sysctl.conf:kernel.dmesg_restrict = 1 If "kernel.dmesg_restrict" is not set to "1", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261270`

### Rule: SLEM 5 kernel core dumps must be disabled unless needed.

**Rule ID:** `SV-261270r996860_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kernel core dumps may contain the full contents of system memory at the time of the crash. Kernel core dumps may consume a considerable amount of disk space and may result in denial of service (DoS) by exhausting the available space on the target file system partition.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLEM 5 kernel core dumps are disabled unless needed with the following command: > systemctl status kdump.service kdump.service - Load kdump kernel and initrd Loaded: loaded (/usr/lib/systemd/system/kdump.service; disabled; vendor preset: disabled) Active: inactive (dead) If "kdump.service" is active, ask the system administrator if the use of the service is required and documented with the information system security officer (ISSO). If the service is active and is not documented, this is a finding.

## Group: SRG-OS-000433-GPOS-00193

**Group ID:** `V-261271`

### Rule: Address space layout randomization (ASLR) must be implemented by SLEM 5 to protect memory from unauthorized code execution.

**Rule ID:** `SV-261271r996306_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in nonexecutable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can either be hardware enforced or software enforced, with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 implements Address space layout randomization (ASLR) with the following command: > sudo sysctl kernel.randomize_va_space kernel.randomize_va_space = 2 If the kernel parameter "randomize_va_space" is not equal to "2", or nothing is returned, this is a finding.

## Group: SRG-OS-000433-GPOS-00192

**Group ID:** `V-261272`

### Rule: SLEM 5 must implement kptr-restrict to prevent the leaking of internal kernel addresses.

**Rule ID:** `SV-261272r996309_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in nonexecutable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can either be hardware enforced or software enforced, with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 prevents leaking of internal kernel addresses with the following command: > sudo sysctl kernel.kptr_restrict kernel.kptr_restrict = 1 If the kernel parameter "kptr_restrict" is not equal to "1", or nothing is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261273`

### Rule: Vendor-packaged SLEM 5 security patches and updates must be installed and up to date.

**Rule ID:** `SV-261273r996311_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Timely patching is critical for maintaining the operational availability, confidentiality, and integrity of information technology (IT) systems. However, failure to keep SLEM 5 and application software patched is a common mistake made by IT professionals. New patches are released frequently, and it is often difficult for even experienced system administrators (SAs) to keep up with of all the new patches. When new weaknesses in a SLEM 5 exist, patches are usually made available by the vendor to resolve the problems. If the most recent security patches and updates are not installed, unauthorized users may take advantage of weaknesses in the unpatched software. The lack of prompt attention to patching could result in a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 security patches and updates are installed and up to date. Note: Updates are required to be applied with a frequency determined by the site or Program Management Office (PMO). Check for required SLEM 5 patches and updates with the following command: > sudo zypper patch-check 0 patches needed (0 security patches) If the patch repository data is corrupt, check that the available package security updates have been installed on the system with the following command: > sudo cut -d "|" -f 1-4 -s --output-delimiter " | " /var/log/zypp/history | grep -v " radd " 2023-09-25 12:23:25 | install | cockpit-ws | 298-150500.1.4 2023-09-25 12:23:26 | install | cockpit-storaged | 298-150500.1.4 2023-09-25 12:23:26 | install | cockpit-selinux | 298-150500.1.4 If SLEM 5 has not been patched within the site or PMO frequency, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-261274`

### Rule: The SLEM 5 tool zypper must have gpgcheck enabled.

**Rule ID:** `SV-261274r996312_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of SLEM 5. This requirement ensures the software has not been tampered with and has been provided by a trusted vendor. Accordingly, patches, service packs, device drivers, or SLEM 5 components must be signed with a certificate recognized and approved by the organization. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. SLEM 5 should not have to verify the software again. This requirement does not mandate DOD certificates for this purpose; however, the certificate used to verify the software must be from an approved Certification Authority (CA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLEM 5 tool zypper has gpgcheck enabled with the following command: > grep -i '^gpgcheck' /etc/zypp/zypp.conf gpgcheck = on If "gpgcheck" is not set to "on", is commented out, or missing, this is a finding.

## Group: SRG-OS-000437-GPOS-00194

**Group ID:** `V-261275`

### Rule: SLEM 5 must remove all outdated software components after updated versions have been installed.

**Rule ID:** `SV-261275r996314_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Previous versions of software components that are not removed from the information system after updates have been installed may be exploited by adversaries. Some information technology products may remove older versions of software automatically from the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 removes all outdated software components after updated version have been installed by running the following command: > grep -i upgraderemovedroppedpackages /etc/zypp/zypp.conf solver.upgradeRemoveDroppedPackages = true If "solver.upgradeRemoveDroppedPackages" is not set to "true", is commented out, or missing, this is a finding.

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-261276`

### Rule: SLEM 5 must use vlock to allow for session locking.

**Rule ID:** `SV-261276r996316_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Regardless of where the session lock is determined and implemented, once invoked, the session lock must remain in place until the user reauthenticates. No other activity aside from reauthentication must unlock the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that SLEM 5 has the "vlock" package installed with the following command: > zypper search --installed-only --match-exact --provides vlock i | kbd | Keyboard and Font Utilities | package If the command outputs "no matching items found", this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-261277`

### Rule: SLEM 5 must not have the telnet-server package installed.

**Rule ID:** `SV-261277r996318_rule`
**Severity:** high

**Description:**
<VulnDiscussion>It is detrimental for SLEM 5 to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked, and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. SLEM 5 is capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions and functions). Examples of nonessential capabilities include but are not limited to games, software packages, tools, and demonstration software not related to requirements or providing a wide array of functionality not required for every mission but which cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the telnet-server package is not installed on SLEM 5. Check that the telnet-server package is not installed on SLEM 5 by running the following command: > sudo zypper se telnet-server | grep Installed If the telnet-server package is installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261278`

### Rule: A separate file system must be used for SLEM 5 user home directories (such as /home or an equivalent).

**Rule ID:** `SV-261278r996320_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of separate file systems for different paths can protect the system from failures resulting from a file system becoming full or failing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a separate file system/partition has been created for SLEM 5 nonprivileged local interactive users (those with a UID greater than 1000) home directories with the following command: > awk -F: '($3>=1000)&&($7 !~ /nologin/){print $1, $3, $6, $7}' /etc/passwd adamsj 1002 /home/adamsj /bin/bash jacksonm 1003 /home/jacksonm /bin/bash smithj 1001 /home/smithj /bin/bash The output of the command will give the directory/partition that contains the home directories for the nonprivileged users on the system (in this example, /home) and user's shell. All accounts with a valid shell (such as /bin/bash) are considered interactive users. Check that a file system/partition has been created for the nonprivileged interactive users with the following command: Note: The partition of /home is used in the example. > grep /home /etc/fstab UUID=c4e898dd-6cd9-4091-a733-9435e505957a /home btrfs defaults,subvol=@/home 0 0 If a separate entry for the file system/partition that contains the nonprivileged interactive users' home directories does not exist, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261279`

### Rule: SLEM 5 must use a separate file system for /var.

**Rule ID:** `SV-261279r996322_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of separate file systems for different paths can protect the system from failures resulting from a file system becoming full or failing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLEM 5 has a separate file system/partition for "/var" with the following command: > grep /var /etc/fstab UUID=c4e898dd-6cd9-4091-a733-9435e505957a /var btrfs defaults,subvol=@/var,x-initrd.mount 0 0 If a separate entry for "/var" does not exist, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261280`

### Rule: SLEM 5 must use a separate file system for the system audit data path.

**Rule ID:** `SV-261280r996324_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of separate file systems for different paths can protect the system from failures resulting from a file system becoming full or failing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLEM 5 has a separate file system/partition for the system audit data path with the following command: Note: "/var/log/audit" is used as the example as it is a common location. > grep /var/log/audit /etc/fstab UUID=c4e898dd-6cd9-4091-a733-9435e505957a /var btrfs defaults,subvol=@/var/log/audit 0 0 If a separate entry for the system audit data path (in this example the "/var/log/audit" path) does not exist, ask the system administrator if the system audit logs are being written to a different file system/partition on the system and then grep for that file system/partition. If a separate file system/partition does not exist for the system audit data path, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261281`

### Rule: SLEM 5 file systems that are being imported via Network File System (NFS) must be mounted to prevent files with the setuid and setgid bit set from being executed.

**Rule ID:** `SV-261281r996326_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 file systems that are being NFS exported are mounted with the "nosuid" option with the following command: > grep nfs /etc/fstab UUID=e06097bb-cfcd-437b-9e4d-a691f5662a7d /store nfs rw,nosuid 0 0 If a file system found in "/etc/fstab" refers to NFS and it does not have the "nosuid" option set, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261282`

### Rule: SLEM 5 file systems that are being imported via Network File System (NFS) must be mounted to prevent binary files from being executed.

**Rule ID:** `SV-261282r996328_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 file systems that are being NFS exported are mounted with the "noexec" option with the following command: > grep nfs /etc/fstab UUID=e06097bb-cfcd-437b-9e4d-a691f5662a7d /store nfs rw,noexec 0 0 If a file system found in "/etc/fstab" refers to NFS and it does not have the "noexec" option set, and use of NFS exported binaries is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261283`

### Rule: SLEM 5 file systems that are used with removable media must be mounted to prevent files with the setuid and setgid bit set from being executed.

**Rule ID:** `SV-261283r996330_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 file systems used for removable media are mounted with the "nosuid" option with the following command: > more /etc/fstab UUID=2bc871e4-e2a3-4f29-9ece-3be60c835222 /mnt/usbflash vfat noauto,owner,ro,nosuid 0 0 If a file system found in "/etc/fstab" refers to removable media and does not have the "nosuid" option set, this is a finding.

## Group: SRG-OS-000185-GPOS-00079

**Group ID:** `V-261284`

### Rule: All SLEM 5 persistent disk partitions must implement cryptographic mechanisms to prevent unauthorized disclosure or modification of all information that requires at-rest protection.

**Rule ID:** `SV-261284r996864_rule`
**Severity:** high

**Description:**
<VulnDiscussion>SLEM 5 handling data requiring data-at-rest protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 prevents unauthorized disclosure or modification of all information requiring at-rest protection by using disk encryption. Verify the system partitions are all encrypted with the following commands: > sudo blkid /dev/sda1: "UUID=26d4a101-7f48-4394-b730-56dc00e65f64" TYPE="crypto_LUKS" /dev/sda2: "UUID=f5b8a790-14cb-4b82-882d-707d52f27765" TYPE="crypto_LUKS" /dev/sda3: "UUID=f2d86128-f975-478d-a5b0-25806c900eac" TYPE="crypto_LUKS" Every persistent disk partition present must be of type "crypto_LUKS". If any partitions other than the boot partition or pseudo file systems (such as /proc or /sys) or temporary file systems (that are tmpfs) are not type "crypto_LUKS", ask the administrator to indicate how the partitions are encrypted. If there is no evidence that these partitions are encrypted, this is a finding. > sudo more /etc/crypttab cr_root UUID=26d4a101-7f48-4394-b730-56dc00e65f64 cr_home UUID=f5b8a790-14cb-4b82-882d-707d52f27765 cr_swap UUID=f2d86128-f975-478d-a5b0-25806c900eac Every persistent disk partition present on the system must have an entry in the /etc/crypttab file. If any partitions other than pseudo file systems (such as /proc or /sys) are not listed or "/etc/crypttab" does not exist, this is a finding. Verify the system works in FIPS mode with the following command: > sudo sysctl - a | grep fips crypto.fips_enabled = 1

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261285`

### Rule: SLEM 5 file systems that contain user home directories must be mounted to prevent files with the setuid and setgid bit set from being executed.

**Rule ID:** `SV-261285r996838_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute setuid and setgid files with owner privileges. This option must be used for mounting any file system not containing approved setuid and setguid files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLEM 5 file systems that contain user home directories are mounted with the "nosuid" option. Print the currently active file system mount options of the file system(s) that contain the user home directories with the following command: > for X in `awk -F: '($3>=1000)&&($7 !~ /nologin/){print $6}' /etc/passwd`; do findmnt -nkT $X; done | sort -r /home /dev/mapper/system-home ext4 rw,nosuid,realtime,data=ordered If a file system containing user home directories is not mounted with the FSTYPE OPTION nosuid, this is a finding. Note: If a separate file system has not been created for the user home directories (user home directories are mounted under "/"), this is not a finding as the "nosuid" option cannot be used on the "/" system.

## Group: SRG-OS-000114-GPOS-00059

**Group ID:** `V-261286`

### Rule: SLEM 5 must disable the file system automounter unless required.

**Rule ID:** `SV-261286r996338_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatically mounting file systems permits easy introduction of unknown devices, thereby facilitating malicious activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 disables the ability to automount devices. Verify the automounter service is installed with the following command: > sudo zypper se autofs If it is installed, verify the automounter service is active with the following command: > systemctl status autofs autofs.service - Automounts filesystems on demand Loaded: loaded (/usr/lib/systemd/system/autofs.service; disabled) Active: inactive (dead) If the "autofs" status is set to "active" and is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-261287`

### Rule: SLEM 5 must have directories that contain system commands set to a mode of 755 or less permissive.

**Rule ID:** `SV-261287r996341_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SLEM 5 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SLEM 5 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the system command directories have mode "755" or less permissive with the following command: > find -L /usr/local/bin /usr/local/sbin -perm /022 -type d -exec stat -c "%n %a" '{}' \; If any directories are found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-261288`

### Rule: SLEM 5 must have system commands set to a mode of 755 or less permissive.

**Rule ID:** `SV-261288r996344_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SLEM 5 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SLEM 5 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the system command directories have mode "755" or less permissive with the following command: > find -L /usr/local/bin /usr/local/sbin -perm /022 -type d -exec stat -c "%n %a" '{}' \; If any directories are found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-261289`

### Rule: SLEM 5 library directories must have mode 755 or less permissive.

**Rule ID:** `SV-261289r996347_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SLEM 5 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SLEM 5 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system-wide shared library directories "/lib", "/lib64", "/usr/lib" and "/usr/lib64" have mode "755" or less permissive with the following command: > sudo find /lib /lib64 /usr/lib /usr/lib64 -perm /022 -type d -exec stat -c "%n %a" '{}' \; If any of the aforementioned directories are found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-261290`

### Rule: SLEM 5 library files must have mode 755 or less permissive.

**Rule ID:** `SV-261290r1102096_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SLEM 5 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SLEM 5 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and "/usr/lib64" have mode 0755 or less permissive. Check that the systemwide shared library files have mode 0755 or less permissive with the following command: > sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' -perm /022 -exec stat -c "%n %a" {} + If any output is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261291`

### Rule: All SLEM 5 local interactive user home directories must have mode 750 or less permissive.

**Rule ID:** `SV-261291r996352_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on local interactive user home directories may allow unauthorized access to user files by other users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This may miss interactive users that have been assigned a privileged User Identifier (UID). Evidence of interactive use may be obtained from a number of log files containing system logon information. Verify the assigned home directory of all SLEM 5 local interactive users has a mode of "750" or less permissive with the following command: > ls -ld $(awk -F: '($3>=1000)&&($7 !~ /nologin/){print $6}' /etc/passwd) -rwxr-x--- 1 smithj users 18 Mar 5 17:6 /home/smithj If home directories referenced in "/etc/passwd" do not have a mode of "750" or less permissive, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261292`

### Rule: All SLEM 5 local initialization files must have mode 740 or less permissive.

**Rule ID:** `SV-261292r996354_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Local initialization files are used to configure the user's shell environment upon logon. Malicious modification of these files could compromise accounts upon logon.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all SLEM 5 local initialization files have a mode of "740" or less permissive with the following command: Note: The example will be for the user "smithj", who has a home directory of "/home/smithj". > sudo ls -al /home/smithj/.* | more -rw-r-x---- 1 smithj users 896 Mar 10 2011 .profile -rw-r-x---- 1 smithj users 497 Jan 6 27 .login -rw-r-x---- 1 smithj users 886 Jan 6 27 .something If any local initialization files have a mode more permissive than "740", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261293`

### Rule: SLEM 5 SSH daemon public host key files must have mode 644 or less permissive.

**Rule ID:** `SV-261293r996357_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a public host key file is modified by an unauthorized user, the SSH service may be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 SSH daemon public host key files have mode "644" or less permissive with the following command: Note: SSH public key files may be found in other directories on the system depending on the installation. > find /etc/ssh -name 'ssh_host*key.pub' -exec stat -c "%a %n" {} \; 644 /etc/ssh/ssh_host_rsa_key.pub 644 /etc/ssh/ssh_host_dsa_key.pub 644 /etc/ssh/ssh_host_ecdsa_key.pub 644 /etc/ssh/ssh_host_ed25519_key.pub If any file has a mode more permissive than "644", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261294`

### Rule: SLEM 5 SSH daemon private host key files must have mode 640 or less permissive.

**Rule ID:** `SV-261294r996359_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an unauthorized user obtains the private SSH host key file, the host could be impersonated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 SSH daemon private host key files have mode "640" or less permissive. The following command will find all SSH private key files on the system with the following command: > sudo find / -name '*ssh_host*key' -exec ls -lL {} \; Check the mode of the private host key files under "/etc/ssh" file with the following command: > find /etc/ssh -name 'ssh_host*key' -exec stat -c "%a %n" {} \; 640 /etc/ssh/ssh_host_rsa_key 640 /etc/ssh/ssh_host_dsa_key 640 /etc/ssh/ssh_host_ecdsa_key 640 /etc/ssh/ssh_host_ed25519_key If any file has a mode more permissive than "640", this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-261295`

### Rule: SLEM 5 library files must be owned by root.

**Rule ID:** `SV-261295r1102099_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SLEM 5 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SLEM 5 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and "/usr/lib64" are owned by root with the following command: > sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' ! -user root -exec stat -c "%n %U" {} + If any output is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-261296`

### Rule: SLEM 5 library files must be group-owned by root.

**Rule ID:** `SV-261296r1102102_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SLEM 5 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SLEM 5 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and "/usr/lib64" are group owned by root with the following command: > sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' ! -group root -exec stat -c "%n %G" {} + If any output is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-261297`

### Rule: SLEM 5 library directories must be owned by root.

**Rule ID:** `SV-261297r996368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SLEM 5 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SLEM 5 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system-wide shared library directories contained in the directories "/lib", "/lib64", "/usr/lib" and "/usr/lib64" are owned by root with the following command: > sudo find /lib /lib64 /usr/lib /usr/lib64 ! -user root -type d -exec stat -c "%n %U" '{}' \; If any system wide library directory is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-261298`

### Rule: SLEM 5 library directories must be group-owned by root.

**Rule ID:** `SV-261298r996371_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SLEM 5 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SLEM 5 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system-wide shared library directories contained in the directories "/lib", "/lib64", "/usr/lib" and "/usr/lib64" are group-owned by root with the following command: > sudo find /lib /lib64 /usr/lib /usr/lib64 ! -group root -type d -exec stat -c "%n %G" '{}' \; If any system wide library directory is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-261299`

### Rule: SLEM 5 must have system commands owned by root.

**Rule ID:** `SV-261299r996373_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SLEM 5 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SLEM 5 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the system commands are owned by root with the following command: > sudo find -L /usr/local/bin /usr/local/sbin ! -user root -type f -exec stat -c "%n %U" '{}' \; If any system commands are returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-261300`

### Rule: SLEM 5 must have system commands group-owned by root or a system account.

**Rule ID:** `SV-261300r996375_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SLEM 5 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SLEM 5 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the system commands are group-owned by root with the following command: > sudo find -L /usr/local/bin /usr/local/sbin! -group root -type f -exec stat -c "%n %G" '{}' \; If any system commands are returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-261301`

### Rule: SLEM 5 must have directories that contain system commands owned by root.

**Rule ID:** `SV-261301r996377_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SLEM 5 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SLEM 5 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the system command directories are owned by root with the following command: > find -L /usr/local/bin /usr/local/sbin ! -user root -type d -exec stat -c "%n %U" '{}' \; If any system command directories are returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-261302`

### Rule: SLEM 5 must have directories that contain system commands group-owned by root.

**Rule ID:** `SV-261302r996380_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SLEM 5 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SLEM 5 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the system command directories are group-owned by root with the following command: > find -L /usr/local/bin /usr/local/sbin ! -group root -type d -exec stat -c "%n %G" '{}' \; If any system command directories are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261303`

### Rule: All SLEM 5 files and directories must have a valid owner.

**Rule ID:** `SV-261303r996382_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unowned files and directories may be unintentionally inherited if a user is assigned the same User Identifier (UID) as the UID of the unowned files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all SLEM 5 files and directories on the system have a valid owner with the following command: Note: The value after -fstype must be replaced with the filesystem type. XFS is used as an example. > sudo find / -fstype xfs -nouser If any files on the system do not have a valid owner, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261304`

### Rule: All SLEM 5 files and directories must have a valid group owner.

**Rule ID:** `SV-261304r996384_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Files without a valid group owner may be unintentionally inherited if a group is assigned the same Group Identifier (GID) as the GID of the files without a valid group owner.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all SLEM 5 files and directories on the system have a valid group with the following command: Note: The value after -fstype must be replaced with the filesystem type. XFS is used as an example. > sudo find / -fstype xfs -nogroup If any files on the system do not have a valid group, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261305`

### Rule: All SLEM 5 local interactive user home directories must be group-owned by the home directory owner's primary group.

**Rule ID:** `SV-261305r996387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Group Identifier (GID) of a local interactive user's home directory is not the same as the primary GID of the user, this would allow unauthorized access to the user's files, and users that share the same group may not be able to access files that they legitimately should.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the assigned home directory of all SLEM 5 local interactive users is group-owned by that user's primary GID with the following command: Note: This may miss local interactive users that have been assigned a privileged User Identifier (UID). Evidence of interactive use may be obtained from a number of log files containing system logon information. The returned directory "/home/smithj" is used as an example. > awk -F: '($3>=1000)&&($7 !~ /nologin/){print $4, $6}' /etc/passwd) 250:/home/smithj Check the user's primary group with the following command: > grep users /etc/group users:x:250:smithj,jonesj,jacksons If the user home directory referenced in "/etc/passwd" is not group-owned by that user's primary GID, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261306`

### Rule: All SLEM 5 world-writable directories must be group-owned by root, sys, bin, or an application group.

**Rule ID:** `SV-261306r996389_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a world-writable directory has the sticky bit set and is not group-owned by a privileged Group Identifier (GID), unauthorized users may be able to modify files created by others. The only authorized public directories are those temporary directories supplied with the system or those designed to be temporary file repositories. The setting is normally reserved for directories used by the system and by users for temporary file storage, (e.g., /tmp), and for directories requiring global read/write access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all SLEM 5 world-writable directories are group-owned by root, sys, bin, or an application group with the following command: > sudo find / -perm -002 -type d -exec ls -lLd {} \; drwxrwxrwt. 2 root root 40 Aug 26 13:7 /dev/mqueue drwxrwxrwt. 2 root root 220 Aug 26 13:23 /dev/shm drwxrwxrwt. 14 root root 4096 Aug 26 13:29 /tmp If any world-writable directories are not owned by root, sys, bin, or an application group associated with the directory, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-261307`

### Rule: The sticky bit must be set on all SLEM 5 world-writable directories.

**Rule ID:** `SV-261307r996392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, and hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DOD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 prevents unauthorized and unintended information transfer via the shared system resources with the following command: > sudo find / \( -path /.snapshots -o -path /sys -o -path /proc \) -prune -o -perm -002 -type d -exec ls -lLd {} \; 256 0 drwxrwxrwt 1 root root 4096 Jun 14 06:45 /tmp If any of the returned directories do not have the sticky bit set, or are not documented as having the write permission for the other class, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-261308`

### Rule: SLEM 5 must prevent unauthorized users from accessing system error messages.

**Rule ID:** `SV-261308r996395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify SLEM 5 or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 prevents unauthorized users from accessing system error messages. Check the "/var/log/messages" file permissions with the following command: > sudo stat -c "%n %U:%G %a" /var/log/messages /var/log/messages root:root 640 Check that "permissions.local" file contains the correct permissions rules with the following command: > grep -i messages /etc/permissions.local /var/log/messages root:root 640 If the effective permissions do not match the "permissions.local" file, the command does not return any output, or is commented out, this is a finding.

## Group: SRG-OS-000205-GPOS-00083

**Group ID:** `V-261309`

### Rule: SLEM 5 must generate error messages that provide information necessary for corrective actions without revealing information that could be exploited by adversaries.

**Rule ID:** `SV-261309r996398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any operating system providing too much information in error messages risks compromising the data and security of the structure, and content of error messages needs to be carefully considered by the organization. Organizations carefully consider the structure/content of error messages. The extent to which information systems are able to identify and handle error conditions is guided by organizational policy and operational requirements. Information that could be exploited by adversaries includes, for example, erroneous logon attempts with passwords entered by mistake as the username, mission/business information that can be derived from (if not stated explicitly by) information recorded, and personal information, such as account numbers, social security numbers, and credit card numbers. The /var/log/btmp, /var/log/wtmp, and /var/log/lastlog files have group write and global read permissions to allow for the lastlog function to perform. Limiting the permissions beyond this configuration will result in the failure of functions that rely on the lastlog database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 has all system log files under the /var/log directory with a permission set to "640", by using the following command: Note: The btmp, wtmp, and lastlog files are excluded. Refer to the Vulnerability Discussion for details. > sudo find /var/log -perm /137 ! -name '*[bw]tmp' ! -name '*lastlog' -type f -exec stat -c "%n %a" {} \; If command displays any output, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-261310`

### Rule: SLEM 5 must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services as defined in the Ports, Protocols, and Services Management (PPSM) Category Assignments List (CAL) and vulnerability assessments.

**Rule ID:** `SV-261310r996401_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Additionally, operating system remote access functionality must have the capability to immediately disconnect current users remotely accessing the information system and/or disable further remote access. The speed of disconnect or disablement varies based on the criticality of mission functions and the need to eliminate immediate or future remote access to organizational information systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 "firewalld.service" is enabled and running with the following command: > systemctl status firewalld.service firewalld.service - firewalld - dynamic firewall daemon Loaded: loaded (/usr/lib/systemd/system/firewalld.service; enabled; vendor preset: disabled) Active: active (running) since Wed 2023-11-29 08:12:35 MST If the service is not enabled and active, this is a finding. Check the firewall configuration for any unnecessary or prohibited functions, ports, protocols, and/or services by running the following command: > sudo firewall-cmd --list-all Ask the system administrator for the site or program PPSM Component Local Services Assessment (Component Local Services Assessment (CLSA). Verify the services allowed by the firewall match the PPSM CLSA. If there are any additional ports, protocols, or services that are not included in the PPSM CLSA, this is a finding. If there are any ports, protocols, or services that are prohibited by the PPSM CAL, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-261311`

### Rule: SLEM 5 clock must, for networked systems, be synchronized to an authoritative DOD time source at least every 24 hours.

**Rule ID:** `SV-261311r1038944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLEM 5 clock must be configured to synchronize to an authoritative DOD time source when the time difference is greater than one second with the following command: > sudo grep maxpoll /etc/chrony.conf server 0.us.pool.ntp.mil maxpoll 16 If the "server" parameter is not set to an authoritative DOD time source, "maxpoll" is greater than "16", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261312`

### Rule: SLEM 5 must not have network interfaces in promiscuous mode unless approved and documented.

**Rule ID:** `SV-261312r996406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network interfaces in promiscuous mode allow for the capture of all network traffic visible to the system. If unauthorized individuals can access these applications, it may allow then to collect information such as logon IDs, passwords, and key exchanges between systems. If the system is being used to perform a network troubleshooting function, the use of these tools must be documented with the information system security officer (ISSO) and restricted to only authorized personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 network interfaces are not in promiscuous mode with the following command: > ip link | grep -i promisc If network interfaces are found on the system in promiscuous mode and their use has not been approved by the ISSO and documented, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261313`

### Rule: SLEM 5 must not forward Internet Protocol version 4 (IPv4) source-routed packets.

**Rule ID:** `SV-261313r996409_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when IPv4/IPv6 forwarding is enabled and the system is functioning as a router.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 does not accept IPv4 source-routed packets with the following command: > sudo sysctl net.ipv4.conf.all.accept_source_route net.ipv4.conf.all.accept_source_route = 0 If the network parameter "ipv4.conf.all.accept_source_route" is not equal to "0", or nothing is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261314`

### Rule: SLEM 5 must not forward Internet Protocol version 4 (IPv4) source-routed packets by default.

**Rule ID:** `SV-261314r996412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when IPv4 forwarding is enabled and the system is functioning as a router.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 does not accept IPv4 source-routed packets by default with the following command: > sudo sysctl net.ipv4.conf.default.accept_source_route net.ipv4.conf.default.accept_source_route = 0 If the network parameter "ipv4.conf.default.accept_source_route" is not equal to "0", or nothing is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261315`

### Rule: SLEM 5 must prevent Internet Protocol version 4 (IPv4) Internet Control Message Protocol (ICMP) redirect messages from being accepted.

**Rule ID:** `SV-261315r996415_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 does not accept IPv4 ICMP redirect messages with the following command: > sudo sysctl net.ipv4.conf.all.accept_redirects net.ipv4.conf.all.accept_redirects = 0 If the network parameter "ipv4.conf.all.accept_redirects" is not equal to "0", or nothing is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261316`

### Rule: SLEM 5 must not allow interfaces to accept Internet Protocol version 4 (IPv4) Internet Control Message Protocol (ICMP) redirect messages by default.

**Rule ID:** `SV-261316r996418_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 does not accept IPv4 ICMP redirect messages by default with the following command: > sudo sysctl net.ipv4.conf.default.accept_redirects net.ipv4.conf.default.accept_redirects = 0 If the network parameter "ipv4.conf.default.accept_redirects" is not equal to "0", or nothing is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261317`

### Rule: SLEM 5 must not send Internet Protocol version 4 (IPv4) Internet Control Message Protocol (ICMP) redirects.

**Rule ID:** `SV-261317r996421_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages contain information from the system's route table, possibly revealing portions of the network topology.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 does not allow interfaces to perform IPv4 ICMP redirects with the following command: > sudo sysctl net.ipv4.conf.all.send_redirects net.ipv4.conf.all.send_redirects = 0 If the network parameter "ipv4.conf.all.send_redirects" is not equal to "0", or nothing is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261318`

### Rule: SLEM 5 must not allow interfaces to send Internet Protocol version 4 (IPv4) Internet Control Message Protocol (ICMP) redirect messages by default.

**Rule ID:** `SV-261318r996424_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages contain information from the system's route table, possibly revealing portions of the network topology.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 does not allow interfaces to perform IPv4 ICMP redirects by default with the following command: > sudo sysctl net.ipv4.conf.default.send_redirects net.ipv4.conf.default.send_redirects = 0 If the network parameter "ipv4.conf.default.send_redirects" is not equal to "0", or nothing is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261319`

### Rule: SLEM 5 must not be performing Internet Protocol version 4 (IPv4) packet forwarding unless the system is a router.

**Rule ID:** `SV-261319r996427_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 is not performing IPv4 packet forwarding, unless the system is a router with the following command: > sudo sysctl net.ipv4.ip_forward net.ipv4.ip_forward = 0 If the network parameter "ipv4.ip_forward" is not equal to "0", or nothing is returned, this is a finding.

## Group: SRG-OS-000142-GPOS-00071

**Group ID:** `V-261320`

### Rule: SLEM 5 must be configured to use TCP syncookies.

**Rule ID:** `SV-261320r996861_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Denial of service (DoS) is a condition in which a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Managing excess capacity ensures that sufficient capacity is available to counter flooding attacks. Employing increased capacity and service redundancy may reduce the susceptibility to some DoS attacks. Managing excess capacity may include, for example, establishing selected usage priorities, quotas, or partitioning.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 is configured to use IPv4 TCP syncookies with the following command: > sudo sysctl net.ipv4.tcp_syncookies net.ipv4.tcp_syncookies = 1 If the network parameter "ipv4.tcp_syncookies" is not equal to "1", or nothing is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261321`

### Rule: SLEM 5 must not forward Internet Protocol version 6 (IPv6) source-routed packets.

**Rule ID:** `SV-261321r996433_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when IPv4 forwarding is enabled and the system is functioning as a router.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 does not accept IPv6 source-routed packets with the following command: > sudo sysctl net.ipv6.conf.all.accept_source_route net.ipv6.conf.all.accept_source_route = 0 If the network parameter "ipv6.conf.all.accept_source_route" is not equal to "0" or nothing is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261322`

### Rule: SLEM 5 must not forward Internet Protocol version 6 (IPv6) source-routed packets by default.

**Rule ID:** `SV-261322r996436_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when IPv4 forwarding is enabled and the system is functioning as a router.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 does not accept IPv6 source-routed packets by default with the following command: > sudo sysctl net.ipv6.conf.default.accept_source_route net.ipv6.conf.default.accept_source_route = 0 If the network parameter "ipv6.conf.default.accept_source_route" is not equal to "0", or nothing is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261323`

### Rule: SLEM 5 must prevent Internet Protocol version 6 (IPv6) Internet Control Message Protocol (ICMP) redirect messages from being accepted.

**Rule ID:** `SV-261323r996439_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 does not accept IPv6 ICMP redirect messages with the following command: > sudo sysctl net.ipv6.conf.all.accept_redirects net.ipv6.conf.all.accept_redirects = 0 If the network parameter "ipv6.conf.all.accept_redirects" is not equal to "0", or nothing is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261324`

### Rule: SLEM 5 must not allow interfaces to accept Internet Protocol version 6 (IPv6) Internet Control Message Protocol (ICMP) redirect messages by default.

**Rule ID:** `SV-261324r996442_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 does not allow IPv6 ICMP redirect messages by default with the following command: > sudo sysctl net.ipv6.conf.default.accept_redirects net.ipv6.conf.default.accept_redirects = 0 If the network parameter "ipv6.conf.default.accept_redirects" is not equal to "0", or nothing is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261325`

### Rule: SLEM 5 must not be performing Internet Protocol version 6 (IPv6) packet forwarding unless the system is a router.

**Rule ID:** `SV-261325r996445_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 is not performing IPv6 packet forwarding, unless the system is a router with the following command: > sudo sysctl net.ipv6.conf.all.forwarding net.ipv6.conf.all.forwarding = 0 If the network parameter "ipv6.conf.all.forwarding" is not equal to "0", or nothing is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261326`

### Rule: SLEM 5 must not be performing Internet Protocol version 6 (IPv6) packet forwarding by default unless the system is a router.

**Rule ID:** `SV-261326r996448_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 is not performing IPv6 packet forwarding by default, unless the system is a router with the following command: > sudo sysctl net.ipv6.conf.default.forwarding net.ipv6.conf.default.forwarding = 0 If the network parameter "ipv6.conf.default.forwarding" is not equal to "0", or nothing is returned, this is a finding.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-261327`

### Rule: SLEM 5 must have SSH installed to protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-261327r996450_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, logical means (cryptography) do not have to be employed, and vice versa.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH package is installed by using the following command: > zypper info openssh | grep -i installed Name : openssh Version : 8.4p1-3.9.1 Arch : X86_64 Vendor : SUSE LLC <https://www.suse.com> Installed Size : 0 B Installed : Yes Status : up-to-date If the "openssh" package is not installed, this is a finding.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-261328`

### Rule: SLEM 5 must use SSH to protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-261328r996453_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, logical means (cryptography) do not have to be employed, and vice versa.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "sshd.service" is enabled and active by using the following command: > systemctl status sshd.service | grep -i active Active: active (running) since Wed 2023-11-29 09:49:45 MST; 2 months 23 days ago If "openssh.service" is not active, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-261329`

### Rule: SLEM 5 must display the Standard Mandatory DOD Notice and Consent Banner before granting access via SSH.

**Rule ID:** `SV-261329r996455_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to SLEM 5 ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for SLEM 5 that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the system via SSH with the following command: > sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*banner' /etc/ssh/sshd_config:Banner /etc/issue If "Banner" is not set to "/etc/issue", is commented out, missing, or conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-261330`

### Rule: SLEM 5 must not allow unattended or automatic logon via SSH.

**Rule ID:** `SV-261330r996457_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Failure to restrict system access via SSH to authenticated users negatively impacts SLEM 5 security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 disables unattended or automatic logon via SSH with the following command: > sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iEH '^\s*(permit(.*?)(passwords|environment))' /etc/ssh/sshd_config:PermitEmptyPasswords no /etc/ssh/sshd_config:PermitUserEnvironment no If "PermitEmptyPasswords" or "PermitUserEnvironment" keywords are not set to "no", are commented out, or are missing completely, this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-261331`

### Rule: SLEM 5 must be configured so that all network connections associated with SSH traffic terminate after becoming unresponsive.

**Rule ID:** `SV-261331r996459_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an unresponsive SSH session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle SSH session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level and deallocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean the operating system terminates all sessions or network access; it only ends the unresponsive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH server automatically terminates a user session after the SSH client has become unresponsive by using the following command: > sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*clientalivecountmax' /etc/ssh/sshd_config:ClientAliveCountMax 1 If "ClientAliveCountMax" is not set to "1", is commented out, missing, or conflicting results are returned, this is a finding.

## Group: SRG-OS-000126-GPOS-00066

**Group ID:** `V-261332`

### Rule: SLEM 5 must be configured so that all network connections associated with SSH traffic are terminated after 10 minutes of becoming unresponsive.

**Rule ID:** `SV-261332r996462_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an unresponsive SSH session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle SSH session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level and deallocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that the operating system terminates all sessions or network access; it only ends the unresponsive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH server automatically terminates a user session after the SSH client has been unresponsive for 10 minutes by using the following command: > sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*clientaliveinterval' /etc/ssh/sshd_config:ClientAliveInterval 600 If "ClientAliveInterval" is not set to "600" or less, is commented out, missing, or conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261333`

### Rule: SLEM 5 SSH daemon must disable forwarded remote X connections for interactive users, unless to fulfill documented and validated mission requirements.

**Rule ID:** `SV-261333r996464_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The security risk of using X11 forwarding is that the client's X11 display server may be exposed to attack when the SSH client requests forwarding. A system administrator may have a stance in which they want to protect clients that may expose themselves to attack by unwittingly requesting X11 forwarding, which can warrant a ''no'' setting. X11 forwarding should be enabled with caution. Users with the ability to bypass file permissions on the remote host (for the user's X11 authorization database) can access the local X11 display through the forwarded connection. An attacker may then be able to perform activities such as keystroke monitoring if the ForwardX11Trusted option is also enabled. If X11 services are not required for the system's intended function, they should be disabled or restricted as appropriate to the system's needs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 SSH daemon remote X forwarded connections for interactive users are disabled with the following command: > sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*x11forwarding' /etc/ssh/sshd_config:X11Forwarding no If the "X11Forwarding" keyword is set to "yes" and is not documented with the information system security officer (ISSO) as an operational requirement, is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-261334`

### Rule: SLEM 5 must implement DOD-approved encryption to protect the confidentiality of SSH remote connections.

**Rule ID:** `SV-261334r996467_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection (e.g., RDP), thereby providing a degree of confidentiality. The encryption strength of a mechanism is selected based on the security categorization of the information. The system will attempt to use the first cipher presented by the client that matches the server list. Listing the values "strongest to weakest" is a method to ensure the use of the strongest cipher available to secure the SSH connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLEM 5 implements DOD-approved encryption to protect the confidentiality of SSH remote connections with the following command: > sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*ciphers' /etc/ssh/sshd_config:Ciphers aes256-ctr,aes192-ctr,aes128-ctr If any ciphers other than "aes256-ctr", "aes192-ctr", or "aes128-ctr" are listed, the order differs from the example above, the line is commented out, or the "Ciphers" keyword is missing, or conflicting results are returned, this is a finding.

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-261335`

### Rule: SLEM 5 SSH daemon must be configured to only use Message Authentication Codes (MACs) employing FIPS 140-2/140-3 approved cryptographic hash algorithms.

**Rule ID:** `SV-261335r996469_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. The system will attempt to use the first hash presented by the client that matches the server list. Listing the values "strongest to weakest" is a method to ensure the use of the strongest hash available to secure the SSH connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 SSH daemon is configured to only use MACs that employ FIPS 140-2/140-3 approved hashes with the following command: > sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*macs' /etc/ssh/sshd_config:MACs hmac-sha2-512,hmac-sha2-256 If any ciphers other than "hmac-sha2-512" or "hmac-sha2-256" are listed, the order differs from the example above, is commented out, missing, or conflicting results are returned, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-261336`

### Rule: SLEM 5 SSH server must be configured to use only FIPS 140-2/140-3 validated key exchange algorithms.

**Rule ID:** `SV-261336r996472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without cryptographic integrity protections provided by FIPS 140-2/140-3 validated cryptographic algorithms, information can be viewed and altered by unauthorized users without detection. The system will attempt to use the first algorithm presented by the client that matches the server list. Listing the values "strongest to weakest" is a method to ensure the use of the strongest algorithm available to secure the SSH connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SSH server is configured to use only FIPS 140-2/140-3 validated key exchange algorithms with the following command: > sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*kexalgorithms' KexAlgorithms ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256 If "KexAlgorithms" does not contain the list of algorithms in the exact order, is commented out, missing, or conflicting results are returned, this is a finding.

## Group: SRG-OS-000109-GPOS-00056

**Group ID:** `V-261337`

### Rule: SLEM 5 must deny direct logons to the root account using remote access via SSH.

**Rule ID:** `SV-261337r996844_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure individual accountability and prevent unauthorized access, organizational users must be individually identified and authenticated. A group authenticator is a generic account used by multiple individuals. Use of a group authenticator alone does not uniquely identify individual users. Examples of the group authenticator is the Unix OS "root" user account, the Windows "Administrator" account, the "sa" account, or a "helpdesk" account. For example, the Unix and Windows SLEM 5 offer a "switch user" capability, allowing users to authenticate with their individual credentials and, when needed, "switch" to the administrator role. This method provides for unique individual authentication prior to using a group authenticator. Users (and any processes acting on behalf of users) need to be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization, which outlines specific user actions that can be performed on SLEM 5 without identification or authentication. Requiring individuals to be authenticated with an individual authenticator prior to using a group authenticator allows for traceability of actions, as well as adding an additional level of protection of the actions that can be taken with group account knowledge.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 denies direct logons to the root account using remote access via SSH with the following command: > sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*permitrootlogin' /etc/ssh/sshd_config:PermitRootLogin no If the "PermitRootLogin" keyword is set to "yes", is commented out, missing, or conflicting results are returned, this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-261338`

### Rule: SLEM 5 must log SSH connection attempts and failures to the server.

**Rule ID:** `SV-261338r996845_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyberattacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SSH is configured to verbosely log connection attempts and failed logon attempts to SLEM 5 with the following command: > sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*loglevel' /etc/ssh/sshd_config:LogLevel VERBOSE If "LogLevel" is not set to "VERBOSE", is commented out, missing, or conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261339`

### Rule: SLEM 5 must display the date and time of the last successful account logon upon an SSH logon.

**Rule ID:** `SV-261339r996480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Providing users with feedback on when account accesses via SSH last occurred facilitates user recognition and reporting of unauthorized account use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all remote connections via SSH to SLEM 5 display feedback on when account accesses last occurred with the following command: > sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*printlastlog' /etc/ssh/sshd_config:PrintLastLog yes If the "PrintLastLog" is not set to "yes", is commented out, missing, or conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261340`

### Rule: SLEM 5 SSH daemon must be configured to not allow authentication using known hosts authentication.

**Rule ID:** `SV-261340r996483_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring this setting for the SSH daemon provides additional assurance that remote logon via SSH will require a password, even in the event of misconfiguration elsewhere.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 SSH daemon is configured to not allow authentication using "known hosts" authentication with the following command: > sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*ignoreuserknownhosts' /etc/ssh/sshd_config:IgnoreUserKnownHosts yes If "IgnoreUserKnownHosts" is not set to "no", is commented out, missing, or conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261341`

### Rule: SLEM 5 SSH daemon must perform strict mode checking of home directory configuration files.

**Rule ID:** `SV-261341r996486_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If other users have access to modify user-specific SSH configuration files, they may be able to log on to the system as another user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 SSH daemon performs strict mode checking of home directory configuration files with the following command: > sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*strictmodes' /etc/ssh/sshd_config:StrictModes yes If "StrictModes" is not set to "yes", is commented out, missing, or conflicting results are returned, this is a finding.

## Group: SRG-OS-000067-GPOS-00035

**Group ID:** `V-261342`

### Rule: SLEM 5, for PKI-based authentication, must enforce authorized access to the corresponding private key.

**Rule ID:** `SV-261342r996488_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the private key is discovered, an attacker can use the key to authenticate as an authorized user and gain access to the network infrastructure. The cornerstone of the PKI is the private key used to encrypt or digitally sign information. If the private key is stolen, this will lead to the compromise of the authentication and nonrepudiation gained through PKI because the attacker can use the private key to digitally sign documents and pretend to be the authorized user. Both the holders of a digital certificate and the issuing authority must protect the computers, storage devices, or whatever they use to keep the private keys.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH private key files have a passcode. For each private key stored on the system, use the following command (with the example of "/etc/ssh/ssh_host_dsa_key"): > ssh-keygen -y -f /etc/ssh/ssh_host_dsa_key Load key "/etc/ssh/ssh_host_dsa_key": Permission denied If the contents of any key are displayed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261343`

### Rule: There must be no .shosts files on SLEM 5.

**Rule ID:** `SV-261343r996489_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The .shosts files are used to configure host-based authentication for individual users or the system via SSH. Host-based authentication is not sufficient for preventing unauthorized access to the system as it does not require interactive identification and authentication of a connection request or for the use of two-factor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there are no ".shosts" files on SLEM 5 with the following command: > sudo find / \( -path /.snapshots -o -path /sys -o -path /proc \) -prune -o -name '.shosts' -print If any ".shosts" files are found on the system, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261344`

### Rule: There must be no shosts.equiv files on SLEM 5.

**Rule ID:** `SV-261344r996490_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The shosts.equiv files are used to configure host-based authentication for the system via SSH. Host-based authentication is not sufficient for preventing unauthorized access to the system, as it does not require interactive identification and authentication of a connection request, or for the use of two-factor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there are no "shosts.equiv" files on SLEM 5 with the following command: > sudo find /etc -name shosts.equiv If any "shosts.equiv" files are found on the system, this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-261345`

### Rule: SLEM 5 must not allow unattended or automatic logon via the graphical user interface (GUI).

**Rule ID:** `SV-261345r996493_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Failure to restrict system access to authenticated users negatively impacts SLEM 5 security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If a graphical user interface is not installed, this requirement is not applicable. Verify SLEM 5 does not allow unattended or automatic logon via the GUI. Check that unattended or automatic login is disabled with the following commands: > grep -i ^DISPLAYMANAGER_AUTOLOGIN /etc/sysconfig/displaymanager DISPLAYMANAGER_AUTOLOGIN="" > grep -i ^DISPLAYMANAGER_PASSWORD_LESS_LOGIN /etc/sysconfig/displaymanager DISPLAYMANAGER_PASSWORD_LESS_LOGIN="no" If the "DISPLAYMANAGER_AUTOLOGIN" parameter includes a username or the "DISPLAYMANAGER_PASSWORD_LESS_LOGIN" is not set to "no", this is a finding.

## Group: SRG-OS-000299-GPOS-00117

**Group ID:** `V-261346`

### Rule: SLEM 5 wireless network adapters must be disabled unless approved and documented.

**Rule ID:** `SV-261346r996496_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of communications with wireless peripherals, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read, altered, or used to compromise SLEM 5. This requirement applies to wireless peripheral technologies (e.g., wireless mice, keyboards, displays, etc.) used with a SLEM 5. Wireless peripherals (e.g., Wi-Fi/Bluetooth/IR keyboards, mice, pointing devices, and Near Field Communications [NFC]) present a unique challenge by creating an open, unsecured port on a computer. Wireless peripherals must meet DOD requirements for wireless data transmission and be approved for use by the AO. Even though some wireless peripherals, such as mice and pointing devices, do not ordinarily carry information that need to be protected, modification of communications with these wireless peripherals may be used to compromise SLEM 5. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of communications with wireless peripherals can be accomplished by physical means (e.g., employing physical barriers to wireless radio frequencies) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. If the wireless peripheral is only passing telemetry data, encryption of the data may not be required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLEM 5 has no wireless network adapters enabled with the following command: > sudo wicked show all ... wlan0 up link: #3, state up, mtu 1500 type: wireless, hwaddr 06:00:00:00:00:02 config: wicked:xml:/etc/wicked/ifconfig/wlan0.xml leases: ipv4 dhcp granted addr: ipv4 10.0.0.101/16 [dhcp] route: ipv4 default via 10.0.0.1 proto dhcp If a wireless interface is configured and has not been documented and approved by the AO, this is a finding.

## Group: SRG-OS-000378-GPOS-00163

**Group ID:** `V-261347`

### Rule: SLEM 5 must disable the USB mass storage kernel module.

**Rule ID:** `SV-261347r996498_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without identifying devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Peripherals include but are not limited to such devices as flash drives, external storage, and printers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 does not automount USB mass storage devices when connected to the host with the following command: > grep usb-storage /etc/modprobe.d/50-blacklist.conf blacklist usb-storage If the line is commented out or the line is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261348`

### Rule: All SLEM 5 local interactive user accounts, upon creation, must be assigned a home directory.

**Rule ID:** `SV-261348r996500_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If local interactive users are not assigned a valid home directory, there is no place for the storage and control of files they should own.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all SLEM 5 local interactive users on the system are assigned a home directory upon creation with the following command: > grep -i create_home /etc/login.defs CREATE_HOME yes If the "CREATE_HOME" parameter is not set to "yes", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-261349`

### Rule: SLEM 5 default permissions must be defined in such a way that all authenticated users can only read and modify their own files.

**Rule ID:** `SV-261349r996502_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the most restrictive default permissions ensures that when new accounts are created, they do not have unnecessary access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 defines default permissions for all authenticated users in such a way that the users can only read and modify their own files with the following command: > grep -i "^umask" /etc/login.defs UMASK 077 If the "UMASK" variable is set to "000", the severity is raised to a CAT I and this is a finding. If the value of "UMASK" is not set to "077", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-261350`

### Rule: SLEM 5 shadow password suite must be configured to enforce a delay of at least five seconds between logon prompts following a failed logon attempt.

**Rule ID:** `SV-261350r996504_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of logon attempts over a certain time interval reduces the chances that an unauthorized user may gain access to an account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 enforces a delay of at least five seconds between logon prompts following a failed logon attempt with the following command: > grep -i fail_delay /etc/login.defs FAIL_DELAY 5 If the value of "FAIL_DELAY" is not set to "5" or greater, the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261351`

### Rule: All SLEM 5 local interactive users must have a home directory assigned in the /etc/passwd file.

**Rule ID:** `SV-261351r996506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If local interactive users are not assigned a valid home directory, there is no place for the storage and control of files they should own.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 local interactive users on the system have a home directory assigned with the following command: > sudo pwck -r user 'smithj': directory '/home/smithj' does not exist Ask the system administrator (SA) if any users found without home directories are local interactive users. If the SA is unable to provide a response, check for users with a User Identifier (UID) of 1000 or greater with the following command: > awk -F: '($3>=1000)&&($1!="nobody"){print $1 ":" $3}' /etc/passwd If any interactive users do not have a home directory assigned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261352`

### Rule: All SLEM 5 local interactive user home directories defined in the /etc/passwd file must exist.

**Rule ID:** `SV-261352r996862_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a local interactive user has a home directory defined that does not exist, the user may be given access to the / directory as the current working directory upon logon. This could create a denial of service (DoS) because the user would not be able to access their logon configuration files, and it may give them visibility to system files they normally would not be able to access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the assigned home directory of all SLEM 5 local interactive users on the system exists. Check the home directory assignment for all local interactive nonprivileged users on the system with the following command: > awk -F: '($3>=1000)&&($7 !~ /nologin/){print $1, $6}' /etc/passwd smithj /home/smithj Note: This may miss interactive users that have been assigned a privileged User Identifier (UID). Evidence of interactive use may be obtained from a number of log files containing system logon information. Check that all referenced home directories exist with the following command: > sudo pwck -r user 'smithj': directory '/home/smithj' does not exist If any home directories referenced in "/etc/passwd" are returned as not defined, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261353`

### Rule: All SLEM 5 local interactive user initialization files executable search paths must contain only paths that resolve to the users' home directory.

**Rule ID:** `SV-261353r996512_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The executable search path (typically the PATH environment variable) contains a list of directories for the shell to search to find executables. If this path includes the current working directory (other than the user's home directory), executables in these directories may be executed instead of system commands. This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon or two consecutive colons, this is interpreted as the current working directory. If deviations from the default system search path for the local interactive user are required, they must be documented with the information system security officer (ISSO).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all SLEM 5 local interactive user initialization files executable search path statements do not contain statements that will reference a working directory other than the user's home directory with the following command: Note: The example will be for the user "smithj", who has a home directory of "/home/smithj". > sudo grep -i path= /home/smithj/.* /home/smithj/.bash_profile:PATH=$PATH:$HOME/.local/bin:$HOME/bin If any local interactive user initialization files have executable search path statements that include directories outside of their home directory, and the additional path statements are not documented with the ISSO as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261354`

### Rule: All SLEM 5 local initialization files must not execute world-writable programs.

**Rule ID:** `SV-261354r996514_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If user start-up files execute world-writable programs, especially in unprotected directories, they could be maliciously modified to destroy user files or otherwise compromise the system at the user level. If the system is compromised at the user level, it is easier to elevate privileges to eventually compromise the system at the root and network level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLEM 5 local initialization files do not execute world-writable programs with the following command: > sudo find / -xdev -perm -002 -type f -exec ls -ld {} \; For all files listed, check for their presence in the local initialization files with the following command: Note: The example will be for a system that is configured to create users' home directories in the "/home" directory. > sudo find /home/* -maxdepth 1 -type f -name \.\* -exec grep -H <file > {} \; If any local initialization files are found to reference world-writable files, this is a finding.

## Group: SRG-OS-000123-GPOS-00064

**Group ID:** `V-261355`

### Rule: SLEM 5 must automatically expire temporary accounts within 72 hours.

**Rule ID:** `SV-261355r996516_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Temporary accounts are privileged or nonprivileged accounts established during pressing circumstances, such as new software or hardware configuration or an incident response, where the need for prompt account activation requires bypassing normal account authorization procedures. If any inactive temporary accounts are left enabled on the system and are not either manually removed or automatically expired within 72 hours, the security posture of the system will be degraded and exposed to exploitation by unauthorized users or insider threat actors. Temporary accounts are different from emergency accounts. Emergency accounts, also known as "last resort" or "break glass" accounts, are local logon accounts enabled on the system for emergency use by authorized system administrators to manage a system when standard logon methods are failing or not available. Emergency accounts are not subject to manual removal or scheduled expiration requirements. The automatic expiration of temporary accounts may be extended as needed by the circumstances, but it must not be extended indefinitely. A documented permanent account should be established for privileged users who need long-term maintenance accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify temporary accounts have been provisioned with an expiration date of 72 hours with the following command: > sudo chage -l <temporary_account_name> | grep -E '(Password|Account) expires' If any temporary accounts have no expiration date set or do not expire within 72 hours, this is a finding.

## Group: SRG-OS-000123-GPOS-00064

**Group ID:** `V-261356`

### Rule: SLEM 5 must never automatically remove or disable emergency administrator accounts.

**Rule ID:** `SV-261356r996518_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Emergency administrator accounts, also known as "last resort" or "break glass" accounts, are local logon accounts enabled on the system for emergency use by authorized system administrators to manage a system when standard logon methods are failing or not available. Emergency accounts are not subject to manual removal or scheduled expiration requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 is configured such that emergency administrator accounts are never automatically removed or disabled with the following command: Note: Root is typically the "account of last resort" on a system and is also used as the example emergency administrator account. If another account is being used as the emergency administrator account, the command should be used against that account. > sudo chage -l <emergency_administrator_account_name> | grep -E '(Password|Account) expires' Password expires: never Account expires: never If "Password expires" or "Account expires" is set to anything other than "never", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261357`

### Rule: SLEM 5 must not have unnecessary accounts.

**Rule ID:** `SV-261357r996521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accounts providing no operational purpose provide additional opportunities for system compromise. Unnecessary accounts include user accounts for individuals not requiring access to the system and application accounts for applications not installed on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all SLEM 5 accounts are assigned to an active system, application, or user account with the following command: > more /etc/passwd root:x:0:0:root:/root:/bin/bash ... games:x:12:100:Games account:/var/games:/bin/bash Obtain the list of authorized system accounts from the information system security officer (ISSO). If the accounts on the system do not match the provided documentation, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261358`

### Rule: SLEM 5 must not have unnecessary account capabilities.

**Rule ID:** `SV-261358r996829_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accounts providing no operational purpose provide additional opportunities for system compromise. Therefore all necessary noninteractive accounts should not have an interactive shell assigned to them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all noninteractive SLEM 5 accounts do not have an interactive shell assigned to them with the following command: Check the system accounts on the system. > awk -F: '($7 !~ "/sbin/nologin" && $7 !~ "/bin/false"){print $1 ":" $3 ":" $7}' /etc/passwd root:0:/bin/bash nobody:65534:/bin/bash Obtain the list of authorized system accounts from the information system security officer (ISSO). If noninteractive accounts such as "games" or "nobody" are listed with an interactive shell, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261359`

### Rule: SLEM 5 root account must be the only account with unrestricted access to the system.

**Rule ID:** `SV-261359r996526_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account other than root also has a User Identifier (UID) of "0", it has root authority, giving that account unrestricted access to the entire SLEM 5. Multiple accounts with a UID of "0" afford an opportunity for potential intruders to guess a password for a privileged account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLEM 5 root account is the only account with unrestricted access to the system with the following command: > awk -F: '$3 == 0 {print $1}' /etc/passwd root If any accounts other than root are listed, this is a finding.

## Group: SRG-OS-000118-GPOS-00060

**Group ID:** `V-261360`

### Rule: SLEM 5 must disable account identifiers (individuals, groups, roles, and devices) after 35 days of inactivity after password expiration.

**Rule ID:** `SV-261360r996529_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. SLEM 5 must track periods of inactivity and disable application identifiers after 35 days of inactivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 disables account identifiers after 35 days of inactivity after the password expiration with the following command: > sudo grep -i '^inactive' /etc/default/useradd INACTIVE=35 If the value for "INACTIVE" is not set to a value greater than "0" and less than or equal to "35", if the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-261361`

### Rule: SLEM 5 must not have duplicate User IDs (UIDs) for interactive users.

**Rule ID:** `SV-261361r996530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, interactive users must be identified and authenticated to prevent potential misuse and compromise of the system. Interactive users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Interactive users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 contains no duplicate UIDs for interactive users with the following command: > awk -F ":" 'list[$3]++{print $1, $3}' /etc/passwd If output is produced, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261362`

### Rule: SLEM 5 must display the date and time of the last successful account logon upon logon.

**Rule ID:** `SV-261362r996533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Providing users with feedback on when account accesses last occurred facilitates user recognition and reporting of unauthorized account use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 users are provided with feedback on when account accesses last occurred with the following command: > grep pam_lastlog /etc/pam.d/login session required pam_lastlog.so showfailed If "pam_lastlog" is missing from "/etc/pam.d/login" file, the "silent" option is present, the second column value different from "requisite", or the returned line is commented out, this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-261363`

### Rule: SLEM 5 must initiate a session lock after a 15-minute period of inactivity.

**Rule ID:** `SV-261363r996536_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the users to manually lock their SLEM 5 session prior to vacating the vicinity, SLEM 5 needs to be able to identify when a user's session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 must initiate a session logout after a 15-minute period of inactivity for all connection type with the following command: > cat /etc/profile.d/autologout.sh TMOUT=900 readonly TMOUT export TMOUT If the file "/etc/profile.d/autologout.sh" does not exist or the output from the function call is not exactly the same, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-261364`

### Rule: SLEM 5 must lock an account after three consecutive invalid access attempts.

**Rule ID:** `SV-261364r996863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed access attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account. The pam_tally2.so module maintains a count of attempted accesses. This includes username entry into a logon field as well as password entry. With counting access attempts, it is possible to lock an account without presenting a password into the password field. This should be taken into consideration as it poses as an avenue for denial of service (DoS).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 locks a user account after three consecutive failed access attempts until the locked account is released by an administrator with the following command: > grep pam_tally2.so /etc/pam.d/common-auth auth required pam_tally2.so onerr=fail deny=3 If "deny" set to a value other than "1", "2", or "3", if "onerr=fail" is missing, if the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-261365`

### Rule: SLEM 5 must enforce a delay of at least five seconds between logon prompts following a failed logon attempt via pluggable authentication modules (PAM).

**Rule ID:** `SV-261365r996541_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of logon attempts over a certain time interval reduces the chances that an unauthorized user may gain access to an account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 enforces a delay of at least five seconds between logon prompts following a failed logon attempt with the following command: > grep pam_faildelay /etc/pam.d/common-auth auth required pam_faildelay.so delay=5000000 If the value of "delay" is not set to "5000000" or greater, "delay" is missing, the line is commented out, or the "pam_faildelay" line is missing completely, this is a finding.

## Group: SRG-OS-000027-GPOS-00008

**Group ID:** `V-261367`

### Rule: SLEM 5 must limit the number of concurrent sessions to 10 for all accounts and/or account types.

**Rule ID:** `SV-261367r996839_rule`
**Severity:** low

**Description:**
<VulnDiscussion>SLEM 5 management includes the ability to control the number of users and user sessions that use a SLEM 5. Limiting the number of allowed users and sessions per user is helpful in reducing the risks related to denial-of-service (DoS) attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based on mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 limits the number of concurrent sessions to 10 for all accounts and/or account types with the following command: > grep "maxlogins" /etc/security/limits.conf * hard maxlogins 10 If the "maxlogins" does not have a value of "10" or less, is commented out, or is missing, this is a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-261368`

### Rule: SLEM 5 must have policycoreutils package installed.

**Rule ID:** `SV-261368r996548_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. Policycoreutils contains the policy core utilities that are required for basic operation of an SELinux-enabled system. These utilities include load_policy to load SELinux policies, setfile to label filesystems, newrole to switch roles, and run_init to run /etc/init.d scripts in the proper context.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 has the policycoreutils package installed with the following command: > sudo zypper search -i policycoreutils I | policycoreutils | SELinux policy core utilities | package If the policycoreutils package is not installed, this is a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-261369`

### Rule: SLEM 5 must use a Linux Security Module configured to enforce limits on system services.

**Rule ID:** `SV-261369r996549_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. This requirement applies to operating systems performing security function verification/testing and/or systems and environments that require this functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "SELinux" is active and in "Enforcing" mode with the following command: > sudo getenforce Enforcing If "SELinux" is not in "Enforcing" mode, this is a finding.

## Group: SRG-OS-000445-GPOS-00199

**Group ID:** `V-261370`

### Rule: SLEM 5 must enable the SELinux targeted policy.

**Rule ID:** `SV-261370r996551_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. This requirement applies to operating systems performing security function verification/testing and/or systems and environments that require this functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "SELinux" is active and enforcing the targeted policy with the following command: > sudo sestatus SELinux status: enabled SELinuxfs mount: /sys/fs/selinux SELinux root directory: /etc/selinux Loaded policy name: targeted Current mode: enforcing Mode from config file: enforcing Policy MLS status: enabled Policy deny_unknown status: allowed Memory protection checking: actual (secure) Max kernel policy version: 33 If the "Loaded policy name" is not set to "targeted", this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-261371`

### Rule: SLEM 5 must prevent nonprivileged users from executing privileged functions, including disabling, circumventing, or altering implemented security safeguards/countermeasures.

**Rule ID:** `SV-261371r996554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing nonprivileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Privileged functions include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Nonprivileged users are individuals who do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from nonprivileged users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 prevents nonprivileged users from executing privileged functions, including disabling, circumventing, or altering implemented security safeguards/countermeasures. Obtain a list of authorized users (other than system administrator and guest accounts) for the system. Check the list against the system with the following command: > sudo semanage login -l | more Login Name SELinux User MLS/MCS Range Service __default__ user_u s0-s0:c0.c1023 * root unconfined_u s0-s0:c0.c1023 * system_u system_u s0-s0:c0.c1023 * joe staff_u s0-s0:c0.c1023 * All administrators must be mapped to the "sysadm_u", "staff_u", or an appropriately tailored confined role as defined by the organization. All authorized nonadministrative users must be mapped to the "user_u" role. If any interactive users are not mapped in this way, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261372`

### Rule: SLEM 5 must use the invoking user's password for privilege escalation when using "sudo".

**Rule ID:** `SV-261372r996556_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The sudoers security policy requires that users authenticate themselves before they can use sudo. When sudoers requires authentication, it validates the invoking user's credentials. If the rootpw, targetpw, or runaspw flags are defined and not disabled, by default the operating system will prompt the invoking user for the "root" user password. For more information on each of the listed configurations, reference the sudoers(5) manual page.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the sudoers security policy is configured to use the invoking user's password for privilege escalation with the following command: > sudo egrep -ir '(rootpw|targetpw|runaspw)' /etc/sudoers /etc/sudoers.d* | grep -v '#' /etc/sudoers:Defaults !targetpw /etc/sudoers:Defaults !rootpw /etc/sudoers:Defaults !runaspw If "Defaults" types are not defined for "!targetpw", "!rootpw", and "!runaspw", there are conflicting results between files, this is a finding.

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-261373`

### Rule: SLEM 5 must reauthenticate users when changing authenticators, roles, or escalating privileges.

**Rule ID:** `SV-261373r1050789_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When SLEM 5 provides the capability to change user authenticators, change security roles, or escalate a functional capability, it is critical the user reauthenticate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLEM 5 requires reauthentication when changing authenticators, roles, or escalating privileges with the following command: > sudo egrep -i '(nopasswd|!authenticate)' /etc/sudoers If any uncommented lines containing "!authenticate", or "NOPASSWD" are returned and active accounts on the system have valid passwords, this is a finding.

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-261374`

### Rule: SLEM 5 must require reauthentication when using the "sudo" command.

**Rule ID:** `SV-261374r1050789_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the organization requires the user to reauthenticate when using the "sudo" command. If the value is set to an integer less than 0, the user's time stamp will not expire and the user will not have to reauthenticate for privileged actions until the user's session is terminated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 requires reauthentication when using the "sudo" command to elevate privileges with the following command: > sudo grep -ir 'timestamp_timeout' /etc/sudoers /etc/sudoers.d /etc/sudoers:Defaults timestamp_timeout=0 If "timestamp_timeout" is set to a negative number, is commented out, conflicting results are returned, or no results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261375`

### Rule: SLEM 5 must restrict privilege elevation to authorized personnel.

**Rule ID:** `SV-261375r996562_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The sudo command allows a user to execute programs with elevated (administrator) privileges. It prompts the user for their password and confirms the request to execute a command by checking a file, called sudoers. If the "sudoers" file is not configured correctly, any user defined on the system can initiate privileged actions on the target system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "sudoers" file restricts sudo access to authorized personnel with the following command: > sudo grep -iw 'ALL' /etc/sudoers /etc/sudoers.d/* root ALL=(ALL) ALL If "ALL ALL=(ALL) ALL" or "ALL ALL=(ALL:ALL) ALL" entries are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261376`

### Rule: SLEM 5 must specify the default "include" directory for the /etc/sudoers file.

**Rule ID:** `SV-261376r996564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "sudo" command allows authorized users to run programs (including shells) as other users, system users, and root. The "/etc/sudoers" file is used to configure authorized "sudo" users as well as the programs they are allowed to run. Some configuration options in the "/etc/sudoers" file allow configured users to run programs without reauthenticating. Use of these configuration options makes it easier for one compromised account to be used to compromise other accounts. It is possible to include other sudoers files from within the sudoers file currently being parsed using the @include and @includedir directives. For compatibility with sudo versions prior to 1.9.1, #include and #includedir are also accepted. When sudo reaches this line it will suspend processing of the current file (/etc/sudoers) and switch to the specified file/directory. Once the end of the included file(s) is reached, the rest of /etc/sudoers will be processed. Files that are included may themselves include other files. A hard limit of 128 nested include files is enforced to prevent include file loops.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 specifies only the default "include" directory for the /etc/sudoers file, and does not have nested "include" files or directories within the /etc/sudoers.d directory with the following command: Note: If the "include" and "includedir" directives are not present in the /etc/sudoers file, this requirement is not applicable. > sudo find /etc/sudoers /etc/sudoers.d -type f -exec grep -H "[#@]include" {} + /etc/sudoers:@includedir /etc/sudoers.d If the results are not "/etc/sudoers.d" or additional files or directories are specified, this is a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-261377`

### Rule: SLEM 5 must enforce passwords that contain at least one uppercase character.

**Rule ID:** `SV-261377r996566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 enforces password complexity by requiring at least one uppercase character with the following command: > grep pam_cracklib.so /etc/pam.d/common-password password requisite pam_cracklib.so ucredit=-1 If the value for "ucredit" is not "-1", if "ucredit" is missing from the line, the second column value different from "requisite", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000070-GPOS-00038

**Group ID:** `V-261378`

### Rule: SLEM 5 must enforce passwords that contain at least one lowercase character.

**Rule ID:** `SV-261378r996568_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 enforces password complexity by requiring at least one lower character with the following command: > grep pam_cracklib.so /etc/pam.d/common-password password requisite pam_cracklib.so lcredit=-1 If the value for "lcredit" is not "-1", if "lcredit" is missing from the line, the second column value different from "requisite", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000071-GPOS-00039

**Group ID:** `V-261379`

### Rule: SLEM 5 must enforce passwords that contain at least one numeric character.

**Rule ID:** `SV-261379r996570_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 enforces password complexity by requiring at least one numeric character with the following command: > grep pam_cracklib.so /etc/pam.d/common-password password requisite pam_cracklib.so dcredit=-1 If the value for "dcredit" is not "-1", if "dcredit" is missing from the line, the second column value different from "requisite", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000266-GPOS-00101

**Group ID:** `V-261380`

### Rule: SLEM 5 must enforce passwords that contain at least one special character.

**Rule ID:** `SV-261380r996572_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps increase the time and resources required to compromise the password. Password complexity or strength is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor in determining how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Special characters are not alphanumeric. Examples include: ~ ! @ # $ % ^ *.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 enforces password complexity by requiring at least one special character with the following command: > grep pam_cracklib.so /etc/pam.d/common-password password requisite pam_cracklib.so ocredit=-1 If the value for "ocredit" is not "-1", if "ucredit" is missing from the line, the second column value different from "requisite", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-261381`

### Rule: SLEM 5 must prevent the use of dictionary words for passwords.

**Rule ID:** `SV-261381r996574_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SLEM 5 allows the user to select passwords based on dictionary words, this increases the chances of password compromise by increasing the opportunity for successful guesses and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 prevents the use of dictionary words for passwords with the following command: > grep pam_cracklib.so /etc/pam.d/common-password password requisite pam_cracklib.so If the second column value is different from "requisite", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-261382`

### Rule: SLEM 5 must employ passwords with a minimum of 15 characters.

**Rule ID:** `SV-261382r996577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps determine strength and how long it takes to crack a password. Use of more characters in a password helps exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 enforces a minimum 15-character password length with the following command: > grep pam_cracklib.so /etc/pam.d/common-password password requisite pam_cracklib.so minlen=15 If the value for "minlen" is not "15" or greater, the "minlen" option is missing from the line, the second column has a value different from "requisite", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-261383`

### Rule: SLEM 5 must require the change of at least eight of the total number of characters when passwords are changed.

**Rule ID:** `SV-261383r996580_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SLEM 5 allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 requires at least eight characters be changed between the old and new passwords during a password change with the following command: > grep pam_cracklib.so /etc/pam.d/common-password password requisite pam_cracklib.so difok=8 If the value for "difok" is not "8" or greater, if "difok" is missing from the line, the second column value different from "requisite", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000077-GPOS-00045

**Group ID:** `V-261384`

### Rule: SLEM 5 must not allow passwords to be reused for a minimum of five generations.

**Rule ID:** `SV-261384r996583_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 prohibits the reuse of a password for a minimum of five generations with the following command: > grep pam_pwhistory.so /etc/pam.d/common-password password requisite pam_pwhistory.so remember=5 use_authtok If the value for "remember" is not "5" or greater, if the "remember" option is missing from the line, if the "use_authtok" option is missing, if the second column has a value different from "requisite", if the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-261385`

### Rule: SLEM 5 must configure the Linux Pluggable Authentication Modules (PAM) to only store encrypted representations of passwords.

**Rule ID:** `SV-261385r996586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 configures the Linux PAM to only store encrypted representations of passwords with the following command: > grep pam_unix.so /etc/pam.d/common-password password required pam_unix.so sha512 If the value "sha512" is not present in the line, the second column value is different from "requisite", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261386`

### Rule: SLEM 5 must not be configured to allow blank or null passwords.

**Rule ID:** `SV-261386r996587_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 is not configured to allow blank or null passwords with the following command: > grep pam_unix.so /etc/pam.d/* | grep nullok If this produces any output, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261387`

### Rule: SLEM 5 must not have accounts configured with blank or null passwords.

**Rule ID:** `SV-261387r996588_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log on and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the "/etc/shadow" file for blank passwords with the following command: > sudo awk -F: '!$2 {print $1}' /etc/shadow If the command returns any results, this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-261388`

### Rule: SLEM 5 must employ user passwords with a minimum lifetime of 24 hours (one day).

**Rule ID:** `SV-261388r996591_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 enforces a minimum time period between password changes for each user account of one day or greater with the following command: > sudo awk -F: '$4 < 1 {print $1 ":" $4}' /etc/shadow smithj:1 If any results are returned that are not associated with a system account, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-261389`

### Rule: SLEM 5 must employ user passwords with a maximum lifetime of 60 days.

**Rule ID:** `SV-261389r1038967_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If SLEM 5 does not limit the lifetime of passwords and force users to change their passwords, there is the risk that SLEM 5 passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLEM 5 enforces a maximum user password age of 60 days or less with the following command: > sudo awk -F: '$5 > 60 || $5 == "" {print $1 ":" $5}' /etc/shadow If any results are returned that are not associated with a system account, this is a finding.

## Group: SRG-OS-000077-GPOS-00045

**Group ID:** `V-261390`

### Rule: SLEM 5 must employ a password history file.

**Rule ID:** `SV-261390r996595_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the password history file exists on SLEM 5 with the following command: > ls -al /etc/security/opasswd -rw------- 1 root root 82 Dec 7 19:41 /etc/security/opasswd If the "/etc/security/opasswd" file does not exist, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-261391`

### Rule: SLEM 5 must employ FIPS 140-2/140-3-approved cryptographic hashing algorithms for system authentication.

**Rule ID:** `SV-261391r996598_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The system must use a strong hashing algorithm to store the password. The system must use a sufficient number of hashing rounds to ensure the required level of entropy. Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 shadow password suite is configured to encrypt interactive user passwords using FIPS 140-2/140-3-approved cryptographic hash with the following command: > sudo cut -d: -f2 /etc/shadow $6$kcOnRq/5$NUEYPuyL.wghQwWssXRcLRFiiru7f5JPV6GaJhNC2aK5F3PZpE/BCCtwrxRc/AInKMNX3CdMw11m9STiql12f/ Password hashes "!" or "*" indicate inactive accounts not available for logon and are not evaluated. If any interactive user password hash does not begin with "$6", this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-261392`

### Rule: SLEM 5 shadow password suite must be configured to use a sufficient number of hashing rounds.

**Rule ID:** `SV-261392r996600_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The system must use a strong hashing algorithm to store the password. The system must use a sufficient number of hashing rounds to ensure the required level of entropy. Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 shadow password suite is configured to encrypt passwords using sufficient number of hashing rounds. > egrep "^SHA_CRYPT_" /etc/login.defs SHA_CRYPT_MIN_ROUNDS 5000 SHA_CRYPT_MAX_ROUNDS 5000 If only one of "SHA_CRYPT_MIN_ROUNDS" or "SHA_CRYPT_MAX_ROUNDS" is set, and this value is below "5000", this is a finding. If both "SHA_CRYPT_MIN_ROUNDS" and "SHA_CRYPT_MAX_ROUNDS" are set, and the highest value for either is below "5000", this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-261393`

### Rule: SLEM 5 must employ FIPS 140-2/140-3 approved cryptographic hashing algorithm for system authentication (login.defs).

**Rule ID:** `SV-261393r996602_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied on to provide confidentiality or integrity, and DOD data may be compromised. SLEM 5 using encryption are required to use FIPS 140-2/140-3 compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2/140-3 is the current standard for validating that mechanisms used to access cryptographic modules use authentication that meets DOD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general-purpose computing system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the shadow password suite configuration is set to encrypt password with a FIPS 140-2/140-3 approved cryptographic hashing algorithm with the following command: > grep "^ENCRYPT_METHOD " /etc/login.defs ENCRYPT_METHOD SHA512 If "ENCRYPT_METHOD" is not set to "SHA512", if any values other that "SHA512" are configured, or if no output is produced, this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-261394`

### Rule: SLEM 5 must be configured to create or update passwords with a minimum lifetime of 24 hours (one day).

**Rule ID:** `SV-261394r996604_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 creates or updates passwords with minimum password age of one day or greater with the following command: > grep '^PASS_MIN_DAYS' /etc/login.defs PASS_MIN_DAYS 1 If "PASS_MIN_DAYS" does not have a value of "1" or greater, the line is commented out, or no line is returned, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-261395`

### Rule: SLEM 5 must be configured to create or update passwords with a maximum lifetime of 60 days.

**Rule ID:** `SV-261395r1038967_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If SLEM 5 does not limit the lifetime of passwords and force users to change their passwords, there is the risk that SLEM 5 passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLEM 5 is configured to create or update passwords with a maximum password age of 60 days or less with the following command: > grep '^PASS_MAX_DAYS' /etc/login.defs If "PASS_MAX_DAYS" is not set to a value of "60" or less, but greater than "0", the line is commented out, or no line is returned, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-261396`

### Rule: SLEM 5 must have the packages required for multifactor authentication to be installed.

**Rule ID:** `SV-261396r996610_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a Common Access Card (CAC) or token separate from the information system, ensures that even if the information system is compromised, that compromise will not affect credentials stored on the authentication device. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification (PIV) card and the DOD CAC. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., VPN, proxy capability). This does not apply to authentication for the purpose of configuring the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 has the packages required for multifactor authentication installed. Check for the presence of the packages required to support multifactor authentication with the following commands: > zypper info pam_pkcs11 | grep -i installed Installed: Yes > zypper info mozilla-nss | grep -i installed Installed: Yes > zypper info mozilla-nss-tools | grep -i installed Installed: Yes > zypper info pcsc-ccid | grep -i installed Installed: Yes > zypper info pcsc-lite | grep -i installed Installed: Yes > zypper info pcsc-tools | grep -i installed Installed: Yes > zypper info opensc | grep -i installed Installed: Yes > zypper info coolkey | grep -i installed Installed: Yes If any of the packages required for multifactor authentication are not installed, this is a finding.

## Group: SRG-OS-000068-GPOS-00036

**Group ID:** `V-261397`

### Rule: SLEM 5 must implement multifactor authentication for access to privileged accounts via pluggable authentication modules (PAM).

**Rule ID:** `SV-261397r996612_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a Common Access Card (CAC) or token that is separate from the information system, ensures that even if the information system is compromised, that compromise will not affect credentials stored on the authentication device. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification (PIV) card and the DOD CAC. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., VPN, proxy capability). This does not apply to authentication for the purpose of configuring the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 implements multifactor authentication for remote access to privileged accounts via PAM with the following command: > grep pam_pkcs11.so /etc/pam.d/common-auth auth sufficient pam_pkcs11.so If "pam_pkcs11.so" is not set in "/etc/pam.d/common-auth", or the line is commented out, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-261398`

### Rule: SLEM 5 must implement certificate status checking for multifactor authentication.

**Rule ID:** `SV-261398r996615_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a Common Access Card (CAC) or token separate from the information system, ensures credentials stored on the authentication device will not be affected if the information system is compromised. Multifactor solutions that require devices separate from information systems to gain access include hardware tokens providing time-based or challenge-response authenticators, and smart cards such as the U.S. Government Personal Identity Verification (PIV) card and the DOD CAC. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. This requirement only applies to components with device-specific functions, or for organizational users (e.g., VPN, proxy capability). This does not apply to authentication for the purpose of configuring the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 implements certificate status checking for multifactor authentication with the following command: > grep use_pkcs11_module /etc/pam_pkcs11/pam_pkcs11.conf | awk '/pkcs11_module coolkey {/,/}/' /etc/pam_pkcs11/pam_pkcs11.conf | grep cert_policy cert_policy = ca,ocsp_on,signature,crl_auto; If "cert_policy" is not set to include "ocsp", this is a finding.

## Group: SRG-OS-000383-GPOS-00166

**Group ID:** `V-261399`

### Rule: If Network Security Services (NSS) is being used by SLEM 5 it must prohibit the use of cached authentications after one day.

**Rule ID:** `SV-261399r996617_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cached authentication information is out of date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If NSS is used by SLEM 5, verify it prohibits the use of cached authentications after one day with the following command: Note: If NSS is not used on the operating system, this is not applicable. > sudo grep -i "memcache_timeout" /etc/sssd/sssd.conf memcache_timeout = 86400 If "memcache_timeout" has a value greater than "86400", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000383-GPOS-00166

**Group ID:** `V-261400`

### Rule: SLEM 5 must configure the Linux Pluggable Authentication Modules (PAM) to prohibit the use of cached offline authentications after one day.

**Rule ID:** `SV-261400r996619_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cached authentication information is out of date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLEM 5 PAM prohibits the use of cached off line authentications after one day with the following command: Note: If SSSD is not being used on the operating system, this is not applicable. > sudo grep "offline_credentials_expiration" /etc/sssd/sssd.conf offline_credentials_expiration = 1 If "offline_credentials_expiration" is not set to a value of "1", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-261401`

### Rule: SLEM 5, for PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

**Rule ID:** `SV-261401r996622_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 for PKI-based authentication had valid certificates by constructing a certification path (which includes status information) to an accepted trust anchor with the following command: > grep cert_policy /etc/pam_pkcs11/pam_pkcs11.conf cert_policy = ca,oscp_on,signature,crl_auto; If "cert_policy" is not set to include "ca" on all returned lines, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261402`

### Rule: SLEM 5 must be configured to not overwrite Pluggable Authentication Modules (PAM) configuration on package changes.

**Rule ID:** `SV-261402r996624_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "pam-config" command line utility automatically generates a system PAM configuration as packages are installed, updated, or removed from the system. "pam-config" removes configurations for PAM modules and parameters that it does not know about. It may render ineffective PAM configuration by the system administrator and thus impact system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 is configured to not overwrite PAM configuration on package changes with the following command: > find /etc/pam.d/ -type l -iname "common-*" If any results are returned, this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-261403`

### Rule: SLEM 5 must use a file integrity tool to verify correct operation of all security functions.

**Rule ID:** `SV-261403r996627_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly, and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. This requirement applies to SLEM 5 performing security function verification/testing and/or systems and environments that require this functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Advanced Intrusion Detection Environment (AIDE) is installed and verifies the correct operation of all security functions with the following command: > sudo zypper if aide | grep -i installed Installed: Yes If AIDE is not installed, ask the system administrator how file integrity checks are performed on the system. If there is no application installed to perform integrity checks, this is a finding. If AIDE is installed, check if it has been initialized with the following command: > sudo aide --check If the output is "Couldn't open file /var/lib/aide/aide.db for reading", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261404`

### Rule: SLEM 5 file integrity tool must be configured to verify Access Control Lists (ACLs).

**Rule ID:** `SV-261404r996629_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ACLs can provide permissions beyond those permitted through the file mode and must be verified by file integrity tools.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLEM 5 file integrity tool is configured to verify extended attributes. > sudo grep acl /etc/aide.conf All= p+i+n+u+g+s+m+S+sha512+acl+xattrs+selinux If the "acl" rule is not being used on all selection lines in the "/etc/aide.conf" file, or extended attributes are not being checked by another file integrity tool, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261405`

### Rule: SLEM 5 file integrity tool must be configured to verify extended attributes.

**Rule ID:** `SV-261405r996631_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Extended attributes in file systems are used to contain arbitrary data and file metadata with security implications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLEM 5 file integrity tool is configured to verify extended attributes. > sudo grep xattrs /etc/aide.conf All= p+i+n+u+g+s+m+S+sha512+acl+xattrs+selinux If the "xattrs" rule is not being used on all selection lines in the "/etc/aide.conf" file, or extended attributes are not being checked by another file integrity tool, this is a finding.

## Group: SRG-OS-000278-GPOS-00108

**Group ID:** `V-261406`

### Rule: SLEM 5 file integrity tool must be configured to protect the integrity of the audit tools.

**Rule ID:** `SV-261406r996634_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting the integrity of the tools used for auditing purposes is a critical step toward ensuring the integrity of audit information. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Audit tools include but are not limited to vendor-provided and open-source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. It is not uncommon for attackers to replace the audit tools or inject code into the existing tools to provide the capability to hide or erase system activity from the audit logs. To address this risk, audit tools must be cryptographically signed to provide the capability to identify when the audit tools have been modified, manipulated, or replaced. An example is a checksum hash of the file or files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLEM 5 file integrity tool is configured to protect the integrity of the audit tools. Check that AIDE is properly configured to protect the integrity of the audit tools by running the following command: > sudo grep /usr/sbin/au /etc/aide.conf /usr/sbin/auditctl p+i+n+u+g+s+b+acl+selinux+xattrs+sha512 /usr/sbin/auditd p+i+n+u+g+s+b+acl+selinux+xattrs+sha512 /usr/sbin/ausearch p+i+n+u+g+s+b+acl+selinux+xattrs+sha512 /usr/sbin/aureport p+i+n+u+g+s+b+acl+selinux+xattrs+sha512 /usr/sbin/autrace p+i+n+u+g+s+b+acl+selinux+xattrs+sha512 /usr/sbin/audispd p+i+n+u+g+s+b+acl+selinux+xattrs+sha512 /usr/sbin/augenrules p+i+n+u+g+s+b+acl+selinux+xattrs+sha512 If any of the seven lines do not appear as shown, are commented out, or are missing, this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-261407`

### Rule: Advanced Intrusion Detection Environment (AIDE) must verify the baseline SLEM 5 configuration at least weekly.

**Rule ID:** `SV-261407r996637_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to SLEM 5. Changes to SLEM 5 configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of SLEM 5. SLEM 5's information system security manager (ISSM)/information system security officer (ISSO) and system administrator (SA) must be notified via email and/or monitoring system trap when there is an unauthorized modification of a configuration item.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 checks the baseline configuration using AIDE for unauthorized changes at least once weekly with the following command: Note: A file integrity tool other than AIDE may be used, but the tool must be executed at least once per week. > sudo grep -R aide /etc/crontab /etc/cron.* /etc/crontab: 30 04 * * * root /usr/sbin/aide If the file integrity application does not exist, or a "crontab" file does not exist in "/etc/crontab", the "/etc/cron.daily" subdirectory, or "/etc/cron.weekly" subdirectory, this is a finding.

## Group: SRG-OS-000447-GPOS-00201

**Group ID:** `V-261408`

### Rule: SLEM 5 must notify the system administrator (SA) when Advanced Intrusion Detection Environment (AIDE) discovers anomalies in the operation of any security functions.

**Rule ID:** `SV-261408r996640_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If anomalies are not acted on, security functions may fail to secure the system. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. Notifications provided by information systems include messages to local computer consoles and/or hardware indications, such as lights. This capability must take into account operational requirements for availability for selecting an appropriate response. The organization may choose to shut down or restart the information system upon security function anomaly detection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 notifies the SA when AIDE discovers anomalies in the operation of any security functions. Note: A file integrity tool other than AIDE may be used, but the tool must be configured to notify the system administrator and/or ISSO if there is an anomaly. Verify the aide cron job sends an email when executed with the following command: > sudo grep -i "aide" /etc/cron.*/aide 0 0 * * * /usr/sbin/aide --check | /bin/mail -s "$HOSTNAME - Daily AIDE integrity check run" root@example_server_name.mil If the "aide" file does not exist under the "/etc/cron" directory structure or the cron job is not configured to execute a binary to send an email (such as "/bin/mail"), this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-261409`

### Rule: SLEM 5 must offload rsyslog messages for networked systems in real time and offload standalone systems at least weekly.

**Rule ID:** `SV-261409r996643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLEM 5 must offload syslog-ng messages for networked systems in real time and offload standalone systems at least weekly. For standalone hosts, verify with the system administrator that the log files are offloaded at least weekly. For networked systems, check that syslog-ng is sending log messages to a remote server with the following command: > sudo egrep "^destination logserver" /etc/syslog-ng/syslog-ng.conf syslog("10.10.10.10" transport("udp") port(514)); }; If any active message labels in the file do not have a line to send log messages to a remote server, this is a finding.

## Group: SRG-OS-000337-GPOS-00129

**Group ID:** `V-261410`

### Rule: SLEM 5 must have the auditing package installed.

**Rule ID:** `SV-261410r996645_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, the source of events, where events occurred, and the outcome of events, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in SLEM 5 audit logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured SLEM 5.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 auditing package is installed with the following command: > zypper info audit Name : audit Version : 2.8.5-3.2 Arch : X86_64 Vendor : SUSE LLC <https://www.suse.com> Installed Size : 646.2 KiB Installed : Yes (automatically) Status : up-to-date If the package "audit" is not installed on the system, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261411`

### Rule: SLEM 5 audit records must contain information to establish what type of events occurred, the source of events, where events occurred, and the outcome of events.

**Rule ID:** `SV-261411r996646_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, the source of events, where events occurred, and the outcome of events, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in SLEM 5 audit logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured SLEM 5.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 produces audit records with the following commands: > systemctl is-active auditd.service active > systemctl is-enabled auditd.service enabled If the service is not active or not enabled, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-261412`

### Rule: The audit-audispd-plugins package must be installed on SLEM 5.

**Rule ID:** `SV-261412r996649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. The auditd service does not include the ability to send audit records to a centralized server for management directly. However, it can use a plug-in for audit event multiplexor to pass audit records to a remote server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "audit-audispd-plugins" package is installed on SLEM 5 with the following command: > zypper info audit-audispd-plugins | grep Installed Installed : Yes If the "audit-audispd-plugins" package is not installed, this is a finding. Verify the "au-remote" plugin is enabled with the following command: > sudo grep -i active /etc/audisp/plugins.d/au-remote.conf active = yes If "active" is not set to "yes", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-261413`

### Rule: SLEM 5 must allocate audit record storage capacity to store at least one week of audit records when audit records are not immediately sent to a central audit record storage facility.

**Rule ID:** `SV-261413r996652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure SLEM 5 has a sufficient storage capacity in which to write the audit logs, SLEM 5 must be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial installation of SLEM 5.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 allocates audit record storage capacity to store at least one week of audit records when audit records are not immediately sent to a central audit record storage facility. Determine which partition the audit records are being written to with the following command: > sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Check the size of the partition that audit records are written to (with the example being /var/log/audit/) with the following command: > df -h /var/log/audit/ Filesystem Size Used Avail Use% Mounted on /dev/sda2 24G 10.4G 13.6G 43% /var If the audit records are not written to a partition made specifically for audit records (/var/log/audit is a separate partition), determine the amount of space being used by other files in the partition with the following command: > sudo du -sh <audit_partition> 1.8G /var/log/audit The partition size needed to capture a week of audit records is based on the activity level of the system and the total storage capacity available. If the audit record partition is not allocated sufficient storage capacity, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-261414`

### Rule: SLEM 5 auditd service must notify the system administrator (SA) and information system security officer (ISSO) immediately when audit storage capacity is 75 percent full.

**Rule ID:** `SV-261414r996654_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches 75 percent utilization, they are unable to plan for audit record storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if SLEM 5 auditd is configured to notify the SA and ISSO when the audit record storage volume reaches 75 percent of the storage capacity with the following command: > sudo grep -iw space_left /etc/audit/auditd.conf space_left = 25% If "space_left" is not set to "25%" or greater, this is a finding.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-261415`

### Rule: SLEM 5 audit system must take appropriate action when the audit storage volume is full.

**Rule ID:** `SV-261415r1038966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when SLEM 5 is at risk of failing to process audit logs as required, it takes action to mitigate the failure. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. Responses to audit failure depend on the nature of the failure mode. When availability is an overriding concern, other approved actions in response to an audit failure are as follows: 1) If the failure was caused by the lack of audit record storage capacity, SLEM 5 must continue generating audit records if possible (automatically restarting the audit service if necessary), overwriting the oldest audit records in a first-in-first-out manner. 2) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, SLEM 5 must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 takes the appropriate action when the audit storage volume is full using the following command: > sudo grep disk_full_action /etc/audit/auditd.conf disk_full_action = HALT If "disk_full_action" is not set to "HALT", "SYSLOG", or "SINGLE", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-261416`

### Rule: SLEM 5 must offload audit records onto a different system or media from the system being audited.

**Rule ID:** `SV-261416r996660_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify what action the audit system takes if it cannot offload audit records to a different system or storage media from SLEM 5 being audited. Check the action that the audit system takes in the event of a network failure with the following command: > sudo grep -i "network_failure_action" /etc/audisp/audisp-remote.conf network_failure_action = syslog If the "network_failure_action" option is not set to "syslog", "single", or "halt" or the line is commented out, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-261417`

### Rule: Audispd must take appropriate action when SLEM 5 audit storage is full.

**Rule ID:** `SV-261417r996662_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit system offloads audit records if SLEM 5 storage volume becomes full. Check that the records are properly offloaded to a remote server with the following command: > sudo grep -i "disk_full_action" /etc/audisp/audisp-remote.conf disk_full_action = syslog If "disk_full_action" is not set to "syslog", "single", or "halt" or the line is commented out, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-261418`

### Rule: SLEM 5 must protect audit rules from unauthorized modification.

**Rule ID:** `SV-261418r996665_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SLEM 5 protects audit rules from unauthorized modification with the following command: > grep -i audit /etc/permissions.local /var/log/audit root:root 600 /var/log/audit/audit.log root:root 600 /etc/audit/audit.rules root:root 640 /etc/audit/rules.d/audit.rules root:root 640 If the command does not return any output or all four lines as shown, this is a finding. Check that all of the audit information files and folders have the correct permissions with the following command: > sudo chkstat /etc/permissions.local If the command returns any output, this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-261419`

### Rule: SLEM 5 audit tools must have the proper permissions configured to protect against unauthorized access.

**Rule ID:** `SV-261419r996668_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information includes identifying and protecting the tools used to view and manipulate log data. Protecting audit tools is necessary to prevent unauthorized operation on audit information. SLEM 5 providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open-source audit tools needed to view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To protect from unauthorized access verify that SLEM 5 audit tools have the proper permissions configured in the permissions profile by using the following command: > grep "^/usr/sbin/au" /etc/permissions.local /usr/sbin/audispd root:root 750 /usr/sbin/auditctl root:root 750 /usr/sbin/auditd root:root 750 /usr/sbin/ausearch root:root 755 /usr/sbin/aureport root:root 755 /usr/sbin/autrace root:root 750 /usr/sbin/augenrules root:root 750 If the command does not return any output, this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-261420`

### Rule: SLEM 5 audit tools must have the proper permissions applied to protect against unauthorized access.

**Rule ID:** `SV-261420r996670_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information includes identifying and protecting the tools used to view and manipulate log data. Protecting audit tools is necessary to prevent unauthorized operation on audit information. SLEM 5 providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open-source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To protect from unauthorized access verify that SLEM 5 audit tools have the proper permissions applied from the permissions profile by using the following command: > sudo chkstat /etc/permissions.local If the command returns any output, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-261421`

### Rule: SLEM 5 audit event multiplexor must be configured to use Kerberos.

**Rule ID:** `SV-261421r996672_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Allowing devices and users to connect to or from the system without first authenticating them allows untrusted access and can lead to a compromise or attack. Audit events that may include sensitive data must be encrypted prior to transmission. Kerberos provides a mechanism to provide both authentication and encryption for audit event records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if SLEM 5 audit event multiplexor is configured to use Kerberos by running the following command: > sudo grep enable_krb5 /etc/audisp/audisp-remote.conf enable_krb5 = yes If "enable_krb5" is not set to "yes", or is commented out, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-261422`

### Rule: Audispd must offload audit records onto a different system or media from SLEM 5 being audited.

**Rule ID:** `SV-261422r996674_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "audispd" offloads audit records onto a different system or media from SLEM 5 being audited with the following command: > sudo grep remote_server /etc/audisp/audisp-remote.conf remote_server = 240.9.19.81 If "remote_server" is not set to an external server or media, or is commented out, this is a finding.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-261423`

### Rule: The information system security officer (ISSO) and system administrator (SA), at a minimum, must have mail aliases to be notified of a SLEM 5 audit processing failure.

**Rule ID:** `SV-261423r996677_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the administrators are notified in the event of a SLEM 5 audit processing failure with the following commands: > grep -i "^postmaster:" /etc/aliases postmaster: root If the above command does not return a value of "root", or the output is commented out, this is a finding. Verify the alias for root forwards to a monitored e-mail account: > grep -i "^root:" /etc/aliases root: person@server.mil If the alias for root does not forward to a monitored e-mail account, or the output is commented out, this is a finding.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-261424`

### Rule: The information system security officer (ISSO) and system administrator (SA), at a minimum, must be alerted of a SLEM 5 audit processing failure event.

**Rule ID:** `SV-261424r996679_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system is configured to send email to an account when it needs to notify an administrator with the following command: > sudo grep action_mail /etc/audit/auditd.conf action_mail_acct = root If the value of the "action_mail_acct" keyword is not set to "root" and/or other accounts for security personnel, the returned line is commented out, or the "action_mail_acct" keyword is missing, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261425`

### Rule: SLEM 5 must generate audit records for all uses of the "chacl" command.

**Rule ID:** `SV-261425r996682_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "chacl" command with the following command: > sudo auditctl -l | grep -w '/usr/bin/chacl' -a always,exit -S all -F path=/usr/bin/chacl -F perm=x -F auid>=1000 -F auid!=-1 -F key=prim_mod If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261426`

### Rule: SLEM 5 must generate audit records for all uses of the "chage" command.

**Rule ID:** `SV-261426r996685_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for any use of the "chage" command with the following command: > sudo auditctl -l | grep -w '/usr/bin/chage' -a always,exit -S all -F path=/usr/bin/chage -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-chage If the command does not return any output, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261427`

### Rule: SLEM 5 must generate audit records for all uses of the "chcon" command.

**Rule ID:** `SV-261427r996688_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "chcon" command with the following command: > sudo auditctl -l | grep -w '/usr/bin/chcon' -a always,exit -S all -F path=/usr/bin/chcon -F perm=x -F auid>=1000 -F auid!=-1 -F key=prim_mod If the command does not return any output, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261428`

### Rule: SLEM 5 must generate audit records for all uses of the "chfn" command.

**Rule ID:** `SV-261428r996691_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "chfn" command with the following command: > sudo auditctl -l | grep -w '/usr/bin/chfn' -a always,exit -S all -F path=/usr/bin/chfn -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-chfn If the command does not return any output or the returned line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261429`

### Rule: SLEM 5 must generate audit records for all uses of the "chmod" command.

**Rule ID:** `SV-261429r996694_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "chmod" command with the following command: > sudo auditctl -l | grep -w '/usr/bin/chmod' -a always,exit -S all -F path=/usr/bin/chmod -F perm=x -F auid>=1000 -F auid!=-1 -F key=prim_mod If the command does not return any output, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261430`

### Rule: SLEM 5 must generate audit records for a uses of the "chsh" command.

**Rule ID:** `SV-261430r996697_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "chsh" command with the following command: > sudo auditctl -l | grep -w '/usr/bin/chsh' -a always,exit -S all -F path=/usr/bin/chsh -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-chsh If the command does not return any output, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261431`

### Rule: SLEM 5 must generate audit records for all uses of the "crontab" command.

**Rule ID:** `SV-261431r996700_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for any use of the "crontab" command with the following command: > sudo auditctl -l | grep -w '/usr/bin/crontab' -a always,exit -S all -F path=/usr/bin/crontab -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-crontab If the command does not return any output, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261432`

### Rule: SLEM 5 must generate audit records for all uses of the "gpasswd" command.

**Rule ID:** `SV-261432r996703_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "gpasswd" command with the following command: > sudo auditctl -l | grep -w '/usr/bin/gpasswd' -a always,exit -S all -F path=/usr/bin/gpasswd -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-gpasswd If the command does not return any output, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261433`

### Rule: SLEM 5 must generate audit records for all uses of the "insmod" command.

**Rule ID:** `SV-261433r996706_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DOD has defined the following list of events for which SLEM 5 will provide an audit record generation capability: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 is generates an audit record for all uses of the "insmod" command with the following command: > sudo auditctl -l | grep -w '/sbin/insmod' -w /sbin/insmod -p x -k modules If the system is configured to audit the execution of the module management program "insmod", the command will return a line. If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261434`

### Rule: SLEM 5 must generate audit records for all uses of the "kmod" command.

**Rule ID:** `SV-261434r996709_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DOD has defined the following list of events for which SLEM 5 will provide an audit record generation capability: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "kmod" command with the following command: > sudo auditctl -l | grep -w '/usr/bin/kmod' -w /usr/bin/kmod -p x -k modules If the system is configured to audit the execution of the module management program "kmod", the command will return a line. If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261435`

### Rule: SLEM 5 must generate audit records for all uses of the "modprobe" command.

**Rule ID:** `SV-261435r996712_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DOD has defined the following list of events for which SLEM 5 will provide an audit record generation capability: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "modprobe" command with the following command: > sudo auditctl -l | grep -w '/sbin/modprobe' -w /sbin/modprobe -p x -k modules If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261436`

### Rule: SLEM 5 must generate audit records for all uses of the "newgrp" command.

**Rule ID:** `SV-261436r996715_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "newgrp" command with the following command: > sudo auditctl -l | grep -w '/usr/bin/newgrp' -a always,exit -S all -F path=/usr/bin/newgrp -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-newgrp If the command does not return any output, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261437`

### Rule: SLEM 5 must generate audit records for all uses of the "pam_timestamp_check" command.

**Rule ID:** `SV-261437r996718_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for any use of the "pam_timestamp_check" command with the following command: > sudo auditctl -l | grep -w '/sbin/pam_timestamp_check' -a always,exit -S all -F path=/sbin/pam_timestamp_check -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-pam_timestamp_check If the command does not return any output, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261438`

### Rule: SLEM 5 must generate audit records for all uses of the "passwd" command.

**Rule ID:** `SV-261438r996721_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "passwd" command with the following command: > sudo auditctl -l | grep -w '/usr/bin/passwd' -a always,exit -S all -F path=/usr/bin/passwd -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-passwd If the command does not return any output, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261439`

### Rule: SLEM 5 must generate audit records for all uses of the "rm" command.

**Rule ID:** `SV-261439r996724_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "rm" command with the following command: > sudo auditctl -l | grep -w '/usr/bin/rm' -a always,exit -S all -F path=/usr/bin/rm -F perm=x -F auid>=1000 -F auid!=-1 -F key=prim_mod If the command does not return any output, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261440`

### Rule: SLEM 5 must generate audit records for all uses of the "rmmod" command.

**Rule ID:** `SV-261440r996727_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DOD has defined the following list of events for which SLEM 5 will provide an audit record generation capability: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "rmmod" command with the following command: > sudo auditctl -l | grep -w '/sbin/rmmod' -w /sbin/rmmod -p x -k modules If the system is configured to audit the execution of the module management program "rmmod", the command will return a line. If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261441`

### Rule: SLEM 5 must generate audit records for all uses of the "setfacl" command.

**Rule ID:** `SV-261441r996730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "setfacl" command with the following command: > sudo auditctl -l | grep -w '/usr/bin/setfacl' -a always,exit -S all -F path=/usr/bin/setfacl -F perm=x -F auid>=1000 -F auid!=-1 -F key=prim_mod If the command does not return any output, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261442`

### Rule: SLEM 5 must generate audit records for all uses of the "ssh-agent" command.

**Rule ID:** `SV-261442r996733_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "ssh-agent" command with the following command: > sudo auditctl -l | grep -w '/usr/bin/ssh-agent' -a always,exit -S all -F path=/usr/bin/ssh-agent -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-ssh-agent If the command does not return any output or the returned line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261443`

### Rule: SLEM 5 must generate audit records for all uses of the "ssh-keysign" command.

**Rule ID:** `SV-261443r996736_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "ssh-keysign" command with the following command: > sudo auditctl -l | grep -w '/usr/lib/ssh/ssh-keysign' -a always,exit -S all -F path=/usr/lib/ssh/ssh-keysign -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-ssh-keysign If the command does not return any output, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261444`

### Rule: SLEM 5 must generate audit records for all uses of the "su" command.

**Rule ID:** `SV-261444r996739_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for any use of the "su" command with the following command: > sudo auditctl -l | grep -w '/usr/bin/su' -a always,exit -S all -F path=/usr/bin/su -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-priv_change If the command does not return any output or the returned line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261445`

### Rule: SLEM 5 must generate audit records for all uses of the "sudo" command.

**Rule ID:** `SV-261445r996742_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for any use of the "sudo" command with the following command: > sudo auditctl -l | grep -w '/usr/bin/sudo' -a always,exit -S all -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-sudo If the command does not return any output, or the returned line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261446`

### Rule: SLEM 5 must generate audit records for all uses of the "sudoedit" command.

**Rule ID:** `SV-261446r996745_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an audit record is generated for all uses of the "sudoedit" command with the following command: > sudo auditctl -l | grep -w '/usr/bin/sudoedit' -a always,exit -S all -F path=/usr/bin/sudoedit -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-sudoedit If the command does not return any output or the returned line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261447`

### Rule: SLEM 5 must generate audit records for all uses of the "unix_chkpwd" or "unix2_chkpwd" commands.

**Rule ID:** `SV-261447r996748_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for any use of the "unix_chkpwd" or "unix2_chkpwd" commands with the following command: > sudo auditctl -l | egrep -w "(unix_chkpwd|unix2_chkpwd)" -a always,exit -S all -F path=/sbin/unix_chkpwd -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-unix-chkpwd -a always,exit -S all -F path=/sbin/unix2_chkpwd -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-unix2-chkpwd If the command does not return any output, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261448`

### Rule: SLEM 5 must generate audit records for all uses of the "usermod" command.

**Rule ID:** `SV-261448r996751_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for any use of the "usermod" command with the following command: > sudo auditctl -l | grep -w '/usr/sbin/usermod' -a always,exit -S all -F path=/usr/sbin/usermod -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-usermod If the command does not return any output, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-261449`

### Rule: SLEM 5 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/group.

**Rule ID:** `SV-261449r996754_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply create a new account. Auditing account creation mitigates this risk. To address access requirements, SLEM 5 may be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record when modifications occur to the "/etc/group" file with the following command: > sudo auditctl -l | grep -w '/etc/group' -w /etc/group -p wa -k account_mod If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "-k" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-261450`

### Rule: SLEM 5 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/security/opasswd.

**Rule ID:** `SV-261450r996757_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply create a new account. Auditing account creation mitigates this risk. To address access requirements, SLEM 5 may be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record when modifications occur to the "/etc/security/opasswd" file with the following command: > sudo auditctl -l | grep -w '/etc/security/opasswd' -w /etc/security/opasswd -p wa -k account_mod If the command does not return a line that matches the example or the line is commented out, this is a finding. Notes: The "-k" allows for specifying an arbitrary identifier. The string following "-k" does not need to match the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-261451`

### Rule: SLEM 5 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/passwd.

**Rule ID:** `SV-261451r996760_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply create a new account. Auditing account creation mitigates this risk. To address access requirements, SLEM 5 may be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record when all modifications occur to the "/etc/passwd" file with the following command: > sudo auditctl -l | grep -w '/etc/passwd' -w /etc/passwd -p wa -k account_mod If the command does not return a line that matches the example or the line is commented out, this is a finding. Notes: The "-k" allows for specifying an arbitrary identifier. The string following "-k" does not need to match the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-261452`

### Rule: SLEM 5 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/shadow.

**Rule ID:** `SV-261452r996763_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply create a new account. Auditing account creation mitigates this risk. To address access requirements, SLEM 5 may be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record when modifications occur to the "/etc/shadow" file with the following command: > sudo auditctl -l | grep -w '/etc/shadow' -w /etc/shadow -p wa -k account_mod If the command does not return a line that matches the example or the line is commented out, this is a finding. Notes: The "-k" allows for specifying an arbitrary identifier. The string following "-k" does not need to match the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261453`

### Rule: SLEM 5 must generate audit records for all uses of the "chmod", "fchmod" and "fchmodat" system calls.

**Rule ID:** `SV-261453r996848_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is important to use syscall rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. However, the performance can be helped by combining syscalls into one rule whenever possible.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "chmod", "fchmod" and "fchmodat" system calls with the following command: > sudo auditctl -l | grep chmod -a always,exit -F arch=b32 -S chmod,fchmod,fchmodat -F auid>=1000 -F auid!=-1 -F key=perm_mod -a always,exit -F arch=b64 -S chmod,fchmod,fchmodat -F auid>=1000 -F auid!=-1 -F key=perm_mod If both the "b32" and "b64" audit rules are not defined for the "chmod", "fchmod", and "fchmodat" syscalls, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261454`

### Rule: SLEM 5 must generate audit records for all uses of the "chown", "fchown", "fchownat", and "lchown" system calls.

**Rule ID:** `SV-261454r996769_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary, since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining syscalls into one rule whenever possible.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "chown", "fchown", "fchownat", and "lchown" system calls with the following command: > sudo auditctl -l | grep chown -a always,exit -F arch=b32 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=-1 -F key=perm_mod -a always,exit -F arch=b64 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=-1 -F key=perm_mod If both the "b32" and "b64" audit rules are not defined for the "chown", "fchown", "fchownat", and "lchown" syscalls, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261455`

### Rule: SLEM 5 must generate audit records for all uses of the "creat", "open", "openat", "open_by_handle_at", "truncate", and "ftruncate" system calls.

**Rule ID:** `SV-261455r996772_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary, since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining syscalls into one rule whenever possible.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "creat", "open", "openat", "open_by_handle_at", "truncate", and "ftruncate" system calls with the following command: > sudo auditctl -l | grep 'open\|truncate\|creat' -a always,exit -F arch=b32 -S creat,open,openat,open_by_handle_at,truncate,ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=-1 -F key=perm_access -a always,exit -F arch=b64 -S creat,open,openat,open_by_handle_at,truncate,ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=-1 -F key=perm_access -a always,exit -F arch=b32 -S creat,open,openat,open_by_handle_at,truncate,ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=-1 -F key=perm_access -a always,exit -F arch=b64 -S creat,open,openat,open_by_handle_at,truncate,ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=-1 -F key=perm_access If both the "b32" and "b64" audit rules are not defined for the "creat", "open", "openat", "open_by_handle_at", "truncate", and "ftruncate" syscalls, this is a finding. If the output does not produce rules containing "-F exit=-EPERM", this is a finding. If the output does not produce rules containing "-F exit=-EACCES", this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261456`

### Rule: SLEM 5 must generate audit records for all uses of the "delete_module" system call.

**Rule ID:** `SV-261456r996775_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "delete_module" system call with the following command: > sudo auditctl -l | grep -w 'delete_module' -a always,exit -F arch=b32 -S delete_module -F auid>=1000 -F auid!=-1 -F key=unload_module -a always,exit -F arch=b64 -S delete_module -F auid>=1000 -F auid!=-1 -F key=unload_module If both the "b32" and "b64" audit rules are not defined for the "unload_module" syscall, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261457`

### Rule: SLEM 5 must generate audit records for all uses of the "init_module" and "finit_module" system calls.

**Rule ID:** `SV-261457r996778_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary, since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining syscalls into one rule whenever possible.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "init_module" and "finit_module" system calls with the following command: > sudo auditctl -l | grep init_module -a always,exit -F arch=b32 -S init_module,finit_module -F auid>=1000 -F auid!=-1 -F key=moduleload -a always,exit -F arch=b64 -S init_module,finit_module -F auid>=1000 -F auid!=-1 -F key=moduleload If both the "b32" and "b64" audit rules are not defined for the init_module" and "finit_module" syscalls, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261458`

### Rule: SLEM 5 must generate audit records for all uses of the "mount" system call.

**Rule ID:** `SV-261458r996781_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "mount" system call with the following command: > sudo auditctl -l | grep -w 'mount' -a always,exit -F arch=b32 -S mount -F auid>=1000 -F auid!=-1 -F key=privileged-mount -a always,exit -F arch=b64 -S mount -F auid>=1000 -F auid!=-1 -F key=privileged-mount If both the "b32" and "b64" audit rules are not defined for the "mount" syscall, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261459`

### Rule: SLEM 5 must generate audit records for all uses of the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr" system calls.

**Rule ID:** `SV-261459r996784_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary, since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining syscalls into one rule whenever possible.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr" system calls with the following command: > sudo auditctl -l | grep xattr -a always,exit -F arch=b32 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=-1 -F key=perm_mod -a always,exit -F arch=b64 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=-1 -F key=perm_mod If both the "b32" and "b64" audit rules are not defined for the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr" syscalls, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261460`

### Rule: SLEM 5 must generate audit records for all uses of the "umount" system call.

**Rule ID:** `SV-261460r996787_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "umount" and "umount2" system calls with the following command: > sudo auditctl -l | grep 'umount' -a always,exit -F arch=b32 -S umount -F auid>=1000 -F auid!=-1 -F key=privileged-umount -a always,exit -F arch=b32 -S umount2 -F auid>=1000 -F auid!=-1 -F key=privileged-umount -a always,exit -F arch=b64 -S umount2 -F auid>=1000 -F auid!=-1 -F key=privileged-umount If both the "b32" and "b64" audit rules are not defined for the "umount" syscall, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000468-GPOS-00212

**Group ID:** `V-261461`

### Rule: SLEM 5 must generate audit records for all uses of the "unlink", "unlinkat", "rename", "renameat", and "rmdir" system calls.

**Rule ID:** `SV-261461r996790_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary, since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining syscalls into one rule whenever possible.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "unlink", "unlinkat", "rename", "renameat", and "rmdir" system calls with the following command: > sudo auditctl -l | grep 'unlink\|rename\|rmdir' -a always,exit -F arch=b32 -S unlink,unlinkat,rename,renameat,rmdir -F auid>=1000 -F auid!=-1 -F key=perm_mod -a always,exit -F arch=b64 -S unlink,unlinkat,rename,renameat,rmdir -F auid>=1000 -F auid!=-1 -F key=perm_mod If both the "b32" and "b64" audit rules are not defined for the "unlink", "unlinkat", "rename", "renameat", and "rmdir" syscalls, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-261462`

### Rule: SLEM 5 must generate audit records for all uses of privileged functions.

**Rule ID:** `SV-261462r996793_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for any privileged use of the "execve" system call with the following command: > sudo auditctl -l | grep -w 'execve' -a always,exit -F arch=b32 -S execve -C uid!=euid -F euid=0 -F key=setuid -a always,exit -F arch=b64 -S execve -C uid!=euid -F euid=0 -F key=setuid -a always,exit -F arch=b32 -S execve -C gid!=egid -F egid=0 -F key=setgid -a always,exit -F arch=b64 -S execve -C gid!=egid -F egid=0 -F key=setgid If both the "b32" and "b64" audit rules for "SUID" files are not defined, this is a finding. If both the "b32" and "b64" audit rules for "SGID" files are not defined, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261463`

### Rule: SLEM 5 must generate audit records for all modifications to the "lastlog" file.

**Rule ID:** `SV-261463r996796_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record when all modifications to the "lastlog" file occur with the following command: > sudo auditctl -l | grep -w '/var/log/lastlog' -w /var/log/lastlog -p wa -k logins If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261464`

### Rule: SLEM 5 must generate audit records for all modifications to the "tallylog" file must generate an audit record.

**Rule ID:** `SV-261464r996799_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record when all modifications to the "tallylog" file occur with the following command: > sudo auditctl -l | grep -w '/var/log/tallylog' -w /var/log/tallylog -p wa -k logins If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-261465`

### Rule: SLEM 5 must audit all uses of the sudoers file and all files in the "/etc/sudoers.d/" directory.

**Rule ID:** `SV-261465r996802_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged access commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates audit records when successful/unsuccessful attempts to access the "/etc/sudoers" file and files in the "/etc/sudoers.d/" directory with the following command: > sudo auditctl -l | grep -w '/etc/sudoers' -w /etc/sudoers -p wa -k privileged-actions -w /etc/sudoers.d -p wa -k privileged-actions If the commands do not return output that match the examples, this is a finding. Notes: The "-k" allows for specifying an arbitrary identifier. The string following "-k" does not need to match the example output above.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-261466`

### Rule: Successful/unsuccessful uses of "setfiles" in SLEM 5 must generate an audit record.

**Rule ID:** `SV-261466r996805_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. The "setfiles" command is primarily used to initialize the security context fields (extended attributes) on one or more filesystems (or parts of them). Usually it is initially run as part of the SELinux installation process (a step commonly known as labeling). When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "setfiles" command with the following command: > sudo grep -w "setfiles" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/setfiles -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return a line, or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-261467`

### Rule: Successful/unsuccessful uses of "semanage" in SLEM 5 must generate an audit record.

**Rule ID:** `SV-261467r996808_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. The "semanage" command is used to configure certain elements of SELinux policy without requiring modification to or recompilation from policy sources. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "semanage" command with the following command: > sudo grep -w "semanage" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/semanage -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return a line, or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-261468`

### Rule: Successful/unsuccessful uses of "setsebool" in SLEM 5 must generate an audit record.

**Rule ID:** `SV-261468r997405_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. The "setsebool" command sets the current state of a particular SELinux Boolean or a list of Booleans to a given value. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for all uses of the "setsebool" command with the following command: > sudo grep -w "setsebool" /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/setsebool -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return a line, or the line is commented out, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000472-GPOS-00217

**Group ID:** `V-261469`

### Rule: SLEM 5 must generate audit records for the "/run/utmp file".

**Rule ID:** `SV-261469r996814_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for the "/run/utmp" file with the following command: > sudo auditctl -l | grep -w '/run/utmp' -w /run/utmp -p wa -k login_mod If the command does not return a line that matches the example, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000472-GPOS-00217

**Group ID:** `V-261470`

### Rule: SLEM 5 must generate audit records for the "/var/log/btmp" file.

**Rule ID:** `SV-261470r996817_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for the "/var/log/btmp" file with the following command: > sudo auditctl -l | grep -w '/var/log/btmp' -w /var/log/btmp -p wa -k login_mod If the command does not return a line that matches the example, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000472-GPOS-00217

**Group ID:** `V-261471`

### Rule: SLEM 5 must generate audit records for the "/var/log/wtmp" file.

**Rule ID:** `SV-261471r996820_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 generates an audit record for the "/var/log/wtmp" file with the following command: > sudo auditctl -l | grep -w '/var/log/wtmp' -w /var/log/wtmp -p wa -k login_mod If the command does not return a line that matches the example, this is a finding. Note: The "key=" value is arbitrary and can be different from the example output above.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-261472`

### Rule: SLEM 5 must not disable syscall auditing.

**Rule ID:** `SV-261472r996865_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, SLEM 5 includes the "-a task,never" audit rule as a default. This rule suppresses syscall auditing for all tasks started with this rule in effect. Because the audit daemon processes the "audit.rules" file from the top down, this rule supersedes all other defined syscall rules; therefore no syscall auditing can take place on the operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify syscall auditing has not been disabled with the following command: > sudo auditctl -l | grep -i "a task,never" If any results are returned, this is a finding. Verify the default rule "-a task,never" is not statically defined: > grep -rv "^#" /etc/audit/rules.d/ | grep -i "a task,never" If any results are returned, this is a finding.

## Group: SRG-OS-000396-GPOS-00176

**Group ID:** `V-261473`

### Rule: FIPS 140-2/140-3 mode must be enabled on SLEM 5.

**Rule ID:** `SV-261473r996824_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. SLEM 5 must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SLEM 5 is running in FIPS mode by running the following command. > cat /proc/sys/crypto/fips_enabled 1 If the value returned is "0", nothing is returned, or the file does not exist, this is a finding.

