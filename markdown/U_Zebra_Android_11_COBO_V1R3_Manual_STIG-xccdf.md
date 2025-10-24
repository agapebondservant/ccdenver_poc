# STIG Benchmark: Zebra Android 11 COBO Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: PP-MDF-301010

**Group ID:** `V-252850`

### Rule: Zebra Android 11 must be configured to enforce a minimum password length of six characters.

**Rule ID:** `SV-252850r820477_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password strength is a measure of the effectiveness of a password in resisting guessing and brute force attacks. The ability to crack a password is a function of how many attempts an adversary is permitted, how quickly an adversary can do each attempt, and the size of the password space. The longer the minimum length of the password is, the larger the password space. Having a too-short minimum password length significantly reduces password strength, increasing the chance of password compromise and resulting device and data compromise. SFR ID: FMT_SMF_EXT.1.1 #1a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Zebra Android device configuration settings to determine if the mobile device is enforcing a minimum password length of six characters. This validation procedure is performed on both the EMM Administration Console and the Android 11 device. On the EMM console: 1. Open "Password constraints". 2. Select "Personal Profile". 3. Open "Minimum password quality". 4. Check that "Numeric Complex", "Alphabetic, Alphanumeric", or "Complex" is selected. 5. Verify that "Minimum password length" is "6". On the Android 11 device, do the following: 1. Open Settings >> Security >> Screen lock. 2. Enter current password. 3. Tap "Password or PIN". 4. Verify Password length listed is at least "6". If the device password length is not set to six characters or more on EMM console or on the Android 11 device, this is a finding.

## Group: PP-MDF-301020

**Group ID:** `V-252851`

### Rule: Zebra Android 11 must be configured to not allow passwords that include more than four repeating or sequential characters.

**Rule ID:** `SV-252851r820480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password strength is a measure of the effectiveness of a password in resisting guessing and brute force attacks. Passwords that contain repeating or sequential characters are significantly easier to guess than those that do not contain repeating or sequential characters. Therefore, disallowing repeating or sequential characters increases password strength and decreases risk. The numeric (complex) setting allows the use of a numeric only keyboard for passwords and enforces the repeating or sequential characters limitation. SFR ID: FMT_SMF_EXT.1.1 #1b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Zebra Android device configuration settings to determine if the mobile device is prohibiting passwords with more than four repeating or sequential characters. This validation procedure is performed on both the EMM Administration Console and the Android 11 device. On the EMM console, do the following: 1. Open "Password constraints". 2. Select "Personal Profile". 3. Verify that quality is set to "Numeric (Complex)". On the Android 11 device, do the following: 1. Open Settings >> Security >> Screen lock. 2. Enter current password. 3. Tap "Password". 4. Try to enter a new PIN or Password with repeating numbers or characters. 5. Verify Password complexity requirements are listed: Ascending, descending, or repeated sequence of digits is not allowed. If the EMM console device policy is set to a password with more than four repeating or sequential characters or on the Android 11 device, the device policy is set to a password with more than four repeating or sequential characters, this is a finding. Note: Alphabetic, Alphanumeric, and Complex are also acceptable selections, but these selections will cause the user to select a complex password, which is not required by the STIG.

## Group: PP-MDF-301030

**Group ID:** `V-252852`

### Rule: Zebra Android 11 must be configured to enable a screen-lock policy that will lock the display after a period of inactivity.

**Rule ID:** `SV-252852r820483_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The screen-lock timeout helps protect the device from unauthorized access. Devices without a screen-lock timeout provide an opportunity for adversaries who gain physical access to the mobile device through loss, theft, etc. Such devices are much more likely to be in an unlocked state when acquired by an adversary, thus granting immediate access to the data on the mobile device and possibly access to DoD networks. SFR ID: FMT_SMF_EXT.1.1 #2a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Zebra Android device configuration settings to determine if the mobile device is enforcing a screen-lock policy that will lock the display after a period of inactivity. This validation procedure is performed on both the EMM Administration Console and the Android 11 device. On the EMM Console: 1. Open "Lock screen restrictions". 2. Select "Personal Profile". 3. Verify that "Max time to screen lock" is set to any number desired. The units are in seconds. On the Android 11 device, do the following: 1. Open Settings >> Display. 2. Tap "Screen timeout". 3. Ensure the Screen timeout value is set to the desired value and cannot be set to a larger value. If the EMM console device policy is not set to enable a screen-lock policy that will lock the display after a period of inactivity or on the Android 11 device, the device policy is not set to enable a screen-lock policy that will lock the display after a period of inactivity, this is a finding.

## Group: PP-MDF-301040

**Group ID:** `V-252853`

### Rule: Zebra Android 11 must be configured to lock the display after 15 minutes (or less) of inactivity.

**Rule ID:** `SV-252853r820486_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The screen lock timeout must be set to a value that helps protect the device from unauthorized access. Having a too-long timeout would increase the window of opportunity for adversaries who gain physical access to the mobile device through loss, theft, etc. Such devices are much more likely to be in an unlocked state when acquired by an adversary, thus granting immediate access to the data on the mobile device. The maximum timeout period of 15 minutes has been selected to balance functionality and security; shorter timeout periods may be appropriate depending on the risks posed to the mobile device. SFR ID: FMT_SMF_EXT.1.1 #2b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Zebra Android device configuration settings to determine if the mobile device has the screen lock timeout set to 15 minutes or less. This validation procedure is performed on both the EMM Administration Console and the Android 11 device. On the EMM Console: 1. Open "Lock screen restrictions". 2. Select "Personal Profile". 3. Verify that "Max time to screen lock" is set to any number between 1 and 900. Units are in seconds; therefore, 900 represents 15 minutes. On the Android 11 device, do the following: 1. Open Settings >> Display. 2. Tap "Screen timeout". 3. Ensure the Screen timeout value is set between 1 and 15 (minutes). If the EMM console device policy is not set to 15 minutes or less for the screen lock timeout or on the Android 11 device, the device policy is not set to 15 minutes or less for the screen lock timeout, this is a finding.

