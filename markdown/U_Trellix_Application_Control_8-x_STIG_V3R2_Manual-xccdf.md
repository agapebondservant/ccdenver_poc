# STIG Benchmark: Trellix Application Control 8.x Security Technical Implementation Guide 

---

**Version:** 3

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000386

**Group ID:** `V-213316`

### Rule: A Trellix Application Control written policy must be documented to outline the organization-specific variables for application whitelisting.

**Rule ID:** `SV-213316r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling application whitelisting without adequate design and organization-specific requirements will either result in an implementation which is too relaxed or an implementation which causes denial of service to its user community. Documenting the specific requirements and trust model before configuring and deploying the Trellix Application Control software is mandatory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the ISSO/ISSM to review the organizational-specific written policy for the Trellix Application Control software. If no written policy exists, this is a finding.

## Group: SRG-APP-000165

**Group ID:** `V-213317`

### Rule: The use of a Solidcore 8.x local Command Line Interface (CLI) Access Password must be documented in the organizations written policy.

**Rule ID:** `SV-213317r1015267_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Solidcore client can be configured locally at the CLI, but only when accessed with the required password. Since the Trellix Application Control configuration is to be managed by ePO policies, allowing enablement of the CLI to would introduce the capability of local configuration changes. Strict management of the accessibility of the CLI is necessary in order to prevent its misuse. The misuse of the CLI would open the system up to the possible configuration changes potentially allowing malicious applications to execute unknowingly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: The CLI Access is in lockdown mode by default when being managed by ePO. Since the CLI Access can be recovered for troubleshooting, this requirement needs to be met. Consult with the information system security officer (ISSO)/information system security manager (ISSM) to obtain a copy of the organization's documented policy for application whitelisting. Review the written policy for how and when the Solidcore CLI is used by the organization. If the use of the CLI is not documented in the organization's written policy, this is a finding.

## Group: SRG-APP-000169

**Group ID:** `V-213318`

### Rule: The Solidcore client Command Line Interface (CLI) Access password complexity requirements must be documented in the organizations written policy.

**Rule ID:** `SV-213318r1015874_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Solidcore client can be configured locally at the CLI, but only when accessed with the required password. The misuse of the CLI would open the system up to the possible configuration, allowing malicious applications to execute unknowingly. Strict management of the accessibility of the CLI is necessary in order to prevent its misuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: The CLI Access is in lockdown mode by default when being managed by ePO. Since the CLI Access can be recovered for troubleshooting, this requirement needs to be met. Since the Solidcore CLI does not allow for technical enforcement of password complexity the enforcement will be via this written policy directive. Consult with the information system security officer (ISSO)/information system security manager (ISSM) to obtain a copy of the organization's documented policy for application whitelisting. Review the written policy for CLI password complexity requirements. Verify the policy requires the password to be 15 characters in length and contain a mix of at least one lowercase, one uppercase, one number, and one special character. If the written policy does not document the requirement for password complexity and/or does not specify the password must be 15 characters in length and contain a mix of at least one lowercase, one uppercase, one number, and one special character, this is a finding.

## Group: SRG-APP-000172

**Group ID:** `V-213319`

### Rule: The Solidcore client Command Line Interface (CLI) Access Password protection process must be documented in the organizations written policy.

**Rule ID:** `SV-213319r961029_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Solidcore client can be configured locally at the CLI, but only when accessed with the required password. Since the Trellix Application Control configuration is to be managed by ePO policies, allowing enablement of the CLI to would introduce the capability of local configuration changes. Strict management of the accessibility of the CLI is necessary in order to prevent its misuse. The misuse of the CLI would open the system up to the possible configuration changes potentially allowing malicious applications to execute unknowingly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: The CLI Access is in lockdown mode by default when being managed by ePO. Since the CLI Access can be recovered for troubleshooting, this requirement needs to be met. Consult with the ISSO/ISSM to obtain a copy of the organization's documented policy for application whitelisting. Review the written policy for how the Solidcore client interface is used by the organization. Verify the policy identifies how the CLI password is protected. Ask the ePO admin, "What protection measures are used for the CLI password?" The protection measures should include, at a minimum, storage in a sealed envelope, which is then stored in an approved safe. Note: The envelope will contain the last access date along with those authorized to use it. If the written policy does not contain specific information on how the CLI password is protected and/or if that policy does not include, at a minimum, that the password be stored in a sealed envelope in an approved safe with the last access date noted, this is a finding.

