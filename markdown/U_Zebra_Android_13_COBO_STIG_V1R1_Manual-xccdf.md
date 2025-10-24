# STIG Benchmark: Zebra Android 13 COBO Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: PP-MDF-993300

**Group ID:** `V-270007`

### Rule: Zebra Android 13 must be configured to enable audit logging.

**Rule ID:** `SV-270007r1052761_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit logs enable monitoring of security-relevant events and subsequent forensics when breaches occur. To be useful, administrators must have the ability to view the audit logs. SFR ID: FMT_SMF_EXT.1.1 #32</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Inspect the configuration on the managed Zebra Android 13 device to enable audit logging. This validation procedure is performed only on the EMM Administration Console. On the EMM console: COBO and COPE: 1. Open the "Device owner management" section. 2. Verify "Enable security logging" is toggled to "ON". If the EMM console device policy is not set to enable audit logging, this is a finding.

## Group: PP-MDF-333024

**Group ID:** `V-270030`

### Rule: Zebra Android 13 must be configured to enforce a minimum password length of six characters.

**Rule ID:** `SV-270030r1052830_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password strength is a measure of the effectiveness of a password in resisting guessing and brute force attacks. The ability to crack a password is a function of how many attempts an adversary is permitted, how quickly an adversary can do each attempt, and the size of the password space. The longer the minimum length of the password is, the larger the password space. Having a too-short minimum password length significantly reduces password strength, increasing the chance of password compromise and resulting device and data compromise. SFR ID: FMT_SMF_EXT.1.1 #1a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Zebra Android 13 device configuration settings to determine if the mobile device is enforcing a minimum password length of six characters. This validation procedure is performed on both the EMM Administration Console and the managed Zebra Android 13 device. On the EMM console: COBO: 1. Open "Lock screen" settings. 2. Open "Password constraints". 3. Open "Minimum password quality". 4. Verify Numeric Complex, Alphabetic, Alphanumeric, or Complex is selected. 5. Open "Minimum password length". 6. Verify "6" is set for number of characters. COPE: 1. Open "Lock screen" settings. 2. Open "Password constraints". 3. Select "Personal Profile". 4. Verify "Minimum password quality" is set to Numeric Complex, Alphabetic, Alphanumeric, or Complex. 5. Open "Minimum password length". 6. Verify the number of characters is set to "6" or higher. _____________________________ On the managed Zebra Android 13 device: COBO and COPE: 1. Open Settings >> Security >> Screen lock. 2. Enter current password. 3. Tap "Pin or Password". 4. Verify Password length required is at least "6". If the device password length is not set to six characters or more on EMM console or on the managed Zebra Android 13 device, this is a finding.

## Group: PP-MDF-333025

**Group ID:** `V-270031`

### Rule: Zebra Android 13 must be configured to not allow passwords that include more than four repeating or sequential characters.

**Rule ID:** `SV-270031r1052833_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password strength is a measure of the effectiveness of a password in resisting guessing and brute force attacks. Passwords that contain repeating or sequential characters are significantly easier to guess than those that do not contain repeating or sequential characters. Therefore, disallowing repeating or sequential characters increases password strength and decreases risk. SFR ID: FMT_SMF_EXT.1.1 #1b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Zebra Android 13 device configuration settings to determine if the mobile device is prohibiting passwords with more than four repeating or sequential characters. This validation procedure is performed on both the EMM Administration Console and the managed Zebra Android 13 device. On the EMM console: COBO: 1. Open "Lock screen" settings. 2. Open "Password constraints". 3. Verify that quality is set to "Numeric (Complex)" or higher. COPE: 1. Open "Lock screen" settings. 2. Open "Password constraints". 3. Select "Personal Profile". 4. Verify that quality is set to "Numeric (Complex)" or higher. ____________________________ On the managed Zebra Android 13 device: COBO and COPE: 1. Open Settings >> Security >> Screen lock. 2. Enter current password. 3. Select "PIN". 4. Try to enter a new PIN with repeating numbers. 5. Verify Password complexity requirements are listed: Ascending, descending, or repeated sequence of digits is not allowed. If the EMM console device policy is set to a password with more than two repeating or sequential characters or on the managed Zebra Android 13 device, the device policy is set to a password with more than two repeating or sequential characters, this is a finding. Note: Alphabetic, Alphanumeric, and Complex are also acceptable selections, but these selections will cause the user to select a complex password, which is not required by the STIG.

## Group: PP-MDF-333030

**Group ID:** `V-270032`

### Rule: Zebra Android 13 must be configured to lock the display after 15 minutes (or less) of inactivity.

**Rule ID:** `SV-270032r1052836_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The screen lock timeout must be set to a value that helps protect the device from unauthorized access. Having a too-long timeout would increase the window of opportunity for adversaries who gain physical access to the mobile device through loss, theft, etc. Such devices are much more likely to be in an unlocked state when acquired by an adversary, thus granting immediate access to the data on the mobile device. The maximum timeout period of 15 minutes has been selected to balance functionality and security; shorter timeout periods may be appropriate depending on the risks posed to the mobile device. SFR ID: FMT_SMF_EXT.1.1 #2a, #2b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Zebra Android device configuration settings to determine if the mobile device is enforcing a screen-lock policy that will lock the display after a period of 15 minutes or less of inactivity. Note: Zebra Android 13 does not support the 15-minute increment. The available allowable selection is 10 mins then increases to 30 minutes. Therefore, the control should be set to 10 minutes. This validation procedure is performed on both the EMM Administration Console and the Android 13 device. On the EMM Console: COBO: 1. Open "Lock screen restrictions". 2. Verify that "Max time to screen lock" is set to "600". Note: The units are in seconds. COPE: 1. Open "Lock screen restrictions". 2. Select "Personal Profile". 3. Verify that "Max time to screen lock" is set to "600". Note: The units are in seconds. On the managed Zebra Android 13 device: COBO and COPE: 1. Open Settings >> Display. 2. Tap "Screen timeout". 3. Ensure the Screen timeout value is set to "600" seconds. If the EMM console device policy is not set to enable a screen-lock policy that will lock the display after a period of inactivity of 600 seconds, this is a finding.

