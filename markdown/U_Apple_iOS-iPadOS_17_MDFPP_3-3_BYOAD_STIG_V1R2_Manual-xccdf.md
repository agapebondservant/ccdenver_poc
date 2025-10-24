# STIG Benchmark: Apple iOS/iPadOS 17 MDFPP 3.3 BYOAD Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: PP-MDF-331090

**Group ID:** `V-259760`

### Rule: Apple iOS/iPadOS 17 must allow the administrator (MDM) to perform the following management function: enable/disable VPN protection across the device.

**Rule ID:** `SV-259760r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The system administrator must have the capability to configure VPN access to meet organization-specific policies based on mission needs. Otherwise, a user could inadvertently or maliciously set up a VPN and connect to a network that poses unacceptable risk to DOD information systems. An adversary could exploit vulnerabilities created by the weaker configuration to compromise DOD sensitive information. SFR ID: FMT_SMF_EXT.1.1 #3</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the list of unmanaged apps installed on the iPhone and iPad and determine if any third-party VPN clients are installed. If so, verify the VPN app is not configured with a DOD network (work) VPN profile. This validation procedure is performed on the iOS device only. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap the "VPN and Device Management" line and determine if any "Personal VPN" exists. 4. If not, the requirement has been met. 5. If there are personal VPNs, open each VPN app. Review the list of VPN profiles configured on the VPN client. 6. Verify no DOD network VPN profiles are configured on the VPN client. If any third-party unmanaged VPN apps are installed (personal VPN) and they have a DOD network VPN profile configured on the client, this is a finding. Note: This setting cannot be managed by the MDM administrator and is a User-Based Enforcement (UBE) requirement.

## Group: PP-MDF-333250

**Group ID:** `V-259761`

### Rule: Apple iOS/iPadOS 17 must not allow backup to remote systems (managed applications data stored in iCloud).

**Rule ID:** `SV-259761r958524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user is able to configure the security setting, the user could inadvertently or maliciously set it to a value that poses unacceptable risk to DOD information systems. An adversary could exploit vulnerabilities created by the weaker configuration to compromise DOD sensitive information. SFR ID: FMT_MOF_EXT.1.2 #40</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm "Allow managed apps to store data in iCloud" is disabled. This check procedure is performed on both the Apple iOS/iPadOS management tool and the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the Apple iOS/iPadOS management tool, verify "Allow managed apps to store data in iCloud" is unchecked. Alternatively, verify the text "<key>allowManagedAppsCloudSync</key> <false/>" appears in the configuration profile (.mobileconfig file). On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the Apple iOS/iPadOS management tool containing the restrictions policy. 5. Tap "Restrictions". 6. Verify "Managed apps cloud sync not allowed" is listed. If "Allow managed apps to store data in iCloud" is checked in the Apple iOS/iPadOS management tool, "<key>allowManagedAppsCloudSync</key> <true/>" appears in the configuration profile, or the restrictions policy on the iPhone and iPad does not list "Managed apps cloud sync not allowed", this is a finding.

## Group: PP-MDF-333250

**Group ID:** `V-259762`

### Rule: Apple iOS/iPadOS 17 must not allow backup to remote systems (enterprise books).

**Rule ID:** `SV-259762r958524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user is able to configure the security setting, the user could inadvertently or maliciously set it to a value that poses unacceptable risk to DOD information systems. An adversary could exploit vulnerabilities created by the weaker configuration to compromise DOD sensitive information. SFR ID: FMT_MOF_EXT.1.2 #40</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm "Allow backup of enterprise books" is disabled. This check procedure is performed on both the Apple iOS/iPadOS management tool and the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the Apple iOS/iPadOS management tool, verify "Allow backup of enterprise books" is unchecked. Alternatively, verify the text "<key>allowEnterpriseBookBackup</key> <false/>" appears in the configuration profile (.mobileconfig file). On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the Apple iOS/iPadOS management tool containing the restrictions policy. 5. Tap "Restrictions". 6. Verify "Backing up enterprise books not allowed" is listed. If "Allow backup of enterprise books" is checked in the Apple iOS/iPadOS management tool, "<key>allowEnterpriseBookBackup</key> <true/>" appears in the configuration profile, or the restrictions policy on the iPhone and iPad does not list "Backing up enterprise books not allowed", this is a finding.

## Group: PP-MDF-333024

**Group ID:** `V-259763`

### Rule: Apple iOS/iPadOS 17 must be configured to enforce a minimum password length of six characters.

**Rule ID:** `SV-259763r985624_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password strength is a measure of the effectiveness of a password in resisting guessing and brute force attacks. The ability to crack a password is a function of how many attempts an adversary is permitted, how quickly an adversary can do each attempt, and the size of the password space. The longer the minimum length of the password is, the larger the password space. Having a too-short minimum password length significantly reduces password strength, increasing the chance of password compromise and resulting device and data compromise. SFR ID: FMT_SMF_EXT.1.1 #1a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm the minimum passcode length is six or more characters. This procedure is performed in the Apple iOS/iPadOS management tool and on the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the Management tool, verify the "Minimum passcode length" value is set to six or greater. Alternatively, verify the text "<key>minLength</key> <integer>6</integer>" appears in the configuration profile (.mobileconfig file). It also is acceptable for the integer value to be greater than six. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the Apple iOS/iPadOS management tool containing the password policy. 5. Tap "Restrictions". 6. Tap "Passcode". 7. Verify "Minimum length" is listed as "six or greater". If the "Minimum passcode length" is less than six characters in the iOS management tool, "<key>minLength</key> " has an integer value of less than six, or the password policy on the iPhone and iPad from the Apple iOS/iPadOS management tool does not list "Minimum length" of six or more, this is a finding.

