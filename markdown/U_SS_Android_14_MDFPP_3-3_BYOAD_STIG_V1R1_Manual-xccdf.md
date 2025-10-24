# STIG Benchmark: Samsung Android 14 MDFPP 3.3 BYOAD Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: PP-MDF-993300

**Group ID:** `V-260439`

### Rule: Samsung Android must be enrolled as a BYOD device.

**Rule ID:** `SV-260439r950896_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Work profile is the designated application group for the BYOD use case. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices are enrolled in a DOD-approved use case. This validation procedure is performed on both the management tool Administration Console and the Samsung Android device. On the management tool, verify the default enrollment is set to "Work profile for personally-owned devices". On the Samsung Android device: 1. Open Settings >> Security and privacy >> More security settings >> Device admin apps. 2. Verify the management tool Agent is listed. 3. Go to the app drawer. 4. Verify a "Personal" and "Work" tab are present. If on the management tool the default enrollment is not set as "Work profile for personally-owned devices", or on the Samsung Android device the "Personal" and "Work" tabs are not present or the management tool Agent is not listed, this is a finding.

## Group: PP-MDF-333160

**Group ID:** `V-260440`

### Rule: Samsung Android must be configured to display the DOD advisory warning message at startup or each time the user unlocks the device.

**Rule ID:** `SV-260440r953769_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Before granting access to the system, the mobile operating system is required to display the DOD-approved system use notification message or banner that provides privacy and security notices consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. Required banners help ensure that DOD can audit and monitor the activities of mobile device users without legal restriction. System use notification messages can be displayed when individuals first access or unlock the mobile device. The banner must be implemented as a "click-through" banner at device unlock (to the extent permitted by the operating system). A "click-through" banner prevents further activity on the information system unless and until the user executes a positive action to manifest agreement by clicking on a box indicating "OK." The approved DOD text must be used exactly as required in the Knowledge Service referenced in DODI 8500.01. For devices accommodating banners of 1300 characters, the banner text is: You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE, or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. Refer to User Agreement for details. For devices with severe character limitations, the banner text is: I've read & consent to terms in IS user agreem't. The Administrator must configure the banner text exactly as written without any changes. SFR ID: FMT_SMF_EXT.1.1 #36</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The DOD warning banner can be displayed using the following method (required text is found in the Vulnerability Discussion): Place the DOD warning banner in the user agreement signed by each Samsung Android device user (preferred method). Note: It is not possible for the EMM to force a warning banner be placed on the device screen when using "work profile for employee-owned devices (BYOD)" deployment mode. Review the signed user agreements for several Samsung Android device users and verify the agreement includes the required DOD warning banner text. If the required warning banner text is not on all signed user agreements reviewed, this is a finding.

## Group: PP-MDF-333025

**Group ID:** `V-260441`

### Rule: Samsung Android must be configured to not allow passwords that include more than four repeating or sequential characters.