## Group: PP-MDF-333040

**Group ID:** `V-270033`

### Rule: Zebra Android 13 must be configured to not allow more than 10 consecutive failed authentication attempts.

**Rule ID:** `SV-270033r1052839_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The more attempts an adversary has to guess a password, the more likely the adversary will enter the correct password and gain access to resources on the device. Setting a limit on the number of attempts mitigates this risk. Setting the limit at 10 or less gives authorized users the ability to make a few mistakes when entering the password but still provides adequate protection against dictionary or brute force attacks on the password. SFR ID: FMT_SMF_EXT.1.1 #2c, FIA_AFL_EXT.1.5</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Zebra Android 13 device configuration settings to determine if the mobile device has the maximum number of consecutive failed authentication attempts set at 10 or fewer. This validation procedure is performed on both the EMM Administration Console and the managed Zebra Android 13 device. On the EMM Console: COBO: 1. Open "Lock screen" settings. 2. Open "Lock screen restrictions". 3. Verify that "Max password failures for local wipe" is set to a number between 1 and 10. COPE: 1. Open "Lock screen" settings. 2. Open "Lock screen restrictions". 3. Select "Personal Profile". 4. Verify that "Max password failures for local wipe" is set to a number between 1 and 10. _________________________ On the managed Zebra Android 13 device: COBO and COPE: 1. Lock the device screen. 2. Attempt to unlock the screen and validate that the device autowipes after a specified number of invalid entries. Note: Perform this verification only with a test phone set up with a production profile. If the EMM console device policy is not set to the maximum number of consecutive failed authentication attempts at 10 or fewer, or if on the managed Zebra Android 13 device the device policy is not set to the maximum number of consecutive failed authentication attempts at 10 or fewer, this is a finding.

## Group: PP-MDF-333050

**Group ID:** `V-270034`

### Rule: Zebra Android 13 must be configured to enforce an application installation policy by specifying one or more authorized application repositories, including [selection: DOD-approved commercial app repository, MDM server, mobile application store].

**Rule ID:** `SV-270034r1052842_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Forcing all applications to be installed from authorized application repositories can prevent unauthorized and malicious applications from being installed and executed on mobile devices. Allowing such installations and executions could cause a compromise of DOD data accessible by these unauthorized/malicious applications. SFR ID: FMT_SMF_EXT.1.1 #8a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Zebra Android 13 device configuration settings to determine if the mobile device has only approved application repositories (DOD-approved commercial app repository, EMM server, and/or mobile application store). This validation procedure is performed on both the EMM Administration Console and the managed Zebra Android 13 device. On the EMM Console: COBO and COPE: 1. Open "Set user restrictions". 2. Verify that "Disallow install unknown sources" is toggled to "ON". 3. Verify that "Disallow installs from unknown sources globally" is toggled to "ON". On the Zebra Android 13 device: COBO and COPE: 1. Open Settings >> Apps >> Special app access. 2. Open "Install unknown apps". 3. Ensure the list of apps is blank or if an app is on the list, "Disabled by admin" is listed under the app name. If the EMM console device policy is not set to allow connections to only approved application repositories or on the managed Zebra Android 13 device, the device policy is not set to allow connections to only approved application repositories, this is a finding.

## Group: PP-MDF-333060

**Group ID:** `V-270035`

### Rule: Zebra Android 13 must be configured to enforce an application installation policy by specifying an application allowlist that restricts applications by the following characteristics: [selection: list of digital signatures, cryptographic hash values, names, application version].

