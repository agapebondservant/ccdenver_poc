# STIG Benchmark: Anduril NixOS Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000298-GPOS-00116

**Group ID:** `V-268078`

### Rule: NixOS must enable the built-in firewall.

**Rule ID:** `SV-268078r1039122_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to immediately disconnect or disable remote access, an attack or other compromise taking place would not be immediately stopped. Operating system remote access functionality must have the capability to immediately disconnect current users remotely accessing the information system and/or disable further remote access. The speed of disconnect or disablement varies based on the criticality of mission's functions and the need to eliminate immediate or future remote access to organizational information systems. The remote access functionality (e.g., RDP) may implement features such as automatic disconnect (or user-initiated disconnect) in case of adverse information based on an indicator of compromise or attack. Satisfies: SRG-OS-000298-GPOS-00116, SRG-OS-000096-GPOS-00050, SRG-OS-000297-GPOS-00115, SRG-OS-000480-GPOS-00232</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS has the network firewall enabled with the following command: $ grep firewall.enable /etc/nixos/configuration.nix networking.firewall.enable = true; If "networking.firewall.enable" is not set to "true", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000002-GPOS-00002

**Group ID:** `V-268079`

### Rule: NixOS emergency or temporary user accounts must be provisioned with an expiration time of 72 hours or less.

**Rule ID:** `SV-268079r1039591_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If emergency or temporary user accounts remain active when no longer needed or for an excessive period, these accounts may be used to gain unauthorized access. To mitigate this risk, automated termination of all emergency or temporary accounts must be set upon account creation. Temporary accounts are established as part of normal account activation procedures when there is a need for short-term accounts without the demand for immediacy in account activation. Emergency accounts are privileged accounts that are established in response to crisis situations where the need for rapid account activation is required. Therefore, emergency account activation may bypass normal account authorization processes. If these accounts are automatically disabled, system maintenance during emergencies may not be possible, thus adversely affecting system availability. Emergency accounts are different from infrequently used accounts (i.e., local login accounts used by the organization's system administrators when network or normal login/access is not available). Infrequently used accounts are not subject to automatic termination dates. Emergency accounts are accounts created in response to crisis situations, usually for use by maintenance personnel. The automatic expiration or disabling time period may be extended as needed until the crisis is resolved; however, it must not be extended indefinitely. A permanent account should be established for privileged users who need long-term maintenance accounts. Satisfies: SRG-OS-000002-GPOS-00002, SRG-OS-000123-GPOS-00064</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that emergency or temporary accounts have been provisioned with an expiration date of 72 hours. For every existing emergency or temporary account, run the following command to obtain its account expiration information. $ sudo chage -l system_account_name If any emergency or temporary accounts have no expiration date set or do not expire within 72 hours, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-268080`

### Rule: NixOS must enable the audit daemon.

**Rule ID:** `SV-268080r1039128_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create an account. Auditing account creation actions provides logging that can be used for forensic purposes. Note: For the "security.audit.enable" configuration, both "true" and "lock" are valid values. The "true" value allows for loading of audit rules (synonymous with "-e 1" in audit rules), while the "lock" value loads audit rules and enforces that the rules cannot be changed without the system rebooting (synonymous with "-e 2"). Setting this value to "lock" is recommended to be performed as the final step in configuring the audit daemon. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000254-GPOS-00095, SRG-OS-000344-GPOS-00135, SRG-OS-000348-GPOS-00136, SRG-OS-000349-GPOS-00137, SRG-OS-000350-GPOS-00138, SRG-OS-000351-GPOS-00139, SRG-OS-000352-GPOS-00140, SRG-OS-000353-GPOS-00141, SRG-OS-000354-GPOS-00142, SRG-OS-000122-GPOS-00063, SRG-OS-000358-GPOS-00145</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS has the audit service configured with the following command: $ grep security.audit /etc/nixos/configuration.nix security.auditd.enable = true; security.audit.enable = true; If auditd, and audit are not set to true or lock, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-268081`

### Rule: NixOS must enforce the limit of three consecutive invalid login attempts by a user during a 15-minute time period.

**Rule ID:** `SV-268081r1039549_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000329-GPOS-00128, SRG-OS-000470-GPOS-00214</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that NixOS locks an account after three unsuccessful login attempts within 15 minutes with the following commands: $ cat /etc/pam.d/login auth required pam_faillock.so preauth deny=3 even_deny_root fail_interval=900 unlock_time=0 dir=/var/log/faillock If the "fail_interval" option is not set to "900" or less (but not "0") on the "preauth" lines with the "pam_faillock" module, or is missing from this line, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-268082`

### Rule: NixOS must be configured to display the Standard Mandatory DOD Notice and Consent Banner before granting local or remote access to the system via a command line user login.

**Rule ID:** `SV-268082r1039551_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreement." 2) Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that NixOS displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the system via a command line user login. Check /etc/nixos/configuration.nix and any files imported from it to ensure the attribute "services.getty.helpLine" is defined to the following value with the following command: $ grep -R helpLine /etc/nixos /etc/nixos/configuration.nix:services.getty.helpLine = '' You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. ''; If the "services.getty.helpLine" service is not configured with a banner, or the banner does not match the Standard Mandatory DOD Notice and Consent Banner, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-268083`

### Rule: NixOS must be configured to display the Standard Mandatory DOD Notice and Consent Banner before granting local or remote access to the system via an SSH login.

**Rule ID:** `SV-268083r1039553_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreement." 2) Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the system via an SSH login. Check /etc/nixos/configuration.nix and any files imported from it to ensure the attribute "services.openssh.banner" is defined with the following value with the following command: $ grep -R openssh.banner /etc/nixos /etc/nixos/configuration.nix:services.openssh.banner = '' You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. ''; If the "services.openssh.banner" service is not configured with a banner, or the banner does not match the Standard Mandatory DOD Notice and Consent Banner, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-268084`

### Rule: NixOS must be configured to display the Standard Mandatory DOD Notice and Consent Banner before granting local or remote access to the system via a graphical user login.

**Rule ID:** `SV-268084r1039592_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreement." 2) Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist. Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the system via the graphical user login with the following command: $ grep -R gdm.banner /etc/nixos /etc/nixos/configuration.nix:services.xserver.displayManager.gdm.banner = "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details."; If the "services.xserver.displayManager.gdm.banner" service is not configured with a banner, or the banner does not match the Standard Mandatory DOD Notice and Consent Banner, this is a finding.

## Group: SRG-OS-000027-GPOS-00008

**Group ID:** `V-268085`

### Rule: NixOS must be configured to limit the number of concurrent sessions to ten for all accounts and/or account types.

**Rule ID:** `SV-268085r1039143_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Operating system management includes the ability to control the number of users and user sessions that use an operating system. Limiting the number of allowed users and sessions per user is helpful in reducing the risks related to denial-of-service (DoS) attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS limits the number of concurrent sessions to ten for all accounts and/or account types. Check /etc/nixos/configuration.nix and any files imported from it to ensure the attribute "security.pam.loginLimits" is defined to include the following value with the following command: $ grep -R -A 5 pam.loginLimits /etc/nixos /etc/nixos/configuration.nix:security.pam.loginLimits = [ /etc/nixos/configuration.nix:{ /etc/nixos/configuration.nix:domain = "*"; /etc/nixos/configuration.nix:item = "maxlogins"; /etc/nixos/configuration.nix:type = "hard"; /etc/nixos/configuration.nix:value = "10"; If the "maxlogins" item is missing, commented out, or the value is set greater than "10" and is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-268086`

### Rule: NixOS must initiate a session lock after a 10-minute period of inactivity for graphical user login.

**Rule ID:** `SV-268086r1039559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, operating systems need to be able to identify when a user's session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS initiates a session lock after a 10-minute period of inactivity for graphical user login with the following command: $ sudo gsettings get org.gnome.desktop.session idle-delay uint32 600 If "idle-delay" is set to "0" or a value greater than "600", this is a finding.

## Group: SRG-OS-000030-GPOS-00011

**Group ID:** `V-268087`

### Rule: NixOS must provide the capability for users to directly initiate a session lock for all connection types.

**Rule ID:** `SV-268087r1039606_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Rather than be forced to wait for a period of time to expire before the user session can be locked, operating systems need to provide users with the ability to manually invoke a session lock so users may secure their session should the need arise for them to temporarily vacate the immediate physical vicinity. Satisfies: SRG-OS-000030-GPOS-00011, SRG-OS-000028-GPOS-00009, SRG-OS-000031-GPOS-00012</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the NixOS operating system has the "vlock" package installed by running the following command: $ nix-store --query --requisites /run/current-system | cut -d- -f2- | sort | uniq | grep vlock vlock-2.2.2 If the "vlock" package is not installed, this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-268088`

### Rule: NixOS must monitor remote access methods.

**Rule ID:** `SV-268088r1039596_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyberattacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Configure the NixOS to monitors remote access methods with the following command: $ grep -R openssh.logLevel /etc/nixos /etc/nixos/configuration.nix:services.openssh.logLevel = "VERBOSE"; If services.openssh.logLevel does not equal VERBOSE, is missing, or is commented out, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-268089`

### Rule: NixOS must implement DOD-approved encryption to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-268089r1039597_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection (e.g., RDP), thereby providing a degree of confidentiality. The encryption strength of a mechanism is selected based on the security categorization of the information. Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000250-GPOS-00093, SRG-OS-000394-GPOS-00174</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS is configured to only use ciphers employing FIPS 140-3 approved algorithms with the following command: $ grep -R -A 4 openssh.setting.Ciphers /etc/nixos/configuration.nix:services.openssh.setting.Ciphers = [ /etc/nixos/configuration.nix- "aes256-ctr" /etc/nixos/configuration.nix- "aes192-ctr" /etc/nixos/configuration.nix- "aes128-ctr" /etc/nixos/configuration.nix- ]; If the cipher entries in the "configuration.nix" file have any ciphers other than "aes256-ctr,aes192-ctr,aes128-ctr", the order differs from the example above, they are missing, or commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-268090`

### Rule: The NixOS audit package must be installed.

**Rule ID:** `SV-268090r1039158_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in the operating system audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured operating system. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00021, SRG-OS-000054-GPOS-00025, SRG-OS-000055-GPOS-00026, SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000255-GPOS-00096, SRG-OS-000303-GPOS-00120, SRG-OS-000327-GPOS-00127</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that NixOS has the audit service is installed with the following command: $ nix-store --query --requisites /run/current-system | cut -d- -f2- | sort | uniq | grep audit audit-3.1.2 audit-3.1.2-bin audit-3.1.2-man audit-start audit-stop unit-auditd.service unit-audit.service If the "audit" package is not installed, this is a finding.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-268091`

### Rule: NixOS must generate audit records for all usage of privileged commands.

**Rule ID:** `SV-268091r1039161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. At a minimum, the organization must audit the full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat. Satisfies: SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000064-GPOS-00033, SRG-OS-000365-GPOS-00152, SRG-OS-000392-GPOS-00172, SRG-OS-000471-GPOS-00215, SRG-OS-000755-GPOS-00220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS generates audit records for all execution of privileged functions with the following command: $ sudo auditctl -l | grep execve -a always,exit -F arch=b64 -S execve -C uid!=euid -F euid=0 -k execpriv -a always,exit -F arch=b32 -S execve -C uid!=euid -F euid=0 -k execpriv -a always,exit -F arch=b32 -S execve -C gid!=egid -F egid=0 -k execpriv -a always,exit -F arch=b64 -S execve -C gid!=egid -F egid=0 -k execpriv If the command does not return the example output, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier. The string following "-k" does not need to match the example output above.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-268092`

### Rule: NixOS must enable auditing of processes that start prior to the audit daemon.

**Rule ID:** `SV-268092r1039560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. If auditing is enabled late in the startup process, the actions of some startup processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created. Audit records can be generated from various components within the information system (e.g., module or policy filter). The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DOD has defined the list of events for which NixOS will provide an audit record generation capability as the following: 1) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); 2) Access actions, such as successful and unsuccessful login attempts, privileged activities or other system-level access, starting and ending time for user access to the system, concurrent logins from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; 3) All account creations, modifications, disabling, and terminations; and 4) All kernel module load, unload, and restart actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS enables auditing of processes that start prior to the audit daemon with the following command: $ grep audit=1 /proc/cmdline BOOT_IMAGE=(hd0,msdos1)/nix/store/glc0midc78caq9sc7pzciymx4c3in7kn-linux-6.1.64/bzImage init=/nix/store/grl4baymr9q60mbcz3sidm4agckn3bx5-nixos-system-nixos-23.1.1.20231129.057f9ae/init audit=1 loglevel=4 If the "audit" entry does not equal "1" or is missing, this is a finding.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-268093`

### Rule: NixOS must allocate an audit_backlog_limit of sufficient size to capture processes that start prior to the audit daemon.

**Rule ID:** `SV-268093r1039167_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. If auditing is enabled late in the startup process, the actions of some startup processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created. Audit records can be generated from various components within the information system (e.g., module or policy filter). Allocating an audit_backlog_limit of sufficient size is critical in maintaining a stable boot process. With an insufficient limit allocated, the system is susceptible to boot failures and crashes. Satisfies: SRG-OS-000042-GPOS-00020, SRG-OS-000341-GPOS-00132</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS allocates a sufficient audit_backlog_limit to capture processes that start prior to the audit daemon with the following command: $ grep backlog_limit /proc/cmdline BOOT_IMAGE=(hd0,msdos1)/nix/store/glc0midc78caq9sc7pzciymx4c3in7kn-linux-6.1.64/bzImage init=/nix/store/grl4baymr9q60mbcz3sidm4agckn3bx5-nixos-system-nixos-23.1.1.20231129.057f9ae/init audit=1 audit_backlog_limit=8192 loglevel=4 If the "audit_backlog_limit" entry does not equal "8192" or greater or is missing, this is a finding.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-268094`

### Rule: Successful/unsuccessful uses of the mount syscall in NixOS must generate an audit record.

**Rule ID:** `SV-268094r1039561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "mount" syscall is used to mount a filesystem. When a user logs in, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS generates an audit record for any successful/unsuccessful use of the "mount" syscall with the following command: $ sudo auditctl -l | grep -w "\-S mount" -a always,exit -F arch=b32 -S mount -F auid>=1000 -F auid!=-1 -k privileged-mount -a always,exit -F arch=b64 -S mount -F auid>=1000 -F auid!=-1 -k privileged-mount If the command does not return the example output, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier. The string following "-k" does not need to match the example output above.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-268095`

### Rule: Successful/unsuccessful uses of the rename, unlink, rmdir, renameat, and unlinkat system calls in NixOS must generate an audit record.

**Rule ID:** `SV-268095r1039562_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "rename" system call will rename the specified files by replacing the first occurrence of expression in their name by replacement. The "unlink" system call deletes a name from the filesystem. If that name was the last link to a file and no processes have the file open, the file is deleted and the space it was using is made available for reuse. The "rmdir" system call removes empty directories. The "renameat" system call renames a file, moving it between directories if required. The "unlinkat" system call operates in exactly the same way as either "unlink" or "rmdir" except for the differences described in the manual page. When a user logs in, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. Performance can be helped, however, by combining syscalls into one rule whenever possible.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS generates an audit record upon successful/unsuccessful attempts to use the "rename", "unlink", "rmdir", "renameat", and "unlinkat" system calls with the following command: $ sudo auditctl -l | grep -w 'rename\|unlink\|rmdir' -a always,exit -F arch=b32 -S rename,unlink,rmdir,renameat,unlinkat -F auid>=1000 -F auid!=-1 -k delete -a always,exit -F arch=b64 -S rename,unlink,rmdir,renameat,unlinkat -F auid>=1000 -F auid!=-1 -k delete If the command does not return an audit rule for "rename", "unlink", "rmdir", "renameat", and "unlinkat", this is a finding. Note: The "-k" allows for specifying an arbitrary identifier. The string following "-k" does not need to match the example output above.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-268096`

### Rule: Successful/unsuccessful uses of the init_module, finit_module, and delete_module system calls in NixOS must generate an audit record.

**Rule ID:** `SV-268096r1039563_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "init_module" and "finit_module" system calls are used to load a kernel module, and the "delete_module" is used to unload a kernel module. When a user logs in, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000042-GPOS-00020, SRG-OS-000471-GPOS-00216</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS generates an audit record upon successful/unsuccessful attempts to use the "init_module", "finit_module", and "delete_module" system calls. Check the auditing rules currently loaded into the audit daemon with the following command: $ sudo auditctl -l | grep -w init_module -a always,exit -F arch=b32 -S init_module,finit_module,delete_module -F auid>=1000 -F auid!=-1 -k module_chng -a always,exit -F arch=b64 -S init_module,finit_module,delete_module -F auid>=1000 -F auid!=-1 -k module_chng If the command does not return an audit rule for "init_module", "finit_module", and "delete_module", this is a finding. Note: The "-k" allows for specifying an arbitrary identifier. The string following "-k" does not need to match the example output above.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-268097`

### Rule: NixOS must generate an audit record for successful/unsuccessful modifications to the cron configuration.

**Rule ID:** `SV-268097r1039179_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Cron is a program that is similar to the task scheduler used in other operating systems. When a user logs on, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS generates an audit record when successful/unsuccessful attempts to modify the cron configuration. Check the auditing rules currently loaded into the audit daemon with the following command: $ sudo auditctl -l | grep -w cron -w /var/cron/tabs/ -p wa -k services -w /var/cron/cron.allow -p wa -k services -w /var/cron/cron.deny -p wa -k services If the command does not return the example output, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier. The string following "-k" does not need to match the example output above.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-268098`

### Rule: NixOS must generate an audit record for successful/unsuccessful uses of the truncate, ftruncate, creat, open, openat, and open_by_handle_at system calls.

**Rule ID:** `SV-268098r1039593_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "truncate" and "ftruncate" functions are used to truncate a file to a specified length. The "creat" system call is used to open and possibly create a file or device. The "open" system call opens a file specified by a pathname. If the specified file does not exist, it may optionally be created by "open". The "openat" system call opens a file specified by a relative pathname. The "name_to_handle_at" and "open_by_handle_at" system calls split the functionality of "openat" into two parts: "name_to_handle_at" returns an opaque handle that corresponds to a specified file; "open_by_handle_at" opens the file corresponding to a handle returned by a previous call to "name_to_handle_at" and returns an open file descriptor. When a user logs in, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000042-GPOS-00020, SRG-OS-000461-GPOS-00205</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS generates an audit record upon unsuccessful attempts to use the "truncate", "ftruncate", "creat", "open", "openat", and "open_by_handle_at" system calls. Check the auditing rules currently loaded into the audit daemon with the following command: $ sudo auditctl -l | grep 'open\|truncate\|creat' -a always,exit -F arch=b32 -S open,creat,truncate,ftruncate,openat,open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=-1 -F key=access -a always,exit -F arch=b32 -S open,creat,truncate,ftruncate,openat,open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=-1 -F key=access -a always,exit -F arch=b64 -S open,creat,truncate,ftruncate,openat,open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=-1 -F key=access -a always,exit -F arch=b64 -S open,creat,truncate,ftruncate,openat,open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=-1 -F key=access If the command does not return an audit rule for "truncate", "ftruncate", "creat", "open", "openat", and "open_by_handle_at", this is a finding. Note: The "-k" allows for specifying an arbitrary identifier. The string following "-k" does not need to match the example output above.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-268099`

### Rule: Successful/unsuccessful uses of the chown, fchown, fchownat, and lchown system calls in NixOS must generate an audit record.

**Rule ID:** `SV-268099r1039185_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS generates an audit record upon attempts to use the "chown", "fchown", "fchownat", and "lchown" system calls. Check the auditing rules currently loaded into the audit daemon with the following command: $ sudo auditctl -l | grep chown -a always,exit -F arch=b32 -S lchown,fchown,chown,fchownat -F auid>=1000 -F auid!=-1 -F key=perm_mod -a always,exit -F arch=b64 -S chown,fchown,lchown,fchownat -F auid>=1000 -F auid!=-1 -F key=perm_mod If the command does not return an audit rule for "chown", "fchown", "fchownat", and "lchown", this is a finding. Note: The "-k" allows for specifying an arbitrary identifier. The string following "-k" does not need to match the example output above.

## Group: SRG-OS-000042-GPOS-00020

**Group ID:** `V-268100`

### Rule: Successful/unsuccessful uses of the chmod, fchmod, and fchmodat system calls in NixOS must generate an audit record.

**Rule ID:** `SV-268100r1039565_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The "chmod" system call changes the file mode bits of each given file according to mode, which can be either a symbolic representation of changes to make, or an octal number representing the bit pattern for the new mode bits. The "fchmod" system call is used to change permissions of a file. The "fchmodat" system call is used to change permissions of a file relative to a directory file descriptor. When a user logs in, the AUID is set to the UID of the account that is being authenticated. Daemons are not user sessions and have the loginuid set to "-1". The AUID representation is an unsigned 32-bit integer, which equals "4294967295". The audit system interprets "-1", "4294967295", and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. Performance can be helped, however, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000042-GPOS-00020, SRG-OS-000462-GPOS-00206</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS generates an audit record upon attempts to use the "chmod", "fchmod", and "fchmodat" system calls. Check the auditing rules currently loaded into the audit daemon with the following command: $ sudo auditctl -l | grep chmod -a always,exit -F arch=b32 -S chmod,fchmod,fchmodat -F auid>=1000 -F auid!=-1 -k perm_mod -a always,exit -F arch=b64 -S chmod,fchmod,fchmodat -F auid>=1000 -F auid!=-1 -k perm_mod If the command does not return an audit rule for "chmod", "fchmod", and "fchmodat, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier. The string following "-k" does not need to match the example output above.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-268101`

### Rule: NixOS must notify the system administrator (SA) and information system security officer (ISSO) (at a minimum) when allocated audit record storage volume reaches 75 percent utilization.

**Rule ID:** `SV-268101r1039599_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches 75 percent utilization, they are unable to plan for audit record storage capacity expansion. Satisfies: SRG-OS-000046-GPOS-00022, SRG-OS-000343-GPOS-00134</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS notifies the SA and ISSO (at a minimum) when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity with the following command: $ sudo grep -w space_left_action /etc/audit/auditd.conf space_left_action = syslog If the "space_left_action" parameter is missing, commented out, or set to blanks, this is a finding. If the "space_left_action" is set to "syslog", the system logs the event, but does not generate a notification, this is a finding. If the "space_left_action" is set to "exec", the system executes a designated script. If this script does not inform the SA of the event, this is a finding. If the "space_left_action" is set to "email" check the value of the "action_mail_acct" parameter with the following command: $ sudo grep action_mail_acct /etc/audit/auditd.conf action_mail_acct root@localhost The "action_mail_acct" parameter, if missing, defaults to "root". If the "action_mail_acct" parameter is not set to the email address of the SA and/or ISSO, this is a finding. Note: If the email address of the SA is on a remote system, a mail package must be available.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-268102`

### Rule: NixOS must notify the system administrator (SA) and information system security officer (ISSO) (at a minimum) when allocated audit record storage volume reaches 90 percent utilization.

**Rule ID:** `SV-268102r1039601_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches 90 percent utilization, they are unable to plan for audit record storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS notifies the SA and ISSO (at a minimum) when allocated audit record storage volume reaches 90 percent of the repository maximum audit record storage capacity with the following command: $ sudo grep -w admin_space_left_action /etc/audit/auditd.conf admin_space_left_action = syslog If the "admin_space_left_action" parameter is missing, commented out, or set to blanks, this is a finding. If the "admin_space_left_action" is set to "syslog", the system logs the event, but does not generate a notification, this is a finding. If the "admin_space_left_action" is set to "exec", the system executes a designated script. If this script does not inform the SA of the event, this is a finding. If the "admin_space_left_action" is set to "email" check the value of the "action_mail_acct" parameter with the following command: $ sudo grep action_mail_acct /etc/audit/auditd.conf action_mail_acct root@localhost The "action_mail_acct" parameter, if missing, defaults to "root". If the "action_mail_acct" parameter is not set to the email address of the SA and/or ISSO, this is a finding. Note: If the email address of the SA is on a remote system, a mail package must be available.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-268103`

### Rule: NixOS must take action when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity.

**Rule ID:** `SV-268103r1039197_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches 75 percent utilization, they are unable to plan for audit record storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS takes action when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity with the following commands: $ sudo grep -w space_left /etc/audit/auditd.conf space_left = 25% If the value of the "space_left" keyword is not set to "25%" or if the line is commented out, this is a finding.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-268104`

### Rule: NixOS must take action when allocated audit record storage volume reaches 90 percent of the repository maximum audit record storage capacity.

**Rule ID:** `SV-268104r1039200_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches 90 percent utilization, they are unable to plan for audit record storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS takes action when allocated audit record storage volume reaches 90 percent of the repository maximum audit record storage capacity with the following commands: $ sudo grep -w admin_space_left /etc/audit/auditd.conf admin_space_left = 10% If the value of the "admin_space_left" keyword is not set to "10%" or if the line is commented out, this is a finding.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-268105`

### Rule: The NixOS audit system must take appropriate action when the audit storage volume is full.

**Rule ID:** `SV-268105r1039203_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when NixOS is at risk of failing to process audit logs as required, it takes action to mitigate the failure. Audit processing failures include software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When availability is an overriding concern, other approved actions in response to an audit failure are as follows: 1) If the failure was caused by the lack of audit record storage capacity, NixOS must continue generating audit records if possible (automatically restarting the audit service if necessary) and overwriting the oldest audit records in a first-in-first-out manner. 2) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, NixOS must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS takes the appropriate action when the audit storage volume is full. Check that NixOS takes the appropriate action when the audit storage volume is full using the following command: $ sudo grep disk_full_action /etc/audit/auditd.conf disk_full_action = HALT If the value of the "disk_full_action" option is not "SYSLOG", "SINGLE", or "HALT", or the line is commented out, ask the system administrator (SA) to indicate how the system takes appropriate action when an audit storage volume is full. If there is no evidence of appropriate action, this is a finding.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-268106`

### Rule: The NixOS audit system must take appropriate action when an audit processing failure occurs.

**Rule ID:** `SV-268106r1039206_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when NixOS is at risk of failing to process audit logs as required, it takes action to mitigate the failure. Audit processing failures include software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When availability is an overriding concern, other approved actions in response to an audit failure are as follows: 1) If the failure was caused by the lack of audit record storage capacity, NixOS must continue generating audit records if possible (automatically restarting the audit service if necessary) and overwriting the oldest audit records in a first-in-first-out manner. 2) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, NixOS must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS takes the appropriate action when an audit processing failure occurs. Check that NixOS takes the appropriate action when an audit processing failure occurs with the following command: $ sudo grep disk_error_action /etc/audit/auditd.conf disk_error_action = HALT If the value of the "disk_error_action" option is not "SYSLOG", "SINGLE", or "HALT", or the line is commented out, ask the system administrator (SA) to indicate how the system takes appropriate action when an audit process failure occurs. If there is no evidence of appropriate action, this is a finding.

## Group: SRG-OS-000051-GPOS-00024

**Group ID:** `V-268107`

### Rule: NixOS must have the packages required for offloading audit logs installed and running.

**Rule ID:** `SV-268107r1039594_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. NixOS supports "syslog-ng". "syslog-ng" is a common system utility providing support for message logging. Support for both internet and Unix domain sockets enables this utility to support both local and remote logging. This utility also natively supports TLS to securely encrypt and off-load auditing. Satisfies: SRG-OS-000051-GPOS-00024, SRG-OS-000269-GPOS-00103</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the syslog-ng service is running with the following command: $ systemctl status syslog-ng.service syslog-ng.service - syslog-ng daemon Loaded: loaded (/etc/systemd/system/syslog-ng.service; enabled; vendor preset: enabled) Active: active (running) since Sat 2022-06-04 02:51:43 UTC; 13min ago If the syslog-ng service is not "active" and "running", this is a finding.

## Group: SRG-OS-000051-GPOS-00024

**Group ID:** `V-268108`

### Rule: The NixOS audit records must be off-loaded onto a different system or storage media from the system being audited.

**Rule ID:** `SV-268108r1039573_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. NixOS supports "syslog-ng". "syslog-ng" is a common system utility providing support for message logging. Support for both internet and Unix domain sockets enables this utility to support both local and remote logging. This utility also natively supports TLS to securely encrypt and off-load auditing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit system off-loads audit records onto a different system or media from the system being audited. List the configured destinations with the following command: $ cat $(egrep -o 'cfgfile=.*\.conf' $(nix-store --query --requisites /run/current-system | grep syslog-ng.service)/syslog-ng.service | awk -F '=' '{print $2}') @version: 4.4 @include "scl.conf" options { keep-hostname(yes); create_dirs(yes); owner(root); group(root); perm(0644); dir_owner(root); dir_group(root); dir_perm(0755); }; source s_local { system(); internal(); }; destination d_local { file("/var/log/messages"); }; destination d_network { syslog( "<remote-logging-server>" port(<port>) transport(tls) tls( cert-file("/var/syslog-ng/certs.d/certificate.crt") key-file("/var/syslog-ng/certs.d/certificate.key") ca-file("/var/syslog-ng/certs.d/cert-bundle.crt") peer-verify(yes) ) ); }; log { source(s_local); destination(d_local); destination(d_network); }; If the configuration does not specify a "log" directive for sources to be sent to a remote destination, or the lines are commented out, ask the system administrator (SA) to indicate how the audit logs are off-loaded to a different system or media. If there is no evidence that the audit logs are being off-loaded to another system or media, this is a finding.

## Group: SRG-OS-000051-GPOS-00024

**Group ID:** `V-268109`

### Rule: NixOS must authenticate the remote logging server for off-loading audit logs.

**Rule ID:** `SV-268109r1039595_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. NixOS supports "syslog-ng". "syslog-ng" is a common system utility providing support for message logging. Support for both internet and Unix domain sockets enables this utility to support both local and remote logging. This utility also natively supports TLS to securely encrypt and off-load auditing. Satisfies: SRG-OS-000051-GPOS-00024, SRG-OS-000342-GPOS-00133, SRG-OS-000479-GPOS-00224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system authenticates the remote logging server for off-loading audit logs. List the configured destinations with the following command: $ cat $(egrep -o 'cfgfile=.*\.conf' $(nix-store --query --requisites /run/current-system | grep syslog-ng.service)/syslog-ng.service | awk -F '=' '{print $2}') @version: 4.4 @include "scl.conf" options { keep-hostname(yes); create_dirs(yes); owner(root); group(root); perm(0644); dir_owner(root); dir_group(root); dir_perm(0755); }; source s_local { system(); internal(); }; destination d_local { file("/var/log/messages"); }; destination d_network { syslog( "<remote-logging-server>" port(<port>) transport(tls) tls( cert-file("/var/syslog-ng/certs.d/certificate.crt") key-file("/var/syslog-ng/certs.d/certificate.key") ca-file("/var/syslog-ng/certs.d/cert-bundle.crt") peer-verify(yes) ) ); }; log { source(s_local); destination(d_local); destination(d_network); }; If the remote destination does not specify "transport(tls)", the remote destination tls configuration does not specify "peer-verify(yes)" or "peer-verify(required-trusted)", or the lines are commented out, ask the system administrator (SA) to indicate how the audit logs are off-loaded to a different system or media. If there is no evidence that the transfer of the audit logs being off-loaded to another system or media is encrypted, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-268110`

### Rule: NixOS audit daemon must generate logs that are group-owned by root.

**Rule ID:** `SV-268110r1039218_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the NixOS system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000206-GPOS-00084</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit daemon is configured to generate logs that are group-owned by root with the following command: $ sudo grep log_group /etc/audit/auditd.conf log_group = root If the audit daemon is not configured to generate logs that are group-owned by "root", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-268111`

### Rule: NixOS audit directory and logs must be owned by root to prevent unauthorized read access.

**Rule ID:** `SV-268111r1039221_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the NixOS system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000206-GPOS-00084</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit directory and logs are owned by "root". First, determine where the audit logs are stored with the following command: $ sudo grep log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the location of the audit log file (if not specified, the default location is "/var/log/audit/audit.log"), determine if the audit log is owned by "root" using the following command: $ sudo find /var/log/audit -exec stat -c "%U %n" {} \; root /var/log/audit root /var/log/audit/audit.log If the audit directory and logs are not owned by "root", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-268112`

### Rule: NixOS audit directory and logs must be group-owned by root to prevent unauthorized read access.

**Rule ID:** `SV-268112r1039224_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the NixOS system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000206-GPOS-00084</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit directory and logs are group-owned by "root". First, determine where the audit logs are stored with the following command: $ sudo grep log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the location of the audit log file (if not specified, the default location is "/var/log/audit/audit.log"), determine if the audit log is group-owned by "root" using the following command: $ sudo find /var/log/audit -exec stat -c "%G %n" {} \; root /var/log/audit root /var/log/audit/audit.log If the audit directory and logs are not group-owned by "root", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-268113`

### Rule: NixOS audit log directory must have a mode of 0700 or less permissive.

**Rule ID:** `SV-268113r1039227_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit NixOS system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the audit log directory has a mode of "0700" or less permissive. First, determine where the audit logs are stored with the following command: $ sudo grep log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the path of the directory containing the audit logs, check if the audit log directory has a mode of "0700" or less by using the following command: $ sudo find /var/log/audit -type d -exec stat -c "%a %n" {} \; 700 /var/log/audit If the audit log directory (or any subfolders) has a mode more permissive than "0700", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-268114`

### Rule: NixOS audit logs must have a mode of 0600 or less permissive.

**Rule ID:** `SV-268114r1039230_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the NixOS system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000206-GPOS-00084</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the audit log files have a mode of "0600" or less permissive. First, determine where the audit logs are stored with the following command: $ sudo grep log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the path of the directory containing the audit logs, check if the audit log files have a mode of "0600" or less by using the following command: $ sudo find /var/log/audit -type f -exec stat -c "%a %n" {} \; 600 /var/log/audit/audit.log If the audit log files have a mode more permissive than "0600", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-268115`

### Rule: NixOS syslog directory and logs must be owned by root to prevent unauthorized read access.

**Rule ID:** `SV-268115r1039233_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the NixOS system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000206-GPOS-00084</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the syslog directories and logs are owned by "root" by executing the following command: $ cat $(egrep -o 'cfgfile=.*\.conf' $(nix-store --query --requisites /run/current-system | grep syslog-ng.service)/syslog-ng.service | awk -F '=' '{print $2}') | grep owner owner(root); dir_owner(root); If any occurrences of "owner" and "dir_owner" are not configured as "root", they are not specified, or they are commented out, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-268116`

### Rule: NixOS syslog directory and logs must be group-owned by root to prevent unauthorized read access.

**Rule ID:** `SV-268116r1039236_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the NixOS system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000206-GPOS-00084</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the syslog directories and logs are group-owned by "root" by executing the following command: $ cat $(egrep -o 'cfgfile=.*\.conf' $(nix-store --query --requisites /run/current-system | grep syslog-ng.service)/syslog-ng.service | awk -F '=' '{print $2}') | grep group group(root); dir_group(root); If any occurrences of "group" and "dir_group" are not configured as "root", they are not specified, or they are commented out, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-268117`

### Rule: NixOS syslog log directory must have a mode of 0750 or less permissive.

**Rule ID:** `SV-268117r1039239_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit NixOS system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS protects audit information from unauthorized read access by implementing a mode of 0750 or less on the creation of log directories with the following command: $ cat $(egrep -o 'cfgfile=.*\.conf' $(nix-store --query --requisites /run/current-system | grep syslog-ng.service)/syslog-ng.service | awk -F '=' '{print $2}') | grep dir_perm dir_perm(0750); If the syslog log directory is not a mode of 0750 or less permissive, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-268118`

### Rule: NixOS syslog logs must have a mode of 0640 or less permissive.

**Rule ID:** `SV-268118r1039602_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the NixOS system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000205-GPOS-00083</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that syslog log files have a mode of "0640" or less permissive by executing the following command: $ cat $(egrep -o 'cfgfile=.*\.conf' $(nix-store --query --requisites /run/current-system | grep syslog-ng.service)/syslog-ng.service | awk -F '=' '{print $2}') | grep -w perm perm(0640); If any occurrences of "perm" are not configured as "0640" or less permissive, they are not specified, or they are commented out, this is a finding.

## Group: SRG-OS-000058-GPOS-00028

**Group ID:** `V-268119`

### Rule: NixOS audit system must protect login UIDs from unauthorized change.

**Rule ID:** `SV-268119r1039577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit information were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit system activity. In immutable mode, unauthorized users cannot execute changes to the audit system to potentially hide malicious activity and then put the audit rules back. A system reboot would be noticeable and a system administrator could then investigate the unauthorized changes. Satisfies: SRG-OS-000058-GPOS-00028, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit system prevents unauthorized changes to login UIDs with the following command: $ sudo auditctl -s | grep -i immutable loginuid_immutable 1 locked If the command does not return "loginuid_immutable 1 locked", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-268120`

### Rule: NixOS system configuration files must have a mode of "0644" or less permissive.

**Rule ID:** `SV-268120r1039248_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict the roles and individuals that can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the NixOS system configuration files have a mode of "0644" or less permissive with the following command: $ sudo find /etc/nixos -type f -exec stat -c "%a %n" {} \; 644 /etc/nixos/configuration.nix 644 /etc/nixos/hardware-configuration.nix If the system configuration files have a mode more permissive than "0644", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-268121`

### Rule: NixOS system configuration file directories must have a mode of "0755" or less permissive.

**Rule ID:** `SV-268121r1039251_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict the roles and individuals that can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the NixOS system configuration file directories have a mode of "0755" or less permissive with the following command: $ sudo find /etc/nixos -type d -exec stat -c "%a %n" {} \; 755 /etc/nixos If the system configuration file directories have a mode more permissive than "0755", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-268122`

### Rule: NixOS system configuration files and directories must be owned by root.

**Rule ID:** `SV-268122r1039254_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict the roles and individuals that can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the NixOS system configuration files and directories are owned by root with the following command: $ sudo find /etc/nixos -exec stat -c "%U %n" {} \; root /etc/nixos root /etc/nixos/configuration.nix root /etc/nixos/hardware-configuration.nix If the system configuration files and directories are not owned by root, this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-268123`

### Rule: NixOS system configuration files and directories must be group-owned by root.

**Rule ID:** `SV-268123r1039257_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict the roles and individuals that can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the NixOS system configuration files and directories are group-owned by root with the following command: $ sudo find /etc/nixos -exec stat -c "%G %n" {} \; root /etc/nixos root /etc/nixos/configuration.nix root /etc/nixos/hardware-configuration.nix If the system configuration files and directories are not group-owned by root, this is a finding.

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-268124`

### Rule: NixOS, for PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

**Rule ID:** `SV-268124r1039260_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement. Satisfies: SRG-OS-000066-GPOS-00034, SRG-OS-000403-GPOS-00182, SRG-OS-000775-GPOS-00230</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS only allows the use of DOD PKI-established certificate authorities by running the following: $ nix-env -iA nixos.openssl $ openssl x509 -text -in /etc/sssd/pki/sssd_auth_ca_db.pem Certificate: Data: Version: 3 (0x2) Serial Number: 1 (0x1) Signature Algorithm: sha256WithRSAEncryption Issuer: C = US, O = U.S. Government, OU = DOD, OU = PKI, CN = DOD Root CA 3 Validity Not Before: Mar 20 18:46:41 2012 GMT Not After : Dec 30 18:46:41 2029 GMT Subject: C = US, O = U.S. Government, OU = DOD, OU = PKI, CN = DOD Root CA 3 Subject Public Key Info: Public Key Algorithm: rsaEncryption If the root CA file is not a DOD-issued certificate with a valid date and installed in the /etc/sssd/pki/sssd_auth_ca_db.pem location, this is a finding.

## Group: SRG-OS-000067-GPOS-00035

**Group ID:** `V-268125`

### Rule: NixOS must enforce authorized access to the corresponding private key for PKI-based authentication.

**Rule ID:** `SV-268125r1039263_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the private key is discovered, an attacker can use the key to authenticate as an authorized user and gain access to the network infrastructure. The cornerstone of the PKI is the private key used to encrypt or digitally sign information. If the private key is stolen, this will lead to the compromise of the authentication and nonrepudiation gained through PKI because the attacker can use the private key to digitally sign documents and pretend to be the authorized user. Both the holders of a digital certificate and the issuing authority must protect the computers, storage devices, or whatever they use to keep the private keys.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH private key files have a passcode. For each private key stored on the system, use the following command: $ sudo ssh-keygen -y -f /path/to/file If the contents of the key are displayed, this is a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-268126`

### Rule: NixOS must enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-268126r1039266_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS enforces password complexity by requiring at least one uppercase character with the following command: $ grep ucredit /etc/security/pwquality.conf ucredit=-1 If the value of "ucredit" is a positive number or is commented out, this is a finding.

## Group: SRG-OS-000070-GPOS-00038

**Group ID:** `V-268127`

### Rule: NixOS must enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-268127r1039269_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS enforces password complexity by requiring at least one lowercase character with the following command: $ grep lcredit /etc/security/pwquality.conf lcredit=-1 If the value of "lcredit" is a positive number or is commented out, this is a finding.

## Group: SRG-OS-000071-GPOS-00039

**Group ID:** `V-268128`

### Rule: NixOS must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-268128r1039272_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS enforces password complexity by requiring at least one numeric character with the following command: $ grep dcredit /etc/security/pwquality.conf dcredit=-1 If the value of "dcredit" is a positive number or is commented out, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-268129`

### Rule: NixOS must require the change of at least 50 percent of the total number of characters when passwords are changed.

**Rule ID:** `SV-268129r1039275_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS enforces password complexity by requiring that at least 50 percent of the characters are changed with the following command: $ grep difok /etc/security/pwquality.conf difok=8 If the value of "difok" is set to less than "8", or is commented out, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-268130`

### Rule: NixOS must store only encrypted representations of passwords.

**Rule ID:** `SV-268130r1039278_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS stores only encrypted representations of passwords with the following command: $ grep ENCRYPT_METHOD /etc/login.defs ENCRYPT_METHOD SHA512 If "ENCRYPT_METHOD" does not equal SHA512 or greater, is commented out, or is missing, this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-268131`

### Rule: NixOS must not have the telnet package installed.

**Rule ID:** `SV-268131r1039281_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the telnet package is not installed and available with the following command: $ whereis telnet telnet: If there is a path, and the output looks like "telnet: /nix/store/sqiphymcpky1yysgdc1aj4lr9jg9n53a-inetutils-2.2/bin/telnet", this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-268132`

### Rule: NixOS must enforce 24 hours/one day as the minimum password lifetime.

**Rule ID:** `SV-268132r1039284_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS enforces 24 hours/one day as the minimum password lifetime with the following command: $ grep PASS_MIN_DAYS /etc/login.defs PASS_MIN_DAYS 1 If PASS_MIN_DAYS_1 is not present, is commented out, or is a value different from 1, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-268133`

### Rule: NixOS must enforce a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-268133r1039287_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If the operating system does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the operating system passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS enforces a 60-day maximum password lifetime for new user accounts by running the following command: $ grep PASS_MAX_DAYS /etc/login.defs PASS_MAX_DAYS 60 If the "PASS_MAX_DAYS" parameter value is less than 60 or commented out, this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-268134`

### Rule: NixOS must enforce a minimum 15-character password length.

**Rule ID:** `SV-268134r1039290_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS enforces a minimum 15-character password length with the following command: $ grep minlen /etc/security/pwquality.conf minlen=15 If the value of "minlen" is set to less than "15", or is commented out, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-268135`

### Rule: NixOS must uniquely identify and must authenticate organizational users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-268135r1039293_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. Satisfies: SRG-OS-000104-GPOS-00051, SRG-OS-000121-GPOS-00062</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the NixOS operating system contains no duplicate User IDs (UIDs) for interactive users with the following command: $ awk -F ":" 'list[$3]++{print $1, $3}' /etc/passwd If output is produced and the accounts listed are interactive user accounts, this is a finding.

## Group: SRG-OS-000105-GPOS-00052

**Group ID:** `V-268136`

### Rule: NixOS must use multifactor authentication for network access to privileged accounts.

**Rule ID:** `SV-268136r1039296_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: 1) something a user knows (e.g., password/PIN); 2) something a user has (e.g., cryptographic identification device, token); and 3) something a user is (e.g., biometric). A privileged account is defined as an information system account with authorizations of a privileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the internet). The DOD CAC with DOD-approved PKI is an example of multifactor authentication. Satisfies: SRG-OS-000105-GPOS-00052, SRG-OS-000106-GPOS-00053, SRG-OS-000107-GPOS-00054, SRG-OS-000108-GPOS-00055</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS has the packages required for multifactor authentication installed with the following command: $ grep -R pkgs.opencrypto /etc/nixos pkgs.opencryptoki If the "pkgs.opencryptoki" package is not installed, this is a finding.

## Group: SRG-OS-000109-GPOS-00056

**Group ID:** `V-268137`

### Rule: NixOS must not allow direct login to the root account via SSH.

**Rule ID:** `SV-268137r1039578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure individual accountability and prevent unauthorized access, organizational users must be individually identified and authenticated. A group authenticator is a generic account used by multiple individuals. Use of a group authenticator alone does not uniquely identify individual users. Examples of the group authenticator is the Unix OS "root" user account, the Windows "Administrator" account, the "sa" account, or a "helpdesk" account. For example, the Unix and Windows operating systems offer a "switch user" capability allowing users to authenticate with their individual credentials and, when needed, "switch" to the administrator role. This method provides for unique individual authentication prior to using a group authenticator. Users (and any processes acting on behalf of users) need to be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization, which outlines specific user actions that can be performed on the operating system without identification or authentication. Requiring individuals to be authenticated with an individual authenticator prior to using a group authenticator allows for traceability of actions, as well as adding an additional level of protection of the actions that can be taken with group account knowledge.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the NixOS configuration disallows directly logging into the root account via SSH with the following command: $ grep PermitRootLogin /etc/ssh/sshd_config PermitRootLogin no If the value is anything other than "no", this is a finding.

## Group: SRG-OS-000109-GPOS-00056

**Group ID:** `V-268138`

### Rule: NixOS must not allow direct login to the root account.

**Rule ID:** `SV-268138r1039579_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure individual accountability and prevent unauthorized access, organizational users must be individually identified and authenticated. A group authenticator is a generic account used by multiple individuals. Use of a group authenticator alone does not uniquely identify individual users. Examples of the group authenticator is the Unix OS "root" user account, the Windows "Administrator" account, the "sa" account, or a "helpdesk" account. For example, the Unix and Windows operating systems offer a "switch user" capability allowing users to authenticate with their individual credentials and, when needed, "switch" to the administrator role. This method provides for unique individual authentication prior to using a group authenticator. Users (and any processes acting on behalf of users) need to be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization, which outlines specific user actions that can be performed on the operating system without identification or authentication. Requiring individuals to be authenticated with an individual authenticator prior to using a group authenticator allows for traceability of actions, as well as adding an additional level of protection of the actions that can be taken with group account knowledge.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the NixOS operating system prevents directly logging in to the root account with the following command: $ sudo passwd -S root root L 01/02/1970 -1 -1 -1 -1 If the second field in the output is not "L", then the root account is not locked, and this is a finding.

## Group: SRG-OS-000114-GPOS-00059

**Group ID:** `V-268139`

### Rule: NixOS must enable USBguard.

**Rule ID:** `SV-268139r1039607_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without identifying devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Peripherals include, but are not limited to, such devices as flash drives, external storage, and printers. Satisfies: SRG-OS-000114-GPOS-00059, SRG-OS-000378-GPOS-00163, SRG-OS-000690-GPOS-00140</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS had enabled the use of the USBGuard with the following command: $ systemctl status usbguard usbguard.service - USBGuard daemon Loaded: loaded (/etc/systemd/system/usbguard.service; enabled; present: enabled) Active: active (running) since Sat 2022-06-04 02:51:43 UTC; 13min ago If the usbguard.service is not "active" and "running", this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-268140`

### Rule: A sticky bit must be set on all NixOS public directories to prevent unauthorized and unintended information transferred via shared system resources.

**Rule ID:** `SV-268140r1039308_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DOD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS is configured with the sticky bit on world-writable directories with the following command: $ sudo find / -type d \( -perm -0002 -a ! -perm -1000 \) -print 2>/dev/null If any of the returned directories are world-writable and do not have the sticky bit set, this is a finding.

## Group: SRG-OS-000142-GPOS-00071

**Group ID:** `V-268141`

### Rule: NixOS must manage excess capacity, bandwidth, or other redundancy to limit the effects of information flooding types of denial-of-service (DoS) attacks.

**Rule ID:** `SV-268141r1039311_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Managing excess capacity ensures that sufficient capacity is available to counter flooding attacks. Employing increased capacity and service redundancy may reduce the susceptibility to some DoS attacks. Managing excess capacity may include, for example, establishing selected usage priorities, quotas, or partitioning.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS is configured to use IPv4 TCP syncookies with the following command: $ sudo sysctl net.ipv4.tcp_syncookies net.ipv4.tcp_syncookies = 1 If the network parameter "ipv4.tcp_syncookies" is not equal to "1" or nothing is returned, this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-268142`

### Rule: NixOS must terminate all SSH connections after 10 minutes of becoming unresponsive.

**Rule ID:** `SV-268142r1039535_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, and de-allocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that the operating system terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session. Satisfies: SRG-OS-000163-GPOS-00072, SRG-OS-000279-GPOS-00109, SRG-OS-000395-GPOS-00175</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all network connections associated with SSH traffic are automatically terminated after 10 minutes of becoming unresponsive with the following command: $ grep -i clientaliveinterval /etc/ssh/sshd_config ClientAliveInterval 600 If "ClientAliveInterval" does not have a value of "600" or less, is commented out, or is missing, this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-268143`

### Rule: NixOS must terminate all SSH connections after becoming unresponsive.

**Rule ID:** `SV-268143r1039317_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, and de-allocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that the operating system terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all network connections associated with SSH traffic are automatically terminated after becoming unresponsive with the following command: $ grep -i clientalivecount /etc/ssh/sshd_config ClientAliveCountMax 1 If "ClientAliveCountMax" is not set to "1", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000185-GPOS-00079

**Group ID:** `V-268144`

### Rule: NixOS must protect the confidentiality and integrity of all information at rest.

**Rule ID:** `SV-268144r1039320_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Information at rest refers to the state of information when it is located on a secondary storage device (e.g., disk drive and tape drive, when used for backups) within an operating system. This requirement addresses protection of user-generated data, as well as operating system-specific configuration data. Organizations may choose to employ different mechanisms to achieve confidentiality and integrity protections, as appropriate, in accordance with the security category and/or classification of the information. Satisfies: SRG-OS-000185-GPOS-00079, SRG-OS-000404-GPOS-00183, SRG-OS-000405-GPOS-00184, SRG-OS-000780-GPOS-00240</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS prevents unauthorized disclosure or modification of all information requiring at-rest protection by using disk encryption. Verify all system partitions are encrypted with the following command: $ sudo blkid /dev/sda1: LABEL="nixos" UUID="67b7d7fe-de60-6fd0-befb-e6748cf97743" TYPE="crypto_LUKS" Every persistent disk partition present must be of type "crypto_LUKS". If any partitions other than the boot partition or pseudo file systems (such as /proc or /sys) are not type "crypto_LUKS", ask the administrator to indicate how the partitions are encrypted. If there is no evidence that these partitions are encrypted, this is a finding.

## Group: SRG-OS-000266-GPOS-00101

**Group ID:** `V-268145`

### Rule: NixOS must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-268145r1039323_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity or strength is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor in determining how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Special characters are those characters that are not alphanumeric. Examples include: ~ ! @ # $ % ^ *.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS enforces the use of at least one special character in passwords with the following command: $ grep minlen /etc/security/pwquality.conf ocredit=-1 If the value of "ocredit" is a positive number or is commented out, this is a finding.

## Group: SRG-OS-000299-GPOS-00117

**Group ID:** `V-268146`

### Rule: NixOS must protect wireless access to and from the system using encryption.

**Rule ID:** `SV-268146r1039326_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Allowing devices and users to connect to or from the system without first authenticating them allows untrusted access and can lead to a compromise or attack. Since wireless communications can be intercepted, it is necessary to use encryption to protect the confidentiality of information in transit. Wireless technologies include, for example, microwave, packet radio (UHF/VHF), 802.11x, and Bluetooth. Wireless networks use authentication protocols (e.g., EAP/TLS, PEAP), which provide credential protection and mutual authentication. This requirement applies to those operating systems that control wireless devices. Satisfies: SRG-OS-000299-GPOS-00117, SRG-OS-000481-GPOS-00481</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS disables wireless adapters by running the following command: $ grep -R networking.wireless /etc/nixos/ /etc/nixos/configuratino.nix:networking.wireless.enable = false; If " networking.wireless.enable", does not equal false, is missing, or is commented out, this is a finding.

## Group: SRG-OS-000300-GPOS-00118

**Group ID:** `V-268147`

### Rule: NixOS must protect wireless access to the system using authentication of users and/or devices.

**Rule ID:** `SV-268147r1039329_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing devices and users to connect to the system without first authenticating them allows untrusted access and can lead to a compromise or attack. Wireless technologies include, for example, microwave, packet radio (UHF/VHF), 802.11x, and Bluetooth. Wireless networks use authentication protocols (e.g., EAP/TLS, PEAP), which provide credential protection and mutual authentication. This requirement applies to operating systems that control wireless devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS disables Bluetooth adapters by running the following command: $ grep -R hardware.bluetooth /etc/nixos/ /etc/nixos/configuration.nix:hardware.bluetooth.enable = false; If "hardware.bluetooth.enable", does not equal false, is missing, or is commented out, this is a finding.

## Group: SRG-OS-000326-GPOS-00126

**Group ID:** `V-268148`

### Rule: NixOS must prevent all software from executing at higher privilege levels than users executing the software.

**Rule ID:** `SV-268148r1039332_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, software applications/programs need to execute with elevated privileges to perform required functions. However, if the privileges required for execution are at a higher level than the privileges assigned to organizational users invoking such applications/programs, those users are indirectly provided with greater privileges than assigned by the organizations. Some programs and processes are required to operate at a higher privilege level and therefore should be excluded from the organization-defined software list after review.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS audits and provides alerts of audit failures by running the following command: $grep A -15 security.auditd /etc/nixos/configuration.nix /etc/nixos/configuration.nix: security.auditd.enable = true; security.audit.enable = true; security.audit.rules = [ '' <audit_rules> '' ]; security.audit.rules = [ "-a always,exit -F arch=b32 -S execve -C uid!=euid -F euid=0 -k execpriv" "-a always,exit -F arch=b64 -S execve -C uid!=euid -F euid=0 -k execpriv" "-a always,exit -F arch=b32 -S execve -C gid!=egid -F egid=0 -k execpriv" "-a always,exit -F arch=b64 -S execve -C gid!=egid -F egid=0 -k execpriv" ]; If "security.auditd", "security.audit" and the additional modifications do not equal true, are missing, or are commented out, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-268149`

### Rule: NixOS must, for networked systems, compare internal information system clocks at least every 24 hours with a server which is synchronized to one of the redundant United States Naval Observatory (USNO) time servers, or a time server designated for the appropriate DOD network (NIPRNet/SIPRNet), and/or the Global Positioning System (GPS).

**Rule ID:** `SV-268149r1039335_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). Satisfies: SRG-OS-000355-GPOS-00143, SRG-OS-000359-GPOS-00146, SRG-OS-000785-GPOS-00250</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS is configured with an approved time server with the following command: $ timedatectl show-timesync | grep NTPServers SystemNTPServers=tick.usnogps.navy.mil FallbackNTPServers=tock.usnogps.navy.mil If the output of the command does not list authorized time servers, this is a finding.

## Group: SRG-OS-000356-GPOS-00144

**Group ID:** `V-268150`

### Rule: NixOS must synchronize internal information system clocks to the authoritative time source when the time difference is greater than one second.

**Rule ID:** `SV-268150r1039338_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider setting time periods for different types of systems (e.g., financial, legal, or mission-critical systems). Organizations should also consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). This requirement is related to the comparison done every 24 hours in SRG-OS-000355 because a comparison must be done to determine the time difference.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS synchronizes internal information system clocks to the authoritative time source when the time difference is greater than one second with the following command: $ grep -iR pollinterval /etc/nixos/ services.timesyncd.extraConfig = "PollIntervalMaxSec=60"; If "PollIntervalMaxSec" is greater than "60", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000356-GPOS-00144

**Group ID:** `V-268151`

### Rule: NixOS must have time synchronization enabled.

**Rule ID:** `SV-268151r1039341_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider setting time periods for different types of systems (e.g., financial, legal, or mission-critical systems). Organizations should also consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). This requirement is related to the comparison done every 24 hours in SRG-OS-000355 because a comparison must be done to determine the time difference.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS synchronizes internal information system clocks to the authoritative time source when the time difference is greater than one second with the following command: $ grep -iR timesyncd.enable /etc/nixos/ services.timesyncd.enable = true; If "services.timesyncd.enable" is not set to "true", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000362-GPOS-00149

**Group ID:** `V-268152`

### Rule: NixOS must prohibit user installation of system software without explicit privileged status.

**Rule ID:** `SV-268152r1039344_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing regular users to install software, without explicit privileges, creates the risk that untested or potentially malicious software will be installed on the system. Explicit privileges (escalated or administrative privileges) provide the regular user with explicit capabilities and control that exceeds the rights of a regular user. Operating system functionality will vary, and while users are not permitted to install unapproved software, there may be instances where the organization allows the user to install approved software packages, such as from an approved software repository. The operating system or software configuration management utility must enforce control of software installation by users based upon what types of software installations are permitted (e.g., updates and security patches to existing software) and what types of installations are prohibited (e.g., software whose pedigree with regard to being potentially malicious is unknown or suspect) by the organization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS prevents unauthorized users from using nix with the following command: $ grep -R allowed-users /etc/nixos/ /etc/nixos/configuration.nix:nix.settings.allowed-users = [ "root" "@wheel" ]; If any other groups or users are included in "nix.settings.allowed-users" other than "root" and "wheel", or the configuration setting does not exist, this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-268153`

### Rule: NixOS must notify designated personnel if baseline configurations are changed in an unauthorized manner.

**Rule ID:** `SV-268153r1039347_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to the operating system. Changes to operating system configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of the operating system. The operating system's IMO/ISSO and SAs must be notified via email and/or monitoring system trap when there is an unauthorized modification of a configuration item. Satisfies: SRG-OS-000363-GPOS-00150, SRG-OS-000445-GPOS-00199, SRG-OS-000446-GPOS-00200, SRG-OS-000447-GPOS-00201</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS notifies if baseline configurations are changed with Advanced Intrusion Detection Environment with the following commands: $ nix-store --query --requisites /run/current-system | cut -d- -f2- | sort | uniq | grep aide aide-0.18.6 etc-aide.conf $ cat /etc/nixos/configuration.nix | grep -A 5 aide.conf If aide is not installed and is not configured to alert on file system changes, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-268154`

### Rule: NixOS must prevent the installation of patches, service packs, device drivers, or operating system components without verification they have been digitally signed using a certificate that is recognized and approved by the organization.

**Rule ID:** `SV-268154r1039350_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. Accordingly, patches, service packs, device drivers, or operating system components must be signed with a certificate recognized and approved by the organization. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. The operating system should not have to verify the software again. This requirement does not mandate DOD certificates for this purpose; however, the certificate used to verify the software must be from an approved certificate authority (CA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS prevents installations that have not been digitally signed with the following command: $ grep -R require-sigs /etc/nixos/ /etc/nixos/configuration.nix:nix.settings.require-sigs = true; If "nix.settings.require-sigs" is not set to "true", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-268155`

### Rule: NixOS must require users to reauthenticate for privilege escalation.

**Rule ID:** `SV-268155r1039536_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the user reauthenticate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS enforces reauthentication with sudo with the following command: $ sudo grep timestamp_timeout /etc/sudoers Defaults timestamp_timeout=0 If "timestamp_timeout" is greater than 0, is commented out, or is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-268156`

### Rule: NixOS must require users to reauthenticate when changing roles.

**Rule ID:** `SV-268156r1039539_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to change security roles, it is critical the user reauthenticate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS requires users to reauthenticate when changing roles with the following command: $ grep -iR wheelneedspassword /etc/nixos/ /etc/nixos/configuration.nix:security.sudo.wheelNeedsPassword = true; If the returned line does not have a value of "true" or is commented out, this is a finding.

## Group: SRG-OS-000393-GPOS-00173

**Group ID:** `V-268157`

### Rule: NixOS must implement cryptographic mechanisms to protect the integrity of nonlocal maintenance and diagnostic communications, when used for nonlocal maintenance sessions.

**Rule ID:** `SV-268157r1039359_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Privileged access contains control and configuration information and is particularly sensitive, so additional protections are necessary. This is maintained by using cryptographic mechanisms, such as a hash function or digital signature, to protect integrity. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. The operating system can meet this requirement through leveraging a cryptographic module. This requirement does not cover hardware/software components that may support information system maintenance, yet are a part of the system (e.g., the software implementing "ping," "ls," "ipconfig," or the hardware and software implementing the monitoring port of an Ethernet switch).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS uses the following FIPS 140-3 approved MAC codes in openssh with the following command: $grep services.openssh.macs -A 3 /etc/nixos/configuration.nix services.openssh.macs = [ "hmac-sha2-512" "hmac-sha2-256" ]; If "services.openssh.macs" contains any ciphers other than "hmac-sha2-512" or "hmac-sha2-256", this is a finding.

## Group: SRG-OS-000420-GPOS-00186

**Group ID:** `V-268158`

### Rule: NixOS must protect against or limit the effects of denial-of-service (DoS) attacks by ensuring the operating system is implementing rate-limiting measures on impacted network interfaces.

**Rule ID:** `SV-268158r1039362_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS firewall enforces rate limits using the hashlimit module. $ sudo iptables -L | grep limit nixos-fw-refuse tcp -- anywhere anywhere tcp dpt:ssh limit: above 1000000b/s mode srcip nixos-fw-refuse tcp -- anywhere anywhere tcp dpt:http limit: above 1000/min burst 5 mode srcip nixos-fw-refuse tcp -- anywhere anywhere tcp dpt:https limit: above 1000/min burst 5 mode srcip If the command does not produce any rate limiting rules, this is a finding.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-268159`

### Rule: NixOS must protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-268159r1039541_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000112-GPOS-00057, SRG-OS-000113-GPOS-00058, SRG-OS-000424-GPOS-00188, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS to enables sshd for secure, confidentially preserving remote access with the following command: $ systemctl status sshd sshd.service - SSH daemon Loaded: loaded (/etc/systemd/system/sshd.service; enabled; present: enabled) Active: active (running) since Sat 2022-06-04 02:51:43 UTC; 13min ago If the sshd.service is not "active" and "running", this is a finding.

## Group: SRG-OS-000433-GPOS-00192

**Group ID:** `V-268160`

### Rule: NixOS must implement nonexecutable data to protect its memory from unauthorized code execution.

**Rule ID:** `SV-268160r1039368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in nonexecutable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can either be hardware-enforced or software-enforced with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks. Satisfies: SRG-OS-000433-GPOS-00192, SRG-OS-000132-GPOS-00067</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS prevents internal kernel addresses from being leaked with the following command: $ sudo sysctl kernel.kptr_restrict kernel.kptr_restrict = 1 If "kernel.kptr_restrict" does not have a value of "1" or is missing, this is a finding.

## Group: SRG-OS-000433-GPOS-00193

**Group ID:** `V-268161`

### Rule: NixOS must implement address space layout randomization to protect its memory from unauthorized code execution.

**Rule ID:** `SV-268161r1039371_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in nonexecutable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can either be hardware-enforced or software-enforced with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS enables address space layout randomization with the following command: $ sudo sysctl kernel.randomize_va_space kernel.randomize_va_space = 2 If "kernel.randomize_va_space" does not have a value of "2" or is missing, this is a finding.

## Group: SRG-OS-000437-GPOS-00194

**Group ID:** `V-268162`

### Rule: NixOS must remove all software components after updated versions have been installed.

**Rule ID:** `SV-268162r1039374_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Previous versions of software components that are not removed from the information system after updates have been installed may be exploited by adversaries. Some information technology products may remove older versions of software automatically from the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS removes all software components after updated versions have been installed by reviewing /etc/nixos/configuration.nix and remove any references to outdated versions of nixpkgs. If any outdated versions of nixpkgs are present in the configuration.nix file, this is a finding.

## Group: SRG-OS-000463-GPOS-00207

**Group ID:** `V-268163`

### Rule: NixOS must generate audit records when successful/unsuccessful attempts to modify security objects occur.

**Rule ID:** `SV-268163r1039377_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000463-GPOS-00207, SRG-OS-000042-GPOS-00020, SRG-OS-000458-GPOS-00203, SRG-OS-000474-GPOS-00219</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the NixOS generates audit records when successful/unsuccessful attempts to modify security objects occur with the following command: $ sudo auditctl -l | grep xattr -a always,exit -F arch=b32 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=-1 -k perm_mod -a always,exit -F arch=b32 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid=0 -k perm_mod -a always,exit -F arch=b64 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=-1 -k perm_mod -a always,exit -F arch=b64 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid=0 -k perm_mod If the command does not return an audit rule for "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr", this is a finding.

## Group: SRG-OS-000466-GPOS-00210

**Group ID:** `V-268164`

### Rule: NixOS must generate audit records when successful/unsuccessful attempts to delete privileges occur.

**Rule ID:** `SV-268164r1039380_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS generates audit records when attempts to delete privileges occur with the following command: $ sudo auditctl -l | grep usermod -a always,exit -S all -F path=/run/current-system/sw/bin/usermod -F perm=x -F auid>=1000 -F auid!=-1 -k privileged-usermod If the command does not return an audit rule for "usermod", this is a finding.

## Group: SRG-OS-000468-GPOS-00212

**Group ID:** `V-268165`

### Rule: NixOS must generate audit records when successful/unsuccessful attempts to delete security objects occur.

**Rule ID:** `SV-268165r1039383_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that NixOS generates audit records when successful/unsuccessful attempts to delete security objects occur with the following command: $ sudo auditctl -l | grep /bin/ch -a always,exit -S all -F path=/run/current-system/sw/bin/chage -F perm=x -F auid>=1000 -F auid!=-1 -k privileged-chage -a always,exit -S all -F path=/run/current-system/sw/bin/chcon -F perm=x -F auid>=1000 -F auid!=-1 -k perm_mod If the command does not return an audit rule for "chage" and "chcon", this is a finding.

## Group: SRG-OS-000473-GPOS-00218

**Group ID:** `V-268166`

### Rule: NixOS must generate audit records when concurrent logins to the same account occur from different sources.

**Rule ID:** `SV-268166r1039580_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000473-GPOS-00218, SRG-OS-000042-GPOS-00020, SRG-OS-000475-GPOS-00220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS is configured to generate audit records with the following command: $ sudo auditctl -l | grep -w lastlog -w /var/log/lastlog -p wa -k logins If the command does not return a watch for the lastlog file, this is a finding.

## Group: SRG-OS-000476-GPOS-00221

**Group ID:** `V-268167`

### Rule: NixOS must generate audit records for all account creations, modifications, disabling, and termination events.

**Rule ID:** `SV-268167r1039389_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000476-GPOS-00221, SRG-OS-000042-GPOS-00020, SRG-OS-000274-GPOS-00104, SRG-OS-000275-GPOS-00105, SRG-OS-000276-GPOS-00106, SRG-OS-000277-GPOS-00107, SRG-OS-000477-GPOS-00222, SRG-OS-000304-GPOS-00121</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS is configured to generate audit records on account events with the following command: $ sudo auditctl -l | grep /etc -w /etc/sudoers -p wa -k identity -w /etc/passwd -p wa -k identity -w /etc/shadow -p wa -k identity -w /etc/gshadow -p wa -k identity -w /etc/group -p wa -k identity -w /etc/security/opasswd -p wa -k identity If the output from the command does not include the example output, this is a finding.

## Group: SRG-OS-000478-GPOS-00223

**Group ID:** `V-268168`

### Rule: NixOS must implement NIST FIPS-validated cryptography for the following: to provision digital signatures, to generate cryptographic hashes, and to protect unclassified information requiring confidentiality and cryptographic protection in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.

**Rule ID:** `SV-268168r1039392_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. The operating system must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. Satisfies: SRG-OS-000478-GPOS-00223, SRG-OS-000396-GPOS-00176</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS is configured to operate in FIPS mode with the following command: $ grep fips /proc/cmdline BOOT_IMAGE=(hd0,msdos1)/nix/store/glc0midc78caq9sc7pzciymx4c3in7kn-linux-6.1.64/bzImage init=/nix/store/grl4baymr9q60mbcz3sidm4agckn3bx5-nixos-system-nixos-23.1.1.20231129.057f9ae/init audit=1 audit_backlog_limit=8192 fips=1 loglevel=4 If the "fips" entry does not equal "1" or is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-268169`

### Rule: NixOS must prevent the use of dictionary words for passwords.

**Rule ID:** `SV-268169r1039395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system allows the user to select passwords based on dictionary words, then this increases the chances of password compromise by increasing the opportunity for successful guesses and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS prevents the use of dictionary words for passwords with the following command: $ grep dict /etc/security/pwquality.conf dictcheck=1 If the value of "ocredit" is a positive number or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-268170`

### Rule: NixOS must enable the use of pwquality.

**Rule ID:** `SV-268170r1039398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system allows the user to select passwords based on dictionary words, then this increases the chances of password compromise by increasing the opportunity for successful guesses and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS prevents the use of dictionary words for passwords with the following command: $ grep -i pam_pwquality /etc/pam.d/passwd /etc/pam.d/chpasswd /etc/pam.d/sudo /etc/pam.d/passwd:password requisite /nix/store/db96zr26w71dzx0bzf47d88kw19fr0l7-libpwquality-1.4.5.-lib/lib/security/pam_pwquality.so /etc/pam.d/chpasswd:password requisite /nix/store/db96zr26w71dzx0bzf47d88kw19fr0l7-libpwquality-1.4.5.-lib/lib/security/pam_pwquality.so /etc/pam.d/sudo:password requisite /nix/store/db96zr26w71dzx0bzf47d88kw19fr0l7-libpwquality-1.4.5.-lib/lib/security/pam_pwquality.so If the pam_pwquality.so module is not present in the passwd, chpasswd, and sudo pam files, this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-268171`

### Rule: NixOS must enforce a delay of at least four seconds between login prompts following a failed login attempt.

**Rule ID:** `SV-268171r1039583_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of login attempts over a certain time interval reduces the chances that an unauthorized user may gain access to an account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the NixOS operating system enforces a four-second delay between login attempts with the following command: $ grep -I delay /etc/login.defs FAIL_DELAY 4 If "FAIL_DELAY" is not set to "4" or greater, is commented out, or is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-268172`

### Rule: NixOS must not allow an unattended or automatic login to the system via the console.

**Rule ID:** `SV-268172r1039586_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Failure to restrict system access via the console to authenticated users negatively impacts operating system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS does not allow an unattended or automatic login to the system via the console with the following command: $ grep -iR autologin.user /etc/nixos If "services.xserver.displayManager.autoLogin.user" is defined and is not "null", this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-268173`

### Rule: NixOS must be configured to use AppArmor.

**Rule ID:** `SV-268173r1039407_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Users' home directories/folders may contain information of a sensitive nature. Nonprivileged users should coordinate any sharing of information with a system administrator (SA) through shared resources. Satisfies: SRG-OS-000480-GPOS-00230, SRG-OS-000368-GPOS-00154</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS is configured to use AppArmor with the following command: $ sudo systemctl status apparmor.service apparmor.service - Load AppArmor policies Loaded: loaded (/etc/systemd/system/apparmor.service; enabled; present: enabled) Active: active (running) since Sat 2022-06-04 02:51:43 UTC; 13min ago If the "apparmor.service" is not enabled and active, this is a finding.

## Group: SRG-OS-000118-GPOS-00060

**Group ID:** `V-268174`

### Rule: NixOS must disable account identifiers (individuals, groups, roles, and devices) after 35 days of inactivity.

**Rule ID:** `SV-268174r1039410_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. Operating systems need to track periods of inactivity and disable application identifiers after 35 days of inactivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS disables account identifiers (individuals, groups, roles, and devices) after 35 days of inactivity with the following command: $ grep -i inactive /etc/default/useradd INACTIVE=35 If INACTIVE is not set to 35 or less, or is missing or commented out, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-268175`

### Rule: NixOS must employ approved cryptographic hashing algorithms for all stored passwords.

**Rule ID:** `SV-268175r1039413_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and DOD data may be compromised. Operating systems using encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-3 is the current standard for validating that mechanisms used to access cryptographic modules use authentication that meets DOD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general purpose computing system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS uses employs approved cryptographic hashing algorithms for all stored passwords with the following command: (Change <unique-username> to the desired user to verify.) $ sudo cat /etc/shadow | grep "<unique-username>" | cut -d'$' -f2 If the command does not return 6 for SHA512, this is a finding.

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-268176`

### Rule: NixOS must employ strong authenticators in the establishment of nonlocal maintenance and diagnostic sessions.

**Rule ID:** `SV-268176r1039416_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If maintenance tools are used by unauthorized personnel, they may accidentally or intentionally damage or compromise the system. The act of managing systems and applications includes the ability to access sensitive application information, such as system configuration details, diagnostic information, user information, and potentially sensitive application data. Some maintenance and test tools are either standalone devices with their own operating systems or are applications bundled with an operating system. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. Typically, strong authentication requires authenticators that are resistant to replay attacks and employ multifactor authentication. Strong authenticators include, for example, PKI where certificates are stored on a token protected by a password, passphrase, or biometric.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS employs strong authentication in the establishment of nonlocal sessions with SSH by the following command: $ sudo /run/current-system/sw/bin/sshd -G | grep pam usepam yes If usepam is not yes, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-268177`

### Rule: NixOS must implement multifactor authentication for remote access to privileged accounts in such a way that one of the factors is provided by a device separate from the system gaining access.

**Rule ID:** `SV-268177r1039419_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a CAC or token that is separate from the information system, ensures that even if the information system is compromised, that compromise will not affect credentials stored on the authentication device. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification (PIV) card and the DOD Common Access Card (CAC). A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., VPN, proxy capability). This does not apply to authentication for the purpose of configuring the device itself (management). This requires further clarification from NIST. Satisfies: SRG-OS-000375-GPOS-00160, SRG-OS-000068-GPOS-00036, SRG-OS-000376-GPOS-00161, SRG-OS-000377-GPOS-00162, SRG-OS-000705-GPOS-00150</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS provides authentication via the security and pam modules with the following command: $ cat /etc/nixos/configuration.nix | grep -A 1 security.pam.p11 security.pam.p11.enable = true; If security.pam.p11.enable is not. "true", is not present or is commented out, this is a finding.

## Group: SRG-OS-000383-GPOS-00166

**Group ID:** `V-268178`

### Rule: NixOS must prohibit the use of cached authenticators after one day.

**Rule ID:** `SV-268178r1039543_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cached authentication information is out-of-date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS, for PKI-based authentication, only caches authenticators for one day with the following command: $ sudo grep expiration /etc/sssd/sssd.conf offline_credentials_expiration = 1 If the offline_credentials_expiration is not set to "1" or is commented out, this is a finding.

## Group: SRG-OS-000384-GPOS-00167

**Group ID:** `V-268179`

### Rule: For PKI-based authentication, NixOS must implement a local cache of revocation data to support path discovery and validation in case of the inability to access revocation information via the network.

**Rule ID:** `SV-268179r1039545_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without configuring a local cache of revocation data, there is the potential to allow access to users who are no longer authorized (users with revoked certificates).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS, for PKI-based authentication, uses local revocation data when unable to access the network to obtain it remotely with the following command: $ grep cert_policy /etc/pam_pkcs11/pam_pkcs11.conf cert_policy = ca,signature,ocsp_on, crl_auto; If the cert_policy does not contain the options in the example output, this is a finding.

## Group: SRG-OS-000439-GPOS-00195

**Group ID:** `V-268180`

### Rule: NixOS must run a supported release of the operating system.

**Rule ID:** `SV-268180r1039428_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security flaws with operating systems are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NixOS is running a supported version with the following command: $ nixos-version 23.11.20231129.057f9ae (Tapir) If the NixOS is not running a supported version, this is a finding.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-268181`

### Rule: NixOS must define default permissions for all authenticated users in such a way that the user can only read and modify their own files.

**Rule ID:** `SV-268181r1039431_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the most restrictive default permissions ensures that when new accounts are created they do not have unnecessary access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the NixOS operating system to change default file permissions so users may only modify their own files. Ensure the following settings are present in the /etc/nixos/configuration.nix file: { config, pkgs, lib, ... }: environment.etc = { ""login.defs"".source = lib.mkForce (pkgs.writeText ""login.defs"" '' DEFAULT_HOME yes SYS_UID_MIN 400 SYS_UID_MAX 999 UID_MIN 1000 UID_MAX 29999 SYS_GID_MIN 400 SYS_GID_MAX 999 GID_MIN 1000 GID_MAX 29999 TTYGROUP tty TTYPERM 0620 # Ensure privacy for newly created home directories. UMASK 077 # Uncomment this and install chfn SUID to allow nonroot # users to change their account GECOS information. # This should be made configurable. #CHFN_RESTRICT frwh ''; }; If the above configurations are not present in the configuration.nix file, this is a finding.

