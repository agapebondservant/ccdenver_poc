# STIG Benchmark: BlackBerry CylancePROTECT Mobile for UEM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-257260`

### Rule: CylancePROTECT Mobile malware detection must be configured with the following compliance actions for system apps (Android only):
-Prompt for compliance: Immediate enforcement action.
-Prevent the user from accessing work resources and apps on the device while it is out of compliance.
-Prevent the user from accessing BlackBerry Dynamics apps while the device is out of compliance.

**Rule ID:** `SV-257260r918364_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a compliance failure is detected, compliance actions must be implemented immediately to limit exposure of sensitive data and unauthorized access to the mobile device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following compliance actions are enabled when malware is detected for system apps (Android only): -Prompt for compliance: Immediate enforcement action. -Prevent the user from accessing work resources and apps on the device while it is out of compliance. -Prevent the user from accessing BlackBerry Dynamics apps while the device is out of compliance. 1. Log on to the BlackBerry UEM console. 2. Select Policies and profiles >> Compliance >> Compliance. 3. Select a compliance profile to review. 4. On the Android tab in the BlackBerry Protect section, verify: a. The "System app malware detected" box is selected. b. In the Prompt for compliance box, verify "Immediate enforcement action" is selected. c. In the "Enforcement action for device" drop-down list, verify "Untrust" is selected. d. In the "Enforcement action for BlackBerry Dynamics apps" drop-down list, verify "Do not allow BlackBerry Dynamics apps to run" is selected. If required compliance actions when malware is detected for system apps are not configured, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-257261`

### Rule: CylancePROTECT Mobile malware detection must be configured with the following compliance actions for nonsystem apps (Android only):
-Prompt for compliance: Immediate enforcement action.
-Prevent the user from accessing work resources and apps on the device while it is out of compliance.
-Prevent the user from accessing BlackBerry Dynamics apps while the device is out of compliance.

**Rule ID:** `SV-257261r918367_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a compliance failure is detected, compliance actions must be implemented immediately to limit exposure of sensitive data and unauthorized access to the mobile device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following compliance actions are enabled when malware is detected for nonsystem apps (Android only): -Prompt for compliance: Immediate enforcement action. -Prevent the user from accessing work resources and apps on the device while it is out of compliance. -Prevent the user from accessing BlackBerry Dynamics apps while the device is out of compliance. 1. Log on to the BlackBerry UEM console. 2. Select Policies and profiles >> Compliance >> Compliance. 3. Select a compliance profile to review. 4. On the Android tab in the BlackBerry Protect section, verify: a. The "Malicious app package detected" box is selected. b. In the Prompt for compliance box, verify "Immediate enforcement action" is selected. c. In the "Enforcement action for device" drop-down list, verify "Untrust" is selected. d. In the "Enforcement action for BlackBerry Dynamics apps" drop-down list, verify "Do not allow BlackBerry Dynamics apps to run" is selected. If required compliance actions when malware is detected for nonsystem apps are not configured, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-257262`

### Rule: CylancePROTECT Mobile must be configured with the following compliance action when a compliance event occurs:
-Notify Administrator (send event notification).

**Rule ID:** `SV-257262r918370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a compliance failure is detected, compliance actions must be implemented immediately to limit exposure of sensitive data and unauthorized access to the mobile device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following compliance action for CylancePROTECT Mobile has been enabled: -Notify Administrator (send event notification). 1. Log on to the BlackBerry UEM console. 2. On the menu bar, click Settings >> General settings. 3. Click "Event notifications". 4. Verify each of the following BlackBerry Protect notifications are listed: "Safe Browsing", "Malicious app removed from UEM", "Malicious app detected on device", and "Sideloaded app detected on app". If all four of the BlackBerry Protect notifications listed above are not enabled, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-257263`

### Rule: CylancePROTECT Mobile must be configured with the following compliance actions when sideloaded apps are detected:
-Prompt for compliance: Immediate enforcement action.
-Prevent the user from accessing work resources and apps on the device while it is out of compliance.
-Prevent the user from accessing BlackBerry Dynamics apps while the device is out of compliance.

**Rule ID:** `SV-257263r918373_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a compliance failure is detected, compliance actions must be implemented immediately to limit exposure of sensitive data and unauthorized access to the mobile device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following compliance actions have been enabled when sideloaded apps are detected: -Prompt for compliance: Immediate enforcement action. -Prevent the user from accessing work resources and apps on the device while it is out of compliance. -Prevent the user from accessing BlackBerry Dynamics apps while the device is out of compliance. 1. Log on to the BlackBerry UEM console. 2. In the management console on the menu bar, click Policies and profiles >> Compliance >> Compliance. 3. Find the CylancePROTECT Mobile sideloaded app compliance profile (have the site system administrator identify the correct profile). 4. Select the iOS tab and verify the following selections: 5. In the "Prompt for compliance" drop-down list verify "Immediate enforcement action" is selected. 6. In the "Enforcement action for device" drop-down list, verify "Untrust" is selected. 7. In the "Enforcement action for BlackBerry Dynamics apps" drop-down list, verify "Do not allow BlackBerry Dynamics apps to run" is selected. 8. Repeat steps 4–6 for Android. If required compliance actions for when sideloaded apps are detected for iOS and Android are not configured, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-257264`

