# STIG Benchmark: Samsung Android 15 BYOAD Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: PP-BYO-000020

**Group ID:** `V-272498`

### Rule: The EMM system supporting the Samsung Android 15 BYOAD must be configured for autonomous monitoring, compliance, and validation to ensure security/configuration settings of mobile devices do not deviate from the approved configuration baseline.

**Rule ID:** `SV-272498r1098267_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD policy requires BYOAD devices with DOD data be managed by a DOD MDM server, MAM server, or VMI system. This ensures the device can be monitored for compliance with the approved security baseline and the work profile can be removed when the device is out of compliance, which protects DOD data from unauthorized exposure. Examples of possible EMM security controls are as follows: 1. Device access restrictions: Restrict or isolate access based on the device access type (i.e., from the internet), authentication type (e.g., password), credential strength, etc. 2. User and device activity monitoring: Configured to detect anomalous activity, malicious activity, and unauthorized attempts to access DOD information. 3. Device health tracking: Monitor device attestation, health, and agents reporting compromised applications, connections, intrusions, and/or signatures. Reference: DOD policy "Use of Non-Government Mobile Devices" (3.a.(3)ii, 3.b.(2)ii.1 & 2). SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM system supporting the Samsung Android 15 BYOAD has been configured to conduct autonomous monitoring, compliance, and validation to ensure security/configuration settings of mobile devices do not deviate from the approved configuration baseline. The exact procedure will depend on the EMM system used at the site. If the EMM system supporting the Samsung Android 15 BYOAD has not been configured to conduct autonomous monitoring, compliance, and validation to ensure security/configuration settings of mobile devices, this is a finding.

## Group: PP-BYO-000030

**Group ID:** `V-272499`

### Rule: The EMM system supporting the Samsung Android 15 BYOAD must be configured to initiate autonomous monitoring, compliance, and validation prior to granting the Samsung Android 15 BYOAD access to DOD information and IT resources.

**Rule ID:** `SV-272499r1098270_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD policy requires BYOAD devices with DOD data be managed by a DOD MDM server, MAM server, or VMI system. This ensures the device can be monitored for compliance with the approved security baseline and the work profile can be removed when the device is out of compliance, which protects DOD data from unauthorized exposure. Reference: DOD policy "Use of Non-Government Mobile Devices" (3.a.(3)iii). SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM system supporting the Samsung Android 15 BYOAD has been configured to initiate autonomous monitoring, compliance, and validation prior to granting the BYOAD access to DOD information and IT resources. The exact procedure will depend on the EMM system used at the site. If the EMM system supporting the Samsung Android 15 BYOAD has not been configured to initiate autonomous monitoring, compliance, and validation prior to granting the BYOAD access to DOD information and IT resources, this is a finding.

## Group: PP-BYO-000040

**Group ID:** `V-272500`

### Rule: The EMM system supporting the Samsung Android 15 BYOAD must be configured to detect if the Samsung Android 15 BYOAD native security controls are disabled.

