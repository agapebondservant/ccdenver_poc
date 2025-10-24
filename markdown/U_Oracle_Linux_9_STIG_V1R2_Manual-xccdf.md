# STIG Benchmark: Oracle Linux 9 Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000780-GPOS-00240

**Group ID:** `V-271431`

### Rule: The OL 9 operating system must implement cryptographic mechanisms to prevent unauthorized modification of all information at rest.

**Rule ID:** `SV-271431r1092616_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Operating systems handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If there is a documented and approved reason for not having data at rest encryption, this requirement is Not Applicable. Verify that OL 9 prevents unauthorized disclosure or modification of all information requiring at rest protection by using disk encryption. Determine the partition layout for the system with the following command: $ sudo fdisk -l (..) Disk /dev/vda: 15 GiB, 16106127360 bytes, 31457280 sectors Units: sectors of 1 * 512 = 512 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disklabel type: gpt Disk identifier: 83298450-B4E3-4B19-A9E4-7DF147A5FEFB Device Start End Sectors Size Type /dev/vda1 2048 4095 2048 1M BIOS boot /dev/vda2 4096 2101247 2097152 1G Linux filesystem /dev/vda3 2101248 31455231 29353984 14G Linux filesystem (...) Verify that the system partitions are all encrypted with the following command: $ sudo more /etc/crypttab Every persistent disk partition present must have an entry in the file. If any partitions other than the boot partition or pseudo file systems (such as /proc or /sys) are not listed, this is a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-271432`

### Rule: OL 9 must use a separate file system for the system audit data path.

**Rule ID:** `SV-271432r1091008_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Placing "/var/log/audit" in its own partition enables better separation between audit files and other system files and helps ensure that auditing cannot be halted due to the partition running out of space.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 uses a separate file system for the system audit data path with the following command: Note: /var/log/audit is used as the example as it is a common location. $ mount | grep /var/log/audit UUID=2efb2979-45ac-82d7-0ae632d11f51 on /var/log/home type xfs (rw,realtime,seclabel,attr2,inode64) If no line is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271433`

### Rule: OL 9 must be configured so that a separate file system must be used for user home directories (such as /home or an equivalent).

**Rule ID:** `SV-271433r1091011_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensuring that "/home" is mounted on its own partition enables the setting of more restrictive mount options, and also helps ensure that users cannot trivially fill partitions used for log or audit data storage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 uses a separate file system for user home directories (such as /home or an equivalent) with the following command: $ mount | grep /home UUID=fba5000f-2ffa-4417-90eb-8c54ae74a32f on /home type ext4 (rw,nodev,nosuid,noexec,seclabel) If a separate entry for "/home" is not in use, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271434`

### Rule: OL 9 must use a separate file system for /tmp.

**Rule ID:** `SV-271434r1091014_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/tmp" partition is used as temporary storage by many programs. Placing "/tmp" in its own partition enables the setting of more restrictive mount options, which can help protect programs that use it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 uses a separate file system/partition for "/tmp" with the following command: $ mount | grep /tmp tmpfs /tmp tmpfs noatime,mode=1777 0 0 If a separate entry for "/tmp" is not in use, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271435`

### Rule: OL 9 must use a separate file system for /var.

**Rule ID:** `SV-271435r1091017_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Ensuring that "/var" is mounted on its own partition enables the setting of more restrictive mount options. This helps protect system services such as daemons or other programs which use it. It is not uncommon for the "/var" directory to contain world-writable directories installed by other software packages.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 uses a separate file system/partition for "/var" with the following command: $ mount | grep /var UUID=c274f65f-c5b5-4481-b007-bee96feb8b05 /var xfs noatime 1 2 If a separate entry for "/var" is not in use, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271436`

### Rule: OL 9 must use a separate file system for /var/log.

**Rule ID:** `SV-271436r1091020_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Placing "/var/log" in its own partition enables better separation between log files and other files in "/var/".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 uses a separate file system/partition for "/var/log" with the following command: $ mount | grep /var/log UUID=c274f65f-c5b5-4486-b021-bee96feb8b21 /var/log xfs noatime 1 2 If a separate entry for "/var/log" is not in use, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271437`

### Rule: OL 9 must use a separate file system for /var/tmp.

**Rule ID:** `SV-271437r1091023_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/var/tmp" partition is used as temporary storage by many programs. Placing "/var/tmp" in its own partition enables the setting of more restrictive mount options, which can help protect programs that use it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 uses a separate file system/partition for "/var/tmp" with the following command: $ mount | grep /var/tmp UUID=c274f65f-c5b5-4379-b017-bee96feb7a34 /var/log xfs noatime 1 2 If a separate entry for "/var/tmp" is not in use, this is a finding.

## Group: SRG-OS-000439-GPOS-00195

**Group ID:** `V-271438`

### Rule: OL 9 must be a vendor supported release.

**Rule ID:** `SV-271438r1091026_rule`
**Severity:** high

**Description:**
<VulnDiscussion>An operating system release is considered "supported" if the vendor continues to provide security patches for the product. With an unsupported release, it will not be possible to resolve security issues discovered in the system software. Oracle offers Oracle Linux Premier Support, for a fee, for those customers who wish to standardize on a specific minor release for an extended period.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is vendor supported with the following command: $ cat /etc/oracle-release Oracle Linux Server release 9.5 If the installed version of OL 9 is not supported, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271439`

### Rule: OL 9 vendor packaged system security patches and updates must be installed and up to date.

**Rule ID:** `SV-271439r1091029_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Installing software updates is a fundamental mitigation against the exploitation of publicly known vulnerabilities. If the most recent security patches and updates are not installed, unauthorized users may take advantage of weaknesses in the unpatched software. The lack of prompt attention to patching could result in a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 security patches and updates are installed and up to date. Updates are required to be applied with a frequency determined by organizational policy. Obtain the list of available package security updates from Oracle. The URL for updates is https://linux.oracle.com/errata/. It is important to note that updates provided by Oracle may not be present on the system if the underlying packages are not installed. Check that the available package security updates have been installed on the system with the following command: $ dnf history list | more ID | Command line | Date and time | Action(s) | Altered ------------------------------------------------------------------------------- 70 | install aide | 2023-03-05 10:58 | Install | 1 69 | update -y | 2023-03-04 14:34 | Update | 18 EE 68 | install vlc | 2023-02-21 17:12 | Install | 21 67 | update -y | 2023-02-21 17:04 | Update | 7 EE Typical update frequency may be overridden by Information Assurance Vulnerability Alert (IAVA) notifications from CYBERCOM. If the system is in noncompliance with the organizational patching policy, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271440`

### Rule: OL 9 must be configured so that the graphical display manager is not the default target unless approved.

**Rule ID:** `SV-271440r1092462_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unnecessary service packages must not be installed to decrease the attack surface of the system. Graphical display managers have a long history of security vulnerabilities and must not be used unless approved and documented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to boot to the command line: $ systemctl get-default multi-user.target If the system default target is not set to "multi-user.target" and the information system security officer (ISSO) lacks a documented requirement for a graphical user interface, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-271441`

### Rule: OL 9 must require authentication to access emergency mode.

**Rule ID:** `SV-271441r1091035_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. This requirement prevents attackers with physical access from trivially bypassing security on the machine and gaining root access. Such accesses are further prevented by configuring the bootloader password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 requires authentication for emergency mode with the following command: $ grep sulogin-shell /usr/lib/systemd/system/emergency.service ExecStart=-/usr/lib/systemd/systemd-sulogin-shell emergency If this line is not returned, or is commented out, this is a finding. If the output is different, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-271442`

### Rule: OL 9 must require authentication to access single-user mode.

**Rule ID:** `SV-271442r1091038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. This requirement prevents attackers with physical access from trivially bypassing security on the machine and gaining root access. Such accesses are further prevented by configuring the bootloader password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 requires authentication for single-user mode with the following command: $ grep sulogin /usr/lib/systemd/system/rescue.service ExecStart=-/usr/lib/systemd/systemd-sulogin-shell rescue If this line is not returned, or is commented out, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-271443`

### Rule: OL 9 must be configured to disable the Asynchronous Transfer Mode (ATM) kernel module.

**Rule ID:** `SV-271443r1092463_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Disabling ATM protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 disables the ability to load the ATM kernel module with the following command: $ grep -r atm /etc/modprobe.conf /etc/modprobe.d/* install atm /bin/false blacklist atm If the command does not return any output, or the line is commented out, and use of ATM is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-271444`

### Rule: OL 9 must be configured to disable the Controller Area Network (CAN) kernel module.

**Rule ID:** `SV-271444r1091044_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Disabling CAN protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 disables the ability to load the CAN kernel module with the following command: $ grep -r can /etc/modprobe.conf /etc/modprobe.d/* install can /bin/false blacklist can If the command does not return any output, or the line is commented out, and use of CAN is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-271445`

### Rule: OL 9 must be configured to disable the FireWire kernel module.

**Rule ID:** `SV-271445r1091047_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Disabling firewire protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 disables the ability to load the firewire-core kernel module with the following command: $ grep -r firewire-core /etc/modprobe.conf /etc/modprobe.d/* install firewire-core /bin/true blacklist firewire-core If the command does not return any output, or the line is commented out, and use of firewire-core is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-271446`

### Rule: OL 9 must disable the Stream Control Transmission Protocol (SCTP) kernel module.

**Rule ID:** `SV-271446r1091050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Failing to disconnect unused protocols can result in a system compromise. The SCTP is a transport layer protocol, designed to support the idea of message-oriented communication, with several streams of messages within one connection. Disabling SCTP protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 disables the ability to load the sctp kernel module with the following command: $ grep -r sctp /etc/modprobe.conf /etc/modprobe.d/* blacklist sctp If the command does not return any output, or the line is commented out, and use of sctp is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-271447`

### Rule: OL 9 must disable the Transparent Inter Process Communication (TIPC) kernel module.

**Rule ID:** `SV-271447r1092464_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Failing to disconnect unused protocols can result in a system compromise. The TIPC is a protocol that is specially designed for intra-cluster communication. It can be configured to transmit messages either on UDP or directly across Ethernet. Message delivery is sequence guaranteed, loss free, and flow controlled. Disabling TIPC protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 disables the ability to load the tipc kernel module with the following command: $ grep -r tipc /etc/modprobe.conf /etc/modprobe.d/* blacklist tipc If the command does not return any output, or the line is commented out, and use of TIPC is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-271448`

### Rule: OL 9 must disable mounting of cramfs.

**Rule ID:** `SV-271448r1091056_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Removing support for unneeded filesystem types reduces the local attack surface of the server. Compressed ROM/RAM file system (or cramfs) is a read-only file system designed for simplicity and space-efficiency. It is mainly used in embedded and small-footprint systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 disables the ability to load the cramfs kernel module with the following command: $ grep -ri cramfs /etc/modprobe.d/* | grep -i "/bin/false" install cramfs /bin/false If the command does not return any output, or the line is commented out, and use of the cramfs protocol is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding. Verify the operating system disables the ability to use the cramfs kernel module. Determine if the cramfs kernel module is disabled with the following command: $ grep -ri cramfs /etc/modprobe.d/* | grep -i "blacklist" blacklist cramfs If the command does not return any output or the output is not "blacklist cramfs", and use of the cramfs kernel module is not documented with the ISSO as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-271449`

### Rule: OL 9 Bluetooth must be disabled.

