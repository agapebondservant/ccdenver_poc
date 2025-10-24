# STIG Benchmark: SUSE Linux Enterprise Server 12 Security Technical Implementation Guide

---

**Version:** 3

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217101`

### Rule: The SUSE operating system must be a vendor-supported release.

**Rule ID:** `SV-217101r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A SUSE operating system release is considered "supported" if the vendor continues to provide security patches for the product. With an unsupported release, it will not be possible to resolve security issues discovered in the system software.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system is a vendor-supported release. Use the following command to verify the SUSE operating system is a vendor-supported release: # cat /etc/os-release NAME="SLES" VERSION="12" Current End of Life for SLES 12 General Support is 31 Oct 2024 and Long-term Support is until 31 Oct 2027. If the release is not supported by the vendor, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217102`

### Rule: Vendor-packaged SUSE operating system security patches and updates must be installed and up to date.

**Rule ID:** `SV-217102r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Timely patching is critical for maintaining the operational availability, confidentiality, and integrity of information technology (IT) systems. However, failure to keep SUSE operating system and application software patched is a common mistake made by IT professionals. New patches are released frequently, and it is often difficult for even experienced System Administrators (SAs) to keep abreast of all the new patches. When new weaknesses in a SUSE operating system exist, patches are usually made available by the vendor to resolve the problems. If the most recent security patches and updates are not installed, unauthorized users may take advantage of weaknesses in the unpatched software. The lack of prompt attention to patching could result in a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system security patches and updates are installed and up to date. Note: Updates are required to be applied with a frequency determined by the site or Program Management Office (PMO). Check for required SUSE operating system patches and updates with the following command: # sudo zypper patch-check 0 patches needed (0 security patches) If the patch repository data is corrupt check that the available package security updates have been installed on the system with the following command: # cut -d "|" -f 1-4 -s --output-delimiter " | " /var/log/zypp/history | grep -v " radd " 2016-12-14 11:59:36 | install | libapparmor1-32bit | 2.8.0-2.4.1 2016-12-14 11:59:36 | install | pam_apparmor | 2.8.0-2.4.1 2016-12-14 11:59:36 | install | pam_apparmor-32bit | 2.8.0-2.4.1 If the SUSE operating system has not been patched within the site or PMO frequency, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-217103`

### Rule: The SUSE operating system must display the Standard Mandatory DoD Notice and Consent Banner until users acknowledge the usage conditions and take explicit actions to log on for further access to the local graphical user interface.

**Rule ID:** `SV-217103r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the SUSE operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. The banner must be acknowledged by the user prior to allowing the user access to the SUSE operating system. This provides assurance that the user has seen the message and accepted the conditions for access. If the consent banner is not acknowledged by the user, DoD will not be in compliance with system use notifications required by law. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for the SUSE operating system: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000024-GPOS-00007</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system displays the Standard Mandatory DoD Notice and Consent Banner until users acknowledge the usage conditions and take explicit actions to log on via the local graphical user interface. Note: If a graphical user interface is not installed, this requirement is Not Applicable. Check the configuration by running the following command: # more /etc/gdm/Xsession The beginning of the file must contain the following text immediately after (#!/bin/sh): if ! zenity --text-info \ --title "Consent" \ --filename=/etc/gdm/banner \ --no-markup \ --checkbox="Accept." 10 10; then sleep 1; exit 1; fi If the beginning of the file does not contain the above text immediately after the line (#!/bin/sh), this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-217104`

### Rule: The SUSE operating system must display the Standard Mandatory DoD Notice and Consent Banner before granting access via local console.

**Rule ID:** `SV-217104r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the SUSE operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. The banner must be acknowledged by the user prior to allowing the user access to the SUSE operating system. This provides assurance that the user has seen the message and accepted the conditions for access. If the consent banner is not acknowledged by the user, DoD will not be in compliance with system use notifications required by law. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for SUSE operating system: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system displays the Standard Mandatory DoD Notice and Consent Banner before granting access to the system via local console. Check the "/etc/issue" file to verify that it contains the DoD required banner text: # more /etc/issue The output must display the following DoD-required banner text: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the output does not display the correct banner text, this is a finding.

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-217105`

### Rule: The SUSE operating system must display a banner before granting local or remote access to the system via a graphical user logon.

**Rule ID:** `SV-217105r958586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the SUSE operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. The banner must be acknowledged by the user prior to allowing the user access to the SUSE operating system. This provides assurance that the user has seen the message and accepted the conditions for access. If the consent banner is not acknowledged by the user, DoD will not be in compliance with system use notifications required by law. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for SUSE operating system: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system does not have a graphical user interface installed, this requirement is Not Applicable. Verify the SUSE operating system to display a banner before local or remote access to the system via a graphical user logon. Check that the SUSE operating system displays a banner at the logon screen by performing the following command: > grep banner-message-enable /etc/dconf/db/gdm.d/* banner-message-enable=true > cat /etc/dconf/profile/gdm user-db:user system-db:gdm file-db:/usr/share/gdm/greeter-dconf-defaults If "banner-message-enable" is set to "false" or is missing completely, this is a finding.

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-217106`

### Rule: The SUSE operating system must display the approved Standard Mandatory DoD Notice before granting local or remote access to the system via a graphical user logon.

**Rule ID:** `SV-217106r958586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the SUSE operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. The banner must be acknowledged by the user prior to allowing the user access to the SUSE operating system. This provides assurance that the user has seen the message and accepted the conditions for access. If the consent banner is not acknowledged by the user, DoD will not be in compliance with system use notifications required by law. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for SUSE operating system: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system displays the approved Standard Mandatory DoD Notice before granting local or remote access to the system via a graphical user logon. Note: If the system does not have a graphical user interface installed, this requirement is Not Applicable. Check that the SUSE operating system displays the exact approved Standard Mandatory DoD Notice and Consent Banner text by performing the following command: > grep banner-message-text /etc/dconf/db/gdm.d/* banner-message-text= "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only.\nBy using this IS (which includes any device attached to this IS), you consent to the following conditions:\n-The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations.\n-At any time, the USG may inspect and seize data stored on this IS.\n-Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose.\n-This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy.\n-Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Note: The "\n" characters are for formatting only. They will not be displayed on the graphical user interface. If the banner text does not exactly match the approved Standard Mandatory DoD Notice and Consent Banner, this is a finding.

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-217107`

### Rule: The SUSE operating system must be able to lock the graphical user interface (GUI).

**Rule ID:** `SV-217107r1015203_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Regardless of where the session lock is determined and implemented, once invoked, the session lock must remain in place until the user reauthenticates. No other activity aside from reauthentication must unlock the system. Satisfies: SRG-OS-000028-GPOS-00009, SRG-OS-000030-GPOS-00011</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system allows the user to lock the GUI. Note: If the system does not have a graphical user interface installed, this requirement is Not Applicable. This command must be run from an X11 session, otherwise the command will not work correctly. Run the following command: # gsettings get org.gnome.desktop.lockdown disable-lock-screen If the result is "true", this is a finding.

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-217108`

### Rule: The SUSE operating system must utilize vlock to allow for session locking.

**Rule ID:** `SV-217108r1015204_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Regardless of where the session lock is determined and implemented, once invoked, the session lock must remain in place until the user reauthenticates. No other activity aside from reauthentication must unlock the system. Satisfies: SRG-OS-000028-GPOS-00009, SRG-OS-000030-GPOS-00011, SRG-OS-000031-GPOS-00012</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that the SUSE operating system has the "vlock" package installed by running the following command: # zypper se -i --provides vlock If the command outputs "no matching items found", this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-217109`

### Rule: The SUSE operating system must initiate a session lock after a 15-minute period of inactivity for the graphical user interface.

**Rule ID:** `SV-217109r958402_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the users to manually lock their SUSE operating system session prior to vacating the vicinity, the SUSE operating system needs to be able to identify when a user's session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system initiates a session lock after a 15-minute period of inactivity via the graphical user interface by running the following command: Note: If the system does not have a graphical user interface installed, this requirement is Not Applicable. > sudo gsettings get org.gnome.desktop.session idle-delay uint32 900 If the command does not return a value less than or equal to "900", this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-217110`

### Rule: The SUSE operating system must initiate a session lock after a 10-minute period of inactivity.

**Rule ID:** `SV-217110r1015002_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the users to manually lock their SUSE operating system session prior to vacating the vicinity, the SUSE operating system needs to be able to identify when a user's session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system must initiate a session logout after a 10-minute period of inactivity for all connection types. Check the proper script exists to kill an idle session after a 10-minute period of inactivity with the following command: # cat /etc/profile.d/autologout.sh TMOUT=600 readonly TMOUT export TMOUT If the file "/etc/profile.d/autologout.sh" does not exist or the output from the function call is not the same, this is a finding.

## Group: SRG-OS-000031-GPOS-00012

**Group ID:** `V-217111`

### Rule: The SUSE operating system must conceal, via the session lock, information previously visible on the display with a publicly viewable image in the graphical user interface.

**Rule ID:** `SV-217111r958404_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. The SUSE operating system session lock event must include an obfuscation of the display screen to prevent other users from reading what was previously displayed. Publicly viewable images can include static or dynamic images, such as patterns used with screen savers, photographic images, solid colors, a clock, a battery life indicator, or a blank screen, with the additional caveat that none of the images conveys sensitive information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system conceals via the session lock information previously visible on the display with a publicly viewable image in the graphical user interface. Note: If the system does not have a graphical user interface installed, this requirement is Not Applicable. Check that the lock screen is set to a publicly viewable image by running the following command: # gsettings get org.gnome.desktop.screensaver picture-uri 'file:///usr/share/wallpapers/SLE-default-static.xml' If nothing is returned or "org.gnome.desktop.screensaver" is not set, this is a finding.

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-217112`

### Rule: The SUSE operating system must reauthenticate users when changing authenticators, roles, or escalating privileges.

**Rule ID:** `SV-217112r1050789_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When SUSE operating system provide the capability to change user authenticators, change security roles, or escalate a functional capability, it is critical the user reauthenticate. Satisfies: SRG-OS-000373-GPOS-00156, SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00158</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SUSE operating system requires reauthentication when changing authenticators, roles, or escalating privileges. Check that "/etc/sudoers" has no occurrences of "NOPASSWD" or "!authenticate" with the following command: > sudo egrep -i '(nopasswd|!authenticate)' /etc/sudoers If any uncommented lines containing "!authenticate", or "NOPASSWD" are returned and active accounts on the system have valid passwords, this is a finding.

## Group: SRG-OS-000027-GPOS-00008

**Group ID:** `V-217113`

### Rule: The SUSE operating system must limit the number of concurrent sessions to 10 for all accounts and/or account types.

**Rule ID:** `SV-217113r958398_rule`
**Severity:** low

**Description:**
<VulnDiscussion>SUSE operating system management includes the ability to control the number of users and user sessions that utilize a SUSE operating system. Limiting the number of allowed users and sessions per user is helpful in reducing the risks related to Denial-of-Service (DoS) attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based on mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system limits the number of concurrent sessions to 10 for all accounts and/or account types by running the following command: # grep "maxlogins" /etc/security/limits.conf /etc/security/limits.d/*.conf The result must contain the following line: * hard maxlogins 10 If the "maxlogins" item is missing, the line does not begin with a star symbol, or the value is not set to "10" or less, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-217114`

### Rule: The SUSE operating system must lock an account after three consecutive invalid access attempts.

**Rule ID:** `SV-217114r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed access attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. The pam_tally2.so module maintains a count of attempted accesses. This includes user name entry into a logon field as well as password entry. With counting access attempts, it is possible to lock an account without presenting a password into the password field. This should be taken into consideration as it poses as an avenue for denial of service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system locks a user account after three consecutive failed access attempts until the locked account is released by an administrator. Check that the system locks a user account after three consecutive failed login attempts using the following command: # grep pam_tally2.so /etc/pam.d/common-auth auth required pam_tally2.so onerr=fail deny=3 If no line is returned or the line is commented out, this is a finding. If the line is missing "onerr=fail", this is a finding. If the line has "deny" set to a value other than 1, 2, or 3, this is a finding. Check that the system resets the failed login attempts counter after a successful login using the following command: # grep pam_tally2.so /etc/pam.d/common-account account required pam_tally2.so If the account option is missing, or commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-217116`

### Rule: The SUSE operating system must enforce a delay of at least four (4) seconds between logon prompts following a failed logon attempt.

**Rule ID:** `SV-217116r991588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of logon attempts over a certain time interval reduces the chances that an unauthorized user may gain access to an account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system enforces a delay of at least four (4) seconds between logon prompts following a failed logon attempt. Check that the SUSE operating system enforces a delay of at least four (4) seconds between logon prompts following a failed logon attempt with the following command: # grep FAIL_DELAY /etc/login.defs FAIL_DELAY 4 If the value of "FAIL_DELAY" is not set to "4", "FAIL_DELAY" is commented out, or "FAIL_DELAY" is missing, then this is a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-217117`

### Rule: The SUSE operating system must enforce passwords that contain at least one upper-case character.

**Rule ID:** `SV-217117r1015206_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system enforces password complexity by requiring that at least one upper-case character. Check that the operating system enforces password complexity by requiring that at least one upper-case character be used by using the following command: # grep pam_cracklib.so /etc/pam.d/common-password password requisite pam_cracklib.so ucredit=-1 If the command does not return anything, the returned line is commented out, or has a second column value different from "requisite", or does not contain "ucredit=-1", this is a finding.

## Group: SRG-OS-000070-GPOS-00038

**Group ID:** `V-217118`

### Rule: The SUSE operating system must enforce passwords that contain at least one lower-case character.

**Rule ID:** `SV-217118r1015207_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system enforces password complexity by requiring that at least one lower-case character. Check that the operating system enforces password complexity by requiring that at least one lower-case character be used by using the following command: # grep pam_cracklib.so /etc/pam.d/common-password password requisite pam_cracklib.so lcredit=-1 If the command does not return anything, the returned line is commented out, or has a second column value different from "requisite", or does not contain "lcredit=-1", this is a finding.

## Group: SRG-OS-000071-GPOS-00039

**Group ID:** `V-217119`

### Rule: The SUSE operating system must enforce passwords that contain at least one numeric character.

**Rule ID:** `SV-217119r1015208_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system enforces password complexity by requiring that at least one numeric character. Check that the operating system enforces password complexity by requiring that at least one numeric character be used by using the following command: # grep pam_cracklib.so /etc/pam.d/common-password password requisite pam_cracklib.so dcredit=-1 If the command does not return anything, the returned line is commented out, or has a second column value different from "requisite", or does not contain "dcredit=-1", this is a finding.

## Group: SRG-OS-000266-GPOS-00101

**Group ID:** `V-217120`

### Rule: The SUSE operating system must enforce passwords that contain at least one special character.

**Rule ID:** `SV-217120r1015209_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps increase the time and resources required to compromise the password. Password complexity or strength is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor in determining how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Special characters are not alphanumeric. Examples include: ~ ! @ # $ % ^ *.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system enforces password complexity by requiring that at least one special character. Check that the operating system enforces password complexity by requiring that at least one special character be used by using the following command: # grep pam_cracklib.so /etc/pam.d/common-password password requisite pam_cracklib.so ocredit=-1 If the command does not return anything, the returned line is commented out, or has a second column value different from "requisite", or does not contain "ocredit=-1", this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-217121`

### Rule: The SUSE operating system must require the change of at least eight (8) of the total number of characters when passwords are changed.

**Rule ID:** `SV-217121r1015210_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the SUSE operating system allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system requires at least eight (8) characters be changed between the old and new passwords during a password change. Check that the operating system requires at least eight (8) characters be changed between the old and new passwords during a password change by running the following command: # grep pam_cracklib.so /etc/pam.d/common-password password requisite pam_cracklib.so difok=8 If the command does not return anything, the returned line is commented out, or has a second column value different from "requisite", or does not contain "difok", or the value is less than "8", this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-217122`

### Rule: The SUSE operating system must employ FIPS 140-2 approved cryptographic hashing algorithm for system authentication (login.defs).

**Rule ID:** `SV-217122r971535_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied on to provide confidentiality or integrity, and DoD data may be compromised. SUSE operating systems using encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules use authentication that meets DoD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general purpose computing system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system requires that the "ENCRYPT_METHOD" value in "/etc/login.defs" is set to "SHA512". Check the value of "ENCRYPT_METHOD" value in "/etc/login.defs" with the following command: > grep "^ENCRYPT_METHOD " /etc/login.defs ENCRYPT_METHOD SHA512 If "ENCRYPT_METHOD" is not set to "SHA512", if any values other that "SHA512" are configured, or if no output is produced, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-217123`

### Rule: The SUSE operating system must employ FIPS 140-2-approved cryptographic hashing algorithms for all stored passwords.

**Rule ID:** `SV-217123r1015211_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The system must use a strong hashing algorithm to store the password. The system must use a sufficient number of hashing rounds to ensure the required level of entropy. Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Satisfies: SRG-OS-000073-GPOS-00041, SRG-OS-000120-GPOS-00061</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system requires the shadow password suite configuration be set to encrypt interactive user passwords using a strong cryptographic hash. Check that the interactive user account passwords are using a strong password hash with the following command: > sudo cut -d: -f2 /etc/shadow $6$kcOnRq/5$NUEYPuyL.wghQwWssXRcLRFiiru7f5JPV6GaJhNC2aK5F3PZpE/BCCtwrxRc/AInKMNX3CdMw11m9STiql12f/ Password hashes "!" or "*" indicate inactive accounts not available for logon and are not evaluated. If any interactive user password hash does not begin with "$6", this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-217124`

### Rule: The SUSE operating system must configure the Linux Pluggable Authentication Modules (PAM) to only store encrypted representations of passwords.

**Rule ID:** `SV-217124r1015212_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Satisfies: SRG-OS-000120-GPOS-00061</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system configures the Linux PAM to only store encrypted representations of passwords. All account passwords must be hashed with SHA512 encryption strength. Check that PAM is configured to create SHA512 hashed passwords by running the following command: # grep pam_unix.so /etc/pam.d/common-password password required pam_unix.so sha512 If the command does not return anything or the returned line is commented out, has a second column value different from "required", or does not contain "sha512", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217125`

