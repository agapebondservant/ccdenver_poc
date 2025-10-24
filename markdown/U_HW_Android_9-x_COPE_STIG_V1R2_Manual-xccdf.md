# STIG Benchmark: Honeywell Android 9.x COPE Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: PP-MDF-301020

**Group ID:** `V-235063`

### Rule: The Honeywell Mobility Edge Android Pie device must be configured to not allow passwords that include more than two repeating or sequential characters.

**Rule ID:** `SV-235063r626531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password strength is a measure of the effectiveness of a password in resisting guessing and brute force attacks. Passwords that contain repeating or sequential characters are significantly easier to guess than those that do not contain repeating or sequential characters. Therefore, disallowing repeating or sequential characters increases password strength and decreases risk. SFR ID: FMT_SMF_EXT.1.1 #1b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Honeywell Android device configuration settings to determine if the mobile device is prohibiting passwords with more than two repeating or sequential characters. This validation procedure is performed on both the MDM Administration console and the Android Pie device. On the MDM console: 1. Open password requirements. 2. Open device password section. 3. Ensure the password quality is set to "Numeric (Complex)". On the Honeywell Android Pie device: 1. Open Settings >> Security & location >> Screen lock. 2. Enter current password. 3. Tap on "Password". 4. Verify Password complexity requirements are listed: Must contain at least 1 letter. If the MDM console device policy is set to a password with more than two repeating or sequential characters or on the Honeywell Android Pie device, the device policy is set to a password with more than two repeating or sequential characters, this is a finding. NOTE: Alphabetic, Alphanumeric, and Complex are also acceptable selections, but these selections will cause the user to select a complex password, which is not required by the STIG.

## Group: PP-MDF-301030

**Group ID:** `V-235064`

### Rule: The Honeywell Mobility Edge Android Pie device must be configured to enable a screen-lock policy that will lock the display after a period of inactivity.

**Rule ID:** `SV-235064r626531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The screen-lock timeout helps protect the device from unauthorized access. Devices without a screen-lock timeout provide an opportunity for adversaries who gain physical access to the mobile device through loss, theft, etc. Such devices are much more likely to be in an unlocked state when acquired by an adversary, thus granting immediate access to the data on the mobile device, and possibly access to DoD networks. SFR ID: FMT_SMF_EXT.1.1 #2a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Honeywell Android device configuration settings to determine if the mobile device is enforcing a screen-lock policy that will lock the display after a period of inactivity. This validation procedure is performed on both the MDM Administration console and the Android Pie device. On the MDM console: 1. Open password requirements. 2. Open device password section. 3. Ensure "Device Lock Timeout" is set to any number desired. Units are in minutes. On the Honeywell Android Pie device: 1. Open settings >> Security & location. 2. Click the "gear" icon next to "Screen lock". 3. Ensure "Automatically lock" is set at a required time. If the MDM console device policy is not set to enable a screen-lock policy that will lock the display after a period of inactivity or on the Honeywell Android Pie device, the device policy is not set to enable a screen-lock policy that will lock the display after a period of inactivity, this is a finding.

## Group: PP-MDF-301040

**Group ID:** `V-235065`

### Rule: The Honeywell Mobility Edge Android Pie device must be configured to lock the display after 15 minutes (or less) of inactivity.

**Rule ID:** `SV-235065r626531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The screen lock timeout must be set to a value that helps protect the device from unauthorized access. Having a too-long timeout would increase the window of opportunity for adversaries who gain physical access to the mobile device through loss, theft, etc. Such devices are much more likely to be in an unlocked state when acquired by an adversary, thus granting immediate access to the data on the mobile device. The maximum timeout period of 15 minutes has been selected to balance functionality and security; shorter timeout periods may be appropriate depending on the risks posed to the mobile device. SFR ID: FMT_SMF_EXT.1.1 #2b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Honeywell Android device configuration settings to determine if the mobile device has the screen lock timeout set to 15 minutes or less. This validation procedure is performed on both the MDM Administration console and the Android Pie device. On the MDM console: 1. Open passcode requirements. 2. Open device passcode section. 3. Ensure "Device Lock Timeout" to any number between 1 and 15. On the Honeywell Android Pie device: 1. Open settings >> Security & location. 2. Click the "gear" icon next to "Screen lock". 3. Ensure "Automatically lock" is set to between 0 and 15 minutes. If the MDM console device policy is not set to 15 minutes or less for the screen lock timeout or on the Honeywell Android Pie device, the device policy is not set to 15 minutes or less for the screen lock timeout, this is a finding.

## Group: PP-MDF-301050

**Group ID:** `V-235066`

### Rule: The Honeywell Mobility Edge Android Pie device must be configured to not allow more than 10 consecutive failed authentication attempts.

**Rule ID:** `SV-235066r626531_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The more attempts an adversary has to guess a password, the more likely the adversary will enter the correct password and gain access to resources on the device. Setting a limit on the number of attempts mitigates this risk. Setting the limit at 10 or less gives authorized users the ability to make a few mistakes when entering the password but still provides adequate protection against dictionary or brute force attacks on the password. SFR ID: FMT_SMF_EXT.1.1 #2c, FIA_AFL_EXT.1.5</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Honeywell Android device configuration settings to determine if the mobile device has the maximum number of consecutive failed authentication attempts set at 10 or fewer. This validation procedure is performed on both the MDM Administration console and the Android Pie device. On the MDM console: 1. Open password requirements. 2. Open device password section. 3. Review the policy configuration that was pushed down to the device and ensure the "Maximum Number of Failed Attempts" is set between 1 and 10. On the Honeywell Android Pie device: 1. Open Setting >> Security & location >> Advanced >> Managed device info. 2. Verify "Failed password attempts before deleting all device data" is set to 10 or fewer attempts. If the MDM console device policy is not set to the maximum number of consecutive failed authentication attempts at 10 or fewer or on the Honeywell Android Pie device, the device policy is not set to the maximum number of consecutive failed authentication attempts at 10 or fewer, this is a finding.