## Group: PP-MDF-301050

**Group ID:** `V-252854`

### Rule: Zebra Android 11 must be configured to not allow more than 10 consecutive failed authentication attempts.

**Rule ID:** `SV-252854r820489_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The more attempts an adversary has to guess a password, the more likely the adversary will enter the correct password and gain access to resources on the device. Setting a limit on the number of attempts mitigates this risk. Setting the limit at 10 or less gives authorized users the ability to make a few mistakes when entering the password, but still provides adequate protection against dictionary or brute force attacks on the password. SFR ID: FMT_SMF_EXT.1.1 #2c, FIA_AFL_EXT.1.5</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Zebra Android device configuration settings to determine if the mobile device has the maximum number of consecutive failed authentication attempts set at 10 or fewer. This validation procedure is performed on both the EMM Administration Console and the Android 11 device. On the EMM Console: 1. Open "Lock screen restrictions". 2. Select "Personal Profile". 3. Verify that "Max password failures for local wipe" is set to a number between 1 and 10. On the Android 11 device, do the following: 1. Lock the device screen. 2. Attempt to unlock the screen and validate that the device autowipes after specified number of invalid entries. If the EMM console device policy is not set to the maximum number of consecutive failed authentication attempts at 10 or fewer, or if on the Android 11 device the device policy is not set to the maximum number of consecutive failed authentication attempts at 10 or fewer, this is a finding.

## Group: PP-MDF-301080

**Group ID:** `V-252855`

### Rule: Zebra Android 11 must be configured to enforce an application installation policy by specifying one or more authorized application repositories, including [selection: DoD-approved commercial app repository, EMM server, mobile application store].

**Rule ID:** `SV-252855r820492_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Forcing all applications to be installed from authorized application repositories can prevent unauthorized and malicious applications from being installed and executed on mobile devices. Allowing such installations and executions could cause a compromise of DoD data accessible by these unauthorized/malicious applications. SFR ID: FMT_SMF_EXT.1.1 #8a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Zebra Android device configuration settings to determine if the mobile device has only approved application repositories (DoD-approved commercial app repository, EMM server, and/or mobile application store). This validation procedure is performed on both the EMM Administration Console and the Android 11 device. On the EMM Console: 1. Open "Set user restrictions". 2. Verify that "Disallow install unknown sources" is toggled to "On". 3. Verify that "Disallow installs from unknown sources globally" is toggled to "On". On the Zebra device, do the following: 1. Open Settings >> Apps and notifications >> Advanced >> Special app access. 2. Open Install unknown apps. 3. Ensure the list of apps is blank or if an app is on the list, "Disabled by admin" is listed under the app name. If the EMM console device policy is not set to allow connections to "Only approved application repositories" or on the Android 11 device, the device policy is not set to allow connections to "Only approved application repositories, this is a finding.

## Group: PP-MDF-301090

**Group ID:** `V-252856`

### Rule: Zebra Android 11 must be configured to enforce an application installation policy by specifying an application allow list that restricts applications by the following characteristics: [selection: list of digital signatures, cryptographic hash values, names, application version].