## Group: SRG-APP-000174

**Group ID:** `V-213320`

### Rule: The requirement for scheduled Solidcore client Command Line Interface (CLI) Access Password changes must be documented in the organizations written policy.

**Rule ID:** `SV-213320r1043190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Solidcore client can be configured locally at the CLI, but only when accessed with the required password. The misuse of the CLI would open the system up to the possible configuration, allowing malicious applications to execute unknowingly. Strict management of the accessibility of the CLI is necessary in order to prevent its misuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: The CLI Access is in lockdown mode by default when being managed by ePO. Since the CLI Access can be recovered for troubleshooting, this requirement needs to be met. Consult with the information system security officer (ISSO)/information system security manager (ISSM) to obtain a copy of the organization's documented policy for application whitelisting. Review the written policy for how the Solidcore client interface is used by the organization. Verify the policy identifies the frequency with which the CLI password is changed. If the written policy does not contain specific information on frequency with which the CLI password is changed, this is a finding.

## Group: SRG-APP-000397

**Group ID:** `V-213321`

### Rule: The process by which the Solidcore client Command Line Interface (CLI) Access Password is made available to administrators when needed must be documented in the organizations written policy.

**Rule ID:** `SV-213321r986211_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Solidcore client can be configured locally at the CLI, but only when accessed with the required password. Since the Trellix Application Control configuration is to be managed by ePO policies, allowing enablement of the CLI to would introduce the capability of local configuration changes. Strict management of the accessibility of the CLI is necessary in order to prevent its misuse. The misuse of the CLI would open the system up to the possible configuration changes potentially allowing malicious applications to execute unknowingly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: The CLI Access is in lockdown mode by default when being managed by ePO. Since the CLI Access can be recovered for troubleshooting, this requirement needs to be met. Consult with the information system security officer (ISSO)/information system security manager (ISSM) to obtain a copy of the organization's documented policy for application whitelisting. The policy must contain procedures for accessing the CLI password, to include the system administrator (SA) gaining access to an approved safe in order for obtaining the password. If a procedure does not exist for accessing the CLI password as described above, this is a finding.

## Group: SRG-APP-000276

**Group ID:** `V-213322`

### Rule: The Trellix Application Control Options Advanced Threat Defense (ATD) settings, if being used, must be confined to the organizations enclave.

**Rule ID:** `SV-213322r1015876_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data will be leaving the endpoint to be analyzed by the ATD. Because data could feasibly be intercepted en route, risk of outside threats is minimized by ensuring the ATD is in the same enclave as the endpoints.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If an ATD server is not being used in the environment, this is Not Applicable. Consult with the information system security officer (ISSO)/information system security manager (ISSM) to review the written policy to ensure the usage of an ATD is documented. If the usage of an ATD is not documented in the written policy, this is a finding. Determine the location of the ATD being used by the organization and verify the ATD is confined to the organization's enclave. If the location of the ATD being used by the organization cannot be determined and the ATD is not confined to the organization's enclave, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-213323`

### Rule: The configuration of features under Trellix Application Control Options policies Enforce feature control must be documented in the organizations written policy.

**Rule ID:** `SV-213323r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, the Trellix Application Control prevents installation of ActiveX controls on endpoints, enforces memory protection techniques on endpoints, and prevents MSI-installers from running on endpoints. The Feature Control allows for those safeguards to be bypassed and in doing so renders the Trellix Application Control less effective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the ISSO/ISSM to obtain a copy of the organization's documented policy for application whitelisting. Review the written policy for how the Solidcore client interface is used by the organization. Verify the written policy identifies whether additional features are enabled or not under "Enforce feature control" of the Trellix Application Control Options ePO policy. If the written policy does not identify whether additional features are enabled or not under "Enforce feature control" of the Trellix Application Control Options ePO policy, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-213324`

### Rule: The organizations written policy must include a process for how whitelisted applications are deemed to be allowed.