### Rule: CylancePROTECT Mobile must be configured with the following safe browsing controls for BlackBerry Dynamics apps:
-Block all unsafe URLs
-Select one of the following for "scanning option": "Cloud scanning" or "On device scanning".
-Disable "Allow users to override blocked resources and enable access to the requested domain".

**Rule ID:** `SV-257264r918376_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The required application configurations will ensure that the minimum security baseline of the system is maintained to limit exposure of sensitive data and unauthorized access to the mobile device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify safe browsing with BlackBerry Dynamics apps has been configured as required: 1. Log on to the BlackBerry UEM console. 2. In the management console on the menu bar, click Policies and profiles >> Protection >> BlackBerry Protect. 3. Open the BlackBerry Protect profile (have the site system administrator identify the profile from the list). 4. Select the platform (iOS or Android) to review. 5. Verify that the "Check for unsafe web resources within the BlackBerry Dynamics apps" check box is selected. 6. Verify "Block" is selected in the Action for unsafe web resources drop-down list. 7. Verify in the Scanning option drop-down list, one of the following has been selected AND "No scanning" is not selected: -"Cloud scanning". -"On device scanning". 8. Verify "Allow users to override blocked resources and enable access to the requested domain" is not selected. 9. Repeat steps 4–8 for the other platform (iOS or Android). If safe browsing for BlackBerry Dynamics apps on iOS and Android devices is not configured as required, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-257265`

### Rule: CylancePROTECT Mobile must be configured with the following compliance actions when insecure networks are detected for mobile devices:
-Block device from network connection and insecure Wi-Fi access points.
-Block access to BlackBerry Dynamics apps.

**Rule ID:** `SV-257265r918379_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a compliance failure is detected, compliance actions must be implemented immediately to limit exposure of sensitive data and unauthorized access to the mobile device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following compliance actions are enabled when insecure networks are detected: -Block device from network connection and insecure Wi-Fi access points. -Block access to BlackBerry Dynamics apps. 1. Log on to the BlackBerry UEM console. 2. In the management console on the menu bar, click Policies and profiles >> Compliance >> Compliance. 3. Open the appropriate compliance profile (have the site system administrator identify the profile). 4. Verify required compliance actions for insecure network detection are enabled. a. On both the iOS and Android tabs, in the BlackBerry Protect section, verify "Insecure network detected" is selected. b. In the "Prompt for compliance" drop-down list, verify "Immediate enforcement action" is selected. c. In the "Enforcement action for device" drop-down list, verify "Untrust" is selected (Android only). d. In the "Enforcement action for BlackBerry Dynamics apps" drop-down list, verify "Do not allow BlackBerry Dynamics apps to run" is selected. 5. Verify compliance actions for insecure Wi-Fi access point detection are enabled (Android only). a. On the Android tab in the BlackBerry Protect section, verify "Insecure Wi-Fi network detected" is selected. b. In the "Prompt for compliance" drop-down list, verify "Immediate enforcement action" is selected. c. In the "Enforcement action for device" drop-down list, verify "Untrust" is selected. d. In the "Enforcement action for BlackBerry Dynamics apps" drop-down list, verify "Do not allow BlackBerry Dynamics apps to run" is selected. If any required compliance actions for insecure network detection for mobile devices has not been implemented, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-257266`

### Rule: CylancePROTECT Mobile must be configured with the following compliance actions for integrity violations with BlackBerry Dynamics apps on iOS devices:
-Prompt for compliance: Immediate enforcement action
-Prevent the user from accessing BlackBerry Dynamics apps while the device is out of compliance.

**Rule ID:** `SV-257266r918382_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a compliance failure is detected, compliance actions must be implemented immediately to limit exposure of sensitive data and unauthorized access to the mobile device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following compliance actions for BlackBerry Dynamics apps are configured when there is an iOS device integrity violation: -Prompt for compliance: Immediate enforcement action. -Prevent the user from accessing BlackBerry Dynamics apps while the device is out of compliance. 1. Log on to the BlackBerry UEM console. 2. In the management console on the menu bar, click Policies and profiles >> Compliance >> Compliance. 3. View the appropriate compliance profile (have the site system administrator identify the profile). 4. On the iOS tab in the BlackBerry Protect section, verify the "App integrity failed" check box is selected. 5. In the "Prompt for compliance" drop-down list verify "Immediate enforcement action" is selected 6. In the "Enforcement action for BlackBerry Dynamics apps" drop-down list, verify "Do not allow BlackBerry Dynamics apps to run" is selected. If required compliance actions for integrity violations for BlackBerry Dynamics apps on iOS devices are not enabled, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-257267`