### Rule: The SUSE operating system must not be configured to allow blank or null passwords.

**Rule ID:** `SV-217125r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating is not configured to allow blank or null passwords. Check that blank or null passwords cannot be used by running the following command: # grep pam_unix.so /etc/pam.d/* | grep nullok If this produces any output, it may be possible to log on with accounts with empty passwords. If null passwords can be used, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-217126`

### Rule: The SUSE operating system must employ FIPS 140-3 approved cryptographic hashing algorithms for all stored passwords.

**Rule ID:** `SV-217126r1044807_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The system must use a strong hashing algorithm to store the password. The system must use a sufficient number of hashing rounds to ensure the required level of entropy. Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Satisfies: SRG-OS-000073-GPOS-00041, SRG-OS-000120-GPOS-00061</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system configures the shadow password suite configuration to encrypt passwords using a strong cryptographic hash. Check that a minimum number of hash rounds is configured by running the following command: egrep "^SHA_CRYPT_" /etc/login.defs If only one of "SHA_CRYPT_MIN_ROUNDS" or "SHA_CRYPT_MAX_ROUNDS" is set, and this value is below "100000", this is a finding. If both "SHA_CRYPT_MIN_ROUNDS" and "SHA_CRYPT_MAX_ROUNDS" are set, and the highest value for either is below "100000", this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-217127`

### Rule: The SUSE operating system must employ passwords with a minimum of 15 characters.

**Rule ID:** `SV-217127r1015214_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps determine strength and how long it takes to crack a password. Use of more characters in a password helps exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system enforces a minimum 15-character password length. Check that the operating system enforces a minimum 15-character password length with the following command: # grep pam_cracklib.so /etc/pam.d/common-password password requisite pam_cracklib.so minlen=15 If the command does not return anything, the returned line is commented out, or has a second column value different from "requisite", or does not contain "minlen" value, or the value is less than "15", this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-217128`

### Rule: The SUSE operating system must be configured to create or update passwords with a minimum lifetime of 24 hours (one day).

**Rule ID:** `SV-217128r1015215_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system to create or update passwords with minimum password age of one day or greater. Check that the SUSE operating system enforces 24 hours/one day as the minimum password age, run the following command: > grep '^PASS_MIN_DAYS' /etc/login.defs PASS_MIN_DAYS 1 If no output is produced, or if "PASS_MIN_DAYS" does not have a value of "1" or greater, this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-217129`

### Rule: The SUSE operating system must employ user passwords with a minimum lifetime of 24 hours (one day).

**Rule ID:** `SV-217129r1015216_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system enforces a minimum time period between password changes for each user account of one day or greater. Check the minimum time period between password changes for each user account with the following command: > sudo awk -F: '$4 < 1 {print $1 ":" $4}' /etc/shadow smithj:1 If any results are returned that are not associated with a system account, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-217130`

### Rule: The SUSE operating system must be configured to create or update passwords with a maximum lifetime of 60 days.

**Rule ID:** `SV-217130r1038967_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If the SUSE operating system does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the SUSE operating system passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SUSE operating system is configured to create or update passwords with a maximum password age of 60 days or less. Check that the SUSE operating system enforces 60 days or less as the maximum password age with the following command: > grep '^PASS_MAX_DAYS' /etc/login.defs The DoD requirement is "60" days or less (greater than zero, as zero days will lock the account immediately). If no output is produced, or if PASS_MAX_DAYS is not set to "60" days or less, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-217131`

### Rule: The SUSE operating system must employ user passwords with a maximum lifetime of 60 days.

**Rule ID:** `SV-217131r1038967_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If the SUSE operating system does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the SUSE operating system passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SUSE operating system enforces a maximum user password age of 60 days or less. Check that the SUSE operating system enforces 60 days or less as the maximum user password age with the following command: > sudo awk -F: '$5 > 60 || $5 == "" {print $1 ":" $5}' /etc/shadow If any results are returned that are not associated with a system account, this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-217134`

### Rule: The SUSE operating system must prevent the use of dictionary words for passwords.

