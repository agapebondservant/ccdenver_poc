# STIG Benchmark: VMware vSphere 8.0 Virtual Machine Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258703`

### Rule: Virtual machines (VMs) must have copy operations disabled.

**Rule ID:** `SV-258703r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Copy and paste operations are disabled by default; however, explicitly disabling this feature will enable audit controls to verify this setting is correct. Copy, paste, drag and drop, or GUI copy/paste operations between the guest operating system and the remote console could provide the means for an attacker to compromise the VM.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to Edit Settings >> Advanced Parameters. Verify the "isolation.tools.copy.disable" value is set to "true". or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM "VM Name" | Get-AdvancedSetting -Name isolation.tools.copy.disable If the virtual machine advanced setting "isolation.tools.copy.disable" is not set to "true", this is a finding. If the virtual machine advanced setting "isolation.tools.copy.disable" does not exist, this is not a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258704`

### Rule: Virtual machines (VMs) must have drag and drop operations disabled.

**Rule ID:** `SV-258704r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Copy and paste operations are disabled by default; however, explicitly disabling this feature will enable audit controls to verify this setting is correct. Copy, paste, drag and drop, or GUI copy/paste operations between the guest operating system and the remote console could provide the means for an attacker to compromise the VM.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to Edit Settings >> Advanced Parameters. Verify the "isolation.tools.dnd.disable" value is set to "true". or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM "VM Name" | Get-AdvancedSetting -Name isolation.tools.dnd.disable If the virtual machine advanced setting "isolation.tools.dnd.disable" is not set to "true", this is a finding. If the virtual machine advanced setting "isolation.tools.dnd.disable" does not exist, this is not a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258705`

### Rule: Virtual machines (VMs) must have paste operations disabled.

**Rule ID:** `SV-258705r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Copy and paste operations are disabled by default; however, explicitly disabling this feature will enable audit controls to verify this setting is correct. Copy, paste, drag and drop, or GUI copy/paste operations between the guest operating system and the remote console could provide the means for an attacker to compromise the VM.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to Edit Settings >> Advanced Parameters. Verify the "isolation.tools.paste.disable" value is set to "true". or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM "VM Name" | Get-AdvancedSetting -Name isolation.tools.paste.disable If the virtual machine advanced setting "isolation.tools.paste.disable" is not set to "true", this is a finding. If the virtual machine advanced setting "isolation.tools.paste.disable" does not exist, this is not a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258706`

### Rule: Virtual machines (VMs) must have virtual disk shrinking disabled.

**Rule ID:** `SV-258706r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Shrinking a virtual disk reclaims unused space in it. If there is empty space in the disk, this process reduces the amount of space the virtual disk occupies on the host drive. Normal users and processes (those without root or administrator privileges) within virtual machines have the capability to invoke this procedure. However, if this is done repeatedly, the virtual disk can become unavailable while this shrinking is being performed, effectively causing a denial of service. In most datacenter environments, disk shrinking is not done, so this feature must be disabled. Repeated disk shrinking can make a virtual disk unavailable. The capability to shrink is available to nonadministrative users operating within the VM's guest operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to Edit Settings >> Advanced Parameters. Verify the "isolation.tools.diskShrink.disable" value is set to "true". or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM "VM Name" | Get-AdvancedSetting -Name isolation.tools.diskShrink.disable If the virtual machine advanced setting "isolation.tools.diskShrink.disable" is not set to "true", this is a finding. If the virtual machine advanced setting "isolation.tools.diskShrink.disable" does not exist, this is not a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258707`

### Rule: Virtual machines (VMs) must have virtual disk wiping disabled.