**Rule ID:** `SV-271449r1091059_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement applies to wireless peripheral technologies (e.g., wireless mice, keyboards, displays, etc.) used with OL 9 systems. Wireless peripherals (e.g., Wi-Fi/Bluetooth/IR keyboards, mice and pointing devices, and near field communications [NFC]) present a unique challenge by creating an open, unsecured port on a computer. Wireless peripherals must meet DOD requirements for wireless data transmission and be approved for use by the authorizing official (AO). Even though some wireless peripherals, such as mice and pointing devices, do not ordinarily carry information that need to be protected, modification of communications with these wireless peripherals may be used to compromise the OL 9 operating system. Satisfies: SRG-OS-000095-GPOS-00049, SRG-OS-000300-GPOS-00118</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 disables the ability to load the Bluetooth kernel module with the following command: $ grep -r bluetooth /etc/modprobe.conf /etc/modprobe.d/* install bluetooth /bin/false blacklist bluetooth If the command does not return any output, or the line is commented out, and use of Bluetooth is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000114-GPOS-00059

**Group ID:** `V-271450`

### Rule: OL 9 must be configured to disable USB mass storage.

**Rule ID:** `SV-271450r1092466_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>USB mass storage permits easy introduction of unknown devices, thereby facilitating malicious activity. Satisfies: SRG-OS-000114-GPOS-00059, SRG-OS-000378-GPOS-00163</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 disables the ability to load the USB Storage kernel module with the following command: $ grep -r usb-storage /etc/modprobe.conf /etc/modprobe.d/* install usb-storage /bin/false blacklist usb-storage If the command does not return any output, or the line is commented out, and use of USB Storage is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-271451`

### Rule: OL 9 must require a unique superuser's name upon booting into single-user and maintenance modes.

**Rule ID:** `SV-271451r1091065_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Having a nondefault grub superuser username makes password-guessing attacks less effective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 requires a unique username for the grub superuser account. Verify the boot loader superuser account has been set with the following command: $ sudo grep -A1 "superusers" /etc/grub2.cfg set superusers="<superusers-account>" export superusers password_pbkdf2 root ${GRUB2_PASSWORD} The <superusers-account> is the actual account name different from common names like root, admin, or administrator. If superusers contains easily guessable usernames, this is a finding.

## Group: SRG-OS-000445-GPOS-00199

**Group ID:** `V-271452`

### Rule: OL 9 must use a Linux Security Module configured to enforce limits on system services.

**Rule ID:** `SV-271452r1091068_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. This requirement applies to operating systems performing security function verification/testing and/or systems and environments that require this functionality. Satisfies: SRG-OS-000445-GPOS-00199, SRG-OS-000134-GPOS-00068</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 enforces the correct operation of security functions through the use of SELinux with the following command: $ getenforce Enforcing If SELINUX is not set to "Enforcing", this is a finding. Verify that SELinux is configured to be enforcing at boot. $ grep "SELINUX=" /etc/selinux/config # SELINUX= can take one of these three values: # NOTE: In earlier Fedora kernel builds, SELINUX=disabled would also SELINUX=enforcing If SELINUX line is missing, commented out, or not set to "enforcing", this is a finding.

## Group: SRG-OS-000445-GPOS-00199

**Group ID:** `V-271453`

### Rule: OL 9 must enable the SELinux targeted policy.

**Rule ID:** `SV-271453r1091071_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the SELinux policy to "targeted" or a more specialized policy ensures the system will confine processes that are likely to be targeted for exploitation, such as network or system services. Note: During the development or debugging of SELinux modules, it is common to temporarily place nonproduction systems in "permissive" mode. In such temporary cases, SELinux policies should be developed, and once work is completed, the system should be reconfigured to "targeted".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 enables the SELinux targeted policy with the following command: $ sestatus | grep policy Loaded policy name: targeted If the loaded policy name is not "targeted", this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-271454`

### Rule: OL 9 must enable FIPS mode.

**Rule ID:** `SV-271454r1092458_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. The operating system must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. This includes NIST FIPS-validated cryptography for the following: Provisioning digital signatures, generating cryptographic hashes, and to protect data requiring data-at-rest protections in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards. Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000125-GPOS-00065, SRG-OS-000396-GPOS-00176, SRG-OS-000423-GPOS-00187, SRG-OS-000478-GPOS-00223</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is in FIPS mode with the following command: $ fips-mode-setup --check FIPS mode is enabled. If FIPS mode is not enabled, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-271455`

### Rule: OL 9 must display the Standard Mandatory DOD Notice and Consent Banner before granting local or remote access to the system via a command line user logon.

**Rule ID:** `SV-271455r1091077_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist. Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the operating system via a command line user logon. Check that a banner is displayed at the command line login screen with the following command: $ cat /etc/issue If the banner is set correctly it will return the following text: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the banner text does not match the Standard Mandatory DOD Notice and Consent Banner exactly, or the line is commented out, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-271456`

### Rule: OL 9 must not have the nfs-utils package installed.

**Rule ID:** `SV-271456r1091080_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>"nfs-utils" provides a daemon for the kernel NFS server and related tools. This package also contains the "showmount" program. "showmount" queries the mount daemon on a remote host for information about the Network File System (NFS) server on the remote host. For example, "showmount" can display the clients that are mounted on that host.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 does not have the nfs-utils package installed with the following command: $ dnf list --installed nfs-utils Error: No matching Packages to list If the "nfs-utils" package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-271457`

### Rule: OL 9 must not have the rsh-server package installed.

**Rule ID:** `SV-271457r1091083_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "rsh-server" service provides unencrypted remote access service, which does not provide for the confidentiality and integrity of user passwords or the remote session and has very weak authentication. If a privileged user were to login using this service, the privileged user password could be compromised. The "rsh-server" package provides several obsolete and insecure network services. Removing it decreases the risk of accidental (or intentional) activation of those services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 does not have the rsh-server package installed with the following command: $ dnf list --installed rsh-server Error: No matching Packages to list If the "rsh-server" package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-271458`

### Rule: OL 9 must not have the telnet-server package installed.

**Rule ID:** `SV-271458r1091086_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities are often overlooked and therefore, may remain unsecure. They increase the risk to the platform by providing additional attack vectors. The telnet service provides an unencrypted remote access service, which does not provide for the confidentiality and integrity of user passwords or the remote session. If a privileged user were to login using this service, the privileged user password could be compromised. Removing the "telnet-server" package decreases the risk of accidental (or intentional) activation of the telnet service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 does not have the telnet-server package installed with the following command: $ dnf list --installed telnet-server Error: No matching Packages to list If the "telnet-server" package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-271459`

### Rule: OL 9 must not have the gssproxy package installed.

**Rule ID:** `SV-271459r1091089_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore, may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations (e.g., key missions, functions). The gssproxy package is a proxy for GSS API credential handling and could expose secrets on some networks. It is not needed for normal function of the OS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 does not have the gssproxy package installed with the following command: $ dnf list --installed gssproxy Error: No matching Packages to list If the "gssproxy" package is installed and is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-271460`

### Rule: OL 9 must not have the iprutils package installed.

**Rule ID:** `SV-271460r1091092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). The iprutils package provides a suite of utilities to manage and configure SCSI devices supported by the ipr SCSI storage device driver.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 does not have the iprutils package installed with the following command: $ dnf list --installed iprutils Error: No matching Packages to list If the "iprutils" package is installed and is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-271461`

### Rule: OL 9 must not have the tuned package installed.

**Rule ID:** `SV-271461r1091095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). The tuned package contains a daemon that tunes the system settings dynamically. It does so by monitoring the usage of several system components periodically. Based on that information, components will then be put into lower or higher power savings modes to adapt to the current usage. The tuned package is not needed for normal OS operations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 does not have the tuned package installed with the following command: $ dnf list --installed tuned Error: No matching Packages to list If the "tuned" package is installed and is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-271462`

### Rule: OL 9 must not have a File Transfer Protocol (FTP) server package installed.

**Rule ID:** `SV-271462r1091098_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The FTP service provides an unencrypted remote access that does not provide for the confidentiality and integrity of user passwords or the remote session. If a privileged user were to log on using this service, the privileged user password could be compromised. SSH or other encrypted file transfer methods must be used in place of this service. Removing the "vsftpd" package decreases the risk of accidental activation. Satisfies: SRG-OS-000074-GPOS-00042, SRG-OS-000095-GPOS-00049</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 does not have an FTP server package installed with the following command: $ dnf list --installed | grep ftp If the "ftp" package is installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271463`

### Rule: OL 9 must not have a Trivial File Transfer Protocol (TFTP) server package installed.

**Rule ID:** `SV-271463r1091101_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Removing the "tftp-server" package decreases the risk of the accidental (or intentional) activation of tftp services. If TFTP is required for operational support (such as transmission of router configurations), its use must be documented with the information systems security manager (ISSM), restricted to only authorized personnel, and have access control rules established.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 does not have a tftp server package installed with the following command: $ dnf list --installed | grep tftp If the "tftp" package is installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271464`

### Rule: OL 9 must not have the quagga package installed.

**Rule ID:** `SV-271464r1092459_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Quagga is a network routing software suite providing implementations of Open Shortest Path First (OSPF), Routing Information Protocol (RIP), Border Gateway Protocol (BGP) for Unix and Linux platforms. If there is no need to make the router software available, removing it provides a safeguard against its activation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 does not have the quagga package installed with the following command: $ dnf list --installed quagga Error: No matching Packages to list If the quagga package is installed and is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271465`

### Rule: OL 9 must not have a graphical display manager installed unless approved.

**Rule ID:** `SV-271465r1091107_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unnecessary service packages must not be installed to decrease the attack surface of the system. Graphical display managers have a long history of security vulnerabilities and must not be used, unless approved and documented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 does not have a graphical user interface installed with the following command: $ dnf list --installed "xorg*common" Error: No matching Packages to list If the "x11-server-common" package is installed, and the use of a graphical user interface has not been documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-271466`

### Rule: OL 9 must not have the sendmail package installed.

**Rule ID:** `SV-271466r1091110_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The sendmail software was not developed with security in mind, and its design prevents it from being effectively contained by SELinux. Postfix must be used instead.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 does not have the sendmail package installed with the following command: $ dnf list --installed sendmail Error: No matching Packages to list If the "sendmail" package is installed, this is a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-271467`

### Rule: OL 9 must have policycoreutils package installed.

**Rule ID:** `SV-271467r1091113_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. Policycoreutils contains the policy core utilities that are required for basic operation of an SELinux-enabled system. These utilities include load_policy to load SELinux policies, setfile to label filesystems, newrole to switch roles, and run_init to run /etc/init.d scripts in the proper context.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has the policycoreutils package installed with the following command: $ dnf list --installed policycoreutils Installed Packages policycoreutils.x86_64 3.6-2.1.el9 @anaconda If the "policycoreutils" package is not installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271468`

### Rule: OL 9 policycoreutils-python-utils package must be installed.

**Rule ID:** `SV-271468r1091116_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The policycoreutils-python-utils package is required to operate and manage an SELinux environment and its policies. It provides utilities such as semanage, audit2allow, audit2why, chcat, and sandbox.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 policycoreutils-python-utils service package is installed with the following command: $ dnf list --installed policycoreutils-python-utils Installed Packages policycoreutils-python-utils.noarch 3.6-2.1.el9 @AppStream If the "policycoreutils-python-utils" package is not installed, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-271469`

### Rule: OL 9 must have the firewalld package installed.

**Rule ID:** `SV-271469r1091119_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Firewalld provides an easy and effective way to block/limit remote access to the system via ports, services, and protocols. Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. OL 9 functionality (e.g., SSH) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets). Satisfies: SRG-OS-000096-GPOS-00050, SRG-OS-000297-GPOS-00115, SRG-OS-000298-GPOS-00116, SRG-OS-000480-GPOS-00232</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has the firewalld package installed with the following command: $ dnf list --installed firewalld Installed Packages firewalld.noarch 1.3.4-1.0.1.el9 @anaconda If the "firewall" package is not installed, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-271470`

### Rule: OL 9 must be configured so that the firewalld service is active.

**Rule ID:** `SV-271470r1092618_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Firewalld provides an easy and effective way to block/limit remote access to the system via ports, services, and protocols. Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. OL 9 functionality (e.g., RDP) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets). Satisfies: SRG-OS-000096-GPOS-00050, SRG-OS-000297-GPOS-00115</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 firewalld is active with the following command: $ systemctl is-active firewalld active If the firewalld service is not active, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-271471`

### Rule: OL 9 must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the Ports, Protocols, and Services Management (PPSM) Category Assignments List (CAL) and vulnerability assessments.

**Rule ID:** `SV-271471r1091125_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary ports, protocols, and services on information systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 9 is configured to prohibit or restrict the use of functions, ports, protocols, and/or services that are unnecessary or prohibited. Inspect the firewall configuration and running services to verify which services are currently active with the following command: $ sudo firewall-cmd --list-all-zones custom (active) target: DROP icmp-block-inversion: no interfaces: ens33 sources: services: dhcpv6-client dns http https ldaps rpc-bind ssh ports: masquerade: no forward-ports: icmp-blocks: rich rules: Ask the system administrator for the site or program PPSM Component Local Service Assessment (CLSA). Verify the services allowed by the firewall match the PPSM CLSA. If there are additional ports, protocols, or services that are not in the PPSM CLSA, or there are ports, protocols, or services that are prohibited by the PPSM CAL, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-271472`

### Rule: OL 9 must control remote access methods.

**Rule ID:** `SV-271472r1091128_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by one component. To support the requirements and principles of least functionality, the operating system must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business. Satisfies: SRG-OS-000096-GPOS-00050, SRG-OS-000297-GPOS-00115</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 controls remote access methods. Inspect the list of enabled firewall ports and verify they are configured correctly by running the following command: $ sudo firewall-cmd --list-all Ask the system administrator for the site or program Ports, Protocols, and Services Management Component Local Service Assessment (PPSM CLSA). Verify the services allowed by the firewall match the PPSM CLSA. If there are additional ports, protocols, or services that are not in the PPSM CLSA, or there are ports, protocols, or services that are prohibited by the PPSM Category Assurance List (CAL), or there are no firewall rules configured, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271473`

### Rule: OL 9 must be configured so that the firewall employs a deny-all, allow-by-exception policy for allowing connections to other systems.

**Rule ID:** `SV-271473r1091131_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to restrict network connectivity only to authorized systems permits inbound connections from malicious systems. It also permits outbound connections that may facilitate exfiltration of DOD data. OL 9 incorporates the "firewalld" daemon, which allows for many different configurations. One of these configurations is zones. Zones can be used to a deny-all, allow-by-exception approach. The default "drop" zone will drop all incoming network packets unless it is explicitly allowed by the configuration file or is related to an outgoing network connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to employ a deny-all, allow-by-exception policy for allowing connections to other systems with the following commands: $ sudo firewall-cmd --state running $ sudo firewall-cmd --get-active-zones public interfaces: ens33 $ sudo firewall-cmd --info-zone=public | grep target target: DROP $ sudo firewall-cmd --permanent --info-zone=public | grep target target: DROP If no zones are active on the OL 9 interfaces or if runtime and permanent targets are set to a different option other than "DROP", this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-271474`

### Rule: OL 9 must have the sudo package installed.

**Rule ID:** `SV-271474r1091134_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>sudo is a program designed to allow a system administrator to give limited root privileges to users and log root activity. The basic philosophy is to give as few privileges as possible but still allow system users to complete their work.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has the sudo package installed with the following command: $ dnf list --installed sudo Installed Packages sudo.x86_64 1.9.5p2-10.el9_3 @anaconda If the sudo package is not installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271475`

### Rule: OL 9 must use the invoking user's password for privilege escalation when using sudo.

**Rule ID:** `SV-271475r1091137_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the rootpw, targetpw, or runaspw flags are defined and not disabled, by default the operating system will prompt the invoking user for the "root" user password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to enforce the sudoers security policy to use the invoking user's password for privilege escalation with the following command: $ sudo egrep -i '(!rootpw|!targetpw|!runaspw)' /etc/sudoers /etc/sudoers.d/* | grep -v '#' /etc/sudoers:Defaults !targetpw /etc/sudoers:Defaults !rootpw /etc/sudoers:Defaults !runaspw If no results are returned, this is a finding. If results are returned from more than one file location, this is a finding. If "Defaults !targetpw" is not defined, this is a finding. If "Defaults !rootpw" is not defined, this is a finding. If "Defaults !runaspw" is not defined, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271476`

### Rule: OL 9 must restrict privilege elevation to authorized personnel.

**Rule ID:** `SV-271476r1091140_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the sudoers file is not configured correctly, any user defined on the system can initiate privileged actions on the target system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 restricts privilege elevation to authorized personnel with the following command: $ sudo sh -c 'grep -iw ALL /etc/sudoers /etc/sudoers.d/*' If the either of the following entries are returned, this is a finding: ALL ALL=(ALL) ALL ALL ALL=(ALL:ALL) ALL

## Group: SRG-OS-000396-GPOS-00176

**Group ID:** `V-271477`

### Rule: OL 9 must have the crypto-policies package installed.

**Rule ID:** `SV-271477r1091143_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Centralized cryptographic policies simplify applying secure ciphers across an operating system and the applications that run on that operating system. Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. Satisfies: SRG-OS-000396-GPOS-00176, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 crypto-policies package is installed with the following command: $ dnf list --installed crypto-policies Installed Packages crypto-policies.noarch 20240202-1.git283706d.el9 @ol9_baseos_latest If the crypto-policies package is not installed, this is a finding.

## Group: SRG-OS-000396-GPOS-00176

**Group ID:** `V-271478`

### Rule: OL 9 must implement a FIPS 140-3 compliant system-wide cryptographic policy.

**Rule ID:** `SV-271478r1092620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Centralized cryptographic policies simplify applying secure ciphers across an operating system and the applications that run on that operating system. Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. Satisfies: SRG-OS-000396-GPOS-00176, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is set to use a modified FIPS compliant systemwide crypto-policy. $ update-crypto-policies --show FIPS If the system wide crypto policy is not set to "FIPS", this is a finding. Note: If subpolicies have been configured, they will be listed in a colon-separated list starting with FIPS as follows: FIPS:<SUBPOLICY-NAME>:<SUBPOLICY-NAME>. Verify the current minimum crypto-policy configuration with the following commands: $ grep -E 'rsa_size|hash' /etc/crypto-policies/state/CURRENT.pol hash = SHA2-256 SHA2-384 SHA2-512 SHA2-224 SHA3-256 SHA3-384 SHA3-512 SHAKE-256 min_rsa_size = 2048 If the "hash" values do not include at least the following FIPS 140-3 compliant algorithms "SHA2-256 SHA2-384 SHA2-512 SHA2-224 SHA3-256 SHA3-384 SHA3-512 SHAKE-256", this is a finding. If there are algorithms that include "SHA1" or a hash value less than "256" this is a finding. If the "min_rsa_size" is not set to a value of at least 2048, this is a finding. If these commands do not return any output, this is a finding.

## Group: SRG-OS-000396-GPOS-00176

**Group ID:** `V-271479`

### Rule: OL 9 must not allow the cryptographic policy to be overridden.

**Rule ID:** `SV-271479r1092621_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Centralized cryptographic policies simplify applying secure ciphers across an operating system and the applications that run on that operating system. Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. Satisfies: SRG-OS-000396-GPOS-00176, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 cryptographic policies are not overridden. Verify that the configured policy matches the generated policy with the following command: $ sudo update-crypto-policies --check && echo PASS The configured policy matches the generated policy PASS If the last line is not "PASS", this is a finding. List all of the crypto backends configured on the system with the following command: $ ls -l /etc/crypto-policies/back-ends/ lrwxrwxrwx. 1 root root 40 Nov 13 16:29 bind.config -> /usr/share/crypto-policies/FIPS/bind.txt lrwxrwxrwx. 1 root root 42 Nov 13 16:29 gnutls.config -> /usr/share/crypto-policies/FIPS/gnutls.txt lrwxrwxrwx. 1 root root 40 Nov 13 16:29 java.config -> /usr/share/crypto-policies/FIPS/java.txt lrwxrwxrwx. 1 root root 46 Nov 13 16:29 javasystem.config -> /usr/share/crypto-policies/FIPS/javasystem.txt lrwxrwxrwx. 1 root root 40 Nov 13 16:29 krb5.config -> /usr/share/crypto-policies/FIPS/krb5.txt lrwxrwxrwx. 1 root root 45 Nov 13 16:29 libreswan.config -> /usr/share/crypto-policies/FIPS/libreswan.txt lrwxrwxrwx. 1 root root 42 Nov 13 16:29 libssh.config -> /usr/share/crypto-policies/FIPS/libssh.txt -rw-r--r--. 1 root root 398 Nov 13 16:29 nss.config lrwxrwxrwx. 1 root root 43 Nov 13 16:29 openssh.config -> /usr/share/crypto-policies/FIPS/openssh.txt lrwxrwxrwx. 1 root root 49 Nov 13 16:29 opensshserver.config -> /usr/share/crypto-policies/FIPS/opensshserver.txt lrwxrwxrwx. 1 root root 46 Nov 13 16:29 opensslcnf.config -> /usr/share/crypto-policies/FIPS/opensslcnf.txt lrwxrwxrwx. 1 root root 43 Nov 13 16:29 openssl.config -> /usr/share/crypto-policies/FIPS/openssl.txt lrwxrwxrwx. 1 root root 48 Nov 13 16:29 openssl_fips.config -> /usr/share/crypto-policies/FIPS/openssl_fips.txt If the paths do not point to the respective files under /usr/share/crypto-policies/FIPS path, this is a finding. Note: nss.config should not be hyperlinked.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271480`

### Rule: OL 9 must be configured so that the cryptographic hashes of system files match vendor values.

**Rule ID:** `SV-271480r1091152_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The hashes of important files like system executables should match the information given by the RPM database. Executables with erroneous hashes could be a sign of nefarious activity on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured so that the cryptographic hashes of system files match vendor values. List files on the system that have file hashes different from what is expected by the RPM database with the following command: $ sudo rpm -Va --noconfig | awk '$1 ~ /..5/ && $2 != "c"' If there is output, this is a finding.

## Group: SRG-OS-000478-GPOS-00223

**Group ID:** `V-271481`

### Rule: OL 9 cryptographic policy files must match files shipped with the operating system.

**Rule ID:** `SV-271481r1091155_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The OL 9 package crypto-policies defines the cryptography policies for the system. If the files are changed from those shipped with the operating system, it may be possible for OL 9 to use cryptographic functions that are not FIPS 140-3 approved. Satisfies: SRG-OS-000478-GPOS-00223, SRG-OS-000396-GPOS-00176</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 crypto-policies package has not been modified with the following command: $ rpm -V crypto-policies If the command has any output, this is a finding.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-271482`

### Rule: OL 9 networked systems must have SSH installed.

**Rule ID:** `SV-271482r1091158_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has the openssh-server package installed with the following command: $ dnf list --installed openssh-server Installed Packages openssh-server.x86_64 8.7p1-38.0.2.el9_4.4 @ol9_baseos_latest If the "openssh-server" package is not installed, this is a finding.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-271483`

### Rule: OL 9 networked systems must have and implement SSH to protect the confidentiality and integrity of transmitted and received information, as well as information during preparation for transmission.

**Rule ID:** `SV-271483r1091161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 networked systems implement SSH to protect the confidentiality and integrity of transmitted and received information, as well as information during preparation for transmission. Verify that "sshd" is active with the following command: $ systemctl is-active sshd active If the "sshd" service is not active, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-271484`

### Rule: The OL 9 SSH daemon must be configured to use systemwide cryptographic policies.

**Rule ID:** `SV-271484r1092624_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. OL 9 incorporates systemwide crypto policies by default. The SSH configuration file has no effect on the ciphers, MACs, or algorithms unless specifically defined in the /etc/sysconfig/sshd file. The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/ directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to implement systemwide cryptographic policies when the SSH daemon is invoked. Verify that systemwide cryptographic policies are in effect with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*include' /etc/ssh/sshd_config:Include /etc/ssh/sshd_config.d/*.conf /etc/ssh/sshd_config.d/50-redhat.conf:Include /etc/crypto-policies/back-ends/opensshserver.config If "Include /etc/ssh/sshd_config.d/*.conf" or "Include /etc/crypto-policies/back-ends/opensshserver.config" are not included in the system sshd config this is a finding. Additionally, if the file /etc/ssh/sshd_config.d/50-redhat.conf is missing, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-271485`

### Rule: OL 9 SSH server must be configured to use only ciphers employing FIPS 140-3 validated cryptographic hash algorithms to protect the confidentiality of SSH server connections.

**Rule ID:** `SV-271485r1092625_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. OL 9 incorporates systemwide crypto policies by default. The SSH configuration file has no effect on the ciphers, MACs, or algorithms unless specifically defined in the /etc/sysconfig/sshd file. The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/opensshserver.config file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 SSH server is configured to use only ciphers employing FIPS 140-3 approved algorithms. To verify the ciphers in the systemwide SSH configuration file, use the following command: $ sudo grep -i Ciphers /etc/crypto-policies/back-ends/opensshserver.config Ciphers aes256-gcm@openssh.com,aes256-ctr,aes128-gcm@openssh.com,aes128-ctr If the cipher entries in the "opensshserver.config" file have any ciphers other than "aes256-gcm@openssh.com,aes256-ctr,aes128-gcm@openssh.com,aes128-ctr", or they are missing or commented out, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-271486`

### Rule: OL 9 SSH server must be configured to use only Message Authentication Codes (MACs) employing FIPS 140-3 validated cryptographic hash algorithms to protect the confidentiality of SSH server connections.

**Rule ID:** `SV-271486r1092626_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. OL 9 incorporates systemwide crypto policies by default. The SSH configuration file has no effect on the ciphers, MACs, or algorithms unless specifically defined in the /etc/sysconfig/sshd file. The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/opensshserver.config file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 SSH server is configured to use only MACs employing FIPS 140-3 approved algorithms. To verify the MACs in the systemwide SSH configuration file, use the following command: $ sudo grep -i MACs /etc/crypto-policies/back-ends/opensshserver.config MACs hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha2-256,hmac-sha2-512 If the MACs entries in the "opensshserver.config" file have any hashes other than "hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha2-256,hmac-sha2-512", or they are missing or commented out, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-271487`

### Rule: OL 9 must display the Standard Mandatory DOD Notice and Consent Banner before granting local or remote access to the system via a SSH logon.

**Rule ID:** `SV-271487r1091173_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The warning message reinforces policy awareness during the logon process and facilitates possible legal action against attackers. Alternatively, systems whose ownership should not be obvious should ensure usage of a banner that does not provide easy attribution. Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the system via SSH connections. Check for the location of the banner file currently being used with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*banner' banner /etc/issue If the line is commented out or if the file is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271488`

### Rule: OL 9 must have the openssh-clients package installed.

**Rule ID:** `SV-271488r1091176_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This package includes utilities to make encrypted connections and transfer files securely to SSH servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has the openssh-clients package installed with the following command: $ dnf list --installed openssh-clients Installed Packages openssh-clients.x86_64 8.7p1-38.0.2.el9_4.4 @ol9_baseos_latest If the openssh-clients package is not installed, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-271489`

### Rule: OL 9 SSH client must be configured to use only DOD-approved encryption ciphers employing FIPS 140-3 validated cryptographic hash algorithms to protect the confidentiality of SSH client connections.

**Rule ID:** `SV-271489r1092627_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. OL 9 incorporates systemwide crypto policies by default. The SSH configuration file has no effect on the ciphers, MACs, or algorithms unless specifically defined in the /etc/sysconfig/sshd file. The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/opensshserver.config file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured so that the SSH client uses only ciphers employing FIPS 140-3 approved algorithms. To verify the ciphers in the systemwide SSH configuration file, use the following command: $ grep -i Ciphers /etc/crypto-policies/back-ends/openssh.config Ciphers aes256-gcm@openssh.com,aes256-ctr,aes128-gcm@openssh.com,aes128-ctr If the cipher entries in the "openssh.config" file have any ciphers other than "aes256-gcm@openssh.com,aes256-ctr,aes128-gcm@openssh.com,aes128-ctr", or they are missing or commented out, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-271490`

### Rule: OL 9 SSH client must be configured to use only DOD-approved Message Authentication Codes (MACs) employing FIPS 140-3 validated cryptographic hash algorithms to protect the confidentiality of SSH client connections.

**Rule ID:** `SV-271490r1092628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. OL 9 incorporates systemwide crypto policies by default. The SSH configuration file has no effect on the ciphers, MACs, or algorithms unless specifically defined in the /etc/sysconfig/sshd file. The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/opensshserver.config file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured so that the SSH client uses only MACs employing FIPS 140-3 approved algorithms. To verify the MACs in the systemwide SSH configuration file, use the following command: $ grep -i MACs /etc/crypto-policies/back-ends/openssh.config MACs hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha2-256,hmac-sha2-512 If the MACs entries in the "openssh.config" file have any hashes other than "hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha2-256,hmac-sha2-512", or they are missing or commented out, this is a finding.

## Group: SRG-OS-000105-GPOS-00052

**Group ID:** `V-271491`

### Rule: OL 9 must have the openssl-pkcs11 package installed.

**Rule ID:** `SV-271491r1091185_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. A privileged account is defined as an information system account with authorizations of a privileged user. The DOD CAC with DOD-approved PKI is an example of multifactor authentication. Satisfies: SRG-OS-000105-GPOS-00052, SRG-OS-000375-GPOS-00160, SRG-OS-000376-GPOS-00161, SRG-OS-000377-GPOS-00162</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has the openssl-pkcs11 package installed with the following command: $ dnf list --installed openssl-pkcs11 Installed Packages openssl-pkcs11.x86_64 0.4.11-9.el9 @ol9_baseos_latest If the "openssl-pkcs11" package is not installed, this is a finding.

## Group: SRG-OS-000705-GPOS-00150

**Group ID:** `V-271492`

### Rule: OL 9 must implement multifactor authentication for remote access to privileged accounts in such a way that one of the factors is provided by a device separate from the system gaining access.

**Rule ID:** `SV-271492r1091188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a CAC or token that is separate from the information system, ensures that even if the information system is compromised, that compromise will not affect credentials stored on the authentication device. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification card and the DOD Common Access Card. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., VPN, proxy capability). This does not apply to authentication for the purpose of configuring the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has the packages required for multifactor authentication installed with the following command: $ dnf list --installed libpam-pkcs11 ii libpam-pkcs11 0.6.12-2build3 amd64 Fully featured PAM module for using PKCS#11 smart cards If the "libpam-pkcs11" package is not installed, this is a finding.

## Group: SRG-OS-000705-GPOS-00150

**Group ID:** `V-271493`

### Rule: OL 9 must have the SSSD package installed.

**Rule ID:** `SV-271493r1091191_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a CAC or token that is separate from the information system, ensures that even if the information system is compromised, that compromise will not affect credentials stored on the authentication device. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification card and the DOD Common Access Card. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., VPN, proxy capability). This does not apply to authentication for the purpose of configuring the device itself (management). Satisfies: SRG-OS-000705-GPOS-00150, SRG-OS-000105-GPOS-00052, SRG-OS-000106-GPOS-00053, SRG-OS-000107-GPOS-00054, SRG-OS-000108-GPOS-00055, SRG-OS-000375-GPOS-00160</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has the SSSD package installed with the following command: $ dnf list --installed sssd Installed Packages sssd.x86_64 2.9.5-4.0.1.el9_5.1 @ol9_baseos_latest If the SSSD package is not installed, this is a finding.

## Group: SRG-OS-000705-GPOS-00150

**Group ID:** `V-271494`

### Rule: OL 9 must use the SSSD package for multifactor authentication services.

**Rule ID:** `SV-271494r1091194_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a CAC or token that is separate from the information system, ensures that even if the information system is compromised, that compromise will not affect credentials stored on the authentication device. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification card and the DOD Common Access Card. A privileged account is defined as an information system account with authorizations of a privileged user. Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: 1) Something a user knows (e.g., password/PIN); 2) Something a user has (e.g., cryptographic identification device, token); and 3) Something a user is (e.g., biometric). A privileged account is defined as an information system account with authorizations of a privileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the internet). The DOD common access card (CAC) with DOD-approved PKI is an example of multifactor authentication. Satisfies: SRG-OS-000705-GPOS-00150, SRG-OS-000105-GPOS-00052, SRG-OS-000106-GPOS-00053, SRG-OS-000107-GPOS-00054, SRG-OS-000108-GPOS-00055, SRG-OS-000375-GPOS-00161</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured so that the sssd.service is enabled and active with the following commands: $ sudo systemctl is-enabled sssd enabled $ sudo systemctl is-active sssd active If sssd.service is not active or enabled, this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-271495`

### Rule: OL 9 must have the s-nail package installed.

**Rule ID:** `SV-271495r1091197_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The s-nail package provides the mail command required to allow sending email notifications of unauthorized configuration changes to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has the s-nail package installed on the system with the following command: $ dnf list --installed s-nail Installed Packages s-nail.x86_64 14.9.22-6.el9 @ol9_appstream If the s-nail package is not installed, this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-271496`

### Rule: OL 9 must have the Advanced Intrusion Detection Environment (AIDE) package installed.

**Rule ID:** `SV-271496r1091200_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly, and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. Satisfies: SRG-OS-000363-GPOS-00150, SRG-OS-000445-GPOS-00199</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has the package installed with the following command: $ dnf list --installed aide Installed Packages aide.x86_64 0.16-100.el9 @ol9_appstream If AIDE is not installed, ask the system administrator (SA) how file integrity checks are performed on the system. If there is no application installed to perform integrity checks, this is a finding. If AIDE is installed, check if it has been initialized with the following command: $ sudo /usr/sbin/aide --check If the output is "Couldn't open file /var/lib/aide/aide.db.gz for reading", this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-271497`

### Rule: OL 9 must routinely check the baseline configuration for unauthorized changes and notify the system administrator (SA) when anomalies in the operation of any security functions are discovered.

**Rule ID:** `SV-271497r1092471_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to the operating system. Changes to operating system configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of the operating system. The operating system's information management officer (IMO)/information system security officer (ISSO) and SAs must be notified via email and/or monitoring system trap when there is an unauthorized modification of a configuration item. Notifications provided by information systems include messages to local computer consoles, and/or hardware indications, such as lights. This capability must take into account operational requirements for availability for selecting an appropriate response. The organization may choose to shut down or restart the information system upon security function anomaly detection. Satisfies: SRG-OS-000363-GPOS-00150, SRG-OS-000446-GPOS-00200, SRG-OS-000447-GPOS-00201</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 routinely executes a file integrity scan for changes to the system baseline. The command used in the example will use a daily occurrence. Check the cron directories for scripts controlling the execution and notification of results of the file integrity application. For example, if Advanced Intrusion Detection Environment (AIDE) is installed on the system, use the following commands: $ ls -al /etc/cron.* | grep aide -rwxr-xr-x 1 root root 29 Nov 22 2015 aide $ sudo grep aide /etc/crontab /var/spool/cron/root /etc/crontab: 30 04 * * * root usr/sbin/aide /var/spool/cron/root: 30 04 * * * root usr/sbin/aide $ more /etc/cron.daily/aide #!/bin/bash /usr/sbin/aide --check | /bin/mail -s "$HOSTNAME - Daily aide integrity check run" root@sysname.mil If the file integrity application does not exist, or a script file controlling the execution of the file integrity application does not exist, or the file integrity application does not notify designated personnel of changes, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271498`

### Rule: OL 9 must use a file integrity tool that is configured to use FIPS 140-3-approved cryptographic hashes for validating file contents and directories.

**Rule ID:** `SV-271498r1091206_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OL 9 installation media ships with an optional file integrity tool called Advanced Intrusion Detection Environment (AIDE). AIDE is highly configurable at install time. This requirement assumes the "aide.conf" file is under the "/etc" directory. File integrity tools use cryptographic hashes for verifying file contents and directories have not been altered. These hashes must be FIPS 140-3-approved cryptographic hashes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 uses a file integrity tool that is configured to use FIPS 140-3-approved cryptographic hashes for validating file contents and directories. Verify that AIDE is configured to use FIPS 140-3 file hashing with the following command: $ sudo grep sha512 /etc/aide.conf All=p+i+n+u+g+s+m+S+sha512+acl+xattrs+selinux If the "sha512" rule is not being used on all uncommented selection lines in the "/etc/aide.conf" file, or another file integrity tool is not using FIPS 140-3-approved cryptographic hashes for validating file contents and directories, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271499`

### Rule: OL 9 must be configured so that the file integrity tool verifies Access Control Lists (ACLs).

**Rule ID:** `SV-271499r1091209_rule`
**Severity:** low

**Description:**
<VulnDiscussion>OL 9 installation media ships with an optional file integrity tool called Advanced Intrusion Detection Environment (AIDE). AIDE is highly configurable at install time. This requirement assumes the "aide.conf" file is under the "/etc" directory. ACLs can provide permissions beyond those permitted through the file mode and must be verified by the file integrity tools.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured so that AIDE is verifying ACLs with the following command: $ sudo grep acl /etc/aide.conf All= p+i+n+u+g+s+m+S+sha512+acl+xattrs+selinux If the "acl" rule is not being used on all uncommented selection lines in the "/etc/aide.conf" file, or ACLs are not being checked by another file integrity tool, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271500`

### Rule: OL 9 must be configured so that the file integrity tool verifies extended attributes.

**Rule ID:** `SV-271500r1091212_rule`
**Severity:** low

**Description:**
<VulnDiscussion>OL 9 installation media ships with an optional file integrity tool called Advanced Intrusion Detection Environment (AIDE). AIDE is highly configurable at install time. This requirement assumes the "aide.conf" file is under the "/etc" directory. Extended attributes in file systems are used to contain arbitrary data and file metadata with security implications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured so that AIDE is configured to verify extended attributes with the following command: $ sudo grep xattrs /etc/aide.conf All= p+i+n+u+g+s+m+S+sha512+acl+xattrs+selinux If the "xattrs" rule is not being used on all uncommented selection lines in the "/etc/aide.conf" file, or extended attributes are not being checked by another file integrity tool, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-271501`

### Rule: OL 9 must have the chrony package installed.

**Rule ID:** `SV-271501r1091215_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has the chrony package installed with the following command: $ dnf list --installed chrony Installed Packages chrony.x86_64 4.5-1.0.2.el9 @ol9_baseos_latest If the chrony package is not installed, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-271502`

### Rule: OL 9 must enable the chronyd service.

**Rule ID:** `SV-271502r1091218_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 chronyd service is set to active with the following command: $ systemctl is-active chronyd active If the chronyd service is not active, this is a finding.

## Group: SRG-OS-000378-GPOS-00163

**Group ID:** `V-271503`

### Rule: OL 9 must have the USBGuard package installed.

**Rule ID:** `SV-271503r1091221_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The USBguard-daemon is the main component of the USBGuard software framework. It runs as a service in the background and enforces the USB device authorization policy for all USB devices. The policy is defined by a set of rules using a rule language described in the usbguard-rules.conf file. The policy and the authorization state of USB devices can be modified during runtime using the usbguard tool. The system administrator (SA) must work with the site information system security officer (ISSO) to determine a list of authorized peripherals and establish rules within the USBGuard software framework to allow only authorized devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has USBGuard installed on the operating system with the following command: $ dnf list --installed usbguard Installed Packages usbguard.x86_64 1.0.0-15.el9 @ol9_appstream If the USBGuard package is not installed, ask the SA to indicate how unauthorized peripherals are being blocked. If there is no evidence that unauthorized peripherals are being blocked before establishing a connection, this is a finding.

## Group: SRG-OS-000378-GPOS-00163

**Group ID:** `V-271504`

### Rule: OL 9 must enable the USBGuard package.

**Rule ID:** `SV-271504r1091224_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The USBguard-daemon is the main component of the USBGuard software framework. It runs as a service in the background and enforces the USB device authorization policy for all USB devices. The policy is defined by a set of rules using a rule language described in the usbguard-rules.conf file. The policy and the authorization state of USB devices can be modified during runtime using the usbguard tool. The system administrator (SA) must work with the site information system security officer (ISSO) to determine a list of authorized peripherals and establish rules within the USBGuard software framework to allow only authorized devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 USBGuard is enabled with the following command: $ systemctl is-active usbguard active If usbguard is not active, ask the SA to indicate how unauthorized peripherals are being blocked. If there is no evidence that unauthorized peripherals are being blocked before establishing a connection, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-271505`

### Rule: OL 9 must have the subscription-manager package installed.

**Rule ID:** `SV-271505r1092629_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Oracle Linux Manager, based on the Spacewalk open source software, helps automate Oracle Linux systems management. This enables users to control the system software life cycle from initial installation through maintenance, software configuration, upgrades, and eventual decommissioning. Oracle Linux Manager also helps automate a kickstart installation, system configuration, and maintenance tasks, which enables rapid deployment of proven and consistent software configurations for Oracle Linux systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 oracle-linux-manager package is installed with the following command: $ dnf list installed oracle-linux-manager-client-release-el9 Installed Packages oracle-linux-manager-client-release-el9.noarch 1.0-2.el9 @ol9_baseos_latest If the "oracle-linux-manager" package is not installed, this is a finding.

## Group: SRG-OS-000370-GPOS-00155

**Group ID:** `V-271506`

### Rule: OL 9 must have the fapolicy module installed.

**Rule ID:** `SV-271506r1091230_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as allowlisting. Using an allowlist provides a configuration management method for allowing the execution of only authorized software. Using only authorized software decreases risk by limiting the number of potential vulnerabilities. Verification of allowlisted software occurs prior to execution or at system startup. User home directories/folders may contain information of a sensitive nature. Nonprivileged users should coordinate any sharing of information with a system administrator (SA) through shared resources. OL 9 ships with many optional packages. One such package is a file access policy daemon called "fapolicyd". "fapolicyd" is a userspace daemon that determines access rights to files based on attributes of the process and file. It can be used to either blocklist or allowlist processes or file access. Proceed with caution with enforcing the use of this daemon. Improper configuration may render the system nonfunctional. The "fapolicyd" API is not namespace aware and can cause issues when launching or running containers. Satisfies: SRG-OS-000370-GPOS-00155, SRG-OS-000368-GPOS-00154</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 fapolicyd package is installed with the following command: $ dnf list --installed fapolicyd Installed Packages fapolicyd.x86_64 1.3.2-100.0.1.el9 @ol9_appstream If the fapolicyd package is not installed, this is a finding.

## Group: SRG-OS-000370-GPOS-00155

**Group ID:** `V-271507`

### Rule: OL 9 must enable the fapolicy module.

**Rule ID:** `SV-271507r1091233_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as allowlisting. Using an allowlist provides a configuration management method for allowing the execution of only authorized software. Using only authorized software decreases risk by limiting the number of potential vulnerabilities. Verification of allowlisted software occurs prior to execution or at system startup. User home directories/folders may contain information of a sensitive nature. Nonprivileged users should coordinate any sharing of information with a system administrator (SA) through shared resources. OL 9 ships with many optional packages. One such package is a file access policy daemon called "fapolicyd". "fapolicyd" is a userspace daemon that determines access rights to files based on attributes of the process and file. It can be used to either blocklist or allowlist processes or file access. Proceed with caution with enforcing the use of this daemon. Improper configuration may render the system nonfunctional. The "fapolicyd" API is not namespace aware and can cause issues when launching or running containers. Satisfies: SRG-OS-000370-GPOS-00155, SRG-OS-000368-GPOS-00154</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 fapolicyd is active with the following command: $ systemctl is-active fapolicyd active If fapolicyd module is not active, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-271508`

### Rule: OL 9 must have the rsyslog package installed.

**Rule ID:** `SV-271508r1091236_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>rsyslogd is a system utility providing support for message logging. Support for both internet and Unix domain sockets enables this utility to support both local and remote logging. Couple this utility with "gnutls" (which is a secure communications library implementing the SSL, TLS, and DTLS protocols), to create a method to securely encrypt and offload auditing. Satisfies: SRG-OS-000479-GPOS-00224, SRG-OS-000051-GPOS-00024</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has the rsyslogd package installed with the following command: $ dnf list --installed rsyslog Installed Packages rsyslog.x86_64 8.2310.0-4.el9 @AppStream If the rsyslogd package is not installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271509`

### Rule: OL 9 must be configured so that the rsyslog service is active.

**Rule ID:** `SV-271509r1091239_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The rsyslog service must be running to provide logging services, which are essential to system administration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 rsyslog is active with the following command: $ systemctl is-active rsyslog active If the rsyslog service is not active, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-271510`

### Rule: OL 9 must have the packages required for encrypting offloaded audit logs installed.

**Rule ID:** `SV-271510r1091242_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The rsyslog-gnutls package provides Transport Layer Security (TLS) support for the rsyslog daemon, which enables secure remote logging.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has the rsyslog-gnutls package installed with the following command: $ dnf list --installed rsyslog-gnutls Installed Packages rsyslog-gnutls.x86_64 8.2310.0-4.el9 @AppStream If the rsyslog-gnutls package is not installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271511`

### Rule: OL 9 must enable the hardware random number generator entropy gatherer service.

**Rule ID:** `SV-271511r1091245_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The most important characteristic of a random number generator is its randomness, namely its ability to deliver random numbers that are impossible to predict. Entropy in computer security is associated with the unpredictability of a source of randomness. The random source with high entropy tends to achieve a uniform distribution of random values. Random number generators are one of the most important building blocks of cryptosystems. The rngd service feeds random data from hardware device to kernel random device. Quality (nonpredictable) random number generation is important for several security functions (i.e., ciphers).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has enabled the hardware random number generator entropy gatherer service with the following command: $ systemctl is-active rngd active If the rngd service is not active, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271512`

### Rule: OL 9 must have the rng-tools package installed.

**Rule ID:** `SV-271512r1091248_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>rng-tools provides hardware random number generator tools, such as those used in the formation of x509/PKI certificates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has the rng-tools package installed with the following command: $ dnf list --installed rng-tools Installed Packages rng-tools.x86_64 6.16-1.el9 @ol9_baseos_latest If the rng-tools package is not installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271513`

### Rule: OL 9 must have the nss-tools package installed.

**Rule ID:** `SV-271513r1091251_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network Security Services (NSS) is a set of libraries designed to support cross-platform development of security-enabled client and server applications. Install the "nss-tools" package to install command-line tools to manipulate the NSS certificate and key database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has the nss-tools package installed with the following command: $ dnf list --installed nss-tools Installed Packages nss-tools.x86_64 3.101.0-7.el9_2 @ol9_appstream If the nss-tools package is not installed, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-271514`

### Rule: OL 9 must have the pcsc-lite package installed.

**Rule ID:** `SV-271514r1091254_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The pcsc-lite package must be installed if it is to be available for multifactor authentication using smart cards.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has the pcsc-lite package installed with the following command: $ dnf list --installed pcsc-lite Installed Packages pcsc-lite.x86_64 1.9.4-1.el9 @ol9_baseos_latest If the pcsc-lite package is not installed, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-271515`

### Rule: OL 9 must have the opensc package installed.

**Rule ID:** `SV-271515r1091257_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. The DOD has mandated the use of the Common Access Card (CAC) to support identity management and personal authentication for systems covered under Homeland Security Presidential Directive (HSPD) 12, as well as making the CAC a primary component of layered protection for national security systems. Satisfies: SRG-OS-000375-GPOS-00160, SRG-OS-000376-GPOS-00161</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has the opensc package installed with the following command: $ dnf list --installed opensc Installed Packages opensc.x86_64 0.23.0-4.el9_3 @ol9_baseos_latest If the opensc package is not installed, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-271516`

### Rule: OL 9 must be configured so that the pcscd service is active.

**Rule ID:** `SV-271516r1091260_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The information system ensures that even if the information system is compromised, that compromise will not affect credentials stored on the authentication device. The daemon program for pcsc-lite and the MuscleCard framework is pcscd. It is a resource manager that coordinates communications with smart card readers and smart cards and cryptographic tokens that are connected to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 pcscd service is active with the following command: $ systemctl is-active pcscd active If the pcscdservice is not active, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-271517`

### Rule: OL 9 must have the libreswan package installed.

**Rule ID:** `SV-271517r1101885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Providing the ability for remote users or systems to initiate a secure VPN connection protects information when it is transmitted over a wide area network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If there is no operational need for Libreswan to be installed, this rule is not applicable. Verify that OL 9 libreswan service package is installed. Check that the libreswan service package is installed with the following command: $ dnf list --installed libreswan Installed Packages libreswan.x86_64 4.12-2.0.1.el9_4.1 @ol9_appstream If the libreswan package is not installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271518`

### Rule: OL 9 must have the gnutls-utils package installed.

**Rule ID:** `SV-271518r1091266_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>GnuTLS is a secure communications library implementing the SSL, TLS, and DTLS protocols and technologies around them. It provides a simple C language application programming interface (API) to access the secure communications protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and other required structures. This package contains command line TLS client and server and certificate manipulation tools.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has the gnutls-utils package installed with the following command: $ dnf list --installed gnutls-utils Installed Packages gnutls-utils.x86_64 3.8.3-4.el9_4 @ol9_appstream If the gnutls-utils package is not installed, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-271519`

### Rule: OL 9 must have the audit package installed.

**Rule ID:** `SV-271519r1091269_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, the source of events, where events occurred, and the outcome of events, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in audit logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured OL 9 system. Satisfies: SRG-OS-000062-GPOS-00031, SRG-OS-000037-GPOS-00015, SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00021, SRG-OS-000051-GPOS-00024, SRG-OS-000054-GPOS-00025, SRG-OS-000122-GPOS-00063, SRG-OS-000254-GPOS-00095, SRG-OS-000255-GPOS-00096, SRG-OS-000337-GPOS-00129, SRG-OS-000348-GPOS-00136, SRG-OS-000349-GPOS-00137, SRG-OS-000350-GPOS-00138, SRG-OS-000351-GPOS-00139, SRG-OS-000352-GPOS-00140, SRG-OS-000353-GPOS-00141, SRG-OS-000354-GPOS-00142, SRG-OS-000358-GPOS-00145, SRG-OS-000365-GPOS-00152, SRG-OS-000392-GPOS-00172, SRG-OS-000475-GPOS-00220, SRG-OS-000055-GPOS-00026</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 audit service package is installed. Check that the audit service package is installed with the following command: $ dnf list --installed audit Installed Packages audit.x86_64 3.1.2-2.0.1.el9 @ol9_baseos_latest If the audit package is not installed, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-271520`

### Rule: OL 9 audit service must be enabled.

**Rule ID:** `SV-271520r1091272_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Ensuring the "auditd" service is active ensures audit records generated by the kernel are appropriately recorded. Additionally, a properly configured audit subsystem ensures that actions of individual system users can be uniquely traced to those users so they can be held accountable for their actions. Satisfies: SRG-OS-000062-GPOS-00031, SRG-OS-000037-GPOS-00015, SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00021, SRG-OS-000051-GPOS-00024, SRG-OS-000054-GPOS-00025, SRG-OS-000122-GPOS-00063, SRG-OS-000254-GPOS-00095, SRG-OS-000255-GPOS-00096, SRG-OS-000337-GPOS-00129, SRG-OS-000348-GPOS-00136, SRG-OS-000349-GPOS-00137, SRG-OS-000350-GPOS-00138, SRG-OS-000351-GPOS-00139, SRG-OS-000352-GPOS-00140, SRG-OS-000353-GPOS-00141, SRG-OS-000354-GPOS-00142, SRG-OS-000358-GPOS-00145, SRG-OS-000365-GPOS-00152, SRG-OS-000392-GPOS-00172, SRG-OS-000475-GPOS-00220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 audit service is configured to produce audit records with the following command: $ systemctl status auditd.service auditd.service - Security Auditing Service Loaded:loaded (/usr/lib/systemd/system/auditd.service; enabled; vendor preset: enabled) Active: active (running) since Tues 2022-05-24 12:56:56 EST; 4 weeks 0 days ago If the audit service is not "active" and "running", this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-271521`

### Rule: OL 9 must have the audispd-plugins package installed.

**Rule ID:** `SV-271521r1091275_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>audispd-plugins provides plug-ins for the real-time interface to the audit subsystem, audispd. These plug-ins can do things like relay events to remote machines or analyze events for suspicious behavior.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has the audispd-plugins package for installed with the following command: $ dnf list --installed audispd-plugins Example output: Installed Packages audispd-plugins.x86_64 3.1.2-2.0.1.el9 @ol9_baseos_latest If the audispd-plugins package is not installed, this is a finding.

## Group: SRG-OS-000437-GPOS-00194

**Group ID:** `V-271522`

### Rule: OL 9 must remove all software components after updated versions have been installed.

**Rule ID:** `SV-271522r1091278_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Previous versions of software components that are not removed from the information system after updates have been installed may be exploited by some adversaries.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 removes all software components after updated versions have been installed with the following command: $ grep clean /etc/dnf/dnf.conf clean_requirements_on_remove=True If clean_requirements_on_remove is not set to "True", this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-271523`

### Rule: OL 9 must check the GPG signature of locally installed software packages before installation.

**Rule ID:** `SV-271523r1091281_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. All software packages must be signed with a cryptographic key recognized and approved by the organization. Verifying the authenticity of software prior to installation validates the integrity of the software package received from a vendor. This verifies the software has not been tampered with and that it has been provided by a trusted vendor.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 dnf package manager always checks the GPG signature of locally installed software packages before installation: $ grep localpkg_gpgcheck /etc/dnf/dnf.conf localpkg_gpgcheck=1 If "localpkg_gpgcheck" is not set to "1", or if the option is missing or commented out, ask the system administrator how the GPG signatures of local software packages are being verified. If there is no process to verify GPG signatures that is approved by the organization, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-271524`

### Rule: OL 9 must check the GPG signature of software packages originating from external software repositories before installation.

**Rule ID:** `SV-271524r1091284_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. All software packages must be signed with a cryptographic key recognized and approved by the organization. Verifying the authenticity of software prior to installation validates the integrity of the software package received from a vendor. This verifies the software has not been tampered with and that it has been provided by a trusted vendor.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 dnf package manager always checks the GPG signature of software packages originating from external software repositories before installation: $ grep gpgcheck /etc/dnf/dnf.conf gpgcheck=1 If "gpgcheck" is not set to "1", or if the option is missing or commented out, ask the system administrator how the GPG signatures of software packages are being verified. If there is no process to verify GPG signatures that is approved by the organization, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-271525`

### Rule: OL 9 must have GPG signature verification enabled for all software repositories.

**Rule ID:** `SV-271525r1091287_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. All software packages must be signed with a cryptographic key recognized and approved by the organization. Verifying the authenticity of software prior to installation validates the integrity of the software package received from a vendor. This verifies the software has not been tampered with and that it has been provided by a trusted vendor.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 software repositories defined in "/etc/yum.repos.d/" have been configured with "gpgcheck" enabled: $ grep gpgcheck /etc/yum.repos.d/*.repo | more gpgcheck = 1 If "gpgcheck" is not set to "1" for all returned lines, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-271526`

### Rule: OL 9 must ensure cryptographic verification of vendor software packages.

**Rule ID:** `SV-271526r1092460_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cryptographic verification of vendor software packages ensures that all software packages are obtained from a valid source and protects against spoofing that could lead to installation of malware on the system. Oracle cryptographically signs all software packages, which includes updates, with a GPG key to verify that they are valid.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 ensures cryptographic verification of vendor software packages by confirming that Oracle package-signing keys are installed on the system, and verify their fingerprints match vendor values. Note: For OL 9 software packages, Oracle uses GPG keys labeled "release key 1" and "auxiliary key 1". The keys are defined in key file "/etc/pki/rpm-gpg/RPM-GPG-KEY-oracle" by default. List Oracle GPG keys installed on the system: $ sudo rpm -q --queryformat "%{SUMMARY}\n" gpg-pubkey | grep -i "oracle" Oracle Linux (release key 1) <secalert_us@oracle.com> public key Oracle Linux (backup key 1) <secalert_us@oracle.com> public key If Oracle GPG keys "release key 1" and "backup key 1" are not installed, this is a finding. List key fingerprints of installed Oracle GPG keys: $ sudo gpg -q --keyid-format short --with-fingerprint /etc/pki/rpm-gpg/RPM-GPG-KEY-oracle If key file "/etc/pki/rpm-gpg/RPM-GPG-KEY-oracle" is missing, this is a finding. pub rsa4096/8D8B756F 2022-01-19 [SC] [expires: 2042-01-14] Key fingerprint = 3E6D 826D 3FBA B389 C2F3 8E34 BC4D 06A0 8D8B 756F uid Oracle Linux (release key 1) <secalert_us@oracle.com> sub rsa4096/2E708C25 2022-01-19 [E] [expires: 2041-06-01] pub rsa4096/8B4EFBE6 2022-01-19 [SC] [expires: 2042-01-14] Key fingerprint = 9822 3175 9C74 6706 5D0C E9B2 A7DD 0708 8B4E FBE6 uid Oracle Linux (backup key 1) <secalert_us@oracle.com> sub rsa4096/DA900791 2022-01-19 [E] [expires: 2041-06-02] Compare key fingerprints of installed Oracle GPG keys with fingerprints listed for OL 9 on Oracle verification webpage at https://linux.oracle.com/security/gpg/#gpg. If key fingerprints do not match, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-271527`

### Rule: OL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/sudoers.

**Rule ID:** `SV-271527r1092474_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The actions taken by system administrators must be audited to keep a record of what was executed on the system, as well as for accountability purposes. Editing the sudoers file may be sign of an attacker trying to establish persistent methods to a system, auditing the editing of the sudoers files mitigates this risk. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/sudoers" with the following command: $ sudo auditctl -l | grep /etc/sudoers -w /etc/sudoers -p wa -k identity -w /etc/sudoers.d -p wa -k identity If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-271528`

### Rule: OL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/sudoers.d/ directory.

**Rule ID:** `SV-271528r1092476_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The actions taken by system administrators must be audited to keep a record of what was executed on the system, as well as for accountability purposes. Editing the sudoers file may be sign of an attacker trying to establish persistent methods to a system, auditing the editing of the sudoers files mitigates this risk. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/sudoers.d/" with the following command: $ sudo auditctl -l | grep /etc/sudoers.d -w /etc/sudoers.d/ -p wa -k identity If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-271529`

### Rule: OL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/group.

**Rule ID:** `SV-271529r1092478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In addition to auditing new user and group accounts, these watches will alert the system administrator(s) to any modifications. Any unexpected users, groups, or modifications must be investigated for legitimacy. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/group" with the following command: $ sudo auditctl -l | egrep '(/etc/group)' -w /etc/group -p wa -k identity If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-271530`

### Rule: OL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/gshadow.

**Rule ID:** `SV-271530r1092480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In addition to auditing new user and group accounts, these watches will alert the system administrator(s) to any modifications. Any unexpected users, groups, or modifications should be investigated for legitimacy. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/gshadow" with the following command: $ sudo auditctl -l | egrep '(/etc/gshadow)' -w /etc/gshadow -p wa -k identity If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-271531`

### Rule: OL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/opasswd.

**Rule ID:** `SV-271531r1092482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In addition to auditing new user and group accounts, these watches will alert the system administrator(s) to any modifications. Any unexpected users, groups, or modifications should be investigated for legitimacy. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/security/opasswd" with the following command: $ sudo auditctl -l | egrep '(/etc/security/opasswd)' -w /etc/security/opasswd -p wa -k identity If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-271532`

### Rule: OL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/passwd.

**Rule ID:** `SV-271532r1092484_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In addition to auditing new user and group accounts, these watches will alert the system administrator(s) to any modifications. Any unexpected users, groups, or modifications should be investigated for legitimacy. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221, SRG-OS-000274-GPOS-00104, SRG-OS-000275-GPOS-00105, SRG-OS-000276-GPOS-00106, SRG-OS-000277-GPOS-00107</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/passwd" with the following command: $ sudo auditctl -l | egrep '(/etc/passwd)' -w /etc/passwd -p wa -k identity If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-271533`

### Rule: OL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/shadow.

**Rule ID:** `SV-271533r1092486_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In addition to auditing new user and group accounts, these watches will alert the system administrator(s) to any modifications. Any unexpected users, groups, or modifications should be investigated for legitimacy. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/shadow" with the following command: $ sudo auditctl -l | egrep '(/etc/shadow)' -w /etc/shadow -p wa -k identity If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271534`

### Rule: OL 9 must audit all uses of the unix_update command.

**Rule ID:** `SV-271534r1092488_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit record specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000064-GPOS-00033, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the "unix_update" command with the following command: $ sudo auditctl -l | grep unix_update -a always,exit -F path=/usr/sbin/unix_update -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271535`

### Rule: OL 9 must audit all uses of the su command.

**Rule ID:** `SV-271535r1092490_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit record specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000064-GPOS-00033, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000466-GPOS-00210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the su command with the following command: $ sudo auditctl -l | grep /usr/bin/su -a always,exit -F path=/usr/bin/su -F perm=x -F auid>=1000 -F auid!=unset -k privileged-priv_change If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271536`

### Rule: OL 9 must audit all uses of the setxattr, fsetxattr, lsetxattr, removexattr, fremovexattr, and lremovexattr system calls.

**Rule ID:** `SV-271536r1092492_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000458-GPOS-00203, SRG-OS-000462-GPOS-00206, SRG-OS-000463-GPOS-00207, SRG-OS-000471-GPOS-00215, SRG-OS-000474-GPOS-00219, SRG-OS-000466-GPOS-00210, SRG-OS-000064-GPOS-00033</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the setxattr, fsetxattr, lsetxattr, removexattr, fremovexattr, and lremovexattr system calls with the following command: $ sudo auditctl -l | grep xattr -a always,exit -F arch=b32 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b64 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b32 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid=0 -k perm_mod -a always,exit -F arch=b64 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid=0 -k perm_mod If both the "b32" and "b64" audit rules are not defined for the setxattr, fsetxattr, lsetxattr, removexattr, fremovexattr, and lremovexattr system calls, or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271537`

### Rule: OL 9 must audit all uses of the chage command.

**Rule ID:** `SV-271537r1092494_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the chage command with the following command: $ sudo auditctl -l | grep chage -a always,exit -F path=/usr/bin/chage -F perm=x -F auid>=1000 -F auid!=unset -k privileged-chage If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271538`

### Rule: OL 9 must audit all uses of the chcon command.

**Rule ID:** `SV-271538r1092496_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215, SRG-OS-000463-GPOS-00207, SRG-OS-000465-GPOS-00209</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the chcon command with the following command: $ sudo auditctl -l | grep chcon -a always,exit -F path=/usr/bin/chcon -F perm=x -F auid>=1000 -F auid!=unset -k perm_mod If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271539`

### Rule: OL 9 must audit all uses of the setfacl command.

**Rule ID:** `SV-271539r1092498_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the setfacl command with the following command: $ sudo auditctl -l | grep setfacl -a always,exit -F path=/usr/bin/setfacl -F perm=x -F auid>=1000 -F auid!=unset -k perm_mod If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271540`

### Rule: OL 9 must audit all uses of the chsh command.

**Rule ID:** `SV-271540r1092500_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the chsh command with the following command: $ sudo auditctl -l | grep chsh -a always,exit -F path=/usr/bin/chsh -F perm=x -F auid>=1000 -F auid!=unset -k priv_cmd If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271541`

### Rule: OL 9 must audit all uses of the crontab command.

**Rule ID:** `SV-271541r1092502_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the crontab command with the following command: $ sudo auditctl -l | grep crontab -a always,exit -F path=/usr/bin/crontab -F perm=x -F auid>=1000 -F auid!=unset -k privileged-crontab If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271542`

### Rule: OL 9 must audit all uses of the gpasswd command.

**Rule ID:** `SV-271542r1092504_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the gpasswd command with the following command: $ sudo auditctl -l | grep gpasswd -a always,exit -F path=/usr/bin/gpasswd -F perm=x -F auid>=1000 -F auid!=unset -k privileged-gpasswd If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271543`

### Rule: OL 9 must audit all uses of the newgrp command.

**Rule ID:** `SV-271543r1092506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the newgrp command with the following command: $ sudo auditctl -l | grep newgrp -a always,exit -F path=/usr/bin/newgrp -F perm=x -F auid>=1000 -F auid!=unset -k priv_cmd If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271544`

### Rule: OL 9 must audit all uses of the pam_timestamp_check command.

**Rule ID:** `SV-271544r1092508_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the pam_timestamp_check command with the following command: $ sudo auditctl -l | grep timestamp -a always,exit -F path=/usr/sbin/pam_timestamp_check -F perm=x -F auid>=1000 -F auid!=unset -k privileged-pam_timestamp_check If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271545`

### Rule: OL 9 must audit all uses of the passwd command.

**Rule ID:** `SV-271545r1092510_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/passwd" with the following command: $ sudo auditctl -l | egrep '(/usr/bin/passwd)' -a always,exit -F path=/usr/bin/passwd -F perm=x -F auid>=1000 -F auid!=unset -k privileged-passwd If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271546`

### Rule: OL 9 must audit all uses of the postdrop command.

**Rule ID:** `SV-271546r1092512_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the postdrop command with the following command: $ sudo auditctl -l | grep postdrop -a always,exit -F path=/usr/sbin/postdrop -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271547`

### Rule: OL 9 must audit all uses of the postqueue command.

**Rule ID:** `SV-271547r1092514_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit record specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the postqueue command with the following command: $ sudo auditctl -l | grep postqueue -a always,exit -F path=/usr/sbin/postqueue -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271548`

### Rule: OL 9 must audit all uses of the ssh-agent command.

**Rule ID:** `SV-271548r1092516_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit record specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the ssh-agent command with the following command: $ sudo auditctl -l | grep ssh-agent -a always,exit -F path=/usr/bin/ssh-agent -F perm=x -F auid>=1000 -F auid!=unset -k privileged-ssh If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271549`

### Rule: OL 9 must audit all uses of the ssh-keysign command.

**Rule ID:** `SV-271549r1092518_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit record specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the ssh-keysign command with the following command: $ sudo auditctl -l | grep ssh-keysign -a always,exit -F path=/usr/libexec/openssh/ssh-keysign -F perm=x -F auid>=1000 -F auid!=unset -k privileged-ssh If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271550`

### Rule: OL 9 must audit all uses of the sudoedit command.

**Rule ID:** `SV-271550r1092520_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit record specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the sudoedit command with the following command: $ sudo auditctl -l | grep /usr/bin/sudoedit -a always,exit -F path=/usr/bin/sudoedit -F perm=x -F auid>=1000 -F auid!=unset -k priv_cmd If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271551`

### Rule: OL 9 must audit all uses of the unix_chkpwd command.

**Rule ID:** `SV-271551r1092522_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit record specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the unix_chkpwd command with the following command: $ sudo auditctl -l | grep unix_chkpwd -a always,exit -F path=/usr/sbin/unix_chkpwd -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271552`

### Rule: OL 9 must audit all uses of the userhelper command.

**Rule ID:** `SV-271552r1092524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit record specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the userhelper command with the following command: $ sudo auditctl -l | grep userhelper -a always,exit -F path=/usr/sbin/userhelper -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271553`

### Rule: OL 9 must audit all uses of the mount command.

**Rule ID:** `SV-271553r1092526_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the mount command with the following command: $ sudo auditctl -l | grep /usr/bin/mount -a always,exit -F path=/usr/bin/mount -F perm=x -F auid>=1000 -F auid!=unset -k privileged-mount If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271554`

### Rule: OL 9 must audit all uses of the truncate, ftruncate, creat, open, openat, and open_by_handle_at system calls.

**Rule ID:** `SV-271554r1092528_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000064-GPOS-00033, SRG-OS-000458-GPOS-00203, SRG-OS-000461-GPOS-00205</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit successful/unsuccessful attempts to use the truncate, ftruncate, creat, open, openat, and open_by_handle_at system calls with the following command: $ sudo auditctl -l | grep 'open\|truncate\|creat' -a always,exit -F arch=b32 -S truncate,ftruncate,creat,open,openat,open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b64 -S truncate,ftruncate,creat,open,openat,open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b32 -S truncate,ftruncate,creat,open,openat,open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access -a always,exit -F arch=b64 -S truncate,ftruncate,creat,open,openat,open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=unset -k perm_access If the output does not produce rules containing "-F exit=-EPERM", this is a finding. If the output does not produce rules containing "-F exit=-EACCES", this is a finding. If the command does not return an audit rule for truncate, ftruncate, creat, open, openat, and open_by_handle_at or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271555`

### Rule: OL 9 must audit all uses of the chmod, fchmod, and fchmodat system calls.

**Rule ID:** `SV-271555r1092530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000064-GPOS-00033, SRG-OS-000466-GPOS-00210, SRG-OS-000458-GPOS-00203</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the chmod, fchmod, and fchmodat system calls with the following command: $ sudo auditctl -l | grep chmod -a always,exit -F arch=b32 -S chmod,fchmod,fchmodat -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b64 -S chmod,fchmod,fchmodat -F auid>=1000 -F auid!=unset -k perm_mod If both the "b32" and "b64" audit rules are not defined for the chmod, fchmod, and fchmodat system calls, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271556`

### Rule: OL 9 must audit all uses of the chown, fchown, fchownat, and lchown system calls.

**Rule ID:** `SV-271556r1092532_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000064-GPOS-00033, SRG-OS-000466-GPOS-00210, SRG-OS-000458-GPOS-00203, SRG-OS-000474-GPOS-00219</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the chown, fchown, fchownat, and lchown system calls with the following command: $ sudo auditctl -l | grep chown -a always,exit -F arch=b32 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b64 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=unset -k perm_mod If both the "b32" and "b64" audit rules are not defined for the chown, fchown, fchownat, and lchown system calls, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271557`

### Rule: OL 9 must audit all uses of the semanage command.

**Rule ID:** `SV-271557r1092534_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000463-GPOS-00207, SRG-OS-000465-GPOS-00209</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the semanage command with the following command: $ sudo auditctl -l | grep semanage -a always,exit -F path=/usr/sbin/semanage -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271558`

### Rule: OL 9 must audit all uses of the setfiles command.

**Rule ID:** `SV-271558r1092536_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000463-GPOS-00207, SRG-OS-000465-GPOS-00209</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the setfiles command with the following command: $ sudo auditctl -l | grep setfiles -a always,exit -F path=/usr/sbin/setfiles -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271559`

### Rule: OL 9 must audit all uses of the setsebool command.

**Rule ID:** `SV-271559r1092538_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000463-GPOS-00207, SRG-OS-000465-GPOS-00209</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the setsebool command with the following command: $ sudo auditctl -l | grep setsebool -a always,exit -F path=/usr/sbin/setsebool -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271560`

### Rule: OL 9 must audit all uses of the chacl command.

**Rule ID:** `SV-271560r1092540_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000466-GPOS-00210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the chacl command with the following command: $ sudo auditctl -l | grep chacl -a always,exit -F path=/usr/bin/chacl -F perm=x -F auid>=1000 -F auid!=unset -k perm_mod If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271561`

### Rule: OL 9 must audit all uses of the sudo command.

**Rule ID:** `SV-271561r1092542_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit record specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000466-GPOS-00210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the sudo command with the following command: $ sudo auditctl -l | grep /usr/bin/sudo -a always,exit -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -F auid!=unset -k priv_cmd If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271562`

### Rule: OL 9 must audit all uses of the usermod command.

**Rule ID:** `SV-271562r1092544_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit record specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000466-GPOS-00210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the usermod command with the following command: $ sudo auditctl -l | grep usermod -a always,exit -F path=/usr/sbin/usermod -F perm=x -F auid>=1000 -F auid!=unset -k privileged-usermod If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271563`

### Rule: OL 9 must audit all uses of the rename, unlink, rmdir, renameat, and unlinkat system calls.

**Rule ID:** `SV-271563r1092546_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000466-GPOS-00210, SRG-OS-000467-GPOS-00211, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit successful/unsuccessful attempts to use the rename, unlink, rmdir, renameat, and unlinkat system calls with the following command: $ sudo auditctl -l | grep 'rename\|unlink\|rmdir' -a always,exit -F arch=b32 -S rename,unlink,rmdir,renameat,unlinkat -F auid>=1000 -F auid!=unset -k delete -a always,exit -F arch=b64 -S rename,unlink,rmdir,renameat,unlinkat -F auid>=1000 -F auid!=unset -k delete If the command does not return an audit rule for rename, unlink, rmdir, renameat, and unlinkat or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271564`

### Rule: OL 9 must audit all uses of the delete_module system call.

**Rule ID:** `SV-271564r1092548_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000471-GPOS-00216, SRG-OS-000477-GPOS-00222</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the delete_module system call with the following command: $ sudo auditctl -l | grep delete_module -a always,exit -F arch=b32 -S delete_module -F auid>=1000 -F auid!=unset -k module_chng -a always,exit -F arch=b64 -S delete_module -F auid>=1000 -F auid!=unset -k module_chng If both the "b32" and "b64" audit rules are not defined for the delete_module system call, or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271565`

### Rule: OL 9 must audit all uses of the init_module and finit_module system calls.

**Rule ID:** `SV-271565r1092550_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000471-GPOS-00216, SRG-OS-000477-GPOS-00222</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the init_module and finit_module system calls with the following command: $ sudo auditctl -l | grep init_module -a always,exit -F arch=b32 -S init_module,finit_module -F auid>=1000 -F auid!=unset -k module_chng -a always,exit -F arch=b64 -S init_module,finit_module -F auid>=1000 -F auid!=unset -k module_chng If both the "b32" and "b64" audit rules are not defined for the init_module and finit_module system calls, or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271566`

### Rule: OL 9 must audit all uses of the kmod command.

**Rule ID:** `SV-271566r1092552_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000471-GPOS-00216, SRG-OS-000477-GPOS-00222</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the kmod command with the following command: $ sudo auditctl -l | grep kmod -a always,exit -F path=/usr/bin/kmod -F perm=x -F auid>=1000 -F auid!=unset -k modules If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271567`

### Rule: OL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /var/log/lastlog.

**Rule ID:** `SV-271567r1092554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000473-GPOS-00218, SRG-OS-000470-GPOS-00214</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 generates audit records for all account creations, modifications, disabling, and termination events that affect /var/log/lastlog with the following command: $ sudo auditctl -l | grep /var/log/lastlog -w /var/log/lastlog -p wa -k logins If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271568`

### Rule: OL 9 must audit all uses of umount system calls.

**Rule ID:** `SV-271568r1092556_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the umount command with the following command: $ sudo auditctl -l | grep umount -a always,exit -F path=/usr/bin/umount -F perm=x -F auid>=1000 -F auid!=unset -k privileged-mount If the command does not return an audit rule for umount or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-271569`

### Rule: OL 9 must use cryptographic mechanisms to protect the integrity of audit tools.

**Rule ID:** `SV-271569r1091419_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting the integrity of the tools used for auditing purposes is a critical step toward ensuring the integrity of audit information. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Audit tools include, but are not limited to, vendor-provided and open-source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. It is not uncommon for attackers to replace the audit tools or inject code into the existing tools to provide the capability to hide or erase system activity from the audit logs. To address this risk, audit tools must be cryptographically signed to provide the capability to identify when the audit tools have been modified, manipulated, or replaced. An example is a checksum hash of the file or files. Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000257-GPOS-00098, SRG-OS-000258-GPOS-00099, SRG-OS-000278-GPOS-00108</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 uses cryptographic mechanisms to protect the integrity of the audit tools with the following command: $ sudo cat /etc/aide.conf | grep /usr/sbin/au /usr/sbin/auditctl p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/auditd p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/ausearch p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/aureport p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/autrace p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/autrace p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/augenrules p+i+n+u+g+s+b+acl+xattrs+sha512 If AIDE is not installed, ask the system administrator (SA) how file integrity checks are performed on the system. If any of the audit tools listed above do not have a corresponding line, ask the SA to indicate what cryptographic mechanisms are being used to protect the integrity of the audit tools. If there is no evidence of integrity protection, this is a finding.

## Group: SRG-OS-000326-GPOS-00126

**Group ID:** `V-271570`

### Rule: OL 9 must audit uses of the execve system call.

**Rule ID:** `SV-271570r1092558_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat. Satisfies: SRG-OS-000326-GPOS-00126, SRG-OS-000327-GPOS-00127, SRG-OS-000755-GPOS-00220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the execve system call with the following command: $ sudo auditctl -l | grep execve -a always,exit -F arch=b32 -S execve -C uid!=euid -F euid=0 -k execpriv -a always,exit -F arch=b64 -S execve -C uid!=euid -F euid=0 -k execpriv -a always,exit -F arch=b32 -S execve -C gid!=egid -F egid=0 -k execpriv -a always,exit -F arch=b64 -S execve -C gid!=egid -F egid=0 -k execpriv If the command does not return all lines or the lines are commented out, this is a finding.

## Group: SRG-OS-000392-GPOS-00172

**Group ID:** `V-271571`

### Rule: OL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /var/log/faillock.

**Rule ID:** `SV-271571r1092560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Satisfies: SRG-OS-000392-GPOS-00172, SRG-OS-000470-GPOS-00214, SRG-OS-000473-GPOS-00218</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 generates audit records for all account creations, modifications, disabling, and termination events that affect /var/log/faillock with the following command: $ sudo auditctl -l | grep /var/log/faillock -w /var/log/faillock -p wa -k logins If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000392-GPOS-00172

**Group ID:** `V-271572`

### Rule: OL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /var/log/tallylog.

**Rule ID:** `SV-271572r1092562_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Satisfies: SRG-OS-000392-GPOS-00172, SRG-OS-000470-GPOS-00214, SRG-OS-000473-GPOS-00218</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 generates audit records for all account creations, modifications, disabling, and termination events that affect /var/log/tallylog with the following command: $ sudo auditctl -l | grep /var/log/tallylog -w /var/log/tallylog -p wa -k logins If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-271573`

### Rule: OL 9 must be configured so that successful/unsuccessful uses of the init command generate an audit record.

**Rule ID:** `SV-271573r1092564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of the init command may cause availability issues for the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the init command with the following command: $ sudo auditctl -l | grep init -a always,exit -F path=/usr/sbin/init -F perm=x -F auid>=1000 -F auid!=unset -k privileged-init If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-271574`

### Rule: OL 9 must be configured so that successful/unsuccessful uses of the poweroff command generate an audit record.

**Rule ID:** `SV-271574r1092566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of the poweroff command may cause availability issues for the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the poweroff command with the following command: $ sudo auditctl -l | grep poweroff -a always,exit -F path=/usr/sbin/poweroff -F perm=x -F auid>=1000 -F auid!=unset -k privileged-poweroff If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-271575`

### Rule: OL 9 must be configured so that successful/unsuccessful uses of the reboot command generate an audit record.

**Rule ID:** `SV-271575r1092568_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of the reboot command may cause availability issues for the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the reboot command with the following command: $ sudo auditctl -l | grep reboot -a always,exit -F path=/usr/sbin/reboot -F perm=x -F auid>=1000 -F auid!=unset -k privileged-reboot If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-271576`

### Rule: OL 9 must be configured so that successful/unsuccessful uses of the shutdown command generate an audit record.

**Rule ID:** `SV-271576r1092570_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of the shutdown command may cause availability issues for the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to audit the execution of the shutdown command with the following command: $ sudo auditctl -l | grep shutdown -a always,exit -F path=/usr/sbin/shutdown -F perm=x -F auid>=1000 -F auid!=unset -k privileged-shutdown If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271577`

### Rule: OL 9 must enable auditing of processes that start prior to the audit daemon.

**Rule ID:** `SV-271577r1091443_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. If auditing is enabled late in the startup process, the actions of some startup processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000473-GPOS-00218, SRG-OS-000254-GPOS-00095</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to enable auditing of processes that start prior to the audit daemon. Check that the current GRUB 2 configuration enables auditing: $ sudo grubby --info=ALL | grep audit args="ro crashkernel=auto resume=/dev/mapper/ol-swap rd.lvm.lv=ol/root rd.lvm.lv=ol/swap rhgb quiet fips=1 audit=1 audit_backlog_limit=8192 pti=on If "audit" is not set to "1" or is missing, this is a finding. Check that auditing is enabled by default to persist through kernel updates: $ sudo grep audit /etc/default/grub GRUB_CMDLINE_LINUX="audit=1" If "audit" is not set to "1", is missing, or is commented out, this is a finding.

## Group: SRG-OS-000039-GPOS-00017

**Group ID:** `V-271578`

### Rule: OL 9 must label all offloaded audit logs before sending them to the central log server.

**Rule ID:** `SV-271578r1092572_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enriched logging is needed to determine who, what, and when events occur on a system. Without this, determining root cause of an event will be much more difficult. When audit logs are not labeled before they are sent to a central log server, the audit data will not be able to be analyzed and tied back to the correct system. Satisfies: SRG-OS-000039-GPOS-00017, SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 Audit Daemon is configured to label all offloaded audit logs, with the following command: $ sudo grep name_format /etc/audit/auditd.conf name_format = hostname If the "name_format" option is not "hostname", "fqd", or "numeric", or the line is commented out, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-271579`

### Rule: OL 9 audit system must take appropriate action when an error writing to the audit storage volume occurs.

**Rule ID:** `SV-271579r1091449_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the operating system is at risk of failing to process audit logs as required, it takes action to mitigate the failure. Audit processing failures include software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 takes the appropriate action when an audit processing failure occurs. Check that OL 9 takes the appropriate action when an audit processing failure occurs with the following command: $ sudo grep disk_error_action /etc/audit/auditd.conf disk_error_action = HALT If the value of the "disk_error_action" option is not "SYSLOG", "SINGLE", or "HALT", or the line is commented out, ask the system administrator (SA) to indicate how the system takes appropriate action when an audit process failure occurs. If there is no evidence of appropriate action, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-271580`

### Rule: OL 9 audit system must take appropriate action when the audit storage volume is full.

**Rule ID:** `SV-271580r1091452_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the operating system is at risk of failing to process audit logs as required, it takes action to mitigate the failure. Audit processing failures include software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 takes the appropriate action when the audit storage volume is full. Check that OL 9 takes the appropriate action when the audit storage volume is full with the following command: $ sudo grep disk_full_action /etc/audit/auditd.conf disk_full_action = HALT If the value of the "disk_full_action" option is not "SYSLOG", "SINGLE", or "HALT", or the line is commented out, ask the system administrator (SA) to indicate how the system takes appropriate action when an audit storage volume is full. If there is no evidence of appropriate action, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-271581`

### Rule: OL 9 audit system must take appropriate action when the audit files have reached maximum size.

**Rule ID:** `SV-271581r1091455_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the operating system is at risk of failing to process audit logs as required, it takes action to mitigate the failure. Audit processing failures include software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 takes the appropriate action when the audit files have reached maximum size with the following command: $ sudo grep max_log_file_action /etc/audit/auditd.conf max_log_file_action = ROTATE If the value of the "max_log_file_action" option is not "ROTATE", "SINGLE", or the line is commented out, ask the system administrator (SA)to indicate how the system takes appropriate action when an audit storage volume is full. If there is no evidence of appropriate action, this is a finding.

## Group: SRG-OS-000051-GPOS-00024

**Group ID:** `V-271582`

### Rule: OL 9 must periodically flush audit records to disk to prevent the loss of audit records.

**Rule ID:** `SV-271582r1092574_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If option "freq" is not set to a value that requires audit records being written to disk after a threshold number is reached, then audit records may be lost.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to flush audit records to disk after every 100 records with the following command: $ sudo grep freq /etc/audit/auditd.conf freq = 100 If "freq" isn't set to a value of "100" or greater, the value is missing, or the line is commented out, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-271583`

### Rule: OL 9 audit logs must be group-owned by root or by a restricted logging group to prevent unauthorized read access.

**Rule ID:** `SV-271583r1091461_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029, SRG-OS-000206-GPOS-00084</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 audit logs are group-owned by "root" or a restricted logging group. First determine if a group other than "root" has been assigned to the audit logs with the following command: $ sudo grep log_group /etc/audit/auditd.conf log_group = root Then determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Then, using the location of the audit log file, determine if the audit log is group-owned by "root" using the following command: $ sudo stat -c "%G %n" /var/log/audit/audit.log root /var/log/audit/audit.log If the audit log is not group-owned by "root" or the configured alternative logging group, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-271584`

### Rule: OL 9 audit log directory must be owned by root to prevent unauthorized read access.

**Rule ID:** `SV-271584r1091464_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029, SRG-OS-000206-GPOS-00084</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 audit logs directory is owned by "root". First determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Then using the location of the audit log file, determine if the audit log directory is owned by "root" using the following command: $ sudo ls -ld /var/log/audit drwx------ 2 root root 23 Jun 11 11:56 /var/log/audit If the audit log directory is not owned by "root", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-271585`

### Rule: OL 9 audit logs file must have mode 0600 or less permissive to prevent unauthorized access to the audit log.

**Rule ID:** `SV-271585r1091467_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the OL 9 system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029, SRG-OS-000206-GPOS-00084</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 audit logs have a mode of "0600". First determine where the audit logs are stored with the following command: $ sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Then using the location of the audit log file, determine if the audit log files as a mode of "0640" with the following command: $ sudo ls -la /var/log/audit/*.log rw-------. 2 root root 237923 Jun 11 11:56 /var/log/audit/audit.log If the audit logs have a mode more permissive than "0600", this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-271586`

### Rule: OL 9 audit system must audit local events.

**Rule ID:** `SV-271586r1092576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, the source of events, where events occurred, and the outcome of events, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. If option "local_events" isn't set to "yes" only events from network will be aggregated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 audit system is configured to audit local events with the following command: $ sudo grep local_events /etc/audit/auditd.conf local_events = yes If "local_events" isn't set to "yes", if the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-271587`

### Rule: OL 9 must allow only the information system security manager (ISSM) (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited.

**Rule ID:** `SV-271587r1091473_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict the roles and individuals that can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 sets files in directories "/etc/audit/rules.d/" and "/etc/audit/auditd.conf" files to have a mode of "0640" or less permissive with the following command: $ sudo stat -c "%a %n" /etc/audit/rules.d/*.rules $ sudo sh -c 'stat -c "%a %n" /etc/audit/rules.d/*.rules' 600 /etc/audit/rules.d/audit.rules If the files in the "/etc/audit/rules.d/" directory or the "/etc/audit/auditd.conf" file have a mode more permissive than "0640", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-271588`

### Rule: OL 9 /etc/audit/auditd.conf file must have 0640 or less permissive to prevent unauthorized access.

**Rule ID:** `SV-271588r1091476_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict the roles and individuals that can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 sets the mode of /etc/audit/auditd.conf with the command: $ sudo stat -c "%a %n" /etc/audit/auditd.conf 640 /etc/audit/auditd.conf If "/etc/audit/auditd.conf" does not have a mode of "0640", this is a finding.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-271589`

### Rule: OL 9 must forward mail from postmaster to the root account using a postfix alias.

**Rule ID:** `SV-271589r1091479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 administrators are notified in the event of an audit processing failure. Check that the "/etc/aliases" file has a defined value for "root". $ grep "postmaster:\s*root$" /etc/aliases If the command does not return a line, or the line is commented out, ask the system administrator to indicate how they and the information systems security officer (ISSO) are notified of an audit process failure. If there is no evidence of the proper personnel being notified of an audit processing failure, this is a finding.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-271590`

### Rule: OL 9 must take appropriate action when a critical audit processing failure occurs.

**Rule ID:** `SV-271590r1091482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. Satisfies: SRG-OS-000046-GPOS-00022, SRG-OS-000343-GPOS-00135</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 audit service is configured to panic on a critical error with the following command: $ sudo grep "\-f" /etc/audit/audit.rules -f 2 If the value for "-f" is not "2", and availability is not documented as an overriding concern, this is a finding.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-271591`

### Rule: The OL 9 system administrator (SA) and/or information system security officer (ISSO) (at a minimum) must be alerted of an audit processing failure event.

**Rule ID:** `SV-271591r1092578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both. Satisfies: SRG-OS-000046-GPOS-00022, SRG-OS-000343-GPOS-00134</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to notify the SA and/or ISSO (at a minimum) in the event of an audit processing failure with the following command: $ sudo grep action_mail_acct /etc/audit/auditd.conf action_mail_acct = root If the value of the "action_mail_acct" keyword is not set to "root" and/or other accounts for security personnel, the "action_mail_acct" keyword is missing, or the retuned line is commented out, ask the SA to indicate how they and the ISSO are notified of an audit process failure. If there is no evidence of the proper personnel being notified of an audit processing failure, this is a finding.

## Group: SRG-OS-000254-GPOS-00095

**Group ID:** `V-271592`

### Rule: OL 9 must allocate an audit_backlog_limit of sufficient size to capture processes that start prior to the audit daemon.

**Rule ID:** `SV-271592r1091488_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. If auditing is enabled late in the startup process, the actions of some startup processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created. Audit records can be generated from various components within the information system (e.g., module or policy filter). Allocating an audit_backlog_limit of sufficient size is critical in maintaining a stable boot process. With an insufficient limit allocated, the system is susceptible to boot failures and crashes. Satisfies: SRG-OS-000254-GPOS-00095, SRG-OS-000341-GPOS-00132</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 allocates a sufficient audit_backlog_limit to capture processes that start prior to the audit daemon with the following command: $ sudo grubby --info=ALL | grep args | grep -v 'audit_backlog_limit=8192' If the command returns any outputs, and audit_backlog_limit is less than "8192", this is a finding.

## Group: SRG-OS-000255-GPOS-00096

**Group ID:** `V-271593`

### Rule: OL 9 must produce audit records containing information to establish the identity of any individual or process associated with the event.

**Rule ID:** `SV-271593r1092580_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, the source of events, where events occurred, and the outcome of events, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Enriched logging aids in making sense of who, what, and when events occur on a system. Without this, determining root cause of an event will be much more difficult.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 audit system is configured to resolve audit information before writing to disk, with the following command: $ sudo grep log_format /etc/audit/auditd.conf log_format = ENRICHED If the "log_format" option is not "ENRICHED", or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271594`

### Rule: OL 9 must be configured so that successful/unsuccessful uses of the umount system call generate an audit record.

**Rule ID:** `SV-271594r1092582_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The changing of file permissions could indicate that a user is attempting to gain access to information that would otherwise be disallowed. Auditing DAC modifications can facilitate the identification of patterns of abuse among both authorized and unauthorized users. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 generates an audit record for all uses of the umount system call with the following commands: $ sudo grep "umount" /etc/audit/audit.* $ sudo grep umount /etc/audit/audit.rules If the system is configured to audit this activity, it will return a line like the following: -a always,exit -F arch=b32 -S umount -F auid>=1000 -F auid!=unset -k privileged-umount If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-271595`

### Rule: OL 9 must be configured so that successful/unsuccessful uses of the umount2 system call generate an audit record.

**Rule ID:** `SV-271595r1092584_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The changing of file permissions could indicate that a user is attempting to gain access to information that would otherwise be disallowed. Auditing discretionary access control (DAC) modifications can facilitate the identification of patterns of abuse among both authorized and unauthorized users. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 generates an audit record for all uses of the umount2 system call with the following commands: $ sudo grep "umount2" /etc/audit/audit.rules $ sudo sh -c 'grep "umount2" /etc/audit/audit.rules' If the system is configured to audit this activity, it will return a line. If no line is returned, this is a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-271596`

### Rule: OL 9 must allocate audit record storage capacity to store at least one week's worth of audit records.

**Rule ID:** `SV-271596r1091500_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure OL 9 systems have a sufficient storage capacity in which to write the audit logs, OL 9 needs to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial installation of OL 9. Satisfies: SRG-OS-000341-GPOS-00132, SRG-OS-000342-GPOS-00133</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 allocates audit record storage capacity to store at least one week of audit records when audit records are not immediately sent to a central audit record storage facility. Note: The partition size needed to capture a week of audit records is based on the activity level of the system and the total storage capacity available. Typically 10GB of storage space for audit records should be sufficient. Determine which partition the audit records are being written to with the following command: $ sudo grep log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Check the size of the partition that audit records are written to with the following command and verify whether it is sufficiently large: # df -h /var/log/audit/ /dev/sda2 24G 10.4G 13.6G 43% /var/log/audit If the audit record partition is not allocated for sufficient storage capacity, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-271597`

### Rule: OL 9 must be configured to offload audit records onto a different system from the system being audited via syslog.

**Rule ID:** `SV-271597r1092586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The auditd service does not include the ability to send audit records to a centralized server for management directly. However, it can use a plug-in for audit event multiplexor (audispd) to pass audit records to the local syslog server. Satisfies: SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured use the audisp-remote syslog service with the following command: $ sudo grep active /etc/audit/plugins.d/syslog.conf active = yes If the "active" keyword does not have a value of "yes", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-271598`

### Rule: OL 9 must take appropriate action when the internal event queue is full.

**Rule ID:** `SV-271598r1092588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The audit system should have an action setup in the event the internal event queue becomes full so that no data is lost. Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. Satisfies: SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 audit system is configured to take an appropriate action when the internal event queue is full: $ sudo grep -i overflow_action /etc/audit/auditd.conf overflow_action = syslog If the value of the "overflow_action" option is not set to "syslog", "single", "halt" or the line is commented out, ask the system administrator (SA) to indicate how the audit logs are offloaded to a different system or media. If there is no evidence that the transfer of the audit logs being offloaded to another system or media takes appropriate action if the internal event queue becomes full, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-271599`

### Rule: OL 9 must take action when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity.

**Rule ID:** `SV-271599r1091509_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches 75 percent utilization, they are unable to plan for audit record storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 takes action when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity with the following command: $ sudo grep -w space_left /etc/audit/auditd.conf space_left = 25% If the value of the "space_left" keyword is not set to 25 percent of the storage volume allocated to audit logs, or if the line is commented out, ask the system administrator (SA) to indicate how the system is providing real-time alerts to the SA and information system security officer (ISSO). If the "space_left" value is not configured to the correct value, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-271600`

### Rule: OL 9 must notify the system administrator (SA) and information system security officer (ISSO) (at a minimum) when allocated audit record storage volume 75 percent utilization.

**Rule ID:** `SV-271600r1091512_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches 75 percent utilization, they are unable to plan for audit record storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 notifies the SA and ISSO (at a minimum) when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity with the following command: $ sudo grep -w space_left_action /etc/audit/auditd.conf space_left_action = email If the value of the "space_left_action" is not set to "email", or if the line is commented out, ask the SA to indicate how the system is providing real-time alerts to the SA and ISSO. If there is no evidence that real-time alerts are configured on the system, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-271601`

### Rule: OL 9 must take action when allocated audit record storage volume reaches 95 percent of the audit record storage capacity.

**Rule ID:** `SV-271601r1091515_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If action is not taken when storage volume reaches 95 percent utilization, the auditing system may fail when the storage volume reaches capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 takes action when allocated audit record storage volume reaches 95 percent of the repository maximum audit record storage capacity with the following command: $ sudo grep -w admin_space_left /etc/audit/auditd.conf admin_space_left = 5% If the value of the "admin_space_left" keyword is not set to 5 percent of the storage volume allocated to audit logs, or if the line is commented out, ask the system administrator (SA) to indicate how the system is taking action if the allocated storage is about to reach capacity. If the "space_left" value is not configured to the correct value, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271602`

### Rule: OL 9 must write audit records to disk.

**Rule ID:** `SV-271602r1092590_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit data should be synchronously written to disk to ensure log integrity. This setting ensures that all audit event data is written disk.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 audit system is configured to write logs to the disk with the following command: $ sudo grep write_logs /etc/audit/auditd.conf write_logs = yes If "write_logs" does not have a value of "yes", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-271603`

### Rule: OL 9 must act when allocated audit record storage volume reaches 95 percent of the repository maximum audit record storage capacity.

**Rule ID:** `SV-271603r1092592_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If action is not taken when storage volume reaches 95 percent utilization, the auditing system may fail when the storage volume reaches capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to take action in the event of allocated audit record storage volume reaches 95 percent of the repository maximum audit record storage capacity with the following command: $ sudo grep admin_space_left_action /etc/audit/auditd.conf admin_space_left_action = single If the value of the "admin_space_left_action" is not set to "single", or if the line is commented out, ask the system administrator (SA) to indicate how the system is providing real-time alerts to the SA and information system security officer (ISSO). If there is no evidence that real-time alerts are configured on the system, this is a finding.

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-271604`

### Rule: OL 9, for PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

**Rule ID:** `SV-271604r1091524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a certification authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement. Satisfies: SRG-OS-000066-GPOS-00034, SRG-OS-000384-GPOS-00167, SRG-OS-000775-GPOS-00230</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 for PKI-based authentication has valid certificates by constructing a certification path (which includes status information) to an accepted trust anchor. Check that the system has a valid DOD root CA installed with the following command: $ sudo openssl x509 -text -in /etc/sssd/pki/sssd_auth_ca_db.pem Example output: Certificate: Data: Version: 3 (0x2) Serial Number: 1 (0x1) Signature Algorithm: sha256WithRSAEncryption Issuer: C = US, O = U.S. Government, OU = DOD, OU = PKI, CN = DOD Root CA 3 Validity Not Before: Mar 20 18:46:41 2012 GMT Not After: Dec 30 18:46:41 2029 GMT Subject: C = US, O = U.S. Government, OU = DOD, OU = PKI, CN = DOD Root CA 3 Subject Public Key Info: Public Key Algorithm: rsaEncryption If the root CA file is not a DOD-issued certificate with a valid date and installed in the "/etc/sssd/pki/sssd_auth_ca_db.pem" location, this is a finding.

## Group: SRG-OS-000067-GPOS-00035

**Group ID:** `V-271605`

### Rule: OL 9, for PKI-based authentication, must enforce authorized access to the corresponding private key.

**Rule ID:** `SV-271605r1091527_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the private key is discovered, an attacker can use the key to authenticate as an authorized user and gain access to the network infrastructure. The cornerstone of the PKI is the private key used to encrypt or digitally sign information. If the private key is stolen, this will lead to the compromise of the authentication and nonrepudiation gained through PKI because the attacker can use the private key to digitally sign documents and pretend to be the authorized user. Both the holders of a digital certificate and the issuing authority must protect the computers, storage devices, or whatever they use to keep the private keys.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 SSH private key files have a passcode. For each private key stored on the system, use the following command: $ sudo ssh-keygen -y -f /path/to/file If the contents of the key are displayed, this is a finding.

## Group: SRG-OS-000068-GPOS-00036

**Group ID:** `V-271606`

### Rule: OL 9 must map the authenticated identity to the user or group account for PKI-based authentication.

**Rule ID:** `SV-271606r1091530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without mapping the certificate used to authenticate to the user account, the ability to determine the identity of the individual user or group will not be available for forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 maps the authenticated identity to the certificate of the user or group to the corresponding user or group in the "sssd.conf" file with the following command: $ sudo cat /etc/sssd/sssd.conf [certmap/testing.test/rule_name] matchrule =<SAN>.*EDIPI@mil maprule = (userCertificate;binary={cert!bin}) domains = testing.test If the certmap section does not exist, ask the system administrator (SA) to indicate how certificates are mapped to accounts. If there is no evidence of certificate mapping, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-271607`

### Rule: OL 9 must enable certificate-based smart card authentication.

**Rule ID:** `SV-271607r1091533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of multifactor authentication (MFA), the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. A privileged account is defined as an information system account with authorizations of a privileged user. The DOD Common Access Card (CAC) with DOD-approved PKI is an example of multifactor authentication. Satisfies: SRG-OS-000375-GPOS-00160, SRG-OS-000105-GPOS-00052</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has smart cards enabled in System Security Services Daemon (SSSD) if smart cards are used for MFA with the following command: $ sudo grep pam_cert_auth /etc/sssd/sssd.conf pam_cert_auth = True If "pam_cert_auth" is not set to "True", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-271608`

### Rule: OL 9 must implement certificate status checking for multifactor authentication (MFA).

**Rule ID:** `SV-271608r1091536_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a DOD Common Access Card (CAC) or token that is separate from the information system, ensures that even if the information system is compromised, credentials stored on the authentication device will not be affected. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification (PIV) card and the DOD CAC. OL 9 includes multiple options for configuring certificate status checking, but for this requirement focuses on the System Security Services Daemon (SSSD). By default, SSSD performs Online Certificate Status Protocol (OCSP) checking and certificate verification using a sha256 digest function. Satisfies: SRG-OS-000375-GPOS-00160, SRG-OS-000377-GPOS-00162</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 implements Online Certificate Status Protocol (OCSP) and is using the proper digest value on the system with the following command: $ sudo grep certificate_verification /etc/sssd/sssd.conf /etc/sssd/conf.d/*.conf | grep -v "^#" certificate_verification = ocsp_dgst=sha512 If the certificate_verification line is missing from the [sssd] section, or is missing "ocsp_dgst=sha512", ask the administrator to indicate what type of multifactor authentication is being used and how the system implements certificate status checking. If there is no evidence of certificate status checking being used, this is a finding.

## Group: SRG-OS-000383-GPOS-00166

**Group ID:** `V-271609`

### Rule: OL 9 must prohibit the use of cached authenticators after one day.

**Rule ID:** `SV-271609r1091539_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cached authentication information is out-of-date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If smart card authentication is not being used on the system, this requirement is Not Applicable. Verify that OL 9's System Security Services Daemon (SSSD) prohibits the use of cached authentications after one day. Check that SSSD allows cached authentications with the following command: $ sudo grep cache_credentials /etc/sssd/sssd.conf cache_credentials = true If "cache_credentials" is set to "false" or missing from the configuration file, this is not a finding and no further checks are required. If "cache_credentials" is set to "true", check that SSSD prohibits the use of cached authentications after one day with the following command: $ sudo grep offline_credentials_expiration /etc/sssd/sssd.conf offline_credentials_expiration = 1 If "offline_credentials_expiration" is not set to a value of "1", this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-271610`

### Rule: OL 9 must use the CAC smart card driver.

**Rule ID:** `SV-271610r1091542_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Smart card login provides two-factor authentication stronger than that provided by a username and password combination. Smart cards leverage public key infrastructure to provide and verify credentials. Configuring the smart card driver in use by the organization helps to prevent users from using unauthorized smart cards. Satisfies: SRG-OS-000104-GPOS-00051, SRG-OS-000106-GPOS-00053, SRG-OS-000107-GPOS-00054, SRG-OS-000109-GPOS-00056, SRG-OS-000108-GPOS-00055, SRG-OS-000112-GPOS-00057, SRG-OS-000113-GPOS-00058</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 loads the CAC driver with the following command: $ grep card_drivers /etc/opensc.conf card_drivers = cac; If "cac" is not listed as a card driver, or there is no line returned for "card_drivers", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271611`

### Rule: OL 9 must ensure the password complexity module is enabled in the system-auth file.

**Rule ID:** `SV-271611r1091545_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling PAM password complexity permits enforcement of strong passwords and consequently makes the system less prone to dictionary attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 uses "pwquality" to enforce the password complexity rules in the system-auth file with the following command: $ cat /etc/pam.d/system-auth | grep pam_pwquality password required pam_pwquality.so If the command does not return a line containing the value "pam_pwquality.so", or the line is commented out, this is a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-271612`

### Rule: OL 9 must ensure the password complexity module in the system-auth file is configured for three retries or less.

**Rule ID:** `SV-271612r1091548_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. "pwquality" enforces complex password construction configuration and has the ability to limit brute-force attacks on the system. OL 9 uses "pwquality" as a mechanism to enforce password complexity. This is set in both: /etc/pam.d/password-auth /etc/pam.d/system-auth By limiting the number of attempts to meet the pwquality module complexity requirements before returning with an error, the system will audit abnormal attempts at password changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to limit the "pwquality" retry option to "3". Check for the use of the "pwquality" retry option in the system-auth file with the following command: $ grep pam_pwquality /etc/pam.d/system-auth password required pam_pwquality.so retry=3 If the value of "retry" is set to "0" or greater than "3", or is missing, this is a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-271613`

### Rule: OL 9 must enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-271613r1091551_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Requiring a minimum number of uppercase characters makes password guessing attacks more difficult by ensuring a larger search space.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 enforces password complexity by requiring at least one uppercase character. Check the value for "ucredit" with the following command: $ grep ucredit /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf ucredit = -1 If the value of "ucredit" is a positive number or is commented out, this is a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-271614`

### Rule: OL 9 must ensure the password complexity module is enabled in the password-auth file.

**Rule ID:** `SV-271614r1091554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling PAM password complexity permits enforcement of strong passwords and consequently makes the system less prone to dictionary attacks. Satisfies: SRG-OS-000069-GPOS-00037, SRG-OS-000070-GPOS-00038</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 uses "pwquality" to enforce the password complexity rules in the password-auth file with the following command: $ grep pam_pwquality /etc/pam.d/password-auth | grep pam_pwquality password required pam_pwquality.so If the command does not return a line containing the value "pam_pwquality.so", or the line is commented out, this is a finding.

## Group: SRG-OS-000070-GPOS-00038

**Group ID:** `V-271615`

### Rule: OL 9 must enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-271615r1091557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Requiring a minimum number of lowercase characters makes password guessing attacks more difficult by ensuring a larger search space.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 enforces password complexity by requiring at least one lowercase character. Check the value for "lcredit" with the following command: $ grep lcredit /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf /etc/security/pwquality.conf:lcredit = -1 If the value of "lcredit" is a positive number or is commented out, this is a finding.

## Group: SRG-OS-000071-GPOS-00039

**Group ID:** `V-271616`

### Rule: OL 9 must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-271616r1091560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Requiring digits makes password guessing attacks more difficult by ensuring a larger search space.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 enforces password complexity by requiring at least one numeric character. Check the value for "dcredit" with the following command: $ grep dcredit /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf /etc/security/pwquality.conf:dcredit = -1 If the value of "dcredit" is a positive number or is commented out, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-271617`

### Rule: OL 9 must require the change of at least eight characters when passwords are changed.

**Rule ID:** `SV-271617r1091563_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Requiring a minimum number of different characters during password changes ensures that newly changed passwords will not resemble previously compromised ones. Note that passwords changed on compromised systems will still be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 requires the change of at least eight characters when passwords are changed. Verify the value of the "difok" option in "/etc/security/pwquality.conf" with the following command: $ grep difok /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf difok = 8 If the value of "difok" is set to less than "8", or is commented out, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-271618`

### Rule: OL 9 must require the maximum number of repeating characters of the same character class be limited to four when passwords are changed.

**Rule ID:** `SV-271618r1091566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex a password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 requires the maximum number of repeating characters of the same character class be limited to four when passwords are changed. Verify the value of the "maxclassrepeat" option in "/etc/security/pwquality.conf" with the following command: $ grep maxclassrepeat /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf maxclassrepeat = 4 If the value of "maxclassrepeat" is set to "0", more than "4", or is commented out, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-271619`

### Rule: OL 9 must require the maximum number of repeating characters be limited to three when passwords are changed.

**Rule ID:** `SV-271619r1091569_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex a password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 requires the maximum number of repeating characters be limited to three when passwords are changed. Verify the value of the "maxrepeat" option in "/etc/security/pwquality.conf" with the following command: $ grep maxrepeat /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf maxrepeat = 3 If the value of "maxrepeat" is set to more than "3", or is commented out, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-271620`

### Rule: OL 9 must require the change of at least four character classes when passwords are changed.

**Rule ID:** `SV-271620r1091572_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex a password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 requires the change of at least four character classes when passwords are changed. Verify the value of the "minclass" option in "/etc/security/pwquality.conf" with the following command: $ grep minclass /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf minclass = 4 If the value of "minclass" is set to less than "4", or is commented out, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-271621`

### Rule: OL 9 must enforce password complexity rules for the root account.

**Rule ID:** `SV-271621r1091575_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Satisfies: SRG-OS-000072-GPOS-00040, SRG-OS-000071-GPOS-00039, SRG-OS-000070-GPOS-00038, SRG-OS-000266-GPOS-00101, SRG-OS-000078-GPOS-00046, SRG-OS-000480-GPOS-00225, SRG-OS-000069-GPOS-00037</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 enforces password complexity rules for the root account. Check if root user is required to use complex passwords with the following command: $ grep enforce_for_root /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf /etc/security/pwquality.conf:enforce_for_root If "enforce_for_root" is commented or missing, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-271622`

### Rule: OL 9 must be configured so that user and group account administration utilities are configured to store only encrypted representations of passwords.

**Rule ID:** `SV-271622r1091578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Passwords that are encrypted with a weak algorithm are no more protected than if they are kept in plain text. This setting ensures user and group account administration utilities are configured to store only encrypted representations of passwords. Additionally, the "crypt_style" configuration option ensures the use of a strong hashing algorithm that makes password cracking attacks more difficult.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 user and group account administration utilities are configured to store only encrypted representations of passwords with the following command: # grep crypt /etc/libuser.conf crypt_style = sha512 If the "crypt_style" variable is not set to "sha512", is not in the defaults section, is commented out, or does not exist, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-271623`

### Rule: OL 9 must be configured to use the shadow file to store only encrypted representations of passwords.

**Rule ID:** `SV-271623r1091581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Passwords that are encrypted with a weak algorithm are no more protected than if they are kept in plain text. This setting ensures user and group account administration utilities are configured to store only encrypted representations of passwords. Additionally, the "crypt_style" configuration option ensures the use of a strong hashing algorithm that makes password cracking attacks more difficult.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 shadow file is configured to store only encrypted representations of passwords with a hash value of "SHA512" with the following command: # grep -i encrypt_method /etc/login.defs ENCRYPT_METHOD SHA512 If "ENCRYPT_METHOD" does not have a value of "SHA512", or the line is commented out, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-271624`

### Rule: OL 9 pam_unix.so module must be configured in the password-auth file to use a FIPS 140-3 approved cryptographic hashing algorithm for system authentication.

**Rule ID:** `SV-271624r1091584_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore, cannot be relied upon to provide confidentiality or integrity, and DOD data may be compromised. OL 9 systems using encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-3 is the current standard for validating that mechanisms used to access cryptographic modules use authentication that meets DOD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general-purpose computing system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 pam_unix.so module is configured to use sha512 in /etc/pam.d/password-auth with the following command: $ grep "^password.*pam_unix.so.*sha512" /etc/pam.d/password-auth password sufficient pam_unix.so sha512 If "sha512" is missing, or the line is commented out, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-271625`

### Rule: OL 9 password-auth must be configured to use a sufficient number of hashing rounds.

**Rule ID:** `SV-271625r1091587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Passwords that are encrypted with a weak algorithm are no more protected than if they are kept in plain text. Using more hashing rounds makes password cracking attacks more difficult. Satisfies: SRG-OS-000073-GPOS-00041, SRG-OS-000120-GPOS-00061</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 password-auth is configured to use a sufficient number of hashing rounds with the following command: $ sudo grep rounds /etc/pam.d/password-auth password sufficient pam_unix.so sha512 rounds=100000 If a matching line is not returned or "rounds" is less than "100000", this a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-271626`

### Rule: OL 9 system-auth must be configured to use a sufficient number of hashing rounds.

**Rule ID:** `SV-271626r1091590_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Passwords that are encrypted with a weak algorithm are no more protected than if they are kept in plain text. Using more hashing rounds makes password cracking attacks more difficult. Satisfies: SRG-OS-000073-GPOS-00041, SRG-OS-000120-GPOS-00061</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 system-auth is configured to use a sufficient number of hashing rounds with the following command: $ sudo grep rounds /etc/pam.d/system-auth password sufficient pam_unix.so sha512 rounds=100000 If a matching line is not returned or "rounds" is less than 100000, this a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-271627`

### Rule: OL 9 shadow password suite must be configured to use a sufficient number of hashing rounds.

**Rule ID:** `SV-271627r1091593_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Passwords that are encrypted with a weak algorithm are no more protected than if they are kept in plain text. Using more hashing rounds makes password cracking attacks more difficult. Satisfies: SRG-OS-000073-GPOS-00041, SRG-OS-000120-GPOS-00061</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has a minimum number of hash rounds configured with the following command: $ grep -i sha_crypt /etc/login.defs If "SHA_CRYPT_MIN_ROUNDS" or "SHA_CRYPT_MAX_ROUNDS" is less than "100000", this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-271628`

### Rule: OL 9 must employ FIPS 140-3 approved cryptographic hashing algorithms for all stored passwords.

**Rule ID:** `SV-271628r1091596_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The system must use a strong hashing algorithm to store the password. Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Satisfies: SRG-OS-000073-GPOS-00041, SRG-OS-000120-GPOS-00061</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 interactive user account passwords are using a strong password hash with the following command: $ sudo cut -d: -f2 /etc/shadow $6$kcOnRq/5$NUEYPuyL.wghQwWssXRcLRFiiru7f5JPV6GaJhNC2aK5F3PZpE/BCCtwrxRc/AInKMNX3CdMw11m9STiql12f/ Password hashes "!" or "*" indicate inactive accounts not available for logon and are not evaluated. If any interactive user password hash does not begin with "$6", this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-271629`

### Rule: OL 9 passwords for new users or password changes must have a 24-hour minimum password lifetime restriction in /etc/login.defs.

**Rule ID:** `SV-271629r1091599_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse. Setting the minimum password age protects against users cycling back to a favorite password after satisfying the password reuse requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 enforces a 24-hour minimum password lifetime for new user accounts. Check for the value of "PASS_MIN_DAYS" in "/etc/login.defs" with the following command: $ grep -i pass_min_days /etc/login.defs PASS_MIN_DAYS 1 If the "PASS_MIN_DAYS" parameter value is not "1" or greater, or is commented out, this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-271630`

### Rule: OL 9 passwords must have a 24-hour minimum password lifetime restriction in /etc/shadow.

**Rule ID:** `SV-271630r1091602_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has configured the minimum time period between password changes for each user account as 24 hours or greater with the following command: $ sudo awk -F: '$4 < 1 {print $1 " " $4}' /etc/shadow If any results are returned that are not associated with a system account, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-271631`

### Rule: OL 9 user account passwords for new users or password changes must have a 60-day maximum password lifetime restriction in /etc/login.defs.

**Rule ID:** `SV-271631r1091605_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked; therefore, passwords need to be changed periodically. If the operating system does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the operating system passwords could be compromised. Setting the password maximum age ensures users are required to periodically change their passwords. Requiring shorter password lifetimes increases the risk of users writing down the password in a convenient location subject to physical compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 enforces a 60-day maximum password lifetime for new user accounts by running the following command: $ grep -i pass_max_days /etc/login.defs PASS_MAX_DAYS 60 If the "PASS_MAX_DAYS" parameter value is greater than "60", or commented out, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-271632`

### Rule: OL 9 user account passwords must have a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-271632r1091608_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked; therefore, passwords need to be changed periodically. If OL 9 does not limit the lifetime of passwords and force users to change their passwords, there is the risk that OL 9 passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 user account passwords have a 60-day maximum password lifetime restriction with the following commands: $ sudo awk -F: '$5 > 60 {print $1 "" "" $5}' /etc/shadow $ sudo awk -F: '$5 <= 0 {print $1 "" "" $5}' /etc/shadow If any results are returned that are not associated with a system account, this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-271633`

### Rule: OL 9 passwords must be created with a minimum of 15 characters.

**Rule ID:** `SV-271633r1091611_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to increase exponentially the time and/or resources required to compromise the password. OL 9 uses "pwquality" as a mechanism to enforce password complexity. Configurations are set in the "etc/security/pwquality.conf" file. The "minlen", sometimes noted as minimum length, acts as a "score" of complexity based on the credit components of the "pwquality" module. By setting the credit components to a negative value, not only will those components be required, but they will not count toward the total "score" of "minlen". This will enable "minlen" to require a 15-character minimum. The DOD minimum password requirement is 15 characters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 enforces a minimum 15-character password length with the following command: $ grep minlen /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf minlen = 15 If the command does not return a "minlen" value of "15" or greater, does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271634`

### Rule: OL 9 must not allow blank or null passwords.

**Rule ID:** `SV-271634r1091614_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log in and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 does not allow null passwords with the following command: $ grep -i nullok /etc/pam.d/system-auth /etc/pam.d/password-auth If output is produced, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-271635`

### Rule: OL 9 must require a boot loader superuser password.

**Rule ID:** `SV-271635r1091617_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Password protection on the boot loader configuration ensures users with physical access cannot trivially alter important bootloader settings. These include which kernel to use, and whether to enter single-user mode.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 requires a boot loader superuser password with the following command: $ sudo grep "superusers" /etc/grub2.cfg password_pbkdf2 superusers-account ${GRUB2_PASSWORD} To verify the boot loader superuser account password has been set, and the password encrypted, run the following command: $ sudo cat /boot/grub2/user.cfg GRUB2_PASSWORD=grub.pbkdf2.sha512.10000.C4E08AC72FBFF7E837FD267BFAD7AEB3D42DDC 2C99F2A94DD5E2E75C2DC331B719FE55D9411745F82D1B6CFD9E927D61925F9BBDD1CFAA0080E0 916F7AB46E0D.1302284FCCC52CD73BA3671C6C12C26FF50BA873293B24EE2A96EE3B57963E6D7 0C83964B473EC8F93B07FE749AA6710269E904A9B08A6BBACB00A2D242AD828 If a "GRUB2_PASSWORD" is not set, this is a finding.

## Group: SRG-OS-000266-GPOS-00101

**Group ID:** `V-271636`

### Rule: OL 9 must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-271636r1091620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. OL 9 uses "pwquality" as a mechanism to enforce password complexity. Note that to require special characters without degrading the "minlen" value, the credit value must be expressed as a negative number in "/etc/security/pwquality.conf".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 enforces password complexity by requiring at least one special character with the following command: $ sudo grep ocredit /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf ocredit = -1 If the value of "ocredit" is a positive number or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-271637`

### Rule: OL 9 must prevent the use of dictionary words for passwords.

**Rule ID:** `SV-271637r1091623_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If OL 9 allows the user to select passwords based on dictionary words, this increases the chances of password compromise by increasing the opportunity for successful guesses, and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 prevents the use of dictionary words for passwords with the following command: $ grep dictcheck /etc/security/pwquality.conf /etc/pwquality.conf.d/*.conf /etc/security/pwquality.conf:dictcheck=1 If "dictcheck" does not have a value other than "0", or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271638`

### Rule: OL 9 must not have accounts configured with blank or null passwords.

**Rule ID:** `SV-271638r1091626_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log in and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 does not have accounts configured with blank or null passwords with the following command: $ sudo awk -F: '!$2 {print $1}' /etc/shadow If the command returns any results, this is a finding.

## Group: SRG-OS-000114-GPOS-00059

**Group ID:** `V-271639`

### Rule: OL 9 file system automount function must be disabled unless required.

**Rule ID:** `SV-271639r1091629_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. Satisfies: SRG-OS-000114-GPOS-00059, SRG-OS-000378-GPOS-00163</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 file system automount function has been disabled and masked with the following command: $ systemctl is-enabled autofs masked If the returned value is not "masked" and is not documented as operational requirement with the information system security officer (ISSO), this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271640`

### Rule: OL 9 must be configured so that the Network File System (NFS) is configured to use RPCSEC_GSS.

**Rule ID:** `SV-271640r1091632_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When an NFS server is configured to use RPCSEC_SYS, a selected userid and groupid are used to handle requests from the remote user. The userid and groupid could mistakenly or maliciously be set incorrectly. The RPCSEC_GSS method of authentication uses certificates on the server and client systems to authenticate the remote mount request more securely.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If no NFS mounts are configured, this requirement is Not Applicable. Verify that OL 9 has the "sec" option configured for all NFS mounts with the following command: $ cat /etc/fstab | grep nfs 192.168.22.2:/mnt/export /data nfs4 rw,nosuid,nodev,noexec,sync,soft,sec=krb5p:krb5i:krb5 If the system is mounting file systems via NFS and has the sec option without the "krb5:krb5i:krb5p" settings, the "sec" option has the "sys" setting, or the "sec" option is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271641`

### Rule: OL 9 must prevent special devices on file systems that are imported via Network File System (NFS).

**Rule ID:** `SV-271641r1091635_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If no NFS mounts are configured, this requirement is Not Applicable. Verify that OL 9 has the "nodev" option configured for all NFS mounts with the following command: $ cat /etc/fstab | grep nfs 192.168.22.2:/mnt/export /data nfs4 rw,nosuid,nodev,noexec,sync,soft,sec=krb5:krb5i:krb5p If the system is mounting file systems via NFS and the "nodev" option is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271642`

### Rule: OL 9 must prevent code from being executed on file systems that are imported via Network File System (NFS).

**Rule ID:** `SV-271642r1092593_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "noexec" mount option causes the system not to execute binary files. This option must be used for mounting any file system not containing approved binary as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If no NFS mounts are configured, this requirement is Not Applicable. Verify that OL 9 has the "noexec" option configured for all NFS mounts with the following command: $ cat /etc/fstab | grep nfs 192.168.22.2:/mnt/export /data nfs4 rw,nosuid,nodev,noexec,sync,soft,sec=krb5:krb5i:krb5p If the system is mounting file systems via NFS and the "noexec" option is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271643`

### Rule: OL 9 must prevent files with the setuid and setgid bit set from being executed on file systems that are imported via Network File System (NFS).

**Rule ID:** `SV-271643r1091641_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system not to execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If no NFS mounts are configured, this requirement is Not Applicable. Verify that OL 9 has the "nosuid" option configured for all NFS mounts with the following command: $ cat /etc/fstab | grep nfs 192.168.22.2:/mnt/export /data nfs4 rw,nosuid,nodev,noexec,sync,soft,sec=krb5:krb5i:krb5p If the system is mounting file systems via NFS and the "nosuid" option is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271644`

### Rule: OL 9 must prevent code from being executed on file systems that are used with removable media.

**Rule ID:** `SV-271644r1091644_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "noexec" mount option causes the system not to execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 file systems that are used for removable media are mounted with the "noexec" option with the following command: $ more /etc/fstab UUID=2bc871e4-e2a3-4f29-9ece-3be60c835222 /mnt/usbflash vfat noauto,owner,ro,nosuid,nodev,noexec 0 0 If a file system found in "/etc/fstab" refers to removable media and it does not have the "noexec" option set, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271645`

### Rule: OL 9 must prevent special devices on file systems that are used with removable media.

**Rule ID:** `SV-271645r1091647_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system not to interpret character or block special devices. Executing character or blocking special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 file systems that are used for removable media are mounted with the "nodev" option with the following command: $ more /etc/fstab UUID=2bc871e4-e2a3-4f29-9ece-3be60c835222 /mnt/usbflash vfat noauto,owner,ro,nosuid,nodev,noexec 0 0 If a file system found in "/etc/fstab" refers to removable media and it does not have the "nodev" option set, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271646`

### Rule: OL 9 must prevent files with the setuid and setgid bit set from being executed on file systems that are used with removable media.

**Rule ID:** `SV-271646r1091650_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system not to execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 file systems that are used for removable media are mounted with the "nosuid" option with the following command: $ more /etc/fstab UUID=2bc871e4-e2a3-4f29-9ece-3be60c835222 /mnt/usbflash vfat noauto,owner,ro,nosuid,nodev,noexec 0 0 If a file system found in "/etc/fstab" refers to removable media and it does not have the "nosuid" option set, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271647`

### Rule: OL 9 must mount /boot with the nodev option.

**Rule ID:** `SV-271647r1091653_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The only legitimate location for device files is the "/dev" directory located on the root partition. The only exception to this is chroot jails.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /boot with the nodev option. Verify that the "/boot" mount point has the "nodev" option is with the following command: $ mount | grep '\s/boot\s' /dev/sda1 on /boot type xfs (rw,nodev,relatime,seclabel,attr2) If the "/boot" file system does not have the "nodev" option set, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271648`

### Rule: OL 9 must prevent files with the setuid and setgid bit set from being executed on the /boot directory.

**Rule ID:** `SV-271648r1091656_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system not to execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /boot with the nosuid option. Verify that the /boot directory is mounted with the "nosuid" option with the following command: $ mount | grep '\s/boot\s' /dev/sda1 on /boot type xfs (rw,nosuid,relatime,seclabe,attr2,inode64,noquota) If the /boot file system does not have the "nosuid" option set, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271649`

### Rule: OL 9 must prevent files with the setuid and setgid bit set from being executed on the /boot/efi directory.

**Rule ID:** `SV-271649r1091659_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system not to execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For systems that use BIOS, this requirement is Not Applicable. Verify that OL 9 /boot/efi directory is mounted with the "nosuid" option with the following command: $ mount | grep '\s/boot/efi\s' /dev/sda1 on /boot/efi type vfat (rw,nosuid,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=ascii,shortname=winnt,errors=remount-ro) If the /boot/efi file system does not have the "nosuid" option set, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271650`

### Rule: OL 9 must mount /dev/shm with the nodev option.

**Rule ID:** `SV-271650r1091662_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The nodev mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access. The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /dev/shm with the nodev option. Verify "/dev/shm" is mounted with the "nodev" option with the following command: $ mount | grep /dev/shm tmpfs on /dev/shm type tmpfs (rw,nodev,nosuid,noexec,seclabel) If the /dev/shm file system is mounted without the "nodev" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271651`

### Rule: OL 9 must mount /dev/shm with the noexec option.

**Rule ID:** `SV-271651r1091665_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The noexec mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /dev/shm with the noexec option. Verify "/dev/shm" is mounted with the "noexec" option with the following command: $ mount | grep /dev/shm tmpfs on /dev/shm type tmpfs (rw,nodev,nosuid,noexec,seclabel) If the /dev/shm file system is mounted without the "noexec" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271652`

### Rule: OL 9 must mount /dev/shm with the nosuid option.

**Rule ID:** `SV-271652r1094966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /dev/shm with the nosuid option. Verify "/dev/shm" is mounted with the "nosuid" option with the following command: $ mount | grep /dev/shm tmpfs on /dev/shm type tmpfs (rw,nodev,nosuid,noexec,seclabel) If the /dev/shm file system is mounted without the "nosuid" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271653`

### Rule: OL 9 must mount /tmp with the nodev option.

**Rule ID:** `SV-271653r1091671_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access. The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /tmp with the nodev option. Verify "/tmp" is mounted with the "nodev" option: $ mount | grep /tmp /dev/mapper/ol-tmp on /tmp type xfs (rw,nodev,nosuid,noexec,seclabel) If the "/tmp" file system is mounted without the "nodev" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271654`

### Rule: OL 9 must mount /tmp with the noexec option.

**Rule ID:** `SV-271654r1091674_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /tmp with the noexec option. Verify "/tmp" is mounted with the "noexec" option: $ mount | grep /tmp /dev/mapper/ol-tmp on /tmp type xfs (rw,nodev,nosuid,noexec,seclabel) If the "/tmp" file system is mounted without the "noexec" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271655`

### Rule: OL 9 must mount /tmp with the nosuid option.

**Rule ID:** `SV-271655r1091677_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /tmp with the nosuid option. Verify "/tmp" is mounted with the "nosuid" option: $ mount | grep /tmp /dev/mapper/ol-tmp on /tmp type xfs (rw,nodev,nosuid,noexec,seclabel) If the "/tmp" file system is mounted without the "nosuid" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271656`

### Rule: OL 9 must mount /var with the nodev option.

**Rule ID:** `SV-271656r1091680_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access. The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /var with the nodev option. Verify "/var" is mounted with the "nodev" option: $ mount | grep /var /dev/mapper/ol-var on /var type xfs (rw,nodev,nosuid,noexec,seclabel) If the "/var" file system is mounted without the "nodev" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271657`

### Rule: OL 9 must mount /var/log with the nodev option.

**Rule ID:** `SV-271657r1091683_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access. The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /var/log with the nodev option. Verify "/var/log" is mounted with the "nodev" option: $ mount | grep /var/log /dev/mapper/ol-var-log on /var/log type xfs (rw,nodev,nosuid,noexec,seclabel) If the "/var/log" file system is mounted without the "nodev" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271658`

### Rule: OL 9 must mount /var/log with the noexec option.

**Rule ID:** `SV-271658r1091686_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /var/log with the noexec option. Verify "/var/log" is mounted with the "noexec" option: $ mount | grep /var/log /dev/mapper/ol-var-log on /var/log type xfs (rw,nodev,nosuid,noexec,seclabel) If the "/var/log" file system is mounted without the "noexec" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271659`

### Rule: OL 9 must mount /var/log with the nosuid option.

**Rule ID:** `SV-271659r1091689_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /var/log with the nosuid option. Verify "/var/log" is mounted with the "nosuid" option: $ mount | grep /var/log /dev/mapper/ol-var-log on /var/log type xfs (rw,nodev,nosuid,noexec,seclabel) If the "/var/log" file system is mounted without the "nosuid" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271660`

### Rule: OL 9 must mount /var/log/audit with the nodev option.

**Rule ID:** `SV-271660r1091692_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access. The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /var/log/audit with the nodev option. Verify "/var/log/audit" is mounted with the "nodev" option: $ mount | grep /var/log/audit /dev/mapper/ol-var-log-audit on /var/log/audit type xfs (rw,nodev,nosuid,noexec,seclabel) If the "/var/log/audit" file system is mounted without the "nodev" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271661`

### Rule: OL 9 must mount /var/log/audit with the noexec option.

**Rule ID:** `SV-271661r1091695_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /var/log/audit with the noexec option. Verify "/var/log/audit" is mounted with the "noexec" option: $ mount | grep /var/log/audit /dev/mapper/ol-var-log-audit on /var/log/audit type xfs (rw,nodev,nosuid,noexec,seclabel) If the "/var/log/audit" file system is mounted without the "noexec" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271662`

### Rule: OL 9 must mount /var/log/audit with the nosuid option.

**Rule ID:** `SV-271662r1091698_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /var/log/audit with the nosuid option. Verify "/var/log/audit" is mounted with the "nosuid" option: $ mount | grep /var/log/audit /dev/mapper/ol-var-log-audit on /var/log/audit type xfs (rw,nodev,nosuid,noexec,seclabel) If the "/var/log/audit" file system is mounted without the "nosuid" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271663`

### Rule: OL 9 must mount /var/tmp with the nodev option.

**Rule ID:** `SV-271663r1091701_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access. The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /var/tmp with the nodev option. Verify "/var/tmp" is mounted with the "nodev" option: $ mount | grep /var/tmp /dev/mapper/ol-var-tmp on /var/tmp type xfs (rw,nodev,nosuid,noexec,seclabel) If the "/var/tmp" file system is mounted without the "nodev" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271664`

### Rule: OL 9 must mount /var/tmp with the noexec option.

**Rule ID:** `SV-271664r1091704_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /var/tmp with the noexec option. Verify "/var/tmp" is mounted with the "noexec" option: $ mount | grep /var/tmp /dev/mapper/ol-var-tmp on /var/tmp type xfs (rw,nodev,nosuid,noexec,seclabel) If the "/var/tmp" file system is mounted without the "noexec" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271665`

### Rule: OL 9 must mount /var/tmp with the nosuid option.

**Rule ID:** `SV-271665r1091707_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /var/tmp with the nosuid option. Verify "/var/tmp" is mounted with the "nosuid" option: $ mount | grep /var/tmp /dev/mapper/ol-var-tmp on /var/tmp type xfs (rw,nodev,nosuid,noexec,seclabel) If the "/var/tmp" file system is mounted without the "nosuid" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271666`

### Rule: OL 9 must prevent device files from being interpreted on file systems that contain user home directories.

**Rule ID:** `SV-271666r1091710_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access. The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /home with the nodev option. Verify "/home" is mounted with the "nodev" option with the following command: Note: If a separate file system has not been created for the user home directories (user home directories are mounted under "/"), this is automatically a finding, as the "nodev" option cannot be used on the "/" system. $ mount | grep /home tmpfs on /home type tmpfs (rw,nodev,nosuid,noexec,seclabel) If the "/home" file system is mounted without the "nodev" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271667`

### Rule: OL 9 must prevent files with the setuid and setgid bit set from being executed on file systems that contain user home directories.

**Rule ID:** `SV-271667r1091713_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /home with the nosuid option. Verify "/home" is mounted with the "nosuid" option with the following command: Note: If a separate file system has not been created for the user home directories (user home directories are mounted under "/"), this is automatically a finding, as the "nosuid" option cannot be used on the "/" system. $ mount | grep /home tmpfs on /home type tmpfs (rw,nodev,nosuid,noexec,seclabel) If the "/home" file system is mounted without the "nosuid" option, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271668`

### Rule: OL 9 must prevent code from being executed on file systems that contain user home directories.

**Rule ID:** `SV-271668r1091716_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The noexec mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mount /home with the nodexec option. Verify "/home" is mounted with the "noexec" option with the following command: Note: If a separate file system has not been created for the user home directories (user home directories are mounted under "/"), this is automatically a finding, as the "noexec" option cannot be used on the "/" system. $ mount | grep /home tmpfs on /home type xfs (rw,nodev,nosuid,noexec,seclabel) If the "/home" file system is mounted without the "noexec" option, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271669`

### Rule: OL 9 must prevent special devices on nonroot local partitions.

**Rule ID:** `SV-271669r1091719_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access. The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 prevents special devices on nonroot local partitions. Verify all nonroot local partitions are mounted with the "nodev" option with the following command: $ mount | grep '^/dev\S* on /\S' | grep --invert-match 'nodev' If any output is produced, this is a finding.

## Group: SRG-OS-000114-GPOS-00059

**Group ID:** `V-271670`

### Rule: OL 9 must disable the graphical user interface automount function unless required.

**Rule ID:** `SV-271670r1091722_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatically mounting file systems permits easy introduction of unknown devices, thereby facilitating malicious activity. Satisfies: SRG-OS-000114-GPOS-00059, SRG-OS-000378-GPOS-00163</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 disables the graphical user interface automount function with the following command: $ gsettings get org.gnome.desktop.media-handling automount-open false If "automount-open" is set to "true", and is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-271671`

### Rule: OL 9 must disable the graphical user interface autorun function unless required.

**Rule ID:** `SV-271671r1091725_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing autorun commands to execute may introduce malicious code to a system. Configuring this setting prevents autorun commands from executing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 disables the graphical user interface autorun function with the following command: $ gsettings get org.gnome.desktop.media-handling autorun-never true If "autorun-never" is set to "false", and is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271672`

### Rule: OL 9 must disable the user list at logon for graphical user interfaces.

**Rule ID:** `SV-271672r1092631_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Leaving the user list enabled is a security risk since it allows anyone with physical access to the system to enumerate known user accounts without authenticated access to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 disables the user logon list for graphical user interfaces with the following command: $ gsettings get org.gnome.login-screen disable-user-list true If the setting is "false", this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-271673`

### Rule: OL 9 must initiate a session lock for graphical user interfaces when the screensaver is activated.

**Rule ID:** `SV-271673r1091731_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to logout because of the temporary nature of the absence.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 initiates a session lock for graphical user interfaces when the screensaver is activated with the following command: $ gsettings get org.gnome.desktop.screensaver lock-delay uint32 5 If the "uint32" setting is not set to "5" or less, or is missing, this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-271674`

### Rule: OL 9 must automatically lock graphical user sessions after 15 minutes of inactivity.

**Rule ID:** `SV-271674r1091734_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not logout because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, the GNOME desktop can be configured to identify when a user's session has idled and take action to initiate a session lock. Satisfies: SRG-OS-000029-GPOS-00010, SRG-OS-000031-GPOS-00012</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 initiates a session lock after a 15-minute period of inactivity for graphical user interfaces with the following command: $ gsettings get org.gnome.desktop.session idle-delay uint32 900 If "idle-delay" is set to "0" or a value greater than "900", this is a finding.

## Group: SRG-OS-000031-GPOS-00012

**Group ID:** `V-271676`

### Rule: OL 9 must conceal, via the session lock, information previously visible on the display with a publicly viewable image.

**Rule ID:** `SV-271676r1091740_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the screensaver mode to blank-only conceals the contents of the display from passersby.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 configures the screensaver to be blank with the following command: $ gsettings get org.gnome.desktop.screensaver picture-uri If properly configured, the output should be "''". To ensure that users cannot set the screensaver background, run the following: $ grep picture-uri /etc/dconf/db/local.d/locks/* If properly configured, the output should be "/org/gnome/desktop/screensaver/picture-uri". If it is not set or configured properly, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271677`

### Rule: OL 9 must disable the ability of a user to accidentally press Ctrl-Alt-Del and cause a system to shut down or reboot.

**Rule ID:** `SV-271677r1091743_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A locally logged-in user who presses Ctrl-Alt-Del, when at the console, can reboot the system. If accidentally pressed, as could happen in the case of mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 is configured to ignore the Ctrl-Alt-Del sequence in the GNOME desktop with the following command: $ gsettings get org.gnome.settings-daemon.plugins.media-keys logout "['']" If the GNOME desktop is configured to shut down when Ctrl-Alt-Del is pressed, this is a finding.

## Group: SRG-OS-000114-GPOS-00059

**Group ID:** `V-271678`

### Rule: OL 9 must prevent a user from overriding the disabling of the graphical user interface automount function.

**Rule ID:** `SV-271678r1091746_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A nonprivileged account is any operating system account with authorizations of a nonprivileged user. Satisfies: SRG-OS-000114-GPOS-00059, SRG-OS-000378-GPOS-00163</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 disables ability of the user to override the graphical user interface automount setting. Determine which profile the system database is using with the following command: $ grep system-db /etc/dconf/profile/user system-db:local Check that the automount setting is locked from nonprivileged user modification with the following command: Note: The example below is using the database "local" for the system, so the path is "/etc/dconf/db/local.d". This path must be modified if a database other than "local" is being used. $ grep 'automount-open' /etc/dconf/db/local.d/locks/* /org/gnome/desktop/media-handling/automount-open If the command does not return at least the example result, this is a finding.

## Group: SRG-OS-000114-GPOS-00059

**Group ID:** `V-271679`

### Rule: OL 9 must prevent a user from overriding the disabling of the graphical user interface autorun function.

**Rule ID:** `SV-271679r1091749_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., TLS, WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators. Satisfies: SRG-OS-000114-GPOS-00059, SRG-OS-000378-GPOS-00163</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 disables ability of the user to override the graphical user interface autorun setting. Determine which profile the system database is using with the following command: $ grep system-db /etc/dconf/profile/user system-db:local Check that the automount setting is locked from nonprivileged user modification with the following command: Note: The example below is using the database "local" for the system, so the path is "/etc/dconf/db/local.d". This path must be modified if a database other than "local" is being used. $ grep 'autorun-never' /etc/dconf/db/local.d/locks/* /org/gnome/desktop/media-handling/autorun-never If the command does not return at least the example result, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-271680`

### Rule: OL 9 must prevent a user from overriding the banner-message-enable setting for the graphical user interface.

**Rule ID:** `SV-271680r1091752_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. For U.S. government systems, system use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist. Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 prevents a user from overriding settings for graphical user interfaces. Determine which profile the system database is using with the following command: $ grep system-db /etc/dconf/profile/user system-db:local Check that graphical settings are locked from nonprivileged user modification with the following command: Note: The example below is using the database "local" for the system, so the path is "/etc/dconf/db/local.d". This path must be modified if a database other than "local" is being used. $ grep banner-message-enable /etc/dconf/db/local.d/locks/* /org/gnome/login-screen/banner-message-enable If the output is not "/org/gnome/login-screen/banner-message-enable", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-271681`

### Rule: OL 9 must prevent a user from overriding the screensaver lock-enabled setting for the graphical user interface.

**Rule ID:** `SV-271681r1091755_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, operating systems need to be able to identify when a user's session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. Implementing session settings will have little value if a user is able to manipulate these settings from the defaults prescribed in the other requirements of this implementation guide. Satisfies: SRG-OS-000028-GPOS-00009, SRG-OS-000030-GPOS-00011</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 prevents a user from overriding settings for graphical user interfaces. Determine which profile the system database is using with the following command: $ grep system-db /etc/dconf/profile/user system-db:local Check that graphical settings are locked from nonprivileged user modification with the following command: Note: The example below is using the database "local" for the system, so the path is "/etc/dconf/db/local.d". This path must be modified if a database other than "local" is being used. $ grep -i lock-enabled /etc/dconf/db/local.d/locks/* /org/gnome/desktop/screensaver/lock-enabled If the command does not return at least the example result, this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-271682`

### Rule: OL 9 must prevent a user from overriding the session idle-delay setting for the graphical user interface.

**Rule ID:** `SV-271682r1091758_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not logout because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, the GNOME desktop can be configured to identify when a user's session has idled and take action to initiate the session lock. As such, users should not be allowed to change session settings. Satisfies: SRG-OS-000029-GPOS-00010, SRG-OS-000031-GPOS-00012</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 prevents a user from overriding settings for graphical user interfaces. Determine which profile the system database is using with the following command: $ grep system-db /etc/dconf/profile/user system-db:local Check that graphical settings are locked from nonprivileged user modification with the following command: Note: The example below is using the database "local" for the system, so the path is "/etc/dconf/db/local.d". This path must be modified if a database other than "local" is being used. $ grep -i idle /etc/dconf/db/local.d/locks/* /org/gnome/desktop/session/idle-delay If the command does not return at least the example result, this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-271683`

### Rule: OL 9 must prevent a user from overriding the session lock-delay setting for the graphical user interface.

**Rule ID:** `SV-271683r1091761_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not logout because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, the GNOME desktop can be configured to identify when a user's session has idled and take action to initiate the session lock. As such, users should not be allowed to change session settings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 prevents a user from overriding settings for graphical user interfaces. Determine which profile the system database is using with the following command: $ grep system-db /etc/dconf/profile/user system-db:local Check that graphical settings are locked from nonprivileged user modification with the following command: Note: The example below is using the database "local" for the system, so the path is "/etc/dconf/db/local.d". This path must be modified if a database other than "local" is being used. $ grep -i lock-delay /etc/dconf/db/local.d/locks/* /org/gnome/desktop/screensaver/lock-delay If the command does not return at least the example result, this is a finding.

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-271684`

### Rule: OL 9 must prevent a user from overriding the disabling of the graphical user smart card removal action.

**Rule ID:** `SV-271684r1091764_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Rather than be forced to wait for a period of time to expire before the user session can be locked, OL 9 must provide users with the ability to manually invoke a session lock so users can secure their session if it is necessary to temporarily vacate the immediate physical vicinity. Satisfies: SRG-OS-000028-GPOS-00009, SRG-OS-000030-GPOS-00011</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 disables ability of the user to override the smart card removal action setting. Determine which profile the system database is using with the following command: $ grep system-db /etc/dconf/profile/user system-db:local Check that the removal action setting is locked from nonprivileged user modification with the following command: Note: The example below is using the database "local" for the system, so the path is "/etc/dconf/db/local.d". This path must be modified if a database other than "local" is being used. $ grep 'removal-action' /etc/dconf/db/local.d/locks/* /org/gnome/settings-daemon/peripherals/smartcard/removal-action If the command does not return at least the example result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271685`

### Rule: OL 9 must disable the ability of a user to restart the system from the login screen.

**Rule ID:** `SV-271685r1091767_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A user who is at the console can reboot the system at the login screen. If restart or shutdown buttons are pressed at the login screen, this can create the risk of short-term loss of availability of systems due to reboot.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 disables a user's ability to restart the system with the following command: $ grep -R disable-restart-buttons /etc/dconf/db/* /etc/dconf/db/distro.d/20-authselect:disable-restart-buttons='true' If the "disable-restart-button" setting is not set to "true", is missing or commented out from the dconf database files, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271686`

### Rule: OL 9 must prevent a user from overriding the disable-restart-buttons setting for the graphical user interface.

**Rule ID:** `SV-271686r1091770_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A user who is at the console can reboot the system at the login screen. If restart or shutdown buttons are pressed at the login screen, this can create the risk of short-term loss of availability of systems due to reboot.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 prevents a user from overriding the disable-restart-buttons setting for graphical user interfaces. Determine which profile the system database is using with the following command: $ grep system-db /etc/dconf/profile/user system-db:local Check that graphical settings are locked from nonprivileged user modification with the following command: Note: The example below is using the database "local" for the system, so the path is "/etc/dconf/db/local.d". This path must be modified if a database other than "local" is being used. $ grep disable-restart-buttons /etc/dconf/db/local.d/locks/* /org/gnome/login-screen/disable-restart-buttons If the command does not return at least the example result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271687`

### Rule: OL 9 must prevent a user from overriding the Ctrl-Alt-Del sequence settings for the graphical user interface.

**Rule ID:** `SV-271687r1091773_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A locally logged-in user who presses Ctrl-Alt-Del, when at the console, can reboot the system. If accidentally pressed, as could happen in the case of mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 users cannot enable the Ctrl-Alt-Del sequence in the GNOME desktop with the following command: $ grep logout /etc/dconf/db/local.d/locks/* /org/gnome/settings-daemon/plugins/media-keys/logout If the output is not "/org/gnome/settings-daemon/plugins/media-keys/logout", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-271688`

### Rule: OL 9 must be configured to enable the display of the Standard Mandatory DOD Notice and Consent Banner before granting local or remote access to the system via a graphical user logon.

**Rule ID:** `SV-271688r1091776_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. For U.S. government systems, system use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist. Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 displays a banner before granting access to the operating system via a graphical user logon. Determine if the operating system displays a banner at the logon screen with the following command: $ gsettings get org.gnome.login-screen banner-message-enable true If the result is "false", this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-271689`

### Rule: OL 9 must display the Standard Mandatory DOD Notice and Consent Banner before granting local or remote access to the system via a graphical user logon.

**Rule ID:** `SV-271689r1091779_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the operating system via a graphical user logon. Check that the operating system displays the exact Standard Mandatory DOD Notice and Consent Banner text with the command: $ gsettings get org.gnome.login-screen banner-message-text banner-message-text= 'You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only.\nBy using this IS (which includes any device attached to this IS), you consent to the following conditions:\n-The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations.\n-At any time, the USG may inspect and seize data stored on this IS.\n-Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose.\n-This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy.\n-Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details.' Note: The "\n " characters are for formatting only. They will not be displayed on the graphical interface. If the banner does not match the Standard Mandatory DOD Notice and Consent Banner exactly, this is a finding.

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-271690`

### Rule: OL 9 must be able to directly initiate a session lock for all connection types using smart card when the smart card is removed.

**Rule ID:** `SV-271690r1092634_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Rather than be forced to wait for a period of time to expire before the user session can be locked, OL 9 needs to provide users with the ability to manually invoke a session lock so users can secure their session if it is necessary to temporarily vacate the immediate physical vicinity. Satisfies: SRG-OS-000028-GPOS-00009, SRG-OS-000030-GPOS-00011</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 enables a user's session lock until that user reestablishes access using established identification and authentication procedures with the following command: $ grep -R removal-action /etc/dconf/db/* /etc/dconf/db/distro.d/20-authselect:removal-action='lock-screen' If the "removal-action='lock-screen'" setting is missing or commented out from the dconf database files, this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-271691`

### Rule: OL 9 must not allow unattended or automatic logon via the graphical user interface.

**Rule ID:** `SV-271691r1091785_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Failure to restrict system access to authenticated users negatively impacts operating system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 does not allow an unattended or automatic logon to the system via a graphical user interface. Check for the value of the "AutomaticLoginEnable" in the "/etc/gdm/custom.conf" file with the following command: $ grep -i automaticlogin /etc/gdm/custom.conf [daemon] AutomaticLoginEnable=false If the value of "AutomaticLoginEnable" is not set to "false", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271692`

### Rule: OL 9 effective dconf policy must match the policy keyfiles.

**Rule ID:** `SV-271692r1091788_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unlike text-based keyfiles, the binary database is impossible to check through most automated and all manual means; therefore, to evaluate dconf configuration, both have to be true at the same time - configuration files have to be compliant, and the database needs to be more recent than those keyfiles, which gives confidence that it reflects them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement assumes the use of the OL 9 default graphical user interface—the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that OL 9 effective dconf policy matches the policy keyfiles. Check the last modification time of the local databases, comparing it to the last modification time of the related keyfiles. The following command will check every dconf database and compare its modification time to the related system keyfiles: $ function dconf_needs_update { for db in $(find /etc/dconf/db -maxdepth 1 -type f); do db_mtime=$(stat -c %Y "$db"); keyfile_mtime=$(stat -c %Y "$db".d/* | sort -n | tail -1); if [ -n "$db_mtime" ] && [ -n "$keyfile_mtime" ] && [ "$db_mtime" -lt "$keyfile_mtime" ]; then echo "$db needs update"; return 1; fi; done; }; dconf_needs_update If the command has any output, then a dconf database needs to be updated, and this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271693`

### Rule: OL 9 must define default permissions for the bash shell.

**Rule ID:** `SV-271693r1091791_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The umask controls the default access mode assigned to newly created files. A umask of 077 limits new files to mode 600 or less permissive. Although umask can be represented as a four-digit number, the first digit representing special access modes is typically ignored or required to be "0". This requirement applies to the globally configured system defaults and the local interactive user defaults for each account on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 "umask" setting is configured correctly in the "/etc/bashrc" file with the following command: Note: If the value of the "umask" parameter is set to "000" "/etc/bashrc" file, the severity of this requirement is raised to a CAT I. $ grep umask /etc/bashrc umask 077 umask 077 If the value for the "umask" parameter is not "077", or the "umask" parameter is missing or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271694`

### Rule: OL 9 must define default permissions for the c shell.

**Rule ID:** `SV-271694r1091794_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The umask controls the default access mode assigned to newly created files. A umask of 077 limits new files to mode 600 or less permissive. Although umask can be represented as a four-digit number, the first digit representing special access modes is typically ignored or required to be "0". This requirement applies to the globally configured system defaults and the local interactive user defaults for each account on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 "umask" setting is configured correctly in the "/etc/csh.cshrc" file with the following command: Note: If the value of the "umask" parameter is set to "000" "/etc/csh.cshrc" file, the severity of this requirement is raised to a CAT I. $ grep umask /etc/csh.cshrc umask 077 umask 077 If the value for the "umask" parameter is not "077", or the "umask" parameter is missing or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271695`

### Rule: OL 9 must define default permissions for the system default profile.

**Rule ID:** `SV-271695r1091797_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The umask controls the default access mode assigned to newly created files. A umask of 077 limits new files to mode 600 or less permissive. Although umask can be represented as a four-digit number, the first digit representing special access modes is typically ignored or required to be "0". This requirement applies to the globally configured system defaults and the local interactive user defaults for each account on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 "umask" setting is configured correctly in the "/etc/profile" file with the following command: Note: If the value of the "umask" parameter is set to "000" "/etc/profile" file, the severity of this requirement is raised to a CAT I. $ grep umask /etc/profile umask 077 If the value for the "umask" parameter is not "077", or the "umask" parameter is missing or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-271696`

### Rule: OL 9 must define default permissions for all authenticated users in such a way that the user can only read and modify their own files.

**Rule ID:** `SV-271696r1091800_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the most restrictive default permissions ensures that when new accounts are created, they do not have unnecessary access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 defines default permissions for all authenticated users in such a way that the user can only read and modify their own files with the following command: Note: If the value of the "UMASK" parameter is set to "000" in "/etc/login.defs" file, the severity of this requirement is raised to a CAT I. $ grep -i umask /etc/login.defs UMASK 077 If the value for the "UMASK" parameter is not "077", or the "UMASK" parameter is missing or is commented out, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-271697`

### Rule: OL 9 must disable the chrony daemon from acting as a server.

**Rule ID:** `SV-271697r1091803_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Minimizing the exposure of the server functionality of the chrony daemon diminishes the attack surface. Satisfies: SRG-OS-000096-GPOS-00050, SRG-OS-000095-GPOS-00049</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 disables the chrony daemon from acting as a server with the following command: $ grep -w port /etc/chrony.conf port 0 If the "port" option is not set to "0", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-271698`

### Rule: OL 9 must disable network management of the chrony daemon.

**Rule ID:** `SV-271698r1091806_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Not exposing the management interface of the chrony daemon on the network diminishes the attack space. Satisfies: SRG-OS-000096-GPOS-00050, SRG-OS-000095-GPOS-00049</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 disables network management of the chrony daemon with the following command: $ grep -w cmdport /etc/chrony.conf cmdport 0 If the "cmdport" option is not set to "0", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-271699`

### Rule: OL 9 must securely compare internal information system clocks at least every 24 hours.

**Rule ID:** `SV-271699r1091809_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Depending on the infrastructure being used the "pool" directive may not be supported. Authoritative time sources include the United States Naval Observatory (USNO) time servers, a time server designated for the appropriate DOD network (NIPRNet/SIPRNet), and/or the Global Positioning System (GPS). Satisfies: SRG-OS-000355-GPOS-00143, SRG-OS-000356-GPOS-00144, SRG-OS-000359-GPOS-00146</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 securely compares internal information system clocks at least every 24 hours with an NTP server with the following command: $ grep maxpoll /etc/chrony.conf server 0.us.pool.ntp.mil iburst maxpoll 16 If the "maxpoll" option is set to a number greater than 16 or the line is commented out, this is a finding. Verify the "chrony.conf" file is configured to an authoritative DOD time source by running the following command: $ grep -i server /etc/chrony.conf server 0.us.pool.ntp.mil If the parameter "server" is not set or is not set to an authoritative DOD time source, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-271700`

### Rule: OL 9 must enable Linux audit logging for the USBGuard daemon.

**Rule ID:** `SV-271700r1091812_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. If auditing is enabled late in the startup process, the actions of some startup processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DOD has defined the list of events for which OL 9 will provide an audit record generation capability as the following: 1. Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2. Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3. All account creations, modifications, disabling, and terminations; and 4. All kernel module load, unload, and restart actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 Linux Audit logging is enabled for the USBGuard daemon with the following command: $ sudo grep AuditBackend /etc/usbguard/usbguard-daemon.conf AuditBackend=LinuxAudit If "AuditBackend" is not set to "LinuxAudit", this is a finding.

## Group: SRG-OS-000378-GPOS-00163

**Group ID:** `V-271701`

### Rule: OL 9 must block unauthorized peripherals before establishing a connection.

**Rule ID:** `SV-271701r1091815_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The USBguard-daemon is the main component of the USBGuard software framework. It runs as a service in the background and enforces the USB device authorization policy for all USB devices. The policy is defined by a set of rules using a rule language described in the usbguard-rules.conf file. The policy and the authorization state of USB devices can be modified during runtime using the usbguard tool. The system administrator (SA) must work with the site information system security officer (ISSO) to determine a list of authorized peripherals and establish rules within the USBGuard software framework to allow only authorized devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 USBGuard has a policy configured with the following command: $ usbguard list-rules allow id 1d6b:0001 serial If the command does not return results or an error is returned, ask the SA to indicate how unauthorized peripherals are being blocked. If there is no evidence that unauthorized peripherals are being blocked before establishing a connection, this is a finding.

## Group: SRG-OS-000690-GPOS-00140

**Group ID:** `V-271702`

### Rule: OL 9 must disable automatic mounting of Universal Serial Bus (USB) mass storage driver.

**Rule ID:** `SV-271702r1091818_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Peripherals include, but are not limited to, such devices as flash drives, external storage, and printers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 disables automatic mounting of the USB storage kernel module with the following command: $ grep usb-storage /etc/modprobe.d/* | grep "/bin/true" install usb-storage /bin/true If the command does not return any output, or the line is commented out, this is a finding. Verify the operating system disables the ability to use USB mass storage device. $ grep usb-storage /etc/modprobe.d/* | grep -i "blacklist" blacklist usb-storage If the command does not return any output, or the line is commented out, this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-271703`

### Rule: OL 9 must log SSH connection attempts and failures to the server.

**Rule ID:** `SV-271703r1091821_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH provides several logging levels with varying amounts of verbosity. "DEBUG" is specifically not recommended other than strictly for debugging SSH communications since it provides so much data that it is difficult to identify important security information. "INFO" or "VERBOSE" level is the basic level that only records login activity of SSH users. In many situations, such as Incident Response, it is important to determine when a particular user was active on a system. The logout record can eliminate those users who disconnected, which helps narrow the field.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 logs SSH connection attempts and failures to the server. Check what the SSH daemon's "LogLevel" option is set to with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*loglevel' LogLevel VERBOSE If a value of "VERBOSE" is not returned, the line is commented out, or is missing, this is a finding.

## Group: SRG-OS-000364-GPOS-00151

**Group ID:** `V-271704`

### Rule: OL 9 SSH daemon must not allow Generic Security Service Application Program Interface (GSSAPI) authentication.

**Rule ID:** `SV-271704r1091824_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>GSSAPI authentication is used to provide additional authentication mechanisms to applications. Allowing GSSAPI authentication through SSH exposes the system's GSSAPI to remote hosts, increasing the attack surface of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 SSH daemon does not allow GSSAPI authentication with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*gssapiauthentication' GSSAPIAuthentication no If the value is returned as "yes", the returned line is commented out, no output is returned, and the use of GSSAPI authentication has not been documented with the information system security officer (ISSO), this is a finding.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-271705`

### Rule: OL 9 must force a frequent session key renegotiation for SSH connections to the server.

**Rule ID:** `SV-271705r1091827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. Session key regeneration limits the chances of a session key becoming compromised. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000033-GPOS-00014, SRG-OS-000424-GPOS-00188</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 SSH server is configured to force frequent session key renegotiation with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*rekeylimit' RekeyLimit 1G 1h If "RekeyLimit" does not have a maximum data amount and maximum time defined, is missing or commented out, this is a finding.

## Group: SRG-OS-000106-GPOS-00053

**Group ID:** `V-271706`

### Rule: OL 9 SSHD must not allow blank passwords.

**Rule ID:** `SV-271706r1091830_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log on and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 remote access using SSH prevents logging on with a blank password with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*permitemptypasswords' PermitEmptyPasswords no If the "PermitEmptyPasswords" keyword is set to "yes", is missing, or is commented out, this is a finding.

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-271707`

### Rule: OL 9 must enable the Pluggable Authentication Module (PAM) interface for SSHD.

**Rule ID:** `SV-271707r1091833_rule`
**Severity:** high

**Description:**
<VulnDiscussion>When UsePAM is set to "yes", PAM runs through account and session types properly. This is important when restricted access to services based off of IP, time, or other factors of the account is needed. Additionally, this ensures users can inherit certain environment variables on login or disallow access to the server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 SSHD is configured to allow for the UsePAM interface with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*usepam' UsePAM yes If the "UsePAM" keyword is set to "no", is missing, or is commented out, this is a finding.

## Group: SRG-OS-000109-GPOS-00056

**Group ID:** `V-271708`

### Rule: OL 9 must not permit direct logons to the root account using remote access via SSH.

**Rule ID:** `SV-271708r1092594_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Even though the communications channel may be encrypted, an additional layer of security is gained by extending the policy of not logging directly on as root. In addition, logging in with a user-specific account provides individual accountability of actions performed on the system and also helps to minimize direct attack attempts on root's password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 remote access using SSH prevents users from logging on directly as "root" with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*permitrootlogin' PermitRootLogin no If the "PermitRootLogin" keyword is set to "yes", is missing, or is commented out, this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-271709`

### Rule: OL 9 must be configured so that all network connections associated with SSH traffic terminate after becoming unresponsive.

**Rule ID:** `SV-271709r1091839_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an unresponsive SSH session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle SSH session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level and deallocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean the operating system terminates all sessions or network access; it only ends the unresponsive session and releases the resources associated with that session. OL 9 uses /etc/ssh/sshd_config for configurations of OpenSSH. Within the sshd_config, the product of the values of "ClientAliveInterval" and "ClientAliveCountMax" are used to establish the inactivity threshold. The "ClientAliveInterval" is a timeout interval in seconds, after which if no data has been received from the client, SSHD will send a message through the encrypted channel to request a response from the client. The "ClientAliveCountMax" is the number of client alive messages that may be sent without SSHD receiving any messages back from the client. If this threshold is met, sshd will disconnect the client. For more information on these settings and others, refer to the sshd_config man pages. Satisfies: SRG-OS-000163-GPOS-00072, SRG-OS-000279-GPOS-00109</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured so that all network connections associated with SSH traffic terminate after becoming unresponsive. Verify that the "ClientAliveCountMax" is set to "1" by performing the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*clientalivecountmax' ClientAliveCountMax 1 If "ClientAliveCountMax" does not exist, is not set to a value of "1" in "/etc/ssh/sshd_config", or is commented out, this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-271710`

### Rule: OL 9 must be configured so that all network connections associated with SSH traffic are terminated after 10 minutes of becoming unresponsive.

**Rule ID:** `SV-271710r1092596_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an unresponsive SSH session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle SSH session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level and deallocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean the operating system terminates all sessions or network access; it only ends the unresponsive session and releases the resources associated with that session. OL 9 uses /etc/ssh/sshd_config for configurations of OpenSSH. Within the sshd_config, the product of the values of "ClientAliveInterval" and "ClientAliveCountMax" are used to establish the inactivity threshold. The "ClientAliveInterval" is a timeout interval in seconds, after which if no data has been received from the client, SSHD will send a message through the encrypted channel to request a response from the client. The "ClientAliveCountMax" is the number of client alive messages that may be sent without SSHD receiving any messages back from the client. If this threshold is met, SSHD will disconnect the client. For more information on these settings and others, refer to the sshd_config man pages. Satisfies: SRG-OS-000163-GPOS-00072, SRG-OS-000279-GPOS-00109, SRG-OS-000395-GPOS-00175</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured so that all network connections associated with SSH traffic are terminated after 10 minutes of becoming unresponsive. Verify that the "ClientAliveInterval" variable is set to a value of "600" or less by performing the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*clientaliveinterval' ClientAliveInterval 600 If "ClientAliveInterval" does not exist, does not have a value of "600" or less in "/etc/ssh/sshd_config", or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271711`

### Rule: OL 9 SSH daemon must not allow rhosts authentication.

**Rule ID:** `SV-271711r1091845_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH trust relationships mean a compromise on one host can allow an attacker to move trivially to other hosts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 SSH daemon does not allow rhosts authentication with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*ignorerhosts' IgnoreRhosts yes If the value is returned as "no", the returned line is commented out, or no output is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271712`

### Rule: OL 9 SSH daemon must not allow known hosts authentication.

**Rule ID:** `SV-271712r1091848_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the IgnoreUserKnownHosts setting for the SSH daemon provides additional assurance that remote login via SSH will require a password, even in the event of misconfiguration elsewhere.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 SSH daemon does not allow known hosts authentication with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*ignoreuserknownhosts' IgnoreUserKnownHosts yes If the value is returned as "no", the returned line is commented out, or no output is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271713`

### Rule: OL 9 SSH daemon must disable remote X connections for interactive users.

**Rule ID:** `SV-271713r1091851_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When X11 forwarding is enabled, there may be additional exposure to the server and client displays if the SSHD proxy display is configured to listen on the wildcard address. By default, SSHD binds the forwarding server to the loopback address and sets the hostname part of the DISPLAY environment variable to localhost. This prevents remote hosts from connecting to the proxy display.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 SSH daemon does not allow X11Forwarding with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*x11forwarding' X11forwarding no If the value is returned as "yes", the returned line is commented out, or no output is returned, and X11 forwarding is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271714`

### Rule: OL 9 SSH daemon must perform strict mode checking of home directory configuration files.

**Rule ID:** `SV-271714r1091854_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If other users have access to modify user-specific SSH configuration files, they may be able to log into the system as another user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 SSH daemon performs strict mode checking of home directory configuration files with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*strictmodes' StrictModes yes If the "StrictModes" keyword is set to "no", the returned line is commented out, or no output is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271715`

### Rule: OL 9 SSH daemon must display the date and time of the last successful account logon upon an SSH logon.

**Rule ID:** `SV-271715r1091857_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Providing users feedback on when account accesses last occurred facilitates user recognition and reporting of unauthorized account use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 SSH daemon provides users with feedback on when account accesses last occurred with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*printlastlog' PrintLastLog yes If the "PrintLastLog" keyword is set to "no", the returned line is commented out, or no output is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271716`

### Rule: OL 9 SSH daemon must prevent remote hosts from connecting to the proxy display.

**Rule ID:** `SV-271716r1091860_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When X11 forwarding is enabled, there may be additional exposure to the server and client displays if the SSHD proxy display is configured to listen on the wildcard address. By default, SSHD binds the forwarding server to the loopback address and sets the hostname part of the "DISPLAY" environment variable to localhost. This prevents remote hosts from connecting to the proxy display.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 SSH daemon prevents remote hosts from connecting to the proxy display with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*x11uselocalhost' X11UseLocalhost yes If the "X11UseLocalhost" keyword is set to "no", is missing, or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271717`

### Rule: OL 9 SSH daemon must not allow compression or must only allow compression after successful authentication.

**Rule ID:** `SV-271717r1091863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If compression is allowed in an SSH connection prior to authentication, vulnerabilities in the compression software could result in compromise of the system from an unauthenticated connection, potentially with root privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 SSH daemon performs compression after a user successfully authenticates with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*compression' Compression delayed If the "Compression" keyword is set to "yes", is missing, or the returned line is commented out, this is a finding.

## Group: SRG-OS-000364-GPOS-00151

**Group ID:** `V-271718`

### Rule: OL 9 SSH daemon must not allow Kerberos authentication.

**Rule ID:** `SV-271718r1091866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kerberos authentication for SSH is often implemented using Generic Security Service Application Program Interface (GSSAPI). If Kerberos is enabled through SSH, the SSH daemon provides a means of access to the system's Kerberos implementation. Vulnerabilities in the system's Kerberos implementations may be subject to exploitation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 SSH daemon does not allow Kerberos authentication with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*kerberosauthentication' KerberosAuthentication no If the value is returned as "yes", the returned line is commented out, no output is returned, and the use of Kerberos authentication has not been documented with the information system security officer (ISSO), this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-271719`

### Rule: OL 9 must not allow a noncertificate trusted host SSH logon to the system.

**Rule ID:** `SV-271719r1091869_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH trust relationships mean a compromise on one host can allow an attacker to move trivially to other hosts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 does not allow a noncertificate trusted host SSH logon to the system with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*hostbasedauthentication' HostbasedAuthentication no If the "HostbasedAuthentication" keyword is not set to "no", is missing, or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-271720`

### Rule: OL 9 must not allow users to override SSH environment variables.

**Rule ID:** `SV-271720r1091872_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH environment options potentially allow users to bypass access restriction in some configurations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 does not allow users to override SSH environment variables. Verify that unattended or automatic logon via SSH is disabled with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*permituserenvironment' PermitUserEnvironment no If "PermitUserEnvironment" is set to "yes", is missing completely, or is commented out, this is a finding.

## Group: SRG-OS-000105-GPOS-00052

**Group ID:** `V-271721`

### Rule: OL 9 SSHD must accept public key authentication.

**Rule ID:** `SV-271721r1091875_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. A privileged account is defined as an information system account with authorizations of a privileged user. A DOD CAC with DOD-approved PKI is an example of multifactor authentication. Satisfies: SRG-OS-000105-GPOS-00052, SRG-OS-000106-GPOS-00053, SRG-OS-000107-GPOS-00054, SRG-OS-000108-GPOS-00055</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 SSH daemon accepts public key encryption with the following command: $ sudo grep -i PubkeyAuthentication /etc/ssh/sshd_config PubkeyAuthentication yes If "PubkeyAuthentication" is set to no, the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271722`

### Rule: OL 9 must require reauthentication when using the "sudo" command.

**Rule ID:** `SV-271722r1091878_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the organization requires the user to reauthenticate when using the "sudo" command. If the value is set to an integer less than "0", the user's time stamp will not expire and the user will not have to reauthenticate for privileged actions until the user's session is terminated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 requires reauthentication when using the "sudo" command to elevate privileges with the following command: $ sudo grep -i 'timestamp_timeout' /etc/sudoers /etc/sudoers.d/* /etc/sudoers:Defaults timestamp_timeout=0 If results are returned from more than one file location, this is a finding. If "timestamp_timeout" is set to a negative number, is commented out, or no results are returned, this is a finding.

## Group: SRG-OS-000312-GPOS-00123

**Group ID:** `V-271723`

### Rule: OL 9 must restrict the use of the su command.

**Rule ID:** `SV-271723r1091881_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The su program allows to run commands with a substitute user and group ID. It is commonly used to run commands as the root user. Limiting access to such commands is considered a good security practice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 requires uses to be members of the "wheel" group with the following command: $ grep pam_wheel /etc/pam.d/su auth required pam_wheel.so use_uid If a line for "pam_wheel.so" does not exist, or is commented out, this is a finding.

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-271724`

### Rule: OL 9 must require users to reauthenticate for privilege escalation.

**Rule ID:** `SV-271724r1091884_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical that the user reauthenticate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 requires users to reauthenticate for privilege escalation. Verify that "/etc/sudoers" has no occurrences of "!authenticate" with the following command: $ sudo grep -ri '!authenticate' /etc/sudoers /etc/sudoers.d/* If any occurrences of "!authenticate" are returned, this is a finding.

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-271725`

### Rule: OL 9 must require users to provide a password for privilege escalation.

**Rule ID:** `SV-271725r1091887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical that the user reauthenticate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 requires users to provide a password for privilege escalation. Verify that "/etc/sudoers" has no occurrences of "NOPASSWD" with the following command: $ sudo grep -ri nopasswd /etc/sudoers /etc/sudoers.d/* If any occurrences of "NOPASSWD" are returned, this is a finding.

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-271726`

### Rule: OL 9 must not be configured to bypass password requirements for privilege escalation.

**Rule ID:** `SV-271726r1091890_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the user reauthenticate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is not configured to bypass password requirements for privilege escalation with the following command: $ grep pam_succeed_if /etc/pam.d/sudo If any occurrences of "pam_succeed_if" are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271727`

### Rule: OL 9 must disable the use of user namespaces.

**Rule ID:** `SV-271727r1091893_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User namespaces are used primarily for Linux containers. The value "0" disallows the use of user namespaces.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: User namespaces are used primarily for Linux containers. If containers are in use, this requirement is Not Applicable. Verify that OL 9 disables the use of user namespaces with the following commands: $ sysctl user.max_user_namespaces user.max_user_namespaces = 0 If the returned line does not have a value of "0", or a line is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271728`

### Rule: OL 9 must disable the kernel.core_pattern.

**Rule ID:** `SV-271728r1091896_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers trying to debug problems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 disables storing core dumps with the following commands: $ sysctl kernel.core_pattern kernel.core_pattern = |/bin/false If the returned line does not have a value of "|/bin/false", or a line is not returned and the need for core dumps is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271729`

### Rule: OL 9 must disable core dump backtraces.

**Rule ID:** `SV-271729r1091899_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers or system operators trying to debug problems. Enabling core dumps on production systems is not recommended; however, there may be overriding operational requirements to enable advanced debugging. Permitting temporary enablement of core dumps during such situations must be reviewed through local needs and policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 disables core dump backtraces by issuing the following command: $ grep -i process /etc/systemd/coredump.conf ProcessSizeMax=0 If the "ProcessSizeMax" item is missing, commented out, or the value is anything other than "0" and the need for core dumps is not documented with the information system security officer (ISSO) as an operational requirement for all domains that have the "core" item assigned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271730`

### Rule: OL 9 must disable storing core dumps.

**Rule ID:** `SV-271730r1091902_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers or system operators trying to debug problems. Enabling core dumps on production systems is not recommended; however, there may be overriding operational requirements to enable advanced debugging. Permitting temporary enablement of core dumps during such situations must be reviewed through local needs and policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 disables storing core dumps for all users by issuing the following command: $ grep -i storage /etc/systemd/coredump.conf Storage=none If the "Storage" item is missing, commented out, or the value is anything other than "none" and the need for core dumps is not documented with the information system security officer (ISSO) as an operational requirement for all domains that have the "core" item assigned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271731`

### Rule: OL 9 must disable core dumps for all users.

**Rule ID:** `SV-271731r1091905_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers trying to debug problems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 disables core dumps for all users by issuing the following command: $ grep -r -s core /etc/security/limits.conf /etc/security/limits.d/*.conf /etc/security/limits.conf:* hard core 0 This can be set as a global domain (with the * wildcard) but may be set differently for multiple domains. If the "core" item is missing, commented out, or the value is anything other than "0" and the need for core dumps is not documented with the information system security officer (ISSO) as an operational requirement for all domains that have the "core" item assigned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271732`

### Rule: OL 9 must disable acquiring, saving, and processing core dumps.

**Rule ID:** `SV-271732r1091908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers trying to debug problems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is not configured to acquire, save, or process core dumps with the following command: $ systemctl status systemd-coredump.socket systemd-coredump.socket Loaded: masked (Reason: Unit systemd-coredump.socket is masked.) Active: inactive (dead) If the "systemd-coredump.socket" is loaded and not masked and the need for core dumps is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271733`

### Rule: OL 9 must be configured so that the kdump service is disabled.

**Rule ID:** `SV-271733r1092598_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kernel core dumps may contain the full contents of system memory at the time of the crash. Kernel core dumps consume a considerable amount of disk space and may result in denial of service by exhausting the available space on the target file system partition. Unless the system is used for kernel development or testing, there is little need to run the kdump service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 kdump service is disabled or masked in system boot configuration with the following command: $ systemctl is-enabled kdump disabled (or masked) Verify that the kdump service is not active (i.e., not running) through current runtime configuration with the following command: $ systemctl is-active kdump inactive Verify that the kdump service is masked with the following command: $ systemctl show kdump | grep "LoadState\|UnitFileState" LoadState=masked UnitFileState=masked If the "kdump" service is loaded or active, and is not masked, this is a finding.

## Group: SRG-OS-000433-GPOS-00192

**Group ID:** `V-271734`

### Rule: OL 9 must clear SLUB/SLAB objects to prevent use-after-free attacks.

**Rule ID:** `SV-271734r1091914_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in nonexecutable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can be either hardware-enforced or software-enforced with hardware providing the greater strength of mechanism. Poisoning writes an arbitrary value to freed pages, so any modification or reference to that page after being freed or before being initialized will be detected and prevented. This prevents many types of use-after-free vulnerabilities at little performance cost. Also prevents leak of data and detection of corrupted memory. SLAB objects are blocks of physically contiguous memory. SLUB is the unqueued SLAB allocator. Satisfies: SRG-OS-000433-GPOS-00192, SRG-OS-000134-GPOS-00068</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 GRUB 2 is configured to enable poisoning of SLUB/SLAB objects to mitigate use-after-free vulnerabilities with the following commands: Check that the current GRUB 2 configuration has poisoning of SLUB/SLAB objects enabled: $ sudo grubby --info=ALL | grep args | grep -v 'slub_debug=P' If any output is returned, this is a finding. Check that poisoning of SLUB/SLAB objects is enabled by default to persist in kernel updates: $ sudo grep slub_debug /etc/default/grub GRUB_CMDLINE_LINUX="slub_debug=P" If "slub_debug" is not set to "P", is missing or commented out, this is a finding.

## Group: SRG-OS-000433-GPOS-00193

**Group ID:** `V-271735`

### Rule: OL 9 must enable mitigations against processor-based vulnerabilities.

**Rule ID:** `SV-271735r1091917_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Kernel page-table isolation is a kernel feature that mitigates the Meltdown security vulnerability and hardens the kernel against attempts to bypass kernel address space layout randomization (KASLR). Satisfies: SRG-OS-000433-GPOS-00193, SRG-OS-000095-GPOS-00049</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 enables kernel page-table isolation with the following command: $ sudo grubby --info=ALL | grep pti args="ro crashkernel=auto resume=/dev/mapper/ol-swap rd.lvm.lv=ol/root rd.lvm.lv=ol/swap rhgb quiet fips=1 audit=1 audit_backlog_limit=8192 pti=on If the "pti" entry does not equal "on", or is missing, this is a finding. Check that kernel page-table isolation is enabled by default to persist in kernel updates: $ sudo grep pti /etc/default/grub GRUB_CMDLINE_LINUX="pti=on" If "pti" is not set to "on", is missing or commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271736`

### Rule: OL 9 must disable the ability of systemd to spawn an interactive boot process.

**Rule ID:** `SV-271736r1091920_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using interactive or recovery boot, the console user could disable auditing, firewalls, or other services, weakening system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 GRUB 2 is configured to disable interactive boot. Check that the current GRUB 2 configuration disables the ability of systemd to spawn an interactive boot process with the following command: $ sudo grubby --info=ALL | grep args | grep 'systemd.confirm_spawn' If any output is returned, this is a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-271737`

### Rule: OL 9 must disable virtual system calls.

**Rule ID:** `SV-271737r1094967_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System calls are special routines in the Linux kernel, which userspace applications ask to do privileged tasks. Invoking a system call is an expensive operation because the processor must interrupt the currently executing task and switch context to kernel mode and then back to userspace after the system call completes. Virtual system calls map into user space a page that contains some variables and the implementation of some system calls. This allows the system calls to be executed in userspace to alleviate the context switching expense. Virtual system calls provide an opportunity of attack for a user who has control of the return instruction pointer. Disabling virtual system calls help to prevent return-oriented programming (ROP) attacks via buffer overflows and overruns. If the system intends to run containers based on OL 6 components, virtual system calls will have to be enabled so the components function properly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 disables virtual system calls. Check the current GRUB 2 configuration with the following command: $ sudo grubby --info=ALL | grep args | grep -v 'vsyscall=none' If any output is returned, this is a finding. Check that virtual system calls are disabled by default to persist in kernel updates with the following command: $ grep vsyscall /etc/default/grub GRUB_CMDLINE_LINUX="vsyscall=none" If "vsyscall" is not set to "none", is missing or commented out, and is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-271738`

### Rule: OL 9 must clear the page allocator to prevent use-after-free attacks.

**Rule ID:** `SV-271738r1092600_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Poisoning writes an arbitrary value to freed pages, so any modification or reference to that page after being freed or before being initialized will be detected and prevented. This prevents many types of use-after-free vulnerabilities at little performance cost. Also prevents leak of data and detection of corrupted memory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 clears the page allocator to prevent use-after-free attacks. Verify that GRUB 2 is configured to enable page poisoning to mitigate use-after-free vulnerabilities. Check that the current GRUB 2 configuration has page poisoning enabled with the following command: $ sudo grubby --info=ALL | grep args | grep -v 'page_poison=1' If any output is returned, this is a finding. Check that page poisoning is enabled by default to persist in kernel updates with the following command: $ grep page_poison /etc/default/grub GRUB_CMDLINE_LINUX="page_poison=1" If "page_poison" is not set to "1", is missing or commented out, this is a finding.

## Group: SRG-OS-000269-GPOS-00103

**Group ID:** `V-271739`

### Rule: OL 9 systemd-journald service must be enabled.

**Rule ID:** `SV-271739r1091929_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In the event of a system failure, OL 9 must preserve any information necessary to determine cause of failure and any information necessary to return to operations with least disruption to system processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 systemd-journald is active with the following command: $ systemctl is-active systemd-journald active If the systemd-journald service is not active, this is a finding.

## Group: SRG-OS-000312-GPOS-00123

**Group ID:** `V-271740`

### Rule: OL 9 must enable kernel parameters to enforce discretionary access control on hardlinks.

**Rule ID:** `SV-271740r1091932_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By enabling the fs.protected_hardlinks kernel parameter, users can no longer create soft or hard links to files they do not own. Disallowing such hardlinks mitigates vulnerabilities based on insecure file system accessed by privileged programs, avoiding an exploitation vector exploiting unsafe use of open() or creat(). Satisfies: SRG-OS-000312-GPOS-00123, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to enable DAC on hardlinks. Check the status of the fs.protected_hardlinks kernel parameter with the following command: $ sudo sysctl fs.protected_hardlinks fs.protected_hardlinks = 1 If "fs.protected_hardlinks" is not set to "1" or is missing, this is a finding.

## Group: SRG-OS-000312-GPOS-00123

**Group ID:** `V-271741`

### Rule: OL 9 must enable kernel parameters to enforce discretionary access control on symlinks.

**Rule ID:** `SV-271741r1091935_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By enabling the fs.protected_symlinks kernel parameter, symbolic links are permitted to be followed only when outside a sticky world-writable directory, or when the user identifier (UID) of the link and follower match, or when the directory owner matches the symlink's owner. Disallowing such symlinks helps mitigate vulnerabilities based on insecure file system accessed by privileged programs, avoiding an exploitation vector exploiting unsafe use of open() or creat(). Satisfies: SRG-OS-000312-GPOS-00123, SRG-OS-000324-GPOS-00125</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to enable DAC on symlinks. Check the status of the fs.protected_symlinks kernel parameter with the following command: $ sudo sysctl fs.protected_symlinks fs.protected_symlinks = 1 If "fs.protected_symlinks " is not set to "1" or is missing, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-271742`

### Rule: OL 9 debug-shell systemd service must be disabled.

**Rule ID:** `SV-271742r1091938_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The debug-shell requires no authentication and provides root privileges to anyone who has physical access to the machine. While this feature is disabled by default, masking it adds an additional layer of assurance that it will not be enabled via a dependency in systemd. This also prevents attackers with physical access from trivially bypassing security on the machine through valid troubleshooting configurations and gaining root access when the system is rebooted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to mask the debug-shell systemd service with the following command: $ systemctl status debug-shell.service debug-shell.service Loaded: masked (Reason: Unit debug-shell.service is masked.) Active: inactive (dead) If the "debug-shell.service" is loaded and not masked, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-271743`

### Rule: OL 9 IP tunnels must use 140-3 approved cryptographic algorithms.

**Rule ID:** `SV-271743r1092635_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Overriding the system crypto policy makes the behavior of the Libreswan service violate expectations and makes system configuration more fragmented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the IPsec service is not installed, this requirement is Not Applicable. Verify that the IPsec service uses the systemwide cryptographic policy with the following command: $ grep include /etc/ipsec.conf /etc/ipsec.d/*.conf /etc/ipsec.conf:include /etc/crypto-policies/back-ends/libreswan.config If the IPsec configuration file does not contain "include /etc/crypto-policies/back-ends/libreswan.config", this is a finding.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-271744`

### Rule: OL 9 must have mail aliases to notify the information system security officer (ISSO) and system administrator (SA) (at a minimum) in the event of an audit processing failure.

**Rule ID:** `SV-271744r1091944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to notify the appropriate interactive users in the event of an audit processing failure. Find the alias maps that are being used with the following command: $ postconf alias_maps alias_maps = hash:/etc/aliases Query the Postfix alias maps for an alias for the root user with the following command: $ postmap -q root hash:/etc/aliases isso If an alias is not set, this is a finding.

## Group: SRG-OS-000132-GPOS-00067

**Group ID:** `V-271745`

### Rule: OL 9 must restrict access to the kernel message buffer.

**Rule ID:** `SV-271745r1091947_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DOD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components. Restricting access to the kernel message buffer limits access to only root. This prevents attackers from gaining additional system information as a nonprivileged user. Satisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000138-GPOS-00069</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to restrict access to the kernel message buffer with the following commands: Check the status of the kernel.dmesg_restrict kernel parameter. $ sudo sysctl kernel.dmesg_restrict kernel.dmesg_restrict = 1 If "kernel.dmesg_restrict" is not set to "1" or is missing, this is a finding.

## Group: SRG-OS-000132-GPOS-00067

**Group ID:** `V-271746`

### Rule: OL 9 must prevent kernel profiling by nonprivileged users.

**Rule ID:** `SV-271746r1091950_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DOD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components. Setting the kernel.perf_event_paranoid kernel parameter to "2" prevents attackers from gaining additional system information as a nonprivileged user. Satisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000138-GPOS-00069</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to prevent kernel profiling by nonprivileged users with the following commands: Check the status of the kernel.perf_event_paranoid kernel parameter. $ sysctl kernel.perf_event_paranoid kernel.perf_event_paranoid = 2 If "kernel.perf_event_paranoid" is not set to "2" or is missing, this is a finding.

## Group: SRG-OS-000132-GPOS-00067

**Group ID:** `V-271747`

### Rule: OL 9 must restrict exposed kernel pointer addresses access.

**Rule ID:** `SV-271747r1091953_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Exposing kernel pointers (through procfs or "seq_printf()") exposes kernel writeable structures, which may contain functions pointers. If a write vulnerability occurs in the kernel, allowing write access to any of this structure, the kernel can be compromised. This option disallows any program without the CAP_SYSLOG capability to get the addresses of kernel pointers by replacing them with "0". Satisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000433-GPOS-00192</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 restricts access to exposed kernel pointers with the following command: $ sysctl kernel.kptr_restrict kernel.kptr_restrict = 1

## Group: SRG-OS-000132-GPOS-00067

**Group ID:** `V-271748`

### Rule: OL 9 must disable access to network bpf system call from nonprivileged processes.

**Rule ID:** `SV-271748r1091956_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Loading and accessing the packet filters programs and maps using the bpf() system call has the potential of revealing sensitive information about the kernel state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 prevents privilege escalation thru the kernel by disabling access to the bpf system call with the following commands: $ sysctl kernel.unprivileged_bpf_disabled kernel.unprivileged_bpf_disabled = 1 If the returned line does not have a value of "1", or a line is not returned, this is a finding.

## Group: SRG-OS-000132-GPOS-00067

**Group ID:** `V-271749`

### Rule: OL 9 must restrict usage of ptrace to descendant processes.

**Rule ID:** `SV-271749r1091959_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted usage of ptrace allows compromised binaries to run ptrace on other processes of the user. Like this, the attacker can steal sensitive information from the target processes (e.g., SSH sessions, web browser, etc.) without any additional assistance from the user (i.e., without resorting to phishing).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 restricts usage of ptrace to descendant processes with the following commands: $ sysctl kernel.yama.ptrace_scope kernel.yama.ptrace_scope = 1 If the returned line does not have a value of "1", or a line is not returned, this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-271750`

### Rule: OL 9 must automatically exit interactive command shell user sessions after 15 minutes of inactivity.

**Rule ID:** `SV-271750r1091962_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle interactive command shell user session within a short time period reduces the window of opportunity for unauthorized personnel to take control of it when left unattended in a virtual terminal or physical console. Satisfies: SRG-OS-000163-GPOS-00072, SRG-OS-000029-GPOS-00010</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to exit interactive command shell user sessions after 15 minutes of inactivity or less with the following command: $ grep -i tmout /etc/profile /etc/profile.d/*.sh /etc/profile.d/tmout.sh:declare -xr TMOUT=900 If "TMOUT" is not set to "900" or less in a script located in the "/etc/'profile.d/ directory, is missing or is commented out, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-271751`

### Rule: OL 9 must be configured so that the systemd Ctrl-Alt-Delete burst key sequence is disabled.

**Rule ID:** `SV-271751r1091965_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A locally logged-on user who presses Ctrl-Alt-Delete when at the console can reboot the system. If accidentally pressed, as could happen in the case of a mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot. In a graphical user environment, risk of unintentional reboot from the Ctrl-Alt-Delete sequence is reduced because the user will be prompted before any action is taken.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to not reboot the system when Ctrl-Alt-Delete is pressed seven times within two seconds with the following command: $ grep -i ctrl /etc/systemd/system.conf CtrlAltDelBurstAction=none If the "CtrlAltDelBurstAction" is not set to "none", commented out, or is missing, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-271752`

### Rule: OL 9 must be configured so that the x86 Ctrl-Alt-Delete key sequence is disabled.

**Rule ID:** `SV-271752r1091968_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A locally logged-on user who presses Ctrl-Alt-Delete when at the console can reboot the system. If accidentally pressed, as could happen in the case of a mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot. In a graphical user environment, risk of unintentional reboot from the Ctrl-Alt-Delete sequence is reduced because the user will be prompted before any action is taken.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is not configured to reboot the system when Ctrl-Alt-Delete is pressed with the following command: $ systemctl status ctrl-alt-del.target ctrl-alt-del.target Loaded: masked (Reason: Unit ctrl-alt-del.target is masked.) Active: inactive (dead) If the "ctrl-alt-del.target" is loaded and not masked, this is a finding.

## Group: SRG-OS-000027-GPOS-00008

**Group ID:** `V-271753`

### Rule: OL 9 must limit the number of concurrent sessions to ten for all accounts and/or account types.

**Rule ID:** `SV-271753r1091971_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Operating system management includes the ability to control the number of users and user sessions that use an operating system. Limiting the number of allowed users and sessions per user is helpful in reducing the risks related to denial-of-service (DoS) attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions must be defined based on mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 limits the number of concurrent sessions to "10" for all accounts and/or account types with the following command: $ grep -r -s maxlogins /etc/security/limits.conf /etc/security/limits.d/*.conf /etc/security/limits.conf:* hard maxlogins 10 This can be set as a global domain (with the * wildcard) but may be set differently for multiple domains. If the "maxlogins" item is missing, commented out, or the value is set greater than "10" and is not documented with the information system security officer (ISSO) as an operational requirement for all domains that have the "maxlogins" item assigned, this is a finding.

## Group: SRG-OS-000329-GPOS-00128

**Group ID:** `V-271754`

### Rule: OL 9 must automatically lock an account when three unsuccessful logon attempts occur during a 15-minute time period.

**Rule ID:** `SV-271754r1091974_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account. Satisfies: SRG-OS-000329-GPOS-00128, SRG-OS-000021-GPOS-00005</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system administrator demonstrates the use of an approved centralized account management method that locks an account after three unsuccessful logon attempts within a period of 15 minutes, this requirement is Not Applicable. Verify that OL 9 locks an account after three unsuccessful logon attempts within a period of 15 minutes with the following command: $ grep fail_interval /etc/security/faillock.conf fail_interval = 900 If the "fail_interval" option is not set to "900" or less (but not "0"), the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000329-GPOS-00128

**Group ID:** `V-271755`

### Rule: OL 9 must maintain an account lock until the locked account is released by an administrator.

**Rule ID:** `SV-271755r1091977_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account. Satisfies: SRG-OS-000329-GPOS-00128, SRG-OS-000021-GPOS-00005</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to lock an account until released by an administrator after three unsuccessful logon attempts with the command: $ grep 'unlock_time =' /etc/security/faillock.conf unlock_time = 0 If the "unlock_time" option is not set to "0", the line is missing, or commented out, this is a finding.

## Group: SRG-OS-000405-GPOS-00184

**Group ID:** `V-271756`

### Rule: OL 9 local disk partitions must implement cryptographic mechanisms to prevent unauthorized disclosure or modification of all information that requires at rest protection.

**Rule ID:** `SV-271756r1091980_rule`
**Severity:** high

**Description:**
<VulnDiscussion>OL 9 systems handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). Satisfies: SRG-OS-000405-GPOS-00184, SRG-OS-000185-GPOS-00079, SRG-OS-000404-GPOS-00183</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If there is a documented and approved reason for not having data-at-rest encryption, this requirement is Not Applicable. Verify that OL 9 prevents unauthorized disclosure or modification of all information requiring at-rest protection by using disk encryption. Verify all system partitions are encrypted with the following command: $ sudo blkid /dev/map per/ol-root: UUID="67b7d7fe-de60-6fd0-befb-e6748cf97743" TYPE="crypto_LUKS" Every persistent disk partition present must be of type "crypto_LUKS". If any partitions other than the boot partition or pseudo file systems (such as /proc or /sys) or temporary file systems (that are tmpfs) are not type "crypto_LUKS", ask the administrator to indicate how the partitions are encrypted. If there is no evidence that these partitions are encrypted, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271757`

### Rule: OL 9 file systems must not contain shosts.equiv files.

**Rule ID:** `SV-271757r1092604_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The shosts.equiv files are used to configure host-based authentication for the system via SSH. Host-based authentication is not sufficient for preventing unauthorized access to the system, as it does not require interactive identification and authentication of a connection request, or for the use of two-factor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has no "shosts.equiv" files on the system with the following command: $ sudo find / -name shosts.equiv If a "shosts.equiv" file is found, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271758`

### Rule: OL 9 file systems must not contain .shosts files.

**Rule ID:** `SV-271758r1091986_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The .shosts files are used to configure host-based authentication for individual users or the system via SSH. Host-based authentication is not sufficient for preventing unauthorized access to the system, as it does not require interactive identification and authentication of a connection request, or for the use of two-factor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has no ".shosts" files on the system with the following command: $ sudo find / -name .shosts If a ".shosts" file is found, this is a finding.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-271759`

### Rule: OL 9 must implement DOD-approved encryption in the bind package.

**Rule ID:** `SV-271759r1091989_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. OL 9 incorporates system-wide crypto policies by default. The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/ directory. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000426-GPOS-00190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the "bind" package is not installed, this requirement is Not Applicable. Verify that OL 9 BIND uses the system crypto policy with the following command: $ sudo grep include /etc/named.conf include "/etc/crypto-policies/back-ends/bind.config";' If BIND is installed and the BIND config file does not include the "/etc/crypto-policies/back-ends/bind.config" directive, or the line is commented out, this is a finding.

## Group: SRG-OS-000433-GPOS-00192

**Group ID:** `V-271760`

### Rule: OL 9 must implement nonexecutable data to protect its memory from unauthorized code execution.

**Rule ID:** `SV-271760r1091992_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ExecShield uses the segmentation feature on all x86 systems to prevent execution in memory higher than a certain address. It writes an address as a limit in the code segment descriptor, to control where code can be executed, on a per-process basis. When the kernel places a process's memory regions such as the stack and heap higher than this address, the hardware prevents execution in that address range. This is enabled by default on the latest Oracle systems if supported by the hardware.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 ExecShield is enabled on 64-bit systems with the following command: $ sudo dmesg | grep '[NX|DX]*protection' [ 0.000000] NX (Execute Disable) protection: active If "dmesg" does not show "NX (Execute Disable) protection" active, this is a finding.

## Group: SRG-OS-000433-GPOS-00193

**Group ID:** `V-271761`

### Rule: OL 9 must implement address space layout randomization (ASLR) to protect its memory from unauthorized code execution.

**Rule ID:** `SV-271761r1091995_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ASLR makes it more difficult for an attacker to predict the location of attack code they have introduced into a process' address space during an attempt at exploitation. Additionally, ASLR makes it more difficult for an attacker to know the location of existing code to repurpose it using return-oriented programming (ROP) techniques.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is implementing ASLR with the following command: $ sysctl kernel.randomize_va_space kernel.randomize_va_space = 2 If "kernel.randomize_va_space" is not set to "2" or is missing, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-271762`

### Rule: OL 9 must use mechanisms meeting the requirements of applicable federal laws, executive orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module.

**Rule ID:** `SV-271762r1091998_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Overriding the system crypto policy makes the behavior of Kerberos violate expectations and makes system configuration more fragmented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures Kerberos to use the systemwide crypto policy with the following command: $ file /etc/crypto-policies/back-ends/krb5.config /etc/crypto-policies/back-ends/krb5.config: symbolic link to /usr/share/crypto-policies/FIPS/krb5.txt If the symlink does not exist or points to a different target, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271763`

### Rule: OL 9 must be configured to prevent unrestricted mail relaying.

**Rule ID:** `SV-271763r1092001_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If unrestricted mail relaying is permitted, unauthorized senders could use this host as a mail relay for the purpose of sending spam or other unauthorized activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If postfix is not installed, this requirement is Not Applicable. Verify that OL 9 is configured to prevent unrestricted mail relaying with the following command: $ postconf -n smtpd_client_restrictions smtpd_client_restrictions = permit_mynetworks,reject If the "smtpd_client_restrictions" parameter contains any entries other than "permit_mynetworks" and "reject", and the additional entries have not been documented with the information system security officer (ISSO), this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271764`

### Rule: OL 9 Trivial File Transfer Protocol (TFTP) daemon must be configured to operate in secure mode if the TFTP server is required. 

**Rule ID:** `SV-271764r1092004_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting TFTP to a specific directory prevents remote users from copying, transferring, or overwriting system files. Using the "-s" option causes the TFTP service to only serve files from the given directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 TFTP daemon is configured to operate in secure mode. Check if a TFTP server is installed with the following command: $ sudo dnf list --installed tftp-server Installed Packages tftp-server.x86_64 5.2-38.el9 @ol9_appstream Note: If a TFTP server is not installed, this requirement is Not Applicable. If a TFTP server is installed, check for the server arguments with the following command: $ systemctl cat tftp | grep ExecStart ExecStart=/usr/sbin/in.tftpd -s /var/lib/tftpboot If the "ExecStart" line does not have a "-s" option, and a subdirectory is not assigned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271765`

### Rule: OL 9 must be configured so that local initialization files do not execute world-writable programs.

**Rule ID:** `SV-271765r1092007_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If user start-up files execute world-writable programs, especially in unprotected directories, they could be maliciously modified to destroy user files or otherwise compromise the system at the user level. If the system is compromised at the user level, it is easier to elevate privileges to eventually compromise the system at the root and network level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured so that local initialization files do not execute world-writable programs with the following command: Note: The example will be for a system that is configured to create user home directories in the "/home" directory. $ sudo find /home -perm -002 -type f -name ".[^.]*" -exec ls -ld {} \; If any local initialization files are found to reference world-writable files, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-271766`

### Rule: OL 9 must prevent the loading of a new kernel for later execution.

**Rule ID:** `SV-271766r1092010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. Disabling kexec_load prevents an unsigned kernel image (that could be a windows kernel or modified vulnerable kernel) from being loaded. Kexec can be used subvert the entire secureboot process and should be avoided at all costs especially since it can load unsigned kernel images.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to disable kernel image loading. Check the status of the kernel.kexec_load_disabled kernel parameter with the following command: $ sysctl kernel.kexec_load_disabled kernel.kexec_load_disabled = 1 If "kernel.kexec_load_disabled" is not set to "1" or is missing, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-271767`

### Rule: OL 9 must prevent system daemons from using Kerberos for authentication.

**Rule ID:** `SV-271767r1092013_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms used for authentication to the cryptographic module are not verified; therefore, cannot be relied upon to provide confidentiality or integrity and DOD data may be compromised. OL 9 systems using encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. The key derivation function (KDF) in Kerberos is not FIPS compatible. Ensuring the system does not have any keytab files present prevents system daemons from using Kerberos for authentication. A keytab is a file containing pairs of Kerberos principals and encrypted keys. FIPS 140-3 is the current standard for validating that mechanisms used to access cryptographic modules use authentication that meets DOD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general-purpose computing system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 prevents system daemons from using Kerberos for authentication with the following command: $ ls -al /etc/*.keytab ls: cannot access '/etc/*.keytab': No such file or directory If this command produces any "keytab" file(s), this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271768`

### Rule: OL 9 must enable hardening for the Berkeley Packet Filter (BPF) just-in-time compiler.

**Rule ID:** `SV-271768r1092016_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When hardened, the extended BPF just-in-time (JIT) compiler will randomize any kernel addresses in the BPF programs and maps and will not expose the JIT addresses in "/proc/kallsyms".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 enables hardening for the BPF JIT with the following commands: $ sudo sysctl net.core.bpf_jit_harden net.core.bpf_jit_harden = 2 If the returned line does not have a value of "2", or a line is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271769`

### Rule: OL 9 must be configured so that all system device files are correctly labeled to prevent unauthorized modification.

**Rule ID:** `SV-271769r1092019_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an unauthorized or modified device is allowed to exist on the system, there is the possibility the system may perform unintended or unauthorized operations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures all system device files to be correctly labeled to prevent unauthorized modification. List all device files on the system that are incorrectly labeled with the following commands: Note: Device files are normally found under "/dev", but applications may place device files in other directories and may necessitate a search of the entire system. $ sudo find /dev -context *:device_t:* \( -type c -o -type b \) -printf "%p %Z\n" $ sudo find /dev -context *:unlabeled_t:* \( -type c -o -type b \) -printf "%p %Z\n" Note: There are device files, such as "/dev/dtrace/helper" or "/dev/vmci", that are used for system trace capabilities or when the operating system is a host virtual machine. They will not be owned by a user on the system and require the "device_t" label to operate. These device files are not a finding. If there is output from either of these commands, other than already noted, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271770`

### Rule: OL 9 must not have unauthorized accounts.

**Rule ID:** `SV-271770r1092022_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accounts providing no operational purpose provide additional opportunities for system compromise. Unnecessary accounts include user accounts for individuals not requiring access to the system and application accounts for applications not installed on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 prohibits unauthorized interactive user accounts with the following command: $ less /etc/passwd root:x:0:0:root:/root:/bin/bash ... games:x:12:100:games:/usr/games:/sbin/nologin scsaustin:x:1001:1001:scsaustin:/home/scsaustin:/bin/bash djohnson:x:1002:1002:djohnson:/home/djohnson:/bin/bash Interactive user account, generally will have a user identifier (UID) of 1000 or greater, a home directory in a specific partition, and an interactive shell. Obtain the list of interactive user accounts authorized to be on the system from the system administrator or information system security officer (ISSO) and compare it to the list of local interactive user accounts on the system. If there are unauthorized local user accounts on the system, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271771`

### Rule: OL 9 SSH private host key files must have mode 0640 or less permissive.

**Rule ID:** `SV-271771r1092025_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an unauthorized user obtains the private SSH host key file, the host could be impersonated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 SSH private host key files have a mode of "0640" or less permissive with the following command: $ ls -l /etc/ssh/*_key 640 /etc/ssh/ssh_host_dsa_key 640 /etc/ssh/ssh_host_ecdsa_key 640 /etc/ssh/ssh_host_ed25519_key 640 /etc/ssh/ssh_host_rsa_key If any private host key file has a mode more permissive than "0640", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271772`

### Rule: OL 9 SSH public host key files must have mode 0644 or less permissive.

**Rule ID:** `SV-271772r1092028_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a public host key file is modified by an unauthorized user, the SSH service may be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 SSH public host key files have a mode of "0644" or less permissive with the following command: Note: SSH public key files may be found in other directories on the system depending on the installation. $ sudo stat -c "%a %n" /etc/ssh/*.pub 644 /etc/ssh/ssh_host_dsa_key.pub 644 /etc/ssh/ssh_host_ecdsa_key.pub 644 /etc/ssh/ssh_host_ed25519_key.pub 644 /etc/ssh/ssh_host_rsa_key.pub If any key.pub file has a mode more permissive than "0644", this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-271773`

### Rule: OL 9 system commands must be group-owned by root or a system account.

**Rule ID:** `SV-271773r1092031_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If OL 9 allowed any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to OL 9 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 system commands contained in the following directories are group-owned by "root", or a required system account, with the following command: $ sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -group root -exec ls -l {} \; If any system commands are returned and is not group-owned by a required system account, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-271774`

### Rule: OL 9 system commands must be owned by root.

**Rule ID:** `SV-271774r1092034_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If OL 9 allowed any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to OL 9 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 system commands contained in the following directories are owned by "root" with the following command: $ sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/libexec /usr/local/bin /usr/local/sbin ! -user root -exec ls -l {} \; If any system commands are found to not be owned by root, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-271775`

### Rule: OL 9 system commands must have mode 755 or less permissive.

**Rule ID:** `SV-271775r1092037_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If OL 9 allowed any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to OL 9 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 system commands contained in the following directories have mode "755" or less permissive with the following command: $ sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/libexec /usr/local/bin /usr/local/sbin -perm /022 -exec ls -l {} \; If any system commands are found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271776`

### Rule: OL 9 SSH server configuration file must be group-owned by root.

**Rule ID:** `SV-271776r1092040_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Service configuration files enable or disable features of their respective services, which if configured incorrectly, can lead to insecure and vulnerable configurations. Therefore, service configuration files must be owned by the correct group to prevent unauthorized changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures group ownership of the "/etc/ssh/sshd_config" file with the following command: $ ls -al /etc/ssh/sshd_config rw-------. 1 root root 3669 Feb 22 11:34 /etc/ssh/sshd_config If the "/etc/ssh/sshd_config" file does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271777`

### Rule: OL 9 SSH server configuration file must be owned by root.

**Rule ID:** `SV-271777r1092043_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Service configuration files enable or disable features of their respective services, which if configured incorrectly, can lead to insecure and vulnerable configurations. Therefore, service configuration files must be owned by the correct group to prevent unauthorized changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures ownership of the "/etc/ssh/sshd_config" file with the following command: $ ls -al /etc/ssh/sshd_config rw-------. 1 root root 3669 Feb 22 11:34 /etc/ssh/sshd_config If the "/etc/ssh/sshd_config" file does not have an owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271778`

### Rule: OL 9 SSH server configuration file must have mode 0600 or less permissive.

**Rule ID:** `SV-271778r1092046_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Service configuration files enable or disable features of their respective services that if configured incorrectly can lead to insecure and vulnerable configurations. Therefore, service configuration files should be owned by the correct group to prevent unauthorized changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures permissions of the "/etc/ssh/sshd_config" file with the following command: $ ls -al /etc/ssh/sshd_config rw-------. 1 root root 3669 Feb 22 11:34 /etc/ssh/sshd_config If the "/etc/ssh/sshd_config" permissions are not "0600", this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-271779`

### Rule: OL 9 must be configured so that a sticky bit must be set on all public directories.

**Rule ID:** `SV-271779r1092049_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DOD or other government agencies.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 world-writable directories have the sticky bit set. Determine if all world-writable directories have the sticky bit set by running the following command: $ sudo find / -type d \( -perm -0002 -a ! -perm -1000 \) -print 2>/dev/null drwxrwxrwt 7 root root 4096 Jul 26 11:19 /tmp If any of the returned directories are world-writable and do not have the sticky bit set, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271780`

### Rule: OL 9 local files and directories must have a valid group owner.

**Rule ID:** `SV-271780r1092052_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Files without a valid group owner may be unintentionally inherited if a group is assigned the same Group Identifier (GID) as the GID of the files without a valid group owner.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 local files and directories have a valid group with the following command: $ df --local -P | awk {'if (NR!=1) print $6'} | sudo xargs -I '{}' find '{}' -xdev -nogroup If any files on the system do not have an assigned group, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271781`

### Rule: OL 9 local files and directories must have a valid owner.

**Rule ID:** `SV-271781r1092055_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unowned files and directories may be unintentionally inherited if a user is assigned the same user identifier "UID" as the UID of the unowned files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 local files and directories on OL 9 have a valid owner with the following command: $ df --local -P | awk {'if (NR!=1) print $6'} | sudo xargs -I '{}' find '{}' -xdev -nouser If any files on the system do not have an assigned owner, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271782`

### Rule: OL 9 local initialization files must have mode 0740 or less permissive.

**Rule ID:** `SV-271782r1092058_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Local initialization files are used to configure the user's shell environment upon logon. Malicious modification of these files could compromise accounts upon logon.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures all local initialization files to have a mode of "0740" or less permissive with the following command: Note: The example will be for the "wadea" user, who has a home directory of "/home/wadea". $ sudo ls -al /home/wadea/.[^.]* | more -rwxr-xr-x 1 wadea users 896 Mar 10 2011 .profile -rwxr-xr-x 1 wadea users 497 Jan 6 2007 .login -rwxr-xr-x 1 wadea users 886 Jan 6 2007 .something If any local initialization files have a mode more permissive than "0740", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271783`

### Rule: OL 9 local interactive user home directories must be group-owned by the home directory owner's primary group.

**Rule ID:** `SV-271783r1092061_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Group Identifier (GID) of a local interactive user's home directory is not the same as the primary GID of the user, this would allow unauthorized access to the user's files, and users that share the same group may not be able to access files that they legitimately should.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures assigned home directories of all local interactive users to be group-owned by that user's primary GID with the following command: Note: This may miss local interactive users that have been assigned a privileged user identifier (UID). Evidence of interactive use may be obtained from a number of log files containing system logon information. The returned directory "/home/wadea" is used as an example. $ sudo ls -ld $(awk -F: '($3>=1000)&&($7 !~ /nologin/){print $6}' /etc/passwd) drwxr-x--- 2 wadea admin 4096 Jun 5 12:41 wadea Check the user's primary group with the following command: $ sudo grep $(grep wadea /etc/passwd | awk -F: '{print $4}') /etc/group admin:x:250:wadea,jonesj,jacksons If the user home directory referenced in "/etc/passwd" is not group-owned by that user's primary GID, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271784`

### Rule: OL 9 local interactive user home directories must have mode 0750 or less permissive.

**Rule ID:** `SV-271784r1092064_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on local interactive user home directories may allow unauthorized access to user files by other users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures assigned home directories of all local interactive users to have a mode of "0750" or less permissive with the following command: Note: This may miss interactive users that have been assigned a privileged user identifier (UID). Evidence of interactive use may be obtained from a number of log files containing system logon information. $ sudo ls -ld $(awk -F: '($3>=1000)&&($7 !~ /nologin/){print $6}' /etc/passwd) drwxr-x--- 2 wadea admin 4096 Jun 5 12:41 wadea If home directories referenced in "/etc/passwd" do not have a mode of "0750" or less permissive, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-271785`

### Rule: OL 9 world-writable directories must be owned by root, sys, bin, or an application user.

**Rule ID:** `SV-271785r1092067_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a world-writable directory is not owned by root, sys, bin, or an application user identifier (UID), unauthorized users may be able to modify files created by others. The only authorized public directories are those temporary directories supplied with the system or those designed to be temporary file repositories. The setting is normally reserved for directories used by the system and by users for temporary file storage, (e.g., /tmp), and for directories requiring global read/write access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures world writable directories to be owned by root, a system account, or an application account with the following command. It will discover and print world-writable directories that are not owned by root. Run it once for each local partition [PART]: $ sudo find [PART] -xdev -type d -perm -0002 -uid +0 -print If there is output, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-271786`

### Rule: OL 9 library directories must be group-owned by root or a system account.

**Rule ID:** `SV-271786r1092070_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If OL 9 allowed any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to OL 9 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 system-wide shared library directories are group-owned by "root" with the following command: $ sudo find /lib /lib64 /usr/lib /usr/lib64 ! -group root -type d -exec stat -c "%n %G" '{}' \; If any system-wide shared library directory is returned and is not group-owned by a required system account, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-271787`

### Rule: OL 9 library directories must be owned by root.

**Rule ID:** `SV-271787r1092073_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If OL 9 allowed any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to OL 9 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 system-wide shared library directories are owned by "root" with the following command: $ sudo find /lib /lib64 /usr/lib /usr/lib64 ! -user root -type d -exec stat -c "%n %U" '{}' \; If any system-wide shared library directory is not owned by root, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-271788`

### Rule: OL 9 library directories must have mode 755 or less permissive.

**Rule ID:** `SV-271788r1092076_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If OL 9 allowed any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to OL 9 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 system-wide shared library directories have mode "755" or less permissive with the following command: $ sudo find -L /lib /lib64 /usr/lib /usr/lib64 -perm /022 -type d -exec ls -l {} \; If any system-wide shared library file is found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-271789`

### Rule: OL 9 library files must be group-owned by root or a system account.

**Rule ID:** `SV-271789r1092079_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If OL 9 allowed any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to OL 9 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 system-wide shared library files are group-owned by "root" with the following command: $ sudo find -L /lib /lib64 /usr/lib /usr/lib64 ! -group root -exec ls -l {} \; If any system-wide shared library file is returned and is not group-owned by a required system account, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-271790`

### Rule: OL 9 library files must be owned by root.

**Rule ID:** `SV-271790r1092082_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If OL 9 allowed any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to OL 9 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 system-wide shared library files are owned by "root" with the following command: $ sudo find -L /lib /lib64 /usr/lib /usr/lib64 ! -user root -exec ls -l {} \; If any system-wide shared library file is not owned by root, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-271791`

### Rule: OL 9 library files must have mode 755 or less permissive.

**Rule ID:** `SV-271791r1092085_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If OL 9 allowed any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to OL 9 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 system-wide shared library files contained in the following directories have mode "755" or less permissive with the following command: $ sudo find -L /lib /lib64 /usr/lib /usr/lib64 -perm /022 -type f -exec ls -l {} \; If any system-wide shared library file is found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271792`

### Rule: OL 9 /boot/grub2/grub.cfg file must be group-owned by root.

**Rule ID:** `SV-271792r1094968_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "root" group is a highly privileged group. The group-owner of this file should not have any access privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures the group ownership of the "/boot/grub2/grub.cfg" file with the following command: $ sudo stat -c "%G %n" /boot/grub2/grub.cfg root /boot/grub2/grub.cfg If "/boot/grub2/grub.cfg" file does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271793`

### Rule: OL 9 /boot/grub2/grub.cfg file must be owned by root.

**Rule ID:** `SV-271793r1092605_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/boot/grub2/grub.cfg" file stores sensitive system configuration. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures ownership of the "/boot/grub2/grub.cfg" file with the following command: $ sudo stat -c "%U %n" /boot/grub2/grub.cfg root /boot/grub2/grub.cfg If "/boot/grub2/grub.cfg" file does not have an owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271794`

### Rule: OL 9 /etc/group file must be group-owned by root.

**Rule ID:** `SV-271794r1092094_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/group" file contains information regarding groups that are configured on the system. Protection of this file is important for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures group ownership of the "/etc/group" file with the following command: $ stat -c "%G %n" /etc/group root /etc/group If "/etc/group" file does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271795`

### Rule: OL 9 /etc/group- file must be group-owned by root.

**Rule ID:** `SV-271795r1092097_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/group-" file is a backup file of "/etc/group", and as such, contains information regarding groups that are configured on the system. Protection of this file is important for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures group ownership of the "/etc/group-" file with the following command: $ stat -c "%G %n" /etc/group- root /etc/group- If "/etc/group-" file does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271796`

### Rule: OL 9 /etc/group file must be owned by root.

**Rule ID:** `SV-271796r1092100_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/group" file contains information regarding groups that are configured on the system. Protection of this file is important for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures ownership of the "/etc/group" file with the following command: $ stat -c "%U %n" /etc/group root /etc/group If "/etc/group" file does not have an owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271797`

### Rule: OL 9 /etc/group- file must be owned by root.

**Rule ID:** `SV-271797r1092103_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/group-" file is a backup file of "/etc/group", and as such, contains information regarding groups that are configured on the system. Protection of this file is important for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures ownership of the "/etc/group-" file with the following command: $ stat -c "%U %n" /etc/group- root /etc/group- If "/etc/group-" file does not have an owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271798`

### Rule: OL 9 /etc/group file must have mode 0644 or less permissive to prevent unauthorized access.

**Rule ID:** `SV-271798r1092106_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/group" file contains information regarding groups that are configured on the system. Protection of this file is important for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures the "/etc/group" file to have a mode of "0644" or less permissive with the following command: $ stat -c "%a %n" /etc/group 644 /etc/group If a value of "0644" or less permissive is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271799`

### Rule: OL 9 /etc/group- file must have mode 0644 or less permissive to prevent unauthorized access.

**Rule ID:** `SV-271799r1092109_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/group-" file is a backup file of "/etc/group", and as such, contains information regarding groups that are configured on the system. Protection of this file is important for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures the "/etc/group-" file to have a mode "0644" or less permissive with the following command: $ stat -c "%a %n" /etc/group- 644 /etc/group- If a value of "0644" or less permissive is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271800`

### Rule: OL 9 /etc/gshadow file must be group-owned by root.

**Rule ID:** `SV-271800r1092112_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/gshadow" file contains group password hashes. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures group ownership of the "/etc/gshadow" file with the following command: $ stat -c "%G %n" /etc/gshadow root /etc/gshadow If "/etc/gshadow" file does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271801`

### Rule: OL 9 /etc/gshadow- file must be group-owned by root.

**Rule ID:** `SV-271801r1092115_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/gshadow-" file is a backup of "/etc/gshadow", and as such, contains group password hashes. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures group ownership of the "/etc/gshadow-" file with the following command: $ stat -c "%G %n" /etc/gshadow- root /etc/gshadow- If "/etc/gshadow-" file does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271802`

### Rule: OL 9 /etc/gshadow file must be owned by root.

**Rule ID:** `SV-271802r1092118_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/gshadow" file contains group password hashes. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures ownership of the "/etc/gshadow" file with the following command: $ stat -c "%U %n" /etc/gshadow root /etc/gshadow If "/etc/gshadow" file does not have an owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271803`

### Rule: OL 9 /etc/gshadow- file must be owned by root.

**Rule ID:** `SV-271803r1092121_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/gshadow-" file is a backup of "/etc/gshadow", and as such, contains group password hashes. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures ownership of the "/etc/gshadow-" file with the following command: $ stat -c "%U %n" /etc/gshadow- root /etc/gshadow- If "/etc/gshadow-" file does not have an owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271804`

### Rule: OL 9 /etc/gshadow file must have mode 0000 or less permissive to prevent unauthorized access.

**Rule ID:** `SV-271804r1092124_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/gshadow" file contains group password hashes. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures the "/etc/gshadow" file to have a mode pf "0000" with the following command: $ stat -c "%a %n" /etc/gshadow 0 /etc/gshadow If a value of "0" is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271805`

### Rule: OL 9 /etc/gshadow- file must have mode 0000 or less permissive to prevent unauthorized access.

**Rule ID:** `SV-271805r1092127_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/gshadow-" file is a backup of "/etc/gshadow", and as such, contains group password hashes. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures the "/etc/gshadow-" file to have a mode of "0000" with the following command: $ stat -c "%a %n" /etc/gshadow- 0 /etc/gshadow- If a value of "0" is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271806`

### Rule: OL 9 /etc/passwd file must be group-owned by root.

**Rule ID:** `SV-271806r1092130_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/passwd" file contains information about the users that are configured on the system. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures group ownership of the "/etc/passwd" file with the following command: $ stat -c "%G %n" /etc/passwd root /etc/passwd If "/etc/passwd" file does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271807`

### Rule: OL 9 /etc/passwd- file must be group-owned by root.

**Rule ID:** `SV-271807r1092133_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/passwd-" file is a backup file of "/etc/passwd", and as such, contains information about the users that are configured on the system. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures group ownership of the "/etc/passwd-" file with the following command: $ stat -c "%G %n" /etc/passwd- root /etc/passwd- If "/etc/passwd-" file does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271808`

### Rule: OL 9 /etc/passwd file must be owned by root.

**Rule ID:** `SV-271808r1092136_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/passwd" file contains information about the users that are configured on the system. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures ownership of the "/etc/passwd" file with the following command: $ stat -c "%U %n" /etc/passwd root /etc/passwd If "/etc/passwd" file does not have an owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271809`

### Rule: OL 9 /etc/passwd- file must be owned by root.

**Rule ID:** `SV-271809r1092139_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/passwd-" file is a backup file of "/etc/passwd", and as such, contains information about the users that are configured on the system. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures ownership of the "/etc/passwd-" file with the following command: $ stat -c "%U %n" /etc/passwd- root /etc/passwd- If "/etc/passwd-" file does not have an owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271810`

### Rule: OL 9 /etc/passwd file must have mode 0644 or less permissive to prevent unauthorized access.

**Rule ID:** `SV-271810r1092142_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the "/etc/passwd" file is writable by a group-owner or the world the risk of its compromise is increased. The file contains the list of accounts on the system and associated information, and protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures the "/etc/passwd" file to have a mode of "0644" or less permissive with the following command: $ stat -c "%a %n" /etc/passwd 644 /etc/passwd If a value of "0644" or less permissive is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271811`

### Rule: OL 9 /etc/passwd- file must have mode 0644 or less permissive to prevent unauthorized access.

**Rule ID:** `SV-271811r1092145_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/passwd-" file is a backup file of "/etc/passwd", and as such, contains information about the users that are configured on the system. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures the "/etc/passwd-" file to have a mode of "0644" or less permissive with the following command: $ stat -c "%a %n" /etc/passwd- 644 /etc/passwd- If a value of "0644" or less permissive is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271812`

### Rule: OL 9 /etc/shadow file must be group-owned by root.

**Rule ID:** `SV-271812r1092148_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/shadow" file stores password hashes. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures group ownership of the "/etc/shadow" file with the following command: $ stat -c "%G %n" /etc/shadow root /etc/shadow If "/etc/shadow" file does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271813`

### Rule: OL 9 /etc/shadow- file must be group-owned by root.

**Rule ID:** `SV-271813r1092151_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/shadow-" file is a backup file of "/etc/shadow", and as such, contains the list of local system accounts and password hashes. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures group ownership of the "/etc/shadow-" file with the following command: $ stat -c "%G %n" /etc/shadow- root /etc/shadow- If "/etc/shadow-" file does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271814`

### Rule: OL 9 /etc/shadow file must be owned by root.

**Rule ID:** `SV-271814r1092154_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/shadow" file contains the list of local system accounts and stores password hashes. Protection of this file is critical for system security. Failure to give ownership of this file to root provides the designated owner with access to sensitive information, which could weaken the system security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures ownership of the "/etc/shadow" file with the following command: $ stat -c "%U %n" /etc/shadow root /etc/shadow If "/etc/shadow" file does not have an owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271815`

### Rule: OL 9 /etc/shadow- file must be owned by root.

**Rule ID:** `SV-271815r1092157_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/shadow-" file is a backup file of "/etc/shadow", and as such, contains the list of local system accounts and password hashes. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures ownership of the "/etc/shadow-" file with the following command: $ stat -c "%U %n" /etc/shadow- root /etc/shadow- If "/etc/shadow-" file does not have an owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271816`

### Rule: OL 9 /etc/shadow- file must have mode 0000 or less permissive to prevent unauthorized access.

**Rule ID:** `SV-271816r1092160_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/shadow-" file is a backup file of "/etc/shadow", and as such, contains the list of local system accounts and password hashes. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures the "/etc/shadow-" file to have a mode of "0000" with the following command: $ stat -c "%a %n" /etc/shadow- 0 /etc/shadow- If a value of "0" is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271817`

### Rule: OL 9 /etc/shadow file must have mode 0000 to prevent unauthorized access.

**Rule ID:** `SV-271817r1092163_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/shadow" file contains the list of local system accounts and stores password hashes. Protection of this file is critical for system security. Failure to give ownership of this file to root provides the designated owner with access to sensitive information, which could weaken the system security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures the "/etc/shadow" file to have a mode of "0000" with the following command: $ stat -c "%a %n" /etc/shadow 0 /etc/shadow If a value of "0" is not returned, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-271818`

### Rule: OL 9 /var/log directory must be group-owned by root.

**Rule ID:** `SV-271818r1092166_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the OL 9 system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures the "/var/log" directory to be group-owned by root with the following command: $ ls -ld /var/log drwxr-xr-x. 16 root root 4096 July 11 11:34 /var/log If "/var/log" does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-271819`

### Rule: OL 9 /var/log directory must be owned by root.

**Rule ID:** `SV-271819r1092169_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the OL 9 system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures the "/var/log" directory to be owned by root with the following command: $ ls -ld /var/log drwxr-xr-x. 16 root root 4096 July 11 11:34 /var/log If "/var/log" does not have an owner of "root", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-271820`

### Rule: OL 9 /var/log directory must have mode 0755 or less permissive.

**Rule ID:** `SV-271820r1092172_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the OL 9 system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures the "/var/log" directory to have a mode of "0755" or less permissive with the following command: $ ls -ld /var/log drwxr-xr-x. 16 root root 4096 July 11 11:34 /var/log If "/var/log" does not have a mode of "0755" or less permissive, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-271821`

### Rule: OL 9 /var/log/messages file must be group-owned by root.

**Rule ID:** `SV-271821r1092175_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the OL 9 system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures the "/var/log/messages" file to be group-owned by root with the following command: $ ls -la /var/log/messages rw-------. 1 root root 564223 July 11 11:34 /var/log/messages If "/var/log/messages" does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-271822`

### Rule: OL 9 /var/log/messages file must be owned by root.

**Rule ID:** `SV-271822r1092178_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the OL 9 system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures the "/var/log/messages" file to be owned by root with the following command: $ ls -la /var/log/messages rw-------. 1 root root 564223 July 11 11:34 /var/log/messages If "/var/log/messages" does not have an owner of "root", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-271823`

### Rule: OL 9 /var/log/messages file must have mode 0640 or less permissive.

**Rule ID:** `SV-271823r1092181_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the OL 9 system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures the "/var/log/messages" file to have a mode of "0640" or less permissive with the following command: $ ls -la /var/log/messages rw-------. 1 root root 564223 July 11 11:34 /var/log/messages If "/var/log/messages" does not have a mode of "0640" or less permissive, this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-271824`

### Rule: OL 9 audit tools must be group-owned by root.

**Rule ID:** `SV-271824r1092184_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data; therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. OL 9 systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools, and the corresponding rights the user enjoys, to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 audit tools are group owned by "root" with the following command: $ sudo stat -c "%G %n" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/rsyslogd /sbin/augenrules root /sbin/auditctl root /sbin/aureport root /sbin/ausearch root /sbin/autrace root /sbin/auditd root /sbin/rsyslogd root /sbin/augenrules If any audit tools do not have a group owner of "root", this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-271825`

### Rule: OL 9 audit tools must be owned by root.

**Rule ID:** `SV-271825r1092187_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. OL 9 systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools, and the corresponding rights the user enjoys, to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 audit tools are owned by "root" with the following command: $ sudo stat -c "%U %n" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/rsyslogd /sbin/augenrules root /sbin/auditctl root /sbin/aureport root /sbin/ausearch root /sbin/autrace root /sbin/auditd root /sbin/rsyslogd root /sbin/augenrules If any audit tools do not have an owner of "root", this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-271826`

### Rule: OL 9 audit tools must have a mode of 0755 or less permissive.

**Rule ID:** `SV-271826r1092190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. OL 9 systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools, and the corresponding rights the user enjoys, to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 audit tools have a mode of "0755" or less with the following command: $ stat -c "%a %n" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/rsyslogd /sbin/augenrules 755 /sbin/auditctl 755 /sbin/aureport 755 /sbin/ausearch 750 /sbin/autrace 755 /sbin/auditd 755 /sbin/rsyslogd 755 /sbin/augenrules If any of the audit tool files have a mode more permissive than "0755", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271827`

### Rule: OL 9 cron configuration directories must have a mode of 0700 or less permissive.

**Rule ID:** `SV-271827r1092193_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Service configuration files enable or disable features of their respective services that if configured incorrectly can lead to insecure and vulnerable configurations. Therefore, service configuration files should have the correct access rights to prevent unauthorized changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures permissions of the cron directories with the following command: $ find /etc/cron* -type d | xargs stat -c "%a %n" 700 /etc/cron.d 700 /etc/cron.daily 700 /etc/cron.hourly 700 /etc/cron.monthly 700 /etc/cron.weekly If any cron configuration directory is more permissive than "700", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271828`

### Rule: OL 9 cron configuration files directory must be group-owned by root.

**Rule ID:** `SV-271828r1092196_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Service configuration files enable or disable features of their respective services that if configured incorrectly can lead to insecure and vulnerable configurations; therefore, service configuration files should be owned by the correct group to prevent unauthorized changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures group ownership of all cron configuration files with the following command: $ stat -c "%G %n" /etc/cron* root /etc/cron.d root /etc/cron.daily root /etc/cron.deny root /etc/cron.hourly root /etc/cron.monthly root /etc/crontab root /etc/cron.weekly If any crontab is not group owned by root, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271829`

### Rule: OL 9 cron configuration files directory must be owned by root.

**Rule ID:** `SV-271829r1092199_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Service configuration files enable or disable features of their respective services that if configured incorrectly can lead to insecure and vulnerable configurations; therefore, service configuration files must be owned by the correct group to prevent unauthorized changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures ownership of all cron configuration files with the command: $ stat -c "%U %n" /etc/cron* root /etc/cron.d root /etc/cron.daily root /etc/cron.deny root /etc/cron.hourly root /etc/cron.monthly root /etc/crontab root /etc/cron.weekly If any crontab is not owned by root, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271830`

### Rule: OL 9 /etc/crontab file must have mode 0600.

**Rule ID:** `SV-271830r1092202_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Service configuration files enable or disable features of their respective services that if configured incorrectly can lead to insecure and vulnerable configurations; therefore, service configuration files must have the correct access rights to prevent unauthorized changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures permissions of /etc/crontab with the following command: $ stat -c "%a %n" /etc/crontab 0600 If /etc/crontab does not have a mode of "0600", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271831`

### Rule: OL 9 must be configured so that the root account is the only account having unrestricted access to the system.

**Rule ID:** `SV-271831r1092205_rule`
**Severity:** high

**Description:**
<VulnDiscussion>An account has root authority if it has a user identifier (UID) of "0". Multiple accounts with a UID of "0" afford more opportunity for potential intruders to guess a password for a privileged account. Proper configuration of sudo is recommended to afford multiple system administrators access to root privileges in an accountable manner.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures only the "root" account to have a UID "0" assignment with the following command: $ awk -F: '$3 == 0 {print $1}' /etc/passwd root If any accounts other than "root" have a UID of "0", this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-271832`

### Rule: OL 9 duplicate User IDs (UIDs) must not exist for interactive users.

**Rule ID:** `SV-271832r1092208_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, interactive users must be identified and authenticated to prevent potential misuse and compromise of the system. Satisfies: SRG-OS-000104-GPOS-00051, SRG-OS-000121-GPOS-00062, SRG-OS-000042-GPOS-00020</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 contains no duplicate UIDs for interactive users with the following command: $ sudo awk -F ":" 'list[$3]++{print $1, $3}' /etc/passwd If output is produced and the accounts listed are interactive user accounts, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271833`

### Rule: OL 9 local interactive users must have a home directory assigned in the /etc/passwd file.

**Rule ID:** `SV-271833r1092607_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If local interactive users are not assigned a valid home directory, there is no place for the storage and control of files they should own.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures interactive users on the system have a home directory assigned with the following command: $ sudo awk -F: '($3>=1000)&&($7 !~ /nologin/){print $1, $3, $6}' /etc/passwd smithk:x:1000:1000:smithk:/home/smithk:/bin/bash scsaustin:x:1001:1001:scsaustin:/home/scsaustin:/bin/bash djohnson:x:1002:1002:djohnson:/home/djohnson:/bin/bash Inspect the output and verify that all interactive users (normally users with a user identifier [UID] greater that 1000) have a home directory defined. If users home directory is not defined, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-271834`

### Rule: OL 9 interactive users must have a primary group that exists.

**Rule ID:** `SV-271834r1092214_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user is assigned the Group Identifier (GID) of a group that does not exist on the system, and a group with the GID is subsequently created, the user may have unintended rights to any files associated with the group.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 interactive users have a valid GID. Check that the interactive users have a valid GID with the following command: $ sudo pwck -qr If the system has any interactive users with duplicate GIDs, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-271835`

### Rule: OL 9 groups must have unique Group ID (GID).

**Rule ID:** `SV-271835r1092217_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, groups must be identified uniquely to prevent potential misuse and compromise of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 contains no duplicate GIDs for interactive users with the following command: $ cut -d : -f 3 /etc/group | uniq -d If the system has duplicate GIDs, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-271836`

### Rule: OL 9 must configure SELinux context type to allow the use of a nondefault faillock tally directory.

**Rule ID:** `SV-271836r1092637_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Not having the correct SELinux context on the faillock directory may lead to unauthorized access to the directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system does not have SELinux enabled and enforcing a targeted policy, or if the pam_faillock module is not configured for use, this requirement is Not Applicable. Verify that OL 9 configures the SELinux context type to allow the use of a nondefault faillock tally directory. Verify the location of the nondefault tally directory for the pam_faillock module with the following command: $ grep 'dir =' /etc/security/faillock.conf dir = /var/log/faillock Check the security context type of the nondefault tally directory with the following command: $ ls -Zd /var/log/faillock unconfined_u:object_r:faillog_t:s0 /var/log/faillock If the security context type of the nondefault tally directory is not "faillog_t", this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-271837`

### Rule: OL 9 must configure the use of the pam_faillock.so module in the /etc/pam.d/system-auth file.

**Rule ID:** `SV-271837r1092223_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the pam_faillock.so module is not loaded, the system will not correctly lockout accounts to prevent password guessing attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures the pam_faillock.so module to exist in the "/etc/pam.d/system-auth" file with the following command: $ grep pam_faillock.so /etc/pam.d/system-auth auth required pam_faillock.so preauth auth required pam_faillock.so authfail account required pam_faillock.so If the pam_faillock.so module is not present in the "/etc/pam.d/system-auth" file with the "preauth" line listed before pam_unix.so, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-271838`

### Rule: OL 9 must configure the use of the pam_faillock.so module in the /etc/pam.d/password-auth file.

**Rule ID:** `SV-271838r1092226_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the pam_faillock.so module is not loaded, the system will not correctly lockout accounts to prevent password guessing attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures the pam_faillock.so module to exist in the "/etc/pam.d/password-auth" file with the following command: $ grep pam_faillock.so /etc/pam.d/password-auth auth required pam_faillock.so preauth auth required pam_faillock.so authfail account required pam_faillock.so If the pam_faillock.so module is not present in the "/etc/pam.d/password-auth" file with the "preauth" line listed before pam_unix.so, this is a finding.

## Group: SRG-OS-000329-GPOS-00128

**Group ID:** `V-271839`

### Rule: OL 9 must automatically lock an account when three unsuccessful logon attempts occur.

**Rule ID:** `SV-271839r1092229_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. Satisfies: SRG-OS-000329-GPOS-00128, SRG-OS-000021-GPOS-00005</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to lock an account after three unsuccessful logon attempts with the command: $ grep 'deny =' /etc/security/faillock.conf deny = 3 If the "deny" option is not set to "3" or less (but not "0"), is missing or commented out, this is a finding.

## Group: SRG-OS-000329-GPOS-00128

**Group ID:** `V-271840`

### Rule: OL 9 must automatically lock the root account until the root account is released by an administrator when three unsuccessful logon attempts occur during a 15-minute time period.

**Rule ID:** `SV-271840r1092232_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, also known as brute-forcing, is reduced. Limits are imposed by locking the account. Satisfies: SRG-OS-000329-GPOS-00128, SRG-OS-000021-GPOS-00005</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to lock the root account after three unsuccessful logon attempts with the command: $ grep even_deny_root /etc/security/faillock.conf even_deny_root If the "even_deny_root" option is not set, is missing or commented out, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-271841`

### Rule: OL 9 must log username information when unsuccessful logon attempts occur.

**Rule ID:** `SV-271841r1092235_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing of these events, it may be harder or impossible to identify what an attacker did after an attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 logs username information when unsuccessful logon attempts occur. Verify the "/etc/security/faillock.conf" file is configured to log username information when unsuccessful logon attempts occur with the following command: $ grep audit /etc/security/faillock.conf audit If the "audit" option is not set, is missing, or is commented out, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-271842`

### Rule: OL 9 must ensure account lockouts persist.

**Rule ID:** `SV-271842r1092238_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Having lockouts persist across reboots ensures that account is only unlocked by an administrator. If the lockouts did not persist across reboots, an attacker could simply reboot the system to continue brute force attacks against the accounts on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 ensures that account lockouts persist. Verify the "/etc/security/faillock.conf" file is configured use a nondefault faillock directory to ensure contents persist after reboot with the following command: $ grep 'dir =' /etc/security/faillock.conf dir = /var/log/faillock If the "dir" option is not set to a nondefault documented tally log directory, is missing or commented out, this is a finding.

## Group: SRG-OS-000123-GPOS-00064

**Group ID:** `V-271843`

### Rule: OL 9 must automatically expire temporary accounts within 72 hours.

**Rule ID:** `SV-271843r1094969_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Temporary accounts are privileged or nonprivileged accounts that are established during pressing circumstances, such as new software or hardware configuration or an incident response, where the need for prompt account activation requires bypassing normal account authorization procedures. If any inactive temporary accounts are left enabled on the system and are not either manually removed or automatically expired within 72 hours, the security posture of the system will be degraded and exposed to exploitation by unauthorized users or insider threat actors. Temporary accounts are different from emergency accounts. Emergency accounts, also known as "last resort" or "break glass" accounts, are local logon accounts enabled on the system for emergency use by authorized system administrators to manage a system when standard logon methods are failing or not available. Emergency accounts are not subject to manual removal or scheduled expiration requirements. The automatic expiration of temporary accounts may be extended as needed by the circumstances, but it must not be extended indefinitely. A documented permanent account should be established for privileged users who need long-term maintenance accounts. Satisfies: SRG-OS-000123-GPOS-00064, SRG-OS-000002-GPOS-00002</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures temporary accounts to be provisioned with an expiration date of 72 hours. For every existing temporary account, run the following command to obtain its account expiration information: $ chage -l <temporary_account_name> | grep -i "account expires" Verify each of these accounts has an expiration date set within 72 hours. If any temporary accounts have no expiration date set or do not expire within 72 hours, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271844`

### Rule: OL 9 local interactive user home directories defined in the /etc/passwd file must exist.

**Rule ID:** `SV-271844r1092244_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a local interactive user has a home directory defined that does not exist, the user may be given access to the / directory as the current working directory upon logon. This could create a denial of service because the user would not be able to access their logon configuration files, and it may give them visibility to system files they normally would not be able to access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 assigned home directories of all interactive users on the system exist with the following command: $ sudo pwck -r The output should not return any interactive users. If users home directory does not exist, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271845`

### Rule: OL 9 system accounts must not have an interactive login shell.

**Rule ID:** `SV-271845r1092247_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensuring shells are not given to system accounts upon login makes it more difficult for attackers to make use of system accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures system accounts to not have an interactive login shell with the following command: $ awk -F: '($3<1000){print $1 ":" $3 ":" $7}' /etc/passwd root:0:/bin/bash bin:1:/sbin/nologin daemon:2:/sbin/nologin adm:3:/sbin/nologin lp:4:/sbin/nologin Identify the system accounts from this listing that do not have a nologin shell. If any system account (other than the root account) has a login shell and it is not documented with the information system security officer (ISSO), this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271846`

### Rule: OL 9 local interactive user accounts must be assigned a home directory upon creation.

**Rule ID:** `SV-271846r1092250_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If local interactive users are not assigned a valid home directory, there is no place for the storage and control of files they should own.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 local interactive users are assigned a home directory upon creation with the following command: $ grep -i create_home /etc/login.defs CREATE_HOME yes If the value for "CREATE_HOME" parameter is not set to "yes", the line is missing, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271847`

### Rule: OL 9 must be configured so that executable search paths within the initialization files of all local interactive users must only contain paths that resolve to the system default or the users home directory.

**Rule ID:** `SV-271847r1092253_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The executable search path (typically the PATH environment variable) contains a list of directories for the shell to search to find executables. If this path includes the current working directory (other than the users home directory), executables in these directories may be executed instead of system commands. This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon or two consecutive colons, this is interpreted as the current working directory. If deviations from the default system search path for the local interactive user are required, they must be documented with the information system security officer (ISSO).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 local interactive user initialization file executable search path statements do not contain statements that will reference a working directory other than user home directories with the following commands: $ sudo grep -i path= /home/*/.* /home/[localinteractiveuser]/.bash_profile:PATH=$PATH:$HOME/.local/bin:$HOME/bin If any local interactive user initialization files have executable search path statements that include directories outside of their home directory and is not documented with the ISSO as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271848`

### Rule: OL 9 must set the umask value to 077 for all local interactive user accounts.

**Rule ID:** `SV-271848r1092256_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The umask controls the default access mode assigned to newly created files. A umask of 077 limits new files to mode 600 or less permissive. Although umask can be represented as a four-digit number, the first digit representing special access modes is typically ignored or required to be "0". This requirement applies to the globally configured system defaults and the local interactive user defaults for each account on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures the default umask for all local interactive users to be "077". Identify the locations of all local interactive user home directories by looking at the "/etc/passwd" file. Check all local interactive user initialization files for interactive users with the following command: Note: The example is for a system that is configured to create users home directories in the "/home" directory. $ grep -ri umask /home/ /home/wadea/.bash_history:grep -i umask /etc/bashrc /etc/csh.cshrc /etc/profile /home/wadea/.bash_history:grep -i umask /etc/login.defs If any local interactive user initialization files are found to have a umask statement that sets a value less restrictive than "077", this is a finding.