**Rule ID:** `SV-217134r991587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the SUSE operating system allows the user to select passwords based on dictionary words, this increases the chances of password compromise by increasing the opportunity for successful guesses and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system prevents the use of dictionary words for passwords. Check that the SUSE operating system prevents the use of dictionary words for passwords with the following command: # grep pam_cracklib.so /etc/pam.d/common-password password requisite pam_cracklib.so retry=3 If the command does not return anything, or the returned line is commented out, this is a finding. If the value of "retry" is greater than 3, this is a finding.

## Group: SRG-OS-000123-GPOS-00064

**Group ID:** `V-217135`

### Rule: The SUSE operating system must never automatically remove or disable emergency administrator accounts.

**Rule ID:** `SV-217135r958508_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Emergency accounts are privileged accounts that are established in response to crisis situations where the need for rapid account activation is required. Therefore, emergency account activation may bypass normal account authorization processes. If these accounts are automatically disabled, system maintenance during emergencies may not be possible, thus adversely affecting system availability. Emergency accounts are different from infrequently used accounts (i.e., local logon accounts used by the organization's system administrators when network or normal logon/access is not available). Infrequently used accounts are not subject to automatic termination dates. Emergency accounts are accounts created in response to crisis situations, usually for use by maintenance personnel. The automatic expiration or disabling time period may be extended as needed until the crisis is resolved; however, it must not be extended indefinitely. A permanent account should be established for privileged users who need long-term maintenance accounts. To address access requirements the SUSE operating system can be integrated with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system is configured such that emergency administrator accounts are never automatically removed or disabled. Note: Root is typically the "account of last resort" on a system and is also used as the example emergency administrator account. If another account is being used as the emergency administrator account, the command should be used against that account. Check to see if the root account password or account expires with the following command: # sudo chage -l [Emergency_Administrator] Password expires:never If "Password expires" or "Account expires" is set to anything other than "never", this is a finding.

## Group: SRG-OS-000118-GPOS-00060

**Group ID:** `V-217136`

### Rule: The SUSE operating system must disable account identifiers (individuals, groups, roles, and devices) after 35 days of inactivity after password expiration.

**Rule ID:** `SV-217136r1015219_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. The SUSE operating system needs to track periods of inactivity and disable application identifiers after 35 days of inactivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system disables account identifiers after 35 days of inactivity since the password expiration Check the account inactivity value by performing the following command: # sudo grep -i inactive /etc/default/useradd INACTIVE=35 If "INACTIVE" is not set to a value greater than "0" and less than or equal to "35", this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-217138`

### Rule: The SUSE operating system must enforce a delay of at least four seconds between logon prompts following a failed logon attempt.

**Rule ID:** `SV-217138r991588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of logon attempts over a certain time interval reduces the chances that an unauthorized user may gain access to an account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system enforces a delay of at least four seconds between logon prompts following a failed logon attempt. # grep pam_faildelay /etc/pam.d/common-auth* auth required pam_faildelay.so delay=4000000 If the value of "delay" is not set to "4000000" or greater, "delay" is commented out, "delay" is missing, or the "pam_faildelay" line is missing completely, this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-217139`

### Rule: The SUSE operating system must not allow unattended or automatic logon via the graphical user interface.

**Rule ID:** `SV-217139r991591_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Failure to restrict system access to authenticated users negatively impacts SUSE operating system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If a graphical user interface is not installed, this requirement is Not Applicable. Verify the SUSE operating system does not allow unattended or automatic logon via a graphical user interface. Check that unattended or automatic login is disabled with the following commands: > grep -i ^DISPLAYMANAGER_AUTOLOGIN /etc/sysconfig/displaymanager DISPLAYMANAGER_AUTOLOGIN="" > grep -i ^DISPLAYMANAGER_PASSWORD_LESS_LOGIN /etc/sysconfig/displaymanager DISPLAYMANAGER_PASSWORD_LESS_LOGIN="no" If the "DISPLAYMANAGER_AUTOLOGIN" parameter includes a username or the "DISPLAYMANAGER_PASSWORD_LESS_LOGIN" parameter is not set to "no", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217140`

### Rule: The SUSE operating system must display the date and time of the last successful account logon upon logon.

**Rule ID:** `SV-217140r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Providing users with feedback on when account accesses last occurred facilitates user recognition and reporting of unauthorized account use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system users are provided with feedback on when account accesses last occurred. Check that "pam_lastlog" is used and not silent with the following command: > grep pam_lastlog /etc/pam.d/login session required pam_lastlog.so showfailed If "pam_lastlog" is missing from "/etc/pam.d/login" file, the "silent" option is present, or the returned line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217141`

### Rule: There must be no .shosts files on the SUSE operating system.

**Rule ID:** `SV-217141r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The .shosts files are used to configure host-based authentication for individual users or the system via SSH. Host-based authentication is not sufficient for preventing unauthorized access to the system, as it does not require interactive identification and authentication of a connection request, or for the use of two-factor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there are no ".shosts" files on the SUSE operating system. Check the system for the existence of these files with the following command: # find / -name '.shosts' If any ".shosts" files are found on the system, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217142`

### Rule: There must be no shosts.equiv files on the SUSE operating system.

**Rule ID:** `SV-217142r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The shosts.equiv files are used to configure host-based authentication for the system via SSH. Host-based authentication is not sufficient for preventing unauthorized access to the system, as it does not require interactive identification and authentication of a connection request, or for the use of two-factor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there are no "shosts.equiv" files on the SUSE operating system. Check the system for the existence of these files with the following command: # find /etc -name shosts.equiv If any "shosts.equiv" files are found on the system, this is a finding.

## Group: SRG-OS-000478-GPOS-00223

**Group ID:** `V-217143`

### Rule: FIPS 140-2 mode must be enabled on the SUSE operating system.

**Rule ID:** `SV-217143r959006_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. The SUSE operating system must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. Satisfies: SRG-OS-000396-GPOS-00176, SRG-OS-000478-GPOS-00223</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system is running in FIPS mode by running the following command. # cat /proc/sys/crypto/fips_enabled 1 If nothing is returned, the file does not exist, or the value returned is "0", this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-217144`

### Rule: SUSE operating systems with a basic input/output system (BIOS) must require authentication upon booting into single-user and maintenance modes.

**Rule ID:** `SV-217144r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SUSE operating system has set an encrypted root password. Note: If the system does not use a basic input/output system (BIOS) this requirement is Not Applicable. Check that the encrypted password is set for a boot user with the following command: # sudo cat /boot/grub2/grub.cfg | grep -i password password_pbkdf2 boot grub.pbkdf2.sha512.10000.VeryLongString If the boot user password entry does not begin with "password_pbkdf2", this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-217145`

### Rule: SUSE operating systems with Unified Extensible Firmware Interface (UEFI) implemented must require authentication upon booting into single-user mode and maintenance.

**Rule ID:** `SV-217145r958472_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system allows a user to boot into single-user or maintenance mode without authentication, any user that invokes single-user or maintenance mode is granted privileged access to all system information. If the system is running in EFI mode, SLES 12 by default will use GRUB 2 EFI as the boot loader.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SUSE operating system has set an encrypted boot password. Note: If the system does not use Unified Extensible Firmware Interface (UEFI) this requirement is Not Applicable. Check that the encrypted password is set for a boot user with the following command: # sudo cat /boot/efi/EFI/sles/grub.cfg | grep -i password password_pbkdf2 boot grub.pbkdf2.sha512.10000.VeryLongString If the boot user password entry does not begin with "password_pbkdf2", this is a finding.

## Group: SRG-OS-000185-GPOS-00079

**Group ID:** `V-217146`

### Rule: All SUSE operating system persistent disk partitions must implement cryptographic mechanisms to prevent unauthorized disclosure or modification of all information that requires at rest protection.

**Rule ID:** `SV-217146r1015305_rule`
**Severity:** high

**Description:**
<VulnDiscussion>SUSE operating systems handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). Satisfies: SRG-OS-000185-GPOS-00079, SRG-OS-000404-GPOS-00183, SRG-OS-000405-GPOS-00184</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system prevents unauthorized disclosure or modification of all information requiring at rest protection by using disk encryption. Determine the partition layout for the system with the following command: # sudo fdisk -l Device Boot Start End Sectors Size Id Type /dev/sda1 2048 4208639 4206592 2G 82 Linux swap / Solaris /dev/sda2 * 4208640 53479423 49270784 23.5G 83 Linux /dev/sda3 53479424 125829119 72349696 34.5G 83 Linux Verify the system partitions are all encrypted with the following command: # sudo more /etc/crypttab luks UUID=114167a-2a94-6cda-f1e7-15ad146c258b swap /dev/sda1 /dev/urandom swap truecrypt /dev/sda2 /etc/container_password tcrypt truecrypt /dev/sda3 /etc/container_password tcrypt Every persistent disk partition present on the system must have an entry in the file. If any partitions other than pseudo file systems (such as /proc or /sys) are not listed or "/etc/crypttab" does not exist, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-217147`

### Rule: The sticky bit must be set on all SUSE operating system world-writable directories.

**Rule ID:** `SV-217147r958524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, and hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DoD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system prevents unauthorized and unintended information transfer via the shared system resources. Note: The example below should be repeated for each locally defined partition. Check that world-writable directories have the sticky bit set with the following command: # sudo find / -xdev -perm -002 -type d -fstype xfs -exec ls -lLd {} \; 256 0 drwxrwxrwt 1 root root 4096 Jun 14 06:45 /tmp If any of the returned directories do not have the sticky bit set, or are not documented as having the write permission for the other class, this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-217148`

### Rule: Advanced Intrusion Detection Environment (AIDE) must verify the baseline SUSE operating system configuration at least weekly.

**Rule ID:** `SV-217148r958794_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to the SUSE operating system. Changes to SUSE operating system configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of the SUSE operating system. The SUSE operating system's Information System Security Manager (ISSM)/Information System Security Officer (ISSO) and System Administrator (SAs) must be notified via email and/or monitoring system trap when there is an unauthorized modification of a configuration item.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system checks the baseline configuration for unauthorized changes at least once weekly. Note: A file integrity tool other than Advanced Intrusion Detection Environment (AIDE) may be used, but the tool must be executed at least once per week. Check for a "crontab" that controls the execution of the file integrity application. For example, if AIDE is installed on the system, use the following command: # sudo crontab -l 0 0 * * 6 /usr/bin/aide --check | /bin/mail -s "$HOSTNAME - Daily AIDE integrity check run" root@example_server_name.mil If the file integrity application does not exist, or a "crontab" entry does not exist, check the cron directories for a script that runs the file integrity application: # ls -al /etc/cron.daily /etc/cron.weekly Inspect the file and ensure that the file integrity tool is being executed. If a file integrity tool is not configured in the crontab or in a script that runs at least weekly, this is a finding.

## Group: SRG-OS-000447-GPOS-00201

**Group ID:** `V-217149`

### Rule: The SUSE operating system must notify the System Administrator (SA) when AIDE discovers anomalies in the operation of any security functions.

**Rule ID:** `SV-217149r958948_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If anomalies are not acted on, security functions may fail to secure the system. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. Notifications provided by information systems include messages to local computer consoles and/or hardware indications, such as lights. This capability must take into account operational requirements for availability for selecting an appropriate response. The organization may choose to shut down or restart the information system upon security function anomaly detection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system notifies the SA when AIDE discovers anomalies in the operation of any security functions. Check to see if the aide cron job sends an email when executed with the following command: # sudo crontab -l 0 0 * * 6 /usr/sbin/aide --check | /bin/mail -s "$HOSTNAME - Daily AIDE integrity check run" root@example_server_name.mil If a "crontab" entry does not exist, check the cron directories for a script that runs the file integrity application and is configured to execute a binary to send an email: # ls -al /etc/cron.daily /etc/cron.weekly If a cron job is not configured to execute a binary to send an email (such as "/bin/mail"), this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217150`

### Rule: The SUSE operating system file integrity tool must be configured to verify Access Control Lists (ACLs).

**Rule ID:** `SV-217150r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>ACLs can provide permissions beyond those permitted through the file mode and must be verified by file integrity tools.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SUSE operating system file integrity tool is configured to verify ACLs. Check the "aide.conf" file to determine if the "acl" rule has been added to the rule list being applied to the files and directories selection lists. An example rule that includes the "acl" rule follows: All= p+i+n+u+g+s+m+S+sha512+acl+xattrs+selinux /bin All # apply the custom rule to the files in bin /sbin All # apply the same custom rule to the files in sbin If the "acl" rule is not being used on all selection lines in the "/etc/aide.conf" file, or ACLs are not being checked by another file integrity tool, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217151`

### Rule: The SUSE operating system file integrity tool must be configured to verify extended attributes.

**Rule ID:** `SV-217151r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Extended attributes in file systems are used to contain arbitrary data and file metadata with security implications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SUSE operating system file integrity tool is configured to verify extended attributes. Check the "aide.conf" file to determine if the "xattrs" rule has been added to the rule list being applied to the files and directories selection lists. An example rule that includes the "xattrs" rule follows: All= p+i+n+u+g+s+m+S+sha512+acl+xattrs+selinux /bin All # apply the custom rule to the files in bin /sbin All # apply the same custom rule to the files in sbin If the "xattrs" rule is not being used on all selection lines in the "/etc/aide.conf" file, or extended attributes are not being checked by another file integrity tool, this is a finding.

## Group: SRG-OS-000278-GPOS-00108

**Group ID:** `V-217152`

### Rule: The SUSE operating system file integrity tool must be configured to protect the integrity of the audit tools.

**Rule ID:** `SV-217152r991567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting the integrity of the tools used for auditing purposes is a critical step toward ensuring the integrity of audit information. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Audit tools include but are not limited to vendor-provided and open-source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. It is not uncommon for attackers to replace the audit tools or inject code into the existing tools to provide the capability to hide or erase system activity from the audit logs. To address this risk, audit tools must be cryptographically signed to provide the capability to identify when the audit tools have been modified, manipulated, or replaced. An example is a checksum hash of the file or files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SUSE operating system file integrity tool is configured to protect the integrity of the audit tools. Check that AIDE is properly configured to protect the integrity of the audit tools by running the following command: # sudo cat /etc/aide.conf | grep /usr/sbin/au /usr/sbin/auditctl p+i+n+u+g+s+b+acl+selinux+xattrs+sha512 /usr/sbin/auditd p+i+n+u+g+s+b+acl+selinux+xattrs+sha512 /usr/sbin/ausearch p+i+n+u+g+s+b+acl+selinux+xattrs+sha512 /usr/sbin/aureport p+i+n+u+g+s+b+acl+selinux+xattrs+sha512 /usr/sbin/autrace p+i+n+u+g+s+b+acl+selinux+xattrs+sha512 /usr/sbin/audispd p+i+n+u+g+s+b+acl+selinux+xattrs+sha512 /usr/sbin/augenrules p+i+n+u+g+s+b+acl+selinux+xattrs+sha512 If AIDE is configured properly to protect the integrity of the audit tools, all lines listed above will be returned from the command. If one or more lines are missing, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-217153`

### Rule: The SUSE operating system tool zypper must have gpgcheck enabled.

**Rule ID:** `SV-217153r1015220_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the SUSE operating system. This requirement ensures the software has not been tampered with and has been provided by a trusted vendor. Accordingly, patches, service packs, device drivers, or SUSE operating system components must be signed with a certificate recognized and approved by the organization. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. The SUSE operating system should not have to verify the software again. This requirement does not mandate DoD certificates for this purpose; however, the certificate used to verify the software must be from an approved Certification Authority (CA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SUSE operating system tool zypper has gpgcheck enabled. Check that zypper has gpgcheck enabled with the following command: > grep -i '^gpgcheck' /etc/zypp/zypp.conf gpgcheck = 1 If "gpgcheck" is set to "0", "off", "no", or "false", this is a finding.

## Group: SRG-OS-000437-GPOS-00194

**Group ID:** `V-217154`

### Rule: The SUSE operating system must remove all outdated software components after updated versions have been installed.

**Rule ID:** `SV-217154r958936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Previous versions of software components that are not removed from the information system after updates have been installed may be exploited by adversaries. Some information technology products may remove older versions of software automatically from the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system removes all outdated software components after updated version have been installed by running the following command: # grep -i upgraderemovedroppedpackages /etc/zypp/zypp.conf solver.upgradeRemoveDroppedPackages = true If "solver.upgradeRemoveDroppedPackages" is commented out, is set to "false", or is missing completely, this is a finding.

## Group: SRG-OS-000378-GPOS-00163

**Group ID:** `V-217155`

### Rule: The SUSE operating system must disable the USB mass storage kernel module.

**Rule ID:** `SV-217155r958820_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without identifying devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Peripherals include but are not limited to such devices as flash drives, external storage, and printers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system does not automount USB mass storage devices when connected to the host. Check that "usb-storage" is blacklisted in the "/etc/modprobe.d/50-blacklist.conf" file with the following command: # grep usb-storage /etc/modprobe.d/50-blacklist.conf blacklist usb-storage If nothing is output from the command, this is a finding.

## Group: SRG-OS-000114-GPOS-00059

**Group ID:** `V-217156`

### Rule: The SUSE operating system must disable the file system automounter unless required.

**Rule ID:** `SV-217156r958498_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatically mounting file systems permits easy introduction of unknown devices, thereby facilitating malicious activity. Satisfies: SRG-OS-000114-GPOS-00059, SRG-OS-000378-GPOS-00163, SRG-OS-000480-GPOS-00227</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system disables the ability to automount devices. Check to see if automounter service is active with the following command: # systemctl status autofs autofs.service - Automounts filesystems on demand Loaded: loaded (/usr/lib/systemd/system/autofs.service; disabled) Active: inactive (dead) If the "autofs" status is set to "active" and is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000312-GPOS-00122

**Group ID:** `V-217158`

### Rule: The SUSE operating system Apparmor tool must be configured to control whitelisted applications and user home directory access control.

**Rule ID:** `SV-217158r958702_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using a whitelist provides a configuration management method for allowing the execution of only authorized software. Using only authorized software decreases risk by limiting the number of potential vulnerabilities. The organization must identify authorized software programs and permit execution of authorized software by adding each authorized program to the "pam_apparmor" exception policy. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as whitelisting. Verification of whitelisted software occurs prior to execution or at system startup. Users' home directories/folders may contain information of a sensitive nature. Nonprivileged users should coordinate any sharing of information with a System Administrator (SA) through shared resources. Apparmor can confine users to their home directory, not allowing them to make any changes outside of their own home directories. Confining users to their home directory will minimize the risk of sharing information. Satisfies: SRG-OS-000312-GPOS-00122, SRG-OS-000312-GPOS-00123SRG-OS-000312-GPOS-00124, SRG-OS-000324-GPOS-00125, SRG-OS-000326-GPOS-00126, SRG-OS-000370-GPOS-00155, SRG-OS-000480-GPOS-00230</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SUSE operating system Apparmor tool is configured to control whitelisted applications and user home directory access control. Check that "pam_apparmor" is installed on the system with the following command: > zypper info pam_apparmor | grep "Installed" If the package "pam_apparmor" is not installed on the system, this is a finding. Check that the "apparmor" daemon is running with the following command: > systemctl status apparmor.service | grep -i active Active: active (exited) since Fri 2017-01-13 01:01:01 GMT; 1day 1h ago If something other than "Active: active" is returned, this is a finding. Note: "pam_apparmor" must have properly configured profiles. All configurations will be based on the actual system setup and organization. See the "pam_apparmor" documentation for more information on configuring profiles.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217159`

### Rule: The SUSE operating system must disable the x86 Ctrl-Alt-Delete key sequence.

**Rule ID:** `SV-217159r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A locally logged-on user who presses Ctrl-Alt-Delete, when at the console, can reboot the system. If accidentally pressed, as could happen in the case of a mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system is not configured to reboot the system when Ctrl-Alt-Delete is pressed. Check that the ctrl-alt-del.target is masked with the following command: > systemctl status ctrl-alt-del.target Loaded: masked (/dev/null; masked) Active: inactive (dead) If the ctrl-alt-del.target is not masked, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217160`

### Rule: The SUSE operating system must disable the x86 Ctrl-Alt-Delete key sequence for Graphical User Interfaces.

**Rule ID:** `SV-217160r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A locally logged-on user who presses Ctrl-Alt-Delete, when at the console, can reboot the system. If accidentally pressed, as could happen in the case of a mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot. In the GNOME graphical environment, risk of unintentional reboot from the Ctrl-Alt-Delete sequence is reduced because the user will be prompted before any action is taken.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If a graphical user interface is not installed, this requirement is Not Applicable. Verify the SUSE operating system is not configured to reboot the system when Ctrl-Alt-Delete is pressed in the graphical user interface. Check that the dconf setting was disabled to allow the Ctrl-Alt-Delete sequence in the graphical user interface with the following command: Check the default logout key sequence: > sudo gsettings get org.gnome.settings-daemon.plugins.media-keys logout '' Check that the value is not writable and cannot be changed by the user: > sudo gsettings writable org.gnome.settings-daemon.plugins.media-keys logout false If the logout value is not [''] and the writable status is not false, this is a finding.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-217161`

### Rule: The SUSE operating system default permissions must be defined in such a way that all authenticated users can only read and modify their own files.

**Rule ID:** `SV-217161r991590_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the most restrictive default permissions ensures that when new accounts are created, they do not have unnecessary access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system defines default permissions for all authenticated users in such a way that the users can only read and modify their own files. Check the system default permissions with the following command: # grep -i "umask" /etc/login.defs UMASK 077 If the "UMASK" variable is set to "000", the severity is raised to a CAT I, and this is a finding. If the value of "UMASK" is not set to "077", "UMASK" is commented out, or "UMASK" is missing completely, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217162`

### Rule: The SUSE operating system must not have unnecessary accounts.

**Rule ID:** `SV-217162r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accounts providing no operational purpose provide additional opportunities for system compromise. Unnecessary accounts include user accounts for individuals not requiring access to the system and application accounts for applications not installed on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all SUSE operating system accounts are assigned to an active system, application, or user account. Obtain the list of authorized system accounts from the Information System Security Officer (ISSO). Check the system accounts on the system with the following command: # more /etc/passwd root:x:0:0:root:/root:/bin/bash ... games:x:12:100:Games account:/var/games:/bin/bash Accounts such as "games" and "gopher" are not authorized accounts as they do not support authorized system functions. If the accounts on the system do not match the provided documentation, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-217163`

### Rule: The SUSE operating system must not have duplicate User IDs (UIDs) for interactive users.

**Rule ID:** `SV-217163r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, interactive users must be identified and authenticated to prevent potential misuse and compromise of the system. Interactive users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Interactive users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. Satisfies: SRG-OS-000104-GPOS-00051, SRG-OS-000121-GPOS-00062</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system contains no duplicate UIDs for interactive users. Check that the SUSE operating system contains no duplicate UIDs for interactive users by running the following command: # awk -F ":" 'list[$3]++{print $1, $3}' /etc/passwd If output is produced, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217164`

### Rule: The SUSE operating system root account must be the only account having unrestricted access to the system.

**Rule ID:** `SV-217164r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account other than root also has a User Identifier (UID) of "0", it has root authority, giving that account unrestricted access to the entire SUSE operating system. Multiple accounts with a UID of "0" afford an opportunity for potential intruders to guess a password for a privileged account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SUSE operating system root account is the only account with unrestricted access to the system. Check the system for duplicate UID "0" assignments with the following command: # awk -F: '$3 == 0 {print $1}' /etc/passwd root If any accounts other than root have a UID of "0", this is a finding.

## Group: SRG-OS-000383-GPOS-00166

**Group ID:** `V-217166`

### Rule: If Network Security Services (NSS) is being used by the SUSE operating system it must prohibit the use of cached authentications after one day.

**Rule ID:** `SV-217166r958828_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cached authentication information is out of date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If NSS is not used on the operating system, this is Not Applicable. If NSS is used by the SUSE operating system, verify it prohibits the use of cached authentications after one day. Check that cached authentications cannot be used after one day with the following command: # sudo grep -i "memcache_timeout" /etc/sssd/sssd.conf memcache_timeout = 86400 If "memcache_timeout" has a value greater than "86400", or is missing, this is a finding.

## Group: SRG-OS-000383-GPOS-00166

**Group ID:** `V-217167`

### Rule: The SUSE operating system must configure the Linux Pluggable Authentication Modules (PAM) to prohibit the use of cached offline authentications after one day.

**Rule ID:** `SV-217167r958828_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cached authentication information is out of date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If SSSD is not being used on the operating system, this is Not Applicable. Verify that the SUSE operating system Pluggable Authentication Modules (PAM) prohibits the use of cached off line authentications after one day. Check that cached off line authentications cannot be used after one day with the following command: # sudo grep "offline_credentials_expiration" /etc/sssd/sssd.conf offline_credentials_expiration = 1 If "offline_credentials_expiration" is not set to a value of "1", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217168`

### Rule: All SUSE operating system files and directories must have a valid owner.

**Rule ID:** `SV-217168r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unowned files and directories may be unintentionally inherited if a user is assigned the same User Identifier (UID) as the UID of the unowned files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all SUSE operating system files and directories on the system have a valid owner. Check the owner of all files and directories with the following command: Note: The value after -fstype must be replaced with the filesystem type. XFS is used as an example. # find / -fstype xfs -nouser If any files on the system do not have an assigned owner, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217169`

### Rule: All SUSE operating system files and directories must have a valid group owner.

**Rule ID:** `SV-217169r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Files without a valid group owner may be unintentionally inherited if a group is assigned the same Group Identifier (GID) as the GID of the files without a valid group owner.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all SUSE operating system files and directories on the system have a valid group. Check the owner of all files and directories with the following command: Note: The value after -fstype must be replaced with the filesystem type. XFS is used as an example. # find / -fstype xfs -nogroup If any files on the system do not have an assigned group, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217170`

### Rule: All SUSE operating system local interactive users must have a home directory assigned in the /etc/passwd file.

**Rule ID:** `SV-217170r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If local interactive users are not assigned a valid home directory, there is no place for the storage and control of files they should own.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SUSE operating system local interactive users on the system have a home directory assigned. Check for missing local interactive user home directories with the following command: > sudo pwck -r user 'smithj': directory '/home/smithj' does not exist Ask the System Administrator (SA) if any users found without home directories are local interactive users. If the SA is unable to provide a response, check for users with a User Identifier (UID) of 1000 or greater with the following command: > sudo awk -F: '($3>=1000)&&($7 !~ /nologin/){print $1, $3, $6}' /etc/passwd If any interactive users do not have a home directory assigned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217171`

### Rule: All SUSE operating system local interactive user accounts, upon creation, must be assigned a home directory.

**Rule ID:** `SV-217171r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If local interactive users are not assigned a valid home directory, there is no place for the storage and control of files they should own.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all SUSE operating system local interactive users on the system are assigned a home directory upon creation. Check to see if the system is configured to create home directories for local interactive users with the following command: # grep -i create_home /etc/login.defs CREATE_HOME yes If the value for "CREATE_HOME" parameter is not set to "yes", the line is missing, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217172`

### Rule: All SUSE operating system local interactive user home directories defined in the /etc/passwd file must exist.

**Rule ID:** `SV-217172r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a local interactive user has a home directory defined that does not exist, the user may be given access to the / directory as the current working directory upon logon. This could create a Denial of Service because the user would not be able to access their logon configuration files, and it may give them visibility to system files they normally would not be able to access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the assigned home directory of all SUSE operating system local interactive users on the system exists. Check the home directory assignment for all local interactive non-privileged users on the system with the following command: # awk -F: '($3>=1000)&&($7 !~ /nologin/){print $1, $6}' /etc/passwd smithj /home/smithj Note: This may miss interactive users that have been assigned a privileged UID. Evidence of interactive use may be obtained from a number of log files containing system logon information. Check that all referenced home directories exist with the following command: # pwck -r user 'smithj': directory '/home/smithj' does not exist If any home directories referenced in "/etc/passwd" are returned as not defined, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217173`

### Rule: All SUSE operating system local interactive user home directories must have mode 0750 or less permissive.

**Rule ID:** `SV-217173r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on local interactive user home directories may allow unauthorized access to user files by other users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the assigned home directory of all SUSE operating system local interactive users has a mode of "0750" or less permissive. Check the home directory assignment for all non-privileged users on the system with the following command: Note: This may miss interactive users that have been assigned a privileged User Identifier (UID). Evidence of interactive use may be obtained from a number of log files containing system logon information. # ls -ld $(awk -F: '($3>=1000)&&($7 !~ /nologin/){print $6}' /etc/passwd) -rwxr-x--- 1 smithj users 18 Mar 5 17:06 /home/smithj If home directories referenced in "/etc/passwd" do not have a mode of "0750" or less permissive, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217174`

### Rule: All SUSE operating system local interactive user home directories must be group-owned by the home directory owners primary group.

**Rule ID:** `SV-217174r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Group Identifier (GID) of a local interactive user’s home directory is not the same as the primary GID of the user, this would allow unauthorized access to the user’s files, and users that share the same group may not be able to access files that they legitimately should.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the assigned home directory of all SUSE operating system local interactive users is group-owned by that user's primary GID. Check the home directory assignment for all non-privileged users on the system with the following command: Note: This may miss local interactive users that have been assigned a privileged UID. Evidence of interactive use may be obtained from a number of log files containing system logon information. The returned directory "/home/smithj" is used as an example. # awk -F: '($3>=1000)&&($7 !~ /nologin/){print $4, $6}' /etc/passwd 250 /home/smithj Check the user's primary group with the following command: # grep users /etc/group users:x:250:smithj,jonesj,jacksons If the user home directory referenced in "/etc/passwd" is not group-owned by that user's primary GID, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217175`

### Rule: All SUSE operating system local initialization files must have mode 0740 or less permissive.

**Rule ID:** `SV-217175r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Local initialization files are used to configure the user's shell environment upon logon. Malicious modification of these files could compromise accounts upon logon.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all SUSE operating system local initialization files have a mode of "0740" or less permissive. Check the mode on all SUSE operating system local initialization files with the following command: Note: The example will be for the user "smithj", who has a home directory of "/home/smithj". # ls -al /home/smithj/.* | more -rwxr-xr-x 1 smithj users 896 Mar 10 2011 .profile -rwxr-xr-x 1 smithj users 497 Jan 6 2007 .login -rwxr-xr-x 1 smithj users 886 Jan 6 2007 .something If any local initialization files have a mode more permissive than "0740", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217176`

### Rule: All SUSE operating system local interactive user initialization files executable search paths must contain only paths that resolve to the users home directory.

**Rule ID:** `SV-217176r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The executable search path (typically the PATH environment variable) contains a list of directories for the shell to search to find executables. If this path includes the current working directory (other than the user's home directory), executables in these directories may be executed instead of system commands. This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon or two consecutive colons, this is interpreted as the current working directory. If deviations from the default system search path for the local interactive user are required, they must be documented with the Information System Security Officer (ISSO).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all SUSE operating system local interactive user initialization files executable search path statements do not contain statements that will reference a working directory other than the user's home directory. Check the executable search path statement for all operating system local interactive user initialization files in the user's home directory with the following commands: Note: The example will be for the user "smithj", who has a home directory of "/home/smithj". # sudo grep -i path= /home/smithj/.* /home/smithj/.bash_profile:PATH=$PATH:$HOME/.local/bin:$HOME/bin If any local interactive user initialization files have executable search path statements that include directories outside of their home directory, and the additional path statements are not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217177`

### Rule: All SUSE operating system local initialization files must not execute world-writable programs.

**Rule ID:** `SV-217177r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If user start-up files execute world-writable programs, especially in unprotected directories, they could be maliciously modified to destroy user files or otherwise compromise the system at the user level. If the system is compromised at the user level, it is easier to elevate privileges to eventually compromise the system at the root and network level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SUSE operating system local initialization files do not execute world-writable programs. Check the system for world-writable files with the following command: > sudo find / -xdev -perm -002 -type f -exec ls -ld {} \; For all files listed, check for their presence in the local initialization files with the following command: Note: The example will be for a system that is configured to create users' home directories in the "/home" directory. > sudo find /home/* -maxdepth 1 -type f -name \.\* -exec grep -H <file> {} \; If any local initialization files are found to reference world-writable files, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217178`

### Rule: SUSE operating system file systems that contain user home directories must be mounted to prevent files with the setuid and setgid bit set from being executed.

**Rule ID:** `SV-217178r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute setuid and setgid files with owner privileges. This option must be used for mounting any file system not containing approved setuid and setguid files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SUSE operating system file systems that contain user home directories are mounted with the "nosuid" option. Print the currently active file system mount options of the file system(s) that contain the user home directories with the following command: # for X in `awk -F: '($3>=1000)&&($7 !~ /nologin/){print $6}' /etc/passwd`; do findmnt -nkT $X; done | sort -r /home /dev/mapper/system-home ext4 rw,nosuid,relatime,data=ordered If a file system containing user home directories is not mounted with the FSTYPE OPTION nosuid, this is a finding. Note: If a separate file system has not been created for the user home directories (user home directories are mounted under "/"), this is not a finding as the "nosuid" option cannot be used on the "/" system.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217179`

### Rule: SUSE operating system file systems that are used with removable media must be mounted to prevent files with the setuid and setgid bit set from being executed.

**Rule ID:** `SV-217179r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SUSE operating system file systems used for removable media are mounted with the "nosuid" option. Check the file systems that are mounted at boot time with the following command: # more /etc/fstab UUID=2bc871e4-e2a3-4f29-9ece-3be60c835222 /mnt/usbflash vfat noauto,owner,ro,nosuid 0 0 If a file system found in "/etc/fstab" refers to removable media and it does not have the "nosuid" option set, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217180`

### Rule: SUSE operating system file systems that are being imported via Network File System (NFS) must be mounted to prevent files with the setuid and setgid bit set from being executed.

**Rule ID:** `SV-217180r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SUSE operating system file systems that are being NFS exported are mounted with the "nosuid" option. Find the file system(s) that contain the directories being exported with the following command: # more /etc/fstab | grep nfs UUID=e06097bb-cfcd-437b-9e4d-a691f5662a7d /store nfs rw,nosuid 0 0 If a file system found in "/etc/fstab" refers to NFS and it does not have the "nosuid" option set, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217181`

### Rule: SUSE operating system file systems that are being imported via Network File System (NFS) must be mounted to prevent binary files from being executed.

**Rule ID:** `SV-217181r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files as they may be incompatible. Executing files from untrusted file systems increases the opportunity for unprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system file systems that are being NFS exported are mounted with the "noexec" option. Find the file system(s) that contain the directories being exported with the following command: # more /etc/fstab | grep nfs UUID=e06097bb-cfcd-437b-9e4d-a691f5662a7d /store nfs rw,noexec 0 0 If a file system found in "/etc/fstab" refers to NFS and it does not have the "noexec" option set, and use of NFS exported binaries is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217182`

### Rule: All SUSE operating system world-writable directories must be group-owned by root, sys, bin, or an application group.

**Rule ID:** `SV-217182r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a world-writable directory has the sticky bit set and is not group-owned by a privileged Group Identifier (GID), unauthorized users may be able to modify files created by others. The only authorized public directories are those temporary directories supplied with the system or those designed to be temporary file repositories. The setting is normally reserved for directories used by the system and by users for temporary file storage, (e.g., /tmp), and for directories requiring global read/write access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all SUSE operating system world-writable directories are group-owned by root, sys, bin, or an application group. Check the system for world-writable directories with the following command: Note: The example below should be repeated for each locally defined partition. The value after -fstype must be replaced with the filesystem type. XFS is used as an example. # find / -xdev -perm -002 -type d -fstype xfs -exec ls -lLd {} \; drwxrwxrwt. 2 root root 40 Aug 26 13:07 /dev/mqueue drwxrwxrwt. 2 root root 220 Aug 26 13:23 /dev/shm drwxrwxrwt. 14 root root 4096 Aug 26 13:29 /tmp If any world-writable directories are not owned by root, sys, bin, or an application group associated with the directory, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217183`

### Rule: SUSE operating system kernel core dumps must be disabled unless needed.

**Rule ID:** `SV-217183r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kernel core dumps may contain the full contents of system memory at the time of the crash. Kernel core dumps may consume a considerable amount of disk space and may result in denial of service by exhausting the available space on the target file system partition.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SUSE operating system kernel core dumps are disabled unless needed. Check the status of the "kdump" service with the following command: # systemctl status kdump.service Loaded: not-found (Reason: No such file or directory) Active: inactive (dead) If the "kdump" service is active, ask the System Administrator if the use of the service is required and documented with the Information System Security Officer (ISSO). If the service is active and is not documented, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217184`

### Rule: A separate file system must be used for SUSE operating system user home directories (such as /home or an equivalent).

**Rule ID:** `SV-217184r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The use of separate file systems for different paths can protect the system from failures resulting from a file system becoming full or failing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a separate file system/partition has been created for SUSE operating system non-privileged local interactive user home directories. Check the home directory assignment for all non-privileged users (those with a UID greater than 1000) on the system with the following command: # awk -F: '($3>=1000)&&($7 !~ /nologin/){print $1, $3, $6, $7}' /etc/passwd adamsj 1002 /home/adamsj /bin/bash jacksonm 1003 /home/jacksonm /bin/bash smithj 1001 /home/smithj /bin/bash The output of the command will give the directory/partition that contains the home directories for the non-privileged users on the system (in this example, /home) and user's shell. All accounts with a valid shell (such as /bin/bash) are considered interactive users. Check that a file system/partition has been created for the non-privileged interactive users with the following command: Note: The partition of /home is used in the example. # grep /home /etc/fstab UUID=333ada18 /home ext4 noatime,nobarrier,nodev 1 2 If a separate entry for the file system/partition that contains the non-privileged interactive users' home directories does not exist, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217185`

### Rule: The SUSE operating system must use a separate file system for /var.

**Rule ID:** `SV-217185r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The use of separate file systems for different paths can protect the system from failures resulting from a file system becoming full or failing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SUSE operating system has a separate file system/partition for "/var". Check that a file system/partition has been created for "/var" with the following command: # grep /var /etc/fstab UUID=c274f65f /var ext4 noatime,nobarrier 1 2 If a separate entry for "/var" is not in use, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217186`

### Rule: The SUSE operating system must use a separate file system for the system audit data path.

**Rule ID:** `SV-217186r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The use of separate file systems for different paths can protect the system from failures resulting from a file system becoming full or failing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SUSE operating system has a separate file system/partition for the system audit data path. Check that a file system/partition has been created for the system audit data path with the following command: Note: "/var/log/audit" is used as the example as it is a common location. #grep /var/log/audit /etc/fstab UUID=3645951a /var/log/audit ext4 defaults 1 2 If a separate entry for the system audit data path (in this example the "/var/log/audit" path) does not exist, ask the System Administrator if the system audit logs are being written to a different file system/partition on the system and then grep for that file system/partition. If a separate file system/partition does not exist for the system audit data path, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-217188`

### Rule: The SUSE operating system must prevent unauthorized users from accessing system error messages.

**Rule ID:** `SV-217188r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the SUSE operating system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SUSE operating system prevents unauthorized users from accessing system error messages. Check the "/var/log/messages" file permissions with the following comand: > sudo stat -c "%n %U:%G %a" /var/log/messages /var/log/messages root:root 640 Check that "permissions.local" file contains the correct permissions rules with the following command: > grep -i messages /etc/permissions.local /var/log/messages root:root 640 If the effective permissions do not match the "permissions.local" file, the command does not return any output, or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217189`

### Rule: The SUSE operating system must be configured to not overwrite Pluggable Authentication Modules (PAM) configuration on package changes.

**Rule ID:** `SV-217189r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>"pam-config" is a command line utility that automatically generates a system PAM configuration as packages are installed, updated or removed from the system. "pam-config" removes configurations for PAM modules and parameters that it does not know about. It may render ineffective PAM configuration by the system administrator and thus impact system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system is configured to not overwrite Pluggable Authentication Modules (PAM) configuration on package changes. Check that soft links between PAM configuration files are removed with the following command: > find /etc/pam.d/ -type l -iname "common-*" If any results are returned, this is a finding.

## Group: SRG-OS-000337-GPOS-00129

**Group ID:** `V-217190`

### Rule: The SUSE operating system must have the auditing package installed.

**Rule ID:** `SV-217190r1015221_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, the source of events, where events occurred, and the outcome of events, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in the SUSE operating system audit logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured SUSE operating system. Satisfies: SRG-OS-000337-GPOS-00129, SRG-OS-000348-GPOS-00136, SRG-OS-000349-GPOS-00137, SRG-OS-000350-GPOS-00138, SRG-OS-000351-GPOS-00139, SRG-OS-000352-GPOS-00140, SRG-OS-000353-GPOS-00141, SRG-OS-000354-GPOS-00142, SRG-OS-000358-GPOS-00145, SRG-OS-000359-GPOS-00146, SRG-OS-000365-GPOS-00152, SRG-OS-000474-GPOS-00219, SRG-OS-000475-GPOS-00220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system auditing package is installed. Check that the "audit" package is installed by performing the following command: # zypper se audit i | audit | User Space Tools for 2.6 Kernel Auditing If the package "audit" is not installed on the system, then this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217191`

### Rule: SUSE operating system audit records must contain information to establish what type of events occurred, the source of events, where events occurred, and the outcome of events.

**Rule ID:** `SV-217191r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, the source of events, where events occurred, and the outcome of events, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in the SUSE operating system audit logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured SUSE operating system. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00021, SRG-OS-000051-GPOS-00024, SRG-OS-000054-GPOS-00025, SRG-OS-000122-GPOS-00063, SRG-OS-000254-GPOS-00095, SRG-OS-000255-GPOS-00096, SRG-OS-000392-GPOS-00172, SRG-OS-000480-GPOS-00227</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system produces audit records. Check that the SUSE operating system produces audit records by running the following command to determine the current status of the auditd service: # systemctl status auditd.service If the service is enabled, the returned message must contain the following text: Active: active (running) If the service is not running, this is a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-217192`

### Rule: The SUSE operating system must allocate audit record storage capacity to store at least one weeks worth of audit records when audit records are not immediately sent to a central audit record storage facility.

**Rule ID:** `SV-217192r958752_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure SUSE operating systems have a sufficient storage capacity in which to write the audit logs, SUSE operating systems need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial installation of the SUSE operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system allocates audit record storage capacity to store at least one week's worth of audit records when audit records are not immediately sent to a central audit record storage facility. Determine which partition the audit records are being written to with the following command: # sudo grep log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Check the size of the partition that audit records are written to (with the example being /var/log/audit/) with the following command: # df -h /var/log/audit/ /dev/sda2 24G 10.4G 13.6G 43% /var/log/audit If the audit records are not written to a partition made specifically for audit records (/var/log/audit is a separate partition), determine the amount of space being used by other files in the partition with the following command: #du -sh [audit_partition] 1.8G /var/log/audit The partition size needed to capture a week's worth of audit records is based on the activity level of the system and the total storage capacity available. In normal circumstances, 10.0 GB of storage space for audit records will be sufficient. If the audit record partition is not allocated sufficient storage capacity, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-217193`

### Rule: The SUSE operating system auditd service must notify the System Administrator (SA) and Information System Security Officer (ISSO) immediately when audit storage capacity is 75 percent full.

**Rule ID:** `SV-217193r971542_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches 75 percent utilization, they are unable to plan for audit record storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the SUSE operating system auditd is configured to notify the System Administrator (SA) and Information System Security Officer (ISSO) when the audit record storage volume reaches 75 percent of the storage capacity. Check the system configuration to determine the partition to which audit records are written using the following command: # grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Check the size of the partition to which audit records are written (e.g., "/var/log/audit/"): # df -h /var/log/audit/ 0.9G /var/log/audit If the audit records are not being written to a partition specifically created for audit records (in this example "/var/log/audit" is a separate partition), use the following command to determine the amount of space other files in the partition currently occupy: # du -sh <partition> 1.8G /var Determine the threshold for the system to take action when 75 percent of the repository maximum audit record storage capacity is reached: # grep -iw space_left /etc/audit/auditd.conf space_left = 225 If the value of the "space_left" keyword is not set to 25 percent of the total partition size, this is a finding.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-217194`

### Rule: The Information System Security Officer (ISSO) and System Administrator (SA), at a minimum, must be alerted of a SUSE operating system audit processing failure event.

**Rule ID:** `SV-217194r958424_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the administrators are notified in the event of a SUSE operating system audit processing failure by inspecting "/etc/audit/auditd.conf". Check if the system is configured to send email to an account when it needs to notify an administrator with the following command: sudo grep action_mail /etc/audit/auditd.conf action_mail_acct = root If the value of the "action_mail_acct" keyword is not set to "root" and/or other accounts for security personnel, the "action_mail_acct" keyword is missing, or the returned line is commented out, this is a finding.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-217195`

### Rule: The Information System Security Officer (ISSO) and System Administrator (SA), at a minimum, must have mail aliases to be notified of a SUSE operating system audit processing failure.

**Rule ID:** `SV-217195r958424_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the administrators are notified in the event of a SUSE operating system audit processing failure by checking that "/etc/aliases" has a defined value for root. > grep -i "^postmaster:" /etc/aliases postmaster: root If the above command does not return a value of "root", this is a finding Verify the alias for root forwards to a monitored e-mail account: > grep -i "^root:" /etc/aliases root: person@server.mil If the alias for root does not forward to a monitored e-mail account, this is a finding.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-217196`

### Rule: The SUSE operating system audit system must take appropriate action when the audit storage volume is full.

**Rule ID:** `SV-217196r1038966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the SUSE operating system is at risk of failing to process audit logs as required, it takes action to mitigate the failure. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. Responses to audit failure depend on the nature of the failure mode. When availability is an overriding concern, other approved actions in response to an audit failure are as follows: 1) If the failure was caused by the lack of audit record storage capacity, the SUSE operating system must continue generating audit records if possible (automatically restarting the audit service if necessary), overwriting the oldest audit records in a first-in-first-out manner. 2) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, the SUSE operating system must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system takes the appropriate action when the audit storage volume is full. Check that the SUSE operating system takes the appropriate action when the audit storage volume is full with the following command: # sudo grep disk_full_action /etc/audit/auditd.conf disk_full_action = SYSLOG If the value of the "disk_full_action" option is not "SYSLOG", "SINGLE", or "HALT", or the line is commented out, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-217197`

### Rule: The audit-audispd-plugins must be installed on the SUSE operating system.

**Rule ID:** `SV-217197r958754_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "audit-audispd-plugins" package is installed on the SUSE operating system. Check that the "audit-audispd-plugins" package is installed on the SUSE operating system with the following command: # zypper se audit-audispd-plugins If the "audit-audispd-plugins" package is not installed, this is a finding. Verify the "au-remote" plugin is enabled with the following command: # grep -i active /etc/audisp/plugins.d/au-remote.conf active = yes If "active" is missing, commented out, or is not set to "yes", this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-217198`

### Rule: The SUSE operating system audit event multiplexor must be configured to use Kerberos.

**Rule ID:** `SV-217198r958754_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Allowing devices and users to connect to or from the system without first authenticating them allows untrusted access and can lead to a compromise or attack. Audit events may include sensitive data must be encrypted prior to transmission. Kerberos provides a mechanism to provide both authentication and encryption for audit event records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the SUSE operating system audit event multiplexor is configured to use Kerberos by running the following command: # sudo cat /etc/audisp/audisp-remote.conf | grep enable_krb5 enable_krb5 = yes If "enable-krb5" is not set to "yes", this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-217199`

### Rule: Audispd must off-load audit records onto a different system or media from the SUSE operating system being audited.

**Rule ID:** `SV-217199r958754_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "audispd" off-loads audit records onto a different system or media from the SUSE operating system being audited. Check if "audispd" is configured to off-load audit records onto a different system or media from the SUSE operating system by running the following command: # sudo cat /etc/audisp/audisp-remote.conf | grep remote_server remote_server = 192.168.1.101 If "remote_server" is not set to an external server or media, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-217200`

### Rule: The audit system must take appropriate action when the network cannot be used to off-load audit records.

**Rule ID:** `SV-217200r959008_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify what action the audit system takes if it cannot off-load audit records to a different system or storage media from the SUSE operating system being audited. Check the action that the audit system takes in the event of a network failure with the following command: # sudo grep -i "network_failure_action" /etc/audisp/audisp-remote.conf network_failure_action = syslog If the "network_failure_action" option is not set to "syslog", "single", or "halt" or the line is commented out, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-217201`

### Rule: Audispd must take appropriate action when the SUSE operating system audit storage is full.

**Rule ID:** `SV-217201r959008_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit system off-loads audit records if the SUSE operating system storage volume becomes full. Check that the records are properly off-loaded to a remote server with the following command: # sudo grep -i "disk_full_action" /etc/audisp/audisp-remote.conf disk_full_action = syslog If "disk_full_action" is not set to "syslog", "single", or "halt" or the line is commented out, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-217202`

### Rule: The SUSE operating system must protect audit rules from unauthorized modification.

**Rule ID:** `SV-217202r958434_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SUSE operating system protects audit rules from unauthorized modification. Check that "permissions.local" file contains the correct permissions rules with the following command: # grep -i audit /etc/permissions.local /var/log/audit root:root 600 /var/log/audit/audit.log root:root 600 /etc/audit/audit.rules root:root 640 /etc/audit/rules.d/audit.rules root:root 640 If the command does not return any output, this is a finding. Check that all of the audit information files and folders have the correct permissions with the following command: # sudo chkstat /etc/permissions.local If the command returns any output, this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-217203`

### Rule: The SUSE operating system audit tools must have the proper permissions configured to protect against unauthorized access.

**Rule ID:** `SV-217203r991557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. SUSE operating systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys to make access decisions regarding the access to audit tools. Audit tools include but are not limited to vendor-provided and open-source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000257-GPOS-00098, SRG-OS-000258-GPOS-00099</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SUSE operating system audit tools have the proper permissions configured in the permissions profile to protect from unauthorized access. Check that "permissions.local" file contains the correct permissions rules with the following command: > grep "^/usr/sbin/au" /etc/permissions.local /usr/sbin/audispd root:root 0750 /usr/sbin/auditctl root:root 0750 /usr/sbin/auditd root:root 0750 /usr/sbin/ausearch root:root 0755 /usr/sbin/aureport root:root 0755 /usr/sbin/autrace root:root 0750 /usr/sbin/augenrules root:root 0750 If the command does not return any output, this is a finding. Check that all of the audit information files and folders have the correct permissions with the following command: > sudo chkstat /etc/permissions.local If the command returns any output, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217204`

### Rule: The SUSE operating system must not disable syscall auditing.

**Rule ID:** `SV-217204r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, the SUSE operating system includes the "-a task,never" audit rule as a default. This rule suppresses syscall auditing for all tasks started with this rule in effect. Because the audit daemon processes the "audit.rules" file from the top down, this rule supersedes all other defined syscall rules; therefore no syscall auditing can take place on the operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify syscall auditing has not been disabled: > sudo auditctl -l | grep -i "a task,never" If any results are returned, this is a finding. Verify the default rule "-a task,never" is not statically defined : > sudo grep -rv "^#" /etc/audit/rules.d/ | grep -i "a task,never" If any results are returned, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-217205`

### Rule: The SUSE operating system must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/passwd.

**Rule ID:** `SV-217205r1015222_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply create a new account. Auditing of account creation mitigates this risk. To address access requirements, many SUSE operating systems may be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000304-GPOS-00121, SRG-OS-000470-GPOS-00214, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record when all modifications occur to the "/etc/passwd" file. Check that the following file is being watched by performing the following command on the system rules in "/etc/audit/audit.rules": # sudo grep /etc/passwd /etc/audit/audit.rules -w /etc/passwd -p wa -k account_mod If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-217206`

### Rule: The SUSE operating system must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/group.

**Rule ID:** `SV-217206r1015223_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply create a new account. Auditing of account creation mitigates this risk. To address access requirements, many SUSE operating systems may be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record when modifications occur to the "/etc/group" file. Check that the following file is being watched by performing the following command on the system rules in "/etc/audit/audit.rules": # sudo grep /etc/group /etc/audit/audit.rules -w /etc/group -p wa -k account_mod If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-217207`

### Rule: The SUSE operating system must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/shadow.

**Rule ID:** `SV-217207r1015224_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply create a new account. Auditing of account creation mitigates this risk. To address access requirements, many SUSE operating systems may be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record when modifications occur to the "/etc/shadow" file. Check that the following file is being watched by performing the following command on the system rules in "/etc/audit/audit.rules": # sudo grep /etc/shadow /etc/audit/audit.rules -w /etc/shadow -p wa -k account_mod If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-217208`

### Rule: The SUSE operating system must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/opasswd.

**Rule ID:** `SV-217208r1015225_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply create a new account. Auditing of account creation mitigates this risk. To address access requirements, many SUSE operating systems may be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record when modifications occur to the "/etc/security/opasswd" file. Check that the following file is being watched by performing the following command on the system rules in "/etc/audit/audit.rules": # grep /etc/security/opasswd /etc/audit/audit.rules -w /etc/security/opasswd -p wa -k account_mod If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-217209`

### Rule: The SUSE operating system must generate audit records for all uses of the privileged functions.

**Rule ID:** `SV-217209r1015226_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000337-GPOS-00129, SRG-OS-000348-GPOS-00136, SRG-OS-000349-GPOS-00137, SRG-OS-000350-GPOS-00138, SRG-OS-000351-GPOS-00139, SRG-OS-000352-GPOS-00140, SRG-OS-000353-GPOS-00141, SRG-OS-000354-GPOS-00142, SRG-OS-000358-GPOS-00145, SRG-OS-000359-GPOS-00146, SRG-OS-000365-GPOS-00152</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system audits the execution of privileged functions using the following command: # grep -iw execve /etc/audit/audit.rules -a always,exit -F arch=b32 -S execve -C uid!=euid -F euid=0 -k setuid -a always,exit -F arch=b64 -S execve -C uid!=euid -F euid=0 -k setuid -a always,exit -F arch=b32 -S execve -C gid!=egid -F egid=0 -k setgid -a always,exit -F arch=b64 -S execve -C gid!=egid -F egid=0 -k setgid If both the "b32" and "b64" audit rules for "SUID" files are not defined, this is a finding. If both the "b32" and "b64" audit rules for "SGID" files are not defined, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217210`

### Rule: The SUSE operating system must generate audit records for all uses of the su command.

**Rule ID:** `SV-217210r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for any use of the "su" command. Check that the following command call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": # sudo egrep "\/usr\/bin\/su\s" /etc/audit/audit.rules -a always,exit -F path=/usr/bin/su -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-priv_change If the command does not return any output or the returned line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217211`

### Rule: The SUSE operating system must generate audit records for all uses of the sudo command.

**Rule ID:** `SV-217211r958412_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for any use of the "sudo" command. Check that the following command call is being audited by performing the following command on the system rules in "/etc/audit/audit.rules": # sudo grep -iw sudo /etc/audit/audit.rules -a always,exit -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-sudo If the command does not return any output or the returned line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217212`

### Rule: The SUSE operating system must generate audit records for all uses of the chfn command.

**Rule ID:** `SV-217212r958412_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "chfn" command. Check that the following command call is being audited by performing the following command on the system rules in "/etc/audit/audit.rules": # sudo grep -i chfn /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chfn -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-chfn If the command does not return any output or the returned line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217213`

### Rule: The SUSE operating system must generate audit records for all uses of the mount command.

**Rule ID:** `SV-217213r958412_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "mount" command. Check that the following command call is being audited by performing the following command on the system rules in "/etc/audit/audit.rules": # sudo grep -iw mount /etc/audit/audit.rules -a always,exit -F arch=b32 -S mount -F auid>=1000 -F auid!=4294967295 -k privileged-mount -a always,exit -F arch=b64 -S mount -F auid>=1000 -F auid!=4294967295 -k privileged-mount -a always,exit -F path=/usr/bin/mount -F auid>=1000 -F auid!=4294967295 -k privileged-mount If both the "b32" and "b64" audit rules are not defined for the "mount" syscall, this is a finding. If all uses of the "mount" command are not being audited, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217214`

### Rule: The SUSE operating system must generate audit records for all uses of the umount command.

**Rule ID:** `SV-217214r958412_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "umount" command. Check that the following command call is being audited by performing the following command on the system rules in "/etc/audit/audit.rules": # sudo grep -iw umount /etc/audit/audit.rules -a always,exit -F arch=b32 -S umount -F auid>=1000 -F auid!=4294967295 -k privileged-umount -a always,exit -F arch=b32 -S umount2 -F auid>=1000 -F auid!=4294967295 -k privileged-umount -a always,exit -F arch=b64 -S umount2 -F auid>=1000 -F auid!=4294967295 -k privileged-umount If both the "b32" and "b64" audit rules are not defined for the "umount" syscall, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217215`

### Rule: The SUSE operating system must generate audit records for all uses of the ssh-agent command.

**Rule ID:** `SV-217215r958412_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "ssh-agent" command. Check that the following command call is being audited by performing the following command on the system rules in "/etc/audit/audit.rules": # sudo grep -i ssh-agent /etc/audit/audit.rules -a always,exit -F path=/usr/bin/ssh-agent -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-ssh-agent If the command does not return any output or the returned line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217216`

### Rule: The SUSE operating system must generate audit records for all uses of the ssh-keysign command.

**Rule ID:** `SV-217216r958412_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "ssh-keysign" command. Check that the following command call is being audited by performing the following command on the system rules in "/etc/audit/audit.rules": # sudo grep -i ssh-keysign /etc/audit/audit.rules -a always,exit -F path=/usr/lib/ssh/ssh-keysign -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-ssh-keysign If the command does not return any output or the returned line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217217`

### Rule: The SUSE operating system must generate audit records for all uses of the kmod command.

**Rule ID:** `SV-217217r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the following list of events for which the SUSE operating system will provide an audit record generation capability: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "kmod" command. Check that the following command call is being audited by performing the following command on the system rules in "/etc/audit/audit.rules": # sudo grep kmod /etc/audit/audit.rules -w /usr/bin/kmod -p x -k modules If the system is configured to audit the execution of the module management program "kmod", the command will return a line. If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217218`

### Rule: The SUSE operating system must generate audit records for all uses of the setxattr, fsetxattr, lsetxattr, removexattr, fremovexattr, and lremovexattr syscalls.

**Rule ID:** `SV-217218r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, however, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr" syscalls. Verify that the following command call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": > sudo grep xattr /etc/audit/audit.rules -a always,exit -F arch=b32 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=4294967295 -k perm_mod -a always,exit -F arch=b64 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=4294967295 -k perm_mod If both the "b32" and "b64" audit rules are not defined for the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr" syscalls, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217223`

### Rule: The SUSE operating system must generate audit records for all uses of the chown, fchown, fchownat, and lchown syscalls.

**Rule ID:** `SV-217223r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, however, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "chown", "fchown", "fchownat", and "lchown" syscalls. Verify that the following command call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": > sudo grep chown /etc/audit/audit.rules -a always,exit -F arch=b32 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=4294967295 -k perm_mod -a always,exit -F arch=b64 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=4294967295 -k perm_mod If both the "b32" and "b64" audit rules are not defined for the "chown", "fchown", "fchownat", "lchown" syscalls, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217227`

### Rule: The SUSE operating system must generate audit records for all uses of the chmod, fchmod, and fchmodat system calls.

**Rule ID:** `SV-217227r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, however, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "chmod", "fchmod" and "fchmodat" system calls. Verify that the following command call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": > sudo grep chmod /etc/audit/audit.rules -a always,exit -F arch=b32 -S chmod,fchmod,fchmodat -F auid>=1000 -F auid!=4294967295 -k perm_mod -a always,exit -F arch=b64 -S chmod,fchmod,fchmodat -F auid>=1000 -F auid!=4294967295 -k perm_mod If both the "b32" and "b64" audit rules are not defined for the "chmod", "fchmod", and "fchmodat" syscalls, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217230`

### Rule: The SUSE operating system must generate audit records for all uses of the creat, open, openat, open_by_handle_at, truncate, and ftruncate syscalls.

**Rule ID:** `SV-217230r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, however, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "creat", "open", "openat", "open_by_handle_at", "truncate", and "ftruncate" syscalls. Verify that the following command call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": > sudo grep 'open\|truncate\|creat' /etc/audit/audit.rules -a always,exit -F arch=b32 -S creat,open,openat,open_by_handle_at,truncate,ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k perm_access -a always,exit -F arch=b64 -S creat,open,openat,open_by_handle_at,truncate,ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=4294967295 -k perm_access -a always,exit -F arch=b32 -S creat,open,openat,open_by_handle_at,truncate,ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k perm_access -a always,exit -F arch=b64 -S creat,open,openat,open_by_handle_at,truncate,ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=4294967295 -k perm_access If both the "b32" and "b64" audit rules are not defined for the "creat", "open", "openat", "open_by_handle_at", "truncate", and "ftruncate" syscalls, this is a finding. If the output does not produce rules containing "-F exit=-EPERM", this is a finding. If the output does not produce rules containing "-F exit=-EACCES", this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217236`

### Rule: The SUSE operating system must generate audit records for all uses of the passwd command.

**Rule ID:** `SV-217236r958412_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "passwd" command. Check that the following command call is being audited by performing the following command on the system rules in "/etc/audit/audit.rules": # sudo grep -i /usr/bin/passwd /etc/audit/audit.rules -a always,exit -F path=/usr/bin/passwd -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-passwd If the command does not return any output or the returned line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217237`

### Rule: The SUSE operating system must generate audit records for all uses of the gpasswd command.

**Rule ID:** `SV-217237r958412_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "gpasswd" command. Check that the following command call is being audited by performing the following command on the system rules in "/etc/audit/audit.rules": # sudo grep -i gpasswd /etc/audit/audit.rules -a always,exit -F path=/usr/bin/gpasswd -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-gpasswd If the command does not return any output or the returned line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217238`

### Rule: The SUSE operating system must generate audit records for all uses of the newgrp command.

**Rule ID:** `SV-217238r958412_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "newgrp" command. Check that the following command call is being audited by performing the following command on the system rules in "/etc/audit/audit.rules": # sudo grep -i newgrp /etc/audit/audit.rules -a always,exit -F path=/usr/bin/newgrp -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-newgrp If the command does not return any output or the returned line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217239`

### Rule: The SUSE operating system must generate audit records for a uses of the chsh command.

**Rule ID:** `SV-217239r958412_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "chsh" command. Check that the following command call is being audited by performing the following command on the system rules in "/etc/audit/audit.rules": # sudo grep -i chsh /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chsh -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-chsh If the command does not return any output or the returned line is commented out, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-217240`

### Rule: The SUSE operating system must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/gshadow.

**Rule ID:** `SV-217240r958368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply create a new account. Auditing of account creation mitigates this risk. To address access requirements, many SUSE operating systems may be integrated with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record when all modifications occur to the "/etc/gshadow" file. Check that the following file is being watched by performing the following command on the system rules in "/etc/audit/audit.rules": # sudo grep /etc/gshadow /etc/audit/audit.rules -w /etc/gshadow -p wa -k account_mod If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217241`

### Rule: The SUSE operating system must generate audit records for all uses of the chmod command.

**Rule ID:** `SV-217241r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "chmod" command. Check that the following command call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": # sudo grep -i chmod /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chmod -F perm=x -F auid>=1000 -F auid!=4294967295 -k prim_mod If the command does not return any output or the returned line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217242`

### Rule: The SUSE operating system must generate audit records for all uses of the setfacl command.

**Rule ID:** `SV-217242r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "setfacl" command. Check that the following command call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": # sudo grep -i setfacl /etc/audit/audit.rules -a always,exit -F path=/usr/bin/setfacl -F perm=x -F auid>=1000 -F auid!=4294967295 -k prim_mod If the command does not return any output or the returned line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217243`

### Rule: The SUSE operating system must generate audit records for all uses of the chacl command.

**Rule ID:** `SV-217243r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "chacl" command. Check that the following command call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": # sudo grep -i chacl /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chacl -F perm=x -F auid>=1000 -F auid!=4294967295 -k prim_mod If the command does not return any output or the returned line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217244`

### Rule: Successful/unsuccessful attempts to modify categories of information (e.g., classification levels) must generate audit records.

**Rule ID:** `SV-217244r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify audit records are generated when successful/unsuccessful attempts to modify categories of information (e.g., classification levels) occur. Check that the following command call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": # sudo grep -i 'chcon' /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chcon -F perm=x -F auid>=1000 -F auid!=4294967295 -k prim_mod If the command does not return any output or the returned line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217245`

### Rule: The SUSE operating system must generate audit records for all uses of the rm command.

**Rule ID:** `SV-217245r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "rm" command. Check that the following command call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": # sudo grep -i rm /etc/audit/audit.rules -a always,exit -F path=/usr/bin/rm -F perm=x -F auid>=1000 -F auid!=4294967295 -k prim_mod If the command does not return any output or the returned line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217246`

### Rule: The SUSE operating system must generate audit records for all modifications to the tallylog file must generate an audit record.

**Rule ID:** `SV-217246r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000473-GPOS-00218</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record when all modifications to the "tallylog" file occur. Check that the following command call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": # sudo grep -i tallylog /etc/audit/audit.rules -w /var/log/tallylog -p wa -k logins If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217247`

### Rule: The SUSE operating system must generate audit records for all modifications to the lastlog file.

**Rule ID:** `SV-217247r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record when all modifications to the "lastlog" file occur. Check that the following is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": # sudo grep -i lastlog /etc/audit/audit.rules -w /var/log/lastlog -p wa -k logins If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217248`

### Rule: The SUSE operating system must generate audit records for all uses of the passmass command.

**Rule ID:** `SV-217248r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "passmass" command. Check that the following command call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": # sudo grep -i passmass /etc/audit/audit.rules -a always,exit -F path=/usr/bin/passmass -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-passmass If the command does not return any output or the returned line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217249`

### Rule: The SUSE operating system must generate audit records for all uses of the unix_chkpwd command.

**Rule ID:** `SV-217249r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an audit record is generated for all uses of the "unix_chkpwd" command. Check that the following command call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": # sudo egrep -i '(unix_chkpwd|unix2_chkpwd)' /etc/audit/audit.rules -a always,exit -F path=/sbin/unix_chkpwd -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-unix-chkpwd -a always,exit -F path=/sbin/unix2_chkpwd -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-unix2-chkpwd If the command does not return any output or the returned line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217250`

### Rule: The SUSE operating system must generate audit records for all uses of the chage command.

**Rule ID:** `SV-217250r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an audit record is generated for all uses of the "chage" command. Perform the verification by running the following command: Check that the following command call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": # sudo grep -i 'chage' /etc/audit/audit.rules -a always,exit -F path=/usr/bin/chage -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-chage If the command does not return any output or the returned line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217251`

### Rule: The SUSE operating system must generate audit records for all uses of the usermod command.

**Rule ID:** `SV-217251r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an audit record is generated for all uses of the "usermod" command. Check that the following command call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": # sudo grep -i 'usermod' /etc/audit/audit.rules -a always,exit -F path=/usr/sbin/usermod -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-usermod If the command does not return any output or the returned line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217252`

### Rule: The SUSE operating system must generate audit records for all uses of the crontab command.

**Rule ID:** `SV-217252r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an audit record is generated for all uses of the "crontab" command. Check for the following command call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": # sudo grep -i 'crontab' /etc/audit/audit.rules -a always,exit -F path=/usr/bin/crontab -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-crontab If the command does not return any output or the returned line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217253`

### Rule: The SUSE operating system must generate audit records for all uses of the pam_timestamp_check command.

**Rule ID:** `SV-217253r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an audit record is generated for all uses of the "pam_timestamp_check" command. Check for the following command call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": # sudo grep -i 'pam_timestamp_check' /etc/audit/audit.rules -a always,exit -F path=/sbin/pam_timestamp_check -F perm=x -F auid>=1000 -F auid!=4294967295 -k privileged-pam_timestamp_check If the command does not return any output or the returned line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217254`

### Rule: The SUSE operating system must generate audit records for all uses of the delete_module command.

**Rule ID:** `SV-217254r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "delete_module" command. Check that the following command call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": # sudo grep -i delete_module /etc/audit/audit.rules -a always,exit -F arch=b32 -S delete_module -F auid>=1000 -F auid!=4294967295 -k unload_module -a always,exit -F arch=b64 -S delete_module -F auid>=1000 -F auid!=4294967295 -k unload_module If both the "b32" and "b64" audit rules are not defined for the "unload_module" syscall, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217255`

### Rule: The SUSE operating system must generate audit records for all uses of the init_module and finit_module syscalls.

**Rule ID:** `SV-217255r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, however, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "init_module" and "finit_module" syscalls. Verify that the following command call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": > sudo grep init_module /etc/audit/audit.rules -a always,exit -F arch=b32 -S init_module,finit_module -F auid>=1000 -F auid!=4294967295 -k moduleload -a always,exit -F arch=b64 -S init_module,finit_module -F auid>=1000 -F auid!=4294967295 -k moduleload If both the "b32" and "b64" audit rules are not defined for the "init_module" and "finit_module" syscalls, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-217257`

### Rule: The SUSE operating system must generate audit records for all modifications to the faillog file.

**Rule ID:** `SV-217257r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record when all modifications to the "faillog" file occur. Check that the following is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": # sudo grep -i faillog /etc/audit/audit.rules -w /var/log/faillog -p wa -k logins If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-217258`

### Rule: The SUSE operating system must not have the telnet-server package installed.

**Rule ID:** `SV-217258r987796_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for SUSE operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. SUSE operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions and functions). Examples of nonessential capabilities include but are not limited to games, software packages, tools, and demonstration software not related to requirements or providing a wide array of functionality not required for every mission but which cannot be disabled. Satisfies: SRG-OS-000074-GPOS-00042, SRG-OS-000095-GPOS-00049</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the telnet-server package is not installed on the SUSE operating system. Check that the telnet-server package is not installed on the SUSE operating system by running the following command: # zypper se telnet-server If the telnet-server package is installed, this is a finding.

## Group: SRG-OS-000024-GPOS-00007

**Group ID:** `V-217260`

### Rule: The SUSE operating system file /etc/gdm/banner must contain the Standard Mandatory DoD Notice and Consent banner text.

**Rule ID:** `SV-217260r958392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The banner must be acknowledged by the user prior to allowing the user access to the SUSE operating system. This provides assurance that the user has seen the message and accepted the conditions for access. If the consent banner is not acknowledged by the user, DoD will not be in compliance with system use notifications required by law. To establish acceptance of the application usage policy, a click-through banner at system logon is required. The system must prevent further activity until the user executes a positive action to manifest agreement by clicking on a box indicating "OK".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system file "/etc/gdm/banner" contains the Standard Mandatory DoD Notice and Consent Banner text by running the following command: # more /etc/gdm/banner If the file does not contain the following text, this is a finding. "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details."

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-217261`

### Rule: The SUSE operating system must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services as defined in the Ports, Protocols, and Services Management (PPSM) Category Assignments List (CAL) and vulnerability assessments.

**Rule ID:** `SV-217261r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. SUSE operating systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the SUSE operating system must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or address authorized quality-of-life issues. Satisfies: SRG-OS-000096-GPOS-00050, SRG-OS-000297-GPOS-00115, SRG-OS-000480-GPOS-00231, SRG-OS-000480-GPOS-00232</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system is configured to prohibit or restrict the use of functions, ports, protocols, and/or services as defined in the Ports, Protocols, and Services Management (PPSM) Category Assignments List (CAL) and vulnerability assessments. Check that the "SuSEfirewall2.service" is enabled and running by running the following command: # systemctl status SuSEfirewall2.service * SuSEfirewall2.service - SuSEfirewall2 phase 2 Loaded: loaded (/usr/lib/systemd/system/SuSEfirewall2.service; enabled; vendor preset: disabled) Active: active (exited) since Thu 2017-03-09 17:33:29 UTC; 6 days ago Main PID: 2533 (code=exited, status=0/SUCCESS) Tasks: 0 (limit: 512) Memory: 0B CPU: 0 CGroup: /system.slice/SuSEfirewall2.service If the service is not enabled, this is a finding. If the service is not active, this is a finding. Check the firewall configuration for any unnecessary or prohibited functions, ports, protocols, and/or services by running the following command: # grep ^FW_ /etc/sysconfig/SuSEfirewall2 Ask the System Administrator for the site or program PPSM Component Local Services Assessment (Component Local Services Assessment (CLSA). Verify the services allowed by the firewall match the PPSM CLSA. If there are any additional ports, protocols, or services that are not included in the PPSM CLSA, this is a finding. If there are any ports, protocols, or services that are prohibited by the PPSM CAL, this is a finding.

## Group: SRG-OS-000420-GPOS-00186

**Group ID:** `V-217262`

### Rule: SuSEfirewall2 must protect against or limit the effects of Denial-of-Service (DoS) attacks on the SUSE operating system by implementing rate-limiting measures on impacted network interfaces.

**Rule ID:** `SV-217262r958902_rule`
**Severity:** high

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of the SUSE operating system to mitigate the impact on system availability of DoS attacks that have occurred or are ongoing. For each system, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or establishing memory partitions). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "SuSEfirewall2" is configured to protect the SUSE operating system against or limit the effects of DoS attacks. Run the following command: # grep -i fw_services_accept_ext /etc/sysconfig/SuSEfirewall2 FW_SERVICES_ACCEPT_EXT="0/0,tcp,22,,hitcount=3,blockseconds=60,recentname=ssh" If the "FW_SERVICES_ACCEPT_EXT" rule does not contain both the "hitcount" and "blockseconds" parameters, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-217263`

