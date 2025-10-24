# STIG Benchmark: McAfee Application Control 7.x Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000386

**Group ID:** `V-74175`

### Rule: A McAfee Application Control written policy must be documented to outline the organization-specific variables for application whitelisting.

**Rule ID:** `SV-88849r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling application whitelisting without adequate design and organization-specific requirements will either result in an implementation which is too relaxed or an implementation which causes denial of service to its user community. Documenting the specific requirements and trust model before configuring and deploying the McAfee Application Control software is mandatory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the ISSO/ISSM to review the organizational-specific written policy for the McAfee Application Control software. If no written policy exists, this is a finding.

## Group: SRG-APP-000172

**Group ID:** `V-74195`

### Rule: The Solidcore client Command Line Interface (CLI) Access Password protection process must be documented in the organizations written policy.

**Rule ID:** `SV-88869r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Solidcore client can be configured locally at the CLI, but only when accessed with the required password. Since the McAfee Application Control configuration is to be managed by ePO policies, allowing enablement of the CLI to would introduce the capability of local configuration changes. Strict management of the accessibility of the CLI is necessary in order to prevent its misuse. The misuse of the CLI would open the system up to the possible configuration changes potentially allowing malicious applications to execute unknowingly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: The CLI Access is in lockdown mode by default when being managed by ePO. Since the CLI Access can be recovered for troubleshooting, this requirement needs to be met. Consult with the ISSO/ISSM to obtain a copy of the organization's documented policy for application whitelisting. Review the written policy for how the Solidcore client interface is used by the organization. Verify the policy identifies how the CLI password is protected. Ask the ePO admin, "What protection measures are used for the CLI password?" The protection measures should include, at a minimum, storage in a sealed envelope, which is then stored in an approved safe. Note: The envelope will contain the last access date along with those authorized to use it. If the written policy does not contain specific information on how the CLI password is protected and/or if that policy does not include, at a minimum, that the password be stored in a sealed envelope in an approved safe with the last access date noted, this is a finding.

## Group: SRG-APP-000174

**Group ID:** `V-74197`

### Rule: The requirement for scheduled Solidcore client Command Line Interface (CLI) Access Password changes must be documented in the organizations written policy.

**Rule ID:** `SV-88871r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Solidcore client can be configured locally at the CLI, but only when accessed with the required password. The misuse of the CLI would open the system up to the possible configuration, allowing malicious applications to execute unknowingly. Strict management of the accessibility of the CLI is necessary in order to prevent its misuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: The CLI Access is in lockdown mode by default when being managed by ePO. Since the CLI Access can be recovered for troubleshooting, this requirement needs to be met. Consult with the ISSO/ISSM to obtain a copy of the organization's documented policy for application whitelisting. Review the written policy for how the Solidcore client interface is used by the organization. Verify the policy identifies the frequency with which the CLI password is changed. If the written policy does not contain specific information on frequency with which the CLI password is changed, this is a finding.

## Group: SRG-APP-000397

**Group ID:** `V-74199`

### Rule: The process by which the Solidcore client Command Line Interface (CLI) Access Password is made available to administrators when needed must be documented in the organizations written policy.

**Rule ID:** `SV-88873r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Solidcore client can be configured locally at the CLI, but only when accessed with the required password. Since the McAfee Application Control configuration is to be managed by ePO policies, allowing enablement of the CLI to would introduce the capability of local configuration changes. Strict management of the accessibility of the CLI is necessary in order to prevent its misuse. The misuse of the CLI would open the system up to the possible configuration changes potentially allowing malicious applications to execute unknowingly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: The CLI Access is in lockdown mode by default when being managed by ePO. Since the CLI Access can be recovered for troubleshooting, this requirement needs to be met. Consult with the ISSO/ISSM to obtain a copy of the organization's documented policy for application whitelisting. The policy must contain procedures for accessing the CLI password, to include the SA gaining access to an approved safe in order for obtaining the password. If a procedure does not exist for accessing the CLI password as described above, this is a finding.

## Group: SRG-APP-000276

**Group ID:** `V-74201`

