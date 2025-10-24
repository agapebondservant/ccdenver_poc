# STIG Benchmark: Canonical Ubuntu 18.04 LTS Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-219147`

### Rule: Ubuntu operating systems booted with a BIOS must require authentication upon booting into single-user and maintenance modes.

**Rule ID:** `SV-219147r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an encrypted root password is set. This is only applicable on systems that use a basic Input/Output System BIOS. Run the following command to verify the encrypted password is set: $ grep –i password /boot/grub/grub.cfg password_pbkdf2 root grub.pbkdf2.sha512.10000.MFU48934NJA87HF8NSD34493GDHF84NG If the root password entry does not begin with “password_pbkdf2”, this is a finding.

## Group: SRG-OS-000080-GPOS-00048

**Group ID:** `V-219148`

### Rule: Ubuntu operating systems booted with United Extensible Firmware Interface (UEFI) implemented must require authentication upon booting into single-user mode and maintenance.

**Rule ID:** `SV-219148r958472_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., web servers and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include: identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include: access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an encrypted root password is set. This is only applicable on Ubuntu operating systems that use UEFI. Run the following command to verify the encrypted password is set: $ grep -i password /boot/efi/EFI/ubuntu/grub.cfg password_pbkdf2 root grub.pbkdf2.sha512.10000.VeryLongString If the root password entry does not begin with “password_pbkdf2”, this is a finding.

## Group: SRG-OS-000254-GPOS-00095

**Group ID:** `V-219149`

### Rule: The Ubuntu operating system must initiate session audits at system startup.

**Rule ID:** `SV-219149r991555_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If auditing is enabled late in the startup process, the actions of some startup processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system enables auditing at system startup. Check that the auditing is enabled in grub with the following command: grep "^\s*linux" /boot/grub/grub.cfg linux /vmlinuz-4.15.0-55-generic root=/dev/mapper/ubuntu--vg-root ro quiet splash $vt_handoff audit=1 linux /vmlinuz-4.15.0-55-generic root=/dev/mapper/ubuntu--vg-root ro recovery nomodeset audit=1 If any linux lines do not contain "audit=1", this is a finding.

## Group: SRG-OS-000185-GPOS-00079

**Group ID:** `V-219150`

### Rule: Ubuntu operating systems handling data requiring data at rest protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest.

**Rule ID:** `SV-219150r958552_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information at rest refers to the state of information when it is located on a secondary storage device (e.g., disk drive and tape drive, when used for backups) within an operating system. This requirement addresses protection of user-generated data, as well as Ubuntu operating system-specific configuration data. Organizations may choose to employ different mechanisms to achieve confidentiality and integrity protections, as appropriate, in accordance with the security category and/or classification of the information. Satisfies: SRG-OS-000185-GPOS-00079, SRG-OS-000404-GPOS-00183, SRG-OS-000405-GPOS-00184</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If there is a documented and approved reason for not having data-at-rest encryption, this requirement is Not Applicable. Verify the Ubuntu operating system prevents unauthorized disclosure or modification of all information requiring at rest protection by using disk encryption. Determine the partition layout for the system with the following command: #sudo fdisk -l (..) Disk /dev/vda: 15 GiB, 16106127360 bytes, 31457280 sectors Units: sectors of 1 * 512 = 512 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disklabel type: gpt Disk identifier: 83298450-B4E3-4B19-A9E4-7DF147A5FEFB Device Start End Sectors Size Type /dev/vda1 2048 4095 2048 1M BIOS boot /dev/vda2 4096 2101247 2097152 1G Linux filesystem /dev/vda3 2101248 31455231 29353984 14G Linux filesystem (...) Verify that the system partitions are all encrypted with the following command: # more /etc/crypttab Every persistent disk partition present must have an entry in the file. If any partitions other than the boot partition or pseudo file systems (such as /proc or /sys) are not listed, this is a finding.

## Group: SRG-OS-000478-GPOS-00223

**Group ID:** `V-219151`

### Rule: The Ubuntu operating system must implement NIST FIPS-validated cryptography to protect classified information and for the following: to provision digital signatures, to generate cryptographic hashes, and to protect unclassified information requiring confidentiality and cryptographic protection in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.

**Rule ID:** `SV-219151r959006_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The operating system must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. Satisfies: SRG-OS-000478-GPOS-00223, SRG-OS-000396-GPOS-00176</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system is configured to run in FIPS mode. Check that the system is configured to run in FIPS mode with the following command: # grep -i 1 /proc/sys/crypto/fips_enabled 1 If a value of "1" is not returned, this is a finding.

## Group: SRG-OS-000343-GPOS-00134

**Group ID:** `V-219152`

### Rule: The Ubuntu operating system must immediately notify the SA and ISSO (at a minimum) when allocated audit record storage volume reaches 75% of the repository maximum audit record storage capacity.

**Rule ID:** `SV-219152r971542_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If security personnel are not notified immediately when storage volume reaches 75% utilization, they are unable to plan for audit record storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system notifies the System Administrator (SA) and Information System Security Officer (ISSO) (at a minimum) when allocated audit record storage volume reaches 75% of the repository maximum audit record storage capacity. Check that the Ubuntu operating system notifies the SA and ISSO (at a minimum) when allocated audit record storage volume reaches 75% of the repository maximum audit record storage capacity with the following command: # sudo grep ^space_left_action /etc/audit/auditd.conf space_left_action email # sudo grep ^space_left /etc/audit/auditd.conf space_left 250000 If the "space_left" parameter is missing, set to blanks or set to a value less than 25% of the space free in the allocated audit record storage, this is a finding. If the "space_left_action" parameter is missing or set to blanks, this is a finding. If the "space_left_action" is set to "syslog", the system logs the event, but does not generate a notification, so this is a finding. If the "space_left_action" is set to "exec", the system executes a designated script. If this script informs the SA of the event, this is not a finding. If the "space_left_action" is set to "email" check the value of the "action_mail_acct" parameter with the following command: # sudo grep action_mail_acct /etc/audit/auditd.conf action_mail_acct root@localhost The "action_mail_acct" parameter, if missing, defaults to "root". If the "action_mail_acct parameter" is not set to the e-mail address of the system administrator(s) and/or ISSO, this is a finding. Note: If the email address of the system administrator is on a remote system a mail package must be available.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-219153`

### Rule: The Ubuntu operating system audit event multiplexor must be configured to off-load audit logs onto a different system in real time, if the system is interconnected.

**Rule ID:** `SV-219153r959008_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit event multiplexor is configured to off-load audit records to a different system or storage media from the system being audited. Check that audisp-remote plugin is installed: # sudo dpkg -s audispd-plugins If status is "not installed", this is a finding. Check that the records are being off-loaded to a remote server with the following command: # sudo grep -i active /etc/audisp/plugins.d/au-remote.conf active = yes If "active" is not set to "yes", or the line is commented out, this is a finding. Check that audisp-remote plugin is configured to send audit logs to a different system: # sudo grep -i ^remote_server /etc/audisp/audisp-remote.conf remote_server = 192.168.122.126 If the remote_server parameter is not set or is set with a local address, or is set with invalid address, this is a finding.

## Group: SRG-OS-000479-GPOS-00224

**Group ID:** `V-219154`

### Rule: The Ubuntu operating system must have a crontab script running weekly to off-load audit events of standalone systems.

**Rule ID:** `SV-219154r959008_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there is a script which off-loads audit data and if that script runs weekly. Check if there is a script in the /etc/cron.weekly directory which off-loads audit data: # sudo ls /etc/cron.weekly audit-offload Check if the script inside the file does offloading of audit logs to an external media. If the script file does not exist or if the script file doesn't offload audit logs, this is a finding.

## Group: SRG-OS-000366-GPOS-00153

**Group ID:** `V-219155`

### Rule: Advance package Tool (APT) must be configured to prevent the installation of patches, service packs, device drivers, or Ubuntu operating system components without verification they have been digitally signed using a certificate that is recognized and approved by the organization.

**Rule ID:** `SV-219155r982212_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the Ubuntu operating system. This requirement ensures the software has not been tampered with and that it has been provided by a trusted vendor. Accordingly, patches, service packs, device drivers, or Ubuntu operating system components must be signed with a certificate recognized and approved by the organization. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and that it has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. The Ubuntu operating system should not have to verify the software again. This requirement does not mandate DoD certificates for this purpose; however, the certificate used to verify the software must be from an approved CA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Advance package Tool (APT) is configured to prevent the installation of patches, service packs, device drivers, or Ubuntu operating system components without verification they have been digitally signed using a certificate that is recognized and approved by the organization. Check that the "AllowUnauthenticated" variable is not set at all or set to "false" with the following command: # grep AllowUnauthenticated /etc/apt/apt.conf.d/* /etc/apt/apt.conf.d/01-vendor-Ubuntu:APT::Get::AllowUnauthenticated "false"; If any of the files returned from the command with "AllowUnauthenticated" set to "true", this is a finding.

## Group: SRG-OS-000437-GPOS-00194

**Group ID:** `V-219156`

### Rule: The Ubuntu operating system must be configured so that Advance package Tool (APT) removes all software components after updated versions have been installed.

**Rule ID:** `SV-219156r958936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Previous versions of software components that are not removed from the information system after updates have been installed may be exploited by adversaries. Some information technology products may remove older versions of software automatically from the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Advance package Tool (APT) is configured to remove all software components after updated versions have been installed. Check that APT is configured to remove all software components after updating with the following command: # grep -i remove-unused /etc/apt/apt.conf.d/50unattended-upgrades Unattended-Upgrade::Remove-Unused-Dependencies "true"; Unattended-Upgrade::Remove-Unused-Kernel-Packages "true"; If the "::Remove-Unused-Dependencies" and "::Remove-Unused-Kernel-Packages" parameters are not set to "true", or are missing, or are commented out, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-219157`

### Rule: The Ubuntu operating system must not have the Network Information Service (NIS) package installed.

**Rule ID:** `SV-219157r958478_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Removing the Network Information Service (NIS) package decreases the risk of the accidental (or intentional) activation of NIS or NIS+ services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Network Information Service (NIS) package is not installed on the Ubuntu operating system. Check to see if the NIS package is installed with the following command: # dpkg -l | grep nis If the NIS package is installed, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-219158`

### Rule: The Ubuntu operating system must not have the rsh-server package installed.

**Rule ID:** `SV-219158r958478_rule`
**Severity:** high

**Description:**
<VulnDiscussion>It is detrimental for Ubuntu operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Ubuntu operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). The rsh-server service provides an unencrypted remote access service that does not provide for the confidentiality and integrity of user passwords or the remote session and has very weak authentication. If a privileged user were to log on using this service, the privileged user password could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check to see if the rsh-server package is installed with the following command: # dpkg -l | grep rsh-server If the rsh-server package is installed, this is a finding.

## Group: SRG-OS-000191-GPOS-00080

**Group ID:** `V-219159`

### Rule: The Ubuntu operating system must deploy Endpoint Security for Linux Threat Prevention (ENSLTP).

**Rule ID:** `SV-219159r982191_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of automated mechanisms to scan for security flaws on a continuous and/or periodic basis, the operating system or other system components may remain vulnerable to the exploits presented by undetected software flaws. To support this requirement, the Ubuntu operating system may have an integrated solution incorporating continuous scanning using HBSS and periodic scanning using other tools, as specified in the requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that the "mcafeetp" package has been installed: # dpkg -l | grep -i mcafeetp If the "mcafeetp" package is not installed, this is a finding. Check that the daemon is running: # /opt/McAfee/ens/tp/init/mfetpd-control.sh status If the daemon is not running, this is a finding.

## Group: SRG-OS-000269-GPOS-00103

**Group ID:** `V-219160`

### Rule: The Ubuntu operating system must be configured to preserve log records from failure events.

**Rule ID:** `SV-219160r991562_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known state can address safety or security in accordance with the mission/business needs of the organization. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. Preserving operating system state information helps to facilitate operating system restart and return to the operational mode of the organization with least disruption to mission/business processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the log service is configured to collect system failure events. Check that the log service is installed properly with the following command: # dpkg -l | grep rsyslog ii rsyslog 8.32.0-1ubuntu4 amd64 reliable system and kernel logging daemon If the "rsyslog" package is not installed, this is a finding. Check that the log service is enabled with the following command: # sudo systemctl is-enabled rsyslog enabled If the command above returns "disabled", this is a finding. Check that the log service is properly running and active on the system with the following command: # systemctl is-active rsyslog active If the command above returns "inactive", this is a finding.

## Group: SRG-OS-000297-GPOS-00115

**Group ID:** `V-219161`

### Rule: The Ubuntu operating system must have an application firewall installed in order to control remote access methods.

**Rule ID:** `SV-219161r958672_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Ubuntu operating system functionality (e.g., RDP) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Uncomplicated Firewall is installed. Check that the Uncomplicated Firewall is installed with the following command: # dpkg -l | grep ufw ii ufw 0.35-0Ubuntu2 If the "ufw" package is not installed, ask the System Administrator is another application firewall is installed. If no application firewall is installed this is a finding.

## Group: SRG-OS-000342-GPOS-00133

**Group ID:** `V-219162`

### Rule: The Ubuntu operating system audit event multiplexor must be configured to off-load audit logs onto a different system or storage media from the system being audited.

**Rule ID:** `SV-219162r958754_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit event multiplexor is configured to off-load audit records to a different system or storage media from the system being audited. Check that audisp-remote plugin is installed: # sudo dpkg -s audispd-plugins If status is "not installed", verify that another method to off-load audit logs has been implemented. Check that the records are being off-loaded to a remote server with the following command: # sudo grep -i active /etc/audisp/plugins.d/au-remote.conf active = yes If "active" is not set to "yes", or the line is commented out, ask the System Administrator to indicate how the audit logs are off-loaded to a different system or storage media. If there is no evidence that the system is configured to off-load audit logs to a different system or storage media, this is a finding.

## Group: SRG-OS-000383-GPOS-00166

**Group ID:** `V-219163`

### Rule: The Ubuntu operating system must be configured such that Pluggable Authentication Module (PAM) prohibits the use of cached authentications after one day.

**Rule ID:** `SV-219163r958828_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If cached authentication information is out-of-date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If smart card authentication is not being used on the system this item is Not Applicable. Verify that Pluggable Authentication Module (PAM) prohibits the use of cached authentications after one day. Check that PAM prohibits the use of cached authentications after one day with the following command: # sudo grep offline_credentials_expiration /etc/sssd/sssd.conf /etc/sssd/conf.d/*.conf offline_credentials_expiration = 1 If "offline_credentials_expiration" is not set to a value of "1", in /etc/sssd/sssd.conf or in a file with a name ending in .conf in the /etc/sssd/conf.d/ directory, this is a finding.

## Group: SRG-OS-000480-GPOS-00226

**Group ID:** `V-219164`

### Rule: The Ubuntu operating system must enforce a delay of at least 4 seconds between logon prompts following a failed logon attempt.

**Rule ID:** `SV-219164r991588_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Limiting the number of logon attempts over a certain time interval reduces the chances that an unauthorized user may gain access to an account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system enforces a delay of at least 4 seconds between logon prompts following a failed logon attempt. Check that the Ubuntu operating system enforces a delay of at least 4 seconds between logon prompts with the following command: # grep pam_faildelay /etc/pam.d/common-auth auth required pam_faildelay.so delay=4000000 If the line is not present, or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-219165`

### Rule: The Ubuntu operating system must display the date and time of the last successful account logon upon logon.