**Rule ID:** `SV-258707r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Shrinking and wiping (erasing) a virtual disk reclaims unused space in it. If there is empty space in the disk, this process reduces the amount of space the virtual disk occupies on the host drive. Normal users and processes (those without root or administrator privileges) within virtual machines have the capability to invoke this procedure. However, if this is done repeatedly, the virtual disk can become unavailable while this shrinking is being performed, effectively causing a denial of service. In most datacenter environments, disk shrinking is not done, so this feature must be disabled. Repeated disk shrinking can make a virtual disk unavailable. The capability to wipe (erase) is available to nonadministrative users operating within the VM's guest operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to Edit Settings >> Advanced Parameters. Verify the "isolation.tools.diskWiper.disable" value is set to "true". or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM "VM Name" | Get-AdvancedSetting -Name isolation.tools.diskWiper.disable If the virtual machine advanced setting "isolation.tools.diskWiper.disable" is not set to "true", this is a finding. If the virtual machine advanced setting "isolation.tools.diskWiper.disable" does not exist, this is not a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258708`

### Rule: Virtual machines (VMs) must limit console sharing.

**Rule ID:** `SV-258708r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, more than one user at a time can connect to remote console sessions. When multiple sessions are activated, each terminal window receives a notification about the new session. If an administrator in the VM logs in using a VMware remote console during their session, a nonadministrator in the VM might connect to the console and observe the administrator's actions. Also, this could result in an administrator losing console access to a VM. For example, if a jump box is being used for an open console session and the administrator loses connection to that box, the console session remains open. Allowing two console sessions permits debugging via a shared session. For the highest security, allow only one remote console session at a time.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to Edit Settings >> Advanced Parameters. Verify the "RemoteDisplay.maxConnections" value is set to "1". or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM "VM Name" | Get-AdvancedSetting -Name RemoteDisplay.maxConnections If the virtual machine advanced setting "RemoteDisplay.maxConnections" does not exist or is not set to "1", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258709`

### Rule: Virtual machines (VMs) must limit informational messages from the virtual machine to the VMX file.

**Rule ID:** `SV-258709r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The configuration file containing these name-value pairs is limited to a size of 1MB. If not limited, VMware tools in the guest operating system are capable of sending a large and continuous data stream to the host. This 1MB capacity should be sufficient for most cases, but this value can change if necessary. The value can be increased if large amounts of custom information are being stored in the configuration file. The default limit is 1MB.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to Edit Settings >> Advanced Parameters. Verify the "tools.setinfo.sizeLimit" value is set to "1048576". or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM "VM Name" | Get-AdvancedSetting -Name tools.setinfo.sizeLimit If the virtual machine advanced setting "tools.setinfo.sizeLimit" is not set to "1048576", this is a finding. If the virtual machine advanced setting "tools.setinfo.sizeLimit" does not exist, this is not a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258710`

### Rule: Virtual machines (VMs) must prevent unauthorized removal, connection, and modification of devices.

**Rule ID:** `SV-258710r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In a virtual machine, users and processes without root or administrator privileges can connect or disconnect devices, such as network adaptors and CD-ROM drives, and can modify device settings. Use the virtual machine settings editor or configuration editor to remove unneeded or unused hardware devices. To use the device again, prevent a user or running process in the virtual machine from connecting, disconnecting, or modifying a device from within the guest operating system. By default, a rogue user with nonadministrator privileges in a virtual machine can: 1. Connect a disconnected CD-ROM drive and access sensitive information on the media left in the drive. 2. Disconnect a network adaptor to isolate the virtual machine from its network, which is a denial of service. 3. Modify settings on a device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to Edit Settings >> Advanced Parameters. Verify the "isolation.device.connectable.disable" value is set to "true". or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM "VM Name" | Get-AdvancedSetting -Name isolation.device.connectable.disable If the virtual machine advanced setting "isolation.device.connectable.disable" is not set to "true", this is a finding. If the virtual machine advanced setting "isolation.device.connectable.disable" does not exist, this is not a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258711`

### Rule: Virtual machines (VMs) must not be able to obtain host information from the hypervisor.

**Rule ID:** `SV-258711r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If enabled, a VM can obtain detailed information about the physical host. The default value for the parameter is FALSE. This setting should not be TRUE unless a particular VM requires this information for performance monitoring. An adversary could use this information to inform further attacks on the host.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to Edit Settings >> Advanced Parameters. Verify the "tools.guestlib.enableHostInfo" value is set to "false". or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM "VM Name" | Get-AdvancedSetting -Name tools.guestlib.enableHostInfo If the virtual machine advanced setting "tools.guestlib.enableHostInfo" is not set to "false", this is a finding. If the virtual machine advanced setting "tools.guestlib.enableHostInfo" does not exist, this is not a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258712`