### Rule: The SUSE operating system must display the Standard Mandatory DoD Notice and Consent Banner before granting access via SSH.

**Rule ID:** `SV-217263r958390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the SUSE operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for SUSE operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Satisfies: SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system displays the Standard Mandatory DoD Notice and Consent Banner before granting access to the system via SSH. Check the issue file to verify that it contains one of the DoD required banners. If it does not, this is a finding. # more /etc/issue The output must display the following DoD-required banner text. "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the output does not display the banner text, this is a finding. Check the banner setting for sshd_config: # sudo grep "Banner" /etc/ssh/sshd_config The output must show the value of "Banner" set to "/etc/issue". An example is shown below: # sudo grep "Banner" /etc/ssh/sshd_config Banner /etc/issue If it does not, this is a finding.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-217264`

### Rule: All networked SUSE operating systems must have and implement SSH to protect the confidentiality and integrity of transmitted and received information, as well as information during preparation for transmission.

**Rule ID:** `SV-217264r958908_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, logical means (cryptography) do not have to be employed, and vice versa. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system is not networked this requirement is Not Applicable. Verify that the SUSE operating system implements SSH to protect the confidentiality and integrity of transmitted and received information, as well as information during preparation for transmission. Check that the OpenSSH package is installed on the SUSE operating system with the following command: # zypper se openssh S | Name | Summary | Type --+---------------- --+------------------------------------------------------+-------- i | openssh | Secure Shell Client and Server (Remote L-> | package If the OpenSSH package is not installed, this is a finding. Check that the OpenSSH service active on the SUSE operating system with the following command: # systemctl status sshd.service | grep -i "active:" Active: active (running) since Thu 2017-01-12 15:03:38 UTC; 1 months 4 days ago If OpenSSH service is not active, this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-217265`