**Rule ID:** `SV-260441r950902_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password strength is a measure of the effectiveness of a password in resisting guessing and brute force attacks. Passwords that contain repeating or sequential characters are significantly easier to guess than those that do not. Therefore, disallowing repeating or sequential characters increases password strength and decreases risk. SFR ID: FMT_SMF_EXT.1.1 #1b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices' Work Environment is disallowing passwords containing more than four repeating or sequential characters. This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the device password policies, verify "minimum password quality" is set to "Numeric(Complex)" or better. On the Samsung Android device, confirm if the user has "One Lock" enabled (Settings >> Security and privacy >> More security settings >> Work profile security >> Use one lock). If "One Lock" is enabled: 1. Open Settings >> Lock screen >> Screen lock type. 2. Enter current password. 3. Tap "PIN". 4. Verify that PINs with more than four repeating or sequential numbers are not accepted. If "One Lock" is disabled: 1. Open Settings >> Security and privacy >> More security settings >> Work profile security >> Work profile lock type. 2. Enter current password. 3. Tap "PIN". 4. Verify that PINs with more than four repeating or sequential numbers are not accepted. If on the management tool "minimum password quality" is not set to "Numeric(Complex)" or better, or on the Samsung Android device a password with more than four repeating or sequential numbers is accepted, this is a finding.

## Group: PP-MDF-333024

**Group ID:** `V-260442`

### Rule: Samsung Android must be configured to enforce a minimum password length of six characters.

**Rule ID:** `SV-260442r950905_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password strength is a measure of the effectiveness of a password in resisting guessing and brute force attacks. The ability to crack a password is a function of how many attempts an adversary is permitted, how quickly an adversary can complete each attempt, and the size of the password space. The longer the minimum length of the password is, the larger the password space. Having a too-short minimum password length significantly reduces password strength, increasing the chance of password compromise and resulting device and data compromise. SFR ID: FMT_SMF_EXT.1.1 #1a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices' Work Environment is enforcing a minimum password length of six characters. This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the Work Environment password policies, verify "minimum password length" is set to "6". On the Samsung Android device, confirm if the user has "One Lock" enabled (Settings >> Security and privacy >> More security settings >> Work profile security >> Use one lock). If "One Lock" is enabled: 1. Open Settings >> Lock screen >> Screen lock type. 2. Enter current password. 3. Tap "PIN". 4. Verify the text "PIN must contain at least", followed by a value of at least "6 digits", appears above the PIN entry. If "One Lock" is disabled: 1. Open Settings >> Security and privacy >> More security settings >> Work profile security >> Work profile lock type. 2. Enter current password. 3. Tap "PIN". 4. Verify the text "PIN must contain at least", followed by a value of at least "6 digits", appears above the PIN entry. If on the management tool "minimum password length" is not set to "6", or on the Samsung Android device the text "PIN must contain at least" is followed by a value of less than "6 digits", this is a finding.

## Group: PP-MDF-333040

**Group ID:** `V-260443`

### Rule: Samsung Android must be configured to not allow more than 10 consecutive failed authentication attempts.

**Rule ID:** `SV-260443r950908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The more attempts an adversary has to guess a password, the more likely the adversary will enter the correct password and gain access to resources on the device. Setting a limit on the number of attempts mitigates this risk. Setting the limit at 10 or fewer attempts gives authorized users the ability to make a few mistakes when entering the password but still provides adequate protection against dictionary or brute force attacks on the password. SFR ID: FMT_SMF_EXT.1.1 #2c, FIA_AFL_EXT.1.5</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices' Work Environment is allowing only 10 or fewer consecutive failed authentication attempts. This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the device password policies, verify "max password failures for local wipe" is set to "10" attempts or less. On the Samsung Android device, confirm if the user has "One Lock" enabled (Settings >> Security and privacy >> More security settings >> Work profile security >> Use one lock). If "One Lock" is enabled: 1. Lock the device. 2. Make attempts to unlock the Device with incorrect PIN and validate that the device reports that if you do not enter the correct PIN within the next few attempts that a wipe will occur. If "One Lock" is disabled: 1. Wait for the Work profile to Lock (determined by Auto lock work profile configuration) - or reboot the Device. 2. Attempt to unlock the Work profile with an incorrect PIN and validate that the device reports "9" or less attempts left. If on the management tool "max password failures for local wipe" is not set to "10" attempts or less, or on the Samsung Android device - after making incorrect PIN entry attempts - it does not report that the device will wipe, this is a finding.

## Group: PP-MDF-333026

**Group ID:** `V-260444`

### Rule: Samsung Android must be configured to lock the display after 15 minutes (or less) of inactivity.

**Rule ID:** `SV-260444r950911_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The screen lock timeout must be set to a value that helps protect the device from unauthorized access. Having a too-long timeout would increase the window of opportunity for adversaries who gain physical access to the mobile device through loss, theft, etc. Such devices are much more likely to be in an unlocked state when acquired by an adversary, thus granting immediate access to the data on the mobile device. The maximum timeout period of 15 minutes has been selected to balance functionality and security; shorter timeout periods may be appropriate depending on the risks posed to the mobile device. Satisfies: PP-MDF-333026,PP-MDF-333030 SFR ID: FMT_SMF_EXT.1.1 #2a, 2bb</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices' Work Environment is locking the device display after 15 minutes (or less) of inactivity. This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the Work environment password policies, verify "max time to screen lock" is set to "15 minutes" or less. On the Samsung Android device, confirm if the user has "One Lock" enabled (Settings >> Security and privacy >> More security settings >> Work profile security >> Use one lock). If "One Lock" is enabled: 1. Open Settings >> Lock screen. 2. Verify "Secure lock settings" is present and tap it. 3. Enter current password. 4. Tap "Auto lock when screen turns off". 5. Verify the listed timeout values are 15 minutes or less. If "One Lock" is disabled: 1. Open Settings >> Security and privacy >> More security settings >> Work profile security >> Auto lock work profile. 2. Verify the listed timeout values are 15 minutes or less. If on the management tool "max time to screen lock" is not set to "15 minutes" or less, or on the Samsung Android device the listed Screen timeout values include durations of more than 15 minutes, this is a finding.