**Rule ID:** `SV-213324r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling application whitelisting without adequate design and organization-specific requirements will either result in an implementation which is too relaxed or an implementation which causes denial of service to its user community. Documenting the specific requirements and trust model before configuring and deploying the Trellix Application Control software is mandatory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the ISSO/ISSM to review the organizational-specific written policy for the Trellix Application Control software. Verify the written policy includes a process for how applications are vetted and deemed to be allowed. If no written policy exists, this is a finding. If written policy does not include a process for vetting applications before allowing them, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-213325`

### Rule: The organizations written policy must include procedures for how often the whitelist of allowed applications is reviewed.

**Rule ID:** `SV-213325r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling application whitelisting without adequate design and organization-specific requirements will either result in an implementation which is too relaxed or an implementation which causes denial of service to its user community. Documenting the specific requirements and trust model before configuring and deploying the Trellix Application Control software is mandatory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the ISSO/ISSM to review the organizational-specific written policy for the Trellix Application Control software. Verify the written policy includes a process for how often the application whitelist is reviewed. If no written policy exists, this is a finding. If written policy does not include a process for how often the application whitelist is reviewed, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-213326`

### Rule: The Solidcore client must be enabled.

**Rule ID:** `SV-213326r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Application Control whitelisting must be enabled on all workstation endpoints. To enable Application Control, the Solidcore client needs to be in enabled mode.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset(s) that need the organization-specific policy and view its properties. Click on the "Products" tab. Under "Product", verify the Solidcore 8.x client is listed as a product. If exists, click on the row to review additional information. Verify status shows "Enabled". If the Solidcore 8.x client is listed as an installed product but the status is not "Enabled", this is a finding.

## Group: SRG-APP-000383

**Group ID:** `V-213327`

### Rule: The Solidcore client Command Line Interface (CLI) must be in lockdown mode.

**Rule ID:** `SV-213327r961470_rule`
**Severity:** high

**Description:**
<VulnDiscussion>By default, when an endpoint's Solidcore installation is managed by the ePO server, the CLI will automatically be in lockdown mode. This will ensure the endpoint receives all of its Solidcore configuration settings from the ePO server. The CLI can, however, be activated for troubleshooting efforts during which time the ePO settings will not be enforced. Leaving the CLI in an allowed status will prevent the endpoint from receiving changes from the ePO server for the Solidcore client.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine CLI status. Access the system being reviewed. From an operating system command line, execute the following command: sadmin status <enter> If the status for CLI is "Allowed" or "Recovered", this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-213328`

### Rule: The Solidcore client Command Line Interface (CLI) Access Password must be changed from the default.

**Rule ID:** `SV-213328r961479_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Solidcore client can be configured locally at the CLI, but only when accessed with the required password. Since the Trellix Application Control configuration is to be managed by ePO policies, allowing enablement of the CLI to would introduce the capability of local configuration changes. Strict management of the accessibility of the CLI is necessary in order to prevent its misuse. The misuse of the CLI would open the system up to the possible configuration changes potentially allowing malicious applications to execute unknowingly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is a manual procedure to verify the CLI Access Password has been changed from its default setting by the ePO administrator. Ask the ePO admin, "Has the CLI Access Password been changed from its default setting?" If the default password is being used, this is a finding. Note: The password does not need to be divulged during the review. An interview question of the SA to validate that it is not the default is sufficient.

## Group: SRG-APP-000386

**Group ID:** `V-213329`

### Rule: The organization-specific Rules policy must only include executable and dll files that are associated with applications as allowed by the organizations written policy.

**Rule ID:** `SV-213329r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure Solidcore clients are only configured to STIG and organization-specific settings, organization-specific ePO policies must be applied to all organization workstation endpoints. The Trellix Application Control installs with two Default Rules policies. The Trellix Default Rules policy includes the whitelist for commonly used applications to the platform. The Trellix Applications Default Rules policy include the whitelist for Trellix applications. Both of these policies are at the "My Organization" level of the System Tree and must be inherited by all branches of the System Tree. Organization-specific applications would be whitelisted with an organization-specific policy combined with the two Default policies into one effective policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the organization's written policy for the Trellix Application Control software from the System or ePO Administrator. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset(s) that need the organization-specific policy. Note: The organization specific rules policy is for additional allowed applications. In the event there are Trellix Default rules that need to be excluded in an organization or on a specific asset, a copy of the Trellix Default must be used in place of the Trellix Default rules policy. In that copy, only the specific rules should be removed that the organization wants to deny. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select "Solidcore 8.x: Application Control". For the "Application Control Rules (Windows)" Category, click on "Edit Assignments" under the "Actions" column. Identify the organization-specific Rules policy applied to the system being reviewed. Click on "Edit Policy" beside the organization-specific Rules policy. Verify the list of applications under each of the "Rules Groups" in the organization-specific Rules policy against the written policy's list of allowed applications. If the organization-specific Rules policy contains any applications not documented in the written policy as allowed, this is a finding.