### Rule: The SUSE operating system must log SSH connection attempts and failures to the server.

**Rule ID:** `SV-217265r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyber attacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SSH is configured to verbosely log connection attempts and failed logon attempts to the SUSE operating system. Check that the SSH daemon configuration verbosely logs connection attempts and failed logon attempts to the server with the following command: # sudo grep -i loglevel /etc/ssh/sshd_config The output message must contain the following text: LogLevel VERBOSE If "LogLevel" is not set to "VERBOSE" or "INFO", the LogLevel keyword is missing, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217266`

### Rule: The SUSE operating system must display the date and time of the last successful account logon upon an SSH logon.

**Rule ID:** `SV-217266r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Providing users with feedback on when account accesses via SSH last occurred facilitates user recognition and reporting of unauthorized account use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all remote connections via SSH to the SUSE operating system display feedback on when account accesses last occurred. Check that "PrintLastLog" keyword in the sshd daemon configuration file is used and set to "yes" with the following command: # sudo grep -i printlastlog /etc/ssh/sshd_config PrintLastLog yes If the "PrintLastLog" keyword is set to "no", is missing, or is commented out, this is a finding.

## Group: SRG-OS-000109-GPOS-00056

**Group ID:** `V-217267`

### Rule: The SUSE operating system must deny direct logons to the root account using remote access via SSH.

**Rule ID:** `SV-217267r1015227_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure individual accountability and prevent unauthorized access, organizational users must be individually identified and authenticated. A group authenticator is a generic account used by multiple individuals. Use of a group authenticator alone does not uniquely identify individual users. Examples of the group authenticator is the UNIX OS "root" user account, the Windows "Administrator" account, the "sa" account, or a "helpdesk" account. For example, the UNIX and Windows SUSE operating systems offer a "switch user" capability, allowing users to authenticate with their individual credentials and, when needed, "switch" to the administrator role. This method provides for unique individual authentication prior to using a group authenticator. Users (and any processes acting on behalf of users) need to be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization, which outlines specific user actions that can be performed on the SUSE operating system without identification or authentication. Requiring individuals to be authenticated with an individual authenticator prior to using a group authenticator allows for traceability of actions, as well as adding an additional level of protection of the actions that can be taken with group account knowledge.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system denies direct logons to the root account using remote access via SSH. Check that SSH denies any user trying to log on directly as root with the following command: # sudo grep -i permitrootlogin /etc/ssh/sshd_config PermitRootLogin no If the "PermitRootLogin" keyword is set to "yes", is missing, or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-217268`

