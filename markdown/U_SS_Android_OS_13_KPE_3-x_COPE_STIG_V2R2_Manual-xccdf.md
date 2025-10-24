# STIG Benchmark: Samsung Android OS 13 with Knox 3.x COPE Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: PP-MDF-990000

**Group ID:** `V-255137`

### Rule: Samsung Android must be enrolled as a COPE device.

**Rule ID:** `SV-255137r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Work profile is the designated application group for the COPE use case. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices are enrolled in a DOD-approved use case. This validation procedure is performed on both the management tool Administration Console and the Samsung Android device. On the management tool, verify that the default enrollment is set to "Work profile for company-owned devices". On the Samsung Android device: 1. Open Settings >> Security and privacy >> Other security settings >> Device admin apps. 2. Verify that the management tool Agent is listed. 3. Go to the app drawer. 4. Verify that a "Personal" and "Work" tab are present. If on the management tool the default enrollment is not set as "Work profile for company-owned devices", or on the Samsung Android device the "Personal" and "Work" tabs are not present or the management tool Agent is not listed, this is a finding.

## Group: PP-MDF-323160

**Group ID:** `V-255138`

### Rule: Samsung Android must be configured to display the DOD advisory warning message at startup or each time the user unlocks the device.

**Rule ID:** `SV-255138r958390_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Before granting access to the system, the mobile operating system is required to display the DOD-approved system use notification message or banner that provides privacy and security notices consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. Required banners help ensure that DOD can audit and monitor the activities of mobile device users without legal restriction. System use notification messages can be displayed when individuals first access or unlock the mobile device. The banner must be implemented as a "click-through" banner at device unlock (to the extent permitted by the operating system). A "click-through" banner prevents further activity on the information system unless and until the user executes a positive action to manifest agreement by clicking on a box indicating "OK." The approved DOD text must be used exactly as required in the Knowledge Service referenced in DODI 8500.01. For devices accommodating banners of 1300 characters, the banner text is: You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE, or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. For devices with severe character limitations, the banner text is: I've read & consent to terms in IS user agreem't. The administrator must configure the banner text exactly as written without any changes. SFR ID: FMT_SMF_EXT.1.1 #36</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm if Method #1 or #2 is used at the Samsung device site and follow the appropriate procedure. This validation procedure is performed on both the management tool and the Samsung Android device. Validation procedure for method #1: Place the DOD warning banner in the user agreement signed by each Samsung Android device user (preferred method). Review the signed user agreements for several Samsung Android device users and verify that the agreement includes the required DOD warning banner text. Validation procedure for method #2: Configure the warning banner text in the Lock screen message on each managed mobile device. On the management tool, in the device restrictions section, verify that "Lock Screen Message" is set to the DOD-mandated warning banner text. On the Samsung Android device, verify that the required DOD warning banner text is displayed on the Lock screen. If the warning text has not been placed in the signed user agreement, or if on the management tool "Lock Screen Message" is not set to the DOD-mandated warning banner text, or on the Samsung Android device the required DOD warning banner text is not displayed on the Lock screen, this is a finding.

## Group: PP-MDF-323025

**Group ID:** `V-255139`

### Rule: Samsung Android must be configured to not allow passwords that include more than four repeating or sequential characters.

**Rule ID:** `SV-255139r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password strength is a measure of the effectiveness of a password in resisting guessing and brute force attacks. Passwords that contain repeating or sequential characters are significantly easier to guess than those that do not contain repeating or sequential characters. Therefore, disallowing repeating or sequential characters increases password strength and decreases risk. SFR ID: FMT_SMF_EXT.1.1 #1b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices are disallowing passwords containing more than four repeating or sequential characters. This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the device password policies, verify "minimum password quality" is set to "Numeric(Complex)" or better. On the Samsung Android device: 1. Open Settings >> Lock screen >> Screen lock type. 2. Enter current password. 3. Tap "PIN". 4. Verify that PINS with more than four repeating or sequential numbers are not accepted. If on the management tool "minimum password quality" is not set to "Numeric(Complex)" or better, or on the Samsung Android device a password with more than four repeating or sequential numbers is accepted, this is a finding.

## Group: PP-MDF-323026

**Group ID:** `V-255140`

### Rule: Samsung Android must be configured to enable a screen-lock policy that will lock the display after a period of inactivity.

**Rule ID:** `SV-255140r958402_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The screen-lock timeout helps protect the device from unauthorized access. Devices without a screen-lock timeout provide an opportunity for adversaries who gain physical access to the mobile device through loss, theft, etc. Such devices are much more likely to be in an unlocked state when acquired by an adversary, thus granting immediate access to the data on the mobile device and possibly access to DOD networks. SFR ID: FMT_SMF_EXT.1.1 #2a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify requirement KNOX-13-210030 (minimum password quality) has been implemented. If a "minimum password quality" has not been implemented, this is a finding.