### Rule: The McAfee Application Control Options Advanced Threat Defense (ATD) settings, if being used, must be confined to the organizations enclave.

**Rule ID:** `SV-88875r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data will be leaving the endpoint to be analyzed by the ATD. Because data could feasibly be intercepted en route, risk of outside threats is minimized by ensuring the ATD is in the same enclave as the endpoints.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If an ATD server is not being used in the environment, this is Not Applicable. Consult with the ISSO/ISSM to review the written policy to ensure the usage of an ATD is documented. If the usage of an ATD is not documented in the written policy, this is a finding. Determine the location of the ATD being used by the organization and verify the ATD is confined to the organization's enclave. If the location of the ATD being used by the organization cannot be determined and the ATD is not confined to the organization's enclave, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-74203`

### Rule: The configuration of features under McAfee Application Control Options policies Enforce feature control must be documented in the organizations written policy.

**Rule ID:** `SV-88877r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, the McAfee Application Control prevents installation of ActiveX controls on endpoints, enforces memory protection techniques on endpoints, and prevents MSI-installers from running on endpoints. The Feature Control allows for those safeguards to be bypassed and in doing so renders the McAfee Application Control less effective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the ISSO/ISSM to obtain a copy of the organization's documented policy for application whitelisting. Review the written policy for how the Solidcore client interface is used by the organization. Verify the written policy identifies whether additional features are enabled or not under "Enforce feature control" of the McAfee Application Control Options ePO policy. If the written policy does not identify whether additional features are enabled or not under "Enforce feature control" of the McAfee Application Control Options ePO policy, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-74205`

### Rule: The organizations written policy must include a process for how whitelisted applications are deemed to be allowed.

**Rule ID:** `SV-88879r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling application whitelisting without adequate design and organization-specific requirements will either result in an implementation which is too relaxed or an implementation which causes denial of service to its user community. Documenting the specific requirements and trust model before configuring and deploying the McAfee Application Control software is mandatory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the ISSO/ISSM to review the organizational-specific written policy for the McAfee Application Control software. Verify the written policy includes a process for how applications are vetted and deemed to be allowed. If no written policy exists, this is a finding. If written policy does not include a process for vetting applications before allowing them, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-74207`

### Rule: The organizations written policy must include procedures for how often the whitelist of allowed applications is reviewed.

**Rule ID:** `SV-88881r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling application whitelisting without adequate design and organization-specific requirements will either result in an implementation which is too relaxed or an implementation which causes denial of service to its user community. Documenting the specific requirements and trust model before configuring and deploying the McAfee Application Control software is mandatory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the ISSO/ISSM to review the organizational-specific written policy for the McAfee Application Control software. Verify the written policy includes a process for how often the application whitelist is reviewed. If no written policy exists, this is a finding. If written policy does not include a process for how often the application whitelist is reviewed, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-74209`

### Rule: The Solidcore client must be enabled.

**Rule ID:** `SV-88883r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Application Control whitelisting must be enabled on all workstation endpoints. To enable Application Control, the Solidcore client needs to be in enabled mode.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated and view its properties. Click on the "Products" tab. Under "Product", verify the Solidcore 7 client is listed as a product. If exists, click on the row to review additional information. Verify status shows "Enabled". If the Solidcore 7 client is listed as an installed product but the status is not "Enabled", this is a finding.

## Group: SRG-APP-000383

**Group ID:** `V-74211`

### Rule: The Solidcore client Command Line Interface (CLI) must be in lockdown mode.

**Rule ID:** `SV-88885r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>By default, when an endpoint's Solidcore installation is managed by the ePO server, the CLI will automatically be in lockdown mode. This will ensure the endpoint receives all of its Solidcore configuration settings from the ePO server. The CLI can, however, be activated for troubleshooting efforts during which time the ePO settings will not be enforced. Leaving the CLI in an allowed status will prevent the endpoint from receiving changes from the ePO server for the Solidcore client.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine CLI status. Access the system being reviewed. From an operating system command line, execute the following command: sadmin status <enter> If the status for CLI is "Allowed", this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-74213`