**Rule ID:** `SV-272500r1098273_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Examples of indicators that the native device security controls have been disabled include jailbroken or rooted devices. DOD policy requires BYOAD devices with DOD data be managed by a DOD MDM server, MAM server, or VMI system. This ensures the device can be monitored for compliance with the approved security baseline and the work profile can be removed when the device is out of compliance, which protects DOD data from unauthorized exposure. Detection via collecting and analysis of BYOAD generated logs for noncompliance indicators is acceptable. This detection capability must be implemented prior to BYOAD access to DOD information and IT resources and continuously monitored on the DOD-managed segment of the BYOAD enrolled in the program. If non-DOD information (i.e., personal user data, device information) outside the DOD-managed segment of the BYOAD is required to be accessed, collected, monitored, tracked (i.e., location), or maintained, the circumstances under which this may be done must be outlined in the user agreement. Reference: DOD policy "Use of Non-Government Mobile Devices" (3.a.(3)iii). SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM system supporting the Samsung Android 15 BYOAD has been configured to detect if the BYOAD native security controls are disabled. The exact procedure will depend on the EMM system used at the site. If the EMM system supporting the Samsung Android 15 BYOAD is not configured to detect if the BYOAD native security controls are disabled, this is a finding.

## Group: PP-BYO-000050

**Group ID:** `V-272501`

### Rule: The EMM system supporting the Samsung Android 15 BYOAD must be configured to detect if known malicious applications, blocked, or prohibited applications are installed on the Samsung Android 15 BYOAD (DOD-managed segment only).

**Rule ID:** `SV-272501r1098276_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD policy requires BYOAD devices with DOD data be managed by a DOD MDM server, MAM server, or VMI system. This ensures the device can be monitored for compliance with the approved security baseline and the work profile can be removed when the device is out of compliance, which protects DOD data from unauthorized exposure. Detection via collecting and analysis of BYOAD generated logs for noncompliance indicators is acceptable. This detection capability must be implemented prior to Approved Mobile Device (AMD) (called BYOAD device in the STIG) enrollment, AMD access to DOD information and IT resources, and continuously monitored on the DOD-managed segment of the AMD enrolled in the program. If non-DOD information (i.e., personal user data, device information) outside the DOD-managed segment of the AMD is required to be accessed, collected, monitored, tracked (i.e., location), or maintained, the circumstances under which this may be done must be outlined in the user agreement. Reference: DOD policy "Use of Non-Government Mobile Devices" (3.a.(3)iii). SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an app vetting process is being used to vet apps before work profile apps are placed in the MDM app repository. If an app vetting process is not being used to vet apps before work profile apps are placed in the MDM app repository, this is a finding.

## Group: PP-BYO-000070

**Group ID:** `V-272503`

### Rule: The EMM detection/monitoring system must use continuous monitoring of enrolled Samsung Android 15 BYOAD.

**Rule ID:** `SV-272503r1098282_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD policy requires BYOAD devices with DOD data be managed by a DOD MDM server, MAM server, or VMI system. This ensures the device can be monitored for compliance with the approved security baseline and the work profile can be removed when the device is out of compliance, which protects DOD data from unauthorized exposure. Continuous monitoring must be used to ensure all noncompliance events will be seen by the detection system. Reference: DOD policy "Use of Non-Government Mobile Devices" (3.a.(3)iii). SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM detection/monitoring system is configured to use continuous monitoring of enrolled Samsung Android 15 BYOAD. The exact procedure will depend on the EMM system used at the site. If the EMM detection/monitoring system is not configured to use continuous monitoring of enrolled Samsung Android 15 BYOAD, this is a finding.

## Group: PP-BYO-000080

**Group ID:** `V-272504`

### Rule: The Samsung Android 15 BYOAD must be configured to either disable access to DOD data and IT systems and user accounts or wipe the work profile if the EMM system detects native security controls are disabled.

**Rule ID:** `SV-272504r1098285_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Examples of indicators that the native device security controls have been disabled include jailbroken or rooted devices. When a BYOAD is out of compliance, DOD data and apps must be removed to protect against compromise of sensitive DOD information. Note: The site should review DOD and local data retention policies before wiping the work profile of a BYOAD device. Reference: DOD policy "Use of Non-Government Mobile Devices" (3.b.(4) 3.b.(5)i). SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM has been configured to either disable access to DOD data, IT systems, and user accounts on the Samsung Android 15 BYOAD or wipe the work profile if it has been detected that native BYOAD security controls are disabled (e.g., jailbroken/rooted). The exact procedure will depend on the EMM system used at the site. If the EMM has not been configured to either disable access to DOD data, IT systems, and user accounts on the Samsung Android 15 BYOAD or wipe the work profile if it has been detected that native BYOAD security controls are disabled, this is a finding.

## Group: PP-BYO-000090

**Group ID:** `V-272505`

### Rule: The Samsung Android 15 BYOAD must be configured to either disable access to DOD data and IT systems and user accounts or wipe the work profile if the EMM system detects the Samsung Android 15 BYOAD device has known malicious, blocked, or prohibited applications, or configured to access nonapproved third-party applications stores in the work profile.

