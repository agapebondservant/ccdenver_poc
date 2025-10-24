# STIG Benchmark: Microsoft Defender for Endpoint Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000207

**Group ID:** `V-272882`

### Rule: Microsoft Defender for Endpoint (MDE) must alert administrators on policy violations defined for endpoints.

**Rule ID:** `SV-272882r1119408_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. Applications providing this capability must be able to perform actions in response to detected malware. Responses include blocking, quarantining, deleting, and alerting. Other technology- or organization-specific responses may also be employed to satisfy this requirement. Malicious code includes viruses, worms, Trojan horses, and spyware. This requirement applies to applications providing malicious code protection. Satisfies: SRG-APP-000207, SRG-APP-000279, SRG-APP-000464, SRG-APP-000471, SRG-APP-000485, SRG-APP-000940</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least a Security Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Email notifications (under General) >> Alerts. 2. For each defined Notification rule: - Click on the rule and select "Edit" to enter the "Update notification rule" screen. - Verify the notification settings are configured as defined by the authorizing official (AO). - Verify the Recipient Emails are assigned as defined by the AO. 3. Click "Cancel". 4. In the navigation pane, select Settings >> Endpoints >> Email notifications (under General) >> Vulnerabilities. 5. For each defined notification rule: - Click on the rule and select "Edit" to enter the "Update notification rule" screen. - Verify the notification settings are configured as defined by the AO. - Verify the Recipient Emails are assigned as defined by the AO. 6. Click "Cancel". If Settings >> Endpoints >> Email notifications (under Permissions) >> Alerts does not display rules as defined by the AO, this is a finding. If Settings >> Endpoints >> Email notifications (under Permissions) >> Vulnerabilities does not display rules as defined by the AO, this is a finding. When selecting each rule individually, if the Notification Settings and Recipient Emails are not as defined by the AO, this is a finding.

## Group: SRG-APP-000211

**Group ID:** `V-272886`

### Rule: Roles for use with Microsoft Defender for Endpoint (MDE) must be configured within Entra ID.

**Rule ID:** `SV-272886r1119409_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application management functionality includes functions necessary for administration and requires privileged user access. Allowing nonprivileged users to access application management functionality capabilities increases the risk that nonprivileged users may obtain elevated privileges. Using role-based access control (RBAC), roles and groups can be created within the security operations team to grant appropriate access to the MDE portal. Based on the roles and groups created, the capability will exist to have fine-grained control over what users with access to the portal can view and do. Creation of Entra ID roles is a prerequisite to configuring RBAC within the MDE portal itself. Defender for Endpoint RBAC is designed to support a role-based model and provides granular control over what roles can view, devices they can access, and actions they can take. The RBAC framework is centered around the following controls: - Control who can take specific action. - Create custom roles and control what Defender for Endpoint capabilities they can access with granularity. - Control who can view information on specific device group or groups. Satisfies: SRG-APP-000211, SRG-APP-000267</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Azure Entra ID portal as a Global Admin or other role with the ability to create/assign roles. 1. Select Manage >> Roles and administrators. Click on the "MDE Administrator" role. 2. Under "Active assignments" ensure one or more authorizing official (AO)-approved users are assigned to this role. This role is a top-level administrator within MDE. Note: A custom defined, AO-approved role may be created and used in lieu of the built-in MDE Administrator role. If one or more AO-approved users have not been assigned to the security administrator (or equivalent AO-approved) role, this is a finding. 1. Return to the Entra ID portal home and select Manage >> Groups. Click the number next to "Total Groups". 2. Ensure one or more custom roles have been defined as subordinate roles for MDE administration. The structure of various subordinate groups is to be defined by the AO. 3. Click on each of these groups and ensure one or more users have been assigned. If one or more subordinate groups do not exist, this is a finding. If one or more users do not exist in these subordinate groups, this is a finding.

## Group: SRG-APP-000211

**Group ID:** `V-272887`

### Rule: Microsoft Defender for Endpoint (MDE) must be configured for a least privilege model by implementing Unified Role-Based Access Control (RBAC).