## Group: SRG-OS-000118-GPOS-00060

**Group ID:** `V-271849`

### Rule: OL 9 must disable account identifiers (individuals, groups, roles, and devices) after 35 days of inactivity.

**Rule ID:** `SV-271849r1092259_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Disabling inactive accounts ensures that accounts which may not have been responsibly removed are not available to attackers who may have compromised their credentials. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. Satisfies: SRG-OS-000118-GPOS-00060, SRG-OS-000590-GPOS-00110</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 account identifiers (individuals, groups, roles, and devices) are disabled after 35 days of inactivity with the following command: Check the account inactivity value by performing the following command: $ sudo grep -i inactive /etc/default/useradd INACTIVE=35 If "INACTIVE" is set to "-1", a value greater than "35", or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-271850`

### Rule: OL 9 must enforce a delay of at least four seconds between logon prompts following a failed logon attempt.

**Rule ID:** `SV-271850r1092262_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Increasing the time between a failed authentication attempt and reprompting to enter credentials helps to slow a single-threaded brute force attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 enforces a delay of at least four seconds between console logon prompts following a failed logon attempt with the following command: $ grep -i fail_delay /etc/login.defs FAIL_DELAY 4 If the value of "FAIL_DELAY" is not set to "4" or greater, or the line is commented out, this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-271851`