**Rule ID:** `SV-219165r991589_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Configuring the Ubuntu operating system to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed in hardware, software, or firmware components of the system that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the system, including the parameters required to satisfy other security control requirements. Security-related parameters include, for example: registry settings; account, file, directory permission settings; and settings for functions, ports, protocols, services, and remote connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify users are provided with feedback on when account accesses last occurred. Check that "pam_lastlog" is used and not silent with the following command: # grep pam_lastlog /etc/pam.d/login session required pam_lastlog.so showfailed If "pam_lastlog" is missing from "/etc/pam.d/login" file, is not "required", or the "silent" option is present, this is a finding.

## Group: SRG-OS-000021-GPOS-00005

**Group ID:** `V-219166`

### Rule: The Ubuntu operating system must be configured so that three consecutive invalid logon attempts by a user automatically locks the account until released by an administrator.

**Rule ID:** `SV-219166r958388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-force attacks, is reduced. Limits are imposed by locking the account. Satisfies: SRG-OS-000329-GPOS-00128</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system utilizes the "pam_faillock" module with the following command: $ grep faillock /etc/pam.d/common-auth auth [default=die] pam_faillock.so authfail auth sufficient pam_faillock.so authsucc If the pam_faillock.so module is not present in the "/etc/pam.d/common-auth" file, this is a finding. Verify the pam_faillock module is configured to use the following options: $ sudo egrep 'silent|audit|deny|fail_interval| unlock_time' /etc/security/faillock.conf audit silent deny = 3 fail_interval = 900 unlock_time = 0 If the "silent" keyword is missing or commented out, this is a finding. If the "audit" keyword is missing or commented out, this is a finding. If the "deny" keyword is missing, commented out, or set to a value greater than 3, this is a finding. If the "fail_interval" keyword is missing, commented out, or set to a value greater than 900, this is a finding. If the "unlock_time" keyword is missing, commented out, or is not set to 0, this is a finding.

## Group: SRG-OS-000024-GPOS-00007

**Group ID:** `V-219167`

### Rule: The Ubuntu operating system must display the Standard Mandatory DoD Notice and Consent Banner before granting local access to the system via a graphical user logon.

**Rule ID:** `SV-219167r958392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The banner must be acknowledged by the user prior to allowing the user access to the operating system. This provides assurance that the user has seen the message and accepted the conditions for access. If the consent banner is not acknowledged by the user, DoD will not be in compliance with system use notifications required by law. To establish acceptance of the application usage policy, a click-through banner at system logon is required. The system must prevent further activity until the user executes a positive action to manifest agreement by clicking on a box indicating "OK".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system displays the Standard Mandatory DoD Notice and Consent Banner before granting access to the operating system via a graphical user logon. Note: If the system does not have Graphical User Interface installed, this requirement is Not Applicable. Check that the operating system displays the exact approved Standard Mandatory DoD Notice and Consent Banner text with the command: # grep banner-message-enable /etc/gdm3/greeter.dconf-defaults banner-message-enable=true If the line is commented out or set to "false", this is a finding. # grep banner-message-text /etc/gdm3/greeter.dconf-defaults banner-message-text="You are accessing a U.S. Government \(USG\) Information System \(IS\) that is provided for USG-authorized use only.\s+By using this IS \(which includes any device attached to this IS\), you consent to the following conditions:\s+-The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct \(PM\), law enforcement \(LE\), and counterintelligence \(CI\) investigations.\s+-At any time, the USG may inspect and seize data stored on this IS.\s+-Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose.\s+-This IS includes security measures \(e.g., authentication and access controls\) to protect USG interests--not for your personal benefit or privacy.\s+-Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the banner-message-text is missing, commented out, or the text does not match the Standard Mandatory DoD Notice and Consent Banner exactly, this is a finding.

## Group: SRG-OS-000109-GPOS-00056

**Group ID:** `V-219168`

### Rule: The Ubuntu operating system must prevent direct login into the root account.

**Rule ID:** `SV-219168r982205_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure individual accountability and prevent unauthorized access, organizational users must be individually identified and authenticated. A group authenticator is a generic account used by multiple individuals. Use of a group authenticator alone does not uniquely identify individual users. Examples of the group authenticator is the UNIX OS "root" user account, the Windows "Administrator" account, the "sa" account, or a "helpdesk" account. For example, the UNIX and Windows operating systems offer a 'switch user' capability allowing users to authenticate with their individual credentials and, when needed, 'switch' to the administrator role. This method provides for unique individual authentication prior to using a group authenticator. Users (and any processes acting on behalf of users) need to be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization, which outlines specific user actions that can be performed on the operating system without identification or authentication. Requiring individuals to be authenticated with an individual authenticator prior to using a group authenticator allows for traceability of actions, as well as adding an additional level of protection of the actions that can be taken with group account knowledge.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system prevents direct logins to the root account. Check that the Ubuntu operating system prevents direct logins to the root account with the following command: # sudo passwd -S root root L 11/11/2017 0 99999 7 -1 If the output does not contain "L" in the second field to indicate the account is locked, this is a finding.

## Group: SRG-OS-000134-GPOS-00068

**Group ID:** `V-219169`

### Rule: The Ubuntu operating system must be configured so that only users who need access to security functions are part of the sudo group.

**Rule ID:** `SV-219169r958518_rule`
**Severity:** high

**Description:**
<VulnDiscussion>An isolation boundary provides access control and protects the integrity of the hardware, software, and firmware that perform security functions. Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Operating systems implement code separation (i.e., separation of security functions from nonsecurity functions) in a number of ways, including through the provision of security kernels via processor rings or processor modes. For non-kernel code, security function isolation is often achieved through file system protections that serve to protect the code on disk and address space protections that protect executing code. Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Implementation may include isolation of memory space and libraries. The Ubuntu operating system restricts access to security functions through the use of access control mechanisms and by implementing least privilege capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the sudo group has only members who should have access to security functions. # grep sudo /etc/group sudo:x:27:foo If the sudo group contains users not needing access to security functions, this is a finding.

## Group: SRG-OS-000228-GPOS-00088

**Group ID:** `V-219170`

### Rule: The Ubuntu operating system must display the Standard Mandatory DoD Notice and Consent Banner before granting any publically accessible connection to the system.

**Rule ID:** `SV-219170r958586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the Ubuntu operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with applicable DoD policy: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Satisfies: SRG-OS-000228-GPOS-00088, SRG-OS-000023-GPOS-00006</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system displays the Standard Mandatory DoD Notice and Consent Banner before granting access to the Ubuntu operating system via a ssh logon. Check that the Ubuntu operating system displays the Standard Mandatory DoD Notice and Consent Banner before granting access to the Ubuntu operating system via a ssh logon with the following command: # grep -i banner /etc/ssh/sshd_config Banner /etc/issue The command will return the banner option along with the name of the file that contains the ssh banner. If the line is commented out, this is a finding. Check the specified banner file to check that it matches the Standard Mandatory DoD Notice and Consent Banner exactly: # cat /etc/issue “You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details.” If the banner text does not match the Standard Mandatory DoD Notice and Consent Banner exactly, this is a finding.

## Group: SRG-OS-000069-GPOS-00037

**Group ID:** `V-219172`

### Rule: The Ubuntu operating system must enforce password complexity by requiring that at least one upper-case character be used.

**Rule ID:** `SV-219172r982195_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system enforces password complexity by requiring that at least one upper-case character be used. Determine if the field "ucredit" is set in the "/etc/security/pwquality.conf" file with the following command: # grep -i "ucredit" /etc/security/pwquality.conf ucredit=-1 If the "ucredit" parameter is greater than "-1", or is commented out, this is a finding.

## Group: SRG-OS-000070-GPOS-00038

**Group ID:** `V-219173`

### Rule: The Ubuntu operating system must enforce password complexity by requiring that at least one lower-case character be used.

**Rule ID:** `SV-219173r982196_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system enforces password complexity by requiring that at least one lower-case character be used. Determine if the field "lcredit" is set in the "/etc/security/pwquality.conf" file with the following command: # grep -i "lcredit" /etc/security/pwquality.conf lcredit=-1 If the "lcredit" parameter is greater than "-1", or is commented out, this is a finding.

## Group: SRG-OS-000071-GPOS-00039

**Group ID:** `V-219174`

### Rule: The Ubuntu operating system must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-219174r982197_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system enforces password complexity by requiring that at least one numeric character be used. Determine if the field "dcredit" is set in the "/etc/security/pwquality.conf" file with the following command: # grep -i "dcredit" /etc/security/pwquality.conf dcredit=-1 If the "dcredit" parameter is greater than "-1", or is commented out, this is a finding.

## Group: SRG-OS-000072-GPOS-00040

**Group ID:** `V-219175`

### Rule: The Ubuntu operating system must require the change of at least 8 characters when passwords are changed.

**Rule ID:** `SV-219175r982198_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If the Ubuntu operating system allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. If the password length is an odd number then number of changed characters must be rounded up. For example, a password length of 15 characters must require the change of at least 8 characters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system requires the change of at least 8 characters when passwords are changed. Determine if the field "difok" is set in the "/etc/security/pwquality.conf" file with the following command: # grep -i "difok" /etc/security/pwquality.conf difok=8 If the "difok" parameter is less than "8", or is commented out, this is a finding.

## Group: SRG-OS-000073-GPOS-00041

**Group ID:** `V-219176`

### Rule: The Ubuntu operating system must encrypt all stored passwords with a FIPS 140-2 approved cryptographic hashing algorithm.

**Rule ID:** `SV-219176r982199_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the shadow password suite configuration is set to encrypt password with a FIPS 140-2 approved cryptographic hashing algorithm. Check the hashing algorithm that is being used to hash passwords with the following command: # cat /etc/login.defs | grep -i crypt ENCRYPT_METHOD SHA512 If "ENCRYPT_METHOD" does not equal SHA512 or greater, this is a finding.

## Group: SRG-OS-000074-GPOS-00042

**Group ID:** `V-219177`

### Rule: The Ubuntu operating system must not have the telnet package installed.

**Rule ID:** `SV-219177r987796_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the telnet package is not installed on the Ubuntu operating system. Check that the telnet daemon is not installed on the Ubuntu operating system by running the following command: # dpkg -l | grep telnetd If the package is installed, this is a finding.

## Group: SRG-OS-000075-GPOS-00043

**Group ID:** `V-219178`

### Rule: The Ubuntu operating system must enforce 24 hours/1 day as the minimum password lifetime. Passwords for new users must have a 24 hours/1 day minimum password lifetime restriction.

**Rule ID:** `SV-219178r982188_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system enforces a 24 hours/1 day minimum password lifetime for new user accounts by running the following command: # grep -i pass_min_days /etc/login.defs PASS_MIN_DAYS 1 If the "PASS_MIN_DAYS" parameter value is less than 1, or commented out, this is a finding.

## Group: SRG-OS-000076-GPOS-00044

**Group ID:** `V-219179`

### Rule: The Ubuntu operating system must enforce a 60-day maximum password lifetime restriction. Passwords for new users must have a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-219179r982200_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If the operating system does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the operating system passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system enforces a 60-day maximum password lifetime for new user accounts by running the following command: # grep -i pass_max_days /etc/login.defs PASS_MAX_DAYS 60 If the "PASS_MAX_DAYS" parameter value is less than 60, or commented out, this is a finding.

## Group: SRG-OS-000077-GPOS-00045

**Group ID:** `V-219180`

### Rule: The Ubuntu operating system must prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-219180r982201_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system prevents passwords from being reused for a minimum of five generations by running the following command: # grep -i remember /etc/pam.d/common-password password [success=1 default=ignore] pam_unix.so sha512 shadow remember=5 rounds=5000 If the "remember" parameter value is not greater than or equal to 5, commented out, or not set at all this is a finding.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-219181`

### Rule: The Ubuntu operating system must enforce a minimum 15-character password length.

**Rule ID:** `SV-219181r982202_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if the pwquality configuration file enforces a minimum 15-character password length, by running the following command: # grep -i minlen /etc/security/pwquality.conf minlen=15 If "minlen" parameter value is not 15 or higher, or is commented out, this is a finding.

## Group: SRG-OS-000120-GPOS-00061

**Group ID:** `V-219182`

### Rule: The Ubuntu operating system must employ a FIPS 140-2 approved cryptographic hashing algorithms for all created and stored passwords.

**Rule ID:** `SV-219182r971535_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Ubuntu operating system must use a FIPS-compliant hashing algorithm to securely store the password. The FIPS-compliant hashing algorithm parameters must be selected in order to harden the system against offline attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that encrypted passwords stored in /etc/shadow use a strong cryptographic hash. Check that pam_unix.so auth is configured to use sha512 with the following command: # grep password /etc/pam.d/common-password | grep pam_unix password [success=1 default=ignore] pam_unix.so obscure sha512 If "sha512" is not an option of the output, or is commented out, this is a finding. Check that ENCRYPT_METHOD is set to sha512 in /etc/login.defs: # grep -i ENCRYPT_METHOD /etc/login.defs ENCRYPT_METHOD SHA512 If the output does not contain "sha512", or it is commented out, this is a finding.

## Group: SRG-OS-000380-GPOS-00165

**Group ID:** `V-219183`

### Rule: The Ubuntu operating system must allow the use of a temporary password for system logons with an immediate change to a permanent password.

**Rule ID:** `SV-219183r982193_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without providing this capability, an account may be created without a password. Non-repudiation cannot be guaranteed once an account is created if a user is not forced to change the temporary password upon initial logon. Temporary passwords are typically used to allow access when new accounts are created or passwords are changed. It is common practice for administrators to create temporary passwords for user accounts which allow the users to log on, yet force them to change the password once they have successfully authenticated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify a policy exists that ensures when a user account is created, it is created using a method that forces a user to change their password upon their next login. If a policy does not exist, this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-219184`

### Rule: The Ubuntu operating system must prevent the use of dictionary words for passwords.

**Rule ID:** `SV-219184r991587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Ubuntu operating system allows the user to select passwords based on dictionary words, then this increases the chances of password compromise by increasing the opportunity for successful guesses and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system uses the cracklib library to prevent the use of dictionary words with the following command: # grep dictcheck /etc/security/pwquality.conf dictcheck=1 If the "dictcheck" parameter is not set to "1", or is commented out, this is a finding.

## Group: SRG-OS-000373-GPOS-00156

**Group ID:** `V-219185`

### Rule: The Ubuntu operating system must require users to re-authenticate for privilege escalation and changing roles.

**Rule ID:** `SV-219185r987879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without re-authentication, users may access resources or perform tasks for which they do not have authorization. When the Ubuntu operating system provides the capability to escalate a functional capability or change security roles, it is critical the user re-authenticate. Satisfies: SRG-OS-000373-GPOS-00156, SRG-OS-000373-GPOS-00157</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "/etc/sudoers" has no occurrences of "NOPASSWD" or "!authenticate". Check that the "/etc/sudoers" file has no occurrences of "NOPASSWD" or "!authenticate" by running the following command: # sudo egrep -i '(nopasswd|!authenticate)' /etc/sudoers /etc/sudoers.d/* If any occurrences of "NOPASSWD" or "!authenticate" return from the command, this is a finding.

## Group: SRG-OS-000480-GPOS-00225

**Group ID:** `V-219186`

### Rule: The Ubuntu Operating system must be configured so that when passwords are changed or new passwords are established, pwquality must be used.

**Rule ID:** `SV-219186r991587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. "pwquality" enforces complex password construction configuration and has the ability to limit brute-force attacks on the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system has the libpam-pwquality package installed, by running the following command: # dpkg -l libpam-pwquality ii libpam-pwquality:amd64 1.4.0-2 amd64 PAM module to check password strength If "libpam-pwquality" is not installed, this is a finding. Verify the operating system uses "pwquality" to enforce the password complexity rules. Verify the pwquality module is being enforced by the Ubuntu Operating System, by running the following command: # grep -i enforcing /etc/security/pwquality.conf enforcing = 1 If the value of "enforcing" is not 1 or the line is commented out, this is a finding. Check for the use of "pwquality" with the following command: # sudo cat /etc/pam.d/common-password | grep requisite | grep pam_pwquality password requisite pam_pwquality.so retry=3 enforce_for_root If no output is returned or the line is commented out, this is a finding. If the value of "retry" is set to "0" or greater than "3", this is a finding. If "enforce_for_root" is missing from the configuration line, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-219187`

### Rule: The Ubuntu operating system must set a sticky bit on all public directories to prevent unauthorized and unintended information transferred via shared system resources.