## Group: PP-MDF-333110

**Group ID:** `V-260445`

### Rule: Samsung Android must be configured to disable authentication mechanisms providing user access to protected data other than a Password Authentication Factor: Face recognition.

**Rule ID:** `SV-260445r953770_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The biometric factor can be used to authenticate the user to unlock the mobile device. Unapproved/evaluated biometric mechanisms could allow unauthorized users to have access to DOD sensitive data if compromised. By not permitting the use of unapproved/evaluated biometric authentication mechanisms, this risk is mitigated. SFR ID: FMT_SMF_EXT.1.1 #22, FIA_UAU.5.1</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement is not applicable for specific biometric authentication factors included in the product's Common Criteria evaluation. Review the configuration to determine if the Samsung Android devices' Work Environment is disabling Face Recognition. This validation procedure is performed on both the management tool and the Samsung Android device. Face recognition is not a feature available for unlocking the Work profile unless "One Lock" is used. Otherwise, on the management tool, in the Work Environment restrictions, verify that "Face" is set to "Disable". On the Samsung Android device, confirm if the user has "One Lock" enabled (Settings >> Security and privacy >> More security settings >> Work profile security >> Use one lock). If "One Lock" is enabled: 1. Open Settings >> Lock screen >> Screen lock type. 2. Enter current password. 3. Verify that "Face" is disabled and cannot be enabled. The disablement of Face cannot be verified while "One Lock" is disabled, as they are not an available feature for Work profiles. To verify, the Admin would need to temporarily enable "One Lock" for the purpose of testing only and follow the above instruction. After testing, the User would have to reset their Work profile password when "One Lock" was turned off again. If on the management tool "Face" is not set to "Disable", or on the Samsung Android device "Face" can be enabled, this is a finding.

## Group: PP-MDF-333030

**Group ID:** `V-260446`

### Rule: Samsung Android must be configured to enable a screen-lock policy that will lock the display after a period of inactivity - Disable trust agents.

**Rule ID:** `SV-260446r953771_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The screen lock timeout must be set to a value that helps protect the device from unauthorized access. Having a too-long timeout would increase the window of opportunity for adversaries who gain physical access to the mobile device through loss, theft, etc. Such devices are much more likely to be in an unlocked state when acquired by an adversary, thus granting immediate access to the data on the mobile device. The maximum timeout period of 15 minutes has been selected to balance functionality and security; shorter timeout periods may be appropriate depending on the risks posed to the mobile device. SFR ID: FMT_SMF_EXT.1.1 #2a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices' Work Environment is disabling Trust Agents. This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the device restrictions, verify that "Trust Agents" are set to "Disable". On the Samsung Android device, confirm if the user has "One Lock" enabled (Settings >> Security and privacy >> More security settings >> Work profile security >> Use one lock). If "One Lock" is enabled: 1. Open Settings >> Security and privacy >> More security settings >> Trust agents. 2. Verify that all listed Trust Agents are disabled and cannot be enabled. The disablement of Trust Agents cannot be verified while "One Lock" is disabled, as they are not an available feature for Work profiles. To verify, the Admin would need to temporarily enable "One Lock" for the purpose of testing only and follow the above instruction. After testing, the User would have to reset their Work profile password when "One Lock" was turned off again. If on the management tool "Trust Agents" are not set to "Disable", or on the Samsung Android device a "Trust Agent" can be enabled, this is a finding. Note: If the management tool has been correctly configured but a Trust Agent is still enabled, configure the "List of approved apps listed in managed Google Play" to disable it; refer to KNOX-14-710190. Exception: Trust Agents may be used if the Authorizing Official (AO) allows a screen lock timeout after four hours (or more) of inactivity. This may be applicable to tactical use case.