**Rule ID:** `SV-272887r1119729_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When first accessing the Microsoft Defender portal, either full access or read only access is granted. Full access rights are granted to users with the Security Administrator (or equivalent) role in Microsoft Entra ID. Read only access is granted to users with a Security Reader (or equivalent) role in Microsoft Entra ID. The permission tiers available to assign to custom roles are as follows: View data: - Security Operations - View all security operations data in the portal. - Defender Vulnerability Management - View Defender Vulnerability Management data in the portal. Active remediation actions: - Security Operations - Take response actions, approve or dismiss pending remediation actions, manage allowed/blocked lists for automation and indicators. - Defender Vulnerability Management. - Exception handling - Create new exceptions and manage active exceptions. Defender Vulnerability Management - Remediation handling: - Submit new remediation requests, create tickets, and manage existing remediation activities. Defender Vulnerability Management - Application handling: - Apply immediate mitigation actions by blocking vulnerable applications, as part of the remediation activity and manage the blocked apps and perform unblock actions. Security baselines: - Defender Vulnerability Management. - Manage security baselines assessment profiles. - Create and manage profiles so users can assess if devices comply to security industry baselines. Alerts investigation: - Manage alerts, initiate automated investigations, run scans, collect investigation packages, manage device tags, and download only portable executable (PE) files. Manage portal system settings: - Configure storage settings, SIEM, and threat intel API settings (applies globally), advanced settings, automated file uploads, roles, and device groups. Satisfies: SRG-APP-000211, SRG-APP-000267</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Roles (under Permissions). 2. For each defined role: - Click he role to enter the edit role screen. - Verify the Permissions are configured as defined by the authorizing official (AO). - Verify the appropriate user groups are assigned as defined by the AO. - Click "Cancel". If Settings >> Endpoints >> Roles (under Permissions) does not display roles as defined by the AO, this is a finding. When selecting each role individually, if the permissions and user groups are not as defined by the AO, this is a finding.

## Group: SRG-APP-000246

**Group ID:** `V-272888`

### Rule: Microsoft Defender for Endpoint (MDE) must enable Endpoint Detection and Response (EDR) in block mode.

**Rule ID:** `SV-272888r1119411_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Denial of service (DoS) is a condition in which a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Individuals of concern can include hostile insiders or external adversaries that have successfully breached the information system and are using the system as a platform to launch cyberattacks on third parties. Applications and application developers must take the steps needed to ensure users cannot use an authorized application to launch DoS attacks against other systems and networks. For example, applications may include mechanisms that throttle network traffic so users are not able to generate unlimited network traffic via the application. Limiting system resources allocated to any user to a bare minimum may also reduce the ability of users to launch some DoS attacks. The methods employed to counter this risk will be dependent upon the application layer methods that can be used to exploit it. Satisfies: SRG-APP-000246, SRG-APP-000435</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Advanced features (under General). 2. Verify the slide bar for "Enable EDR in block mode" is set to "On". If the slide bar for "Enable EDR in block mode" is not set to "On", this is a finding.

## Group: SRG-APP-000515

**Group ID:** `V-272889`

### Rule: Microsoft Defender for Endpoint (MDE) must be connected to a central log server.

**Rule ID:** `SV-272889r1119412_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. Satisfies: SRG-APP-000515, SRG-APP-000086, SRG-APP-000108, SRG-APP-000125, SRG-APP-000181, SRG-APP-000358, SRG-APP-000745</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Microsoft Sentinel. 2. Under "Workspaces", verify a Sentinel Workspace has been assigned. If a Sentinel Workspace has not been assigned, this is a finding. If another documented and authorizing official (AO)-approved SIEM/Central Log Server is in use, this is not a finding.

## Group: SRG-APP-000279

**Group ID:** `V-275979`

### Rule: Microsoft Defender for Endpoint (MDE) must enable Automatically Resolve Alerts.

**Rule ID:** `SV-275979r1119709_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. This setting resolves an alert if automated investigation finds no threats or has successfully remediated all malicious artifacts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Advanced features (under General). 2. Verify the slide bar for "Automatically Resolve Alerts" to "On".

## Group: SRG-APP-000279

**Group ID:** `V-275980`

### Rule: Microsoft Defender for Endpoint (MDE) must enable Allow or block file.

**Rule ID:** `SV-275980r1119710_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. This setting ensures Windows Defender Antivirus is turned on and the cloud-based protection feature is enabled to use the allow or block file feature.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Advanced features (under General). 2. Verify the slide bar for "Allow or block file" is set to "On". If the slide bar for "Allow or block file" is not set to "On", this is a finding.

## Group: SRG-APP-000279

**Group ID:** `V-275981`

### Rule: Microsoft Defender for Endpoint (MDE) must enable Hide potential duplicate device records.

**Rule ID:** `SV-275981r1119731_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. When turned on, this setting will hide duplications that might occur for the following reasons: - Devices that were discovered more than once. - Discovery of onboarded devices. - Unintentionally discovered onboarded devices. These duplications will be hidden from multiple experiences in the portal to create a more accurate view of the device inventory. The affected areas in the portal include the Device Inventory, Microsoft Defender Vulnerability Management screens, and Public API for machines data. These devices will still be viewable in global search, advanced hunting, and alert and incidents pages.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Advanced features (under General). 2. Verify the slide bar for "Hide potential duplicate device records" is set to "On". If the slide bar for "Hide potential duplicate device records" is not set to "On", this is a finding.

