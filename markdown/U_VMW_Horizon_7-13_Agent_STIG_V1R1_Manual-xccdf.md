# STIG Benchmark: VMware Horizon 7.13 Agent Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246860`

### Rule: The Horizon Agent must require TLS connections.

**Rule ID:** `SV-246860r768540_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Horizon Agent has the capability to be backward compatible with legacy clients, circa View 5.2, which do not support newer TLS connections. By default, the agent can fall back to this non-TLS mode when being accessed by a legacy client. The Horizon Agent must be configured to not support these legacy clients and enforce TLS connections as mandatory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the vdm_agent*.admx templates are added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops or RDS hosts. Navigate to Computer Configuration >> Policies >> Administrative Templates >> VMware View Agent Configuration >> Agent Security. Double-click the "Accept SSL encrypted framework channel" setting. If "Accept SSL encrypted framework channel" is not "Enabled" and set to "Enforce", this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246861`

### Rule: The Horizon Agent must only run allowed scripts on user connect.

**Rule ID:** `SV-246861r768543_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Horizon Agent has the capability to run scripts on user connect, disconnect, and reconnect. While this can be useful in setting up a user environment, in certain circumstances, the running of such scripts should be delegated to native windows capabilities where possible. These settings are powerful and can serve as a potential space for a privileged attacker to persist. By default, this setting is unconfigured. Should the site require this setting, ensure it is audited and its configuration valid at all times.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the vdm_agent*.admx templates are added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops or RDS hosts. Navigate to Computer Configuration >> Policies >> Administrative Templates >> VMware View Agent Configuration >> Agent Configuration. Double-click the "CommandsToRunOnConnect" setting. If "CommandsToRunOnConnect" is "Not Configured" or "Disabled", this is not a finding. Click the "Show..." button next to "Commands". If any of the listed commands are not expected, approved, and required, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246862`

### Rule: The Horizon Agent must only run allowed scripts on user disconnect.

**Rule ID:** `SV-246862r768546_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Horizon Agent has the capability to run scripts on user connect, disconnect, and reconnect. While this can be useful in setting up a user environment, in certain circumstances, the running of such scripts should be delegated to native windows capabilities where possible. These settings are powerful and can serve as a potential space for a privileged attacker to persist. By default, this setting is unconfigured. Should site require this setting, ensure it is audited and its configuration valid at all times.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the vdm_agent*.admx templates are added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops or RDS hosts. Navigate to Computer Configuration >> Policies >> Administrative Templates >> VMware View Agent Configuration >> Agent Configuration. Double-click the "CommandsToRunOnDisconnect" setting. If "CommandsToRunOnDisconnect" is "Not Configured" or "Disabled", this is not a finding. Click the "Show..." button next to "Commands". If any of the listed commands are not expected, approved, and required, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246863`

### Rule: The Horizon Agent must only run allowed scripts on user reconnect.

**Rule ID:** `SV-246863r768549_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Horizon Agent has the capability to run scripts on user connect, disconnect, and reconnect. While this can be useful in setting up a user environment, in certain circumstances, the running of such scripts should be delegated to native windows capabilities where possible. These settings are powerful and can serve as a potential space for a privileged attacker to persist. By default, this setting is unconfigured. Should a site require this setting, ensure it is audited and the configuration valid at all times.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the vdm_agent*.admx templates are added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops or RDS hosts. Navigate to Computer Configuration >> Policies >> Administrative Templates >> VMware View Agent Configuration >> Agent Configuration. Double-click the "CommandsToRunOnReconnect" setting. If "CommandsToRunOnReconnect" is "Not Configured" or "Disabled", this is not a finding. Click the "Show..." button next to "Commands". If any of the listed commands are not expected, approved, and required, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246864`

### Rule: The Horizon Agent must check the entire chain when validating certificates.

**Rule ID:** `SV-246864r768552_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any time the Horizon Agent establishes an outgoing TLS connection, it verifies the server certificate revocation status. By default, it verifies all intermediates but not the root. DoD policy requires full path validation, thus this default behavior needs to be changed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the vdm_agent*.admx templates are added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops or RDS hosts. Navigate to Computer Configuration >> Policies >> Administrative Templates >> VMware View Common Configuration >> Security Configuration. Double-click the "Type of certificate revocation check" setting. If "Type of certificate revocation check" is "Not Configured" or "Disabled", this is a finding. In the drop-down under "Type of certificate revocation check", if "WholeChain" is not selected, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246865`

### Rule: The Horizon Agent must set an idle timeout.

