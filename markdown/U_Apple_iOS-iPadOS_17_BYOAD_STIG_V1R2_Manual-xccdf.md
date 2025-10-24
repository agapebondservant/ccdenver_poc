# STIG Benchmark: Apple iOS/iPadOS 17 BYOAD Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: PP-BYO-000020

**Group ID:** `V-259742`

### Rule: The EMM system supporting the iOS/iPadOS 17 BYOAD must be configured for autonomous monitoring, compliance, and validation to ensure security/configuration settings of mobile devices do not deviate from the approved configuration baseline.

**Rule ID:** `SV-259742r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD policy requires BYOAD devices with DOD data be managed by a DOD MDM server, MAM server, or VMI system. This ensures the device can be monitored for compliance with the approved security baseline and managed data and apps can be removed when the device is out of compliance, which protects DOD data from unauthorized exposure. Examples of possible EMM security controls are as follows: 1. Device access restrictions: Restrict or isolate access based on the device's access type (i.e., from the internet), authentication type (e.g., password), credential strength, etc. 2. User and device activity monitoring: Configured to detect anomalous activity, malicious activity, and unauthorized attempts to access DOD information. 3. Device health tracking: Monitor device attestation, health, and agents reporting compromised applications, connections, intrusions, and/or signatures. Reference: DOD policy "Use of Non-Government Mobile Devices". 3.a.(3)ii, 3.b.(2)ii,1 and 2. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM system supporting the iOS/iPadOS 17 BYOAD has been configured to conduct autonomous monitoring, compliance, and validation to ensure security/configuration settings of mobile devices do not deviate from the approved configuration baseline. The exact procedure will depend on the EMM system used at the site. If the EMM system supporting the iOS/iPadOS 17 BYOAD has not been configured to conduct autonomous monitoring, compliance, and validation to ensure security/configuration settings of mobile devices, this is a finding.

## Group: PP-BYO-000030

**Group ID:** `V-259743`

### Rule: The EMM system supporting the iOS/iPadOS 17 BYOAD must be configured to initiate autonomous monitoring, compliance, and validation prior to granting the BYOAD access to DOD information and IT resources.

**Rule ID:** `SV-259743r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD policy requires BYOAD devices with DOD data be managed by a DOD MDM server, MAM server, or VMI system. This ensures the device can be monitored for compliance with the approved security baseline and managed data and apps can be removed when the device is out of compliance, which protects DOD data from unauthorized exposure. Reference: DOD policy "Use of Non-Government Mobile Devices". 3.a.(3)iii. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM system supporting the iOS/iPadOS 17 BYOAD has been configured to initiate autonomous monitoring, compliance, and validation prior to granting the BYOAD access to DOD information and IT resources. The exact procedure will depend on the EMM system used at the site. If the EMM system supporting the iOS/iPadOS 17 BYOAD has not been configured to initiate autonomous monitoring, compliance, and validation prior to granting the BYOAD access to DOD information and IT resources, this is a finding.

## Group: PP-BYO-000040

**Group ID:** `V-259744`

### Rule: The EMM system supporting the iOS/iPadOS 17 BYOAD must be configured to detect if the BYOAD native security controls are disabled.

**Rule ID:** `SV-259744r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Examples of indicators that the device native security controls have been disabled include jailbroken or rooted devices. DOD policy requires BYOAD devices with DOD data be managed by a DOD MDM server, MAM server, or VMI system. This ensures the device can be monitored for compliance with the approved security baseline and the work profile can be removed when the device is out of compliance, which protects DOD data from unauthorized exposure. Detection via collection and analysis of BYOAD-generated logs for noncompliance indicators is acceptable. This detection capability must be implemented prior to BYOAD access to DOD information and IT resources and continuously monitored on the DOD-managed segment of the BYOAD enrolled in the program. If non-DOD information (i.e., personal user data, device information) outside the DOD-managed segment of the BYOAD is required to be accessed, collected, monitored, tracked (i.e., location), or maintained, the circumstances under which this may be done must be outlined in the user agreement. Reference: DOD policy "Use of Non-Government Mobile Devices". 3.a.(3)iii. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM system supporting the iOS/iPadOS 17 BYOAD has been configured to detect if the BYOAD native security controls are disabled. The exact procedure will depend on the EMM system used at the site. If the EMM system supporting the iOS/iPadOS 17 BYOAD is not configured to detect if the BYOAD native security controls are disabled, this is a finding.

## Group: PP-BYO-000050

**Group ID:** `V-259745`

### Rule: The EMM system supporting the iOS/iPadOS 17 BYOAD must be configured to detect if known malicious, blocked, or prohibited applications are installed on the BYOAD (DOD-managed segment only).

**Rule ID:** `SV-259745r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD policy requires BYOAD devices with DOD data be managed by a DOD MDM server, MAM server, or VMI system. This ensures the device can be monitored for compliance with the approved security baseline and managed data and apps can be removed when the device is out of compliance, which protects DOD data from unauthorized exposure. Detection via collection and analysis of BYOAD-generated logs for noncompliance indicators is acceptable. This detection capability must be implemented prior to AMD (Approved Mobile Device, called BYOAD device in the STIG) enrollment and AMD access to DOD information and IT resources and continuously monitored on the DOD-managed segment of the AMD enrolled in the program. If non-DOD information (i.e., personal user data, device information) outside the DOD-managed segment of the AMD is required to be accessed, collected, monitored, tracked (i.e., location), or maintained, the circumstances under which this may be done must be outlined in the user agreement. Reference: DOD policy "Use of Non-Government Mobile Devices". 3.a.(3)iii. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an app vetting process is being used before managed apps are placed in the MDM app repository. If an app vetting process is not being used before managed apps are placed in the MDM app repository, this is a finding.