## Group: PP-MDF-993300

**Group ID:** `V-260447`

### Rule: Samsung Android's Work profile must have the DOD root and intermediate PKI certificates installed.

**Rule ID:** `SV-260447r950920_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD root and intermediate PKI certificates are used to verify the authenticity of PKI certificates of users and web services. If the root and intermediate certificates are not available, an adversary could falsely sign a certificate in such a way that it could not be detected. Providing access to the DOD root and intermediate PKI certificates greatly diminishes the risk of this attack. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android's Work profile has the DOD root and intermediate PKI certificates installed. This validation procedure is performed on both the management tool and the Samsung Android device. The current DOD root and intermediate PKI certificates may be obtained in self-extracting zip files at https://cyber.mil/pki-pke (for NIPRNet). On the management tool, in the Work profile policy management, verify the DOD root and intermediate PKI certificates are installed. On the Samsung Android device: 1. Open Settings >> Security and privacy >> More security settings >> View security certificates. 2. In the User tab, verify the DOD root and intermediate PKI certificates are listed in the Work profile. If on the management tool the DOD root and intermediate PKI certificates are not listed in the Work profile, or on the Samsung Android device the DOD root and intermediate PKI certificates are not listed in the Work profile, this is a finding.

## Group: PP-MDF-333060

**Group ID:** `V-260448`

### Rule: Samsung Android's Work profile must be configured to enforce an application installation policy by specifying an application allowlist that restricts applications by the following characteristics: Names.

**Rule ID:** `SV-260448r950923_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The application allowlist, in addition to controlling the installation of applications on the MD, must control user access/execution of all core and preinstalled applications, or the MD must provide an alternate method of restricting user access/execution to core and preinstalled applications. Core application: Any application integrated into the OS by the OS or MD vendors. Preinstalled application: Additional noncore applications included in the OS build by the OS vendor, MD vendor, or wireless carrier. Requiring all authorized applications to be in an application allowlist prevents the execution of any applications (e.g., unauthorized, malicious) that are not part of the allowlist. Failure to configure an application allowlist properly could allow unauthorized and malicious applications to be downloaded, installed, and executed on the mobile device, causing a compromise of DOD data accessible by these applications. The application allowlist, in addition to controlling the installation of applications on the MD, must control user access/execution of all core applications (included in the OS by the OS vendor) and preinstalled applications (provided by the MD vendor and wireless carrier), or the MD must provide an alternate method of restricting user access/execution to core and preinstalled applications. SFR ID: FMT_SMF_EXT.1.1 #8b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Work profile on the Samsung Android device is allowing users to install only applications that have been approved by the Authorizing Official (AO). This validation procedure is performed only on the management tool. On the management tool, in the app catalog for managed Google Play, verify that only AO-approved apps are available. If on the management tool the app catalog for managed Google Play includes non-AO-approved apps, this is a finding.

## Group: PP-MDF-333070

**Group ID:** `V-260449`

### Rule: Samsung Android's Work profile must be configured to not allow installation of applications with the following characteristics: 

- Back up MD data to non-DOD cloud servers (including user and application access to cloud backup services);
- Transmit MD diagnostic data to non-DOD servers;
- Voice assistant application if available when MD is locked;
- Voice dialing application if available when MD is locked;
- Allows synchronization of data or applications between devices associated with user; and
- Allows unencrypted (or encrypted but not FIPS 140-3 validated) data sharing with other MDs or printers.
- Apps which backup their own data to a remote system.