## Group: PP-MDF-323024

**Group ID:** `V-255141`

### Rule: Samsung Android must be configured to enforce a minimum password length of six characters.

**Rule ID:** `SV-255141r1015809_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password strength is a measure of the effectiveness of a password in resisting guessing and brute force attacks. The ability to crack a password is a function of how many attempts an adversary is permitted, how quickly an adversary can do each attempt, and the size of the password space. The longer the minimum length of the password is, the larger the password space. Having a too-short minimum password length significantly reduces password strength, increasing the chance of password compromise and resulting device and data compromise. SFR ID: FMT_SMF_EXT.1.1 #1a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices are enforcing a minimum password length of six characters. This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the device password policies, verify "minimum password length" is set to "6". On the Samsung Android device: 1. Open Settings >> Lock screen >> Screen lock type. 2. Enter current password. 3. Tap "PIN". 4. Verify the text "PIN must contain at least", followed by a value of at least "6 digits", appears above the PIN entry. If on the management tool "minimum password length" is not set to "6", or on the Samsung Android device the text "PIN must contain at least" is followed by a value of less than "6 digits", this is a finding.

## Group: PP-MDF-323040

**Group ID:** `V-255142`

### Rule: Samsung Android must be configured to not allow more than 10 consecutive failed authentication attempts.

**Rule ID:** `SV-255142r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The more attempts an adversary has to guess a password, the more likely the adversary will enter the correct password and gain access to resources on the device. Setting a limit on the number of attempts mitigates this risk. Setting the limit at 10 or less gives authorized users the ability to make a few mistakes when entering the password but still provides adequate protection against dictionary or brute force attacks on the password. SFR ID: FMT_SMF_EXT.1.1 #2c, FIA_AFL_EXT.1.5</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices are allowing only 10 or fewer consecutive failed authentication attempts. This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the device password policies, verify "max password failures for local wipe" is set to "10" attempts or less. On the Samsung Android device: 1. Open Settings >> Lock screen. 2. Verify "Secure lock settings" is present and tap it. 3. Enter current password. 4. Verify that "Auto factory reset" is greyed out, and cannot be configured. Note: When "Auto factory reset" is greyed out, this indicates the Administrator (MDM) is in control of the setting to wipe the device after 10 or fewer consecutive failed authentication attempts. If on the management tool "max password failures for local wipe" is not set to "10" attempts or less, or on the Samsung Android device the "Auto factory reset" menu can be configured, this is a finding.

## Group: PP-MDF-323030

**Group ID:** `V-255143`

### Rule: Samsung Android must be configured to lock the display after 15 minutes (or less) of inactivity.

**Rule ID:** `SV-255143r958402_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The screen lock timeout must be set to a value that helps protect the device from unauthorized access. Having a too-long timeout would increase the window of opportunity for adversaries who gain physical access to the mobile device through loss, theft, etc. Such devices are much more likely to be in an unlocked state when acquired by an adversary, thus granting immediate access to the data on the mobile device. The maximum timeout period of 15 minutes has been selected to balance functionality and security; shorter timeout periods may be appropriate depending on the risks posed to the mobile device. SFR ID: FMT_SMF_EXT.1.1 #2b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices are locking the device display after 15 minutes (or less) of inactivity. This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the device password policies, verify "max time to screen lock" is set to "15 minutes" or less. On the Samsung Android device: 1. Open Settings >> Lock screen. 2. Verify "Secure lock settings" is present and tap it. 3. Enter current password. 4. Tap "Auto lock when screen turns off". 5. Verify the listed timeout values are 15 minutes or less. If on the management tool "max time to screen lock" is not set to "15 minutes" or less, or on the Samsung Android device "Secure lock settings" is not present and the listed Screen timeout values include durations of more than 15 minutes, this is a finding.

## Group: PP-MDF-323110

**Group ID:** `V-255144`

### Rule: Samsung Android must be configured to disable authentication mechanisms providing user access to protected data other than a Password Authentication Factor, including face recognition.

**Rule ID:** `SV-255144r1015810_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The biometric factor can be used to authenticate the user to unlock the mobile device. Unapproved/evaluated biometric mechanisms could allow unauthorized users to have access to DOD sensitive data if compromised. By not permitting the use of unapproved/evaluated biometric authentication mechanisms, this risk is mitigated. SFR ID: FMT_SMF_EXT.1.1 #22, FIA_UAU.5.1</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices are disabling Face Recognition. This validation procedure is performed on both the management tool and the Samsung Android device. If a KPE premium license is activated, Facial Recognition will be automatically disabled. Otherwise, on the management tool in the device restrictions, verify "Face recognition" is set to "Disable". On the Samsung Android device: 1. Open Settings >> Lock screen >> Screen lock type. 2. Enter current password. 3. Verify "Face" is disabled and cannot be enabled. If on the management tool a KPE premium license is not activated and "Face Recognition" is not set to "Disable", or on the Samsung Android device "Face" can be enabled, this is a finding.