**Rule ID:** `SV-252856r820495_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The application allow list, in addition to controlling the installation of applications on the MD, must control user access/execution of all core and preinstalled applications, or the MD must provide an alternate method of restricting user access/execution to core and pre-installed applications. Core application: Any application integrated into the OS by the OS or MD vendors. Pre-installed application: Additional non-core applications included in the OS build by the OS vendor, MD vendor, or wireless carrier. Requiring all authorized applications to be in an application allow list prevents the execution of any applications (e.g., unauthorized, malicious) that are not part of the allow list. Failure to configure an application allow list properly could allow unauthorized and malicious applications to be downloaded, installed, and executed on the mobile device, causing a compromise of DoD data accessible by these applications. The application allow list, in addition to controlling the installation of applications on the MD, must control user access/execution of all core applications (included in the OS by the OS vendor) and pre-installed applications (provided by the MD vendor and wireless carrier), or the MD must provide an alternate method of restricting user access/execution to core and pre-installed applications. SFR ID: FMT_SMF_EXT.1.1 #8b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Zebra Android device configuration settings to determine if the mobile device has an application allow list configured. Verify all applications listed on the allow list have been approved by the Approving Official (AO). On the EMM console, do the following: 1. Go to the Android app catalog for managed Google Play. 2. Verify all selected apps are AO approved. On the Android 11 device, do the following: 1. Open the managed Google Play store. 2. Verify that only the approved apps are visible. Note: Managed Google Play is an allowed App Store. If the EMM console list of selected Managed Google Play apps includes non-approved apps, this is a finding. Note: The application allow list will include approved core applications (included in the OS by the OS vendor) and pre-installed applications (provided by the MD vendor and wireless carrier), or the MD must provide an alternate method of restricting user access/execution to core and pre-installed applications. For Zebra Android, there are no pre-installed applications.

## Group: PP-MDF-301100

**Group ID:** `V-252857`

### Rule: Zebra Android 11 allow list must be configured to not include applications with the following characteristics: 

- back up MD data to non-DoD cloud servers (including user and application access to cloud backup services);
- transmit MD diagnostic data to non-DoD servers;
- voice assistant application if available when MD is locked;
- voice dialing application if available when MD is locked;
- allows synchronization of data or applications between devices associated with user; and
- allows unencrypted (or encrypted but not FIPS 140-2 validated) data sharing with other MDs or printers.

**Rule ID:** `SV-252857r820498_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Requiring all authorized applications to be in an application allow list prevents the execution of any applications (e.g., unauthorized, malicious) that are not part of the allow list. Failure to configure an application allow list properly could allow unauthorized and malicious applications to be downloaded, installed, and executed on the mobile device, causing a compromise of DoD data accessible by these applications. Applications with the listed characteristics have features that can cause the compromise of sensitive DoD data or have features with no known application in the DoD environment. Application Note: The application allow list, in addition to controlling the installation of applications on the MD, must control user access/execution of all core and preinstalled applications, or the MD must provide an alternate method of restricting user access/execution to core and pre-installed applications. Core application: Any application integrated into the OS by the OS or MD vendors. Pre-installed application: Additional non-core applications included in the OS build by the OS vendor, MD vendor, or wireless carrier. SFR ID: FMT_SMF_EXT.1.1 #8b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Zebra Android device configuration settings to determine if the mobile device has an application allow list configured and that the application allow list does not include applications with the following characteristics: - back up MD data to non-DoD cloud servers (including user and application access to cloud backup services); - transmit MD diagnostic data to non-DoD servers; - voice assistant application if available when MD is locked; - voice dialing application if available when MD is locked; - allows synchronization of data or applications between devices associated with user; - payment processing; and - allows unencrypted (or encrypted but not FIPS 140-2 validated) data sharing with other MDs, display screens (screen mirroring), or printers. This validation procedure is performed only on the EMM Administration Console. On the EMM console, do the following: 1. Review the list of selected Managed Google Play apps. 2. Review the details and privacy policy of each selected app to ensure the app does not include prohibited characteristics. If the EMM console device policy includes applications with unauthorized characteristics, this is a finding.

## Group: PP-MDF-301110

**Group ID:** `V-252858`

### Rule: Zebra Android 11 must be configured to disable Bluetooth or configured via User Based Enforcement (UBE) to allow Bluetooth for only Headset Profile (HSP), HandsFree Profile (HFP), and Serial Port Profile (SPP).

