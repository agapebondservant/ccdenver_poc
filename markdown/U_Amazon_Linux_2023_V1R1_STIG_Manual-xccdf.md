# STIG Benchmark: Amazon Linux 2023 Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000185-GPOS-00079

**Group ID:** `V-273994`

### Rule: Amazon Linux 2023 local disk partitions must implement cryptographic mechanisms to prevent unauthorized disclosure or modification of all information that requires at rest protection.

**Rule ID:** `SV-273994r1119970_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Information at rest refers to the state of information when it is located on a secondary storage device (e.g., disk drive and tape drive, when used for backups) within an operating system. This requirement addresses protection of user-generated data, as well as operating system-specific configuration data. Organizations may choose to employ different mechanisms to achieve confidentiality and integrity protections, as appropriate, in accordance with the security category and/or classification of the information. Satisfies: SRG-OS-000185-GPOS-00079, SRG-OS-000404-GPOS-00183, SRG-OS-000405-GPOS-00184</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that all partitions are encrypted with the following command: $ sudo blkid /dev/xvda1: UUID="ed0acbe9-bd05-495e-a9ac-cb615b29327d" TYPE="crypto_LUKS" Every persistent disk partition present must be of "Type" "crypto_LUKS". If any partitions other than the boot partition, bios partition or pseudo file systems (such as /proc or /sys) are not type "crypto_LUKS", this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-273995`

### Rule: Amazon Linux 2023 must ensure cryptographic verification of vendor software packages.

**Rule ID:** `SV-273995r1119973_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cryptographic verification of vendor software packages ensures that all software packages are obtained from a valid source and protects against spoofing that could lead to installation of malware on the system. Amazon Linux cryptographically signs all software packages, which includes updates, with a GPG key to Verify they are valid.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 package-signing keys are installed on the system and verify their fingerprints match vendor values. Note: For Amazon Linux 2023 software packages, AWS uses GPG keys defined in key file "/etc/pki/rpm-gpg/RPM-GPG-KEY-amazon-linux-2023" by default. List Amazon Linux GPG keys installed on the system: $ sudo rpm -q gpg-pubkey --qf "%{NAME}-%{VERSION}-%{RELEASE} %{SUMMARY}\n" gpg-pubkey-d832c631-6515c85e Amazon Linux <amazon-linux@amazon.com> public key If there is no Amazon Linux GPG key installed, this is a finding. Extract the fingerprint from the key with this command: $ sudo gpg -q --keyid-format short --with-fingerprint /etc/pki/rpm-gpg/RPM-GPG-KEY-amazon-linux-2023 pub rsa4096/D832C631 2022-12-08 [SC] Key fingerprint = B21C 50FA 44A9 9720 EAA7 2F7F E951 904A D832 C631 uid Amazon Linux <amazon-linux@amazon.com> Compare the Key fingerprint with the key fingerprint from Amazon Documentation and instructions at https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/verify-keys.html If key fingerprints do not match, or the key file is missing, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-273996`

### Rule: Amazon Linux 2023 must check the GPG signature of locally installed software packages before installation.

**Rule ID:** `SV-273996r1119976_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of Amazon Linux 2023. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. All software packages must be signed with a cryptographic key recognized and approved by the organization. Verifying the authenticity of software prior to installation validates the integrity of the software package received from a vendor. This verifies the software has not been tampered with and that it has been provided by a trusted vendor.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that dnf always checks the GPG signature of locally installed software packages before installation: $ grep localpkg_gpgcheck /etc/dnf/dnf.conf localpkg_gpgcheck=1 If "localpkg_gpgcheck" is not set to "1" or "True", or if the option is missing or commented out, ask the system administrator how the GPG signatures of local software packages are being verified. If there is no process to verify GPG signatures approved by the organization, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-273997`

### Rule: Amazon Linux 2023 must check the GPG signature of software packages originating from external software repositories before installation.

**Rule ID:** `SV-273997r1119979_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of Amazon Linux 2023. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. All software packages must be signed with a cryptographic key recognized and approved by the organization. Verifying the authenticity of software prior to installation validates the integrity of the software package received from a vendor. This verifies the software has not been tampered with and that it has been provided by a trusted vendor.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that dnf always checks the GPG signature of software packages originating from external software repositories before installation: $ grep -w gpgcheck /etc/dnf/dnf.conf gpgcheck=1 If "gpgcheck" is not set to "1" or "True", or if the option is missing or commented out, ask the system administrator how the GPG signatures of software packages are being verified. If there is no process to verify GPG signatures approved by the organization, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-273998`

### Rule: Amazon Linux 2023 must have GPG signature verification enabled for all software repositories.

**Rule ID:** `SV-273998r1119982_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of Amazon Linux 2023. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. All software packages must be signed with a cryptographic key recognized and approved by the organization. Verifying the authenticity of software prior to installation validates the integrity of the software package received from a vendor. This verifies the software has not been tampered with and that it has been provided by a trusted vendor.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 software repositories enforce a signature check on the packages prior to allowing installation with the following command: $ grep -w gpgcheck /etc/yum.repos.d/*.repo | more /etc/yum.repos.d/amazonlinux.repo:gpgcheck=1 /etc/yum.repos.d/amazonlinux.repo:gpgcheck=1 /etc/yum.repos.d/amazonlinux.repo:gpgcheck=1 /etc/yum.repos.d/kernel-livepatch.repo:gpgcheck=1 /etc/yum.repos.d/kernel-livepatch.repo:gpgcheck=1 If any repository has "gpgcheck=0" or "False", or if the option is commented out, this is a finding.

## Group: SRG-OS-000439-GPOS-00195

**Group ID:** `V-273999`

### Rule: Amazon Linux 2023 must be a vendor-supported release.

**Rule ID:** `SV-273999r1119985_rule`
**Severity:** high

**Description:**
<VulnDiscussion>An operating system release is considered "supported" if the vendor continues to provide security patches for the product. With an unsupported release, it will not be possible to resolve security issues discovered in the system software.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is a vendor-supported version with the following command: $ cat /etc/amazon-linux-release Amazon Linux release 2023.6.20250203 (Amazon Linux) If the installed version of Amazon Linux 2023 is not supported, this is a finding.

## Group: SRG-OS-000269-GPOS-00103

**Group ID:** `V-274000`

### Rule: Amazon Linux 2023 systemd-journald service must be enabled.

**Rule ID:** `SV-274000r1119988_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known state can address safety or security in accordance with the mission/business needs of the organization. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. Preserving operating system state information helps to facilitate operating system restart and return to the operational mode of the organization with least disruption to mission/business processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that "systemd-journald" is active with the following command: $ systemctl is-active systemd-journald active If the systemd-journald service is not active, this is a finding.

## Group: SRG-OS-000132-GPOS-00067

**Group ID:** `V-274001`

### Rule: Amazon Linux 2023 must restrict access to the kernel message buffer.

**Rule ID:** `SV-274001r1119991_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DOD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components. Restricting access to the kernel message buffer limits access to only root. This prevents attackers from gaining additional system information as a nonprivileged user. Satisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000138-GPOS-00069</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to restrict access to the kernel message buffer with the following commands: Check the status of the kernel.dmesg_restrict kernel parameter. $ sudo sysctl kernel.dmesg_restrict kernel.dmesg_restrict = 1 If "kernel.dmesg_restrict" is not set to "1" or is missing, this is a finding.

## Group: SRG-OS-000132-GPOS-00067

**Group ID:** `V-274002`

### Rule: Amazon Linux 2023 must prevent kernel profiling by nonprivileged users.

**Rule ID:** `SV-274002r1119994_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DOD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components. Setting the kernel.perf_event_paranoid kernel parameter to "2" prevents attackers from gaining additional system information as a nonprivileged user. Satisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000138-GPOS-00069</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to prevent kernel profiling by nonprivileged users with the following commands: Check the status of the kernel.perf_event_paranoid kernel parameter. $ sudo sysctl kernel.perf_event_paranoid kernel.perf_event_paranoid = 2 If "kernel.perf_event_paranoid" is not set to "2" or is missing, this is a finding.

## Group: SRG-OS-000132-GPOS-00067

**Group ID:** `V-274003`

### Rule: Amazon Linux 2023 must restrict exposed kernel pointer addresses access.

**Rule ID:** `SV-274003r1119997_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Exposing kernel pointers (through procfs or "seq_printf()") exposes kernel writeable structures, which may contain functions pointers. If a write vulnerability occurs in the kernel, allowing write access to any of this structure, the kernel can be compromised. This option disallows any program without the CAP_SYSLOG capability to get the addresses of kernel pointers by replacing them with "0". Satisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000433-GPOS-00192</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 restricts exposed kernel pointer addresses access by validating the runtime status of the Amazon Linux 2023 kernel.kptr_restrict kernel parameter with the following command: $ sudo sysctl kernel.kptr_restrict kernel.kptr_restrict = 1 If "kernel.kptr_restrict" is not set to "1" or is missing, this is a finding.

## Group: SRG-OS-000132-GPOS-00067

**Group ID:** `V-274004`

### Rule: Amazon Linux 2023 must disable access to network bpf system call from nonprivileged processes.

**Rule ID:** `SV-274004r1120000_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Loading and accessing the packet filters programs and maps using the bpf() system call has the potential of revealing sensitive information about the kernel state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 prevents privilege escalation through the kernel by disabling access to the bpf system call with the following commands: $ sudo sysctl kernel.unprivileged_bpf_disabled kernel.unprivileged_bpf_disabled = 1 If the returned line does not have a value of "1", or a line is not returned, this is a finding.

## Group: SRG-OS-000132-GPOS-00067

**Group ID:** `V-274005`

### Rule: Amazon Linux 2023 must restrict usage of ptrace to descendant processes.

**Rule ID:** `SV-274005r1120003_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted usage of ptrace allows compromised binaries to run ptrace on other processes of the user. Like this, the attacker can steal sensitive information from the target processes (e.g., SSH sessions, web browser, etc.) without any additional assistance from the user (i.e., without resorting to phishing).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 restricts usage of ptrace to descendant processes with the following commands: $ sudo sysctl kernel.yama.ptrace_scope kernel.yama.ptrace_scope = 1 If the returned line does not have a value of "1", or a line is not returned, this is a finding.

## Group: SRG-OS-000433-GPOS-00193

**Group ID:** `V-274006`

### Rule: Amazon Linux 2023 must implement address space layout randomization (ASLR) to protect its memory from unauthorized code execution.

**Rule ID:** `SV-274006r1120006_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ASLR makes it more difficult for an attacker to predict the location of attack code they have introduced into a process' address space during an attempt at exploitation. Additionally, ASLR makes it more difficult for an attacker to know the location of existing code to repurpose it using return oriented programming (ROP) techniques.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is implementing ASLR with the following command: $ sysctl kernel.randomize_va_space kernel.randomize_va_space = 2 Check that the configuration files are present to enable this kernel parameter. Verify the configuration of the kernel.kptr_restrict kernel parameter with the following command: $ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F kernel.randomize_va_space | tail -1 kernel.randomize_va_space = 2 If "kernel.randomize_va_space" is not set to "2" or is missing, this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-274007`

### Rule: Amazon Linux 2023 must not have the vsftpd package installed.

**Rule ID:** `SV-274007r1120009_rule`
**Severity:** high

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore, may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of nonessential capabilities include, but are not limited to, games, software packages, tools, and demonstration software, not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled. Satisfies: SRG-OS-000074-GPOS-00042, SRG-OS-000095-GPOS-00049</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 does not have the vsftpd package installed with the following command: $ dnf list --installed vsftpd Error: No matching Packages to list If the "vsftpd" package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-274008`

### Rule: Amazon Linux 2023 must not have the sendmail package installed.

**Rule ID:** `SV-274008r1120012_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore, may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of nonessential capabilities include, but are not limited to, games, software packages, tools, and demonstration software, not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 does not have the sendmail package installed with the following command: $ dnf list --installed sendmail Error: No matching Packages to list If the "sendmail" package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-274009`

### Rule: Amazon Linux 2023 must not have the nfs-utils package installed.

**Rule ID:** `SV-274009r1120015_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore, may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of nonessential capabilities include, but are not limited to, games, software packages, tools, and demonstration software, not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 does not have the nfs-utils package installed with the following command: $ dnf list --installed nfs-utils Error: No matching Packages to list If the "nfs-utils" package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-274010`

### Rule: Amazon Linux 2023 must not have the telnet-server package installed.

**Rule ID:** `SV-274010r1120018_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore, may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of nonessential capabilities include, but are not limited to, games, software packages, tools, and demonstration software, not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 does not have the telnet-server package installed with the following command: $ dnf list --installed telnet-server Error: No matching Packages to list If the "telnet-server" package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-274011`

### Rule: Amazon Linux 2023 must not have the gssproxy package installed.

**Rule ID:** `SV-274011r1120021_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of nonessential capabilities include, but are not limited to, games, software packages, tools, and demonstration software, not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 does not have the gssproxy package installed with the following command: $ dnf list --installed gssproxy Error: No matching Packages to list If the "gssproxy" package is installed, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-274012`

### Rule: Amazon Linux 2023 must have the sudo package installed.

**Rule ID:** `SV-274012r1120710_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "sudo" program is designed to allow a system administrator to give limited root privileges to users and log root activity. The basic philosophy is to give as few privileges as possible but still allow system users to get their work done.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 has the sudo package installed with the following command: $ dnf list --installed sudo Installed Packages sudo.x86_64 1.9.15-1.p5.amzn2023.0.1 @System If the "sudo" package is not installed, this is a finding.

## Group: SRG-OS-000312-GPOS-00123

**Group ID:** `V-274013`

### Rule: Amazon Linux 2023 must not be configured to bypass password requirements for privilege escalation.