## Group: SRG-APP-000276

**Group ID:** `V-213330`

### Rule: The Trellix Application Control Options Reputation setting must be configured to use the Trellix Global Threat Intelligence (Trellix GTI) option.

**Rule ID:** `SV-213330r1015877_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a Threat Intelligence Exchange (TIE) server is being used in the organization, reputation for files and certificates is fetched from the TIE server. The reputation values control execution at endpoints and are displayed on the Application Control pages on the Trellix ePO console. If the GTI is being used, reputation for files and certificates is fetched from the Trellix GTI. For both methods, the administrator can review the reputation values and make informed decisions for inventory items in the enterprise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement is Not Applicable on a classified SIPRNet or otherwise closed network. This requirement is only applicable to Windows platforms. For MAC and Linux platforms, this is Not Applicable. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset(s) that need the organization-specific policy. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 8.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)" that is specific for the asset being reviewed. Select the "Reputation" tab. Verify the "Use Trellix Global Threat Intelligence (Trellix GTI)" option is selected. Note: The "Trellix GTI" option must be selected, as a failover, even if an internal Trellix TIE server is configured. If the "Trellix GTI" option is not selected, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-213331`

### Rule: The Trellix Application Control Options Reputation-Based Execution settings, if enabled, must be configured to allow Most Likely Trusted or Known Trusted only.

**Rule ID:** `SV-213331r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a file is executed on an endpoint, the Application Control performs multiple checks to determine whether to allow or ban the execution. Only files with a reputation of "Most Likely Trusted", "Known Trusted" or "Might be Trusted" are considered to be allowed. By configuring the setting to only "Most Likely Trusted" or "Known Trusted", the files with a reputation of "Might be Trusted" are blocked. While this may impact operationally in the beginning, after the inventories are vetted by the administrators, files with a "Might be Trusted" value may be recategorized in that organization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is only applicable to Windows platforms. For MAC and Linux platforms, this is Not Applicable. If Reputation-Based Execution settings is not enabled, this check is Not Applicable. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset(s) that need the organization-specific policy. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 8.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)" that is specific for the asset being reviewed. Select the "Reputation" tab. Verify the "Reputation-Based Execution Settings" is configured to allow binaries with "Most Likely Trusted" and above. If the allow binaries "Most Likely Trusted" and above is not selected for "Reputation-Based Execution Settings", this is a finding.

## Group: SRG-APP-000276

**Group ID:** `V-213332`

### Rule: The Trellix Application Control Options Advanced Threat Defense (ATD) settings must not be enabled unless an internal ATD is maintained by the organization.

**Rule ID:** `SV-213332r1015878_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This option will automatically send files with a specific file reputation to ATD for further analysis. This option is not selected by default and must only be selected if an ATD is being used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If an ATD server is not being used in the environment, this is Not Applicable. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset(s) that need the organization-specific policy. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 8.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)" that is specific for the asset being reviewed. Select the "Reputation" tab. Verify the option for sending binaries for analysis under the "Advanced Threat Defense (ATD) settings" is selected. Consult with the information system security officer (ISSO)/information system security manager (ISSM) to review the written policy to verify the usage of an ATD is documented. If the option for sending binaries for analysis under the "Advanced Threat Defense (ATD) settings" is selected and the written policy does not include documentation on the usage of an ATD, this is a finding.

## Group: SRG-APP-000276

**Group ID:** `V-213333`

### Rule: The Trellix Application Control Options Advanced Threat Defense (ATD) settings, if being used, must be configured to send all binaries with a reputation of Might be Trusted and below for analysis.