## Group: PP-MDF-301080

**Group ID:** `V-235067`

### Rule: The Honeywell Mobility Edge Android Pie device must be configured to enforce an application installation policy by specifying one or more authorized application repositories, including [selection: DoD-approved commercial app repository, MDM server, mobile application store].

**Rule ID:** `SV-235067r852707_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Forcing all applications to be installed from authorized application repositories can prevent unauthorized and malicious applications from being installed and executed on mobile devices. Allowing such installations and executions could cause a compromise of DoD data accessible by these unauthorized/malicious applications. SFR ID: FMT_SMF_EXT.1.1 #8a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Honeywell Android device configuration settings to determine if the mobile device has only approved application repositories (DoD-approved commercial app repository, MDM server, and/or mobile application store). This validation procedure is performed on both the MDM Administration console and the Android Pie device. On the MDM console: 1. Open Restrictions section. 2. Set Allow "Honeywell Play" (Uses only Managed Honeywell Play). 3. Ensure that Disallow is set for "Install unknown sources". On the Honeywell Android Pie device: 1. Open Settings >> Apps and notifications >> Advanced >> Special app access. 2. Open Install unknown apps. 3. Ensure the list of apps is blank or if an app is on the list, "Disabled by admin" is listed under the app name. If the MDM console device policy is not set to allow connections to only approved application repositories or on the Honeywell Android Pie device, the device policy is not set to allow connections to only approved application repositories, this is a finding.

## Group: PP-MDF-301090

**Group ID:** `V-235068`

### Rule: The Honeywell Mobility Edge Android Pie device must be configured to enforce an application installation policy by specifying an application whitelist that restricts applications by the following characteristics: [selection: list of digital signatures, cryptographic hash values, names, application version].

**Rule ID:** `SV-235068r852708_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The application whitelist, in addition to controlling the installation of applications on the MD, must control user access/execution of all core and preinstalled applications, or the MD must provide an alternate method of restricting user access/execution to core and pre-installed applications. Core application: Any application integrated into the OS by the OS or MD vendors. Pre-installed application: Additional non-core applications included in the OS build by the OS vendor, MD vendor, or wireless carrier. Requiring all authorized applications to be in an application whitelist prevents the execution of any applications (e.g., unauthorized, malicious) that are not part of the whitelist. Failure to configure an application whitelist properly could allow unauthorized and malicious applications to be downloaded, installed, and executed on the mobile device, causing a compromise of DoD data accessible by these applications. The application whitelist, in addition to controlling the installation of applications on the MD, must control user access/execution of all core applications (included in the OS by the OS vendor) and pre-installed applications (provided by the MD vendor and wireless carrier), or the MD must provide an alternate method of restricting user access/execution to core and pre-installed applications. SFR ID: FMT_SMF_EXT.1.1 #8b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Honeywell Android device configuration settings to determine if the mobile device has an application whitelist configured. Verify all applications listed on the whitelist have been approved by the Approving Official (AO). This validation procedure is performed only on the MDM Administration console. On the MDM console: 1. Go to the Android app catalog for managed Honeywell Play. 2. Verify all selected apps are AO approved. NOTE: Managed Google Play is always a Whitelisted App Store. If on the MDM console the list of selected Managed Honeywell Play apps included non-approved apps, this is a finding. NOTE: The application whitelist will include approved core applications (included in the OS by the OS vendor) and pre-installed applications (provided by the MD vendor and wireless carrier), or the MD must provide an alternate method of restricting user access/execution to core and pre-installed applications. For Honeywell Android, there are no pre-installed applications.

## Group: PP-MDF-301100

**Group ID:** `V-235069`

### Rule: The Honeywell Mobility Edge Android Pie device whitelist must be configured to not include applications with the following characteristics: 

- back up MD data to non-DoD cloud servers (including user and application access to cloud backup services);
- transmit MD diagnostic data to non-DoD servers;
- voice assistant application if available when MD is locked;
- voice dialing application if available when MD is locked;
- allows synchronization of data or applications between devices associated with user; and
- allows unencrypted (or encrypted but not FIPS 140-2 validated) data sharing with other MDs or printers.