**Rule ID:** `SV-260449r950926_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Requiring all authorized applications to be in an application allowlist prevents the execution of any applications (e.g., unauthorized, malicious) that are not part of the allowlist. Failure to configure an application allowlist properly could allow unauthorized and malicious applications to be downloaded, installed, and executed on the mobile device, causing a compromise of DOD data accessible by these applications. Applications with the listed characteristics have features that can cause the compromise of sensitive DOD data or have features with no known application in the DOD environment. Application note: The application allowlist, in addition to controlling the installation of applications on the MD, must control user access/execution of all core and preinstalled applications, or the MD must provide an alternate method of restricting user access/execution to core and preinstalled applications. Core application: Any application integrated into the OS by the OS or MD vendors. Preinstalled application: Additional noncore applications included in the OS build by the OS vendor, MD vendor, or wireless carrier. SFR ID: FMT_SMF_EXT.1.1 #8b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify requirement KNOX-14-710190 (managed Google Play) has been implemented. Verify the application allowlist does not include applications with the following characteristics: - Back up MD data to non-DOD cloud servers (including user and application access to cloud backup services); - Transmit MD diagnostic data to non-DOD servers; - Voice assistant application if available when MD is locked; - Voice dialing application if available when MD is locked; - Allows synchronization of data or applications between devices associated with user; - Payment processing; and - Allows unencrypted (or encrypted but not FIPS 140-3 validated) data sharing with other MDs, display screens (screen mirroring), or printers. - Apps which backup their own data to a remote system. If managed Google Play has not been implemented, this is a finding. This validation procedure is performed only on the EMM Administration Console. On the EMM console: 1. Review the list of selected Managed Google Play apps. 2. Review the details and privacy policy of each selected app to ensure the app does not include prohibited characteristics. If the EMM console device policy includes applications with unauthorized characteristics, this is a finding.

## Group: PP-MDF-333080

**Group ID:** `V-260450`

### Rule: Samsung Android must be configured to not display the following (Work Environment) notifications when the device is locked: All notifications.

**Rule ID:** `SV-260450r950929_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Many mobile devices display notifications on the lock screen so that users can obtain relevant information in a timely manner without having to frequently unlock the phone to determine if there are new notifications. However, in many cases, these notifications can contain sensitive information. When they are available on the lock screen, an adversary can see them merely by being in close physical proximity to the device. Configuring the MOS to not send notifications to the lock screen mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #18</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices are not displaying (Work Environment) notifications when the device is locked. Notifications of incoming phone calls are acceptable even when the device is locked. This validation procedure is performed on both the management tool Administration Console and the Samsung Android device. On the management tool, in the Work profile restrictions section, verify "Unredacted Notifications" is set to "Disallow". On the Samsung Android device: 1. Open Settings >> Notifications >> Lock screen notifications. 2. Verify "Sensitive work profile notifications" is disabled. If on the management tool "Unredacted Notifications" is not set to "Disallow", or on the Samsung Android device "Sensitive work profile notifications" is not disabled, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-260451`

### Rule: Samsung Android's Work profile must be configured to prevent users from adding personal email accounts to the work email app.

