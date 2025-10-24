# STIG Benchmark: Google Android 13 BYOAD Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: PP-MDF-331090

**Group ID:** `V-258475`

### Rule: Google Android 13 must prohibit DOD VPN profiles in the Personal Profile.

**Rule ID:** `SV-258475r950986_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If DOD VPN profiles are configured in the Personal Profile DOD sensitive data world be at risk of compromise and the DOD network could be at risk of being attacked by malware installed on the device. SFR ID: FMT_SMF_EXT.1.1 #3</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the list of VPN profiles in the Personal Profile and determine if any VPN profiles are listed. If so, verify the VPN profiles are not configured with a DOD network VPN profile. If any VPN profiles are installed in the Personal Profile and they have a DOD network VPN profile configured, this is a finding. Note: This setting cannot be managed by the MDM administrator and is a User-Based Enforcement (UBE) requirement.

## Group: PP-MDF-333024

**Group ID:** `V-258476`

### Rule: Google Android 13 must be configured to enforce a minimum password length of six characters and not allow passwords that include more than four repeating or sequential characters.

**Rule ID:** `SV-258476r929466_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password strength is a measure of the effectiveness of a password in resisting guessing and brute force attacks. The ability to crack a password is a function of how many attempts an adversary is permitted, how quickly an adversary can do each attempt, and the size of the password space. The longer the minimum length of the password is, the larger the password space. Having a too-short minimum password length significantly reduces password strength, increasing the chance of password compromise and resulting device and data compromise. Satisfies: PP-MDF-333024, PP-MDF-333025 SFR ID: FMT_SMF_EXT.1.1 #1a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Google Android 13 device configuration settings to determine if the mobile device is enforcing a high password quality for the device and standard DOD password complexity rules for the Work Profile (at least six-character length and prevent passwords from containing more than four repeating or sequential characters). 1. Verify the device password configuration: On the EMM console: a. Open "Lock screen" settings. b. Open "Set required password complexity on parent". c. Verify "High" is selected. 2. Verify the Work Profile password configuration: On the EMM console (for the work profile): 1. Open "Lock screen" settings. 2. Open "Password constraints". 3. Open "Minimum password quality". 4. Verify Numeric Complex, Alphabetic, Alphanumeric, or Complex is selected. 5. Open "Minimum password length". 6. Verify "6" is set for number of characters. If the device password quality is not set to High or the Work Profile password length is not set to six characters or the password quality is not set as required, this is a finding. Note: verifying the OneLock configuration is not required because the use of OneLock is optional.

## Group: PP-MDF-333026

**Group ID:** `V-258477`

### Rule: Google Android 13 must be configured to enable a screen-lock policy that will lock the display after a period of inactivity.

**Rule ID:** `SV-258477r929469_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The screen-lock timeout helps protect the device from unauthorized access. Devices without a screen-lock timeout provide an opportunity for adversaries who gain physical access to the mobile device through loss, theft, etc. Such devices are much more likely to be in an unlocked state when acquired by an adversary, thus granting immediate access to the data on the mobile device and possibly access to DOD networks. SFR ID: FMT_SMF_EXT.1.1 #2a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Google Android 13 device configuration settings to determine if the mobile device is enforcing a screen-lock policy that will lock the display after a period of inactivity. This validation procedure is performed on both the EMM Administration Console and the managed Google Android 13 device. On the EMM console: 1. Open "Lock screen" settings. 2. Open "Lock screen restrictions". 3. Verify that "Max time to screen lock" is set to any number desired, the units are in seconds. On the managed Google Android 13 device: 1. Open Settings >> Display. 2. Tap "Screen timeout". 3. Ensure the Screen timeout value is set to the desired value and cannot be set to a larger value. If the EMM console device policy is not set to enable a screen-lock policy that will lock the display after a period of inactivity, this is a finding.

## Group: PP-MDF-333030

**Group ID:** `V-258478`

### Rule: Google Android 13 must be configured to lock the display after 15 minutes (or less) of inactivity.

**Rule ID:** `SV-258478r929472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The screen lock timeout must be set to a value that helps protect the device from unauthorized access. Having a too-long timeout would increase the window of opportunity for adversaries who gain physical access to the mobile device through loss, theft, etc. Such devices are much more likely to be in an unlocked state when acquired by an adversary, thus granting immediate access to the data on the mobile device. The maximum timeout period of 15 minutes has been selected to balance functionality and security; shorter timeout periods may be appropriate depending on the risks posed to the mobile device. SFR ID: FMT_SMF_EXT.1.1 #2b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Google Android device configuration settings to determine if the mobile device is enforcing a screen-lock policy that will lock the display after a period of 15 minutes or less of inactivity. Note: Google Android 13 does not support the 15-minute increment. The available allowable selection is 10 minutes, then increases to 30 minutes. Therefore, the control should be set to 10 minutes. This validation procedure is performed on both the EMM Administration Console and the Android 13 device. On the EMM console: 1. Open "Lock screen restrictions". 2. Verify that "Max time to screen lock" is set to "600". Note: The units are in seconds. On the managed Google Android 13 device: 1. Open Settings >> Display. 2. Tap "Screen timeout". 3. Ensure the Screen timeout value is set to "600" seconds or less. If the EMM console device policy is not set to enable a screen-lock policy that will lock the display after a period of inactivity of 600 seconds or less, this is a finding.