**Rule ID:** `SV-270035r1053270_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The application allowlist, in addition to controlling the installation of applications on the MD, must control user access/execution of all core and preinstalled applications, or the MD must provide an alternate method of restricting user access/execution to core and preinstalled applications. Core application: Any application integrated into the OS by the OS or MD vendors. Preinstalled application: Additional noncore applications included in the OS build by the OS vendor, MD vendor, or wireless carrier. Requiring all authorized applications to be in an application allowlist prevents the execution of any applications (e.g., unauthorized, malicious) that are not part of the allowlist. Failure to configure an application allowlist properly could allow unauthorized and malicious applications to be downloaded, installed, and executed on the mobile device, causing a compromise of DOD data accessible by these applications. The application allowlist, in addition to controlling the installation of applications on the MD, must control user access/execution of all core applications (included in the OS by the OS vendor) and preinstalled applications (provided by the MD vendor and wireless carrier), or the MD must provide an alternate method of restricting user access/execution to core and preinstalled applications. SFR ID: FMT_SMF_EXT.1.1 #8b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Zebra Android 13 device configuration settings to determine if the mobile device has an application allowlist configured. Verify all applications listed on the allowlist have been approved by the authorizing official (AO). On the EMM console: COBO and COPE: 1. Go to the Android app catalog for managed Google Play. 2. Verify all selected apps are AO approved. On the managed Zebra Android 13 device: COBO and COPE: 1. Open the managed Google Play Store. 2. Verify that only the approved apps are visible. Note: Managed Google Play is an allowed App Store. If the EMM console list of selected managed Google Play apps includes nonapproved apps, this is a finding. Note: The application allowlist will include approved core applications (included in the OS by the OS vendor) and preinstalled applications (provided by the MD vendor and wireless carrier), or the MD must provide an alternate method of restricting user access/execution to core and pre-installed applications. For Zebra Android, there are no preinstalled applications.

## Group: PP-MDF-333070

**Group ID:** `V-270036`

### Rule: Zebra Android 13 allowlist must be configured to not include applications with the following characteristics: 

- Back up MD data to non-DOD cloud servers (including user and application access to cloud backup services);
- Transmit MD diagnostic data to non-DOD servers;
- Voice assistant application if available when MD is locked;
- Voice dialing application if available when MD is locked;
- Allows synchronization of data or applications between devices associated with user;
- Payment processing; and
- Allows unencrypted (or encrypted but not FIPS 140-2/140-3 validated) data sharing with other MDs, display screens (screen mirroring), or printers.

**Rule ID:** `SV-270036r1052848_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Requiring all authorized applications to be in an application allowlist prevents the execution of any applications (e.g., unauthorized, malicious) that are not part of the allowlist. Failure to configure an application allowlist properly could allow unauthorized and malicious applications to be downloaded, installed, and executed on the mobile device, causing a compromise of DOD data accessible by these applications. Applications with the listed characteristics have features that can cause the compromise of sensitive DOD data or have features with no known application in the DOD environment. Application Note: The application allowlist, in addition to controlling the installation of applications on the MD, must control user access/execution of all core and preinstalled applications, or the MD must provide an alternate method of restricting user access/execution to core and preinstalled applications. Core application: Any application integrated into the OS by the OS or MD vendors. Preinstalled application: Additional noncore applications included in the OS build by the OS vendor, MD vendor, or wireless carrier. SFR ID: FMT_SMF_EXT.1.1 #8b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Zebra Android 13 device configuration settings to determine if the mobile device has an application allowlist configured and that the application allowlist does not include applications with the following characteristics: - Back up MD data to non-DOD cloud servers (including user and application access to cloud backup services); - Transmit MD diagnostic data to non-DOD servers; - Voice assistant application if available when MD is locked; - Voice dialing application if available when MD is locked; - Allows synchronization of data or applications between devices associated with user; - Payment processing; and - Allows unencrypted (or encrypted but not FIPS 140-2/140-3 validated) data sharing with other MDs, display screens (screen mirroring), or printers. This validation procedure is performed only on the EMM Administration Console. On the EMM console: 1. Review the list of selected Managed Google Play apps. 2. Review the details and privacy policy of each selected app to ensure the app does not include prohibited characteristics. If the EMM console device policy includes applications with unauthorized characteristics, this is a finding.

## Group: PP-MDF-333080

**Group ID:** `V-270037`

### Rule: Zebra Android 13 must be configured to not display the following (work profile) notifications when the device is locked: [selection:

a. email notifications 
b. calendar appointments 
c. contact associated with phone call notification 
d. text message notification
e. other application-based notifications
f. all notifications].

**Rule ID:** `SV-270037r1052851_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Many mobile devices display notifications on the lock screen so that users can obtain relevant information in a timely manner without having to frequently unlock the phone to determine if there are new notifications. However, in many cases, these notifications can contain sensitive information. When they are available on the lock screen, an adversary can see them merely by being in close physical proximity to the device. Configuring the mobile operating system (MOS) to not send notifications to the lock screen mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #18</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Zebra Android 13 device settings to determine if the Zebra Android 13 device displays (work profile) notifications on the lock screen. Notifications of incoming phone calls are acceptable even when the device is locked. This validation procedure is performed on both the EMM Administration Console and the managed Zebra Android 13 device. On the EMM console: COBO: 1. Open "Lock screen" settings. 2. Open "Lock screen restrictions". 3. Verify that "Disable unredacted notifications" is toggled to "ON". COPE: 1. Open "Lock screen" settings. 2. Open "Lock screen restrictions". 3. Select "Work Profile". 4. Verify that "Disable unredacted notifications" is toggled to "ON". ___________________________ On the managed Zebra Android 13 device: COBO: 1. Go to Settings >> Display >> Lock screen. 2. Tap on "Privacy". 3. Verify that "Show sensitive content only when unlocked" is selected. COPE: 1. Go to Settings >> Display >> Lock screen. 2. Tap on "When work profile is locked". 3. Verify that "Hide sensitive work content" is selected. If the EMM console device policy allows work notifications on the lock screen, or the managed Zebra Android 13 device allows work notifications on the lock screen, this is a finding.

## Group: PP-MDF-333110

**Group ID:** `V-270041`

### Rule: Zebra Android 13 must be configured to disable trust agents.

**Rule ID:** `SV-270041r1052863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Trust agents allow a user to unlock a mobile device without entering a passcode when the mobile device is, for example, connected to a user-selected Bluetooth device or in a user-selected location. This technology would allow unauthorized users to have access to DOD sensitive data if compromised. By not permitting the use of nonpassword authentication mechanisms, users are forced to use passcodes that meet DOD passcode requirements. SFR ID: FMT_SMF_EXT.1.1 #22, FIA_UAU.5.1</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review device configuration settings to confirm that trust agents are disabled. This procedure is performed on both the EMM Administration console and the managed Zebra Android 13 device. On the EMM console: COBO: 1. Open "Lock screen restrictions". 2. Verify "Disable trust agents" is toggled to "ON". COPE: 1. Open "Lock screen restrictions". 2. Select "Personal Profile". 3. Verify "Disable trust agents" is toggled to "ON". 4. Select "Work Profile". 5. Verify "Disable trust agents" is toggled to "ON". ____________________________ On the managed Zebra Android 13 device: COBO and COPE: 1. Open Settings. 2. Tap "Security". 3. Tap "Advanced". 4. Tap "Trust agents". 5. Verify all listed trust agents are disabled and cannot be enabled. If on the EMM console, "disable trust agents" is not selected, or on the managed Zebra Android 13 device a trust agent can be enabled, this is a finding.