## Group: PP-BYO-000060

**Group ID:** `V-259746`

### Rule: The EMM system supporting the iOS/iPadOS 17 BYOAD must be configured to detect if the BYOAD is configured to access nonapproved third-party applications stores (DOD-managed segment only).

**Rule ID:** `SV-259746r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD policy requires BYOAD devices with DOD data be managed by a DOD MDM server, MAM server, or VMI system. This ensures the device can be monitored for compliance with the approved security baseline and managed data and apps can be removed when the device is out of compliance, which protects DOD data from unauthorized exposure. Detection via collection and analysis of BYOAD-generated logs for noncompliance indicators is acceptable. This detection capability must be implemented prior to AMD (Approved Mobile Device, called BYOAD device in the STIG) enrollment and AMD access to DOD information and IT resources and continuously monitored on the DOD-managed segment of the AMD enrolled in the program. If non-DOD information (i.e., personal user data, device information) outside the DOD-managed segment of the AMD is required to be accessed, collected, monitored, tracked (i.e., location), or maintained, the circumstances under which this may be done must be outlined in the user agreement. Reference: DOD policy "Use of Non-Government Mobile Devices". 3.a.(3)iii. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm "Allow Trusting New Enterprise App Authors" is disabled. This procedure is performed in the Apple iOS/iPadOS management tool and on the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the Management tool, verify "Allow Trusting New Enterprise App Authors" is disabled. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "Profiles & Device Management" or "Profiles". 4. Tap the Configuration Profile from the Apple iOS/iPadOS management tool containing the restrictions policy. 5. Tap "Restrictions". 6. Verify "Trusting enterprise apps not allowed" is listed. If "Allow Trusting New Enterprise App Authors" is not disabled in the iOS/iPadOS management tool or on the iPhone and iPad, this is a finding. Note: This requirement is the same as AIOS-17-707000 in the Apple iOS/iPadOS 17 BYOAD STIG.

## Group: PP-BYO-000070

**Group ID:** `V-259747`

### Rule: The EMM detection/monitoring system must use continuous monitoring of enrolled iOS/iPadOS 17 BYOAD.

**Rule ID:** `SV-259747r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD policy requires BYOAD devices with DOD data be managed by a DOD MDM server, MAM server, or VMI system. This ensures the device can be monitored for compliance with the approved security baseline and managed data and apps can be removed when the device is out of compliance, which protects DOD data from unauthorized exposure. Detection via collection and analysis of BYOAD-generated logs for noncompliance indicators is acceptable. This detection capability must be implemented prior to AMD (Approved Mobile Device, called BYOAD device in the STIG) enrollment and AMD access to DOD information and IT resources and continuously monitored on the DOD-managed segment of the AMD enrolled in the program. If non-DOD information (i.e., personal user data, device information) outside the DOD-managed segment of the AMD is required to be accessed, collected, monitored, tracked (i.e., location), or maintained, the circumstances under which this may be done must be outlined in the user agreement. Reference: DOD policy "Use of Non-Government Mobile Devices". 3.a.(3)iii. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM detection/monitoring system is configured to use continuous monitoring of enrolled iOS/iPadOS 17 BYOAD. The exact procedure will depend on the EMM system used at the site. If the EMM detection/monitoring system is not configured to use continuous monitoring of enrolled iOS/iPadOS 17 BYOAD, this is a finding.

## Group: PP-BYO-000080