### Rule: The SUSE operating system must not allow automatic logon via SSH.

**Rule ID:** `SV-217268r991591_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Failure to restrict system access via SSH to authenticated users negatively impacts SUSE operating system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system disables automatic logon via SSH. Check that automatic logon via SSH is disabled with the following command: # sudo grep -i "permitemptypasswords" /etc/ssh/sshd_config PermitEmptyPasswords no If "PermitEmptyPasswords" is not set to "no", is missing completely, or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-217269`

### Rule: The SUSE operating system must not allow users to override SSH environment variables.

**Rule ID:** `SV-217269r991591_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH environment options potentially allow users to bypass access restriction in some configurations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system disables unattended via SSH. Check that unattended logon via SSH is disabled with the following command: # sudo grep -i "permituserenvironment" /etc/ssh/sshd_config PermitUserEnvironment no If the "PermitUserEnvironment" keyword is not set to "no", is missing completely, or is commented out, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-217270`

### Rule: The SUSE operating system must implement DoD-approved encryption to protect the confidentiality of SSH remote connections.

**Rule ID:** `SV-217270r958408_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection (e.g., RDP), thereby providing a degree of confidentiality. The encryption strength of a mechanism is selected based on the security categorization of the information. The system will attempt to use the first cipher presented by the client that matches the server list. Listing the values "strongest to weakest" is a method to ensure the use of the strongest cipher available to secure the SSH connection. Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000120-GPOS-00061, SRG-OS-000125-GPOS-00065, SRG-OS-000250-GPOS-00093, SRG-OS-000393-GPOS-00173</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SUSE operating system implements DoD-approved encryption to protect the confidentiality of SSH remote connections. Check the SSH daemon configuration for allowed ciphers with the following command: # sudo grep -i ciphers /etc/ssh/sshd_config | grep -v '^#' Ciphers aes256-ctr,aes192-ctr,aes128-ctr If any ciphers other than "aes256-ctr", "aes192-ctr", or "aes128-ctr" are listed, the order differs from the example above, the "Ciphers" keyword is missing, or the returned line is commented out, this is a finding.

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-217271`

### Rule: The SUSE operating system SSH daemon must be configured to only use Message Authentication Codes (MACs) employing FIPS 140-2 approved cryptographic hash algorithms.

**Rule ID:** `SV-217271r958510_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. The system will attempt to use the first hash presented by the client that matches the server list. Listing the values "strongest to weakest" is a method to ensure the use of the strongest hash available to secure the SSH connection. Satisfies: SRG-OS-000125-GPOS-00065, SRG-OS-000394-GPOS-00174</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system SSH daemon is configured to only use MACs that employ FIPS 140-2 approved hashes. Check that the SSH daemon is configured to only use MACs that employ FIPS 140-2 approved hashes with the following command: # sudo grep -i macs /etc/ssh/sshd_config MACs hmac-sha2-512,hmac-sha2-256 If any hashes other than "hmac-sha2-512" or "hmac-sha2-256" are listed, the order differs from the example above, they are missing, or the returned line is commented out, this is a finding.

## Group: SRG-OS-000126-GPOS-00066

**Group ID:** `V-217272`

### Rule: The SUSE operating system SSH daemon must be configured with a timeout interval.

**Rule ID:** `SV-217272r1015228_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the SUSE operating system level, and deallocating networking assignments at the application level if multiple application sessions are using a single SUSE operating system-level network connection. This does not mean that the SUSE operating system terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session. Satisfies: SRG-OS-000126-GPOS-00066, SRG-OS-000163-GPOS-00072, SRG-OS-000279-GPOS-00109</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system SSH daemon is configured to timeout idle sessions. Check that the "ClientAliveInterval" parameter is set to a value of "600" with the following command: # sudo grep -i clientalive /etc/ssh/sshd_config ClientAliveInterval 600 If "ClientAliveInterval" is not set to "600" in "/etc/ssh/sshd_config", this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-217273`

### Rule: The SUSE operating system for all network connections associated with SSH traffic must immediately terminate at the end of the session or after 10 minutes of inactivity.

**Rule ID:** `SV-217273r1015229_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination terminates all processes associated with a user's logical session except those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific SUSE operating system functionality where the system owner, data owner, or organization requires additional assurance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all network connections associated with SSH traffic are automatically terminated at the end of the session or after "10" minutes of inactivity. Check that the "ClientAliveCountMax" variable is set to a value of "1" or less by performing the following command: # sudo grep -i clientalive /etc/ssh/sshd_config ClientAliveInterval 600 ClientAliveCountMax 1 If "ClientAliveCountMax" does not exist or "ClientAliveCountMax" is not set to a value of "1" in "/etc/ssh/sshd_config", or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217274`

### Rule: The SUSE operating system SSH daemon must be configured to not allow authentication using known hosts authentication.

**Rule ID:** `SV-217274r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring this setting for the SSH daemon provides additional assurance that remote logon via SSH will require a password, even in the event of misconfiguration elsewhere.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system SSH daemon is configured to not allow authentication using known hosts authentication. To determine how the SSH daemon's "IgnoreUserKnownHosts" option is set, run the following command: # sudo grep -i IgnoreUserKnownHosts /etc/ssh/sshd_config IgnoreUserKnownHosts yes If the value is returned as "no", the returned line is commented out, or no output is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217275`

### Rule: The SUSE operating system SSH daemon public host key files must have mode 0644 or less permissive.

**Rule ID:** `SV-217275r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a public host key file is modified by an unauthorized user, the SSH service may be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system SSH daemon public host key files have mode "0644" or less permissive. Note: SSH public key files may be found in other directories on the system depending on the installation. The following command will find all SSH public key files on the system: > find /etc/ssh -name 'ssh_host*key.pub' -exec stat -c "%a %n" {} \; 644 /etc/ssh/ssh_host_rsa_key.pub 644 /etc/ssh/ssh_host_dsa_key.pub 644 /etc/ssh/ssh_host_ecdsa_key.pub 644 /etc/ssh/ssh_host_ed25519_key.pub If any file has a mode more permissive than "0644", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217276`

### Rule: The SUSE operating system SSH daemon private host key files must have mode 0640 or less permissive.

**Rule ID:** `SV-217276r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an unauthorized user obtains the private SSH host key file, the host could be impersonated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system SSH daemon private host key files have mode "0640" or less permissive. The following command will find all SSH private key files on the system: > sudo find / -name '*ssh_host*key' -exec ls -lL {} \; Check the mode of the private host key files under "/etc/ssh" file with the following command: > find /etc/ssh -name 'ssh_host*key' -exec stat -c "%a %n" {} \; 640 /etc/ssh/ssh_host_rsa_key 640 /etc/ssh/ssh_host_dsa_key 640 /etc/ssh/ssh_host_ecdsa_key 640 /etc/ssh/ssh_host_ed25519_key If any file has a mode more permissive than "0640", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217277`

### Rule: The SUSE operating system SSH daemon must perform strict mode checking of home directory configuration files.

**Rule ID:** `SV-217277r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If other users have access to modify user-specific SSH configuration files, they may be able to log on to the system as another user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system SSH daemon performs strict mode checking of home directory configuration files. Check that the SSH daemon performs strict mode checking of home directory configuration files with the following command: # sudo grep -i strictmodes /etc/ssh/sshd_config StrictModes yes If "StrictModes" is set to "no", is missing, or the returned line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217278`

### Rule: The SUSE operating system SSH daemon must use privilege separation.

**Rule ID:** `SV-217278r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH daemon privilege separation causes the SSH process to drop root privileges when not needed, which would decrease the impact of software vulnerabilities in the unprivileged section.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine the version of SSH using the following command: # ssh -V OpenSSH_7.9p1 If the version of SSH is 7.5 or newer, this is Not Applicable. Verify the SUSE operating system SSH daemon is configured to use privilege separation. Check that the SUSE operating system SSH daemon performs privilege separation with the following command: # sudo grep -i usepriv /etc/ssh/sshd_config UsePrivilegeSeparation yes If the "UsePrivilegeSeparation" keyword is not set to "yes" or "sandbox", is missing, or the returned line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217279`

### Rule: The SUSE operating system SSH daemon must not allow compression or must only allow compression after successful authentication.

**Rule ID:** `SV-217279r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If compression is allowed in an SSH connection prior to authentication, vulnerabilities in the compression software could result in compromise of the system from an unauthenticated connection, potentially with root privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the installed version of OpenSSH is 7.4 or above, this requirement is not applicable. Verify the SUSE operating system SSH daemon performs compression after a user successfully authenticates. Check that the SSH daemon performs compression after a user successfully authenticates with the following command: # sudo grep -i compression /etc/ssh/sshd_config Compression delayed If the "Compression" keyword is set to "yes", is missing, or the returned line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217280`

### Rule: The SUSE operating system SSH daemon must disable forwarded remote X connections for interactive users, unless to fulfill documented and validated mission requirements.