**Rule ID:** `SV-235069r852709_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Requiring all authorized applications to be in an application whitelist prevents the execution of any applications (e.g., unauthorized, malicious) that are not part of the whitelist. Failure to configure an application whitelist properly could allow unauthorized and malicious applications to be downloaded, installed, and executed on the mobile device, causing a compromise of DoD data accessible by these applications. Applications with the listed characteristics have features that can cause the compromise of sensitive DoD data or have features with no known application in the DoD environment. Application note: The application whitelist, in addition to controlling the installation of applications on the MD, must control user access/execution of all core and preinstalled applications, or the MD must provide an alternate method of restricting user access/execution to core and pre-installed applications. Core application: Any application integrated into the OS by the OS or MD vendors. Pre-installed application: Additional non-core applications included in the OS build by the OS vendor, MD vendor, or wireless carrier. SFR ID: FMT_SMF_EXT.1.1 #8b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Honeywell Android device configuration settings to determine if the mobile device has an application whitelist configured and that the application whitelist does not include applications with the following characteristics: - back up MD data to non-DoD cloud servers (including user and application access to cloud backup services); - transmit MD diagnostic data to non-DoD servers; - voice assistant application if available when MD is locked; - voice dialing application if available when MD is locked; - allows synchronization of data or applications between devices associated with user; - payment processing; and - allows unencrypted (or encrypted but not FIPS 140-2 validated) data sharing with other MDs, display screens (screen mirroring), or printers. This validation procedure is performed only on the MDM Administration console. On the MDM console: 1. Review the list of selected Managed Honeywell Play apps. 2. Review the details and privacy policy of each selected app to ensure the app does not include prohibited characteristics. If the MDM console device policy includes applications with unauthorized characteristics, this is a finding.

## Group: PP-MDF-301110

**Group ID:** `V-235070`

### Rule: The Honeywell Mobility Edge Android Pie device must be configured to disable Bluetooth or configured via User Based Enforcement (UBE) to allow Bluetooth for only HSP (Headset Profile), HFP (HandsFree Profile), or SPP (Serial Port Profile) capable devices.

**Rule ID:** `SV-235070r852710_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Some Bluetooth profiles provide the capability for remote transfer of sensitive DoD data without encryption or otherwise do not meet DoD IT security policies and therefore should be disabled. SFR ID: FMT_SMF_EXT.1.1 #18h</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the AO has approved the use of Bluetooth at the site. If the AO has not approved the use of Bluetooth, verify Bluetooth has been disabled: On the MDM console: 1. Open Restrictions section. 2. Ensure "Disallow Bluetooth" is set. On the Honeywell Android Pie device: 1. Go to Settings >> Connected Devices >> Connection Preferences >> Bluetooth. 2. Ensure that it is set to "Off" and cannot be toggled to "On". If the AO has approved the use of Bluetooth, on the Honeywell Android Pie device: 1. Go to Settings >> Connected Devices. 2. Verify only approved Bluetooth connected devices using approved profiles are listed. If the AO has not approved the use of Bluetooth, and Bluetooth use is not disabled via an MDM managed device policy, this is a finding. If the AO has approved the use of Bluetooth, and Bluetooth devices using unauthorized Bluetooth profiles are listed on the device under "Connected devices", this is a finding.

## Group: PP-MDF-301120

**Group ID:** `V-235071`

### Rule: The Honeywell Mobility Edge Android Pie device must be configured to not display the following (work profile) notifications when the device is locked: [selection:

- email notifications 
- calendar appointments 
- contact associated with phone call notification 
- text message notification
- other application-based notifications
- all notifications].

**Rule ID:** `SV-235071r626531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Many mobile devices display notifications on the lock screen so that users can obtain relevant information in a timely manner without having to frequently unlock the phone to determine if there are new notifications. However, in many cases, these notifications can contain sensitive information. When they are available on the lock screen, an adversary can see them merely by being in close physical proximity to the device. Configuring the Honeywell Android device to not send notifications to the lock screen mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #19</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Honeywell Android device settings to determine if the Honeywell Android device displays (work container) notifications on the lock screen. Notifications of incoming phone calls are acceptable even when the device is locked. This validation procedure is performed on both the MDM Administration console and the Android Pie device. On the MDM console: 1. Open Restrictions section. 2. Open Work Managed Section. 3. Ensure "Unredacted Notifications" is set to "Disallow". On the Honeywell Android Pie device: 1. Go to Settings >> Security & location. 2. Tap on Lock screen preferences. 3. Ensure "Hide sensitive work content" is listed under "When work profile is locked". If the MDM console device policy allows work notifications on the lock screen or the Android Pie device allows work notifications on the lock screen, this is a finding.

## Group: PP-MDF-301150

**Group ID:** `V-235072`

### Rule: The Honeywell Mobility Edge Android Pie device must be configured to disable trust agents. 
 
NOTE: This requirement is not applicable (NA) for specific biometric authentication factors included in the product's Common Criteria evaluation.

**Rule ID:** `SV-235072r626531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Trust agents allow a user to unlock a mobile device without entering a passcode when the mobile device is, for example, connected to a user-selected Bluetooth device or in a user-selected location. This technology would allow unauthorized users to have access to DoD sensitive data if compromised. By not permitting the use of non-password authentication mechanisms, users are forced to use passcodes that meet DoD passcode requirements. SFR ID: FMT_SMF_EXT.1.1 #23, FIA_UAU.5.1</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review device configuration settings to confirm that trust agents are disabled. This procedure is performed on both the MDM Administration console and the Honeywell Android Pie device. On the MDM console: 1. Open Restrictions section. 2. Set "Disable trust agents" to "On". On the Honeywell Android Pie device: 1. Open Settings. 2. Tap "Security & location". 3. Tap "Advanced". 4. Tap "Trust agents". 5. Verify that all listed trust agents are disabled and cannot be enabled. If on the MDM console "disable trust agents" is not selected, or on the Honeywell Android Pie device a trust agent can be enabled, this is a finding.