**Rule ID:** `SV-213333r1015879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When the file reputation of "Might be Trusted" is configured for being forwarded to ATD, all files with the reputation of "Might be Trusted", "Unknown", "Might be Malicious", "Most Likely Malicious" and "Known Malicious" are forwarded to the ATD. The files with "Might be Trusted" reputation may be redesignated as "Trusted" after analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is only applicable to Windows platforms. For Mac and Linux platforms, this is Not Applicable. If an ATD server is not being used in the environment, this is Not Applicable. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 8.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)" that is specific for the asset being reviewed. Select the "Reputation" tab. If the option for sending binaries for analysis under the "Advanced Threat Defense (ATD) settings" is selected, verify the level of binaries to be sent for analysis is "Might be Trusted" and below. If the level of binaries to be sent for analysis is not "Might be Trusted", this is a finding.

## Group: SRG-APP-000276

**Group ID:** `V-213334`

### Rule: The Trellix Application Control Options Advanced Threat Defense (ATD) settings, if being used, must be configured to only send binaries with a size of 5MB or less.

**Rule ID:** `SV-213334r1015880_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Since binaries can be large, the file size must be limited to avoid congestion on the network and degradation on the endpoint when sending the binaries to the ATD.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is only applicable to Windows platforms. For Mac and Linux platforms, this is Not Applicable. If an ATD server is not being used in the environment, this is Not Applicable. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 8.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)" that is specific for the asset being reviewed. Select the "Reputation" tab. If the option for sending binaries for analysis under the "Advanced Threat Defense (ATD) settings" is selected, verify the "Limit file size to" option is set to 5 MB or less. If the "Limit file size to" option is not set to 5 MB or less, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-213336`

### Rule: The Trellix Application Control Options policy must be configured to disable Self-Approval.

**Rule ID:** `SV-213336r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Trellix Application Control Self-Approval feature allows the user to take an action when a user tries to run a new or unknown application.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is only applicable to Windows platforms. For MAC and Linux platforms, this is Not Applicable. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 8.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)". On the "Self-Approval" tab, verify the "Enable Self-Approval" check box is not selected. If the "Enable Self-Approval" check box is selected, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-213337`

### Rule: The Trellix Application Control Options policy End User Notification, if configured by organization, must have all default variables replaced with the organization-specific data.

**Rule ID:** `SV-213337r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "User Message" option will show a dialog box when an event is detected and display the organization-specified text in the message.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is only applicable to Windows platforms. For MAC and Linux platforms, this is Not Applicable. If "End User Notification" is not used by the organization, this is Not Applicable. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 8.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)". On the "End User Notification" tab, determine if the "User Message:" option "Show the messages dialog box when an event is detected and display the specified text in the message." is selected. If "Show the messages dialog box when an event is detected and display the specified text in the message." is not selected, this is Not Applicable. If "Show the messages dialog box when an event is detected and display the specified text in the message." is selected, consult with the ISSO/ISSM to review the organizational-specific written policy for the Trellix Application Control software. Verify the usage of "End User Notification" is documented in the written policy and verify criteria for configuration. If "End User Notification:" variables are not configured to written documentation, this is a finding. If "End User Notification" is not documented in written policy, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-213338`

### Rule: The Trellix Application Control Options policies Enforce feature control memory protection must be enabled.

**Rule ID:** `SV-213338r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, the Trellix Application Control prevents installation of ActiveX controls on endpoints, enforces memory protection techniques on endpoints, and prevents MSI-installers from running on endpoints. The Feature Control allows for those safeguards to be bypassed and in doing so renders the Trellix Application Control less effective. Because ENS and HIPs have many more types of memory protection techniques than Trellix Application Control, memory protection must be explicitly disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is only applicable to Windows platforms. For MAC and Linux platforms, this is Not Applicable. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset(s) that need the organization-specific policy. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 8.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)". On the "Features" tab, review options selected. If the "Enforce feature control" check box is not selected and/or "Memory protection" is selected, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-213339`

### Rule: Enabled features under Trellix Application Control Options policies Enforce feature control must not be configured unless documented in written policy and approved by ISSO/ISSM.