## Group: PP-MDF-333040

**Group ID:** `V-258479`

### Rule: Google Android 13 must be configured to not allow more than 10 consecutive failed authentication attempts.

**Rule ID:** `SV-258479r929475_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The more attempts an adversary makes to guess a password, the more likely the adversary will enter the correct password and gain access to resources on the device. Setting a limit on the number of attempts mitigates this risk. Setting the limit at 10 or less gives authorized users the ability to make a few mistakes when entering the password but still provides adequate protection against dictionary or brute force attacks on the password. SFR ID: FMT_SMF_EXT.1.1 #2c, FIA_AFL_EXT.1.5</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Google Android 13 device configuration settings to determine if the work profile has the maximum number of consecutive failed authentication attempts set at 10 or fewer. This validation procedure is performed on both the EMM Administration Console and the managed Google Android 13 device. On the EMM console: 1. Open "Lock screen" settings. 2. Open "Lock screen restrictions". 3. Verify that "Max password failures for local wipe" is set to a number between 1 and 10. On the managed Google Android 13 device: 1. Lock the device screen. 2. Attempt to unlock the device and validate that the device autowipes the Work Profile after specified number of invalid entries. Note: Perform this verification only with a test phone set up with a production profile. 3. Attempt to unlock the Work Profile and validate that the device autowipes the Work Profile after specified number of invalid entries. Note: Perform this verification only with a test phone set up with a production profile. If the EMM console device policy is not set to the maximum number of consecutive failed authentication attempts at 10 or fewer, or if on the managed Google Android 13 device the device policy is not set to the maximum number of consecutive failed authentication attempts at 10 or fewer, this is a finding.

## Group: PP-MDF-333050

**Group ID:** `V-258480`

### Rule: Google Android 13 must be configured to enforce an application installation policy by specifying one or more authorized application repositories.

**Rule ID:** `SV-258480r929478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Forcing all applications to be installed from authorized application repositories can prevent unauthorized and malicious applications from being installed and executed on mobile devices. Allowing such installations and executions could cause a compromise of DOD data accessible by these unauthorized/malicious applications. SFR ID: FMT_SMF_EXT.1.1 #8a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Google Android 13 device configuration settings to determine if the mobile device has only approved application repositories. This validation procedure is performed on both the EMM Administration Console and the managed Google Android 13 device. On the EMM console: 1. Open "Set user restrictions". 2. Verify that "Disallow install unknown sources" is toggled to "ON". 3. Verify that "Disallow installs from unknown sources globally" is toggled to "ON". On the Google Android 13 device: 1. Open Settings >> Apps >> Special app access. 2. Open Install unknown apps. 3. Ensure the list of apps is blank or if an app is on the list, "Disabled" is listed under the app name. If the EMM console device policy is not set to allow connections to only approved application repositories or on the managed Google Android 13 device, the device policy is not set to allow connections to only approved application repositories, this is a finding.

## Group: PP-MDF-333060

**Group ID:** `V-258481`

### Rule: Google Android 13 must be configured to enforce an application installation policy by specifying an application allowlist that restricts applications by the following characteristics: [selection: list of digital signatures, cryptographic hash values, names, application version].