## Group: PP-MDF-301170

**Group ID:** `V-235073`

### Rule: The Honeywell Mobility Edge Android Pie device must be configured to disable developer modes.

**Rule ID:** `SV-235073r626531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Developer modes expose features of the Honeywell Android device that are not available during standard operation. An adversary may leverage a vulnerability inherent in a developer mode to compromise the confidentiality, integrity, and availability of DoD sensitive information. Disabling developer modes mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #26</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Honeywell Android device configuration settings to determine whether a developer mode is enabled. This validation procedure is performed on both the MDM Administration console and the Android Pie device. On the MDM console: 1. Open Restrictions section. 2. Confirm that "Debugging Features" is set to "Disallow". On the Honeywell Android Pie device: 1. Go to Settings >> System. 2. Ensure Developer Options is not listed. If the MDM console device policy is not set to disable developer mode or on the Honeywell Android Pie device, the device policy is not set to disable developer mode, this is a finding.

## Group: PP-MDF-301200

**Group ID:** `V-235074`

### Rule: The Honeywell Mobility Edge Android Pie device must be configured to display the DoD advisory warning message at start-up or each time the user unlocks the device.

**Rule ID:** `SV-235074r626531_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Honeywell Mobility Edge Android Pie device is required to display the DoD-approved system use notification message or banner before granting access to the system that provides privacy and security notices consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. Required banners help ensure that DoD can audit and monitor the activities of mobile device users without legal restriction. System use notification messages can be displayed when individuals first access or unlock the mobile device. The banner must be implemented as a "click-through" banner at device unlock (to the extent permitted by the operating system). A "click-through" banner prevents further activity on the information system unless and until the user executes a positive action to manifest agreement by clicking on a box indicating "OK." The approved DoD text must be used exactly as required in the KS referenced in DoDI 8500.01. For devices accommodating banners of 1300 characters, the banner text is: You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. For devices with severe character limitations, the banner text is: I've read & consent to terms in IS user agreem't. The administrator must configure the banner text exactly as written without any changes. SFR ID: FMT_SMF_EXT.1.1 #36</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The DoD warning banner can be displayed by either of the following methods (required text is found in the Vulnerability Description): 1. By placing the DoD warning banner text in the user agreement signed by each Honeywell Android device user (preferred method). 2. By configuring the warning banner text on the MDM console and installing the banner on each managed mobile device. Determine which method is used at the Honeywell Android device site and follow the appropriate validation procedure below. Validation Procedure for Method #1: Review the signed user agreements for several Honeywell Android device users and verify the agreement includes the required DoD warning banner text. Validation Procedure for Method #2: On the MDM console: Ensure "Lock Screen Message" and the appropriate banner text is included. If, for Method #1, the required warning banner text is not on all signed user agreements reviewed, or for Method #2, the MDM console device policy is not set to display a warning banner with the appropriate designated wording or on the Honeywell Android Pie device, the device policy is not set to display a warning banner with the appropriate designated wording, this is a finding.

## Group: PP-MDF-301210

**Group ID:** `V-235075`

### Rule: The Honeywell Mobility Edge Android Pie device must be configured to disable USB mass storage mode.

**Rule ID:** `SV-235075r626531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>USB mass storage mode enables the transfer of data and software from one device to another. This software can include malware. When USB mass storage is enabled on a mobile device, it becomes a potential vector for malware and unauthorized data exfiltration. Prohibiting USB mass storage mode mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #39a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Honeywell Android device configuration settings to determine if the mobile device has a USB mass storage mode and whether it has been disabled. This validation procedure is performed on both the MDM Administration console and the Android Pie device. On the MDM console: 1. Open Device Restrictions. 2. Open Restrictions settings. 3. Ensure "Disallow usb file transfer" is selected. On the Honeywell Android Pie device: 1. Plug USB cable into Android Pie device and connect to a non-DoD network-managed PC. 2. Go to Settings >> Connected devices >> USB. 3. Ensure No data transfer is selected. If the MDM console device policy is not set to disable USB mass storage mode or on the Honeywell Android Pie device, the device policy is not set to disable USB mass storage mode, this is a finding.

## Group: PP-MDF-301220

**Group ID:** `V-235076`

### Rule: The Honeywell Mobility Edge Android Pie device must be configured to not allow backup of [all applications, configuration data] to locally connected systems.

**Rule ID:** `SV-235076r626531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data on mobile devices is protected by numerous mechanisms, including user authentication, access control, and cryptography. When the data is backed up to an external system (either locally connected or cloud-based), many if not all of these mechanisms are no longer present. This leaves the backed-up data vulnerable to attack. Disabling backup to external systems mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #40</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Honeywell Android device configuration settings to determine if the capability to back up to a locally connected system has been disabled. This validation procedure is performed on both the MDM Administration console and the Android Pie device. On the MDM console: 1. Open Device Restrictions. 2. Open Restrictions settings. 3. Ensure "Disallow usb file transfer" is selected. On the Honeywell Android Pie device: 1. Plug USB cable into Android Pie device and connect to a non-DoD network-managed PC. 2. Go to Settings >> Connected devices >> USB. 3. Ensure "No data transfer" is selected. If the MDM console device policy is not set to disable the capability to back up to a locally connected system or on the Honeywell Android Pie device, the device policy is not set to disable the capability to back up to a locally connected system, this is a finding.