## Group: PP-MDF-333025

**Group ID:** `V-259764`

### Rule: Apple iOS/iPadOS 17 must be configured to not allow passwords that include more than four repeating or sequential characters.

**Rule ID:** `SV-259764r985626_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password strength is a measure of the effectiveness of a password in resisting guessing and brute force attacks. Passwords that contain repeating or sequential characters are significantly easier to guess than those that do not contain repeating or sequential characters. Therefore, disallowing repeating or sequential characters increases password strength and decreases risk. SFR ID: FMT_SMF_EXT.1.1 #1b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm simple passcodes are not allowed. This check procedure is performed on both the Apple iOS/iPadOS management tool and the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the Apple iOS/iPadOS management tool, verify "Allow simple value" is unchecked. Alternatively, verify the text "<key>allowSimple</key> <false/>" appears in the configuration profile (.mobileconfig file). On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the iOS management tool containing the password policy. 5. Tap "Restrictions". 6. Tap "Passcode". 7. Verify "Simple passcodes allowed" is set to "No". If "Allow simple value" is checked in the Apple iOS/iPadOS management tool, "<key>allowSimple</key> <true/>" appears in the Configuration Profile, or the password policy on the iPhone and iPad does not have "Simple passcodes allowed" set to "No", this is a finding.

## Group: PP-MDF-333030

**Group ID:** `V-259766`

### Rule: Apple iOS/iPadOS 17 must be configured to lock the display after 15 minutes (or less) of inactivity.

**Rule ID:** `SV-259766r971318_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The screen lock timeout must be set to a value that helps protect the device from unauthorized access. Having a too-long timeout would increase the window of opportunity for adversaries who gain physical access to the mobile device through loss, theft, etc. Such devices are much more likely to be in an unlocked state when acquired by an adversary, thus granting immediate access to the data on the mobile device. The maximum timeout period of 15 minutes has been selected to balance functionality and security; shorter timeout periods may be appropriate depending on the risks posed to the mobile device. SFR ID: FMT_SMF_EXT.1.1 #2b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm the screen lock timeout is set to 15 minutes or less. This check procedure is performed on both the Apple iOS/iPadOS management tool and the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the management tool, verify the sum of the values assigned to "Maximum Auto-Lock time" and "Grace period for device lock" is between 1 and 15 minutes. Alternatively, locate the text "<key>maxGracePeriod</key>" and "<key>maxInactivity</key>" and ensure the sum of their integer value is between 1 and 15 in the configuration profile (.mobileconfig file). For example: "<key>maxGracePeriod</key> <integer>5</integer> <key>maxInactivity</key> <integer>5</integer>" Here, 5 + 5 = 10; this meets the requirement. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the iOS management tool containing the password policy. 5. Tap "Restrictions". 6. Tap "Passcode". 7. Verify the sum of the "Max grace period" and "Max inactivity" values is less than 15 minutes. Note: On some iOS/iPadOS devices, it is not possible to have a sum of exactly 15. In these cases, the sum must be less than 15. A sum of 16 does not meet the requirement. On the management server, if the sum of the "Max grace period" and "Max inactivity" values is not between 1 and 15 minutes in the iOS/iPadOS management tool or the sum of the values assigned to "<key>maxGracePeriod</key>" and "<key>maxInactivity</key>" is not between 1 and 15 minutes in the configuration profile, or if on the iPhone/iPad, the sum of the values assigned to "Max grace period" and "Max inactivity" is not between 1 and 15 minutes, this is a finding.

## Group: PP-MDF-333040

**Group ID:** `V-259767`

### Rule: Apple iOS/iPadOS 17 must be configured to not allow more than 10 consecutive failed authentication attempts.

**Rule ID:** `SV-259767r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The more attempts an adversary has to guess a password, the more likely the adversary will enter the correct password and gain access to resources on the device. Setting a limit on the number of attempts mitigates this risk. Setting the limit at 10 or less gives authorized users the ability to make a few mistakes when entering the password but still provides adequate protection against dictionary or brute force attacks on the password. SFR ID: FMT_SMF_EXT.1.1 #2c, FIA_AFL_EXT.1.5</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm that consecutive failed authentication attempts is set to 10 or fewer. This procedure is performed in the Apple iOS/iPadOS management tool and on the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the Management tool, verify the "Maximum number of failed attempts" value is set to 10 or fewer. Alternatively, verify the text "<key>maxFailedAttempts</key> <integer>10</integer>" appears in the configuration profile (.mobileconfig file). It also is acceptable for the integer value to be less than 10. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the iOS management tool containing the password policy. 5. Tap "Restrictions". 6. Tap "Passcode". 7. Verify "Max failed attempts" is listed as "10" or fewer. If the "Maximum number of failed attempts" is more than 10 in the iOS management tool, "<key>maxFailedAttempts</key> " has an integer value of more than 10, or the password policy on the iPhone and iPad does not list "Max failed attempts" of 10 or fewer, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-259768`

### Rule: Apple iOS/iPadOS 17 must be configured to enforce a passcode reuse prohibition of at least two generations.