**Rule ID:** `SV-252858r820501_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Some Bluetooth profiles provide the capability for remote transfer of sensitive DoD data without encryption or otherwise do not meet DoD IT security policies and therefore should be disabled. SFR ID: FMT_SMF_EXT.1.1 #18h</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the AO has approved the use of Bluetooth at the site. If the AO has not approved the use of Bluetooth, verify Bluetooth has been disabled: On the EMM console, do the following: 1. Open "User restrictions on parent" section. 2. Verify that "Disallow Bluetooth" is toggled to "On". On the Android 11 device, do the following: 1. Go to Settings >> Connected Devices >> Connection Preferences >> Bluetooth. 2. Ensure that it is set to "Off" and cannot be toggled to "On". If the AO has approved the use of Bluetooth, on the Zebra Android 11 device do the following: 1. Go to Settings >> Connected Devices. 2. Verify only approved Bluetooth connected devices using approved profiles are listed. If the AO has not approved the use of Bluetooth, and Bluetooth use is not disabled via an EMM-managed device policy, this is a finding. If the AO has approved the use of Bluetooth, and Bluetooth devices using unauthorized Bluetooth profiles are listed on the device under "Connected devices", this is a finding.

## Group: PP-MDF-301120

**Group ID:** `V-252859`

### Rule: Zebra Android 11 must be configured to not display the following (work profile) notifications when the device is locked: [selection:

- email notifications 
- calendar appointments 
- contact associated with phone call notification 
- text message notification
- other application-based notifications
- all notifications].

**Rule ID:** `SV-252859r820504_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Many mobile devices display notifications on the lock screen so that users can obtain relevant information in a timely manner without having to frequently unlock the phone to determine if there are new notifications. However, in many cases, these notifications can contain sensitive information. When they are available on the lock screen, an adversary can see them merely by being in close physical proximity to the device. Configuring the Zebra Android device to not send notifications to the lock screen mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #19</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Zebra Android device settings to determine if the Zebra Android device displays (work container) notifications on the lock screen. Notifications of incoming phone calls are acceptable even when the device is locked. This validation procedure is performed on both the EMM Administration Console and the Android 11 device. On the EMM console, do the following: 1. Open "Lock screen restrictions" section. 2. Select "Work Profile". 3. Verify that "Disable Unredacted Notifications" is toggled to "On". On the Android 11 device, do the following: 1. Go to Settings >> Display >> Advanced. 2. Tap on Lock screen display. 3. Ensure "Hide sensitive work content" is listed under "When work profile is locked". If the EMM console device policy allows work notifications on the lock screen, or the Android 11 device allows work notifications on the lock screen, this is a finding.

## Group: PP-MDF-301150

**Group ID:** `V-252860`

### Rule: Zebra Android 11 must be configured to disable trust agents.

**Rule ID:** `SV-252860r820507_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Trust agents allow a user to unlock a mobile device without entering a passcode when the mobile device is, for example, connected to a user-selected Bluetooth device or in a user-selected location. This technology would allow unauthorized users to have access to DoD sensitive data if compromised. By not permitting the use of non-password authentication mechanisms, users are forced to use passcodes that meet DoD passcode requirements. SFR ID: FMT_SMF_EXT.1.1 #23, FIA_UAU.5.1</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review device configuration settings to confirm that trust agents are disabled. This procedure is performed on both the EMM Administration console and the Zebra Android 11 device. On the EMM console: 1. Open "Lock screen restrictions" section. 2. Select "Personal Profile". 3. Verify that "Disable trust agents" is toggled to "On". 4. Select "Work Profile". 5. Verify that "Disable trust agents" is toggled to "On". On the Zebra Android 11 device: 1. Open "Settings". 2. Tap "Security". 3. Tap "Advanced". 4. Tap "Trust agents". 5. Verify that all listed trust agents are disabled and cannot be enabled. If on the EMM console "disable trust agents" is not selected, or on the Android 11 device a trust agent can be enabled, this is a finding.

## Group: PP-MDF-301170

**Group ID:** `V-252861`

### Rule: Zebra Android 11 must be configured to disable developer modes.

**Rule ID:** `SV-252861r820510_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Developer modes expose features of the Zebra Android device that are not available during standard operation. An adversary may leverage a vulnerability inherent in a developer mode to compromise the confidentiality, integrity, and availability of DoD sensitive information. Disabling developer modes mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #26</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Zebra Android device configuration settings to determine whether a developer mode is enabled. This validation procedure is performed on both the EMM Administration Console and the Android 11 device. On the EMM Console: 1. Open "Set user restrictions" section. 2. Verify that "Disallow debugging features" is toggled to "On". 3. Open "Set user restrictions on parent" section. 4. Verify that "Disallow debugging features" is toggled to "On". On the Android 11 device, do the following: 1. Go to Settings >> System. 2. Ensure "Developer Options" is not listed. 3. Go to Settings >> About Phone. 4. Tap on the "Build Number" to try to enable "Developer Options" and validate that action is blocked. If the EMM console device policy is not set to disable developer mode or on the Android 11 device, the device policy is not set to disable developer mode, this is a finding.

## Group: PP-MDF-301200

**Group ID:** `V-252862`

### Rule: Zebra Android 11 must be configured to display the DoD advisory warning message at start-up or each time the user unlocks the device.

