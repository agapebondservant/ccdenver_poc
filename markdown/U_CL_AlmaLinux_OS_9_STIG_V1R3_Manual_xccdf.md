# STIG Benchmark: CloudLinux AlmaLinux OS 9 Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000027-GPOS-00008

**Group ID:** `V-269102`

### Rule: AlmaLinux OS 9 must limit the number of concurrent sessions to ten for all accounts and/or account types.

**Rule ID:** `SV-269102r1049984_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Operating system management includes the ability to control the number of users and user sessions that use an operating system. Limiting the number of allowed users and sessions per user is helpful in reducing the risks related to denial-of-service (DoS) attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 limits the number of concurrent sessions to "10" for all accounts and/or account types with the following command: $ grep -rs maxlogins /etc/security/limits.conf /etc/security/limits.d/*.conf /etc/security/limits.d/maxlogins.conf:* hard maxlogins 10 This can be set as a global domain (with the * wildcard) but may be set differently for multiple domains. If the "maxlogins" item is missing, commented out, or the value is set greater than 10, this is a finding.

## Group: SRG-OS-000031-GPOS-00012

**Group ID:** `V-269103`

### Rule: AlmaLinux OS 9 must automatically lock graphical user sessions after 15 minutes of inactivity.

**Rule ID:** `SV-269103r1101811_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. The operating system session lock event must include an obfuscation of the display screen so as to prevent other users from reading what was previously displayed. Publicly viewable images can include static or dynamic images, for example, patterns used with screen savers, photographic images, solid colors, a clock, a battery life indicator, or a blank screen, with the additional caveat that none of the images convey sensitive information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the AlmaLinux OS 9 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify AlmaLinux OS 9 initiates a session lock after a 10-minute period of inactivity for graphical user interfaces with the following command: $ gsettings get org.gnome.desktop.session idle-delay uint32 600 If "idle-delay" is set to "0" or a value greater than "600", this is a finding.

## Group: SRG-OS-000031-GPOS-00012

**Group ID:** `V-269104`

### Rule: AlmaLinux OS 9 must conceal, via the session lock, information previously visible on the display with a publicly viewable image.