### Rule: CylancePROTECT Mobile must be configured with the following Android security patch compliance and hardware certificate attestation controls:
-"Android hardware attestation frequency" = 6 hours
-"Device grace period" = 0 hours
-"Challenge frequency for noncompliant devices" =  6 hours.

**Rule ID:** `SV-257267r940014_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The required application configurations will ensure that the minimum security baseline of the system is maintained to limit exposure of sensitive data and unauthorized access to the mobile device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following Android security patch compliance and hardware certificate attestation controls are enabled for CylancePROTECT Mobile: -"Android hardware attestation frequency" = 6 hours. -"Device grace period" = 3 days (72 hours). -"Challenge frequency for noncompliant devices = 1 day (24 hours). 1. Log on to the BlackBerry UEM console. 2. In the management console, click Settings >> General Settings >> Attestation. 3. In the "Android hardware attestation frequency" section, select verify "Enable hardware patch level attestation challenges for Android devices" is selected. 4. In the "Challenge frequency" drop-down list, verify the device attestation response is set to "1 day" (24 hours). 5. In the "Device grace period drop-down" list, verify the grace period is set to "3 days" (72 hours). 6. In the "Challenge frequency for noncompliant devices" field, verify the frequency UEM tests the integrity of devices that are not currently in compliance is set to "6 hours". If required Android security patch compliance and hardware certificate attestation controls are not enabled, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-257268`

### Rule: CylancePROTECT Mobile must be configured with the following compliance actions when an Android device fails security patch compliance and attestation:
-Prompt behavior: Immediate enforcement action.
-Enforcement action for device: Select either "Untrust", "Delete only work data" or "Delete all data".
-Enforcement action for BlackBerry Dynamics apps: Select either "Do not allow BlackBerry Dynamics apps to run" or "Delete BlackBerry Dynamics apps data".

**Rule ID:** `SV-257268r918388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a compliance failure is detected, compliance actions must be implemented immediately to limit exposure of sensitive data and unauthorized access to the mobile device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following compliance actions when an Android device fails security patch compliance and attestation have been configured: -Prompt behavior: Immediate enforcement action. -Enforcement action for device: Select either "Untrust", "Delete only work data", or "Delete all data". -Enforcement action for BlackBerry Dynamics apps: Select either "Do not allow BlackBerry Dynamics apps to run" or "Delete BlackBerry Dynamics apps data". 1. Log on to the BlackBerry UEM console. 2. In the management console on the menu bar, click Policies and profiles >> Compliance >> Compliance. 3. Select the appropriate compliance profile (have the site system administrator identify the profile). 4. On the Android tab, verify "Required security patch level is not installed" check box has been selected. 5. Verify for "Prompt behavior" "Immediate enforcement action" has been selected. 6. Verify for "Enforcement action for device" either "Untrust", "Delete work data only", or "Delete all data" has been selected. 7. Verify for "Enforcement action for BlackBerry Dynamics apps" either "Do not allow BlackBerry Dynamics apps to run" or "Delete BlackBerry Dynamics apps data" has been selected. If required compliance actions when an Android device fails security patch compliance and attestation have not been configured, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-257269`

### Rule: CylancePROTECT Mobile must be configured with the following compliance actions when a hardware attestation failure occurs (Android only):
-Prompt for compliance: Immediate enforcement action.
-Enforcement action for BlackBerry Dynamics apps: Do not allow BlackBerry Dynamics apps to run.

**Rule ID:** `SV-257269r918391_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a compliance failure is detected, compliance actions must be implemented immediately to limit exposure of sensitive data and unauthorized access to the mobile device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following compliance actions when a hardware attestation failure occurs have been configured (Android only): -Prompt for compliance: Immediate enforcement action. -Enforcement action for BlackBerry Dynamics apps: Do not allow BlackBerry Dynamics apps to run. 1. Log on to the BlackBerry UEM console. 2. In the management console on the menu bar, click Policies and profiles >> Compliance >> Compliance. 3. Select the appropriate compliance profile (have the site system administrator identify the profile). 4. On the Android tab in the BlackBerry Protect section, verify the "Hardware attestation failed" box is checked. 5. In the "Prompt for compliance" drop-down list, verify "Immediate enforcement action" is selected. 6. In the "Enforcement action for BlackBerry Dynamics apps" drop-down list, verify "Do not allow BlackBerry Dynamics apps to run" is selected. If required compliance actions when a hardware attestation failure occurs have not been configured, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-257270`