## Group: SRG-APP-000279

**Group ID:** `V-275982`

### Rule: Microsoft Defender for Endpoint (MDE) must enable Custom network indicators.

**Rule ID:** `SV-275982r1119712_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. This setting configures devices to allow or block connections to IP addresses, domains, or URLs in custom indicator lists. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Advanced features (under General). 2. Verify the slide bar for "Custom network indicators" is set to "On". If the slide bar for "Custom network indicators" is not set to "On", this is a finding.

## Group: SRG-APP-000279

**Group ID:** `V-275983`

### Rule: Microsoft Defender for Endpoint (MDE) must enable Tamper protection.

**Rule ID:** `SV-275983r1119713_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. Tamper protection prevents malicious apps from turning off security features like virus and threat protection, behavior monitoring, cloud-delivered protection, etc., preventing unwanted changes to security solutions and essential functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Advanced features (under General). 2. Verify the slide bar for "Tamper protection" is set to "On". If the slide bar for "Tamper protection" is not set to "On", this is a finding.

## Group: SRG-APP-000279

**Group ID:** `V-275984`

### Rule: Microsoft Defender for Endpoint (MDE) must enable Show user details.

**Rule ID:** `SV-275984r1119714_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. This setting enables displaying user details: picture, name, title, department, stored in Azure Active Directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Advanced features (under General). 2. Verify the slide bar for "Show user details" is set to "On". If the slide bar for "Show user details" is not set to "On", this is a finding.

## Group: SRG-APP-000279

**Group ID:** `V-275985`

### Rule: Microsoft Defender for Endpoint (MDE) must enable Microsoft Defender for Cloud Apps.

**Rule ID:** `SV-275985r1119715_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. This setting forwards Microsoft Defender for Endpoint signals to Defender for Cloud Apps, giving administrators deeper visibility into both sanctioned cloud apps and shadow IT. It also grants the ability to block unauthorized applications when the custom network indicators setting is turned on. Forwarded data is stored and processed in the same location as Cloud App Security data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Advanced features (under General). 2. Verify the slide bar for "Microsoft Defender for Cloud Apps" is set to "On". If the slide bar for "Microsoft Defender for Cloud Apps" is not set to "On", this is a finding.

## Group: SRG-APP-000279

**Group ID:** `V-275986`

### Rule: Microsoft Defender for Endpoint (MDE) must enable Web content filtering.

**Rule ID:** `SV-275986r1119716_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. This setting blocks access to websites containing unwanted content and tracks web activity across all domains. To specify the web content categories to be blocked, a web content filtering policy must be created. Network protection must be set to block mode when deploying the Microsoft Defender for Endpoint security baseline.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Advanced features (under General). 2. Verify the slide bar for "Web content filtering" is set to "On". If the slide bar for "Web content filtering" is not set to "On", this is a finding.

## Group: SRG-APP-000279

**Group ID:** `V-275987`

### Rule: Microsoft Defender for Endpoint (MDE) must enable Device discovery.

**Rule ID:** `SV-275987r1119717_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. This setting allows onboarded devices to discover unmanaged devices in the network and assess vulnerabilities and risks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Advanced features (under General). 2. Verify the slide bar for "Device discovery" is set to "On". If the slide bar for "Device discovery" is not set to "On", this is a finding.

## Group: SRG-APP-000279

**Group ID:** `V-275988`

### Rule: Microsoft Defender for Endpoint (MDE) must enable Download quarantined files.

**Rule ID:** `SV-275988r1119718_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. This setting backs up quarantined files in a secure and compliant location so they can be downloaded directly from quarantine.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Advanced features (under General). 2. Verify the slide bar for "Download quarantined files" is set to "On". If the slide bar for "Download quarantined files" is not set to "On", this is a finding.

## Group: SRG-APP-000279

**Group ID:** `V-275989`

### Rule: Microsoft Defender for Endpoint (MDE) must enable Live Response.

**Rule ID:** `SV-275989r1119719_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. This setting allows users with appropriate RBAC permissions to investigate devices they are authorized to access, using a remote shell connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Advanced features (under General). 2. Verify the slide bar for "Live Response" is set to "On". If the slide bar for "Live Response" is not set to "On", this is a finding.

## Group: SRG-APP-000279

**Group ID:** `V-275990`

### Rule: Microsoft Defender for Endpoint (MDE) must enable Live Response for Servers.