### Rule: Virtual machines (VMs) must have shared salt values disabled.

**Rule ID:** `SV-258712r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>When salting is enabled (Mem.ShareForceSalting=1 or 2) to share a page between two virtual machines, both salt and the content of the page must be same. A salt value is a configurable advanced option for each virtual machine. The salt values can be specified manually in the virtual machine's advanced settings with the new option "sched.mem.pshare.salt". If this option is not present in the virtual machine's advanced settings, the value of the "vc.uuid" option is taken as the default value. Because the "vc.uuid" is unique to each virtual machine, by default Transparent Page Sharing (TPS) happens only among the pages belonging to a particular virtual machine (Intra-VM).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to Edit Settings >> Advanced Parameters. Verify the "sched.mem.pshare.salt" setting does not exist. or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM "VM Name" | Get-AdvancedSetting -Name sched.mem.pshare.salt If the virtual machine advanced setting "sched.mem.pshare.salt" exists, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258713`

### Rule: Virtual machines (VMs) must disable access through the "dvfilter" network Application Programming Interface (API).

**Rule ID:** `SV-258713r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>An attacker might compromise a VM by using the "dvFilter" API. Configure only VMs that need this access to use the API.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to Edit Settings >> Advanced Parameters. Verify the settings with the format "ethernet*.filter*.name" do not exist. or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM "VM Name" | Get-AdvancedSetting -Name "ethernet*.filter*.name*" If the virtual machine advanced setting "ethernet*.filter*.name" exists and dvfilters are not in use, this is a finding. If the virtual machine advanced setting "ethernet*.filter*.name" exists and the value is not valid, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258714`

### Rule: Virtual machines (VMs) must be configured to lock when the last console connection is closed.

**Rule ID:** `SV-258714r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When accessing the VM console, the guest operating system must be locked when the last console user disconnects, limiting the possibility of session hijacking. This setting only applies to Windows-based VMs with VMware tools installed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to Edit Settings >> VM Options >> VMware Remote Console Options. Verify the option "Lock the guest operating system when the last remote user disconnects" is checked. or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM "VM Name" | Get-AdvancedSetting -Name tools.guest.desktop.autolock If the virtual machine advanced setting "tools.guest.desktop.autolock" is not set to "true", this is a finding. If the virtual machine advanced setting "tools.guest.desktop.autolock" does not exist, this is not a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258715`

### Rule: Virtual machines (VMs) must disable 3D features when not required.

**Rule ID:** `SV-258715r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>For performance reasons, it is recommended that 3D acceleration be disabled on virtual machines that do not require 3D functionality (e.g., most server workloads or desktops not using 3D applications).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to Edit Settings. Expand the "Video card" and verify the "Enable 3D Support" checkbox is unchecked. or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM "VM Name" | Get-AdvancedSetting -Name mks.enable3d If the virtual machine advanced setting "mks.enable3d" exists and is not set to "false", this is a finding. If the virtual machine advanced setting "mks.enable3d" does not exist, this is not a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258716`

### Rule: Virtual machines (VMs) must enable encryption for vMotion.

**Rule ID:** `SV-258716r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>vMotion migrations in vSphere 6.0 and earlier transferred working memory and CPU state information in clear text over the vMotion network. As of vSphere 6.5, this transfer can be transparently encrypted using 256-bit AES-GCM with negligible performance impact. vSphere enables encrypted vMotion by default as "Opportunistic", meaning that encrypted channels are used where supported, but the operation will continue in plain text where encryption is not supported. For example, when vMotioning between two hosts, encryption will always be used. However, because 6.0 and earlier releases do not support this feature, vMotion from a 7.0 host to a 6.0 host would be allowed but would not be encrypted. If the encryption is set to "Required", vMotions to unsupported hosts will fail. This must be set to "Opportunistic" or "Required".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to Edit Settings >> VM Options >> Encryption. or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM | Where {($_.ExtensionData.Config.MigrateEncryption -eq "disabled")} If the "Encrypted vMotion" setting does not have a value of "Opportunistic" or "Required", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258717`