## Group: PP-MDF-323030

**Group ID:** `V-255145`

### Rule: Samsung Android must be configured to enable a screen-lock policy that will lock the display after a period of inactivity - Disable trust agents.

**Rule ID:** `SV-255145r1015811_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The screen lock timeout must be set to a value that helps protect the device from unauthorized access. Having a too-long timeout would increase the window of opportunity for adversaries who gain physical access to the mobile device through loss, theft, etc. Such devices are much more likely to be in an unlocked state when acquired by an adversary, thus granting immediate access to the data on the mobile device. The maximum timeout period of 15 minutes has been selected to balance functionality and security; shorter timeout periods may be appropriate depending on the risks posed to the mobile device. SFR ID: FMT_SMF_EXT.1.1 #2a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices are disabling Trust Agents. This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the device restrictions, verify that "Trust Agents" are set to "Disable". On the Samsung Android device: 1. Open Settings >> Security and privacy >> Other security settings >> Trust agents. 2. Verify that all listed Trust Agents are disabled and cannot be enabled. If a Trust Agent is not disabled in the list, verify for that Trust Agent, all of its listed Trustlets are disabled and cannot be enabled. If on the management tool "Trust Agents" are not set to "Disable", or on the Samsung Android device a "Trust Agent" or "Trustlet" can be enabled, this is a finding. Note: If the management tool has been correctly configured but a Trust Agent is still enabled, configure the "List of approved apps listed in managed Google Play" to disable it; refer to KNOX-13-210190. Exception: Trust Agents may be used if the AO allows a screen lock timeout after four hours (or more) of inactivity. This may be applicable to tactical use case.

## Group: PP-MDF-323130

**Group ID:** `V-255146`

### Rule: Samsung Android must be configured to disable developer modes.

**Rule ID:** `SV-255146r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Developer modes expose features of the MOS that are not available during standard operation. An adversary may leverage a vulnerability inherent in a developer mode to compromise the confidentiality, integrity, and availability of DOD sensitive information. Disabling developer modes mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #26</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configure to determine if the Samsung Android devices are disabling developer modes. This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the device restrictions, verify that "Debugging Features" is set to "Disallow". On the Samsung Android device: 1. Open Settings >> About phone >> Software information. 2. Tap on the Build Number to try to enable Developer Options and validate that action is blocked. If on the management tool "Debugging Features" is not set to "Disallow" or on the Samsung Android device "Developer options" action is not blocked, this is a finding.

## Group: PP-MDF-323320

**Group ID:** `V-255147`

### Rule: Samsung Android must be configured to disable all Bluetooth profiles except for HSP (Headset Profile), HFP (Hands-Free Profile), SPP (Serial Port Profile), A2DP (Advanced Audio Distribution Profile), AVRCP (Audio/Video Remote Control Profile), and PBAP (Phone Book Access Profile).