## Group: PP-MDF-333130

**Group ID:** `V-270043`

### Rule: Zebra Android 13 must be configured to disable developer modes.

**Rule ID:** `SV-270043r1052869_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Developer modes expose features of the mobile operating system (MOS) that are not available during standard operation. An adversary may leverage a vulnerability inherent in a developer mode to compromise the confidentiality, integrity, and availability of DOD sensitive information. Disabling developer modes mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #26</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Zebra Android 13 device configuration settings to determine whether a developer mode is enabled. This validation procedure is performed on both the EMM Administration Console and the managed Zebra Android 13 device. On the EMM Console: COBO: 1. Open "Set user restrictions". 2. Verify "Disallow debugging features" is toggled to "ON". COPE: 1. Open "Set user restrictions". 2. Verify "Disallow debugging features" is toggled to "ON". 3. Open "Set user restrictions on parent". 4. Verify "Disallow debugging features" is toggled to "ON". ____________________________ On the managed Zebra Android 13 device: COBO and COPE: 1. Go to Settings >> System. 2. Ensure "Developer Options" is not listed. 3. Go to Settings >> About Phone. 4. Tap on the Build Number to try to enable Developer Options and validate the action is blocked. If the EMM console device policy is not set to disable developer mode or on the managed Zebra Android 13 device, the device policy is not set to disable developer mode, this is a finding.

## Group: PP-MDF-333160

**Group ID:** `V-270046`

### Rule: Zebra Android 13 must be configured to display the DOD advisory warning message at startup or each time the user unlocks the device.

**Rule ID:** `SV-270046r1052878_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Before granting access to the system, the mobile operating system is required to display the DOD-approved system use notification message or banner that provides privacy and security notices consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. Required banners help ensure that DOD can audit and monitor the activities of mobile device users without legal restriction. System use notification messages can be displayed when individuals first access or unlock the mobile device. The banner must be implemented as a "click-through" banner at device unlock (to the extent permitted by the operating system). A "click-through" banner prevents further activity on the information system unless and until the user executes a positive action to manifest agreement by clicking on a box indicating "OK." The approved DOD text must be used exactly as required in the Knowledge Service referenced in DODI 8500.01. For devices accommodating banners of 1300 characters, the banner text is: You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. For devices with severe character limitations, the banner text is: I've read & consent to terms in IS user agreem't. The administrator must configure the banner text exactly as written without any changes. SFR ID: FMT_SMF_EXT.1.1 #36</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The DOD warning banner can be displayed by either of the following methods (required text is found in the Vulnerability Discussion): 1. By placing the DOD warning banner text in the user agreement signed by each managed Android 13 device user (preferred method). 2. By configuring the warning banner text on the EMM console and installing the banner on each managed Android 13 mobile device. Determine which method is used at the Zebra Android 13 device site and follow the appropriate validation procedure below. Validation Procedure for Method #1: Review the signed user agreements for several Zebra Android 13 device users and verify the agreement includes the required DOD warning banner text. Validation Procedure for Method #2: On the EMM Console: COBO: 1. Open "Lock screen restrictions". 2. Select "Lock screen message". 3. Verify the message. COPE: 1. Open "Lock screen restrictions". 2. Select "Personal Profile". 3. Select "Lock screen message". 4. Verify the message. If, for Method #1, the required warning banner text is not on all signed user agreements reviewed, or for Method #2, the EMM console device policy is not set to display a warning banner with the appropriate designated wording or on the managed Zebra Android 13 device, the device policy is not set to display a warning banner with the appropriate designated wording, this is a finding.

## Group: PP-MDF-333170

**Group ID:** `V-270047`

### Rule: Zebra Android 13 must be configured to generate audit records for the following auditable events: Detected integrity violations.