**Rule ID:** `SV-274013r1120027_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the user reauthenticate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is not configured to bypass password requirements for privilege escalation with the following command: $ sudo grep pam_succeed_if /etc/pam.d/sudo If any occurrences of "pam_succeed_if" are returned, this is a finding.

## Group: SRG-OS-000373-GPOS-00157

**Group ID:** `V-274014`

### Rule: Amazon Linux 2023 must require reauthentication when using the "sudo" command.

**Rule ID:** `SV-274014r1120030_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 requires reauthentication when using the "sudo" command to elevate privileges with the following command: $ sudo grep -ir 'timestamp_timeout' /etc/sudoers /etc/sudoers.d/ /etc/sudoers:Defaults timestamp_timeout=0 If results are returned from more than one file location, this is a finding. If "timestamp_timeout" is set to a negative number, is commented out, or no results are returned, this is a finding.

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-274015`

### Rule: Amazon Linux 2023 must require users to reauthenticate for privilege escalation.

**Rule ID:** `SV-274015r1120033_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 requires users to reauthenticate for privilege escalation. Ensure that "/etc/sudoers" has no occurrences of "!authenticate" with the following command: $ sudo grep -ir '!authenticate' /etc/sudoers /etc/sudoers.d/ If any occurrences of "!authenticate" are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-274016`

### Rule: Amazon Linux 2023 must require users to provide a password for privilege escalation.

**Rule ID:** `SV-274016r1120036_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 requires users to provide a password for privilege escalation. Ensure that "/etc/sudoers" has no occurrences of "NOPASSWD" with the following command: $ sudo grep -ri nopasswd /etc/sudoers /etc/sudoers.d/ If any occurrences of "NOPASSWD" are returned, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-274017`

### Rule: Amazon Linux 2023 must have the audit package installed.

**Rule ID:** `SV-274017r1120039_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Successful incident response and auditing relies on timely, accurate system information and analysis to allow the organization to identify and respond to potential incidents in a proficient manner. If Amazon Linux 2023 does not provide the ability to centrally review Amazon Linux 2023 logs, forensic analysis is negatively impacted. Segregation of logging data to multiple disparate computer systems is counterproductive and makes log analysis and log event alarming difficult to implement and manage, particularly when the system has multiple logging components writing to different locations or systems. To support the centralized capability, Amazon Linux 2023 must be able to provide the information in a format that can be extracted and used, allowing the application performing the centralization of the log records to meet this requirement. Satisfies: SRG-OS-000062-GPOS-00031, SRG-OS-000042-GPOS-00021, SRG-OS-000037-GPOS-00015, SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000051-GPOS-00024, SRG-OS-000054-GPOS-00025, SRG-OS-000122-GPOS-00063, SRG-OS-000254-GPOS-00095, SRG-OS-000255-GPOS-00096, SRG-OS-000337-GPOS-00129, SRG-OS-000348-GPOS-00136, SRG-OS-000349-GPOS-00137, SRG-OS-000350-GPOS-00138, SRG-OS-000351-GPOS-00139, SRG-OS-000352-GPOS-00140, SRG-OS-000353-GPOS-00141, SRG-OS-000354-GPOS-00142, SRG-OS-000358-GPOS-00145, SRG-OS-000365-GPOS-00152, SRG-OS-000392-GPOS-00172, SRG-OS-000475-GPOS-00220, SRG-OS-000055-GPOS-00026</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 has the audit package installed with the following command: $ dnf list --installed audit Installed Packages audit.x86_64 3.0.6-1.amzn2023.0.2 @System If the "audit" package is not installed, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-274018`

### Rule: Amazon Linux 2023 must produce audit records containing information to establish what type of events occurred.

**Rule ID:** `SV-274018r1120042_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in Amazon Linux 2023 audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured operating system. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000062-GPOS-00031, SRG-OS-000042-GPOS-00021, SRG-OS-000051-GPOS-00024, SRG-OS-000054-GPOS-00025, SRG-OS-000122-GPOS-00063, SRG-OS-000254-GPOS-00095, SRG-OS-000255-GPOS-00096, SRG-OS-000337-GPOS-00129, SRG-OS-000348-GPOS-00136, SRG-OS-000349-GPOS-00137, SRG-OS-000350-GPOS-00138, SRG-OS-000351-GPOS-00139, SRG-OS-000352-GPOS-00140, SRG-OS-000353-GPOS-00141, SRG-OS-000354-GPOS-00142, SRG-OS-000358-GPOS-00145, SRG-OS-000365-GPOS-00152, SRG-OS-000392-GPOS-00172, SRG-OS-000475-GPOS-00220, SRG-OS-000755-GPOS-00220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to produce audit records with the following command: $ sudo systemctl status auditd.service auditd.service - Security Auditing Service Loaded:loaded (/usr/lib/systemd/system/auditd.service; enabled; preset: enabled) Active: active (running) since Wed 2024-01-131 12:56:56 EST; 1 weeks 0 days ago If the audit service is not "active" and "running", this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-274019`

### Rule: Amazon Linux 2023 audispd-plugins package must be installed.

**Rule ID:** `SV-274019r1120045_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "audispd-plugins" package provides plugins for the real-time interface to the audit subsystem, "audispd". These plugins can, for example, relay events to remote machines or analyze events for suspicious behavior.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 has the audispd-plugins package installed with the following command: $ sudo dnf list --installed audispd-plugins Installed Packages audispd-plugins.x86_64 3.0.6-1.amzn2023.0.2 @amazonlinux If the "audispd-plugins" package is not installed, this is a finding.

## Group: SRG-OS-000051-GPOS-00024

**Group ID:** `V-274020`

### Rule: Amazon Linux 2023 must have the rsyslog package installed.

**Rule ID:** `SV-274020r1120048_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Successful incident response and auditing relies on timely, accurate system information and analysis allow the organization to identify and respond to potential incidents in a proficient manner. If Amazon Linux 2023 does not provide the ability to centrally review Amazon Linux 2023 logs, forensic analysis is negatively impacted. Segregation of logging data to multiple disparate computer systems is counterproductive and makes log analysis and log event alarming difficult to implement and manage, particularly when the system has multiple logging components writing to different locations or systems. To support the centralized capability, Amazon Linux 2023 must be able to provide the information in a format that can be extracted and used, allowing the application performing the centralization of the log records to meet this requirement. Satisfies: SRG-OS-000051-GPOS-00024, SRG-OS-000479-GPOS-00224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to collect system failure events with the following command: $ dnf list --installed rsyslog Installed Packages rsyslog.x86_64 8.2204.0-3.amzn2023.0.4 @amazonlinux If the "rsyslog" package is not installed, this is a finding. Check that the log service is enabled with the following command: $ dnf list --installed vsftpd Error: No matching Packages to list If the command above returns "disabled", this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-274021`

### Rule: Amazon Linux 2023 must monitor remote access methods.

**Rule ID:** `SV-274021r1120695_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk and make remote user access management difficult at best.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 monitors all remote access methods. Check that remote access methods are being logged by running the following command: $ sudo grep -E '(auth.*|authpriv.*|daemon.*)' /etc/rsyslog.conf auth.*;authpriv.*;daemon.* /var/log/secure If "auth.*", "authpriv.*", or "daemon.*" are not configured to be logged, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-274022`

### Rule: Amazon Linux 2023 must have the chrony package installed.

**Rule ID:** `SV-274022r1120054_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 has the chrony package installed with the following command: $ sudo dnf list --installed chrony Installed Packages chrony.x86_64 4.3-1.amzn2023.0.5 @System If the "chrony" package is not installed, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-274023`

### Rule: Amazon Linux 2023 chronyd service must be enabled.

**Rule ID:** `SV-274023r1120057_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 has the chronyd service set to active with the following command: $ systemctl is-active chronyd active If the chronyd service is not active, this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-274024`

### Rule: Amazon Linux 2023 must have the Advanced Intrusion Detection Environment (AIDE) package installed.

**Rule ID:** `SV-274024r1120060_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly, and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. Satisfies: SRG-OS-000363-GPOS-00150, SRG-OS-000445-GPOS-00199, SRG-OS-000358-GPOS-00145</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 has the AIDE package installed with the following command: $ dnf list --installed aide Installed Packages aide.x86_64 0.18.6-1.amzn2023.0.1 @amazonlinux If AIDE is not installed, ask the system administrator (SA) how file integrity checks are performed on the system. If there is no application installed to perform integrity checks, this is a finding. If AIDE is installed, check if it has been initialized with the following command: $ sudo /usr/sbin/aide --check If the output is "Couldn't open file /var/lib/aide/aide.db.gz for reading", this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-274025`

### Rule: Amazon Linux 2023 must routinely check the baseline configuration for unauthorized changes and notify the system administrator when anomalies in the operation of any security functions are discovered.

**Rule ID:** `SV-274025r1120723_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to Amazon Linux 2023. Changes to operating system configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of Amazon Linux 2023. Amazon Linux 2023's information management officer (IMO)/information system security officer (ISSO) and system administrators (SAs) must be notified via email and/or monitoring system trap when there is an unauthorized modification of a configuration item. Notifications provided by information systems include messages to local computer consoles, and/or hardware indications, such as lights. This capability must take into account operational requirements for availability for selecting an appropriate response. The organization may choose to shut down or restart the information system upon security function anomaly detection. Satisfies: SRG-OS-000363-GPOS-00150, SRG-OS-000446-GPOS-00200, SRG-OS-000447-GPOS-00201</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 routinely executes a file integrity scan for changes to the system baseline. The commands used in the example will use a daily occurrence. Check the cron directories for scripts controlling the execution and notification of results of the file integrity application. For example, if Advanced Intrusion Detection Environment (AIDE) is installed on the system, use the following commands: $ ls -al /etc/cron.daily | grep aide -rwxr-xr-x 1 root root 29 Nov 22 2015 aide $ sudo grep aide /etc/crontab /var/spool/cron/root /etc/crontab: 30 04 * * * root usr/sbin/aide /var/spool/cron/root: 30 04 * * * root usr/sbin/aide $ sudo more /etc/cron.daily/aide #!/bin/bash /usr/sbin/aide --check | /bin/mail -s "$HOSTNAME - Daily aide integrity check run" root@sysname.mil If the file integrity application does not exist, or a script file controlling the execution of the file integrity application does not exist, or the file integrity application does not notify designated personnel of changes, this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-274026`

### Rule: Amazon Linux 2023 must use cryptographic mechanisms to protect the integrity of audit tools.

**Rule ID:** `SV-274026r1120066_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting the integrity of the tools used for auditing purposes is a critical step toward ensuring the integrity of audit information. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Audit tools include, but are not limited to, vendor-provided and open-source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. It is not uncommon for attackers to replace the audit tools or inject code into the existing tools to provide the capability to hide or erase system activity from the audit logs. To address this risk, audit tools must be cryptographically signed to provide the capability to identify when the audit tools have been modified, manipulated, or replaced. An example is a checksum hash of the file or files. Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000257-GPOS-00098, SRG-OS-000258-GPOS-00099, SRG-OS-000278-GPOS-00108</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is properly configured to protect the integrity of the Advanced Intrusion Detection Environment (AIDE) audit tools with the following command: $ sudo grep /usr/sbin/au /etc/aide.conf /usr/sbin/auditctl p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/auditd p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/ausearch p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/aureport p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/autrace p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/augenrules p+i+n+u+g+s+b+acl+xattrs+sha512 If AIDE is not installed, ask the system administrator (SA) how file integrity checks are performed on the system. If any of the audit tools listed above do not have a corresponding line, ask the SA to indicate what cryptographic mechanisms are being used to protect the integrity of the audit tools. If there is no evidence of integrity protection, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-274027`

### Rule: Amazon Linux 2023 must have the firewalld package installed.

**Rule ID:** `SV-274027r1120069_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, Amazon Linux 2023 must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues. Satisfies: SRG-OS-000096-GPOS-00050, SRG-OS-000297-GPOS-00115, SRG-OS-000298-GPOS-00116, SRG-OS-000480-GPOS-00232, SRG-OS-000304-GPOS-00121</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 has the firewalld package installed with the following command: $ dnf list --installed firewalld Installed Packages firewalld.noarch 1.2.3-1.amzn2023 @amazonlinux If the "firewalld" package is not installed, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-274028`

### Rule: Amazon Linux 2023 must have the firewalld servicew active.

**Rule ID:** `SV-274028r1120072_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Operating systems are capable of providing a variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, Amazon Linux 2023 must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues. Satisfies: SRG-OS-000096-GPOS-00050, SRG-OS-000297-GPOS-00115, SRG-OS-000298-GPOS-00116, SRG-OS-000480-GPOS-00232, SRG-OS-000304-GPOS-00121</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 firewalld service is active with the following command: $ systemctl is-active firewalld active If the "firewalld" service is not active, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-274029`

### Rule: Amazon Linux 2023 must be configured to disable nonessential capabilities.

**Rule ID:** `SV-274029r1120075_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of nonessential capabilities include, but are not limited to, games, software packages, tools, and demonstration software, not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to disable nonessential capabilities. Inspect the list of enabled firewall ports and verify they are configured correctly by running the following command: $ sudo firewall-cmd --list-all Ask the system administrator for the site or program Ports, Protocols, and Services Management Component Local Service Assessment (PPSM CLSA). Verify the services allowed by the firewall match the PPSM CLSA. If there are additional ports, protocols, or services that are not in the PPSM CLSA, or there are ports, protocols, or services that are prohibited by the PPSM Category Assurance List (CAL), or there are no firewall rules configured, this is a finding.

## Group: SRG-OS-000142-GPOS-00071

**Group ID:** `V-274030`

### Rule: Amazon Linux 2023 must manage excess capacity, bandwidth, or other redundancy to limit the effects of information flooding types of denial-of-service (DoS) attacks.

**Rule ID:** `SV-274030r1120078_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Managing excess capacity ensures that sufficient capacity is available to counter flooding attacks. Employing increased capacity and service redundancy may reduce the susceptibility to some DoS attacks. Managing excess capacity may include, for example, establishing selected usage priorities, quotas, or partitioning.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 manages excess capacity, bandwidth, or other redundancy to limit the effects of information flooding types of DoS attacks. Verify nftables is configured to allow rate limits on any connection to the system with the following command: $ sudo grep -i firewallbackend /etc/firewalld/firewalld.conf FirewallBackend=nftables

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-274031`

### Rule: Amazon Linux 2023 must have the s-nail package installed.

**Rule ID:** `SV-274031r1120081_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "s-nail" package provides the mail command required to allow sending email notifications of unauthorized configuration changes to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 has the "s-nail" package is installed on the system with the following command: $ dnf list --installed s-nail Installed Packages s-nail.x86_64 14.9.24-6.amzn2023 @amazonlinux If the "s-nail" package is not installed, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-274032`

### Rule: Amazon Linux 2023 must have the libreswan package installed.

**Rule ID:** `SV-274032r1120084_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore, cannot be relied upon to provide confidentiality or integrity, and DOD data may be compromised. Operating systems utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2/140-3 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DOD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general purpose computing system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 has the libreswan package installed with the following command: $ dnf list --installed libreswan Installed Packages libreswan.x86_64 4.12-3.amzn2023.0.2 @amazonlinux If the "libreswan" package is not installed, this is a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-274033`

### Rule: Amazon Linux 2023 must have the policycoreutils package installed.

**Rule ID:** `SV-274033r1120087_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An isolation boundary provides access control and protects the integrity of the hardware, software, and firmware that perform security functions. Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Operating systems implement code separation (i.e., separation of security functions from nonsecurity functions) in a number of ways, including through the provision of security kernels via processor rings or processor modes. For nonkernel code, security function isolation is often achieved through file system protections that serve to protect the code on disk and address space protections that protect executing code. Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Implementation may include isolation of memory space and libraries. Operating systems restrict access to security functions through the use of access control mechanisms and by implementing least privilege capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 has the policycoreutils package installed with the following command: $ dnf list --installed policycoreutils Installed Packages policycoreutils.x86_64 3.4-6.amzn2023.0.2 @System If the "policycoreutils" package is not installed, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-274034`

### Rule: Amazon Linux 2023 must have the pcsc-lite package installed.

**Rule ID:** `SV-274034r1120090_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The pcsc-lite package must be installed if it is to be available for multifactor authentication using smart cards.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 has the pcsc-lite package installed with the following command: $ dnf list --installed pcsc-lite Installed Packages pcsc-lite.x86_64 1.9.1-1.amzn2023.0.4 @amazonlinux If the "pcsc-lite" package is not installed, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-274035`

### Rule: Amazon Linux 2023 must have the packages required for encrypting off-loaded audit logs installed.

**Rule ID:** `SV-274035r1120093_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms used for authentication to the cryptographic module are not verified and therefore, cannot be relied upon to provide confidentiality or integrity, and DOD data may be compromised. Operating systems utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2/140-3 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DOD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general purpose computing system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 has the rsyslog-openssl package installed with the following command: $ dnf list --installed rsyslog-openssl Installed Packages rsyslog-openssl.x86_64 8.2204.0-3.amzn2023.0.4 @amazonlinux If the "rsyslog-openssl" package is not installed, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-274036`

### Rule: Amazon Linux 2023 must have the opensc package installed.

**Rule ID:** `SV-274036r1120096_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. The DOD has mandated the use of the Common Access Card (CAC) to support identity management and personal authentication for systems covered under Homeland Security Presidential Directive (HSPD) 12, as well as making the CAC a primary component of layered protection for national security systems. Satisfies: SRG-OS-000375-GPOS-00160, SRG-OS-000376-GPOS-00161</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 has the opensc package installed with the following command: $ sudo dnf list --installed opensc Installed Packages opensc.x86_64 0.24.0-1.amzn2023.0.4 @amazonlinux If the "opensc" package is not installed, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-274037`

### Rule: Amazon Linux 2023 must have the openssl-pkcs11 package installed.

**Rule ID:** `SV-274037r1120099_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. A privileged account is defined as an information system account with authorizations of a privileged user. The DOD Common Access Card (CAC) with DOD-approved PKI is an example of multifactor authentication. Satisfies: SRG-OS-000375-GPOS-00160, SRG-OS-000376-GPOS-00161, SRG-OS-000377-GPOS-00162</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 has the openssl-pkcs11 package installed with the following command: $ dnf list --installed openssl-pkcs11 Installed Packages openssl-pkcs11.x86_64 0.4.12-3.amzn2023.0.1 @System If the "openssl-pkcs11" package is not installed, this is a finding.

## Group: SRG-OS-000112-GPOS-00057

**Group ID:** `V-274038`

### Rule: Amazon Linux 2023 must have SSH installed.