**Rule ID:** `SV-255147r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Some Bluetooth profiles provide the capability for remote transfer of sensitive DOD data without encryption or otherwise do not meet DOD IT security policies and therefore must be disabled. SFR ID: FMT_SMF_EXT.1.1/BLUETOOTH BT-8</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Samsung documentation and inspect the configuration to verify the Samsung Android devices are paired only with devices which support HSP, HFP, SPP, A2DP, AVRCP, and PBAP Bluetooth profiles. This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the device restrictions section, verify "Bluetooth" is set to the AO-approved selection; "Allow" - if the AO has approved the use of Bluetooth - or "Disallow", if not. On the Samsung Android device: 1. Open Settings >> Connections >> Bluetooth. 2. Verify that all listed paired Bluetooth devices use only authorized Bluetooth profiles. If on the management tool "Bluetooth" is not set to the AO-approved value, or the Samsung Android device is paired with a device that uses unauthorized Bluetooth profiles, this is a finding.

## Group: PP-MDF-323100

**Group ID:** `V-255148`

### Rule: Samsung Android must be configured to enable encryption for data at rest on removable storage media or, alternately, the use of removable storage media must be disabled.

**Rule ID:** `SV-255148r958552_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The MOS must ensure the data being written to the mobile device's removable media is protected from unauthorized access. If data at rest is unencrypted, it is vulnerable to disclosure. Even if the operating system enforces permissions on data access, an adversary can read removable media directly, thereby circumventing operating system controls. Encrypting the data ensures confidentiality is protected even when the operating system is not running. SFR ID: FMT_SMF_EXT.1.1 #20, #47d</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Configure the Samsung Android devices to enable data at rest protection for removable media, or alternatively, disable their use. This requirement is not applicable for devices that do not support removable storage media. On the management tool, in the device restrictions, set "Mount physical media" to "Disallow". This disables the use of all removable storage, e.g., micro SD cards, USB thumb drives, etc. If the deployment requires the use of micro SD cards, KPE can be used to allow its usage in a STIG-approved configuration. In this case, do not configure the policy above, and instead: On the management tool, in the device restrictions, set "Enforce external storage encryption" to "enable".

## Group: PP-MDF-323230

**Group ID:** `V-255149`

### Rule: Samsung Android must be configured to disable USB mass storage mode.

**Rule ID:** `SV-255149r958478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>USB mass storage mode enables the transfer of data and software from one device to another. This software can include malware. When USB mass storage is enabled on a mobile device, it becomes a potential vector for malware and unauthorized data exfiltration. Prohibiting USB mass storage mode mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #39</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices are disabling USB mass storage mode. This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the device restrictions, verify that "USB file transfer" has been set to "Disallow". On the Samsung Android device, from the USB settings notification, verify that a "File Transfer" is not an option. If on the management tool "USB file transfer" is not set to "Disallow", or on the Samsung Android device a "File Transfer" is an option, this is a finding.

## Group: PP-MDF-323240

**Group ID:** `V-255150`

### Rule: Samsung Android must be configured to not allow backup of all applications and configuration data to locally connected systems.

**Rule ID:** `SV-255150r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data on mobile devices is protected by numerous mechanisms, including user authentication, access control, and cryptography. When the data is backed up to an external system (either locally connected or cloud based), many if not all of these mechanisms are no longer present. This leaves the backed-up data vulnerable to attack. Disabling backup to external systems mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #40</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify requirement KNOX-13-210140 (Disallow USB file transfer) has been implemented. If "Disallow USB file transfer" has not been implemented, this is a finding.

## Group: PP-MDF-323260

**Group ID:** `V-255151`

### Rule: Samsung Android must be configured to enable authentication of personal hotspot connections to the device using a pre-shared key.

**Rule ID:** `SV-255151r958672_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If no authentication is required to establish personal hotspot connections, an adversary may be able to use that device to perform attacks on other devices or networks without detection. A sophisticated adversary may also be able to exploit unknown system vulnerabilities to access information and computing resources on the device. Requiring authentication to establish personal hotspot connections mitigates this risk. Application note: If hotspot functionality is permitted, it must be authenticated via a preshared key. There is no requirement to enable hotspot functionality, and it is recommended this functionality be disabled by default. SFR ID: FMT_SMF_EXT.1.1 #41</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Configure the Samsung Android devices to enable authentication of personal hotspot connections to the device using a pre-shared key. On the management tool in the device restrictions, set "Configure tethering" to "Disallow". If the deployment requires the use of Mobile Hotspot and Tethering, KPE policy can be used to allow its usage in a STIG-approved configuration. In this case, do not configure the policy above, and instead: On the management tool, in the device Wi-Fi section, set "Unsecured hotspot" to "Disallow" and add Training Topic "Don't use Wi-Fi Sharing" (see supplemental document for additional information).

## Group: PP-MDF-990000

**Group ID:** `V-255152`

### Rule: Samsung Android must be configured to disallow configuration of the device's date and time.

**Rule ID:** `SV-255152r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Determining the correct time a particular application event occurred on a system is critical when conducting forensic analysis and investigating system events. Periodically synchronizing internal clocks with an authoritative time source is needed to correctly correlate the timing of events that occur across the enterprise. The three authoritative time sources for Samsung Android are an authoritative time server that is synchronized with redundant United States Naval Observatory (USNO) time servers as designated for the appropriate DOD network (NIPRNet or SIPRNet), the Global Positioning System (GPS), or the wireless carrier. Time stamps generated by the audit system in Samsung Android must include both date and time. The time may be expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices are disallowing the users from changing the date and time. This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the device restrictions, verify that "Configure Date/Time" is set to "Disallow". On the Samsung Android device: 1. Open Settings >> General management >> Date and time. 2. Verify that "Automatic data and time" is on and the user cannot disable it. If on the management tool "Configure Date/Time" is not set to "Disallow", or on the Samsung Android device "Automatic date and time" is not set or the user can disable it, this is a finding.