**Rule ID:** `SV-272505r1098288_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a BYOAD is out of compliance, DOD data and apps must be removed to protect against compromise of sensitive DOD information. Reference: DOD policy "Use of Non-Government Mobile Devices" (3.a.(3)iii). SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM system has been configured to either disable access to DOD data and IT systems and user accounts or the work profile if it has detected the Samsung Android 15 BYOAD device has known malicious, blocked, or prohibited managed applications, or configured to access nonapproved third-party applications stores for managed apps. The exact procedure will depend on the EMM system used at the site. If the EMM system has not been configured to either disable access to DOD data and IT systems and user accounts or wipe the work profile if it has detected the Samsung Android 15 BYOAD device has known malicious, blocked, or prohibited managed applications, or configured to access nonapproved third-party applications stores for managed apps, this is a finding.

## Group: PP-BYO-000100

**Group ID:** `V-272506`

### Rule: The Samsung Android 15 BYOAD must be configured so that the work profile is removed if the device is no longer receiving security or software updates.

**Rule ID:** `SV-272506r1098291_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a BYOAD is out of compliance, DOD data and apps must be removed to protect against compromise of sensitive DOD information. Reference: DOD policy "Use of Non-Government Mobile Devices" (3.b.(1)ii). SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM system is configured to wipe the work profile if the Samsung Android 15 BYOAD is no longer receiving security or software updates. The exact procedure will depend on the EMM system used at the site. If the EMM system is not configured to wipe the work profile if the Samsung Android 15 BYOAD is no longer receiving security or software updates, this is a finding.

## Group: PP-BYO-000110

**Group ID:** `V-272507`

### Rule: The Samsung Android 15 BYOAD and DOD enterprise must be configured to limit access to only AO-approved, corporate-owned enterprise IT resources.

**Rule ID:** `SV-272507r1098766_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Note: IT resources includes DOD networks and applications (for example, DOD email). The system administrator must have the capability to limit access of the BYOAD to DOD networks and DOD IT resources based on mission needs and risk. An adversary could exploit vulnerabilities created by the weaker configuration to compromise DOD sensitive information. The AO should document networks, IT resources, and enterprise applications that BYOAD can access. Examples of EMM security controls are as follows: 1. Device access restrictions: Restrict or isolate access based on the device access type (i.e., from the internet), authentication type (e.g., password), credential strength, etc. 2. User and device activity monitoring: Configured to detect anomalous activity, malicious activity, and unauthorized attempts to access DOD information. 3. Device health tracking: Monitor device attestation, health, and agents reporting compromised applications, connections, intrusions, and/or signatures. Reference: DOD policy "Use of Non-Government Mobile Devices" (3.b.(2)ii). SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM system and DOD enterprise have been configured to limit the Samsung Android 15 BYOAD access to only AO-approved enterprise IT resources. The exact procedure will depend on the EMM system used and IT resources at the site. If the EMM system and DOD enterprise have not been configured to limit Samsung Android 15 BYOAD access to only AO-approved enterprise IT resources, this is a finding.

## Group: PP-BYO-000200

**Group ID:** `V-272516`

### Rule: The EMM system supporting the Samsung Android 15 BYOAD must be NIAP validated (included on the NIAP list of compliant products or products in evaluation) unless the DOD CIO has granted an Approved Exception to Policy (E2P).

**Rule ID:** `SV-272516r1098321_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Note: For a VMI solution, both the client and server must be NIAP compliant. Nonapproved EMM systems may not include sufficient controls to protect work data, applications, and networks from malware or adversary attack. EMM: mobile device management (MDM), mobile application management (MAM), mobile content management (MCM), or virtual mobile infrastructure (VMI). Components must only approve devices listed on the NIAP list of compliant products or products listed in evaluation at the following links respectfully: - https://www.niap-ccevs.org/Product/ - https://www.niap-ccevs.org/Product/PINE.cfm Reference: DOD policy "Use of Non-Government Mobile Devices" (3.a.(2)). SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM system supporting the Samsung Android 15 BYOAD is NIAP-validated (included on the NIAP list of compliant products or products in evaluation). If not, verify the DOD CIO has granted an Approved Exception to Policy (E2P). Note: For a VMI solution, both the client and server components must be NIAP compliant. If the EMM system supporting the Samsung Android 15 BYOAD is not NIAP-validated (included on the NIAP list of compliant products or products in evaluation) and the DOD CIO has not granted an Approved Exception to Policy (E2P), this is a finding.