**Rule ID:** `SV-219187r958524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection. This requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DoD or other government agencies. There may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all public (world writeable) directories have the public sticky bit set. Find world-writable directories that lack the sticky bit by running the following command: # sudo find / -type d -perm -002 ! -perm -1000 If any world-writable directories are found missing the sticky bit, this is a finding.

## Group: SRG-OS-000205-GPOS-00083

**Group ID:** `V-219188`

### Rule: The Ubuntu operating system must generate error messages that provide information necessary for corrective actions without revealing information that could be exploited by adversaries.

**Rule ID:** `SV-219188r958564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any operating system providing too much information in error messages risks compromising the data and security of the structure, and content of error messages needs to be carefully considered by the organization. Organizations carefully consider the structure/content of error messages. The extent to which information systems are able to identify and handle error conditions is guided by organizational policy and operational requirements. Information that could be exploited by adversaries includes, for example, erroneous logon attempts with passwords entered by mistake as the username, mission/business information that can be derived from (if not stated explicitly by) information recorded, and personal information, such as account numbers, social security numbers, and credit card numbers. The /var/log/btmp, /var/log/wtmp, and /var/log/lastlog files have group write and global read permissions to allow for the lastlog function to perform. Limiting the permissions beyond this configuration will result in the failure of functions that rely on the lastlog database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system has all system log files under the /var/log directory with a permission set to "640", by using the following command: Note: The btmp, wtmp, and lastlog files are excluded. Refer to the Discussion for details. $ sudo find /var/log -perm /137 ! -name '*[bw]tmp' ! -name '*lastlog' -type f -exec stat -c "%n %a" {} \; If the command displays any output, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-219189`

### Rule: The Ubuntu operating system must configure the /var/log directory to be group-owned by syslog.

**Rule ID:** `SV-219189r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system configures the /var/log directory to be group-owned by syslog. Check that the /var/log directory is group owned by syslog with the following command: # sudo stat -c "%n %G" /var/log /var/log syslog If the /var/log directory is not group-owned by syslog, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-219190`

### Rule: The Ubuntu operating system must configure the /var/log directory to be owned by root.

**Rule ID:** `SV-219190r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system configures the /var/log directory to be owned by root. Check that the /var/log directory is owned by root with the following command: # sudo stat -c "%n %U" /var/log /var/log root If the /var/log directory is not owned by root, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-219191`

### Rule: The Ubuntu operating system must configure the /var/log directory to have mode 0755 or less permissive.

**Rule ID:** `SV-219191r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, personally identifiable information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system configures the /var/log directory with a mode of "755" or less permissive. Check the mode of the /var/log directory with the following command: Note: If rsyslog is active and enabled on the operating system, this requirement is not applicable. $ stat -c "%n %a" /var/log /var/log 755 If a value of "755" or less permissive is not returned, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-219192`

### Rule: The Ubuntu operating system must configure the /var/log/syslog file to be group-owned by adm.

**Rule ID:** `SV-219192r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system configures the /var/log/syslog file to be group-owned by adm. Check that the /var/log/syslog file is group-owned by adm with the following command: # sudo stat -c "%n %G" /var/log/syslog /var/log/syslog adm If the /var/log/syslog file is not group-owned by adm, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-219193`

### Rule: The Ubuntu operating system must configure /var/log/syslog file to be owned by syslog.

**Rule ID:** `SV-219193r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system configures the /var/log/syslog file to be owned by syslog. Check that the /var/log/syslog file is owned by syslog with the following command: # sudo stat -c "%n %U" /var/log/syslog /var/log/syslog syslog If the /var/log/syslog file is not owned by syslog, this is a finding.

## Group: SRG-OS-000206-GPOS-00084

**Group ID:** `V-219194`

### Rule: The Ubuntu operating system must configure /var/log/syslog file with mode 0640 or less permissive.

**Rule ID:** `SV-219194r958566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the operating system or platform. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system configures the /var/log/syslog file with mode 0640 or less permissive. Check the /var/log/syslog permissions by running the following command: # stat -c "%n %a" /var/log/syslog /var/log/syslog 640 If a value of "640" or less permissive is not returned, this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-219195`

### Rule: The Ubuntu operating system must configure audit tools with a mode of 0755 or less permissive.

**Rule ID:** `SV-219195r991557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. The Ubuntu operating system providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. Satisfies: SRG-OS-000256-GPOS-00097, SRG-OS-000257-GPOS-00098, SRG-OS-000258-GPOS-00099</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit tools are protected from unauthorized access, deletion, or modification by checking the permissive mode. For each audit tool, /sbin/auditctl, /sbin/aureport, /sbin/ausearch, /sbin/autrace, /sbin/auditd, /sbin/audispd, /sbin/augenrules Check the permissions by running the following command: # stat -c "%n %a" /sbin/auditctl 755 /sbin/auditctl If any of the audit tools have a mode more permissive than 0755, this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-219196`

### Rule: The Ubuntu operating system must configure audit tools to be owned by root.

**Rule ID:** `SV-219196r991557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. The Ubuntu operating system providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system configures the audit tools to be owned by root to prevent any unauthorized access, deletion, or modification. For each audit tool, /sbin/auditctl, /sbin/aureport, /sbin/ausearch, /sbin/autrace, /sbin/auditd, /sbin/audispd, /sbin/augenrules Check the ownership by running the following command: # stat -c "%n %U" /sbin/auditctl /sbin/auditctl root If any of the audit tools are not owned by root, this is a finding.

## Group: SRG-OS-000256-GPOS-00097

**Group ID:** `V-219197`

### Rule: The Ubuntu operating system must configure the audit tools to be group-owned by root.

**Rule ID:** `SV-219197r991557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit information also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit information. The Ubuntu operating system providing tools to interface with audit information will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system configures the audit tools to be group-owned by root to prevent any unauthorized access, deletion, or modification. For each audit tools, /sbin/auditctl, /sbin/aureport, /sbin/ausearch, /sbin/autrace, /sbin/auditd, /sbin/audispd, /sbin/augenrules Check the group-owner of each audit tool by running the following commands: stat -c "%n %G" /sbin/auditctl /sbin/auditctl root If any of the audit tools are not group-owned by root, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-219198`

### Rule: The Ubuntu operating system library files must have mode 0755 or less permissive.

**Rule ID:** `SV-219198r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system-wide shared library files contained in the directories "/lib", "/lib64" and "/usr/lib" have mode 0755 or less permissive. Check that the system-wide shared library files have mode 0755 or less permissive with the following command: $ sudo find /lib /lib64 /usr/lib -perm /022 -type f -exec stat -c "%n %a" '{}' \; /usr/lib64/pkcs11-spy.so If any library files are found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-219199`

### Rule: The Ubuntu operating system library directories must have mode 0755 or less permissive.

**Rule ID:** `SV-219199r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Ubuntu operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to Ubuntu operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system-wide shared library directories "/lib", "/lib64" and "/usr/lib have mode 0755 or less permissive. Check that the system-wide shared library directories have mode 0755 or less permissive with the following command: # sudo find /lib /lib64 /usr/lib -perm /022 -type d -exec stat -c "%n %a" '{}' \; If any of the aforementioned directories are found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-219200`

### Rule: The Ubuntu operating system library files must be owned by root.

**Rule ID:** `SV-219200r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Ubuntu operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to Ubuntu operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system-wide shared library files contained in the directories "/lib", "/lib64" and "/usr/lib" are owned by root. Check that the system-wide shared library files are owned by root with the following command: # sudo find /lib /usr/lib /lib64 ! -user root -type f -exec stat -c "%n %U" '{}' \; If any system wide library file is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-219201`

### Rule: The Ubuntu operating system library directories must be owned by root.

**Rule ID:** `SV-219201r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Ubuntu operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to Ubuntu operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system-wide shared library directories "/lib", "/lib64" and "/usr/lib" are owned by root. Check that the system-wide shared library directories are owned by root with the following command: # sudo find /lib /usr/lib /lib64 ! -user root -type d -exec stat -c "%n %U" '{}' \; If any system wide library directory is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-219202`

### Rule: The Ubuntu operating system library files must be group-owned by root.

**Rule ID:** `SV-219202r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Ubuntu operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to Ubuntu operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system-wide library files contained in the directories "/lib", "/lib64" and "/usr/lib" are group-owned by root. Check that the system-wide library files are group-owned by root with the following command: $ sudo find /lib /usr/lib /lib64 ! -group root -type f -exec stat -c "%n %G" '{}' \; If any system wide shared library file is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-219203`

### Rule: The Ubuntu operating system library directories must be group-owned by root.

**Rule ID:** `SV-219203r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Ubuntu operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to Ubuntu operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system-wide library directories "/lib", "/lib64" and "/usr/lib" are group-owned by root. Check that the system-wide library directories are group-owned by root with the following command: # sudo find /lib /usr/lib /lib64 ! -group root -type d -exec stat -c "%n %G" '{}' \; If any system wide shared library directory is returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-219204`

### Rule: The Ubuntu operating system must have system commands set to a mode of 0755 or less permissive.

**Rule ID:** `SV-219204r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Ubuntu operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to Ubuntu operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands contained in the following directories have mode 0755 or less permissive: /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin Check that the system command files have mode 0755 or less permissive with the following command: # find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin -perm /022 -type f -exec stat -c "%n %a" '{}' \; If any files are found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-219205`

### Rule: The Ubuntu operating system must have directories that contain system commands set to a mode of 0755 or less permissive.

**Rule ID:** `SV-219205r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Ubuntu operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to Ubuntu operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands directories have mode 0755 or less permissive: /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin Check that the system command directories have mode 0755 or less permissive with the following command: # find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin -perm /022 -type d -exec stat -c "%n %a" '{}' \; If any directories are found to be group-writable or world-writable, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-219206`

### Rule: The Ubuntu operating system must have system commands owned by root.

**Rule ID:** `SV-219206r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Ubuntu operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to Ubuntu operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands contained in the following directories are owned by root: /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin Use the following command for the check: # sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -user root -type f -exec stat -c "%n %U" '{}' \; If any system commands are returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-219207`

### Rule: The Ubuntu operating system must have directories that contain system commands owned by root.

**Rule ID:** `SV-219207r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Ubuntu operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to Ubuntu operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands directories are owned by root: /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin Use the following command for the check: # sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -user root -type d -exec stat -c "%n %U" '{}' \; If any system commands directories are returned, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-219208`

### Rule: The Ubuntu operating system must have system commands group-owned by root or a system account.

**Rule ID:** `SV-219208r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Ubuntu operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to Ubuntu operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands contained in the following directories are group-owned by root or a system account: /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin Run the check with the following command: $ sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -group root -type f -exec stat -c "%n %G" '{}' \; If any system commands are returned that are not Set Group ID up on execution (SGID) files and group-owned by a required system account, this is a finding.

## Group: SRG-OS-000259-GPOS-00100

**Group ID:** `V-219209`

### Rule: The Ubuntu operating system must have directories that contain system commands group-owned by root.

**Rule ID:** `SV-219209r991560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Ubuntu operating system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement applies to Ubuntu operating systems with software libraries that are accessible and configurable, as in the case of interpreted languages. Software libraries also include privileged programs which execute with escalated privileges. Only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system commands directories are group-owned by root: /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin Run the check with the following command: # sudo find -L /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin ! -group root -type d -exec stat -c "%n %G" '{}' \; If any system commands directories are returned that are not Set Group ID up on execution (SGID) files and owned by a privileged account, this is a finding.

## Group: SRG-OS-000266-GPOS-00101

**Group ID:** `V-219210`

### Rule: The Ubuntu operating system must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-219210r991561_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity or strength is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor in determining how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Special characters are those characters that are not alphanumeric. Examples include: ~ ! @ # $ % ^ *.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the field "ocredit" is set in the "/etc/security/pwquality.conf" file with the following command: # grep -i "ocredit" /etc/security/pwquality.conf ocredit=-1 If the "ocredit" parameter is greater than "-1", or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-219211`

### Rule: The Ubuntu Operating system must disable the x86 Ctrl-Alt-Delete key sequence if a graphical user interface is installed.

**Rule ID:** `SV-219211r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A locally logged-on user who presses Ctrl-Alt-Delete, when at the console, can reboot the system. If accidentally pressed, as could happen in the case of a mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot. In the graphical environment, risk of unintentional reboot from the Ctrl-Alt-Delete sequence is reduced because the user will be prompted before any action is taken.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system is not configured to reboot the system when Ctrl-Alt-Delete is pressed when using a graphical user interface. Check that the "logout" target is not bound to an action with the following command: # grep logout /etc/dconf/db/local.d/* logout='' If the "logout" key is bound to an action, is commented out, or is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-219212`

### Rule: The Ubuntu Operating system must disable the x86 Ctrl-Alt-Delete key sequence.

**Rule ID:** `SV-219212r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A locally logged-on user who presses Ctrl-Alt-Delete, when at the console, can reboot the system. If accidentally pressed, as could happen in the case of a mixed OS environment, this can create the risk of short-term loss of availability of systems due to unintentional reboot.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system is not configured to reboot the system when Ctrl-Alt-Delete is pressed. Check that the "ctrl-alt-del.target" (otherwise also known as reboot.target) is not active with the following command: $ sudo systemctl status ctrl-alt-del.target ctrl-alt-del.target Loaded: masked (/dev/null; bad) Active: inactive (dead) If the "ctrl-alt-del.target" is not masked, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219213`

### Rule: The Ubuntu operating system must generate audit records for the use and modification of the tallylog file.

**Rule ID:** `SV-219213r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000470-GPOS-00214, SRG-OS-000473-GPOS-00218</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record when successful/unsuccessful modifications to the "tallylog" file occur. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep tallylog -w /var/log/tallylog -p wa -k logins If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219214`

### Rule: The Ubuntu operating system must generate audit records for the use and modification of faillog file.

**Rule ID:** `SV-219214r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000470-GPOS-00214, SRG-OS-000473-GPOS-00218</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record when successful/unsuccessful modifications to the "faillog" file occur. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep faillog -w /var/log/faillog -p wa -k logins If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219215`

### Rule: The Ubuntu operating system must generate audit records for the use and modification of the lastlog file.

**Rule ID:** `SV-219215r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000470-GPOS-00214, SRG-OS-000473-GPOS-00218</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record when successful/unsuccessful modifications to the "lastlog" file occur. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep lastlog -w /var/log/lastlog -p wa -k logins If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000471-GPOS-00215

**Group ID:** `V-219216`

### Rule: The Ubuntu operating system must generate audit records for privileged activities or other system-level access.

**Rule ID:** `SV-219216r991579_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system audits privileged activities. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep sudo.log -w /var/log/sudo.log -p wa -k priv_actions If the command does not return lines that match the example or the lines are commented out, this is a finding. Notes: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000472-GPOS-00217

**Group ID:** `V-219217`

### Rule: The Ubuntu operating system must generate audit records for the /var/log/wtmp file.

**Rule ID:** `SV-219217r991581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records showing start and stop times for user access to the system via /va/rlog/wtmp. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep '/var/log/wtmp' -w /var/log/wtmp -p wa -k logins If the command does not return a line matching the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000472-GPOS-00217

**Group ID:** `V-219218`

### Rule: The Ubuntu operating system must generate audit records for the /var/run/utmp file.

**Rule ID:** `SV-219218r991581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records showing start and stop times for user access to the system via /var/run/utmp file. Check the currently configured audit rules with the following command: $ sudo auditctl -l | grep '/var/run/utmp' -w /var/run/utmp -p wa -k logins If the command does not return a line matching the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000472-GPOS-00217

**Group ID:** `V-219219`

### Rule: The Ubuntu operating system must generate audit records for the /var/log/btmp file.

**Rule ID:** `SV-219219r991581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records showing start and stop times for user access to the system via /var/log/btmp file. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep '/var/log/btmp' -w /var/log/btmp -p wa -k logins If the command does not return a line matching the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000476-GPOS-00221

**Group ID:** `V-219220`

### Rule: The Ubuntu operating system must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/passwd.

**Rule ID:** `SV-219220r991585_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000476-GPOS-00221, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207, SRG-OS-000004-GPOS-00004</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records for all account creations, modifications, disabling, and termination events that affect /etc/passwd. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep passwd -w /etc/passwd -p wa -k usergroup_modification If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000476-GPOS-00221