**Rule ID:** `SV-252862r820513_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Zebra Android 11 is required to display the DoD-approved system use notification message or banner before granting access to the system that provides privacy and security notices consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. Required banners help ensure that DoD can audit and monitor the activities of mobile device users without legal restriction. System use notification messages can be displayed when individuals first access or unlock the mobile device. The banner must be implemented as a "click-through" banner at device unlock (to the extent permitted by the operating system). A "click-through" banner prevents further activity on the information system unless and until the user executes a positive action to manifest agreement by clicking on a box indicating "OK." The approved DoD text must be used exactly as required in the KS referenced in DoDI 8500.01. For devices accommodating banners of 1300 characters, the banner text is: You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. For devices with severe character limitations, the banner text is: I've read & consent to terms in IS user agreem't. The administrator must configure the banner text exactly as written without any changes. SFR ID: FMT_SMF_EXT.1.1 #36</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The DoD warning banner can be displayed by either of the following methods (required text is found in the Vulnerability Discussion): 1. By placing the DoD warning banner text in the user agreement signed by each Zebra Android device user (preferred method). 2. By configuring the warning banner text on the EMM console and installing the banner on each managed mobile device. Determine which method is used at the Zebra Android device site and follow the appropriate validation procedure below. Validation Procedure for Method #1: Review the signed user agreements for several Zebra Android device users and verify the agreement includes the required DoD warning banner text. Validation Procedure for Method #2: On the EMM Console: 1. Open "Lock screen restrictions". 2. Select "Personal Profile". 3. Select "Lock screen message". 4. Verify message. If, for Method #1, the required warning banner text is not on all signed user agreements reviewed, or for Method #2, the EMM console device policy is not set to display a warning banner with the appropriate designated wording or on the Android 11 device, the device policy is not set to display a warning banner with the appropriate designated wording, this is a finding.

## Group: PP-MDF-301210

**Group ID:** `V-252863`

### Rule: Zebra Android 11 must be configured to disable USB mass storage mode.

**Rule ID:** `SV-252863r820516_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>USB mass storage mode enables the transfer of data and software from one device to another. This software can include malware. When USB mass storage is enabled on a mobile device, it becomes a potential vector for malware and unauthorized data exfiltration. Prohibiting USB mass storage mode mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #39a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Zebra Android device configuration settings to determine if the mobile device has a USB mass storage mode and whether it has been disabled. This validation procedure is performed on both the EMM Administration Console and the Android 11 device. On the EMM console, do the following: 1. Open "User restrictions on parent". 2. Verify that "Disallow USB file transfer" is toggled to "On". On the Android 11 device, do the following: 1. Plug a USB cable into Android 11 device and connect to a non-DoD network-managed PC. 2. Go to Settings >> Connected devices >> USB. 3. Ensure "No data transfer" is selected. If the EMM console device policy is not set to disable USB mass storage mode or on the Android 11 device, the device policy is not set to disable USB mass storage mode, this is a finding.

## Group: PP-MDF-301220

**Group ID:** `V-252864`

### Rule: Zebra Android 11 must be configured to not allow backup of [all applications, configuration data] to locally connected systems.

**Rule ID:** `SV-252864r820519_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data on mobile devices is protected by numerous mechanisms, including user authentication, access control, and cryptography. When the data is backed up to an external system (either locally connected or cloud-based), many if not all of these mechanisms are no longer present. This leaves backed-up data vulnerable to attack. Disabling backup to external systems mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #40</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Zebra Android device configuration settings to determine if the capability to back up to a locally connected system has been disabled. This validation procedure is performed on both the EMM Administration Console and the Android 11 device. On the EMM console, do the following: 1. Open "Device owner management" section. 2. Verify that "Enable backup service" is toggled to "Off". 3. Open "User restrictions on parent". 4. Verify that "Disallow USB file transfer" is toggled to "On". On the Android 11 device, do the following: 1. Plug a USB cable into Android 11 device and connect to a non-DoD network-managed PC. 2. Go to Settings >> Connected devices >> USB. 3. Ensure “No data transfer” is selected. If the EMM console device policy is not set to disable the capability to back up to a locally connected system or on the Android 11 device, the device policy is not set to disable the capability to back up to a locally connected system, this is a finding.

## Group: PP-MDF-301230

**Group ID:** `V-252865`

### Rule: Zebra Android 11 must be configured to not allow backup of all applications and configuration data to remote systems.

**Rule ID:** `SV-252865r820522_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Backups to remote systems (including cloud backup) can leave data vulnerable to breach on the external systems, which often offer less protection than the Zebra Android device. Where the remote backup involves a cloud-based solution, the backup capability is often used to synchronize data across multiple devices. In this case, DoD devices may synchronize DoD sensitive information to a user's personal device or other unauthorized computers that are vulnerable to breach. Disallowing remote backup mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #40</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Zebra Android device configuration settings to determine if the capability to back up to a remote system has been disabled. This validation procedure is performed on both the EMM Administration Console and the Android 11 device. On the EMM console, do the following: 1. Open "User restrictions". 2. Verify that "Disallow backup service" is toggled to "Off". On the Android 11 device, do the following: 1. Go to Settings >> System. 2. Ensure Backup is set to "Off". If the EMM console device policy is not set to disable the capability to back up to a remote system or on the Android 11 device, the device policy is not set to disable the capability to back up to a remote system, this is a finding.

