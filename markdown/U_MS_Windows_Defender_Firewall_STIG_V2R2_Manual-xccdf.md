# STIG Benchmark: Microsoft Windows Defender Firewall with Advanced Security Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-241989`

### Rule: Windows Defender Firewall with Advanced Security must be enabled when connected to a domain.

**Rule ID:** `SV-241989r922928_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack. To be effective, it must be enabled and properly configured. This setting enables the firewall when connected to the domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is not a member of a domain, the Domain Profile requirements can be marked NA. If the following policy-based registry value exists and is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile\ Value Name: EnableFirewall Type: REG_DWORD Value: 0x00000001 (1) If the policy-based registry value does not exist, verify the following registry value. If it is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\DomainProfile\ Value Name: EnableFirewall Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-241990`

### Rule: Windows Defender Firewall with Advanced Security must be enabled when connected to a private network.

**Rule ID:** `SV-241990r922930_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack. To be effective, it must be enabled and properly configured. This setting enables the firewall when connected to a private network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following policy-based registry value exists and is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\WindowsFirewall\PrivateProfile\ Value Name: EnableFirewall Type: REG_DWORD Value: 0x00000001 (1) If the policy-based registry value does not exist, verify the following registry value. If it is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile\ Value Name: EnableFirewall Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-241991`

### Rule: Windows Defender Firewall with Advanced Security must be enabled when connected to a public network.

**Rule ID:** `SV-241991r922932_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack. To be effective, it must be enabled and properly configured. This setting enables the firewall when connected to a public network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the following policy-based registry value exists and is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile\ Value Name: EnableFirewall Type: REG_DWORD Value: 0x00000001 (1) If the policy-based registry value does not exist, verify the following registry value. If it is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\PublicProfile\ Value Name: EnableFirewall Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-241992`

### Rule: Windows Defender Firewall with Advanced Security must block unsolicited inbound connections when connected to a domain.

**Rule ID:** `SV-241992r922934_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack. To be effective, it must be enabled and properly configured. Unsolicited inbound connections may be malicious attempts to gain access to a system. Unsolicited inbound connections, for which there is no rule allowing the connection, will be blocked in the domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is not a member of a domain, the Domain Profile requirements can be marked NA. If the system is a member of a domain and the firewall's Domain Profile is not enabled (see V-17415), this requirement is also a finding. If the following policy-based registry value exists and is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile\ Value Name: DefaultInboundAction Type: REG_DWORD Value: 0x00000001 (1) If the policy-based registry value does not exist, verify the following registry value. If it is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\DomainProfile\ Value Name: DefaultInboundAction Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-241993`

### Rule: Windows Defender Firewall with Advanced Security must allow outbound connections, unless a rule explicitly blocks the connection when connected to a domain.

**Rule ID:** `SV-241993r922936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack. To be effective, it must be enabled and properly configured. Outbound connections are allowed in the domain, unless a rule explicitly blocks the connection. This allows normal outbound communication, which could be restricted as necessary with additional rules.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is not a member of a domain, the Domain Profile requirements can be marked NA. If the system is a member of a domain and the firewall's Domain Profile is not enabled (see V-17415), this requirement is also a finding. If the following policy-based registry value exists and is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile\ Value Name: DefaultOutboundAction Type: REG_DWORD Value: 0x00000000 (0) If the policy-based registry value does not exist, verify the following registry value. If it is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\DomainProfile\ Value Name: DefaultOutboundAction Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-241994`

### Rule: Windows Defender Firewall with Advanced Security log size must be configured for domain connections.

**Rule ID:** `SV-241994r922938_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack. To be effective, it must be enabled and properly configured. The firewall log file size for a domain connection will be set to ensure enough capacity is allocated for audit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is not a member of a domain, the Domain Profile requirements can be marked NA. If the system is a member of a domain and the firewall's Domain Profile is not enabled (see V-17415), this requirement is also a finding. If the following policy-based registry value exists and is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile\Logging\ Value Name: LogFileSize Type: REG_DWORD Value: 0x00004000 (16384) (or greater) If the policy-based registry value does not exist, verify the following registry value. If it is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\DomainProfile\Logging\ Value Name: LogFileSize Type: REG_DWORD Value: 0x00004000 (16384) (or greater)

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-241995`

### Rule: Windows Defender Firewall with Advanced Security must log dropped packets when connected to a domain.

**Rule ID:** `SV-241995r922940_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack. To be effective, it must be enabled and properly configured. Logging of dropped packets for a domain connection will be enabled to maintain an audit trail of potential issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is not a member of a domain, the Domain Profile requirements can be marked NA. If the system is a member of a domain and the firewall's Domain Profile is not enabled (see V-17415), this requirement is also a finding. If the following policy-based registry value exists and is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile\Logging\ Value Name: LogDroppedPackets Type: REG_DWORD Value: 0x00000001 (1) If the policy-based registry value does not exist, verify the following registry value. If it is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\DomainProfile\Logging\ Value Name: LogDroppedPackets Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-241996`