### Rule: Virtual machines (VMs) must enable encryption for Fault Tolerance.

**Rule ID:** `SV-258717r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Fault Tolerance log traffic can be encrypted. This could contain sensitive data from the protected machine's memory or CPU instructions. vSphere Fault Tolerance performs frequent checks between a primary VM and secondary VM so the secondary VM can quickly resume from the last successful checkpoint. The checkpoint contains the VM state that has been modified since the previous checkpoint. When Fault Tolerance is turned on, FT encryption is set to "Opportunistic" by default, which means it enables encryption only if both the primary and secondary host are capable of encryption.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Virtual Machine does not have Fault Tolerance enabled, this is not applicable. For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to Edit Settings >> VM Options >> Encryption. or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM | Where {($_.ExtensionData.Config.FtEncryptionMode -ne "ftEncryptionOpportunistic") -and ($_.ExtensionData.Config.FtEncryptionMode -ne "ftEncryptionRequired")} If the "Encrypted FT" setting does not have a value of "Opportunistic" or "Required", this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258718`

### Rule: Virtual machines (VMs) must configure log size.

**Rule ID:** `SV-258718r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ESXi hypervisor maintains logs for each individual VM by default. These logs contain information including but not limited to power events, system failure information, tools status and activity, time sync, virtual hardware changes, vMotion migrations, and machine clones. By default, the size of these logs is unlimited, and they are only rotated on vMotion or power events. This can cause storage issues at scale for VMs that do not vMotion or power cycle often.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to Edit Settings >> Advanced Parameters. Verify the "log.rotateSize" value is set to "2048000". or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM "VM Name" | Get-AdvancedSetting -Name log.rotateSize If the virtual machine advanced setting "log.rotateSize" is not set to "2048000", this is a finding. If the virtual machine advanced setting "log.rotateSize" does NOT exist, this is NOT a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258719`

### Rule: Virtual machines (VMs) must configure log retention.

**Rule ID:** `SV-258719r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ESXi hypervisor maintains logs for each individual VM by default. These logs contain information including but not limited to power events, system failure information, tools status and activity, time sync, virtual hardware changes, vMotion migrations, and machine clones. By default, 10 of these logs are retained. This is normally sufficient for most environments, but this configuration must be verified and maintained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to Edit Settings >> Advanced Parameters. Verify the "log.keepOld" value is set to "10". or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM "VM Name" | Get-AdvancedSetting -Name log.keepOld If the virtual machine advanced setting "log.keepOld" is not set to "10", this is a finding. If the virtual machine advanced setting "log.keepOld" does NOT exist, this is NOT a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258720`

### Rule: Virtual machines (VMs) must enable logging.

**Rule ID:** `SV-258720r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ESXi hypervisor maintains logs for each individual VM by default. These logs contain information including, but not limited to, power events, system failure information, tools status and activity, time sync, virtual hardware changes, vMotion migrations and machine clones. Due to the value these logs provide for the continued availability of each VM and potential security incidents, these logs must be enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to Edit Settings >> VM Options >> Advanced. Ensure that the checkbox next to "Enable logging" is checked. or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM | Where {$_.ExtensionData.Config.Flags.EnableLogging -ne "True"} If logging is not enabled, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258721`

### Rule: Virtual machines (VMs) must not use independent, nonpersistent disks.

**Rule ID:** `SV-258721r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The security issue with nonpersistent disk mode is that successful attackers, with a simple shutdown or reboot, might undo or remove any traces they were ever on the machine. To safeguard against this risk, production virtual machines should be set to use persistent disk mode; additionally, ensure activity within the VM is logged remotely on a separate server, such as a syslog server or equivalent Windows-based event collector. Without a persistent record of activity on a VM, administrators might never know whether they have been attacked or hacked. There can be valid use cases for these types of disks, such as with an application presentation solution where read-only disks are desired, and such cases should be identified and documented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to "Edit Settings". Review the attached hard disks and verify they are not configured as independent nonpersistent disks. or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM "VM Name" | Get-HardDisk | Select Parent, Name, Filename, DiskType, Persistence | FT -AutoSize If the virtual machine has attached disks that are in independent nonpersistent mode and are not documented, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258722`