## Group: PP-BYO-000210

**Group ID:** `V-272517`

### Rule: The user agreement must include a description of what personal data and information is being monitored, collected, or managed by the EMM system or deployed agents or tools.

**Rule ID:** `SV-272517r1098324_rule`
**Severity:** low

**Description:**
<VulnDiscussion>DOD policy states BYOAD owners must sign a user agreement and be made aware of what personal data and activities will be monitored by the Enterprise by including this information in the user agreement. Reference: DOD policy "Use of Non-Government Mobile Devices" (3.a.(3)ii, and 3.c.(4)). SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the user agreement includes a description of what personal data and information is being monitored, collected, or managed by the EMM system or deployed agents or tools. If the user agreement does not include a description of what personal data and information is being monitored, collected, or managed by the EMM system or deployed agents or tools, this is a finding.

## Group: PP-BYO-000220

**Group ID:** `V-272518`

### Rule: The DOD Mobile Service Provider must not allow Samsung Android 15 BYOADs in facilities where personally owned mobile devices are prohibited.

**Rule ID:** `SV-272518r1098327_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD policy requires BYOAD devices with DOD data be managed by a DOD MDM server, MAM server, or VMI system. This ensures the device can be monitored for compliance with the approved security baseline and the work profile can be removed when the device is out of compliance, which protects DOD data from unauthorized exposure. Follow local physical security procedures regarding allowing or prohibiting personally owned mobile devices in a DOD facility. If BYOAD devices are brought into facilities where the AO has determined the risk of using personal devices is unacceptable, this could lead to the exposure of sensitive DOD data. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DOD Mobile Service Provider or information system security officer (ISSO)/information system security manager (ISSM) do not allow BYOADs in facilities where personally owned mobile devices are prohibited. If the DOD Mobile Service Provider or ISSO/ISSM allows BYOADs in facilities where personally owned mobile devices are prohibited, this is a finding.

## Group: PP-BYO-000230

**Group ID:** `V-272519`

### Rule: The Samsung Android 15 BYOAD must be configured to disable device cameras and/or microphones when brought into DOD facilities where mobile phone cameras and/or microphones are prohibited.

**Rule ID:** `SV-272519r1098330_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In some DOD operational environments, the use of the mobile device camera or microphone could lead to a security incident or compromise of DOD information. The system administrator must have the capability to disable the mobile device camera and/or microphone based on mission needs. Alternatively, mobile devices with cameras or microphones that cannot be disabled must be prohibited from the facility by the information system security officer (ISSO)/information system security manager (ISSM). If BYOAD devices are brought into facilities where the AO has determined the risk of using mobile device cameras or microphones is unacceptable, this could lead to the exposure of sensitive DOD data. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Samsung Android 15 BYOADs are prohibited in DOD facilities that prohibit mobile devices with cameras and microphones. If for DOD sites that prohibit mobile devices with cameras and microphones, Samsung Android 15 BYOADs have not been prohibited from the facility by the ISSO/ISSM, this is a finding.

## Group: PP-BYO-000200

**Group ID:** `V-272524`

### Rule: The mobile device used for BYOAD must be NIAP validated.

**Rule ID:** `SV-272524r1098767_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Nonapproved mobile devices may not include sufficient controls to protect work data, applications, and networks from malware or adversary attack. Components must only approve devices listed on the NIAP list of compliant products or products listed in evaluation at the following links respectively: - https://www.niap-ccevs.org/Product/ - https://www.niap-ccevs.org/Product/PINE.cfm Reference: DOD policy "Use of Non-Government Mobile Devices" (3.b.(1)i). SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the mobile device used for BYOAD is NIAP-validated (included on the NIAP list of compliant products or products in evaluation). If the mobile device used for BYOAD is not NIAP-validated (included on the NIAP list of compliant products or products in evaluation), this is a finding.