**Group ID:** `V-219221`

### Rule: The Ubuntu operating system must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/group.

**Rule ID:** `SV-219221r991585_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000476-GPOS-00221, SRG-OS-000239-GPOS-00089, SRG-OS-000240-GPOS-00090, SRG-OS-000241-GPOS-00091, SRG-OS-000303-GPOS-00120, SRG-OS-000458-GPOS-00203, SRG-OS-000463-GPOS-00207</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records for all account creations, modifications, disabling, and termination events that affect /etc/group. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep group -w /etc/group -p wa -k usergroup_modification If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000476-GPOS-00221

**Group ID:** `V-219222`

### Rule: The Ubuntu operating system must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/gshadow.

**Rule ID:** `SV-219222r991585_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000476-GPOS-00221, SRG-OS-000463-GPOS-00207, SRG-OS-000458-GPOS-00203, SRG-OS-000303-GPOS-00120, SRG-OS-000241-GPOS-00091, SRG-OS-000240-GPOS-00090, SRG-OS-000239-GPOS-00089</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records for all account creations, modifications, disabling, and termination events that affect /etc/gshadow. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep gshadow -w /etc/gshadow -p wa -k usergroup_modification If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000476-GPOS-00221

**Group ID:** `V-219223`

### Rule: The Ubuntu operating system must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/shadow.

**Rule ID:** `SV-219223r991585_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000476-GPOS-00221, SRG-OS-000463-GPOS-00207, SRG-OS-000458-GPOS-00203, SRG-OS-000303-GPOS-00120, SRG-OS-000241-GPOS-00091, SRG-OS-000240-GPOS-00090, SRG-OS-000239-GPOS-00089</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records for all account creations, modifications, disabling, and termination events that affect /etc/shadow. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep shadow -w /etc/shadow -p wa -k usergroup_modification If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000476-GPOS-00221

**Group ID:** `V-219224`

### Rule: The Ubuntu operating system must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/security/opasswd.

**Rule ID:** `SV-219224r991585_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000476-GPOS-00221, SRG-OS-000463-GPOS-00207, SRG-OS-000458-GPOS-00203, SRG-OS-000303-GPOS-00120, SRG-OS-000241-GPOS-00091, SRG-OS-000240-GPOS-00090, SRG-OS-000239-GPOS-00089</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records for all account creations, modifications, disabling, and termination events that affect /etc/security/opasswd. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep opasswd -w /etc/security/opasswd -p wa -k usergroup_modification If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000038-GPOS-00016

**Group ID:** `V-219225`

### Rule: The Ubuntu operating system must produce audit records and reports containing information to establish when, where, what type, the source, and the outcome for all DoD-defined auditable events and actions in near real time.

**Rule ID:** `SV-219225r958414_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing the when, where, type, source, and outcome of events that occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. Successful incident response and auditing relies on timely, accurate system information and analysis in order to allow the organization to identify and respond to potential incidents in a proficient manner. If the operating system does not provide the ability to centrally review the operating system logs, forensic analysis is negatively impacted. Associating event types with detected events in the Ubuntu operating system audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured operating system. Satisfies: SRG-OS-000038-GPOS-00016, SRG-OS-000039-GPOS-00017, SRG-OS-000040-GPOS-00018, SRG-OS-000041-GPOS-00019, SRG-OS-000042-GPOS-00020, SRG-OS-000042-GPOS-00021, SRG-OS-000051-GPOS-00024, SRG-OS-000054-GPOS-00025, SRG-OS-000062-GPOS-00031, SRG-OS-000122-GPOS-00063, SRG-OS-000337-GPOS-00129, SRG-OS-000348-GPOS-00136, SRG-OS-000349-GPOS-00137, SRG-OS-000350-GPOS-00138, SRG-OS-000351-GPOS-00139, SRG-OS-000352-GPOS-00140, SRG-OS-000365-GPOS-00152, SRG-OS-000392-GPOS-00172, SRG-OS-000475-GPOS-00220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the audit service is configured to produce audit records. Check that the audit service is installed properly with the following command: # dpkg -l | grep auditd If the "auditd" package is not installed, this is a finding. Check that the audit service is enabled with the following command: # systemctl is-enabled auditd.service If the command above returns "disabled", this is a finding. Check that the audit service is properly running and active on the system with the following command: # systemctl is-active auditd.service active If the command above returns "inactive", this is a finding.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-219226`

### Rule: The Ubuntu operating system must alert the ISSO and SA (at a minimum) in the event of an audit processing failure.

**Rule ID:** `SV-219226r958424_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the System Administrator (SA) and Information System Security Officer (ISSO) (at a minimum) are notified in the event of an audit processing failure. Check that the Ubuntu operating system notifies the SA and ISSO (at a minimum) win the event of an audit processing failure with the following command: # sudo grep action_mail_acct = root /etc/audit/auditd.conf action_mail_acct = root If the value of the "action_mail_acct" keyword is not set to "root" and/or other accounts for security personnel, the "action_mail_acct" keyword is missing, or the returned line is commented out, this is a finding.

## Group: SRG-OS-000047-GPOS-00023

**Group ID:** `V-219227`

### Rule: The Ubuntu operating system must shut down by default upon audit failure (unless availability is an overriding concern).

**Rule ID:** `SV-219227r958426_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the Ubuntu operating system is at risk of failing to process audit logs as required, it takes action to mitigate the failure. Audit processing failures include: software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When availability is an overriding concern, other approved actions in response to an audit failure are as follows: 1) If the failure was caused by the lack of audit record storage capacity, the Ubuntu operating system must continue generating audit records if possible (automatically restarting the audit service if necessary), overwriting the oldest audit records in a first-in-first-out manner. 2) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, the Ubuntu operating system must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system takes the appropriate action when the audit storage volume is full. Check that the Ubuntu operating system takes the appropriate action when the audit storage volume is full with the following command: # sudo grep disk_full_action /etc/audit/auditd.conf disk_full_action = HALT If the value of the "disk_full_action" option is not "SYSLOG", "SINGLE", or "HALT", or the line is commented out, this is a finding.

## Group: SRG-OS-000058-GPOS-00028

**Group ID:** `V-219228`

### Rule: The Ubuntu operating system must be configured so that audit log files cannot be read or write-accessible by unauthorized users.

**Rule ID:** `SV-219228r958436_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit information were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit information, the operating system must protect audit information from unauthorized modification. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit information system activity. Satisfies: SRG-OS-000058-GPOS-00028, SRG-OS-000057-GPOS-00027</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the audit log files have a mode of "0600" or less permissive. First determine where the audit logs are stored with the following command: # sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the path of the directory containing the audit logs, check if the audit log files have a mode of "0600" or less by using the following command: # sudo stat -c "%n %a" /var/log/audit/* /var/log/audit/audit.log 600 If the audit log files have a mode more permissive than "0600", this is a finding.

## Group: SRG-OS-000058-GPOS-00028

**Group ID:** `V-219229`

### Rule: The Ubuntu operating system must permit only authorized accounts ownership of the audit log files.

**Rule ID:** `SV-219229r958436_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit information were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit information, the operating system must protect audit information from unauthorized modification. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit information system activity. Satisfies: SRG-OS-000058-GPOS-00028, SRG-OS-000057-GPOS-00027</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the audit log files are owned by "root" account. First determine where the audit logs are stored with the following command: # sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the path of the directory containing the audit logs, check if the audit log files are owned by the "root" user by using the following command: # sudo stat -c "%n %U" /var/log/audit/* /var/log/audit/audit.log root If the audit log files are owned by an user other than "root", this is a finding.

## Group: SRG-OS-000058-GPOS-00028

**Group ID:** `V-219230`

### Rule: The Ubuntu operating system must permit only authorized groups to own the audit log files.

**Rule ID:** `SV-219230r958436_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit information were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit information, the operating system must protect audit information from unauthorized modification. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit information system activity. Satisfies: SRG-OS-000058-GPOS-00028, SRG-OS-000057-GPOS-00027</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the audit log files are owned by "root" group. First determine where the audit logs are stored with the following command: # sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the path of the directory containing the audit logs, check if the audit log files are owned by the "root" group by using the following command: # sudo stat -c "%n %G" /var/log/audit/* /var/log/audit/audit.log root If the audit log files are owned by a group other than "root", this is a finding.

## Group: SRG-OS-000059-GPOS-00029

**Group ID:** `V-219231`

### Rule: The Ubuntu operating system must be configured so that the audit log directory is not write-accessible by unauthorized users.

**Rule ID:** `SV-219231r958438_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit information were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit information, the operating system must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit information system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the audit log directory has a mode of "0750" or less permissive. First determine where the audit logs are stored with the following command: # sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the path of the directory containing the audit logs, check if the directory has a mode of "0750" or less by using the following command: # sudo stat -c "%n %a" /var/log/audit /var/log/audit 750 If the audit log directory has a mode more permissive than "0750", this is a finding.

## Group: SRG-OS-000059-GPOS-00029

**Group ID:** `V-219232`

### Rule: The Ubuntu operating system must allow only authorized accounts to own the audit log directory.

**Rule ID:** `SV-219232r958438_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit information were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit information, the operating system must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit information system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the audit log directory is owned by "root" account. First determine where the audit logs are stored with the following command: # sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the path of the directory containing the audit logs, check if the directory is owned by the "root" user by using the following command: # sudo stat -c "%n %U" /var/log/audit /var/log/audit root If the audit log directory is owned by an user other than "root", this is a finding.

## Group: SRG-OS-000059-GPOS-00029

**Group ID:** `V-219233`

### Rule: The Ubuntu operating system must ensure only authorized groups can own the audit log directory and its underlying files.

**Rule ID:** `SV-219233r958438_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit information were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit information, the operating system must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Audit information includes all information (e.g., audit records, audit settings, audit reports) needed to successfully audit information system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the audit log directory is owned by "root" group. First determine where the audit logs are stored with the following command: # sudo grep -iw log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Using the path of the directory containing the audit logs, check if the directory is owned by the "root" group by using the following command: # sudo stat -c "%n %G" /var/log/audit /var/log/audit root If the audit log directory is owned by a group other than "root", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-219234`

### Rule: The Ubuntu operating system must be configured so that audit configuration files are not write-accessible by unauthorized users.

**Rule ID:** `SV-219234r958444_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "/etc/audit/audit.rules", "/etc/audit/rules.d/*" and "/etc/audit/auditd.conf" files have a mode of 0640 or less permissive by using the following command: # sudo ls -al /etc/audit/ /etc/audit/rules.d/ /etc/audit/: drwxr-x--- 3 root root 4096 Nov 25 11:02 . drwxr-xr-x 130 root root 12288 Dec 19 13:42 .. -rw-r----- 1 root root 804 Nov 25 11:01 auditd.conf -rw-r----- 1 root root 9128 Dec 27 09:56 audit.rules -rw-r----- 1 root root 9373 Dec 27 09:56 audit.rules.prev -rw-r----- 1 root root 127 Feb 7 2018 audit-stop.rules drwxr-x--- 2 root root 4096 Dec 27 09:56 rules.d /etc/audit/rules.d/: drwxr-x--- 2 root root 4096 Dec 27 09:56 . drwxr-x--- 3 root root 4096 Nov 25 11:02 .. -rw-r----- 1 root root 10357 Dec 27 09:56 stig.rules If "/etc/audit/audit.rule","/etc/audit/rules.d/*" or "/etc/audit/auditd.conf" file have a mode more permissive than "0640", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-219235`

### Rule: The Ubuntu operating system must permit only authorized accounts to own the audit configuration files.

**Rule ID:** `SV-219235r958444_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "/etc/audit/audit.rules", "/etc/audit/rules.d/*" and "/etc/audit/auditd.conf" files are owned by root account by using the following command: # sudo ls -al /etc/audit/ /etc/audit/rules.d/ /etc/audit/: drwxr-x--- 3 root root 4096 Nov 25 11:02 . drwxr-xr-x 130 root root 12288 Dec 19 13:42 .. -rw-r----- 1 root root 804 Nov 25 11:01 auditd.conf -rw-r----- 1 root root 9128 Dec 27 09:56 audit.rules -rw-r----- 1 root root 9373 Dec 27 09:56 audit.rules.prev -rw-r----- 1 root root 127 Feb 7 2018 audit-stop.rules drwxr-x--- 2 root root 4096 Dec 27 09:56 rules.d /etc/audit/rules.d/: drwxr-x--- 2 root root 4096 Dec 27 09:56 . drwxr-x--- 3 root root 4096 Nov 25 11:02 .. -rw-r----- 1 root root 10357 Dec 27 09:56 stig.rules If "/etc/audit/audit.rules" or "/etc/audit/rules.d/*" or "/etc/audit/auditd.conf" file is owned by a user other than "root", this is a finding.

## Group: SRG-OS-000063-GPOS-00032

**Group ID:** `V-219236`

### Rule: The Ubuntu operating system must permit only authorized groups to own the audit configuration files.

**Rule ID:** `SV-219236r958444_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that "/etc/audit/audit.rules", "/etc/audit/rules.d/*" and "/etc/audit/auditd.conf" files are owned by root group by using the following command: # sudo ls -al /etc/audit/ /etc/audit/rules.d/ /etc/audit/: drwxr-x--- 3 root root 4096 Nov 25 11:02 . drwxr-xr-x 130 root root 12288 Dec 19 13:42 .. -rw-r----- 1 root root 804 Nov 25 11:01 auditd.conf -rw-r----- 1 root root 9128 Dec 27 09:56 audit.rules -rw-r----- 1 root root 9373 Dec 27 09:56 audit.rules.prev -rw-r----- 1 root root 127 Feb 7 2018 audit-stop.rules drwxr-x--- 2 root root 4096 Dec 27 09:56 rules.d /etc/audit/rules.d/: drwxr-x--- 2 root root 4096 Dec 27 09:56 . drwxr-x--- 3 root root 4096 Nov 25 11:02 .. -rw-r----- 1 root root 10357 Dec 27 09:56 stig.rules If "/etc/audit/audit.rules" or "/etc/audit/rules.d/*" or "/etc/audit/auditd.conf" file is owned by a group other than "root", this is a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-219237`

### Rule: The Ubuntu operating system must allocate audit record storage capacity to store at least one weeks worth of audit records, when audit records are not immediately sent to a central audit record storage facility.

**Rule ID:** `SV-219237r958752_rule`
**Severity:** low

**Description:**
<VulnDiscussion>In order to ensure Ubuntu operating systems have sufficient storage capacity in which to write the audit logs, Ubuntu operating system needs to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial installation of the Ubuntu operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system allocates audit record storage capacity to store at least one week's worth of audit records when audit records are not immediately sent to a central audit record storage facility. Determine which partition the audit records are being written to with the following command: # sudo grep log_file /etc/audit/auditd.conf log_file = /var/log/audit/audit.log Check the size of the partition that audit records are written to (with the example being /var/log/audit/) with the following command: # df –h /var/log/audit/ /dev/sda2 24G 10.4G 13.6G 43% /var/log/audit If the audit records are not written to a partition made specifically for audit records (/var/log/audit is a separate partition), determine the amount of space being used by other files in the partition with the following command: #du –sh [audit_partition] 1.8G /var/log/audit Note: The partition size needed to capture a week's worth of audit records is based on the activity level of the system and the total storage capacity available. In normal circumstances, 10.0 GB of storage space for audit records will be sufficient. If the audit record partition is not allocated for sufficient storage capacity, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219238`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the su command.

**Rule ID:** `SV-219238r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if the Ubuntu operating system generates audit records when successful/unsuccessful attempts to use the "su" command occur. Check the configured audit rules with the following commands: # sudo auditctl -l | grep '/bin/su' -a always,exit -F path=/bin/su -F perm=x -F auid>=1000 -F auid!=-1 -k privileged-priv_change If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219239`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the chfn command.

**Rule ID:** `SV-219239r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if the Ubuntu operating system generates audit records when successful/unsuccessful attempts to use of the "chfn" command occur. Check the configured audit rules with the following commands: # sudo auditctl -l | grep '/usr/bin/chfn' -a always,exit -F path=/usr/bin/chfn -F perm=x -F auid>=1000 -F auid!=-1 -k privileged-chfn If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219240`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the mount command.