## Group: PP-MDF-990000

**Group ID:** `V-255153`

### Rule: Samsung Android's Work profile must have the DOD root and intermediate PKI certificates installed.

**Rule ID:** `SV-255153r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD root and intermediate PKI certificates are used to verify the authenticity of PKI certificates of users and web services. If the root and intermediate certificates are not available, an adversary could falsely sign a certificate in such a way that it could not be detected. Providing access to the DOD root and intermediate PKI certificates greatly diminishes the risk of this attack. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android's Work profile has the DOD root and intermediate PKI certificates installed. This validation procedure is performed on both the management tool and the Samsung Android device. The current DOD root and intermediate PKI certificates may be obtained in self-extracting zip files at https://cyber.mil/pki-pke (for NIPRNet). On the management tool, in the Work profile policy management, verify that the DOD root and intermediate PKI certificates are installed. On the Samsung Android device: 1. Open Settings >> Security and privacy >> Other security settings >> View security certificates. 2. In the User tab, verify that the DOD root and intermediate PKI certificates are listed in the Work profile. If on the management tool the DOD root and intermediate PKI certificates are not listed in the Work profile, or on the Samsung Android device the DOD root and intermediate PKI certificates are not listed in the Work profile, this is a finding.

## Group: PP-MDF-323060

**Group ID:** `V-255154`

### Rule: Samsung Android's Work profile must be configured to enforce an application installation policy by specifying an application allowlist that restricts applications by the following characteristics: Names.

**Rule ID:** `SV-255154r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The application allowlist, in addition to controlling the installation of applications on the MD, must control user access/execution of all core and preinstalled applications, or the MD must provide an alternate method of restricting user access/execution to core and preinstalled applications. Core application: Any application integrated into the OS by the OS or MD vendors. Preinstalled application: Additional noncore applications included in the OS build by the OS vendor, MD vendor, or wireless carrier. Requiring all authorized applications to be in an application allowlist prevents the execution of any applications (e.g., unauthorized, malicious) that are not part of the allowlist. Failure to configure an application allowlist properly could allow unauthorized and malicious applications to be downloaded, installed, and executed on the mobile device, causing a compromise of DOD data accessible by these applications. The application allowlist, in addition to controlling the installation of applications on the MD, must control user access/execution of all core applications (included in the OS by the OS vendor) and preinstalled applications (provided by the MD vendor and wireless carrier), or the MD must provide an alternate method of restricting user access/execution to core and preinstalled applications. SFR ID: FMT_SMF_EXT.1.1 #8b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Work profile on the Samsung Android device is allowing users to install only applications that have been approved by the Authorizing Official (AO). This validation procedure is performed only on the management tool. On the management tool, in the app catalog for managed Google Play, verify that only AO-approved apps are available. If on the management tool the app catalog for managed Google Play includes non-AO-approved apps, this is a finding.

## Group: PP-MDF-323070

**Group ID:** `V-255155`

### Rule: Samsung Android's Work profile must be configured to not allow installation of applications with the following characteristics: 

- Back up MD data to non-DOD cloud servers (including user and application access to cloud backup services);
- Transmit MD diagnostic data to non-DOD servers;
- Voice assistant application if available when MD is locked;
- Voice dialing application if available when MD is locked;
- Allows synchronization of data or applications between devices associated with user; and
- Allows unencrypted (or encrypted but not FIPS 140-2 validated) data sharing with other MDs or printers.