**Rule ID:** `SV-274038r1120102_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. Satisfies: SRG-OS-000112-GPOS-00057, SRG-OS-000113-GPOS-00058, SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 has the openssh-server package installed with the following command: $ dnf list --installed openssh-server Installed Packages openssh-server.x86_64 8.7p1-8.amzn2023.0.13 @amazonlinux If the "openssh-server" package is not installed, this is a finding.

## Group: SRG-OS-000112-GPOS-00057

**Group ID:** `V-274039`

### Rule: Amazon Linux 2023 must implement SSH to protect the confidentiality and integrity of transmitted and received information, as well as information during preparation for transmission.

**Rule ID:** `SV-274039r1120105_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Encrypting information for transmission protects information from unauthorized disclosure and modification. Cryptographic mechanisms implemented to protect information integrity include, for example, cryptographic hash functions that have common application in digital signatures, checksums, and message authentication codes. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, operating systems need to leverage transmission protection mechanisms such as TLS, SSL VPNs, or IPSec. Satisfies: SRG-OS-000112-GPOS-00057, SRG-OS-000113-GPOS-00058, SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 has "sshd" set to active with the following command: $ systemctl is-active sshd active If the "sshd" service is not active, this is a finding.

## Group: SRG-OS-000396-GPOS-00176

**Group ID:** `V-274040`

### Rule: Amazon Linux 2023 must have the crypto-policies package installed.

**Rule ID:** `SV-274040r1120108_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Centralized cryptographic policies simplify applying secure ciphers across an operating system and the applications that run on that operating system. Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. Satisfies: SRG-OS-000396-GPOS-00176, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174, SRG-OS-000424-GPOS-00188</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 crypto-policies package is installed with the following command: $ dnf list --installed crypto-policies Installed Packages crypto-policies.noarch 20240828-2.git626aa59.amzn2023.0.1 @System If the "crypto-policies" package is not installed, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-274041`

### Rule: Amazon Linux 2023 SSH server must be configured to use systemwide crypto policies.

**Rule ID:** `SV-274041r1120111_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 employs systemwide crypto policies for SSH with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*include' /etc/ssh/sshd_config:Include /etc/ssh/sshd_config.d/*.conf /etc/ssh/sshd_config.d/50-redhat.conf:Include /etc/crypto-policies/back-ends/opensshserver.config If "Include /etc/ssh/sshd_config.d/*.conf" or "Include /etc/crypto-policies/back-ends/opensshserver.config" are not included in the system sshd config or the file /etc/ssh/sshd_config.d/50-redhat.conf is missing, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-274042`

### Rule: Amazon Linux 2023 server must be configured to use only DOD-approved encryption ciphers employing FIPS 140-2/140-3 validated cryptographic hash algorithms to protect the confidentiality of SSH server connections.

**Rule ID:** `SV-274042r1120114_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. Amazon Server 2023 incorporates systemwide crypto policies by default. The SSH configuration file has no effect on the ciphers, MACs, or algorithms unless specifically defined in the /etc/sysconfig/sshd file. The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/opensshserver.config file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 SSH server is configured to use only ciphers employing FIPS 140-2/140-3 approved algorithms with the following command: $ sudo grep -i Ciphers /etc/crypto-policies/back-ends/opensshserver.config Ciphers aes256-gcm@openssh.com,aes256-ctr,aes128-gcm@openssh.com,aes128-ctr If the cipher entries in the "opensshserver.config" file have any ciphers other than "aes256-gcm@openssh.com,aes256-ctr,aes128-gcm@openssh.com,aes128-ctr", or they are missing or commented out, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-274043`

### Rule: Amazon Linux 2023 SSH server must be configured to use only Message Authentication Codes (MACs) employing FIPS 140-2/140-3 validated cryptographic hash algorithms to protect the confidentiality of SSH server connections.

**Rule ID:** `SV-274043r1120117_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. Amazon Linux 2023 incorporates systemwide crypto policies by default. The SSH configuration file has no effect on the ciphers, MACs, or algorithms unless specifically defined in the /etc/sysconfig/sshd file. The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/opensshserver.config file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 SSH server is configured to use only MACs employing FIPS 140-2/140-3 approved algorithms. To verify the MACs in the systemwide SSH configuration file, use the following command: $ sudo grep -i MACs /etc/crypto-policies/back-ends/opensshserver.config MACs hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha2-256,hmac-sha2-512 If the MACs entries in the "opensshserver.config" file have any hashes other than "hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha2-256,hmac-sha2-512", or they are missing or commented out, this is a finding.

## Group: SRG-OS-000364-GPOS-00151

**Group ID:** `V-274044`

### Rule: Amazon Linux 2023 SSH daemon must not allow Generic Security Service Application Program Interface (GSSAPI) authentication.

**Rule ID:** `SV-274044r1120120_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>GSSAPI authentication is used to provide additional authentication mechanisms to applications. Allowing GSSAPI authentication through SSH exposes the system's GSSAPI to remote hosts, increasing the attack surface of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the SSH daemon does not allow GSSAPI authentication with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*gssapiauthentication' /etc/ssh/sshd_config.d/50-redhat.conf:GSSAPIAuthentication no If the value is returned as "yes", the returned line is commented out, no output is returned, and the use of GSSAPI authentication has not been documented with the information system security officer (ISSO), this is a finding. If the required value is not set, this is a finding.

## Group: SRG-OS-000364-GPOS-00151

**Group ID:** `V-274045`

### Rule: Amazon Linux 2023 SSH daemon must not allow Kerberos authentication.

**Rule ID:** `SV-274045r1120123_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kerberos authentication for SSH is often implemented using Generic Security Service Application Program Interface (GSSAPI). If Kerberos is enabled through SSH, the SSH daemon provides a means of access to the system's Kerberos implementation. Vulnerabilities in the system's Kerberos implementations may be subject to exploitation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the SSH daemon does not allow Kerberos authentication with the following command: $ [ec2-user@ip-172-31-12-63 ~]$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*kerberosauthentication' /etc/ssh/sshd_config.d/93-KerberosAuthentication.conf:KerberosAuthentication no If the value is returned as "yes", the returned line is commented out, no output is returned, and the use of Kerberos authentication has not been documented with the information system security officer (ISSO), this is a finding.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-274046`

### Rule: Amazon Linux 2023 must force a frequent session key renegotiation for SSH connections to the server.

**Rule ID:** `SV-274046r1120126_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. Session key regeneration limits the chances of a session key becoming compromised. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000033-GPOS-00014, SRG-OS-000424-GPOS-00188</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the SSH forces frequent session key renegotiation with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*rekeylimit' RekeyLimit 1G 1h If "RekeyLimit" does not have a maximum data amount and maximum time defined, is missing, or is commented out, this is a finding.

## Group: SRG-OS-000105-GPOS-00052

**Group ID:** `V-274047`

### Rule: Amazon Linux 2023 SSHD must accept public key authentication.

**Rule ID:** `SV-274047r1120129_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: 1. Something a user knows (e.g., password/PIN); 2. Something a user has (e.g., cryptographic identification device, token); and 3. Something a user is (e.g., biometric). A privileged account is defined as an information system account with authorizations of a privileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the internet). The DOD Common Access Card (CAC) with DOD-approved PKI is an example of multifactor authentication. Satisfies: SRG-OS-000105-GPOS-00052, SRG-OS-000106-GPOS-00053, SRG-OS-000107-GPOS-00054, SRG-OS-000108-GPOS-00055</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the SSH daemon accepts public key encryption with the following command: $ sudo grep -ir PubkeyAuthentication /etc/ssh/sshd_config /etc/ssh/sshd_config.d/ /etc/ssh/sshd_config:#PubkeyAuthentication yes /etc/ssh/sshd_config.d/90-PubkeyAuth:PubkeyAuthentication yes If "PubkeyAuthentication" is set to no, the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000106-GPOS-00053

**Group ID:** `V-274048`

### Rule: Amazon Linux 2023 SSHD must not allow blank passwords.

**Rule ID:** `SV-274048r1120132_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log on and run commands with the privileges of that account. Accounts with empty passwords must never be used in operational environments. Satisfies: SRG-OS-000106-GPOS-00053, SRG-OS-000480-GPOS-00229</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 remote access using SSH prevents logging on with a blank password with the following command: $ sudo grep -ir PermitEmptyPasswords /etc/ssh/sshd_config /etc/ssh/sshd_config.d/ /etc/ssh/sshd_config:PermitEmptyPasswords no If the "PermitEmptyPassword" keyword is set to "yes", is missing, or is commented out, this is a finding.

## Group: SRG-OS-000109-GPOS-00056

**Group ID:** `V-274049`

### Rule: Amazon Linux 2023 must not permit direct logons to the root account using remote access via SSH.

**Rule ID:** `SV-274049r1120135_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure individual accountability and prevent unauthorized access, organizational users must be individually identified and authenticated. Additionally, an additional layer of security is gained by extending the policy of not logging directly on as root, even though the communications channel may be encrypted. A group authenticator is a generic account used by multiple individuals. Use of a group authenticator alone does not uniquely identify individual users. Examples of the group authenticator is the Unix OS "root" user account, the Windows "Administrator" account, the "sa" account, or a "helpdesk" account. For example, the Unix and Windows operating systems offer a "switch user" capability allowing users to authenticate with their individual credentials and, when needed, switch" to the administrator role. This method provides for unique individual authentication prior to using a group authenticator. Users (and any processes acting on behalf of users) need to be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization, which outlines specific user actions that can be performed on Amazon Linux 2023 without identification or authentication. Requiring individuals to be authenticated with an individual authenticator prior to using a group authenticator allows for traceability of actions, as well as adding an additional level of protection of the actions that can be taken with group account knowledge.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 remote access using SSH prevents users from logging on directly as "root" with the following command: $ sudo grep -ir PermitRootLogin /etc/ssh/sshd_config /etc/ssh/sshd_config.d/ /etc/ssh/sshd_config:PermitRootLogin no If the "PermitRootLogin" keyword is set to "yes", is missing, or is commented out, this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-274050`

### Rule: Amazon Linux 2023 must be configured so that all network connections associated with SSH traffic are terminated after 10 minutes of becoming unresponsive.

**Rule ID:** `SV-274050r1120138_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at Amazon Linux 2023 level, and de-allocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that Amazon Linux 2023 terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session. Satisfies: SRG-OS-000163-GPOS-00072, SRG-OS-000279-GPOS-00109, SRG-OS-000395-GPOS-00175</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 has the "ClientAliveInterval" variable set to a value of "600" or less by performing the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*clientaliveinterval' /etc/ssh/sshd_config.d/91-ClientAliveInterval.conf:ClientAliveInterval 600 If "ClientAliveInterval" does not exist, does not have a value of "600" or less in "/etc/ssh/sshd_config" or a dropfile in "/etc/ssh/sshd_config.d", or is commented out, this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-274051`

### Rule: Amazon Linux 2023 must be configured so that all network connections associated with SSH traffic terminate after becoming unresponsive.

**Rule ID:** `SV-274051r1120141_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at Amazon Linux 2023 level, and de-allocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that Amazon Linux 2023 terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session. Satisfies: SRG-OS-000163-GPOS-00072, SRG-OS-000279-GPOS-00109</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 SSHD has the "ClientAliveCountMax" set to "1" by performing the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*clientalivecountmax' /etc/ssh/sshd_config.d/92-ClientAliveCountMax.conf:ClientAliveCountMax 1 If "ClientAliveCountMax" do not exist, is not set to a value of "1" in "/etc/ssh/sshd_config" or a dropfile in "/etc/ssh/sshd_config.d" , or is commented out, this is a finding.

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-274052`

### Rule: Amazon Linux 2023 must enable the Pluggable Authentication Module (PAM) interface for SSHD.

**Rule ID:** `SV-274052r1120144_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If maintenance tools are used by unauthorized personnel, they may accidentally or intentionally damage or compromise the system. The act of managing systems and applications includes the ability to access sensitive application information, such as system configuration details, diagnostic information, user information, and potentially sensitive application data. Some maintenance and test tools are either standalone devices with their own operating systems or are applications bundled with an operating system. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. Typically, strong authentication requires authenticators that are resistant to replay attacks and employ multifactor authentication. Strong authenticators include, for example, PKI where certificates are stored on a token protected by a password, passphrase, or biometric.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 SSHD is configured to allow for the UsePAM interface with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*usepam' /etc/ssh/sshd_config.d/50-redhat.conf:UsePAM yes If the "UsePAM" keyword is set to "no", is missing, or is commented out, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-274053`

### Rule: Amazon Linux 2023 must implement DOD-approved encryption in the OpenSSL package.

**Rule ID:** `SV-274053r1120147_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the OpenSSL library uses only ciphers employing FIPS 140-2/140-3 approved algorithms with the following command: $ sudo grep -i opensslcnf.config /etc/pki/tls/openssl.cnf .include = /etc/crypto-policies/back-ends/opensslcnf.config If the "opensslcnf.config" is not defined in the "/etc/pki/tls/openssl.cnf" file, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-274054`

### Rule: Amazon Linux 2023 must implement DOD-approved TLS encryption in the OpenSSL package.

**Rule ID:** `SV-274054r1120150_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the OpenSSL library uses TLS 1.2 encryption or stronger with following command: $ grep -i minprotocol /etc/crypto-policies/back-ends/opensslcnf.config TLS.MinProtocol = TLSv1.2 DTLS.MinProtocol = DTLSv1.2 If the "TLS.MinProtocol" is set to anything older than "TLSv1.2" or the "DTLS.MinProtocol" is set to anything older than "DTLSv1.2", this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-274055`

### Rule: Amazon Linux 2023 must implement a FIPS 140-2/140-3 compliant systemwide cryptographic policy.

**Rule ID:** `SV-274055r1120153_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Centralized cryptographic policies simplify applying secure ciphers across an operating system and the applications that run on that operating system. Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. Satisfies: SRG-OS-000120-GPOS-00061, SRG-OS-000396-GPOS-00176, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174, SRG-OS-000424-GPOS-00188</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is set to use a FIPS 140-2/140-3 compliant systemwide cryptographic policy. $ update-crypto-policies --show FIPS If the systemwide crypto policy is not set to "FIPS", this is a finding. Inspect the contents of the REQUIRE.pmod file (if it exists) to verify only authorized modifications to the current policy are included with the following command: $ cat /etc/crypto-policies/policies/modules/REQUIRE.pmod Note: If subpolicies have been configured, they could be listed in a colon-separated list starting with FIPS as follows FIPS:<SUBPOLICY-NAME>:<SUBPOLICY-NAME>. This is not a finding. If the AD-SUPPORT subpolicy module is included (e.g., "FIPS:AD-SUPPORT"), and Active Directory support is not documented as an operational requirement with the information system security officer (ISSO), this is a finding. If the NO-ENFORCE-EMS subpolicy module is included (e.g., "FIPS:NO-ENFORCE-EMS"), and not enforcing EMS is not documented as an operational requirement with the ISSO, this is a finding. Verify the current minimum crypto-policy configuration with the following commands: $ grep -E 'rsa_size|hash' /etc/crypto-policies/state/CURRENT.pol hash = SHA2-256 SHA2-384 SHA2-512 SHA2-224 SHA3-256 SHA3-384 SHA3-512 SHAKE-256 min_rsa_size = 2048 If the "hash" values do not include at least the following FIPS 140-2/140-3 compliant algorithms "SHA2-256 SHA2-384 SHA2-512 SHA2-224 SHA3-256 SHA3-384 SHA3-512 SHAKE-256", this is a finding. If there are algorithms that include "SHA1" or a hash value less than "256" this is a finding. If the "min_rsa_size" is not set to a value of at least 2048, this is a finding. If these commands do not return any output, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-274056`

### Rule: Amazon Linux 2023 must implement DOD-approved encryption to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-274056r1120156_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection (e.g., RDP), thereby providing a degree of confidentiality. The encryption strength of a mechanism is selected based on the security categorization of the information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the SSH server uses only ciphers employing FIPS 140-2/140-3 approved algorithms with the following command: $ sudo grep -i ciphers /etc/crypto-policies/back-ends/opensshserver.config Ciphers aes256-gcm@openssh.com,aes256-ctr,aes128-gcm@openssh.com,aes128-ctr If the cipher entries in the "opensshserver.config" file have any ciphers other than "aes256-gcm@openssh.com,aes256-ctr,aes128-gcm@openssh.com,aes128-ctr", they are missing, or commented out, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-274057`