**Rule ID:** `SV-217280r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The security risk of using X11 forwarding is that the client's X11 display server may be exposed to attack when the SSH client requests forwarding. A system administrator may have a stance in which they want to protect clients that may expose themselves to attack by unwittingly requesting X11 forwarding, which can warrant a ''no'' setting. X11 forwarding should be enabled with caution. Users with the ability to bypass file permissions on the remote host (for the user's X11 authorization database) can access the local X11 display through the forwarded connection. An attacker may then be able to perform activities such as keystroke monitoring if the ForwardX11Trusted option is also enabled. If X11 services are not required for the system's intended function, they should be disabled or restricted as appropriate to the system’s needs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if X11Forwarding is disabled with the following command: # sudo grep -i x11forwarding /etc/ssh/sshd_config X11Forwarding no If the "X11Forwarding" keyword is set to "yes" and is not documented with the Information System Security Officer (ISSO) as an operational requirement, is missing, or is commented out, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-217281`

### Rule: The SUSE operating system clock must, for networked systems, be synchronized to an authoritative DoD time source at least every 24 hours.

**Rule ID:** `SV-217281r1038944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). Satisfies: SRG-OS-000355-GPOS-00143, SRG-OS-000356-GPOS-00144</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system clock must be configured to synchronize to an authoritative DoD time source when the time difference is greater than one second. Check that the SUSE operating system clock must be configured to synchronize to an authoritative DoD time source when the time difference is greater than one second with the following command: > sudo grep maxpoll /etc/ntp.conf server 0.us.pool.ntp.mil maxpoll 16 If nothing is returned or "maxpoll" is greater than "16", or is commented out, this is a finding. Verify the "ntp.conf" file is configured to an authoritative DoD time source by running the following command: > sudo grep -i server /etc/ntp.conf server 0.us.pool.ntp.mil If the parameter "server" is not set or is not set to an authoritative DoD time source, this is a finding.

## Group: SRG-OS-000359-GPOS-00146

**Group ID:** `V-217282`

### Rule: The SUSE operating system must be configured to use Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

**Rule ID:** `SV-217282r958788_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the SUSE operating system include date and time. Time is commonly expressed in UTC, a modern continuation of GMT, or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SUSE operating system is configured to use UTC or GMT. Check that the SUSE operating system is configured to use UTC or GMT with the following command: > timedatectl status | grep -i "time zone" Timezone: UTC (UTC, +0000) If "Time zone" is not set to "UTC" or "GMT", this is a finding.

## Group: SRG-OS-000433-GPOS-00192

**Group ID:** `V-217283`

### Rule: The SUSE operating system must implement kptr-restrict to prevent the leaking of internal kernel addresses.

**Rule ID:** `SV-217283r958928_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in nonexecutable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can either be hardware-enforced or software-enforced, with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system prevents leaking of internal kernel addresses. Check that the SUSE operating system prevents leaking of internal kernel addresses by running the following command: > sudo sysctl kernel.kptr_restrict kernel.kptr_restrict = 1 If the kernel parameter "kptr_restrict" is not equal to "1" or nothing is returned, this is a finding.

## Group: SRG-OS-000433-GPOS-00193

**Group ID:** `V-217284`

### Rule: Address space layout randomization (ASLR) must be implemented by the SUSE operating system to protect memory from unauthorized code execution.

**Rule ID:** `SV-217284r958928_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in nonexecutable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can either be hardware-enforced or software-enforced, with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system implements ASLR. Check that the SUSE operating system implements ASLR by running the following command: > sudo sysctl kernel.randomize_va_space kernel.randomize_va_space = 2 If the kernel parameter "randomize_va_space" is not equal to "2" or nothing is returned, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-217285`

### Rule: The SUSE operating system must off-load rsyslog messages for networked systems in real time and off-load standalone systems at least weekly.

**Rule ID:** `SV-217285r959008_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SUSE operating system must off-load rsyslog messages for networked systems in real time and off-load standalone systems at least weekly. For stand-alone hosts, verify with the System Administrator that the log files are off-loaded at least weekly. For networked systems, check that rsyslog is sending log messages to a remote server with the following command: # sudo grep "\*.\*" /etc/rsyslog.conf | grep "@" | grep -v "^#" *.*;mail.none;news.none @192.168.1.101:514 If any active message labels in the file do not have a line to send log messages to a remote server, this is a finding.

## Group: SRG-OS-000142-GPOS-00071

**Group ID:** `V-217286`

### Rule: The SUSE operating system must be configured to use TCP syncookies.

**Rule ID:** `SV-217286r958528_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Denial of Service (DoS) is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Managing excess capacity ensures that sufficient capacity is available to counter flooding attacks. Employing increased capacity and service redundancy may reduce the susceptibility to some DoS attacks. Managing excess capacity may include, for example, establishing selected usage priorities, quotas, or partitioning.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system is configured to use TCP syncookies. Check to see if syncookies are used with the following command: # sudo sysctl net.ipv4.tcp_syncookies net.ipv4.tcp_syncookies = 1 If the value is not set to "1", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217287`

### Rule: The SUSE operating system must not forward Internet Protocol version 4 (IPv4) source-routed packets.

**Rule ID:** `SV-217287r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when IPv4 forwarding is enabled and the system is functioning as a router.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system does not accept IPv4 source-routed packets. Check the value of the accept source route variable with the following command: # sysctl net.ipv4.conf.all.accept_source_route net.ipv4.conf.all.accept_source_route = 0 If the returned line does not have a value of "0" this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217288`

### Rule: The SUSE operating system must not forward Internet Protocol version 6 (IPv6) source-routed packets.

**Rule ID:** `SV-217288r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when IPv4 forwarding is enabled and the system is functioning as a router.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system does not accept IPv6 source-routed packets. Check the value of the accept source route variable with the following command: # sudo sysctl net.ipv6.conf.all.accept_source_route net.ipv6.conf.all.accept_source_route = 0 If the returned line does not have a value of "0", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217289`

### Rule: The SUSE operating system must not forward Internet Protocol version 4 (IPv4) source-routed packets by default.

**Rule ID:** `SV-217289r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when IPv4 forwarding is enabled and the system is functioning as a router.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system does not accept IPv4 source-routed packets by default. Check the value of the default accept source route variable with the following command: # sysctl net.ipv4.conf.default.accept_source_route net.ipv4.conf.default.accept_source_route = 0 If the returned line does not have a value of "0" this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217290`

### Rule: The SUSE operating system must not respond to Internet Protocol version 4 (IPv4) Internet Control Message Protocol (ICMP) echoes sent to a broadcast address.

**Rule ID:** `SV-217290r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Responding to broadcast (ICMP) echoes facilitates network mapping and provides a vector for amplification attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system does not accept IPv4 source-routed packets. Check the value of the accept source route variable with the following command: # sysctl net.ipv4.icmp_echo_ignore_broadcasts net.ipv4.icmp_echo_ignore_broadcasts = 1 If the returned line does not have a value of "1" this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217291`

### Rule: The SUSE operating system must prevent Internet Protocol version 4 (IPv4) Internet Control Message Protocol (ICMP) redirect messages from being accepted.

**Rule ID:** `SV-217291r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system does not accept ICMP redirect messages. Check the value of the "net.ipv4.conf.all.accept_redirects" variable with the following command: # sysctl net.ipv4.conf.all.accept_redirects net.ipv4.conf.all.accept_redirects =0 If the returned line does not have a value of "0" this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217292`

### Rule: The SUSE operating system must not allow interfaces to accept Internet Protocol version 4 (IPv4) Internet Control Message Protocol (ICMP) redirect messages by default.

**Rule ID:** `SV-217292r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system ignores IPv4 ICMP redirect messages. Check the value of the "accept_redirects" variables with the following command: # sysctl net.ipv4.conf.default.accept_redirects net.ipv4.conf.default.accept_redirects = 0 If the returned line does not have a value of "0" this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217293`

### Rule: The SUSE operating system must not allow interfaces to accept Internet Protocol version 6 (IPv6) Internet Control Message Protocol (ICMP) redirect messages by default.

**Rule ID:** `SV-217293r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system does not allow IPv6 ICMP redirect messages by default. Check the value of the "default accept_redirects" variables with the following command: # sudo sysctl net.ipv6.conf.default.accept_redirects net.ipv6.conf.default.accept_redirects = 0 If the returned line does not have a value of "0", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217294`

### Rule: The SUSE operating system must not allow interfaces to send Internet Protocol version 4 (IPv4) Internet Control Message Protocol (ICMP) redirect messages by default.

**Rule ID:** `SV-217294r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages contain information from the system's route table, possibly revealing portions of the network topology.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system does not allow interfaces to perform IPv4 ICMP redirects by default. Check the value of the "default send_redirects" variables with the following command: # sysctl net.ipv4.conf.default.send_redirects net.ipv4.conf.default.send_redirects = 0 If the returned line does not have a value of "0” this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217295`

### Rule: The SUSE operating system must not send Internet Protocol version 4 (IPv4) Internet Control Message Protocol (ICMP) redirects.

**Rule ID:** `SV-217295r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages contain information from the system's route table, possibly revealing portions of the network topology.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system does not send IPv4 ICMP redirect messages. Check the value of the "all send_redirects" variables with the following command: # sysctl net.ipv4.conf.all.send_redirects net.ipv4.conf.all.send_redirects =0 If the returned line does not have a value of "0” this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217296`

### Rule: The SUSE operating system must not be performing Internet Protocol version 4 (IPv4) packet forwarding unless the system is a router.

**Rule ID:** `SV-217296r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system is not performing IPv4packet forwarding, unless the system is a router. Check to see if IPv4 forwarding is enabled using the following command: > sysctl net.ipv4.ip_forward net.ipv4.ip_forward = 0 If the network parameter "ipv4.ip_forward" is not equal to "0" or nothing is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-217297`

### Rule: The SUSE operating system must not have network interfaces in promiscuous mode unless approved and documented.

**Rule ID:** `SV-217297r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network interfaces in promiscuous mode allow for the capture of all network traffic visible to the system. If unauthorized individuals can access these applications, it may allow then to collect information such as logon IDs, passwords, and key exchanges between systems. If the system is being used to perform a network troubleshooting function, the use of these tools must be documented with the Information System Security Officer (ISSO) and restricted to only authorized personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system network interfaces are not in promiscuous mode unless approved by the ISSO and documented. Check for the status with the following command: # ip link | grep -i promisc If network interfaces are found on the system in promiscuous mode and their use has not been approved by the ISSO and documented, this is a finding.

## Group: SRG-OS-000299-GPOS-00117

**Group ID:** `V-217298`

### Rule: The SUSE operating system wireless network adapters must be disabled unless approved and documented.

**Rule ID:** `SV-217298r991568_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of communications with wireless peripherals, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read, altered, or used to compromise the SUSE operating system. This requirement applies to wireless peripheral technologies (e.g., wireless mice, keyboards, displays, etc.) used with A SUSE operating system. Wireless peripherals (e.g., Wi-Fi/Bluetooth/IR Keyboards, Mice, and Pointing Devices and Near Field Communications [NFC]) present a unique challenge by creating an open, unsecured port on a computer. Wireless peripherals must meet DoD requirements for wireless data transmission and be approved for use by the AO. Even though some wireless peripherals, such as mice and pointing devices, do not ordinarily carry information that need to be protected, modification of communications with these wireless peripherals may be used to compromise the SUSE operating system. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of communications with wireless peripherals can be accomplished by physical means (e.g., employing physical barriers to wireless radio frequencies) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. If the wireless peripheral is only passing telemetry data, encryption of the data may not be required. Satisfies: SRG-OS-000299-GPOS-00117, SRG-OS-000300-GPOS-00118, SRG-OS-000481-GPOS-000481</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SUSE operating system has no wireless network adapters enabled. Check that there are no wireless interfaces configured on the system with the following command: # wicked show all lo up link: #1, state up type: loopback config: compat:suse:/etc/sysconfig/network/ifcfg-lo leases: ipv4 static granted leases: ipv6 static granted addr: ipv4 127.0.0.1/8 [static] addr: ipv6 ::1/128 [static] eth0 up link: #2, state up, mtu 1500 type: ethernet, hwaddr 06:00:00:00:00:01 config: compat:suse:/etc/sysconfig/network/ifcfg-eth0 leases: ipv4 dhcp granted leases: ipv6 dhcp granted, ipv6 auto granted addr: ipv4 10.0.0.100/16 [dhcp] route: ipv4 default via 10.0.0.1 proto dhcp wlan0 up link: #3, state up, mtu 1500 type: wireless, hwaddr 06:00:00:00:00:02 config: wicked:xml:/etc/wicked/ifconfig/wlan0.xml leases: ipv4 dhcp granted addr: ipv4 10.0.0.101/16 [dhcp] route: ipv4 default via 10.0.0.1 proto dhcp If a wireless interface is configured it must be documented and approved by the local Authorizing Official. If a wireless interface is configured and has not been documented and approved, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-217299`

### Rule: The SUSE operating system must have the packages required for multifactor authentication to be installed.

**Rule ID:** `SV-217299r1015231_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a CAC or token that is separate from the information system, ensures that even if the information system is compromised, that compromise will not affect credentials stored on the authentication device. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification card and the DoD Common Access Card. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., VPN, proxy capability). This does not apply to authentication for the purpose of configuring the device itself (management). Satisfies: SRG-OS-000375-GPOS-00160, SRG-OS-000376-GPOS-00161, SRG-OS-000377-GPOS-00162</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system has the packages required for multifactor authentication installed. Check for the presence of the packages required to support multifactor authentication with the following commands: # zypper se pam_pkcs11 i | pam_pkcs11 | PKCS #11 PAM Module | package # zypper se mozilla-nss i | mozilla-nss | Network Security Services | package i | mozilla-nss-tools | Tools for developing, debugging, and managing applications t-> | package # zypper se pcsc i | pcsc-ccid | PCSC Driver for CCID Based Smart Card Readers and GemPC Twin -> | package i | pcsc-lite | PCSC Smart Cards Library | package i | pcsc-tools | PCSC Tools | package # zypper se opensc i | opensc | Smart Card Utilities | package # zypper info coolkey | grep -i installed Installed: Yes If any of the packages required for multifactor authentication are not installed, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-217300`

### Rule: The SUSE operating system must implement certificate status checking for multifactor authentication.

**Rule ID:** `SV-217300r1015232_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a Common Access Card (CAC) or token separate from the information system, ensures credentials stored on the authentication device will not be affected if the information system is compromised. Multifactor solutions that require devices separate from information systems to gain access include: hardware tokens providing time-based or challenge-response authenticators, and smart cards such as the U.S. Government Personal Identity Verification (PIV) card and the DoD CAC. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. This requirement only applies to components with device-specific functions, or for organizational users (e.g., VPN, proxy capability). This does not apply to authentication for the purpose of configuring the device itself (management). Satisfies: SRG-OS-000375-GPOS-00160, SRG-OS-000376-GPOS-00161, SRG-OS-000377-GPOS-00162</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system implements certificate status checking for multifactor authentication. Check that certificate status checking for multifactor authentication is implemented with the following command: # grep use_pkcs11_module /etc/pam_pkcs11/pam_pkcs11.conf | awk '/pkcs11_module coolkey {/,/}/' /etc/pam_pkcs11/pam_pkcs11.conf | grep cert_policy cert_policy = ca,ocsp_on,signature,crl_auto; If "cert_policy" is not set to include "ocsp_on", this is a finding.

## Group: SRG-OS-000068-GPOS-00036

**Group ID:** `V-217301`

### Rule: The SUSE operating system must implement multifactor authentication for access to privileged accounts via pluggable authentication modules (PAM).

**Rule ID:** `SV-217301r1015233_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a CAC or token that is separate from the information system, ensures that even if the information system is compromised, that compromise will not affect credentials stored on the authentication device. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification card and the DoD Common Access Card. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., VPN, proxy capability). This does not apply to authentication for the purpose of configuring the device itself (management). Satisfies: SRG-OS-000068-GPOS-00036, SRG-OS-000105-GPOS-00052, SRG-OS-000106-GPOS-00053, SRG-OS-000107-GPOS-00054, SRG-OS-000108-GPOS-00055, SRG-OS-000375-GPOS-00160, SRG-OS-000375-GPOS-00161, SRG-OS-000375-GPOS-00162</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system implements multifactor authentication for remote access to privileged accounts via pluggable authentication modules (PAM). Check that the "pam_pkcs11.so" option is configured in the "/etc/pam.d/common-auth" file with the following command: # grep pam_pkcs11.so /etc/pam.d/common-auth auth sufficient pam_pkcs11.so If "pam_pkcs11.so" is not set in "/etc/pam.d/common-auth", this is a finding.

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-217302`

### Rule: The SUSE operating system, for PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

**Rule ID:** `SV-217302r1015234_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement. Satisfies: SRG-OS-000066-GPOS-00034, SRG-OS-000384-GPOS-00167</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system, for PKI-based authentication, had valid certificates by constructing a certification path (which includes status information) to an accepted trust anchor. Check that the certification path to an accepted trust anchor for multifactor authentication is implemented with the following command: > grep cert_policy /etc/pam_pkcs11/pam_pkcs11.conf cert_policy = ca,oscp_on,signature,crl_auto; If "cert_policy" is not set to include "ca", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-222386`

### Rule: The SUSE operating system must use a virus scan program.

**Rule ID:** `SV-222386r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Virus scanning software can be used to protect a system from penetration from computer viruses and to limit their spread through intermediate systems. The virus scanning software should be configured to perform scans dynamically on accessed files. If this capability is not available, the system must be configured to scan, at a minimum, all altered files on the system on a daily basis. If the system processes inbound SMTP mail, the virus scanner must be configured to scan all received mail.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an anti-virus solution is installed on the system. The anti-virus solution may be bundled with an approved host-based security solution. If there is no anti-virus solution installed on the system, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-233308`

### Rule: The SUSE operating system SSH daemon must prevent remote hosts from connecting to the proxy display.

**Rule ID:** `SV-233308r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When X11 forwarding is enabled, there may be additional exposure to the server and client displays if the sshd proxy display is configured to listen on the wildcard address. By default, sshd binds the forwarding server to the loopback address and sets the hostname part of the DIPSLAY environment variable to localhost. This prevents remote hosts from connecting to the proxy display.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system SSH daemon prevents remote hosts from connecting to the proxy display. Check the SSH X11UseLocalhost setting with the following command: # sudo grep -i x11uselocalhost /etc/ssh/sshd_config X11UseLocalhost yes If the "X11UseLocalhost" keyword is set to "no", is missing, or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237603`