**Rule ID:** `SV-259768r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>iOS/iPadOS 17 includes a new feature that allows the previous passcode to be valid for 72 hours after a passcode change. If the previous passcode has been compromised and the attacker has access to it and the Apple device, enterprise data and the enterprise network can be compromised. Currently there is no MDM control to force the old passcode to expire immediately after passcode change. The previous passcode will expire immediately after a passcode change if the MDM password history control is implemented. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm the Apple iOS or iPadOS device has a passcode reuse prohibition of at least two generations. This procedure is performed in the Apple iOS/iPadOS management tool and on the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the Management tool, verify the "Passcode History" value is set to two or greater. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the Apple iOS/iPadOS management tool containing the password policy. 5. Tap "Restrictions". 6. Tap "Passcode". 7. Verify "Number of unique recent passcodes required" is listed as "two" or greater. If the Apple iOS or iPadOS device does not enforce a passcode reuse prohibition of at least two generations, this is a finding.

## Group: PP-MDF-333050

**Group ID:** `V-259769`

### Rule: Apple iOS/iPadOS 17 must be configured to enforce an application installation policy by specifying one or more authorized application repositories, including [selection: DOD-approved commercial app repository, MDM server, mobile application store].

**Rule ID:** `SV-259769r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Forcing all applications to be installed from authorized application repositories can prevent unauthorized and malicious applications from being installed and executed on mobile devices. Allowing such installations and executions could cause a compromise of DOD data accessible by these unauthorized/malicious applications. SFR ID: FMT_SMF_EXT.1.1 #8a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm "Allow Trusting New Enterprise App Authors" is disabled. This procedure is performed in the Apple iOS/iPadOS management tool and on the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the Management tool, verify "Allow Trusting New Enterprise App Authors" is disabled. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the Apple iOS/iPadOS management tool containing the restrictions policy. 5. Tap "Restrictions". 6. Verify "Trusting enterprise apps not allowed" is listed. If "Allow Trusting New Enterprise App Authors" is not disabled in the iOS/iPadOS management tool or on the iPhone and iPad, this is a finding.

## Group: PP-MDF-333070

**Group ID:** `V-259770`

### Rule: Apple iOS/iPadOS 17 allow list must be configured to not include applications with the following characteristics: 

- backs up MD data to non-DOD cloud servers (including user and application access to cloud backup services);
- transmits MD diagnostic data to non-DOD servers;
- allows synchronization of data or applications between devices associated with user; and
- allows unencrypted (or encrypted but not FIPS 140-2/FIPS 140-3 validated) data sharing with other MDs or printers.

**Rule ID:** `SV-259770r1032950_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Requiring all authorized applications to be in an application allow list prevents the execution of any applications (e.g., unauthorized, malicious) that are not part of the allow list. Failure to configure an application allow list properly could allow unauthorized and malicious applications to be downloaded, installed, and executed on the mobile device, causing a compromise of DOD data accessible by these applications. Applications with the listed characteristics have features that can cause the compromise of sensitive DOD data or have features with no known application in the DOD environment. Application note: The application allow list, in addition to controlling the installation of applications on the MD, must control user access/execution of all core and preinstalled applications, or the MD must provide an alternate method of restricting user access/execution to core and preinstalled applications. Core application: Any application integrated into the OS by the OS or MD vendors. Preinstalled application: Additional noncore applications included in the OS build by the OS vendor, MD vendor, or wireless carrier. SFR ID: FMT_SMF_EXT.1.1 #8b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify no apps with the following prohibited characteristics are included in the configuration profile: - backs up MD data to non-DOD cloud servers (including user and application access to cloud backup services); - transmits MD diagnostic data to non-DOD servers; - allows synchronization of data or applications between devices associated with user; and - allows unencrypted (or encrypted but not FIPS 140-2/FIPS 140-3 validated) data sharing with other MDs or printers. This check procedure is performed on the Apple iOS/iPadOS management tool. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the Apple iOS/iPadOS management tool, verify "Allow Listed App" (allowlistedAppBundleIDs) is configured and there are no apps with prohibited characteristics. If "Allow listed apps" is not configured and contains apps with prohibited characteristics, this is a finding.

## Group: PP-MDF-333080

**Group ID:** `V-259771`

### Rule: Apple iOS/iPadOS 17 must be configured to not display notifications when the device is locked.

**Rule ID:** `SV-259771r958404_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Many mobile devices display notifications on the lock screen so users can obtain relevant information in a timely manner without having to frequently unlock the phone to determine if there are new notifications. However, in many cases, these notifications can contain sensitive information. When they are available on the lock screen, an adversary can see them merely by being in close physical proximity to the device. Configuring the mobile operating system to not send notifications to the lock screen mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #18</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm the display of notifications when the device is locked has been disabled. There are two acceptable methods. The first method is preferred. Verification Procedure for Method 1: This check procedure is performed only on the Apple iOS/iPadOS management tool. In the Apple iOS/iPadOS management tool, for each managed app, verify the app is configured to disable Notifications preview. If one or more managed apps are not set to disable notification previews, this is a finding. Verification Procedure for Method 2: This check procedure is performed on both the Apple iOS/iPadOS management tool and the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the Apple iOS/iPadOS management tool, verify "Show Notification Center in Lock screen" is unchecked. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the iOS management tool containing the management policy. 5. Tap "Restrictions". 6. Verify "Notifications view on lock screen not allowed" is present. If "Show Notification Center in Lock screen" is checked in the Apple iOS/iPadOS management tool or the restrictions policy on the iPhone and iPad does not list "Notifications View on lock screen not allowed", this is a finding.

## Group: PP-MDF-333080

**Group ID:** `V-259772`

### Rule: Apple iOS/iPadOS 17 must not display notifications (calendar information) when the device is locked.