### Rule: Virtual machines (VMs) must remove unneeded floppy devices.

**Rule ID:** `SV-258722r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensure no device is connected to a virtual machine if it is not required. For example, floppy, serial, and parallel ports are rarely used for virtual machines in a data center environment, and CD/DVD drives are usually connected only temporarily during software installation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Floppy drives are no longer visible through the vSphere Client and must be done via the Application Programming Interface (API) or PowerCLI. From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM | Get-FloppyDrive | Select Parent, Name, ConnectionState If a virtual machine has a floppy drive connected, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258723`

### Rule: Virtual machines (VMs) must remove unneeded CD/DVD devices.

**Rule ID:** `SV-258723r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Ensure no device is connected to a virtual machine if it is not required. For example, floppy, serial, and parallel ports are rarely used for virtual machines in a data center environment, and CD/DVD drives are usually connected only temporarily during software installation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to "Edit Settings". Review the VMs hardware and verify no CD/DVD drives are connected. or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM | Get-CDDrive | Where {$_.extensiondata.connectable.connected -eq $true} | Select Parent,Name If a virtual machine has a CD/DVD drive connected other than temporarily, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258724`

### Rule: Virtual machines (VMs) must remove unneeded parallel devices.

**Rule ID:** `SV-258724r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensure no device is connected to a virtual machine if it is not required. For example, floppy, serial, and parallel ports are rarely used for virtual machines in a data center environment, and CD/DVD drives are usually connected only temporarily during software installation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Parallel devices are no longer visible through the vSphere Client and must be done via the Application Programming Interface (API) or PowerCLI. From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM | Where {$_.ExtensionData.Config.Hardware.Device.DeviceInfo.Label -match "parallel"} If a virtual machine has a parallel device present, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258725`

### Rule: Virtual machines (VMs) must remove unneeded serial devices.

**Rule ID:** `SV-258725r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensure no device is connected to a virtual machine if it is not required. For example, floppy, serial, and parallel ports are rarely used for virtual machines in a data center environment, and CD/DVD drives are usually connected only temporarily during software installation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to "Edit Settings". Review the VMs hardware and verify no serial devices exist. or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM | Where {$_.ExtensionData.Config.Hardware.Device.DeviceInfo.Label -match "serial"} If a virtual machine has a serial device present, this is a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258726`

### Rule: Virtual machines (VMs) must remove unneeded USB devices.

**Rule ID:** `SV-258726r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensure no device is connected to a virtual machine if it is not required. For example, floppy, serial, and parallel ports are rarely used for virtual machines in a data center environment, and CD/DVD drives are usually connected only temporarily during software installation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, right-click the Virtual Machine and go to "Edit Settings". Review the VM's hardware and verify no USB devices exist. or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following commands: Get-VM | Where {$_.ExtensionData.Config.Hardware.Device.DeviceInfo.Label -match "usb"} Get-VM | Get-UsbDevice If a virtual machine has any USB devices or USB controllers present, this is a finding. If USB smart card readers are used to pass smart cards through the VM console to a VM, the use of a USB controller and USB devices for that purpose is not a finding.

## Group: SRG-OS-000480-VMM-002000

**Group ID:** `V-258727`

### Rule: Virtual machines (VMs) must disable DirectPath I/O devices when not required.

**Rule ID:** `SV-258727r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>VMDirectPath I/O (PCI passthrough) enables direct assignment of hardware PCI functions to VMs. This gives the VM access to the PCI functions with minimal intervention from the ESXi host. This is a powerful feature for legitimate applications such as virtualized storage appliances, backup appliances, dedicated graphics, etc., but it also allows a potential attacker highly privileged access to underlying hardware and the PCI bus.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each virtual machine do the following: From the vSphere Client, view the Summary tab. Review the PCI devices section and verify none exist. or From a PowerCLI command prompt while connected to the ESXi host or vCenter server, run the following command: Get-VM "VM Name" | Get-PassthroughDevice If the virtual machine has passthrough devices present, and the specific device returned is not approved, this is a finding.