### Rule: OL 9 remote access methods must be monitored.

**Rule ID:** `SV-271851r1092265_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Logging remote access methods can be used to trace the decrease in the risks associated with remote user access management. It can also be used to spot cyberattacks and ensure ongoing compliance with organizational policies surrounding the use of remote access methods.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 monitors all remote access methods. Check that remote access methods are being logged by running the following command: $ grep -rE '(auth.\*|authpriv.\*|daemon.\*)' /etc/rsyslog.conf authpriv.* /var/log/secure If "auth.*", "authpriv.*" or "daemon.*" are not configured to be logged, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-271852`

### Rule: OL 9 must be configured to forward audit records via TCP to a different system or media from the system being audited via rsyslog.

**Rule ID:** `SV-271852r1092608_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. OL 9 installation media provides "rsyslogd", a system utility providing support for message logging. Support for both internet and Unix domain sockets enables this utility to support both local and remote logging. Coupling this utility with "gnutls" (a secure communications library implementing the SSL, TLS, and DTLS protocols) creates a method to securely encrypt and offload auditing. Rsyslog provides three ways to forward message: the traditional UDP transport, which is extremely lossy but standard; the plain TCP based transport, which loses messages only during certain situations but is widely available; and the RELP transport, which does not lose messages but is currently available only as part of the rsyslogd 3.15.0 and above. Examples of each configuration: UDP *.* @remotesystemname TCP *.* @@remotesystemname RELP *.* :omrelp:remotesystemname:2514 Note that a port number was given as there is no standard port for RELP. Satisfies: SRG-OS-000479-GPOS-00224, SRG-OS-000342-GPOS-00133</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 audit system offloads audit records onto a different system or media from the system being audited via rsyslog using TCP with the following command: $ grep @@ /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.conf:*.* @@[remoteloggingserver]:[port] If a remote server is not configured, or the line is commented out, ask the system administrator (SA) to indicate how the audit logs are offloaded to a different system or media. If there is no evidence that the audit logs are being offloaded to another system or media, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271853`