**Rule ID:** `SV-255155r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Requiring all authorized applications to be in an application allowlist prevents the execution of any applications (e.g., unauthorized, malicious) that are not part of the allowlist. Failure to configure an application allowlist properly could allow unauthorized and malicious applications to be downloaded, installed, and executed on the mobile device, causing a compromise of DOD data accessible by these applications. Applications with the listed characteristics have features that can cause the compromise of sensitive DOD data or have features with no known application in the DOD environment. Application note: The application allowlist, in addition to controlling the installation of applications on the MD, must control user access/execution of all core and preinstalled applications, or the MD must provide an alternate method of restricting user access/execution to core and preinstalled applications. Core application: Any application integrated into the OS by the OS or MD vendors. Preinstalled application: Additional noncore applications included in the OS build by the OS vendor, MD vendor, or wireless carrier. SFR ID: FMT_SMF_EXT.1.1 #8b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify requirement KNOX-13-210190 (managed Google Play) has been implemented. If "managed Google Play" has not been implemented, this is a finding.

## Group: PP-MDF-323080

**Group ID:** `V-255156`

### Rule: Samsung Android must be configured to not display the following (Work Environment) notifications when the device is locked: All notifications.

**Rule ID:** `SV-255156r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Many mobile devices display notifications on the lock screen so that users can obtain relevant information in a timely manner without having to frequently unlock the phone to determine if there are new notifications. However, in many cases, these notifications can contain sensitive information. When they are available on the lock screen, an adversary can see them merely by being in close physical proximity to the device. Configuring the MOS to not send notifications to the lock screen mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #18</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices are not displaying (Work Environment) notifications when the device is locked. Notifications of incoming phone calls are acceptable even when the device is locked. This validation procedure is performed on both the management tool Administration Console and the Samsung Android device. On the management tool, in the Work profile restrictions section, verify that "Unredacted Notifications" is set to "Disallow". On the Samsung Android device: 1. Open Settings >> Lock screen >> Notifications. 2. Verify that "Sensitive work profile notifications" is disabled. If on the management tool "Unredacted Notifications" is not set to "Disallow", or on the Samsung Android device "Sensitive work profile notifications" is not disabled, this is a finding.

## Group: PP-MDF-990000

**Group ID:** `V-255157`

### Rule: Samsung Android's Work profile must be configured to enable audit logging.

**Rule ID:** `SV-255157r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit logs enable monitoring of security-relevant events and subsequent forensics when breaches occur. They help identify attacks so that breaches can either be prevented or limited in their scope. They facilitate analysis to improve performance and security. The Requirement Statement lists key events for which the system must generate an audit record. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices' Work profile is enabling audit logging. This validation procedure is performed on the management tool only. On the management tool, in the Work profile restrictions, verify that "Security logging" is set to "Enable". If on the management tool "Security logging" is not set to "Enable", this is a finding.

## Group: PP-MDF-990000

**Group ID:** `V-255158`

### Rule: Samsung Android's Work profile must be configured to prevent users from adding personal email accounts to the work email app.

**Rule ID:** `SV-255158r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the user is able to add a personal email account (POP3, IMAP, EAS) to the work email app, it could be used to forward sensitive DOD data to unauthorized recipients. Restricting email account addition to the Administrator or to allowlisted accounts mitigates this vulnerability. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices are preventing users from adding personal email accounts to the work email app. On the management tool, in the device restrictions section, verify "Modify accounts" is set to "Disallow". On the Samsung Android device: 1. Open Settings >> Accounts and backup >> Manage accounts. 2. Navigate to the "Work" tab. 3. Verify that no account can be added. If on the management tool "Modify accounts" is not set to "Disallow", or on the Samsung Android device an account can be added, this is a finding.

## Group: PP-MDF-323250

**Group ID:** `V-255159`

### Rule: Samsung Android's Work profile must be configured to not allow backup of all applications, configuration data to remote systems.

- Disable Data Sync Framework.