**Rule ID:** `SV-258481r929481_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The application allowlist, in addition to controlling the installation of applications on the MD, must control user access/execution of all core and preinstalled applications, or the MD must provide an alternate method of restricting user access/execution to core and preinstalled applications. Core application: Any application integrated into the OS by the OS or MD vendors. Preinstalled application: Additional noncore applications included in the OS build by the OS vendor, MD vendor, or wireless carrier. Requiring all authorized applications to be in an application allowlist prevents the execution of any applications (e.g., unauthorized, malicious) that are not part of the allowlist. Failure to configure an application allowlist properly could allow unauthorized and malicious applications to be downloaded, installed, and executed on the mobile device, causing a compromise of DOD data accessible by these applications. The application allowlist, in addition to controlling the installation of applications on the MD, must control user access/execution of all core applications (included in the OS by the OS vendor) and preinstalled applications (provided by the MD vendor and wireless carrier), or the MD must provide an alternate method of restricting user access/execution to core and preinstalled applications. SFR ID: FMT_SMF_EXT.1.1 #8b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Google Android 13 device configuration settings to determine if the mobile device has an application allowlist configured. Verify all applications listed on the allowlist have been approved by the Approving Official (AO). On the EMM console: 1. Go to the Android app catalog for managed Google Play. 2. Verify all selected apps are AO approved. On the managed Google Android 13 device: 1. Open the managed Google Play Store. 2. Verify that only the approved apps are visible. Note: Managed Google Play is an allowed App Store. If the EMM console list of selected managed Google Play apps includes nonapproved apps, this is a finding. Note: The application allowlist will only include approved core applications (included in the OS by the OS vendor) and pre-installed applications (provided by the MD vendor and wireless carrier), or the MD must provide an alternate method of restricting user access/execution to core and pre-installed applications. For Google Android, there are no pre-installed applications.

## Group: PP-MDF-333070

**Group ID:** `V-258482`

### Rule: Google Android 13 allowlist must be configured to not include applications with the following characteristics (work profile only):

1. Back up mobile device (MD) data to non-DOD cloud servers (including user and application access to cloud backup services);
2. Transmit MD diagnostic data to non-DOD servers;
3. Voice assistant application if available when MD is locked;
4. Voice dialing application if available when MD is locked;
5. Allows synchronization of data or applications between devices associated with user; and
6. Allows unencrypted (or encrypted but not FIPS 140-2 validated) data sharing with other MDs or printers.

**Rule ID:** `SV-258482r929484_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Requiring all authorized applications to be in an application allowlist prevents the execution of any applications (e.g., unauthorized, malicious) that are not part of the allowlist. Failure to configure an application allowlist properly could allow unauthorized and malicious applications to be downloaded, installed, and executed on the mobile device, causing a compromise of DOD data accessible by these applications. Applications with the listed characteristics have features that can cause the compromise of sensitive DOD data or have features with no known application in the DOD environment. Application Note: The application allowlist, in addition to controlling the installation of applications on the MD, must control user access/execution of all core and preinstalled applications, or the MD must provide an alternate method of restricting user access/execution to core and preinstalled applications. Core application: Any application integrated into the OS by the OS or MD vendors. Preinstalled application: Additional noncore applications included in the OS build by the OS vendor, MD vendor, or wireless carrier. SFR ID: FMT_SMF_EXT.1.1 #8b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Google Android 13 device configuration settings to determine if the mobile device has an application allowlist configured and that the application allowlist does not include applications with the following characteristics: - Back up MD data to non-DOD cloud servers (including user and application access to cloud backup services); - Transmit MD diagnostic data to non-DOD servers; - Voice assistant application if available when MD is locked; - Voice dialing application if available when MD is locked; - Allows synchronization of data or applications between devices associated with user; - Payment processing; and - Allows unencrypted (or encrypted but not FIPS 140-2 validated) data sharing with other MDs, display screens (screen mirroring), or printers. This validation procedure is performed only on the EMM Administration Console. On the EMM console: 1. Review the list of selected Managed Google Play apps. 2. Review the details and privacy policy of each selected app to ensure the app does not include prohibited characteristics. If the EMM console device policy includes applications with unauthorized characteristics, this is a finding.

## Group: PP-MDF-333080