### Rule: Amazon Linux 2023 must enable FIPS mode.

**Rule ID:** `SV-274057r1120159_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. Amazon Linux 2023 must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000125-GPOS-00065, SRG-OS-000396-GPOS-00176, SRG-OS-000423-GPOS-00187, SRG-OS-000478-GPOS-00223</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is in FIPS mode with the following command: $ sudo fips-mode-setup --check FIPS mode is enabled. If FIPS mode is not enabled, this is a finding.

## Group: SRG-OS-000396-GPOS-00176

**Group ID:** `V-274058`

### Rule: Amazon Linux 2023 crypto policy must not be overridden.

**Rule ID:** `SV-274058r1120162_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Centralized cryptographic policies simplify applying secure ciphers across an operating system and the applications that run on that operating system. Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. Satisfies: SRG-OS-000396-GPOS-00176, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174, SRG-OS-000424-GPOS-00188, SRG-OS-000073-GPOS-00041, SRG-OS-000120-GPOS-00061</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 custom crypto policies are loaded correctly with the following command: $ ls -l /etc/crypto-policies/back-ends/ lrwxrwxrwx. 1 root root 40 Mar 7 19:22 bind.config -> /usr/share/crypto-policies/FIPS/bind.txt lrwxrwxrwx. 1 root root 42 Mar 7 19:22 gnutls.config -> /usr/share/crypto-policies/FIPS/gnutls.txt lrwxrwxrwx. 1 root root 40 Mar 7 19:22 java.config -> /usr/share/crypto-policies/FIPS/java.txt lrwxrwxrwx. 1 root root 46 Mar 7 19:22 javasystem.config -> /usr/share/crypto-policies/FIPS/javasystem.txt lrwxrwxrwx. 1 root root 40 Mar 7 19:22 krb5.config -> /usr/share/crypto-policies/FIPS/krb5.txt lrwxrwxrwx. 1 root root 45 Mar 7 19:22 libreswan.config -> /usr/share/crypto-policies/FIPS/libreswan.txt lrwxrwxrwx. 1 root root 42 Mar 7 19:22 libssh.config -> /usr/share/crypto-policies/FIPS/libssh.txt -rw-r--r--. 1 root root 398 Mar 7 19:22 nss.config lrwxrwxrwx. 1 root root 43 Mar 7 19:22 openssh.config -> /usr/share/crypto-policies/FIPS/openssh.txt lrwxrwxrwx. 1 root root 49 Mar 7 19:22 opensshserver.config -> /usr/share/crypto-policies/FIPS/opensshserver.txt lrwxrwxrwx. 1 root root 43 Mar 7 19:22 openssl.config -> /usr/share/crypto-policies/FIPS/openssl.txt lrwxrwxrwx. 1 root root 48 Mar 7 19:22 openssl_fips.config -> /usr/share/crypto-policies/FIPS/openssl_fips.txt lrwxrwxrwx. 1 root root 46 Mar 7 19:22 opensslcnf.config -> /usr/share/crypto-policies/FIPS/opensslcnf.txt If the paths do not point to the respective files under /usr/share/crypto-policies/FIPS path, this is a finding. Note: nss.config must not be hyperlinked.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-274059`

### Rule: Amazon Linux 2023 must enable certificate-based smart card authentication.

**Rule ID:** `SV-274059r1120165_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. A privileged account is defined as an information system account with authorizations of a privileged user. The DOD Common Access Card (CAC) with DOD-approved PKI is an example of multifactor authentication. Satisfies: SRG-OS-000375-GPOS-00160, SRG-OS-000705-GPOS-00150</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system administrator demonstrates the use of an approved alternate multifactor authentication method, this requirement is not applicable. Verify Amazon Linux 2023 has smart cards enabled in System Security Services Daemon (SSSD), run the following command: $ sudo grep -ir pam_cert_auth /etc/sssd/sssd.conf /etc/sssd/conf.d/ /etc/sssd/sssd.conf:pam_cert_auth = True If "pam_cert_auth" is not set to "True", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000068-GPOS-00036

**Group ID:** `V-274060`

### Rule: Amazon Linux 2023 must map the authenticated identity to the user or group account for PKI-based authentication.

**Rule ID:** `SV-274060r1120168_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without mapping the certificate used to authenticate to the user account, the ability to determine the identity of the individual user or group will not be available for forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system administrator (SA) demonstrates the use of an approved alternate multifactor authentication method, this requirement is not applicable. Verify the certificate of the user or group is mapped to the corresponding user or group in the "sssd.conf" file with the following command: $ sudo find /etc/sssd/sssd.conf /etc/sssd/conf.d/ -type f -exec cat {} \; [sssd] config_file_version = 2 services = pam, sudo, ssh domains = testing.test [pam] pam_cert_auth = True offline_credentials_expiration = 1 [domain/testing.test] id_provider = ldap [certmap/testing.test/rule_name] matchrule =<SAN>.*EDIPI@mil maprule = (userCertificate;binary={cert!bin}) domains = testing.test If the certmap section does not exist, ask the SA to indicate how certificates are mapped to accounts. If there is no evidence of certificate mapping, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-274061`

### Rule: Amazon Linux 2023 must implement certificate status checking for multifactor authentication.

**Rule ID:** `SV-274061r1120171_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a DOD Common Access Card (CAC) or token that is separate from the information system, ensures that even if the information system is compromised, credentials stored on the authentication device will not be affected. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification (PIV) card and the DOD CAC. Amazon Linux 2023 includes multiple options for configuring certificate status checking, but for this requirement focuses on the System Security Services Daemon (SSSD). By default, SSSD performs Online Certificate Status Protocol (OCSP) checking and certificate verification using a sha256 digest function. Satisfies: SRG-OS-000375-GPOS-00160, SRG-OS-000377-GPOS-00162</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system administrator (SA) demonstrates the use of an approved alternate multifactor authentication method, this requirement is not applicable. Verify Amazon Linux 2023 implements Online Certificate Status Protocol (OCSP) and is using the proper digest value on the system with the following command: $ sudo grep -ir certificate_verification /etc/sssd/sssd.conf /etc/sssd/conf.d/ | grep -v "^#" certificate_verification = ocsp_dgst=sha512 If the certificate_verification line is missing from the [sssd] section, or is missing "ocsp_dgst=sha512", ask the administrator to indicate what type of multifactor authentication is being utilized and how the system implements certificate status checking. If there is no evidence of certificate status checking being used, this is a finding.

## Group: SRG-OS-000383-GPOS-00166

**Group ID:** `V-274062`

### Rule: Amazon Linux 2023 must prohibit the use of cached authenticators after one day.

**Rule ID:** `SV-274062r1120174_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cached authentication information is out-of-date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the System Security Services Daemon (SSSD) prohibits the use of cached authentications after one day. Note: Cached authentication settings should be configured even if smart card authentication is not used on the system. Check that SSSD allows cached authentications with the following command: $ sudo grep -ir cache_credentials /etc/sssd/sssd.conf /etc/sssd/conf.d/ /etc/sssd/sssd.conf:cache_credentials = true If "cache_credentials" is set to "false" or missing from the configuration file, this is not a finding and no further checks are required. If "cache_credentials" is set to "true", check that SSSD prohibits the use of cached authentications after one day with the following command: $ sudo grep -ir offline_credentials_expiration /etc/sssd/sssd.conf /etc/sssd/conf.d/ /etc/sssd/sssd.conf:offline_credentials_expiration = 1 If "offline_credentials_expiration" is not set to a value of "1", this is a finding.

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-274063`

### Rule: Amazon Linux 2023, for PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

**Rule ID:** `SV-274063r1120712_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement. Satisfies: SRG-OS-000066-GPOS-00034, SRG-OS-000775-GPOS-00230, SRG-OS-000384-GPOS-00167, SRG-OS-000403-GPOS-00182</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system administrator (SA) demonstrates the use of an approved alternate multifactor authentication method, this requirement is not applicable. Verify Amazon Linux 2023 for PKI-based authentication has valid certificates by constructing a certification path (which includes status information) to an accepted trust anchor. Check that the system has a valid DOD root CA installed with the following command: $ sudo openssl x509 -text -in /etc/sssd/pki/sssd_auth_ca_db.pem Certificate: Data: Version: 3 (0x2) Serial Number: 1 (0x1) Signature Algorithm: sha256WithRSAEncryption Issuer: C = US, O = U.S. Government, OU = DOD, OU = PKI, CN = DOD Root CA 3 Validity Not Before: Mar 20 18:46:41 2012 GMT Not After : Dec 30 18:46:41 2029 GMT Subject: C = US, O = U.S. Government, OU = DOD, OU = PKI, CN = DOD Root CA 3 Subject Public Key Info: Public Key Algorithm: rsaEncryption If the root ca file is not a DOD-issued certificate with a valid date and installed in the /etc/sssd/pki/sssd_auth_ca_db.pem location, this is a finding.

## Group: SRG-OS-000067-GPOS-00035

**Group ID:** `V-274064`

### Rule: Amazon Linux 2023, for PKI-based authentication, must enforce authorized access to the corresponding private key.

**Rule ID:** `SV-274064r1120180_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the private key is discovered, an attacker can use the key to authenticate as an authorized user and gain access to the network infrastructure. The cornerstone of the PKI is the private key used to encrypt or digitally sign information. If the private key is stolen, this will lead to the compromise of the authentication and nonrepudiation gained through PKI because the attacker can use the private key to digitally sign documents and pretend to be the authorized user. Both the holders of a digital certificate and the issuing authority must protect the computers, storage devices, or whatever they use to keep the private keys.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 SSH private key files have a passcode. For each private key stored on the system, use the following command: $ sudo ssh-keygen -y -f /path/to/file If the contents of the key are displayed, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-274065`

### Rule: Amazon Linux 2023 must display the Standard Mandatory DOD Notice and Consent Banner before granting local or remote access to the system.

**Rule ID:** `SV-274065r1120699_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to Amazon Linux 2023 ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the system over any publicly accessible connection. View the file specified by the banner keyword to check that it matches the text of the Standard Mandatory DOD Notice and Consent Banner with the following command: $ more /etc/issue "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the system does not display a logon banner or the banner text does not match the Standard Mandatory DOD Notice and Consent Banner, this is a finding.

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-274066`

### Rule: Amazon Linux 2023 must display the Standard Mandatory DOD Notice and Consent Banner before granting local or remote access to the system via a SSH logon.

**Rule ID:** `SV-274066r1120186_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the system from any SSH connection. Check for the location of the banner file being used with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*banner' /etc/ssh/sshd_config.d/80-bannerPointer.conf:Banner /etc/issue This command will return the banner keyword and the name of the file that contains the SSH banner (in this case "/etc/issue"). If the line is commented out, this is a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-274067`

### Rule: Amazon Linux 2023 must allocate audit record storage capacity to store at least one week's worth of audit records, when audit records are not immediately sent to a central audit record storage facility.

**Rule ID:** `SV-274067r1120653_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure operating systems have a sufficient storage capacity in which to write the audit logs, operating systems must be able to allocate audit record storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 allocates audit record storage capacity to store at least one week of audit records when audit records are not immediately sent to a central audit record storage facility. Note: The partition size needed to capture a week of audit records is based on the activity level of the system and the total storage capacity available. Typically 10.0 GB of storage space for audit records should be sufficient. Determine which partition the audit records are being written to with the following command: $ sudo grep log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Check the size of the partition that audit records are written to with the following command and verify whether it is sufficiently large: # df -h /var/log/audit/ /dev/sda2 24G 10.4G 13.6G 43% /var/log/audit If the audit record partition is not allocated for sufficient storage capacity, this is a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-274068`

### Rule: Amazon Linux 2023 must use a separate file system for the system audit data path.

**Rule ID:** `SV-274068r1120192_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Placing "/var/log/audit" in its own partition enables better separation between audit files and other system files and helps ensure that auditing cannot be halted due to the partition running out of space.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 has a separate file system/partition created for the system audit data path with the following command: Note: /var/log/audit is used as the example as it is a common location. $ mount | grep /var/log/audit UUID=2efb2979-45ac-82d7-0ae632d11f51 on /var/log/home type xfs (rw,realtime,seclabel,attr2,inode64)

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-274069`

### Rule: Amazon Linux 2023 must label all off-loaded audit logs before sending them to the central log server.

**Rule ID:** `SV-274069r1120195_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enriched logging is needed to determine who, what, and when events occur on a system. Without this, determining root cause of an event will be much more difficult.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the Audit Daemon labels all off-loaded audit logs with the following command: $ sudo grep name_format /etc/audit/auditd.conf name_format = hostname If the "name_format" option is not "hostname", "fqd", or "numeric", or the line is commented out, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-274070`

### Rule: Amazon Linux 2023 must take appropriate action when the internal event queue is full.

**Rule ID:** `SV-274070r1120198_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The audit system should have an action setup in the event the internal event queue becomes full so that no data is lost. Information stored in one location is vulnerable to accidental or incidental deletion or alteration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 audit system is configured to take an appropriate action when the internal event queue is full: $ sudo grep -i overflow_action /etc/audit/auditd.conf overflow_action = syslog If the value of the "overflow_action" option is not set to "syslog", "single", "halt" or the line is commented out, ask the system administrator (SA) to indicate how the audit logs are off-loaded to a different system or media. If there is no evidence that the transfer of the audit logs being off-loaded to another system or media takes appropriate action if the internal event queue becomes full, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-274071`

### Rule: Amazon Linux 2023 must take action when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity.

**Rule ID:** `SV-274071r1120201_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches 75 percent utilization, they are unable to plan for audit record storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 takes action when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity with the following command: $ sudo grep -w space_left /etc/audit/auditd.conf space_left = 25% If the value of the "space_left" keyword is not set to 25 percent of the storage volume allocated to audit logs, or if the line is commented out, ask the system administrator (SA) to indicate how the system is providing real-time alerts to the SA and information system security officer (ISSO). If the "space_left" value is not configured to the correct value, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-274072`

### Rule: Amazon Linux 2023 must notify the system administrator (SA) and information system security officer (ISSO) (at a minimum) when allocated audit record storage volume 75 percent utilization.

**Rule ID:** `SV-274072r1120204_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches 75 percent utilization, they are unable to plan for audit record storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 notifies the SA and ISSO (at a minimum) when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity with the following command: $ sudo grep -w space_left_action /etc/audit/auditd.conf space_left_action = email If the value of the "space_left_action" is not set to "email", or if the line is commented out, ask the SA to indicate how the system is providing real-time alerts to the SA and ISSO. If there is no evidence that real-time alerts are configured on the system, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-274073`

### Rule: Amazon Linux 2023 must take action when allocated audit record storage volume reaches 95 percent of the audit record storage capacity.

**Rule ID:** `SV-274073r1120207_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If action is not taken when storage volume reaches 95 percent utilization, the auditing system may fail when the storage volume reaches capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 takes action when allocated audit record storage volume reaches 95 percent of the repository maximum audit record storage capacity with the following command: $ sudo grep -w admin_space_left /etc/audit/auditd.conf admin_space_left = 5% If the value of the "admin_space_left" keyword is not set to 5 percent of the storage volume allocated to audit logs, or if the line is commented out, ask the system administrator (SA) to indicate how the system is taking action if the allocated storage is about to reach capacity. If the "space_left" value is not configured to the correct value, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-274074`

### Rule: Amazon Linux 2023 must take action when allocated audit record storage volume reaches 95 percent of the repository maximum audit record storage capacity.

**Rule ID:** `SV-274074r1120210_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If action is not taken when storage volume reaches 95 percent utilization, the auditing system may fail when the storage volume reaches capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to take action in the event of allocated audit record storage volume reaches 95 percent of the repository maximum audit record storage capacity with the following command: $ sudo grep admin_space_left_action /etc/audit/auditd.conf admin_space_left_action = single If the value of the "admin_space_left_action" is not set to "single", or if the line is commented out, ask the system administrator (SA) to indicate how the system is providing real-time alerts to the SA and information system security officer (ISSO). If there is no evidence that real-time alerts are configured on the system, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-274075`

### Rule: Amazon Linux 2023 must immediately notify the system administrator (SA) and information system security officer (ISSO), at a minimum, of an audit processing failure event.