**Rule ID:** `SV-260451r950932_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the user is able to add a personal email account (POP3, IMAP, EAS) to the work email app, it could be used to forward sensitive DOD data to unauthorized recipients. Restricting email account addition to the Administrator or to allowlisted accounts mitigates this vulnerability. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices are preventing users from adding personal email accounts to the work email app. On the management tool, in the device restrictions section, verify "Modify accounts" is set to "Disallow". On the Samsung Android device: 1. Open Settings >> Accounts and backup >> Manage accounts. 2. Navigate to the "Work" tab. 3. Verify no account can be added. If on the management tool "Modify accounts" is not set to "Disallow", or on the Samsung Android device an account can be added, this is a finding.

## Group: PP-MDF-333250

**Group ID:** `V-260452`

### Rule: Samsung Android's Work profile must be configured to not allow backup of all applications, configuration data to remote systems.- Disable Data Sync Framework.

**Rule ID:** `SV-260452r953767_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Backups to remote systems (including cloud backup) can leave data vulnerable to breach on the external systems, which often offer less protection than the MOS. Where the remote backup involves a cloud-based solution, the backup capability is often used to synchronize data across multiple devices. In this case, DOD devices may synchronize DOD sensitive information to a user's personal device or other unauthorized computers that are vulnerable to breach. The Data Sync Framework allows apps to synchronize data between the mobile device and other web based services. This uses accounts for services the user has added to the mobile device. Preventing the user from adding accounts to the device mitigates this risk. For BYOD Work profile data cannot be backed up remotely via Backup Services. Work profile data could be backed up thru adding an account to an app that supports the data sync framework, however, this is mitigated by preventing adding any accounts to the Work profile. SFR ID: FMT_SMF_EXT.1.1 #40</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify requirement KNOX-14-710230 (disallow modify accounts) has been implemented. If "disallow modify accounts" has not been implemented, this is a finding.

## Group: PP-MDF-333280

**Group ID:** `V-260453`

### Rule: Samsung Android's Work profile must be configured to disable exceptions to the access control policy that prevent application processes and groups of application processes from accessing all data stored by other application processes and groups of application processes.

**Rule ID:** `SV-260453r950938_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>App data sharing gives apps the ability to access the data of other apps for enhanced user functionality. However, sharing also poses a significant risk that unauthorized users or apps will obtain access to DOD sensitive information. To mitigate this risk, there are data sharing restrictions, primarily from sharing data from personal (unmanaged) apps and work (managed) apps. If a user is allowed to make exceptions to the data sharing restriction policy, the user could enable unauthorized sharing of data, leaving it vulnerable to breach. Limiting the granting of exceptions to either the Administrator or common application developer mitigates this risk. Copy/paste of data between applications in different application processes or groups of application processes is considered an exception to the access control policy and therefore, the Administrator must be able to enable/disable the feature. Other exceptions include allowing any data or application sharing between process groups. SFR ID: FMT_SMF_EXT.1.1 #42, FDP_ACF_EXT.1.2</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Samsung documentation and inspect the configuration to verify the Samsung Android devices are enabling an access control policy that prevents application processes and groups of application processes from accessing all data stored by other application processes and groups of application processes. This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the Work profile restrictions, set "Cross profile copy/paste" to "Disallow". On the Samsung Android device: 1. Using any Work app, copy text to the clipboard. 2. Using any Personal app, verify the clipboard text cannot be pasted. If on the management tool "Cross profile copy/paste" is not set to "Disallow", or on the Samsung Android device the clipboard text can be pasted into a Personal app, this is a finding.

## Group: PP-MDF-333350

**Group ID:** `V-260454`

### Rule: Samsung Android's Work profile must allow only the Administrator (management tool) to perform the following management function: Install/remove DOD root and intermediate PKI certificates.

**Rule ID:** `SV-260454r950941_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD root and intermediate PKI certificates are used to verify the authenticity of PKI certificates of users and web services. If the user is allowed to remove root and intermediate certificates, the user could allow an adversary to falsely sign a certificate in such a way that it could not be detected. Restricting the ability to remove DOD root and intermediate PKI certificates to the Administrator mitigates this risk. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices' Work profile is preventing users from removing DOD root and intermediate PKI certificates. This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the Work profile restrictions, verify "Configure credentials" is set to "Disallow". On the Samsung Android device: 1. Open Settings >> Security and privacy >> More security settings >> View security certificates. 2. In the System tab, verify no listed certificate in the Work profile can be untrusted. 3. In the User tab, verify no listed certificate in the Work profile can be removed. If on the management tool the device "Configure credentials" is not set to "Disallow", or on the Samsung Android device a certificate can be untrusted or removed, this is a finding.

## Group: PP-MDF-333050

**Group ID:** `V-260455`

### Rule: Samsung Android must be configured to enforce an application installation policy by specifying one or more authorized application repositories, including DOD-approved commercial app repository, management tool server, or mobile application store.