## Group: PP-MDF-301230

**Group ID:** `V-235077`

### Rule: The Honeywell Mobility Edge Android Pie device must be configured to not allow backup of all applications and configuration data to remote systems.

**Rule ID:** `SV-235077r852711_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Backups to remote systems (including cloud backup) can leave data vulnerable to breach on the external systems, which often offer less protection than the Honeywell Android device. Where the remote backup involves a cloud-based solution, the backup capability is often used to synchronize data across multiple devices. In this case, DoD devices may synchronize DoD sensitive information to a user's personal device or other unauthorized computers that are vulnerable to breach. Disallowing remote backup mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #40</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Honeywell Android device configuration settings to determine if the capability to back up to a remote system has been disabled. This validation procedure is performed on both the MDM Administration console and the Android Pie device. On the MDM console: 1. Open Device Restrictions. 2. Open Restrictions settings. 3. Ensure "Disallow backup servicer" is not selected. On the Honeywell Android Pie device: 1. Go to Settings >> System. 2. Ensure Backup is set to "Off". If the MDM console device policy is not set to disable the capability to back up to a remote system or on the Honeywell Android Pie device, the device policy is not set to disable the capability to back up to a remote system, this is a finding.

## Group: PP-MDF-301260

**Group ID:** `V-235078`

### Rule: The Honeywell Mobility Edge Android Pie device must be configured to disable exceptions to the access control policy that prevents application processes from accessing all data stored by other application processes.

**Rule ID:** `SV-235078r852712_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>App data sharing gives apps the ability to access the data of other apps for enhanced user functionality. However, sharing also poses a significant risk that unauthorized users or apps will obtain access to DoD sensitive information. To mitigate this risk, there are data sharing restrictions. If a user is allowed to make exceptions to the data sharing restriction policy, the user could enable unauthorized sharing of data, leaving it vulnerable to breach. Limiting the granting of exceptions to either the Administrator or common application developer mitigates this risk. Copy/paste of data between applications in different application processes or groups of application processes is considered an exception to the access control policy and therefore, the Administrator must be able to enable/disable the feature. Other exceptions include allowing any data or application sharing between process groups. SFR ID: FMT_SMF_EXT.1.1 #42, FDP_ACF_EXT.1.2</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review documentation on the Honeywell Android device and inspect the configuration on the Honeywell Android device to verify the access control policy that prevents [selection: application processes] from accessing [selection: all] data stored by other [selection: application processes] is enabled. This validation procedure is performed only on the MDM Administration console. On the MDM console: 1. Open Restrictions settings. 2. Open User restrictions. 3. Ensure "Disallow cross profile copy/paste" is selected. 4. Ensure "Disallow sharing data into the profile" is selected. If the MDM console device policy is not set to disable data sharing between profiles, this is a finding.

## Group: PP-MDF-301280

**Group ID:** `V-235079`

### Rule: The Honeywell Mobility Edge Android Pie device must be configured to disable multi-user modes.

**Rule ID:** `SV-235079r852713_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Multi-user mode allows multiple users to share a mobile device by providing a degree of separation between user data. To date, no mobile device with multi-user mode features meets DoD requirements for access control, data separation, and non-repudiation for user accounts. In addition, the MDFPP does not include design requirements for multi-user account services. Disabling multi-user mode mitigates the risk of not meeting DoD multi-user account security policies. SFR ID: FMT_SMF_EXT.1.1 #47b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review documentation on the Honeywell Android device and inspect the configuration on the Honeywell Android device to disable multi-user modes. This validation procedure is performed on both the MDM Administration console and the Android Pie device. On the MDM console: 1. Open the Restrictions settings. 2. Open User settings. 3. Confirm "Disallow Add User" is selected. On the Honeywell Android Pie device: 1. Go to Settings >> System >> Advanced >> Multiple users. 2. Verify there is no option to add a user. If the MDM console device policy is not set to disable multi-user modes or on the Honeywell Android Pie device, the device policy is not set to disable multi-user modes, this is a finding.

## Group: PP-MDF-302370

**Group ID:** `V-235080`

### Rule: The Honeywell Mobility Edge Android Pie device must be configured to enable audit logging.

**Rule ID:** `SV-235080r852714_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit logs enable monitoring of security-relevant events and subsequent forensics when breaches occur. To be useful, Administrators must have the ability to view the audit logs. SFR ID: FMT_SMF_EXT.1.1 #32</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review documentation on the Honeywell Android device and inspect the configuration on the Honeywell Android device to enable audit logging. This validation procedure is performed on only on the MDM Administration console. On the MDM console: 1. Open the Restrictions settings. 2. Open User settings. 3. Select "Enable security logging". 4. Select "Enable network logging". If the MDM console device policy is not set to enable audit logging, this is a finding.