### Rule: The Solidcore client Command Line Interface (CLI) Access Password must be changed from the default.

**Rule ID:** `SV-88887r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Solidcore client can be configured locally at the CLI, but only when accessed with the required password. Since the McAfee Application Control configuration is to be managed by ePO policies, allowing enablement of the CLI to would introduce the capability of local configuration changes. Strict management of the accessibility of the CLI is necessary in order to prevent its misuse. The misuse of the CLI would open the system up to the possible configuration changes potentially allowing malicious applications to execute unknowingly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is a manual procedure to verify the CLI Access Password has been changed from its default setting by the ePO administrator. Ask the ePO admin, "Has the CLI Access Password been changed from its default setting?" If the default password is being used, this is a finding. Note: The password does not need to be divulged during the review. An interview question of the SA to validate that it is not the default is sufficient.

## Group: SRG-APP-000386

**Group ID:** `V-74215`

### Rule: The organization-specific Rules policy must only include executable and dll files that are associated with applications as allowed by the organizations written policy.

**Rule ID:** `SV-88889r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure Solidcore clients are only configured to STIG and organization-specific settings, organization-specific ePO policies must be applied to all organization workstation endpoints. The McAfee Application Control installs with two Default Rules policies. The McAfee Default Rules policy includes the whitelist for commonly used applications to the platform. The McAfee Applications Default Rules policy include the whitelist for McAfee applications. Both of these policies are at the "My Organization" level of the System Tree and must be inherited by all branches of the System Tree. Organization-specific applications would be whitelisted with an organization-specific policy combined with the two Default policies into one effective policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the organization's written policy for the McAfee Application Control software from the System or ePO Administrator. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select "Solidcore 7.x: Application Control". For the "Application Control Rules (Windows)" Category, click on "Edit Assignments" under the "Actions" column. Identify the organization-specific Rules policy applied to the system being reviewed. Click on "Edit Policy" beside the organization-specific Rules policy. Verify the list of applications under each of the "Rules Groups" in the organization-specific Rules policy against the written policy's list of allowed applications. If the organization-specific Rules policy contains any applications not documented in the written policy as allowed, this is a finding.

## Group: SRG-APP-000276

**Group ID:** `V-74217`

### Rule: The McAfee Application Control Options Reputation setting must be configured to use the McAfee Global Threat Intelligence (McAfee GTI) option.

**Rule ID:** `SV-88891r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a Threat Intelligence Exchange (TIE) server is being used in the organization, reputation for files and certificates is fetched from the TIE server. The reputation values control execution at endpoints and are displayed on the Application Control pages on the McAfee ePO console. If the GTI is being used, reputation for files and certificates is fetched from the McAfee GTI. For both methods, the administrator can review the reputation values and make informed decisions for inventory items in the enterprise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
NOTE: This requirement is Not Applicable on a classified SIPRNet or otherwise closed network. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 7.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)" that is specific for the asset being reviewed. Select the "Reputation" tab. Verify the "Use McAfee Global Threat Intelligence (McAfee GTI)" option is selected. Note: The "McAfee GTI" option must be selected, as a failover, even if an internal McAfee TIE server is configured. If the "McAfee GTI" option is not selected, this is a finding.

## Group: SRG-APP-000165

**Group ID:** `V-74219`

### Rule: The use of a Solidcore 7.x local Command Line Interface (CLI) Access Password must be documented in the organizations written policy.

**Rule ID:** `SV-88893r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Solidcore client can be configured locally at the CLI, but only when accessed with the required password. Since the McAfee Application Control configuration is to be managed by ePO policies, allowing enablement of the CLI to would introduce the capability of local configuration changes. Strict management of the accessibility of the CLI is necessary in order to prevent its misuse. The misuse of the CLI would open the system up to the possible configuration changes potentially allowing malicious applications to execute unknowingly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: The CLI Access is in lockdown mode by default when being managed by ePO. Since the CLI Access can be recovered for troubleshooting, this requirement needs to be met. Consult with the ISSO/ISSM to obtain a copy of the organization's documented policy for application whitelisting. Review the written policy for how and when the Solidcore CLI is used by the organization. If the use of the CLI is not documented in the organization's written policy, this is a finding.

