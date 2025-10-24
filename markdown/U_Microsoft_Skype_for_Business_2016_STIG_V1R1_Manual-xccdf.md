# STIG Benchmark: Microsoft Skype for Business 2016 Security Technical Implementation Guide

---

**Version:** 1

**Description:**
The Microsoft Skype for Business 2016 Security Technical Implementation Guide (STIG) is published as a tool to improve the security of Department of Defense (DoD) information systems. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000516

**Group ID:** `V-70901`

### Rule: The ability to store user passwords in Skype must be disabled.


**Rule ID:** `SV-85525r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allows Microsoft Lync to store user passwords. If you enable this policy setting, Microsoft Lync can store a password on request from the user. If you disable this policy setting, Microsoft Lync cannot store a password. If you do not configure this policy setting and the user logs on to a domain, Microsoft Lync does not store the password. If you do not configure this policy setting and the user does not log on to a domain (for example, if the user logs on to a workgroup), Microsoft Lync can store the password. Note: You can configure this policy setting under both Computer Configuration and User Configuration, but the policy setting under Computer Configuration takes precedence. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Skype for Business 2016 -> Microsoft Lync Feature Policies "Allow storage of user passwords" is set to "Disabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\office\16.0\lync Criteria: If the value savepassword is REG_DWORD = 0, this is not a finding.

## Group: SRG-APP-000219

**Group ID:** `V-70903`

### Rule: Session Initiation Protocol (SIP) security mode must be configured.


**Rule ID:** `SV-85527r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When Lync connects to the server, it supports various authentication mechanisms. This policy allows the user to specify whether Digest and Basic authentication are supported. Disabled (default): NTLM/Kerberos/TLS-DSK/Digest/Basic Enabled: Authentication mechanisms: NTLM/Kerberos/TLS-DSK Gal Download: Requires HTTPS if user is not logged in as an internal user. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Skype for Business 2016 -> Microsoft Lync Feature Policies "Configure SIP security mode" is set to "Enabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\office\16.0\lync Criteria: If the value enablesiphighsecuritymode is REG_DWORD = 1, this is not a finding.

## Group: SRG-APP-000219

**Group ID:** `V-70905`

### Rule: In the event a secure Session Initiation Protocol (SIP) connection fails, the connection must be restricted from resorting to the unencrypted HTTP.


**Rule ID:** `SV-85529r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Prevents from HTTP being used for SIP connection in case TLS or TCP fail. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the policy value for Computer Configuration -> Administrative Templates -> Skype for Business 2016 -> Microsoft Lync Feature Policies "Disable HTTP fallback for SIP connection" is set to "Enabled". Procedure: Use the Windows Registry Editor to navigate to the following key: HKLM\Software\Policies\Microsoft\office\16.0\lync Criteria: If the value disablehttpconnect is REG_DWORD = 1, this is not a finding.