## Group: PP-MDF-301420

**Group ID:** `V-235081`

### Rule: The Honeywell Mobility Edge Android Pie device must be configured to generate audit records for the following auditable events: detected integrity violations.

**Rule ID:** `SV-235081r626531_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Audit logs enable monitoring of security-relevant events and subsequent forensics when breaches occur. They help identify attacks so that breaches can either be prevented or limited in their scope. They facilitate analysis to improve performance and security. The Requirement Statement lists key events the system must generate in an audit record. Application note: Requirement applies only to integrity violation detections that can be logged by the audit logging component. SFR ID: FMT_SMF_EXT.1.1 #37</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Honeywell Android device configuration settings to determine if the mobile device is configured to generate audit records for the following auditable events: detected integrity violations. This validation procedure is performed only on the MDM Administration console. On the MDM console: 1. Go to Policy management. 2. Confirm Security Logging is enabled. If the MDM console device policy is not set to enable security logging, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-235082`

### Rule: Honeywell Mobility Edge Android Pie devices users must complete required training.

**Rule ID:** `SV-235082r626531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The security posture of Honeywell devices requires the device user to configure several required policy rules on their device. User-Based Enforcement (UBE) is required for these controls. In addition, if the Authorizing Official (AO) has approved the use of an unmanaged personal space, the user must receive training on risks. If a user is not aware of their responsibilities and does not comply with UBE requirements, the security posture of the Honeywell mobile device may become compromised and DoD sensitive data may become compromised. SFR ID: NA</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review a sample of site User Agreements for Honeywell device users or similar training records and training course content. Verify that Honeywell device users have completed the required training. The intent is that required training is renewed on a periodic basis in a time period determined by the AO. If any Honeywell device user has not completed the required training, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-235083`

### Rule: Honeywell Mobility Edge Android Pie devices must have the DoD root and intermediate PKI certificates installed.

**Rule ID:** `SV-235083r626531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoD root and intermediate PKI certificates are used to verify the authenticity of PKI certificates of users and web services. If the root and intermediate certificates are not available, an adversary could falsely sign a certificate in such a way that it could not be detected. Providing access to the DoD root and intermediate PKI certificates greatly diminishes the risk of this attack. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review device configuration settings to confirm that the DoD root and intermediate PKI certificates are installed. This procedure is performed on both the MDM Administration console and the Honeywell Android Pie device. The current DoD root and intermediate PKI certificates may be obtained in self-extracting zip files at http://cyber.mil/pki-pke (for NIPRNet). On the MDM console, verify that the DoD root and intermediate certificates are part of a device and/or work profile that is being pushed down to the devices. On the Honeywell Android Pie device: 1. Open Settings. 2. Tap "Security & Location". 3. Tap on "Advanced". 4. Tap on "Encryption & credentials". 5. Tap on "Trusted credentials". 6. Verify that DoD root and intermediate PKI certificates are listed under the user tab. If on the MDM console the DoD root and intermediate certificates are not listed in a profile, or on the Honeywell Android Pie device does not list the DoD root and intermediate certificates under the user tab, this is a finding.

## Group: PP-MDF-992000

**Group ID:** `V-235084`

### Rule: The Honeywell Mobility Edge Android Pie must allow only the administrator (MDM) to install/remove DoD root and intermediate PKI certificates.

**Rule ID:** `SV-235084r626531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoD root and intermediate PKI certificates are used to verify the authenticity of PKI certificates of users and web services. If the user is allowed to remove root and intermediate certificates, the user could allow an adversary to falsely sign a certificate in such a way that it could not be detected. Restricting the ability to remove DoD root and intermediate PKI certificates to the Administrator mitigates this risk. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration to confirm that the user is unable to remove DoD root and intermediate PKI certificates. On the MDM console: 1. Open the User restrictions setting. 2. Verify that "Disallow config credentials" to "On" for the work profile. On the Honeywell Android Pie device: 1. Open Settings. 2. Tap "Security & Location". 3. Tap on "Advanced". 4. Tap on "Encryption & credentials". 5. Tap on "Trusted credentials". 6. Verify that the user is unable to untrust or remove any work certificates. If on the Honeywell Android Pie device the user is able to remove certificates, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-235085`

### Rule: The Honeywell Mobility Edge Android Pie device Work Profile must be configured to prevent users from adding personal email accounts to the work email app.

**Rule ID:** `SV-235085r626531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the user is able to add a personal email account (POP3, IMAP, EAS) to the work email app, it could be used to forward sensitive DoD data to unauthorized recipients. Restricting email account addition to the administrator or restricting email account addition to whitelisted accounts mitigates this vulnerability. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Honeywell Mobility Edge Android Pie devices Work Profile configuration settings to confirm that users are prevented from adding personal email accounts to the work email app. This procedure is performed on both the MDM Administrator console and the Honeywell Mobility Edge Android Pie devices device. On the MDM console: 1. Open the User restrictions setting. 2. Verify that "Disallow add accounts" is set to "On". On the Honeywell Android Pie device, do the following: 1. Open Settings. 2. Tap "Accounts". 3. Verify that "Add account" is grayed out under the Work section. If on the MDM console the restriction to "Disallow add accounts" is not set or on the Honeywell Mobility Edge Android Pie device the user is able to add an account, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-235086`

### Rule: Honeywell Mobility Edge Android Pie devices work profile must be configured to enforce the system application disable list.

**Rule ID:** `SV-235086r626531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The system application disable list controls user access to/execution of all core and preinstalled applications. Core application: Any application integrated into Honeywell Mobility Edge Android Pie devices by Honeywell. Preinstalled application: Additional noncore applications included in the Honeywell Mobility Edge Android Pie device build by Honeywell or the wireless carrier. Some system applications can compromise DoD data or upload users' information to non-DoD-approved servers. A user must be blocked from using such applications that exhibit behavior that can result in compromise of DoD data or DoD user information. The site administrator must analyze all preinstalled applications on the device and disable all applications not approved for DoD use by configuring the system application disable list. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Honeywell Mobility Edge Android Pie devices Work Profile configuration settings to confirm the system application disable list is enforced. This setting is enforced by default. What needs to happen is to verify only approved system apps have been placed on the core whitelist. This procedure is performed on the MDM Administrator console. Review the system app whitelist and verify only approved apps are on the list. If on the MDM console the system app whitelist contains unapproved core apps, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-235087`