## Group: SRG-APP-000169

**Group ID:** `V-74221`

### Rule: The Solidcore client Command Line Interface (CLI) Access password complexity requirements must be documented in the organizations written policy.

**Rule ID:** `SV-88895r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Solidcore client can be configured locally at the CLI, but only when accessed with the required password. The misuse of the CLI would open the system up to the possible configuration, allowing malicious applications to execute unknowingly. Strict management of the accessibility of the CLI is necessary in order to prevent its misuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: The CLI Access is in lockdown mode by default when being managed by ePO. Since the CLI Access can be recovered for troubleshooting, this requirement needs to be met. Since the Solidcore CLI does not allow for technical enforcement of password complexity the enforcement will be via this written policy directive. Consult with the ISSO/ISSM to obtain a copy of the organization's documented policy for application whitelisting. Review the written policy for CLI password complexity requirements. Verify the policy requires the password to be 15 characters in length and contain a mix of at least one lower-case, one upper-case, one number, and one special character. If the written policy does not document the requirement for password complexity and/or does not specify the password must be 15 characters in length and contain a mix of at least one lower-case, one upper-case, one number, and one special character, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-74223`

### Rule: The McAfee Application Control Options Reputation-Based Execution settings, if enabled, must be configured to allow Most Likely Trusted or Known Trusted only.

**Rule ID:** `SV-88897r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a file is executed on an endpoint, the Application Control performs multiple checks to determine whether to allow or ban the execution. Only files with a reputation of "Most Likely Trusted", "Known Trusted" or "Might be Trusted" are considered to be allowed. By configuring the setting to only "Most Likely Trusted" or "Known Trusted", the files with a reputation of "Might be Trusted" are blocked. While this may impact operationally in the beginning, after the inventories are vetted by the administrators, files with a "Might be Trusted" value may be recategorized in that organization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If Reputation-Based Execution settings is not enabled, this check is Not Applicable. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 7.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)" that is specific for the asset being reviewed. Select the "Reputation" tab. Verify the "Reputation-Based Execution Settings" is configured to allow binaries with "Most Likely Trusted" and above. If the allow binaries "Most Likely Trusted" and above is not selected for "Reputation-Based Execution Settings", this is a finding.

## Group: SRG-APP-000276

**Group ID:** `V-74225`

### Rule: The McAfee Application Control Options Advanced Threat Defense (ATD) settings must not be enabled unless an internal ATD is maintained by the organization.

**Rule ID:** `SV-88899r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This option will automatically send files with a specific file reputation to ATD for further analysis. This option is not selected by default and must only be selected if an ATD is being used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If an ATD server is not being used in the environment, this is Not Applicable. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 7.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)" that is specific for the asset being reviewed. Select the "Reputation" tab. Verify the option for sending binaries for analysis under the "Advanced Threat Defense (ATD) settings" is selected. Consult with the ISSO/ISSM to review the written policy to verify the usage of an ATD is documented. If the option for sending binaries for analysis under the "Advanced Threat Defense (ATD) settings" is selected and the written policy does not include documentation on the usage of an ATD, this is a finding.

## Group: SRG-APP-000276

**Group ID:** `V-74227`

### Rule: The McAfee Application Control Options Advanced Threat Defense (ATD) settings, if being used, must be configured to send all binaries with a reputation of Might be Trusted and below for analysis.