**Group ID:** `V-258483`

### Rule: Google Android 13 must be configured to not display the following (work profile) notifications when the device is locked: [selection:
a. email notifications 
b. calendar appointments 
c. contact associated with phone call notification 
d. text message notification
e. other application-based notifications
f. all notifications].

**Rule ID:** `SV-258483r929487_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Many mobile devices display notifications on the lock screen so that users can obtain relevant information in a timely manner without having to frequently unlock the phone to determine if there are new notifications. However, in many cases, these notifications can contain sensitive information. When they are available on the lock screen, an adversary can see them merely by being in close physical proximity to the device. Configuring the mobile operating system (MOS) to not send notifications to the lock screen mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #18</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Google Android 13 device settings to determine if the Google Android 13 device displays (work profile) notifications on the lock screen. Notifications of incoming phone calls are acceptable even when the device is locked. This validation procedure is performed on both the EMM Administration Console and the managed Google Android 13 device. On the EMM console: 1. Open "Lock screen" settings. 2. Open "Lock screen restrictions". 3. Verify that "Disable unredacted notifications" is toggled to "ON". On the managed Google Android 13 device: 1. Go to Settings >> Display >> Lock screen. 2. Tap on "When work profile is locked". 3. Verify that "Hide sensitive work content" is selected. If the EMM console device policy allows work notifications on the lock screen, or the managed Google Android 13 device allows work notifications on the lock screen, this is a finding.

## Group: PP-MDF-333110

**Group ID:** `V-258484`

### Rule: Google Android 13 must be configured to disable trust agents.

**Rule ID:** `SV-258484r930570_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Trust agents allow a user to unlock a mobile device without entering a passcode when the mobile device is, for example, connected to a user-selected Bluetooth device or in a user-selected location. This technology would allow unauthorized users to have access to DOD sensitive data if compromised. By not permitting the use of nonpassword authentication mechanisms, users are forced to use passcodes that meet DOD passcode requirements. SFR ID: FMT_SMF_EXT.1.1 #22, FIA_UAU.5.1</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review device configuration settings to confirm that trust agents are disabled at the same location where the DOD password is implemented (device or work profile). This procedure is performed on both the EMM Administration console and the managed Google Android 13 device. On the EMM console: 1. Open "Lock screen restrictions". 2. Select "Personal Profile". 3. Verify that "Disable trust agents" is toggled to "ON". 4. Open "Lock screen restrictions". 5. Select "Work Profile". 6. Verify that "Disable trust agents" is toggled to "ON". On the managed Google Android 13 device: 1. Open Settings. 2. Tap "Security & privacy". 3. Tap "More security settings". 4. Tap "Trust agents". 5. Verify that all listed trust agents are disabled and cannot be enabled. If on the EMM console, "disable trust agents" is not selected, or on the managed Google Android 13 device a trust agent can be enabled, this is a finding.

## Group: PP-MDF-333160

**Group ID:** `V-258485`

### Rule: Google Android 13 must be configured to display the DOD advisory warning message at startup or each time the user unlocks the Work Profile.