### Rule: Honeywell Mobility Edge Android Pie devices must be provisioned as a fully managed device and configured to create a work profile.

**Rule ID:** `SV-235087r626531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Android Enterprise Work Profile is the designated application group for the COPE use case. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review that Honeywell Mobility Edge Android Pie devices is configured as Corporate Owned Work Managed. This procedure is performed on both the MDM Administrator console and the Honeywell Mobility Edge Android Pie devices device. On the MDM console, verify that the default enrollment is set to Corporate Owned Work Managed. On the Honeywell Android Pie device: 1. Go to the application drawer. 2. Ensure there is a Personal tab and a Work tab. If on the MDM console the default enrollment is set to Corporate Owned Work Managed or on the Honeywell Android Pie device the user does not see a Work tab, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-235088`

### Rule: Honeywell Mobility Edge Android Pie devices work profile must be configured to disable automatic completion of workspace internet browser text input.

**Rule ID:** `SV-235088r626531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The autofill functionality in the web browser allows the user to complete a form that contains sensitive information, such as personally identifiable information (PII), without previous knowledge of the information. By allowing the use of autofill functionality, an adversary who learns a user's Honeywell Mobility Edge Android Pie devices' password, or who otherwise is able to unlock the device, may be able to further breach other systems by relying on the autofill feature to provide information unknown to the adversary. By disabling the autofill functionality, the risk of an adversary gaining further information about the device's user or compromising other systems is significantly mitigated. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Chrome Browser in the Honeywell Android Pie device's Work Profile autofill setting. This procedure is performed only on the MDM Administrator console. On the MDM console, for the Work Profile, do the following: 1. Open the Chrome Browser Settings. 2. Verify "Enable autofill" is set to "Off". If on the MDM console autofill is set to "On" in the Chrome Browser Settings, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-235089`

### Rule: Honeywell Mobility Edge Android Pie devices Work Profile must be configured to disable the autofill services.

**Rule ID:** `SV-235089r626531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The autofill services allow the user to complete text inputs that could contain sensitive information, such as personally identifiable information (PII), without previous knowledge of the information. By allowing the use of autofill services, an adversary who learns a user's Honeywell Android Pie device password, or who otherwise is able to unlock the device, may be able to further breach other systems by relying on the autofill services to provide information unknown to the adversary. By disabling the autofill services, the risk of an adversary gaining further information about the device's user or compromising other systems is significantly mitigated. Examples of apps that offer autofill services include Samsung Pass, Honeywell, Dashlane, LastPass, and 1Password. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Honeywell Mobility Edge Android Pie devices Workspace configuration settings to confirm that autofill services are disabled. This procedure is performed only on the MDM Administration console. On the MDM console, for the Workspace, in the "Android user restrictions" group, under the work profile, verify that "disallow autofill" is selected. If on the MDM console "disallow autofill" is selected, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-235090`

### Rule: Honeywell Mobility Edge Android Pie devices must be configured to disallow configuration of date and time.

**Rule ID:** `SV-235090r626531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Determining the correct time a particular application event occurred on a system is critical when conducting forensic analysis and investigating system events. Periodically synchronizing internal clocks with an authoritative time source is necessary to correctly correlate the timing of events that occur across the enterprise. The three authoritative time sources for Honeywell Mobility Edge Android Pie devices are an authoritative time server that is synchronized with redundant United States Naval Observatory (USNO) time servers as designated for the appropriate DoD network (NIPRNet or SIPRNet), or the Global Positioning System (GPS), or the wireless carrier. Time stamps generated by the audit system in Honeywell Mobility Edge Android Pie devices must include both date and time. The time may be expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Honeywell Android Pie device's Work Profile configuration settings to confirm that autofill services are disabled. This procedure is performed on both the MDM Administration console and the Honeywell Android Pie device. On the MDM console, verify that "Set auto (network) time required" is set to "On". On the Honeywell Android Pie device: 1. Open Settings. 2. Tap "System". 3. Tap "Date & times". 4. Verify that "Automatic date & time" is grayed out. If on the MDM console "Set auto (network) time required" is not set to "On", or on the Honeywell Android Pie device "Automatic date & time" is grayed out, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-235091`