### Rule: OL 9 must use cron logging.

**Rule ID:** `SV-271853r1092271_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cron logging can be used to trace the successful or unsuccessful execution of cron jobs. It can also be used to spot intrusions into the use of the cron facility by unauthorized and malicious users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 rsyslog is configured to log cron events with the following command: Note: If another logging package is used, substitute the utility configuration file for "/etc/rsyslog.conf" or "/etc/rsyslog.d/*.conf" files. $ grep -s cron /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.conf:*.info;mail.none;authpriv.none;cron.none /var/log/messages /etc/rsyslog.conf:cron.* /var/log/cron If the command does not return a response, check for cron logging all facilities with the following command: $ grep -s /var/log/messages /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.conf:*.info;mail.none;authpriv.none;cron.none /var/log/messages If "rsyslog" is not logging messages for the cron facility or all facilities, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-271854`

### Rule: OL 9 must authenticate the remote logging server for offloading audit logs via rsyslog.

**Rule ID:** `SV-271854r1092274_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. OL 9 installation media provides "rsyslogd", a system utility providing support for message logging. Support for both internet and Unix domain sockets enables this utility to support both local and remote logging. Coupling this utility with "gnutls" (a secure communications library implementing the SSL, TLS, and DTLS protocols) creates a method to securely encrypt and offload auditing. "Rsyslog" supported authentication modes include: anon - anonymous authentication x509/fingerprint - certificate fingerprint authentication x509/certvalid - certificate validation only x509/name - certificate validation and subject name authentication Satisfies: SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 authenticates the remote logging server for off-loading audit logs with the following command: $ grep -i '$ActionSendStreamDriverAuthMode' /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.conf:$ActionSendStreamDriverAuthMode x509/name If the value of the "$ActionSendStreamDriverAuthMode" option is not set to "x509/name" or the line is commented out, ask the system administrator (SA) to indicate how the audit logs are offloaded to a different system or media. If there is no evidence that the transfer of the audit logs being offloaded to another system or media is encrypted, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-271855`