**Rule ID:** `SV-270047r1052881_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit logs enable monitoring of security-relevant events and subsequent forensics when breaches occur. They help identify attacks so that breaches can be prevented or limited in their scope. They facilitate analysis to improve performance and security. The Requirement Statement lists key events for which the system must generate an audit record. Note: This requirement applies only to integrity violation detections that can be logged by the audit logging component. SFR ID: FMT_SMF_EXT.1.1 #37, FAU_GEN.1.1 #6 (FPT_TST_EXT.2/PREKERNAL)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Zebra Android 13 device configuration settings to determine if the mobile device is configured to generate audit records for the following auditable events: Detected integrity violations. This validation procedure is performed only on the EMM Administration Console. On the EMM console: COBO and COPE: 1. Open "Device owner management" section. 2. Verify that "Enable security logging" is toggled to "ON". If the EMM console device policy is not set to enable security logging, this is a finding.

## Group: PP-MDF-333230

**Group ID:** `V-270051`

### Rule: Zebra Android 13 must be configured to disable USB mass storage mode.

**Rule ID:** `SV-270051r1052893_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>USB mass storage mode enables the transfer of data and software from one device to another. This software can include malware. When USB mass storage is enabled on a mobile device, it becomes a potential vector for malware and unauthorized data exfiltration. Prohibiting USB mass storage mode mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #39</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Zebra Android 13 device configuration settings to determine if the mobile device has a USB mass storage mode and whether it has been disabled. This validation procedure is performed on both the EMM Administration Console and the managed Zebra Android 13 device. On the EMM console: COBO: 1. Open "User restrictions". 2. Open "Set user restrictions". 3. Verify that "Disallow USB file transfer" is toggled to "ON". COPE: 1. Open "User restrictions". 2. Open "Set user restrictions on parent". 3. Verify "Disallow USB file transfer" is toggled to "ON". ______________________________ On the managed Zebra Android 13 device: 1. Plug a USB cable into the managed Zebra Android 13 device and connect to a non-DOD network-managed PC. 2. Go to Settings >> Connected devices >> USB. 3. Verify "No data transfer" is selected. If the EMM console device policy is not set to disable USB mass storage mode or on the managed Zebra Android 13 device, the device policy is not set to disable USB mass storage mode, this is a finding.

## Group: PP-MDF-333240

**Group ID:** `V-270052`

### Rule: Zebra Android 13 must be configured to not allow backup of [all applications, configuration data] to locally connected systems.

**Rule ID:** `SV-270052r1052896_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data on mobile devices is protected by numerous mechanisms, including user authentication, access control, and cryptography. When the data is backed up to an external system (either locally connected or cloud based), many if not all of these mechanisms are no longer present. This leaves the backed-up data vulnerable to attack. Disabling backup to external systems mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #40</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Zebra Android 13 device configuration settings to determine if the capability to back up to a locally connected system has been disabled. This validation procedure is performed on both the EMM Administration Console and the managed Zebra Android 13 device. On the EMM console: COBO and COPE: 1. Open "Device owner management". 2. Verify "Enable backup service" is toggled to "OFF". On the managed Zebra Android 13 device: COBO: 1. Go to Settings >> System >> Backup. 2. Verify Backup settings is "Not available". COPE: 1. Go to Settings >> System >> Backup. 2. Select "Work". 3. Verify Backup settings is "Not available". If the EMM console device policy is not set to disable the capability to back up to a locally connected system or on the managed Zebra Android 13 device, the device policy is not set to disable the capability to back up to a locally connected system, and this is a finding.

## Group: PP-MDF-333250

**Group ID:** `V-270053`

### Rule: Zebra Android 13 must be configured to not allow backup of [all applications, configuration data] to remote systems.

**Rule ID:** `SV-270053r1052899_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Backups to remote systems (including cloud backup) can leave data vulnerable to breach on the external systems, which often offer less protection than the mobile operating system (MOS). Where the remote backup involves a cloud-based solution, the backup capability is often used to synchronize data across multiple devices. In this case, DOD devices may synchronize DOD sensitive information to a user's personal device or other unauthorized computers that are vulnerable to breach. Disallowing remote backup mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #40</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Zebra Android 13 device configuration settings to determine if the capability to back up to a remote system has been disabled. Note: Since personal accounts cannot be added to the work profile (ZEBR-13-009800), this control only impacts personal profile accounts. Site can allow backup based on local policy. This validation procedure is performed on both the EMM Administration Console and the managed Zebra Android 13 device. On the EMM console: COBO and COPE: 1. Open "Device owner management". 2. Verify "Enable backup service" is toggled to "OFF". On the managed Zebra Android 13 device: COBO: 1. Go to Settings >> System >> System >> Backup. 2. Verify Backup settings is "Not available". COPE: 1. Go to Settings >> System >> System >> Backup. 2. Select "Work". 3. Verify Backup settings is "Not available". If the EMM console device policy is not set to disable the capability to back up to a remote system or on the managed Zebra Android 13 device, the device policy is not set to disable the capability to back up to a remote system, this is a finding.

## Group: PP-MDF-333260

**Group ID:** `V-270054`

### Rule: Zebra Android 13 must be configured to enable authentication of personal hotspot connections to the device using a pre-shared key.