## Group: PP-MDF-301280

**Group ID:** `V-252866`

### Rule: Zebra Android 11 must be configured to disable multi-user modes.

**Rule ID:** `SV-252866r820525_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Multi-user mode allows multiple users to share a mobile device by providing a degree of separation between user data. To date, no mobile device with multi-user mode features meets DoD requirements for access control, data separation, and non-repudiation for user accounts. In addition, the MDFPP does not include design requirements for multi-user account services. Disabling multi-user mode mitigates the risk of not meeting DoD multi-user account security policies. SFR ID: FMT_SMF_EXT.1.1 #47b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review documentation on the Zebra Android device and inspect the configuration on the Zebra Android device to disable multi-user modes. This validation procedure is performed on both the EMM Administration Console and the Android 11 device. On the EMM console, do the following: 1. Open "Set user restrictions". 2. Verify that "Disallow modify accounts" is toggled to "On". On the Android 11 device, do the following: 1. Go to Settings >> Accounts>> Work. 2. Validate that "Add Account" is grayed out. If the EMM console device policy is not set to disable multi-user modes or on the Android 11 device, the device policy is not set to disable multi-user modes, this is a finding.

## Group: PP-MDF-302340

**Group ID:** `V-252867`

### Rule: Zebra Android 11 must allow only the Administrator (EMM) to perform the following management function: Enable/disable location services.

**Rule ID:** `SV-252867r820528_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If a user is able to configure the security setting, the user could inadvertently or maliciously set it to a value that poses unacceptable risk to DoD information systems. An adversary could exploit vulnerabilities created by the weaker configuration to compromise DoD sensitive information. SFR ID: FMT_MOF_EXT.1.2 #22</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Zebra Android device configuration settings to determine if the mobile device has location services on/off. This validation procedure is performed on both the EMM Administration Console and the Android 11 device. On the EMM console, do the following: 1. Open "Set user restrictions on parent". 2. Verify that "Disallow config location" is toggled to "On". 3. Verify that "Disallow share location" is toggled to "On". On the Zebra device, do the following: 1. Open Settings >> Location. 2. Validate that Location Services is "off" for Work. If the mobile device has location services enabled, this is a finding.

## Group: PP-MDF-302370

**Group ID:** `V-252868`

### Rule: Zebra Android 11 must be configured to enable audit logging.

**Rule ID:** `SV-252868r820531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit logs enable monitoring of security-relevant events and subsequent forensics when breaches occur. To be useful, Administrators must have the ability to view the audit logs. SFR ID: FMT_SMF_EXT.1.1 #32</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review documentation on the Zebra Android device and inspect the configuration on the Zebra Android device to enable audit logging. This validation procedure is performed on only on the EMM Administration Console. On the EMM console, do the following: 1. Open "Device owner management" section. 2. Verify that "Enable security logging" is toggled to "On". If the EMM console device policy is not set to enable audit logging, this is a finding.

## Group: PP-MDF-301420

**Group ID:** `V-252869`

### Rule: Zebra Android 11 must be configured to generate audit records for the following auditable events: Detected integrity violations.

**Rule ID:** `SV-252869r820534_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Audit logs enable monitoring of security-relevant events and subsequent forensics when breaches occur. They help identify attacks so that breaches can either be prevented or limited in their scope. They facilitate analysis to improve performance and security. The Requirement Statement lists key events that the system must generate an audit record for. Application Note: Requirement applies only to integrity violation detections that can be logged by the audit logging component. SFR ID: FMT_SMF_EXT.1.1 #37</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Zebra Android device configuration settings to determine if the mobile device is configured to generate audit records for the following auditable events: Detected integrity violations. This validation procedure is performed only on the EMM Administration Console. On the EMM console: 1. Open "Device owner management" section. 2. Verify that "Enable security logging" is toggled to "On". If the EMM console device policy is not set to enable security logging, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-252870`

### Rule: Zebra Android 11 users must complete required training.

**Rule ID:** `SV-252870r820537_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The security posture of Zebra devices requires the device user to configure several required policy rules on their device. User-Based Enforcement (UBE) is required for these controls. In addition, if the Authorizing Official (AO) has approved the use of an unmanaged personal space, the user must receive training on risks. If a user is not aware of their responsibilities and does not comply with UBE requirements, the security posture of the Zebra mobile device may become compromised and DoD sensitive data may become compromised. SFR ID: NA</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review a sample of site User Agreements for Zebra device users or similar training records and training course content. Verify that Zebra device users have completed the required training. The intent is that required training is renewed periodically in a time period determined by the AO. If any Zebra device user has not completed the required training, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-252871`

### Rule: Zebra Android 11 must be configured to enforce that Wi-Fi Sharing is disabled.