### Rule: The SUSE operating system must restrict privilege elevation to authorized personnel.

**Rule ID:** `SV-237603r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The sudo command allows a user to execute programs with elevated (administrator) privileges. It prompts the user for their password and confirms your request to execute a command by checking a file, called sudoers. If the "sudoers" file is not configured correctly, any user defined on the system can initiate privileged actions on the target system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "sudoers" file restricts sudo access to authorized personnel. $ sudo grep -iw 'ALL' /etc/sudoers /etc/sudoers.d/* If the either of the following entries are returned, this is a finding: ALL ALL=(ALL) ALL ALL ALL=(ALL:ALL) ALL

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237604`

### Rule: The SUSE operating system must use the invoking user's password for privilege escalation when using "sudo".

**Rule ID:** `SV-237604r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The sudoers security policy requires that users authenticate themselves before they can use sudo. When sudoers requires authentication, it validates the invoking user's credentials. If the rootpw, targetpw, or runaspw flags are defined and not disabled, by default the operating system will prompt the invoking user for the "root" user password. For more information on each of the listed configurations, reference the sudoers(5) manual page.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the sudoers security policy is configured to use the invoking user's password for privilege escalation. > sudo egrep -ir '(rootpw|targetpw|runaspw)' /etc/sudoers /etc/sudoers.d* | grep -v '#' /etc/sudoers:Defaults !targetpw /etc/sudoers:Defaults !rootpw /etc/sudoers:Defaults !runaspw If conflicting results are returned, this is a finding. If "Defaults !targetpw" is not defined, this is a finding. If "Defaults !rootpw" is not defined, this is a finding. If "Defaults !runaspw" is not defined, this is a finding.

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-237605`

### Rule: The SUSE operating system must require re-authentication when using the "sudo" command.

**Rule ID:** `SV-237605r1050789_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without re-authentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the organization requires the user to re-authenticate when using the "sudo" command. If the value is set to an integer less than 0, the user's time stamp will not expire and the user will not have to re-authenticate for privileged actions until the user's session is terminated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system requires re-authentication when using the "sudo" command to elevate privileges. > sudo grep -ir 'timestamp_timeout' /etc/sudoers /etc/sudoers.d /etc/sudoers:Defaults timestamp_timeout=0 If conflicting results are returned, this is a finding. If "timestamp_timeout" is set to a negative number, is commented out, or no results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237606`

### Rule: The SUSE operating system must not have unnecessary account capabilities.

**Rule ID:** `SV-237606r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accounts providing no operational purpose provide additional opportunities for system compromise. Therefore all necessary non-interactive accounts should not have an interactive shell assigned to them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all non-interactive SUSE operating system accounts do not have an interactive shell assigned to them. Obtain the list of authorized system accounts from the Information System Security Officer (ISSO). Check the system accounts on the system with the following command: > awk -F: '($7 !~ "/sbin/nologin" && $7 !~ "/bin/false"){print $1 ":" $3 ":" $7}' /etc/passwd root:0:/bin/bash nobody:65534:/bin/bash If a non-interactive accounts such as "games" or "nobody" is listed with an interactive shell, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-237607`

### Rule: The SUSE operating system library files must have mode 0755 or less permissive.

**Rule ID:** `SV-237607r1106480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the SUSE operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SUSE operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and "/usr/lib64" have mode 0755 or less permissive. Check that the systemwide shared library files have mode 0755 or less permissive with the following command: > sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' -perm /022 -exec stat -c "%n %a" {} + If any output is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-237608`

### Rule: The SUSE operating system library directories must have mode 0755 or less permissive.

**Rule ID:** `SV-237608r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the SUSE operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SUSE operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system-wide shared library directories "/lib", "/lib64", "/usr/lib" and "/usr/lib64" have mode 0755 or less permissive. Check that the system-wide shared library directories have mode 0755 or less permissive with the following command: > sudo find /lib /lib64 /usr/lib /usr/lib64 -perm /022 -type d -exec stat -c "%n %a" '{}' \; If any of the aforementioned directories are found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-237609`

### Rule: The SUSE operating system library files must be owned by root.

**Rule ID:** `SV-237609r1102108_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the SUSE operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SUSE operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and "/usr/lib64" are owned by root with the following command: > sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' ! -user root -exec stat -c "%n %U" {} + If any output is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-237610`

### Rule: The SUSE operating system library directories must be owned by root.

**Rule ID:** `SV-237610r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the SUSE operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SUSE operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system-wide shared library directories "/lib", "/lib64", "/usr/lib/" and "/usr/lib64" are owned by root. Check that the system-wide shared library directories are owned by root with the following command: > sudo find /lib /lib64 /usr/lib /usr/lib64 ! -user root -type d -exec stat -c "%n %U" '{}' \; If any system wide library directory is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-237611`

### Rule: The SUSE operating system library files must be group-owned by root.

**Rule ID:** `SV-237611r1102111_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the SUSE operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SUSE operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and "/usr/lib64" are group owned by root with the following command: > sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' ! -group root -exec stat -c "%n %G" {} + If any output is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-237612`

### Rule: The SUSE operating system library directories must be group-owned by root.

**Rule ID:** `SV-237612r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the SUSE operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SUSE operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system-wide library directories "/lib", "/lib64", "/usr/lib" and "/usr/lib64" are group-owned by root. Check that the system-wide library directories are group-owned by root with the following command: > sudo find /lib /lib64 /usr/lib /usr/lib64 ! -group root -type d -exec stat -c "%n %G" '{}' \; If any system wide shared library directory is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-237613`

### Rule: The SUSE operating system must have system commands set to a mode of 755 or less permissive.

**Rule ID:** `SV-237613r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the SUSE operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SUSE operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands contained in the following directories have mode 755 or less permissive: /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin Check that the system command files have mode 755 or less permissive with the following command: > find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin -perm /022 -type f -exec stat -c "%n %a" '{}' \; If any files are found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-237614`

### Rule: The SUSE operating system must have directories that contain system commands set to a mode of 0755 or less permissive.

**Rule ID:** `SV-237614r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the SUSE operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SUSE operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands directories have mode 0755 or less permissive: /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin Check that the system command directories have mode 0755 or less permissive with the following command: > find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin -perm /022 -type d -exec stat -c "%n %a" '{}' \; If any directories are found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-237615`

### Rule: The SUSE operating system must have system commands owned by root.

**Rule ID:** `SV-237615r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the SUSE operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SUSE operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands contained in the following directories are owned by root: /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin Use the following command for the check: > sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -user root -type f -exec stat -c "%n %U" '{}' \; If any system commands are returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-237616`

### Rule: The SUSE operating system must have directories that contain system commands owned by root.

**Rule ID:** `SV-237616r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the SUSE operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SUSE operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands directories are owned by root: /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin Use the following command for the check: > sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -user root -type d -exec stat -c "%n %U" '{}' \; If any system commands directories are returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-237617`

### Rule: The SUSE operating system must have system commands group-owned by root or a system account.

**Rule ID:** `SV-237617r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the SUSE operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SUSE operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands contained in the following directories are group-owned by root or a system account: /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin Run the check with the following command: > sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -group root -type f -exec stat -c "%n %G" '{}' \; If any system commands are returned that are not Set Group ID upon execution (SGID) files and group-owned by a required system account, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-237618`

### Rule: The SUSE operating system must have directories that contain system commands group-owned by root.

**Rule ID:** `SV-237618r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the SUSE operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to SUSE operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands directories are group-owned by root: /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin Run the check with the following command: > sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -group root -type d -exec stat -c "%n %G" '{}' \; If any system commands directories are returned that are not Set Group ID up on execution (SGID) files and owned by a privileged account, this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-237619`

### Rule: The SUSE operating system must not have the vsftpd package installed if not required for operational support.

**Rule ID:** `SV-237619r987796_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for SUSE operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked, and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. SUSE operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions and functions). Examples of nonessential capabilities include but are not limited to games, software packages, tools, and demonstration software not related to requirements or providing a wide array of functionality not required for every mission but which cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the vsftpd package is not installed on the SUSE operating system. Check that the vsftpd package is not installed on the SUSE operating system by running the following command: > zypper info vsftpd | grep Installed If "vsftpd" is installed and is not documented with the Information System Security Officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237620`

### Rule: The SUSE operating system must not forward Internet Protocol version 6 (IPv6) source-routed packets by default.

**Rule ID:** `SV-237620r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest that routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when IPv4 forwarding is enabled and the system is functioning as a router.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system does not accept IPv6 source-routed packets by default. Check the value of the default IPv6 accept source route variable with the following command: > sudo sysctl net.ipv6.conf.default.accept_source_route net.ipv6.conf.default.accept_source_route = 0 If the network parameter "ipv6.conf.default.accept_source_route" is not equal to "0" or nothing is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237621`

### Rule: The SUSE operating system must prevent Internet Protocol version 6 (IPv6) Internet Control Message Protocol (ICMP) redirect messages from being accepted.

**Rule ID:** `SV-237621r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system does not accept IPv6 source-routed packets by default. Verify the SUSE operating system does not accept IPv6 ICMP redirect messages. Check the value of the IPv6 accept_redirects variable with the following command: > sudo sysctl net.ipv6.conf.all.accept_redirects net.ipv6.conf.all.accept_redirects =0 If the network parameter "ipv6.conf.all.accept_redirects" is not equal to "0" or nothing is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237622`

### Rule: The SUSE operating system must not be performing Internet Protocol version 6 (IPv6) packet forwarding unless the system is a router.

**Rule ID:** `SV-237622r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system is not performing IPv6 packet forwarding, unless the system is a router. Check to see if IPv6 forwarding is enabled using the following command: > sudo sysctl net.ipv6.conf.all.forwarding net.ipv6.conf.all.forwarding = 0 If the network parameter "ipv6.conf.all.forwarding" is not equal to "0" or nothing is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237623`

### Rule: The SUSE operating system must not be performing Internet Protocol version 6 (IPv6) packet forwarding by default unless the system is a router.

**Rule ID:** `SV-237623r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system is not performing IPv6 packet forwarding by default, unless the system is a router. Check to see if IPv6 forwarding is disabled by default using the following command: > sudo sysctl net.ipv6.conf.default.forwarding net.ipv6.conf.default.forwarding = 0 If the network parameter "ipv6.conf.default.forwarding" is not equal to "0" or nothing is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-251719`

### Rule: The SUSE operating system must specify the default "include" directory for the /etc/sudoers file.

**Rule ID:** `SV-251719r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "sudo" command allows authorized users to run programs (including shells) as other users, system users, and root. The "/etc/sudoers" file is used to configure authorized "sudo" users as well as the programs they are allowed to run. Some configuration options in the "/etc/sudoers" file allow configured users to run programs without re-authenticating. Use of these configuration options makes it easier for one compromised account to be used to compromise other accounts. It is possible to include other sudoers files from within the sudoers file currently being parsed using the #include and #includedir directives. When sudo reaches this line it will suspend processing of the current file (/etc/sudoers) and switch to the specified file/directory. Once the end of the included file(s) are reached, the rest of /etc/sudoers will be processed. Files that are included may themselves include other files. A hard limit of 128 nested include files is enforced to prevent include file loops.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the "include" and "includedir" directives are not present in the /etc/sudoers file, this requirement is not applicable. Verify the operating system specifies only the default "include" directory for the /etc/sudoers file with the following command: > sudo grep include /etc/sudoers #includedir /etc/sudoers.d If the results are not "/etc/sudoers.d" or additional files or directories are specified, this is a finding. Verify the operating system does not have nested "include" files or directories within the /etc/sudoers.d directory with the following command: > sudo grep -r include /etc/sudoers.d If results are returned, this is a finding.

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-251720`

### Rule: The SUSE operating system must not be configured to bypass password requirements for privilege escalation.

**Rule ID:** `SV-251720r1050789_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without re-authentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the user re-authenticate. Satisfies: SRG-OS-000373-GPOS-00156, SRG-OS-000373-GPOS-00157, SRG-OS-000373-GPOS-00158</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system is not configured to bypass password requirements for privilege escalation. Check the configuration of the "/etc/pam.d/sudo" file with the following command: $ sudo grep pam_succeed_if /etc/pam.d/sudo If any occurrences of "pam_succeed_if" are returned from the command, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-251721`

### Rule: The SUSE operating system must not have accounts configured with blank or null passwords.

**Rule ID:** `SV-251721r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log on and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the "/etc/shadow" file for blank passwords with the following command: $ sudo awk -F: '!$2 {print $1}' /etc/shadow If the command returns any results, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-251722`

### Rule: The SUSE operating system must generate audit records for all uses of the unlink, unlinkat, rename, renameat and rmdir syscalls.

**Rule ID:** `SV-251722r958412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, however, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SUSE operating system generates an audit record for all uses of the "unlink", "unlinkat", "rename", "renameat", and "rmdir" syscalls. Verify that the following command call is being audited by performing the following command to check the file system rules in "/etc/audit/audit.rules": > sudo grep 'unlink\|rename\|rmdir' /etc/audit/audit.rules -a always,exit -F arch=b32 -S unlink, unlinkat,rename,renameat,rmdir -F auid>=1000 -F auid!=4294967295 -k delete -a always,exit -F arch=b64 -S unlink, unlinkat,rename,renameat,rmdir -F auid>=1000 -F auid!=4294967295 -k delete If both the "b32" and "b64" audit rules are not defined for the "unlink", "unlinkat", "rename", "renameat", and "rmdir" syscalls, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-255914`

### Rule: The SUSE operating system SSH server must be configured to use only FIPS-validated key exchange algorithms.

**Rule ID:** `SV-255914r991554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections provided by FIPS-validated cryptographic algorithms, information can be viewed and altered by unauthorized users without detection. The system will attempt to use the first algorithm presented by the client that matches the server list. Listing the values "strongest to weakest" is a method to ensure the use of the strongest algorithm available to secure the SSH connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SSH server is configured to use only FIPS-validated key exchange algorithms: $ sudo grep -i kexalgorithms /etc/ssh/sshd_config KexAlgorithms ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256 If "KexAlgorithms" is not configured, is commented out, or does not contain only the algorithms "ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256" in exact order, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-255915`

### Rule: The SUSE operating system must restrict access to the kernel message buffer.

**Rule ID:** `SV-255915r958524_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Restricting access to the kernel message buffer limits access only to root. This prevents attackers from gaining additional system information as a nonprivileged user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system is configured to restrict access to the kernel message buffer with the following commands: $ sudo sysctl kernel.dmesg_restrict kernel.dmesg_restrict = 1 If "kernel.dmesg_restrict" is not set to "1" or is missing, this is a finding. Check that the configuration files are present to enable this kernel parameter: $ sudo grep -r kernel.dmesg_restrict /run/sysctl.d/* /etc/sysctl.d/* /usr/local/lib/sysctl.d/* /usr/lib/sysctl.d/* /lib/sysctl.d/* /etc/sysctl.conf 2> /dev/null /etc/sysctl.conf:kernel.dmesg_restrict = 1 /etc/sysctl.d/99-sysctl.conf:kernel.dmesg_restrict = 1 If "kernel.dmesg_restrict" is not set to "1", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-255916`

### Rule: The SUSE operating system must use a file integrity tool to verify correct operation of all security functions.

**Rule ID:** `SV-255916r958794_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly, and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. This requirement applies to the SUSE operating system performing security function verification/testing and/or systems and environments that require this functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Advanced Intrusion Detection Environment (AIDE) is installed and verifies the correct operation of all security functions. Check that the AIDE package is installed with the following command: $ sudo zypper if aide | grep "Installed" Installed: Yes If AIDE is not installed, ask the System Administrator how file integrity checks are performed on the system. If there is no application installed to perform integrity checks, this is a finding. If AIDE is installed, check if it has been initialized with the following command: $ sudo aide --check If the output is "Couldn't open file /var/lib/aide/aide.db for reading", this is a finding.

## Group: SRG-OS-000123-GPOS-00064

**Group ID:** `V-256980`

### Rule: The SUSE operating system must automatically expire temporary accounts within 72 hours.

**Rule ID:** `SV-256980r958508_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Temporary accounts are privileged or nonprivileged accounts that are established during pressing circumstances, such as new software or hardware configuration or an incident response, where the need for prompt account activation requires bypassing normal account authorization procedures. If any inactive temporary accounts are left enabled on the system and are not either manually removed or automatically expired within 72 hours, the security posture of the system will be degraded and exposed to exploitation by unauthorized users or insider threat actors. Temporary accounts are different from emergency accounts. Emergency accounts, also known as "last resort" or "break glass" accounts, are local logon accounts enabled on the system for emergency use by authorized system administrators to manage a system when standard logon methods are failing or not available. Emergency accounts are not subject to manual removal or scheduled expiration requirements. The automatic expiration of temporary accounts may be extended as needed by the circumstances but it must not be extended indefinitely. A documented permanent account should be established for privileged users who need long-term maintenance accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify temporary accounts have been provisioned with an expiration date of 72 hours. For every existing temporary account, run the following command to obtain its account expiration information: > sudo chage -l <temporary_account_name> | grep -i "account expires" Verify each of these accounts has an expiration date set within 72 hours. If any temporary accounts have no expiration date set or do not expire within 72 hours, this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-256981`

### Rule: The SUSE operating system must be configured to allow sending email notifications of unauthorized configuration changes to designated personnel.

**Rule ID:** `SV-256981r958794_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to the operating system. Changes to operating system configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of the operating system. The operating system's IMO/ISSO and SAs must be notified via email and/or monitoring system trap when there is an unauthorized modification of a configuration item.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the operating system is configured to allow sending email notifications. Note: The "mailx" package provides the "mail" command that is used to send email messages. Verify that the "mailx" package is installed on the system: > sudo zypper se mailx i | mailx | A MIME-Capable Implementation of the mailx Command | package If "mailx" package is not installed, this is a finding.