**Rule ID:** `SV-270054r1052902_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If no authentication is required to establish personal hotspot connections, an adversary may be able to use that device to perform attacks on other devices or networks without detection. A sophisticated adversary may also be able to exploit unknown system vulnerabilities to access information and computing resources on the device. Requiring authentication to establish personal hotspot connections mitigates this risk. Application note: If hotspot functionality is permitted, it must be authenticated via a pre-shared key. There is no requirement to enable hotspot functionality, and it is recommended this functionality be disabled by default. SFR ID: FMT_SMF_EXT.1.1 #41</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is a User-Based Enforcement (UBE) control. Check a sample of Pixel phones at the site and verify the Wi-Fi hotspot pre-shared key (password) is set to "WPA2/WPA3-Personal" or "WPA3-Personal". 1. Go to Settings >> Network & Internet >> Hotspot & tethering. 2. Enable "Wi-Fi hotspot". 3. On the left of the slide, tap "Wi-Fi Hotspot" to bring up the configuration options. 4. Click the "Security" link and verify either "WPA2/WPA3-Personal" or "WPA3-Personal" is selected. If the Wi-Fi hotspot security is not set to "WPA2/WPA3-Personal" or "WPA3-Personal", this is a finding.

## Group: PP-MDF-333280

**Group ID:** `V-270055`

### Rule: Zebra Android 13 must be configured to disable exceptions to the access control policy that prevent [selection: application processes, groups of application processes] from accessing [selection: all, private] data stored by other [selection: application processes, groups of application processes].

**Rule ID:** `SV-270055r1052905_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>App data sharing gives apps the ability to access the data of other apps for enhanced user functionality. However, sharing also poses a significant risk that unauthorized users or apps will obtain access to DOD sensitive information. To mitigate this risk, there are data sharing restrictions, primarily from sharing data from personal (unmanaged) apps and work (managed) apps. If a user is allowed to make exceptions to the data sharing restriction policy, the user could enable unauthorized sharing of data, leaving it vulnerable to breach. Limiting the granting of exceptions to either the Administrator or common application developer mitigates this risk. Copy/paste of data between applications in different application processes or groups of application processes is considered an exception to the access control policy and therefore, the Administrator must be able to enable/disable the feature. Other exceptions include allowing any data or application sharing between process groups. SFR ID: FMT_SMF_EXT.1.1 #42, FDP_ACF_EXT.1.2</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review documentation on the managed Zebra Android 13 device and inspect the configuration on the Zebra Android device to verify the access control policy that prevents [selection: application processes] from accessing [selection: all] data stored by other [selection: application processes] is enabled. This validation procedure is performed only on the EMM Administration Console. On the EMM console: COPE: 1. Open "User restrictions". 2. Open "Set user restrictions". 3. Verify "Disallow cross profile copy/paste" is toggled to "ON". 4. Verify "Disallow sharing data into the profile" is toggled to "ON". If the EMM console device policy is not set to disable data sharing between profiles, this is a finding.

## Group: PP-MDF-333290

**Group ID:** `V-270056`

### Rule: Zebra Android 13 must be configured to disable multiuser modes.

**Rule ID:** `SV-270056r1052908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Multiuser mode allows multiple users to share a mobile device by providing a degree of separation between user data. To date, no mobile device with multiuser mode features meets DOD requirements for access control, data separation, and nonrepudiation for user accounts. In addition, the MDFPP does not include design requirements for multiuser account services. Disabling multiuser mode mitigates the risk of not meeting DOD multiuser account security policies. SFR ID: FMT_SMF_EXT.1.1 #47a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review documentation on the managed Zebra Android 13 device and inspect the configuration on the Zebra Android device to disable multiuser modes. This validation procedure is performed on both the EMM Administration Console and the managed Zebra Android 13 device. On the EMM console: COBO and COPE: 1. Open "User restrictions". 2. Open "Set user restrictions". 3. Verify "Disallow modify accounts" is toggled to "ON". On the managed Zebra Android 13 device: COBO and COPE: 1. Go to Settings >> Passwords & Accounts >> Accounts for Owner. 2. Tap "Add account". 3. Verify the action is not allowed. If the EMM console device policy is not set to disable multi-user modes or on the managed Zebra Android 13 device, the device policy is not set to disable multi-user modes, this is a finding.

## Group: PP-MDF-333320

**Group ID:** `V-270060`

### Rule: Zebra Android 13 must be configured to disable Bluetooth or configured via User Based Enforcement (UBE) to allow Bluetooth for only Headset Profile (HSP), Hands-Free Profile (HFP), and Serial Port Profile (SPP).

**Rule ID:** `SV-270060r1052920_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Some Bluetooth profiles provide the capability for remote transfer of sensitive DOD data without encryption or otherwise do not meet DOD IT security policies and therefore must be disabled. SFR ID: FMT_SMF_EXT.1.1/BLUETOOTH BT-8</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the authorizing official (AO) has approved the use of Bluetooth at the site. If the AO has not approved the use of Bluetooth, verify Bluetooth has been disabled. On the EMM console: COBO: 1. Open "User restrictions" section. 2. Verify "Disallow Bluetooth" is toggled to "ON". COPE: 1. Open "User restrictions on parent" section. 2. Verify "Disallow Bluetooth" is toggled to "ON". On the managed Zebra Android 13 device: COBO and COPE: 1. Go to Settings >> Connected Devices >> Connection Preferences >> Bluetooth. 2. Verify "Use Bluetooth" is set to OFF and cannot be toggled to "ON". If the AO has approved the use of Bluetooth, on the managed Android 13 device: 1. Go to Settings >> Connected Devices. 2. Verify only approved Bluetooth connected devices using approved profiles are listed. If the AO has not approved the use of Bluetooth, and Bluetooth use is not disabled via an EMM-managed device policy, this is a finding. If the AO has approved the use of Bluetooth, and Bluetooth devices using unauthorized Bluetooth profiles are listed on the device under "Connected devices", this is a finding.