**Rule ID:** `SV-255159r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Backups to remote systems (including cloud backup) can leave data vulnerable to breach on the external systems, which often offer less protection than the MOS. Where the remote backup involves a cloud-based solution, the backup capability is often used to synchronize data across multiple devices. In this case, DOD devices may synchronize DOD sensitive information to a user's personal device or other unauthorized computers that are vulnerable to breach. The Data Sync Framework allows apps to synchronize data between the mobile device and other web based services. This uses accounts for those services that the user has added to the mobile device. Preventing the user from adding accounts to the device mitigates this risk. SFR ID: FMT_SMF_EXT.1.1 #40</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify requirement KNOX-13-210230 (Disallow modify accounts) has been implemented. If "Disallow modify accounts" has not been implemented, this is a finding.

## Group: PP-MDF-323280

**Group ID:** `V-255160`

### Rule: Samsung Android's Work profile must be configured to disable exceptions to the access control policy that prevent application processes, and groups of application processes from accessing all data stored by other application processes, and groups of application processes.

**Rule ID:** `SV-255160r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>App data sharing gives apps the ability to access the data of other apps for enhanced user functionality. However, sharing also poses a significant risk that unauthorized users or apps will obtain access to DOD sensitive information. To mitigate this risk, there are data sharing restrictions, primarily from sharing data from personal (unmanaged) apps and work (managed) apps. If a user is allowed to make exceptions to the data sharing restriction policy, the user could enable unauthorized sharing of data, leaving it vulnerable to breach. Limiting the granting of exceptions to either the Administrator or common application developer mitigates this risk. Copy/paste of data between applications in different application processes or groups of application processes is considered an exception to the access control policy and therefore, the Administrator must be able to enable/disable the feature. Other exceptions include allowing any data or application sharing between process groups. SFR ID: FMT_SMF_EXT.1.1 #42, FDP_ACF_EXT.1.2</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Samsung documentation and inspect the configuration to verify the Samsung Android devices are enabling an "access control policy" that prevents "application processes, and groups of application processes from accessing all data stored by other application processes, and groups of application processes". This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the Work profile restrictions, set "Cross profile copy/paste" to "Disallow". On the Samsung Android device: 1. Using any Work app, copy text to the clipboard. 2. Using any Personal app, verify that the clipboard text cannot be pasted. If on the management tool "Cross profile copy/paste" is not set to "Disallow", or on the Samsung Android device the clipboard text can be pasted into a Personal app, this is a finding.

## Group: PP-MDF-323350

**Group ID:** `V-255161`

### Rule: Samsung Android's Work profile must allow only the Administrator (management tool) to perform the following management function: Install/remove DOD root and intermediate PKI certificates.

**Rule ID:** `SV-255161r970707_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD root and intermediate PKI certificates are used to verify the authenticity of PKI certificates of users and web services. If the user is allowed to remove root and intermediate certificates, the user could allow an adversary to falsely sign a certificate in such a way that it could not be detected. Restricting the ability to remove DOD root and intermediate PKI certificates to the Administrator mitigates this risk. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices' Work profile is preventing users from removing DOD root and intermediate PKI certificates. This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the Work profile restrictions, verify that "Configure credentials" is set to "Disallow". On the Samsung Android device: 1. Open Settings >> Security and privacy >> Other security settings >> View security certificates. 2. In the System tab, verify that no listed certificate in the Work profile can be untrusted. 3. In the User tab, verify that no listed certificate in the Work profile can be removed. If on the management tool the device "Configure credentials" is not set to "Disallow", or on the Samsung Android device a certificate can be untrusted or removed, this is a finding.

## Group: PP-MDF-323050

**Group ID:** `V-255162`

### Rule: Samsung Android must be configured to enforce an application installation policy by specifying one or more authorized application repositories, including DOD-approved commercial app repository, management tool server, or mobile application store.

**Rule ID:** `SV-255162r959010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Forcing all applications to be installed from authorized application repositories can prevent unauthorized and malicious applications from being installed and executed on mobile devices. Allowing such installations and executions could cause a compromise of DOD data accessible by these unauthorized/malicious applications. SFR ID: FMT_SMF_EXT.1.1 #8a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices are disabling unauthorized application repositories. This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the Work profile restrictions, verify that "installs from unknown sources globally" is set to "Disallow". On the Samsung Android device: 1. Open Settings >> Security and privacy >> Install unknown apps. 2. In the "Personal" tab, ensure that each app listed has the status "Disabled" under the app name or that no apps are listed. 3. In the "Work" tab, ensure that each app listed has the status "Disabled" under the app name or that no apps are listed. If on the management tool "installs from unknown sources globally" is not set to "Disallow", or on the Samsung Android device an app is listed with a status other than "Disabled", this is a finding.

## Group: PP-MDF-990000

**Group ID:** `V-255163`

### Rule: Samsung Android's Work profile must be configured to enable Common Criteria (CC) mode.