**Rule ID:** `SV-88901r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When the file reputation of "Might be Trusted" is configured for being forwarded to ATD, all files with the reputation of "Might be Trusted", "Unknown", "Might be Malicious", "Most Likely Malicious" and "Known Malicious" are forwarded to the ATD. The files with "Might be Trusted" reputation may be redesignated as "Trusted" after analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If an ATD server is not being used in the environment, this is Not Applicable. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 7.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)" that is specific for the asset being reviewed. Select the "Reputation" tab. If the option for sending binaries for analysis under the "Advanced Threat Defense (ATD) settings" is selected, verify the level of binaries to be sent for analysis is "Might be Trusted" and below. If the level of binaries to be sent for analysis is not "Might be Trusted", this is a finding.

## Group: SRG-APP-000276

**Group ID:** `V-74229`

### Rule: The McAfee Application Control Options Advanced Threat Defense (ATD) settings, if being used, must be configured to only send binaries with a size of 5 MB or less.

**Rule ID:** `SV-88903r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Since binaries can be large, the file size must be limited to avoid congestion on the network and degradation on the endpoint when sending the binaries to the ATD.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If an ATD server is not being used in the environment, this is Not Applicable. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 7.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)" that is specific for the asset being reviewed. Select the "Reputation" tab. If the option for sending binaries for analysis under the "Advanced Threat Defense (ATD) settings" is selected, verify the "Limit file size to" option is set to 5 MB or less. If the "Limit file size to" option is not set to 5 MB or less, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-74231`

### Rule: Organization-specific McAfee Applications Control Options policies must be created and applied to all endpoints.

**Rule ID:** `SV-88905r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure Solidcore clients are only configured to STIG and organization-specific settings, organization-specific ePO policies must be applied to all organization workstation endpoints rather than resorting to the McAfee Applications Control (Default) policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 7.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)" that is specific for the asset being reviewed. If the only "Application Control Options" policy applied to the system is the "McAfee Default" policy, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-74233`

### Rule: The McAfee Application Control Options policy must be configured to disable Self-Approval.

**Rule ID:** `SV-88907r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The McAfee Application Control Self-Approval feature allows the user to take an action when a user tries to run a new or unknown application.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 7.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)". On the "Self-Approval" tab, verify the "Enable Self-Approval" check box is not selected. If the "Enable Self-Approval" check box is selected, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-74235`

### Rule: The McAfee Application Control Options policy End User Notification, if configured by organization, must have all default variables replaced with the organization-specific data.

**Rule ID:** `SV-88909r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "User Message" option will show a dialog box when an event is detected and display the organization-specified text in the message.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If "End User Notification" is not used by the organization, this is Not Applicable. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 7.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)". On the "End User Notification" tab, determine if the "User Message:" option "Show the messages dialog box when an event is detected and display the specified text in the message." is selected. If "Show the messages dialog box when an event is detected and display the specified text in the message." is not selected, this is Not Applicable. If "Show the messages dialog box when an event is detected and display the specified text in the message." is selected, consult with the ISSO/ISSM to review the organizational-specific written policy for the McAfee Application Control software. Verify the usage of "End User Notification" is documented in the written policy and verify criteria for configuration. If "End User Notification:" variables are not configured to written documentation, this is a finding. If "End User Notification" is not documented in written policy, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-74237`

### Rule: The McAfee Application Control Options policies Enforce feature control memory protection must be enabled.

**Rule ID:** `SV-88911r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, the McAfee Application Control prevents installation of ActiveX controls on endpoints, enforces memory protection techniques on endpoints, and prevents MSI-installers from running on endpoints. The Feature Control allows for those safeguards to be bypassed and in doing so renders the McAfee Application Control less effective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If HIPS/ENS is enabled and enforced, this is Not Applicable. From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 7.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)". On the "Features" tab, review options selected. If the "Enforce feature control" check box is not selected and "Memory protection" is selected, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-74239`

### Rule: Enabled features under McAfee Application Control Options policies Enforce feature control must not be configured unless documented in written policy and approved by ISSO/ISSM.

**Rule ID:** `SV-88913r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, the McAfee Application Control prevents installation of ActiveX controls on endpoints, enforces memory protection techniques on endpoints, and prevents MSI-installers from running on endpoints. The "Feature Control" allows for those safeguards to be bypassed and in doing so renders the McAfee Application Control less effective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 7.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)". On the "Features" tab, review options selected. If the "Enforce feature control" check box is selected with any features, consult with the ISSO/ISSM to review the written policy and ensure the usage of additional features are documented. If the usage of additional features are not documented in the written policy, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-74241`