**Rule ID:** `SV-258485r929493_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Before granting access to the system, the mobile operating system is required to display the DOD-approved system use notification message or banner that provides privacy and security notices consistent with applicable Federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. Required banners help ensure that DOD can audit and monitor the activities of mobile device users without legal restriction. System use notification messages can be displayed when individuals first access or unlock the mobile device. The banner must be implemented as a "click-through" banner at device unlock (to the extent permitted by the operating system). A "click-through" banner prevents further activity on the information system unless and until the user executes a positive action to manifest agreement by clicking on a box indicating "OK". The approved DOD text must be used exactly as required in the Knowledge Service referenced in DODI 8500.01. For devices accommodating banners of 1300 characters, the banner text is: You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. For devices with severe character limitations, the banner text is: I've read & consent to terms in IS user agreem't. The administrator must configure the banner text exactly as written without any changes. SFR ID: FMT_SMF_EXT.1.1 #36</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The DOD warning banner can be displayed using the following method (required text is found in the Vulnerability Discussion): By placing the DOD warning banner text in the user agreement signed by each managed Android 13 device user (preferred method). Note: It is not possible for the EMM to force a warning banner be placed on the device screen when using "work profile for employee-owned devices (BYOD)" deployment mode. Review the signed user agreements for several Google Android 13 device users and verify the agreement includes the required DOD warning banner text. If the required warning banner text is not on all signed user agreements reviewed, this is a finding.

## Group: PP-MDF-333250

**Group ID:** `V-258486`

### Rule: Google Android 13 must be configured to not allow backup of all work profile applications to remote systems.

**Rule ID:** `SV-258486r929496_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Backups to remote systems (including cloud backup) can leave data vulnerable to breach on the external systems, which often offer less protection than the mobile operating system (MOS). Where the remote backup involves a cloud-based solution, the backup capability is often used to synchronize data across multiple devices. In this case, DOD devices may synchronize DOD sensitive information to a user's personal device or other unauthorized computers that are vulnerable to breach. Disallowing remote backup mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #40</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review managed Google Android 13 device configuration settings to determine if the capability to back up to a remote system has been disabled. Note: Since personal accounts cannot be added to the work profile (GOOG-13-710100), this control only impacts personal accounts, this setting is used to prevent violations within the work profile for backing up data. This is not applicable to the personal profile. This validation procedure is performed on both the EMM Administration Console and the managed Google Android 13 device. On the EMM console: 1. Open "Device owner management". 2. Verify "Enable backup service" is toggled to "OFF". On the managed Google Android 13 device: 1. Go to Settings >> System >> System >> Backup. 2. Select "Work". 3. Verify Backup settings is "Not available". If backup service for the work profile has not been disabled, this is a finding.

## Group: PP-MDF-333280

**Group ID:** `V-258487`

### Rule: Google Android 13 must be configured to disable exceptions to the access control policy that prevent [selection: application processes, groups of application processes] from accessing [selection: all, private] data stored by other [selection: application processes, groups of application processes].

**Rule ID:** `SV-258487r929499_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>App data sharing gives apps the ability to access the data of other apps for enhanced user functionality. However, sharing also poses a significant risk that unauthorized users or apps will obtain access to DOD sensitive information. To mitigate this risk, there are data sharing restrictions, primarily from sharing data from personal (unmanaged) apps and work (managed) apps. If a user is allowed to make exceptions to the data sharing restriction policy, the user could enable unauthorized sharing of data, leaving it vulnerable to breach. Limiting the granting of exceptions to either the Administrator or common application developer mitigates this risk. Copy/paste of data between applications in different application processes or groups of application processes is considered an exception to the access control policy and therefore, the Administrator must be able to enable/disable the feature. Other exceptions include allowing any data or application sharing between process groups. SFR ID: FMT_SMF_EXT.1.1 #42, FDP_ACF_EXT.1.2</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review documentation on the managed Google Android 13 device and inspect the configuration on the Google Android device to verify the access control policy that prevents [selection: application processes] from accessing [selection: all] data stored by other [selection: application processes] is enabled. This validation procedure is performed only on the EMM Administration Console. On the EMM console: 1. Open "User restrictions". 2. Open "Set user restrictions". 3. Verify that "Disallow cross profile copy/paste" is toggled to "ON". 4. Verify that "Disallow sharing data into the profile" is toggled to "ON". If the EMM console device policy is not set to disable data sharing between profiles, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-258488`

### Rule: Google Android 13 users must complete required training.

**Rule ID:** `SV-258488r929502_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The security posture of Google devices requires the device user to configure several required policy rules on their device. User-Based Enforcement (UBE) is required for these controls. In addition, if the Authorizing Official (AO) has approved the use of an unmanaged personal space, the user must receive training on risks. If a user is not aware of their responsibilities and does not comply with UBE requirements, the security posture of the Google mobile device and DOD sensitive data may become compromised. SFR ID: NA</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review a sample of site User Agreements for Google Android 13 device users or similar training records and training course content. Verify the Google Android 13 device users have completed the required training. The intent is that required training is renewed on a periodic basis in a time period determined by the AO. If any Google Android 13 device user has not completed the required training, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-258489`

### Rule: Google Android 13 must have the DOD root and intermediate PKI certificates installed (work profile only).