**Rule ID:** `SV-252871r820540_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Wi-Fi Sharing is an optional configuration of Wi-Fi Tethering/Mobile Hotspot, which allows the device to share its Wi-Fi connection with other wirelessly connected devices instead of its mobile (cellular) connection. Wi-Fi Sharing grants the "other" device access to a corporate Wi-Fi network and may possibly bypass the network access control mechanisms. This risk can be partially mitigated by requiring the use of a preshared key for personal hotspots. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review device configuration settings to confirm Wi-Fi Sharing is disabled. Mobile Hotspot must be enabled to enable Wi-Fi Sharing. If the Authorizing Official (AO) has not approved Mobile Hotspot, and it has been verified as disabled on the EMM console, no further action is needed. If Mobile Hotspot is being used, use the following procedure to verify Wi-Fi Sharing is disabled: On the EMM console: 1. Open "Set user restrictions on parent". 2. Verify that "Disallow config tethering" is toggled to "On". On the Zebra Android 11 device, do the following: 1. Open Settings. 2. Tap "Networks & internet". 3. Verify that "Hotspots & tethering" is disabled. If on the Zebra Android 11 device "Wi-Fi sharing" is enabled, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-252872`

### Rule: Zebra Android 11 must have the DoD root and intermediate PKI certificates installed.

**Rule ID:** `SV-252872r820543_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoD root and intermediate PKI certificates are used to verify the authenticity of PKI certificates of users and web services. If the root and intermediate certificates are not available, an adversary could falsely sign a certificate in such a way that it could not be detected. Providing access to the DoD root and intermediate PKI certificates greatly diminishes the risk of this attack. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review device configuration settings to confirm that the DoD root and intermediate PKI certificates are installed. This procedure is performed on both the EMM Administration console and the Zebra Android 11 device. The current DoD root and intermediate PKI certificates may be obtained in self-extracting zip files at http://cyber.mil/pki-pke (for NIPRNet). On the EMM console verify that the DoD root and intermediate certificates are part of a device and/or work profile that is being pushed down to the devices. On the Zebra Android 11 device, do the following: 1. Open "Settings". 2. Tap "Security". 3. Tap "Advanced". 4. Tap "Encryption & credentials". 5. Tap "Trusted credentials". 6. Verify that DoD root and intermediate PKI certificates are listed under the User tab in the Work section. If on the EMM console the DoD root and intermediate certificates are not listed in a profile, or the Zebra Android 11 device does not list the DoD root and intermediate certificates under the user tab, this is a finding.

## Group: PP-MDF-992000

**Group ID:** `V-252873`

### Rule: Zebra Android 11 must allow only the administrator (EMM) to install/remove DoD root and intermediate PKI certificates.

**Rule ID:** `SV-252873r820546_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoD root and intermediate PKI certificates are used to verify the authenticity of PKI certificates of users and web services. If the user is allowed to remove root and intermediate certificates, the user could allow an adversary to falsely sign a certificate in such a way that it could not be detected. Restricting the ability to remove DoD root and intermediate PKI certificates to the Administrator mitigates this risk. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration to confirm that the user is unable to remove DoD root and intermediate PKI certificates. On the EMM console: 1. Open "Set user restrictions". 2. Verify that "Disallow config credentials" is toggled to "On". On the Zebra Android 11 device, do the following: 1. Open "Settings". 2. Tap "Security". 3. Tap "Advanced". 4. Tap "Encryption & credentials". 5. Tap "Trusted credentials". 6. Verify that the user is unable to untrust or remove any work certificates. If on the Zebra Android 11 device the user is able to remove certificates, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-252874`

### Rule: Zebra Android 11 work profile must be configured to enforce the system application disable list.

**Rule ID:** `SV-252874r820549_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The system application disable list controls user access to/execution of all core and preinstalled applications. Core application: Any application integrated into Zebra Android 11 by Zebra. Preinstalled application: Additional noncore applications included in the Zebra Android 11 build by Google or the wireless carrier. Some system applications can compromise DoD data or upload users' information to non-DoD-approved servers. A user must be blocked from using such applications that exhibit behavior that can result in compromise of DoD data or DoD user information. The site administrator must analyze all preinstalled applications on the device and disable all applications not approved for DoD use by configuring the system application disable list. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Zebra Android 11 Work Profile configuration settings to confirm the system application disable list is enforced. This setting is enforced by default. Verify only approved system apps have been placed on the core allow list. This procedure is performed on the EMM Administrator console. Review the system app allow list and verify only approved apps are on the list. 1. Open "Apps management" section. 2. Select "Hide apps on parent". 3. Verify package names of apps. If on the EMM console the system app allow list contains unapproved core apps, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-252875`

### Rule: Zebra Android 11 work profile must be configured to disable automatic completion of work space internet browser text input.