**Rule ID:** `SV-259772r958404_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Many mobile devices display notifications on the lock screen so users can obtain relevant information in a timely manner without having to frequently unlock the phone to determine if there are new notifications. However, in many cases, these notifications can contain sensitive information. When they are available on the lock screen, an adversary can see them merely by being in close physical proximity to the device. Configuring the mobile operating system to not send notifications to the lock screen mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #18</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm "Show Today view in Lock screen" is disabled. This check procedure is performed on both the Apple iOS/iPadOS management tool and the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the Apple iOS/iPadOS management tool, verify "Show Today view in Lock screen" is unchecked. Alternatively, verify the text "<key>allowLockScreenTodayView</key><false/>" appears in the configuration profile (.mobileconfig file). On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "Profiles & Device Management" or Profiles". 4. Tap the Configuration Profile from the iOS management tool containing the management policy. 5. Tap "Restrictions". 6. Verify "Today view on lock screen not allowed" is present. If "Show Today view in Lock screen" is checked in the Apple iOS/iPadOS management tool, "<key>allowLockScreenTodayView</key><true/>" appears in the configuration profile, or the restrictions policy on the iPhone and iPad does not list "Today view on lock screen not allowed", this is a finding.

## Group: PP-MDF-333160

**Group ID:** `V-259773`

### Rule: Apple iOS/iPadOS 17 must be configured to display the DOD advisory warning message at startup or each time the user unlocks the device.

**Rule ID:** `SV-259773r958390_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Before granting access to the system, the mobile operating system is required to display the DOD-approved system use notification message or banner that provides privacy and security notices consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. Required banners help ensure the DOD can audit and monitor the activities of mobile device users without legal restriction. System use notification messages can be displayed when individuals first access or unlock the mobile device. The banner must be implemented as a "click-through" banner at device unlock (to the extent permitted by the operating system). A "click-through" banner prevents further activity on the information system unless and until the user executes a positive action to manifest agreement by clicking on a box indicating "OK". The approved DOD text must be used exactly as required in the Knowledge Service referenced in DODI 8500.01. For devices accommodating banners of 1300 characters, the banner text is: You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. Refer to User Agreement for details. For devices with severe character limitations, the banner text is: I've read & consent to terms in IS user agreem't. The administrator must configure the banner text exactly as written without any changes. SFR ID: FMT_SMF_EXT.1.1 #36</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The DOD warning banner can be displayed by either of the following methods (required text is found in the Vulnerability Discussion): Method 1: By placing the DOD warning banner text in the user agreement signed by each iPhone and iPad user. Method 2: By installing a Lock Screen Message payload with the required text (preferred method). Determine which method is used at the iOS device site and follow the appropriate validation procedure below. Validation Procedure for Method 1: Review the signed user agreements for several iOS device users and verify the agreement includes the required DOD warning banner text. Validation Procedure for Method 2: In the Apple iOS/iPadOS management tool, verify a Lock Screen Message payload has been installed on each managed device. The LockScreenFootnote string should include required text. If for Method 1, the required warning banner text is not on all signed user agreements reviewed, or for Method 2, the DOD warning banner text is not set as the lock screen footnote, this is a finding.

## Group: PP-MDF-333240

**Group ID:** `V-259774`

### Rule: Apple iOS/iPadOS 17 must be configured to not allow backup of [all applications, configuration data] to locally connected systems.

**Rule ID:** `SV-259774r958524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data on mobile devices is protected by numerous mechanisms, including user authentication, access control, and cryptography. When the data is backed up to an external system (either locally connected or cloud based), many if not all of these mechanisms are no longer present. This leaves the backed-up data vulnerable to attack. Disabling backup to external systems mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #40</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm backup in management apps is disabled and "Encrypt local backup" is enabled in iTunes (for Windows computer) and in Finder on Mac. Note: iTunes Backup/Finder backup is implemented by the configuration policy rule "Force encrypted backups", which is included in AIOS-17-710700 and therefore not included in the procedure below. This check procedure is performed on both the Apple iOS/iPadOS management tool and the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the Apple iOS/iPadOS management tool, verify backing up app data is disabled. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the Apple iOS/iPadOS management tool containing the restrictions policy. 5. Tap "Apps". 6. Tap a "managed app". 7. Verify "App data will not be backed up" is listed. Note: Steps 6 and 7 must be performed for each managed app. If backing up app data is not disabled in the Apple iOS/iPadOS management tool or "app data will not be backed up" is not listed for each managed app on the iPhone and iPad, this is a finding.

## Group: PP-MDF-333280

**Group ID:** `V-259775`

### Rule: Apple iOS/iPadOS 17 must not allow non-DOD applications to access DOD data.

**Rule ID:** `SV-259775r958878_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>App data sharing gives apps the ability to access the data of other apps for enhanced user functionality. However, sharing also poses a significant risk that unauthorized users or apps will obtain access to sensitive DOD information. To mitigate this risk, there are data sharing restrictions. If a user is allowed to make exceptions to the data sharing restriction policy, the user could enable unauthorized sharing of data, leaving it vulnerable to breach. Limiting the granting of exceptions to either the administrator or common application developer mitigates this risk. Copy/paste of data between applications in different application processes or groups of application processes is considered an exception to the access control policy; therefore, the administrator must be able to enable/disable the feature. Other exceptions include allowing any data or application sharing between process groups. SFR ID: FMT_SMF_EXT.1.1 #42, FDP_ACF_EXT.1.2</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm "Allow documents from managed apps in unmanaged apps" is disabled. This check procedure is performed on both the Apple iOS/iPadOS management tool and the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the iOS management tool, verify "Allow documents from managed apps in unmanaged apps" is unchecked. Alternatively, verify the text "<key>allowOpenFromManagedToUnmanaged</key><false/>" appears in the configuration profile (.mobileconfig file). On the iOS device: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the iOS management tool containing the restrictions policy. 5. Tap "Restrictions". 6. Verify "Opening documents from managed to unmanaged apps not allowed" is listed. If "Allow documents from managed apps in unmanaged apps" is checked in the iOS management tool, "<key>allowOpenFromManagedToUnmanaged</key><true/>" appears in the configuration profile, or the restrictions policy on the iPhone and iPad does not list "Opening documents from managed to unmanaged apps not allowed", this is a finding.