## Group: PP-MDF-333330

**Group ID:** `V-270061`

### Rule: Zebra Android 13 must be configured to disable ad hoc wireless client-to-client connection capability.

**Rule ID:** `SV-270061r1052923_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ad hoc wireless client-to-client connections allow mobile devices to communicate with each other directly, circumventing network security policies and making the traffic invisible. This could allow the exposure of sensitive DOD data and increase the risk of downloading and installing malware of the DOD mobile device. SFR ID: FMT_SMF_EXT.1.1/WLAN</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Zebra Android devices are disallowing Wi-Fi Direct. This validation procedure is performed on both the management tool and the Zebra Android device. On the management tool, in the user restrictions, verify "Wi-Fi Direct" has been set to "Disallow". On the Zebra Android device: 1. Open Settings >> Connections >> Wi-Fi. 2. From the hamburger menu, select Wi-Fi Direct. 3. Verify that Wi-Fi Direct cannot be selected. If on the management tool "Wi-Fi Direct" is not set to "Disallow", or on the Zebra Android device a Wi-Fi direct device is listed that can be connected to, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-270063`

### Rule: Zebra Android 13 users must complete required training.

**Rule ID:** `SV-270063r1052929_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The security posture of Zebra devices requires the device user to configure several required policy rules on their device. User-Based Enforcement (UBE) is required for these controls. In addition, if the authorizing official (AO) has approved the use of an unmanaged personal space, the user must receive training on risks. If a user is not aware of their responsibilities and does not comply with UBE requirements, the security posture of the Zebra mobile device and DOD sensitive data may become compromised. SFR ID: NA</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review a sample of site User Agreements for Zebra Android 13 device users or similar training records and training course content. Verify that the Zebra Android 13 device users have completed the required training. The intent is that required training is renewed on a periodic basis in a time period determined by the AO. If any Zebra Android 13 device user has not completed the required training, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-270064`

### Rule: Zebra Android 13 must be configured to enforce that Wi-Fi Sharing is disabled.

**Rule ID:** `SV-270064r1052932_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Wi-Fi Sharing is an optional configuration of Wi-Fi Tethering/Mobile Hotspot, which allows the device to share its Wi-Fi connection with other wirelessly connected devices instead of its mobile (cellular) connection. Wi-Fi Sharing grants the "other" device access to a corporate Wi-Fi network and may possibly bypass the network access control mechanisms. This risk can be partially mitigated by requiring the use of a pre-shared key for personal hotspots. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review device configuration settings to confirm Wi-Fi Sharing is disabled. Mobile Hotspot must be enabled to enable Wi-Fi Sharing. If the authorizing official (AO) has not approved Mobile Hotspot, and it has been verified as disabled on the EMM console, no further action is needed. If Mobile Hotspot is being used, use the following procedure to verify Wi-Fi Sharing is disabled: On the EMM console: COBO: 1. Open "Set user restrictions". 2. Verify "Disallow config tethering" is toggled to "ON". COPE: 1. Open "Set user restrictions on parent". 2. Toggle "Disallow config tethering" to "ON". On the managed Zebra Android 13 device: COBO and COPE: 1. Go to Settings >> Network & Internet. 2. Verify "Hotspot & tethering" is "Controlled by admin". 3. Verify that tapping "Hotspot & tethering" provides a prompt to the user specifying "Action not allowed". If on the managed Zebra Android 13 device "Hotspot & tethering" is enabled, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-270065`

### Rule: The Zebra Android 13 work profile must be configured to prevent users from adding personal email accounts to the work email app.

**Rule ID:** `SV-270065r1052935_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the user is able to add a personal email account (POP3, IMAP, EAS) to the work email app, it could be used to forward sensitive DOD data to unauthorized recipients. Restricting email account addition to the administrator or restricting email account addition to allowlisted accounts mitigates this vulnerability. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the managed Zebra Android 13 work profile configuration settings to confirm that users are prevented from adding personal email accounts to the work email app. This procedure is performed on both the EMM Administrator console and the managed Zebra Android 13 device. COPE: On the EMM console: 1. Open "Set user restrictions". 2. Verify "Disallow modify accounts" is toggled to "ON". On the managed Zebra Android 13 device: 1. Open "Settings". 2. Tap "Passwords & accounts". 3. Select "Work". 4. Tap "Add account". 5. Verify a message is displayed to the user stating, "Action not allowed". If on the EMM console the restriction to "Disallow modify accounts" is not set, or on the managed Zebra Android 13 device the user is able to add an account in the Work section, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-270066`

### Rule: The Zebra Android 13 work profile must be configured to disable the autofill services.

**Rule ID:** `SV-270066r1052938_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The autofill services allow the user to complete text inputs that could contain sensitive information, such as personally identifiable information (PII), without previous knowledge of the information. By allowing the use of autofill services, an adversary who learns a user's Android 13 device password, or who otherwise is able to unlock the device, may be able to further breach other systems by relying on the autofill services to provide information unknown to the adversary. By disabling the autofill services, the risk of an adversary gaining further information about the device's user or compromising other systems is significantly mitigated. Examples of apps that offer autofill services include Samsung Pass, Google, Dashlane, LastPass, and 1Password. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Zebra Android 13 work profile configuration settings to confirm that autofill services are disabled. This procedure is performed only on the EMM Administration console. On the EMM console: COPE: 1. Open "Set user restrictions". 2. Verify "Disable autofill" is toggled to "ON". If on the EMM console "disallow autofill" is not selected, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-270067`