**Rule ID:** `SV-258489r929505_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD root and intermediate PKI certificates are used to verify the authenticity of PKI certificates of users and web services. If the root and intermediate certificates are not available, an adversary could falsely sign a certificate in such a way that it could not be detected. Providing access to the DOD root and intermediate PKI certificates greatly diminishes the risk of this attack. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review device configuration settings to confirm that the DOD root and intermediate PKI certificates are installed (work profile only). This procedure is performed on both the EMM Administration console and the managed Google Android 13 device. The current DOD root and intermediate PKI certificates may be obtained in self-extracting zip files at http://cyber.mil/pki-pke (for NIPRNet). On the EMM console verify that the DOD root and intermediate certificates are part of a device and/or work profile that is being pushed down to the devices. On the managed Google Android 13 device: 1. Open Settings. 2. Tap "Security & privacy". 3. Tap "More security settings". 4. Tap "Encryption & credentials". 5. Tap "Trusted credentials". 6. Verify that DOD root and intermediate PKI certificates are listed under the User tab in the Work section. If on the EMM console the DOD root and intermediate certificates are not listed in a profile, or the managed Android 13 device does not list the DOD root and intermediate certificates under the user tab, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-258490`

### Rule: The Google Android 13 work profile must be configured to prevent users from adding personal email accounts to the work email app.

**Rule ID:** `SV-258490r929508_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the user can add a personal email account (POP3, IMAP, EAS) to the work email app, it could be used to forward sensitive DOD data to unauthorized recipients. Restricting email account addition to the administrator or restricting email account addition to allowlisted accounts mitigates this vulnerability. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the managed Google Android 13 work profile configuration settings to confirm that users are prevented from adding personal email accounts to the work email app. This procedure is performed on both the EMM Administrator console and the managed Google Android 13 device. On the EMM console: 1. Open "Set user restrictions". 2. Verify "Disallow modify accounts" is toggled to "ON". On the managed Google Android 13 device: 1. Open Settings. 2. Tap "Passwords & accounts". 3. Select "Work". 4. Tap "Add account". 5. Verify a message is displayed to the user stating, "Blocked by your IT admin". If on the EMM console the restriction to "Disallow modify accounts" is not set, or on the managed Android 13 device the user is able to add an account in the Work section, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-258491`

### Rule: The Google Android 13 work profile must be configured to enforce the system application disable list (work profile only).

**Rule ID:** `SV-258491r929511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The system application disables list controls user access to/execution of all core and preinstalled applications. Core application: Any application integrated into Google Android 13 by Google. Preinstalled application: Additional noncore applications included in the Google Android 13 build by Google or the wireless carrier. Some system applications can compromise DOD data or upload users' information to non-DOD-approved servers. A user must be blocked from using such applications that exhibit behavior that can result in compromise of DOD data or DOD user information. The site administrator must analyze all preinstalled applications on the device and disable all applications not approved for DOD use by configuring the system application disable list. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the managed Google Android 13 work profile configuration settings to confirm the system application disable list is enforced (work profile only). This setting is enforced by default. Verify only approved system apps have been placed on the core allowlist. This procedure is performed on the EMM Administrator console. Review the system app allowlist and verify only approved apps are on the list. 1. Open "Apps management" section. 2. Select "Hide apps on parent". 3. Verify package names of apps are listed. If on the EMM console the system app allowlist contains unapproved core apps, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-258492`

### Rule: Google Android 13 must be provisioned as a BYOAD device (Android work profile for employee-owned devices [BYOD]).

**Rule ID:** `SV-258492r929530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Android work profile for employee-owned devices (BYOD) is the designated application group for the BYOAD use case. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review that managed Google Android 13 is configured for BYOD (work profile for employee-owned devices [BYOD]). This procedure is performed on both the EMM Administrator console and the managed Google Android 13 device. On the EMM console, configure the default enrollment as work profile for employee-owned devices (BYOD). On the managed Google Android 13 device: 1. Go to the application drawer. 2. Ensure a Personal tab and a Work tab are present. If on the EMM console, the default enrollment is not set for BYOD (work profile for employee-owned devices [BYOD]), or if on the managed Android 13 device, the user does not have a Work tab, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-258493`

### Rule: The Google Android 13 work profile must be configured to disable automatic completion of workspace internet browser text input.