## Group: PP-MDF-333300

**Group ID:** `V-259776`

### Rule: Apple iOS/iPadOS 17 must be configured to [selection: wipe protected data, wipe sensitive data] upon unenrollment from MDM.

**Rule ID:** `SV-259776r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a mobile device is no longer going to be managed by MDM technologies, its protected/sensitive data must be sanitized because it will no longer be protected by the MDM software, putting it at much greater risk of unauthorized access and disclosure. At least one of the two options must be selected. SFR ID: FMT_SMF_EXT.2.1</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: Not all Apple iOS/iPadOS deployments involve MDM. If the site uses an authorized alternative to MDM for distribution of configuration profiles (Apple Configurator), this check procedure is not applicable. This check procedure is performed on the Apple iOS/iPadOS management tool or on the iOS device. In the Apple iOS/iPadOS management tool, for each managed app, verify the app is configured to be removed when the MDM profile is removed. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the iOS management tool containing the management policy. 5. Tap "Apps". 6. Tap an app and verify "App and data will be removed when device is no longer managed" is listed. Repeat steps 5 and 6 for each managed app in the list. If one or more managed apps are not set to be removed upon device MDM unenrollment, this is a finding.

## Group: PP-MDF-333310

**Group ID:** `V-259777`

### Rule: Apple iOS/iPadOS 17 must be configured to [selection: remove Enterprise applications, remove all noncore applications (any nonfactory installed application)] upon unenrollment from MDM.

**Rule ID:** `SV-259777r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a mobile device will no longer be managed by MDM technologies, its protected/sensitive data must be sanitized because it will no longer be protected by the MDM software, putting it at much greater risk of unauthorized access and disclosure. At least one of the two options must be selected. SFR ID: FMT_SMF_EXT.2.1</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: Not all Apple iOS/iPadOS deployments involve MDM. If the site uses an authorized alternative to MDM for distribution of configuration profiles (Apple Configurator), this check procedure is not applicable. This check procedure is performed on the Apple iOS/iPadOS management tool or on the iOS device. In the Apple iOS/iPadOS management tool, for each managed app, verify the app is configured to be removed when the MDM profile is removed. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the iOS management tool containing the management policy. 5. Tap "Apps". 6. Tap an app and verify "App and data will be removed when device is no longer managed" is listed. Repeat steps 5 and 6 for each managed app in the list. If one or more managed apps are not set to be removed upon device MDM unenrollment, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-259778`

### Rule: Apple iOS/iPadOS 17 must require a valid password be successfully entered before the mobile device data is unencrypted.

**Rule ID:** `SV-259778r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords provide a form of access control that prevents unauthorized individuals from accessing computing resources and sensitive data. Passwords may also be a source of entropy for generation of key encryption or data encryption keys. If a password is not required to access data, this data is accessible to any adversary who obtains physical possession of the device. Requiring that a password be successfully entered before the mobile device data is unencrypted mitigates this risk. Note: MDF PP requires a Password Authentication Factor and requires management of its length and complexity. It leaves open whether the existence of a password is subject to management. This requirement addresses the configuration to require a password, which is critical to the cybersecurity posture of the device. SFR ID: FIA_UAU_EXT.1.1</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm the device is set to require a passcode before use. This procedure is performed on the iOS and iPadOS device. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the iOS management tool containing the password policy. 5. Tap "Restrictions". 6. Tap "Passcode". 7. Verify "Passcode required" is set to "Yes". If "Passcode required" is not set to "Yes", this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-259779`

### Rule: Apple iOS/iPadOS 17 must implement the management setting: Encrypt backups/Encrypt local backup.

**Rule ID:** `SV-259779r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If iCloud backups are not encrypted, this could lead to the unauthorized disclosure of DOD sensitive information if non-DOD personnel are able to access that machine. Forcing the backup to be encrypted greatly mitigates the risk of compromising sensitive data. Work data iCloud backup and USB connections to computers are not authorized, but this control provides defense-in-depth for cases in which a user violates policy either intentionally or inadvertently. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm "Force encrypted backups" is enabled. This check procedure is performed on both the Apple iOS/iPadOS management tool and the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the Apple iOS/iPadOS management tool, verify "Encrypt local backup" is checked. Alternatively, verify the text "<key>forceEncryptedBackup</key><true/>" appears in the configuration profile (.mobileconfig file). On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the Apple iOS/iPadOS management tool containing the restrictions policy. 5. Tap "Restrictions". 6. Verify "Encrypt backups enforced" is listed. If "Encrypt local backup" is unchecked in the Apple iOS/iPadOS management tool, "<key>forceEncryptedBackup</key><false/>" appears in the configuration profile, or the restrictions policy on the iPhone and iPad does not list "Encrypt backups enforced", this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-259780`

### Rule: Apple iOS/iPadOS 17 must implement the management setting: require the user to enter a password when connecting to an AirPlay-enabled device.

**Rule ID:** `SV-259780r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>When a user is allowed to use AirPlay without a password, it may mistakenly associate the iPhone and iPad with an AirPlay-enabled device other than the one intended (i.e., by choosing the wrong one from the AirPlay list displayed). This creates the potential for someone in control of a mistakenly associated device to obtain DOD sensitive information without authorization. Requiring a password before such an association mitigates this risk. Passwords do not require any administration and are not required to comply with any complexity requirements. SFR ID: FMT_SMF_EXT.1.1 #40</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm "Require passcode on outgoing AirPlay request" is enabled. This check procedure is performed on both the Apple iOS/iPadOS management tool and the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the Apple iOS/iPadOS management tool, verify "Require passcode on outgoing AirPlay request" is checked. Alternatively, verify the text "<key>forceAirPlayOutgoingRequestsPairingPassword</key><false/>" appears in the configuration profile (.mobileconfig file). On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the Apple iOS/iPadOS management tool containing the restrictions policy. 5. Tap "Restrictions". 6. Verify "AirPlay outgoing requests pairing password enforced" is listed. If "Require passcode on outgoing AirPlay request" is unchecked in the Apple iOS/iPadOS management tool, "<key>forceAirPlayOutgoingRequestsPairingPassword</key><true/>" appears in the configuration profile, or the restrictions policy on the iPhone and iPad does not list "AirPlay outgoing requests pairing password enforced", this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-259781`