**Rule ID:** `SV-275990r1119720_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. This setting allows users with Live Response privileges to connect remotely to servers (Windows Server or Linux devices) they are authorized to access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Advanced features (under General). 2. Verify the slide bar for "Live Response for Servers" is set to "On". If the slide bar for "Live Response for Servers" is not set to "On", this is a finding.

## Group: SRG-APP-000279

**Group ID:** `V-275991`

### Rule: Microsoft Defender for Endpoint (MDE) must enable Share endpoint alerts with Microsoft Compliance Center.

**Rule ID:** `SV-275991r1119721_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. This setting forwards endpoint security alerts and their triage status to Microsoft Purview portal, allowing enhanced insider risk management policies with alerts and the ability to remediate internal risks before they cause harm. Forwarded data is processed and stored in the same location as Office 365 data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Advanced features (under General). 2. Verify the slide bar for "Share endpoint alerts with Microsoft Compliance Center" is set to "On". If the slide bar for "Share endpoint alerts with Microsoft Compliance Center" is not set to "On", this is a finding.

## Group: SRG-APP-000279

**Group ID:** `V-275992`

### Rule: Microsoft Defender for Endpoint (MDE) must enable Microsoft Intune connection.

**Rule ID:** `SV-275992r1119722_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. Connecting to Microsoft Intune enables sharing of device information and enhanced policy enforcement. Intune provides additional information about managed devices for secure score. It can use risk information to enforce conditional access and other security policies.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Advanced features (under General). 2. Verify the slide bar for "Microsoft Intune connection" is set to "On". If the slide bar for "Microsoft Intune connection" is not set to "On", this is a finding.

## Group: SRG-APP-000279

**Group ID:** `V-275993`

### Rule: Microsoft Defender for Endpoint (MDE) must enable Authenticated telemetry.

**Rule ID:** `SV-275993r1119723_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. The authenticated telemetry setting prevents spoofing telemetry into the dashboard.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Advanced features (under General). 2. Verify the slide bar for "Authenticated telemetry" is set to "On". If the slide bar for "Authenticated telemetry" is not set to "On", this is a finding.

## Group: SRG-APP-000279

**Group ID:** `V-275994`

### Rule: Microsoft Defender for Endpoint (MDE) must enable File Content Analysis.

**Rule ID:** `SV-275994r1119724_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. Content analysis submits suspicious files identified by Automated investigation to the cloud for additional inspection. Only files with the specified extension names will be submitted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Automation uploads (under Rules). 2. Verify the slide bar for "File Content Analysis" is set to "On". If the slide bar for "File Content Analysis" is not set to "On", this is a finding.

## Group: SRG-APP-000279

**Group ID:** `V-275995`

### Rule: Microsoft Defender for Endpoint (MDE) must enable Memory Content Analysis.

**Rule ID:** `SV-275995r1119725_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. This setting automatically investigates memory content of processes. When enabled, memory content can be uploaded to MDE during an Automated investigation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Automation uploads (under Rules). 2. Verify the slide bar for "Memory Content Analysis" is set to "On". If the slide bar for "Memory Content Analysis" is not set to "On", this is a finding.

## Group: SRG-APP-000279

**Group ID:** `V-275996`

### Rule: Microsoft Defender for Endpoint (MDE) Discovery Mode must enable Log4j2 detection.

**Rule ID:** `SV-275996r1119726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. This setting detects devices with applications using the vulnerable Log4j2 library through unauthenticated probing. This option will also enable discovery using Server 2019+ onboarded devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Device Discovery >> Discovery setup (under Discovery setup). 2. Verify Standard discovery is selected and the slide bar for "Enable Log4j2 detection" is selected. If the slide bar for "Enable Log4j2 detection" is not selected, this is a finding.

## Group: SRG-APP-000279

**Group ID:** `V-275997`

### Rule: Microsoft Defender for Endpoint (MDE) Discovery Mode must be set to All Devices.

**Rule ID:** `SV-275997r1119727_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. This setting enables standard discovery for supported devices that have been onboarded.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Device Discovery. Select which devices to use for Standard discovery (under Discovery setup). 2. Verify "All devices (recommended)" is selected. If the slide bar for "All devices (recommended)" is not selected, this is a finding.

## Group: SRG-APP-000279

**Group ID:** `V-275998`

### Rule: Microsoft Defender for Endpoint (MDE) must enable Full remediation for Device groups.

**Rule ID:** `SV-275998r1119728_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited to, antivirus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. Full remediation is necessary to automatically investigate and remediate devices without human intervention which lowers SOC fatigue. This is also required for Attack Disruption.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the MDE portal as a user with at least an MDE Administrator or equivalent role: 1. In the navigation pane, select Settings >> Endpoints >> Device groups (under Permissions). 2. For all device groups: Verify the remediation column is set to Full remediation. If the remediation column for all Device groups is not set to "Full remediation", this is a finding.