**Group ID:** `V-259748`

### Rule: The iOS/iPadOS 17 BYOAD must be configured to either disable access to DOD data, IT systems, and user accounts or wipe managed data and apps if the EMM system detects native security controls are disabled.

**Rule ID:** `SV-259748r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Examples of indicators that the native device security controls have been disabled include jailbroken or rooted devices. When a BYOAD is out of compliance, DOD data and apps must be removed to protect against compromise of sensitive DOD information. Note: The site should review DOD and local data retention policies before wiping the work profile of a BYOAD device. Reference: DOD policy "Use of Non-Government Mobile Devices". 3.b.(4), 3.b.(5)i. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM has been configured to either disable access to DOD data, IT systems, and user accounts on the iOS/iPadOS 17 BYOAD or wipe managed data and apps if it has been detected that native BYOAD security controls are disabled (e.g., jailbroken/rooted). When managed data and apps are wiped, all managed data and files in the Files app must be wiped as well. The exact procedure will depend on the EMM system used at the site. If the EMM has not been configured to either disable access to DOD data, IT systems, and user accounts on the iOS/iPadOS 17 BYOAD or wipe managed data and apps if it has been detected that native BYOAD security controls are disabled, this is a finding.

## Group: PP-BYO-000090

**Group ID:** `V-259749`

### Rule: The iOS/iPadOS 17 BYOAD must be configured to either disable access to DOD data, IT systems, and user accounts or wipe managed data and apps if the EMM system detects the BYOAD device has known malicious, blocked, or prohibited applications or is configured to access nonapproved managed third-party applications stores.

**Rule ID:** `SV-259749r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a BYOAD is out of compliance, DOD data and apps must be removed to protect against compromise of sensitive DOD information. Reference: DOD policy "Use of Non-Government Mobile Devices". 3.a.(3)iii. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM system has been configured to either disable access to DOD data, IT systems, and user accounts or wipe managed data and apps if it has detected the iOS/iPadOS 17 BYOAD device has known malicious, blocked, or prohibited managed applications or is configured to access nonapproved third-party applications stores for managed apps. When the Work profile is wiped, all managed data and files in the Files app must be wiped as well. The exact procedure will depend on the EMM system used at the site. If the EMM system has not been configured to either disable access to DOD data, IT systems, and user accounts or wipe managed data and apps if it has detected the iOS/iPadOS 17 BYOAD device has known malicious, blocked, or prohibited managed applications or is configured to access nonapproved third-party applications stores for managed apps, this is a finding.

## Group: PP-BYO-000100

**Group ID:** `V-259750`

### Rule: The iOS/iPadOS 17 BYOAD must be configured so that managed data and apps are removed if the device is no longer receiving security or software updates.

**Rule ID:** `SV-259750r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a BYOAD is out of compliance, DOD data and apps must be removed to protect against compromise of sensitive DOD information. Reference: DOD policy "Use of Non-Government Mobile Devices". 3.b.(1)ii. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM system is configured to wipe managed data and apps if the iOS/iPadOS 17 BYOAD is no longer receiving security or software updates. When managed data and apps are wiped, all managed data and files in the Files app must be wiped as well. The exact procedure will depend on the EMM system used at the site. If the EMM system is not configured to wipe managed data and apps if the iOS/iPadOS 17 BYOAD is no longer receiving security or software updates, this is a finding.

## Group: PP-BYO-000110

**Group ID:** `V-259751`

### Rule: The BYOAD and DOD enterprise must be configured to limit access to only enterprise IT resources approved by the authorizing official (AO).

**Rule ID:** `SV-259751r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Note: IT resources includes DOD networks and applications (for example, DOD email). The system administrator must have the capability to limit access of the BYOAD to DOD networks and DOD IT resources based on mission needs and risk. An adversary could exploit vulnerabilities created by the weaker configuration to compromise DOD sensitive information. The AO should document networks, IT resources, and enterprise applications that BYOAD can access. Examples of EMM security controls are as follows: 1. Device access restrictions: Restrict or isolate access based on the device's access type (i.e., from the internet), authentication type (e.g., password), credential strength, etc. 2. User and device activity monitoring: Configured to detect anomalous activity, malicious activity, and unauthorized attempts to access DOD information. 3. Device health tracking: Monitor device attestation, health, and agents reporting compromised applications, connections, intrusions, and/or signatures. Reference: DOD policy "Use of Non-Government Mobile Devices". 3.b.(2)ii. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM system and DOD enterprise have been configured to limit iOS/iPadOS 17 BYOAD access to only AO-approved enterprise IT resources. The exact procedure will depend on the EMM system used and IT resources at the site. If the EMM system and DOD enterprise have not been configured to limit iOS/iPadOS 17 BYOAD access to only AO-approved enterprise IT resources, this is a finding.