### Rule: Honeywell Mobility Edge Android Pie devices must configured to disallow outgoing beam.

**Rule ID:** `SV-235091r626531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Outgoing beam allows transfer of data through near field communication (NFC) and Bluetooth by touching two unlocked devices together. If it were enabled, sensitive DoD data could be transmitted. Because of the security risks of sharing sensitive DoD data, users must not be able to allow outgoing beam. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Honeywell Android Pie device configuration settings to confirm that outgoing beam is disallowed. This procedure is performed on both the MDM Administration console and the Honeywell Android Pie device. On the MDM console, in the Android user restrictions section, verify that "Disallow outgoing beam" is set to "On". On the Honeywell Android Pie device: 1. Open Settings. 2. Tap "Connected devices". 3. Tap "Connection preferences". 4. Verify that "Android Beam" is off and grayed out. If on the MDM console "Disallow outgoing beam" is not set to "On", or on the Honeywell Android Pie device "Android Beam" is not off and grayed out, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-235092`

### Rule: Honeywell Mobility Edge Android Pie devices must have a NIAP validated Honeywell Mobility Edge Android Pie devices operating system installed.

**Rule ID:** `SV-235092r626531_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Required security features are not available in earlier operating system versions. In addition, there may be known vulnerabilities in earlier versions. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review device configuration settings to confirm that version HON660-P-88.00.12 is installed (it is the NIAP-approved version). NOTE: This version of Android can only be installed on devices purchased directly from Honeywell. This procedure is performed on both the MDM console and the Honeywell Android Pie device. In the MDM management console, review the version of Honeywell Android Pie installed on a sample of managed devices. On the Honeywell Mobility Edge Android Pie device, to see the installed operating system version: 1. Open Settings. 2. Tap "About phone". 3. Verify "Build number". If the installed version of the Android operating system on any reviewed Honeywell devices is not the latest released by the wireless carrier, this is a finding. Honeywell's Android operating system patch website is available at https://source.android.com/security/bulletin/. If the installed version of the Android Pie operating system is not the NIAP-approved version, this is a finding.

## Group: PP-MDF-301010

**Group ID:** `V-235094`

### Rule: On all Honeywell Mobility Edge Android Pie devices, cryptography must be configured to be in FIPS 140-2 validated mode.

**Rule ID:** `SV-235094r626531_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved cryptographic algorithms cannot be relied upon to provide confidentiality or integrity, and DoD data could be compromised as a result. The Honeywell Android devices common vulnerabilities with cryptographic modules are those associated with poor implementation. FIPS 140-2 validation provides assurance that the relevant cryptography has been implemented correctly. FIPS 140-2 validation is also a strict requirement for use of cryptography in the Federal Government for protecting unclassified data. SFR ID: FCS</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Honeywell Android device configuration settings to determine if the mobile device is in FIPS enforce mode. This validation procedure is performed on the Android Pie device. On the Honeywell Android Pie device: 1. Open Settings >> Honeywell Settings >> FIPS Enforce Mode. 2. Verify the option of "FIPS Enforce Mode" is enabled. If the option of "FIPS Enforce Mode" is disabled on the Honeywell Android Pie device, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-259208`

### Rule: All Honeywell Android 9 installations must be removed.

**Rule ID:** `SV-259208r942501_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Honeywell Android 9 is no longer supported by Honeywell and therefore may contain security vulnerabilities. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there are no installations of Honeywell Android 9 at the site. If Honeywell Android 9 is being used at the site, this is a finding.

## Group: PP-MDF-301010

**Group ID:** `V-259714`

### Rule: The Honeywell Mobility Edge Android Pie device must be configured to enforce a minimum password length of six characters.

**Rule ID:** `SV-259714r942508_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password strength is a measure of the effectiveness of a password in resisting guessing and brute force attacks. The ability to crack a password is a function of how many attempts an adversary is permitted, how quickly an adversary can do each attempt, and the size of the password space. The longer the minimum length of the password is, the larger the password space. Having a too-short minimum password length significantly reduces password strength, increasing the chance of password compromise, and resulting device and data compromise. SFR ID: FMT_SMF_EXT.1.1 #1a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Honeywell Android device configuration settings to determine if the mobile device is enforcing a minimum password length of six characters. This validation procedure is performed on both the MDM Administration console and the Android Pie device. On the MDM console: 1. Open password requirements. 2. Open device password section. 3. Ensure the minimum password length is set to "6" characters. On the Honeywell Android Pie device: 1. Open Settings >> Security & location >> Screen lock. 2. Enter current password. 3. Tap on "Password". 4. Verify Password length listed is at least "6". If the device password length is not set to six characters or more on the MDM console or on the Honeywell Android Pie device, this is a finding.