### Rule: Apple iOS/iPadOS 17 must implement the management setting: require passcode for incoming Airplay connection requests.

**Rule ID:** `SV-259781r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>When an incoming AirPlay request is allowed without a password, it may mistakenly associate the iPhone and iPad with an AirPlay-enabled device other than the one intended (i.e., by choosing the wrong one from the AirPlay list displayed). This creates the potential for someone in control of a mistakenly associated device to obtain DOD sensitive information without authorization. Requiring a password before such an association mitigates this risk. Passwords do not require any administration and are not required to comply with any complexity requirements. SFR ID: FMT_SMF_EXT.1.1 #40</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm "Require passcode for incoming AirPlay connection requests" is enabled. This check procedure is performed on both the Apple iOS/iPadOS management tool and the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the Apple iOS/iPadOS management tool, verify "Require passcode for incoming AirPlay connection requests" is checked. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the Apple iOS/iPadOS management tool containing the restrictions policy. 5. Tap "Restrictions". 6. Verify "AirPlay incoming requests pairing password enforced" is listed. If "Require passcode for incoming AirPlay connection requests" is unchecked in the Apple iOS/iPadOS management tool or the restrictions policy on the iPhone and iPad does not list "AirPlay incoming requests pairing password enforced", this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-259782`

### Rule: iPhone and iPad must have the latest available iOS/iPadOS operating system installed.

**Rule ID:** `SV-259782r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Required security features are not available in earlier OS versions. In addition, earlier versions may have known vulnerabilities. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm the most recently released version of iOS is installed. This validation procedure is performed on both the Apple iOS/iPadOS management tool and the iPhone and iPad. Go to https://www.apple.com and determine the most current version of iOS released by Apple. In the MDM management console, review the version of iOS installed on a sample of managed devices. This procedure will vary depending on the MDM product. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "About" and view the installed version of iOS. 4. Go back to the "General" screen. Tap "Software Update" and verify the following message is shown on the screen: "Your software is up to date." If the installed version of iOS on any reviewed iOS/iPadOS devices is not the latest released by Apple, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-259783`

### Rule: Apple iOS/iPadOS 17 must implement the management setting: use SSL for Exchange ActiveSync.

**Rule ID:** `SV-259783r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Exchange email messages are a form of data in transit and thus are vulnerable to eavesdropping and man-in-the-middle attacks. Secure Sockets Layer (SSL), also referred to as Transport Layer Security (TLS), provides encryption and authentication services that mitigate the risk of breach. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm "Use SSL" for the Exchange account is enabled for incoming mail. This check procedure is performed on both the Apple iOS/iPadOS management tool and the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the Apple iOS/iPadOS management tool, verify "Use SSL for incoming mail" is checked under the Exchange payload. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the Apple iOS/iPadOS management tool containing the Exchange policy. 5. Tap "Mail". 6. Tap the name of the Exchange account. 7. Verify "SSL for incoming mail" is set to "Yes". If "Use SSL for incoming mail" is unchecked in the Apple iOS/iPadOS management tool or the Exchange policy on the iPhone and iPad has "SSL for incoming mail" set to "No", this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-259784`

### Rule: Apple iOS/iPadOS 17 must implement the management setting: not allow messages in an ActiveSync Exchange account to be forwarded or moved to other accounts in the Apple iOS/iPadOS 17 Mail app.

**Rule ID:** `SV-259784r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Apple iOS/iPadOS Mail app can be configured to support multiple email accounts concurrently. These email accounts are likely to involve content of varying degrees of sensitivity (e.g., both personal and enterprise messages). To prevent the unauthorized and undetected forwarding or moving of messages from one account to another, Mail ActiveSync Exchange accounts can be configured to block such behavior. While users may still send a message from the Exchange account to another account, these transactions must involve an Exchange server, enabling audit records of the transaction, filtering of mail content, and subsequent forensic analysis. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm "Allow messages to be moved" is disabled. This check procedure is performed on both the Apple iOS/iPadOS management tool and the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the Apple iOS/iPadOS management tool, verify "Allow messages to be moved" is unchecked under the Exchange payload. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the Apple iOS/iPadOS management tool containing the Exchange policy. 5. Tap "Mail". 6. Tap the "name of the Exchange account". 7. Verify "Prevent Move" is set to "Yes". If "Allow messages to be moved" is checked in the Apple iOS/iPadOS management tool or the Exchange policy on the iPhone and iPad has "Prevent Move" set to "No", this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-259785`

### Rule: Apple iOS/iPadOS 17 must implement the management setting: Treat AirDrop as an unmanaged destination.