**Rule ID:** `SV-269104r1049986_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the screensaver mode to blank-only conceals the contents of the display from passersby.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the AlmaLinux OS 9 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. To ensure the screensaver is configured to be blank, run the following command: $ gsettings get org.gnome.desktop.screensaver picture-uri If properly configured, the output should be "''". To ensure that users cannot set the screensaver background, run the following: $ grep picture-uri /etc/dconf/db/local.d/locks/* If properly configured, the output should be "/org/gnome/desktop/screensaver/picture-uri". If it is not set or configured properly, this is a finding.

## Group: SRG-OS-000031-GPOS-00012

**Group ID:** `V-269105`

### Rule: AlmaLinux OS 9 must prevent a user from overriding the session idle-delay setting for the graphical user interface.

**Rule ID:** `SV-269105r1101820_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. The operating system session lock event must include an obfuscation of the display screen so as to prevent other users from reading what was previously displayed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the AlmaLinux OS 9 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify AlmaLinux OS 9 prevents a user from overriding settings for graphical user interfaces. Determine which profile the system database is using with the following command: $ grep system-db /etc/dconf/profile/user system-db:local Check that graphical settings are locked from nonprivileged user modification with the following command: Note: The example below is using the database "local" for the system, so the path is "/etc/dconf/db/local.d". This path must be modified if a database other than "local" is being used. $ grep -i idle /etc/dconf/db/local.d/locks/* /org/gnome/desktop/session/idle-delay If the command does not return at least the example result, this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-269106`

### Rule: AlmaLinux OS 9 must initiate a session lock for graphical user interfaces when the screensaver is activated.

**Rule ID:** `SV-269106r1049988_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to logout because of the temporary nature of the absence.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the AlmaLinux OS 9 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify AlmaLinux OS 9 initiates a session lock for graphical user interfaces when the screensaver is activated with the following command: $ gsettings get org.gnome.desktop.screensaver lock-delay uint32 5 If the "uint32" setting is not set to "5" or less, or is missing, this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-269107`

### Rule: AlmaLinux OS 9 must prevent a user from overriding the session lock-delay setting for the graphical user interface.

**Rule ID:** `SV-269107r1049989_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not logout because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, the GNOME desktop can be configured to identify when a user's session has idled and take action to initiate the session lock. As such, users should not be allowed to change session settings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the AlmaLinux OS 9 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify AlmaLinux OS 9 prevents a user from overriding settings for graphical user interfaces. Determine which profile the system database is using with the following command: $ grep system-db /etc/dconf/profile/user system-db:local Check that graphical settings are locked from nonprivileged user modification with the following command: Note: The example below is using the database "local" for the system, so the path is "/etc/dconf/db/local.d". This path must be modified if a database other than "local" is being used. $ grep -i lock-delay /etc/dconf/db/local.d/locks/* /etc/dconf/db/local.d/locks/session:/org/gnome/desktop/screensaver/lock-delay If the command does not return at least the example result, this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-269108`

### Rule: AlmaLinux OS 9 must automatically exit interactive command shell user sessions after 10 minutes of inactivity.

**Rule ID:** `SV-269108r1049990_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle interactive command shell user session within a short time period reduces the window of opportunity for unauthorized personnel to take control of it when left unattended in a virtual terminal or physical console. Declaring $TMOUT as read-only means the user cannot override the setting. Satisfies: SRG-OS-000029-GPOS-00010, SRG-OS-000281-GPOS-00111, SRG-OS-000163-GPOS-00072</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 is configured to exit interactive command shell user sessions after 10 minutes of inactivity or less with the following command: $ grep TMOUT /etc/profile /etc/profile.d/*.sh /etc/profile.d/tmout.sh:declare -xr TMOUT=600 If "TMOUT" is not set to "600" or less in a script located in the "/etc/'profile.d/ directory, is missing or is commented out, this is a finding.

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-269109`

### Rule: AlmaLinux OS 9 must be able to directly initiate a session lock for all connection types using smart card when the smart card is removed.

**Rule ID:** `SV-269109r1049991_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Regardless of where the session lock is determined and implemented, once invoked, the session lock must remain in place until the user re-authenticates. No other activity aside from re-authentication must unlock the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the AlmaLinux OS 9 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify AlmaLinux OS 9 enables a user's session lock until that user re-establishes access using established identification and authentication procedures with the following command: $ grep -R removal-action= /etc/dconf/db/* /etc/dconf/db/distro.d/00-security-settings:removal-action='lock-screen' If the "removal-action='lock-screen'" setting is missing or commented out from the dconf database files, this is a finding.

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-269110`

### Rule: AlmaLinux OS 9 must prevent a user from overriding the disabling of the graphical user smart card removal action.

**Rule ID:** `SV-269110r1049992_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Regardless of where the session lock is determined and implemented, once invoked, the session lock must remain in place until the user re-authenticates. No other activity aside from re-authentication must unlock the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 disables the ability of the user to override the smart card removal action setting. Note: This requirement assumes the use of the AlmaLinux OS 9 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Determine which profile the system database is using with the following command: $ grep system-db /etc/dconf/profile/user system-db:local Check that the removal action setting is locked from nonprivileged user modification with the following command: Note: The example below is using the database "local" for the system, so the path is "/etc/dconf/db/local.d". This path must be modified if a database other than "local" is being used. $ grep 'removal-action' /etc/dconf/db/local.d/locks/* /etc/dconf/db/local.d/locks/00-security-settings-lock:/org/gnome/settings-daemon/peripherals/smartcard/removal-action If the command does not return at least the example result, this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-269111`

### Rule: AlmaLinux OS 9 must log SSH connection attempts and failures to the server.

**Rule ID:** `SV-269111r1050605_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk, and make remote user access management difficult at best. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyber attacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets). SSH provides several logging levels with varying amounts of verbosity. "DEBUG" is specifically not recommended other than strictly for debugging SSH communications since it provides so much data that it is difficult to identify important security information. "INFO" or "VERBOSE" level is the basic level that only records login activity of SSH users. In many situations, such as Incident Response, it is important to determine when a particular user was active on a system. The logout record can eliminate those users who disconnected, which helps narrow the field.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 logs SSH connection attempts and failures to the server. Check what the SSH daemon's "LogLevel" option is set to with the following command: $ sshd -T | grep loglevel loglevel VERBOSE If a value of "VERBOSE" is not returned, or is commented out, this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-269112`

### Rule: All AlmaLinux OS 9 remote access methods must be monitored.

**Rule ID:** `SV-269112r1050606_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk, and make remote user access management difficult at best. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyber attacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets). Monitoring of remote access can be used to spot attacks such as brute-force authentication attempts and denial-of-service (DoS) attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 monitors all remote access methods, by running the following command: $ grep -rsE '^(auth|authpriv|daemon)\.\*' /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.conf:authpriv.* /var/log/secure If "auth.*", "authpriv.*" or "daemon.*" are not configured to be logged, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-269113`

### Rule: AlmaLinux OS 9 SSH client must be configured to use only encryption ciphers employing FIPS 140-3-validated cryptographic hash algorithms to protect the confidentiality of SSH client connections.

**Rule ID:** `SV-269113r1107624_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. AlmaLinux OS 9 incorporates systemwide crypto policies by default. Configuration files in /etc/ssh/ have no effect on the ciphers, MACs, or algorithms used by the operating system. The employed ssh client algorithms can be viewed in the /etc/crypto-policies/back-ends/openssh.config file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH client is configured to use only ciphers employing FIPS 140-3-approved algorithms with the following command: $ grep -i Ciphers /etc/crypto-policies/back-ends/openssh.config Ciphers aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes128-ctr If the cipher entries in the "openssh.config" file have any ciphers other than "aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes128-ctr", they are missing, or commented out, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-269114`

### Rule: AlmaLinux OS 9 must implement DOD-approved encryption ciphers to protect the confidentiality of SSH connections.

**Rule ID:** `SV-269114r1101819_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. AlmaLinux OS 9 incorporates systemwide crypto policies by default. The SSH configuration file has no effect on the ciphers, MACs, or algorithms unless specifically defined in the /etc/sysconfig/sshd file. The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/opensshserver.config file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that systemwide crypto policies are in effect with the following command: $ sudo grep Include /etc/ssh/sshd_config /etc/ssh/sshd_config.d/* /etc/ssh/sshd_config:Include /etc/ssh/sshd_config.d/*.conf /etc/ssh/sshd_config.d/50-redhat.conf:Include /etc/crypto-policies/back-ends/opensshserver.config If "Include /etc/ssh/sshd_config.d/*.conf" or "Include /etc/crypto-policies/back-ends/opensshserver.config" are not included in the system sshd config or the file "/etc/ssh/sshd_config.d/50-redhat.conf" is missing, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-269115`

### Rule: AlmaLinux OS 9 SSH client must be configured to use only Message Authentication Codes (MACs) employing FIPS 140-3-validated cryptographic hash algorithms.

**Rule ID:** `SV-269115r1107608_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g. RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. AlmaLinux OS 9 incorporates systemwide crypto policies by default. The /etc/ssh/ssh_config file has no effect on the ciphers, MACs, or algorithms. The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/openssh.config file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH client is configured to use only MACs employing FIPS 140-3-approved algorithms. To verify the MACs in the systemwide SSH configuration file, use the following command: $ grep -i MACs /etc/crypto-policies/back-ends/openssh.config MACs hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha2-256,hmac-sha2-512 If the MACs entries in the "openssh.config" file have any hashes other than "hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha2-256,hmac-sha2-512", or they are missing or commented out, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-269116`

### Rule: The AlmaLinux 9 SSH server must be configured to use only DOD-approved encryption ciphers employing FIPS 140-3-validated cryptographic hash algorithms to protect the confidentiality of SSH server connections.

**Rule ID:** `SV-269116r1107625_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH server is configured to use only ciphers employing FIPS 140-3-approved algorithms. To verify the ciphers in the systemwide SSH configuration file, use the following command: $ sudo grep -i Ciphers /etc/crypto-policies/back-ends/opensshserver.config Ciphers aes256-gcm@openssh.com,aes256-ctr,aes128-gcm@openssh.com,aes128-ctr If the cipher entries in the "opensshserver.config" file have any ciphers other than "aes256-gcm@openssh.com,aes256-ctr,aes128-gcm@openssh.com,aes128-ctr", or they are missing or commented out, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-269118`

### Rule: AlmaLinux OS 9 must implement DOD-approved systemwide cryptographic policies to protect the confidentiality of SSH server connections.

**Rule ID:** `SV-269118r1050609_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that systemwide crypto policies are in effect with the following command: $ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*include' /etc/ssh/sshd_config:Include /etc/ssh/sshd_config.d/*.conf /etc/ssh/sshd_config.d/50-redhat.conf:Include /etc/crypto-policies/back-ends/opensshserver.config If "Include /etc/ssh/sshd_config.d/*.conf" or "Include /etc/crypto-policies/back-ends/opensshserver.config" are not included in the system sshd config or the file /etc/ssh/sshd_config.d/50-redhat.conf is missing, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-269119`

### Rule: The AlmaLinux OS 9 SSH server must be configured to use only Message Authentication Codes (MACs) employing FIPS 140-3-validated cryptographic hash algorithms to protect the confidentiality of SSH server connections.

**Rule ID:** `SV-269119r1107614_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. AlmaLinux OS 9 incorporates systemwide crypto policies by default. The SSH configuration file has no effect on the ciphers, MACs, or algorithms employed on the server. The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/opensshserver.config file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH server is configured to use only MACs employing FIPS 140-3-approved algorithms. To verify the MACs in the systemwide SSH configuration file, use the following command: $ sudo grep -i MACs /etc/crypto-policies/back-ends/opensshserver.config MACs hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha2-256,hmac-sha2-512 If the MACs entries in the "opensshserver.config" file have any hashes other than "hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha2-256,hmac-sha2-512", or they are missing or commented out, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-269120`

### Rule: AlmaLinux OS 9 must force a frequent session key renegotiation for SSH connections to the server.

**Rule ID:** `SV-269120r1050610_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection (e.g., RDP), thereby providing a degree of confidentiality. The encryption strength of a mechanism is selected based on the security categorization of the information. Session key regeneration limits the chances of a session key becoming compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH server is configured to force frequent session key renegotiation with the following command: $ sshd -T | grep rekeylimit rekeylimit 1073741824 3600 If "RekeyLimit" does not have a maximum data amount and maximum time defined, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-269121`

### Rule: AlmaLinux OS 9 must implement DOD-approved TLS encryption in the GnuTLS package.

**Rule ID:** `SV-269121r1050611_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if GnuTLS uses defined DOD-approved TLS Crypto Policy with the following command: $ update-crypto-policies --show FIPS If the system wide crypto policy is not set to "FIPS", this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-269122`

### Rule: AlmaLinux OS 9 IP tunnels must use FIPS 140-3 approved cryptographic algorithms.

**Rule ID:** `SV-269122r1050004_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Overriding the system crypto policy makes the behavior of the Libreswan service violate expectations and makes the system configuration more fragmented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the Libreswan package is not installed, this requirement is Not Applicable. Verify that the IPsec service uses the system crypto policy with the following command: $ grep -rE '^include ' /etc/ipsec.conf /etc/ipsec.d/ /etc/ipsec.conf:include /etc/crypto-policies/back-ends/libreswan.config /etc/ipsec.conf:include /etc/ipsec.d/*.conf If the IPsec configuration file does not contain "include /etc/crypto-policies/back-ends/libreswan.config", this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-269123`

### Rule: AlmaLinux OS 9 must implement DOD-approved encryption in the OpenSSL package.

**Rule ID:** `SV-269123r1050005_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/openssl.config file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 OpenSSL library is configured to use only ciphers employing FIPS 140-3 approved algorithms with the following command: $ grep -i opensslcnf.config /etc/pki/tls/openssl.cnf .include = /etc/crypto-policies/back-ends/opensslcnf.config If the "opensslcnf.config" is not defined in the "/etc/pki/tls/openssl.cnf" file, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-269124`

### Rule: AlmaLinux OS 9 must implement DOD-approved TLS encryption in the OpenSSL package.

**Rule ID:** `SV-269124r1050006_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access (e.g., RDP) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/openssl.config file.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 OpenSSL library is configured to use TLS 1.2 encryption or stronger with following command: $ grep -i minprotocol /etc/crypto-policies/back-ends/opensslcnf.config TLS.MinProtocol = TLSv1.2 DTLS.MinProtocol = DTLSv1.2 If the "TLS.MinProtocol" is set to anything older than "TLSv1.2" or the "DTLS.MinProtocol" is set to anything older than "DTLSv1.2", this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-269125`

### Rule: AlmaLinux OS 9 must use the TuxCare ESU repository.

**Rule ID:** `SV-269125r1107616_rule`
**Severity:** high

**Description:**
<VulnDiscussion>FIPS 140-3-validated packages are available from TuxCare. The TuxCare repositories provide the packages and updates not found in the community repositories. Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000125-GPOS-00065, SRG-OS-000396-GPOS-00176, SRG-OS-000478-GPOS-00223</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is using the TuxCare ESU repositories with the following command: $ dnf repolist | grep tuxcare tuxcare-base TuxCare Enterprise Support for AlmaLinux 9.2 - Base tuxcare-esu TuxCare Enterprise Support for AlmaLinux 9.2 - ESU tuxcare-radar TuxCare Radar If the tuxcare-esu repository is not enabled, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-269126`

### Rule: AlmaLinux OS 9 must use the TuxCare FIPS packages and not the default encryption packages.

**Rule ID:** `SV-269126r1107617_rule`
**Severity:** high

**Description:**
<VulnDiscussion>FIPS 140-3-validated packages are available from TuxCare here: https://tuxcare.com/fips-for-almalinux/ The original community packages must be replaced with the versions that have gone through the CMVP. Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000478-GPOS-00223, SRG-OS-000396-GPOS-00176, SRG-OS-000125-GPOS-00065</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is using the TuxCare FIPS packages with the following command: $ rpm -qa | grep -E '^(gnutls|nettle|nss|openssl|libgcrypt|kernel)-[0-9]+' | grep -v tuxcare If the command returns anything, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-269127`

### Rule: AlmaLinux OS 9 must enable FIPS mode.

**Rule ID:** `SV-269127r1107618_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection (e.g., RDP), thereby providing a degree of confidentiality. The encryption strength of a mechanism is selected based on the security categorization of the information. The operating system must use cryptographic modules that have been validated by NIST's FIPS 140-3 program. Using weak or untested cryptography could compromise the confidentiality and integrity of data at rest and in transit. Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000478-GPOS-00223, SRG-OS-000396-GPOS-00176, SRG-OS-000125-GPOS-00065</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is in FIPS mode with the following command: $ fips-mode-setup --check FIPS mode is enabled. If FIPS mode is not enabled, this is a finding.

## Group: SRG-OS-000002-GPOS-00002

**Group ID:** `V-269128`

### Rule: AlmaLinux OS 9 must automatically expire temporary accounts within 72 hours.

**Rule ID:** `SV-269128r1050010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Temporary accounts are accounts created during a time of need when prompt action requires bypassing the normal account creation authorization process – such as during incident response. If these temporary accounts are left enabled (and may have elevated permissions via sudo, group membership or SSH keys) and are not automatically expired or manually removed, the security posture of the system will be degraded and left vulnerable to insider threat. Temporary accounts are not the same as "last resort" or "break glass" emergency accounts which are local system accounts to be used by and maintained by authorized system administrators when standard remote access/authentication is unavailable. Emergency accounts are not subject to removal or expiration requirements. Satisfies: SRG-OS-000002-GPOS-00002, SRG-OS-000123-GPOS-00064</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify temporary accounts have been provisioned with an expiration date of 72 hours. For every existing temporary account, run the following command to obtain its account expiration information: $ chage -l <account name> | grep -i "account expires" Verify each of these accounts has an expiration date set within 72 hours. If any temporary accounts have an expiration date set to "never" or do not expire within 72 hours, this is a finding.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-269129`

### Rule: AlmaLinux OS 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/sudoers.

**Rule ID:** `SV-269129r1050011_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit records provide a means to investigate events related to a security incident. Insufficient audit coverage will make identifying those responsible challenging or impossible. This auditd policy will watch for and alert the system administrators regarding any modifications to the "/etc/sudoers" file such as adding privileged users, groups, or commands. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221, SRG-OS-000755-GPOS-00220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 generates audit records for all account creations, modifications, disabling, and termination events that affect the "/etc/sudoers" file, with the following command: $ grep /etc/sudoers /etc/audit/audit.rules -w /etc/sudoers -p wa -k identity If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-269130`

### Rule: AlmaLinux OS 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/group.

**Rule ID:** `SV-269130r1050012_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit records provide a means to investigate events related to a security incident. Insufficient audit coverage will make identifying those responsible challenging or impossible. This auditd policy will watch for and alert the system administrators regarding any modifications to the "/etc/group" file such as adding/removing/disabling groups. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 generates audit records for all account creations, modifications, disabling, and termination events that affect the "/etc/group" file, with the following command: $ grep /etc/group /etc/audit/audit.rules -w /etc/group -p wa -k identity If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-269131`

### Rule: AlmaLinux OS 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/gshadow.

**Rule ID:** `SV-269131r1050013_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit records provide a means to investigate events related to a security incident. Insufficient audit coverage will make identifying those responsible challenging or impossible. This auditd policy will watch for and alert the system administrators regarding any modifications to the "/etc/gshadow" file such as adding/removing/disabling users. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 generates audit records for all account creations, modifications, disabling, and termination events that affect the "/etc/gshadow" file, with the following command: $ grep /etc/gshadow /etc/audit/audit.rules -w /etc/gshadow -p wa -k identity If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-269132`

### Rule: AlmaLinux OS 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/security/opasswd.

**Rule ID:** `SV-269132r1050014_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit records provide a means to investigate events related to a security incident. Insufficient audit coverage will make identifying those responsible challenging or impossible. This auditd policy will watch for and alert the system administrators regarding any modifications to the "/etc/security/opasswd" file such as adding/removing/disabling users. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 generates audit records for all account creations, modifications, disabling, and termination events that affect the "/etc/security/opasswd" file, with the following command: $ grep /etc/security/opasswd /etc/audit/audit.rules -w /etc/security/opasswd -p wa -k identity If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-269133`

### Rule: AlmaLinux OS 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/passwd.

**Rule ID:** `SV-269133r1050015_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit records provide a means to investigate events related to a security incident. Insufficient audit coverage will make identifying those responsible challenging or impossible. This auditd policy will watch for and alert the system administrators regarding any modifications to the "/etc/passwd" file such as adding/removing/disabling users. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221, SRG-OS-000274-GPOS-00104, SRG-OS-000275-GPOS-00105, SRG-OS-000276-GPOS-00106, SRG-OS-000277-GPOS-00107</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 generates audit records for all account creations, modifications, disabling, and termination events that affect the "/etc/passwd" file, with the following command: $ grep /etc/passwd /etc/audit/audit.rules -w /etc/passwd -p wa -k identity If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-269134`

### Rule: AlmaLinux OS 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/shadow.

**Rule ID:** `SV-269134r1050016_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit records provide a means to investigate events related to a security incident. Insufficient audit coverage will make identifying those responsible challenging or impossible. This auditd policy will watch for and alert the system administrators regarding any modifications to the "/etc/shadow" file such as adding/removing/disabling users. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 generates audit records for all account creations, modifications, disabling, and termination events that affect the "/etc/shadow" file, with the following command: $ grep /etc/shadow /etc/audit/audit.rules -w /etc/shadow -p wa -k identity If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000004-GPOS-00004

**Group ID:** `V-269135`

### Rule: AlmaLinux OS 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect the files within /etc/sudoers.d/

**Rule ID:** `SV-269135r1050017_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit records provide a means to investigate events related to a security incident. Insufficient audit coverage will make identifying those responsible challenging or impossible. This auditd policy will watch for and alert the system administrators regarding any modifications to the files within "/etc/sudoers.d/" such as adding privileged users, groups, or commands. Satisfies: SRG-OS-000004-GPOS-00004, SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000304-GPOS-00121, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000470-GPOS-00214, SRG-OS-000471-GPOS-00215, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000466-GPOS-00210, SRG-OS-000476-GPOS-00221</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 generates audit records for all account creations, modifications, disabling, and termination events that affect the files within "/etc/sudoers.d/", with the following command: $ grep /etc/sudoers.d/ /etc/audit/audit.rules -w /etc/sudoers.d/ -p wa -k identity If the command does not return a line or the line is commented out, this is a finding. Note: The "-k" allows for specifying an arbitrary identifier, and the string after it does not need to match the example output above.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-269136`

### Rule: AlmaLinux OS 9 must require authentication to access emergency mode.

**Rule ID:** `SV-269136r1050018_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement prevents attackers with physical access from easily bypassing security on the machine and gaining root access. Such accesses are further prevented by configuring the bootloader password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 requires authentication for emergency mode with the following command: $ grep -E 'ExecStart.*sulogin' /usr/lib/systemd/system/emergency.service ExecStart=-/usr/lib/systemd/systemd-sulogin-shell emergency If this line is not returned, or is commented out, this is a finding. If the output is different, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-269137`

### Rule: AlmaLinux OS 9 must require a boot loader password.

**Rule ID:** `SV-269137r1050019_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password protection on the boot loader configuration ensures users with physical access cannot trivially alter important bootloader settings. These include which kernel to use, and whether to enter single-user mode.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the boot loader superuser password is required using the following command: $ grep password /etc/grub2.cfg password_pbkdf2 superman ${GRUB2_PASSWORD} Verify the boot loader superuser password has been set and the password is encrypted using the following command: $ cat /boot/grub2/user.cfg GRUB2_PASSWORD=grub.pbkdf2.sha512.10000.5766DCE424DCD4F0A2F5AC774C044BE8B904BC F0022B671CD5E522A3568C599F327EBA3F3F5AB30D69A9B9A4FD172B12435BC10BE0A9B40669FB A5C5ECBE8D1B.EAC815AE6F8A3F79F800D2EC7F454933BC3D63282532AAB1C487CA25331DD359F 5BF61166EDB53FB33977E982A9F20327D988DA15CBF7E4238357E65C5AEAF3C If a "GRUB2_PASSWORD" is not set, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-269138`

### Rule: AlmaLinux OS 9 must require a unique superuser's name upon booting into single-user and maintenance modes.

**Rule ID:** `SV-269138r1050020_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Having a nondefault grub superuser username makes password-guessing attacks less effective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the boot loader superuser account has been set with the following command: $ grep -A1 "superusers" /etc/grub2.cfg set superusers="superman" export superusers password_pbkdf2 superman ${GRUB2_PASSWORD} In this example "superman" is the actual account name, changed from the default "root". If superusers contains easily guessable usernames, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-269139`

### Rule: AlmaLinux OS 9 must require authentication to access single-user mode.

**Rule ID:** `SV-269139r1050021_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement prevents attackers with physical access from easily bypassing security on the machine and gaining root access. Such accesses are further prevented by configuring the bootloader password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 requires authentication for single-user mode with the following command: $ grep -E 'ExecStart.*sulogin' /usr/lib/systemd/system/rescue.service ExecStart=-/usr/lib/systemd/systemd-sulogin-shell rescue If this line is not returned or is commented out, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-269140`

### Rule: The systemd Ctrl-Alt-Delete burst key sequence in AlmaLinux OS 9 must be disabled.

**Rule ID:** `SV-269140r1050022_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A locally logged-on user who presses Ctrl-Alt-Delete in quick succession when at the console can reboot the system. If accidentally pressed, as could happen in the case of a mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot. In a graphical user environment, risk of unintentional reboot from the Ctrl-Alt-Delete sequence is reduced because the user will be prompted before any action is taken.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 is configured to not reboot the system when Ctrl-Alt-Delete is pressed seven times within two seconds with the following command: $ systemd-analyze cat-config systemd/system.conf | grep -v '#' | grep CtrlAltDel CtrlAltDelBurstAction=none If "CtrlAltDelBurstAction" is not set to "none", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-269141`

### Rule: The Ctrl-Alt-Delete key sequence must be disabled on AlmaLinux OS 9.

**Rule ID:** `SV-269141r1101851_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A locally logged-on user who presses Ctrl-Alt-Delete when at the console can reboot the system. If accidentally pressed, as could happen in the case of a mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot. In a graphical user environment, risk of unintentional reboot from the Ctrl-Alt-Delete sequence is reduced because the user will be prompted before any action is taken.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 is not configured to reboot the system when Ctrl-Alt-Delete is pressed with the following command: $ systemctl status ctrl-alt-del.target ctrl-alt-del.target Loaded: masked (Reason: Unit ctrl-alt-del.target is masked.) Active: inactive (dead) If the "ctrl-alt-del.target" is loaded and not masked, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-269142`

### Rule: AlmaLinux OS 9 must have the sudo package installed.

**Rule ID:** `SV-269142r1050024_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>"sudo" is a program designed to allow a system administrator to give limited root privileges to users and log root activity. The basic philosophy is to give as few privileges as possible but still allow system users to complete their work.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the AlmaLinux OS 9 sudo package is installed with the following command: $ dnf list --installed sudo Installed Packages sudo.x86_64 1.9.5p2-9.el9 @anaconda If the "sudo" package is not installed, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-269143`

### Rule: The AlmaLinux OS 9 debug-shell systemd service must be disabled.

**Rule ID:** `SV-269143r1050025_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The debug-shell requires no authentication and provides root privileges to anyone who has physical access to the machine. While this feature is disabled by default, masking it adds an additional layer of assurance that it will not be enabled via a dependency in systemd. This also prevents attackers with physical access from easily bypassing security on the machine through valid troubleshooting configurations and gaining root access when the system is rebooted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 is configured to mask the debug-shell systemd service with the following command: $ systemctl status debug-shell.service debug-shell.service Loaded: masked (Reason: Unit debug-shell.service is masked.) Active: inactive (dead) If the "debug-shell.service" is loaded and not masked, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-269144`

### Rule: AlmaLinux OS 9 must enable kernel parameters to enforce discretionary access control on hardlinks.

**Rule ID:** `SV-269144r1050026_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By enabling the fs.protected_hardlinks kernel parameter, users can no longer create soft or hard links to files they do not own. Disallowing such hardlinks mitigates vulnerabilities based on unsecure file systems accessed by privileged programs, avoiding an exploitation vector exploiting unsafe use of open() or creat().</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 is configured to enable DAC on hardlinks with the following command: $ sysctl fs.protected_hardlinks fs.protected_hardlinks = 1 If "fs.protected_hardlinks" is not set to "1" or is missing, this is a finding. Check that the configuration files are present to enable this kernel parameter: $ /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F fs.protected_hardlinks | tail -1 fs.protected_hardlinks = 1 If "fs.protected_hardlinks" is not set to "1" or is missing, this is a finding.

## Group: SRG-OS-000324-GPOS-00125

**Group ID:** `V-269145`

### Rule: AlmaLinux OS 9 must enable kernel parameters to enforce discretionary access control (DAC) on symlinks.

**Rule ID:** `SV-269145r1050027_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By enabling the fs.protected_symlinks kernel parameter, symbolic links are permitted to be followed only when outside a sticky world-writable directory, or when the user identifier (UID) of the link and follower match, or when the directory owner matches the symlink's owner. Disallowing such symlinks helps mitigate vulnerabilities based on unsecure file systems accessed by privileged programs, avoiding an exploitation vector exploiting unsafe use of open() or creat().</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 is configured to enable DAC on symlinks with the following command: $ sysctl fs.protected_symlinks fs.protected_symlinks = 1 If "fs.protected_symlinks " is not set to "1" or is missing, this is a finding. Check that the configuration files are present to enable this kernel parameter: $ /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F fs.protected_symlinks | tail -1 fs.protected_symlinks = 1 If "fs.protected_symlinks" is not set to "1" or is missing, this is a finding.

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-269146`

### Rule: AlmaLinux OS 9 must audit uses of the "execve" system call.

**Rule ID:** `SV-269146r1050028_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat. Satisfies: SRG-OS-000327-GPOS-00127, SRG-OS-000326-GPOS-00126</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "execve" system call with the following command: $ auditctl -l | grep execve -a always,exit -F arch=b32 -S execve -C uid!=euid -F euid=0 -F key=execpriv -a always,exit -F arch=b64 -S execve -C uid!=euid -F euid=0 -F key=execpriv -a always,exit -F arch=b32 -S execve -C gid!=egid -F egid=0 -F key=execpriv -a always,exit -F arch=b64 -S execve -C gid!=egid -F egid=0 -F key=execpriv If the command does not return all lines, or the lines are commented out, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-269147`

### Rule: AlmaLinux OS 9 must automatically lock an account when three unsuccessful logon attempts occur.

**Rule ID:** `SV-269147r1050029_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 is configured to lock an account after three unsuccessful logon attempts with the command: $ grep deny /etc/security/faillock.conf deny = 3 If the "deny" option is not set to 3 or less (but not 0), is missing or commented out, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-269148`

### Rule: AlmaLinux OS 9 must automatically lock the root account until the root account is released by an administrator when three unsuccessful logon attempts occur during a 15-minute time period.

**Rule ID:** `SV-269148r1050030_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 is configured to lock the root account after three unsuccessful logon attempts with the command: $ grep even_deny_root /etc/security/faillock.conf even_deny_root If the "even_deny_root" option is not set, is missing, or is commented out, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-269149`

### Rule: AlmaLinux OS 9 must automatically lock an account when three unsuccessful logon attempts occur during a 15-minute time period.

**Rule ID:** `SV-269149r1050031_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system administrator demonstrates the use of an approved centralized account management method that locks an account after three unsuccessful logon attempts within a period of 15 minutes, this requirement is Not Applicable. Verify AlmaLinux OS 9 locks an account after three unsuccessful logon attempts within a period of 15 minutes with the following command: $ grep fail_interval /etc/security/faillock.conf fail_interval = 900 If the "fail_interval" option is not set to 900 or less (but not 0), the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-269150`

### Rule: AlmaLinux OS 9 must configure the use of the pam_faillock.so module in the /etc/pam.d/system-auth file.

**Rule ID:** `SV-269150r1050032_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. If the pam_faillock.so module is not loaded, the system will not correctly lockout accounts to prevent password guessing attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the pam_faillock.so module is present in the "/etc/pam.d/system-auth" file: $ grep pam_faillock.so /etc/pam.d/system-auth auth required pam_faillock.so preauth auth required pam_faillock.so authfail account required pam_faillock.so If the pam_faillock.so module is not present in the "/etc/pam.d/system-auth" file with the "preauth" line listed before pam_unix.so, this is a finding. If the system administrator (SA) can demonstrate that the required configuration is contained in a PAM configuration file included or substacked from the system-auth file, this is not a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-269151`

### Rule: AlmaLinux OS 9 must configure the use of the pam_faillock.so module in the /etc/pam.d/password-auth file.

**Rule ID:** `SV-269151r1050033_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. If the pam_faillock.so module is not loaded, the system will not correctly lockout accounts to prevent password guessing attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the pam_faillock.so module is present in the "/etc/pam.d/password-auth" file: $ grep pam_faillock.so /etc/pam.d/password-auth auth required pam_faillock.so preauth auth required pam_faillock.so authfail account required pam_faillock.so If the pam_faillock.so module is not present in the "/etc/pam.d/password-auth" file with the "preauth" line listed before pam_unix.so, this is a finding. If the system administrator (SA) can demonstrate that the required configuration is contained in a PAM configuration file included or substacked from the system-auth file, this is not a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-269152`

### Rule: AlmaLinux OS 9 must log username information when unsuccessful logon attempts occur.

**Rule ID:** `SV-269152r1050034_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing of these events, it may be harder or impossible to identify what an attacker did after an attack. Satisfies: SRG-OS-000021-GPOS-00005, SRG-OS-000470-GPOS-00214</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/etc/security/faillock.conf" file is configured to log username information when unsuccessful logon attempts occur with the following command: $ grep audit /etc/security/faillock.conf audit If the "audit" option is not set, is missing, or is commented out, this is a finding.

## Group: SRG-OS-000329-GPOS-00128

**Group ID:** `V-269153`

### Rule: AlmaLinux OS 9 must maintain an account lock until the locked account is manually released by an administrator; and not automatically after a set time.

**Rule ID:** `SV-269153r1050035_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 is configured to lock an account until released by an administrator after three unsuccessful logon attempts with the command: $ grep unlock_time /etc/security/faillock.conf unlock_time = 0 If the "unlock_time" option is not set to "0", the line is missing, or is commented out, this is a finding.

## Group: SRG-OS-000329-GPOS-00128

**Group ID:** `V-269154`

### Rule: AlmaLinux OS 9 must ensure account locks persist across reboots.

**Rule ID:** `SV-269154r1050036_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account. Having account locks persist across reboots ensures that a locked account is only unlocked by an administrator. If the locks did not persist across reboots, an attacker could reboot the system to continue brute force attacks against the accounts on the system. The default /var/run/faillock directory is cleared upon reboot and should not be used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/etc/security/faillock.conf" file is configured to use a nondefault faillock directory to ensure its contents persist after reboot with the following command: $ grep "dir =" /etc/security/faillock.conf dir = /var/log/faillock If the "dir" option is set to the default /var/run/faillock directory, is missing, or is commented out, this is a finding.

## Group: SRG-OS-000329-GPOS-00128

**Group ID:** `V-269155`

### Rule: AlmaLinux OS 9 must configure the appropriate SELinux context on the nondefault faillock tally directory.

**Rule ID:** `SV-269155r1050037_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account. Not having the correct SELinux context on the faillock directory may lead to unauthorized access to the directory meaning that accounts could be unlocked by a nonadministrator.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system does not have SELinux enabled and enforcing, a targeted policy, or if the pam_faillock module is not configured for use, this requirement is Not Applicable. Verify the location of the nondefault tally directory for the pam_faillock module with the following command: $ grep "dir =" /etc/security/faillock.conf dir = /var/log/faillock Check the security context type of the nondefault tally directory with the following command: $ ls -Zd /var/log/faillock system_u:object_r:faillog_t:s0 /var/log/faillock If the security context type of the nondefault tally directory is not "faillog_t", this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-269156`

### Rule: AlmaLinux OS 9 must prevent users from disabling the Standard Mandatory DOD Notice and Consent Banner for graphical user interfaces.

**Rule ID:** `SV-269156r1050038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." If a login banner is not displayed, it may be difficult to prosecute an attacker. Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify AlmaLinux OS 9 prevents a user from disabling the banner for graphical user interfaces. Determine if the operating system prevents modification of the GNOME banner setting with the following command: $ grep banner-message-enable /etc/dconf/db/local.d/locks/* banner-message-enable If "banner-message-enable" is commented out or is missing, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-269157`

### Rule: AlmaLinux OS 9 must display the Standard Mandatory DOD Notice and Consent Banner before granting local or remote access to the system via a graphical user logon.

**Rule ID:** `SV-269157r1050039_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." If a login banner is not displayed, it may be difficult to prosecute an attacker. Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify AlmaLinux OS 9 displays a banner before granting access to the operating system via a graphical user logon. First, identify the location of the banner message file with the following command: $ grep banner-message-text /etc/dconf/db/local.d/* /etc/dconf/db/local.d/01-banner-message Determine if the operating system displays a banner at the logon screen with the following command: $ gsettings get org.gnome.login-screen banner-message-enable true Next, check that file contains the correct wording with the following command (substituting the path from above): $ cat /etc/dconf/db/local.d/01-banner-message If the banner is set correctly it will return the following text: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the banner text does not match the Standard Mandatory DOD Notice and Consent Banner exactly, or the dconf database does not include the "banner-message-text" setting or if it is not enabled, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-269158`

### Rule: AlmaLinux OS 9 must display the Standard Mandatory DOD Notice and Consent Banner before granting local or remote access to the system via a command line user logon.

**Rule ID:** `SV-269158r1050040_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." If a login banner is not displayed, it may be difficult to prosecute an attacker. Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the operating system via a command line user logon. Check that a banner is displayed at the command line login screen with the following command: $ cat /etc/issue If the banner is set correctly it will return the following text: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the banner text does not match the Standard Mandatory DOD Notice and Consent Banner exactly, this is a finding.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-269159`

### Rule: AlmaLinux OS 9 must display the Standard Mandatory DOD Notice and Consent Banner before granting local or remote access to the system via an SSH user logon.

**Rule ID:** `SV-269159r1050041_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." If a login banner is not displayed, it may be difficult to prosecute an attacker. Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the operating system via a command line user logon. First, check that a banner text is correct with the following command: $ cat /etc/issue.net If the banner is set correctly it will return the following text: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Next, check that the OpenSSH server is configured to display the banner using the following command: $ sshd -T | grep banner banner /etc/issue.net If the banner text does not match the Standard Mandatory DOD Notice and Consent Banner exactly, or the SSH configuration does not include "Banner /etc/issue.net", this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-269160`

### Rule: AlmaLinux OS 9 must have the s-nail package installed.

**Rule ID:** `SV-269160r1050042_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "s-nail" package provides the mail command required to allow sending email notifications of unauthorized configuration changes to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 has the "s-nail" package is installed on the system with the following command: $ dnf list --installed s-nail s-nail.x86_64 14.9.22-6.el9 @AppStream If "s-nail" package is not installed, this is a finding.

## Group: SRG-OS-000364-GPOS-00151

**Group ID:** `V-269161`

### Rule: AlmaLinux OS 9 SSH daemon must not allow Generic Security Service Application Program Interface (GSSAPI) authentication.

**Rule ID:** `SV-269161r1050043_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>GSSAPI authentication is used to provide additional authentication mechanisms to applications. Allowing GSSAPI authentication through SSH exposes the system's GSSAPI to remote hosts, increasing the attack surface of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon does not allow GSSAPI authentication with the following command: $ /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*gssapiauthentication' gssapiauthentication no If the value is returned as "yes", the returned line is commented out, no output is returned, and the use of GSSAPI authentication has not been documented with the information system security officer (ISSO), this is a finding. If the required value is not set, this is a finding.

## Group: SRG-OS-000364-GPOS-00151

**Group ID:** `V-269162`

### Rule: AlmaLinux OS 9 SSH daemon must not allow Kerberos authentication.

**Rule ID:** `SV-269162r1050044_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kerberos authentication for SSH is often implemented using Generic Security Service Application Program Interface (GSSAPI). If Kerberos is enabled through SSH, the SSH daemon provides a means of access to the system's Kerberos implementation. Vulnerabilities in the system's Kerberos implementations may be subject to exploitation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon does not allow Kerberos authentication with the following command: $ /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*kerberosauthentication' kerberosauthentication no If the value is returned as "yes", the returned line is commented out, no output is returned, and the use of Kerberos authentication has not been documented with the information system security officer (ISSO), this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-269163`

### Rule: AlmaLinux OS 9 must check the GPG signature of software packages originating from external software repositories before installation.

**Rule ID:** `SV-269163r1050045_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. Accordingly, patches, service packs, device drivers, or operating system components must be signed with a certificate recognized and approved by the organization. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are not allowed by this requirement. The operating system should not have to verify the software again. This requirement does not mandate DOD certificates for this purpose; however, the certificate used to verify the software must be from an approved certificate authority (CA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that dnf always checks the GPG signature of software packages originating from external software repositories before installation: $ grep gpgcheck /etc/dnf/dnf.conf gpgcheck=1 If "gpgcheck" is not set to "1", or if the option is missing or commented out, ask the system administrator how the GPG signatures of software packages are verified. If there is no process to verify GPG signatures that is approved by the organization, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-269164`

### Rule: AlmaLinux OS 9 must ensure cryptographic verification of vendor software packages.

**Rule ID:** `SV-269164r1050046_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. Accordingly, patches, service packs, device drivers, or operating system components must be signed with a certificate recognized and approved by the organization. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are not allowed by this requirement. The operating system should not have to verify the software again. This requirement does not mandate DOD certificates for this purpose; however, the certificate used to verify the software must be from an approved certificate authority (CA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm AlmaLinux and TuxCare package-signing keys are installed on the system and verify their fingerprints match vendor values. The keys are stored as "RPM-GPG-KEY-AlmaLinux-9" and "RPM-GPG-KEY-TuxCare" inside the "/etc/pki/rpm-gpg/" directory. List GPG keys installed on the system using the following command: $ rpm -q --queryformat "%{SUMMARY}\n" gpg-pubkey TuxCare (Software Signing Key) <packager@tuxcare.com> public key AlmaLinux OS 9 <packager@almalinux.org> public key If the AlmaLinux and TuxCare GPG keys are not installed, this is a finding. List key fingerprints of installed GPG keys using the following commands: $ gpg -q --keyid-format short --with-fingerprint /etc/pki/rpm-gpg/RPM-GPG-KEY-AlmaLinux-9 pub rsa4096/B86B3716 2022-01-18 [SC] Key fingerprint = BF18 AC28 7617 8908 D6E7 1267 D36C B86C B86B 3716 uid AlmaLinux OS 9 <packager@almalinux.org> sub rsa4096/C9BA6CAA 2022-01-18 [E] $ gpg -q --keyid-format short --with-fingerprint /etc/pki/rpm-gpg/RPM-GPG-KEY-TuxCare pub rsa4096/8D50EB66 2023-03-06 [SC] Key fingerprint = FAD7 8590 81D0 738B 7A82 8496 D07B F2A0 8D50 EB66 uid TuxCare (Software Signing Key) <packager@tuxcare.com> sub rsa4096/A9C70659 2023-03-06 [E] If either "/etc/pki/rpm-gpg/RPM-GPG-KEY-AlmaLinux-9" or "/etc/pki/rpm-gpg/RPM-GPG-KEY-TuxCare" key files are missing, this is a finding. Compare key fingerprints of installed AlmaLinux and TuxCare GPG keys with fingerprints listed at https://almalinux.org/security/ https://docs.tuxcare.com/enterprise-support-for-almalinux/#gnupg-keys If the key fingerprints do not match, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-269165`

### Rule: AlmaLinux OS 9 must check the GPG signature of locally installed software packages before installation.

**Rule ID:** `SV-269165r1050047_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. Accordingly, patches, service packs, device drivers, or operating system components must be signed with a certificate recognized and approved by the organization. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. The operating system should not have to verify the software again. This requirement does not mandate DOD certificates for this purpose; however, the certificate used to verify the software must be from an approved certificate authority (CA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that dnf always checks the GPG signature of locally installed software packages before installation: $ grep localpkg_gpgcheck /etc/dnf/dnf.conf localpkg_gpgcheck=1 If "localpkg_gpgcheck" is not set to "1", or if the option is missing, or is commented out, ask the system administrator (SA) how the GPG signatures of local software packages are being verified. If there is no process to verify GPG signatures that is approved by the organization, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-269166`

### Rule: AlmaLinux OS 9 must check the GPG signature of repository metadata before package installation.

**Rule ID:** `SV-269166r1050048_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. Accordingly, patches, service packs, device drivers, or operating system components must be signed with a certificate recognized and approved by the organization. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. The operating system should not have to verify the software again. This requirement does not mandate DOD certificates for this purpose; however, the certificate used to verify the software must be from an approved certificate authority (CA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that dnf always checks the GPG signature of repository metadata: $ grep repo_gpgcheck /etc/dnf/dnf.conf /etc/yum.repos.d/*.repo repo_gpgcheck=1 If "repo_gpgcheck" is not set to "1" in the global "/etc/dnf/dnf.conf" file, or if the option is missing or commented out, this is a finding. If "repo_gpgcheck" is set to "0" in any of the "/etc/yum.repos.d/*.repo" files and the information system security officer (ISSO) lacks a documented requirement, this is a finding. Note: Not all repositories support this feature.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-269167`

### Rule: AlmaLinux OS 9 must have GPG signature verification enabled for all software repositories.

**Rule ID:** `SV-269167r1050049_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. Accordingly, patches, service packs, device drivers, or operating system components must be signed with a certificate recognized and approved by the organization. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. The operating system should not have to verify the software again. This requirement does not mandate DOD certificates for this purpose; however, the certificate used to verify the software must be from an approved certificate authority (CA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all software repositories defined in "/etc/yum.repos.d/" have been configured with "gpgcheck" enabled: $ grep gpgcheck /etc/yum.repos.d/*.repo /etc/yum.repos.d/tuxcare-fips.repo:gpgcheck=1 If "gpgcheck" is not set to "1" for all returned lines, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-269168`

### Rule: AlmaLinux OS 9 must prevent the loading of a new kernel for later execution.

**Rule ID:** `SV-269168r1050050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. Disabling kexec_load prevents an unsigned kernel image (that could be a windows kernel or modified vulnerable kernel) from being loaded. Kexec can be used subvert the entire secureboot process and should be avoided at all costs especially since it can load unsigned kernel images.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 is configured to disable kernel image loading. Check the status of the kernel.kexec_load_disabled kernel parameter with the following command: $ sysctl kernel.kexec_load_disabled kernel.kexec_load_disabled = 1 If "kernel.kexec_load_disabled" is not set to "1" or is missing, this is a finding. Check that the configuration files are present to enable this kernel parameter with the following command: $ /usr/lib/systemd/systemd-sysctl --cat-config | kernel.kexec_load_disabled kernel.kexec_load_disabled = 1 If "kernel.kexec_load_disabled" is not set to "1" or is missing, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-269169`

### Rule: AlmaLinux OS 9 system commands must be group-owned by root or a system account.

**Rule ID:** `SV-269169r1050051_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If AlmaLinux OS 9 allowed any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to AlmaLinux OS 9 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands contained in the following directories are group-owned by "root", or a required system account, with the following command: $ find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -group root -exec ls -l {} \; If any system commands are returned and is not group-owned by a required system account, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-269170`

### Rule: AlmaLinux OS 9 system commands must be owned by root.

**Rule ID:** `SV-269170r1050052_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If AlmaLinux OS 9 allowed any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to AlmaLinux OS 9 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands contained in the following directories are owned by "root" with the following command: $ find -L /bin /sbin /usr/bin /usr/sbin /usr/libexec /usr/local/bin /usr/local/sbin ! -user root -exec ls -l {} \; If any system commands are found to not be owned by root, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-269171`

### Rule: AlmaLinux OS 9 system commands must have mode 755 or less permissive.

**Rule ID:** `SV-269171r1050053_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If AlmaLinux OS 9 allowed any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to AlmaLinux OS 9 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands contained in the following directories have mode "755" or less permissive with the following command: $ find -L /bin /sbin /usr/bin /usr/sbin /usr/libexec /usr/local/bin /usr/local/sbin -perm /022 -exec ls -l {} \; If any system commands are found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-269172`

### Rule: AlmaLinux OS 9 library directories must be group-owned by root or a system account.

**Rule ID:** `SV-269172r1050054_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If AlmaLinux OS 9 allowed any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to AlmaLinux OS 9 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library directories are group-owned by "root" with the following command: $ find -L /lib /lib64 /usr/lib /usr/lib64 ! -group root -type d -exec stat -c "%n %G" '{}' \; If any systemwide shared library directory is returned and is not group owned by a required system account, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-269173`

### Rule: AlmaLinux OS 9 library directories must be owned by root.

**Rule ID:** `SV-269173r1050055_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If AlmaLinux OS 9 allowed any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to AlmaLinux OS 9 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library directories are owned by "root" with the following command: $ find -L /lib /lib64 /usr/lib /usr/lib64 ! -user root -type d -exec stat -c "%n %U" '{}' \; If any systemwide shared library directory is not owned by root, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-269174`

### Rule: AlmaLinux OS 9 library directories must have mode 755 or less permissive.

**Rule ID:** `SV-269174r1050056_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If AlmaLinux OS 9 allowed any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to AlmaLinux OS 9 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library directories have mode "755" or less permissive with the following command: $ find -L /lib /lib64 /usr/lib /usr/lib64 -perm /022 -type d -exec ls -l {} \; If any systemwide shared library file is found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-269175`

### Rule: AlmaLinux OS 9 library files must be group-owned by root or a system account.

**Rule ID:** `SV-269175r1101800_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If AlmaLinux OS 9 allowed any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to AlmaLinux OS 9 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and "/usr/lib64" are group owned by root with the following command: $ sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' ! -group root -exec stat -c "%n %G" {} + If any output is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-269176`

### Rule: AlmaLinux OS 9 library files must be owned by root.

**Rule ID:** `SV-269176r1101803_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If AlmaLinux OS 9 allowed any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to AlmaLinux OS 9 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and "/usr/lib64" are owned by root with the following command: $ sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' ! -user root -exec stat -c "%n %U" {} + If any output is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-269177`

### Rule: AlmaLinux OS 9 library files must have mode 755 or less permissive.

**Rule ID:** `SV-269177r1101806_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If AlmaLinux OS 9 allowed any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to AlmaLinux OS 9 with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs that execute with escalated privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and "/usr/lib64" have mode 0755 or less permissive. Check that the systemwide shared library files have mode 0755 or less permissive with the following command: $ sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' -perm /022 -exec stat -c "%n %a" {} + If any output is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269178`

### Rule: AlmaLinux OS 9 must disable core dumps for all users.

**Rule ID:** `SV-269178r1050060_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers or system operators trying to debug problems. Enabling core dumps on production systems is not recommended; however, there may be overriding operational requirements to enable advanced debugging. Permitting temporary enablement of core dumps during such situations must be reviewed through local needs and policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 disables core dumps for all users by issuing the following command: $ grep -s core /etc/security/limits.conf /etc/security/limits.d/*.conf /etc/security/limits.conf:# - core - limits the core file size (KB) /etc/security/limits.conf:#* soft core 0 This can be set as a global domain (with the * wildcard) but may be set differently for multiple domains. If the "core" item is missing, commented out, or the value is anything other than "0" and the need for core dumps is not documented with the information system security officer (ISSO) as an operational requirement for all domains that have the "core" item assigned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269179`

### Rule: AlmaLinux OS 9 must disable acquiring, saving, and processing core dumps.

**Rule ID:** `SV-269179r1050061_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers or system operators trying to debug problems. Enabling core dumps on production systems is not recommended; however, there may be overriding operational requirements to enable advanced debugging. Permitting temporary enablement of core dumps during such situations must be reviewed through local needs and policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 is not configured to acquire, save, or process core dumps with the following command: $ systemctl status systemd-coredump.socket systemd-coredump.socket Loaded: masked (Reason: Unit systemd-coredump.socket is masked.) Active: inactive (dead) since Mon 2024-02-26 13:31:02 UTC; 26s ago Duration: 3h 13min 22.428s If the "systemd-coredump.socket" is loaded and not masked and the need for core dumps is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269180`

### Rule: AlmaLinux OS 9 must disable storing core dumps.

**Rule ID:** `SV-269180r1050062_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers or system operators trying to debug problems. Enabling core dumps on production systems is not recommended; however, there may be overriding operational requirements to enable advanced debugging. Permitting temporary enablement of core dumps during such situations must be reviewed through local needs and policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 disables storing core dumps for all users by issuing the following command: $ systemd-analyze cat-config systemd/coredump.conf | grep Storage Storage=none If the "Storage" item is missing, commented out, or the value is anything other than "none" and the need for core dumps is not documented with the information system security officer (ISSO) as an operational requirement for all domains that have the "core" item assigned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269181`

### Rule: AlmaLinux OS 9 must disable core dump backtraces.

**Rule ID:** `SV-269181r1050063_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers or system operators trying to debug problems. Enabling core dumps on production systems is not recommended; however, there may be overriding operational requirements to enable advanced debugging. Permitting temporary enablement of core dumps during such situations must be reviewed through local needs and policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 disables core dump backtraces by issuing the following command: $ systemd-analyze cat-config systemd/coredump.conf | grep ProcessSizeMax ProcessSizeMax=0 If the "ProcessSizeMax" item is missing, commented out, or the value is anything other than "0" and the need for core dumps is not documented with the information system security officer (ISSO) as an operational requirement for all domains that have the "core" item assigned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269182`

### Rule: AlmaLinux OS 9 must disable the kernel.core_pattern.

**Rule ID:** `SV-269182r1050064_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers trying to debug problems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 disables storing core dumps with the following commands: $ sysctl kernel.core_pattern kernel.core_pattern = |/bin/false If the returned line does not have a value of "|/bin/false", or a line is not returned and the need for core dumps is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding. Check that the configuration files are present to disable core dump storage. $ /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F kernel.core_pattern | tail -1 kernel.core_pattern = |/bin/false If "kernel.core_pattern" is not set to "|/bin/false" and is not documented with the ISSO as an operational requirement, or is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269183`

### Rule: AlmaLinux OS 9 cron configuration files directory must be group-owned by root.

**Rule ID:** `SV-269183r1050065_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Service configuration files enable or disable features of their respective services that if configured incorrectly can lead to insecure and vulnerable configurations; therefore, service configuration files must be owned by the correct group to prevent unauthorized changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the group ownership of all cron configuration files with the following command: $ stat -c "%G %n" /etc/cron* root /etc/cron.d root /etc/cron.daily root /etc/cron.deny root /etc/cron.hourly root /etc/cron.monthly root /etc/crontab root /etc/cron.weekly If any crontab is not group owned by root, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269184`

### Rule: AlmaLinux OS 9 cron configuration files directory must be owned by root.

**Rule ID:** `SV-269184r1050066_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Service configuration files enable or disable features of their respective services that if configured incorrectly can lead to insecure and vulnerable configurations; therefore, service configuration files must be owned by the correct group to prevent unauthorized changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ownership of all cron configuration files with the command: $ stat -c "%U %n" /etc/cron* root /etc/cron.d root /etc/cron.daily root /etc/cron.deny root /etc/cron.hourly root /etc/cron.monthly root /etc/crontab root /etc/cron.weekly If any crontab is not owned by root, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269185`

### Rule: AlmaLinux OS 9 cron configuration directories must have a mode of 0700 or less permissive.

**Rule ID:** `SV-269185r1050067_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Service configuration files enable or disable features of their respective services that if configured incorrectly can lead to insecure and vulnerable configurations. Therefore, service configuration files should have the correct access rights to prevent unauthorized changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the permissions of the cron directories with the following command: $ find /etc/cron* -type d | xargs stat -c "%#a %n" 0700 /etc/cron.d 0700 /etc/cron.daily 0700 /etc/cron.hourly 0700 /etc/cron.monthly 0700 /etc/cron.weekly If any cron configuration directory is more permissive than "700", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269186`

### Rule: AlmaLinux OS 9 /etc/crontab file must have mode 0600.

**Rule ID:** `SV-269186r1050068_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Service configuration files enable or disable features of their respective services that if configured incorrectly can lead to insecure and vulnerable configurations; therefore, service configuration files must have the correct access rights to prevent unauthorized changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the permissions of /etc/crontab with the following command: $ stat -c "%#a %n" /etc/crontab 0600 If /etc/crontab does not have a mode of "0600", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269187`

### Rule: AlmaLinux OS 9 must disable the ability of a user to accidentally press Ctrl-Alt-Del and cause a system to shut down or reboot.

**Rule ID:** `SV-269187r1050069_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A locally logged-in user who presses Ctrl-Alt-Del, when at the console, can reboot the system. If accidentally pressed, as could happen in the case of mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the AlmaLinux OS 9 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify AlmaLinux OS 9 is configured to ignore the Ctrl-Alt-Del sequence in the GNOME desktop with the following command: $ gsettings get org.gnome.settings-daemon.plugins.media-keys logout "['']" If the GNOME desktop is configured to shut down when Ctrl-Alt-Del is pressed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269188`

### Rule: AlmaLinux OS 9 must prevent a user from overriding the Ctrl-Alt-Del sequence settings for the graphical user interface.

**Rule ID:** `SV-269188r1050070_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A locally logged-in user who presses Ctrl-Alt-Del, when at the console, can reboot the system. If accidentally pressed, as could happen in the case of mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the AlmaLinux OS 9 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify that users cannot enable the Ctrl-Alt-Del sequence in the GNOME desktop with the following command: $ grep logout /etc/dconf/db/local.d/locks/* /org/gnome/settings-daemon/plugins/media-keys/logout If the output is not "/org/gnome/settings-daemon/plugins/media-keys/logout", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269189`

### Rule: All AlmaLinux OS 9 local files and directories must have a valid group owner.

**Rule ID:** `SV-269189r1050071_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Files without a valid group owner may be unintentionally inherited if a group is assigned the same Group Identifier (GID) as the GID of the files without a valid group owner.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all local files and directories on AlmaLinux OS 9 have a valid group with the following command: $ df --local -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -nogroup If any files on the system do not have an assigned group, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269190`

### Rule: All AlmaLinux OS 9 local files and directories must have a valid owner.

**Rule ID:** `SV-269190r1050072_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unowned files and directories may be unintentionally inherited if a user is assigned the same user identifier "UID" as the UID of the unowned files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all local files and directories on AlmaLinux OS 9 have a valid owner with the following command: $ df --local -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -nouser If any files on the system do not have an assigned owner, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269191`

### Rule: AlmaLinux OS 9 /etc/group- file must be group owned by root.

**Rule ID:** `SV-269191r1050073_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/group-" file is a backup file of "/etc/group", and as such, contains information regarding groups that are configured on the system. Protection of this file is important for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the group ownership of the "/etc/group-" file with the following command: $ stat -c "%G %n" /etc/group- root /etc/group- If "/etc/group-" file does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269192`

### Rule: AlmaLinux OS 9 /etc/group- file must be owned by root.

**Rule ID:** `SV-269192r1050074_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/group-" file is a backup file of "/etc/group", and as such, contains information regarding groups that are configured on the system. Protection of this file is important for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ownership of the "/etc/group-" file with the following command: $ stat -c "%U %n" /etc/group- root /etc/group- If "/etc/group-" file does not have an owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269193`

### Rule: AlmaLinux OS 9 /etc/group- file must have mode 0644 or less permissive to prevent unauthorized access.

**Rule ID:** `SV-269193r1050075_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/group-" file is a backup file of "/etc/group", and as such, contains information regarding groups that are configured on the system. Protection of this file is important for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "/etc/group-" file has mode "0644" or less permissive with the following command: $ stat -c "%#a %n" /etc/group- 0644 /etc/group- If a value of "0644" or less permissive is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269194`

### Rule: AlmaLinux OS 9 /etc/group file must be group owned by root.

**Rule ID:** `SV-269194r1050076_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/group" file contains information regarding groups that are configured on the system. Protection of this file is important for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the group ownership of the "/etc/group" file with the following command: $ stat -c "%G %n" /etc/group root /etc/group If "/etc/group" file does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269195`

### Rule: AlmaLinux OS 9 /etc/group file must be owned by root.

**Rule ID:** `SV-269195r1050077_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/group" file contains information regarding groups that are configured on the system. Protection of this file is important for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ownership of the "/etc/group" file with the following command: $ stat -c "%U %n" /etc/group root /etc/group If "/etc/group" file does not have an owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269196`

### Rule: AlmaLinux OS 9 /etc/group file must have mode 0644 or less permissive to prevent unauthorized access.

**Rule ID:** `SV-269196r1050078_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/group" file contains information regarding groups that are configured on the system. Protection of this file is important for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "/etc/group" file has mode "0644" or less permissive with the following command: $ stat -c "%#a %n" /etc/group 0644 /etc/group If a value of "0644" or less permissive is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269197`

### Rule: The /boot/grub2/grub.cfg file must be group-owned by root.

**Rule ID:** `SV-269197r1050079_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "root" group is a highly privileged group. Furthermore, the group-owner of this file should not have any access privileges anyway.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the group ownership of the "/boot/grub2/grub.cfg" file with the following command: $ stat -c "%G %n" /boot/grub2/grub.cfg root /boot/grub2/grub.cfg If "/boot/grub2/grub.cfg" file does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269198`

### Rule: The /boot/grub2/grub.cfg file must be owned by root.

**Rule ID:** `SV-269198r1050779_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/boot/grub2/grub.cfg" file stores sensitive system configuration. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ownership of the "/boot/grub2/grub.cfg" file with the following command: $ stat -c "%U %n" /boot/grub2/grub.cfg root /boot/grub2/grub.cfg If "/boot/grub2/grub.cfg" file does not have an owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269199`

### Rule: AlmaLinux OS 9 must disable the ability of systemd to spawn an interactive boot process.

**Rule ID:** `SV-269199r1050081_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using interactive or recovery boot, the console user could disable auditing, firewalls, or other services, weakening system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that GRUB 2 is configured to disable interactive boot. Check that the current GRUB 2 configuration disables the ability of systemd to spawn an interactive boot process with the following command: $ grubby --info=ALL | grep args | grep 'systemd.confirm_spawn' If any output is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269200`

### Rule: AlmaLinux OS 9 /etc/gshadow- file must be group-owned by root.

**Rule ID:** `SV-269200r1050082_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/gshadow-" file is a backup of "/etc/gshadow", and as such, contains group password hashes. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the group ownership of the "/etc/gshadow-" file with the following command: $ stat -c "%G %n" /etc/gshadow- root /etc/gshadow- If "/etc/gshadow-" file does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269201`

### Rule: AlmaLinux OS 9 /etc/gshadow- file must be owned by root.

**Rule ID:** `SV-269201r1050083_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/gshadow-" file is a backup of "/etc/gshadow", and as such, contains group password hashes. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ownership of the "/etc/gshadow-" file with the following command: $ stat -c "%U %n" /etc/gshadow- root /etc/gshadow- If "/etc/gshadow-" file does not have an owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269202`

### Rule: AlmaLinux OS 9 /etc/gshadow- file must have mode 0000 or less permissive to prevent unauthorized access.

**Rule ID:** `SV-269202r1050084_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/gshadow-" file is a backup of "/etc/gshadow", and as such, contains group password hashes. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "/etc/gshadow-" file has mode "0000" with the following command: $ stat -c "%a %n" /etc/gshadow- 0 /etc/gshadow- If a value of "0" is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269203`

### Rule: AlmaLinux OS 9 /etc/gshadow file must be group-owned by root.

**Rule ID:** `SV-269203r1050085_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/gshadow" file contains group password hashes. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the group ownership of the "/etc/gshadow" file with the following command: $ stat -c "%G %n" /etc/gshadow root /etc/gshadow If "/etc/gshadow" file does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269204`

### Rule: AlmaLinux OS 9 /etc/gshadow file must be owned by root.

**Rule ID:** `SV-269204r1050086_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/gshadow" file contains group password hashes. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ownership of the "/etc/gshadow" file with the following command: $ stat -c "%U %n" /etc/gshadow root /etc/gshadow If "/etc/gshadow" file does not have an owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269205`

### Rule: AlmaLinux OS 9 /etc/gshadow file must have mode 0000 or less permissive to prevent unauthorized access.

**Rule ID:** `SV-269205r1050087_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/gshadow" file contains group password hashes. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "/etc/gshadow" file has mode "0000" with the following command: $ stat -c "%a %n" /etc/gshadow 0 /etc/gshadow If a value of "0" is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269206`

### Rule: The graphical display manager must not be the default target on AlmaLinux OS 9 unless approved.


**Rule ID:** `SV-269206r1050088_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unnecessary service packages must not be installed to decrease the attack surface of the system. Graphical display managers have a long history of security vulnerabilities and must not be used, unless approved and documented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to boot to the command line: $ systemctl get-default multi-user.target If the system default target is not set to "multi-user.target" and the information system security officer (ISSO) lacks a documented requirement for a graphical user interface, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269207`

### Rule: AlmaLinux OS 9 must disable the user list at logon for graphical user interfaces.

**Rule ID:** `SV-269207r1050089_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Leaving the user list enabled is a security risk since it allows anyone with physical access to the system to enumerate known user accounts without authenticated access to the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 disables the user logon list for graphical user interfaces with the following command: Note: This requirement assumes the use of the AlmaLinux OS 9 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. $ gsettings get org.gnome.login-screen disable-user-list true If the setting is "false", this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-269208`

### Rule: All AlmaLinux OS 9 local interactive user accounts must be assigned a home directory upon creation.

**Rule ID:** `SV-269208r1050090_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If local interactive users are not assigned a valid home directory, there is no place for the storage and control of files they should own.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all local interactive users on AlmaLinux OS 9 are assigned a home directory upon creation with the following command: $ grep CREATE_HOME /etc/login.defs CREATE_HOME yes If the value for "CREATE_HOME" parameter is not set to "yes", the line is missing, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-269209`

### Rule: All AlmaLinux OS 9 local interactive user home directories defined in the /etc/passwd file must exist.

**Rule ID:** `SV-269209r1050091_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a local interactive user has a home directory defined that does not exist, the user may be given access to the / directory as the current working directory upon logon. This could create a denial of service because the user would not be able to access their logon configuration files, and it may give them visibility to system files they normally would not be able to access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the assigned home directories of all interactive users on the system exist with the following command: $ pwck -r user 'testdupe': directory '/home/testdupe' does not exist The output should not return any interactive users. If users home directory does not exist, this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-269210`

### Rule: All AlmaLinux OS 9 local interactive user home directories must be group-owned by the home directory owner's primary group.

**Rule ID:** `SV-269210r1050092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Group Identifier (GID) of a local interactive users home directory is not the same as the primary GID of the user, this would allow unauthorized access to the users files, and users that share the same group may not be able to access files that they legitimately should.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the assigned home directory of all local interactive users is group-owned by that user's primary GID with the following command: Note: This may miss local interactive users that have been assigned a privileged UID. Evidence of interactive use may be obtained from a number of log files containing system logon information. The returned directory "/home/test" is used as an example. $ stat --format="%n: GID=%g (%G), UID=%u (%U), MODE=%0.4a" $(awk -F: '($3>=1000)&&($7 !~ /nologin/){print $6}' /etc/passwd) /home/test: GID=1001 (test), UID=1001 (test), MODE=0700 Check the user's primary group with the following command: $ grep $(grep -E '^test:' /etc/passwd | awk -F: '{print $4}') /etc/group test:x:1001: If the user home directory referenced in "/etc/passwd" is not group-owned by that user's primary GID (1001 in the above example) this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-269211`

### Rule: AlmaLinux OS 9 must prevent code from being executed on file systems that contain user home directories.

**Rule ID:** `SV-269211r1050093_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/home" is mounted with the "noexec" option with the following command: Note: If a separate file system has not been created for the user home directories (user home directories are mounted under "/"), this is automatically a finding, as the "noexec" option cannot be used on the "/" system. $ mount | grep /home /dev/mapper/luks-10a20c46-483d-4d12-831f-5328eda18fd1 on /home type xfs (rw,noexec,nosuid,nodev,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota) If the "/home" file system is mounted without the "noexec" option, this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-269212`

### Rule: A separate file system must be used for user home directories (such as /home or an equivalent).

**Rule ID:** `SV-269212r1050094_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensuring that "/home" is mounted on its own partition enables the setting of more restrictive mount options, and also helps ensure that users cannot trivially fill partitions used for log or audit data storage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a separate file system/partition has been created for "/home" with the following command: $ mount | grep /home /dev/mapper/luks-10a20c46-483d-4d12-831f-5328eda18fd1 on /home type xfs (rw,nosuid,nodev,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota) If a separate entry for "/home" is not in use, this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-269213`

### Rule: All AlmaLinux OS 9 local interactive users must have a home directory assigned in the /etc/passwd file.

**Rule ID:** `SV-269213r1050095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If local interactive users are not assigned a valid home directory, there is no place for the storage and control of files they should own.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that interactive users on the system have a home directory assigned with the following command: $ awk -F: '($3>=1000)&&($7 !~ /nologin/){print $1, $6}' /etc/passwd simon /home/simon test /home/test testdupe /home/testdupe Inspect the output and verify that all interactive users (normally users with a UID greater that 1000) have a home directory defined. If users home directory is not defined, this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-269214`

### Rule: Executable search paths within the initialization files of all local interactive AlmaLinux OS 9 users must only contain paths that resolve to the system default or the users home directory.

**Rule ID:** `SV-269214r1050096_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The executable search path (typically the $PATH environment variable) contains a list of directories for the shell to search to find executables. If this path includes the current working directory (other than the users home directory), executables in these directories may be executed instead of system commands. This variable is formatted as a colon-separated list of directories. If there is an empty entry, such as a leading or trailing colon or two consecutive colons, this is interpreted as the current working directory. If deviations from the default system search path for the local interactive user are required, they must be documented with the information system security officer (ISSO).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all local interactive user initialization file executable search path statements do not contain statements that will reference a working directory other than user home directories with the following commands: $ grep -i path= /home/*/.* grep -i path= /home/*/.* 2>/dev/null /home/simon/.bashrc: PATH="$HOME/.local/bin:$HOME/bin:$PATH" /home/test/.bashrc: PATH="$HOME/.local/bin:$HOME/bin:$PATH" If any local interactive user initialization files have executable search path statements that include directories outside of their home directory and is not documented with the ISSO as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-269215`

### Rule: All AlmaLinux OS 9 local interactive user home directories must have mode 0750 or less permissive.

**Rule ID:** `SV-269215r1050097_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on local interactive user home directories may allow unauthorized access to user files by other users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This may miss interactive users that have been assigned a privileged user identifier (UID). Evidence of interactive use may be obtained from a number of log files containing system logon information. Verify the assigned home directory of all local interactive users has a mode of "0750" or less permissive with the following command: $ ls -ld $(awk -F: '($3>=1000)&&($7 !~ /nologin/){print $6}' /etc/passwd) drwx------. 2 simon simon 83 Nov 30 12:30 /home/simon drwx------. 2 test test 83 Jan 19 14:18 /home/test drwx------. 2 test testdupe 62 Jan 15 11:44 /home/testdupe If home directories referenced in "/etc/passwd" do not have a mode of "0750" or less permissive, this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-269216`

### Rule: AlmaLinux OS 9 must not allow unattended or automatic logon via the graphical user interface.

**Rule ID:** `SV-269216r1050098_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Failure to restrict system access to authenticated users negatively impacts operating system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the AlmaLinux OS 9 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify AlmaLinux OS 9 does not allow an unattended or automatic logon to the system via a graphical user interface. Check for the value of the "AutomaticLoginEnable" in the "/etc/gdm/custom.conf" file with the following command: $ grep -i automaticlogin /etc/gdm/custom.conf [daemon] AutomaticLoginEnable=false If the value of "AutomaticLoginEnable" is not set to "false", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269217`

### Rule: AlmaLinux OS 9 must enforce a delay of at least four seconds between logon prompts following a failed logon attempt.

**Rule ID:** `SV-269217r1050099_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Increasing the time between a failed authentication attempt and prompting to re-enter credentials helps to slow a single-threaded brute force attack. Satisfies: SRG-OS-000480-GPOS-00227, SRG-OS-000480-GPOS-00226</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 enforces a delay of at least four seconds between console logon prompts following a failed logon attempt with the following command: $ grep -i fail_delay /etc/login.defs FAIL_DELAY 4 If the value of "FAIL_DELAY" is not set to "4" or greater, or the line is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269218`

### Rule: AlmaLinux OS 9 must not allow blank or null passwords.

**Rule ID:** `SV-269218r1050100_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log in and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that null passwords cannot be used with the following command: $ grep -i nullok /etc/pam.d/system-auth /etc/pam.d/password-auth If output is produced, this is a finding. If the system administrator (SA) can demonstrate that the required configuration is contained in a PAM configuration file included or substacked from the system-auth file, this is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269219`

### Rule: AlmaLinux OS 9 must not have accounts configured with blank or null passwords.

**Rule ID:** `SV-269219r1050101_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log in and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that null or blank passwords cannot be used with the following command: $ awk -F: '!$2 {print $1}' /etc/shadow If the command returns any results, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269220`

### Rule: AlmaLinux OS 9 /etc/passwd- file must be group-owned by root.

**Rule ID:** `SV-269220r1050102_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/passwd-" file is a backup file of "/etc/passwd", and as such, contains information about the users that are configured on the system. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the group ownership of the "/etc/passwd-" file with the following command: $ stat -c "%G %n" /etc/passwd- root /etc/passwd- If "/etc/passwd-" file does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269221`

### Rule: AlmaLinux OS 9 /etc/passwd- file must be owned by root.

**Rule ID:** `SV-269221r1050103_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/passwd-" file is a backup file of "/etc/passwd", and as such, contains information about the users that are configured on the system. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ownership of the "/etc/passwd-" file with the following command: $ stat -c "%U %n" /etc/passwd- root /etc/passwd- If "/etc/passwd-" file does not have an owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269222`

### Rule: AlmaLinux OS 9 /etc/passwd- file must have mode 0644 or less permissive to prevent unauthorized access.

**Rule ID:** `SV-269222r1050104_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/passwd-" file is a backup file of "/etc/passwd", and as such, contains information about the users that are configured on the system. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "/etc/passwd-" file has mode "0644" or less permissive with the following command: $ stat -c "%#a %n" /etc/passwd- 0644 /etc/passwd- If a value of "0644" or less permissive is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269223`

### Rule: AlmaLinux OS 9 /etc/passwd file must be group-owned by root.

**Rule ID:** `SV-269223r1050105_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/passwd" file contains information about the users that are configured on the system. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the group ownership of the "/etc/passwd" file with the following command: $ stat -c "%G %n" /etc/passwd root /etc/passwd If "/etc/passwd" file does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269224`

### Rule: AlmaLinux OS 9 /etc/passwd file must be owned by root.

**Rule ID:** `SV-269224r1050106_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/passwd" file contains information about the users that are configured on the system. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ownership of the "/etc/passwd" file with the following command: $ stat -c "%U %n" /etc/passwd root /etc/passwd If "/etc/passwd" file does not have an owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269225`

### Rule: AlmaLinux OS 9 /etc/passwd file must have mode 0644 or less permissive to prevent unauthorized access.

**Rule ID:** `SV-269225r1050107_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the "/etc/passwd" file is writable by a group-owner or the world the risk of its compromise is increased. The file contains the list of accounts on the system and associated information, and protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "/etc/passwd" file has mode "0644" or less permissive with the following command: $ stat -c "%#a %n" /etc/passwd 0644 /etc/passwd If a value of "0644" or less permissive is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269226`

### Rule: AlmaLinux OS 9 /etc/shadow- file must be group-owned by root.

**Rule ID:** `SV-269226r1050108_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/shadow-" file is a backup file of "/etc/shadow", and as such, contains the list of local system accounts and password hashes. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the group ownership of the "/etc/shadow-" file with the following command: $ stat -c "%G %n" /etc/shadow- root /etc/shadow- If "/etc/shadow-" file does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269227`

### Rule: AlmaLinux OS 9 /etc/shadow- file must be owned by root.

**Rule ID:** `SV-269227r1050109_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/shadow-" file is a backup file of "/etc/shadow", and as such, contains the list of local system accounts and password hashes. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ownership of the "/etc/shadow-" file with the following command: $ stat -c "%U %n" /etc/shadow- root /etc/shadow- If "/etc/shadow-" file does not have an owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269228`

### Rule: AlmaLinux OS 9 /etc/shadow- file must have mode 0000 or less permissive to prevent unauthorized access.

**Rule ID:** `SV-269228r1050110_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/shadow-" file is a backup file of "/etc/shadow", and as such, contains the list of local system accounts and password hashes. Protection of this file is critical for system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "/etc/shadow-" file has mode "0000" with the following command: $ stat -c "%a %n" /etc/shadow- 0 /etc/shadow- If a value of "0" is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269229`

### Rule: AlmaLinux OS 9 /etc/shadow file must be group-owned by root.

**Rule ID:** `SV-269229r1050111_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/shadow" file contains the list of local system accounts and stores password hashes. Protection of this file is critical for system security. Failure to give ownership of this file to root provides the designated owner with access to sensitive information, which could weaken the system security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the group ownership of the "/etc/shadow" file with the following command: $ stat -c "%G %n" /etc/shadow root /etc/shadow If "/etc/shadow" file does not have a group owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269230`

### Rule: AlmaLinux OS 9 /etc/shadow file must be owned by root.

**Rule ID:** `SV-269230r1050112_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/shadow" file contains the list of local system accounts and stores password hashes. Protection of this file is critical for system security. Failure to give ownership of this file to root provides the designated owner with access to sensitive information, which could weaken the system security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ownership of the "/etc/shadow" file with the following command: $ stat -c "%U %n" /etc/shadow root /etc/shadow If "/etc/shadow" file does not have an owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269231`

### Rule: AlmaLinux OS 9 /etc/shadow file must have mode 0000 to prevent unauthorized access.

**Rule ID:** `SV-269231r1050113_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/etc/shadow" file contains the list of local system accounts and stores password hashes. Protection of this file is critical for system security. Failure to give ownership of this file to root provides the designated owner with access to sensitive information, which could weaken the system security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "/etc/shadow" file has mode "0000" with the following command: $ stat -c "%a %n" /etc/shadow 0 /etc/shadow If a value of "0" is not returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269232`

### Rule: AlmaLinux OS 9 must restrict privilege elevation to authorized personnel.

**Rule ID:** `SV-269232r1101826_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the "sudoers" file is not configured correctly, any user defined on the system can initiate privileged actions on the target system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 restricts privilege elevation to authorized personnel with the following command: $ sudo grep -iwR 'ALL' /etc/sudoers /etc/sudoers.d/ | grep -v '#' /etc/sudoers:root ALL=(ALL) ALL /etc/sudoers:%wheel ALL=(ALL) NOPASSWD: ALL If the either of the following entries are returned, including their NOPASSWD equivalents, this is a finding: ALL ALL=(ALL) ALL ALL ALL=(ALL:ALL) ALL

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269233`

### Rule: AlmaLinux OS 9 must use the invoking user's password for privilege escalation when using "sudo".

**Rule ID:** `SV-269233r1050115_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the rootpw, targetpw, or runaspw flags are defined and not disabled, by default the operating system will prompt the invoking user for the "root" user password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the sudoers security policy is configured to use the invoking user's password for privilege escalation with the following command: $ grep -E '(!rootpw|!targetpw|!runaspw)' /etc/sudoers /etc/sudoers.d/* | grep -v '#' /etc/sudoers.d/01_stig:Defaults !targetpw /etc/sudoers.d/01_stig:Defaults !rootpw /etc/sudoers.d/01_stig:Defaults !runaspw If no results are returned, this is a finding. If results are returned from more than one file location, this is a finding. If "Defaults !targetpw" is not defined, this is a finding. If "Defaults !rootpw" is not defined, this is a finding. If "Defaults !runaspw" is not defined, this is a finding.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-269234`

### Rule: AlmaLinux OS 9 must set the umask value to 077 for all local interactive user accounts.

**Rule ID:** `SV-269234r1050116_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the most restrictive default permissions ensures that when new accounts are created they do not have unnecessary access. With a UMASK of 077, files will be created with 0600 permissions (owner read/write only) and directories will have 0700 permissions (owner read/write/execute only).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the default umask for all local interactive users is "077". Identify the locations of all local interactive user home directories by looking at the "/etc/passwd" file. Check all local interactive user initialization files for interactive users with the following command: Note: The example is for a system that is configured to create users home directories in the "/home" directory. $ grep -ir umask /home | grep -v '.bash_history' If any local interactive user initialization files are found to have a umask statement that sets a value less restrictive than "077", this is a finding.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-269235`

### Rule: AlmaLinux OS 9 must define default permissions for all authenticated users in such a way that the user can only read and modify their own files.

**Rule ID:** `SV-269235r1050117_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the most restrictive default permissions ensures that when new accounts are created they do not have unnecessary access. With a UMASK of 077, files will be created with 0600 permissions (owner read/write only) and directories will have 0700 permissions (owner read/write/execute only).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 defines default permissions for all authenticated users in such a way that the user can only read and modify their own files with the following command: Note: If the value of the "UMASK" parameter is set to "000" in the "/etc/login.defs" file, the severity is raised to a CAT I. $ grep UMASK /etc/login.defs UMASK 077 If the value for the "UMASK" parameter is not "077", or the "UMASK" parameter is missing or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-269236`

### Rule: AlmaLinux OS 9 must define default permissions for PAM users.

**Rule ID:** `SV-269236r1050118_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the most restrictive default permissions ensures that when new accounts are created they do not have unnecessary access. With a UMASK of 077, files will be created with 0600 permissions (owner read/write only) and directories will have 0700 permissions (owner read/write/execute only).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "pam_umask" module is enabled with the following command: $ grep -i umask /etc/pam.d/* /etc/pam.d/postlogin:session optional pam_umask.so silent umask=0022 If a "pam_umask.so" line is not returned, this is a finding. If the "umask" setting is set to anything other than "0077", this is a finding. Note: If the "umask" setting is not found, it will use the default UMASK entry in /etc/login.defs.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-269237`

### Rule: AlmaLinux OS 9 must define default permissions for logon and nonlogon shells.

**Rule ID:** `SV-269237r1050119_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the most restrictive default permissions ensures that when new accounts are created they do not have unnecessary access. With a UMASK of 077, files will be created with 0600 permissions (owner read/write only) and directories will have 0700 permissions (owner read/write/execute only).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "umask" setting for installed shells is "077". Note: If the value of the "umask" parameter is set to "000", the severity is raised to a CAT I. $ grep -ir umask /etc/profile* /etc/bashrc* /etc/csh* /etc/csh.cshrc: umask 077 If the "umask" parameter is set to anything other than "077", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269238`

### Rule: AlmaLinux OS 9 must not have unauthorized accounts.

**Rule ID:** `SV-269238r1050120_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accounts providing no operational purpose provide additional opportunities for system compromise. Unnecessary accounts include user accounts for individuals not requiring access to the system and application accounts for applications not installed on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that there are no unauthorized interactive user accounts with the following command: $ cat /etc/passwd root:x:0:0:root:/root:/bin/bash ... sync:x:5:0:sync:/sbin:/bin/sync shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown halt:x:7:0:halt:/sbin:/sbin/halt simon:x:1000:1000::/home/simon:/bin/bash Interactive user accounts, generally will have a user identifier (UID) of 1000 or greater, a home directory in a specific partition, and an interactive shell. Obtain the list of interactive user accounts authorized to be on the system from the system administrator or information system security officer (ISSO) and compare it to the list of local interactive user accounts on the system. If there are unauthorized local user accounts on the system, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269239`

### Rule: AlmaLinux OS 9 must be configured so that the file integrity tool verifies Access Control Lists (ACLs).

**Rule ID:** `SV-269239r1050121_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ACLs can provide permissions beyond those permitted through the file mode and must be verified by the file integrity tools.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that that AIDE is verifying ACLs with the following command: $ grep acl /etc/aide.conf All= p+i+n+u+g+s+m+S+sha512+acl+xattrs+selinux If the "acl" rule is not being used on all uncommented selection lines in the "/etc/aide.conf" file, or ACLs are not being checked by another file integrity tool, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269240`

### Rule: AlmaLinux OS 9 must use a file integrity tool that is configured to use FIPS 140-3-approved cryptographic hashes for validating file contents and directories.

**Rule ID:** `SV-269240r1050122_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>File integrity tools use cryptographic hashes for verifying file contents and directories have not been altered. These hashes must be FIPS 140-3 approved cryptographic hashes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AIDE is configured to use FIPS 140-3 file hashing with the following command: $ grep sha512 /etc/aide.conf All=p+i+n+u+g+s+m+S+sha512+acl+xattrs+selinux If the "sha512" rule is not being used on all uncommented selection lines in the "/etc/aide.conf" file, or another file integrity tool is not using FIPS 140-3-approved cryptographic hashes for validating file contents and directories, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269241`

### Rule: AlmaLinux OS 9 must be configured so that the file integrity tool verifies extended attributes.

**Rule ID:** `SV-269241r1050123_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Extended attributes in file systems are used to contain arbitrary data and file metadata with security implications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AIDE is configured to verify extended attributes with the following command: $ grep xattrs /etc/aide.conf All= p+i+n+u+g+s+m+S+sha512+acl+xattrs+selinux If the "xattrs" rule is not being used on all uncommented selection lines in the "/etc/aide.conf" file, or extended attributes are not being checked by another file integrity tool, this is a finding. If the "acl" rule is not being used on all uncommented selection lines in the "/etc/aide.conf" file, or ACLs are not being checked by another file integrity tool, this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-269242`

### Rule: AlmaLinux OS 9 must prevent the use of dictionary words for passwords.

**Rule ID:** `SV-269242r1050124_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 prevents the use of dictionary words for passwords with the following command: $ grep -r dictcheck /etc/security/pwquality.conf* /etc/security/pwquality.conf.d/stig.conf:dictcheck = 1 If the value of "dictcheck" is not "1" , is not set, is commented out, or if conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269243`

### Rule: AlmaLinux OS 9 must not accept router advertisements on all IPv6 interfaces.

**Rule ID:** `SV-269243r1050125_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An illicit router advertisement message could result in a man-in-the-middle attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If IPv6 is disabled on the system, this requirement is Not Applicable. Verify AlmaLinux OS 9 does not accept router advertisements on any IPv6 interfaces, unless the system is a router. Determine if router advertisements are not accepted by using the following command: $ sysctl -a | grep 'accept_ra ' net.ipv6.conf.all.accept_ra = 1 net.ipv6.conf.default.accept_ra = 1 net.ipv6.conf.enp1s0.accept_ra = 0 net.ipv6.conf.lo.accept_ra = 1 If any of the returned lines are not set to "0" and it is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269244`

### Rule: AlmaLinux OS 9 must ignore Internet Control Message Protocol (ICMP) redirect messages.

**Rule ID:** `SV-269244r1050126_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP redirect message could result in a man-in-the-middle attack. This feature of the IP protocol has few legitimate uses. It should be disabled unless absolutely required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 will not accept ICMP redirect messages. Check the value of the "accept_redirects" variables with the following command: $ sysctl -a | grep accept_redirects net.ipv4.conf.all.accept_redirects = 0 net.ipv4.conf.default.accept_redirects = 0 net.ipv4.conf.enp1s0.accept_redirects = 0 net.ipv4.conf.lo.accept_redirects = 0 net.ipv6.conf.all.accept_redirects = 0 net.ipv6.conf.default.accept_redirects = 0 net.ipv6.conf.enp1s0.accept_redirects = 0 net.ipv6.conf.lo.accept_redirects = 0 If the returned lines do not all have a value of "0", this is a finding.

## Group: SRG-OS-000480-GPOS-00232

**Group ID:** `V-269245`

### Rule: The firewalld service on AlmaLinux OS 9 must be active.

**Rule ID:** `SV-269245r1050613_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>"Firewalld" provides an easy and effective way to block/limit remote access to the system via ports, services, and protocols. Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. AlmaLinux OS 9 functionality (e.g., SSH) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets). Satisfies: SRG-OS-000480-GPOS-00232, SRG-OS-000096-GPOS-00050, SRG-OS-000297-GPOS-00115</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "firewalld" is active with the following command: $ systemctl is-active firewalld active If the firewalld service is not active, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269246`

### Rule: AlmaLinux OS 9 firewall must employ a deny-all, allow-by-exception policy for allowing connections to other systems.

**Rule ID:** `SV-269246r1050780_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to restrict network connectivity only to authorized systems permits inbound connections from malicious systems. It also permits outbound connections that may facilitate exfiltration of DOD data. AlmaLinux OS 9 incorporates the "firewalld" daemon, which allows for many different configurations. One of these configurations is zones. Zones can be used to a deny-all, allow-by-exception approach. The default "drop" zone will drop all incoming network packets unless it is explicitly allowed by the configuration file or is related to an outgoing network connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AlmaLinux OS 9 "firewalld" is configured to employ a deny-all, allow-by-exception policy for allowing connections to other systems. First ensure firewalld is running: $ firewall-cmd --state running Next, get the active zones: $ firewall-cmd --get-active-zones public interfaces: enp1s0 Check the target of the zones returned from the previous command: $ firewall-cmd --info-zone=public | grep target target: DROP Check the runtime and permanent rules match: $ firewall-cmd --permanent --info-zone=public | grep target target: DROP If no zones are active on the AlmaLinux OS 9 interfaces or if runtime and permanent targets are set to a different option other than "DROP", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269247`

### Rule: AlmaLinux OS 9 must limit the number of bogus Internet Control Message Protocol (ICMP) response errors logs.

**Rule ID:** `SV-269247r1050129_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some routers will send responses to broadcast frames that violate RFC-1122, which fills up a log file system with many useless error messages. An attacker may take advantage of this and attempt to flood the logs with bogus error logs. Ignoring bogus ICMP error responses reduces log size, although some activity would not be logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 ignores bogus ICMP error responses with the following command: $ sysctl net.ipv4.icmp_ignore_bogus_error_responses net.ipv4.icmp_ignore_bogus_error_responses = 1 If the returned line does not have a value of "1", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269248`

### Rule: AlmaLinux OS 9 must not respond to Internet Control Message Protocol (ICMP) echoes sent to a broadcast address.

**Rule ID:** `SV-269248r1050130_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Responding to broadcast (ICMP) echoes facilitates network mapping and provides a vector for amplification attacks. Ignoring ICMP echo requests (pings) sent to broadcast or multicast addresses makes the system slightly more difficult to enumerate on the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 does not respond to ICMP echoes sent to a broadcast address with the following command: $ sysctl net.ipv4.icmp_echo_ignore_broadcasts net.ipv4.icmp_echo_ignore_broadcasts = 1 If the returned line does not have a value of "1", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269249`

### Rule: AlmaLinux OS 9 must not enable IP packet forwarding unless the system is a router.

**Rule ID:** `SV-269249r1050131_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this capability is used when not required, system network information may be unnecessarily transmitted across the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 is not performing IP packet forwarding, unless the system is a router. Check that IP forwarding is disabled using the following command: $ sysctl -a | grep -E '\.forwarding' net.ipv4.conf.all.forwarding = 0 net.ipv4.conf.default.forwarding = 0 net.ipv4.conf.enp1s0.forwarding = 0 net.ipv4.conf.lo.forwarding = 0 net.ipv6.conf.all.forwarding = 0 net.ipv6.conf.default.forwarding = 0 net.ipv6.conf.enp1s0.forwarding = 0 net.ipv6.conf.lo.forwarding = 0 If any of the returned lines are not set to "0" and it is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269250`

### Rule: AlmaLinux OS 9 must not have unauthorized IP tunnels configured.

**Rule ID:** `SV-269250r1050132_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IP tunneling mechanisms can be used to bypass network filtering. If tunneling is required, it must be documented with the information system security officer (ISSO).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 does not have unauthorized IP tunnels configured. Determine if the "IPsec" service is active with the following command: $ systemctl status ipsec ipsec.service - Internet Key Exchange (IKE) Protocol Daemon for IPsec Loaded: loaded (/usr/lib/systemd/system/ipsec.service; disabled; preset: disabled) Active: inactive (dead) If the "IPsec" service is active, check for configured IPsec connections ("conn"), with the following command: $ grep -ri conn /etc/ipsec.conf /etc/ipsec.d/ | grep -v '#' Verify any returned results are documented with the ISSO. If the IPsec tunnels are active and not approved, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269251`

### Rule: AlmaLinux OS 9 must log packets with impossible addresses.

**Rule ID:** `SV-269251r1050133_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The presence of "martian" packets (which have impossible addresses) as well as spoofed packets, source-routed packets, and redirects could be a sign of nefarious network activity. Logging these packets enables this activity to be detected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 logs martian packets. Check the value of the "log_martians" variables with the following command: $ sysctl -a | grep log_martians net.ipv4.conf.all.log_martians = 1 net.ipv4.conf.default.log_martians = 1 net.ipv4.conf.enp1s0.log_martians = 1 net.ipv4.conf.lo.log_martians = 1 If the returned lines do not all have a value of "1", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269252`

### Rule: AlmaLinux OS 9 must be configured to prevent unrestricted mail relaying.

**Rule ID:** `SV-269252r1050134_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If unrestricted mail relaying is permitted, unauthorized senders could use this host as a mail relay for the purpose of sending spam or other unauthorized activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If postfix is not installed, this is Not Applicable. Verify AlmaLinux OS 9 is configured to prevent unrestricted mail relaying with the following command: $ postconf -n smtpd_client_restrictions smtpd_client_restrictions = permit_mynetworks,reject If the "smtpd_client_restrictions" parameter contains any entries other than "permit_mynetworks" and "reject", and the additional entries have not been documented with the information system security officer (ISSO), this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269253`

### Rule: AlmaLinux OS 9 must have the nss-tools package installed.

**Rule ID:** `SV-269253r1101817_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network Security Services (NSS) is a set of libraries designed to support cross-platform development of security-enabled client and server applications. Install the "nss-tools" package to install command-line tools to manipulate the NSS certificate and key database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 has the FIPS-validated nss-tools package installed with the following command: $ dnf list --installed nss-tools Installed Packages nss-tools.x86_64 3.90.0-6.el9_2.tuxcare.1 @@commandline If the TuxCare version of the "nss-tools" package is not installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269254`

### Rule: AlmaLinux OS 9 network interfaces must not be in promiscuous mode.

**Rule ID:** `SV-269254r1050136_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network interfaces in promiscuous mode allow for the capture of all network traffic visible to the system. If unauthorized individuals can access these applications, it may allow them to collect information such as logon IDs, passwords, and key exchanges between systems. If the system is being used to perform a network troubleshooting function, the use of these tools must be documented with the information system security officer (ISSO) and restricted to only authorized personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify network interfaces are not in promiscuous mode with the following command: $ ip link | grep -i promisc If network interfaces are found on the system in promiscuous mode and their use has not been approved by the ISSO and documented, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269255`

### Rule: AlmaLinux OS 9 must use reverse path filtering on all IP interfaces.

**Rule ID:** `SV-269255r1050137_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling reverse path filtering drops packets with source addresses that should not have been able to be received on the interface on which they were received. It must not be used on systems that are routers for complicated networks, but is helpful for end hosts and routers serving small networks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 uses reverse path filtering on all IP interfaces with the following command: $ sysctl -a | grep -E '\.rp_filter' net.ipv4.conf.all.rp_filter = 0 net.ipv4.conf.default.rp_filter = 1 net.ipv4.conf.enp1s0.rp_filter = 1 net.ipv4.conf.lo.rp_filter = 1 If the returned lines do not all have a value of "1", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269256`

### Rule: AlmaLinux OS 9 must not send Internet Control Message Protocol (ICMP) redirects.

**Rule ID:** `SV-269256r1050138_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages contain information from the system's route table possibly revealing portions of the network topology. The ability to send ICMP redirects is only appropriate for systems acting as routers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 does not send ICMP redirects. Check the value of the "send_redirects" variables with the following command: $ sysctl -a | grep send_redirects net.ipv4.conf.all.send_redirects = 0 net.ipv4.conf.default.send_redirects = 0 net.ipv4.conf.enp1s0.send_redirects = 0 net.ipv4.conf.lo.send_redirects = 0 If the returned lines do not all have a value of "0", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269257`

### Rule: There must be no .shosts files on AlmaLinux OS 9.

**Rule ID:** `SV-269257r1050139_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The .shosts files are used to configure host-based authentication for individual users or the system via SSH. Host-based authentication is not sufficient for preventing unauthorized access to the system, as it does not require interactive identification and authentication of a connection request, or for the use of two-factor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there are no ".shosts" files on AlmaLinux OS 9 with the following command: $ find / -name .shosts If a ".shosts" file is found, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269258`

### Rule: There must be no shosts.equiv files on AlmaLinux OS 9.

**Rule ID:** `SV-269258r1050140_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shosts.equiv files are used to configure host-based authentication for the system via SSH. Host-based authentication is not sufficient for preventing unauthorized access to the system, as it does not require interactive identification and authentication of a connection request, or for the use of two-factor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there are no "shosts.equiv" files on AlmaLinux OS 9 with the following command: $ find / -name shosts.equiv If a "shosts.equiv" file is found, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269259`

### Rule: Alma Linux OS 9 must not accept IPv4 source-routed packets by default.

**Rule ID:** `SV-269259r1107619_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Source-routed packets allow the source of the packet to suggest routers forward the packet along a different path than configured on the router, which can be used to bypass network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when IP forwarding is enabled and the system is functioning as a router. Accepting source-routed packets has few legitimate uses. It must be disabled unless it is absolutely required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 will not accept source-routed packets. Check the value of the "accept_source_route" variables with the following command: $ sysctl -a | grep accept_source_route net.ipv4.conf.all.accept_source_route = 0 net.ipv4.conf.default.accept_source_route = 0 net.ipv4.conf.enp1s0.accept_source_route = 0 net.ipv4.conf.lo.accept_source_route = 0 net.ipv6.conf.all.accept_source_route = 0 net.ipv6.conf.default.accept_source_route = 0 net.ipv6.conf.enp1s0.accept_source_route = 0 net.ipv6.conf.lo.accept_source_route = 0 If the returned lines do not all have a value of "0", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269260`

### Rule: AlmaLinux OS 9 SSH daemon must not allow compression or must only allow compression after successful authentication.

**Rule ID:** `SV-269260r1050142_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If compression is allowed in an SSH connection prior to authentication, vulnerabilities in the compression software could result in compromise of the system from an unauthenticated connection, potentially with root privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon performs compression after a user successfully authenticates with the following command: $ sshd -T | grep compression Compression no If the "Compression" keyword is set to "yes", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269261`

### Rule: The AlmaLinux OS 9 SSH server configuration file must be group-owned by root.

**Rule ID:** `SV-269261r1050143_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Service configuration files enable or disable features of their respective services, which if configured incorrectly, can lead to insecure and vulnerable configurations. Therefore, service configuration files must be owned by the correct group to prevent unauthorized changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the group ownership of "/etc/ssh/sshd_config" and any "/etc/ssh/sshd_config.d/*.conf" files with the following command: $ find /etc/ssh/sshd_config /etc/ssh/sshd_config.d -exec stat -c "%G %n" {} \; root /etc/ssh/sshd_config root /etc/ssh/sshd_config.d root /etc/ssh/sshd_config.d/40-stig.conf root /etc/ssh/sshd_config.d/50-redhat.conf root /etc/ssh/sshd_config.d/clientalive.conf If any of the files do not have a group owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269262`

### Rule: The AlmaLinux OS 9 SSH server configuration file must be owned by root.

**Rule ID:** `SV-269262r1050144_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Service configuration files enable or disable features of their respective services, which, if configured incorrectly, can lead to insecure and vulnerable configurations. Therefore, service configuration files must be owned by the correct group to prevent unauthorized changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ownership of "/etc/ssh/sshd_config" and any "/etc/ssh/sshd_config.d/*.conf" files with the following command: $ find /etc/ssh/sshd_config /etc/ssh/sshd_config.d -exec stat -c "%U %n" {} \; root /etc/ssh/sshd_config root /etc/ssh/sshd_config.d root /etc/ssh/sshd_config.d/40-stig.conf root /etc/ssh/sshd_config.d/50-redhat.conf root /etc/ssh/sshd_config.d/clientalive.conf If any of the files do not have an owner of "root", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269263`

### Rule: AlmaLinux OS 9 SSH server configuration files must have mode 0600 or less permissive.

**Rule ID:** `SV-269263r1050145_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Service configuration files enable or disable features of their respective services, which if configured incorrectly, can lead to insecure and vulnerable configurations. Therefore, service configuration files must be owned by the correct group to prevent unauthorized changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the permissions of "/etc/ssh/sshd_config" and any "/etc/ssh/sshd_config.d/*.conf" files with the following command: $ find /etc/ssh/sshd_config /etc/ssh/sshd_config.d -exec stat -c "%#a %n" {} \; 600 /etc/ssh/sshd_config 755 /etc/ssh/sshd_config.d 600 /etc/ssh/sshd_config.d/40-stig.conf 600 /etc/ssh/sshd_config.d/50-redhat.conf 600 /etc/ssh/sshd_config.d/clientalive.conf If any of the files do not have "0600" permissions, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269264`

### Rule: AlmaLinux OS 9 must not allow a noncertificate trusted host SSH logon to the system.

**Rule ID:** `SV-269264r1050146_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH trust relationships mean a compromise on one host can allow an attacker to move trivially to other hosts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system does not allow a noncertificate trusted host SSH logon to the system with the following command: $ sshd -T | grep hostbasedauthentication hostbasedauthentication no If the "HostbasedAuthentication" keyword is not set to "no", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269265`

### Rule: AlmaLinux OS 9 SSH private host key files must have mode 0640 or less permissive.

**Rule ID:** `SV-269265r1050147_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an unauthorized user obtains the private SSH host key file, the host could be impersonated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH private host key files have a mode of "0640" or less permissive with the following command: $ stat -c "%#a %n" /etc/ssh/ssh_host*key 0640 /etc/ssh/ssh_host_ecdsa_key 0640 /etc/ssh/ssh_host_rsa_key If any private host key file has a mode more permissive than "0640", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269266`

### Rule: AlmaLinux OS 9 SSH public host key files must have mode 0644 or less permissive.

**Rule ID:** `SV-269266r1050148_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a public host key file is modified by an unauthorized user, the SSH service may be compromised. Whilst public keys are publicly readable, they should not be writeable by nonowners.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH public host key files have a mode of "0644" or less permissive with the following command: Note: SSH public key files may be found in other directories on the system depending on the installation. $ stat -c "%#a %n" /etc/ssh/ssh_host*key.pub 0644 /etc/ssh/ssh_host_ecdsa_key.pub 0644 /etc/ssh/ssh_host_rsa_key.pub If any public key has a mode more permissive than "0644", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269267`

### Rule: AlmaLinux OS 9 SSH daemon must not allow known hosts authentication.

**Rule ID:** `SV-269267r1050149_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the IgnoreUserKnownHosts setting for the SSH daemon provides additional assurance that remote login via SSH will require a password, even in the event of misconfiguration elsewhere.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon does not allow known hosts authentication with the following command: $ sshd -T | grep ignoreuserknownhosts ignoreuserknownhosts yes If the value is returned as "no", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269268`

### Rule: AlmaLinux OS 9 SSH daemon must display the date and time of the last successful account logon upon an SSH logon.

**Rule ID:** `SV-269268r1050150_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Providing users feedback on when account accesses last occurred facilitates user recognition and reporting of unauthorized account use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon provides users with feedback on when account accesses last occurred with the following command: $ sshd -T | grep printlastlog printlastlog yes If the value is returned as "no", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269269`

### Rule: AlmaLinux OS 9 SSH daemon must not allow rhosts authentication.

**Rule ID:** `SV-269269r1050151_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH trust relationships mean a compromise on one host can allow an attacker to move trivially to other hosts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon does not allow rhosts authentication with the following command: $ sshd -T | grep ignorerhosts ignorerhosts yes If the "IgnoreRhosts" keyword is set to "no", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269270`

### Rule: AlmaLinux OS 9 SSH daemon must disable remote X connections for interactive users.

**Rule ID:** `SV-269270r1050152_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When X11 forwarding is enabled, there may be additional exposure to the server and client displays if the sshd proxy display is configured to listen on the wildcard address. By default, sshd binds the forwarding server to the loopback address and sets the hostname part of the DISPLAY environment variable to localhost. This prevents remote hosts from connecting to the proxy display.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon does not allow X11Forwarding with the following command: $ sshd -T | grep x11forwarding x11forwarding no If the value is returned as "yes" and X11 forwarding is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269271`

### Rule: AlmaLinux OS 9 SSH daemon must prevent remote hosts from connecting to the proxy display.

**Rule ID:** `SV-269271r1050153_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When X11 forwarding is enabled, there may be additional exposure to the server and client displays if the sshd proxy display is configured to listen on the wildcard address. By default, sshd binds the forwarding server to the loopback address and sets the hostname part of the "DISPLAY" environment variable to localhost. This prevents remote hosts from connecting to the proxy display.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon prevents remote hosts from connecting to the proxy display with the following command: $ sshd -T | grep x11uselocalhost x11uselocalhost yes If the value is returned as "no", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269272`

### Rule: If the Trivial File Transfer Protocol (TFTP) server is required, the TFTP daemon must be configured to operate in secure mode.

**Rule ID:** `SV-269272r1050154_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting TFTP to a specific directory prevents remote users from copying, transferring, or overwriting system files. Using the "-s" option causes the TFTP service to only serve files from the given directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If a TFTP server is not installed, this requirement is Not Applicable. Verify the TFTP daemon is configured to operate in secure mode. Check if a TFTP server is installed with the following command: $ dnf list --installed tftp-server Installed Packages tftp-server.x86_64 5.2-37.el9 @appstream If a TFTP server is installed, check for the server arguments with the following command: $ systemctl cat tftp | grep ExecStart= ExecStart=/usr/sbin/in.tftpd -s /var/lib/tftpboot If the "ExecStart" line does not have a "-s" option, and a subdirectory is not assigned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269273`

### Rule: AlmaLinux OS 9 must enable hardening for the Berkeley Packet Filter (BPF) just-in-time (JIT) compiler.

**Rule ID:** `SV-269273r1050155_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When hardened, the extended BPF JIT compiler will randomize any kernel addresses in the BPF programs and maps, and will not expose the JIT addresses in "/proc/kallsyms".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 enables hardening for the BPF JIT with the following commands: $ sysctl net.core.bpf_jit_harden net.core.bpf_jit_harden = 2 If the returned line does not have a value of "2", or a line is not returned, this is a finding. Check that the configuration files are present to enable this kernel parameter. $ /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F net.core.bpf_jit_harden | tail -1 net.core.bpf_jit_harden = 2 If the network parameter "net.core.bpf_jit_harden" is not equal to "2" or nothing is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269274`

### Rule: AlmaLinux OS 9 effective dconf policy must match the policy keyfiles.

**Rule ID:** `SV-269274r1050156_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unlike text-based keyfiles, the binary database is impossible to check through most automated and all manual means; therefore, to evaluate dconf configuration, both have to be true at the same time—configuration files have to be compliant, and the database needs to be more recent than those keyfiles, which gives confidence that it reflects them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the AlmaLinux OS 9 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Check the last modification time of the local databases, comparing it to the last modification time of the related keyfiles. The following command will check every dconf database and compare its modification time to the related system keyfiles: $ function dconf_needs_update { for db in $(find /etc/dconf/db -maxdepth 1 -type f); do db_mtime=$(stat -c %Y "$db"); keyfile_mtime=$(stat -c %Y "$db".d/* | sort -n | tail -1); if [ -n "$db_mtime" ] && [ -n "$keyfile_mtime" ] && [ "$db_mtime" -lt "$keyfile_mtime" ]; then echo "$db needs update"; return 1; fi; done; }; dconf_needs_update If the command has any output, then a dconf database needs to be updated, and this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269275`

### Rule: AlmaLinux OS 9 must be configured so that all system device files are correctly labeled to prevent unauthorized modification.

**Rule ID:** `SV-269275r1050157_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an unauthorized or modified device is allowed to exist on the system, there is the possibility the system may perform unintended or unauthorized operations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all system device files are correctly labeled to prevent unauthorized modification. List all device files on the system that are incorrectly labeled with the following commands: Note: Device files are normally found under "/dev", but applications may place device files in other directories and may necessitate a search of the entire system. # find /dev -context *:device_t:* \( -type c -o -type b \) -printf "%p %Z\n" # find /dev -context *:unlabeled_t:* \( -type c -o -type b \) -printf "%p %Z\n" Note: There are device files, such as "/dev/vmci", that are used when the operating system is a host virtual machine. They will not be owned by a user on the system and require the "device_t" label to operate. These device files are not a finding. If there is output from either of these commands, other than already noted, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269276`

### Rule: All AlmaLinux OS 9 local initialization files must have mode 0740 or less permissive.

**Rule ID:** `SV-269276r1050158_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Local initialization files are used to configure the user's shell environment upon logon. Malicious modification of these files could compromise accounts upon logon. World-readable "dot files" such as .bash_history or .netrc can reveal plaintext credentials, such files should be further protected (e.g., 0600).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all local initialization files have a mode of "0740" or less permissive with the following command: Note: The example will be for the "testuser" account, who has a home directory of "/home/testuser". $ find /home/testuser/.[^.]* -maxdepth 0 -perm -740 -exec stat -c "%a %n" {} \; | more 755 /home/testuser/.cache 755 /home/testuser/.mozilla If any local initialization files have a mode more permissive than "0740", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269277`

### Rule: AlmaLinux OS 9 must have the gnutls-utils package installed.

**Rule ID:** `SV-269277r1050159_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>GnuTLS is a secure communications library implementing the SSL, TLS, and DTLS protocols and technologies around them. It provides a simple C language application programming interface (API) to access the secure communications protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP, and other required structures. This package contains command line TLS client and server and certificate manipulation tools.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 has the gnutls-utils package installed with the following command: $ dnf list --installed gnutls-utils Installed Packages gnutls-utils.x86_64 3.7.6-23.el9_2.tuxcare.3 @@commandline If the "gnutls-utils" package is not installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269278`

### Rule: The kdump service on AlmaLinux OS 9 must be disabled.

**Rule ID:** `SV-269278r1050160_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kernel core dumps may contain the full contents of system memory at the time of the crash. Kernel core dumps consume a considerable amount of disk space and may result in denial of service by exhausting the available space on the target file system partition. Unless the system is used for kernel development or testing, there is little need to run the kdump service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the kdump service is disabled in system boot configuration with the following command: $ systemctl is-enabled kdump masked Verify that the kdump service is not active (i.e., not running) through current runtime configuration with the following command: $ systemctl is-active kdump inactive Verify that the kdump service is masked with the following command: $ systemctl show kdump | grep "LoadState\|UnitFileState" LoadState=masked UnitFileState=masked If the "kdump" service is loaded or active, and is not masked, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269279`

### Rule: AlmaLinux OS 9 must disable the ability of a user to restart the system from the login screen.

**Rule ID:** `SV-269279r1050161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A user who is at the console can reboot the system at the login screen. If restart or shutdown buttons are pressed at the login screen, this can create the risk of short-term loss of availability of systems due to reboot.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the AlmaLinux OS 9 default graphical user interface, Gnome Shell. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify AlmaLinux OS 9 disables a user's ability to restart the system with the following command: $ grep -R disable-restart-buttons /etc/dconf/db/* /etc/dconf/db/distro.d/20-authselect:disable-restart-buttons='true' If the "disable-restart-button" setting is not set to "true", is missing or commented out from the dconf database files, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269280`

### Rule: AlmaLinux OS 9 must prevent a user from overriding the disable-restart-buttons setting for the graphical user interface.

**Rule ID:** `SV-269280r1050162_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A user who is at the console can reboot the system at the login screen. If restart or shutdown buttons are pressed at the login screen, this can create the risk of short-term loss of availability of systems due to reboot.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the AlmaLinux OS 9 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify AlmaLinux OS 9 prevents a user from overriding the disable-restart-buttons setting for graphical user interfaces. Determine which profile the system database is using with the following command: $ grep system-db /etc/dconf/profile/user system-db:local Check that graphical settings are locked from nonprivileged user modification with the following command: Note: The example below is using the database "local" for the system, so the path is "/etc/dconf/db/local.d". This path must be modified if a database other than "local" is being used. $ grep disable-restart-buttons /etc/dconf/db/local.d/locks/* /org/gnome/login-screen/disable-restart-buttons If the command does not return at least the example result, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269281`

### Rule: AlmaLinux OS 9 must prevent special devices on file systems that are used with removable media.

**Rule ID:** `SV-269281r1050163_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system not to interpret character or block special devices. Executing character or blocking special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify file systems that are used for removable media are mounted with the "nodev" option with the following command: $ cat /etc/fstab UUID=0cb43738-b102-48f8-9174-061d8ee537b8 /mnt/usbdrive vfat noauto,owner,ro,nosuid,nodev,noexec 0 0 If a file system found in "/etc/fstab" refers to removable media and it does not have the "nodev" option set, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269282`

### Rule: AlmaLinux OS 9 must prevent code from being executed on file systems that are used with removable media.

**Rule ID:** `SV-269282r1050164_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify file systems that are used for removable media are mounted with the "noexec" option with the following command: $ cat /etc/fstab UUID=0cb43738-b102-48f8-9174-061d8ee537b8 /mnt/usbdrive vfat noauto,owner,ro,nosuid,nodev,noexec 0 0 If a file system found in "/etc/fstab" refers to removable media and it does not have the "noexec" option set, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269283`

### Rule: AlmaLinux OS 9 must prevent files with the setuid and setgid bit set from being executed on file systems that are used with removable media.

**Rule ID:** `SV-269283r1050165_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify file systems that are used for removable media are mounted with the "nosuid" option with the following command: $ cat /etc/fstab UUID=0cb43738-b102-48f8-9174-061d8ee537b8 /mnt/usbdrive vfat noauto,owner,ro,nosuid,nodev,noexec 0 0 If a file system found in "/etc/fstab" refers to removable media and it does not have the "nosuid" option set, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269284`

### Rule: AlmaLinux OS 9 must disable the use of user namespaces.

**Rule ID:** `SV-269284r1101813_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User namespaces are used primarily for Linux containers. The value "0" disallows the use of user namespaces.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: User namespaces are used primarily for Linux containers. If containers are in use, this requirement is Not Applicable. Verify AlmaLinux OS 9 disables the use of user namespaces with the following commands: $ sysctl user.max_user_namespaces user.max_user_namespaces = 0 If the returned line does not have a value of "0", or a line is not returned, this is a finding. Check that the configuration files are present to enable this kernel parameter. $ /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F user.max_user_namespaces | tail -1 user.max_user_namespaces = 0 If the network parameter "user.max_user_namespaces" is not equal to "0", or nothing is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269285`

### Rule: AlmaLinux OS 9 must prevent special devices on file systems that are imported via Network File System (NFS).

**Rule ID:** `SV-269285r1050167_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If no NFS mounts are configured, this requirement is Not Applicable. Verify AlmaLinux OS 9 has the "nodev" option configured for all NFS mounts with the following command: $ grep nfs /etc/fstab 192.168.1.9:/mnt/export /backups nfs4 rw,nosuid,nodev,noexec,sync,soft,sec=krb5p:krb5i:krb5 If the system is mounting file systems via NFS and the "nodev" option is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269286`

### Rule: AlmaLinux OS 9 must prevent code execution on file systems that are imported via Network File System (NFS).

**Rule ID:** `SV-269286r1050168_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If no NFS mounts are configured, this requirement is Not Applicable. Verify AlmaLinux OS 9 has the "noexec" option configured for all NFS mounts with the following command: $ grep nfs /etc/fstab 192.168.1.9:/mnt/export /backups nfs4 rw,nosuid,nodev,noexec,sync,soft,sec=krb5p:krb5i:krb5 If the system is mounting file systems via NFS and the "noexec" option is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269287`

### Rule: AlmaLinux OS 9 must prevent files with the setuid and setgid bit set from being executed on file systems that are imported via Network File System (NFS).

**Rule ID:** `SV-269287r1050169_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system not to execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If no NFS mounts are configured, this requirement is Not Applicable. Verify AlmaLinux OS 9 has the "nosuid" option configured for all NFS mounts with the following command: $ grep nfs /etc/fstab 192.168.22.2:/mnt/export /data nfs4 rw,nosuid,nodev,noexec,sync,soft,sec=krb5:krb5i:krb5p If the system is mounting file systems via NFS and the "nosuid" option is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269288`

### Rule: AlmaLinux OS 9 must configure a DNS processing mode set be Network Manager.

**Rule ID:** `SV-269288r1050170_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure that DNS resolver settings are respected, a DNS mode in Network Manager must be configured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If AlmaLinux OS 9 is configured to use a DNS resolver other than Network Manager, the configuration must be documented and approved by the information system security officer (ISSO). Verify that AlmaLinux OS 9 has a DNS mode configured in Network Manager. $ NetworkManager --print-config [main] dns=none If the "dns" key in the [main] section does not exist or is not set to "none" or "default", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269289`

### Rule: AlmaLinux OS 9 systems using Domain Name Servers (DNS) resolution must have at least two name servers configured.

**Rule ID:** `SV-269289r1050171_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To provide availability for name resolution services, multiple redundant name servers are mandated. A failure in name resolution could lead to the failure of security functions requiring name resolution, which may include time synchronization, centralized authentication, and remote system logging.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the name servers used by the system with the following command: $ grep nameserver /etc/resolv.conf nameserver 192.168.2.4 nameserver 192.168.2.5 If less than two lines are returned that are not commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269290`

### Rule: AlmaLinux OS 9 must prevent special devices on nonroot local partitions.

**Rule ID:** `SV-269290r1050172_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access. The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all nonroot local partitions are mounted with the "nodev" option with the following command: $ mount | grep '^/dev\S* on /\S' | grep --invert-match 'nodev' If any output is produced, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269291`

### Rule: The root account must be the only account having unrestricted access to an AlmaLinux OS 9 system.

**Rule ID:** `SV-269291r1050173_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An account has root authority if it has a user identifier (UID) of "0". Multiple accounts with a UID of "0" afford more opportunity for potential intruders to guess a password for a privileged account. Proper configuration of sudo is recommended to afford multiple system administrators access to root privileges in an accountable manner.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that only the "root" account has a UID "0" assignment with the following command: $ awk -F: '$3 == 0 {print $1}' /etc/passwd root If any accounts other than "root" have a UID of "0", this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269292`

### Rule: AlmaLinux OS 9 must be configured so that the cryptographic hashes of system files match vendor values.

**Rule ID:** `SV-269292r1050174_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The hashes of important files like system executables should match the information given by the RPM database. Executables with erroneous hashes could be a sign of nefarious activity on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The following command will list which files on the system have file hashes different from what is expected by the RPM database: $ rpm -Va --noconfig | awk '$1 ~ /..5/ && $2 != "c"' If there is an output, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269293`

### Rule: AlmaLinux OS 9 must clear the page allocator to prevent use-after-free attacks.

**Rule ID:** `SV-269293r1050175_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Poisoning writes an arbitrary value to freed pages, so any modification or reference to that page after being freed or before being initialized will be detected and prevented. This prevents many types of use-after-free vulnerabilities at little performance cost. This also prevents data leaks and detects corrupted memory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that GRUB 2 is configured to enable page poisoning to mitigate use-after-free vulnerabilities. Check that the current GRUB 2 configuration has page poisoning enabled with the following command: $ grubby --info=ALL | grep args | grep -v 'page_poison=1' If any output is returned, this is a finding. Check that page poisoning is enabled by default to persist in kernel updates with the following command: $ grep page_poison /etc/default/grub GRUB_CMDLINE_LINUX="page_poison=1" If "page_poison" is not set to "1", is missing or commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269294`

### Rule: AlmaLinux OS 9 must display the date and time of the last successful account logon upon logon.

**Rule ID:** `SV-269294r1050176_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Users need to be aware of activity that occurs regarding their account. Providing users with information regarding the number of unsuccessful attempts that were made to login to their account allows the user to determine if any unauthorized activity has occurred and gives them an opportunity to notify administrators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify users are provided with feedback on when account accesses last occurred with the following command: $ grep pam_lastlog /etc/pam.d/postlogin session required pam_lastlog.so showfailed If "pam_lastlog" is missing from "/etc/pam.d/postlogin" file, or the silent option is present, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269295`

### Rule: AlmaLinux OS 9 security patches and updates must be installed and up to date.

**Rule ID:** `SV-269295r1050177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Installing software updates is a fundamental mitigation against the exploitation of publicly known vulnerabilities. If the most recent security patches and updates are not installed, unauthorized users may take advantage of weaknesses in the unpatched software. The lack of prompt attention to patching could result in a system compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 security patches and updates are installed and up to date. Updates are required to be applied with a frequency determined by organizational policy. Obtain the list of available package security updates from TuxCare. The URL for updates is https://cve.tuxcare.com/els/cve/. It is important to note that updates may not be present on the system if the underlying packages are not installed. Check if there are security updates available that have not been installed with the following command: $ dnf updateinfo list updates security CLSA-2024:1708029809 Important/Sec. gnutls-3.7.6-21.el9_2.tuxcare.els1.x86_64 CLSA-2024:1708029936 Important/Sec. gnutls-3.7.6-21.el9_2.tuxcare.els2.x86_64 CLSA-2024:1708416911 Important/Sec. libxml2-2.9.13-3.el9_2.1.tuxcare.els1.x86_64 CLSA-2024:1708417063 Moderate/Sec. python3-rpm-4.16.1.3-22.el9.tuxcare.els1.x86_64 CLSA-2024:1708417063 Moderate/Sec. rpm-4.16.1.3-22.el9.tuxcare.els1.x86_64 CLSA-2024:1708417063 Moderate/Sec. rpm-build-libs-4.16.1.3-22.el9.tuxcare.els1.x86_64 CLSA-2024:1708417063 Moderate/Sec. rpm-libs-4.16.1.3-22.el9.tuxcare.els1.x86_64 CLSA-2024:1708417063 Moderate/Sec. rpm-plugin-audit-4.16.1.3-22.el9.tuxcare.els1.x86_64 CLSA-2024:1708417063 Moderate/Sec. rpm-plugin-selinux-4.16.1.3-22.el9.tuxcare.els1.x86_64 CLSA-2024:1708417063 Moderate/Sec. rpm-plugin-systemd-inhibit-4.16.1.3-22.el9.tuxcare.els1.x86_64 CLSA-2024:1708417063 Moderate/Sec. rpm-sign-libs-4.16.1.3-22.el9.tuxcare.els1.x86_64 Typical update frequency may be overridden by Information Assurance Vulnerability Alert (IAVA) notifications from CYBERCOM. If the system is in not compliant with the organizational patching policy, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269296`

### Rule: AlmaLinux OS 9 policycoreutils-python-utils package must be installed.

**Rule ID:** `SV-269296r1050178_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The policycoreutils-python-utils package is required to operate and manage an SELinux environment and its policies. It provides utilities such as semanage, audit2allow, audit2why, chcat, and sandbox.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 policycoreutils-python-utils service package is installed with the following command: $ dnf list --installed policycoreutils-python-utils policycoreutils-python-utils.noarch 3.5-1.el9 @AppStream If the "policycoreutils-python-utils" package is not installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269297`

### Rule: AlmaLinux OS 9 must enable the hardware random number generator entropy gatherer service.

**Rule ID:** `SV-269297r1050179_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The most important characteristic of a random number generator is its randomness, specifically its ability to deliver random numbers that are impossible to predict. Entropy in computer security is associated with the unpredictability of a source of randomness. The random source with high entropy tends to achieve a uniform distribution of random values. Random number generators are one of the most important building blocks of cryptosystems. The rngd service feeds random data from hardware device to kernel random device. Quality (nonpredictable) random number generation is important for several security functions (i.e., ciphers).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For AlmaLinux OS 9 systems running with FIPS mode enabled, this requirement is Not Applicable. Verify that AlmaLinux OS 9 has enabled the hardware random number generator entropy gatherer service with the following command: $ systemctl is-active rngd active If the "rngd" service is not active, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269298`

### Rule: AlmaLinux OS 9 must have the rng-tools package installed.

**Rule ID:** `SV-269298r1050180_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>"rng-tools" provides hardware random number generator tools, such as those used in the formation of x509/PKI certificates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 has the rng-tools package installed with the following command: $ dnf list --installed rng-tools rng-tools.x86_64 6.15-3.el9 @baseos If the "rng-tools" package is not installed, this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-269299`

### Rule: The SSH daemon must perform strict mode checking of home directory configuration files.

**Rule ID:** `SV-269299r1050181_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If other users have access to modify user-specific SSH configuration files or read keys, they may be able to log into the system as another user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon performs strict mode checking of home directory configuration files with the following command: $ sshd -T | grep strictmodes strictmodes yes If the "StrictModes" keyword is set to "no", or no output is returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269300`

### Rule: AlmaLinux OS 9 system accounts must not have an interactive login shell.

**Rule ID:** `SV-269300r1050182_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensuring shells are not given to system accounts upon login makes it more difficult for attackers to make use of system accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that system accounts must not have an interactive login shell with the following command: $ awk -F: '($3<1000){print $1 ":" $3 ":" $7}' /etc/passwd root:0:/bin/bash bin:1:/sbin/nologin daemon:2:/sbin/nologin adm:3:/sbin/nologin lp:4:/sbin/nologin sync:5:/bin/sync shutdown:6:/sbin/shutdown halt:7:/sbin/halt mail:8:/sbin/nologin operator:11:/sbin/nologin games:12:/sbin/nologin ftp:14:/sbin/nologin systemd-coredump:999:/sbin/nologin dbus:81:/sbin/nologin polkitd:998:/sbin/nologin tss:59:/sbin/nologin sssd:997:/sbin/nologin unbound:996:/sbin/nologin fapolicyd:995:/sbin/nologin postfix:89:/sbin/nologin sshd:74:/sbin/nologin chrony:994:/sbin/nologin systemd-oom:989:/usr/sbin/nologin Identify the system accounts from this listing that do not have a nologin shell. If any system account (other than the root account) has a login shell and it is not documented with the information system security officer (ISSO), this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269301`

### Rule: AlmaLinux OS 9 must use a separate file system for /tmp.

**Rule ID:** `SV-269301r1050183_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/tmp" partition is used as temporary storage by many programs. Placing "/tmp" in its own partition enables the setting of more restrictive mount options, which can help protect programs that use it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a separate file system/partition has been created for "/tmp" with the following command: $ mount | grep ' /tmp ' tmpfs on /tmp type tmpfs (rw,nosuid,nodev,noexec,relatime,seclabel,size=2097152k,inode64) If a separate entry for "/tmp" is not in use, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269302`

### Rule: Local AlmaLinux OS 9 initialization files must not execute world-writable programs.

**Rule ID:** `SV-269302r1050184_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If user start-up files execute world-writable programs, especially in unprotected directories, they could be maliciously modified to destroy user files or otherwise compromise the system at the user level. If the system is compromised at the user level, it is easier to elevate privileges to eventually compromise the system at the root and network level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that local initialization files do not execute world-writable programs with the following command: Note: The example will be for a system that is configured to create user home directories in the "/home" directory. $ find /home -perm -002 -type f -name ".[^.]*" -exec ls -ld {} \; If any local initialization files are found to reference world-writable files, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269303`

### Rule: AlmaLinux OS 9 must use a separate file system for /var/log.

**Rule ID:** `SV-269303r1050185_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Placing "/var/log" in its own partition enables better separation between log files and other files in "/var/".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a separate file system/partition has been created for "/var/log" with the following command: $ mount | grep ' /var/log ' /dev/mapper/luks-e0d162f5-fad8-463e-8e39-6bd09e672961 on /var/log type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota) If a separate entry for "/var/log" is not in use, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269304`

### Rule: AlmaLinux OS 9 must use a separate file system for /var.

**Rule ID:** `SV-269304r1050186_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Ensuring that "/var" is mounted on its own partition enables the setting of more restrictive mount options. This helps protect system services such as daemons or other programs which use it. It is not uncommon for the "/var" directory to contain world-writable directories installed by other software packages.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a separate file system/partition has been created for "/var" with the following command: $ mount | grep ' /var ' /dev/mapper/luks-b23d8276-7844-4e79-8a58-505150b6eb42 on /var type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota) If a separate entry for "/var" is not in use, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269305`

### Rule: AlmaLinux OS 9 must use a separate file system for /var/tmp.

**Rule ID:** `SV-269305r1050187_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "/var/tmp" partition is used as temporary storage by many programs. Placing "/var/tmp" in its own partition enables the setting of more restrictive mount options, which can help protect programs that use it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a separate file system/partition has been created for "/var/tmp" with the following command: $ mount | grep /var/tmp /dev/mapper/luks-0e7206e7-bfb1-4a23-ae14-b9cea7cf76d5 on /var/tmp type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota) If a separate entry for "/var/tmp" is not in use, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269306`

### Rule: AlmaLinux OS 9 must disable virtual system calls.

**Rule ID:** `SV-269306r1050188_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System calls are special routines in the Linux kernel, which userspace applications ask to do privileged tasks. Invoking a system call is an expensive operation because the processor must interrupt the currently executing task and switch context to kernel mode, and then switch back to userspace after the system call completes. Virtual system calls map a page into userspace that contains some variables and the implementation of some system calls. This allows the system calls to be executed in userspace to alleviate the context switching expense. Virtual system calls provide an opportunity of attack for a user who has control of the return instruction pointer. Disabling virtual system calls help to prevent return oriented programming (ROP) attacks via buffer overflows and overruns. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the current GRUB 2 configuration disables virtual system calls with the following command: $ grubby --info=ALL | grep args | grep -v 'vsyscall=none' If any output is returned, this is a finding. Check that virtual system calls are disabled by default to persist in kernel updates with the following command: $ grep vsyscall /etc/default/grub GRUB_CMDLINE_LINUX="vsyscall=none" If "vsyscall" is not set to "none", is missing or commented out, and is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269307`

### Rule: AlmaLinux OS 9 must use cron logging.

**Rule ID:** `SV-269307r1050189_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cron logging can be used to trace the successful or unsuccessful execution of cron jobs. It can also be used to spot intrusions into the use of the cron facility by unauthorized and malicious users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "rsyslog" is configured to log cron events with the following command: Note: If another logging package is used, substitute the utility configuration file for "/etc/rsyslog.conf" or "/etc/rsyslog.d/*.conf" files. $ grep -s cron /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.conf:*.info;mail.none;authpriv.none;cron.none /var/log/messages /etc/rsyslog.conf:# Log cron stuff /etc/rsyslog.conf:cron.* /var/log/cron If the command does not return a response, check for cron logging all facilities with the following command: $ grep -s /var/log/messages /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.conf:*.info;mail.none;authpriv.none;cron.none /var/log/messages If "rsyslog" is not logging messages for the cron facility or all facilities, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-269308`

### Rule: AlmaLinux OS 9 must be configured so that the rsyslog daemon does not accept log messages from other servers unless the server is being used for log aggregation.

**Rule ID:** `SV-269308r1050190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unintentionally running a rsyslog server accepting remote messages puts the system at increased risk. Malicious rsyslog messages sent to the server could exploit vulnerabilities in the server software itself, could introduce misleading information into the system's logs, or could fill the system's storage leading to a denial of service. If the system is intended to be a log aggregation server, its use must be documented with the information system security officer (ISSO).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is not configured to receive remote logs using rsyslog with the following commands: $ grep -i modload /etc/rsyslog.conf /etc/rsyslog.d/* $ModLoad imtcp $ModLoad imrelp $ grep -i serverrun /etc/rsyslog.conf /etc/rsyslog.d/* $InputTCPServerRun 514 $InputRELPServerRun 514 Note: An error regarding no files or directories may be returned. This is not a finding. If any lines are returned by the command, then rsyslog is configured to receive remote messages, and this is a finding. If any modules are being loaded in the "/etc/rsyslog.conf" file or in the "/etc/rsyslog.d" subdirectories, ask to view the documentation for the system being used for log aggregation. If the documentation does not exist or does not specify the server as a log aggregation system, this is a finding.

## Group: SRG-OS-000480-GPOS-00230

**Group ID:** `V-269309`

### Rule: AlmaLinux OS 9 must prevent files with the setuid and setgid bit set from being executed on file systems that contain user home directories.

**Rule ID:** `SV-269309r1050191_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access. Satisfies: SRG-OS-000480-GPOS-00230, SRG-OS-000368-GPOS-00154</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/home" is mounted with the "nosuid" option with the following command: Note: If a separate file system has not been created for the user home directories (user home directories are mounted under "/"), this is automatically a finding, as the "nosuid" option cannot be used on the "/" system. $ mount | grep /home /dev/mapper/luks-10a20c46-483d-4d12-831f-5328eda18fd1 on /home type xfs (rw,nosuid,nodev,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota) If the "/home" file system is mounted without the "nosuid" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-269310`

### Rule: AlmaLinux OS 9 must prevent device files from being interpreted on file systems that contain user home directories.

**Rule ID:** `SV-269310r1050192_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access. The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/home" is mounted with the "nodev" option with the following command: Note: If a separate file system has not been created for the user home directories (user home directories are mounted under "/"), this is automatically a finding, as the "nodev" option cannot be used on the "/" system. $ mount | grep /home /dev/mapper/luks-10a20c46-483d-4d12-831f-5328eea18fd1 on /home type xfs (rw,nosuid,nodev,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota) If the "/home" file system is mounted without the "nodev" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-269311`

### Rule: AlmaLinux OS 9 must prevent files with the setuid and setgid bit set from being executed on the /boot/efi directory.

**Rule ID:** `SV-269311r1050193_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system not to execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: For systems that use BIOS, this requirement is Not Applicable. Verify the /boot/efi directory is mounted with the "nosuid" option with the following command: $ mount | grep '\s/boot/efi\s' /dev/sda1 on /boot/efi type vfat (rw,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=ascii,shortname=winnt,errors=remount-ro) If the /boot/efi file system does not have the "nosuid" option set, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-269312`

### Rule: AlmaLinux OS 9 must mount /boot with the nodev option.

**Rule ID:** `SV-269312r1050194_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The only legitimate location for device files is the "/dev" directory located on the root partition. The only exception to this is chroot jails.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "/boot" mount point has the "nodev" option is with the following command: $ mount | grep '\s/boot\s' /dev/sda2 on /boot type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota) If the "/boot" file system does not have the "nodev" option set, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-269313`

### Rule: AlmaLinux OS 9 must prevent files with the setuid and setgid bit set from being executed on the /boot directory.

**Rule ID:** `SV-269313r1050195_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system not to execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the /boot directory is mounted with the "nosuid" option with the following command: $ mount | grep '\s/boot\s' /dev/sda2 on /boot type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota) If the /boot file system does not have the "nosuid" option set, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-269314`

### Rule: AlmaLinux OS 9 must mount /dev/shm with the nodev option.

**Rule ID:** `SV-269314r1050196_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access. The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/dev/shm" is mounted with the "nodev" option with the following command: $ mount | grep /dev/shm tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev,noexec,seclabel,size=2097152k,inode64) If the /dev/shm file system is mounted without the "nodev" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-269315`

### Rule: AlmaLinux OS 9 must mount /dev/shm with the noexec option.

**Rule ID:** `SV-269315r1050197_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/dev/shm" is mounted with the "noexec" option with the following command: $ mount | grep /dev/shm tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev,noexec,seclabel,size=2097152k,inode64) If the /dev/shm file system is mounted without the "noexec" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-269316`

### Rule: AlmaLinux OS 9 must mount /dev/shm with the nosuid option.

**Rule ID:** `SV-269316r1050198_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/dev/shm" is mounted with the "nosuid" option with the following command: $ mount | grep /dev/shm tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev,noexec,seclabel,size=2097152k,inode64) If the /dev/shm file system is mounted without the "noexec" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-269317`

### Rule: AlmaLinux OS 9 must mount /tmp with the nodev option.

**Rule ID:** `SV-269317r1050199_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access. The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/tmp" is mounted with the "nodev" option: $ mount | grep ' /tmp' tmpfs on /tmp type tmpfs (rw,nosuid,nodev,noexec,relatime,seclabel,size=2097152k,inode64) If the "/tmp" file system is mounted without the "nodev" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-269318`

### Rule: AlmaLinux OS 9 must mount /tmp with the noexec option.

**Rule ID:** `SV-269318r1050200_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/tmp" is mounted with the "noexec" option: $ mount | grep ' /tmp' tmpfs on /tmp type tmpfs (rw,nosuid,nodev,noexec,relatime,seclabel,size=2097152k,inode64) If the "/tmp" file system is mounted without the "noexec" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-269319`

### Rule: AlmaLinux OS 9 must mount /tmp with the nosuid option.

**Rule ID:** `SV-269319r1050201_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/tmp" is mounted with the "nosuid" option: $ mount | grep ' /tmp' tmpfs on /tmp type tmpfs (rw,nosuid,nodev,noexec,relatime,seclabel,size=2097152k,inode64) If the "/tmp" file system is mounted without the "nosuid" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-269320`

### Rule: AlmaLinux OS 9 must mount /var/log/audit with the nodev option.

**Rule ID:** `SV-269320r1050202_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access. The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/var/log/audit" is mounted with the "nodev" option: $ mount | grep /var/log/audit /dev/mapper/luks-29b74747-2f82-4472-82f5-0b5eb763effc on /var/log/audit type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota) If the "/var/log/audit" file system is mounted without the "nodev" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-269321`

### Rule: AlmaLinux OS 9 must mount /var/log/audit with the noexec option.

**Rule ID:** `SV-269321r1050203_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/var/log/audit" is mounted with the "noexec" option: $ mount | grep /var/log/audit /dev/mapper/luks-29b74747-2f82-4472-82f5-0b5eb763effc on /var/log/audit type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota) If the "/var/log/audit" file system is mounted without the "noexec" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-269322`

### Rule: AlmaLinux OS 9 must mount /var/log/audit with the nosuid option.

**Rule ID:** `SV-269322r1050204_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/var/log/audit" is mounted with the "nosuid" option: $ mount | grep /var/log/audit /dev/mapper/luks-29b74747-2f82-4472-82f5-0b5eb763effc on /var/log/audit type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota) If the "/var/log/audit" file system is mounted without the "nosuid" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-269323`

### Rule: AlmaLinux OS 9 must mount /var/log with the nodev option.

**Rule ID:** `SV-269323r1050205_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access. The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/var/log" is mounted with the "nodev" option: $ mount | grep '/var/log ' /dev/mapper/luks-e0d162f5-fad8-463e-8e39-6bd09e672961 on /var/log type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota) If the "/var/log" file system is mounted without the "nodev" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-269324`

### Rule: AlmaLinux OS 9 must mount /var/log with the noexec option.

**Rule ID:** `SV-269324r1050206_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/var/log" is mounted with the "noexec" option: $ mount | grep '/var/log ' /dev/mapper/luks-e0d162f5-fad8-463e-8e39-6bd09e672961 on /var/log type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota) If the "/var/log" file system is mounted without the "noexec" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-269325`

### Rule: AlmaLinux OS 9 must mount /var/log with the nosuid option.

**Rule ID:** `SV-269325r1050207_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/var/log" is mounted with the "nosuid" option: $ mount | grep '/var/log ' /dev/mapper/luks-e0d162f5-fad8-463e-8e39-6bd09e672961 on /var/log type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota) If the "/var/log" file system is mounted without the "nosuid" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-269326`

### Rule: AlmaLinux OS 9 must mount /var with the nodev option.

**Rule ID:** `SV-269326r1050208_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access. The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/var" is mounted with the "nodev" option: $ mount | grep ' /var ' /dev/mapper/luks-b23d8276-7844-4e79-8a58-505150b6eb42 on /var type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota) If the "/var" file system is mounted without the "nodev" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-269327`

### Rule: AlmaLinux OS 9 must mount /var/tmp with the nodev option.

**Rule ID:** `SV-269327r1050209_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nodev" mount option causes the system to not interpret character or block special devices. Executing character or block special devices from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access. The only legitimate location for device files is the "/dev" directory located on the root partition, with the exception of chroot jails if implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/var/tmp" is mounted with the "nodev" option: $ mount | grep /var/tmp /dev/mapper/luks-0e7206e7-bfb1-4a23-ae14-b9cea7cf76d5 on /var/tmp type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota) If the "/var/tmp" file system is mounted without the "nodev" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-269328`

### Rule: AlmaLinux OS 9 must mount /var/tmp with the noexec option.

**Rule ID:** `SV-269328r1050210_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "noexec" mount option causes the system to not execute binary files. This option must be used for mounting any file system not containing approved binary files, as they may be incompatible. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/var/tmp" is mounted with the "noexec" option: $ mount | grep /var/tmp /dev/mapper/luks-0e7206e7-bfb1-4a23-ae14-b9cea7cf76d5 on /var/tmp type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota) If the "/var/tmp" file system is mounted without the "noexec" option, this is a finding.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-269329`

### Rule: AlmaLinux OS 9 must mount /var/tmp with the nosuid option.

**Rule ID:** `SV-269329r1050211_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "nosuid" mount option causes the system to not execute "setuid" and "setgid" files with owner privileges. This option must be used for mounting any file system not containing approved "setuid" and "setguid" files. Executing files from untrusted file systems increases the opportunity for nonprivileged users to attain unauthorized administrative access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "/var/tmp" is mounted with the "nosuid" option: $ mount | grep /var/tmp /dev/mapper/luks-0e7206e7-bfb1-4a23-ae14-b9cea7cf76d5 on /var/tmp type xfs (rw,nosuid,nodev,noexec,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota) If the "/var/tmp" file system is mounted without the "nosuid" option, this is a finding.

## Group: SRG-OS-000370-GPOS-00155

**Group ID:** `V-269330`

### Rule: AlmaLinux OS 9 fapolicy module must be enabled.

**Rule ID:** `SV-269330r1050212_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as allowlisting. Utilizing an allowlist provides a configuration management method for allowing the execution of only authorized software. Using only authorized software decreases risk by limiting the number of potential vulnerabilities. Verification of allowlisted software occurs prior to execution or at system startup. User home directories/folders may contain information of a sensitive nature. Nonprivileged users should coordinate any sharing of information with a system administrator (SA) through shared resources. AlmaLinux OS 9 ships with many optional packages. One such package is a file access policy daemon called "fapolicyd". "fapolicyd" is a userspace daemon that determines access rights to files based on attributes of the process and file. It can be used to either blocklist or allowlist processes or file access. Proceed with caution with enforcing the use of this daemon. Improper configuration may render the system nonfunctional. The "fapolicyd" API is not namespace aware and can cause issues when launching or running containers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 fapolicyd is active with the following command: $ systemctl status fapolicyd fapolicyd.service - File Access Policy Daemon Loaded: loaded (/usr/lib/systemd/system/fapolicyd.service; enabled; preset: disabled) Active: active (running) since Thu 2024-02-08 09:42:05 UTC; 3h 38min ago If fapolicyd module is not active, this is a finding.

## Group: SRG-OS-000370-GPOS-00155

**Group ID:** `V-269331`

### Rule: AlmaLinux OS 9 fapolicy module must be installed.

**Rule ID:** `SV-269331r1050213_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must identify authorized software programs and permit execution of authorized software. The process used to identify software programs that are authorized to execute on organizational information systems is commonly referred to as allowlisting. Utilizing an allowlist provides a configuration management method for allowing the execution of only authorized software. Using only authorized software decreases risk by limiting the number of potential vulnerabilities. Verification of allowlisted software occurs prior to execution or at system startup. User home directories/folders may contain information of a sensitive nature. Nonprivileged users should coordinate any sharing of information with a system administrator (SA) through shared resources. AlmaLinux OS 9 ships with many optional packages. One such package is a file access policy daemon called "fapolicyd". "fapolicyd" is a userspace daemon that determines access rights to files based on attributes of the process and file. It can be used to either blocklist or allowlist processes or file access. Proceed with caution with enforcing the use of this daemon. Improper configuration may render the system nonfunctional. The "fapolicyd" API is not namespace aware and can cause issues when launching or running containers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 fapolicyd package is installed with the following command: $ dnf list --installed fapolicyd Installed Packages fapolicyd.x86_64 1.1.3-104.el9 @AppStream If the "fapolicyd" package is not installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269332`

### Rule: AlmaLinux OS 9 must disable remote management of the chrony daemon.

**Rule ID:** `SV-269332r1050214_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Not exposing the management interface of the chrony daemon on the network reduces the attack surface.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 disables remote management of the chrony daemon with the following command: $ chronyd -p | grep -w cmdport cmdport 0 If the "cmdport" option is not set to "0" or is missing, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269333`

### Rule: AlmaLinux OS 9 must prevent the chrony daemon from acting as a server.

**Rule ID:** `SV-269333r1050215_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Being able to determine the system time of a server can be useful information for various attacks from timebomb attacks to location discovery based on time zone. Minimizing the exposure of the server functionality of the chrony daemon reduces the attack surface.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 disables the chrony daemon from acting as a server with the following command: $ chronyd -p | grep -w port port 0 If the "port" option is not set to "0" or is missing, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269334`

### Rule: AlmaLinux OS 9 must not have the iprutils package installed.

**Rule ID:** `SV-269334r1050216_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The iprutils package provides a suite of utilities to manage and configure SCSI devices supported by the ipr SCSI storage device driver.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the iprutils package is not installed with the following command: $ dnf list --installed iprutils Error: No matching Packages to list If the "iprutils" package is installed and is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269335`

### Rule: AlmaLinux OS 9 must not have the quagga package installed.

**Rule ID:** `SV-269335r1050217_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Quagga is a network routing software suite providing implementations of Open Shortest Path First (OSPF), Routing Information Protocol (RIP), Border Gateway Protocol (BGP) for Unix and Linux platforms. If there is no need to make the router software available, removing it provides a safeguard against its activation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the quagga package is not installed with the following command: $ dnf list --installed quagga Error: No matching Packages to list If the "quagga" package is installed, and is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269336`

### Rule: AlmaLinux OS 9 must not have the sendmail package installed.

**Rule ID:** `SV-269336r1050218_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The sendmail software was not developed with security in mind, and its design prevents it from being effectively contained by SELinux. Postfix must be used instead.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the sendmail package is not installed with the following command: $ dnf list --installed sendmail Error: No matching Packages to list If the "sendmail" package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269337`

### Rule: AlmaLinux OS 9 must not have the telnet-server package installed.

**Rule ID:** `SV-269337r1050219_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities are often overlooked and therefore, may remain unsecure. They increase the risk to the platform by providing additional attack vectors. The telnet service provides an unencrypted remote access service, which does not provide for the confidentiality and integrity of user passwords or the remote session. If a privileged user were to login using this service, the privileged user password could be compromised. Removing the "telnet-server" package decreases the risk of accidental (or intentional) activation of the telnet service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the telnet-server package is not installed with the following command: $ dnf list --installed telnet-server Error: No matching Packages to list If the "telnet-server" package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269338`

### Rule: AlmaLinux OS 9 must not have a Trivial File Transfer Protocol (TFTP) client package installed.

**Rule ID:** `SV-269338r1050220_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If TFTP is required for operational support (such as transmission of router configurations), its use must be documented with the information systems security manager (ISSM), restricted to only authorized personnel, and have access control rules established.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the tftp package is not installed with the following command: $ dnf list --installed tftp If the "tftp" package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269339`

### Rule: AlmaLinux OS 9 must not have the cups package installed.

**Rule ID:** `SV-269339r1050221_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The cups package provides printer drivers as well as a print server, webserver, and discovery mechanisms. Removing the package reduces the potential attack surface.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the cups package is not installed with the following command: $ dnf list –installed cups Error: No matching Packages to list If the "cups" package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269340`

### Rule: AlmaLinux OS 9 must not have the gssproxy package installed.

**Rule ID:** `SV-269340r1050222_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The gssproxy package is a proxy for GSS API credential handling and could expose secrets on some networks. It is not needed for normal function of the OS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the gssproxy package is not installed with the following command: $ dnf list --installed gssproxy Error: No matching Packages to list If the "gssproxy" package is installed and is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269341`

### Rule: AlmaLinux OS 9 must disable the Asynchronous Transfer Mode (ATM) kernel module.


**Rule ID:** `SV-269341r1050223_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ATM is a transport layer protocol designed for digital transmission of multiple types of traffic, including telephony (voice), data, and video signals, in one network without the use of separate overlay networks. Disabling ATM protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 disables the ability to load the atm kernel module with the following command: $ grep -r atm /etc/modprobe.conf /etc/modprobe.d/* /etc/modprobe.d/atm.conf:install atm /bin/false /etc/modprobe.d/atm.conf:blacklist atm If the command does not return any output, or the line is commented out, and use of atm is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269342`

### Rule: AlmaLinux OS 9 must be configured to disable Bluetooth.

**Rule ID:** `SV-269342r1050224_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement applies to wireless peripheral technologies (e.g., wireless mice, keyboards, displays, etc.) used with AlmaLinux OS 9 systems. Wireless peripherals (e.g., Wi-Fi/Bluetooth/IR keyboards, mice and pointing devices, and near field communications [NFC]) present a unique challenge by creating an open, unsecured port on a computer. Wireless peripherals must meet DOD requirements for wireless data transmission and be approved for use by the authorizing official (AO). Even though some wireless peripherals, such as mice and pointing devices, do not ordinarily carry information that need to be protected, modification of communications with these wireless peripherals may be used to compromise the AlmaLinux OS 9 operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 disables the ability to load the Bluetooth kernel module with the following command: $ grep -r bluetooth /etc/modprobe.conf /etc/modprobe.d/* /etc/modprobe.d/bluetooth.conf:install bluetooth /bin/false /etc/modprobe.d/bluetooth.conf:blacklist bluetooth If the command does not return any output, or the line is commented out, and use of Bluetooth is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269343`

### Rule: AlmaLinux OS 9 must disable the Controller Area Network (CAN) kernel module.


**Rule ID:** `SV-269343r1050225_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The CAN protocol is a robust vehicle bus standard designed to allow microcontrollers and devices to communicate with each other's applications without a host computer. Disabling CAN protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 disables the ability to load the can kernel module with the following command: $ grep -r can /etc/modprobe.conf /etc/modprobe.d/* /etc/modprobe.d/can.conf:install can /bin/false /etc/modprobe.d/can.conf:blacklist can If the command does not return any output, or the line is commented out, and use of CAN is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269344`

### Rule: AlmaLinux OS 9 must disable mounting of cramfs.

**Rule ID:** `SV-269344r1050226_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Removing support for unneeded filesystem types reduces the local attack surface of the server. Compressed ROM/RAM file system (or cramfs) is a read-only file system designed for simplicity and space-efficiency. It is mainly used in embedded and small-footprint systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 disables the ability to load the cramfs kernel module with the following command: $ grep cramfs /etc/modprobe.conf /etc/modprobe.d/* blacklist cramfs If the command does not return any output, or the line is commented out, and use of cramfs is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269345`

### Rule: AlmaLinux OS 9 must disable the Stream Control Transmission Protocol (SCTP) kernel module.


**Rule ID:** `SV-269345r1050227_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The SCTP is a transport layer protocol, designed to support the idea of message-oriented communication, with several streams of messages within one connection. Disabling SCTP protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 disables the ability to load the SCTP kernel module with the following command: $ grep -r sctp /etc/modprobe.conf /etc/modprobe.d/* /etc/modprobe.d/sctp.conf:install sctp /bin/false /etc/modprobe.d/sctp.conf:blacklist sctp If the command does not return any output, or the line is commented out, and use of SCTP is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269346`

### Rule: AlmaLinux OS 9 must disable mounting of squashfs.

**Rule ID:** `SV-269346r1050228_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Removing support for unneeded filesystem types reduces the local attack surface of the server. A squashfs compressed filesystem image can be mounted without first decompressing the image. Note that Snap packages use squashfs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 disables the ability to load the squashfs kernel module with the following command: $ grep squashfs /etc/modprobe.conf /etc/modprobe.d/* blacklist squashfs If the command does not return any output, or the line is commented out, and use of squashfs is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269347`

### Rule: AlmaLinux OS 9 must disable the Transparent Inter Process Communication (TIPC) kernel module.

**Rule ID:** `SV-269347r1050229_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Failing to disconnect unused protocols can result in a system compromise. The TIPC is a protocol that is specially designed for intra-cluster communication. It can be configured to transmit messages either on UDP or directly across Ethernet. Message delivery is sequence guaranteed, loss free and flow controlled. Disabling TIPC protects the system against exploitation of any flaws in its implementation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 disables the ability to load the TIPC kernel module with the following command: $ grep -r tipc /etc/modprobe.conf /etc/modprobe.d/* /etc/modprobe.d/tipc.conf:install tipc /bin/false /etc/modprobe.d/tipc.conf:blacklist tipc If the command does not return any output, or the line is commented out, and use of TIPC is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269348`

### Rule: AlmaLinux OS 9 must disable mounting of udf.

**Rule ID:** `SV-269348r1050230_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Removing support for unneeded filesystem types reduces the local attack surface of the server. The UDF filesystem is used to write DVDs and so could assist in data exfiltration, the so-called "sneakernet". Note that Microsoft Azure uses UDF.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 disables the ability to load the udf kernel module with the following command: $ grep udf /etc/modprobe.conf /etc/modprobe.d/* blacklist udf If the command does not return any output, or the line is commented out, and use of UDF is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269349`

### Rule: Cameras must be disabled or covered when not in use.

**Rule ID:** `SV-269349r1050232_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Failing to disconnect from collaborative computing devices (i.e., cameras) can result in subsequent compromises of organizational information. Providing easy methods to physically disconnect from such devices after a collaborative computing session helps to ensure participants actually carry out the disconnect activity without having to go through complex and tedious procedures; it also ensures that microphones built into the cameras are also disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system disables the ability to load the uvcvideo kernel module: $ grep -r uvcvideo /etc/modprobe.conf /etc/modprobe.d/* /etc/modprobe.d/uvcvideo.conf:install uvcvideo /bin/false /etc/modprobe.d/uvcvideo.conf:blacklist uvcvideo If the command does not return any output, or either line is commented out, and the collaborative computing device has not been authorized for use, this is a finding. If a built-in camera is not protected with a cover or is not physically disabled, this is a finding. For an external camera, if there is not a method for the operator to manually disconnect the camera (e.g., unplug, power off) at the end of collaborative computing sessions, this is a finding. If the device or operating system does not have a camera installed, this requirement is not applicable.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269350`

### Rule: AlmaLinux OS 9 must not have the nfs-utils package installed.

**Rule ID:** `SV-269350r1050233_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>"nfs-utils" provides a daemon for the kernel Network File System (NFS) server and related tools. This package also contains the "showmount" program. "showmount" queries the mount daemon on a remote host for information about the NFS server on the remote host. For example, "showmount" can display the clients that are mounted on that host.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the nfs-utils package is not installed with the following command: $ dnf list --installed nfs-utils Error: No matching Packages to list If the "nfs-utils" package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269351`

### Rule: AlmaLinux OS 9 must not have the rsh package installed.

**Rule ID:** `SV-269351r1050234_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "rsh" package provides a client for several obsolete and insecure network services. Removing it decreases the risk of accidental (or intentional) use of those services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the rsh package is not installed with the following command: $ dnf list --installed rsh Error: No matching Packages to list If the "rsh" package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269352`

### Rule: AlmaLinux OS 9 must not have the rsh-server package installed.

**Rule ID:** `SV-269352r1050235_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "rsh-server" service provides unencrypted remote access service, which does not provide for the confidentiality and integrity of user passwords or the remote session and has very weak authentication. If a privileged user were to login using this service, the privileged user password could be compromised. The "rsh-server" package provides several obsolete and insecure network services. Removing it decreases the risk of accidental (or intentional) activation of those services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the rsh-server package is not installed with the following command: $ dnf list --installed rsh-server Error: No matching Packages to list If the "rsh-server" package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269353`

### Rule: AlmaLinux OS 9 must not have the tuned package installed.

**Rule ID:** `SV-269353r1050236_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The tuned package contains a daemon that tunes the system settings dynamically. It does so by monitoring the usage of several system components periodically. Based on that information, components will then be put into lower or higher power savings modes to adapt to the current usage. The tuned package is not needed for normal OS operations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the tuned package is not installed with the following command: $ dnf list --installed tuned Error: No matching Packages to list If the "tuned" package is installed and is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269354`

### Rule: A graphical display manager must not be installed on AlmaLinux OS 9 unless approved.


**Rule ID:** `SV-269354r1050237_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unnecessary service packages must not be installed to decrease the attack surface of the system. Graphical display managers have a long history of security vulnerabilities and must not be used, unless approved and documented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a graphical user interface is not installed with the following command: $ dnf list --installed "xorg-x11-server-common" Error: No matching Packages to list If the "xorg-x11-server-common" package is installed, and the use of a graphical user interface has not been documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269355`

### Rule: AlmaLinux OS 9 must not have the ypserv package installed.

**Rule ID:** `SV-269355r1050238_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The NIS service provides an unencrypted authentication service, which does not provide for the confidentiality and integrity of user passwords or the remote session. Removing the "ypserv" package decreases the risk of the accidental (or intentional) activation of NIS or NIS+ services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the ypserv package is not installed with the following command: $ dnf list --installed ypserv Error: No matching Packages to list If the "ypserv" package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269356`

### Rule: AlmaLinux OS 9 must not have the avahi package installed.

**Rule ID:** `SV-269356r1050239_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The avahi package provides the zeroconf capability to discover remote services such as printers and announce itself as a service for sharing files and devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the avahi package is not installed with the following command: $ dnf list –installed avahi Error: No matching Packages to list If the "avahi" package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-269357`

### Rule: AlmaLinux OS 9 must be configured to disable USB mass storage.

**Rule ID:** `SV-269357r1050240_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>USB mass storage permits easy introduction of unknown devices, thereby facilitating malicious activity. Satisfies: SRG-OS-000095-GPOS-00049, SRG-OS-000378-GPOS-00163, SRG-OS-000114-GPOS-00059, SRG-OS-000690-GPOS-00140</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 disables the ability to load the USB Storage kernel module with the following command: $ grep -r usb-storage /etc/modprobe.conf /etc/modprobe.d/* /etc/modprobe.d/usb-storage.conf:install usb-storage /bin/false /etc/modprobe.d/usb-storage.conf:blacklist usb-storage If the command does not return any output, or the line is commented out, and use of usb-storage is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-269358`

### Rule: AlmaLinux OS 9 must have the firewalld package installed.

**Rule ID:** `SV-269358r1050241_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>"Firewalld" provides an easy and effective way to block/limit remote access to the system via ports, services, and protocols. Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. AlmaLinux OS 9 functionality (e.g., SSH) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets). Satisfies: SRG-OS-000096-GPOS-00050, SRG-OS-000298-GPOS-00116, SRG-OS-000297-GPOS-00115</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the firewalld package is installed with the following command: $ dnf list --installed firewalld Installed Packages firewalld.noarch 1.2.1-1.el9 @anaconda If the "firewalld" package is not installed, this is a finding.

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-269359`

### Rule: AlmaLinux OS 9 must require users to provide authentication for privilege escalation.

**Rule ID:** `SV-269359r1101824_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without re-authentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the user re-authenticate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "/etc/sudoers" has no occurrences of "!authenticate" with the following command: $ sudo egrep -iR '!authenticate' /etc/sudoers /etc/sudoers.d/ If any occurrences of "!authenticate" are returned, this is a finding.

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-269360`

### Rule: AlmaLinux OS 9 must require users to provide a password for privilege escalation.

**Rule ID:** `SV-269360r1101822_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without re-authentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the user re-authenticate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the sudo configuration files have no occurrences of "NOPASSWD" with the following command: $ sudo grep -iR 'NOPASSWD' /etc/sudoers /etc/sudoers.d/ If any occurrences of "NOPASSWD" are returned from the command and have not been documented with the information systems security officer (ISSO) as an organizationally defined administrative group using multifactor authentication (MFA), this is a finding.

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-269361`

### Rule: AlmaLinux OS 9 must not be configured to bypass password requirements for privilege escalation.

**Rule ID:** `SV-269361r1050244_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without re-authentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the user re-authenticate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system is not configured to bypass password requirements for privilege escalation with the following command: $ grep pam_succeed_if /etc/pam.d/sudo If any occurrences of "pam_succeed_if" are returned, this is a finding.

## Group: SRG-OS-000327-GPOS-00127

**Group ID:** `V-269362`

### Rule: AlmaLinux OS 9 must require reauthentication when using the "sudo" command.

**Rule ID:** `SV-269362r1050245_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without re-authentication, users may access resources or perform tasks for which they do not have authorization. When operating systems provide the capability to escalate a functional capability, it is critical the user re-authenticate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 requires reauthentication when using the "sudo" command to elevate privileges with the following command: $ grep timestamp_timeout /etc/sudoers /etc/sudoers.d/* /etc/sudoers.d/01_stig:Defaults timestamp_timeout=0 If "timestamp_timeout" is set to a negative number, is commented out, conflicting results or no results are returned, this is a finding.

## Group: SRG-OS-000109-GPOS-00056

**Group ID:** `V-269363`

### Rule: AlmaLinux OS 9 must restrict the use of the "su" command.

**Rule ID:** `SV-269363r1050246_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "su" program provides a "switch user" capability. It is commonly used to become root but can be used to switch to any user. Limiting access to such commands is considered a good security practice. Satisfies: SRG-OS-000109-GPOS-00056, SRG-OS-000312-GPOS-00124, SRG-OS-000312-GPOS-00122, SRG-OS-000312-GPOS-00123</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 requires uses to be members of the "wheel" group with the following command: $ grep pam_wheel /etc/pam.d/su auth required pam_wheel.so use_uid If a line for "pam_wheel.so" does not exist, or is commented out, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-269364`

### Rule: Groups must have unique Group IDs (GIDs).

**Rule ID:** `SV-269364r1050247_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 contains no duplicate GIDs with the following command: $ cut -f3 -d":" /etc/group | uniq -d If the system has duplicate GIDs, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-269365`

### Rule: Duplicate User IDs (UIDs) must not exist for interactive users.

**Rule ID:** `SV-269365r1050248_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. Satisfies: SRG-OS-000104-GPOS-00051, SRG-OS-000121-GPOS-00062</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 contains no duplicate UIDs for interactive users with the following command: $ cut -f3 -d":" /etc/passwd | uniq -d If output is produced and the UIDs listed are for interactive user accounts, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-269366`

### Rule: All AlmaLinux OS 9 interactive users must have a primary group that exists.


**Rule ID:** `SV-269366r1050249_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a user is assigned the Group Identifier (GID) of a group that does not exist on the system, and a group with the GID is subsequently created, the user may have unintended rights to any files associated with the group.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all AlmaLinux OS 9 interactive users have a valid GID with the following command: $ pwck -r /etc/passwd If the system has any interactive users with a nonexistent primary group, this is a finding.

## Group: SRG-OS-000105-GPOS-00052

**Group ID:** `V-269367`

### Rule: AlmaLinux OS 9 SSHD must accept public key authentication.

**Rule ID:** `SV-269367r1050250_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: 1) something a user knows (e.g., password/PIN); 2) something a user has (e.g., cryptographic identification device, token); and 3) something a user is (e.g., biometric). A privileged account is defined as an information system account with authorizations of a privileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the internet). The DOD CAC with DOD-approved PKI is an example of multifactor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system administrator (SA) demonstrates the use of an approved alternate multifactor authentication method, this requirement is Not Applicable. Verify that AlmaLinux OS 9 SSH daemon accepts public key encryption with the following command: $ sshd -T | grep -i pubkeyauthentication pubkeyauthentication yes If "PubkeyAuthentication" is set to no, or the line is missing, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-269368`

### Rule: AlmaLinux OS 9 must have the opensc package installed.

**Rule ID:** `SV-269368r1050614_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a CAC or token that is separate from the information system, ensures that even if the information system is compromised, that compromise will not affect credentials stored on the authentication device. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification card and the DOD Common Access Card. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., VPN, proxy capability). This does not apply to authentication for the purpose of configuring the device itself (management). This requires further clarification from NIST.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 has the opensc package installed with the following command: $ dnf list --installed opensc Installed Packages opensc.x86_64 0.22.0-2.el9 @anaconda If the "opensc" package is not installed, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-269369`

### Rule: The pcscd socket on AlmaLinux OS 9 must be active.

**Rule ID:** `SV-269369r1050615_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a CAC or token that is separate from the information system, ensures that even if the information system is compromised, that compromise will not affect credentials stored on the authentication device. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification card and the DOD Common Access Card. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., VPN, proxy capability). This does not apply to authentication for the purpose of configuring the device itself (management). This requires further clarification from NIST.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "pcscd" socket is active with the following command: $ systemctl status pcscd.socket pcscd.socket - PC/SC Smart Card Daemon Activation Socket Loaded: loaded (/usr/lib/systemd/system/pcscd.socket; enabled; preset: enabled) Active: active (listening) since Thu 2024-04-11 16:03:24 BST; 2 weeks 3 days ago Triggers: pcscd.service Listen: /run/pcscd/pcscd.comm (Stream) CGroup: /system.slice/pcscd.socket If the pcscd.socket is not active, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-269370`

### Rule: AlmaLinux OS 9 must have the pcsc-lite package installed.

**Rule ID:** `SV-269370r1050616_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a CAC or token that is separate from the information system, ensures that even if the information system is compromised, that compromise will not affect credentials stored on the authentication device. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification card and the DOD Common Access Card. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., VPN, proxy capability). This does not apply to authentication for the purpose of configuring the device itself (management). This requires further clarification from NIST.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the System Administrator demonstrates the use of an approved alternate multifactor authentication method, this requirement is Not Applicable. Verify that AlmaLinux OS 9 has the pcsc-lite package installed with the following command: $ dnf list --installed pcsc-lite Installed Packages pcsc-lite.x86_64 1.9.4-1.el9 @anaconda If the "pcsc-lite" package is not installed, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-269371`

### Rule: AlmaLinux OS 9 must implement certificate status checking for multifactor authentication.

**Rule ID:** `SV-269371r1050254_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a DOD Common Access Card (CAC) or token that is separate from the information system, ensures that even if the information system is compromised, credentials stored on the authentication device will not be affected. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification (PIV) card and the DOD CAC. AlmaLinux OS 9 includes multiple options for configuring certificate status checking, but for this requirement focuses on the System Security Services Daemon (SSSD). By default, SSSD performs Online Certificate Status Protocol (OCSP) checking and certificate verification using a sha256 digest function.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system administrator (SA) demonstrates the use of an approved alternate multifactor authentication method, this requirement is Not Applicable. Verify the operating system implements Online Certificate Status Protocol (OCSP) and is using the proper digest value on the system with the following command: $ grep certificate_verification /etc/sssd/sssd.conf /etc/sssd/conf.d/*.conf /etc/sssd/conf.d/certificate_verification.conf:certificate_verification = ocsp_dgst=sha512 If the certificate_verification line is missing from the [sssd] section, or is missing "ocsp_dgst=sha512", ask the administrator to indicate what type of multifactor authentication is being used and how the system implements certificate status checking. If there is no evidence of certificate status checking being used, this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-269372`

### Rule: AlmaLinux OS 9 must enable certificate based smart card authentication.

**Rule ID:** `SV-269372r1050617_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a CAC or token that is separate from the information system, ensures that even if the information system is compromised, that compromise will not affect credentials stored on the authentication device. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification card and the DOD Common Access Card. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., VPN, proxy capability). This does not apply to authentication for the purpose of configuring the device itself (management). This requires further clarification from NIST. Satisfies: SRG-OS-000375-GPOS-00160, SRG-OS-000105-GPOS-00052, SRG-OS-000705-GPOS-00150</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the System Administrator demonstrates the use of an approved alternate multifactor authentication method, this requirement is Not Applicable. Verify that AlmaLinux OS 9 has smart cards are enabled in System Security Services Daemon (SSSD), run the following command: $ grep pam_cert_auth /etc/sssd/sssd.conf /etc/sssd/conf.d/*.conf /etc/sssd/conf.d/certificate_verification.conf:pam_cert_auth = True If "pam_cert_auth" is not set to "True", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000377-GPOS-00162

**Group ID:** `V-269373`

### Rule: AlmaLinux OS 9 must have the openssl-pkcs11 package installed.

**Rule ID:** `SV-269373r1050256_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. DOD has mandated the use of the CAC to support identity management and personal authentication for systems covered under Homeland Security Presidential Directive (HSPD) 12, as well as making the CAC a primary component of layered protection for national security systems. Satisfies: SRG-OS-000377-GPOS-00162, SRG-OS-000376-GPOS-00161, SRG-OS-000375-GPOS-00160, SRG-OS-000105-GPOS-00052</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the System Administrator demonstrates the use of an approved alternate multifactor authentication method, this requirement is Not Applicable. Verify that AlmaLinux OS 9 has the openssl-pkcs11 package installed with the following command: $ dnf list --installed openssl-pkcs11 Installed Packages openssl-pkcs11.x86_64 0.4.11-7.el9 @baseos If the "openssl-pkcs11" package is not installed, this is a finding.

## Group: SRG-OS-000106-GPOS-00053

**Group ID:** `V-269374`

### Rule: AlmaLinux OS 9 SSHD must not allow blank passwords.

**Rule ID:** `SV-269374r1050257_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log on and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments. Satisfies: SRG-OS-000106-GPOS-00053, SRG-OS-000108-GPOS-00055</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 remote access using SSH prevents logging on with a blank password with the following command: $ sshd -T | grep -i permitemptypasswords permitemptypasswords no If "PermitEmptyPasswords" is set to "yes", or the line is missing, this is a finding.

## Group: SRG-OS-000107-GPOS-00054

**Group ID:** `V-269375`

### Rule: AlmaLinux OS 9 must use the CAC smart card driver.

**Rule ID:** `SV-269375r1050258_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Smart card login provides two-factor authentication stronger than that provided by a username and password combination. Smart cards leverage public key infrastructure to provide and verify credentials. Configuring the smart card driver in use by the organization helps to prevent users from using unauthorized smart cards. Satisfies: SRG-OS-000107-GPOS-00054, SRG-OS-000108-GPOS-00055, SRG-OS-000112-GPOS-00057, SRG-OS-000113-GPOS-00058</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 loads the CAC driver with the following command: $ grep card_drivers /etc/opensc.conf card_drivers = cac; If "cac" is not listed as a card driver, or there is no line returned for "card_drivers", this is a finding.

## Group: SRG-OS-000109-GPOS-00056

**Group ID:** `V-269376`

### Rule: AlmaLinux OS 9 must not permit direct logons to the root account using remote access via SSH.

**Rule ID:** `SV-269376r1050259_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Even though the communications channel may be encrypted, an additional layer of security is gained by extending the policy of not logging directly on as root. In addition, logging in with a user-specific account provides individual accountability of actions performed on the system. The root account is a known default username, so should not allow direct login as half of the username/password combination is known, making it vulnerable to brute-force password guessing attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 prevents users from logging on directly as "root" over SSH with the following command: $ sshd -T |grep -I permitrootlogin permitrootlogin no If the "PermitRootLogin" keyword is set to "yes" or "without-password", this is a finding.

## Group: SRG-OS-000378-GPOS-00163

**Group ID:** `V-269377`

### Rule: AlmaLinux OS 9 must disable the graphical user interface automount function unless required.

**Rule ID:** `SV-269377r1050260_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatically mounting file systems permits easy introduction of unknown devices, thereby facilitating malicious activity. Satisfies: SRG-OS-000378-GPOS-00163, SRG-OS-000114-GPOS-00059</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the AlmaLinux OS 9 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify AlmaLinux OS 9 disables the graphical user interface automount function with the following command: $ gsettings get org.gnome.desktop.media-handling automount-open false If "automount-open" is set to "true", and is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.

## Group: SRG-OS-000378-GPOS-00163

**Group ID:** `V-269378`

### Rule: AlmaLinux OS 9 must prevent a user from overriding the disabling of the graphical user interface automount function.

**Rule ID:** `SV-269378r1050261_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatically mounting file systems permits easy introduction of unknown devices, thereby facilitating malicious activity. Satisfies: SRG-OS-000378-GPOS-00163, SRG-OS-000114-GPOS-00059</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the AlmaLinux OS 9 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify AlmaLinux OS 9 disables ability of the user to override the graphical user interface automount setting. Determine which profile the system database is using with the following command: $ grep system-db /etc/dconf/profile/user system-db:local Check that the automount setting is locked from nonprivileged user modification with the following command: Note: The example below is using the database "local" for the system, so the path is "/etc/dconf/db/local.d". This path must be modified if a database other than "local" is being used. $ grep 'automount-open' /etc/dconf/db/local.d/locks/* /org/gnome/desktop/media-handling/automount-open If the command does not return at least the example result, this is a finding.

## Group: SRG-OS-000378-GPOS-00163

**Group ID:** `V-269379`

### Rule: AlmaLinux OS 9 must prevent a user from overriding the disabling of the graphical user interface autorun function.

**Rule ID:** `SV-269379r1050262_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatically mounting filesystems and running applications upon insertion of a device facilitates malicious activity. Satisfies: SRG-OS-000378-GPOS-00163, SRG-OS-000114-GPOS-00059</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement assumes the use of the AlmaLinux OS 9 default graphical user interface, the GNOME desktop environment. If the system does not have any graphical user interface installed, this requirement is Not Applicable. Verify AlmaLinux OS 9 disables ability of the user to override the graphical user interface autorun setting. Determine which profile the system database is using with the following command: $ grep system-db /etc/dconf/profile/user system-db:local Check that the automount setting is locked from nonprivileged user modification with the following command: Note: The example below is using the database "local" for the system, so the path is "/etc/dconf/db/local.d". This path must be modified if a database other than "local" is being used. $ grep 'autorun-never' /etc/dconf/db/local.d/locks/* /org/gnome/desktop/media-handling/autorun-never If the command does not return at least the example result, this is a finding.

## Group: SRG-OS-000378-GPOS-00163

**Group ID:** `V-269380`

### Rule: AlmaLinux OS 9 must have the USBGuard package installed.

**Rule ID:** `SV-269380r1050263_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The USBGuard-daemon is the main component of the USBGuard software framework. It runs as a service in the background and enforces the USB device authorization policy for all USB devices. The policy is defined by a set of rules using a rule language described in the usbguard-rules.conf file. The policy and the authorization state of USB devices can be modified during runtime using the USBGuard tool. The system administrator (SA) must work with the site information system security officer (ISSO) to determine a list of authorized peripherals and establish rules within the USBGuard software framework to allow only authorized devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system is virtual machine with no virtual or physical USB peripherals attached, this is not a finding. Verify USBGuard is installed on the operating system with the following command: $ dnf list installed usbguard Installed Packages usbguard.x86_64 1.0.0-15.el9 @AppStream If the USBGuard package is not installed, ask the SA to indicate how unauthorized peripherals are being blocked. If there is no evidence that unauthorized peripherals are being blocked before establishing a connection, this is a finding.

## Group: SRG-OS-000378-GPOS-00163

**Group ID:** `V-269381`

### Rule: AlmaLinux OS 9 must have the USBGuard package enabled.

**Rule ID:** `SV-269381r1050264_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The USBGuard-daemon is the main component of the USBGuard software framework. It runs as a service in the background and enforces the USB device authorization policy for all USB devices. The policy is defined by a set of rules using a rule language described in the usbguard-rules.conf file. The policy and the authorization state of USB devices can be modified during runtime using the USBGuard tool. The system administrator (SA) must work with the site information system security officer (ISSO) to determine a list of authorized peripherals and establish rules within the USBGuard software framework to allow only authorized devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system is virtual machine with no virtual or physical USB peripherals attached, this is not a finding. Verify AlmaLinux OS 9 has USBGuard enabled with the following command: $ systemctl status usbguard usbguard.service - USBGuard daemon Loaded: loaded (/usr/lib/systemd/system/usbguard.service; enabled; preset: disabled) Active: active (running) since Thu 2024-02-08 09:42:05 UTC; 1h 24min ago If USBGuard is not active, ask the SA to indicate how unauthorized peripherals are being blocked. If there is no evidence that unauthorized peripherals are being blocked before establishing a connection, this is a finding.

## Group: SRG-OS-000378-GPOS-00163

**Group ID:** `V-269382`

### Rule: AlmaLinux OS 9 must block unauthorized peripherals before establishing a connection.

**Rule ID:** `SV-269382r1050265_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The USBGuard-daemon is the main component of the USBGuard software framework. It runs as a service in the background and enforces the USB device authorization policy for all USB devices. The policy is defined by a set of rules using a rule language described in the usbguard-rules.conf file. The policy and the authorization state of USB devices can be modified during runtime using the USBGuard tool. The system administrator (SA) must work with the site information system security officer (ISSO) to determine a list of authorized peripherals and establish rules within the USBGuard software framework to allow only authorized devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system is virtual machine with no virtual or physical USB peripherals attached, this is not a finding. Verify the USBGuard has a policy configured with the following command: $ usbguard list-rules 1: allow id 1d6b:0002 serial "0000:03:00.0" name "xHCI Host Controller" with-interface 09:00:00 with-connect-type "" 2: allow id 1d6b:0003 serial "0000:03:00.0" name "xHCI Host Controller" with-interface 09:00:00 with-connect-type "" 3: allow id 0627:0001 serial "28754-0000:00:02.2:00.0-1" name "QEMU USB Tablet" with-interface 03:00:00 with-connect-type "unknown" If the command does not return results or an error is returned, ask the SA to indicate how unauthorized peripherals are being blocked. If there is no evidence that unauthorized peripherals are being blocked before establishing a connection, this is a finding.

## Group: SRG-OS-000379-GPOS-00164

**Group ID:** `V-269383`

### Rule: AlmaLinux OS 9 must not have the autofs package installed.

**Rule ID:** `SV-269383r1050266_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. Bidirectional authentication solutions include, but are not limited to, IEEE 802.1x and Extensible Authentication Protocol (EAP), RADIUS server with EAP-Transport Layer Security (TLS) authentication, Kerberos, and SSL mutual authentication. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area network, wide area network, or the internet). A remote connection is any connection with a device communicating through an external network (e.g., the internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply this requirement to those limited number (and type) of devices that truly need to support this capability. Satisfies: SRG-OS-000379-GPOS-00164, SRG-OS-000114-GPOS-00059</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the autofs service is not installed, this requirement is Not Applicable. Verify that the autofs package is not installed with the following command: $ dnf list --installed autofs Error: No matching Packages to list If the "autofs" package is installed, and is not documented as an operational requirement with the information system security officer (ISSO), this is a finding.

## Group: SRG-OS-000118-GPOS-00060

**Group ID:** `V-269384`

### Rule: AlmaLinux OS 9 must disable account identifiers (individuals, groups, roles, and devices) after 35 days of inactivity.

**Rule ID:** `SV-269384r1050267_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Automatically disabling inactive accounts ensures that accounts which may not have been responsibly removed are not available to threat actors who may have compromised their credentials. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 account identifiers (individuals, groups, roles, and devices) are disabled after 35 days of inactivity with the following command: $ useradd -D | grep INACTIVE INACTIVE=35 If the value of "INACTIVE" is set to "-1", a value greater than "35", or is missing, this is a finding.

## Group: SRG-OS-000070-GPOS-00038

**Group ID:** `V-269385`

### Rule: AlmaLinux OS 9 must enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-269385r1050268_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 enforces password complexity by requiring at least one lowercase character with the following command: $ grep -r lcredit /etc/security/pwquality.conf* /etc/security/pwquality.conf.d/stig.conf:lcredit = -1 If the value of "lcredit" is a positive number, is not set, is commented out, or if conflicting results are returned, this is a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-269386`

### Rule: AlmaLinux OS 9 must ensure the password complexity module is enabled in the password-auth file.

**Rule ID:** `SV-269386r1050269_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enabling PAM password complexity permits enforcement of strong passwords and consequently makes the system less prone to dictionary attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 uses "pwquality" to enforce the password complexity rules in the password-auth file with the following command: Check for the use of the "pwquality" module in the PAM auth files with the following command: $ grep pam_pwquality.so /etc/pam.d/system-auth /etc/pam.d/password-auth /etc/pam.d/system-auth:password required pam_pwquality.so retry=3 /etc/pam.d/password-auth:password required pam_pwquality.so retry=3 If the command does not return a line in each file containing the value "pam_pwquality.so", or the line is commented out, this is a finding. If the system administrator (SA) can demonstrate that the required configuration is contained in a PAM configuration file included or substacked from the system-auth file, this is not a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-269387`

### Rule: AlmaLinux OS 9 must ensure the password complexity module in the system-auth file is configured for three retries or less.

**Rule ID:** `SV-269387r1050270_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>AlmaLinux OS 9 uses "pwquality" as a mechanism to enforce password complexity. This is set in both: /etc/pam.d/password-auth /etc/pam.d/system-auth By limiting the number of attempts to meet the pwquality module complexity requirements before returning with an error, the system will audit abnormal attempts at password changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 is configured to limit the "pwquality" retry option to "3". Check for the use of the "pwquality" retry option in the PAM auth files with the following command: $ grep pam_pwquality.so /etc/pam.d/system-auth /etc/pam.d/password-auth /etc/pam.d/system-auth:password required pam_pwquality.so retry=3 /etc/pam.d/password-auth:password required pam_pwquality.so retry=3 If the value of "retry" is set to "0" or greater than "3", or is missing from either, this is a finding. If the system administrator (SA) can demonstrate that the required configuration is contained in a PAM configuration file included or substacked from the system-auth file, this is not a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-269388`

### Rule: AlmaLinux OS 9 must enforce password complexity rules for the root account.

**Rule ID:** `SV-269388r1050271_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 enforces password complexity rules for the root account. Check if root user is required to use complex passwords with the following command: $ grep enforce_for_root /etc/security/pwquality.conf /etc/security/pwquality.conf.d/*.conf /etc/security/pwquality.conf:# enforce_for_root /etc/security/pwquality.conf.d/stig.conf:enforce_for_root If "enforce_for_root" is commented or missing, this is a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-269389`

### Rule: AlmaLinux OS 9 must enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-269389r1050272_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 enforces password complexity by requiring at least one uppercase character with the following command: $ grep -r ucredit /etc/security/pwquality.conf* /etc/security/pwquality.conf.d/stig.conf:ucredit = -1 If the value of "ucredit" is a positive number, is not set, is commented out, or if conflicting results are returned, this is a finding.

## Group: SRG-OS-000266-GPOS-00101

**Group ID:** `V-269390`

### Rule: AlmaLinux OS 9 must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-269390r1050273_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 enforces password complexity by requiring at least one special character with the following command: $ grep -E ocredit /etc/security/pwquality.conf* /etc/security/pwquality.conf.d/stig.conf:ocredit = -1 If the value of "ocredit" is a positive number, is not set, is commented out, or if conflicting results are returned, this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-269391`

### Rule: AlmaLinux OS 9 passwords for new users must have a minimum of 15 characters.

**Rule ID:** `SV-269391r1050274_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 enforces a minimum 15-character password length for new user accounts by running the following command: $ grep PASS_MIN_LEN /etc/login.defs PASS_MIN_LEN 15 If the "PASS_MIN_LEN" parameter value is less than "15", is not set, or is commented out, this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-269392`

### Rule: AlmaLinux OS 9 passwords must be created with a minimum of 15 characters.

**Rule ID:** `SV-269392r1050275_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password. AlmaLinux OS 9 uses the PAM pwquality module as a mechanism to enforce password complexity. Configurations are set in the "/etc/security/pwquality.conf" file or further *.conf files within the "/etc/security/pwquality.conf.d/" directory. The "minlen" parameter acts as a score of complexity based on the credit components of the pwquality module. By setting the credit to a negative value, not only will those components be required, but they will not count toward the total score of minlen. This will result in minlen requiring a 15-character minimum.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 enforces a minimum 15-character password length with the following command: $ grep -r minlen /etc/security/pwquality.conf* /etc/security/pwquality.conf.d/stig.conf:minlen = 15 If the value of "minlen" is less than 15, is not set, is commented out, or if conflicting results are returned, this is a finding.

## Group: SRG-OS-000071-GPOS-00039

**Group ID:** `V-269393`

### Rule: AlmaLinux OS 9 must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-269393r1050276_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 enforces password complexity by requiring at least one numeric character with the following command: $ grep -r dcredit /etc/security/pwquality.conf* /etc/security/pwquality.conf.d/stig.conf:dcredit = -1 If the value of "dcredit" is a positive number, is not set, is commented out, or if conflicting results are returned, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-269394`

### Rule: AlmaLinux OS 9 must require the change of at least four character classes when passwords are changed.

**Rule ID:** `SV-269394r1050277_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the value of the "minclass" option in "/etc/security/pwquality.conf" with the following command: $ grep -ir minclass /etc/security/pwquality.conf* /etc/security/pwquality.conf:# minclass = 0 /etc/security/pwquality.conf.d/stig.conf:minclass = 4 If the value of "minclass" is set to less than "4", or is commented out, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-269395`

### Rule: AlmaLinux OS 9 must require the maximum number of repeating characters be limited to three when passwords are changed.

**Rule ID:** `SV-269395r1050278_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the value of the "maxrepeat" option in "/etc/security/pwquality.conf" with the following command: $ grep -ir maxrepeat /etc/security/pwquality.conf* /etc/security/pwquality.conf:# maxrepeat = 0 /etc/security/pwquality.conf.d/stig.conf:maxrepeat = 3 If the value of "maxrepeat" is set to more than "3", or is commented out, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-269396`

### Rule: AlmaLinux OS 9 must require the maximum number of repeating characters of the same character class be limited to four when passwords are changed.

**Rule ID:** `SV-269396r1050279_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the value of the "maxclassrepeat" option in "/etc/security/pwquality.conf" with the following command: $ grep -ir maxclassrepeat /etc/security/pwquality.conf* /etc/security/pwquality.conf:# maxclassrepeat = 0 /etc/security/pwquality.conf.d/stig.conf:maxclassrepeat = 4 If the value of "maxclassrepeat" is set to "0", more than "4", or is commented out, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-269397`

### Rule: AlmaLinux OS 9 must require the change of at least eight characters when passwords are changed.

**Rule ID:** `SV-269397r1050280_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 enforces password complexity by requiring at least eight characters differ when passwords are changed with the following command: $ grep -r difok /etc/security/pwquality.conf* /etc/security/pwquality.conf.d/stig.conf:difok = 8 If the value of "difok" is less than "8", is not set, is commented out, or if conflicting results are returned, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-269398`

### Rule: AlmaLinux OS 9 PAM must be configured to use a sufficient number of password hashing rounds.

**Rule ID:** `SV-269398r1050281_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords must be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Using more hashing rounds makes password cracking attacks more difficult.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the number of rounds for the password hashing algorithm is configured with the following command: $ grep rounds /etc/pam.d/password-auth /etc/pam.d/system-auth /etc/pam.d/password-auth:password sufficient pam_unix.so sha512 shadow rounds=100000 use_authtok /etc/pam.d/system-auth:password sufficient pam_unix.so sha512 shadow rounds=100000 use_authtok If a matching line is not returned in both files, or "rounds" is less than "100000", this a finding. Add/modify the appropriate sections of the "/etc/pam.d/password-auth" file to match the following lines, ensuring that the "preauth" line is listed before pam_unix.so

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-269399`

### Rule: AlmaLinux OS 9 must be configured so that libuser is configured to store only encrypted representations of passwords.

**Rule ID:** `SV-269399r1050282_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords must be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. The system must use a strong hashing algorithm to store the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the user and group account administration utilities are configured to store only encrypted representations of passwords with the following command: $ grep crypt_style /etc/libuser.conf crypt_style = sha512 If the "crypt_style" variable is not set to "sha512", is not in the defaults section, is commented out, or does not exist, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-269400`

### Rule: AlmaLinux OS 9 must be configured so that the system's shadow file is configured to store only encrypted representations of passwords.

**Rule ID:** `SV-269400r1050283_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords must be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. The system must use a strong hashing algorithm to store the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system's shadow file is configured to store only encrypted representations of passwords with a hash value of SHA512 with the following command: $ grep ENCRYPT_METHOD /etc/login.defs ENCRYPT_METHOD SHA512 If "ENCRYPT_METHOD" does not have a value of "SHA512", or the line is commented out, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-269401`

### Rule: AlmaLinux OS 9 must be configured so that the Pluggable Authentication Module is configured to store only encrypted representations of passwords.

**Rule ID:** `SV-269401r1050284_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords must be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. The system must use a strong hashing algorithm to store the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the pam_unix.so module is configured to use sha512 in /etc/pam.d/password-auth with the following command: $ grep -E "password.*pam_unix.so.*sha512" /etc/pam.d/password-auth password sufficient pam_unix.so sha512 shadow rounds=100000 use_authtok If "sha512" is missing, or the line is commented out, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-269402`

### Rule: AlmaLinux OS 9 must be configured so that interactive user account passwords are using strong password hashes.

**Rule ID:** `SV-269402r1050285_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords must be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. The system must use a strong hashing algorithm to store the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the interactive user account passwords are using a strong password hash with the following command: $ cut -d: -f1,2 /etc/shadow root:$6$88upzIIyml/6UEya$QMLbF.L6gMNnIhzcxRorHgubK6jl3CHZ.MZrMkrEApOlt/MP.N.BFea.ykhPnIS.EYICo6To42koq0DCH8AjB/ bin:* daemon:* Password hashes "!" or "*" indicate inactive accounts not available for logon and are not evaluated. If any interactive user password hash does not begin with "$6", this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-269403`

### Rule: AlmaLinux OS 9 must not have any File Transfer Protocol (FTP) packages installed.

**Rule ID:** `SV-269403r1050286_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords must be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. An FTP server provides an unencrypted file transfer mechanism that does not protect the confidentiality of user credentials or the remote session. If a privileged user were to log on using this service, the privileged user password could be compromised. SFTP or other encrypted file transfer methods must be used instead. Removing the server and client packages prevents inbound and outbound communications from being compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 does not have an FTP client or server package installed with the following command: $ rpm -qa | grep ftp If the "vsftpd" server or "ftp" client packages are installed, this is a finding. Note that there may be third-party or alternative packages that provide the same functionality, which should also be removed.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-269404`

### Rule: AlmaLinux OS 9 must not have any telnet packages installed.

**Rule ID:** `SV-269404r1050287_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords must be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. A telnet server provides an unencrypted remote access mechanism that does not protect the confidentiality of user credentials or the remote session. If a privileged user were to log on using this service, the privileged user password could be compromised. SSH or other encrypted session methods must be used instead. Removing the server and client packages prevents inbound and outbound communications from being compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 does not have a telnet client or server package installed with the following command: $ rpm -qa | grep telnet If the "telnet-server" server or "telnet" client packages are installed, this is a finding. Note that there may be third-party or alternative packages that provide the same functionality, which should also be removed.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-269405`

### Rule: Passwords for existing users must have a 60-day maximum password lifetime restriction in /etc/shadow.

**Rule ID:** `SV-269405r1050288_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, Passwords must be changed periodically. If the operating system does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the operating system passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check whether the maximum time period for existing passwords is restricted to 60 days with the following command: $ awk -F: '$5 <= 0 || $5 > 60 {print $1 " " $5}' /etc/shadow If any results are returned that are not associated with a system account, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-269406`

### Rule: Passwords for new users or password changes must have a 60-day maximum password lifetime restriction in /etc/login.defs.

**Rule ID:** `SV-269406r1050619_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords must be changed periodically. If the operating system does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the operating system passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 enforces a 60-day maximum password lifetime for new user accounts by running the following command: $ grep PASS_MAX_DAYS /etc/login.defs PASS_MAX_DAYS 60 If the "PASS_MAX_DAYS" parameter value is greater than "60", is not set, or is commented out, this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-269407`

### Rule: Passwords for existing users must have a 24-hour minimum password lifetime restriction in /etc/shadow.

**Rule ID:** `SV-269407r1050290_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse. Checking existing users have this setting will ensure that no users created before the policy was configured can evade the password minimum setting.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the minimum time period between password changes for all user accounts is a day or more by running the following command: $ awk -F: '$4 < 1 {print $1 " " $4}' /etc/shadow If any results are returned that are not associated with a system account, this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-269408`

### Rule: Passwords for new users or password changes must have a 24-hour minimum password lifetime restriction in /etc/login.defs.

**Rule ID:** `SV-269408r1050291_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 enforces 24 hours as the minimum password lifetime for new user accounts with the following command: $ grep PASS_MIN_DAYS /etc/login.defs PASS_MIN_DAYS 1 If the value of "PASS_MIN_DAYS" is less than "1", is not set, or is commented out, this is a finding.

## Group: SRG-OS-000383-GPOS-00166

**Group ID:** `V-269409`

### Rule: AlmaLinux OS 9 must prohibit the use of cached authenticators after one day.

**Rule ID:** `SV-269409r1050292_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements. If cached authentication information is out-of-date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If smart card authentication is not being used on the system, this requirement is Not Applicable. Verify that the System Security Services Daemon (SSSD) prohibits the use of cached authentications after one day. Check that SSSD allows cached authentications with the following command: $ grep cache_credentials /etc/sssd/sssd.conf /etc/sssd/conf.d/* /etc/sssd/conf.d/certificate_verification.conf:cache_credentials = true If "cache_credentials" is set to "false" or missing from the configuration, this is not a finding and no further checks are required. If "cache_credentials" is set to "true", check that SSSD prohibits the use of cached authentications after one day with the following command: $ grep offline_credentials_expiration /etc/sssd/sssd.conf /etc/sssd/conf.d/ /etc/sssd/conf.d/certificate_verification.conf:offline_credentials_expiration = 1 If "offline_credentials_expiration" is not set to a value of "1", this is a finding.

## Group: SRG-OS-000067-GPOS-00035

**Group ID:** `V-269410`

### Rule: For PKI-based authentication, AlmaLinux OS 9 must enforce authorized access to the corresponding private key.

**Rule ID:** `SV-269410r1050293_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the private key is discovered, an attacker can use the key to authenticate as an authorized user and gain access to the network infrastructure. The cornerstone of the PKI is the private key used to encrypt or digitally sign information. If the private key is stolen, this will lead to the compromise of the authentication and nonrepudiation gained through PKI because the attacker can use the private key to digitally sign documents and pretend to be the authorized user. Both the holders of a digital certificate and the issuing authority must protect the computers, storage devices, or whatever they use to keep the private keys.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH private key files have a passcode. For each private key stored on the system, use the following command: $ ssh-keygen -y -f /path/to/file If the contents of the key are displayed, instead of a passphrase prompt, this is a finding.

## Group: SRG-OS-000068-GPOS-00036

**Group ID:** `V-269411`

### Rule: AlmaLinux OS 9 must map the authenticated identity to the user or group account for PKI-based authentication.

**Rule ID:** `SV-269411r1050294_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without mapping the certificate used to authenticate to the user account, the ability to determine the identity of the individual user or group will not be available for forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system administrator (SA) demonstrates the use of an approved alternate multifactor authentication method, this requirement is not applicable. Verify the operating system implements Online Certificate Status Protocol (OCSP) and is using the proper digest value on the system with the following command: $ grep certmap /etc/sssd/sssd.conf /etc/sssd/conf.d/*.conf /etc/sssd/conf.d/mapping.conf:[certmap/testing.test/rule_name] If the certmap section does not exist, ask the system administrator (SA) to indicate how certificates are mapped to accounts. If there is no evidence of certificate mapping, this is a finding.

## Group: SRG-OS-000384-GPOS-00167

**Group ID:** `V-269412`

### Rule: AlmaLinux OS 9, for PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

**Rule ID:** `SV-269412r1050295_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement. Satisfies: SRG-OS-000384-GPOS-00167, SRG-OS-000066-GPOS-00034, SRG-OS-000775-GPOS-00230, SRG-OS-000780-GPOS-00240</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 for PKI-based authentication has valid certificates by constructing a certification path (which includes status information) to an accepted trust anchor. Check that the system has a valid DOD root CA installed with the following command: $ openssl x509 -text -in /etc/sssd/pki/sssd_auth_ca_db.pem Certificate: Data: Version: 3 (0x2) Serial Number: 1 (0x1) Signature Algorithm: sha256WithRSAEncryption Issuer: C = US, O = U.S. Government, OU = DOD, OU = PKI, CN = DOD Root CA 3 Validity Not Before: Mar 20 18:46:41 2012 GMT Not After: Dec 30 18:46:41 2029 GMT Subject: C = US, O = U.S. Government, OU = DOD, OU = PKI, CN = DOD Root CA 3 Subject Public Key Info: Public Key Algorithm: rsaEncryption If the root CA file is not a DOD-issued certificate with a valid date and installed in the "/etc/sssd/pki/sssd_auth_ca_db.pem" location, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-269413`

### Rule: AlmaLinux 9 cryptographic policy must not be overridden.

**Rule ID:** `SV-269413r1101794_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Centralized cryptographic policies simplify applying secure ciphers across an operating system and the applications that run on that operating system. Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. Satisfies: SRG-OS-000396-GPOS-00176, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux 9 cryptographic policies are not overridden. Verify that the configured policy matches the generated policy with the following command: $ sudo update-crypto-policies --check The configured policy matches the generated policy If the returned message does not match the above, but instead matches the following, this is a finding: The configured policy does NOT match the generated policy List all of the crypto backends configured on the system with the following command: $ ls -l /etc/crypto-policies/back-ends/ lrwxrwxrwx. 1 root root 40 Nov 13 16:29 bind.config -> /usr/share/crypto-policies/FIPS/bind.txt lrwxrwxrwx. 1 root root 42 Nov 13 16:29 gnutls.config -> /usr/share/crypto-policies/FIPS/gnutls.txt lrwxrwxrwx. 1 root root 40 Nov 13 16:29 java.config -> /usr/share/crypto-policies/FIPS/java.txt lrwxrwxrwx. 1 root root 46 Nov 13 16:29 javasystem.config -> /usr/share/crypto-policies/FIPS/javasystem.txt lrwxrwxrwx. 1 root root 40 Nov 13 16:29 krb5.config -> /usr/share/crypto-policies/FIPS/krb5.txt lrwxrwxrwx. 1 root root 45 Nov 13 16:29 libreswan.config -> /usr/share/crypto-policies/FIPS/libreswan.txt lrwxrwxrwx. 1 root root 42 Nov 13 16:29 libssh.config -> /usr/share/crypto-policies/FIPS/libssh.txt -rw-r--r--. 1 root root 398 Nov 13 16:29 nss.config lrwxrwxrwx. 1 root root 43 Nov 13 16:29 openssh.config -> /usr/share/crypto-policies/FIPS/openssh.txt lrwxrwxrwx. 1 root root 49 Nov 13 16:29 opensshserver.config -> /usr/share/crypto-policies/FIPS/opensshserver.txt lrwxrwxrwx. 1 root root 46 Nov 13 16:29 opensslcnf.config -> /usr/share/crypto-policies/FIPS/opensslcnf.txt lrwxrwxrwx. 1 root root 43 Nov 13 16:29 openssl.config -> /usr/share/crypto-policies/FIPS/openssl.txt lrwxrwxrwx. 1 root root 48 Nov 13 16:29 openssl_fips.config -> /usr/share/crypto-policies/FIPS/openssl_fips.txt If the paths do not point to the respective files under /usr/share/crypto-policies/FIPS path, this is a finding. Note: nss.config should not be symlinked. Note: If there is an operational need to use a subpolicy that causes the links to the crypto backends to break, this is a finding, and exceptions will need to be made by the authorizing official (AO) and documented with the information system security officer (ISSO).

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-269415`

### Rule: The libreswan package must be installed.

**Rule ID:** `SV-269415r1101853_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Providing the ability for remote users or systems to initiate a secure VPN connection protects information when it is transmitted over a wide area network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If there is no operational need for Libreswan to be installed, this rule is not applicable. Verify that the libreswan package is installed with the following command: $ dnf list --installed libreswan libreswan.x86_64 4.9-4.el9_2 @appstream If the "libreswan" package is not installed, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-269416`

### Rule: AlmaLinux OS 9 must have the packages required for encrypting offloaded audit logs installed.

**Rule ID:** `SV-269416r1050299_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The rsyslog-gnutls package provides Transport Layer Security (TLS) support for the rsyslog daemon, which enables secure remote logging.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the rsyslog-gnutls package is installed with the following command: $ dnf list --installed rsyslog-gnutls rsyslog-gnutls.x86_64 8.2102.0-111.el9 @AppStream If the "rsyslog-gnutls" package is not installed, this is a finding.

## Group: SRG-OS-000394-GPOS-00174

**Group ID:** `V-269417`

### Rule: AlmaLinux OS 9 must have the crypto-policies package installed.

**Rule ID:** `SV-269417r1050300_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Centralized cryptographic policies simplify applying secure ciphers across an operating system and the applications that run on that operating system. Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. Satisfies: SRG-OS-000394-GPOS-00174, SRG-OS-000393-GPOS-00173</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the AlmaLinux OS 9 crypto-policies package is installed with the following command: $ dnf list --installed crypto-policies Installed Packages crypto-policies.noarch 20221215-1.git9a18988.el9 @anaconda If the "crypto-policies" package is not installed, this is a finding.

## Group: SRG-OS-000394-GPOS-00174

**Group ID:** `V-269418`

### Rule: AlmaLinux OS 9 must implement a FIPS 140-3-compliant systemwide cryptographic policy.

**Rule ID:** `SV-269418r1107628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Centralized cryptographic policies simplify applying secure ciphers across an operating system and the applications that run on that operating system. Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. Satisfies: SRG-OS-000396-GPOS-00176, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 is set to use a FIPS 140-3-compliant systemwide cryptographic policy with the following command: $ update-crypto-policies --show FIPS If the systemwide crypto policy is not set to "FIPS", this is a finding. Note: If subpolicies have been configured, they could be listed in a colon-separated list starting with "FIPS" as follows FIPS:<SUBPOLICY-NAME>. This is not a finding. Note: Subpolicies like AD-SUPPORT should be configured according to the latest guidance from the operating system vendor. Verify the current minimum crypto-policy configuration with the following commands: $ grep -E 'rsa_size|hash' /etc/crypto-policies/state/CURRENT.pol hash = SHA2-256 SHA2-384 SHA2-512 SHA2-224 SHA3-256 SHA3-384 SHA3-512 SHAKE-256 min_rsa_size = 2048 If the "hash" values do not include at least the following FIPS 140-3-compliant algorithms "SHA2-256 SHA2-384 SHA2-512 SHA2-224 SHA3-256 SHA3-384 SHA3-512 SHAKE-256", this is a finding. If there are algorithms that include "SHA1" or a hash value less than "224" this is a finding. If the "min_rsa_size" is not set to a value of at least 2048, this is a finding. If these commands do not return any output, this is a finding.

## Group: SRG-OS-000395-GPOS-00175

**Group ID:** `V-269419`

### Rule: AlmaLinux OS 9 must be configured so that all network connections associated with SSH traffic are terminated after 10 minutes of becoming unresponsive.

**Rule ID:** `SV-269419r1050302_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an unresponsive SSH session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle SSH session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level and deallocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean the operating system terminates all sessions or network access; it only ends the unresponsive session and releases the resources associated with that session. Satisfies: SRG-OS-000395-GPOS-00175, SRG-OS-000163-GPOS-00072, SRG-OS-000279-GPOS-00109</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "ClientAliveInterval" variable is set to a value of "600" or less and "ClientAliveCountMax" is set to "1" by performing the following command: $ sshd -T | grep clientalive clientaliveinterval 600 clientalivecountmax 1 If "ClientAliveInterval" does not have a value of "600" or less, or "ClientAliveCountMax" is not set to "1", this is a finding.

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-269420`

### Rule: AlmaLinux OS 9 must enable the Pluggable Authentication Module (PAM) interface for SSHD.

**Rule ID:** `SV-269420r1050303_rule`
**Severity:** high

**Description:**
<VulnDiscussion>When UsePAM is set to "yes", PAM runs through account and session types properly. This is important when restricted access to services based off of IP, time, or other factors of the account is needed. Additionally, this ensures users can inherit certain environment variables on login or disallow access to the server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AlmaLinux OS 9 SSHD is configured to allow for the UsePAM interface with the following command: $ sshd -T | grep usepam usepam yes If the "UsePAM" keyword is set to "no", is missing, or is commented out, this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-269421`

### Rule: AlmaLinux OS 9 must terminate idle user sessions.

**Rule ID:** `SV-269421r1050304_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, and de-allocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that the operating system terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 logs out sessions that are idle for 15 minutes with the following command: $ systemd-analyze cat-config systemd/logind.conf | grep StopIdleSessionSec #StopIdleSessionSec=infinity StopIdleSessionSec=900 If "StopIdleSessionSec" is not configured to "900" seconds, this is a finding.

## Group: SRG-OS-000132-GPOS-00067

**Group ID:** `V-269422`

### Rule: AlmaLinux OS 9 must disable access to network bpf system call from nonprivileged processes.

**Rule ID:** `SV-269422r1050305_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Loading and accessing the packet filters programs and maps using the bpf() system call has the potential of revealing sensitive information about the kernel state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 prevents privilege escalation thru the kernel by disabling access to the bpf system call with the following commands: $ sysctl kernel.unprivileged_bpf_disabled kernel.unprivileged_bpf_disabled = 1 If the returned line does not have a value of "1", or a line is not returned, this is a finding. Check that the configuration files are present to enable this kernel parameter. $ /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F kernel.unprivileged_bpf_disabled | tail -1 kernel.unprivileged_bpf_disabled = 1 If "kernel.unprivileged_bpf_disabled" is not set to "1", or nothing is returned, this is a finding.

## Group: SRG-OS-000132-GPOS-00067

**Group ID:** `V-269423`

### Rule: AlmaLinux OS 9 must restrict exposed kernel pointer addresses access.

**Rule ID:** `SV-269423r1050306_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Exposing kernel pointers (through procfs or "seq_printf()") exposes kernel writeable structures, which may contain functions pointers. If a write vulnerability occurs in the kernel, allowing write access to any of this structure, the kernel can be compromised. This option disallows any program without the CAP_SYSLOG capability to get the addresses of kernel pointers by replacing them with "0".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the runtime status of the kernel.kptr_restrict kernel parameter with the following command: $ sysctl kernel.kptr_restrict kernel.kptr_restrict = 1 Verify the configuration of the kernel.kptr_restrict kernel parameter with the following command: $ /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F kernel.kptr_restrict | tail -1 kernel.kptr_restrict =1 If "kernel.kptr_restrict" is not set to "1" or is missing, this is a finding.

## Group: SRG-OS-000132-GPOS-00067

**Group ID:** `V-269424`

### Rule: AlmaLinux OS 9 must restrict usage of ptrace to descendant processes.

**Rule ID:** `SV-269424r1050307_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted usage of ptrace allows compromised binaries to run ptrace on other processes of the user. Like this, the attacker can steal sensitive information from the target processes (e.g. SSH sessions, web browser etc.) without any additional assistance from the user (i.e. without resorting to phishing).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 restricts usage of ptrace to descendant processes (1), admins only (2), or disables ptrace entirely (3) with the following command: $ sysctl kernel.yama.ptrace_scope kernel.yama.ptrace_scope = 1 If the returned line has a value of "0" or a line is not returned, this is a finding. Check that the configuration files are present to enable this kernel parameter. $ /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F kernel.yama.ptrace_scope | tail -1 kernel.yama.ptrace_scope = 1 If "kernel.yama.ptrace_scope" is equal to "0" or nothing is returned, this is a finding.

## Group: SRG-OS-000132-GPOS-00067

**Group ID:** `V-269425`

### Rule: AlmaLinux OS 9 must restrict access to the kernel message buffer.

**Rule ID:** `SV-269425r1050308_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting access to the kernel message buffer limits access to only root. This prevents attackers from gaining additional system information as a nonprivileged user. Satisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000138-GPOS-00069</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 is configured to restrict access to the kernel message buffer with the following commands: Check the status of the kernel.dmesg_restrict kernel parameter. $ sysctl kernel.dmesg_restrict kernel.dmesg_restrict = 1 If "kernel.dmesg_restrict" is not set to "1" or is missing, this is a finding. Check that the configuration files are present to enable this kernel parameter. $ /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F kernel.dmesg_restrict | tail -1 kernel.dmesg_restrict = 1 If "kernel.dmesg_restrict" is not set to "1" or is missing, this is a finding.

## Group: SRG-OS-000132-GPOS-00067

**Group ID:** `V-269426`

### Rule: AlmaLinux OS 9 must prevent kernel profiling by nonprivileged users.

**Rule ID:** `SV-269426r1050309_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the kernel.perf_event_paranoid kernel parameter to "2" prevents attackers from gaining additional system information as a nonprivileged user. Satisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000138-GPOS-00069</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 is configured to prevent kernel profiling by nonprivileged users with the following commands: Check the status of the kernel.perf_event_paranoid kernel parameter. $ sysctl kernel.perf_event_paranoid kernel.perf_event_paranoid = 2 If "kernel.perf_event_paranoid" is not set to "2" or is missing, this is a finding. Check that the configuration files are present to enable this kernel parameter. $ /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F kernel.perf_event_paranoid | tail -1 kernel.perf_event_paranoid = 2 If "kernel.perf_event_paranoid" is not set to "2" or is missing, this is a finding.

## Group: SRG-OS-000403-GPOS-00182

**Group ID:** `V-269427`

### Rule: AlmaLinux OS 9 must only allow the use of DOD PKI-established certificate authorities for authentication in the establishment of protected sessions to the operating system.

**Rule ID:** `SV-269427r1050310_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DOD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DOD-approved CA, trust of this CA has not been established. The DOD will only accept PKI-certificates obtained from a DOD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of SSL/TLS certificates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 only allows the use of DOD PKI-established certificate authorities using the following command: $ trust list pkcs11:id=%7C%42%96%AE%DE%4B%48%3B%FA%92%F8%9E%8C%CF%6D%8B%A9%72%37%95;type=cert type: certificate label: ISRG Root X2 trust: anchor category: authority If any nonapproved CAs are returned, this is a finding.

## Group: SRG-OS-000269-GPOS-00103

**Group ID:** `V-269428`

### Rule: AlmaLinux OS 9 systemd-journald service must be enabled.

**Rule ID:** `SV-269428r1050311_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In the event of a system failure, AlmaLinux OS 9 must preserve any information necessary to determine cause of failure and any information necessary to return to operations with least disruption to system processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "systemd-journald" is active with the following command: $ systemctl status systemd-journald systemd-journald.service - Journal Service Loaded: loaded (/usr/lib/systemd/system/systemd-journald.service; static) Active: active (running) since Tue 2024-02-20 11:02:20 UTC; 14min ago If the systemd-journald service is not active, this is a finding.

## Group: SRG-OS-000405-GPOS-00184

**Group ID:** `V-269429`

### Rule: AlmaLinux OS 9 local disk partitions must implement cryptographic mechanisms to prevent unauthorized disclosure or modification of all information that requires at rest protection.

**Rule ID:** `SV-269429r1050312_rule`
**Severity:** high

**Description:**
<VulnDiscussion>AlmaLinux OS 9 systems handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). Satisfies: SRG-OS-000405-GPOS-00184, SRG-OS-000404-GPOS-00183, SRG-OS-000185-GPOS-00079</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If there is a documented and approved reason for not having data-at-rest encryption at the operating system level, such as encryption provided by a hypervisor or a disk storage array in a virtualized environment, this requirement is Not Applicable. Verify AlmaLinux OS 9 prevents unauthorized disclosure or modification of all information requiring at-rest protection by using disk encryption. Verify all system partitions are encrypted with the following command: $ lsblk -e11 -oNAME,FSTYPE,FSVER,MOUNTPOINTS NAME FSTYPE FSVER MOUNTPOINTS sda +-sda1 vfat FAT16 /boot/efi +-sda2 xfs /boot +-sda3 LVM2_member LVM2 001 +-rootvg-root crypto_LUKS 2 ¦ +-luks-8a7154ec-8eeb-46c8-9d75-66fc4b81d665 xfs / +-rootvg-swap crypto_LUKS 2 ¦ +-luks-89bf0df8-547f-4613-af07-215e5f63e9a9 swap 1 [SWAP] +-rootvg-home crypto_LUKS 2 ¦ +-luks-10a20c46-483d-4d12-831f-5328eda28fd1 xfs /home +-rootvg-varlogaudit crypto_LUKS 2 ¦ +-luks-29b74747-2f82-4472-82f5-0b5eb764effc xfs /var/log/audit +-rootvg-varlog crypto_LUKS 2 ¦ +-luks-e0d162f5-fad8-463e-8e39-6bd09e682961 xfs /var/log +-rootvg-vartmp crypto_LUKS 2 ¦ +-luks-0e7206e7-bfb1-4a23-ae14-b9cea7cf46d5 xfs /var/tmp +-rootvg-var crypto_LUKS 2 +-luks-b23d8276-7844-4e79-8a58-505150b4eb42 xfs /var Every persistent disk partition present must be of type "crypto_LUKS". If any partitions other than the /boot partitions are not type "crypto_LUKS", ask the administrator to indicate how the partitions are encrypted. If there is no evidence that these partitions are encrypted, this is a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-269430`

### Rule: AlmaLinux OS 9 must use a Linux Security Module configured to enforce limits on system services.

**Rule ID:** `SV-269430r1050313_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An isolation boundary provides access control and protects the integrity of the hardware, software, and firmware that perform security functions. Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Operating systems implement code separation (i.e., separation of security functions from nonsecurity functions) in a number of ways, including through the provision of security kernels via processor rings or processor modes. For nonkernel code, security function isolation is often achieved through file system protections that serve to protect the code on disk and address space protections that protect executing code. Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Implementation may include isolation of memory space and libraries. Operating systems restrict access to security functions through the use of access control mechanisms and by implementing least privilege capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that AlmaLinux OS 9 verifies correct operation of security functions through the use of SELinux with the following command: $ getenforce Enforcing If SELINUX is not set to "Enforcing", this is a finding. Verify that SELinux is configured to be enforcing at boot. $ grep -E "^SELINUX=" /etc/selinux/config SELINUX=enforcing If SELINUX line is missing, commented out, or not set to "enforcing", this is a finding. Verify that SELinux is enabled and Enforcing for all kernels: $ grubby --info=ALL | grep -E 'selinux|enforcing' args="ro audit=1 selinux=1 enforcing=1 audit_backlog_limit=8192 page_poison=1 vsyscall=none slub_debug=P pti=on iommu=force resume=/dev/mapper/luks-89bf0df8-547f-4613-af07-215e5f62e9a9 rd.luks.uuid=luks-8a7154ec-8eeb-46c8-9d75-66fc4b80d665 rd.lvm.lv=rootvg/root rd.luks.uuid=luks-89bf0df8-547f-4613-af07-215e5f62e9a9 rd.lvm.lv=rootvg/swap rd.shell=0 quiet splash fips=1 boot=UUID=eda01e9b-b7e1-431b-9549-16d5dcddf665" args="ro audit=1 selinux=1 enforcing=1 audit_backlog_limit=8192 page_poison=1 vsyscall=none slub_debug=P pti=on iommu=force resume=/dev/mapper/luks-89bf0df8-547f-4613-af07-215e5f62e9a9 rd.luks.uuid=luks-8a7154ec-8eeb-46c8-9d75-66fc4b80d665 rd.lvm.lv=rootvg/root rd.luks.uuid=luks-89bf0df8-547f-4613-af07-215e5f62e9a9 rd.lvm.lv=rootvg/swap rd.shell=0 quiet splash fips=1 boot=UUID=eda01e9b-b7e1-431b-9549-16d5dcddf665" If selinux=1 is missing or set to 0, or enforcing=1 is missing or set to 0, this is a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-269431`

### Rule: AlmaLinux OS 9 must have the policycoreutils package installed.

**Rule ID:** `SV-269431r1050314_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Policycoreutils contains the policy core utilities that are required for basic operation of an SELinux-enabled system. These utilities include load_policy to load SELinux policies, setfile to label filesystems, newrole to switch roles, and run_init to run /etc/init.d scripts in the proper context.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 has the policycoreutils package installed with the following command: $ dnf list --installed policycoreutils policycoreutils.x86_64 3.5-1.el9 @anaconda If the "policycoreutils" package is not installed, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-269432`

### Rule: Any AlmaLinux OS 9 world-writable directories must be owned by root, sys, bin, or an application user.

**Rule ID:** `SV-269432r1050315_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a world-writable directory is not owned by root, sys, bin, or an application user identifier (UID), unauthorized users may be able to modify files created by others. The only authorized public directories are those temporary directories supplied with the system or those designed to be temporary file repositories. The setting is normally reserved for directories used by the system and by users for temporary file storage, (e.g., /tmp), and for directories requiring global read/write access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that world writable directories are owned by root, a system account, or an application account with the following command. It will discover and print world-writable directories that are not owned by root. Run it once for each local partition [PART] e.g. "/": $ find PART -xdev -type d -perm -0002 -uid +0 -print If there is output, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-269433`

### Rule: A sticky bit must be set on all AlmaLinux OS 9 public directories.

**Rule ID:** `SV-269433r1050316_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DOD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all world-writable directories have the sticky bit set. Determine if all world-writable directories have the sticky bit set by running the following command: $ find / -type d \( -perm -0002 -a ! -perm -1000 \) -exec ls -ld {} \; drwxrwxrwt 7 root root 4096 Jul 26 11:19 /tmp If any of the returned directories are world-writable and do not have the sticky bit set (trailing "t"), this is a finding.

## Group: SRG-OS-000420-GPOS-00186

**Group ID:** `V-269434`

### Rule: AlmaLinux OS 9 must protect against or limit the effects of denial-of-service (DoS) attacks by ensuring rate-limiting measures on impacted network interfaces are implemented.

**Rule ID:** `SV-269434r1050317_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of the operating system to mitigate the impact of DoS attacks that have occurred or are ongoing on system availability. For each system, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or establishing memory partitions). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify "nftables" is configured to allow rate limits on any connection to the system with the following command: $ grep -i firewallbackend /etc/firewalld/firewalld.conf # FirewallBackend FirewallBackend=nftables If the "nftables" is not set as the "FirewallBackend" default, this is a finding.

## Group: SRG-OS-000420-GPOS-00186

**Group ID:** `V-269435`

### Rule: AlmaLinux OS 9 must be configured to use TCP syncookies.

**Rule ID:** `SV-269435r1050318_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Denial of Service (DoS) is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of the operating system to mitigate the impact of DoS attacks that have occurred or are ongoing on system availability. For each system, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or establishing memory partitions). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks. Satisfies: SRG-OS-000420-GPOS-00186, SRG-OS-000142-GPOS-00071</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 is configured to use IPv4 TCP syncookies with the following command: $ sysctl net.ipv4.tcp_syncookies net.ipv4.tcp_syncookies = 1 Check that the configuration files are present to enable this kernel parameter. $ /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F net.ipv4.tcp_syncookies | tail -1 net.ipv4.tcp_syncookies = 1 If the network parameter "ipv4.tcp_syncookies" is not equal to "1" or nothing is returned, this is a finding.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-269436`

### Rule: All AlmaLinux OS 9 networked systems must have the OpenSSH client installed.

**Rule ID:** `SV-269436r1050319_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 has the openssh client package installed with the following command: $ dnf list --installed openssh Installed Packages openssh.x86_64 8.7p1-28.el9 @anaconda If the "openssh" client package is not installed, this is a finding.

## Group: SRG-OS-000424-GPOS-00188

**Group ID:** `V-269437`

### Rule: All AlmaLinux OS 9 networked systems must implement SSH to protect the confidentiality and integrity of transmitted and received information, including information being prepared for transmission.

**Rule ID:** `SV-269437r1050320_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. Satisfies: SRG-OS-000424-GPOS-00188, SRG-OS-000426-GPOS-00190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "sshd" is active with the following command: $ systemctl status sshd sshd.service - OpenSSH server daemon Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled; preset: enabled) Active: active (running) since Fri 2024-01-26 09:41:09 UTC; 2h 48min ago If the "sshd" service is not enabled and active, this is a finding.

## Group: SRG-OS-000424-GPOS-00188

**Group ID:** `V-269438`

### Rule: All AlmaLinux OS 9 networked systems must have the OpenSSH server installed.

**Rule ID:** `SV-269438r1050321_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. Satisfies: SRG-OS-000424-GPOS-00188, SRG-OS-000426-GPOS-00190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 has the openssh-server package installed with the following command: $ dnf list --installed openssh-server Installed Packages openssh-server.x86_64 8.7p1-28.el9 @anaconda If the "openssh-server" package is not installed, this is a finding.

## Group: SRG-OS-000425-GPOS-00189

**Group ID:** `V-269439`

### Rule: AlmaLinux OS 9 must not allow users to override SSH environment variables.

**Rule ID:** `SV-269439r1050322_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SSH environment options potentially allow users to bypass access restriction in some configurations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon prevents users from overriding SSH environment variables with the following command: $ sshd -T | grep permituserenvironment permituserenvironment no If the "PermitUserEnvironment" keyword is set to "yes", or no output is returned, this is a finding.

## Group: SRG-OS-000426-GPOS-00190

**Group ID:** `V-269440`

### Rule: AlmaLinux OS 9 must implement DOD-approved encryption in the bind package.

**Rule ID:** `SV-269440r1050323_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. AlmaLinux OS 9 incorporates systemwide crypto policies by default. The employed algorithms can be viewed in the /etc/crypto-policies/back-ends/ directory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the "bind" package is not installed, this requirement is Not Applicable. Verify that BIND uses the system crypto policy with the following command: $ grep include /etc/named.conf include "/etc/crypto-policies/back-ends/bind.config"; If BIND is installed and the BIND config file does not contain the "/etc/crypto-policies/back-ends/bind.config" directive, or the line is commented out, this is a finding.

## Group: SRG-OS-000481-GPOS-00481

**Group ID:** `V-269441`

### Rule: AlmaLinux OS 9 wireless network adapters must be disabled.

**Rule ID:** `SV-269441r1050324_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement applies to wireless peripheral technologies (e.g., wireless mice, keyboards, displays, etc.) used with AlmaLinux OS 9 systems. Wireless peripherals (e.g., Wi-Fi/Bluetooth/IR keyboards, mice and pointing devices, and near field communications [NFC]) present a unique challenge by creating an open, unsecured port on a computer. Wireless peripherals must meet DOD requirements for wireless data transmission and be approved for use by the authorizing official (AO). Even though some wireless peripherals, such as mice and pointing devices, do not ordinarily carry information that need to be protected, modification of communications with these wireless peripherals may be used to compromise the AlmaLinux OS 9 operating system. Satisfies: SRG-OS-000481-GPOS-00481, SRG-OS-000299-GPOS-00117, SRG-OS-000300-GPOS-00118</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the system does not have physical wireless network radios, this requirement is Not Applicable. Verify there are no wireless interfaces configured on the system with the following commands: $ nmcli radio all WIFI-HW WIFI WWAN-HW WWAN enabled enabled missing disabled $ nmcli device status DEVICE TYPE STATE CONNECTION wlp2s0 wifi connected cafe lo loopback connected (externally) lo p2p-dev-wlp2s0 wifi-p2p disconnected -- enp3s0f2 ethernet unavailable -- If a wireless interface is configured and has not been documented and approved by the information system security officer (ISSO), this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-269442`

### Rule: AlmaLinux OS 9 must not show boot up messages.

**Rule ID:** `SV-269442r1050325_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the AlmaLinux OS 9 system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Without using the "quiet" grub kernel parameter, the hardware and service information are printed to the console on boot and sometimes afterwards. This information could be useful for attackers with physical access, or so-called "shoulder surfers". Boot failures will still be shown, as will the LUKS password prompt. Verify the grub bootloader has the "quiet" option set with the following command: $ grubby --info=ALL | grep quiet args="ro audit=1 audit_backlog_limit=8192 page_poison=1 vsyscall=none slub_debug=P pti=on iommu=force resume=/dev/mapper/luks-89bf0df8-547f-4613-af07-215e5f62e9a9 rd.luks.uuid=luks-8a7154ec-8eeb-46c8-9d75-66fc4b80d665 rd.lvm.lv=rootvg/root rd.luks.uuid=luks-89bf0df8-547f-4613-af07-215e5f62e9a9 rd.lvm.lv=rootvg/swap rd.shell=0 quiet splash fips=1 boot=UUID=eda01e9b-b7e1-431b-9549-16d5dcddf665 selinux=1 enforcing=1" args="ro audit=1 audit_backlog_limit=8192 page_poison=1 vsyscall=none slub_debug=P pti=on iommu=force resume=/dev/mapper/luks-89bf0df8-547f-4613-af07-215e5f62e9a9 rd.luks.uuid=luks-8a7154ec-8eeb-46c8-9d75-66fc4b80d665 rd.lvm.lv=rootvg/root rd.luks.uuid=luks-89bf0df8-547f-4613-af07-215e5f62e9a9 rd.lvm.lv=rootvg/swap rd.shell=0 quiet splash fips=1 boot=UUID=eda01e9b-b7e1-431b-9549-16d5dcddf665 selinux=1 enforcing=1" If nothing is returned, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-269443`

### Rule: AlmaLinux OS 9 /var/log directory must be group-owned by root.

**Rule ID:** `SV-269443r1050326_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the AlmaLinux OS 9 system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/var/log" directory is group-owned by root with the following command: $ stat -c "%U:%G %#a %n" /var/log root:root 0755 /var/log If "/var/log" does not have a group-owner of "root", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-269444`

### Rule: AlmaLinux OS 9 /var/log/messages file must be group-owned by root.

**Rule ID:** `SV-269444r1050327_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the AlmaLinux OS 9 system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/var/log/messages" file is group-owned by root with the following command: $ stat -c "%U:%G %#a %n" /var/log root:root 0755 /var/log If "/var/log/messages" does not have a group-owner of "root", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-269445`

### Rule: AlmaLinux OS 9 /var/log/messages file must be owned by root.

**Rule ID:** `SV-269445r1050328_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the AlmaLinux OS 9 system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/var/log/messages" file is owned by root with the following command: $ stat -c "%U:%G %#a %n" /var/log root:root 0755 /var/log If "/var/log/messages" does not have an owner of "root", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-269446`

### Rule: AlmaLinux OS 9 /var/log/messages file must have mode 0640 or less permissive.

**Rule ID:** `SV-269446r1050329_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the AlmaLinux OS 9 system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/var/log/messages" file has a mode of "0640" or less permissive with the following command: $ stat -c "%U:%G %#a %n" /var/log/messages root:root 0600 /var/log/messages If "/var/log/messages" does not have a mode of "0640" or less permissive, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-269447`

### Rule: AlmaLinux OS 9 /var/log directory must be owned by root.

**Rule ID:** `SV-269447r1050330_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the AlmaLinux OS 9 system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "/var/log" directory is owned by root with the following command: $ stat -c "%U:%G %#a %n" /var/log root:root 0755 /var/log If "/var/log" does not have an owner of "root", this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-269448`

### Rule: AlmaLinux OS 9 /var/log directory must have mode 0755 or less permissive.

**Rule ID:** `SV-269448r1050331_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the AlmaLinux OS 9 system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the "/var/log" directory has a mode of "0755" or less permissive with the following command: $ stat -c "%U:%G %#a %n" /var/log root:root 0755 /var/log If "/var/log" does not have a mode of "0755" or less permissive, this is a finding.

## Group: SRG-OS-000433-GPOS-00192

**Group ID:** `V-269449`

### Rule: AlmaLinux OS 9 must implement nonexecutable data to protect its memory from unauthorized code execution.

**Rule ID:** `SV-269449r1050620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ExecShield uses the segmentation feature on all x86 systems to prevent execution in memory higher than a certain address. It writes an address as a limit in the code segment descriptor, to control where code can be executed, on a per-process basis. When the kernel places the memory regions of a process, such as the stack and heap, higher than this address, the hardware prevents execution in that address range.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify ExecShield is enabled on 64-bit AlmaLinux OS 9 systems with the following command: $ dmesg | grep '[NX|DX]*protection' [ 0.000000] NX (Execute Disable) protection: active If "dmesg" does not show "NX (Execute Disable) protection active", this is a finding.

## Group: SRG-OS-000433-GPOS-00192

**Group ID:** `V-269450`

### Rule: AlmaLinux OS 9 must enable mitigations against processor-based vulnerabilities.

**Rule ID:** `SV-269450r1050333_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kernel page-table isolation is a kernel feature that mitigates the Meltdown security vulnerability and hardens the kernel against attempts to bypass kernel address space layout randomization (KASLR).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 enables kernel page-table isolation with the following command: $ grubby --info=ALL | grep pti args="ro audit=1 selinux=1 enforcing=1 audit_backlog_limit=8192 page_poison=1 vsyscall=none slub_debug=P pti=on iommu=force resume=/dev/mapper/luks-88bf0df8-547f-4613-af07-215e5f62e9a9 rd.luks.uuid=luks-8a7154ec-8eeb-47c8-9d75-66fd4b80d665 rd.lvm.lv=rootvg/root rd.luks.uuid=luks-89bf0df8-547f-4613-af07-215e5f62e9a9 rd.lvm.lv=rootvg/swap rd.shell=0 quiet splash fips=1 boot=UUID=eda01e9b-b7e1-431b-9549-16d5dcddf665" If the "pti" entry does not equal "on", or is missing, this is a finding. Check that kernel page-table isolation is enabled by default to persist in kernel updates: $ grep pti /etc/default/grub GRUB_CMDLINE_LINUX="pti=on" If "pti" is not set to "on", is missing or commented out, this is a finding.

## Group: SRG-OS-000433-GPOS-00192

**Group ID:** `V-269451`

### Rule: AlmaLinux OS 9 must clear memory when it is freed to prevent use-after-free attacks.

**Rule ID:** `SV-269451r1069342_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in nonexecutable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can be either hardware-enforced or software-enforced with hardware providing the greater strength of mechanism. Poisoning writes an arbitrary value to freed pages, so any modification or reference to that page after being freed or before being initialized will be detected and prevented. This prevents many types of use-after-free vulnerabilities at little performance cost. Also prevents leak of data and detection of corrupted memory. init_on_free is a Linux kernel boot parameter that enhances security by initializing memory regions when they are freed, preventing data leakage. This process ensures that stale data in freed memory cannot be accessed by malicious programs. SLUB canaries add a randomized value (canary) at the end of SLUB-allocated objects to detect memory corruption caused by buffer overflows or underflows. Redzoning adds padding (red zones) around SLUB-allocated objects to detect overflows or underflows by triggering a fault when adjacent memory is accessed. SLUB canaries are often more efficient and provide stronger detection against buffer overflows compared to redzoning. SLUB canaries are supported in hardened Linux kernels like the ones provided by Linux-hardened. SLAB objects are blocks of physically contiguous memory. SLUB is the unqueued SLAB allocator. Satisfies: SRG-OS-000433-GPOS-00192, SRG-OS-000134-GPOS-00068</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that GRUB2 is configured to mitigate use-after-free vulnerabilities by employing memory poisoning. Inspect the "GRUB_CMDLINE_LINUX" entry of /etc/default/grub as follows: $ sudo grep -i grub_cmdline_linux /etc/default/grub GRUB_CMDLINE_LINUX="... init_on_free=1" If "init_on_free=1"is missing or commented out, this is a finding.

## Group: SRG-OS-000433-GPOS-00193

**Group ID:** `V-269452`

### Rule: AlmaLinux OS 9 must implement address space layout randomization (ASLR) to protect its memory from unauthorized code execution.

**Rule ID:** `SV-269452r1050335_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ASLR makes it more difficult for an attacker to predict the location of attack code they have introduced into a process' address space during an attempt at exploitation. Additionally, ASLR makes it more difficult for an attacker to know the location of existing code to repurpose it using return oriented programming (ROP) techniques.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 is implementing ASLR with the following command: $ sysctl kernel.randomize_va_space kernel.randomize_va_space = 2 If "kernel.randomize_va_space" is not set to "2", or is missing, this is a finding.

## Group: SRG-OS-000437-GPOS-00194

**Group ID:** `V-269453`

### Rule: AlmaLinux OS 9 must remove all software components after updated versions have been installed.

**Rule ID:** `SV-269453r1050336_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Previous versions of software components that are not removed from the information system after updates have been installed may be exploited by some adversaries.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 removes all software components after updated versions have been installed with the following command: $ dnf config-manager --dump | grep clean clean_requirements_on_remove = 1 If "clean_requirements_on_remove" is not set to "1", this is a finding.

## Group: SRG-OS-000439-GPOS-00195

**Group ID:** `V-269454`

### Rule: AlmaLinux OS 9 must be a supported release.

**Rule ID:** `SV-269454r1050337_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with operating systems are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the version of AlmaLinux is vendor supported with the following command: $ hostnamectl status | grep -i system AlmaLinux OS 9.2 (Turquois Kodkod) If the installed version of AlmaLinux is not supported, this is a finding.

## Group: SRG-OS-000445-GPOS-00199

**Group ID:** `V-269455`

### Rule: AlmaLinux OS 9 must enable the SELinux targeted policy.

**Rule ID:** `SV-269455r1050338_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the SELinux policy to "targeted" or a more specialized policy ensures the system will confine processes that are likely to be targeted for exploitation, such as network or system services. Note: During the development or debugging of SELinux modules, it is common to temporarily place nonproduction systems in "permissive" mode. In such temporary cases, SELinux policies should be developed, and once work is completed, the system should be reconfigured to "targeted".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SELinux on AlmaLinux OS 9 is using the targeted policy with the following command: $ sestatus | grep policy Loaded policy name: targeted If the loaded policy name is not "targeted", this is a finding.

## Group: SRG-OS-000445-GPOS-00199

**Group ID:** `V-269456`

### Rule: AlmaLinux OS 9 must have the Advanced Intrusion Detection Environment (AIDE) package installed.

**Rule ID:** `SV-269456r1050339_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. This requirement applies to operating systems performing security function verification/testing and/or systems and environments that require this functionality. Satisfies: SRG-OS-000445-GPOS-00199, SRG-OS-000446-GPOS-00200, SRG-OS-000363-GPOS-00150</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 has the AIDE package installed with the following command: $ dnf list --installed aide aide.x86_64 0.16-100.el9 @AppStream If AIDE is not installed, ask the system administrator (SA) how file integrity checks are performed on the system. If there is no application installed to perform integrity checks, this is a finding. If AIDE is installed, check if it has been initialized with the following command: $ /usr/sbin/aide --check If the output is "Couldn't open file /var/lib/aide/aide.db.gz for reading", this is a finding.

## Group: SRG-OS-000447-GPOS-00201

**Group ID:** `V-269457`

### Rule: AlmaLinux OS 9 must routinely check the baseline configuration for unauthorized changes and notify the system administrator when anomalies in the operation of any security functions are discovered.

**Rule ID:** `SV-269457r1050340_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to the operating system. Changes to operating system configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of the operating system. The operating system's information management officer (IMO)/information system security officer (ISSO) and system administrators (SAs) must be notified via email and/or monitoring system trap when there is an unauthorized modification of a configuration item. Notifications provided by information systems include messages to local computer consoles, and/or hardware indications, such as lights. This capability must take into account operational requirements for availability for selecting an appropriate response. The organization may choose to shut down or restart the information system upon security function anomaly detection. Satisfies: SRG-OS-000447-GPOS-00201, SRG-OS-000446-GPOS-00200, SRG-OS-000363-GPOS-00150</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 routinely executes a file integrity scan for changes to the system baseline. The command used in the example will use a daily occurrence. Check the cron directories for scripts controlling the execution and notification of results of the file integrity application. For example, if Advanced Intrusion Detection Environment (AIDE) is installed on the system, use the following commands: $ find /etc/cron* -name '*aide*' /etc/cron.d/0aide $ grep aide /etc/crontab /var/spool/cron/root /var/spool/cron/root:30 04 * * * root /usr/sbin/aide --check $ more /etc/cron.d/aide @daily root /usr/sbin/aide --check | /bin/mail -s "$HOSTNAME - Daily aide integrity check run" root If the file integrity application does not exist, or a script file controlling the execution of the file integrity application does not exist, or the file integrity application does not notify designated personnel of changes, this is a finding.

## Group: SRG-OS-000062-GPOS-00031

**Group ID:** `V-269458`

### Rule: AlmaLinux OS 9 audit system must audit local events.

**Rule ID:** `SV-269458r1050341_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, the source of events, where events occurred, and the outcome of events, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. If option "local_events" is not set to "yes", only events from network will be aggregated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the AlmaLinux OS 9 audit system is configured to audit local events with the following command: $ grep local_events /etc/audit/auditd.conf local_events = yes If "local_events" is not set to "yes", if the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-269459`

### Rule: AlmaLinux OS 9 /etc/audit/auditd.conf file must have 0640 or less permissive to prevent unauthorized access.

**Rule ID:** `SV-269459r1050342_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the mode of /etc/audit/auditd.conf with the command: $ stat -c "%#a %n" /etc/audit/auditd.conf 0640 /etc/audit/auditd.conf If "/etc/audit/auditd.conf" does not have a mode of "0640", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-269460`

### Rule: AlmaLinux OS 9 must allow only the information system security manager (ISSM) (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited.

**Rule ID:** `SV-269460r1050343_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the following files have a mode of "0640" or less permissive with the following command: $ stat -c "%U:%G %#a %n" /etc/audit/rules.d/*.rules /etc/audit/audit.rules /etc/audit/auditd.conf root:root 0600 /etc/audit/rules.d/audit.rules root:root 0640 /etc/audit/audit.rules root:root 0640 /etc/audit/auditd.conf If the files file have a mode more permissive than "0640", this is a finding.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-269461`

### Rule: Successful/unsuccessful uses of the init command in AlmaLinux OS 9 must generate an audit record.

**Rule ID:** `SV-269461r1050344_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000477-GPOS-00222, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "init" command with the following command: $ auditctl -l | grep init -a always,exit -S all -F path=/usr/sbin/init -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged-init If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-269462`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "poweroff" command.

**Rule ID:** `SV-269462r1050345_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000477-GPOS-00222, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "poweroff" command with the following command: $ auditctl -l | grep poweroff -a always,exit -S all -F path=/usr/sbin/poweroff -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged-poweroff If the command does not return an audit rule for "poweroff" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-269463`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "reboot" command.

**Rule ID:** `SV-269463r1050346_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000477-GPOS-00222, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "reboot" command with the following command: $ auditctl -l | grep reboot -a always,exit -S all -F path=/usr/sbin/reboot -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged-reboot If the command does not return an audit rule for "reboot" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-269464`

### Rule: AlmaLinux must generate audit records for any use of the "shutdown" command.

**Rule ID:** `SV-269464r1050347_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000477-GPOS-00222, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "shutdown" command with the following command: $ auditctl -l | grep shutdown -a always,exit -S all -F path=/usr/sbin/shutdown -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged-shutdown If the command does not return an audit rule for "shutdown" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-269465`

### Rule: AlmaLinux OS 9 must enable Linux audit logging for the USBGuard daemon.

**Rule ID:** `SV-269465r1050348_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If the USBGuard daemon is not installed and enabled, this requirement is not applicable. Verify AlmaLinux OS 9 enables Linux audit logging of the USBGuard daemon with the following commands. $ grep AuditBackend /etc/usbguard/usbguard-daemon.conf AuditBackend=LinuxAudit If the "AuditBackend" entry does not equal "LinuxAudit", is missing, or the line is commented out, this is a finding.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-269466`

### Rule: AlmaLinux OS 9 must audit all uses of the delete_module, init_module and finit_module system calls.

**Rule ID:** `SV-269466r1050349_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000477-GPOS-00222, SRG-OS-000471-GPOS-00216</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "delete_module", "init_module" and "finit_module" system calls with the following command: $ auditctl -l | grep module -a always,exit -F arch=b32 -S init_module,finit_module -F auid>=1000 -F auid!=unset -k module_chng -a always,exit -F arch=b64 -S init_module,finit_module -F auid>=1000 -F auid!=unset -k module_chng -a always,exit -F arch=b32 -S delete_module -F auid>=1000 -F auid!=unset -k module_chng -a always,exit -F arch=b64 -S delete_module -F auid>=1000 -F auid!=unset -k module_chng If both the "b32" and "b64" audit rules are not defined for the "delete_module", "init_module" and "finit_module" system calls, or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000392-GPOS-00172

**Group ID:** `V-269467`

### Rule: AlmaLinux OS 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /var/log/tallylog.

**Rule ID:** `SV-269467r1050350_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000392-GPOS-00172, SRG-OS-000470-GPOS-00214, SRG-OS-000473-GPOS-00218</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 generates audit records for all account creations, modifications, disabling, and termination events that affect "/var/log/tallylog" with the following command: $ grep /var/log/tallylog /etc/audit/audit.rules -w /var/log/tallylog -p wa -k logins If the command does not return a line or the line is commented out, this is a finding.

## Group: SRG-OS-000255-GPOS-00096

**Group ID:** `V-269468`

### Rule: AlmaLinux OS 9 must produce audit records containing information to establish the identity of any individual or process associated with the event.

**Rule ID:** `SV-269468r1050351_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without information that establishes the identity of the subjects (i.e., users or processes acting on behalf of users) associated with the events, security personnel cannot determine responsibility for the potentially harmful event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the AlmaLinux OS 9 audit system is configured to resolve audit information before writing to disk with the following command: $ grep log_format /etc/audit/auditd.conf log_format = ENRICHED If the "log_format" option is not "ENRICHED", or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269469`

### Rule: The audit package must be installed on AlmaLinux OS 9.

**Rule ID:** `SV-269469r1050352_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, the source of events, where events occurred, and the outcome of events, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in audit logs provides a means of investigating an attack, recognizing resource usage or capacity thresholds, or identifying an improperly configured AlmaLinux OS 9 system. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00020, SRG-OS-000042-GPOS-00021, SRG-OS-000051-GPOS-00024, SRG-OS-000392-GPOS-00172, SRG-OS-000473-GPOS-00218, SRG-OS-000472-GPOS-00217, SRG-OS-000474-GPOS-00219, SRG-OS-000365-GPOS-00152, SRG-OS-000358-GPOS-00145, SRG-OS-000348-GPOS-00136, SRG-OS-000349-GPOS-00137, SRG-OS-000350-GPOS-00138, SRG-OS-000351-GPOS-00139, SRG-OS-000352-GPOS-00140, SRG-OS-000353-GPOS-00141, SRG-OS-000354-GPOS-00142, SRG-OS-000337-GPOS-00129, SRG-OS-000062-GPOS-00031, SRG-OS-000054-GPOS-00025</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the audit package is installed with the following command: $ dnf list --installed audit Installed Packages audit.x86_64 3.0.7-103.el9 @anaconda If the "audit" package is not installed, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269470`

### Rule: AlmaLinux OS 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /var/log/lastlog.

**Rule ID:** `SV-269470r1050353_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000473-GPOS-00218, SRG-OS-000470-GPOS-00214</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 generates audit records for all account creations, modifications, disabling, and termination events that affect "/var/log/lastlog" with the following command: $ grep /var/log/lastlog /etc/audit/audit.rules -w /var/log/lastlog -p wa -k logins If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269471`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "mount" command.

**Rule ID:** `SV-269471r1050354_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "mount" command with the following command: $ auditctl -l | grep mount -a always,exit -F path=/usr/bin/mount -F perm=x -F auid>=1000 -F auid!=unset -k privileged-mount If the command does not return an audit rule for "/usr/bin/mount" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269472`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "umount" command.

**Rule ID:** `SV-269472r1050355_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "umount" command with the following command: $ auditctl -l | grep umount -a always,exit -F path=/usr/bin/umount -F perm=x -F auid>=1000 -F auid!=unset -k privileged-mount If the command does not return an audit rule for "umount" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269473`

### Rule: Successful/unsuccessful uses of the umount2 system call in AlmaLinux OS 9 must generate an audit record.

**Rule ID:** `SV-269473r1050356_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "umount2" system call with the following command: $ auditctl -l | grep umount2 -a always,exit -F arch=b32 -S umount2 -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S umount2 -F auid>=1000 -F auid!=unset -F key=perm_mod If both the "b32" and "b64" audit rules are not defined for the "umount2" system call, or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269474`

### Rule: AlmaLinux OS 9 must enable auditing of processes that start prior to the audit daemon.

**Rule ID:** `SV-269474r1050357_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. If auditing is enabled late in the startup process, the actions of some startup processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000473-GPOS-00218, SRG-OS-000254-GPOS-00095</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that GRUB 2 is configured to enable auditing of processes that start prior to the audit daemon with the following commands: Check that the all GRUB2 entries have auditing enabled: $ grubby --info=ALL | grep audit args="ro audit=1 selinux=1 enforcing=1 audit_backlog_limit=8192 page_poison=1 vsyscall=none slub_debug=P pti=on iommu=force boot=UUID=eda01e9b-b7e1-431b-9549-16d5dcddf665 resume=/dev/mapper/luks-89bf0df8-547f-4613-af07-215e5f62e9a9 rd.luks.uuid=luks-8a7154ec-8eeb-46c8-9d75-66fc4b80d665 rd.lvm.lv=rootvg/root rd.luks.uuid=luks-89bf0df8-547f-4613-af07-215e5f62e9a9 rd.lvm.lv=rootvg/swap fips=1 rd.shell=0 quiet splash" If "audit" is not set to "1" or is missing, this is a finding. Check that auditing is enabled by default to persist in kernel updates: $ grep audit /etc/default/grub GRUB_CMDLINE_LINUX="audit=1 selinux=1 enforcing=1 audit_backlog_limit=8192 page_poison=1 vsyscall=none slub_debug=P pti=on iommu=force boot=UUID=eda01e9b-b7e1-431b-9549-16d5dcddf665 resume=/dev/mapper/luks-89bf0df8-547f-4613-af07-215e5f62e9a9 rd.luks.uuid=luks-8a7154ec-8eeb-46c8-9d75-66fc4b80d665 rd.lvm.lv=rootvg/root rd.luks.uuid=luks-89bf0df8-547f-4613-af07-215e5f62e9a9 rd.lvm.lv=rootvg/swap fips=1 rd.shell=0 quiet splash" If "audit" is not set to "1", is missing, or is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269475`

### Rule: AlmaLinux OS 9 must audit all uses of the truncate, ftruncate, creat, open, openat, and open_by_handle_at system calls.

**Rule ID:** `SV-269475r1050358_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000064-GPOS-00033, SRG-OS-000458-GPOS-00203, SRG-OS-000461-GPOS-00205</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "truncate", "ftruncate", "creat", "open", "openat", and "open_by_handle_at" system calls with the following command: $ grep -E 'open|truncate|creat' /etc/audit/audit.rules -a always,exit -F arch=b32 -S open,creat,truncate,ftruncate,openat,open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=perm_access -a always,exit -F arch=b64 -S open,truncate,ftruncate,creat,openat,open_by_handle_at -F exit=-EPERM -F auid>=1000 -F auid!=unset -F key=perm_access -a always,exit -F arch=b32 -S open,creat,truncate,ftruncate,openat,open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=perm_access -a always,exit -F arch=b64 -S open,truncate,ftruncate,creat,openat,open_by_handle_at -F exit=-EACCES -F auid>=1000 -F auid!=unset -F key=perm_access If both the "b32" and "b64" audit rules are not defined for the "truncate", "ftruncate", "creat", "open", "openat", and "open_by_handle_at" system calls, or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269476`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "chacl" command.

**Rule ID:** `SV-269476r1050359_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000466-GPOS-00210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "chacl" command with the following command: $ grep /chacl /etc/audit/audit.rules -a always,exit -S all -F path=/usr/bin/chacl -F perm=x -F auid>=1000 -F auid!=unset -F key=perm_mod If the command does not return an audit rule for "chacl" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269477`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "chage" command.

**Rule ID:** `SV-269477r1050360_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "chage" command with the following command: $ grep /chage /etc/audit/audit.rules -a always,exit -S all -F path=/usr/bin/chage -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged-chage If the command does not return an audit rule for "chage" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269478`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "chcon" command.

**Rule ID:** `SV-269478r1050361_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000468-GPOS-00212, SRG-OS-000471-GPOS-00215, SRG-OS-000463-GPOS-00207, SRG-OS-000465-GPOS-00209</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "chcon" command with the following command: $ grep /chcon /etc/audit/audit.rules -a always,exit -S all -F path=/usr/bin/chcon -F perm=x -F auid>=1000 -F auid!=unset -F key=perm_mod If the command does not return an audit rule for "chcon" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269479`

### Rule: AlmaLinux OS 9 must audit all uses of the chmod, fchmod, and fchmodat system calls.

**Rule ID:** `SV-269479r1050362_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000064-GPOS-00033, SRG-OS-000466-GPOS-00210, SRG-OS-000458-GPOS-00203</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "chmod", "fchmod", and "fchmodat" system calls with the following command: $ auditctl -l | grep chmod -a always,exit -F arch=b32 -S chmod,fchmod,fchmodat -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b64 -S chmod,fchmod,fchmodat -F auid>=1000 -F auid!=unset -k perm_mod If both the "b32" and "b64" audit rules are not defined for the "chmod", "fchmod", and "fchmodat" system calls, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269480`

### Rule: AlmaLinux OS 9 must audit all uses of the chown, fchown, fchownat, and lchown system calls.

**Rule ID:** `SV-269480r1050363_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000064-GPOS-00033, SRG-OS-000466-GPOS-00210, SRG-OS-000458-GPOS-00203, SRG-OS-000474-GPOS-00219</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "chown", "fchown", "fchownat", and "lchown" system calls with the following command: $ auditctl -l | grep chown -a always,exit -F arch=b32 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=unset -k perm_mod -a always,exit -F arch=b64 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=unset -k perm_mod If both the "b32" and "b64" audit rules are not defined for the "chown", "fchown", "fchownat", and "lchown" system calls, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269481`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "chsh" command.

**Rule ID:** `SV-269481r1050364_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "chsh" command with the following command: $ auditctl -l | grep chsh -a always,exit -S all -F path=/usr/bin/chsh -F perm=x -F auid>=1000 -F auid!=unset -F key=priv_cmd If the command does not return an audit rule for "chsh" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269482`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "crontab" command.

**Rule ID:** `SV-269482r1050365_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "crontab" command with the following command: $ auditctl -l | grep crontab -a always,exit -S all -F path=/usr/bin/crontab -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged-crontab If the command does not return an audit rule for "crontab" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269483`

### Rule: AlmaLinux OS 9 must audit all uses of the rename, unlink, rmdir, renameat, and unlinkat system calls.

**Rule ID:** `SV-269483r1050366_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000466-GPOS-00210, SRG-OS-000467-GPOS-00211, SRG-OS-000468-GPOS-00212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "rename", "unlink", "rmdir", "renameat", and "unlinkat" system calls with the following command: $ auditctl -l | grep rename -a always,exit -F arch=b32 -S unlink,rename,rmdir,unlinkat,renameat -F auid>=1000 -F auid!=unset -F key=delete -a always,exit -F arch=b64 -S rename,rmdir,unlink,unlinkat,renameat -F auid>=1000 -F auid!=unset -F key=delete If both the "b32" and "b64" audit rules are not defined for the "rename", "unlink", "rmdir", "renameat", and "unlinkat" system calls, or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-269484`

### Rule: AlmaLinux OS 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /var/log/faillock.

**Rule ID:** `SV-269484r1050367_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000477-GPOS-00222, SRG-OS-000476-GPOS-00221, SRG-OS-000475-GPOS-00220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 generates audit records for all account creations, modifications, disabling, and termination events that affect "/var/log/faillock" with the following command: $ grep /var/log/faillock /etc/audit/audit.rules -w /var/log/faillock -p wa -k logins If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269485`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "gpasswd" command.

**Rule ID:** `SV-269485r1050368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "gpasswd" command with the following command: $ auditctl -l | grep gpasswd -a always,exit -S all -F path=/usr/bin/gpasswd -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged-gpasswd If the command does not return an audit rule for "gpasswd" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269486`

### Rule: AlmaLinux OS 9 must audit all uses of the kmod command.

**Rule ID:** `SV-269486r1050369_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000471-GPOS-00216, SRG-OS-000477-GPOS-00222</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "kmod" command with the following command: $ auditctl -l | grep kmod -a always,exit -F path=/usr/bin/kmod -F perm=x -F auid>=1000 -F auid!=unset -k modules If the command does not return a line, or the line is commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269487`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "newgrp" command.

**Rule ID:** `SV-269487r1050370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "newgrp" command with the following command: $ auditctl -l | grep newgrp -a always,exit -S all -F path=/usr/bin/newgrp -F perm=x -F auid>=1000 -F auid!=unset -F key=priv_cmd If the command does not return an audit rule for "newgrp" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269488`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "passwd" command.

**Rule ID:** `SV-269488r1050371_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "passwd" command with the following command: $ auditctl -l | grep passwd -a always,exit -S all -F path=/usr/bin/passwd -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged-passwd If the command does not return an audit rule for "passwd" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269489`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "postdrop" command.

**Rule ID:** `SV-269489r1050372_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "postdrop" command with the following command: $ auditctl -l | grep postdrop -a always,exit -S all -F path=/usr/sbin/postdrop -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged-unix-update If the command does not return an audit rule for "postdrop" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269490`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "postqueue" command.

**Rule ID:** `SV-269490r1050373_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "postqueue" command with the following command: $ auditctl -l | grep postqueue -a always,exit -S all -F path=/usr/sbin/postqueue -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged-unix-update If the command does not return an audit rule for "postqueue" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269491`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "su" command.

**Rule ID:** `SV-269491r1050374_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit record specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000064-GPOS-00033, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000466-GPOS-00210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "su" command with the following command: $ grep -w path=/usr/bin/su /etc/audit/audit.rules -a always,exit -S all -F path=/usr/bin/su -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged-priv_change If the command does not return a matching line, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269492`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "sudo" command.

**Rule ID:** `SV-269492r1050375_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit record specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000064-GPOS-00033, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000466-GPOS-00210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "sudo" command. $ grep -w path=/usr/bin/sudo /etc/audit/audit.rules -a always,exit -S all -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -F auid!=unset -F key=priv_cmd If the command does not return a matching line, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269493`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "semanage" command.

**Rule ID:** `SV-269493r1050376_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000463-GPOS-00207, SRG-OS-000465-GPOS-00209</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "semanage" command with the following command: $ auditctl -l | grep semanage -a always,exit -S all -F path=/usr/sbin/semanage -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged-unix-update If the command does not return an audit rule for "semanage" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269494`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "setfacl" command.

**Rule ID:** `SV-269494r1050377_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "setfacl" command with the following command: $ auditctl -l | grep setfacl -a always,exit -S all -F path=/usr/bin/setfacl -F perm=x -F auid>=1000 -F auid!=unset -F key=perm_mod If the command does not return an audit rule for "setfacl" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269495`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "setfiles" command.

**Rule ID:** `SV-269495r1050378_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000463-GPOS-00207, SRG-OS-000465-GPOS-00209</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "setfiles" command with the following command: $ auditctl -l | grep setfiles -a always,exit -F path=/usr/sbin/setfiles -F perm=x -F auid>=1000 -F auid!=unset -k privileged-unix-update If the command does not return an audit rule for "setfiles" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269496`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "setsebool" command.

**Rule ID:** `SV-269496r1050379_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000463-GPOS-00207, SRG-OS-000465-GPOS-00209</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "setsebool" command with the following command: $ auditctl -l | grep setsebool -a always,exit -S all -F path=/usr/sbin/setsebool -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged If the command does not return an audit rule for "setsebool" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269497`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "ssh-agent" command.

**Rule ID:** `SV-269497r1050380_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "ssh-agent" command with the following command: $ auditctl -l | grep ssh-agent -a always,exit -S all -F path=/usr/bin/ssh-agent -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged-ssh If the command does not return an audit rule for "ssh-agent" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269498`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "ssh-keysign" command.

**Rule ID:** `SV-269498r1050381_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "ssh-keysign" command with the following command: $ auditctl -l | grep ssh-keysign -a always,exit -S all -F path=/usr/bin/ssh-keysign -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged-ssh If the command does not return an audit rule for "ssh-keysign" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269499`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "sudoedit" command.

**Rule ID:** `SV-269499r1050382_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "sudoedit" command with the following command: $ auditctl -l | grep sudoedit -a always,exit -S all -F path=/usr/bin/sudoedit -F perm=x -F auid>=1000 -F auid!=unset -F key=priv_cmd If the command does not return an audit rule for "sudoedit" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269500`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "pam_timestamp_check" command.

**Rule ID:** `SV-269500r1050383_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "pam_timestamp_check" command with the following command: $ auditctl -l | grep timestamp -a always,exit -S all -F path=/usr/sbin/pam_timestamp_check -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged-pam_timestamp_check If the command does not return an audit rule for "pam_timestamp_check" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269501`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "unix_chkpwd" command.

**Rule ID:** `SV-269501r1050384_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "unix_chkpwd" command with the following command: $ auditctl -l | grep unix_chkpwd -a always,exit -S all -F path=/usr/sbin/unix_chkpwd -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged-unix-update If the command does not return an audit rule for "unix_chkpwd" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269502`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "unix_update" command.

**Rule ID:** `SV-269502r1050385_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000064-GPOS-00033, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "unix_update" command with the following command: $ grep /unix_update /etc/audit/audit.rules -a always,exit -S all -F path=/usr/sbin/unix_update -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged-unix-update If the command does not return an audit rule for "unix_update" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269503`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "userhelper" command.

**Rule ID:** `SV-269503r1050386_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "userhelper" command with the following command: $ auditctl -l | grep userhelper -a always,exit -S all -F path=/usr/sbin/userhelper -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged-unix-update If the command does not return an audit rule for "userhelper" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269504`

### Rule: AlmaLinux OS 9 must generate audit records for any use of the "usermod" command.

**Rule ID:** `SV-269504r1050387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000462-GPOS-00206, SRG-OS-000471-GPOS-00215, SRG-OS-000466-GPOS-00210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "usermod" command with the following command: $ auditctl -l | grep usermod -a always,exit -S all -F path=/usr/sbin/usermod -F perm=x -F auid>=1000 -F auid!=unset -F key=privileged-usermod If the command does not return an audit rule for "usermod" or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000037-GPOS-00015

**Group ID:** `V-269505`

### Rule: AlmaLinux OS 9 must audit all uses of the setxattr, fsetxattr, lsetxattr, removexattr, fremovexattr, and lremovexattr system calls.


**Rule ID:** `SV-269505r1050388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). When a user logs on, the auid is set to the uid of the account being authenticated. Daemons are not user sessions and have the loginuid set to -1. The auid representation is an unsigned 32-bit integer, which equals 4294967295. The audit system interprets -1, 4294967295, and "unset" in the same way. The system call rules are loaded into a matching engine that intercepts each system call made by all programs on the system. Therefore, it is very important to use system call rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance can be helped, however, by combining system calls into one rule whenever possible. Satisfies: SRG-OS-000037-GPOS-00015, SRG-OS-000042-GPOS-00020, SRG-OS-000062-GPOS-00031, SRG-OS-000392-GPOS-00172, SRG-OS-000458-GPOS-00203, SRG-OS-000462-GPOS-00206, SRG-OS-000463-GPOS-00207, SRG-OS-000471-GPOS-00215, SRG-OS-000474-GPOS-00219, SRG-OS-000466-GPOS-00210, SRG-OS-000064-GPOS-00033</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr" system calls with the following command: $ auditctl -l | grep xattr -a always,exit -F arch=b32 -S setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b64 -S setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr -F auid>=1000 -F auid!=unset -F key=perm_mod -a always,exit -F arch=b32 -S setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr -F auid=0 -F key=perm_mod -a always,exit -F arch=b64 -S setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr -F auid=0 -F key=perm_mod If both the "b32" and "b64" audit rules are not defined for the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr" system calls, or any of the lines returned are commented out, this is a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-269506`

### Rule: AlmaLinux OS 9 must allocate an audit_backlog_limit of sufficient size to capture processes that start prior to the audit daemon.

**Rule ID:** `SV-269506r1101808_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. If auditing is enabled late in the startup process, the actions of some startup processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created. Audit records can be generated from various components within the information system (e.g., module or policy filter). Allocating an audit_backlog_limit of sufficient size is critical in maintaining a stable boot process. With an insufficient limit allocated, the system is susceptible to boot failures and crashes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 allocates a sufficient audit_backlog_limit to capture processes that start prior to the audit daemon with the following command: $ sudo grubby --info=ALL | grep args | grep 'audit_backlog_limit' If the command returns any outputs, and audit_backlog_limit is less than "8192", this is a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-269507`

### Rule: AlmaLinux OS 9 must use a separate file system for the system audit data path.

**Rule ID:** `SV-269507r1050390_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Placing "/var/log/audit" in its own partition enables better separation between audit files and other system files, and helps ensure that auditing cannot be halted due to the partition running out of space.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a separate file system/partition has been created for the system audit data path with the following command: Note: /var/log/audit is used as the example as it is a common location. $ findmnt /var/log/audit TARGET SOURCE FSTYPE OPTIONS /var/log/audit /dev/mapper/luks-29b74747-2f82-4472-82f5-0b5eb763effc xfs rw,nosuid,nodev,noexec,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota If no line is returned, this is a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-269508`

### Rule: AlmaLinux OS 9 must allocate audit record storage capacity to store at least one week's worth of audit records.

**Rule ID:** `SV-269508r1050391_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure AlmaLinux OS 9 systems have a sufficient storage capacity in which to write the audit logs, AlmaLinux OS 9 needs to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial installation of AlmaLinux OS 9.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 allocates audit record storage capacity to store at least one week of audit records when audit records are not immediately sent to a central audit record storage facility. Note: The partition size needed to capture a week of audit records is based on the activity level of the system and the total storage capacity available. Typically 10GB of storage space for audit records should be sufficient. Determine which partition the audit records are being written to with the following command: $ grep -w log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Check the size of the partition that audit records are written to with the following command and verify whether it is sufficiently large: $ df -h /var/log/audit/ Filesystem Size Used Avail Use% Mounted on /dev/mapper/luks-29b74747-2f82-4472-82f5-0b8eb763effc 1002M 77M 926M 8% /var/log/audit If the audit record partition is not allocated for sufficient storage capacity, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-269509`

### Rule: AlmaLinux OS 9 audispd-plugins package must be installed.

**Rule ID:** `SV-269509r1050392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>"audispd-plugins" provides plugins for the real-time interface to the audit subsystem, "audispd". These plugins can do things like relay events to remote machines or analyze events for suspicious behavior.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 has the audispd-plugins package for installed with the following command: $ dnf list --installed audispd-plugins audispd-plugins.x86_64 3.0.7-103.el9 @anaconda If the "audispd-plugins" package is not installed, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-269510`

### Rule: AlmaLinux OS 9 must label all offloaded audit logs before sending them to the central log server.

**Rule ID:** `SV-269510r1050393_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When audit logs are not labelled before they are sent to a central log server, the audit data will not be able to be analyzed and tied back to the correct system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 Audit Daemon is configured to label all offloaded audit logs, with the following command: $ grep name_format /etc/audit/auditd.conf name_format = HOSTNAME If the "name_format" option is not "HOSTNAME", "fqd", or "numeric", or the line is commented out, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-269511`

### Rule: AlmaLinux OS 9 must take appropriate action when the internal event queue is full.

**Rule ID:** `SV-269511r1050394_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The audit system should have an action setup in the event the internal event queue becomes full so that no data is lost.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 audit system is configured to take an appropriate action when the internal event queue is full: $ grep -i overflow_action /etc/audit/auditd.conf overflow_action = SYSLOG If the value of the "overflow_action" option is not set to "SYSLOG", "SINGLE", "HALT" or the line is commented out, ask the system administrator (SA) to indicate how the audit logs are offloaded to a different system or media. If there is no evidence that the transfer of the audit logs being offloaded to another system or media takes appropriate action if the internal event queue becomes full, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-269512`

### Rule: AlmaLinux OS 9 must be configured to offload audit records onto a different system from the system being audited via syslog.

**Rule ID:** `SV-269512r1050395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The auditd service does not include the ability to send audit records to a centralized server for management directly. However, it can use a plug-in for audit event multiplexor (audispd) to pass audit records to the local syslog server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 is configured use the audisp-remote syslog service with the following command: $ grep active /etc/audit/plugins.d/syslog.conf active = yes If the "active" keyword does not have a value of "yes", the line is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-269513`

### Rule: AlmaLinux OS 9 must authenticate the remote logging server for offloading audit logs via rsyslog.

**Rule ID:** `SV-269513r1050396_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 authenticates the remote logging server for offloading audit logs with the following command: $ grep -i '$ActionSendStreamDriverAuthMode' /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.d/stig.conf:$ActionSendStreamDriverAuthMode x509/name If the value of the "$ActionSendStreamDriverAuthMode" option is not set to "x509/name" or the line is commented out, ask the system administrator (SA) to indicate how the audit logs are offloaded to a different system or media. If there is no evidence that the transfer of the audit logs being offloaded to another system or media is encrypted, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-269514`

### Rule: AlmaLinux OS 9 must encrypt the transfer of audit records offloaded onto a different system or media from the system being audited via rsyslog.

**Rule ID:** `SV-269514r1050397_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 encrypts audit records offloaded onto a different system or media from the system being audited via rsyslog with the following command: $ grep -i '$ActionSendStreamDriverMode' /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.d/stig.conf:$ActionSendStreamDriverMode 1 If the value of the "$ActionSendStreamDriverMode" option is not set to "1" or the line is commented out, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-269515`

### Rule: AlmaLinux OS 9 must encrypt, via the gtls driver, the transfer of audit records offloaded onto a different system or media from the system being audited via rsyslog.

**Rule ID:** `SV-269515r1050398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 uses the gtls driver to encrypt audit records offloaded onto a different system or media from the system being audited with the following command: $ grep -i '$DefaultNetstreamDriver' /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.d/stig.conf:$DefaultNetstreamDriver gtls If the value of the "$DefaultNetstreamDriver" option is not set to "gtls" or the line is commented out, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-269516`

### Rule: AlmaLinux OS 9 must have the rsyslog package installed.

**Rule ID:** `SV-269516r1050399_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>rsyslogd is a system utility providing support for message logging. Support for both internet and Unix domain sockets enables this utility to support both local and remote logging. Couple this utility with "gnutls" (which is a secure communications library implementing the SSL, TLS, and DTLS protocols), to create a method to securely encrypt and offload auditing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 has the rsyslog package installed with the following command: $ dnf list --installed rsyslog rsyslog.x86_64 8.2102.0-113.el9_2.1 @appstream If the "rsyslog" package is not installed, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-269517`

### Rule: AlmaLinux OS 9 must be configured to forward audit records via TCP to a different system or media from the system being audited via rsyslog.

**Rule ID:** `SV-269517r1050400_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 audit system offloads audit records onto a different system or media from the system being audited via rsyslog using TCP with the following command: $ grep @@ /etc/rsyslog.conf /etc/rsyslog.d/*.conf /etc/rsyslog.d/stig.conf:*.* @@loghost.example.com" If a remote server is not configured, or the line is commented out, ask the system administrator (SA) to indicate how the audit logs are offloaded to a different system or media. If there is no evidence that the audit logs are being offloaded to another system or media, this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-269518`

### Rule: The rsyslog service on AlmaLinux OS 9 must be active.

**Rule ID:** `SV-269518r1050401_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The "rsyslog" service must be running to provide logging services, which are essential to system administration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "rsyslog" is active with the following command: $ systemctl status rsyslog rsyslog.service - System Logging Service Loaded: loaded (/usr/lib/systemd/system/rsyslog.service; enabled; preset: enabled) Active: active (running) since Mon 2024-03-04 10:10:08 UTC; 3h 20min ago If the rsyslog service is not active, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-269519`

### Rule: AlmaLinux OS 9 must take action when allocated audit record storage volume reaches 95 percent of the audit record storage capacity.

**Rule ID:** `SV-269519r1050402_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches 75 percent usage, they are unable to plan for audit record storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 takes action when allocated audit record storage volume reaches 95 percent of the repository maximum audit record storage capacity with the following command: $ grep -w admin_space_left /etc/audit/auditd.conf admin_space_left = 5% If the value of the "admin_space_left" keyword is not set to 5 percent of the storage volume allocated to audit logs, or if the line is commented out, ask the system administrator (SA) to indicate how the system is taking action if the allocated storage is about to reach capacity. If the "space_left" value is not configured to the correct value, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-269520`

### Rule: AlmaLinux OS 9 must take action when allocated audit record storage volume reaches 95 percent of the repository maximum audit record storage capacity.

**Rule ID:** `SV-269520r1050403_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches 75 percent usage, they are unable to plan for audit record storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to take action in the event of allocated audit record storage volume reaches 95 percent of the repository maximum audit record storage capacity with the following command: $ grep admin_space_left_action /etc/audit/auditd.conf admin_space_left_action = single If the value of the "admin_space_left_action" is not set to "single", or if the line is commented out, ask the system administrator (SA) to indicate how the system is providing real-time alerts to the SA and information system security officer (ISSO). If there is no evidence that real-time alerts are configured on the system, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-269521`

### Rule: AlmaLinux OS 9 must take action when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity.

**Rule ID:** `SV-269521r1101829_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches a maximum of 75 percent utilization, they are unable to plan for audit record storage capacity expansion. The notification can be set to trigger at lower utilization thresholds at the information system security officer's (ISSO's) discretion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 takes action when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity with the following command: $ grep -w space_left /etc/audit/auditd.conf space_left = 25% If the value of the "space_left" keyword is not set to 25 percent or greater of the storage volume allocated to audit logs, or if the line is commented out, ask the system administrator (SA) to indicate how the system is providing real-time alerts to the SA and ISSO. If the "space_left" value is not configured to the value 25% or more, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-269522`

### Rule: AlmaLinux OS 9 must notify the system administrator (SA) and information system security officer (ISSO) (at a minimum) when allocated audit record storage volume reaches 75 percent usage.

**Rule ID:** `SV-269522r1050604_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches 75 percent usage, they are unable to plan for audit record storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 notifies the SA and ISSO (at a minimum) when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity with the following command: $ grep -w space_left_action /etc/audit/auditd.conf space_left_action = email If the value of the "space_left_action" is not set to "email", or if the line is commented out, ask the SA to indicate how the system is providing real-time alerts to the SA and ISSO. If there is no evidence that real-time alerts are configured on the system, this is a finding.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-269523`

### Rule: AlmaLinux OS 9 System Administrator (SA) and/or information system security officer (ISSO) (at a minimum) must be alerted of an audit processing failure event.

**Rule ID:** `SV-269523r1050406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to notify the SA and/or ISSO (at a minimum) in the event of an audit processing failure with the following command: $ grep action_mail_acct /etc/audit/auditd.conf action_mail_acct = root If the value of the "action_mail_acct" keyword is not set to "root" and/or other accounts for security personnel, the "action_mail_acct" keyword is missing, or the retuned line is commented out, ask the SA to indicate how they and the ISSO are notified of an audit process failure (e.g. using syslog). If there is no evidence of the proper personnel being notified of an audit processing failure, this is a finding.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-269524`

### Rule: AlmaLinux OS 9 must have mail aliases to notify the information system security officer (ISSO) and system administrator (SA) (at a minimum) in the event of an audit processing failure.

**Rule ID:** `SV-269524r1050407_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If postfix is not installed or used to send email remotely, then this requirement is Not Applicable. Verify that AlmaLinux OS 9 is configured to notify the appropriate interactive users in the event of an audit processing failure. Find the alias maps that are being used with the following command: $ postconf alias_maps alias_maps = hash:/etc/aliases Query the Postfix alias maps for an alias for the root user with the following command: $ postmap -q root hash:/etc/aliases isso If an alias is not set, this is a finding.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-269525`

### Rule: AlmaLinux OS 9 audit system must take appropriate action when an error writing to the audit storage volume occurs.

**Rule ID:** `SV-269525r1050408_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the operating system is at risk of failing to process audit logs as required, it takes action to mitigate the failure. Audit processing failures include software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When availability is an overriding concern, other approved actions in response to an audit failure are as follows: 1) If the failure was caused by the lack of audit record storage capacity, the operating system must continue generating audit records if possible (automatically restarting the audit service if necessary), overwriting the oldest audit records in a first-in-first-out manner. 2) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, the operating system must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 takes the appropriate action when an audit processing failure occurs due to a disk error, with the following command: $ grep disk_error_action /etc/audit/auditd.conf disk_error_action = HALT If the value of the "disk_error_action" option is not "SYSLOG", "SINGLE", or "HALT", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-269526`

### Rule: AlmaLinux OS 9 audit system must take appropriate action when the audit storage volume is full.

**Rule ID:** `SV-269526r1050409_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the operating system is at risk of failing to process audit logs as required, it takes action to mitigate the failure. Audit processing failures include software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When availability is an overriding concern, other approved actions in response to an audit failure are as follows: 1) If the failure was caused by the lack of audit record storage capacity, the operating system must continue generating audit records if possible (automatically restarting the audit service if necessary), overwriting the oldest audit records in a first-in-first-out manner. 2) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, the operating system must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 takes the appropriate action when the audit storage volume is full, with the following command: $ grep disk_full_action /etc/audit/auditd.conf disk_full_action = HALT If the value of the "disk_full_action" option is not "SYSLOG", "SINGLE", or "HALT", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-269527`

### Rule: AlmaLinux OS 9 must take appropriate action when a critical audit processing failure occurs.

**Rule ID:** `SV-269527r1050410_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the operating system is at risk of failing to process audit logs as required, it takes action to mitigate the failure. Audit processing failures include software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When availability is an overriding concern, other approved actions in response to an audit failure are as follows: 1) If the failure was caused by the lack of audit record storage capacity, the operating system must continue generating audit records if possible (automatically restarting the audit service if necessary), overwriting the oldest audit records in a first-in-first-out manner. 2) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, the operating system must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the auditd service is configured to panic on a critical error with the following command: $ auditctl -s failure 2 A number of parameters will display. If the value for "failure" is not "2", and availability is not documented as an overriding concern, this is a finding.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-269528`

### Rule: AlmaLinux OS 9 audit system must make full use of the audit storage space.

**Rule ID:** `SV-269528r1050411_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>max_log_file (size in megabytes) multiplied by num_logs must make full use of the auditd storage volume (separate to the root partition). If max_log_file_action is set to ROTATE or KEEP_LOGS then max_log_file must be set to a value that makes the most use of the storage available.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to make full use of the auditd storage volume when rotation is enabled, with the following command: $ grep max_log_file /etc/audit/auditd.conf max_log_file = 8 If the value of the "max_log_file" option is not sufficiently large to maximize the use of the storage volume, is commented out, or is missing, this is a finding.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-269529`

### Rule: AlmaLinux OS 9 audit system must take appropriate action when the audit files have reached maximum size.

**Rule ID:** `SV-269529r1050412_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the operating system is at risk of failing to process audit logs as required, it takes action to mitigate the failure. Audit processing failures include software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When availability is an overriding concern, other approved actions in response to an audit failure are as follows: 1) If the failure was caused by the lack of audit record storage capacity, the operating system must continue generating audit records if possible (automatically restarting the audit service if necessary), overwriting the oldest audit records in a first-in-first-out manner. 2) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, the operating system must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 takes the appropriate action when the audit files have reached maximum size, with the following command: $ grep max_log_file_action /etc/audit/auditd.conf max_log_file_action = ROTATE If the value of the "max_log_file_action" option is not "ROTATE", "KEEP_LOGS", is commented out, or is missing, this is a finding.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-269530`

### Rule: AlmaLinux OS 9 audit system must retain an optimal number of audit records.

**Rule ID:** `SV-269530r1050413_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>max_log_file (size in megabytes) multiplied by num_logs must make full use of the auditd storage volume (separate to the root partition). If max_log_file_action is set to ROTATE or KEEP_LOGS then num_logs must be set to a value between 2 and 99.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to make full use of the auditd storage volume when rotation is enabled, with the following command: $ grep num_logs /etc/audit/auditd.conf num_logs = 5 If the value of the "num_logs" option is not between 2 and 99, is commented out, or is missing, this is a finding.

## Group: SRG-OS-000051-GPOS-00024

**Group ID:** `V-269531`

### Rule: AlmaLinux OS 9 must periodically flush audit records to disk to prevent the loss of audit records.

**Rule ID:** `SV-269531r1050414_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If option "freq" is not set to a value that requires audit records being written to disk after a threshold number is reached, then audit records may be lost.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that audit system is configured to flush to disk after every 100 records with the following command: $ grep freq /etc/audit/auditd.conf freq = 100 If "freq" is not set to a value between "1" and "100", the value is missing, or the line is commented out, this is a finding.

## Group: SRG-OS-000042-GPOS-00021

**Group ID:** `V-269532`

### Rule: The auditd service must be enabled on AlmaLinux OS 9.

**Rule ID:** `SV-269532r1050415_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of events occurred, the source of events, where events occurred, and the outcome of events, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in audit logs provides a means of investigating an attack, recognizing resource usage or capacity thresholds, or identifying an improperly configured AlmaLinux OS 9 system. Satisfies: SRG-OS-000042-GPOS-00021, SRG-OS-000051-GPOS-00024, SRG-OS-000392-GPOS-00172, SRG-OS-000122-GPOS-00063, SRG-OS-000473-GPOS-00218, SRG-OS-000472-GPOS-00217, SRG-OS-000474-GPOS-00219, SRG-OS-000365-GPOS-00152, SRG-OS-000358-GPOS-00145, SRG-OS-000348-GPOS-00136, SRG-OS-000349-GPOS-00137, SRG-OS-000350-GPOS-00138, SRG-OS-000351-GPOS-00139, SRG-OS-000352-GPOS-00140, SRG-OS-000353-GPOS-00141, SRG-OS-000354-GPOS-00142, SRG-OS-000337-GPOS-00129, SRG-OS-000062-GPOS-00031, SRG-OS-000054-GPOS-00025</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the auditd service is enabled with the following command: $ systemctl status auditd.service auditd.service - Security Auditing Service Loaded: loaded (/usr/lib/systemd/system/auditd.service; enabled; preset: enabled) Active: active (running) since Fri 2024-01-05 14:04:30 UTC; 10min ago If the audit service is not "active" and "running", this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-269533`

### Rule: The chronyd service must be enabled.

**Rule ID:** `SV-269533r1050416_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). Satisfies: SRG-OS-000355-GPOS-00143, SRG-OS-000359-GPOS-00146</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the chronyd service is active with the following command: $ systemctl is-active chronyd active If the chronyd service is not active, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-269534`

### Rule: AlmaLinux OS 9 must have the chrony package installed.

**Rule ID:** `SV-269534r1050417_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). Satisfies: SRG-OS-000355-GPOS-00143, SRG-OS-000359-GPOS-00146</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 has the chrony package installed with the following command: $ dnf list --installed chrony Installed Packages chrony.x86_64 4.3-1.el9 @anaconda If the "chrony" package is not installed, this is a finding.

## Group: SRG-OS-000356-GPOS-00144

**Group ID:** `V-269535`

### Rule: AlmaLinux OS 9 must securely compare internal information system clocks at least every 24 hours.

**Rule ID:** `SV-269535r1050418_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider setting time periods for different types of systems (e.g., financial, legal, or mission-critical systems). Organizations should also consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). This requirement is related to the comparison done every 24 hours in SRG-OS-000355 because a comparison must be done to determine the time difference. Satisfies: SRG-OS-000356-GPOS-00144, SRG-OS-000359-GPOS-00146, SRG-OS-000785-GPOS-00250</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify AlmaLinux OS 9 is securely comparing internal information system clocks at least every 24 hours with an NTP server with the following commands: $ grep maxpoll /etc/chrony.conf server 0.us.pool.ntp.mil iburst maxpoll 16 If the "maxpoll" option is set to a number greater than 16 or the line is commented out, this is a finding. Verify the "chrony.conf" file is configured to an authoritative DOD time source by running the following command: $ grep -i server /etc/chrony.conf server 0.us.pool.ntp.mil If the parameter "server" is not set or is not set to an authoritative DOD time source, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-269536`

### Rule: AlmaLinux OS 9 audit log directory must be owned by root to prevent unauthorized read access.

**Rule ID:** `SV-269536r1050419_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit log directory is owned by "root". First determine where the audit logs are stored with the following command: $ grep -w log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Then using the location of the audit log file, determine if the audit log is owned by the "root" user and group using the following command: $ stat -c "%U:%G %n" /var/log/audit root:root /var/log/audit If the audit log directory is not owned by "root:root", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-269537`

### Rule: AlmaLinux OS 9 audit log directory must have 0700 permissions to prevent unauthorized read access.

**Rule ID:** `SV-269537r1050420_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit log directory has 0700 (u=rwx) permissions. First determine where the audit logs are stored with the following command: $ grep -w log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Then using the location of the audit log file, determine if the audit log directory has 0700 permissions using the following command: $ stat -c "%U:%G %#a %n" /var/log/audit root:root 0700 /var/log/audit If the audit log directory does not have 0700 permissions, this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-269538`

### Rule: AlmaLinux OS 9 audit logs must be owned by the root group to prevent unauthorized read access.

**Rule ID:** `SV-269538r1050421_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit logs are owned by the "root" group. First determine if a group other than "root" has been assigned to the audit logs with the following command: $ grep log_group /etc/audit/auditd.conf log_group = root Then determine where the audit logs are stored with the following command: $ grep -w log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Then using the location of the audit log file, determine if the audit log is owned by the "root" group using the following command: $ stat -c "%G" /var/log/audit/audit.log root If the audit log is not owned by the "root" group, or log_group is not set to "root", this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-269539`

### Rule: AlmaLinux OS 9 audit logs must be owned by root to prevent unauthorized read access.

**Rule ID:** `SV-269539r1050422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit logs are owned by the "root" user. First determine where the audit logs are stored with the following command: $ grep -w log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Then using the location of the audit log file, determine if the audit log is owned by the "root" user using the following command: $ stat -c "%U" /var/log/audit/audit.log root If the audit log is not owned by the "root" user this is a finding.

## Group: SRG-OS-000057-GPOS-00027

**Group ID:** `V-269540`

### Rule: AlmaLinux OS 9 audit logs must have 0600 permissions to prevent unauthorized read access.

**Rule ID:** `SV-269540r1050423_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit operating system activity. Satisfies: SRG-OS-000057-GPOS-00027, SRG-OS-000059-GPOS-00029</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit log files have 0600 (u=rw-) permissions. First determine where the audit logs are stored with the following command: $ grep -w log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Then using the location of the audit log file, determine if the audit logs have 0600 permissions using the following command: $ stat -c "%U:%G %#a %n" /var/log/audit/* root:root 0600 /var/log/audit/audit.log If the audit log files do not have 0600 permissions, this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-269541`

### Rule: AlmaLinux OS 9 audit tools must be group-owned by root.

**Rule ID:** `SV-269541r1050424_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. AlmaLinux OS 9 systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools, and the corresponding rights the user enjoys, to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit tools are group owned by "root" with the following command: $ stat -c "%G %n" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/rsyslogd /sbin/augenrules root /sbin/auditctl root /sbin/aureport root /sbin/ausearch root /sbin/autrace root /sbin/auditd root /sbin/rsyslogd root /sbin/augenrules If any audit tools do not have a group owner of "root", this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-269542`

### Rule: AlmaLinux OS 9 audit tools must be owned by root.

**Rule ID:** `SV-269542r1050425_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. AlmaLinux OS 9 systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools, and the corresponding rights the user enjoys, to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000258-GPOS-00099</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit tools are owned by "root" with the following command: $ stat -c "%U %n" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/rsyslogd /sbin/augenrules root /sbin/auditctl root /sbin/aureport root /sbin/ausearch root /sbin/autrace root /sbin/auditd root /sbin/rsyslogd root /sbin/augenrules If any audit tools do not have an owner of "root", this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-269543`

### Rule: AlmaLinux OS 9 audit tools must have a mode of 0755 or less permissive.

**Rule ID:** `SV-269543r1050426_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. AlmaLinux OS 9 systems providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools, and the corresponding rights the user enjoys, to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000258-GPOS-00099</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit tools have a mode of "0755" or less with the following command: $ stat -c "%#a %n" /sbin/auditctl /sbin/aureport /sbin/ausearch /sbin/autrace /sbin/auditd /sbin/rsyslogd /sbin/augenrules 0755 /sbin/auditctl 0755 /sbin/aureport 0755 /sbin/ausearch 0750 /sbin/autrace 0755 /sbin/auditd 0755 /sbin/rsyslogd 0755 /sbin/augenrules If any of the audit tool files have a mode more permissive than "0755", this is a finding.

## Group: SRG-OS-000058-GPOS-00028

**Group ID:** `V-269544`

### Rule: AlmaLinux OS 9 audit system must protect logon UIDs from unauthorized change.

**Rule ID:** `SV-269544r1050427_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If modification of login user identifiers (UIDs) is not prevented, they can be changed by nonprivileged users and make auditing complicated or impossible.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit system prevents unauthorized changes to logon UIDs with the following command: $ grep immutable /etc/audit/audit.rules --loginuid-immutable If the "--loginuid-immutable" option is not returned in the "/etc/audit/audit.rules", or the line is commented out, this is a finding.

## Group: SRG-OS-000278-GPOS-00108

**Group ID:** `V-269545`

### Rule: AlmaLinux OS 9 must use cryptographic mechanisms to protect the integrity of audit tools.

**Rule ID:** `SV-269545r1050428_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting the integrity of the tools used for auditing purposes is a critical step toward ensuring the integrity of audit information. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Satisfies: SRG-OS-000278-GPOS-00108, SRG-OS-000257-GPOS-00098</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that AIDE is properly configured to use cryptographic mechanisms to protect the integrity of the audit tools with the following command: $ grep /usr/sbin/au /etc/aide.conf /usr/sbin/auditctl p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/auditd p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/ausearch p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/aureport p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/autrace p+i+n+u+g+s+b+acl+xattrs+sha512 /usr/sbin/augenrules p+i+n+u+g+s+b+acl+xattrs+sha512 If AIDE is not installed, ask the system administrator (SA) how file integrity checks are performed on the system. If any of the audit tools listed above do not have a corresponding line including "sha512", ask the SA to indicate what cryptographic mechanisms are being used to protect the integrity of the audit tools. If there is no evidence of integrity protection, this is a finding.

## Group: SRG-OS-000058-GPOS-00028

**Group ID:** `V-269546`

### Rule: AlmaLinux OS 9 audit system must protect auditing rules from unauthorized change.

**Rule ID:** `SV-269546r1050429_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized disclosure of audit records can reveal system and configuration data to attackers, thus compromising its confidentiality. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit AlmaLinux OS 9 system activity. In immutable mode, unauthorized users cannot execute changes to the audit system to potentially hide malicious activity and then put the audit rules back. A system reboot would be noticeable, and a system administrator could then investigate the unauthorized changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit system prevents unauthorized changes to the rules with the following command: $ grep -E '^-e 2' /etc/audit/audit.rules -e 2 If the audit system is not set to be immutable by adding the "-e 2" option to the end of "/etc/audit/audit.rules", this is a finding.

## Group: SRG-OS-000304-GPOS-00121

**Group ID:** `V-272485`

### Rule: AlmaLinux OS 9 must have the postfix package installed.

**Rule ID:** `SV-272485r1069405_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Postfix is a free, open-source mail transfer agent (MTA) that sends and receives emails. It is a server-side application that can be used to set up a local mail server, create a null-client mail relay, use a Postfix server as a destination for multiple domains, or choose an LDAP directory instead of files for lookups. Postfix supports protocols like LDAP, SMTP AUTH (SASL), and TLS. It uses the Simple Mail Transfer Protocol (SMTP) to transfer emails between servers. Satisfies: SRG-OS-000304-GPOS-00121, SRG-OS-000343-GPOS-00134, SRG-OS-000363-GPOS-00150, SRG-OS-000447-GPOS-00201</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 has the postfix package installed with the following command: $ dnf list --installed postfix Example output: postfix.x86_64 2:3.5.9-24.el9 @AppStream If the "postfix" package is not installed, this is a finding.

## Group: SRG-OS-000471-GPOS-00215

**Group ID:** `V-274874`

### Rule: AlmaLinux OS 9  must audit any script or executable called by cron as root or by any privileged user.

**Rule ID:** `SV-274874r1101856_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any script or executable called by cron as root or by any privileged user must be owned by that user and must have the permissions 755 or more restrictive and should have no extended rights that allow any nonprivileged user to modify the script or executable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that AlmaLinux OS 9 is configured to audit the execution of any system call made by cron as root or as any privileged user. $ sudo auditctl -l | grep /etc/cron.d -w /etc/cron.d -p wa -k cronjobs $ sudo auditctl -l | grep /var/spool/cron -w /var/spool/cron -p wa -k cronjobs If either of these commands do not return the expected output, or the lines are commented out, this is a finding.