**Rule ID:** `SV-219240r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if the Ubuntu operating system generates audit records when successful/unsuccessful attempts to use of the "mount" command occur. Check the configured audit rules with the following commands: # sudo auditctl -l | grep '/bin/mount' -a always,exit -F path=/bin/mount -F perm=x -F auid>=1000 -F auid!=-1 -k privileged-mount If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219241`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the umount command.

**Rule ID:** `SV-219241r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if the Ubuntu operating system generates audit records when successful/unsuccessful attempts to use of the "umount" command occur. Check the configured audit rules with the following commands: # sudo auditctl -l | grep '/bin/umount' -a always,exit -F path=/bin/umount -F perm=x -F auid>=1000 -F auid!=-1 -k privileged-umount If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219242`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the ssh-agent command.

**Rule ID:** `SV-219242r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record when successful/unsuccessful attempts to use the "ssh-agent" command occur. Check the configured audit rules with the following commands: # sudo auditctl -l | grep '/usr/bin/ssh-agent' -a always,exit -F path=/usr/bin/ssh-agent -F perm=x -F auid>=1000 -F auid!=-1 -k privileged-ssh If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219243`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the ssh-keysign command.

**Rule ID:** `SV-219243r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record when successful/unsuccessful attempts to use the "ssh-keysign" command occur. Check the configured audit rules with the following commands: #sudo auditctl -l | grep ssh-keysign -a always,exit -F path=/usr/lib/openssh/ssh-keysign -F perm=x -F auid>=1000 -F auid!=-1 -k privileged-ssh If the command does not return lines that match the example or the lines are commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219244`

### Rule: The Ubuntu operating system must generate audit records for any usage of the setxattr, fsetxattr, lsetxattr, removexattr, fremovexattr, and lremovexattr system calls.

**Rule ID:** `SV-219244r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, however, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000462-GPOS-00206</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record upon successful/unsuccessful attempts to use the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr" system calls. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep xattr -a always,exit -F arch=b32 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=-1 -k perm_mod -a always,exit -F arch=b32 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid=0 -k perm_mod -a always,exit -F arch=b64 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid>=1000 -F auid!=-1 -k perm_mod -a always,exit -F arch=b64 -S setxattr,fsetxattr,lsetxattr,removexattr,fremovexattr,lremovexattr -F auid=0 -k perm_mod If the command does not return audit rules for the "setxattr", "fsetxattr", "lsetxattr", "removexattr", "fremovexattr", and "lremovexattr" syscalls or the lines are commented out, this is a finding. Notes: For 32-bit architectures, only the 32-bit specific output lines from the commands are required. The "-k" allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219250`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the chown, fchown, fchownat, and lchown system calls.

**Rule ID:** `SV-219250r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, however, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record upon successful/unsuccessful attempts to use the "chown", "fchown", "fchownat", and "lchown" system calls. Check the configured audit rules with the following commands: # sudo auditctl -l | grep chown -a always,exit -F arch=b32 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=-1 -k perm_chng -a always,exit -F arch=b64 -S chown,fchown,fchownat,lchown -F auid>=1000 -F auid!=-1 -k perm_chng If the command does not return audit rules for the "chown", "fchown", "fchownat", and "lchown" syscalls or the lines are commented out, this is a finding. Notes: For 32-bit architectures, only the 32-bit specific output lines from the commands are required. The "-k" allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219254`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the chmod, fchmod, and fchmodat system calls.

**Rule ID:** `SV-219254r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, however, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000462-GPOS-00206</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record upon successful/unsuccessful attempts to use the "chmod", "fchmod", and "fchmodat" system calls. Check the configured audit rules with the following commands: # sudo auditctl -l | grep chmod -a always,exit -F arch=b32 -S chmod,fchmod,fchmodat -F auid>=1000 -F auid!=-1 -k perm_chng -a always,exit -F arch=b64 -S chmod,fchmod,fchmodat -F auid>=1000 -F auid!=-1 -k perm_chng If the command does not return audit rules for the "chmod", "fchmod", and "fchmodat" syscalls or the lines are commented out, this is a finding. Notes: For 32-bit architectures, only the 32-bit specific output lines from the commands are required. The "-k" allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219257`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the creat, open, openat, open_by_handle_at, truncate, and ftruncate system calls.

**Rule ID:** `SV-219257r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, however, by combining syscalls into one rule whenever possible. Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000474-GPOS-00219</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record upon unsuccessful attempts to use the "creat", "open", "openat", "open_by_handle_at", "truncate", and "ftruncate" system calls. Check the configured audit rules with the following commands: # sudo auditctl -l | grep 'open\|truncate\|creat' -a always,exit -F arch=b32 -S creat,open,openat,open_by_handle_at,truncate,ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=-1 -k perm_access -a always,exit -F arch=b32 -S creat,open,openat,open_by_handle_at,truncate,ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=-1 -k perm_access -a always,exit -F arch=b64 -S creat,open,openat,open_by_handle_at,truncate,ftruncate -F exit=-EPERM -F auid>=1000 -F auid!=-1 -k perm_access -a always,exit -F arch=b64 -S creat,open,openat,open_by_handle_at,truncate,ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=-1 -k perm_access If the command does not return audit rules for the "creat", "open", "openat", "open_by_handle_at", "truncate", and "ftruncate" syscalls or the lines are commented out, this is a finding. Notes: For 32-bit architectures, only the 32-bit specific output lines from the commands are required. The "-k" allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219263`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the sudo command.

**Rule ID:** `SV-219263r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "sudo" command. Check the configured audit rules with the following command: # sudo auditctl -l | grep /usr/bin/sudo -a always,exit -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -F auid!=-1 -k priv_cmd If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219264`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the sudoedit command.

**Rule ID:** `SV-219264r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record when successful/unsuccessful attempts to use the "sudoedit" command occur. Check the configured audit rules with the following commands: # sudo auditctl -l | grep /usr/bin/sudoedit -a always,exit -F path=/usr/bin/sudoedit -F perm=x -F auid>=1000 -F auid!=-1 -k priv_cmd If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219265`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the chsh command.

**Rule ID:** `SV-219265r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record when successful/unsuccessful attempts to use the "chsh" command. Check the configured audit rules with the following commands: # sudo auditctl -l | grep chsh -a always,exit -F path=/usr/bin/chsh -F perm=x -F auid>=1000 -F auid!=-1 -k priv_cmd If the command does not return a line that matches the example or the line is commented out, this is a finding. Notes: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219266`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the newgrp command.

**Rule ID:** `SV-219266r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record when successful/unsuccessful attempts to use the "newgrp" command occur. Check the configured audit rules with the following commands: # sudo auditctl -l | grep newgrp -a always,exit -F path=/usr/bin/newgrp -F perm=x -F auid>=1000 -F auid!=-1 -k priv_cmd If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219267`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the chcon command.

**Rule ID:** `SV-219267r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record when successful/unsuccessful attempts to use the "chcon" command occur. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep chcon -a always,exit -F path=/usr/bin/chcon -F perm=x -F auid>=1000 -F auid!=-1 -k perm_chng If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219268`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the apparmor_parser command.

**Rule ID:** `SV-219268r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record when successful/unsuccessful attempts to use the "apparmor_parser" command occur. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep apparmor_parser -a always,exit -F path=/sbin/apparmor_parser -F perm=x -F auid>=1000 -F auid!=-1 -k perm_chng If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219269`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the setfacl command.

**Rule ID:** `SV-219269r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record when successful/unsuccessful attempts to use the "setfacl" command occur. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep setfacl -a always,exit -F path=/usr/bin/setfacl -F perm=x -F auid>=1000 -F auid!=-1 -k perm_chng If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219270`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the chacl command.

**Rule ID:** `SV-219270r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates an audit record when successful/unsuccessful attempts to use the "chacl" command occur. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep chacl -a always,exit -F path=/usr/bin/chacl -F perm=x -F auid>=1000 -F auid!=-1 -k perm_chng If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above. If the command does not return a line that matches the example or the line is commented out, this is a finding.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219271`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the passwd command.

**Rule ID:** `SV-219271r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "passwd" command. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep -w passwd -a always,exit -F path=/usr/bin/passwd -F perm=x -F auid>=1000 -F auid!=-1 -k privileged-passwd If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219272`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the unix_update command.

**Rule ID:** `SV-219272r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "unix_update" command. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep -w unix_update -a always,exit -F path=/sbin/unix_update -F perm=x -F auid>=1000 -F auid!=-1 -k privileged-unix-update If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219273`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the gpasswd command.

**Rule ID:** `SV-219273r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "gpasswd" command. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep -w gpasswd -a always,exit -F path=/usr/bin/gpasswd -F perm=x -F auid>=1000 -F auid!=-1 -k privileged-gpasswd If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219274`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the chage command.

**Rule ID:** `SV-219274r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "chage" command. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep -w chage -a always,exit -F path=/usr/bin/chage -F perm=x -F auid>=1000 -F auid!=-1 -k privileged-chage If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219275`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the usermod command.

**Rule ID:** `SV-219275r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "usermod" command. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep -w usermod -a always,exit -F path=/usr/sbin/usermod -F perm=x -F auid>=1000 -F auid!=-1 -k privileged-usermod If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219276`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the crontab command.

**Rule ID:** `SV-219276r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "crontab" command. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep -w crontab -a always,exit -F path=/usr/bin/crontab -F perm=x -F auid>=1000 -F auid!=-1 -k privileged-crontab If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000064-GPOS-00033

**Group ID:** `V-219277`

### Rule: The Ubuntu operating system must generate audit records for successful/unsuccessful uses of the pam_timestamp_check command.

**Rule ID:** `SV-219277r958446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an audit event is generated for any successful/unsuccessful use of the "pam_timestamp_check" command. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep -w pam_timestamp_check -a always,exit -F path=/usr/sbin/pam_timestamp_check -F perm=x -F auid>=1000 -F auid!=-1 -k privileged-pam_timestamp_check If the command does not return a line that matches the example or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000326-GPOS-00126

**Group ID:** `V-219281`

### Rule: The Ubuntu operating system must prevent all software from executing at higher privilege levels than users executing the software and the audit system must be configured to audit the execution of privileged functions.

**Rule ID:** `SV-219281r958730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, software applications/programs need to execute with elevated privileges to perform required functions. However, if the privileges required for execution are at a higher level than the privileges assigned to organizational users invoking such applications/programs, those users are indirectly provided with greater privileges than assigned by the organizations. Some programs and processes are required to operate at a higher privilege level and therefore should be excluded from the organization-defined software list after review. Satisfies: SRG-OS-000326-GPOS-00126, SRG-OS-000327-GPOS-00127</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system audits the execution of privilege functions by auditing the "execve" system call. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep execve -a always,exit -F arch=b64 -S execve -C uid!=euid -F euid=0 -F key=execpriv -a always,exit -F arch=b64 -S execve -C gid!=egid -F egid=0 -F key=execpriv -a always,exit -F arch=b32 -S execve -C uid!=euid -F euid=0 -F key=execpriv -a always,exit -F arch=b32 -S execve -C gid!=egid -F egid=0 -F key=execpriv If the command does not return lines that match the example or the lines are commented out, this is a finding. Notes: For 32-bit architectures, only the 32-bit specific output lines from the commands are required. The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000468-GPOS-00212

**Group ID:** `V-219287`

### Rule: The Ubuntu operating system must generate audit records upon successful/unsuccessful use of unlink, unlinkat, rename, renameat, and rmdir system calls.

**Rule ID:** `SV-219287r991577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). The system call rules are loaded into a matching engine that intercepts each syscall made by all programs on the system. Therefore, it is very important to use syscall rules only when absolutely necessary since these affect performance. The more rules, the bigger the performance hit. The performance is helped, however, by combining syscalls into one rule whenever possible.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system generates audit records upon successful/unsuccessful use of "unlink", "unlinkat", "rename", "renameat", and "rmdir" system calls. Check the currently configured audit rules with the following command: # sudo auditctl -l | grep 'unlink\|rename\|rmdir' -a always,exit -F arch=b64 -S unlink,unlinkat,rename,renameat,rmdir -F auid>=1000 -F auid!=-1 -k delete -a always,exit -F arch=b32 -S unlink,unlinkat,rename,renameat,rmdir -F auid>=1000 -F auid!=-1 -k delete If the command does not return audit rules for the "unlink", "unlinkat", "rename", "renameat", and "rmdir" syscalls or the lines are commented out, this is a finding. Notes: For 32-bit architectures, only the 32-bit specific output lines from the commands are required. The "-k" allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-219296`

### Rule: The Ubuntu operating system must generate records for successful/unsuccessful uses of init_module or finit_module syscalls.

**Rule ID:** `SV-219296r991586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000064-GPOS-00033</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if the Ubuntu operating system is configured to audit the "init_module" and "finit_module" syscalls, by running the following command: # sudo auditctl -l | grep -E 'init_module|finit_module' -a always,exit -F arch=b64 -S init_module -S finit_module -F key=modules -a always,exit -F arch=b32 -S init_module -S finit_module -F key=modules If the command does not return lines that match the example or the lines are commented out, this is a finding. Notes: For 32-bit architectures, only the 32-bit specific output lines from the commands are required. The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-219297`

### Rule: The Ubuntu operating system must generate records for successful/unsuccessful uses of delete_module syscall and when unloading dynamic kernel modules.

**Rule ID:** `SV-219297r991586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). Satisfies: SRG-OS-000064-GPOS-00033, SRG-OS-000471-GPOS-00216</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if the Ubuntu operating system is configured to audit the "delete_module" syscall, by running the following command: # sudo auditctl -l | egrep delete_module -a always,exit -F arch=b64 -S delete_module -F key=modules -a always,exit -F arch=b32 -S delete_module -F key=modules If the command does not return lines that match the example or the lines are commented out, this is a finding. Notes: For 32-bit architectures, only the 32-bit specific output lines from the commands are required. The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-219298`

### Rule: The Ubuntu operating system must generate audit records when successful/unsuccessful attempts to use modprobe command.

**Rule ID:** `SV-219298r991586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if the Ubuntu operating system is configured to audit the execution of the module management program "modprobe", by running the following command: sudo auditctl -l | grep "/sbin/modprobe" -w /sbin/modprobe -p x -k modules If the command does not return a line, or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-219299`

### Rule: The Ubuntu operating system must generate audit records when successful/unsuccessful attempts to use the kmod command.

**Rule ID:** `SV-219299r991586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if the Ubuntu operating system is configured to audit the execution of the module management program "kmod". Check the currently configured audit rules with the following command: # sudo auditctl -l | grep kmod -w /bin/kmod -p x -k module If the command does not return a line, or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000477-GPOS-00222

**Group ID:** `V-219300`

### Rule: The Ubuntu operating system must generate audit records when successful/unsuccessful attempts to use the fdisk command.

**Rule ID:** `SV-219300r991586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if the Ubuntu operating system is configured to audit the execution of the partition management program "fdisk". Check the currently configured audit rules with the following command: # sudo auditctl -l | grep fdisk -w /sbin/fdisk -p x -k fdisk If the command does not return a line, or the line is commented out, this is a finding. Note: The '-k' allows for specifying an arbitrary identifier and the string after it does not need to match the example output above.

## Group: SRG-OS-000027-GPOS-00008

**Group ID:** `V-219301`

### Rule: The Ubuntu operating system must limit the number of concurrent sessions to ten for all accounts and/or account types.