**Rule ID:** `SV-259785r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>AirDrop is a way to send contact information or photos to other users with AirDrop enabled. This feature enables a possible attack vector for adversaries to exploit. Once the attacker has gained access to the information broadcast by this feature, the attacker may distribute this sensitive information very quickly and without DOD's control or awareness. By disabling this feature, the risk of mass data exfiltration will be mitigated. Note: If the site uses Apple's optional Automatic Device Enrollment, this control is available as a supervised MDM control. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm "Treat AirDrop as an unmanaged destination" is enabled. This check procedure is performed on both the Apple iOS/iPadOS management tool and the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the Apple iOS/iPadOS management tool, verify "Treat AirDrop as unmanaged destination" is checked. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration management tool containing the restrictions policy. 5. Tap "Restrictions". 6. Verify "Sharing managed documents using AirDrop not allowed" is listed. If "Treat AirDrop as unmanaged destination" is disabled in the Apple iOS/iPadOS management tool or the restrictions policy on the iPhone and iPad does not list "Sharing managed documents using AirDrop not allowed", this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-259786`

### Rule: Apple iOS/iPadOS 17 must implement the management setting: force Apple Watch wrist detection.

**Rule ID:** `SV-259786r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Because Apple Watch is a personal device, it is key that any sensitive DOD data displayed on the Apple Watch cannot be viewed when the watch is not in the immediate possession of the user. This control ensures the Apple Watch screen locks when the user takes the watch off, thereby protecting sensitive DOD data from possible exposure. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm "Force Apple Watch wrist detection" is enabled. This check procedure is performed on both the Apple iOS/iPadOS management tool and the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the Apple iOS/iPadOS management tool, verify "Wrist detection enforced on Apple Watch" is enforced. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the Apple iOS/iPadOS management tool containing the restrictions policy. 5. Tap "Restrictions". 6. Verify "Wrist detection enforced on Apple Watch" is listed. If "Wrist detection enforced on Apple Watch" is not enforced in the Apple iOS/iPadOS management tool or the restrictions policy on the iPhone and iPad does not list "Wrist detection enforced on Apple Watch", this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-259787`

### Rule: Apple iOS/iPadOS 17 users must complete required training.

**Rule ID:** `SV-259787r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The security posture on iOS devices requires the device user to configure several required policy rules on their device. User-Based Enforcement (UBE) is required for these controls. In addition, if the authorizing official (AO) has approved users' full access to the Apple App Store, users must receive training on risks. If a user is not aware of their responsibilities and does not comply with UBE requirements, the security posture of the iOS mobile device and DOD sensitive data may become compromised. SFR ID: NA</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review a sample of site User Agreements for iOS device users or similar training records and training course content. Verify iPhone and iPad users have completed required training. If any iPhone/iPad user has not completed required training, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-259788`

### Rule: A managed photo app must be used to take and store work-related photos.

**Rule ID:** `SV-259788r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The iOS Photos app is unmanaged and may sync photos with a device user's personal iCloud account. Therefore, work-related photos must not be taken via the iOS camera app or stored in the Photos app. A managed photo app must be used to take and manage work-related photos. SFR ID: NA</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm a managed photos app is installed on the iOS device. This check procedure is performed on the iPhone and iPad. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the DOD Configuration Profile from the Apple iOS/iPadOS management tool. 5. Tap "Apps". 6. Verify a photo capture and management app is listed. If a managed photo capture and management app is not installed on the iPhone and iPad, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-259789`

### Rule: Apple iOS/iPadOS 17 must not allow managed apps to write contacts to unmanaged contacts accounts.

**Rule ID:** `SV-259789r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Managed apps have been approved for the handling of DOD sensitive information. Unmanaged apps are provided for productivity and morale purposes but are not approved to handle DOD sensitive information. Examples of unmanaged apps include those for news services, travel guides, maps, and social networking. If a document were to be viewed in a managed app and the user had the ability to open this same document in an unmanaged app, this could lead to the compromise of sensitive DOD data. In some cases, the unmanaged apps are connected to cloud backup or social networks that would permit dissemination of DOD sensitive information to unauthorized individuals. Not allowing data to be opened within unmanaged apps mitigates the risk of compromising sensitive data. SFR ID: FMT_SMF_EXT.1.1 #42, FDP_ACF_EXT.1.2</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm "Allow managed apps to write contacts to unmanaged contacts accounts" is disabled. This check procedure is performed on both the Apple iOS/iPadOS management tool and the Apple iOS/iPadOS device. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the iOS/iPadOS management tool, verify "Allow managed apps to write contacts to unmanaged contacts accounts" is unchecked. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the iOS/iPadOS management tool containing the restrictions policy. 5. Tap "Restrictions". 6. Verify "Allow managed apps to write contacts to unmanaged contacts accounts" is not listed. If "Allow managed apps to write contacts to unmanaged contacts accounts" is checked in the iOS/iPadOS management tool or the restrictions policy on the iPhone and iPad lists "Allow managed apps to write contacts to unmanaged contacts accounts", this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-259790`

### Rule: Apple iOS/iPadOS 17 must not allow unmanaged apps to read contacts from managed contacts accounts.

**Rule ID:** `SV-259790r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Managed apps have been approved for the handling of DOD sensitive information. Unmanaged apps are provided for productivity and morale purposes but are not approved to handle DOD sensitive information. Examples of unmanaged apps include those for news services, travel guides, maps, and social networking. If a document were to be viewed in a managed app and the user had the ability to open this same document in an unmanaged app, this could lead to the compromise of sensitive DOD data. In some cases, the unmanaged apps are connected to cloud backup or social networks that would permit dissemination of DOD sensitive information to unauthorized individuals. Not allowing data to be opened within unmanaged apps mitigates the risk of compromising sensitive data. SFR ID: FMT_SMF_EXT.1.1 #42, FDP_ACF_EXT.1.2</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm "Allow unmanaged apps to read contacts from managed contacts accounts" is disabled. This check procedure is performed on both the Apple iOS/iPadOS management tool and the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the iOS management tool, verify "Allow unmanaged apps to read contacts from managed contacts accounts" is unchecked. On the iPhone and iPad: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the iOS/iPadOS management tool containing the restrictions policy. 5. Tap "Restrictions". 6. Verify "Allow unmanaged apps to read contacts from managed contacts accounts" is not listed. If "Allow unmanaged apps to read contacts from managed contacts accounts" is checked in the iOS/iPadOS management tool or the restrictions policy on the iPhone and iPad lists "Allow unmanaged apps to read contacts from managed contacts accounts", this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-259791`