### Rule: Windows Defender Firewall with Advanced Security must log successful connections when connected to a domain.

**Rule ID:** `SV-241996r922942_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack. To be effective, it must be enabled and properly configured. Logging of successful connections for a domain connection will be enabled to maintain an audit trail if issues are discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is not a member of a domain, the Domain Profile requirements can be marked NA. If the system is a member of a domain and the firewall's Domain Profile is not enabled (see V-17415), this requirement is also a finding. If the following policy-based registry value exists and is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile\Logging\ Value Name: LogSuccessfulConnections Type: REG_DWORD Value: 0x00000001 (1) If the policy-based registry value does not exist, verify the following registry value. If it is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\DomainProfile\Logging\ Value Name: LogSuccessfulConnections Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-241997`

### Rule: Windows Defender Firewall with Advanced Security must block unsolicited inbound connections when connected to a private network.

**Rule ID:** `SV-241997r922944_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack. To be effective, it must be enabled and properly configured. Unsolicited inbound connections may be malicious attempts to gain access to a system. Unsolicited inbound connections, for which there is no rule allowing the connection, will be blocked on a private network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the firewall's Private Profile is not enabled (see V-17416), this requirement is also a finding. If the following policy-based registry value exists and is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\WindowsFirewall\PrivateProfile\ Value Name: DefaultInboundAction Type: REG_DWORD Value: 0x00000001 (1) If the policy-based registry value does not exist, verify the following registry value. If it is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile\ Value Name: DefaultInboundAction Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-241998`

### Rule: Windows Defender Firewall with Advanced Security must allow outbound connections, unless a rule explicitly blocks the connection when connected to a private network.

**Rule ID:** `SV-241998r922946_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack. To be effective, it must be enabled and properly configured. Outbound connections are allowed on a private network, unless a rule explicitly blocks the connection. This allows normal outbound communication, which could be restricted as necessary with additional rules.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the firewall's Private Profile is not enabled (see V-17416), this requirement is also a finding. If the following policy-based registry value exists and is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\WindowsFirewall\PrivateProfile\ Value Name: DefaultOutboundAction Type: REG_DWORD Value: 0x00000000 (0) If the policy-based registry value does not exist, verify the following registry value. If it is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile\ Value Name: DefaultOutboundAction Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-241999`

### Rule: Windows Defender Firewall with Advanced Security log size must be configured for private network connections.

**Rule ID:** `SV-241999r922948_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack. To be effective, it must be enabled and properly configured. The firewall log file size for a private connection will be set to ensure enough capacity is allocated for audit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the firewall's Private Profile is not enabled (see V-17416), this requirement is also a finding. If the following policy-based registry value exists and is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\WindowsFirewall\PrivateProfile\Logging\ Value Name: LogFileSize Type: REG_DWORD Value: 0x00004000 (16384) (or greater) If the policy-based registry value does not exist, verify the following registry value. If it is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile\Logging\ Value Name: LogFileSize Type: REG_DWORD Value: 0x00004000 (16384) (or greater)

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-242000`

### Rule: Windows Defender Firewall with Advanced Security must log dropped packets when connected to a private network.

**Rule ID:** `SV-242000r922950_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack. To be effective, it must be enabled and properly configured. Logging of dropped packets for a private network connection will be enabled to maintain an audit trail of potential issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the firewall's Private Profile is not enabled (see V-17416), this requirement is also a finding. If the following policy-based registry value exists and is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\WindowsFirewall\PrivateProfile\Logging\ Value Name: LogDroppedPackets Type: REG_DWORD Value: 0x00000001 (1) If the policy-based registry value does not exist, verify the following registry value. If it is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile\Logging\ Value Name: LogDroppedPackets Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-242001`

### Rule: Windows Defender Firewall with Advanced Security must log successful connections when connected to a private network.

**Rule ID:** `SV-242001r922952_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack. To be effective, it must be enabled and properly configured. Logging of successful connections for a private network connection will be enabled to maintain an audit trail if issues are discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the firewall's Private Profile is not enabled (see V-17416), this requirement is also a finding. If the following policy-based registry value exists and is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\WindowsFirewall\PrivateProfile\Logging\ Value Name: LogSuccessfulConnections Type: REG_DWORD Value: 0x00000001 (1) If the policy-based registry value does not exist, verify the following registry value. If it is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile\Logging\ Value Name: LogSuccessfulConnections Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-242002`

### Rule: Windows Defender Firewall with Advanced Security must block unsolicited inbound connections when connected to a public network.

**Rule ID:** `SV-242002r922954_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack. To be effective, it must be enabled and properly configured. Unsolicited inbound connections may be malicious attempts to gain access to a system. Unsolicited inbound connections, for which there is no rule allowing the connection, will be blocked on a public network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the firewall's Public Profile is not enabled (see V-17417), this requirement is also a finding. If the following policy-based registry value exists and is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile\ Value Name: DefaultInboundAction Type: REG_DWORD Value: 0x00000001 (1) If the policy-based registry value does not exist, verify the following registry value. If it is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\PublicProfile\ Value Name: DefaultInboundAction Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-242003`