### Rule: OL 9 must encrypt the transfer of audit records offloaded onto a different system or media from the system being audited via rsyslog.

**Rule ID:** `SV-271855r1092277_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. OL 9 installation media provides "rsyslogd", a system utility providing support for message logging. Support for both internet and Unix domain sockets enables this utility to support both local and remote logging. Coupling this utility with "gnutls" (a secure communications library implementing the SSL, TLS, and DTLS protocols) creates a method to securely encrypt and offload auditing. "Rsyslog" supported authentication modes include: anon - anonymous authentication x509/fingerprint - certificate fingerprint authentication x509/certvalid - certificate validation only x509/name - certificate validation and subject name authentication Satisfies: SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 encrypts audit records offloaded onto a different system or media from the system being audited via rsyslog with the following command: $ grep -i '$ActionSendStreamDriverMode' /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.conf:$ActionSendStreamDriverMode 1 If the value of the "$ActionSendStreamDriverMode" option is not set to "1" or the line is commented out, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-271856`

### Rule: OL 9 must encrypt via the gtls driver the transfer of audit records offloaded onto a different system or media from the system being audited via rsyslog.

**Rule ID:** `SV-271856r1092280_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. OL 9 installation media provides "rsyslogd", a system utility providing support for message logging. Support for both internet and Unix domain sockets enables this utility to support both local and remote logging. Coupling this utility with "gnutls" (a secure communications library implementing the SSL, TLS, and DTLS protocols) creates a method to securely encrypt and offload auditing. Satisfies: SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 uses the gtls driver to encrypt audit records offloaded onto a different system or media from the system being audited with the following command: $ grep -i '$DefaultNetstreamDriver' /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.conf:$DefaultNetstreamDriver gtls If the value of the "$DefaultNetstreamDriver" option is not set to "gtls" or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271857`