### Rule: The McAfee Application Control Options Inventory option must be configured to hide OS Files.

**Rule ID:** `SV-88915r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, the Windows operating system files are excluded from the inventory. By selecting this option, the overwhelming the inventory with legitimate Windows Files in the <system drive>\Windows folder which are signed by the Microsoft certificate and all files in the <system drive>\Windows\winsxs folder will not be included in the inventory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 7.x: Application Control. From the "Policy" column, select the policy associated with the Category "Application Control Options (Windows)". On the "Inventory" tab, review options selected. If the "Hide Windows OS Files: Inventory items signed with Microsoft certificates will not be sent to McAfee ePO." option is not selected, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-74243`

### Rule: The McAfee Application Control Options Inventory interval option must be configured to pull inventory from endpoints on a regular basis not to exceed seven days.

**Rule ID:** `SV-88917r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When McAfee Application Control is deployed on a system, it creates a whitelist of all executable binaries and scripts present on the system. The whitelist contains all authorized files, and only files that are present in the whitelist are allowed to execute. An executable binary, script, or process that is not in the whitelist is said to be unauthorized and is prevented from running. McAfee Application Control uses a centralized repository of trusted applications and dynamic whitelisting to reduce manual maintenance effort. Running frequent Pull Inventory tasks ensures inventory information does not become stale. There must be the minimum interval between consecutive inventory pull runs (when the inventory information is fetched from the endpoints). By default, this value is 7 days and is the recommended setting. Pulling at an interval of greater than 7 days will allow for the inventory of endpoints to become stale. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Consult with the ISSO to determine the endpoints used for the sampling of inventory pulls. From the McAfee ePO console, select Menu >> Systems >> System Tree. If sampling is a group, select the group in the System Tree and switch to the “Assigned Client Tasks” tab. Otherwise, select each endpoint on the “Systems” page and then click Actions >> Agent >> Modify Tasks on a Single System. Confirm a client task exists with an “SC: Pull Inventory” task type. Review the task properties to validate the task is configured to run at least as frequently as every 7 days. If a sampling of endpoints does not have a “Pull Inventory” task type applied and/or the “Pull Inventory” task is not configured to run at least as frequently as every 7 days, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-74247`

### Rule: The McAfee Applications Default Rules policy must be part of the effective rules policy applied to every endpoint.

**Rule ID:** `SV-88921r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure Solidcore clients are only configured to STIG and organization-specific settings, organization-specific ePO policies must be applied to all organization workstation endpoints. The McAfee Application Control installs with two Default Rules policies. The McAfee Default Rules policy includes the whitelist for commonly used applications to the platform. The McAfee Applications Default Rules policy include the whitelist for McAfee applications. Both of these policies are at the "My Organization" level of the System Tree and must be inherited by all branches of the System Tree. Organization-specific applications would be whitelisted with an organization-specific policy combined with the two Default policies into one effective policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 7.x: Application Control. For the "Application Control Rules (Windows)" Category, click on "Edit Assignments" under the "Actions" column. Verify that the McAfee Applications Default Rules policy is part of the assigned policies applied to the system being reviewed. If the McAfee Applications Default Rules policy is not part of the assigned polices applied to the system being reviewed, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-74249`

### Rule: A copy of the McAfee Default Rules policy must be part of the effective rules policy applied to every endpoint.

**Rule ID:** `SV-88923r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure Solidcore clients are only configured to STIG and organization-specific settings, an organization-specific ePO policies must be applied to all organization workstation endpoints. The McAfee Application Control installs with two Default Rules policies. The McAfee Default Rules policy includes the whitelist for commonly used applications to the platform. The McAfee Applications Default Rules policy include the whitelist for McAfee applications. Both of these policies are at the My Organization level of the System Tree and must be inherited by all branches of the System Tree. Organization-specific applications would be whitelisted with an organization-specific policy combined with the two Default policies into one effective policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 7.x: Application Control. For the "Application Control Rules (Windows)" Category, click on "Edit Assignments" under the "Actions" column. Verify that a Rules policy copied from the McAfee Default Rules policy is part of the assigned policies applied to the system being reviewed. If a Rules policy copied from the McAfee Default Rules policy is not part of the assigned policies applied to the system being reviewed, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-74251`