**Rule ID:** `SV-258493r929517_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The autofill functionality in the web browser allows the user to complete a form that contains sensitive information, such as personally identifiable information (PII), without previous knowledge of the information. By allowing the use of autofill functionality, an adversary who learns a user's Android 13 device password, or who otherwise can unlock the device, may be able to further breach other systems by relying on the autofill feature to provide information unknown to the adversary. By disabling the autofill functionality, the risk of an adversary gaining further information about the device's user or compromising other systems is significantly mitigated. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the work profile Chrome Browser app on the Google Android 13 autofill setting. This procedure is performed only on the EMM Administrator console. On the EMM console: 1. Open "Managed Configurations" section. 2. Select the Chrome Browser version from the work profile. 3. Verify "SearchSuggestEnabled" is turned "OFF". If on the EMM console autofill is set to "On" in the Chrome Browser Settings, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-258494`

### Rule: The Google Android 13 work profile must be configured to disable the autofill services.

**Rule ID:** `SV-258494r929520_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The autofill services allow the user to complete text inputs that could contain sensitive information, such as personally identifiable information (PII), without previous knowledge of the information. By allowing the use of autofill services, an adversary who learns a user's Android 13 device password, or who otherwise can unlock the device, may be able to further breach other systems by relying on the autofill services to provide information unknown to the adversary. By disabling the autofill services, the risk of an adversary gaining further information about the device's user or compromising other systems is significantly mitigated. Examples of apps that offer autofill services include Samsung Pass, Google, Dashlane, LastPass, and 1Password. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Google Android 13 work profile configuration settings to confirm that autofill services are disabled. This procedure is performed only on the EMM Administration console. On the EMM console: 1. Open "Set user restrictions". 2. Verify "Disallow autofill" is toggled to "ON". If on the EMM console "disallow autofill" is not selected, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-258495`

### Rule: Android 13 devices must have the latest available Google Android 13 operating system installed.

**Rule ID:** `SV-258495r929523_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Required security features are not available in earlier operating system versions. In addition, earlier versions may have known vulnerabilities. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review device configuration settings to confirm the Google Android device has the most recently released version of managed Google Android 13 installed. This procedure is performed on both the EMM console and the managed Google Android 13 device. In the EMM management console, review the version of Google Android 13 installed on a sample of managed devices. This procedure will vary depending on the EMM product. To determine the installed operating system version on the managed Google Android 13 device: 1. Open Settings. 2. Tap "About phone". 3. Verify "Build number". If the installed version of the Google Android 13 operating system on any reviewed device is not the latest released by Google, this is a finding. Google's Android operating system patch website: https://source.android.com/security/bulletin/ Android versions for Pixel devices: https://developers.google.com/android/images

## Group: PP-MDF-993300

**Group ID:** `V-258496`

### Rule: Android 13 devices must be configured to disable the use of third-party keyboards (work profile only).

**Rule ID:** `SV-258496r929526_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Many third-party keyboard applications are known to contain malware. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the managed Google Android 13 configuration settings to confirm that no third-party keyboards are enabled (work profile only). This procedure is performed on the EMM console. On the EMM console: 1. Open "Input methods". 2. Tap "Set input methods". 3. Verify only the approved keyboards are selected. If unapproved third-party keyboards are allowed in the work profile, this is a finding.

## Group: PP-MDF-333350

**Group ID:** `V-258497`

### Rule: The Google Android 13 must allow only the administrator (EMM) to install/remove DOD root and intermediate PKI certificates (work profile).

**Rule ID:** `SV-258497r929529_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD root and intermediate PKI certificates are used to verify the authenticity of PKI certificates of users and web services. If the user is allowed to remove root and intermediate certificates, the user could allow an adversary to falsely sign a certificate in such a way that it could not be detected. Restricting the ability to remove DOD root and intermediate PKI certificates to the Administrator mitigates this risk. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration to confirm that the user is unable to remove DOD root and intermediate PKI certificates (work profile). On the EMM console: 1. Open "Set user restrictions". 2. Verify "Disallow config credentials" is toggled to "ON". On the Google Android 13 device: 1. Open Settings. 2. Tap "Security and privacy". 3. Tap "More security settings". 4. Tap "Encryption & credentials". 5. Tap "Trusted credentials". 6. Verify the user is unable to untrust or remove any work certificates. If the user can remove certificates on the Google Android 13 device, this is a finding.