**Rule ID:** `SV-252875r820552_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The autofill functionality in the web browser allows the user to complete a form that contains sensitive information, such as personally identifiable information (PII), without previous knowledge of the information. By allowing the use of autofill functionality, an adversary who learns a user's Zebra Android 11 device password, or who otherwise is able to unlock the device, may be able to further breach other systems by relying on the autofill feature to provide information unknown to the adversary. By disabling the autofill functionality, the risk of an adversary gaining further information about the device's user or compromising other systems is significantly mitigated. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Chrome Browser in Zebra Android 11 Work Profile autofill setting. This procedure is performed only on the EMM Administrator console. On the EMM console: 1. Open "Managed Configurations" section. 2. Select the Chrome Browser version from the work profile. 3.Verify that "SearchSuggestEnabled" is turned off. If on the EMM console autofill is set to "On" in the Chrome Browser Settings, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-252876`

### Rule: Zebra Android 11 Work Profile must be configured to disable the autofill services.

**Rule ID:** `SV-252876r820555_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The autofill services allow the user to complete text inputs that could contain sensitive information, such as personally identifiable information (PII), without previous knowledge of the information. By allowing the use of autofill services, an adversary who learns a user's Zebra Android 11 device password, or who otherwise is able to unlock the device, may be able to further breach other systems by relying on the autofill services to provide information unknown to the adversary. By disabling the autofill services, the risk of an adversary gaining further information about the device's user or compromising other systems is significantly mitigated. Examples of apps that offer autofill services include Samsung Pass, Google, Dashlane, LastPass, and 1Password. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Zebra Android 11 work profile configuration settings to confirm that autofill services are disabled. This procedure is performed only on the EMM Administration console. On the EMM console: 1. Open "Set user restrictions". 2. Verify that "Disable autofill" is toggled to "On". If on the EMM console "disallow autofill" is not selected, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-252877`

### Rule: Zebra Android 11 must be configured to disallow configuration of date and time.

**Rule ID:** `SV-252877r820558_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Determining the correct time a particular application event occurred on a system is critical when conducting forensic analysis and investigating system events. Periodically synchronizing internal clocks with an authoritative time source is necessary to correctly correlate the timing of events that occur across the enterprise. The three authoritative time sources for Zebra Android 11 are an authoritative time server that is synchronized with redundant United States Naval Observatory (USNO) time servers as designated for the appropriate DoD network (NIPRNet or SIPRNet), the Global Positioning System (GPS), or the wireless carrier. Time stamps generated by the audit system in Zebra Android 11 must include both date and time. The time may be expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Zebra Android 11 Work Profile configuration settings to confirm that autofill services are disabled. This procedure is performed on both the EMM Administration console and the Zebra Android 11 device. On the EMM console: 1. Open "Set user restrictions on parent". 2. Verify that "Disallow config date time" is toggled to "On". On the Zebra Android 11 device, do the following: 1. Open "Settings". 2. Tap "System". 3. Tap "Date & time". 4. Validate that "Use network-provided time" is grayed out. If on the EMM console "Disallow config date time" is not set to "On", or on the Zebra Android 11 device "User network-provided time" is not grayed out, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-252878`

### Rule: Zebra Android 11 devices must have the latest available Zebra Android 11 operating system installed.

**Rule ID:** `SV-252878r820561_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Required security features are not available in earlier operating system versions. In addition, there may be known vulnerabilities in earlier versions. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review device configuration settings to confirm the Zebra Android device has the most recently released version of Zebra Android 11 installed. This procedure is performed on both the EMM console and the Zebra Android 11 device. In the EMM management console, review the version of Zebra Android 11 installed on a sample of managed devices. This procedure will vary depending on the EMM product. On the Zebra Android 11 device, to see the installed operating system version: 1. Open "Settings". 2. Tap "About phone". 3. Verify "Build number". If the installed version of the Android operating system on any reviewed Zebra devices is not the latest released by Zebra, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-252879`

### Rule: Zebra Android 11 devices must be configured to disable the use of third-party keyboards.

**Rule ID:** `SV-252879r820564_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Many third-party keyboard applications are known to contain malware. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review device configuration settings to confirm that no third-party keyboards are enabled. This procedure is performed on the EMM console. On the EMM console, configure application allow list for Google Play that does not have any third-party keyboards. If third-party keyboards are allowed, this is a finding.

## Group: PP-MDF-991000

**Group ID:** `V-252880`

### Rule: Zebra Android 11 devices must be configured to enable Common Criteria Mode (CC Mode).

**Rule ID:** `SV-252880r820567_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The CC Mode feature is a superset of other features and behavioral changes that are mandatory MDFPP requirements. If CC mode is not implemented, the device will not be operating in the NIAP-certified compliant CC Mode of operation. CC Mode implements the following behavioral/functional changes: How the Bluetooth and Wi-Fi keys are stored using different types of encryption. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review device configuration settings to confirm CC mode is enabled. This procedure is performed on the EMM console. In the EMM management console, verify CC Mode has been enabled. If CC mode is not enabled, this is a finding.