### Rule: The Apple iOS must be configured to disable automatic transfer of diagnostic data to an external device other than an MDM service with which the device has enrolled.

**Rule ID:** `SV-259791r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Many software systems automatically send diagnostic data to the manufacturer or a third party. This data enables the developers to understand real-world field behavior and improve the product based on that information. Unfortunately, it can also reveal information about what DOD users are doing with the systems and what causes them to fail. An adversary embedded within the software development team or elsewhere could use the information acquired to breach mobile operating system security. Disabling automatic transfer of such information mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #47a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm "Allow sending diagnostic and usage data to Apple" is disabled. This check procedure is performed on both the iOS management tool and the iOS device. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the iOS management tool, verify "Allow sending diagnostic and usage data to Apple" is unchecked. Alternatively, verify the text "<key>allowDiagnosticSubmission</key><false/>" appears in the configuration profile (.mobileconfig file). On the Apple iOS device: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the iOS management tool containing the management policy. 5. Tap "Restrictions". 6. Verify "Diagnostic submission not allowed". Note: This setting also disables "Share With App Developers". If "Allow sending diagnostic and usage data to Apple" is checked in the iOS management tool, "<key>allowDiagnosticSubmission</key><true/>" appears in the configuration profile, or the restrictions policy on the Apple iOS device from the Apple iOS management tool does not list "Diagnostic submission not allowed", this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-259792`

### Rule: Apple iOS/iPadOS 17 must disable copy/paste of data from managed to unmanaged applications.

**Rule ID:** `SV-259792r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user is able to configure the security setting, the user could inadvertently or maliciously set it to a value that poses unacceptable risk to DOD information systems. An adversary could exploit vulnerabilities created by the weaker configuration to compromise DOD sensitive information. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the iOS management tool, verify "Require managed pasteboard" is set to "True". If "Require managed pasteboard" is not set to "True", this is a finding.

## Group: PP-MDF-333350

**Group ID:** `V-259793`

### Rule: Apple iOS/iPadOS 17 must have DOD root and intermediate PKI certificates installed.

**Rule ID:** `SV-259793r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD root and intermediate PKI certificates are used to verify the authenticity of PKI certificates of users and web services. If the user is allowed to remove root and intermediate certificates, the user could allow an adversary to falsely sign a certificate in such a way that it could not be detected. Restricting the ability to remove DOD root and intermediate PKI certificates to the administrator mitigates this risk. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify DOD intermediate and root certificates have been installed on Apple devices. In the iOS management tool, verify the DOD intermediate and root certificates are installed on the Apple device. On the iPhone and iPad device: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the iOS management tool containing the restrictions policy. 5. Tap "Restrictions". 6. Tap "More Details". 7. Verify the DOD intermediate and root certificates are listed. If DOD intermediate and root certificates are not installed on the Apple device, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-259794`

### Rule: Apple iOS/iPadOS 17 must not allow DOD applications to access non-DOD data.

**Rule ID:** `SV-259794r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>App data sharing gives apps the ability to access the data of other apps for enhanced user functionality. However, sharing also poses a significant risk that unauthorized users or apps will obtain access to sensitive DOD information. To mitigate this risk, there are data sharing restrictions. If a user is allowed to make exceptions to the data sharing restriction policy, the user could enable unauthorized sharing of data, leaving it vulnerable to breach. Limiting the granting of exceptions to either the administrator or common application developer mitigates this risk. Copy/paste of data between applications in different application processes or groups of application processes is considered an exception to the access control policy; therefore, the administrator must be able to enable/disable the feature. Other exceptions include allowing any data or application sharing between process groups. SFR ID: FMT_SMF_EXT.1.1 #42, FDP_ACF_EXT.1.2</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration settings to confirm "Allow documents from unmanaged apps in managed apps" is disabled. This check procedure is performed on both the Apple iOS/iPadOS management tool and the iPhone and iPad. Note: If an organization has multiple configuration profiles, the check procedure must be performed on the relevant configuration profiles applicable to the scope of the review. In the iOS management tool, verify "Allow documents from unmanaged apps in managed apps" is unchecked. On the iOS device: 1. Open the Settings app. 2. Tap "General". 3. Tap "VPN & Device Management". 4. Tap the Configuration Profile from the iOS management tool containing the restrictions policy. 5. Tap "Restrictions". 6. Verify "Opening documents from unmanaged to managed apps not allowed" is listed. If "Allow documents from unmanaged apps in managed apps" is checked in the iOS management tool or the restrictions policy on the iPhone and iPad does not list "Opening documents from unmanaged to managed apps not allowed", this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-274439`

### Rule: All Apple iOS/iPadOS 17 BYOAD installations must be removed.

**Rule ID:** `SV-274439r1099863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Apple iOS/iPadOS 17 BYOAD is no longer supported by Apple and therefore, may contain security vulnerabilities. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there are no installations of Apple iOS/iPadOS 17 BYOAD at the site. If Apple iOS/iPadOS 17 BYOAD is being used at the site, this is a finding.