**Rule ID:** `SV-255163r959010_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The CC Mode feature is a superset of other features and behavioral changes that are mandatory MDFPP requirements. If CC mode is not implemented the device will not be operating in the NIAP-certified compliant CC Mode of operation. When enforcing AE CC mode on a Samsung Android device, additional Samsung specific security features are also enabled. CC Mode implements the following behavioral/functional changes to meet MDFPP requirements: - How the Bluetooth and Wi-Fi keys are stored using different types of encryption. - Download Mode is disabled and all updates will occur via FOTA only. In addition, CC Mode adds new restrictions, which are not to meet MDFPP requirements, but to offer better security above what is required: - Force password info following FOTA update for consistency. - Disable Remote unlock by FindMyMobile. - Restrict biometric attempts to 10 for better security. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if the Samsung Android devices are enabling CC mode. This validation procedure is performed on both the management tool and the Samsung Android device. On the management tool, in the Work profile restrictions, verify that "Common Criteria mode" is set to "Enable". On the Samsung Android device, put the device into "Download mode" and verify that the text "Blocked by CC Mode" is displayed on the screen. If on the management tool "Common Criteria mode" is not set to "Enable", or on the Samsung Android device the text "Blocked by CC Mode" is not displayed in "Download mode", this is a finding.

## Group: PP-MDF-321080

**Group ID:** `V-255164`

### Rule: Samsung Android must not accept the certificate when it cannot establish a connection to determine the validity of a certificate.

**Rule ID:** `SV-255164r959026_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Certificate-based security controls depend on the ability of the system to verify the validity of a certificate. If the MOS were to accept an invalid certificate, it could take unauthorized actions, resulting in unanticipated outcomes. At the same time, if the MOS were to disable functionality when it could not determine the validity of the certificate, this could result in a denial of service. Therefore, the ability to provide exceptions is appropriate to balance the tradeoff between security and functionality. Always accepting certificates when they cannot be determined to be valid is the most extreme exception policy and is not appropriate in the DOD context. Involving an Administrator or user in the exception decision mitigates this risk to some degree. SFR ID: FIA_X509_EXT_2.2</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify requirement KNOX-13-210280 (Common Criteria mode) has been implemented. If "Common Criteria mode" has not been implemented, this is a finding.

## Group: PP-MDF-990000

**Group ID:** `V-255165`

### Rule: Samsung Android device users must complete required training.

**Rule ID:** `SV-255165r1042497_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The security posture of Samsung devices requires the device user to configure several required policy rules on their device. User Based Enforcement (UBE) is required for these controls. In addition, if the authorizing official (AO) has approved the use of an unmanaged personal space, the user must receive training on risks. If a user is not aware of their responsibilities and does not comply with UBE requirements, the security posture of the Samsung mobile device may become compromised, and DOD sensitive data may become compromised. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review a sample of site User Agreements of Samsung device users or similar training records and training course content. Verify that Samsung device users have completed required training. The intent is that required training is renewed on a periodic basis in a time period determined by the AO. If any Samsung device user has not completed required training, this is a finding.

## Group: PP-MDF-990000

**Group ID:** `V-255166`

### Rule: The Samsung Android device must have the latest available Samsung Android operating system (OS) installed.

**Rule ID:** `SV-255166r959010_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Required security features are not available in earlier OS versions. In addition, earlier versions may have known vulnerabilities. SFR ID: FMT_MOF_EXT.1.2 #47</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to confirm if the Samsung Android devices have the most recently released version of Samsung Android is installed. This procedure is performed on both the management tool and the Samsung Android device. In the management tool management console, review the version of Samsung Android installed on a sample of managed devices. This procedure will vary depending on the management tool product. See the notes below to determine the latest available OS version. On the Samsung Android device, to see the installed OS version: 1. Open Settings. 2. Tap "About phone". 3. Tap "Software information". If the installed version of Android OS on any reviewed Samsung devices is not the latest released by the wireless carrier, this is a finding. Note: Some wireless carriers list the version of the latest Android OS release by mobile device model online: ATT: https://www.att.com/devicehowto/dsm.html#!/popular/make/Samsung T-Mobile: https://support.t-mobile.com/docs/DOC-34510 Verizon Wireless: https://www.verizonwireless.com/support/software-updates/ Google Android OS patch website: https://source.android.com/security/bulletin/ Samsung Android OS patch website: https://security.samsungmobile.com/securityUpdate.smsb