## Group: PP-BYO-000120

**Group ID:** `V-259752`

### Rule: The iOS/iPadOS 17 BYOAD must be configured to protect users' privacy, personal information, and applications.

**Rule ID:** `SV-259752r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A key construct of a BYOAD is that user personal information and data are protected from exposure to the enterprise. Reference: DOD policy "Use of Non-Government Mobile Devices". 3.b.(4), 3.b.(5). SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM system has been configured to limit access to unmanaged data and apps on the iOS/iPadOS 17 BYOAD to protect users' privacy, personal information, and applications. The exact procedure will depend on the EMM system used at the site. If the BYOAD has not been configured to limit access to unmanaged data and apps on the iOS/iPadOS 17 BYOAD, this is a finding.

## Group: PP-BYO-000130

**Group ID:** `V-259753`

### Rule: The EMM system supporting the iOS/iPadOS 17 BYOAD must be configured to only wipe managed data and apps and not unmanaged data and apps when the user's access is revoked or terminated, the user no longer has the need to access DOD data or IT, or the user reports a registered device as lost, stolen, or showing indicators of compromise.

**Rule ID:** `SV-259753r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>DOD policy requires the protection and privacy of personal data and activities to the maximum extent possible on BYOADs. Reference: DOD policy "Use of Non-Government Mobile Devices". 3.b.(5). SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM system administrators supporting the iOS/iPadOS 17 BYOAD have been trained to only wipe managed data and apps when the user's access is revoked or terminated, the user no longer has the need to access DOD data or IT, or the user reports a registered device as lost, stolen, or showing indicators of compromise. If the EMM system administrators supporting the iOS/iPadOS 17 BYOAD have not been trained to only wipe managed data and apps, this is a finding.

## Group: PP-BYO-000150

**Group ID:** `V-259754`

### Rule: The iOS/iPadOS 17 BYOAD must be deployed in Device Enrollment mode or User Enrollment mode.

**Rule ID:** `SV-259754r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD policy requires BYOAD devices with DOD data be managed by a DOD MDM server, MAM server, or VMI system. This ensures the device can be monitored for compliance with the approved security baseline and the work profile can be removed when the device is out of compliance, which protects DOD data from unauthorized exposure. Note: Technical limitations prohibit using Apple iOS/iPadOS User Enrollment in most DOD environments. Reference: DOD policy "Use of Non-Government Mobile Devices".  SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify iOS/iPadOS 17 BYOAD has been deployed in Device Enrollment mode or User Enrollment mode. This procedure is performed on the iPhone and iPad. For Device Enrollment: 1. On the device, go to Settings >> General >> VPN & Device Management. 2. Verify a Mobile Device Management profile is installed on the device. For User Enrollment: 1. On the device, go to Settings >> General >> VPN & Device Management. 2. Verify a Mobile Device Management profile is installed on the device. 3. On the device, go to "Settings" and click on the User icon. 4. Verify a work AppleID is listed. If the iOS/iPadOS 17 BYOAD has not been deployed in Device Enrollment mode or User Enrollment mode, this is a finding.

## Group: PP-BYO-000200

**Group ID:** `V-259755`

### Rule: The EMM system supporting the iOS/iPadOS 17 BYOAD must be NIAP validated (included on the NIAP list of compliant products or products in evaluation) unless the DOD CIO has granted an approved Exception to Policy (E2P).

**Rule ID:** `SV-259755r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Note: For a virtual mobile infrastructure (VMI) solution, both the client and server components must be NIAP compliant. Nonapproved EMM systems may not include sufficient controls to protect work data, applications, and networks from malware or adversary attack. EMM systems include mobile device management (MDM), mobile application management (MAM), mobile content management (MCM), or VMI. Components must only approve devices listed on the NIAP product compliant list or products listed in evaluation at the following links respectively: - https://www.niap-ccevs.org/Product/ - https://www.niap-ccevs.org/Product/PINE.cfm Reference: DOD policy "Use of Non-Government Mobile Devices". 3.a.(2). SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM system supporting the iOS/iPadOS BYOAD is NIAP validated (included on the NIAP list of compliant products or products in evaluation). If it is not, verify the DOD CIO has granted an approved E2P. Note: For a VMI solution, both the client and server components must be NIAP compliant. If the EMM system supporting the iOS/iPadOS BYOAD is not NIAP validated (included on the NIAP list of compliant products or products in evaluation) and the DOD CIO has not granted an approved E2P, this is a finding.