**Rule ID:** `SV-213339r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, the Trellix Application Control prevents installation of ActiveX controls on endpoints, enforces memory protection techniques on endpoints, and prevents MSI-installers from running on endpoints. The "Feature Control" allows for those safeguards to be bypassed and in doing so renders the Trellix Application Control less effective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is only applicable to Windows platforms. For MAC and Linux platforms, this is Not Applicable. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 8.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)". On the "Features" tab, review options selected. If the "Enforce feature control" check box is selected with any features, consult with the ISSO/ISSM to review the written policy and ensure the usage of additional features are documented. If the usage of additional features are not documented in the written policy, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-213340`

### Rule: The Trellix Application Control Options Inventory option must be configured to hide OS Files.

**Rule ID:** `SV-213340r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, the Windows operating system files are excluded from the inventory. By selecting this option, the overwhelming the inventory with legitimate Windows Files in the <system drive>\Windows folder which are signed by the Microsoft certificate and all files in the <system drive>\Windows\winsxs folder will not be included in the inventory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is only applicable to Windows platforms. For MAC and Linux platforms, this is Not Applicable. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 8.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)". On the "Inventory" tab, review options selected. If the "Hide Windows OS Files: Inventory items signed with Microsoft certificates will not be sent to Trellix ePO." option is not selected, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-213341`

### Rule: The Trellix Application Control Options Inventory interval option must be configured to pull inventory from endpoints on a regular basis not to exceed seven days.

**Rule ID:** `SV-213341r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When Trellix Application Control is deployed on a system, it creates a whitelist of all executable binaries and scripts present on the system. The whitelist contains all authorized files, and only files that are present in the whitelist are allowed to execute. An executable binary, script, or process that is not in the whitelist is said to be unauthorized and is prevented from running. Trellix Application Control uses a centralized repository of trusted applications and dynamic whitelisting to reduce manual maintenance effort. Running frequent Pull Inventory tasks ensures inventory information does not become stale. There must be the minimum interval between consecutive inventory pull runs (when the inventory information is fetched from the endpoints). By default, this value is seven days and is the recommended setting. Pulling at an interval of greater than seven days will allow for the inventory of endpoints to become stale.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For VDI workstations that are reset copies of a VDI master image, this requirement is Not Applicable. For VDI master images, once an inventory is pulled after updates, further inventory is not required. Note: This requirement is only applicable to Windows platforms. For MAC and Linux platforms, this is Not Applicable. Consult with the ISSO to determine the endpoints used for the sampling of inventory pulls. From the Trellix ePO console, select Menu >> Systems >> System Tree. If sampling is a group, select the group in the System Tree and switch to the “Assigned Client Tasks” tab. Otherwise, select each endpoint on the “Systems” page and then click Actions >> Agent >> Modify Tasks on a Single System. Confirm a client task exists with an “SC: Pull Inventory” task type. Review the task properties to validate the task is configured to run at least as frequently as every seven days and tasks randomize the inventory pulls. If a sampling of endpoints does not have a “Pull Inventory” task type applied and/or the “Pull Inventory” task is not configured to run at least as frequently as every seven days at randomized intervals, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-213342`

### Rule: The Trellix Applications Default Rules policy must be part of the effective rules policy applied to every endpoint.

**Rule ID:** `SV-213342r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure Solidcore clients are only configured to STIG and organization-specific settings, organization-specific ePO policies must be applied to all organization workstation endpoints. The Trellix Application Control installs with two Default Rules policies. The Trellix Default Rules policy includes the whitelist for commonly used applications to the platform. The Trellix Applications Default Rules policy include the whitelist for Trellix applications. Both of these policies are at the "My Organization" level of the System Tree and must be inherited by all branches of the System Tree. Organization-specific applications would be whitelisted with an organization-specific policy combined with the two Default policies into one effective policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is only applicable to Windows platforms. For MAC and Linux platforms, this is Not Applicable. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 8.x: Application Control. For the "Application Control Rules (Windows)" Category, click on "Edit Assignments" under the "Actions" column. Verify that the Trellix Applications Default Rules policy is part of the assigned policies applied to the system being reviewed. If the Trellix Applications Default Rules policy is not part of the assigned polices applied to the system being reviewed, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-213343`

### Rule: A copy of the Trellix Default Rules policy must be part of the effective rules policy applied to every endpoint.