### Rule: OL 9 must be configured so that the rsyslog daemon does not accept log messages from other servers unless the server is being used for log aggregation.

**Rule ID:** `SV-271857r1092283_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unintentionally running a rsyslog server accepting remote messages puts the system at increased risk. Malicious rsyslog messages sent to the server could exploit vulnerabilities in the server software itself, could introduce misleading information into the system's logs, or could fill the system's storage leading to a denial of service. If the system is intended to be a log aggregation server, its use must be documented with the information system security officer (ISSO).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is not configured to receive remote logs using rsyslog with the following commands: $ grep -i modload /etc/rsyslog.conf /etc/rsyslog.d/* $ModLoad imtcp $ModLoad imrelp $ grep -i serverrun /etc/rsyslog.conf /etc/rsyslog.d/* $InputTCPServerRun 514 $InputRELPServerRun 514 Note: An error about no files or directories may be returned. This is not a finding. If any lines are returned by the command, then rsyslog is configured to receive remote messages, and this is a finding.

## Group: SRG-OS-000420-GPOS-00186

**Group ID:** `V-271858`

### Rule: OL 9 must protect against or limit the effects of denial-of-service (DoS) attacks by ensuring rate-limiting measures on impacted network interfaces are implemented.

**Rule ID:** `SV-271858r1092286_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of OL 9 to mitigate the impact of DoS attacks that have occurred or are ongoing on system availability. For each system, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exists to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or establishing memory partitions). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 nftables is configured to allow rate limits on any connection to the system with the following command: $ sudo grep -i firewallbackend /etc/firewalld/firewalld.conf # FirewallBackend FirewallBackend=nftables If the "nftables" is not set as the "FirewallBackend" default, this is a finding.