**Rule ID:** `SV-260455r950944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Forcing all applications to be installed from authorized application repositories can prevent unauthorized and malicious applications from being installed and executed on mobile devices. Allowing such installations and executions could cause a compromise of DOD data accessible by these unauthorized/malicious applications. SFR ID: FMT_SMF_EXT.1.1 #8a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices are disabling unauthorized application repositories. This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the Work profile restrictions, verify "installs from unknown sources globally" is set to "Disallow". On the Samsung Android device: 1. Open Settings >> Security and privacy >> More security settings >> Install unknown apps. 2. In the "Personal" tab, verify that each app listed has the status "Disabled" under the app name or no apps are listed. 3. In the "Work" tab, verify that each app listed has the status "Disabled" under the app name or no apps are listed. If on the management tool "installs from unknown sources globally" is not set to "Disallow", or on the Samsung Android device an app is listed with a status other than "Disabled", this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-260456`

### Rule: Samsung Android device users must complete required training.

**Rule ID:** `SV-260456r950947_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The security posture of Samsung devices requires the device user to configure several required policy rules on their device. User-Based Enforcement (UBE) is required for these controls. In addition, if the Authorizing Official (AO) has approved the use of an unmanaged personal space, the user must receive training on risks. If a user is not aware of their responsibilities and does not comply with UBE requirements, the security posture of the Samsung mobile device may become compromised, and DOD sensitive data may become compromised. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review a sample of site User Agreements for Samsung device users or similar training records and training course content. Verify Samsung device users have completed required training. The intent is that required training is renewed on a periodic basis in a time period determined by the AO. If any Samsung device user has not completed required training, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-260457`

### Rule: The Samsung Android device must have the latest available Samsung Android operating system (OS) installed.

**Rule ID:** `SV-260457r950950_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Required security features are not available in earlier OS versions. In addition, earlier versions may have known vulnerabilities. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to confirm if the Samsung Android devices have the most recently released version of Samsung Android installed. This procedure is performed on both the management tool and the Samsung Android device. In the management tool management console, review the version of Samsung Android installed on a sample of managed devices. This procedure will vary depending on the management tool product. Refer to the notes below to determine the latest available OS version. On the Samsung Android device, to determine the installed OS version: 1. Open Settings. 2. Tap "About phone". 3. Tap "Software information". If the installed version of Android OS on any reviewed Samsung devices is not the latest released by the wireless carrier, this is a finding. Note: Some wireless carriers list the version of the latest Android OS release by mobile device model online: ATT: https://www.att.com/devicehowto/dsm.html#!/popular/make/Samsung Verizon Wireless: https://www.verizonwireless.com/support/software-updates/ Google Android OS patch website: https://source.android.com/security/bulletin/ Samsung Android OS patch website: https://security.samsungmobile.com/securityUpdate.smsb

## Group: PP-MDF-331090

**Group ID:** `V-260458`

### Rule: Samsung Android 14 must prohibit DOD VPN profiles in the Personal Profile.

**Rule ID:** `SV-260458r950953_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If DOD VPN profiles are configured in the Personal Profile DOD sensitive data world be at risk of compromise and the DOD network could be at risk of being attacked by malware installed on the device. SFR ID: FMT_SMF_EXT.1.1 #3</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the list of VPN profiles in the Personal Profile and determine if any VPN profiles are listed. If so, verify the VPN profiles are not configured with a DOD network VPN profile. If any VPN profiles are installed in the Personal Profile and they have a DOD network VPN profile configured, this is a finding. Note: This setting cannot be managed by the MDM administrator and is a User-Based Enforcement (UBE) requirement.

## Group: PP-MDF-993300

**Group ID:** `V-260459`

### Rule: The Samsung Android device must be configured to enable Certificate Revocation List (CRL) status checking.