**Rule ID:** `SV-219301r958398_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Ubuntu operating system management includes the ability to control the number of users and user sessions that utilize an operating system. Limiting the number of allowed users and sessions per user is helpful in reducing the risks related to DoS attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based on mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system limits the number of concurrent sessions to ten for all accounts and/or account types by running the following command: $ grep maxlogins /etc/security/limits.conf The result must contain the following line: * hard maxlogins 10 If the "maxlogins" item is missing, or the value is not set to 10 or less, or is commented out, this is a finding.

## Group: SRG-OS-000028-GPOS-00009

**Group ID:** `V-219302`

### Rule: The Ubuntu operating system must retain a users session lock until that user reestablishes access using established identification and authentication procedures.

**Rule ID:** `SV-219302r958400_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Rather than be forced to wait for a period of time to expire before the user session can be locked, Ubuntu operating systems need to provide users with the ability to manually invoke a session lock so users may secure their session should the need arise for them to temporarily vacate the immediate physical vicinity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operation system has a graphical user interface session lock enabled. Note: If the Ubuntu operating system does not have a Graphical User Interface installed, this requirement is Not Applicable. Get the ""lock-enabled"" setting to verify if the graphical user interface session has the lock enabled with the following command: # sudo gsettings get org.gnome.desktop.screensaver lock-enabled true If "lock-enabled" is not set to "true", this is a finding.

## Group: SRG-OS-000029-GPOS-00010

**Group ID:** `V-219303`

### Rule: The Ubuntu operating system must initiate a session lock after a 15-minute period of inactivity for all connection types.

**Rule ID:** `SV-219303r958402_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their operating system session prior to vacating the vicinity, the Ubuntu operating system need to be able to identify when a user's session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system initiates a session logout after a 15-minute period of inactivity. Check that the proper auto logout script exists with the following command: # cat /etc/profile.d/autologout.sh TMOUT=900 readonly TMOUT export TMOUT If the file "/etc/profile.d/autologout.sh" does not exist with the contents shown above, the value of "TMOUT" is greater than 900, or the timeout values are commented out, this is a finding.

## Group: SRG-OS-000030-GPOS-00011

**Group ID:** `V-219304`

### Rule: The Ubuntu operating system must be configured for users to directly initiate a session lock for all connection types.

**Rule ID:** `SV-219304r982194_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not want to log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined. Rather than be forced to wait for a period of time to expire before the user session can be locked, the Ubuntu operating system need to provide users with the ability to manually invoke a session lock so users may secure their session should the need arise for them to temporarily vacate the immediate physical vicinity. Satisfies: SRG-OS-000030-GPOS-00011, SRG-OS-000031-GPOS-00012</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system has the 'vlock' package installed, by running the following command: # dpkg -l | grep vlock If "vlock" is not installed, this is a finding.

## Group: SRG-OS-000032-GPOS-00013

**Group ID:** `V-219306`

### Rule: The Ubuntu operating system must monitor remote access methods.

**Rule ID:** `SV-219306r958406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated monitoring capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Automated monitoring of remote access sessions allows organizations to detect cyber attacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, such as Remote Desktop Protocol (RDP), on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system monitors all remote access methods. Check that remote access methods are being logged by running the following command: $ grep -E -r '^(auth,authpriv\.\*|daemon\.\*)' /etc/rsyslog.* /etc/rsyslog.d/50-default.conf:auth,authpriv.* /var/log/auth.log /etc/rsyslog.d/50-default.conf:daemon.* /var/log/messages If "auth.*", "authpriv.*" or "daemon.*" are not configured to be logged in at least one of the config files, this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-219307`

### Rule: The Ubuntu operating system must implement DoD-approved encryption to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-219307r958408_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection (e.g., RDP), thereby providing a degree of confidentiality. The encryption strength of a mechanism is selected based on the security categorization of the information. By specifying a cipher list with the order of ciphers being in a “strongest to weakest” orientation, the system will automatically attempt to use the strongest cipher for securing SSH connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon is configured to only implement DoD-approved encryption. Check the SSH daemon's current configured ciphers by running the following command: # grep -E '^Ciphers ' /etc/ssh/sshd_config Ciphers aes256-ctr,aes192-ctr, aes128-ctr If any ciphers other than "aes256-ctr", "aes192-ctr", or "aes128-ctr" are listed, the order differs from the example above, the "Ciphers" keyword is missing, or the returned line is commented out, this is a finding.

## Group: SRG-OS-000112-GPOS-00057

**Group ID:** `V-219308`

### Rule: The Ubuntu operating system must enforce SSHv2 for network access to all accounts.

**Rule ID:** `SV-219308r958494_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the operating system. Authentication sessions between the authenticator and the operating system validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. A privileged account is any information system account with authorizations of a privileged user. Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., TLS, WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators. Satisfies: SRG-OS-000112-GPOS-00057, SRG-OS-000113-GPOS-00058</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system enforces SSH protocol 2 for network access. Check the protocol versions that SSH allows with the following command: # grep Protocol /etc/ssh/sshd_config Protocol 2 If the returned line allows for use of protocol "1", is commented out, or the line is missing, this is a finding.

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-219309`

### Rule: The Ubuntu operating system must use strong authenticators in establishing nonlocal maintenance and diagnostic sessions.

**Rule ID:** `SV-219309r958510_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. Typically, strong authentication requires authenticators that are resistant to replay attacks and employ multifactor authentication. Strong authenticators include, for example, PKI where certificates are stored on a token protected by a password, passphrase, or biometric.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system is configured to use strong authenticators in the establishment of nonlocal maintenance and diagnostic maintenance. Check that "UsePAM" is set to yes in /etc/ssh/sshd_config: # grep UsePAM /etc/ssh/sshd_config UsePAM yes If "UsePAM" is not set to "yes", this is a finding.

## Group: SRG-OS-000126-GPOS-00066

**Group ID:** `V-219310`

### Rule: The Ubuntu operating system must immediately terminate all network connections associated with SSH traffic after a period of inactivity.

**Rule ID:** `SV-219310r982190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination terminates all processes associated with a user's logical session except those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific Ubuntu operating system functionality where the system owner, data owner, or organization requires additional assurance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all network connections associated with SSH traffic automatically terminate after a period of inactivity. Check that "ClientAliveCountMax" variable is set in "/etc/ssh/sshd_config" file by performing the following command: # sudo grep -i clientalivecountmax /etc/ssh/sshd_config ClientAliveCountMax 1 If "ClientAliveCountMax" is not set, or not set to "1", or is commented out, this is a finding.

## Group: SRG-OS-000163-GPOS-00072

**Group ID:** `V-219311`

### Rule: The Ubuntu operating system must automatically terminate all network connections associated with SSH traffic at the end of the session or after 10 minutes of inactivity.

**Rule ID:** `SV-219311r970703_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination terminates all processes associated with a user's logical session except those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, and de-allocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that the operating system terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. Satisfies: SRG-OS-000279-GPOS-00109</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all network connections associated with SSH traffic are automatically terminated at the end of the session or after 10 minutes of inactivity. Check that the "ClientAliveInterval" variable is set to a value of "600" or less by performing the following command: # sudo grep -i clientalive /etc/ssh/sshd_config ClientAliveInterval 600 If "ClientAliveInterval" does not exist, is not set to a value of "600" or less in "/etc/ssh/sshd_config", or is commented out, this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-219312`

### Rule: The Ubuntu operating system must configure the SSH daemon to only use Message Authentication Codes (MACs) employing FIPS 140-2 approved cryptographic hash algorithms to protect the integrity of nonlocal maintenance and diagnostic communications.

**Rule ID:** `SV-219312r991554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Local maintenance and diagnostic activities are those activities carried out by individuals physically present at the information system or information system component and not communicating across a network connection. Remote access (e.g., RDP) is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. Satisfies: SRG-OS-000250-GPOS-00093, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system configures the SSH daemon to only use Message Authentication Codes (MACs) that employ FIPS 140-2 approved ciphers. Check that the SSH daemon is configured to only use MACs that employ FIPS 140-2 approved ciphers with the following command: # sudo grep -i macs /etc/ssh/sshd_config MACs hmac-sha2-512,hmac-sha2-256 If any ciphers other than "hmac-sha2-512" or "hmac-sha2-256" are listed, the order differs from the example above, or the returned line is commented out, this is a finding.

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-219313`

### Rule: The Ubuntu operating system must use SSH to protect the confidentiality and integrity of transmitted information unless otherwise protected by alternative physical safeguards, such as, at a minimum, a Protected Distribution System (PDS).

**Rule ID:** `SV-219313r958908_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. Alternative physical protection measures include PDS. PDSs are used to transmit unencrypted classified National Security Information (NSI) through an area of lesser classification or control. Since the classified NSI is unencrypted, the PDS must provide adequate electrical, electromagnetic, and physical safeguards to deter exploitation. Satisfies: SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that the ssh package is installed with the following command: # sudo dpkg -l | grep openssh ii openssh-client 1:7.6p1-4ubuntu0.1 amd64 secure shell (SSH) client, for secure access to remote machines ii openssh-server 1:7.6p1-4ubuntu0.1 amd64 secure shell (SSH) server, for secure access from remote machines ii openssh-sftp-server 1:7.6p1-4ubuntu0.1 amd64 secure shell (SSH) sftp server module, for SFTP access from remote machines If the "openssh" server package is not installed, this is a finding. Check that the "sshd.service" is loaded and active with the following command: # sudo systemctl status sshd.service | egrep -i "(active|loaded)" Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled) Active: active (running) since Thu 2019-01-24 22:52:58 UTC; 1 weeks 3 days ago If "sshd.service" is not active or loaded, this is a finding.

## Group: SRG-OS-000480-GPOS-00229

**Group ID:** `V-219314`

### Rule: The Ubuntu operating system must not allow unattended or automatic login via ssh.

**Rule ID:** `SV-219314r991591_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Failure to restrict system access to authenticated users negatively impacts Ubuntu operating system security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that unattended or automatic login via ssh is disabled. Check that unattended or automatic login via ssh is disabled with the following command: # egrep '(Permit(.*?)(Passwords|Environment))' /etc/ssh/sshd_config PermitEmptyPasswords no PermitUserEnvironment no If "PermitEmptyPasswords" or "PermitUserEnvironment" keywords are not set to "no", are missing completely, or they are commented out, this is a finding.

## Group: SRG-OS-000066-GPOS-00034

**Group ID:** `V-219315`

### Rule: The Ubuntu operating system, for PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

**Rule ID:** `SV-219315r958448_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement. Satisfies: SRG-OS-000066-GPOS-00034, SRG-OS-000384-GPOS-00167</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system, for PKI-based authentication, had valid certificates by constructing a certification path to an accepted trust anchor. Check which pkcs11 module is being used via the use_pkcs11_module in /etc/pam_pkcs11/pam_pkcs11.conf and then ensure "ca" is enabled in "cert_policy" with the following command: # sudo grep use_pkcs11_module /etc/pam_pkcs11/pam_pkcs11.conf | awk '/pkcs11_module opensc {/,/}/' /etc/pam_pkcs11/pam_pkcs11.conf | grep cert_policy | grep ca cert_policy = ca,signature,ocsp_on; If "cert_policy" is not set to "ca", or the line is commented out, this is a finding.

## Group: SRG-OS-000068-GPOS-00036

**Group ID:** `V-219316`

### Rule: The Ubuntu operating system must map the authenticated identity to the user or group account for PKI-based authentication.

**Rule ID:** `SV-219316r958452_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without mapping the certificate used to authenticate to the user account, the ability to determine the identity of the individual user or group will not be available for forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system has the "libpam-pkcs11" package installed, by running the following command: # dpkg -l | grep libpam-pkcs11 If "libpam-pkcs11" is not installed, this is a finding. Check if use_mappers is set to pwent in /etc/pam_pkcs11/pam_pkcs11.conf file # grep use_mappers /etc/pam_pkcs11/pam_pkcs11.conf use_mappers = pwent If "use_mappers" is not found, or is not set to "pwent", this is a finding.

## Group: SRG-OS-000105-GPOS-00052

**Group ID:** `V-219317`

### Rule: The Ubuntu operating system must implement smart card logins for multifactor authentication for access to accounts.

**Rule ID:** `SV-219317r958484_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: 1) something a user knows (e.g., password/PIN); 2) something a user has (e.g., cryptographic identification device, token); and 3) something a user is (e.g., biometric). A privileged account is defined as an information system account with authorizations of a privileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the internet). The DOD CAC with DOD-approved PKI is an example of multifactor authentication. Satisfies: SRG-OS-000105-GPOS-00052, SRG-OS-000106-GPOS-00053, SRG-OS-000107-GPOS-00054, SRG-OS-000108-GPOS-00055, SRG-OS-000377-GPOS-00162</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system uses multifactor authentication for local access to accounts. Check that the "pam_pkcs11.so" option is configured in the "/etc/pam.d/common-auth" file with the following command: # grep pam_pkcs11.so /etc/pam.d/common-auth auth [success=2 default=ignore] pam_pkcs11.so If "pam_pkcs11.so" is not set in "/etc/pam.d/common-auth", this is a finding.

## Group: SRG-OS-000375-GPOS-00160

**Group ID:** `V-219318`

### Rule: The Ubuntu operating system must implement multifactor authentication for remote access to privileged accounts in such a way that one of the factors is provided by a device separate from the system gaining access.

**Rule ID:** `SV-219318r982216_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using an authentication device, such as a CAC or token that is separate from the information system, ensures that even if the information system is compromised, that compromise will not affect credentials stored on the authentication device. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification card and the DoD Common Access Card. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., VPN, proxy capability). This does not apply to authentication for the purpose of configuring the device itself (management). Requires further clarification from NIST.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system has the packages required for multifactor authentication installed. Check for the presence of the packages required to support multifactor authentication with the following commands: # dpkg -l | grep libpam-pkcs11 ii libpam-pkcs11 0.6.8-4 amd64 Fully featured PAM module for using PKCS#11 smart cards If the "libpam-pkcs11" package is not installed, this is a finding.

## Group: SRG-OS-000376-GPOS-00161

**Group ID:** `V-219319`

### Rule: The Ubuntu operating system must accept Personal Identity Verification (PIV) credentials.

**Rule ID:** `SV-219319r958816_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. DoD has mandated the use of the CAC to support identity management and personal authentication for systems covered under Homeland Security Presidential Directive (HSPD) 12, as well as making the CAC a primary component of layered protection for national security systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system accepts Personal Identity Verification (PIV) credentials. Check that the "opensc-pcks11" package is installed on the system with the following command: # dpkg -l | grep opensc-pkcs11 ii opensc-pkcs11:amd64 0.15.0-1Ubuntu1 amd64 Smart card utilities with support for PKCS#15 compatible cards If the "opensc-pcks11" package is not installed, this is a finding.

## Group: SRG-OS-000377-GPOS-00162

**Group ID:** `V-219320`

### Rule: The Ubuntu operating system must implement certificate status checking for multifactor authentication.

**Rule ID:** `SV-219320r958818_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. DoD has mandated the use of the CAC to support identity management and personal authentication for systems covered under Homeland Security Presidential Directive (HSPD) 12, as well as making the CAC a primary component of layered protection for national security systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system implements certificate status checking for multifactor authentication. Check that certificate status checking for multifactor authentication is implemented with the following command: # sudo grep use_pkcs11_module /etc/pam_pkcs11/pam_pkcs11.conf | awk '/pkcs11_module opensc {/,/}/' /etc/pam_pkcs11/pam_pkcs11.conf | grep cert_policy | grep ocsp_on cert_policy = ca,signature,ocsp_on; If "cert_policy" is not set to "ocsp_on", or the line is commented out, this is a finding.

## Group: SRG-OS-000403-GPOS-00182

**Group ID:** `V-219321`

### Rule: The Ubuntu operating system must only allow the use of DoD PKI-established certificate authorities for verification of the establishment of protected sessions.