**Rule ID:** `SV-274075r1120700_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to notify the SA and/or ISSO (at a minimum) in the event of an audit processing failure with the following command: $ sudo grep action_mail_acct /etc/audit/auditd.conf action_mail_acct = root If the value of the "action_mail_acct" keyword is not set to "root" and/or other accounts for security personnel, the "action_mail_acct" keyword is missing, or the retuned line is commented out, ask the SA to indicate how they and the ISSO are notified of an audit process failure. If there is no evidence of the proper personnel being notified of an audit processing failure, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-274076`

### Rule: Amazon Linux 2023 must be configured to off-load audit records onto a different system from the system being audited via syslog.

**Rule ID:** `SV-274076r1120216_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The auditd service does not include the ability to send audit records to a centralized server for management directly. However, it can use a plug-in for audit event multiplexor (audispd) to pass audit records to the local syslog server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured use the audisp-remote syslog service with the following command: $ sudo grep active /etc/audit/plugins.d/syslog.conf active = yes If the "active" keyword does not have a value of "yes", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-274077`

### Rule: Amazon Linux 2023 must authenticate the remote logging server for off-loading audit logs via rsyslog.

**Rule ID:** `SV-274077r1120219_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 authenticates the remote logging server for off-loading audit logs with the following command: $ sudo grep -i '$ActionSendStreamDriverAuthMode' /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.conf:$ActionSendStreamDriverAuthMode x509/name If the value of the "$ActionSendStreamDriverAuthMode" option is not set to "x509/name" or the line is commented out, ask the system administrator (SA) to indicate how the audit logs are off-loaded to a different system or media. If there is no evidence that the transfer of the audit logs being off-loaded to another system or media is encrypted, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-274078`

### Rule: Amazon Linux 2023 must encrypt the transfer of audit records off-loaded onto a different system or media from the system being audited via rsyslog.

**Rule ID:** `SV-274078r1120222_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 encrypts audit records off-loaded onto a different system or media from the system being audited via rsyslog with the following command: $ sudo grep -i '$ActionSendStreamDriverMode' /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.conf:$ActionSendStreamDriverMode 1 If the value of the "$ActionSendStreamDriverMode" option is not set to "1" or the line is commented out, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-274079`

### Rule: Amazon Linux 2023 must encrypt via the gtls driver the transfer of audit records off-loaded onto a different system or media from the system being audited via rsyslog.

**Rule ID:** `SV-274079r1120724_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. Support for both internet and Unix domain sockets enables this utility to support both local and remote logging. Coupling this utility with "gnutls" (a secure communications library implementing the SSL, TLS, and DTLS protocols) creates a method to securely encrypt and off-load auditing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 uses the gtls driver to encrypt audit records off-loaded onto a different system or media from the system being audited with the following command: $ sudo grep -i '$DefaultNetstreamDriver' /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.conf:$DefaultNetstreamDriver ossl If the value of the "$DefaultNetstreamDriver" option is not set to "ossl" or the line is commented out, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-274080`

### Rule: Amazon Linux 2023 must be configured to off-load audit records onto a different system from the system being audited via syslog.

**Rule ID:** `SV-274080r1120228_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The auditd service does not include the ability to send audit records to a centralized server for management directly. However, it can use a plug-in for audit event multiplexor (audispd) to pass audit records to the local syslog server. Satisfies: SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 off-loads audit records onto a different system with the following command: $ more /etc/systemd/journal-upload.conf [Upload] URL=192.168.21.2 ServerKeyFile=/etc/ssl/private/journal-upload.pem ServerCertificateFile=/etc/ssl/certs/journal-upload.pem TrustedCertificateFile=/etc/ssl/ca/trusted.pem If all of the entries do not have values, are commented out, or are missing, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-274081`

### Rule: Amazon Linux 2023 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/sudoers.

**Rule ID:** `SV-274081r1120231_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The actions taken by system administrators must be audited to keep a record of what was executed on the system, as well as for accountability purposes. Editing the sudoers file may be sign of an attacker trying to establish persistent methods to a system, auditing the editing of the sudoers files mitigates this risk. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/sudoers" with the following command: $ sudo auditctl -l | grep '/etc/sudoers[^.]' -w /etc/sudoers -p wa -k identity If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-274082`

### Rule: Amazon Linux 2023 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/sudoers.d/ directory.

**Rule ID:** `SV-274082r1120234_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The actions taken by system administrators must be audited to keep a record of what was executed on the system, as well as for accountability purposes. Editing the sudoers file may be sign of an attacker trying to establish persistent methods to a system, auditing the editing of the sudoers files mitigates this risk. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/sudoers.d/" with the following command: $ sudo auditctl -l | grep /etc/sudoers.d -w /etc/sudoers.d/ -p wa -k identity If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-274083`

### Rule: Amazon Linux 2023 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/group.

**Rule ID:** `SV-274083r1120237_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In addition to auditing new user and group accounts, these watches will alert the system administrator(s) to any modifications. Any unexpected users, groups, or modifications must be investigated for legitimacy. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/group" with the following command: $ sudo auditctl -l | egrep '(/etc/group)' -w /etc/group -p wa -k identity If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-274084`

### Rule: Amazon Linux 2023 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/gshadow.

**Rule ID:** `SV-274084r1120240_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In addition to auditing new user and group accounts, these watches will alert the system administrator(s) to any modifications. Any unexpected users, groups, or modifications must be investigated for legitimacy. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/gshadow" with the following command: $ sudo auditctl -l | egrep '(/etc/gshadow)' -w /etc/gshadow -p wa -k identity If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-274085`

### Rule: Amazon Linux 2023 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/opasswd.

**Rule ID:** `SV-274085r1120243_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In addition to auditing new user and group accounts, these watches will alert the system administrator(s) to any modifications. Any unexpected users, groups, or modifications must be investigated for legitimacy. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/security/opasswd" with the following command: $ sudo auditctl -l | egrep '(/etc/security/opasswd)' -w /etc/security/opasswd -p wa -k identity If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000326-GPOS-00126

**Group ID:** `V-274086`

### Rule: Amazon Linux 2023 must audit uses of the "execve" system call.

**Rule ID:** `SV-274086r1120246_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat. Satisfies: SRG-OS-000326-GPOS-00126, SRG-OS-000327-GPOS-00127</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to audit the execution of the "execve" system call with the following command: $ sudo auditctl -l | grep execve -a always,exit -F arch=b64 -S execve -C uid!=euid -F euid=0 -k execpriv -a always,exit -F arch=b64 -S execve -C gid!=egid -F egid=0 -k execpriv If the command does not return all lines, or the lines are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-274087`

### Rule: Amazon Linux 2023 must audit all uses of the chmod, fchmod, and fchmodat system calls.

**Rule ID:** `SV-274087r1120249_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000064-GPOS-00033, SRG-OS-000466-GPOS-00210, SRG-OS-000458-GPOS-00203</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to audit the execution of the "chmod", "fchmod", and "fchmodat" system calls with the following command: $ sudo auditctl -l | grep chmod -a always,exit -F arch=b64 -S chmod,fchmod,fchmodat -F auid>=1000 -F auid!=unset -k perm_mod If the command does not return the expected line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-274088`

### Rule: Amazon Linux 2023 must audit all uses of the chown, fchown, fchownat, and lchown system calls.

**Rule ID:** `SV-274088r1120252_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000064-GPOS-00033, SRG-OS-000466-GPOS-00210, SRG-OS-000458-GPOS-00203</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to audit the execution of the "chown", "fchown", "fchownat", and "lchown" system calls with the following command: $ sudo auditctl -l | grep chown -a always,exit -F arch=b64 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=unset -k perm_mod If the command does not return the expected line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-274089`

### Rule: Amazon Linux 2023 must audit all uses of the setxattr, fsetxattr, lsetxattr, removexattr, fremovexattr, and lremovexattr system calls.

**Rule ID:** `SV-274089r1120255_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000064-GPOS-00033, SRG-OS-000466-GPOS-00210, SRG-OS-000471-GPOS-00216, SRG-OS-000458-GPOS-00203, SRG-OS-000474-GPOS-00219</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to audit the execution of the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr" system calls with the following command: $ sudo auditctl -l | grep xattr -a always,exit -F arch=b64 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b64 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid=0 -k perm_mod If the audit rules are not defined for the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr" system calls, or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-274090`

### Rule: Amazon Linux 2023 must audit all uses of the truncate, ftruncate, creat, open, openat, and open_by_handle_at system calls.

**Rule ID:** `SV-274090r1120258_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000064-GPOS-00033, SRG-OS-000466-GPOS-00210, SRG-OS-000458-GPOS-00203</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to audit successful/unsuccessful attempts to use the "truncate", "ftruncate", "creat", "open", "openat", and "open_by_handle_at" system calls with the following command: $ sudo auditctl -l | grep 'open\|truncate\|creat' -a always,exit -F arch=b64 -S truncate,ftruncate,creat,open,openat,open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b64 -S truncate,ftruncate,creat,open,openat,open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access If the output does not produce rules containing "-F exit=-EPERM", this is a finding. If the output does not produce rules containing "-F exit=-EACCES", this is a finding. If the command does not return an audit rule for "truncate", "ftruncate", "creat", "open", "openat", and "open_by_handle_at" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-274091`

### Rule: Amazon Linux 2023 must audit all uses of the init_module and finit_module system calls.

**Rule ID:** `SV-274091r1120261_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000064-GPOS-00033, SRG-OS-000466-GPOS-00210, SRG-OS-000458-GPOS-00203</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to audit the execution of the "init_module" and "finit_module" system calls with the following command: $ sudo auditctl -l | grep init_module -a always,exit -F arch=b64 -S init_module,finit_module -F auid>=1000 -F auid!=unset -k module_chng If audit rule is not defined for the "delete_module" system call, or the line returned is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-274092`

### Rule: Amazon Linux 2023 must audit all uses of the create_module system call.

**Rule ID:** `SV-274092r1120264_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000064-GPOS-00033, SRG-OS-000466-GPOS-00210, SRG-OS-000458-GPOS-00203</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 generates audit records when successful/unsuccessful attempts to use the "create_module" syscall occur with the following command: $ sudo auditctl -l | grep "create_module" -a always,exit -F arch=b64 -S create_module -F auid>=1000 -F auid!=-1 -F key=module-change If audit rule is not defined for the "create_module" syscall, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-274093`

### Rule: Amazon Linux 2023 must audit all uses of the kmod command.

**Rule ID:** `SV-274093r1120267_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000064-GPOS-00033, SRG-OS-000466-GPOS-00210, SRG-OS-000458-GPOS-00203</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 generates audit records when successful/unsuccessful attempts to use the "kmod" command occur. Check the auditing rules in "/etc/audit/audit.rules" with the following command: $ sudo auditctl -l | grep kmod -a always,exit -F path=/usr/bin/kmod -F perm=x -F auid>=1000 -F auid!=unset -k modules If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-274094`

### Rule: Amazon Linux 2023 must audit all uses of the rename, unlink, rmdir, renameat, and unlinkat system calls.

**Rule ID:** `SV-274094r1120270_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000466-GPOS-00210, SRG-OS-000467-GPOS-00211, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to audit successful/unsuccessful attempts to use the "rename", "unlink", "rmdir", "renameat", and "unlinkat" system calls with the following command: $ sudo auditctl -l | grep 'rename\|unlink\|rmdir' -a always,exit -F arch=b64 -S rename,unlink,rmdir,renameat,unlinkat -F auid>=1000 -F auid!=unset -k delete If the command does not return an audit rule for "rename", "unlink", "rmdir", "renameat", and "unlinkat" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-274095`

### Rule: Amazon Linux 2023 must audit all uses of the chcon command.

**Rule ID:** `SV-274095r1120273_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215, SRG-OS-000463-GPOS-00207, SRG-OS-000465-GPOS-00209</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to audit the execution of the "chcon" command with the following command: $ sudo auditctl -l | grep chcon -a always,exit -F path=/usr/bin/chcon -F perm=x -F auid>=1000 -F auid!=unset -k perm_mod If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000392-GPOS-00172

**Group ID:** `V-274096`

### Rule: Amazon Linux 2023 must generate audit records for all account creations, modifications, disabling, and termination events that affect /var/log/faillock.

**Rule ID:** `SV-274096r1120276_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Satisfies: SRG-OS-000392-GPOS-00172, SRG-OS-000470-GPOS-00214, SRG-OS-000473-GPOS-00218</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 generates audit records for all account creations, modifications, disabling, and termination events that affect "/var/log/faillock" with the following command: $ sudo auditctl -l | grep /var/log/faillock -w /var/log/faillock -p wa -k logins If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-274097`

### Rule: Amazon Linux 2023 must generate audit records for all account creations, modifications, disabling, and termination events that affect /var/log/lastlog.

**Rule ID:** `SV-274097r1120279_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000473-GPOS-00218, SRG-OS-000470-GPOS-00214</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 generates audit records for all account creations, modifications, disabling, and termination events that affect "/var/log/lastlog" with the following command: $ sudo auditctl -l | grep /var/log/lastlog -w /var/log/lastlog -p wa -k logins If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-274098`

### Rule: Amazon Linux 2023 must audit all uses of the init command.

**Rule ID:** `SV-274098r1120282_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of the init command may cause availability issues for the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to audit the execution of the "init" command with the following command: $ sudo auditctl -l | grep init -a always,exit -F path=/usr/sbin/init -F perm=x -F auid>=1000 -F auid!=unset -k privileged-init If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-274099`

### Rule: Amazon Linux 2023 must audit all uses of the reboot command.

**Rule ID:** `SV-274099r1120285_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of the reboot command may cause availability issues for the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to audit the execution of the "reboot" command with the following command: $ sudo auditctl -l | grep reboot -a always,exit -F path=/usr/sbin/reboot -F perm=x -F auid>=1000 -F auid!=unset -k privileged-reboot If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-274100`

### Rule: Amazon Linux 2023 must audit all uses of the shutdown command.

**Rule ID:** `SV-274100r1120288_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of the shutdown command may cause availability issues for the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to audit the execution of the "shutdown" command with the following command: $ sudo auditctl -l | grep shutdown -a always,exit -F path=/usr/sbin/shutdown -F perm=x -F auid>=1000 -F auid!=unset -k privileged-shutdown If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-274101`

### Rule: Amazon Linux 2023 audit tools must have a mode of "0755" or less permissive.

**Rule ID:** `SV-274101r1120291_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 audit tools have a mode of "0755" or less with the following command: $ stat -c "%a %n" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/rsyslogd /sbin/augenrules 755 /sbin/auditctl 755 /sbin/aureport 755 /sbin/ausearch 750 /sbin/autrace 755 /sbin/auditd 755 /sbin/rsyslogd 755 /sbin/augenrules If any of the audit tool files have a mode more permissive than "0755", this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-274102`

### Rule: Amazon Linux 2023 audit tools must be owned by root.

**Rule ID:** `SV-274102r1120294_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 audit tools are owned by "root" with the following command: $ sudo stat -c "%U %n" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/rsyslogd /sbin/augenrules root /sbin/auditctl root /sbin/aureport root /sbin/ausearch root /sbin/autrace root /sbin/auditd root /sbin/rsyslogd root /sbin/augenrules If any audit tools do not have an owner of "root", this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-274103`

### Rule: Amazon Linux 2023 audit tools must be group-owned by root.

**Rule ID:** `SV-274103r1120297_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. Operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 audit tools are group owned by "root" with the following command: $ sudo stat -c "%G %n" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/rsyslogd /sbin/augenrules root /sbin/auditctl root /sbin/aureport root /sbin/ausearch root /sbin/autrace root /sbin/auditd root /sbin/rsyslogd root /sbin/augenrules If any audit tools do not have a group owner of "root", this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-274104`

### Rule: Amazon Linux 2023 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/passwd.

**Rule ID:** `SV-274104r1120300_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create an account. Auditing account creation actions provides logging that can be used for forensic purposes. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221, SRG-OS-000274-GPOS-00104, SRG-OS-000275-GPOS-00105, SRG-OS-000276-GPOS-00106, SRG-OS-000277-GPOS-00107</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/passwd" with the following command: $ sudo auditctl -l | egrep '(/etc/passwd)' -w /etc/passwd -p wa -k identity If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-274105`

### Rule: Amazon Linux 2023 must audit all successful/unsuccessful uses of the chage command.