### Rule: The organization-specific Rules policies must be part of the effective rules policy applied to all endpoints.

**Rule ID:** `SV-88925r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure Solidcore clients are only configured to STIG and organization-specific settings, an organization-specific ePO policies must be applied to all organization workstation endpoints. The McAfee Application Control installs with two Default Rules policies. The McAfee Default Rules policy includes the whitelist for commonly used applications to the platform. The McAfee Applications Default Rules policy include the whitelist for McAfee applications. Both of these policies are at the "My Organization" level of the System Tree and must be inherited by all branches of the System Tree. Organization-specific applications would be whitelisted with an organization-specific policy combined with the two Default policies into one effective policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 7.x: Application Control. For the "Application Control Rules (Windows)" Category, click on "Edit Assignments" under the "Actions" column. Verify that there exists at least one organization-specific Rules policy as part of the assigned policies applied to the system being reviewed. If an organization-specific Rules policy is not part of the assigned polices applied to the system being reviewed, this is a finding. If the only "Application Control Rules" policy applied to the system is the "McAfee Default" policy, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-74253`

### Rule: The organization-specific Solidcore Client Policies must be created and applied to all endpoints.

**Rule ID:** `SV-88927r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>McAfee Application Control is deployed with default policies. To ensure the default policies are not used and that an organization knowingly configures their systems to their own configuration requirements, organization-specific policies will need to be created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 7.x: General. From the "Policy" column, select the policy associated with the Category "Configuration (Client)" that is specific to the organization. If the only "Configuration (Client)" policy applied to the system is the "McAfee Default" policy, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-74255`

### Rule: The Throttling settings must be enabled and configured to settings according to organizations requirements.

**Rule ID:** `SV-88929r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The throttling settings regulate the data flow between the clients and McAfee ePO. The value for each category defines the number of entries that will be sent to the McAfee ePO daily. Clients start caching for the defined category when the specified threshold value is reached. After the cache is full, new data for that category is dropped and not sent to the McAfee ePO. As such, settings must be high enough to allow for all data to reach the McAfee ePO.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 7.x: General. From the "Policy" column, select the policy associated with the Category "Configuration (Client)" that is specific to the organization and select the "Throttling" tab. Verify the "Enable Throttling" check box is selected. Verify the throttling settings are configured according to organization's written policy. If the "Enable Throttling" check box is not selected, this is a finding. If the throttling settings do not match the organization's written policy or the settings are not documented in the written policy, this is a finding.

## Group: SRG-APP-000386

**Group ID:** `V-74257`

### Rule: The Solidcore Client Exception Rules must be documented in the organizations written policy.

**Rule ID:** `SV-88931r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When exceptions are created for applications, it results in potential attack vectors. As such, exceptions should only be created with a full approval by the local ISSO/ISSM. The organization's entire written policy requires approval by the ISSO/ISSM/AO and is required to be under CAB/CCB oversight.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the ePO server console System Tree, select the "Systems" tab. Select "This Group and All Subgroups". Select the asset to be validated. Select "Actions". Select "Agent". Select "Modify Policies on a Single System". From the product pull-down list, select Solidcore 7.x: General. From the "Policy" column, select the policy associated with the Category "Exception Rules (Windows)" that is specific to the organization. If the "Exception Rules (Windows)" policy applied to the system has exceptions documented, verify the exceptions are documented in the organization's written policy. If the Exceptions are not documented, this is a finding.

## Group: SRG-APP-000456

**Group ID:** `V-74258`

### Rule: The version of McAfee Application Control running on the system must be a supported version.

**Rule ID:** `SV-88932r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and to applications that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
McAfee Application Control 7.0 Managed Desktop is no longer supported by the vendor. If the system is running McAfee Application Control 7.0 Managed Desktop, this is a finding.