**Rule ID:** `SV-219321r958868_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DoD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DoD-approved CA, trust of this CA has not been established. The DoD will only accept PKI-certificates obtained from a DoD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of SSL/TLS certificates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the directory containing the root certificates for the Ubuntu operating system only contains certificate files for DoD PKI-established certificate authorities by iterating over all files in the '/etc/ssl/certs' directory and checking if, at least one, has the subject matching "DOD ROOT CA". If none is found, this is a finding.

## Group: SRG-OS-000312-GPOS-00122

**Group ID:** `V-219322`

### Rule: Pam_Apparmor must be configured to allow system administrators to pass information to any other Ubuntu operating system administrator or user, change security attributes, and to confine all non-privileged users from executing functions to include disabling, circumventing, or altering implemented security safeguards/countermeasures.

**Rule ID:** `SV-219322r958702_rule`
**Severity:** low

**Description:**
<VulnDiscussion>When discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control. Satisfies: SRG-OS-000312-GPOS-00122, SRG-OS-000312-GPOS-00123, SRG-OS-000312-GPOS-00124, SRG-OS-000324-GPOS-0012</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system is configured to allow system administrators to pass information to any other Ubuntu operating system administrator or user. Check that "Pam_Apparmor" is installed on the system with the following command: # dpkg -l | grep -i apparmor ii libpam-apparmor 2.10.95-0Ubuntu2.6 If the "Pam_Apparmor" package is not installed, this is a finding. Check that the "AppArmor" daemon is running with the following command: # systemctl status apparmor.service | grep -i active If something other than "Active: active" is returned, this is a finding. Note: Pam_Apparmor must have properly configured profiles. All configurations will be based on the actual system setup and organization. See the "Pam_Apparmor" documentation for more information on configuring profiles.

## Group: SRG-OS-000368-GPOS-00154

**Group ID:** `V-219323`

### Rule: The Ubuntu operating system must be configured to use AppArmor.

**Rule ID:** `SV-219323r958804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Control of program execution is a mechanism used to prevent execution of unauthorized programs. Some operating systems may provide a capability that runs counter to the mission or provides users with functionality that exceeds mission requirements. This includes functions and services installed at the operating system level. Some of the programs, installed by default, may be harmful or may not be necessary to support essential organizational operations (e.g., key missions, functions). Removal of executable programs is not always possible; therefore, establishing a method of preventing program execution is critical to maintaining a secure system baseline. Methods for complying with this requirement include restricting execution of programs in certain environments, while preventing execution in other environments; or limiting execution of certain program functionality based on organization-defined criteria (e.g., privileges, subnets, sandboxed environments, or roles).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system prevents program execution in accordance with local policies. Check that apparmor is installed and active by running the following command: # dpkg -l | grep apparmor If the "apparmor" package is not installed, this is a finding. #systemctl is-active apparmor.service active If "active" is not returned, this is a finding. #systemctl is-enabled apparmor.service enabled If "enabled" is not returned, then this is a finding.

## Group: SRG-OS-000370-GPOS-00155

**Group ID:** `V-219324`

### Rule: The Apparmor module must be configured to employ a deny-all, permit-by-exception policy to allow the execution of authorized software programs and limit the ability of non-privileged users to grant other users direct access to the contents of their home directories/folders.

**Rule ID:** `SV-219324r958808_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Control of program execution is a mechanism used to prevent execution of unauthorized programs. Some operating systems may provide a capability that runs counter to the mission or provides users with functionality that exceeds mission requirements. This includes functions and services installed at the operating system level. Some of the programs, installed by default, may be harmful or may not be necessary to support essential organizational operations (e.g., key missions, functions). Removal of executable programs is not always possible; therefore, establishing a method of preventing program execution is critical to maintaining a secure system baseline. Methods for complying with this requirement include restricting execution of programs in certain environments, while preventing execution in other environments; or limiting execution of certain program functionality based on organization-defined criteria (e.g., privileges, subnets, sandboxed environments, or roles).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system is configured to employ a deny-all, permit-by-exception policy to allow the execution of authorized software programs and access to user home directories. Check that "Apparmor" is configured to employ application whitelisting and home directory access control with the following command: # sudo apparmor_status apparmor module is loaded. 17 profiles are loaded. 17 profiles are in enforce mode. /sbin/dhclient /usr/bin/lxc-start ... 0 processes are in complain mode. 0 processes are unconfined but have a profile defined. If the defined profiles do not match the organization's list of authorized software, this is a finding.

## Group: SRG-OS-000104-GPOS-00051

**Group ID:** `V-219325`

### Rule: The Ubuntu operating system must uniquely identify interactive users.

**Rule ID:** `SV-219325r958482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and processes acting on behalf of users) must be uniquely identified and authenticated to all accesses, except for the following: 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. Satisfies: SRG-OS-000104-GPOS-00051, SRG-OS-000121-GPOS-00062</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Ubuntu operating system contains no duplicate User IDs (UIDs) for interactive users. Check that the Ubuntu operating system contains no duplicate UIDs for interactive users with the following command: # awk -F ":" 'list[$3]++{print $1, $3}' /etc/passwd If output is produced, and the accounts listed are interactive user accounts, this is a finding.

## Group: SRG-OS-000118-GPOS-00060

**Group ID:** `V-219326`

### Rule: The Ubuntu operating system must disable account identifiers (individuals, groups, roles, and devices) after 35 days of inactivity.

**Rule ID:** `SV-219326r982189_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. Ubuntu operating systems need to track periods of inactivity and disable application identifiers after 35 days of inactivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the account identifiers (individuals, groups, roles, and devices) are disabled after 35 days of inactivity with the following command: Check the account inactivity value by performing the following command: # sudo grep INACTIVE /etc/default/useradd INACTIVE=35 If "INACTIVE" is not set to a value 0<[VALUE]<=35, or is commented out, this is a finding.

## Group: SRG-OS-000123-GPOS-00064

**Group ID:** `V-219327`

### Rule: The Ubuntu operating system must automatically expire temporary accounts within 72 hours.

**Rule ID:** `SV-219327r958508_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Temporary accounts are privileged or nonprivileged accounts that are established during pressing circumstances, such as new software or hardware configuration or an incident response, where the need for prompt account activation requires bypassing normal account authorization procedures. If any inactive temporary accounts are left enabled on the system and are not either manually removed or automatically expired within 72 hours, the security posture of the system will be degraded and exposed to exploitation by unauthorized users or insider threat actors. Temporary accounts are different from emergency accounts. Emergency accounts, also known as "last resort" or "break glass" accounts, are local logon accounts enabled on the system for emergency use by authorized system administrators to manage a system when standard logon methods are failing or not available. Emergency accounts are not subject to manual removal or scheduled expiration requirements. The automatic expiration of temporary accounts may be extended as needed by the circumstances but it must not be extended indefinitely. A documented permanent account should be established for privileged users who need long-term maintenance accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify temporary accounts have been provisioned with an expiration date of 72 hours. For every existing temporary account, run the following command to obtain its account expiration information: $ sudo chage -l <temporary_account_name> | grep -i "account expires" Verify each of these accounts has an expiration date set within 72 hours. If any temporary accounts have no expiration date set or do not expire within 72 hours, this is a finding.

## Group: SRG-OS-000480-GPOS-00228

**Group ID:** `V-219328`

### Rule: The Ubuntu operating system default filesystem permissions must be defined in such a way that all authenticated users can only read and modify their own files.

**Rule ID:** `SV-219328r991590_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting the most restrictive default permissions ensures that when new accounts are created they do not have unnecessary access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system defines default permissions for all authenticated users in such a way that the user can only read and modify their own files. Check that the Ubuntu operating system defines default permissions for all authenticated users with the following command: # grep -i "umask" /etc/login.defs UMASK 077 If the "UMASK" variable is set to "000", this is a finding with the severity raised to a CAT I. If the value of "UMASK" is not set to "077", "UMASK" is commented out or "UMASK" is missing completely, this is a finding.

## Group: SRG-OS-000002-GPOS-00002

**Group ID:** `V-219329`

### Rule: The Ubuntu operating system must provision temporary user accounts with an expiration time of 72 hours or less.

**Rule ID:** `SV-219329r958364_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If temporary user accounts remain active when no longer needed or for an excessive period, these accounts may be used to gain unauthorized access. To mitigate this risk, automated termination of all temporary accounts must be set upon account creation. Temporary accounts are established as part of normal account activation procedures when there is a need for short-term accounts without the demand for immediacy in account activation. If temporary accounts are used, the Ubuntu operating system must be configured to automatically terminate these types of accounts after a DoD-defined time period of 72 hours. To address access requirements, the Ubuntu operating system may be integrated with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system expires temporary user accounts within 72 hours or less. For every existing temporary account, run the following command to obtain its account expiration information. # sudo chage -l system_account_name | grep expires Password expires : Aug 07, 2019 Account expires : Aug 07, 2019 Verify each of these accounts has an expiration date set within 72 hours of accounts' creation. If any temporary account does not expire within 72 hours of that account's creation, this is a finding.

## Group: SRG-OS-000142-GPOS-00071

**Group ID:** `V-219330`

### Rule: The Ubuntu operating system must be configured to use TCP syncookies.

**Rule ID:** `SV-219330r958528_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Managing excess capacity ensures that sufficient capacity is available to counter flooding attacks. Employing increased capacity and service redundancy may reduce the susceptibility to some DoS attacks. Managing excess capacity may include, for example, establishing selected usage priorities, quotas, or partitioning.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system is configured to use TCP syncookies. Check the value of TCP syncookies with the following command: # sysctl net.ipv4.tcp_syncookies net.ipv4.tcp_syncookies = 1 If the value is not "1", this is a finding. Check the saved value of TCP syncookies with the following command: # sudo grep -i net.ipv4.tcp_syncookies /etc/sysctl.conf /etc/sysctl.d/* | grep -v '#' If no output is returned, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-219331`

### Rule: The Ubuntu operating system must, for networked systems, compare internal information system clocks at least every 24 hours with a server which is synchronized to one of the redundant United States Naval Observatory (USNO) time servers, or a time server designated for the appropriate DoD network (NIPRNet/SIPRNet), and/or the Global Positioning System (GPS).

**Rule ID:** `SV-219331r982208_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system is not networked this requirement is Not Applicable. The system clock must be configured to compare the system clock at least every 24 hours to the authoritative time source. Check the value of "maxpoll" in the "/etc/chrony/chrony.conf" file with the following command: # sudo grep maxpoll /etc/chrony/chrony.conf server tick.usno.navy.mil iburst maxpoll 16 If the "maxpoll" option is set to a number greater than 16 or the line is commented out, this is a finding. Verify that the "chrony.conf" file is configured to an authoritative DoD time source by running the following command: # grep -i server /etc/chrony/chrony.conf server tick.usno.navy.mil iburst maxpoll 16 server tock.usno.navy.mil iburst maxpoll 16 server ntp2.usno.navy.mil iburst maxpoll 16 If the parameter "server" is not set, is not set to an authoritative DoD time source, or is commented out, this is a finding.

## Group: SRG-OS-000356-GPOS-00144

**Group ID:** `V-219332`

### Rule: The Ubuntu operating system must synchronize internal information system clocks to the authoritative time source when the time difference is greater than one second.

**Rule ID:** `SV-219332r982209_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider setting time periods for different types of systems (e.g., financial, legal, or mission-critical systems). Organizations should also consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). This requirement is related to the comparison done every 24 hours in SRG-OS-000355 because a comparison must be done in order to determine the time difference.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system synchronizes internal system clocks to the authoritative time source when the time difference is greater than one second. Check the value of "makestep" by running the following command: # sudo grep makestep /etc/chrony/chrony.conf makestep 1 -1 If the makestep option is commented out or is not set to "1 -1", this is a finding.

## Group: SRG-OS-000359-GPOS-00146

**Group ID:** `V-219333`

### Rule: The Ubuntu operating system must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

**Rule ID:** `SV-219333r958788_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the operating system include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The time zone must be configured to use Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT). To verify run the following command. # sudo timedatectl status | grep -i "time zone" Timezone: UTC (UTC, +0000) If "Timezone" is not set to UTC or GMT, this is a finding.

## Group: SRG-OS-000096-GPOS-00050

**Group ID:** `V-219334`

### Rule: The Ubuntu operating system must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-219334r958480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. The Ubuntu operating system is capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., VPN and IPS); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the Ubuntu operating system must support the organizational requirements, providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system is configured to prohibit or restrict the use of functions, ports, protocols, and/or services as defined in the Ports, Protocols, and Services Management (PPSM) Category Assignments List (CAL) and vulnerability assessments. Check the firewall configuration for any unnecessary or prohibited functions, ports, protocols, and/or services by running the following commands: $ sudo ufw show before-rules $ sudo ufw show user-rules $ sudo ufw show after-rules Ask the system administrator for the site or program PPSM Component Local Services Assessment (CLSA). Verify the services allowed by the firewall match the PPSM CLSA. If there are any additional ports, protocols, or services that are not included in the PPSM CLSA, this is a finding. If there are any ports, protocols, or services that are prohibited by the PPSM CAL, this is a finding.

## Group: SRG-OS-000184-GPOS-00078

**Group ID:** `V-219335`

### Rule: Kernel core dumps must be disabled unless needed.

**Rule ID:** `SV-219335r958550_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Kernel core dumps may contain the full contents of system memory at the time of the crash. Kernel core dumps may consume a considerable amount of disk space and may result in denial of service by exhausting the available space on the target file system partition.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that kernel core dumps are disabled unless needed. Check if "kdump" service is active with the following command: # systemctl is-active kdump.service inactive If the "kdump" service is active, ask the System Administrator if the use of the service is required and documented with the Information System Security Officer (ISSO). If the service is active and is not documented, this is a finding.

## Group: SRG-OS-000278-GPOS-00108

**Group ID:** `V-219336`

### Rule: The Ubuntu operating system must use cryptographic mechanisms to protect the integrity of audit tools.

**Rule ID:** `SV-219336r991567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting the integrity of the tools used for auditing purposes is a critical step toward ensuring the integrity of audit information. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. It is not uncommon for attackers to replace the audit tools or inject code into the existing tools with the purpose of providing the capability to hide or erase system activity from the audit logs. To address this risk, audit tools must be cryptographically signed in order to provide the capability to identify when the audit tools have been modified, manipulated, or replaced. An example is a checksum hash of the file or files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Advanced Intrusion Detection Environment (AIDE) is properly configured to use cryptographic mechanisms to protect the integrity of audit tools. Check the selection lines that aide is configured to add/check with the following command: # egrep '(\/sbin\/(audit|au))' /etc/aide/aide.conf /sbin/auditctl p+i+n+u+g+s+b+acl+xattrs+sha512 /sbin/auditd p+i+n+u+g+s+b+acl+xattrs+sha512 /sbin/ausearch p+i+n+u+g+s+b+acl+xattrs+sha512 /sbin/aureport p+i+n+u+g+s+b+acl+xattrs+sha512 /sbin/autrace p+i+n+u+g+s+b+acl+xattrs+sha512 /sbin/audispd p+i+n+u+g+s+b+acl+xattrs+sha512 /sbin/augenrules p+i+n+u+g+s+b+acl+xattrs+sha512 If any of the seven audit tools does not have an appropriate selection line, this is a finding.

## Group: SRG-OS-000297-GPOS-00115

**Group ID:** `V-219337`

### Rule: The Ubuntu operating system must enable and run the uncomplicated firewall(ufw).

**Rule ID:** `SV-219337r958672_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access services, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and make remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Ubuntu operating system functionality (e.g., RDP) must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets). Satisfies: SRG-OS-000480-GPOS-00232</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Uncomplicated Firewall is enabled on the system by running the following command: # systemctl is-enabled ufw If the above command returns the status as "disabled", this is a finding. Verify the Uncomplicated Firewall is active on the system by running the following command: # sudo systemctl is-active ufw If the above command returns 'inactive' or any kind of error, this is a finding. If the Uncomplicated Firewall is not installed ask the System Administrator if another application firewall is installed. If no application firewall is installed this is a finding.

## Group: SRG-OS-000363-GPOS-00150

**Group ID:** `V-219338`

### Rule: The Ubuntu operating system must notify designated personnel if baseline configurations are changed in an unauthorized manner. The file integrity tool must notify the system administrator when changes to the baseline configuration or anomalies in the operation of any security functions are discovered.