## Group: PP-BYO-000210

**Group ID:** `V-259756`

### Rule: The User Agreement must include a description of what personal data and information is being monitored, collected, or managed by the EMM system or deployed agents or tools.

**Rule ID:** `SV-259756r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>DOD policy states BYOAD owners must sign a user agreement and be made aware of what personal data and activities will be monitored by the enterprise by including this information in the user agreement. Reference: DOD policy "Use of Non-Government Mobile Devices" 3.a.(3)ii, and 3.c.(4). SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the user agreement includes a description of what personal data and information is being monitored, collected, or managed by the EMM system or deployed agents or tools. If the user agreement does not include a description of what personal data and information is being monitored, collected, or managed by the EMM system or deployed agents or tools, this is a finding.

## Group: PP-BYO-000220

**Group ID:** `V-259757`

### Rule: The DOD Mobile Service Provider must not allow BYOADs in facilities where personally owned mobile devices are prohibited.

**Rule ID:** `SV-259757r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD policy requires BYOAD devices with DOD data be managed by a DOD MDM server, MAM server, or VMI system. This ensures the device can be monitored for compliance with the approved security baseline and managed data and apps can be removed when the device is out of compliance, which protects DOD data from unauthorized exposure. Follow local physical security procedures regarding allowing or prohibiting personally owned mobile devices in a DOD facility. If BYOAD devices are brought into facilities where the authorizing official (AO) has determined the risk of using personal devices is unacceptable, this could lead to the exposure of sensitive DOD data. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DOD Mobile Service Provider or information system security officer (ISSO)/information system security manager (ISSM) do not allow BYOADs in facilities where personally owned mobile devices are prohibited. If the DOD Mobile Service Provider or ISSO/ISSM allows BYOADs in facilities where personally owned mobile devices are prohibited, this is a finding.

## Group: PP-BYO-000230

**Group ID:** `V-259758`

### Rule: The iOS/iPadOS 17 BYOAD must be configured to disable device cameras and/or microphones when brought into DOD facilities where mobile phone cameras and/or microphones are prohibited.

**Rule ID:** `SV-259758r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In some DOD operational environments, the use of the mobile device camera or microphone could lead to a security incident or compromise of DOD information. The system administrator must have the capability to disable the mobile device camera and/or microphone based on mission needs. Alternatively, mobile devices with cameras or microphones that cannot be disabled must be prohibited from the facility by the information system security officer (ISSO)/information system security manager (ISSM). If BYOAD devices are brought into facilities where the authorizing official (AO) has determined the risk of using mobile device cameras or microphones is unacceptable, this could lead to the exposure of sensitive DOD data. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if iOS/iPadOS 17 BYOADs are prohibited in DOD facilities that prohibit mobile devices with cameras and microphones. Refer to the site Facility Security Standard Operating Procedure (SOP) to determine site requirements. If for DOD sites that prohibit mobile devices with cameras and microphones, the ISSO/ISSM has not prohibited iOS/iPadOS 17 BYOADs from the facility, this is a finding.

## Group: PP-BYO-000200

**Group ID:** `V-259759`

### Rule: The mobile device used for BYOAD must be NIAP validated.

**Rule ID:** `SV-259759r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Note: For a virtual mobile infrastructure (VMI) solution, both the client and server components must be NIAP compliant. Nonapproved mobile devices may not include sufficient controls to protect work data, applications, and networks from malware or adversary attack. Components must only approve devices listed on the NIAP product compliant list or products listed in evaluation at the following links respectively: - https://www.niap-ccevs.org/Product/ - https://www.niap-ccevs.org/Product/PINE.cfm Reference: DOD policy "Use of Non-Government Mobile Devices". 3.b.(1)i. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the mobile device used for BYOAD is NIAP validated (included on the NIAP list of compliant products or products in evaluation). If the mobile device used for BYOAD is not NIAP validated (included on the NIAP list of compliant products or products in evaluation), this is a finding.

## Group: PP-BYO-000120

**Group ID:** `V-274440`

### Rule: All Apple iOS/iPadOS 17 BYOAD installations must be removed.

**Rule ID:** `SV-274440r1099862_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Apple iOS/iPadOS 17 BYOAD is no longer supported by Apple and therefore, may contain security vulnerabilities. SFR ID: FMT_SMF_EXT.1.1 #47 SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there are no installations of Apple iOS/iPadOS 17 BYOAD at the site. If Apple iOS/iPadOS 17 BYOAD is being used at the site, this is a finding.