**Rule ID:** `SV-274105r1120661_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000064-GPOS-00033, SRG-OS-000466-GPOS-00210, SRG-OS-000458-GPOS-00203</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that an audit event is generated for any successful/unsuccessful use of the "chage" command by performing the following command to check the file system rules in "/etc/audit/audit.rules": $ sudo grep -w chage /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chage -F perm=x -F auid>=1000 -F auid!=unset -k privileged-chage If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-274106`

### Rule: Amazon Linux 2023 must alert the information system security officer (ISSO) and system administrator (SA), at a minimum, in the event of an audit processing failure.

**Rule ID:** `SV-274106r1120657_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to notify the SA and ISSO, at a minimum, in the event of an audit processing failure with the following command: $ sudo grep action_mail_acct /etc/audit/auditd.conf action_mail_acct = root If the value of the "action_mail_acct" keyword is not set to "root" and/or other accounts for security personnel, the "action_mail_acct" keyword is missing, or the retuned line is commented out, ask the SA to indicate how they and the ISSO are notified of an audit process failure. If there is no evidence of the proper personnel being notified of an audit processing failure, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-274107`

### Rule: Amazon Linux 2023 must off-load audit records onto a different system in the event the audit storage volume is full.

**Rule ID:** `SV-274107r1120309_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 takes the appropriate action when the audit storage volume is full using the following command: $ sudo grep disk_full_action /etc/audit/auditd.conf disk_full_action = SYSLOG If the value of the "disk_full_action" option is not "SYSLOG", "SINGLE", or "HALT", or the line is commented out, ask the system administrator to indicate how the system takes appropriate action when an audit storage volume is full. If there is no evidence of appropriate action, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-274108`

### Rule: Amazon Linux 2023 audit logs must be group-owned by root or by a restricted logging group to prevent unauthorized read access.

**Rule ID:** `SV-274108r1120312_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029, SRG-OS-000206-GPOS-00084</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 audit logs are group-owned by "root" or a restricted logging group. First determine if a group other than "root" has been assigned to the audit logs with the following command: $ sudo grep log_group /etc/audit/auditd.conf log_group = root Then determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Then using the location of the audit log file, determine if the audit log is group-owned by "root" using the following command: $ sudo stat -c "%G %n" /var/log/audit/audit.log root /var/log/audit/audit.log If the audit log is not group-owned by "root" or the configured alternative logging group, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-274109`

### Rule: Amazon Linux 2023 audit log directory must be owned by root to prevent unauthorized read access.

**Rule ID:** `SV-274109r1120315_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029, SRG-OS-000206-GPOS-00084</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 audit logs directory is owned by "root". First determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Then using the location of the audit log file, determine if the audit log directory is owned by "root" using the following command: $ sudo ls -ld /var/log/audit drwx------ 2 root root 23 Jun 11 11:56 /var/log/audit If the audit log directory is not owned by "root", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-274110`

### Rule: Amazon Linux 2023 audit logs file must have mode "0600" or less permissive to prevent unauthorized access to the audit log.

**Rule ID:** `SV-274110r1120318_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029, SRG-OS-000206-GPOS-00084</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 audit logs have a mode of "0600". First determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Then using the location of the audit log file, determine if the audit log files as a mode of "0640" with the following command: $ sudo find /var/log/audit/ -type f -exec stat -c '%a %n' {} \; 600 /var/log/audit/audit.log If the audit logs have a mode more permissive than "0600", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-274111`

### Rule: Amazon Linux 2023 must allow only the information system security manager (ISSM) (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited.

**Rule ID:** `SV-274111r1120321_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that files in "/etc/audit/rules.d/" and the "/etc/audit/auditd.conf" file have a mode of "0640" or less permissive by using the following commands: $ sudo find /etc/audit/rules.d/ /etc/audit/audit.rules /etc/audit/auditd.conf -type f -exec stat -c "%a %n" {} \; 600 /etc/audit/rules.d/audit.rules 640 /etc/audit/audit.rules 640 /etc/audit/auditd.conf If the files in the "/etc/audit/rules.d/" directory or the "/etc/audit/auditd.conf" file have a mode more permissive than "0640", this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-274112`

### Rule: Amazon Linux 2023 must audit all uses of the sudo command.

**Rule ID:** `SV-274112r1120324_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000064-GPOS-00033, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000466-GPOS-00210, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to audit the execution of the "sudo" command with the following command: $ sudo auditctl -l | grep '/usr/bin/sudo\b' -a always,exit -S all -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -F auid!=-1 -F key=priv_cmd If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-274113`

### Rule: Amazon Linux 2023 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/passwd.

**Rule ID:** `SV-274113r1120327_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In addition to auditing new user and group accounts, these watches will alert the system administrator(s) (SAs) to any modifications. Any unexpected users, groups, or modifications should be investigated for legitimacy. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221, SRG-OS-000274-GPOS-00104, SRG-OS-000275-GPOS-00105, SRG-OS-000276-GPOS-00106, SRG-OS-000277-GPOS-00107</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/passwd" with the following command: $ sudo auditctl -l | egrep '(/etc/passwd)' -w /etc/passwd -p wa -k identity If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-274114`

### Rule: Amazon Linux 2023 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/shadow.

**Rule ID:** `SV-274114r1120330_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In addition to auditing new user and group accounts, these watches will alert the system administrator(s) (SAs) to any modifications. Any unexpected users, groups, or modifications should be investigated for legitimacy. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221, SRG-OS-000275-GPOS-00105</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/shadow with the following command: $ sudo auditctl -l | egrep '(/etc/shadow)' -w /etc/shadow -p wa -k identity If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000255-GPOS-00096

**Group ID:** `V-274115`

### Rule: Amazon Linux 2023 must produce audit records containing information to establish the identity of any individual or process associated with the event.

**Rule ID:** `SV-274115r1120333_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without information that establishes the identity of the subjects (i.e., users or processes acting on behalf of users) associated with the events, security personnel cannot determine responsibility for the potentially harmful event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the audit system resolves audit information before writing to disk, with the following command: $ sudo grep log_format /etc/audit/auditd.conf log_format = ENRICHED If the "log_format" option is not "ENRICHED", or the line is commented out, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-274116`

### Rule: Amazon Linux 2023 audit logs must be group-owned by root or by a restricted logging group to prevent unauthorized read access.

**Rule ID:** `SV-274116r1120336_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify Amazon Linux 2023 or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the audit logs are group-owned by "root" or a restricted logging group. First determine if a group other than "root" has been assigned to the audit logs with the following command: $ sudo grep log_group /etc/audit/auditd.conf Then determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Then using the location of the audit log file, determine if the audit log is group-owned by "root" using the following command: $ sudo stat -c "%G %n" /var/log/audit/audit.log root /var/log/audit/audit.log If the audit log is not group-owned by "root" or the configured alternative logging group, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-274117`

### Rule: Amazon Linux 2023 must ensure the audit log directory be owned by root to prevent unauthorized read access.

**Rule ID:** `SV-274117r1120339_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify Amazon Linux 2023 or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the audit logs directory is owned by "root". First determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Then using the location of the audit log file, determine if the audit log directory is owned by "root" using the following command: sudo stat -c '%U %n' /var/log/audit root /var/log/audit If the audit log directory is not owned by "root", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-274118`

### Rule: Amazon Linux 2023 audit logs file must have mode "0600" or less permissive to prevent unauthorized access to the audit log.

**Rule ID:** `SV-274118r1120342_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify Amazon Linux 2023 or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the audit logs have a mode of "0600". First determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Then using the location of the audit log file, determine if the audit log files as a mode of "0640" with the following command: $ sudo find /var/log/audit/ -type f -exec stat -c '%a %n' {} \; 600 /var/log/audit/audit.log If the audit logs have a mode more permissive than "0600", this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-274119`

### Rule: Amazon Linux 2023 library directories must be group-owned by root or a system account.

**Rule ID:** `SV-274119r1120345_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Amazon Linux 2023 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 systemwide shared library directories are group-owned by "root" with the following command: $ sudo find /lib /lib64 /usr/lib /usr/lib64 ! -group root -type d -exec stat -c "%n %G" '{}' \; If any systemwide shared library directory is returned and is not group-owned by a required system account, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-274120`

### Rule: Amazon Linux 2023 library directories must have mode "755" or less permissive.

**Rule ID:** `SV-274120r1120348_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Amazon Linux 2023 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 systemwide shared library directories have mode "755" or less permissive with the following command: $ sudo find -L /lib /lib64 /usr/lib /usr/lib64 -perm /022 -type d -exec ls -l {} \; If any systemwide shared library file is found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-274121`

### Rule: Amazon Linux 2023 library files must have mode "755" or less permissive.

**Rule ID:** `SV-274121r1120351_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Amazon Linux 2023 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges. Only qualified and authorized individuals will be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 systemwide shared library files contained in the following directories have mode "755" or less permissive with the following command: $ sudo find -L /lib /lib64 /usr/lib /usr/lib64 -perm /022 -type f -exec ls -l {} \; If any systemwide shared library file is found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-274122`

### Rule: Amazon Linux 2023 library files must be owned by root.

**Rule ID:** `SV-274122r1120354_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Amazon Linux 2023 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges. Only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 systemwide shared library files are owned by "root" with the following command: $ sudo find -L /lib /lib64 /usr/lib /usr/lib64 ! -user root -exec ls -l {} \; If any systemwide shared library file is not owned by root, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-274123`

### Rule: Amazon Linux 2023 library files must be group-owned by root or a system account.

**Rule ID:** `SV-274123r1120357_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Amazon Linux 2023 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 systemwide shared library files are group-owned by "root" with the following command: $ sudo find -L /lib /lib64 /usr/lib /usr/lib64 ! -group root -exec ls -l {} \; If any systemwide shared library file is returned and is not group-owned by a required system account, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-274124`

### Rule: Amazon Linux 2023 library directories must be owned by root.

**Rule ID:** `SV-274124r1120360_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Amazon Linux 2023 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 systemwide shared library directories are owned by "root" with the following command: $ sudo find /lib /lib64 /usr/lib /usr/lib64 ! -user root -type d -exec stat -c "%n %U" '{}' \; If any systemwide shared library directory is not owned by root, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-274125`

### Rule: Amazon Linux 2023 must ensure the /var/log directory have mode "0755" or less permissive.

**Rule ID:** `SV-274125r1120363_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify Amazon Linux 2023 or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the "/var/log" directory has a mode of "0755" or less permissive with the following command: $ stat -c '%a %n' /var/log 755 /var/log If "/var/log" does not have a mode of "0755" or less permissive, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-274126`

### Rule: Amazon Linux 2023 must ensure the /var/log directory be owned by root.

**Rule ID:** `SV-274126r1120366_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify Amazon Linux 2023 or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the "/var/log" directory is owned by root with the following command: $ stat -c "%U %n" /var/log root /var/log If "/var/log" does not have an owner of "root", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-274127`

### Rule: Amazon Linux 2023 must ensure the /var/log directory be group-owned by root.

**Rule ID:** `SV-274127r1120369_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify Amazon Linux 2023 or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so the "/var/log" directory is group-owned by root with the following command: $ stat -c "%G %n" /var/log root /var/log If "/var/log" does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-274128`

### Rule: Amazon Linux 2023 must ensure the /var/log/messages file have mode "0640" or less permissive.

**Rule ID:** `SV-274128r1120372_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify Amazon Linux 2023 or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the "/var/log/messages" file has a mode of "0640" or less permissive with the following command: $ stat -c '%a %n' /var/log/messages 600 /var/log/messages If "/var/log/messages" does not have a mode of "0640" or less permissive, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-274129`

### Rule: Amazon Linux 2023 must ensure the /var/log/messages file be group-owned by root.

**Rule ID:** `SV-274129r1120375_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify Amazon Linux 2023 or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the "/var/log/messages" file is group-owned by root with the following command: $ stat -c "%G %n" /var/log/messages root /var/log/messages If "/var/log/messages" does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-274130`

### Rule: Amazon Linux 2023 must ensure the /var/log/messages file be owned by root.

**Rule ID:** `SV-274130r1120378_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify Amazon Linux 2023 or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the "/var/log/messages" file is owned by root with the following command: $ stat -c "%U %n" /var/log/messages root /var/log/messages If "/var/log/messages" does not have an owner of "root", this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-274131`

### Rule: Amazon Linux 2023 system commands must be owned by root.

**Rule ID:** `SV-274131r1120381_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Amazon Linux 2023 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 system commands contained in the following directories are owned by "root" with the following command: $ sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/libexec /usr/local/bin /usr/local/sbin ! -user root -exec ls -l {} \; If any system commands are found to not be owned by root, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-274132`

### Rule: Amazon Linux 2023 system commands must be group-owned by root or a system account.

**Rule ID:** `SV-274132r1120384_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Amazon Linux 2023 were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 system commands contained in the following directories are group-owned by "root", or a required system account, with the following command: $ sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -group root -exec ls -l {} \; If any system commands are returned and is not group-owned by a required system account, this is a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-274133`

### Rule: Amazon Linux 2023 must enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-274133r1120387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Satisfies: SRG-OS-000069-GPOS-00037, SRG-OS-000725-GPOS-00180</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 enforces password complexity by requiring that at least one uppercase character with the following command: $ sudo grep ucredit /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf ucredit = -1 If the value of "ucredit" is a positive number or is commented out, this is a finding.

## Group: SRG-OS-000070-GPOS-00038

**Group ID:** `V-274134`

### Rule: Amazon Linux 2023 must enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-274134r1120390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Satisfies: SRG-OS-000070-GPOS-00038, SRG-OS-000725-GPOS-00180</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 enforces password complexity by requiring that at least one lowercase character with the following command: $ sudo grep lcredit /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf lcredit = -1 If the value of "lcredit" is a positive number or is commented out, this is a finding.

## Group: SRG-OS-000071-GPOS-00039

**Group ID:** `V-274135`

### Rule: Amazon Linux 2023 must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-274135r1120393_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Satisfies: SRG-OS-000071-GPOS-00039, SRG-OS-000725-GPOS-00180</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 enforces password complexity by requiring that at least one numeric character with the following command: $ sudo grep dcredit /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf dcredit = -1 If the value of "dcredit" is a positive number or is commented out, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-274136`

### Rule: Amazon Linux 2023 must require the change of at least 50 percent of the total number of characters when passwords are changed.

**Rule ID:** `SV-274136r1120697_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Amazon Linux 2023 allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. If the password length is an odd number then number of changed characters must be rounded up. For example, a password length of 15 characters must require the change of at least 8 characters. Satisfies: SRG-OS-000072-GPOS-00040, SRG-OS-000725-GPOS-00180</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 enforces password complexity by requiring that at least a change of at least eight characters when passwords are changed with the following command: $ sudo grep difok /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf difok = 8 If the value of "difok" is set to less than "8", or is commented out, this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-274137`

### Rule: Amazon Linux 2023 must enforce a minimum 15-character password length.

**Rule ID:** `SV-274137r1120725_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password. Satisfies: SRG-OS-000078-GPOS-00046, SRG-OS-000725-GPOS-00180</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 enforces a minimum 15-character password length with the following command: $ sudo grep -rs minlen /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf /etc/security/pwquality.conf: minlen = 15 If the command does not return a "minlen" value of 15 or greater, or the line is commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000266-GPOS-00101

**Group ID:** `V-274138`

### Rule: Amazon Linux 2023 must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-274138r1120402_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity or strength is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor in determining how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Special characters are those characters that are not alphanumeric. Examples include: ~ ! @ # $ % ^ *. Satisfies: SRG-OS-000266-GPOS-00101, SRG-OS-000725-GPOS-00180</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 enforces password complexity by requiring at least one special character with the following command: $ sudo grep -rs ocredit /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf /etc/security/pwquality.conf: ocredit = -1 If the value of "ocredit" is a positive number or is commented out, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-274139`

### Rule: Amazon Linux 2023 must enforce password complexity rules for the root account.

**Rule ID:** `SV-274139r1120405_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Satisfies: SRG-OS-000072-GPOS-00040, SRG-OS-000071-GPOS-00039, SRG-OS-000070-GPOS-00038, SRG-OS-000266-GPOS-00101, SRG-OS-000078-GPOS-00046, SRG-OS-000069-GPOS-00037</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 enforces password complexity rules for the root account with the following command: $ sudo grep -rs enforce_for_root /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf /etc/security/pwquality.conf:enforce_for_root If "enforce_for_root" is commented or missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-274140`