### Rule: Zebra Android 13 must be configured to disallow configuration of date and time.

**Rule ID:** `SV-270067r1052941_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Determining the correct time a particular application event occurred on a system is critical when conducting forensic analysis and investigating system events. Periodically synchronizing internal clocks with an authoritative time source is necessary to correctly correlate the timing of events that occur across the enterprise. The three authoritative time sources for Zebra Android 13 are an authoritative time server synchronized with redundant United States Naval Observatory (USNO) time servers as designated for the appropriate DOD network (NIPRNet or SIPRNet), or the Global Positioning System (GPS), or the wireless carrier. Time stamps generated by the audit system in Zebra Android 13 must include both date and time. The time may be expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the managed Zebra Android 13 device configuration settings to confirm that autofill services are disabled. This procedure is performed on both the EMM Administration console and the managed Zebra Android 13 device. On the EMM console: COBO: 1. Open "Set user restrictions". 2. Verify "Disallow config date time" is toggled to "ON". COPE: 1. Open "Set user restrictions on parent". 2. Verify "Disallow config date time" is toggled to "ON". On the managed Zebra Android 13 device: COBO and COPE: 1. Open Settings. 2. Tap "System". 3. Tap "Date & times". 4. Verify "Set time automatically" is grayed out and is "Enabled by admin". If on the EMM console "Disallow config date time" is not set to "On", or on the managed Android 13 device "User network-provided time" is not grayed out, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-270069`

### Rule: Android 13 devices must have the latest available Zebra Android 13 operating system installed.

**Rule ID:** `SV-270069r1052947_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Required security features are not available in earlier operating system versions. In addition, there may be known vulnerabilities in earlier versions. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review device configuration settings to confirm the Zebra Android device has the most recently released version of managed Zebra Android 13 installed. This procedure is performed on both the EMM console and the managed Zebra Android 13 device. In the EMM management console, review the version of Zebra Android 13 installed on a sample of managed devices. This procedure will vary depending on the EMM product. On the managed Zebra Android 13 device, to determine the installed operating system version: COBO and COPE: 1. Open Settings. 2. Tap "About phone". 3. Verify "Build number". If the installed version of the Zebra Android 13 operating system on any reviewed devices is not the latest released by Zebra, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-270070`

### Rule: Android 13 devices must be configured to disable the use of third-party keyboards.

**Rule ID:** `SV-270070r1052950_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Many third-party keyboard applications are known to contain malware. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the managed Zebra Android 13 configuration settings to confirm that no third-party keyboards are enabled. This procedure is performed on the EMM console. On the EMM console: COBO and COPE: 1. Open "Input methods". 2. Tap "Set input methods". 3. Verify only the approved keyboards are selected. If third-party keyboards are allowed, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-270071`

### Rule: Android 13 devices must be configured to enable Common Criteria Mode (CC Mode).

**Rule ID:** `SV-270071r1052953_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The CC Mode feature is a superset of other features and behavioral changes that are mandatory MDFPP requirements. If CC mode is not implemented, the device will not be operating in the NIAP-certified compliant CC Mode of operation. CC Mode implements the following behavioral/functional changes: How the Bluetooth and Wi-Fi keys are stored using different types of encryption. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the managed Zebra Android 13 configuration settings to confirm CC mode is enabled. This procedure is performed on the EMM console. COBO and COPE: 1. Open Device owner management. 2. Verify "Enable Common Criteria mode" is toggled to "ON". If CC mode is not enabled, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-270072`

### Rule: Zebra Android 13 must be configured to disable all data signaling over [assignment: list of externally accessible hardware ports (for example, USB)].

**Rule ID:** `SV-270072r1052956_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user is able to configure the security setting, the user could inadvertently or maliciously set it to a value that poses unacceptable risk to DOD information systems. An adversary could exploit vulnerabilities created by the weaker configuration to compromise DOD sensitive information. SFR ID: FMT_MOF_EXT.1.2 #24</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration to confirm that the USB port is disabled except for charging the device. On the EMM console: 1. Open "Set user restrictions". 2. Verify "Enable USB" is toggled to "OFF". If on EMM console the USB port is not disabled, this is a finding.

## Group: PP-MDF-333350

**Group ID:** `V-270073`

### Rule: The Zebra Android 13 must allow only the administrator (EMM) to install/remove DOD root and intermediate PKI certificates.

**Rule ID:** `SV-270073r1052959_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD root and intermediate PKI certificates are used to verify the authenticity of PKI certificates of users and web services. If the user is allowed to remove root and intermediate certificates, the user could allow an adversary to falsely sign a certificate in such a way that it could not be detected. Restricting the ability to remove DOD root and intermediate PKI certificates to the Administrator mitigates this risk. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration to confirm the user is unable to remove DOD root and intermediate PKI certificates. On the EMM console: 1. Open "Set user restrictions". 2. Verify "Disallow config credentials" is toggled to "ON". On the Zebra Android 13 device: 1. Open Settings. 2. Tap "Security". 3. Tap "Advanced". 4. Tap "Encryption & credentials". 5. Tap "Trusted credentials". 6. Verify the user is unable to untrust or remove any work certificates. If the user is able to remove certificates on the Zebra Android 13 device, this is a finding.