**Rule ID:** `SV-219338r958794_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to the Ubuntu operating system. Changes to Ubuntu operating system configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of the Ubuntu operating system. The Ubuntu operating system's IMO/ISSO and SAs must be notified via email and/or monitoring system trap when there is an unauthorized modification of a configuration item. Satisfies: SRG-OS-000363-GPOS-00150, SRG-OS-000447-GPOS-00201</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Advanced Intrusion Detection Environment (AIDE) notifies the system administrator when anomalies in the operation of any security functions are discovered. Check that AIDE notifies the system administrator when anomalies in the operation of any security functions are discovered with the following command: #sudo grep SILENTREPORTS /etc/default/aide SILENTREPORTS=no If SILENTREPORTS is uncommented and set to yes, this is a finding.

## Group: SRG-OS-000378-GPOS-00163

**Group ID:** `V-219339`

### Rule: The Ubuntu operating system must disable automatic mounting of Universal Serial Bus (USB) mass storage driver.

**Rule ID:** `SV-219339r958820_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Peripherals include, but are not limited to, such devices as flash drives, external storage, and printers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: The "install" and "blacklist" methods are utilized together to fully disable automatic mounting of the USB mass storage driver. Verify the Ubuntu operating system disables the ability to load the USB storage kernel module: $ grep usb-storage /etc/modprobe.d/* | grep "/bin/false" install usb-storage /bin/false If the command does not return any output, or the line is commented out, this is a finding. Verify the operating system disables the ability to use USB mass storage device: $ grep usb-storage /etc/modprobe.d/* | grep -i "blacklist" blacklist usb-storage If the command does not return any output, or the line is commented out, this is a finding.

## Group: SRG-OS-000420-GPOS-00186

**Group ID:** `V-219340`

### Rule: The Ubuntu operating system must configure the uncomplicated firewall to rate-limit impacted network interfaces.

**Rule ID:** `SV-219340r958902_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of the Ubuntu operating system to mitigate the impact of DoS attacks that have occurred or are ongoing on system availability. For each system, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or establishing memory partitions). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an application firewall is configured to rate limit any connection to the system. Check that the Uncomplicated Firewall is configured to rate limit any connection to the system with the following command: $ sudo ufw show user-rules IPV4 (user): Chain ufw-user-input (1 references) pkts bytes target prot opt in out source destination 1 52 ACCEPT tcp -- * * 0.0.0.0/0 0.0.0.0/0 tcp dpt:22 /* 'dapp_OpenSSH' */ 0 0 ACCEPT tcp -- * * 0.0.0.0/0 0.0.0.0/0 tcp dpt:443 Chain ufw-user-forward (1 references) pkts bytes target prot opt in out source destination Chain ufw-user-output (1 references) pkts bytes target prot opt in out source destination Chain ufw-user-limit-accept (0 references) pkts bytes target prot opt in out source destination 0 0 ACCEPT all -- * * 0.0.0.0/0 0.0.0.0/0 Chain ufw-user-limit (0 references) pkts bytes target prot opt in out source destination 0 0 LOG all -- * * 0.0.0.0/0 0.0.0.0/0 limit: avg 3/min burst 5 LOG flags 0 level 4 prefix "[UFW LIMIT BLOCK] " 0 0 REJECT all -- * * 0.0.0.0/0 0.0.0.0/0 reject-with icmp-port-unreachable If any service is not rate limited by the Uncomplicated Firewall, this is a finding.

## Group: SRG-OS-000433-GPOS-00192

**Group ID:** `V-219341`

### Rule: The Ubuntu operating system must implement non-executable data to protect its memory from unauthorized code execution.

**Rule ID:** `SV-219341r958928_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in non-executable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can either be hardware-enforced or software-enforced with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the NX (no-execution) bit flag is set on the system. Check that the no-execution bit flag is set with the following commands: # dmesg | grep -i "execute disable" [ 0.000000] NX (Execute Disable) protection: active If "dmesg" does not show "NX (Execute Disable) protection: active", check the cpuinfo settings with the following command: # grep flags /proc/cpuinfo | grep -w nx | sort -u flags : fpu vme de pse tsc ms nx rdtscp lm constant_tsc If "flags" does not contain the "nx" flag, this is a finding.

## Group: SRG-OS-000433-GPOS-00193

**Group ID:** `V-219342`

### Rule: The Ubuntu operating system must implement address space layout randomization to protect its memory from unauthorized code execution.

**Rule ID:** `SV-219342r958928_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in non-executable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can either be hardware-enforced or software-enforced with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ubuntu operating system implements address space layout randomization (ASLR). Check that ASLR is configured on the system with the following command: # sudo sysctl kernel.randomize_va_space kernel.randomize_va_space = 2 Verify the kernel parameter "randomize_va_space" is set to 2 with the following command: # cat /proc/sys/kernel/randomize_va_space 2 If "kernel.randomize_va_space" is not set to 2, this is a finding. Check the saved value of the kernel.randomize_va_space variable is not different from 2. # sudo egrep -R "^kernel.randomize_va_space=[^2]" /etc/sysctl.conf /etc/sysctl.d If this returns a result, this is a finding.

## Group: SRG-OS-000445-GPOS-00199

**Group ID:** `V-219343`

### Rule: The Ubuntu operating system must use a file integrity tool to verify correct operation of all security functions.

**Rule ID:** `SV-219343r958944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. This requirement applies to the Ubuntu operating system performing security function verification/testing and/or systems and environments that require this functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Advanced Intrusion Detection Environment (AIDE) is installed and verifies the correct operation of all security functions. Check that the AIDE package is installed with the following command: $ sudo dpkg -l | grep aide ii aide 0.16-3ubuntu0.1 amd64 Advanced Intrusion Detection Environment - static binary If AIDE is not installed, ask the System Administrator how file integrity checks are performed on the system. If there is no application installed to perform integrity checks, this is a finding. If AIDE is installed, check if it has been initialized with the following command: $ sudo aide.wrapper --check If the output is "Couldn't open file /var/lib/aide/aide.db for reading", this is a finding.

## Group: SRG-OS-000446-GPOS-00200

**Group ID:** `V-219344`

### Rule: The Ubuntu operating system must be configured so that a file integrity tool verifies the correct operation of security functions every 30 days.

**Rule ID:** `SV-219344r958946_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. Notifications provided by information systems include, for example, electronic alerts to system administrators, messages to local computer consoles, and/or hardware indications, such as lights. This requirement applies to the Ubuntu operating system performing security function verification/testing and/or systems and environments that require this functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Advanced Intrusion Detection Environment (AIDE) performs a verification of the operation of security functions every 30 days. Note: A file integrity tool other than AIDE may be used, but the tool must be executed at least once per week. Check that AIDE is being executed every 30 days or less with the following command: # ls -al /etc/cron.daily/aide -rwxr-xr-x 1 root root 26049 Oct 24 2014 /etc/cron.daily/aide If the "/etc/cron.daily/aide" file does not exist or a cron job is not configured to run at least every 30 days, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-233779`

### Rule: The Ubuntu operating system must be configured so that remote X connections are disabled, unless to fulfill documented and validated mission requirements.

**Rule ID:** `SV-233779r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The security risk of using X11 forwarding is that the client's X11 display server may be exposed to attack when the SSH client requests forwarding. A system administrator may have a stance in which they want to protect clients that may expose themselves to attack by unwittingly requesting X11 forwarding, which can warrant a ''no'' setting. X11 forwarding should be enabled with caution. Users with the ability to bypass file permissions on the remote host (for the user's X11 authorization database) can access the local X11 display through the forwarded connection. An attacker may then be able to perform activities such as keystroke monitoring if the ForwardX11Trusted option is also enabled. If X11 services are not required for the system's intended function, they should be disabled or restricted as appropriate to the system’s needs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that X11Forwarding is disabled with the following command: # grep -i x11forwarding /etc/ssh/sshd_config | grep -v "^#" X11Forwarding no If the "X11Forwarding" keyword is set to "yes" and is not documented with the Information System Security Officer (ISSO) as an operational requirement or is missing, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-233780`

### Rule: The Ubuntu operating system SSH daemon must prevent remote hosts from connecting to the proxy display.

**Rule ID:** `SV-233780r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When X11 forwarding is enabled, there may be additional exposure to the server and client displays if the SSHD proxy display is configured to listen on the wildcard address. By default, SSHD binds the forwarding server to the loopback address and sets the hostname part of the DIPSLAY environment variable to localhost. This prevents remote hosts from connecting to the proxy display.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SSH daemon prevents remote hosts from connecting to the proxy display. Check the SSH X11UseLocalhost setting with the following command: # sudo grep -i x11uselocalhost /etc/ssh/sshd_config X11UseLocalhost yes If the "X11UseLocalhost" keyword is set to "no", is missing, or is commented out, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237768`

### Rule: All local interactive user home directories defined in the /etc/passwd file must exist.

**Rule ID:** `SV-237768r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a local interactive user has a home directory defined that does not exist, the user may be given access to the / directory as the current working directory upon logon. This could create a Denial of Service (DoS) because the user would not be able to access their logon configuration files, and it may give them visibility to system files they normally would not be able to access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the assigned home directory of all local interactive users on the Ubuntu operating system exists. Check the home directory assignment for all local interactive non-privileged users with the following command: $ sudo awk -F: '($3>=1000)&&($7 !~ /nologin/){print $1, $3, $6}' /etc/passwd smithj 1001 /home/smithj Note: This may miss interactive users that have been assigned a privileged User ID (UID). Evidence of interactive use may be obtained from a number of log files containing system logon information. Check that all referenced home directories exist with the following command: $ sudo pwck -r user 'smithj': directory '/home/smithj' does not exist If any home directories referenced in "/etc/passwd" are returned as not defined, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237769`

### Rule: All local interactive user home directories must have mode 0750 or less permissive.

**Rule ID:** `SV-237769r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Excessive permissions on local interactive user home directories may allow unauthorized access to user files by other users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the assigned home directory of all local interactive users has a mode of "0750" or less permissive with the following command: Note: This may miss interactive users that have been assigned a privileged User Identifier (UID). Evidence of interactive use may be obtained from a number of log files containing system logon information. $ sudo ls -ld $(awk -F: '($3>=1000)&&($7 !~ /nologin/){print $6}' /etc/passwd) drwxr-x--- 2 smithj admin 4096 Jun 5 12:41 smithj If home directories referenced in "/etc/passwd" do not have a mode of "0750" or less permissive, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237770`

### Rule: All local interactive user home directories must be group-owned by the home directory owners primary group.

**Rule ID:** `SV-237770r991589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Group Identifier (GID) of a local interactive user’s home directory is not the same as the primary GID of the user, this would allow unauthorized access to the user’s files, and users that share the same group may not be able to access files that they legitimately should.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the assigned home directory of all local interactive users is group-owned by that user’s primary Group Identifier (GID). Check the home directory assignment for all non-privileged users on the system with the following command: Note: This may miss local interactive users that have been assigned a privileged UID. Evidence of interactive use may be obtained from a number of log files containing system logon information. The returned directory "/home/smithj" is used as an example. $ sudo ls -ld $(awk -F: '($3>=1000)&&($7 !~ /nologin/){print $6}' /etc/passwd) drwxr-x--- 2 smithj admin 4096 Jun 5 12:41 smithj Check the user's primary group with the following command: $ sudo grep admin /etc/group admin:x:250:smithj,jonesj,jacksons If the user home directory referenced in "/etc/passwd" is not group-owned by that user’s primary GID, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-251506`

### Rule: The Ubuntu operating system must not have accounts configured with blank or null passwords.

**Rule ID:** `SV-251506r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log on and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the "/etc/shadow" file for blank passwords with the following command: $ sudo awk -F: '!$2 {print $1}' /etc/shadow If the command returns any results, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-251507`

### Rule: The Ubuntu operating system must not allow accounts configured with blank or null passwords.

**Rule ID:** `SV-251507r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If an account has an empty password, anyone could log on and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that null passwords cannot be used, run the following command: $ grep nullok /etc/pam.d/common-password If this produces any output, it may be possible to log on with accounts with empty passwords. If null passwords can be used, this is a finding.

## Group: SRG-OS-000481-GPOS-00481

**Group ID:** `V-252703`

### Rule: The Ubuntu operating system must disable all wireless network adapters.

**Rule ID:** `SV-252703r958358_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of communications with wireless peripherals, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read, altered, or used to compromise the operating system. This requirement applies to wireless peripheral technologies (e.g., wireless mice, keyboards, displays, etc.) used with an operating system. Wireless peripherals (e.g., Wi-Fi/Bluetooth/IR Keyboards, Mice, and Pointing Devices and Near Field Communications [NFC]) present a unique challenge by creating an open, unsecured port on a computer. Wireless peripherals must meet DoD requirements for wireless data transmission and be approved for use by the AO. Even though some wireless peripherals, such as mice and pointing devices, do not ordinarily carry information that need to be protected, modification of communications with these wireless peripherals may be used to compromise the operating system. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of communications with wireless peripherals can be accomplished by physical means (e.g., employing physical barriers to wireless radio frequencies) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. If the wireless peripheral is only passing telemetry data, encryption of the data may not be required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that there are no wireless interfaces configured on the system. Check that the system does not have active wireless interfaces with the following command: Note: This requirement is Not Applicable for systems that do not have physical wireless network radios. # ifconfig -a | more eth0 Link encap:Ethernet HWaddr ff:ff:ff:ff:ff:ff inet addr:192.168.2.100 Bcast:192.168.2.255 Mask:255.255.255.0 ... eth1 IEEE 802.11b ESSID:"tacnet" Mode:Managed Frequency:2.412 GHz Access Point: 00:40:E7:22:45:CD ... lo Link encap:Local Loopback inet addr:127.0.0.1 Mask:255.0.0.0 inet6 addr: ::1/128 Scope:Host ... If a wireless interface is configured and has not been documented and approved by the Information System Security Officer (ISSO), this is a finding.

## Group: SRG-OS-000250-GPOS-00093

**Group ID:** `V-255906`

### Rule: The Ubuntu operating system SSH server must be configured to use only FIPS-validated key exchange algorithms.

**Rule ID:** `SV-255906r991554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections provided by FIPS-validated cryptographic algorithms, information can be viewed and altered by unauthorized users without detection. The system will attempt to use the first algorithm presented by the client that matches the server list. Listing the values "strongest to weakest" is a method to ensure the use of the strongest algorithm available to secure the SSH connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SSH server is configured to use only FIPS-validated key exchange algorithms: $ sudo grep -i kexalgorithms /etc/ssh/sshd_config KexAlgorithms ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256 If "KexAlgorithms" is not configured, is commented out, or does not contain only the algorithms "ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256" in exact order, this is a finding.

## Group: SRG-OS-000138-GPOS-00069

**Group ID:** `V-255907`

### Rule: The Ubuntu operating system must restrict access to the kernel message buffer.

**Rule ID:** `SV-255907r958524_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Restricting access to the kernel message buffer limits access only to root. This prevents attackers from gaining additional system information as a nonprivileged user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system is configured to restrict access to the kernel message buffer with the following commands: $ sudo sysctl kernel.dmesg_restrict kernel.dmesg_restrict = 1 If "kernel.dmesg_restrict" is not set to "1" or is missing, this is a finding. Check that the configuration files are present to enable this kernel parameter: $ sudo grep -r kernel.dmesg_restrict /run/sysctl.d/* /etc/sysctl.d/* /usr/local/lib/sysctl.d/* /usr/lib/sysctl.d/* /lib/sysctl.d/* /etc/sysctl.conf 2> /dev/null /etc/sysctl.conf:kernel.dmesg_restrict = 1 /etc/sysctl.d/99-sysctl.conf:kernel.dmesg_restrict = 1 If "kernel.dmesg_restrict" is not set to "1", is missing or commented out, this is a finding. If conflicting results are returned, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-264388`

### Rule: The Ubuntu operating system must be a vendor supported release.

**Rule ID:** `SV-264388r991589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>An Ubuntu operating system release is considered "supported" if the vendor continues to provide security patches for the product. With an unsupported release, it will not be possible to resolve security issues discovered in the system software.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the version of the Ubuntu operating system is vendor supported. Check the version of the Ubuntu operating system with the following command: # cat /etc/lsb-release DISTRIB_RELEASE=18.04 DISTRIB_CODENAME=bionic DISTRIB_DESCRIPTION="Ubuntu 18.04.1 LTS" Validate that "Extended Security Maintenance" support has been purchased from the vendor. If the operating system does not have a documented "Extended Security Maintenance" agreement in place, this is a finding.