**Rule ID:** `SV-246865r768555_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Idle sessions are at increased risk of being hijacked. If a user has stepped away from their desk and is no long in positive control of their session, that session is in danger of being assumed by an attacker. Idle sessions also waste valuable datacenter resources and could potentially lead to a lack of resources for new, active users. As such, an organizationally defined idle timeout must be supplied to override the Horizon default of "never".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the vdm_agent*.admx templates are added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops or RDS hosts. Navigate to Computer Configuration >> Policies >> Administrative Templates >> VMware View Agent Configuration >> Agent Configuration. Double-click the "Idle Time Until Disconnect (VDI)" setting. If "Idle Time Until Disconnect (VDI)" is "Not Configured" or "Disabled", this is a finding. In the drop-down next to "Idle Timeout", if "Never" is selected, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246866`

### Rule: The Horizon Agent must block server to client clipboard actions for Blast.

**Rule ID:** `SV-246866r768558_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data loss prevention is a primary concern for the DoD, maintaining positive control of data at all times and only allowing flows over channels that are for that explicit purpose and monitored appropriately. By default, the Blast protocol on the Horizon Agent will block clipboard "copy/paste" actions from the desktop to the client but allow actions from the client to the desktop. This configuration must be validated and maintained over time.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the vdm_blast.admx template is added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops or RDS hosts. Navigate to Computer Configuration >> Policies >> Administrative Templates >> VMware Blast. Double-click the "Configure clipboard redirection" setting. If "Configure clipboard redirection" is "Not Configured" or "Disabled", this is not a finding. In the drop-down under "Configure clipboard redirection", if "Enabled server to client only" or "Enabled in both directions" is selected, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246867`

### Rule: The Horizon Agent must block server to client clipboard actions for PCoIP.

**Rule ID:** `SV-246867r768561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data loss prevention is a primary concern for the DoD, maintaining positive control of data at all times and only allowing flows over channels that are for that explicit purpose and monitored appropriately. By default, the PCoIP protocol on the Horizon Agent will block clipboard "copy/paste" actions from the desktop to the client but allow actions from the client to the desktop. This configuration must be validated and maintained over time.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the pcoip.admx template is added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops or RDS hosts. Navigate to Computer Configuration >> Policies >> Administrative Templates >> PCoIP Session Variables >> Not Overridable Administrator Settings. Double-click the "Configure clipboard redirection" setting. If "Configure clipboard redirection" is "Not Configured" or "Disabled", this is not a finding. In the drop-down under "Configure clipboard redirection", if "Enabled server to client only" or "Enabled in both directions" is selected, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246868`

### Rule: The Horizon Agent must not allow file transfers through HTML Access.

**Rule ID:** `SV-246868r768564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data loss prevention is a primary concern for the DoD, maintaining positive control of data at all times and only allowing flows over channels that are for that explicit purpose and monitored appropriately. Additionally, data coming into the environment must be through allowed channels and inspected appropriately. By default, the Blast protocol on the Horizon Agent will allow file transfers through HTML Access only from the client to the desktop. This must be configured to disabled in both directions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the vdm_blast.admx template is added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops or RDS hosts. Navigate to Computer Configuration >> Policies >> Administrative Templates >> VMware Blast. Double-click the "Configure file transfer" setting. If "Configure file transfer" is not "Enabled", this is a finding. In the drop-down under "Configure file transfer", if "Disabled both upload and download" is not selected, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246869`

### Rule: The Horizon Agent must not allow drag and drop for Blast.

**Rule ID:** `SV-246869r768567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data loss prevention is a primary concern for the DoD, maintaining positive control of data at all times and only allowing flows over channels that are for that explicit purpose and monitored appropriately. Additionally, data coming into the environment must be through allowed channels and inspected appropriately. By default, the Blast protocol on the Horizon Agent will allow drag and drop actions from the client to the desktop. This must be configured to disabled in both directions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the vdm_blast.admx template is added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops or RDS hosts. Navigate to Computer Configuration >> Policies >> Administrative Templates >> VMware Blast. Double-click the "Configure drag and drop direction" setting. If "Configure drag and drop direction" is not "Enabled", this is a finding. In the drop-down under "Configure drag and drop", if "Disabled in both directions" is not selected, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246870`

### Rule: The Horizon Agent must not allow drag and drop for PCoIP.

**Rule ID:** `SV-246870r768570_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data loss prevention is a primary concern for the DoD, maintaining positive control of data at all times and only allowing flows over channels that are for that explicit purpose and monitored appropriately. Additionally, data coming into the environment must be through allowed channels and inspected appropriately. By default, the PCoIP protocol on the Horizon Agent will allow drag and drop actions from the client to the desktop. This must be configured to disabled in both directions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the pcoip.admx template is added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops or RDS hosts. Navigate to Computer Configuration >> Policies >> Administrative Templates >> PCoIP Session Variables >> Overridable Administrator Settings. Double-click the "Configure drag and drop direction" setting. If "Configure drag and drop direction" is not "Enabled", this is a finding. In the drop-down under "Configure drag and drop direction", if "Disabled in both directions" is not selected, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246871`