### Rule: Amazon Linux 2023 must prevent the use of dictionary words for passwords.

**Rule ID:** `SV-274140r1120408_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If Amazon Linux 2023 allows the user to select passwords based on dictionary words, this increases the chances of password compromise by increasing the opportunity for successful guesses, and brute-force attacks. Satisfies: SRG-OS-000480-GPOS-00225, SRG-OS-000710-GPOS-00160</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 prevents the use of dictionary words for passwords with the following command: $ sudo grep -rs dictcheck /etc/security/pwquality.conf /etc/pwquality.conf.d/*.conf /etc/security/pwquality.conf:dictcheck=1 If the "dictcheck" parameter is not set to "1", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000027-GPOS-00008

**Group ID:** `V-274141`

### Rule: Amazon Linux 2023 must limit the number of concurrent sessions to ten for all accounts and/or account types.

**Rule ID:** `SV-274141r1120411_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Operating system management includes the ability to control the number of users and user sessions that utilize an operating system. Limiting the number of allowed users and sessions per user is helpful in reducing the risks related to denial-of-service (DoS) attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based on mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 limits the number of concurrent sessions to "10" for all accounts and/or account types with the following command: $ sudo grep -r -s '^[^#].*maxlogins' /etc/security/limits.conf /etc/security/limits.d/*.conf * hard maxlogins 10 This can be set as a global domain (with the * wildcard) but may be set differently for multiple domains. If the "maxlogins" item is missing, commented out, or the value is set greater than "10" and is not documented with the information system security officer (ISSO) as an operational requirement for all domains that have the "maxlogins" item assigned, this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-274142`

### Rule: Amazon Linux 2023 must automatically exit interactive command shell user sessions after 15 minutes of inactivity.

**Rule ID:** `SV-274142r1120414_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle interactive command shell user session within a short time period reduces the window of opportunity for unauthorized personnel to take control of it when left unattended in a virtual terminal or physical console.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to exit interactive command shell user sessions after 10 minutes of inactivity or less with the following command: $ sudo grep -i tmout /etc/profile /etc/profile.d/*.sh /etc/profile.d/tmout.sh:declare -xr TMOUT=600 If "TMOUT" is not set to "600" or less in a script located in the "/etc/'profile.d/ directory, is missing or is commented out, this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-274143`

### Rule: Amazon Linux 2023 must enforce 24 hours/1 day as the minimum password lifetime.

**Rule ID:** `SV-274143r1120417_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 enforces 24 hours as the minimum password lifetime for new user accounts with the following command: $ sudo grep -i pass_min_days /etc/login.defs PASS_MIN_DAYS 1 If the "PASS_MIN_DAYS" parameter value is not "1" or greater, or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-274144`

### Rule: Amazon Linux 2023 must enforce a delay of at least four seconds between logon prompts following a failed logon attempt.

**Rule ID:** `SV-274144r1120420_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Increasing the time between a failed authentication attempt and re-prompting to enter credentials helps to slow a single-threaded brute force attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 enforces a delay of at least four seconds between console logon prompts following a failed logon attempt with the following command: $ sudo grep -i fail_delay /etc/login.defs FAIL_DELAY 4 If the value of "FAIL_DELAY" is not set to "4" or greater, the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-274145`

### Rule: Amazon Linux 2023 must define default permissions for all authenticated users in such a way that the user can only read and modify their own files.

**Rule ID:** `SV-274145r1120423_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the most restrictive default permissions ensures that when new accounts are created, they do not have unnecessary access. Satisfies: SRG-OS-000480-GPOS-00228, SRG-OS-000480-GPOS-00230</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 defines default permissions for all authenticated users in such a way that the user can only read and modify their own files with the following command: Note: If the value of the "UMASK" parameter is set to "000" in "/etc/login.defs" file, the Severity is raised to a CAT I. # grep -i umask /etc/login.defs UMASK 077 If the value for the "UMASK" parameter is not "077", or the "UMASK" parameter is missing or is commented out, this is a finding.

## Group: SRG-OS-000002-GPOS-00002

**Group ID:** `V-274146`

### Rule: Amazon Linux 2023 must automatically remove or disable temporary user accounts after 72 hours.

**Rule ID:** `SV-274146r1120426_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If temporary user accounts remain active when no longer needed or for an excessive period, these accounts may be used to gain unauthorized access. To mitigate this risk, automated termination of all temporary accounts must be set upon account creation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 temporary accounts have been provisioned with an expiration date of 72 hours. For every existing temporary account, run the following command to obtain its account expiration information. $ sudo chage -l system_account_name Verify each of these accounts has an expiration date set within 72 hours. If any temporary accounts have no expiration date set or do not expire within 72 hours, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-274147`

### Rule: Amazon Linux 2023 must automatically lock an account when three unsuccessful logon attempts occur.

**Rule ID:** `SV-274147r1120429_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. Amazon Linux 2023 can utilize the "pam_faillock.so" for this purpose. Note that manual changes to the listed files may be overwritten by the "authselect" program. From "Pam_Faillock" man pages: Note that the default directory that "pam_faillock" uses is usually cleared on system boot so the access will be re-enabled after system reboot. If that is undesirable, a different tally directory must be set with the "dir" option.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 locks an account after three unsuccessful logon attempts with the following commands: Note: If the system administrator demonstrates the use of an approved centralized account management method that locks an account after three unsuccessful logon attempts within a period of 15 minutes, this requirement is met by that method. $ sudo grep pam_faillock.so /etc/pam.d/password-auth auth required pam_faillock.so preauth dir=/var/log/faillock silent audit deny=3 even_deny_root fail_interval=900 unlock_time=0 auth required pam_faillock.so authfail dir=/var/log/faillock unlock_time=0 account required pam_faillock.so If the "deny" option is not set to "3" or less (but not "0") on the "preauth" line with the "pam_faillock.so" module, or is missing from this line, if any of the lines are commented out, or are missing, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-274148`

### Rule: Amazon Linux 2023 must be able to enforce a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-274148r1120432_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If Amazon Linux 2023 does not limit the lifetime of passwords and force users to change their passwords, there is the risk that Amazon Linux 2023 passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 enforces the maximum time period for existing passwords is restricted to 60 days with the following commands: $ sudo awk -F: '$5 > 60 {print $1 " " $5}' /etc/shadow $ sudo awk -F: '$5 <= 0 {print $1 " " $5}' /etc/shadow If any results are returned that are not associated with a system account, this is a finding.

## Group: SRG-OS-000118-GPOS-00060

**Group ID:** `V-274149`

### Rule: Amazon Linux 2023 must disable account identifiers (individuals, groups, roles, and devices) after 35 days of inactivity.

**Rule ID:** `SV-274149r1120435_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. Operating systems need to track periods of inactivity and disable application identifiers after 35 days of inactivity. Satisfies: SRG-OS-000118-GPOS-00060, SRG-OS-000590-GPOS-00110</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 account identifiers (individuals, groups, roles, and devices) are disabled after 35 days of inactivity with the following command: Check the account inactivity value by performing the following command: $ sudo grep -i inactive /etc/default/useradd INACTIVE=35 If "INACTIVE" is set to "-1", a value greater than "35", or is commented out, this is a finding.

## Group: SRG-OS-000123-GPOS-00064

**Group ID:** `V-274150`

### Rule: Amazon Linux 2023 must automatically expire temporary accounts within 72 hours.

**Rule ID:** `SV-274150r1120438_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Temporary accounts are privileged or nonprivileged accounts that are established during pressing circumstances, such as new software or hardware configuration or an incident response, where the need for prompt account activation requires bypassing normal account authorization procedures. If any inactive temporary accounts are left enabled on the system and are not either manually removed or automatically expired within 72 hours, the security posture of the system will be degraded and exposed to exploitation by unauthorized users or insider threat actors. Temporary accounts are different from emergency accounts. Emergency accounts, also known as "last resort" or "break glass" accounts, are local logon accounts enabled on the system for emergency use by authorized system administrators to manage a system when standard logon methods are failing or not available. Emergency accounts are not subject to manual removal or scheduled expiration requirements. The automatic expiration of temporary accounts may be extended as needed by the circumstances but it must not be extended indefinitely. A documented permanent account must be established for privileged users who need long-term maintenance accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 temporary accounts have been provisioned with an expiration date of 72 hours. For every existing temporary account, run the following command to obtain its account expiration information: $ sudo chage -l <temporary_account_name> | grep -i "account expires" Verify each of these accounts has an expiration date set within 72 hours. If any temporary accounts have no expiration date set or do not expire within 72 hours, this is a finding.

## Group: SRG-OS-000312-GPOS-00123

**Group ID:** `V-274151`

### Rule: Amazon Linux 2023 must restrict the use of the "su" command.

**Rule ID:** `SV-274151r1120441_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "su" program allows to run commands with a substitute user and group ID. It is commonly used to run commands as the root user. Limiting access to such commands is considered a good security practice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 requires uses to be members of the "wheel" group with the following command: $ grep pam_wheel /etc/pam.d/su auth required pam_wheel.so use_uid If a line for "pam_wheel.so" does not exist, or is commented out, this is a finding.

## Group: SRG-OS-000445-GPOS-00199

**Group ID:** `V-274152`

### Rule: Amazon Linux 2023 must enable the SELinux targeted policy.

**Rule ID:** `SV-274152r1120738_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the SELinux policy to "targeted" or a more specialized policy ensures the system will confine processes that are likely to be targeted for exploitation, such as network or system services. Note: During the development or debugging of SELinux modules, it is common to temporarily place nonproduction systems in "permissive" mode. In such temporary cases, SELinux policies should be developed, and once work is completed, the system should be reconfigured to "targeted".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 SELINUX is using the targeted policy with the following command: $ sestatus | grep policy Loaded policy name: targeted If the loaded policy name is not "targeted", this is a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-274153`

### Rule: Amazon Linux 2023 must use a Linux Security Module configured to enforce limits on system services.

**Rule ID:** `SV-274153r1120713_rule`
**Severity:** high

**Description:**
<VulnDiscussion>An isolation boundary provides access control and protects the integrity of the hardware, software, and firmware that perform security functions. Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Operating systems implement code separation (i.e., separation of security functions from nonsecurity functions) in a number of ways, including through the provision of security kernels via processor rings or processor modes. For nonkernel code, security function isolation is often achieved through file system protections that serve to protect the code on disk and address space protections that protect executing code. Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Implementation may include isolation of memory space and libraries. Operating systems restrict access to security functions through the use of access control mechanisms and by implementing least privilege capabilities. Satisfies: SRG-OS-000134-GPOS-00068, SRG-OS-000445-GPOS-00199</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 verifies the correct operation of security functions through the use of SELinux with the following command: $ getenforce Enforcing If SELINUX is not set to "Enforcing", this is a finding.

## Group: SRG-OS-000329-GPOS-00128

**Group ID:** `V-274154`

### Rule: Amazon Linux 2023 must automatically lock an account when three unsuccessful logon attempts occur.

**Rule ID:** `SV-274154r1120450_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to lock an account after three unsuccessful logon attempts with the command: $ grep 'deny =' /etc/security/faillock.conf deny = 3 If the "deny" option is not set to "3" or less (but not "0"), is missing or commented out, this is a finding.

## Group: SRG-OS-000329-GPOS-00128

**Group ID:** `V-274155`

### Rule: Amazon Linux 2023 must automatically lock the root account until the root account is released by an administrator when three unsuccessful logon attempts occur during a 15-minute time period.

**Rule ID:** `SV-274155r1120453_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to lock the root account after three unsuccessful logon attempts with the command: $ grep even_deny_root /etc/security/faillock.conf even_deny_root If the "even_deny_root" option is not set, is missing or commented out, this is a finding.

## Group: SRG-OS-000329-GPOS-00128

**Group ID:** `V-274156`

### Rule: Amazon Linux 2023 must automatically lock an account until the locked account is released by an administrator when three unsuccessful logon attempts in 15 minutes occur.

**Rule ID:** `SV-274156r1120456_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system administrator demonstrates the use of an approved centralized account management method that locks an account after three unsuccessful logon attempts within a period of 15 minutes, this requirement is not applicable. Verify Amazon Linux 2023 locks an account after three unsuccessful logon attempts within a period of 15 minutes with the following command: $ grep fail_interval /etc/security/faillock.conf fail_interval = 900 If the "fail_interval" option is not set to "900" or less (but not "0"), the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000329-GPOS-00128

**Group ID:** `V-274157`

### Rule: Amazon Linux 2023 must maintain an account lock until the locked account is released by an administrator.

**Rule ID:** `SV-274157r1120459_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to lock an account until released by an administrator after three unsuccessful logon attempts with the command: $ grep 'unlock_time =' /etc/security/faillock.conf unlock_time = 0 If the "unlock_time" option is not set to "0", the line is missing, or commented out, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-274158`

### Rule: Amazon Linux 2023 must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the Ports, Protocols, and Services Management Category Assurance List (PPSM CAL) and vulnerability assessments.

**Rule ID:** `SV-274158r1120727_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Operating systems are capable of providing a variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, Amazon Linux 2023 must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues. Satisfies: SRG-OS-000096-GPOS-00050, SRG-OS-000297-GPOS-00115</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 firewall is configured to block unregistered ports, protocols, and services. Inspect the list of enabled firewall ports and verify they are configured correctly by running the following command: $ sudo firewall-cmd --list-all Ask the system administrator for the site or program PPSM Component Local Service Assessment (CLSA). Verify the services allowed by the firewall match the PPSM CLSA. If there are additional ports, protocols, or services that are not in the PPSM CLSA, or there are ports, protocols, or services that are prohibited by the PPSM CAL, or there are no firewall rules configured, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-274159`

### Rule: Amazon Linux 2023 must insure all interactive users have a primary group that exists.

**Rule ID:** `SV-274159r1120465_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user is assigned the group identifier (GID) of a group that does not exist on the system, and a group with the GID is subsequently created, the user may have unintended rights to any files associated with the group. Satisfies: SRG-OS-000104-GPOS-00051, SRG-OS-000121-GPOS-00062, SRG-OS-000042-GPOS-00020</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 interactive users have a valid GID with the following command: $ sudo pwck -qr If the system has any interactive users with duplicate GIDs, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-274160`

### Rule: Amazon Linux 2023 must ensure all interactive users have unique User IDs (UIDs).

**Rule ID:** `SV-274160r1120663_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, interactive users must be identified and authenticated to prevent potential misuse and compromise of the system. Satisfies: SRG-OS-000104-GPOS-00051, SRG-OS-000121-GPOS-00062, SRG-OS-000042-GPOS-00020</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 contains no duplicate UIDs for interactive users with the following command: $ sudo awk -F ":" 'list[$3]++{print $1, $3}' /etc/passwd If output is produced and the accounts listed are interactive user accounts, this is a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-274161`

### Rule: Amazon Linux 2023 must ensure the password complexity module is enabled in the password-auth file.

**Rule ID:** `SV-274161r1120471_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling PAM password complexity permits enforcement of strong passwords and consequently makes the system less prone to dictionary attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 uses "pwquality" to enforce the password complexity rules in the password-auth file with the following command: $ grep pam_pwquality /etc/pam.d/password-auth password required pam_pwquality.so If the command does not return a line containing the value "pam_pwquality.so", or the line is commented out, this is a finding. If the system administrator can demonstrate that the required configuration is contained in a PAM configuration file included or substacked from the system-auth file, this is not a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-274162`

### Rule: Amazon Linux 2023 password-auth must be configured to use a sufficient number of hashing rounds.

**Rule ID:** `SV-274162r1120474_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms, used for authentication to the cryptographic module are not verified and therefore, cannot be relied upon to provide confidentiality or integrity, and DOD data may be compromised. Operating systems utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2/140-3 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DOD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general purpose computing system. Satisfies: SRG-OS-000073-GPOS-00041, SRG-OS-000120-GPOS-00061</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 has the required number of rounds for the password hashing algorithm is configured in password-auth with the following command: $ sudo grep rounds /etc/pam.d/password-auth password sufficient pam_unix.so sha512 rounds=100000 If a matching line is not returned or "rounds" is less than "100000", this a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-274163`

### Rule: Amazon Linux 2023 system-auth must be configured to use a sufficient number of hashing rounds.

**Rule ID:** `SV-274163r1120477_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms used for authentication to the cryptographic module are not verified and therefore, cannot be relied upon to provide confidentiality or integrity, and DOD data may be compromised. Operating systems utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2/140-3 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DOD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general purpose computing system. Satisfies: SRG-OS-000073-GPOS-00041, SRG-OS-000120-GPOS-00061</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 has the required number of rounds for the password hashing algorithm is configured in system-auth with the following command: $ sudo grep rounds /etc/pam.d/system-auth password sufficient pam_unix.so sha512 rounds=100000 If a matching line is not returned or "rounds" is less than "100000", this a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-274164`

### Rule: Amazon Linux 2023 must ensure a sticky bit be set on all public directories.

**Rule ID:** `SV-274164r1120480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DOD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 world-writable directories have the sticky bit set. Determine if all world-writable directories have the sticky bit set by running the following command: $ sudo find / -type d -perm -0002 ! -perm -1000 -exec ls -ld {} + If any output is returned, these directories are world-writable and do not have the sticky bit set, and this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-274165`

### Rule: Amazon Linux 2023 must ensure all world-writable directories be owned by root, sys, bin, or an application user.

**Rule ID:** `SV-274165r1120483_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DOD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 world writable directories are owned by root, a system account, or an application account with the following command: $ sudo find / -xdev -type d -perm -0002 ! -user root ! -uid +999 -exec ls -ld {} + If there is output, this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-274166`

### Rule: Amazon Linux 2023 must terminate idle user sessions.

**Rule ID:** `SV-274166r1120486_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at Amazon Linux 2023 level, and de-allocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that Amazon Linux 2023 terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 logs out sessions that are idle for 15 minutes with the following command: $ sudo grep -i ^StopIdleSessionSec /etc/systemd/logind.conf StopIdleSessionSec=900 If "StopIdleSessionSec" is not configured to "900" seconds, is commented out, or is missing, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-274167`

### Rule: Amazon Linux 2023 must enable auditing of processes that start prior to the audit daemon.

**Rule ID:** `SV-274167r1120489_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. If auditing is enabled late in the startup process, the actions of some startup processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000473-GPOS-00218, SRG-OS-000254-GPOS-00095</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that GRUB 2 enables auditing of processes that start prior to the audit daemon with the following commands: Check that the current GRUB 2 configuration enables auditing: $ sudo grubby --info=ALL | grep args | grep -v 'audit=1' If any output is returned, this is a finding. Check that auditing is enabled by default to persist in kernel updates: $ grep audit /etc/default/grub GRUB_CMDLINE_LINUX="audit=1" If "audit" is not set to "1", is missing, or is commented out, this is a finding.

## Group: SRG-OS-000254-GPOS-00095

**Group ID:** `V-274168`

### Rule: Amazon Linux 2023 must allocate an audit_backlog_limit of sufficient size to capture processes that start prior to the audit daemon.

**Rule ID:** `SV-274168r1120492_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. If auditing is enabled late in the startup process, the actions of some startup processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created. Audit records can be generated from various components within the information system (e.g., module or policy filter). Allocating an audit_backlog_limit of sufficient size is critical in maintaining a stable boot process. With an insufficient limit allocated, the system is susceptible to boot failures and crashes. Satisfies: SRG-OS-000254-GPOS-00095, SRG-OS-000341-GPOS-00132</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 allocates a sufficient audit_backlog_limit to capture processes that start prior to the audit daemon with the following command: $ sudo grubby --info=ALL | grep args | grep -v 'audit_backlog_limit=8192' If the command returns any outputs, and audit_backlog_limit is less than "8192", this is a finding.

## Group: SRG-OS-000312-GPOS-00123

**Group ID:** `V-274169`

### Rule: Amazon Linux 2023 must enable discretionary access control on hardlinks.

**Rule ID:** `SV-274169r1120495_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By enabling the fs.protected_hardlinks kernel parameter, users can no longer create soft or hard links to files they do not own. Disallowing such hardlinks mitigates vulnerabilities based on insecure file system accessed by privileged programs, avoiding an exploitation vector exploiting unsafe use of open() or creat(). Satisfies: SRG-OS-000312-GPOS-00123, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to enable DAC on hardlinks. Check the status of the fs.protected_hardlinks kernel parameter with the following command: $ sudo sysctl fs.protected_hardlinks fs.protected_hardlinks = 1 If "fs.protected_hardlinks" is not set to "1" or is missing, this is a finding.

## Group: SRG-OS-000312-GPOS-00123

**Group ID:** `V-274170`

### Rule: Amazon Linux 2023 must enable kernel parameters to enforce discretionary access control on symlinks.

**Rule ID:** `SV-274170r1120498_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By enabling the fs.protected_symlinks kernel parameter, symbolic links are permitted to be followed only when outside a sticky world-writable directory, or when the user identifier (UID) of the link and follower match, or when the directory owner matches the symlink's owner. Disallowing such symlinks helps mitigate vulnerabilities based on insecure file system accessed by privileged programs, avoiding an exploitation vector exploiting unsafe use of open() or creat(). Satisfies: SRG-OS-000312-GPOS-00123, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to enable DAC on symlinks. Check the status of the fs.protected_symlinks kernel parameter with the following command: $ sudo sysctl fs.protected_symlinks fs.protected_symlinks = 1 If "fs.protected_symlinks " is not set to "1" or is missing, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-274173`

### Rule: Amazon Linux 2023 debug-shell systemd service must be disabled.

**Rule ID:** `SV-274173r1120507_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The debug-shell requires no authentication and provides root privileges to anyone who has physical access to the machine. While this feature is disabled by default, masking it adds an additional layer of assurance that it will not be enabled via a dependency in systemd. This also prevents attackers with physical access from trivially bypassing security on the machine through valid troubleshooting configurations and gaining root access when the system is rebooted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to mask the debug-shell systemd service with the following command: $ sudo systemctl status debug-shell.service O debug-shell.service Loaded: masked (Reason: Unit debug-shell.service is masked.) Active: inactive (dead) If the "debug-shell.service" is loaded and not masked, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-274174`

### Rule: Amazon Linux 2023 chrony must be configured with a maximum interval of 24 hours between requests sent to a USNO server or a time server designated for the appropriate DOD network.

**Rule ID:** `SV-274174r1120510_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 chrony service specifies a maximum interval of 24 hours between requests sent to a USNO server with the following command: Note: <USNO/DOD Server> is used in place of a time source IP address. $ sudo grep maxpoll /etc/chrony.conf server <USNO/DOD Server> iburst maxpoll 16 If the "maxpoll" option is not configured, commented out, or set to a number greater than 16 or the line is commented out then this is a finding. Verify Amazon Linux 2023 chrony service is configured to use authoritative USNO or appropriate DOD time source with the following command: $ sudo grep -i server /etc/chrony.conf server <USNO/DOD Server> If the parameter "server" is not set, or is not set to an authoritative USNO/DOD time source, then this is a finding.

## Group: SRG-OS-000356-GPOS-00144

**Group ID:** `V-274175`

### Rule: Amazon Linux 2023 must synchronize internal information system clocks to the authoritative time source at least every 24 hours.

**Rule ID:** `SV-274175r1120659_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Depending on the infrastructure being used the "pool" directive may not be supported. Satisfies: SRG-OS-000356-GPOS-00144, SRG-OS-000785-GPOS-00250, SRG-OS-000359-GPOS-00146</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is securely comparing internal information system clocks at least every 24 hours with an NTP server with the following commands: $ sudo grep maxpoll /etc/chrony.conf server 0.us.pool.ntp.mil iburst maxpoll 16 If the "maxpoll" option is set to a number greater than 16 or the line is commented out, this is a finding. Verify the "chrony.conf" file is configured to an authoritative DOD time source by running the following command: $ sudo grep -i server /etc/chrony.conf server 0.us.pool.ntp.mil If the parameter "server" is not set, or is not set to an authoritative DOD time source, this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-274176`

### Rule: Amazon Linux 2023 must routinely check the baseline configuration for unauthorized changes and notify the system administrator when anomalies in the operation of any security functions are discovered.

**Rule ID:** `SV-274176r1120655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to Amazon Linux 2023. Changes to operating system configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of Amazon Linux 2023. Amazon Linux 2023's information management officer (IMO)/information system security officer (ISSO) and system administrators (SAs) must be notified via email and/or monitoring system trap when there is an unauthorized modification of a configuration item. Notifications provided by information systems include messages to local computer consoles, and/or hardware indications, such as lights. This capability must take into account operational requirements for availability for selecting an appropriate response. The organization may choose to shut down or restart the information system upon security function anomaly detection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 routinely executes a file integrity scan for changes to the system baseline. The command used in the example will use a daily occurrence. Check the cron directories for scripts controlling the execution and notification of results of the file integrity application. For example, if AIDE is installed on the system, use the following commands: $ sudo ls -al /etc/cron.* | grep aide -rwxr-xr-x 1 root root 29 Nov 22 2015 aide $ grep aide /etc/crontab /var/spool/cron/root /etc/crontab: 30 04 * * * root usr/sbin/aide /var/spool/cron/root: 30 04 * * * root usr/sbin/aide $ sudo more /etc/cron.daily/aide #!/bin/bash /usr/sbin/aide --check | /bin/mail -s "$HOSTNAME - Daily aide integrity check run" root@sysname.mil If the file integrity application does not exist, or a script file controlling the execution of the file integrity application does not exist, or the file integrity application does not notify designated personnel of changes, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-274177`

### Rule: Amazon Linux 2023 must prevent the loading of a new kernel for later execution.

**Rule ID:** `SV-274177r1120519_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of Amazon Linux 2023. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. All software packages must be signed with a cryptographic key recognized and approved by the organization. Verifying the authenticity of software prior to installation validates the integrity of the software package received from a vendor. This verifies the software has not been tampered with and that it has been provided by a trusted vendor.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured to disable kernel image loading. Check the status of the kernel.kexec_load_disabled kernel parameter with the following command: $ sudo sysctl kernel.kexec_load_disabled kernel.kexec_load_disabled = 1 If "kernel.kexec_load_disabled" is not set to "1" or is missing, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-274178`

### Rule: Amazon Linux 2023 must prevent files with the setuid and setgid bit set from being executed on the /boot/efi directory.

**Rule ID:** `SV-274178r1120522_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system not to execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the /boot/efi directory is mounted with the "nosuid" option with the following command: $ mount | grep '\s/boot/efi\s' /dev/sda1 on /boot/efi type vfat (rw,nosuid,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=ascii,shortname=winnt,errors=remount-ro) If the /boot/efi file system does not have the "nosuid" option set, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-274179`

### Rule: Amazon Linux 2023 must mount /dev/shm with the nodev option.

**Rule ID:** `SV-274179r1120525_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that "/dev/shm" is mounted with the "nodev" option with the following command: $ mount | grep /dev/shm tmpfs on /dev/shm type tmpfs (rw,nodev,nosuid,noexec,seclabel) If the /dev/shm file system is mounted without the "nodev" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-274180`

### Rule: Amazon Linux 2023 must mount /dev/shm with the nosuid option.

**Rule ID:** `SV-274180r1120528_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that "/dev/shm" is mounted with the "nosuid" option with the following command: $ mount | grep /dev/shm tmpfs on /dev/shm type tmpfs (rw,nodev,nosuid,noexec,seclabel) If the /dev/shm file system is mounted without the "noexec" option, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-274181`

### Rule: Amazon Linux 2023 must ensure the pcscd service is active.

**Rule ID:** `SV-274181r1120531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The information system ensures that even if the information system is compromised, that compromise will not affect credentials stored on the authentication device. The daemon program for pcsc-lite and the MuscleCard framework is pcscd. It is a resource manager that coordinates communications with smart card readers and smart cards and cryptographic tokens connected to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the "pcscd" service is active with the following command: $ systemctl is-active pcscd active If the pcscdservice is not active, this is a finding.

## Group: SRG-OS-000378-GPOS-00163

**Group ID:** `V-274182`

### Rule: Amazon Linux 2023 file system automount function must be disabled unless required.

**Rule ID:** `SV-274182r1120729_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Peripherals include, but are not limited to, such devices as flash drives, external storage, and printers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 disables the file system automount function with the following command: $ sudo systemctl is-enabled autofs masked If the returned value is not "masked", "disabled", "Failed to get unit file state for autofs.service for autofs", or "enabled", and is not documented as operational requirement with the information system security officer (ISSO), this is a finding.

## Group: SRG-OS-000420-GPOS-00186

**Group ID:** `V-274183`

### Rule: Amazon Linux 2023 must protect against or limit the effects of denial-of-service (DoS) attacks by ensuring rate-limiting measures are configured on impacted network interfaces.

**Rule ID:** `SV-274183r1120714_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of Amazon Linux 2023 to mitigate the impact of DoS attacks that have occurred or are ongoing on system availability. For each system, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or establishing memory partitions). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is implementing rate-limiting measures on network interfaces to protect against DoS attacks. Access the AWS Management Console: Sign in to the AWS Management Console and navigate to the EC2 service. To locate the Application Load Balancer (ALB) in the EC2 dashboard, go to the "Load Balancers" section and find the ALB. Check the ALB configuration: Click on the ALB to view its details. The listener configuration for the ALB is located in the "Listener" tab. Look for the rate limiting settings: Scroll down to the "Rules" section. If rate limiting is enabled, a rule with the "Rate Limit" action will be displayed.

## Group: SRG-OS-000433-GPOS-00192

**Group ID:** `V-274184`

### Rule: Amazon Linux 2023 must implement nonexecutable data to protect its memory from unauthorized code execution.

**Rule ID:** `SV-274184r1120540_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The no-execute (NX) feature uses the segmentation feature on all x86 systems to prevent execution in memory higher than a certain address. It writes an address as a limit in the code segment descriptor, to control where code can be executed, on a per-process basis. When the kernel places a process's memory regions such as the stack and heap higher than this address, the hardware prevents execution in that address range. This is enabled by default on the latest Red Hat and Fedora systems if supported by the hardware.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 NX support is enabled with the following command: $ sudo dmesg | grep '[NX|DX]*protection' [ 0.000000] NX (Execute Disable) protection: active If "dmesg" does not show "NX (Execute Disable) protection" active, this is a finding.

## Group: SRG-OS-000437-GPOS-00194

**Group ID:** `V-274185`

### Rule: Amazon Linux 2023 must remove all software components after updated versions have been installed.

**Rule ID:** `SV-274185r1120543_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Previous versions of software components that are not removed from the information system after updates have been installed may be exploited by some adversaries.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 removes all software components after updated versions have been installed with the following command: $ grep clean /etc/dnf/dnf.conf clean_requirements_on_remove=1 If "clean_requirements_on_remove" is not set to "1", "True", or "yes", this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-274186`

### Rule: Amazon Linux 2023 must configure the use of the pam_faillock.so module in the /etc/pam.d/system-auth file.

**Rule ID:** `SV-274186r1120546_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the pam_faillock.so module is not loaded, the system will not correctly lockout accounts to prevent password guessing attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the pam_faillock.so module is present in the "/etc/pam.d/system-auth" file: $ grep pam_faillock.so /etc/pam.d/system-auth auth required pam_faillock.so preauth auth required pam_faillock.so authfail account required pam_faillock.so If the pam_faillock.so module is not present in the "/etc/pam.d/system-auth" file with the "preauth" line listed before pam_unix.so, this is a finding.

## Group: SRG-OS-000462-GPOS-00206

**Group ID:** `V-274187`

### Rule: Amazon Linux 2023 audit system must protect logon user identifiers (UIDs) from unauthorized change.

**Rule ID:** `SV-274187r1120715_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If modification of login UIDs is not prevented, they can be changed by nonprivileged users and make auditing complicated or impossible. Satisfies: SRG-OS-000462-GPOS-00206, SRG-OS-000475-GPOS-00220, SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Amazon Linux 2023 is configured so that the audit system prevents unauthorized changes to login UIDs with the following command: $ sudo grep -i immutable /etc/audit/audit.rules --loginuid-immutable If the "--loginuid-immutable" option is not returned in the "/etc/audit/audit.rules", or the line is commented out, this is a finding.