**Rule ID:** `SV-260459r950956_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A CRL allows a certificate issuer to revoke a certificate for any reason, including improperly issued certificates and compromise of the private keys. Checking the revocation status of the certificate mitigates the risk associated with using a compromised certificate. For this reason, users must not be able to disable this configuration. Samsung Android can control CRL checking but only using Knox APIs. Alternatively, CRL checking is based on app development best practice. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to confirm that revocation checking is enabled. Verify the revocation checklist is set to "All Applications". This procedure is performed on the management tool. On the management tool: 1. Open Certificates Policy >> Revocation section. 2. Select "Get CRL". 3. Verify Toast message "Get revocation check: true". If on the management tool the revocation check is disabled, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-260460`

### Rule: The Samsung Android device work profile must be configured to enforce the system application disable list.

**Rule ID:** `SV-260460r950959_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The system application disable list controls user access to/execution of all core and preinstalled applications. Core application: Any application integrated into Samsung Android 14 by Samsung. Preinstalled application: Additional noncore applications included in the Samsung Android 14 build by Samsung or the wireless carrier. Some system applications can compromise DOD data or upload users' information to non-DOD-approved servers. A user must be blocked from using such applications that exhibit behavior that can result in compromise of DOD data or DOD user information. The site administrator must analyze all preinstalled applications on the device and disable all applications not approved for DOD use by configuring the system application disable list. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to confirm the system application disable list is enforced. This setting is enforced by default. Verify only approved system apps have been placed on the core allowlist. This procedure is performed on the management tool. Review the system app allowlist and verify only approved apps are on the list. On the management tool, in the Apps management section, select "Unhide apps" and verify the names of the apps listed. If on the management tool the system app allowlist contains unapproved core apps, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-260461`

### Rule: The Samsung Android device work profile must be configured to disable automatic completion of workspace internet browser text input.

**Rule ID:** `SV-260461r950962_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The autofill functionality in the web browser allows the user to complete a form that contains sensitive information, such as personally identifiable information (PII), without previous knowledge of the information. By allowing the use of autofill functionality, an adversary who learns a user's Android 14 device password, or who otherwise is able to unlock the device, may be able to further breach other systems by relying on the autofill feature to provide information unknown to the adversary. By disabling the autofill functionality, the risk of an adversary gaining further information about the device's user or compromising other systems is significantly mitigated. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the work profile Chrome Browser app on the Samsung Android 14 autofill setting. This validation procedure is performed on the management tool. On the management tool: 1. Open "Managed Configurations" section. 2. Select the Chrome Browser version from the work profile. 3. Verify "PasswordManagerEnabled" is turned "OFF". 4. Verify "AutofillAddressEnabled" is turned "OFF". 5. Verify "AutofillCreditCardEnabled" is turned "OFF". If on the management tool any of the browser autofill settings are set to "On" in the Chrome Browser Settings, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-260462`

### Rule: The Samsung Android device work profile must be configured to disable the autofill services.

**Rule ID:** `SV-260462r950965_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The autofill services allow the user to complete text inputs that could contain sensitive information, such as personally identifiable information (PII), without previous knowledge of the information. By allowing the use of autofill services, an adversary who learns a user's Android 14 device password, or who otherwise is able to unlock the device, may be able to further breach other systems by relying on the autofill services to provide information unknown to the adversary. By disabling the autofill services, the risk of an adversary gaining further information about the device's user or compromising other systems is significantly mitigated. Examples of apps that offer autofill services include Samsung Pass, Google, Dashlane, LastPass, and 1Password. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Samsung Android 14 work profile configuration settings to confirm that autofill services are disabled. This validation procedure is performed on the management tool. On the management tool: 1. Open "Set user restrictions". 2. Verify "Disable autofill" is toggled to "ON". If on the management tool the "disallow autofill" is not selected, this is a finding.

## Group: PP-MDF-993300

**Group ID:** `V-260463`

### Rule: The Samsung Android device must be configured to disable the use of third-party keyboards.

**Rule ID:** `SV-260463r950968_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Many third-party keyboard applications are known to contain malware. SFR ID: FMT_SMF_EXT.1.1 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the managed Samsung Android 14 configuration settings to confirm that no third-party keyboards are enabled. This procedure is performed on the management tool. On the management tool: 1. Open "Input methods". 2. Tap "Set input methods". 3. Verify only the approved keyboards are selected. If third-party keyboards are allowed, this is a finding.