## Group: SRG-OS-000299-GPOS-00117

**Group ID:** `V-271859`

### Rule: OL 9 wireless network adapters must be disabled.

**Rule ID:** `SV-271859r1092289_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement applies to wireless peripheral technologies (e.g., wireless mice, keyboards, displays, etc.) used with OL 9 systems. Wireless peripherals (e.g., Wi-Fi/Bluetooth/IR keyboards, mice and pointing devices, and near field communications [NFC]) present a unique challenge by creating an open, unsecured port on a computer. Wireless peripherals must meet DOD requirements for wireless data transmission and be approved for use by the authorizing official (AO). Even though some wireless peripherals, such as mice and pointing devices, do not ordinarily carry information that need to be protected, modification of communications with these wireless peripherals may be used to compromise the OL 9 operating system. Satisfies: SRG-OS-000299-GPOS-00117, SRG-OS-000300-GPOS-00118, SRG-OS-000424-GPOS-00188, SRG-OS-000481-GPOS-00481</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For systems that do not have physical wireless network radios, this requirement is Not Applicable. Verify that OL 9 allows no wireless interfaces to be configured on the system with the following command: $ nmcli device status DEVICE TYPE STATE CONNECTION virbr0 bridge connected virbr0 wlp7s0 wifi connected wifiSSID enp6s0 ethernet disconnected -- p2p-dev-wlp7s0 wifi-p2p disconnected -- lo loopback unmanaged -- virbr0-nic tun unmanaged -- If a wireless interface is configured and has not been documented and approved by the information system security officer (ISSO), this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271860`

### Rule: OL 9 must configure a DNS processing mode set be Network Manager.

**Rule ID:** `SV-271860r1092292_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure that DNS resolver settings are respected, a DNS mode in Network Manager must be configured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 has a DNS mode configured in Network Manager. $ NetworkManager --print-config [main] dns=none If the DNS key under main does not exist or is not set to "none" or "default", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271861`

### Rule: OL 9 systems using Domain Name Servers (DNS) resolution must have at least two name servers configured.

**Rule ID:** `SV-271861r1092295_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To provide availability for name resolution services, multiple redundant name servers are mandated. A failure in name resolution could lead to the failure of security functions requiring name resolution, which may include time synchronization, centralized authentication, and remote system logging.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures name servers used by the system with the following command: $ grep nameserver /etc/resolv.conf nameserver 192.168.1.2 nameserver 192.168.1.3 If less than two lines are returned that are not commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271862`

### Rule: OL 9 network interfaces must not be in promiscuous mode.

**Rule ID:** `SV-271862r1092298_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network interfaces in promiscuous mode allow for the capture of all network traffic visible to the system. If unauthorized individuals can access these applications, it may allow them to collect information such as logon IDs, passwords, and key exchanges between systems. If the system is being used to perform a network troubleshooting function, the use of these tools must be documented with the information systems security officer (ISSO) and restricted to only authorized personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 configures network interfaces to not operate in promiscuous mode with the following command: $ ip link | grep -i promisc If network interfaces are found on the system in promiscuous mode and their use has not been approved by the ISSO and documented, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271863`

### Rule: OL 9 must not have unauthorized IP tunnels configured.

**Rule ID:** `SV-271863r1092639_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IP tunneling mechanisms can be used to bypass network filtering. If tunneling is required, it must be documented with the information system security officer (ISSO).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 does not have unauthorized IP tunnels configured. Determine if the IPsec service is active with the following command: $ systemctl status ipsec ipsec.service - Internet Key Exchange (IKE) Protocol Daemon for IPsec Loaded: loaded (/usr/lib/systemd/system/ipsec.service; disabled) Active: inactive (dead) If the IPsec service is active, check for configured IPsec connections ("conn"), with the following command: $ grep -rni conn /etc/ipsec.conf /etc/ipsec.d/ Verify any returned results are documented with the ISSO. If the IPsec tunnels are active and not approved, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271864`

### Rule: OL 9 must ignore Internet Protocol version 4 (IPv4) Internet Control Message Protocol (ICMP) redirect messages.

**Rule ID:** `SV-271864r1092304_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack. This feature of the IPv4 protocol has few legitimate uses. It should be disabled unless absolutely required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 will not accept IPv4 ICMP redirect messages. Check the value of all "accept_redirects" variables with the following command: $ sysctl net.ipv4.conf.all.accept_redirects net.ipv4.conf.all.accept_redirects = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271865`

### Rule: OL 9 must not forward Internet Protocol version 4 (IPv4) source-routed packets.

**Rule ID:** `SV-271865r1092307_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when IPv4 forwarding is enabled and the system is functioning as a router. Accepting source-routed packets in the IPv4 protocol has few legitimate uses. It must be disabled unless it is absolutely required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 will not accept IPv4 source-routed packets. Check the value of the all "accept_source_route" variables with the following command: $ sysctl net.ipv4.conf.all.accept_source_route net.ipv4.conf.all.accept_source_route = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271866`

### Rule: OL 9 must log IPv4 packets with impossible addresses.

**Rule ID:** `SV-271866r1092310_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The presence of "martian" packets (which have impossible addresses) as well as spoofed packets, source-routed packets, and redirects could be a sign of nefarious network activity. Logging these packets enables this activity to be detected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 logs IPv4 martian packets. Check the value of the accept source route variable with the following command: $ sysctl net.ipv4.conf.all.log_martians net.ipv4.conf.all.log_martians = 1 If the returned line does not have a value of "1", a line is not returned, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271867`

### Rule: OL 9 must log IPv4 packets with impossible addresses by default.

**Rule ID:** `SV-271867r1092313_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The presence of "martian" packets (which have impossible addresses) as well as spoofed packets, source-routed packets, and redirects could be a sign of nefarious network activity. Logging these packets enables this activity to be detected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 logs IPv4 martian packets by default. Check the value of the accept source route variable with the following command: $ sysctl net.ipv4.conf.default.log_martians net.ipv4.conf.default.log_martians = 1 If the returned line does not have a value of "1", a line is not returned, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271868`

### Rule: OL 9 must use reverse path filtering on all IPv4 interfaces.

**Rule ID:** `SV-271868r1092316_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling reverse path filtering drops packets with source addresses that should not have been able to be received on the interface on which they were received. It must not be used on systems that are routers for complicated networks but is helpful for end hosts and routers serving small networks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 uses reverse path filtering on all IPv4 interfaces with the following commands: $ sysctl net.ipv4.conf.all.rp_filter net.ipv4.conf.all.rp_filter = 1 If the returned line does not have a value of "1", or a line is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271869`

### Rule: OL 9 must prevent IPv4 Internet Control Message Protocol (ICMP) redirect messages from being accepted.

**Rule ID:** `SV-271869r1092319_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack. This feature of the IPv4 protocol has few legitimate uses. It must be disabled unless absolutely required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 will not accept IPv4 ICMP redirect messages. Check the value of the default "accept_redirects" variables with the following command: $ sysctl net.ipv4.conf.default.accept_redirects net.ipv4.conf.default.accept_redirects = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271870`

### Rule: OL 9 must not forward IPv4 source-routed packets by default.

**Rule ID:** `SV-271870r1092322_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. Accepting source-routed packets in the IPv4 protocol has few legitimate uses. It must be disabled unless it is absolutely required, such as when IPv4 forwarding is enabled and the system is legitimately functioning as a router.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 does not accept IPv4 source-routed packets by default. Check the value of the accept source route variable with the following command: $ sysctl net.ipv4.conf.default.accept_source_route net.ipv4.conf.default.accept_source_route = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271871`

### Rule: OL 9 must use a reverse-path filter for IPv4 network traffic, when possible, by default.

**Rule ID:** `SV-271871r1092325_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling reverse path filtering drops packets with source addresses that should not have been able to be received on the interface on which they were received. It must not be used on systems that are routers for complicated networks but is helpful for end hosts and routers serving small networks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 uses reverse path filtering on IPv4 interfaces with the following commands: $ sysctl net.ipv4.conf.default.rp_filter net.ipv4.conf.default.rp_filter = 1 If the returned line does not have a value of "1", or a line is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271872`

### Rule: OL 9 must not enable IPv4 packet forwarding unless the system is a router.

**Rule ID:** `SV-271872r1092328_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this capability is used when not required, system network information may be unnecessarily transmitted across the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is not performing IPv4 packet forwarding, unless the system is a router. Check that IPv4 forwarding is disabled using the following command: $ sysctl net.ipv4.conf.all.forwarding net.ipv4.conf.all.forwarding = 0 If the IPv4 forwarding value is not "0" and is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271873`

### Rule: OL 9 must not respond to Internet Control Message Protocol (ICMP) echoes sent to a broadcast address.

**Rule ID:** `SV-271873r1092331_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Responding to broadcast (ICMP) echoes facilitates network mapping and provides a vector for amplification attacks. Ignoring ICMP echo requests (pings) sent to broadcast or multicast addresses makes the system slightly more difficult to enumerate on the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 does not respond to ICMP echoes sent to a broadcast address. Check the value of the "icmp_echo_ignore_broadcasts" variable with the following command: $ sysctl net.ipv4.icmp_echo_ignore_broadcasts net.ipv4.icmp_echo_ignore_broadcasts = 1 If the returned line does not have a value of "1", a line is not returned, or the retuned line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271874`

### Rule: OL 9 must limit the number of bogus Internet Control Message Protocol (ICMP) response errors logs.

**Rule ID:** `SV-271874r1092612_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some routers will send responses to broadcast frames that violate RFC-1122, which fills up a log file system with many useless error messages. An attacker may take advantage of this and attempt to flood the logs with bogus error logs. Ignoring bogus ICMP error responses reduces log size, although some activity would not be logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 limits the number of bogus ICMP response errors logs. The runtime status of the net.ipv4.icmp_ignore_bogus_error_responses kernel parameter can be queried by running the following command: $ sysctl net.ipv4.icmp_ignore_bogus_error_responses net.ipv4.icmp_ignore_bogus_error_responses = 1 If "net.ipv4.icmp_ignore_bogus_error_responses" is not set to "1", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271875`

### Rule: OL 9 must not send Internet Control Message Protocol (ICMP) redirects.

**Rule ID:** `SV-271875r1092337_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages contain information from the system's route table possibly revealing portions of the network topology. The ability to send ICMP redirects is only appropriate for systems acting as routers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 does not IPv4 ICMP redirect messages. Check the value of the "all send_redirects" variables with the following command: $ sysctl net.ipv4.conf.all.send_redirects net.ipv4.conf.all.send_redirects = 0 If "net.ipv4.conf.all.send_redirects" is not set to "0" and is not documented with the information system security officer (ISSO) as an operational requirement or is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271876`

### Rule: OL 9 must not allow interfaces to perform Internet Control Message Protocol (ICMP) redirects by default.

**Rule ID:** `SV-271876r1092641_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages contain information from the system's route table possibly revealing portions of the network topology. The ability to send ICMP redirects is only appropriate for systems acting as routers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 does not allow interfaces to perform Internet Protocol version 4 (IPv4) ICMP redirects by default. Check the value of the "default send_redirects" variables with the following command: $ sysctl net.ipv4.conf.default.send_redirects net.ipv4.conf.default.send_redirects=0 If "net.ipv4.conf.default.send_redirects" is not set to "0" and is not documented with the information system security officer (ISSO) as an operational requirement or is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271877`

### Rule: OL 9 must not accept router advertisements on all IPv6 interfaces.

**Rule ID:** `SV-271877r1092343_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An illicit router advertisement message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If IPv6 is disabled on the system, this requirement is Not Applicable. Verify that OL 9 does not accept router advertisements on all IPv6 interfaces, unless the system is a router. Determine if router advertisements are not accepted by using the following command: $ sysctl net.ipv6.conf.all.accept_ra net.ipv6.conf.all.accept_ra = 0 If the "accept_ra" value is not "0" and is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271878`

### Rule: OL 9 must ignore IPv6 Internet Control Message Protocol (ICMP) redirect messages.

**Rule ID:** `SV-271878r1092346_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An illicit ICMP redirect message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If IPv6 is disabled on the system, this requirement is Not Applicable. Verify that OL 9 ignores IPv6 ICMP redirect messages. Check the value of the "accept_redirects" variables with the following command: $ sysctl net.ipv6.conf.all.accept_redirects net.ipv6.conf.all.accept_redirects = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271879`

### Rule: OL 9 must not forward IPv6 source-routed packets.

**Rule ID:** `SV-271879r1092349_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when forwarding is enabled and the system is functioning as a router.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If IPv6 is disabled on the system, this requirement is Not Applicable. Verify that OL 9 does not accept IPv6 source-routed packets. Check the value of the accept source route variable with the following command: $ sysctl net.ipv6.conf.all.accept_source_route net.ipv6.conf.all.accept_source_route = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271880`

### Rule: OL 9 must not enable IPv6 packet forwarding unless the system is a router.

**Rule ID:** `SV-271880r1092352_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IP forwarding permits the kernel to forward packets from one network interface to another. The ability to forward packets between two networks is only appropriate for systems acting as routers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If IPv6 is disabled on the system, this requirement is Not Applicable. Verify that OL 9 is not performing IPv6 packet forwarding, unless the system is a router. Check that IPv6 forwarding is disabled using the following commands: $ sysctl net.ipv6.conf.all.forwarding net.ipv6.conf.all.forwarding = 0 If the IPv6 forwarding value is not "0" and is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271881`

### Rule: OL 9 must not accept router advertisements on all IPv6 interfaces by default.

**Rule ID:** `SV-271881r1092355_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An illicit router advertisement message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If IPv6 is disabled on the system, this requirement is Not Applicable. Verify that OL 9 does not accept router advertisements on all IPv6 interfaces by default unless the system is a router. Determine if router advertisements are not accepted by default by using the following command: $ sysctl net.ipv6.conf.default.accept_ra net.ipv6.conf.default.accept_ra = 0 If the "accept_ra" value is not "0" and is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271882`

### Rule: OL 9 must prevent IPv6 Internet Control Message Protocol (ICMP) redirect messages from being accepted.

**Rule ID:** `SV-271882r1092358_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If IPv6 is disabled on the system, this requirement is Not Applicable. Verify that OL 9 will not accept IPv6 ICMP redirect messages. Check the value of the default "accept_redirects" variables with the following command: $ sysctl net.ipv6.conf.default.accept_redirects net.ipv6.conf.default.accept_redirects = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-271883`

### Rule: OL 9 must not forward IPv6 source-routed packets by default.

**Rule ID:** `SV-271883r1092361_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when forwarding is enabled and the system is functioning as a router. Accepting source-routed packets in the IPv6 protocol has few legitimate uses. It must be disabled unless it is absolutely required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If IPv6 is disabled on the system, this requirement is Not Applicable. Verify that OL 9 does not accept IPv6 source-routed packets by default. Check the value of the accept source route variable with the following command: $ sysctl net.ipv6.conf.default.accept_source_route net.ipv6.conf.default.accept_source_route = 0 If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this is a finding.

## Group: SRG-OS-000420-GPOS-00186

**Group ID:** `V-271884`

### Rule: OL 9 must be configured to use TCP syncookies.

**Rule ID:** `SV-271884r1092364_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Denial of service (DoS) is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Managing excess capacity ensures that sufficient capacity is available to counter flooding attacks. Employing increased capacity and service redundancy may reduce the susceptibility to some DoS attacks. Managing excess capacity may include, for example, establishing selected usage priorities, quotas, or partitioning. Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00071</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 is configured to use IPv4 TCP syncookies. Determine if syncookies are used with the following command: Check the status of the kernel.perf_event_paranoid kernel parameter. $ sysctl net.ipv4.tcp_syncookies net.ipv4.tcp_syncookies = 1 Check that the configuration files are present to enable this kernel parameter.

## Group: SRG-OS-000462-GPOS-00206

**Group ID:** `V-271885`

### Rule: OL 9 audit system must protect logon UIDs from unauthorized change.

**Rule ID:** `SV-271885r1092367_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If modification of login user identifiers (UIDs) is not prevented, they can be changed by nonprivileged users and make auditing complicated or impossible. Satisfies: SRG-OS-000462-GPOS-00206, SRG-OS-000475-GPOS-00220, SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 audit system configuration prevents unauthorized changes to logon UIDs with the following command: $ sudo grep -i immutable /etc/audit/audit.rules --loginuid-immutable If the "--loginuid-immutable" option is not returned in the "/etc/audit/audit.rules", or the line is commented out, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-271886`

### Rule: OL 9 audit system must protect auditing rules from unauthorized change.

**Rule ID:** `SV-271886r1092370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit OL 9 system activity. In immutable mode, unauthorized users cannot execute changes to the audit system to potentially hide malicious activity and then put the audit rules back. A system reboot would be noticeable, and a system administrator could then investigate the unauthorized changes. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that OL 9 audit system configuration prevents unauthorized changes with the following command: $ sudo grep "^\s*[^#]" /etc/audit/audit.rules | tail -1 -e 2 If the audit system is not set to be immutable by adding the "-e 2" option to the end of "/etc/audit/audit.rules", this is a finding.

## Group: SRG-OS-000403-GPOS-00182

**Group ID:** `V-271901`

### Rule: OL 9 must only allow the use of DOD PKI-established certificate authorities for authentication in the establishment of protected sessions to OL 9.

**Rule ID:** `SV-271901r1092415_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted certificate authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DOD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DOD-approved CA, trust of this CA has not been established. The DOD will only accept PKI-certificates obtained from a DOD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of SSL/TLS certificates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify OL 9 only allows the use of DOD PKI-established certificate authorities using the following command: $ trust list pkcs11:id=%7C%42%96%AE%DE%4B%48%3B%FA%92%F8%9E%8C%CF%6D%8B%A9%72%37%95;type=cert type: certificate label: ISRG Root X2 trust: anchor category: authority If any nonapproved CAs are returned, this is a finding.