### Rule: CylancePROTECT Mobile must be configured with the following compliance actions when a hardware attestation certificate failure occurs (Android only):
-Minimum security level required: "Trusted Environment" or "StrongBox"
-Prompt behavior: "Immediate enforcement action".
-Enforcement action for BlackBerry Dynamics apps: "Do not allow BlackBerry Dynamics apps to run".

**Rule ID:** `SV-257270r918394_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a compliance failure is detected, compliance actions must be implemented immediately to limit exposure of sensitive data and unauthorized access to the mobile device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following compliance actions are enabled when a hardware attestation certificate failure occurs (Android only): -Minimum security level required: "Trusted Environment" or "StrongBox". -Prompt behavior: "Immediate enforcement action". -Enforcement action for BlackBerry Dynamics apps: "Do not allow BlackBerry Dynamics apps to run". 1. Log on to the BlackBerry UEM console. 2. In the management console on the menu bar, click Policies and profiles >> Compliance >> Compliance. 3. Select the appropriate compliance profile (have the site system admin identify the profile). 4. On the Android tab in the BlackBerry Protect section, verify "Hardware attestation security level" has been selected. 5. In the "Minimum security level required" drop-down list, verify either "Trusted Environment" or "StrongBox" is selected. 6. In the "Prompt behavior" drop-down list, verify "Immediate enforcement action" is selected. 7. In the "Enforcement action for BlackBerry Dynamics apps" drop-down list, verify "Do not allow BlackBerry Dynamics apps to run" is selected. If required compliance actions are not enabled when a hardware attestation certificate failure occurs, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-257271`

### Rule: CylancePROTECT Mobile must be configured with the following compliance actions when a hardware attestation boot state failure occurs (Android only):
-Prompt behavior: "Immediate enforcement action".
-Enforcement action for BlackBerry Dynamics apps: "Do not allow BlackBerry Dynamics apps to run".

**Rule ID:** `SV-257271r918397_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a compliance failure is detected, compliance actions must be implemented immediately to limit exposure of sensitive data and unauthorized access to the mobile device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the following compliance actions when a hardware attestation boot state failure occurs are configured (Android only): -Prompt behavior: "Immediate enforcement action". -Enforcement action for BlackBerry Dynamics apps: "Do not allow BlackBerry Dynamics apps to run". 1. Log on to the BlackBerry UEM console. 2. In the management console on the menu bar, click Policies and profiles >> Compliance >> Compliance. 3. Select the appropriate compliance profile (have the site system administrator identify the profile). 4. On the Android tab in the BlackBerry Protect section, verify the "Hardware attestation boot state is unverified" is selected. 5. In the "Prompt behavior" drop-down list, verify "Immediate enforcement action" is selected. 6. In the "Enforcement action for BlackBerry Dynamics apps" drop-down list, verify "Do not allow BlackBerry Dynamics apps to run" is selected. If required compliance actions when a hardware attestation boot state failure occurs are not configured, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-257272`

### Rule: CylancePROTECT Mobile must be configured to disable anonymous data collection by BlackBerry for both iOS and Android devices.

**Rule ID:** `SV-257272r918400_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The required application configurations will ensure that the minimum security baseline of the system is maintained to limit exposure of sensitive data and unauthorized access to the mobile device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify anonymous data collection by BlackBerry for both iOS and Android devices has been disabled by CylancePROTECT Mobile: 1. Log on to the BlackBerry UEM console. 2. In Policies and profiles >> Protection >> BlackBerry Protect, select a BlackBerry Protect profile. 3. On the iOS tab, in the "Statistics collection" section, verify "Allow collection of anonymized statistics from devices to improve the performance of BlackBerry Protect" check box has not been selected. 4. On the Android tab, in the "Statistics collection" section, verify the "Allow collection of anonymized statistics from devices to improve the performance of BlackBerry Protect" check box has not been selected. If CylancePROTECT Mobile has not disabled anonymous data collection by BlackBerry for both iOS and Android devices, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-257273`

### Rule: CylancePROTECT Mobile must be configured to enable SMS text message scanning (iOS only).

**Rule ID:** `SV-257273r918403_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The required application configurations will ensure that the minimum security baseline of the system is maintained to limit exposure of sensitive data and unauthorized access to the mobile device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SMS text message scanning has been configured as required (iOS only): 1. Log on to the BlackBerry UEM console. 2. In the management console on the menu bar, click Policies and profiles >> Protection >> BlackBerry Protect. 3. Open the BlackBerry Protect profile (have the site system administrator identify the profile from the list). 4. Select the iOS platform. 5. Verify that the "Enable message scanning" check box is selected. 6. Verify in the Scanning option drop-down list, one of the following has been selected AND "No scanning" is not selected: -"Cloud scanning". -"On device scanning". If SMS text message scanning for iOS devices is not configured as required, this is a finding.