### Rule: The Horizon Agent must audit clipboard actions for Blast.

**Rule ID:** `SV-246871r768573_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data loss prevention is a primary concern for the DoD, maintaining positive control of data at all times and only allowing flows over channels that are for that explicit purpose and monitored appropriately. By default, the Blast protocol on the Horizon Agent will block clipboard "copy/paste" actions from the desktop to the client but allow actions from the client to the desktop. All such allowed actions must be audited for potential future forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the vdm_blast.admx template is added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops or RDS hosts. Navigate to Computer Configuration >> Policies >> Administrative Templates >> VMware Blast. Double-click the "Configure clipboard audit" setting. If "Configure clipboard audit" is "Not Configured" or "Disabled", this is a finding. In the drop-down under "Configure clipboard audit", if "Enabled in both directions" is not selected, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246872`

### Rule: The Horizon Agent must audit clipboard actions for PCoIP.

**Rule ID:** `SV-246872r768576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data loss prevention is a primary concern for the DoD, maintaining positive control of data at all times and only allowing flows over channels that are for that explicit purpose and monitored appropriately. By default, the PCoIP protocol on the Horizon Agent will block clipboard "copy/paste" actions from the desktop to the client but allow actions from the client to the desktop. All such allowed actions must be audited for potential future forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the pcoip.admx template is added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops or RDS hosts. Navigate to Computer Configuration >> Policies >> Administrative Templates >> PCoIP Session Variables >> Overridable Administrator Settings. Double-click the "Configure clipboard audit" setting. If "Configure clipboard audit" is "Not Configured" or "Disabled", this is a finding. In the drop-down under "Configure clipboard audit", if "Enabled in both directions" is not selected, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246873`

### Rule: The Horizon Agent desktops must not allow client drive redirection.

**Rule ID:** `SV-246873r768579_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data loss prevention is a primary concern for the DoD, maintaining positive control of data at all times and only allowing flows over channels that are for that explicit purpose and monitored appropriately. By default, the Horizon Client, Agent, and guest operating systems will coordinate to allow drives local to the client to be redirected over the Client connection and mounted in the virtual desktop. This configuration must be modified to disallow drive sharing in order to protect sensitive DoD data from being maliciously, accidentally, or casually removed from the controlled environment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the vdm_rdsh_server.admx template is added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops or RDS hosts. Navigate to Computer Configuration >> Policies >> Administrative Templates >> Windows Components >> Remote Desktop Services >> Remote Desktop Session Host >> Device and Resource Redirection. Double-click the "Do not allow drive redirection" setting. If "Do not allow drive redirection" is not "Enabled", this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-246874`

### Rule: The Horizon Agent must block USB mass storage.

**Rule ID:** `SV-246874r768582_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Horizon Agent has the capability to granularly control what, if any, USB devices are allowed to be passed from the local client to the agent on the virtual desktop. By default, Horizon blocks certain device families from being redirected to the remote desktop or application. For example, HID (human interface devices) and keyboards are blocked from appearing in the guest as released BadUSB code targets USB keyboard devices. While there are legitimate reasons to pass USB devices to the desktop, these must be carefully analyzed for necessity. At a minimum, USB Mass Storage devices must never passed through, in keeping with long-standing DoD data loss prevention policies. As thumb drives are disallowed for physical PCs, so should they be for virtual desktops. This can be accomplished in many ways, including natively in the Horizon Agent.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the SA. USB mass storage devices can be blocked in a number of ways: 1. The desktop OS 2. A third party DLP solution 3. The "USB Redirection" optional agent feature not being installed on any VDI image 4. On the Connection Server via individual pool policies or global policies If any of these methods are already employed, the risk is already addressed and this control is not applicable. If USB devices are not otherwise blocked, the Horizon agent must be configured to block storage devices via allowlist or denylist. Ensure the vdm_agent*.admx templates are added. Open the "Group Policy Management" MMC snap-in. Open the site-specific GPO applying Horizon settings to the VDI desktops or RDS hosts. Navigate to Computer Configuration >> Policies >> Administrative Templates >> VMware View Agent Configuration >> View USB Configuration. 1. Check for denylisting: Double-click the "Exclude Device Family" setting. If "Exclude Device Family" is not "Enabled", denylisting is Not Configured. If "Exclude Device Family" does not include at least "o:storage", denylisting is Not Configured. If denylisting is Not Configured, continue to check for allowlisting. If denylisting is configured, this is not a finding. 2. Check for allowlisting: Double-click the "Exclude All Devices" setting. If "Exclude All Devices" is not "Enabled", allowlisting is Not Configured. Click "Cancel". Double-click the "Include Device Family" setting. If "Include Device Family" is "Enabled" and includes "storage", allowlisting is Not Configured. If neither denylisting nor allowlisting is properly configured, this is a finding.