**Rule ID:** `SV-213343r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure Solidcore clients are only configured to STIG and organization-specific settings, an organization-specific ePO policies must be applied to all organization workstation endpoints. The Trellix Application Control installs with two Default Rules policies. The Trellix Default Rules policy includes the whitelist for commonly used applications to the platform. The Trellix Applications Default Rules policy include the whitelist for Trellix applications. Both of these policies are at the My Organization level of the System Tree and must be inherited by all branches of the System Tree. Organization-specific applications would be whitelisted with an organization-specific policy combined with the two Default policies into one effective policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is only applicable to Windows platforms. For MAC and Linux platforms, this is Not Applicable. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 8.x: Application Control. For the "Application Control Rules (Windows)" Category, click on "Edit Assignments" under the "Actions" column. Verify that a Rules policy copied from the Trellix Default Rules policy is part of the assigned policies applied to the system being reviewed. If a Rules policy copied from the Trellix Default Rules policy is not part of the assigned policies applied to the system being reviewed, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-213344`

### Rule: The organization-specific Rules policies must be part of the effective rules policy applied to all endpoints.

**Rule ID:** `SV-213344r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure Solidcore clients are only configured to STIG and organization-specific settings, an organization-specific ePO policies must be applied to all organization workstation endpoints. The Trellix Application Control installs with two Default Rules policies. The Trellix Default Rules policy includes the whitelist for commonly used applications to the platform. The Trellix Applications Default Rules policy include the whitelist for Trellix applications. Both of these policies are at the "My Organization" level of the System Tree and must be inherited by all branches of the System Tree. Organization-specific applications would be whitelisted with an organization-specific policy combined with the two Default policies into one effective policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 8.x: Application Control. For Windows Platforms, select the "Application Control Rules (Windows)" Category, click on "Edit Assignments" under the "Actions" column. For MAC/Linux Platforms,select the "Application Control Rules (Unix)" Category, click on "Edit Assignments" under the "Actions" column. Verify that there exists at least one organization-specific Rules policy as part of the assigned policies applied to the system being reviewed. If an organization-specific Rules policy is not part of the assigned polices applied to the system being reviewed, this is a finding. If the only "Application Control Rules" policy applied to the system is the "Trellix Default" policy, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-213345`

### Rule: The organization-specific Solidcore Client Policies must be created and applied to all endpoints.

**Rule ID:** `SV-213345r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Trellix Application Control is deployed with default policies. To ensure the default policies are not used and that an organization knowingly configures their systems to their own configuration requirements, organization-specific policies will need to be created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 8.x: General. From the "Policy" column, select the policy associated with the Category "Configuration (Client)" that is specific to the organization. If the only "Configuration (Client)" policy applied to the system is the "Trellix Default" policy, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-213346`

### Rule: The Throttling settings must be enabled and configured to settings according to organizations requirements.

**Rule ID:** `SV-213346r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The throttling settings regulate the data flow between the clients and Trellix ePO. The value for each category defines the number of entries that will be sent to the Trellix ePO daily. Clients start caching for the defined category when the specified threshold value is reached. After the cache is full, new data for that category is dropped and not sent to the Trellix ePO. As such, settings must be high enough to allow for all data to reach the Trellix ePO.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 8.x: General. From the "Policy" column, select the policy associated with the Category "Configuration (Client)" that is specific to the organization and select the "Throttling" tab. Verify the "Enable Throttling" check box is selected. Verify the throttling settings are configured according to organization's written policy. If the "Enable Throttling" check box is not selected, this is a finding. If the throttling settings do not match the organization's written policy or the settings are not documented in the written policy, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-213347`

### Rule: The Solidcore Client Exception Rules must be documented in the organizations written policy.

**Rule ID:** `SV-213347r961479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When exceptions are created for applications, it results in potential attack vectors. As such, exceptions should only be created with a full approval by the local ISSO/ISSM. The organization's entire written policy requires approval by the ISSO/ISSM/AO and is required to be under CAB/CCB oversight.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 8.x: General. For Windows platforms, from the "Policy" column, select the policy associated with the Category "Exception Rules (Windows)" that is specific to the organization. For Unix Platforms, from the "Policy" column, select the policy associated with the Category "Exception Rules (Unix)" that is specific to the organization. If the "Exception Rules" policy applied to the system has exceptions documented, verify the exceptions are documented in the organization's written policy. If the Exceptions are not documented, this is a finding.