### Rule: Windows Defender Firewall with Advanced Security must allow outbound connections, unless a rule explicitly blocks the connection when connected to a public network.

**Rule ID:** `SV-242003r922956_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack. To be effective, it must be enabled and properly configured. Outbound connections are allowed on a public network, unless a rule explicitly blocks the connection. This allows normal outbound communication, which could be restricted as necessary with additional rules.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the firewall's Public Profile is not enabled (see V-17417), this requirement is also a finding. If the following policy-based registry value exists and is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile\ Value Name: DefaultOutboundAction Type: REG_DWORD Value: 0x00000000 (0) If the policy-based registry value does not exist, verify the following registry value. If it is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\PublicProfile\ Value Name: DefaultOutboundAction Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-242004`

### Rule: Windows Defender Firewall with Advanced Security local firewall rules must not be merged with Group Policy settings when connected to a public network.

**Rule ID:** `SV-242004r922958_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack. To be effective, it must be enabled and properly configured. Local firewall rules will not be merged with Group Policy settings on a public network to prevent Group Policy settings from being changed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is not a member of a domain, this is NA. If the firewall's Public Profile is not enabled (see V-17417), this requirement is also a finding. Verify the registry value below. If this registry value does not exist or is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile\ Value Name: AllowLocalPolicyMerge Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-242005`

### Rule: Windows Defender Firewall with Advanced Security local connection rules must not be merged with Group Policy settings when connected to a public network.

**Rule ID:** `SV-242005r922960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack. To be effective, it must be enabled and properly configured. Local connection rules will not be merged with Group Policy settings on a public network to prevent Group Policy settings from being changed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is not a member of a domain, this is NA. If the firewall's Public Profile is not enabled (see V-17417), this requirement is also a finding. Verify the registry value below. If this registry value does not exist or is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile\ Value Name: AllowLocalIPsecPolicyMerge Type: REG_DWORD Value: 0x00000000 (0)

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-242006`

### Rule: Windows Defender Firewall with Advanced Security log size must be configured for public network connections.

**Rule ID:** `SV-242006r922962_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack. To be effective, it must be enabled and properly configured. The firewall log file size for a public network connection will be set to ensure enough capacity is allocated for audit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the firewall's Public Profile is not enabled (see V-17417), this requirement is also a finding. If the following policy-based registry value exists and is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile\Logging\ Value Name: LogFileSize Type: REG_DWORD Value: 0x00004000 (16384) (or greater) If the policy-based registry value does not exist, verify the following registry value. If it is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\PublicProfile\Logging\ Value Name: LogFileSize Type: REG_DWORD Value: 0x00004000 (16384) (or greater)

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-242007`

### Rule: Windows Defender Firewall with Advanced Security must log dropped packets when connected to a public network.

**Rule ID:** `SV-242007r922964_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack. To be effective, it must be enabled and properly configured. Logging of dropped packets for a public network connection will be enabled to maintain an audit trail of potential issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the firewall's Public Profile is not enabled (see V-17417), this requirement is also a finding. If the following policy-based registry value exists and is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile\Logging\ Value Name: LogDroppedPackets Type: REG_DWORD Value: 0x00000001 (1) If the policy-based registry value does not exist, verify the following registry value. If it is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\PublicProfile\Logging\ Value Name: LogDroppedPackets Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-242008`

### Rule: Windows Defender Firewall with Advanced Security must log successful connections when connected to a public network.

**Rule ID:** `SV-242008r922966_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A firewall provides a line of defense against attack. To be effective, it must be enabled and properly configured. Logging of successful connections for a public network connection will be enabled to maintain an audit trail if issues are discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the firewall's Public Profile is not enabled (see V-17417), this requirement is also a finding. If the following policy-based registry value exists and is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile\Logging\ Value Name: LogSuccessfulConnections Type: REG_DWORD Value: 0x00000001 (1) If the policy-based registry value does not exist, verify the following registry value. If it is not configured as specified, this is a finding. Registry Hive: HKEY_LOCAL_MACHINE Registry Path: \SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\PublicProfile\Logging\ Value Name: LogSuccessfulConnections Type: REG_DWORD Value: 0x00000001 (1)

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-242009`

### Rule: Inbound exceptions to the firewall on domain workstations must only allow authorized remote management hosts.

**Rule ID:** `SV-242009r922967_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing inbound access to domain workstations from other systems may allow lateral movement across systems if credentials are compromised. Limiting inbound connections only from authorized remote management systems will help limit this exposure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is NA for servers and non domain workstations. Verify firewall exceptions for inbound connections on domain workstations only allow authorized management systems and remote management hosts. Review inbound firewall exception rules in Microsoft Defender Firewall with Advanced Security. Firewall rules can be complex and should be reviewed with the firewall administrator. One method for restricting inbound connections is to only allow exceptions for a specific scope of remote IP addresses. If allowed inbound exceptions are not limited to authorized management systems and remote management hosts, this is a finding.

